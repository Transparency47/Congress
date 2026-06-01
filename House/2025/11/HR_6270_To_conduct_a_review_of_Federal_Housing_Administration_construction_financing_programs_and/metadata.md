# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6270?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6270
- Title: Modular Housing Production Act
- Congress: 119
- Bill type: HR
- Bill number: 6270
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-01-07T09:05:54Z
- Update date including text: 2026-01-07T09:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6270",
    "number": "6270",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001136",
        "district": "9",
        "firstName": "Lisa",
        "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
        "lastName": "McClain",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Modular Housing Production Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:54Z",
    "updateDateIncludingText": "2026-01-07T09:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:04:50Z",
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
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "MA"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NC"
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
      "sponsorshipDate": "2026-01-06",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6270ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6270\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mrs. McClain (for herself and Mr. Lynch ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo conduct a review of Federal Housing Administration construction financing programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modular Housing Production Act .\n#### 2. Definitions\nIn this Act:\n**(1) Manufactured home**\nThe term manufactured home has the meaning given the term in section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402 ).\n**(2) Modular home**\nThe term modular home means a home that is constructed in a factory in 1 or more modules, each of which meet applicable State and local building codes of the area in which the home will be located, and that are transported to the home building site, installed on foundations, and completed.\n**(3) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n#### 3. FHA construction financing programs\n##### (a) In general\nThe Secretary shall conduct a review of Federal Housing Administration construction financing programs to identify barriers to the use of modular home methods.\n##### (b) Requirements\nIn conducting the review under subsection (a), the Secretary shall\u2014\n**(1)**\nidentify and evaluate regulatory and programmatic features that restrict participation in construction financing programs by modular home developers, including construction draw schedules; and\n**(2)**\nidentify administrative measures authorized under section 525 of the National Housing Act ( 12 U.S.C. 1735f\u20133 ) to facilitate program utilization by modular home developers.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall publish a report that describes the results of the review conducted under subsection (a), which shall include a description of programmatic and policy changes that the Secretary recommends to reduce or eliminate identified barriers to the use of modular home methods in Federal Housing Administration construction financing programs.\n##### (d) Rulemaking\n**(1) In general**\nNot later than 120 days after the date on which the Secretary publishes the report under subsection (c), the Secretary shall initiate a rulemaking to examine an alternative draw schedule for construction financing loans provided to modular and manufactured home developers, which shall include the ability for interested stakeholders to provide robust public comment.\n**(2) Determination**\nFollowing the period for public comment under paragraph (1), the Secretary shall\u2014\n**(A)**\nissue a final rule regarding an alternative draw schedule described in paragraph (1); or\n**(B)**\nprovide an explanation as to why the rule shall not become final.\n#### 4. Standardized uniform commercial code for modular homes\n##### (a) Award\nThe Secretary may award a grant to study the design and feasibility of a standardized uniform commercial code for modular homes, which shall evaluate\u2014\n**(1)**\nthe utility of a standardized coding system for serializing and securing modules, streamlining design and construction, and improving modular home innovation; and\n**(2)**\na means to coordinate a standardized code with financing incentives.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated such funds as may be necessary to carry out subsection (a).",
      "versionDate": "2025-11-21",
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
        "actionDate": "2025-07-28",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2489",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Modular Housing Production Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-18T16:55:32Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6270ih.xml"
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
      "title": "Modular Housing Production Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T07:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modular Housing Production Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T07:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To conduct a review of Federal Housing Administration construction financing programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T07:33:36Z"
    }
  ]
}
```
