# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1537?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1537
- Title: Veterans’ Transition to Trucking Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1537
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2025-12-05T22:00:21Z
- Update date including text: 2025-12-05T22:00:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1537",
    "number": "1537",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Veterans\u2019 Transition to Trucking Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:00:21Z",
    "updateDateIncludingText": "2025-12-05T22:00:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T19:43:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1537is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1537\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Blumenthal (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to approve interstate commerce carrier apprenticeship programs for purposes of veterans educational assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 Transition to Trucking Act of 2025 .\n#### 2. Authorization for Secretary of Veterans Affairs to approve interstate commerce carrier apprenticeship programs for purposes of veterans educational assistance\nSection 3672(c)(1) of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subparagraph (B) as subparagraph (C);\n**(2)**\nin subparagraph (A), in the matter before clause (i), by striking The State and inserting Except as provided in subparagraph (B), the State ; and\n**(3)**\nby inserting after subparagraph (A) the following new subparagraph (B):\n(B) The Secretary may act in the role of a State approving agency for purposes of approval of a multi-State apprenticeship program. .",
      "versionDate": "2025-04-30",
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
        "actionDate": "2025-09-19",
        "text": "Placed on the Union Calendar, Calendar No. 259."
      },
      "number": "2954",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans\u2019 Transition to Trucking Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-26T16:45:01Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-06-26T16:45:01Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-06-26T16:45:01Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-06-26T16:45:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T20:58:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
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
          "measure-id": "id119s1537",
          "measure-number": "1537",
          "measure-type": "s",
          "orig-publish-date": "2025-04-30",
          "originChamber": "SENATE",
          "update-date": "2025-07-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1537v00",
            "update-date": "2025-07-10"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans'\u00a0Transition to Trucking Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to act as a state approving agency to approve multi-state apprenticeship programs (i.e., non-federal apprenticeship programs operating in more than one state) for purposes of VA educational assistance benefits. (State approving agencies are designated by states to provide, among other duties, approval of courses of education for purposes of VA education benefits.)</p>"
        },
        "title": "Veterans\u2019 Transition to Trucking Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1537.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans'\u00a0Transition to Trucking Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to act as a state approving agency to approve multi-state apprenticeship programs (i.e., non-federal apprenticeship programs operating in more than one state) for purposes of VA educational assistance benefits. (State approving agencies are designated by states to provide, among other duties, approval of courses of education for purposes of VA education benefits.)</p>",
      "updateDate": "2025-07-10",
      "versionCode": "id119s1537"
    },
    "title": "Veterans\u2019 Transition to Trucking Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans'\u00a0Transition to Trucking Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to act as a state approving agency to approve multi-state apprenticeship programs (i.e., non-federal apprenticeship programs operating in more than one state) for purposes of VA educational assistance benefits. (State approving agencies are designated by states to provide, among other duties, approval of courses of education for purposes of VA education benefits.)</p>",
      "updateDate": "2025-07-10",
      "versionCode": "id119s1537"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1537is.xml"
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
      "title": "Veterans\u2019 Transition to Trucking Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans\u2019 Transition to Trucking Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to approve interstate commerce carrier apprenticeship programs for purposes of veterans educational assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:23Z"
    }
  ]
}
```
