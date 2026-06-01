# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6813?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6813
- Title: VA Insurance Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 6813
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-03-07T09:06:41Z
- Update date including text: 2026-03-07T09:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-22 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-22 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6813",
    "number": "6813",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "VA Insurance Improvement Act",
    "type": "HR",
    "updateDate": "2026-03-07T09:06:41Z",
    "updateDateIncludingText": "2026-03-07T09:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-22T15:17:20Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6813ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6813\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Pappas (for himself and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements to the laws administered by the Secretary of Veterans Affairs relating to insurance for veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Insurance Improvement Act .\n#### 2. Expansion of veterans life insurance program\n##### (a) In general\nSection 1922B of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking service-disabled ;\n**(B)**\nby striking paragraph (3);\n**(C)**\nby redesignating paragraphs (4) through (6) as paragraphs (3) through (5), respectively; and\n**(D)**\nin paragraph (5)(A), as so redesignated, by striking paragraph (5) and inserting paragraph (4) ;\n**(2)**\nin subsection (b), by striking the veteran has a service-connected disability and all that follows through the period at the end of paragraph (2) and inserting the following: the veteran submits an application for such insurance before the veteran attains 81 years of age. ; and\n**(3)**\nin subsection (c)(2)(B)(ii), by striking subsection (a)(5) and inserting subsection (a)(4) .\n##### (b) Clerical amendments\n**(1) Section heading**\nSuch section is further amended by striking the section heading and inserting the following:\n1922B. Veterans Affairs life insurance .\n**(2) Table of sections**\nThe table of sections at the beginning of chapter 19 of such title is amended by striking the item relating to section 1922B and inserting the following new item:\n1922B. Veterans Affairs life insurance. .\n#### 3. Veterans\u2019 mortgage life insurance reimbursement of administrative costs\nSection 2106(d) of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraph (2) as paragraph (3);\n**(2)**\nby inserting after paragraph (1) the following new paragraph (2):\n(2) For each fiscal year, the Secretary shall determine the administrative costs to the Department that, in the judgment of the Secretary, are properly allocable to the provision of insurance under this section and shall reimburse the General Operating Expenses appropriations account and the Information Technology Systems, Department of Veterans Affairs appropriations account of the Department in appropriate amounts for such administrative costs from amounts in the Veterans Insurance and Indemnities appropriation account. ; and\n**(3)**\nin paragraph (3), as so redesignated, by striking such account and inserting the Veterans Insurance and Indemnities appropriation account .\n#### 4. Inclusion of Space Force in eligibility for TSGLI\nSection 1965(6) of title 38, United States Code, is amended by inserting Space Force, after Marine Corps, .",
      "versionDate": "2025-12-17",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-21T16:07:54Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6813ih.xml"
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
      "title": "VA Insurance Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Insurance Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain improvements to the laws administered by the Secretary of Veterans Affairs relating to insurance for veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:18Z"
    }
  ]
}
```
