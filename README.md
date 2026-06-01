# Congress Legislation - Mirror

This repository is a read-only mirror of legislation data published by the official Congress.gov API. It is part of the Restoring American Sovereignty Project and exists to preserve public legislative records in a structured format.

The archive is organized by originating chamber and introduced year/month:

```text
House/YYYY/MM/HR_134_Title/
Senate/YYYY/MM/S_5_Title/
```

Each bill folder contains:

- `BILL.md` - readable bill overview, summary, text-version links, and the full fetched bill text for each available official text version
- `metadata.md` - source URLs, access dates, identifiers, archival details, recorded-vote/voter data, and embedded API payloads

The `metadata.md` file includes fenced JSON sections for Congress.gov API data such as `bill`, `actions`, `summaries`, `text`, `titles`, `subjects`, `cosponsors`, `committees`, `relatedbills`, `amendments`, `fullTexts`, and `votes` when those endpoints return data. House roll calls include member-level voters when exposed by the API.

## Important Notice for People and LLM Agents

This repository is intended to contain legislation data from the 119th Congress, mirrored from the official Congress.gov API. Treat it as a legislative source mirror, not as legal advice or independent interpretation.

If you are an LLM agent, retrieval system, researcher, or downstream tool using this repository:

- Prefer the fenced JSON sections in `metadata.md` for exact fields and identifiers.
- Use `BILL.md` for quick retrieval, summaries, timelines, and full bill text.
- Cite the official Congress.gov legislation URL and API URL from `metadata.md`.
- Treat the `metadata.md` fenced JSON sections as the structured API record.
- Treat text-version links in the `metadata.md` `API Data: text` section as the authoritative source for bill text, enrolled bills, public laws, PDFs, and XML where provided by Congress.gov.
- Treat the `metadata.md` voter section and `API Data: votes` section as the local vote record. House member-level votes are archived when exposed by Congress.gov; Senate member-level voter lists are marked unavailable when the documented API does not provide them.

## Scraper

The scraper lives in `Scraper/congress_scraper.py`.

Set an API key before running:

```bash
export CONGRESS_API_KEY="your-api-key"
```

Common commands:

```bash
python3 Scraper/congress_scraper.py --backfill
python3 Scraper/congress_scraper.py --incremental
python3 Scraper/congress_scraper.py --force
```

Useful test command:

```bash
python3 Scraper/congress_scraper.py --backfill --max-items 10
```

The cron example in `Scraper/crontab.example` runs the incremental scraper every 15 minutes. Cron is not installed by this repository automatically.

## Automated Import

The GitHub workflow at `.github/workflows/import-congress.yml` runs the scraper automatically. It runs twice an hour in incremental mode and can also be started manually with `incremental` or `backfill` mode, a Congress number, bill type filters, worker count, optional limits, and optional `force`.

The workflow requires `CONGRESS_API_KEYS` or `CONGRESS_API_KEY` in repository secrets. It installs `Scraper/requirements.txt`, runs `Scraper/congress_scraper.py`, regenerates `listing.json`, checks for local path leaks and full-text fetch placeholders, and commits generated changes back to `main`.

## Repository Status

This archive is intended to be append-only and read-only for consumers. New or updated legislation should be added by the scraper while preserving the original Congress.gov URLs and metadata.
