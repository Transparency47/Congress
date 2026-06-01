# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1127?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1127
- Title: Dennis and Lois Krisfalusy Act
- Congress: 119
- Bill type: S
- Bill number: 1127
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-04-30T11:03:19Z
- Update date including text: 2026-04-30T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1127",
    "number": "1127",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Dennis and Lois Krisfalusy Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:19Z",
    "updateDateIncludingText": "2026-04-30T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
        "item": [
          {
            "date": "2026-04-29T21:37:06Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-25T20:16:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "ND"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1127is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1127\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Fetterman (for himself, Mr. McCormick , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to expand eligibility for memorial headstones and markers furnished by the Secretary of Veterans Affairs to certain individuals who died before November 11, 1998.\n#### 1. Short title\nThis Act may be cited as the Dennis and Lois Krisfalusy Act .\n#### 2. Expansion of eligibility for memorial headstones and markers furnished by Secretary of Veterans Affairs\nSection 2306(b)(2) of title 38, United States Code, is amended in subparagraphs (B) and (C) by striking who dies on or after November 11, 1998, each place it appears.",
      "versionDate": "2025-03-25",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-26",
        "text": "Subcommittee Hearings Held"
      },
      "number": "1344",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Dennis and Lois Krisfalusy Act",
      "type": "HR"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-07T19:24:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119s1127",
          "measure-number": "1127",
          "measure-type": "s",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2025-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1127v00",
            "update-date": "2025-05-21"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Dennis and Lois Krisfalusy Act</strong></p><p>This bill expands eligibility for a memorial headstone or marker for the spouse, surviving spouse, child, or dependent of a veteran or member of the Armed Forces. Currently, for individuals whose remains are unavailable, such benefit is only available for individuals who died on or after November 11, 1998. The bill makes such individuals eligible regardless of the date they died.</p>"
        },
        "title": "Dennis and Lois Krisfalusy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1127.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dennis and Lois Krisfalusy Act</strong></p><p>This bill expands eligibility for a memorial headstone or marker for the spouse, surviving spouse, child, or dependent of a veteran or member of the Armed Forces. Currently, for individuals whose remains are unavailable, such benefit is only available for individuals who died on or after November 11, 1998. The bill makes such individuals eligible regardless of the date they died.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119s1127"
    },
    "title": "Dennis and Lois Krisfalusy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dennis and Lois Krisfalusy Act</strong></p><p>This bill expands eligibility for a memorial headstone or marker for the spouse, surviving spouse, child, or dependent of a veteran or member of the Armed Forces. Currently, for individuals whose remains are unavailable, such benefit is only available for individuals who died on or after November 11, 1998. The bill makes such individuals eligible regardless of the date they died.</p>",
      "updateDate": "2025-05-21",
      "versionCode": "id119s1127"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1127is.xml"
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
      "title": "Dennis and Lois Krisfalusy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dennis and Lois Krisfalusy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to expand eligibility for memorial headstones and markers furnished by the Secretary of Veterans Affairs to certain individuals who died before November 11, 1998.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:40Z"
    }
  ]
}
```
