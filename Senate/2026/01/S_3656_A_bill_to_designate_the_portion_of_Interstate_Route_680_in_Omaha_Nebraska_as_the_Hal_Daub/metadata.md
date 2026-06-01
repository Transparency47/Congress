# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3656?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3656
- Title: A bill to designate the portion of Interstate Route 680 in Omaha, Nebraska, as the "Hal Daub Freeway".
- Congress: 119
- Bill type: S
- Bill number: 3656
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-03-12T11:07:21Z
- Update date including text: 2026-03-12T11:07:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3656",
    "number": "3656",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "A bill to designate the portion of Interstate Route 680 in Omaha, Nebraska, as the \"Hal Daub Freeway\".",
    "type": "S",
    "updateDate": "2026-03-12T11:07:21Z",
    "updateDateIncludingText": "2026-03-12T11:07:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-01-15T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "NE"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3656is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3656\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mrs. Fischer (for herself and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo designate the portion of Interstate Route 680 in Omaha, Nebraska, as the Hal Daub Freeway .\n#### 1. Hal Daub Freeway\n##### (a) Designation\nThe portion of Interstate Route 680 located in Omaha, Nebraska, beginning at mile post 0 and ending at the Missouri River, shall be known and designated as the Hal Daub Freeway .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the portion of Interstate Route 680 referred to in subsection (a) shall be deemed to be a reference to the Hal Daub Freeway .",
      "versionDate": "2026-01-15",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-11T17:18:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-15",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s3656",
          "measure-number": "3656",
          "measure-type": "s",
          "orig-publish-date": "2026-01-15",
          "originChamber": "SENATE",
          "update-date": "2026-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3656v00",
            "update-date": "2026-03-12"
          },
          "action-date": "2026-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill designates a portion of Interstate Route 680 in Omaha, Nebraska, as the\u00a0Hal Daub Freeway.</p><p>Harold John Daub Jr. served in the House of Representatives from 1981-1989 and as the mayor of Omaha, Nebraska, from 1995-2001.</p>"
        },
        "title": "A bill to designate the portion of Interstate Route 680 in Omaha, Nebraska, as the \"Hal Daub Freeway\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3656.xml",
    "summary": {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill designates a portion of Interstate Route 680 in Omaha, Nebraska, as the\u00a0Hal Daub Freeway.</p><p>Harold John Daub Jr. served in the House of Representatives from 1981-1989 and as the mayor of Omaha, Nebraska, from 1995-2001.</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119s3656"
    },
    "title": "A bill to designate the portion of Interstate Route 680 in Omaha, Nebraska, as the \"Hal Daub Freeway\"."
  },
  "summaries": [
    {
      "actionDate": "2026-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill designates a portion of Interstate Route 680 in Omaha, Nebraska, as the\u00a0Hal Daub Freeway.</p><p>Harold John Daub Jr. served in the House of Representatives from 1981-1989 and as the mayor of Omaha, Nebraska, from 1995-2001.</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119s3656"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3656is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to designate the portion of Interstate Route 680 in Omaha, Nebraska, as the \"Hal Daub Freeway\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:38Z"
    },
    {
      "title": "A bill to designate the portion of Interstate Route 680 in Omaha, Nebraska, as the \"Hal Daub Freeway\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T11:56:22Z"
    }
  ]
}
```
