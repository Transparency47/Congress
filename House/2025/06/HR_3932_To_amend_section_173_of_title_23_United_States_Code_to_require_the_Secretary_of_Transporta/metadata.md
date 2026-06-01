# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3932?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3932
- Title: Rural Upgrades for Road Access and Local Growth Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3932
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-07-15T08:05:24Z
- Update date including text: 2025-07-15T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-12 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-12 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3932",
    "number": "3932",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Rural Upgrades for Road Access and Local Growth Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-15T08:05:24Z",
    "updateDateIncludingText": "2025-07-15T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-12T20:49:27Z",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3932ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3932\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Ms. Scholten (for herself and Mr. Wied ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend section 173 of title 23, United States Code, to require the Secretary of Transportation to set aside certain amounts provided under the rural surface transportation grant program for regional hubs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Upgrades for Road Access and Local Growth Act of 2025 .\n#### 2. Rural surface transportation grant program\nSection 173 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (k)\u2014\n**(A)**\nby redesignating paragraph (4) as paragraph (5);\n**(B)**\nby inserting after paragraph (3) the following:\n(4) Regional hubs The Secretary shall reserve 30 percent of the amounts made available for the program for each fiscal year to provide grants for eligible projects located in communities with populations of between 10,000 and 75,000, whether or not 1 or more of such communities are considered part of an urbanized area as designated by the United States Census Bureau. ; and\n**(C)**\nin paragraph (5), as so redesignated, by striking or (3) and inserting (3), or (4) ; and\n**(2)**\nin subsection (l)\u2014\n**(A)**\nin paragraph (1) by striking 60 days and inserting 3 days ;\n**(B)**\nin paragraph (2) by striking 60-day period and inserting 3-day period ; and\n**(C)**\nin paragraph (3) by striking 60-day period and inserting 3-day period .",
      "versionDate": "2025-06-11",
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
        "updateDate": "2025-06-27T13:00:59Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3932ih.xml"
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
      "title": "Rural Upgrades for Road Access and Local Growth Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Upgrades for Road Access and Local Growth Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 173 of title 23, United States Code, to require the Secretary of Transportation to set aside certain amounts provided under the rural surface transportation grant program for regional hubs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:33:19Z"
    }
  ]
}
```
