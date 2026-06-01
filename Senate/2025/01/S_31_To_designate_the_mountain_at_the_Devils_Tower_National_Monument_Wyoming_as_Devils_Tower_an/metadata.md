# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/31?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/31
- Title: A bill to designate the mountain at the Devils Tower National Monument, Wyoming, as Devils Tower, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 31
- Origin chamber: Senate
- Introduced date: 2025-01-08
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-08: Introduced in Senate
- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-01-08: Introduced in Senate

## Actions

- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-08",
    "latestAction": {
      "actionDate": "2025-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/31",
    "number": "31",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A bill to designate the mountain at the Devils Tower National Monument, Wyoming, as Devils Tower, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-08",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-08",
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
          "date": "2025-01-08T16:30:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s31is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 31\nIN THE SENATE OF THE UNITED STATES\nJanuary 8, 2025 Ms. Lummis (for herself and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo designate the mountain at the Devils Tower National Monument, Wyoming, as Devils Tower, and for other purposes.\n#### 1. Designation of Devils Tower\n##### (a) In general\nThe mountain at the Devils Tower National Monument, Wyoming, located at 44\u00b035\u203226\u2033N, by 104\u00b042\u203255\u2033W, and the area located at 44\u00b035\u203221\u2033N, by 104\u00b041\u203248\u2033W, shall be known and designated as Devils Tower .\n##### (b) References\nAny reference in any law, map, regulation, order, document, paper, or other record of the United States to the mountain and area described in subsection (a) shall be deemed to be a reference to Devils Tower .",
      "versionDate": "2025-01-08",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T20:04:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-08",
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
          "measure-id": "id119s31",
          "measure-number": "31",
          "measure-type": "s",
          "orig-publish-date": "2025-01-08",
          "originChamber": "SENATE",
          "update-date": "2025-05-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s31v00",
            "update-date": "2025-05-29"
          },
          "action-date": "2025-01-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill declares that the mountain at the Devils Tower National Monument in Wyoming shall be known and designated as Devils Tower.</p>"
        },
        "title": "A bill to designate the mountain at the Devils Tower National Monument, Wyoming, as Devils Tower, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s31.xml",
    "summary": {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill declares that the mountain at the Devils Tower National Monument in Wyoming shall be known and designated as Devils Tower.</p>",
      "updateDate": "2025-05-29",
      "versionCode": "id119s31"
    },
    "title": "A bill to designate the mountain at the Devils Tower National Monument, Wyoming, as Devils Tower, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill declares that the mountain at the Devils Tower National Monument in Wyoming shall be known and designated as Devils Tower.</p>",
      "updateDate": "2025-05-29",
      "versionCode": "id119s31"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s31is.xml"
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
      "title": "A bill to designate the mountain at the Devils Tower National Monument, Wyoming, as Devils Tower, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:21Z"
    },
    {
      "title": "A bill to designate the mountain at the Devils Tower National Monument, Wyoming, as Devils Tower, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-09T11:56:15Z"
    }
  ]
}
```
