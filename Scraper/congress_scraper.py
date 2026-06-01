#!/usr/bin/env python3
"""Mirror Congress.gov bill data into a structured local archive."""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import html
import json
import os
import random
import re
import sys
import threading
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Iterable
import requests
from bs4 import BeautifulSoup
from dateutil import parser as date_parser


API_BASE = "https://api.congress.gov/v3"
ROOT_DIR = Path(__file__).resolve().parents[1]
SCRAPER_DIR = Path(__file__).resolve().parent
STATE_PATH = SCRAPER_DIR / "state.json"
LOCK_PATH = SCRAPER_DIR / ".congress_scraper.lock"
REQUEST_TIMEOUT = 45
REQUEST_DELAY_SECONDS = 0.12
RETRY_ATTEMPTS = 6
RETRY_BACKOFF_SECONDS = 8
RETRY_MAX_SLEEP_SECONDS = 180
RETRY_STATUS_CODES = {500, 502, 503, 504, 520, 525}
RATE_LIMIT_STATUS = 429
DEFAULT_LIMIT = 250
DEFAULT_SEEN_LIMIT = 50

HOUSE_TYPES = ("hr", "hjres", "hconres", "hres")
SENATE_TYPES = ("s", "sjres", "sconres", "sres")
ALL_TYPES = HOUSE_TYPES + SENATE_TYPES

OPTIONAL_ENDPOINTS = (
    "actions",
    "summaries",
    "text",
    "titles",
    "subjects",
    "cosponsors",
    "committees",
    "relatedbills",
    "amendments",
)


class CongressApiError(Exception):
    pass


@contextlib.contextmanager
def lock_or_exit() -> Iterable[None]:
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOCK_PATH.open("w", encoding="utf-8") as lock_file:
        try:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Another Congress scraper run is already active; exiting.", file=sys.stderr, flush=True)
            raise SystemExit(0)
        yield


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {"seen_bills": {}, "last_successful_run": None, "last_congress": None}
    with STATE_PATH.open("r", encoding="utf-8") as handle:
        state = json.load(handle)
    state.setdefault("seen_bills", {})
    state.setdefault("last_successful_run", None)
    state.setdefault("last_congress", None)
    return state


