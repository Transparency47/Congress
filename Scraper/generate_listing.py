#!/usr/bin/env python3
"""Generate listing.json for the Transparency47 Congress archive."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
LISTING_PATH = ROOT_DIR / "listing.json"


def stable_id(source: str, path: str) -> str:
    digest = hashlib.sha1(f"{source}:{path}".encode("utf-8")).hexdigest()[:16]
    return f"{source}:{digest}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def first_heading(markdown: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else None


def metadata_line(markdown: str, label: str) -> str | None:
    pattern = re.compile(rf"^-\s+{re.escape(label)}:\s*(.+?)\s*$", re.MULTILINE | re.IGNORECASE)
    match = pattern.search(markdown)
    return match.group(1).strip() if match else None


def summary_from(markdown: str) -> str | None:
    match = re.search(r"^##\s+Summary\s*$([\s\S]*?)(?:^##\s+|\Z)", markdown, re.MULTILINE)
    if not match:
        return None
    text = re.sub(r"\s+", " ", match.group(1)).strip()
    return text[:280] if text else None


def year_from_path(relative_path: str) -> str | None:
    match = re.search(r"/([0-9]{4})/", relative_path)
    return match.group(1) if match else None


def build_record(path: Path) -> dict:
    relative_path = path.relative_to(ROOT_DIR).as_posix()
    markdown = read_text(path)
    metadata_path = path.parent / "metadata.md"
    metadata = read_text(metadata_path) if metadata_path.exists() else ""
    is_federal_register = relative_path.endswith("Federal_Register.md")
    chamber = relative_path.split("/", 1)[0] if not is_federal_register else None
    title = metadata_line(metadata, "Title") or first_heading(markdown) or path.parent.name.replace("_", " ")
    date = (
        metadata_line(metadata, "Introduced date")
        or metadata_line(markdown, "Introduced")
        or metadata_line(metadata, "Date published")
        or year_from_path(relative_path)
    )
    if date and len(date) > 10:
        date = date[:10]
    bill_type = metadata_line(metadata, "Bill type") or metadata_line(markdown, "Bill type")
    bill_number = metadata_line(metadata, "Bill number") or metadata_line(markdown, "Bill number")
    category = "Federal Register" if is_federal_register else chamber
    return {
        "id": stable_id("congress", relative_path),
        "title": title,
        "path": relative_path,
        "category": category,
        "kind": "federal_register" if is_federal_register else "bill",
        "date": date,
        "sourceUrl": metadata_line(metadata, "Congress.gov URL") or metadata_line(metadata, "Source"),
        "summary": summary_from(markdown),
        "metadata": {
            "chamber": chamber,
            "congress": metadata_line(metadata, "Congress") or metadata_line(markdown, "Congress"),
            "billType": bill_type,
            "billNumber": bill_number,
            "policyArea": metadata_line(markdown, "Policy area"),
            "latestAction": metadata_line(markdown, "Latest action"),
        },
    }


def discover_records() -> list[Path]:
    records = list(ROOT_DIR.glob("House/**/BILL.md"))
    records.extend(ROOT_DIR.glob("Senate/**/BILL.md"))
    records.extend(ROOT_DIR.glob("Joint/**/BILL.md"))
    records.extend(ROOT_DIR.glob("Federal Register/**/Federal_Register.md"))
    return sorted(records, key=lambda p: p.relative_to(ROOT_DIR).as_posix())


def build_listing() -> dict:
    records = [build_record(path) for path in discover_records()]
    records.sort(key=lambda row: (row.get("date") or "", row.get("title") or ""), reverse=True)
    return {
        "version": 1,
        "source": "congress",
        "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
        "records": records,
    }


def write_listing(path: Path = LISTING_PATH) -> None:
    listing = build_listing()
    tmp_path = path.with_suffix(".tmp")
    with tmp_path.open("w", encoding="utf-8") as handle:
        json.dump(listing, handle, indent=2, sort_keys=True)
        handle.write("\n")
    tmp_path.replace(path)
    print(f"Wrote {path.relative_to(ROOT_DIR)} with {len(listing['records'])} records.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Congress listing.json.")
    parser.parse_args()
    write_listing()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
