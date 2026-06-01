# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3350?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3350
- Title: ACO Assignment Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3350
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-26T16:41:53Z
- Update date including text: 2026-01-26T16:41:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S8512)
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S8512)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3350",
    "number": "3350",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "ACO Assignment Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-01-26T16:41:53Z",
    "updateDateIncludingText": "2026-01-26T16:41:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S8512)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T18:36:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3350is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3350\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Barrasso (for himself and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to improve the way beneficiaries are assigned under the Medicare shared savings program by also basing such assignment on primary care services furnished by nurse practitioners, physician assistants, and clinical nurse specialists.\n#### 1. Short title\nThis Act may be cited as the ACO Assignment Improvement Act of 2025 .\n#### 2. Improvements to the assignment of beneficiaries under the Medicare shared savings program\nSection 1899(c)(1) of the Social Security Act ( 42 U.S.C. 1395jjj(c)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking and at the end;\n**(2)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(C) in the case of performance years beginning on or after January 1, 2026, primary care services provided under this title by an ACO professional described in subsection (h)(1)(B). .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-07-25",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4773",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ACO Assignment Improvement Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-01-07T17:16:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-04",
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
          "measure-id": "id119s3350",
          "measure-number": "3350",
          "measure-type": "s",
          "orig-publish-date": "2025-12-04",
          "originChamber": "SENATE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3350v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-12-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>ACO Assignment Improvement Act of 2025</strong></p><p>This bill establishes additional requirements for assigning Medicare fee-for-service beneficiaries to accountable care organizations (ACOs) under the Medicare shared savings program. Under current law, the program enables ACOs to receive payments for savings stemming from care coordination and management.</p><p>The bill requires the basis for assignment to reflect beneficiaries' utilization of not only primary care services provided by ACO physicians, but also those provided by other ACO practitioners\u2014specifically, physician assistants, nurse practitioners, and clinical nurse specialists.</p>"
        },
        "title": "ACO Assignment Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3350.xml",
    "summary": {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>ACO Assignment Improvement Act of 2025</strong></p><p>This bill establishes additional requirements for assigning Medicare fee-for-service beneficiaries to accountable care organizations (ACOs) under the Medicare shared savings program. Under current law, the program enables ACOs to receive payments for savings stemming from care coordination and management.</p><p>The bill requires the basis for assignment to reflect beneficiaries' utilization of not only primary care services provided by ACO physicians, but also those provided by other ACO practitioners\u2014specifically, physician assistants, nurse practitioners, and clinical nurse specialists.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s3350"
    },
    "title": "ACO Assignment Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>ACO Assignment Improvement Act of 2025</strong></p><p>This bill establishes additional requirements for assigning Medicare fee-for-service beneficiaries to accountable care organizations (ACOs) under the Medicare shared savings program. Under current law, the program enables ACOs to receive payments for savings stemming from care coordination and management.</p><p>The bill requires the basis for assignment to reflect beneficiaries' utilization of not only primary care services provided by ACO physicians, but also those provided by other ACO practitioners\u2014specifically, physician assistants, nurse practitioners, and clinical nurse specialists.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s3350"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3350is.xml"
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
      "title": "ACO Assignment Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ACO Assignment Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to improve the way beneficiaries are assigned under the Medicare shared savings program by also basing such assignment on primary care services furnished by nurse practitioners, physician assistants, and clinical nurse specialists.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:25Z"
    }
  ]
}
```
