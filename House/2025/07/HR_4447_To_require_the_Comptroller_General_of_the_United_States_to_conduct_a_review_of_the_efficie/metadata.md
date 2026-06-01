# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4447?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4447
- Title: Transit Bus Affordability Act
- Congress: 119
- Bill type: HR
- Bill number: 4447
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2025-10-01T08:06:04Z
- Update date including text: 2025-10-01T08:06:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-17 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-17 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4447",
    "number": "4447",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Transit Bus Affordability Act",
    "type": "HR",
    "updateDate": "2025-10-01T08:06:04Z",
    "updateDateIncludingText": "2025-10-01T08:06:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-17T17:04:19Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "OH"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4447ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4447\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Frost (for himself and Mr. Turner of Ohio ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Comptroller General of the United States to conduct a review of the efficient use of funds in procuring new buses for transit service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transit Bus Affordability Act .\n#### 2. Report on options for procuring buses for transit service\n##### (a) In general\nThe Comptroller General of the United States shall conduct a review of the factors responsible for the high and rising costs of transit bus manufacturing and procurement in the United States in order to recommend ways to mitigate those costs and promote the efficient use of Federal, State, and local funds in procuring new buses for transit service.\n##### (b) Requirements\nIn conducting the review under subsection (a), the Comptroller General shall analyze the following:\n**(1)**\nThe primary cost drivers in the design and procurement process for transit buses in the United States.\n**(2)**\nA comparison of\u2014\n**(A)**\nthe costs to design, manufacture, and procure transit buses in the United States with the costs to design, manufacture, and procure such buses in other countries; and\n**(B)**\nin the most recent 10-year period for which data is available, the increase in price of transit buses with increases in the prices of medium-duty vehicles, school buses, and other commercial vehicles.\n**(3)**\nThe effects of bus manufacturing and supplier challenges on bus procurements funded by the Federal Transit Administration, such as buses procured pursuant to the low or no emission grant program and the buses and bus facilities competitive grant program under section 5339 of title 49, United States Code.\n**(4)**\nThe steps taken by the Administrator of the Federal Transit Administration, States, transit agencies, manufacturers, and industry stakeholders to reduce bus costs and accelerate delivery timeframes, including a description of\u2014\n**(A)**\nwhat is known about how likely such steps are to affect the costs and manufacturing timeframes for new transit bus orders;\n**(B)**\nthe effect of the use of State contracts and joint procurement on vehicle costs; and\n**(C)**\nany additional authorities identified by stakeholders that the Administrator or transit agencies may need to help minimize bus costs and delivery delays.\n##### (c) Report\nNot later than 18 months after the date of enactment of this Act, the Comptroller General shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the review conducted under this section.",
      "versionDate": "2025-07-16",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-10T16:50:12Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4447ih.xml"
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
      "title": "Transit Bus Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transit Bus Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General of the United States to conduct a review of the efficient use of funds in procuring new buses for transit service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:48:29Z"
    }
  ]
}
```
