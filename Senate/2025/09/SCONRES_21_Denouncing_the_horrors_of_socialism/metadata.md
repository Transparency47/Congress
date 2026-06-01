# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/21?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/21
- Title: A concurrent resolution denouncing the horrors of socialism.
- Congress: 119
- Bill type: SCONRES
- Bill number: 21
- Origin chamber: Senate
- Introduced date: 2025-09-03
- Update date: 2026-04-14T17:06:02Z
- Update date including text: 2026-04-14T17:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-03: Introduced in Senate
- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6011-6012)
- Latest action: 2025-09-03: Introduced in Senate

## Actions

- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6011-6012)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/21",
    "number": "21",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A concurrent resolution denouncing the horrors of socialism.",
    "type": "SCONRES",
    "updateDate": "2026-04-14T17:06:02Z",
    "updateDateIncludingText": "2026-04-14T17:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S6011-6012)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T20:18:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres21is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. CON. RES. 21\nIN THE SENATE OF THE UNITED STATES\nSeptember 3, 2025 Mr. Scott of Florida submitted the following concurrent resolution; which was referred to the Committee on the Judiciary\nCONCURRENT RESOLUTION\nDenouncing the horrors of socialism.\nThat Congress denounces socialism in all its forms, and opposes the implementation of socialist policies in the United States.",
      "versionDate": "2025-09-03",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-01",
        "text": "Received in the Senate."
      },
      "number": "58",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Denouncing the horrors of socialism.",
      "type": "HCONRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Economic theory",
            "updateDate": "2025-11-18T19:24:05Z"
          },
          {
            "name": "Political movements and philosophies",
            "updateDate": "2025-11-18T19:24:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-18T21:10:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-03",
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
          "measure-id": "id119sconres21",
          "measure-number": "21",
          "measure-type": "sconres",
          "orig-publish-date": "2025-09-03",
          "originChamber": "SENATE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sconres21v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-09-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This concurrent resolution denounces socialism and opposes the implementation of socialist policies in the United States.</p>"
        },
        "title": "A concurrent resolution denouncing the horrors of socialism."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sconres/BILLSUM-119sconres21.xml",
    "summary": {
      "actionDate": "2025-09-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This concurrent resolution denounces socialism and opposes the implementation of socialist policies in the United States.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119sconres21"
    },
    "title": "A concurrent resolution denouncing the horrors of socialism."
  },
  "summaries": [
    {
      "actionDate": "2025-09-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This concurrent resolution denounces socialism and opposes the implementation of socialist policies in the United States.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119sconres21"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres21is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A concurrent resolution denouncing the horrors of socialism.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-05T04:03:24Z"
    },
    {
      "title": "A concurrent resolution denouncing the horrors of socialism.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-04T10:56:18Z"
    }
  ]
}
```
