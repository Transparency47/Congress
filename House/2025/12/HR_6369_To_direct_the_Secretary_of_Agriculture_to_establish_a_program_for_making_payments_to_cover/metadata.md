# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6369?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6369
- Title: Cutting COSTS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6369
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2026-05-16T08:07:57Z
- Update date including text: 2026-05-16T08:07:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6369",
    "number": "6369",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Cutting COSTS Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:57Z",
    "updateDateIncludingText": "2026-05-16T08:07:57Z"
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
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
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
          "date": "2025-12-02T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:02:06Z",
                "name": "Referred to"
              }
            },
            "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
            "systemCode": "hsag16"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:02:06Z",
                "name": "Referred to"
              }
            },
            "name": "Nutrition and Foreign Agriculture Subcommittee",
            "systemCode": "hsag03"
          }
        ]
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6369ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6369\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. Vindman (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo direct the Secretary of Agriculture to establish a program for making payments to covered producers for the cost of carrying out GAP audits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cutting Cumbersome Overhead for Small-farm Testing Savings Act of 2025 or the Cutting COSTS Act of 2025 .\n#### 2. Good agricultural practices payment program\n##### (a) In general\nThe Secretary shall establish a program for making payments to covered producers in an amount that is equal to the full cost incurred by each such producer for carrying out a GAP audit.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, and annually for each of the four years thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report regarding activities under the program established under subsection (a), including\u2014\n**(1)**\nthe number and type of covered producers who received payments under such program; and\n**(2)**\nthe extent to which such payment increased, for each such producer, market access to a retail food store that requires a GAP audit as a condition for such access.\n##### (c) Funding\nThe Secretary shall use the funds of the Commodity Credit Corporation to carry out this section.\n##### (d) Definitions\nIn this Act:\n**(1) Covered producer**\nThe term covered producer means a person\u2014\n**(A)**\nthat\u2014\n**(i)**\noperates a small farm with an average adjusted gross income (as defined in section 1001D(a) of the Food Security Act of 1985 (7 U.S.C. 1308\u20133a(a))) of less than $350,000 each year; or\n**(ii)**\nis a beginning farmer or rancher (as defined in section 3430.602 of title 7, Code of Federal Regulations (or a successor regulation)); and\n**(B)**\nmeets such other requirements as the Secretary may determine appropriate.\n**(2) GAP audit**\nThe term GAP audit means an audit under the Agricultural Marketing Service Audit Verification and Accreditation Programs described in part 62 of title 7, Code of Federal Regulations (or successor regulations), as such programs relate to good agricultural practices and guidance published by the Secretary of Health and Human Services under section 419(e)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350h(e)(1) ).\n**(3) Retail food store**\nThe term retail food store has the meaning given such term in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ).\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (e) Sunset\nThe authority under this section shall terminate on the date that is 5 years after the date of the enactment of this Act.",
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
        "updateDate": "2025-12-19T18:10:22Z"
      }
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6369ih.xml"
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
      "title": "Cutting COSTS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cutting COSTS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cutting Cumbersome Overhead for Small-farm Testing Savings Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to establish a program for making payments to covered producers for the cost of carrying out GAP audits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:04:00Z"
    }
  ]
}
```
