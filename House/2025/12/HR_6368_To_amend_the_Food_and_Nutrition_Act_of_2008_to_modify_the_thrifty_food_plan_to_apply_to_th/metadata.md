# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6368?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6368
- Title: Feeding Rural Families Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6368
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2026-05-16T08:07:47Z
- Update date including text: 2026-05-16T08:07:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6368",
    "number": "6368",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Feeding Rural Families Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:47Z",
    "updateDateIncludingText": "2026-05-16T08:07:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T15:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:01:56Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6368ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6368\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Ms. Tokuda (for herself and Mr. Case ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to modify the thrifty food plan to apply to the urban and rural parts of the State of Hawaii.\n#### 1. Short title\nThis Act may be cited as the Feeding Rural Families Act of 2025 .\n#### 2. Amendment\nSection 3(u)(2) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(u)(2) ) is amended\u2014\n**(1)**\nby inserting urban and rural parts of before Hawaii the 1st place it appears, and\n**(2)**\nby inserting urban and rural before Hawaii the 2d place it appears.",
      "versionDate": "2025-12-02",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-07T16:01:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-02",
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
          "measure-id": "id119hr6368",
          "measure-number": "6368",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-02",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6368v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-12-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Feeding Rural Families Act of 2025</strong></p><p>This bill provides for separate food cost calculations for urban and rural parts of Hawaii for the purposes of determining Supplemental Nutrition Assistance Program (SNAP) maximum monthly benefit allotments. Specifically, the bill requires separate\u00a0food cost adjustments in the Thrifty Food Plan (TFP) for urban and rural parts of Hawaii.</p><p>SNAP maximum monthly benefit allotments are tied to the cost of purchasing a nutritionally adequate low-cost diet, as measured by the Department of Agriculture-created and -calculated TFP. Maximum allotments are set at the monthly cost of the TFP for a four-person family, adjusted for family size. Under current law,\u00a0maximum allotments are higher (to reflect the cost of food) in Hawaii, Guam, and the U.S. Virgin Islands, as well as in urban and rural parts of Alaska.</p>"
        },
        "title": "Feeding Rural Families Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6368.xml",
    "summary": {
      "actionDate": "2025-12-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Feeding Rural Families Act of 2025</strong></p><p>This bill provides for separate food cost calculations for urban and rural parts of Hawaii for the purposes of determining Supplemental Nutrition Assistance Program (SNAP) maximum monthly benefit allotments. Specifically, the bill requires separate\u00a0food cost adjustments in the Thrifty Food Plan (TFP) for urban and rural parts of Hawaii.</p><p>SNAP maximum monthly benefit allotments are tied to the cost of purchasing a nutritionally adequate low-cost diet, as measured by the Department of Agriculture-created and -calculated TFP. Maximum allotments are set at the monthly cost of the TFP for a four-person family, adjusted for family size. Under current law,\u00a0maximum allotments are higher (to reflect the cost of food) in Hawaii, Guam, and the U.S. Virgin Islands, as well as in urban and rural parts of Alaska.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6368"
    },
    "title": "Feeding Rural Families Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Feeding Rural Families Act of 2025</strong></p><p>This bill provides for separate food cost calculations for urban and rural parts of Hawaii for the purposes of determining Supplemental Nutrition Assistance Program (SNAP) maximum monthly benefit allotments. Specifically, the bill requires separate\u00a0food cost adjustments in the Thrifty Food Plan (TFP) for urban and rural parts of Hawaii.</p><p>SNAP maximum monthly benefit allotments are tied to the cost of purchasing a nutritionally adequate low-cost diet, as measured by the Department of Agriculture-created and -calculated TFP. Maximum allotments are set at the monthly cost of the TFP for a four-person family, adjusted for family size. Under current law,\u00a0maximum allotments are higher (to reflect the cost of food) in Hawaii, Guam, and the U.S. Virgin Islands, as well as in urban and rural parts of Alaska.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6368"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6368ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to modify the thrifty food plan to apply to the urban and rural parts of the State of Hawaii.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T07:58:44Z"
    },
    {
      "title": "Feeding Rural Families Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Feeding Rural Families Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:38:19Z"
    }
  ]
}
```