def save_state(state: dict[str, Any]) -> None:
    tmp_path = STATE_PATH.with_suffix(".tmp")
    with tmp_path.open("w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2, sort_keys=True)
        handle.write("\n")
    tmp_path.replace(STATE_PATH)


class ApiKeyRing:
    def __init__(self, keys: Iterable[str], start_index: int = 0) -> None:
        self.keys = [key.strip() for key in keys if key.strip()]
        if not self.keys:
            raise CongressApiError("Set CONGRESS_API_KEY, CONGRESS_API_KEYS, or pass --api-key.")
        self.index = start_index % len(self.keys)
        self.lock = threading.Lock()

    def next(self) -> str:
        with self.lock:
            key = self.keys[self.index]
            self.index = (self.index + 1) % len(self.keys)
            return key


def parse_api_keys(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in re.split(r"[,\s]+", value) if part.strip()]


def get_api_keys(args: argparse.Namespace) -> list[str]:
    keys: list[str] = []
    for value in args.api_key or []:
        keys.extend(parse_api_keys(value))
    keys.extend(parse_api_keys(os.environ.get("CONGRESS_API_KEYS")))
    keys.extend(parse_api_keys(os.environ.get("CONGRESS_API_KEY")))
    deduped = list(dict.fromkeys(keys))
    if not deduped:
        raise CongressApiError("Set CONGRESS_API_KEY, CONGRESS_API_KEYS, or pass --api-key.")
    return deduped


def redacted_url(response: requests.Response) -> str:
    return re.sub(r"api_key=[^&]+", "api_key=REDACTED", response.url)


def retry_delay(response: requests.Response, attempt: int) -> float:
    retry_after = response.headers.get("Retry-After")
    if retry_after:
        try:
            return min(float(retry_after), RETRY_MAX_SLEEP_SECONDS)
        except ValueError:
            pass
    delay = RETRY_BACKOFF_SECONDS * (2 ** attempt)
    delay += random.uniform(0, 2.5)
    return min(delay, RETRY_MAX_SLEEP_SECONDS)


def get_with_retries(
    session: requests.Session,
    url: str,
    retry_status_codes: set[int] | None = None,
    **kwargs: Any,
) -> requests.Response:
    retry_codes = RETRY_STATUS_CODES if retry_status_codes is None else retry_status_codes
    response: requests.Response | None = None
    last_error: requests.RequestException | None = None
    for attempt in range(RETRY_ATTEMPTS):
        try:
            response = session.get(url, timeout=REQUEST_TIMEOUT, **kwargs)
        except requests.RequestException as exc:
            last_error = exc
            if attempt == RETRY_ATTEMPTS - 1:
                raise
            delay = min(RETRY_BACKOFF_SECONDS * (2 ** attempt) + random.uniform(0, 2.5), RETRY_MAX_SLEEP_SECONDS)
            print(
                f"Retryable connection error; sleeping {delay:.1f}s before retrying {url}",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)
            continue
        if response.status_code not in retry_codes:
            return response
        if attempt == RETRY_ATTEMPTS - 1:
            return response
        delay = retry_delay(response, attempt)
        print(
            f"Retryable HTTP {response.status_code}; sleeping {delay:.1f}s before retrying {redacted_url(response)}",
            file=sys.stderr,
            flush=True,
        )
        time.sleep(delay)
    assert response is not None
    if last_error:
        raise last_error
    return response


def api_get(session: requests.Session, path_or_url: str, key_ring: ApiKeyRing, params: dict[str, Any] | None = None) -> dict[str, Any]:
    if path_or_url.startswith("http"):
        url = path_or_url
    else:
        url = f"{API_BASE}{path_or_url}"
    base_params = {"format": "json"}
    if params:
        base_params.update(params)
    last_response: requests.Response | None = None
    for attempt in range(RETRY_ATTEMPTS * len(key_ring.keys)):
        request_params = dict(base_params)
        request_params["api_key"] = key_ring.next()
        response = get_with_retries(session, url, params=request_params)
        last_response = response
        if response.status_code == 404:
            return {}
        if response.status_code != RATE_LIMIT_STATUS:
            response.raise_for_status()
            return response.json()
        print(f"API key rate-limited; rotating key for {redacted_url(response)}", file=sys.stderr, flush=True)
        if (attempt + 1) % len(key_ring.keys) == 0:
            delay = retry_delay(response, attempt // len(key_ring.keys))
            print(f"All API keys rate-limited; sleeping {delay:.1f}s", file=sys.stderr, flush=True)
            time.sleep(delay)
    assert last_response is not None
    last_response.raise_for_status()
    return last_response.json()


def merge_paginated_items(target: dict[str, Any], page: dict[str, Any]) -> None:
    for key, value in page.items():
        if key in {"pagination", "request"}:
            continue
        if isinstance(value, list):
            target.setdefault(key, []).extend(value)
        elif key not in target:
            target[key] = value


def api_get_all(session: requests.Session, path: str, key_ring: ApiKeyRing, limit: int = DEFAULT_LIMIT) -> dict[str, Any]:
    offset = 0
    combined: dict[str, Any] = {}
    last_page: dict[str, Any] = {}
    while True:
        page = api_get(session, path, key_ring, {"limit": limit, "offset": offset})
        if not page:
            return combined
        merge_paginated_items(combined, page)
        last_page = page
        pagination = page.get("pagination") or {}
        if not pagination.get("next"):
            break
        page_count = 0
        for value in page.values():
            if isinstance(value, list):
                page_count = max(page_count, len(value))
        if page_count == 0:
            break
        offset += page_count
        time.sleep(REQUEST_DELAY_SECONDS)
    if "pagination" in last_page:
        combined["pagination"] = {"count": last_page["pagination"].get("count")}
    if "request" in last_page:
        combined["request"] = last_page["request"]
    return combined


def current_congress(session: requests.Session, key_ring: ApiKeyRing) -> int:
    data = api_get(session, "/congress/current", key_ring)
    return int(data["congress"]["number"])


def slugify(value: str, max_length: int = 90) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    normalized = normalized.replace("&", " and ")
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", normalized).strip("_")
    if len(normalized) > max_length:
        normalized = normalized[:max_length].rstrip("_")
    return normalized or "Untitled"


def bill_key(congress: int, bill_type: str, number: str) -> str:
    return f"{congress}:{bill_type.lower()}:{number}"


def chamber_folder(bill: dict[str, Any], bill_type: str) -> Path:
    chamber = bill.get("originChamber")
    if chamber == "House" or bill_type.lower() in HOUSE_TYPES:
        return Path("House")
    return Path("Senate")


def introduced_date(bill: dict[str, Any]) -> dt.date:
    raw = bill.get("introducedDate") or bill.get("latestAction", {}).get("actionDate") or bill.get("updateDate")
    if not raw:
        return dt.datetime.now(dt.timezone.utc).date()
    return date_parser.parse(raw).date()


def bill_archive_dir(bill: dict[str, Any]) -> Path:
    congress = int(bill["congress"])
    bill_type = str(bill["type"]).upper()
    number = str(bill["number"])
    date_value = introduced_date(bill)
    title = slugify(str(bill.get("title") or f"{bill_type} {number}"))
    folder_name = f"{bill_type}_{number}_{title}"
    return (
        ROOT_DIR
        / chamber_folder(bill, bill_type.lower())
        / f"{date_value.year:04d}"
        / f"{date_value.month:02d}"
        / folder_name
    )


def archive_files_complete(bill: dict[str, Any]) -> bool:
    archive_dir = bill_archive_dir(bill)
    return (archive_dir / "BILL.md").exists() and (archive_dir / "metadata.md").exists()


def state_entry_from_listing(bill: dict[str, Any], accessed: str | None = None) -> dict[str, Any]:
    congress = int(bill["congress"])
    bill_type = str(bill["type"]).lower()
    number = str(bill["number"])
    update_marker = bill.get("updateDateIncludingText") or bill.get("updateDate")
    return {
        "title": bill.get("title"),
        "congress": congress,
        "type": bill_type.upper(),
        "number": number,
        "origin_chamber": bill.get("originChamber"),
        "update_marker": update_marker,
        "last_accessed": accessed or now_utc(),
        "path": str(bill_archive_dir(bill).relative_to(ROOT_DIR)),
    }


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")


def html_to_markdown(value: str) -> str:
    if not value:
        return ""
    soup = BeautifulSoup(value, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    for tag in soup.find_all(["strong", "b"]):
        tag.string = f"**{tag.get_text(' ', strip=True)}**"
    for tag in soup.find_all(["em", "i"]):
        tag.string = f"*{tag.get_text(' ', strip=True)}*"
    paragraphs = []
    for block in soup.find_all(["p", "pre", "li"]):
        text = html.unescape(block.get_text(" ", strip=True))
        if text:
            prefix = "- " if block.name == "li" else ""
            paragraphs.append(prefix + text)
    if paragraphs:
        return "\n\n".join(paragraphs)
    return html.unescape(soup.get_text(" ", strip=True))


def normalize_full_text(value: str) -> str:
    value = html.unescape(value).replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in value.splitlines()]
    text = "\n".join(lines).strip()
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def extract_full_text(response_text: str, content_type: str, source_url: str) -> str:
    if "xml" in content_type.lower() or source_url.lower().endswith(".xml"):
        soup = BeautifulSoup(response_text, "html.parser")
        return normalize_full_text(soup.get_text("\n"))

    soup = BeautifulSoup(response_text, "html.parser")
    for selector in ["pre", "body", "main"]:
        node = soup.select_one(selector)
        if node:
            return normalize_full_text(node.get_text("\n"))
    return normalize_full_text(soup.get_text("\n"))


def preferred_text_formats(version: dict[str, Any]) -> list[dict[str, Any]]:
    formats = version.get("formats") or []
    selected: list[dict[str, Any]] = []
    for preferred in ("Formatted XML", "United States Legislative Markup", "Formatted Text"):
        for format_item in formats:
            if format_item.get("type") == preferred and format_item.get("url"):
                selected.append(format_item)
    for format_item in formats:
        if format_item.get("url") and format_item.get("type") != "PDF" and format_item not in selected:
            selected.append(format_item)
    return selected


def fetch_full_texts(session: requests.Session, text_data: dict[str, Any]) -> dict[str, Any]:
    full_texts: list[dict[str, Any]] = []
    for version in text_data.get("textVersions") or []:
        format_items = preferred_text_formats(version)
        if not format_items:
            continue
        errors: list[str] = []
        full_text = ""
        error = None
        format_item = format_items[0]
        source_url = format_item["url"]
        for candidate in format_items:
            source_url = candidate["url"]
            try:
                response = get_with_retries(session, source_url)
                response.raise_for_status()
                full_text = extract_full_text(response.text, response.headers.get("content-type", ""), source_url)
                if full_text:
                    format_item = candidate
                    break
                errors.append(f"{source_url}: empty response text")
            except Exception as exc:
                errors.append(f"{source_url}: {exc}")
                time.sleep(REQUEST_DELAY_SECONDS)
        else:
            error = " | ".join(errors)
        full_texts.append(
            {
                "versionType": version.get("type"),
                "versionDate": version.get("date"),
                "sourceFormat": format_item.get("type"),
                "sourceUrl": source_url,
                "fetchError": error,
                "text": full_text,
            }
        )
        time.sleep(REQUEST_DELAY_SECONDS)
    return {"fullTexts": full_texts}


def sponsor_line(bill: dict[str, Any]) -> str:
    sponsors = bill.get("sponsors") or []
    if not sponsors:
        return "None listed"
    return "; ".join(s.get("fullName", "Unknown") for s in sponsors)


def first_list(data: dict[str, Any], *names: str) -> list[dict[str, Any]]:
    for name in names:
        value = data.get(name)
        if isinstance(value, list):
            return value
    return []


def sorted_actions(related_data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    actions = first_list(related_data.get("actions", {}), "actions")
    return sorted(
        actions,
        key=lambda action: (
            action.get("actionDate") or "",
            action.get("actionTime") or "",
            action.get("text") or "",
        ),
    )


def action_lines(related_data: dict[str, dict[str, Any]]) -> list[str]:
    actions = sorted_actions(related_data)
    if not actions:
        return ["- No actions returned by the Congress.gov actions endpoint."]

    lines: list[str] = []
    for action in actions:
        date = action.get("actionDate", "")
        time_value = action.get("actionTime")
        type_value = action.get("type", "")
        text = action.get("text", "")
        prefix_parts = [part for part in [date, time_value] if part]
        prefix = " ".join(prefix_parts)
        label_parts = [part for part in [prefix, type_value] if part]
        label = " - ".join(label_parts)
        lines.append(f"- {label}: {text}" if label else f"- {text}")
        votes = action.get("recordedVotes") or []
        for vote in votes:
            vote_label = (
                f"{vote.get('chamber', 'Recorded vote')} session {vote.get('sessionNumber', '')}, "
                f"roll {vote.get('rollNumber', '')}"
            )
            lines.append(f"  - Recorded vote: {vote_label} ({vote.get('date', '')})")
    return lines


def timeline_lines(detail: dict[str, Any], related_data: dict[str, dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    introduced = detail.get("introducedDate")
    if introduced:
        lines.append(f"- {introduced}: Introduced in {detail.get('originChamber', 'origin chamber')}")
    lines.extend(action_lines(related_data))
    latest = detail.get("latestAction") or {}
    if latest and latest.get("text"):
        latest_line = f"- Latest action: {latest.get('actionDate', '')}: {latest.get('text', '')}"
        if latest_line not in lines:
            lines.append(latest_line)
    return lines or ["- No timeline data returned by Congress.gov."]


def build_bill_markdown(
    bill: dict[str, Any],
    detail: dict[str, Any],
    related_data: dict[str, dict[str, Any]],
    accessed: str,
) -> str:
    congress = detail["congress"]
    bill_type = detail["type"].upper()
    number = detail["number"]
    latest = detail.get("latestAction") or bill.get("latestAction") or {}
    policy_area = (detail.get("policyArea") or {}).get("name") or ""

    lines = [
        f"# {bill_type} {number}: {bill.get('title', '')}",
        "",
        f"- Congress: {congress}",
        f"- Origin chamber: {bill.get('originChamber', '')}",
        f"- Introduced: {detail.get('introducedDate', bill.get('introducedDate', ''))}",
        f"- Latest action: {latest.get('actionDate', '')} - {latest.get('text', '')}",
        f"- Policy area: {policy_area}",
        f"- Sponsor: {sponsor_line(detail)}",
        f"- Congress.gov: {detail.get('legislationUrl', '')}",
        f"- Date accessed: {accessed}",
    ]

    laws = detail.get("laws") or []
    if laws:
        law_values = [f"{law.get('type', '')} {law.get('number', '')}".strip() for law in laws]
        lines.append(f"- Laws: {', '.join(law_values)}")

    summaries = first_list(related_data.get("summaries", {}), "summaries")
    if summaries:
        lines.extend(["", "## Summary", ""])
        lines.append(html_to_markdown(summaries[0].get("text", "")))

    text_versions = first_list(related_data.get("text", {}), "textVersions")
    if text_versions:
        lines.extend(["", "## Text Versions", ""])
        for version in text_versions:
            lines.append(f"### {version.get('type', 'Text Version')}")
            if version.get("date"):
                lines.append(f"- Date: {version['date']}")
            for format_item in version.get("formats", []):
                lines.append(f"- {format_item.get('type', 'Format')}: {format_item.get('url', '')}")
            lines.append("")

    full_texts = first_list(related_data.get("fullTexts", {}), "fullTexts")
    if full_texts:
        lines.extend(["", "## Full Bill Text", ""])
        for full_text in full_texts:
            lines.append(f"### {full_text.get('versionType') or 'Bill Text'}")
            if full_text.get("versionDate"):
                lines.append(f"- Date: {full_text['versionDate']}")
            lines.append(f"- Source: {full_text.get('sourceUrl', '')}")
            if full_text.get("fetchError"):
                lines.extend(["", f"Unable to fetch full text: {full_text['fetchError']}", ""])
                continue
            lines.extend(["", full_text.get("text", ""), ""])

    lines.extend(["", "## Timeline", ""])
    lines.extend(timeline_lines(detail, related_data))

    return "\n".join(lines).rstrip() + "\n"


def vote_summary_lines(votes_data: dict[str, Any]) -> list[str]:
    votes = votes_data.get("votes") or []
    if not votes:
        return ["- Voters: No recorded votes found in bill actions."]

    lines = [f"- Recorded vote count: {len(votes)}"]
    for vote in votes:
        recorded = vote.get("recordedVote") or {}
        chamber = recorded.get("chamber", "Unknown")
        roll = recorded.get("rollNumber", "")
        session = recorded.get("sessionNumber", "")
        date = recorded.get("date", "")
        detail = (
            vote.get("detail", {}).get("houseRollCallVote")
            or vote.get("detail", {}).get("senateRollCallVote")
            or {}
        )
        member_votes = (
            vote.get("members", {}).get("houseRollCallVoteMemberVotes", {}).get("results")
            or vote.get("members", {}).get("senateRollCallVoteMemberVotes", {}).get("results")
            or []
        )
        lines.append(f"- Vote: {chamber} session {session}, roll {roll}, date {date}")
        if detail:
            lines.append(f"  - Result: {detail.get('result') or detail.get('voteResult') or ''}")
            lines.append(f"  - Question: {detail.get('voteQuestion') or detail.get('voteTitle') or ''}")
            lines.append(f"  - Type: {detail.get('voteType', '')}")
        if member_votes:
            lines.append(f"  - Voters: {len(member_votes)} member votes embedded below in `## API Data: votes`")
            for member in member_votes:
                name = member.get("fullName") or f"{member.get('firstName', '')} {member.get('lastName', '')}".strip()
                party_state = f"{member.get('voteParty', '')}-{member.get('voteState', '')}".strip("-")
                lines.append(f"    - {name} [{party_state}]: {member.get('voteCast', '')}")
        else:
            source = recorded.get("url") or recorded.get("sourceDataURL") or ""
            lines.append("  - Voters: Member-level voter data is not available from the Congress.gov API for this recorded vote.")
            if source:
                lines.append(f"  - Vote source: {source}")
    return lines


def build_metadata(
    bill: dict[str, Any],
    detail: dict[str, Any],
    related_data: dict[str, dict[str, Any]],
    accessed: str,
) -> str:
    congress = detail["congress"]
    bill_type = detail["type"].lower()
    number = detail["number"]
    endpoint = f"{API_BASE}/bill/{congress}/{bill_type}/{number}?format=json"
    lines = [
        "# Metadata",
        "",
        f"- API URL: {endpoint}",
        f"- Congress.gov URL: {detail.get('legislationUrl', '')}",
        f"- Title: {detail.get('title', bill.get('title', ''))}",
        f"- Congress: {congress}",
        f"- Bill type: {detail['type'].upper()}",
        f"- Bill number: {number}",
        f"- Origin chamber: {detail.get('originChamber', bill.get('originChamber', ''))}",
        f"- Introduced date: {detail.get('introducedDate', bill.get('introducedDate', ''))}",
        f"- Update date: {detail.get('updateDate', bill.get('updateDate', ''))}",
        f"- Update date including text: {detail.get('updateDateIncludingText', bill.get('updateDateIncludingText', ''))}",
        f"- Date accessed: {accessed}",
        f"- Embedded API data: {', '.join(['bill'] + sorted(related_data.keys()))}",
    ]
    lines.extend(["", "## Timeline", ""])
    lines.extend(timeline_lines(detail, related_data))
    lines.extend(["", "## Actions", ""])
    lines.extend(action_lines(related_data))
    lines.extend(["", "## Voters", ""])
    lines.extend(vote_summary_lines(related_data.get("votes", {})))
    lines.extend(["", "## API Data: bill", "", "```json", json.dumps({"bill": detail}, indent=2, sort_keys=True), "```"])
    for name in sorted(related_data):
        lines.extend(["", f"## API Data: {name}", "", "```json", json.dumps(related_data[name], indent=2, sort_keys=True), "```"])
    return "\n".join(lines) + "\n"


def list_bills(session: requests.Session, key_ring: ApiKeyRing, congress: int, bill_type: str, limit: int, max_pages: int | None):
    offset = 0
    page = 0
    while True:
        page += 1
        data = api_get(
            session,
            f"/bill/{congress}/{bill_type}",
            key_ring,
            {"limit": limit, "offset": offset},
        )
        bills = data.get("bills") or []
        if not bills:
            break
        yield page, bills, data.get("pagination", {})
        if max_pages is not None and page >= max_pages:
            break
        if not data.get("pagination", {}).get("next"):
            break
        offset += len(bills)
        time.sleep(REQUEST_DELAY_SECONDS)


def fetch_related_data(session: requests.Session, key_ring: ApiKeyRing, congress: int, bill_type: str, number: str) -> dict[str, dict[str, Any]]:
    related: dict[str, dict[str, Any]] = {}
    for endpoint in OPTIONAL_ENDPOINTS:
        path = f"/bill/{congress}/{bill_type}/{number}/{endpoint}"
        data = api_get_all(session, path, key_ring)
        if data:
            related[endpoint] = data
        time.sleep(REQUEST_DELAY_SECONDS)
    return related


def fetch_vote_data(session: requests.Session, key_ring: ApiKeyRing, actions_data: dict[str, Any]) -> dict[str, Any]:
    votes: list[dict[str, Any]] = []
    seen: set[tuple[str, int, int, int]] = set()
    for action in actions_data.get("actions") or []:
        for recorded_vote in action.get("recordedVotes") or []:
            chamber = str(recorded_vote.get("chamber") or "")
            congress = int(recorded_vote.get("congress") or 0)
            session_number = int(recorded_vote.get("sessionNumber") or 0)
            roll = int(recorded_vote.get("rollNumber") or 0)
            key = (chamber, congress, session_number, roll)
            if not chamber or not congress or not session_number or not roll or key in seen:
                continue
            seen.add(key)
            vote_record: dict[str, Any] = {"recordedVote": recorded_vote, "action": action}
            if chamber.lower() == "house":
                detail_path = f"/house-vote/{congress}/{session_number}/{roll}"
                members_path = f"/house-vote/{congress}/{session_number}/{roll}/members"
                vote_record["detail"] = api_get(session, detail_path, key_ring)
                time.sleep(REQUEST_DELAY_SECONDS)
                vote_record["members"] = api_get_all(session, members_path, key_ring)
                time.sleep(REQUEST_DELAY_SECONDS)
            else:
                vote_record["memberDataStatus"] = (
                    "Member-level Senate vote data is not exposed by the documented Congress.gov API endpoints."
                )
            votes.append(vote_record)
    return {"votes": votes}


def archive_bill(session: requests.Session, key_ring: ApiKeyRing, bill: dict[str, Any], state: dict[str, Any], force: bool) -> bool:
    congress = int(bill["congress"])
    bill_type = str(bill["type"]).lower()
    number = str(bill["number"])
    key = bill_key(congress, bill_type, number)
    update_marker = bill.get("updateDateIncludingText") or bill.get("updateDate")

    if not force and state["seen_bills"].get(key, {}).get("update_marker") == update_marker:
        return False

    detail_data = api_get(session, f"/bill/{congress}/{bill_type}/{number}", key_ring)
    detail = detail_data.get("bill") or bill
    related = fetch_related_data(session, key_ring, congress, bill_type, number)
    full_texts = fetch_full_texts(session, related.get("text", {}))
    if full_texts.get("fullTexts"):
        related["fullTexts"] = full_texts
    votes = fetch_vote_data(session, key_ring, related.get("actions", {}))
    if votes.get("votes"):
        related["votes"] = votes
    accessed = now_utc()
    archive_dir = bill_archive_dir(detail)
    archive_dir.mkdir(parents=True, exist_ok=True)

    (archive_dir / "BILL.md").write_text(build_bill_markdown(bill, detail, related, accessed), encoding="utf-8")
    (archive_dir / "metadata.md").write_text(build_metadata(bill, detail, related, accessed), encoding="utf-8")

    state["seen_bills"][key] = state_entry_from_listing(detail, accessed)
    return True


def archive_bill_worker(api_keys: list[str], bill: dict[str, Any]) -> dict[str, Any]:
    session = requests.Session()
    session.headers.update({"User-Agent": "CongressMirrorScraper/1.0 (+local archive)"})
    key_ring = ApiKeyRing(api_keys, random.randrange(len(api_keys)))
    worker_state = {"seen_bills": {}}
    archive_bill(session, key_ring, bill, worker_state, force=True)
    congress = int(bill["congress"])
    bill_type = str(bill["type"]).lower()
    number = str(bill["number"])
    key = bill_key(congress, bill_type, number)
    return {"key": key, "state": worker_state["seen_bills"][key], "bill": bill}


def parse_bill_types(value: str) -> tuple[str, ...]:
    if value == "all":
        return ALL_TYPES
    if value == "house":
        return HOUSE_TYPES
    if value == "senate":
        return SENATE_TYPES
    selected = tuple(part.strip().lower() for part in value.split(",") if part.strip())
    invalid = sorted(set(selected) - set(ALL_TYPES))
    if invalid:
        raise CongressApiError(f"Unsupported bill type(s): {', '.join(invalid)}")
    return selected


def parse_bill_identifier(value: str, default_congress: int) -> tuple[int, str, str]:
    parts = [part.strip().lower() for part in value.replace("/", ":").split(":") if part.strip()]
    if len(parts) == 2:
        congress = default_congress
        bill_type, number = parts
    elif len(parts) == 3:
        congress = int(parts[0])
        bill_type, number = parts[1:]
    else:
        raise CongressApiError(f"Unsupported bill identifier: {value}. Use hr:3503 or 119:hr:3503.")
    if bill_type not in ALL_TYPES:
        raise CongressApiError(f"Unsupported bill type in {value}: {bill_type}")
    return congress, bill_type, number


def archive_specific_bills(args: argparse.Namespace, api_keys: list[str], key_ring: ApiKeyRing, session: requests.Session, state: dict[str, Any], congress: int) -> int:
    total_archived = 0
    for bill_id in args.bill:
        bill_congress, bill_type, number = parse_bill_identifier(bill_id, congress)
        listing_data = api_get(session, f"/bill/{bill_congress}/{bill_type}/{number}", key_ring)
        bill = listing_data.get("bill")
        if not bill:
            print(f"ERROR {bill_id}: bill not found", file=sys.stderr, flush=True)
            continue
        try:
            worker_state = {"seen_bills": {}}
            archive_bill(session, key_ring, bill, worker_state, force=True)
        except Exception as exc:
            print(f"ERROR {bill_id}: {exc}", file=sys.stderr, flush=True)
            continue
        key = bill_key(bill_congress, bill_type, number)
        state["seen_bills"][key] = worker_state["seen_bills"][key]
        total_archived += 1
        print(f"Archived: {bill['type'].upper()} {bill['number']} - {bill.get('title', '')}", flush=True)
    state["last_successful_run"] = now_utc()
    save_state(state)
    print(f"Archived {total_archived} requested bill(s).", flush=True)
    return 0


def run(args: argparse.Namespace) -> int:
    api_keys = get_api_keys(args)
    key_ring = ApiKeyRing(api_keys)
    session = requests.Session()
    session.headers.update({"User-Agent": "CongressMirrorScraper/1.0 (+local archive)"})
    state = load_state()
    congress = args.congress or current_congress(session, key_ring)
    state["last_congress"] = congress
    bill_types = parse_bill_types(args.bill_types)

    total_seen = 0
    total_archived = 0
    consecutive_seen = 0
    workers = max(1, args.workers)
    print(f"Using {len(api_keys)} Congress API key(s).", flush=True)
    if args.bill:
        return archive_specific_bills(args, api_keys, key_ring, session, state, congress)

    for bill_type in bill_types:
        print(f"Scanning {congress} {bill_type.upper()} bills", flush=True)
        for page, bills, pagination in list_bills(session, key_ring, congress, bill_type, args.limit, args.max_pages):
            print(f"Page {page}: {len(bills)} bills (total available: {pagination.get('count', 'unknown')})", flush=True)
            futures = []
            for bill in bills:
                total_seen += 1
                key = bill_key(int(bill["congress"]), str(bill["type"]).lower(), str(bill["number"]))
                update_marker = bill.get("updateDateIncludingText") or bill.get("updateDate")
                unchanged = state["seen_bills"].get(key, {}).get("update_marker") == update_marker
                if not args.force and not unchanged and archive_files_complete(bill):
                    state["seen_bills"][key] = state_entry_from_listing(bill)
                    unchanged = True
                if unchanged and not args.force:
                    if args.incremental:
                        consecutive_seen += 1
                        if consecutive_seen >= args.seen_limit:
                            state["last_successful_run"] = now_utc()
                            save_state(state)
                            print(f"Stopping incremental run after {consecutive_seen} unchanged bills.", flush=True)
                            print(f"Archived {total_archived} new/updated bills from {total_seen} listings.", flush=True)
                            return 0
                    continue
                consecutive_seen = 0

                futures.append((key, bill))
                if args.max_items and total_seen >= args.max_items:
                    break

            with ThreadPoolExecutor(max_workers=workers) as executor:
                future_map = {
                    executor.submit(archive_bill_worker, api_keys, bill): (key, bill)
                    for key, bill in futures
                }
                for future in as_completed(future_map):
                    key, bill = future_map[future]
                    try:
                        result = future.result()
                    except Exception as exc:
                        print(f"ERROR {key}: {exc}", file=sys.stderr, flush=True)
                        continue
                    state["seen_bills"][result["key"]] = result["state"]
                    total_archived += 1
                    print(f"Archived: {bill['type'].upper()} {bill['number']} - {bill.get('title', '')}", flush=True)

            save_state(state)
            if args.max_items and total_seen >= args.max_items:
                state["last_successful_run"] = now_utc()
                save_state(state)
                print(f"Stopped after --max-items={args.max_items}.", flush=True)
                print(f"Archived {total_archived} new/updated bills from {total_seen} listings.", flush=True)
                return 0

    state["last_successful_run"] = now_utc()
    save_state(state)
    print(f"Archived {total_archived} new/updated bills from {total_seen} listings.", flush=True)
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mirror Congress.gov bill data.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--backfill", action="store_true", help="Scan all configured bill types for a Congress.")
    mode.add_argument("--incremental", action="store_true", help="Stop after enough unchanged bills are encountered.")
    parser.add_argument("--force", action="store_true", help="Re-fetch and overwrite archived bills.")
    parser.add_argument("--api-key", action="append", default=[], help="Congress.gov API key. Repeat or comma-separate for rotation. Prefer CONGRESS_API_KEYS for cron.")
    parser.add_argument("--congress", type=int, default=None, help="Congress number. Defaults to current Congress.")
    parser.add_argument("--bill-types", default="all", help="all, house, senate, or comma list: hr,hjres,hconres,hres,s,sjres,sconres,sres")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="API page size.")
    parser.add_argument("--max-pages", type=int, default=None, help="Limit pages per bill type.")
    parser.add_argument("--max-items", type=int, default=None, help="Limit total listing items processed.")
    parser.add_argument("--seen-limit", type=int, default=DEFAULT_SEEN_LIMIT, help="Unchanged-bill stop threshold for incremental runs.")
    parser.add_argument("--workers", type=int, default=10, help="Number of bills to fetch concurrently.")
    parser.add_argument("--bill", action="append", default=[], help="Archive a specific bill, e.g. hr:3503 or 119:hr:3503. Repeat as needed.")
    args = parser.parse_args(argv)
    if not args.incremental:
        args.backfill = True
    return args


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    with lock_or_exit():
        return run(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
