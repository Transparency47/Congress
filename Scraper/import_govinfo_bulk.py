#!/usr/bin/env python3
"""Normalize GovInfo bulk bill files into the API-style Congress mirror."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

import requests

from congress_scraper import (
    ROOT_DIR,
    build_bill_markdown,
    build_metadata,
    bill_key,
    save_state,
    load_state,
)


DEFAULT_DOWNLOAD_ROOT = Path.home() / "Downloads"
TYPE_TO_CHAMBER = {
    "hr": "House",
    "hres": "House",
    "hjres": "House",
    "hconres": "House",
    "s": "Senate",
    "sres": "Senate",
    "sjres": "Senate",
    "sconres": "Senate",
}
VERSION_RANK = {
    "ih": 10,
    "is": 10,
    "rh": 20,
    "rs": 20,
    "rfs": 25,
    "rds": 25,
    "pcs": 30,
    "cps": 30,
    "rcs": 30,
    "eh": 40,
    "es": 40,
    "eah": 45,
    "eas": 45,
    "ats": 50,
    "as": 50,
    "enr": 60,
}


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def slugify(value: str, max_length: int = 90) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    normalized = normalized.replace("&", " and ")
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", normalized).strip("_")
    if len(normalized) > max_length:
        normalized = normalized[:max_length].rstrip("_")
    return normalized or "Untitled"


def local_name(node: ET.Element) -> str:
    return node.tag.rsplit("}", 1)[-1]


def node_text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    text = " ".join(part.strip() for part in node.itertext() if part and part.strip())
    return html.unescape(re.sub(r"\s+", " ", text).strip())


def xml_to_data(node: ET.Element) -> Any:
    children = list(node)
    if not children:
        return node_text(node)
    grouped: dict[str, list[Any]] = defaultdict(list)
    for child in children:
        grouped[local_name(child)].append(xml_to_data(child))
    data: dict[str, Any] = {}
    for key, values in grouped.items():
        data[key] = values[0] if len(values) == 1 else values
    if node.attrib:
        data["@attributes"] = dict(node.attrib)
    text = (node.text or "").strip()
    if text and data:
        data["#text"] = html.unescape(text)
    return data


def find_first(root: ET.Element | None, name: str) -> ET.Element | None:
    if root is None:
        return None
    for node in root.iter():
        if local_name(node) == name:
            return node
    return None


def find_direct(node: ET.Element, name: str) -> ET.Element | None:
    for child in node:
        if local_name(child) == name:
            return child
    return None


def as_list(value: Any) -> list[Any]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, dict) and "item" in value:
        return as_list(value["item"])
    return [value]


def child_text(node: ET.Element | None, name: str) -> str:
    return node_text(find_direct(node, name)) if node is not None else ""


def to_int(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def chamber_name(value: str) -> str:
    value = value.strip().lower()
    if value == "house":
        return "House"
    if value == "senate":
        return "Senate"
    return value.title()


SECTION_TAGS = {
    "section": 4,
    "subsection": 5,
    "paragraph": 0,
    "subparagraph": 0,
    "clause": 0,
    "subclause": 0,
    "item": 0,
}
TEXT_TAGS = {"text", "quoted-block", "action", "legis-type", "official-title", "current-chamber"}


def text_blocks(node: ET.Element) -> list[str]:
    blocks: list[str] = []
    node_name = local_name(node)
    if node_name in TEXT_TAGS:
        text = node_text(node)
        return [text] if text else []

    if node_name in SECTION_TAGS:
        enum = node_text(find_direct(node, "enum"))
        header = node_text(find_direct(node, "header"))
        line = " ".join(part for part in (enum, header) if part)
        if line:
            level = SECTION_TAGS[node_name]
            blocks.append(f"{'#' * level} {line}" if level else f"**{line}**")
        for child in node:
            if local_name(child) not in {"enum", "header"}:
                blocks.extend(text_blocks(child))
        return blocks

    for child in node:
        name = local_name(child)
        if name in {"metadata", "toc"}:
            continue
        if name in SECTION_TAGS:
            blocks.extend(text_blocks(child))
            continue
        if name in TEXT_TAGS:
            text = node_text(child)
            if text:
                blocks.append(text)
            continue
        blocks.extend(text_blocks(child))
    if not blocks and node.text and node.text.strip():
        blocks.append(node.text.strip())
    return blocks


def extract_plain_text(root: ET.Element) -> str:
    parts: list[str] = []
    for tag in ("form", "legis-body", "resolution-body", "engrossed-amendment-body"):
        node = find_first(root, tag)
        if node is not None:
            parts.extend(text_blocks(node))
    return re.sub(r"\n{3,}", "\n\n", "\n".join(part for part in parts if part).strip())


def parse_bill_text(path: Path) -> dict[str, Any]:
    match = re.match(r"BILLS-(\d+)([a-z]+)(\d+)([a-z0-9]+)\.xml$", path.name)
    if not match:
        raise ValueError(f"Unexpected GovInfo bill filename: {path.name}")
    congress, bill_type, number, version_code = match.groups()
    root = ET.fromstring(path.read_bytes())
    session_match = re.match(r"BILLS-\d+-(\d+)-", path.parent.name)
    session = session_match.group(1) if session_match else "1"
    dc_title = node_text(find_first(root, "title"))
    date = node_text(find_first(root, "date"))
    official_title = node_text(find_first(root, "official-title"))
    title = official_title or re.sub(r"^\d+\s+[A-Z]+\s+\d+\s+[A-Z0-9]+:\s*", "", dc_title).strip() or dc_title
    stage = root.attrib.get("bill-stage") or version_code.upper()
    source_url = f"https://www.govinfo.gov/bulkdata/BILLS/{congress}/{session}/{bill_type}/{path.name}"
    return {
        "congress": int(congress),
        "billType": bill_type,
        "number": number,
        "versionCode": version_code,
        "session": session,
        "versionType": stage.replace("-", " "),
        "versionDate": date,
        "title": title,
        "sourceUrl": source_url,
        "text": extract_plain_text(root),
    }


def discover_texts(download_root: Path) -> dict[tuple[int, str, str], list[dict[str, Any]]]:
    grouped: dict[tuple[int, str, str], list[dict[str, Any]]] = defaultdict(list)
    for directory in sorted(download_root.glob("BILLS-119-*-*")):
        if directory.is_dir():
            for path in sorted(directory.glob("*.xml")):
                item = parse_bill_text(path)
                grouped[(item["congress"], item["billType"], item["number"])].append(item)
    for versions in grouped.values():
        versions.sort(key=lambda item: (VERSION_RANK.get(item["versionCode"], 0), item["versionCode"]))
    return grouped


def discover_status(download_root: Path) -> dict[tuple[int, str, str], dict[str, Any]]:
    statuses: dict[tuple[int, str, str], dict[str, Any]] = {}
    for directory in sorted(download_root.glob("BILLSTATUS-119-*")):
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.xml")):
            match = re.match(r"BILLSTATUS-(\d+)([a-z]+)(\d+)\.xml$", path.name)
            if not match:
                continue
            congress, bill_type, number = match.groups()
            payload = xml_to_data(ET.fromstring(path.read_bytes()))
            statuses[(int(congress), bill_type, number)] = {
                "sourceUrl": f"https://www.govinfo.gov/bulkdata/BILLSTATUS/{congress}/{bill_type}/{path.name}",
                "payload": payload,
            }
    return statuses


def discover_summaries(download_root: Path) -> dict[tuple[int, str, str], dict[str, Any]]:
    summaries: dict[tuple[int, str, str], dict[str, Any]] = {}
    for directory in sorted(download_root.glob("BILLSUM-119-*")):
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.xml")):
            match = re.match(r"BILLSUM-(\d+)([a-z]+)(\d+)\.xml$", path.name)
            if not match:
                continue
            root = ET.fromstring(path.read_bytes())
            item = find_first(root, "item")
            if item is None:
                continue
            congress = int(item.attrib.get("congress") or match.group(1))
            bill_type = (item.attrib.get("measure-type") or match.group(2)).lower()
            number = item.attrib.get("measure-number") or match.group(3)
            summary_node = find_first(item, "summary")
            summary_text = node_text(find_first(summary_node, "summary-text")) if summary_node is not None else ""
            summaries[(congress, bill_type, str(number))] = {
                "sourceUrl": f"https://www.govinfo.gov/bulkdata/BILLSUM/{congress}/{bill_type}/{path.name}",
                "payload": xml_to_data(root),
                "summary": {
                    "actionDate": node_text(find_first(summary_node, "action-date")) if summary_node is not None else "",
                    "actionDesc": node_text(find_first(summary_node, "action-desc")) if summary_node is not None else "",
                    "text": summary_text,
                    "updateDate": item.attrib.get("update-date", ""),
                    "versionCode": item.attrib.get("measure-id", ""),
                },
                "title": node_text(find_first(item, "title")),
                "introducedDate": item.attrib.get("orig-publish-date", ""),
                "originChamber": chamber_name(item.attrib.get("originChamber") or ""),
            }
    return summaries


def status_bill(status: dict[str, Any] | None) -> dict[str, Any]:
    if not status:
        return {}
    return status.get("payload", {}).get("bill", {})


def normalize_person(value: dict[str, Any]) -> dict[str, Any]:
    return {
        "bioguideId": value.get("bioguideId", ""),
        "fullName": value.get("fullName", ""),
        "firstName": value.get("firstName", ""),
        "lastName": value.get("lastName", ""),
        "party": value.get("party", ""),
        "state": value.get("state", ""),
        "district": value.get("district", ""),
    }


def normalize_action(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {"text": str(value)}
    action = dict(value)
    recorded_votes = []
    raw_votes = action.get("recordedVotes")
    if isinstance(raw_votes, dict) and "recordedVote" in raw_votes:
        raw_votes = raw_votes["recordedVote"]
    for vote in as_list(raw_votes):
        if isinstance(vote, dict):
            recorded_votes.append(vote)
    if recorded_votes:
        action["recordedVotes"] = recorded_votes
    else:
        action.pop("recordedVotes", None)
    return action


def parse_house_vote_xml(root: ET.Element) -> dict[str, Any]:
    metadata = find_first(root, "vote-metadata")
    member_votes = []
    for recorded_vote in root.iter():
        if local_name(recorded_vote) != "recorded-vote":
            continue
        legislator = find_direct(recorded_vote, "legislator")
        vote = find_direct(recorded_vote, "vote")
        if legislator is None and vote is None:
            continue
        member_votes.append(
            {
                "bioguideId": legislator.attrib.get("name-id", "") if legislator is not None else "",
                "firstName": "",
                "lastName": node_text(legislator),
                "fullName": node_text(legislator),
                "voteParty": legislator.attrib.get("party", "") if legislator is not None else "",
                "voteState": legislator.attrib.get("state", "") if legislator is not None else "",
                "voteCast": node_text(vote),
            }
        )
    return {
        "detail": {
            "houseRollCallVote": {
                "result": child_text(metadata, "vote-result"),
                "voteQuestion": child_text(metadata, "vote-question"),
                "voteType": child_text(metadata, "vote-type"),
                "voteDescription": child_text(metadata, "vote-desc"),
                "actionDate": child_text(metadata, "action-date"),
                "actionTime": child_text(metadata, "action-time"),
                "totals": xml_to_data(find_direct(metadata, "vote-totals")) if metadata is not None and find_direct(metadata, "vote-totals") is not None else {},
            }
        },
        "members": {"houseRollCallVoteMemberVotes": {"results": member_votes}},
    }


def parse_senate_name(value: str) -> tuple[str, str, str]:
    match = re.match(r"^(.*?)\s+\(([A-Z])-([A-Z]{2})\)$", value.strip())
    if not match:
        return value.strip(), "", ""
    return match.group(1).strip(), match.group(2), match.group(3)


def parse_senate_vote_xml(root: ET.Element) -> dict[str, Any]:
    member_votes = []
    members = find_first(root, "members")
    for member in list(members) if members is not None else []:
        if local_name(member) != "member":
            continue
        full_label = child_text(member, "member_full")
        name, party, state = parse_senate_name(full_label)
        member_votes.append(
            {
                "bioguideId": child_text(member, "lis_member_id"),
                "firstName": "",
                "lastName": name,
                "fullName": name,
                "voteParty": party,
                "voteState": state,
                "voteCast": child_text(member, "vote_cast"),
            }
        )
    return {
        "detail": {
            "senateRollCallVote": {
                "result": child_text(root, "vote_result_text") or child_text(root, "vote_result"),
                "voteQuestion": child_text(root, "vote_question_text") or child_text(root, "question"),
                "voteType": child_text(root, "question"),
                "voteTitle": child_text(root, "vote_title"),
                "voteDate": child_text(root, "vote_date"),
                "majorityRequirement": child_text(root, "majority_requirement"),
            }
        },
        "members": {"senateRollCallVoteMemberVotes": {"results": member_votes}},
    }


def fetch_vote_xml(session: requests.Session, recorded_vote: dict[str, Any]) -> dict[str, Any]:
    url = recorded_vote.get("url") or recorded_vote.get("sourceDataURL") or ""
    if not url:
        return {"fetchError": "No vote XML URL was present in BILLSTATUS."}
    response = session.get(url, timeout=30)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    parsed = parse_house_vote_xml(root) if local_name(root) == "rollcall-vote" else parse_senate_vote_xml(root)
    parsed["sourceUrl"] = url
    parsed["sourcePayload"] = xml_to_data(root)
    return parsed


def hydrate_votes(actions_data: dict[str, Any]) -> dict[str, Any]:
    votes: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str]] = set()
    session = requests.Session()
    session.headers.update({"User-Agent": "CongressMirrorScraper/1.0 (+local archive)"})
    for action in actions_data.get("actions") or []:
        for recorded_vote in action.get("recordedVotes") or []:
            chamber = str(recorded_vote.get("chamber") or "")
            congress = str(recorded_vote.get("congress") or "")
            session_number = str(recorded_vote.get("sessionNumber") or "")
            roll = str(recorded_vote.get("rollNumber") or "")
            key = (chamber, congress, session_number, roll)
            if not roll or key in seen:
                continue
            seen.add(key)
            vote_record: dict[str, Any] = {"recordedVote": recorded_vote, "action": action}
            try:
                vote_record.update(fetch_vote_xml(session, recorded_vote))
            except Exception as exc:
                vote_record["fetchError"] = str(exc)
            votes.append(vote_record)
    return {"votes": votes} if votes else {}


def normalize_detail(
    key: tuple[int, str, str],
    status: dict[str, Any] | None,
    versions: list[dict[str, Any]],
    summary: dict[str, Any] | None,
) -> dict[str, Any]:
    congress, bill_type, number = key
    bill = status_bill(status)
    latest_action = {}
    actions = [normalize_action(action) for action in as_list(bill.get("actions"))]
    if actions:
        last = actions[-1]
        latest_action = {"actionDate": last.get("actionDate", ""), "text": last.get("text", "")}
    title = bill.get("title") or (summary or {}).get("title") or (versions[-1]["title"] if versions else f"{bill_type.upper()} {number}")
    origin = bill.get("originChamber") or (summary or {}).get("originChamber") or TYPE_TO_CHAMBER.get(bill_type, "")
    introduced = bill.get("introducedDate") or (summary or {}).get("introducedDate") or (versions[0]["versionDate"] if versions else "")
    policy_area = bill.get("policyArea") or {}
    if isinstance(policy_area, str):
        policy_area = {"name": policy_area}
    return {
        "congress": congress,
        "type": bill_type.upper(),
        "number": number,
        "title": title,
        "originChamber": origin,
        "introducedDate": introduced,
        "updateDate": bill.get("updateDate", ""),
        "updateDateIncludingText": bill.get("updateDateIncludingText", ""),
        "legislationUrl": bill.get("legislationUrl", f"https://www.congress.gov/bill/{congress}th-congress/{bill_type}/{number}"),
        "latestAction": latest_action,
        "policyArea": policy_area,
        "sponsors": [normalize_person(person) for person in as_list(bill.get("sponsors"))],
    }


def normalize_related(status: dict[str, Any] | None, versions: list[dict[str, Any]], summary: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    related: dict[str, dict[str, Any]] = {}
    bill = status_bill(status)
    if bill:
        if "actions" in bill:
            related["actions"] = {"actions": [normalize_action(action) for action in as_list(bill.get("actions"))]}
            votes = hydrate_votes(related["actions"])
            if votes:
                related["votes"] = votes
        for name in ("actions", "titles", "subjects", "cosponsors", "committees", "relatedBills", "amendments", "laws"):
            if name == "actions":
                continue
            if name in bill:
                api_name = "relatedbills" if name == "relatedBills" else name.lower()
                plural = "relatedBills" if name == "relatedBills" else name
                related[api_name] = {plural: as_list(bill.get(name))}
    if summary:
        related["summaries"] = {"summaries": [summary["summary"]], "govinfoBulk": summary}
    if versions:
        related["text"] = {
            "textVersions": [
                {
                    "type": item["versionType"],
                    "date": item["versionDate"],
                    "formats": [{"type": "Formatted XML", "url": item["sourceUrl"]}],
                }
                for item in versions
            ]
        }
        related["fullTexts"] = {
            "fullTexts": [
                {
                    "versionType": item["versionType"],
                    "versionDate": item["versionDate"],
                    "sourceFormat": "Formatted XML",
                    "sourceUrl": item["sourceUrl"],
                    "fetchError": None,
                    "text": item["text"],
                }
                for item in versions
            ]
        }
    return related


def existing_dir(chamber: str, bill_type: str, number: str) -> Path | None:
    prefix = f"{bill_type.upper()}_{number}_"
    for path in (ROOT_DIR / chamber).glob(f"20*/*/{prefix}*"):
        if path.is_dir():
            return path
    return None


def archive_dir(detail: dict[str, Any]) -> Path:
    chamber = detail.get("originChamber") or TYPE_TO_CHAMBER[str(detail["type"]).lower()]
    bill_type = str(detail["type"]).lower()
    number = str(detail["number"])
    found = existing_dir(chamber, bill_type, number)
    if found:
        return found
    date = dt.date.fromisoformat(detail.get("introducedDate") or "2025-01-01")
    folder_name = f"{bill_type.upper()}_{number}_{slugify(detail.get('title') or f'{bill_type.upper()} {number}')}"
    return ROOT_DIR / chamber / f"{date.year:04d}" / f"{date.month:02d}" / folder_name


def import_federal_register(download_root: Path) -> dict[str, int]:
    stats = {"federalRegisterDays": 0}
    for path in sorted((download_root / "FR-2025").glob("*/*.xml")):
        match = re.match(r"FR-(\d{4})-(\d{2})-(\d{2})\.xml$", path.name)
        if not match:
            continue
        year, month, day = match.groups()
        root = ET.fromstring(path.read_bytes())
        date_value = node_text(find_first(root, "DATE")) or f"{year}-{month}-{day}"
        text = "\n".join(part.strip() for part in root.itertext() if part and part.strip())
        out_dir = ROOT_DIR / "Federal Register" / year / month / day
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "Federal_Register.md").write_text(
            "\n".join(
                [
                    f"# Federal Register: {date_value}",
                    "",
                    f"- Source: https://www.govinfo.gov/bulkdata/FR/{year}/{month}/{path.name}",
                    f"- Date accessed: {now_utc()}",
                    "",
                    "## Contents",
                    "",
                    "```text",
                    re.sub(r"\n{3,}", "\n\n", text).strip(),
                    "```",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (out_dir / "metadata.md").write_text(
            "\n".join(
                [
                    "# Metadata",
                    "",
                    f"- Source: https://www.govinfo.gov/bulkdata/FR/{year}/{month}/{path.name}",
                    f"- Date published: {date_value}",
                    f"- Date accessed: {now_utc()}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        stats["federalRegisterDays"] += 1
    return stats


def import_bulk(download_root: Path, include_fr: bool = True) -> dict[str, int]:
    texts = discover_texts(download_root)
    statuses = discover_status(download_root)
    summaries = discover_summaries(download_root)
    keys = sorted(set(texts) | set(statuses) | set(summaries))
    state = load_state()
    stats = {"bills": 0, "created": 0, "updated": 0, "withFullText": 0, "withStatus": 0, "withSummary": 0}
    accessed = now_utc()
    for key in keys:
        versions = texts.get(key, [])
        status = statuses.get(key)
        summary = summaries.get(key)
        detail = normalize_detail(key, status, versions, summary)
        related = normalize_related(status, versions, summary)
        out_dir = archive_dir(detail)
        existed = (out_dir / "BILL.md").exists()
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "BILL.md").write_text(build_bill_markdown(detail, detail, related, accessed), encoding="utf-8")
        (out_dir / "metadata.md").write_text(build_metadata(detail, detail, related, accessed), encoding="utf-8")
        marker = detail.get("updateDateIncludingText") or detail.get("updateDate") or accessed
        state["seen_bills"][bill_key(key[0], key[1], key[2])] = {
            "title": detail.get("title", ""),
            "congress": key[0],
            "type": key[1].upper(),
            "number": key[2],
            "origin_chamber": detail.get("originChamber", ""),
            "update_marker": marker,
            "last_accessed": accessed,
            "path": str(out_dir.relative_to(ROOT_DIR)),
        }
        stats["bills"] += 1
        stats["updated" if existed else "created"] += 1
        stats["withFullText"] += int(bool(versions))
        stats["withStatus"] += int(status is not None)
        stats["withSummary"] += int(summary is not None)
    state["last_successful_run"] = accessed
    save_state(state)
    if include_fr:
        stats.update(import_federal_register(download_root))
    return stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import GovInfo bulk data into the API-style Congress mirror.")
    parser.add_argument("--download-root", type=Path, default=DEFAULT_DOWNLOAD_ROOT)
    parser.add_argument("--no-federal-register", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(json.dumps(import_bulk(args.download_root, include_fr=not args.no_federal_register), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
