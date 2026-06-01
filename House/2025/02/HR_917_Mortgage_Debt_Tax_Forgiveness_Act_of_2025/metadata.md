# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/917?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/917
- Title: Mortgage Debt Tax Forgiveness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 917
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-03-31T14:39:19Z
- Update date including text: 2026-03-31T14:39:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/917",
    "number": "917",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Mortgage Debt Tax Forgiveness Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-31T14:39:19Z",
    "updateDateIncludingText": "2026-03-31T14:39:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-04T17:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr917ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 917\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Ms. Brownley introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to make permanent the exclusion from gross income of discharge of qualified principal residence indebtedness.\n#### 1. Short title\nThis Act may be cited as the Mortgage Debt Tax Forgiveness Act of 2025 .\n#### 2. Permanent extension of exclusion from gross income of discharge of qualified principal residence indebtedness\n##### (a) In general\nSection 108(a)(1)(E) of the Internal Revenue Code of 1986 is amended by striking which is discharged and all that follows and inserting a period.\n##### (b) Effective date\nThe amendment made by this section shall apply to indebtedness discharged after December 31, 2025.",
      "versionDate": "2025-02-04",
      "versionType": "Introduced in House"
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
        "name": "Taxation",
        "updateDate": "2025-04-16T14:53:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "House",
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
          "measure-id": "id119hr917",
          "measure-number": "917",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr917v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mortgage Debt Tax Forgiveness Act of 2025</strong></p><p>This bill makes permanent the exclusion of the discharge of qualified principal residence indebtedness\u00a0from gross income for federal tax purposes.</p><p>Under current law, a taxpayer may generally exclude from gross income\u00a0up to $750,000 (or $375,000 if married but filing a separate federal tax return)\u00a0from\u00a0the discharge of indebtedness that is (1)\u00a0incurred to purchase, build, or substantially improve a principal residence (or refinance such indebtedness); and (2) secured by the principal residence. The discharge must currently occur before January 1, 2026, and some limitations apply.</p>"
        },
        "title": "Mortgage Debt Tax Forgiveness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr917.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mortgage Debt Tax Forgiveness Act of 2025</strong></p><p>This bill makes permanent the exclusion of the discharge of qualified principal residence indebtedness\u00a0from gross income for federal tax purposes.</p><p>Under current law, a taxpayer may generally exclude from gross income\u00a0up to $750,000 (or $375,000 if married but filing a separate federal tax return)\u00a0from\u00a0the discharge of indebtedness that is (1)\u00a0incurred to purchase, build, or substantially improve a principal residence (or refinance such indebtedness); and (2) secured by the principal residence. The discharge must currently occur before January 1, 2026, and some limitations apply.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr917"
    },
    "title": "Mortgage Debt Tax Forgiveness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mortgage Debt Tax Forgiveness Act of 2025</strong></p><p>This bill makes permanent the exclusion of the discharge of qualified principal residence indebtedness\u00a0from gross income for federal tax purposes.</p><p>Under current law, a taxpayer may generally exclude from gross income\u00a0up to $750,000 (or $375,000 if married but filing a separate federal tax return)\u00a0from\u00a0the discharge of indebtedness that is (1)\u00a0incurred to purchase, build, or substantially improve a principal residence (or refinance such indebtedness); and (2) secured by the principal residence. The discharge must currently occur before January 1, 2026, and some limitations apply.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr917"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr917ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Mortgage Debt Tax Forgiveness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mortgage Debt Tax Forgiveness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to make permanent the exclusion from gross income of discharge of qualified principal residence indebtedness.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:30Z"
    }
  ]
}
```
