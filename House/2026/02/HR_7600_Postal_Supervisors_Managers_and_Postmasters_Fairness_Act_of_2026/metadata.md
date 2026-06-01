# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7600?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7600
- Title: Postal Supervisors, Managers, and Postmasters Fairness Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7600
- Origin chamber: House
- Introduced date: 2026-02-17
- Update date: 2026-05-30T08:06:02Z
- Update date including text: 2026-05-30T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-17: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-02-17: Introduced in House

## Actions

- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-17",
    "latestAction": {
      "actionDate": "2026-02-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7600",
    "number": "7600",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000831",
        "district": "11",
        "firstName": "James",
        "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
        "lastName": "Walkinshaw",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Postal Supervisors, Managers, and Postmasters Fairness Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:02Z",
    "updateDateIncludingText": "2026-05-30T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-17",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-17",
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
          "date": "2026-02-17T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "IL"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "ME"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MN"
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
      "sponsorshipDate": "2026-03-26",
      "state": "VA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "DC"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "GA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "IN"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NH"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "DE"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "PA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MI"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7600ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7600\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 17, 2026 Mr. Walkinshaw (for himself and Mr. Bost ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 39, United States Code, to modify procedures for negotiating pay and benefits of supervisory and other managerial personnel of the United States Postal Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Postal Supervisors, Managers, and Postmasters Fairness Act of 2026 .\n#### 2. Negotiation of pay and benefits programs for Postal Service supervisory and managerial personnel positions\n##### (a) In general\nSubsection (e) of section 1004 of title 39, United States Code, is amended to read as follows:\n(e) (1) Not later than 60 days before the date on which a Postal Service pay decision under this section regarding pay policies and schedules and fringe benefit programs is scheduled to expire, the Postal Service shall provide a written proposal to the supervisors\u2019 organization and the postmasters\u2019 organization for any changes in pay policies and schedules and fringe benefit programs for members represented by the supervisors\u2019 organization and the postmasters\u2019 organization for a covered period. (2) Not later than 60 days after the date an agreement is reached on a collective bargaining agreement between the Postal Service and a bargaining representative recognized under section 1203 of this title that affects any matter (including the supervisory differential) concerning supervisor, manager, and postmaster pay policies and schedules and fringe benefit programs, the Postal Service shall provide a written proposal regarding the matters so affected to the supervisors\u2019 organization and the postmasters\u2019 organization for any changes in pay policies and schedules and fringe benefit programs covering members represented by the supervisors\u2019 organization and the postmasters\u2019 organization. (3) The Postal Service, the supervisors\u2019 organization, and the postmasters\u2019 organization shall strive to resolve any differences concerning the proposal described in paragraph (1) or (2) under the procedures provided for, or adopted under, subsection (d). .\n##### (b) Modification of dispute resolution\nParagraph (5) of section 1004(f) of title 39, United States Code, is amended to read as follows:\n(5) Not more than 15 days after the panel has made its recommendation and considered input from the Postal Service, the supervisors\u2019 organization, and the postmasters\u2019 organization pursuant to paragraph (4), the panel shall issue its final determination for pay policies and schedules and fringe benefit programs. Such final determination shall be binding upon the Postal Service, the supervisors\u2019 organization, and the postmasters\u2019 organization. .",
      "versionDate": "2026-02-17",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-27T16:46:45Z"
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
      "date": "2026-02-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7600ih.xml"
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
      "title": "Postal Supervisors, Managers, and Postmasters Fairness Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Postal Supervisors, Managers, and Postmasters Fairness Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 39, United States Code, to modify procedures for negotiating pay and benefits of supervisory and other managerial personnel of the United States Postal Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T09:18:40Z"
    }
  ]
}
```
