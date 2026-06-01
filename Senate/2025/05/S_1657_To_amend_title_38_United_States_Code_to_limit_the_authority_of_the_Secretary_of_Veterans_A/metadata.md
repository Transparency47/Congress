# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1657?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1657
- Title: Review Every Veteran’s Claim Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1657
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-03-27T16:20:17Z
- Update date including text: 2026-03-27T16:20:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1657",
    "number": "1657",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Review Every Veteran\u2019s Claim Act of 2025",
    "type": "S",
    "updateDate": "2026-03-27T16:20:17Z",
    "updateDateIncludingText": "2026-03-27T16:20:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
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
            "date": "2026-03-18T20:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:08Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-07T21:08:25Z",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-07",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1657is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1657\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Banks (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to limit the authority of the Secretary of Veterans Affairs to deny the claim of a veteran for benefits under the laws administered by such Secretary on the sole basis that such veteran failed to appear for a medical examination associated with such claim, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Review Every Veteran\u2019s Claim Act of 2025 .\n#### 2. Prohibition on denial of claims for benefits under laws administered by Secretary of Veterans Affairs on sole basis that veteran failed to appear for certain medical examination\nSubsection (d) of section 5103A of title 38, United States Code, is amended\u2014\n**(1)**\nin the heading, by striking compensation claims and inserting claims for benefits ;\n**(2)**\nin paragraph (2), by striking treat an examination or opinion as being necessary to make a decision on a claim for purposes of and inserting provide for a medical examination or obtain a medical opinion under ; and\n**(3)**\nby adding at the end the following new paragraph:\n(3) If a veteran fails to appear for a medical examination provided by the Secretary in conjunction with a claim for a benefit under a law administered by the Secretary, the Secretary may not deny such claim on the sole basis that such veteran failed to appear for such medical examination. .",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-07-23",
        "text": "Ordered to be Reported by Voice Vote."
      },
      "number": "2137",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Review Every Veterans Claim Act of 2025",
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
            "name": "Veterans' medical care",
            "updateDate": "2025-12-12T21:04:53Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-12-12T21:04:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:28:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-07",
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
          "measure-id": "id119s1657",
          "measure-number": "1657",
          "measure-type": "s",
          "orig-publish-date": "2025-05-07",
          "originChamber": "SENATE",
          "update-date": "2025-06-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1657v00",
            "update-date": "2025-06-30"
          },
          "action-date": "2025-05-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Review Every Veteran's Claim Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from denying a claim for benefits on the sole basis that a veteran failed to appear for a medical examination provided by the VA in conjunction with the claim for benefits.</p>"
        },
        "title": "Review Every Veteran\u2019s Claim Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1657.xml",
    "summary": {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Review Every Veteran's Claim Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from denying a claim for benefits on the sole basis that a veteran failed to appear for a medical examination provided by the VA in conjunction with the claim for benefits.</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119s1657"
    },
    "title": "Review Every Veteran\u2019s Claim Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Review Every Veteran's Claim Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from denying a claim for benefits on the sole basis that a veteran failed to appear for a medical examination provided by the VA in conjunction with the claim for benefits.</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119s1657"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1657is.xml"
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
      "title": "Review Every Veteran\u2019s Claim Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Review Every Veteran\u2019s Claim Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to limit the authority of the Secretary of Veterans Affairs to deny the claim of a veteran for benefits under the laws administered by such Secretary on the sole basis that such veteran failed to appear for a medical examination associated with such claim, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:18Z"
    }
  ]
}
```
