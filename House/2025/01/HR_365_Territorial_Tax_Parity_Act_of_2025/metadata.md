# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/365?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/365
- Title: Territorial Tax Parity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 365
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2026-04-27T15:45:39Z
- Update date including text: 2026-04-27T15:45:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/365",
    "number": "365",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000610",
        "district": "",
        "firstName": "Stacey",
        "fullName": "Del. Plaskett, Stacey E. [D-VI]",
        "lastName": "Plaskett",
        "party": "D",
        "state": "VI"
      }
    ],
    "title": "Territorial Tax Parity Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-27T15:45:39Z",
    "updateDateIncludingText": "2026-04-27T15:45:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:01:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr365ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 365\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Ms. Plaskett introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the residence and source rules to provide for economic recovery in the possessions of the United States.\n#### 1. Short title\nThis Act may be cited as the Territorial Tax Parity Act of 2025 .\n#### 2. Modification to source rules involving possessions\n##### (a) In general\nSection 937(b)(2) of the Internal Revenue Code of 1986 is amended by inserting , but only to the extent such income is attributable to an office or fixed place of business within the United States (determined under the rules of section 864(c)(5)) before the period at the end.\n##### (b) Source rules for personal property sales\nSection 865(j)(3) of such Code is amended by inserting , 932, after 931 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "American Samoa",
            "updateDate": "2025-04-11T14:39:43Z"
          },
          {
            "name": "Caribbean area",
            "updateDate": "2025-04-11T14:39:43Z"
          },
          {
            "name": "Guam",
            "updateDate": "2025-04-11T14:39:43Z"
          },
          {
            "name": "Northern Mariana Islands",
            "updateDate": "2025-04-11T14:39:43Z"
          },
          {
            "name": "Puerto Rico",
            "updateDate": "2025-04-11T14:39:43Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-04-11T14:39:43Z"
          },
          {
            "name": "Taxation of foreign income",
            "updateDate": "2025-04-11T14:39:43Z"
          },
          {
            "name": "U.S. territories and protectorates",
            "updateDate": "2025-04-11T14:39:43Z"
          },
          {
            "name": "Virgin Islands",
            "updateDate": "2025-04-11T14:39:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-14T18:47:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr365",
          "measure-number": "365",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2026-04-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr365v00",
            "update-date": "2026-04-27"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Territorial Tax Equity Parity Act</strong> <strong>of 2025</strong></p><p>This bill modifies the income sourcing rules related to taxation of income from U.S. territories.</p><p>Under the bill, income is U.S.-sourced income or effectively connected to a U.S. trade or business only if attributable to an office or fixed place of business in the United States. (Currently, income is sourced to a U.S. territory and, thus, may be excluded from the gross income of a bona fide resident of a U.S. territory in calculating U.S. federal income tax\u00a0if it is not U.S.-sourced income or effectively connected with a U.S. trade or business.)</p><ul></ul><p>Further, the bill authorizes the Internal Revenue Service (IRS) to limit the income tax payment to the Virgin Islands required to treat income from the sale of certain personal property as foreign-sourced income for federal tax purposes. (Currently, income from certain personal property sales from a fixed place of business in a U.S. territory by a U.S. resident may be U.S.-sourced income unless an income tax of at least\u00a010% is paid to\u00a0the U.S. territory. The Internal Revenue Service (IRS) may limit the 10% tax payment requirement related to income from personal property sales in Guam, American Samoa, the Northern Mariana Islands, and Puerto Rico.)</p>"
        },
        "title": "Territorial Tax Parity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr365.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Territorial Tax Equity Parity Act</strong> <strong>of 2025</strong></p><p>This bill modifies the income sourcing rules related to taxation of income from U.S. territories.</p><p>Under the bill, income is U.S.-sourced income or effectively connected to a U.S. trade or business only if attributable to an office or fixed place of business in the United States. (Currently, income is sourced to a U.S. territory and, thus, may be excluded from the gross income of a bona fide resident of a U.S. territory in calculating U.S. federal income tax\u00a0if it is not U.S.-sourced income or effectively connected with a U.S. trade or business.)</p><ul></ul><p>Further, the bill authorizes the Internal Revenue Service (IRS) to limit the income tax payment to the Virgin Islands required to treat income from the sale of certain personal property as foreign-sourced income for federal tax purposes. (Currently, income from certain personal property sales from a fixed place of business in a U.S. territory by a U.S. resident may be U.S.-sourced income unless an income tax of at least\u00a010% is paid to\u00a0the U.S. territory. The Internal Revenue Service (IRS) may limit the 10% tax payment requirement related to income from personal property sales in Guam, American Samoa, the Northern Mariana Islands, and Puerto Rico.)</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hr365"
    },
    "title": "Territorial Tax Parity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Territorial Tax Equity Parity Act</strong> <strong>of 2025</strong></p><p>This bill modifies the income sourcing rules related to taxation of income from U.S. territories.</p><p>Under the bill, income is U.S.-sourced income or effectively connected to a U.S. trade or business only if attributable to an office or fixed place of business in the United States. (Currently, income is sourced to a U.S. territory and, thus, may be excluded from the gross income of a bona fide resident of a U.S. territory in calculating U.S. federal income tax\u00a0if it is not U.S.-sourced income or effectively connected with a U.S. trade or business.)</p><ul></ul><p>Further, the bill authorizes the Internal Revenue Service (IRS) to limit the income tax payment to the Virgin Islands required to treat income from the sale of certain personal property as foreign-sourced income for federal tax purposes. (Currently, income from certain personal property sales from a fixed place of business in a U.S. territory by a U.S. resident may be U.S.-sourced income unless an income tax of at least\u00a010% is paid to\u00a0the U.S. territory. The Internal Revenue Service (IRS) may limit the 10% tax payment requirement related to income from personal property sales in Guam, American Samoa, the Northern Mariana Islands, and Puerto Rico.)</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hr365"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr365ih.xml"
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
      "title": "Territorial Tax Parity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Territorial Tax Parity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modify the residence and source rules to provide for economic recovery in the possessions of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:17Z"
    }
  ]
}
```
