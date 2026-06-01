# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4989?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4989
- Title: Streamlining Rural Housing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4989
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2026-03-19T08:07:25Z
- Update date including text: 2026-03-19T08:07:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4989",
    "number": "4989",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "S001188",
        "district": "3",
        "firstName": "Marlin",
        "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
        "lastName": "Stutzman",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Streamlining Rural Housing Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:25Z",
    "updateDateIncludingText": "2026-03-19T08:07:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CO"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "MI"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "GA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "IA"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "MT"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "NC"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NC"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NH"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4989ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4989\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Stutzman (for himself, Ms. Pettersen , Mrs. McClain , and Mr. David Scott of Georgia ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of Housing and Urban Development and the Secretary of Agriculture to enter into a memorandum of understanding relating to housing projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Rural Housing Act of 2025 .\n#### 2. Memorandum of understanding\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Housing and Urban Development and the Secretary of Agriculture shall enter into a memorandum of understanding to\u2014\n**(1)**\nevaluate categorical exclusions (as defined in section 111 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336e )) for housing projects funded by amounts from the Department of the Housing and Urban Development and the Department of Agriculture;\n**(2)**\ndevelop a process to designate a lead agency among the Department of Housing and Urban Development and the Department of Agriculture and streamline the adoption of environmental impact statements and environmental assessments approved by the other agency to construct housing projects funded by amounts from both agencies;\n**(3)**\nmaintain compliance with environmental regulations under part 58 of title 24, Code of Federal Regulations, as in effect on January 1, 2025; and\n**(4)**\nevaluate the feasibility of a joint physical inspection process for housing projects funded by amounts from the Department of the Housing and Urban Development and the Department of Agriculture.\n##### (b) Advisory working group\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Housing and Urban Development and the Secretary of Agriculture shall establish an advisory working group for the purpose of consulting on the implementation of the memorandum of understanding entered into under subsection (a).\n**(2) Members**\nThe advisory working group established under paragraph (1) shall consist of rural and non-rural stakeholders, including\u2014\n**(A)**\naffordable housing nonprofit organizations;\n**(B)**\nState housing and housing finance agencies;\n**(C)**\nnonprofit and for-profit home builders and housing developers;\n**(D)**\nproperty management companies;\n**(E)**\nowners of multifamily properties, including nonprofit and for-profit owners and operators;\n**(F)**\npublic housing agencies;\n**(G)**\nresidents in housing assisted by the Department of Housing and Urban Development or the Department of Agriculture and representatives of those residents; and\n**(H)**\nhousing contract administrators.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary of Housing and Urban Development and the Secretary of Agriculture shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that includes recommendations for legislative, regulatory, or administrative actions\u2014\n**(1)**\nto improve the efficiency and effectiveness of housing projects funded by amounts from the Department of the Housing and Urban Development and the Department of Agriculture; and\n**(2)**\nthat do not materially, with respect to residents of housing projects described in paragraph (1)\u2014\n**(A)**\nreduce the safety of those residents;\n**(B)**\nshift long-term costs onto those residents; or\n**(C)**\nundermine the environmental standards of those residents.",
      "versionDate": "2025-08-15",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2423",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Streamlining Rural Housing Act of 2025",
      "type": "S"
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-12T15:19:18Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4989ih.xml"
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
      "title": "Streamlining Rural Housing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T05:28:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining Rural Housing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-20T05:28:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development and the Secretary of Agriculture to enter into a memorandum of understanding relating to housing projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T05:11:17Z"
    }
  ]
}
```
