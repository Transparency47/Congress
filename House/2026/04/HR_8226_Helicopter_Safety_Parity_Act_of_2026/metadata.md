# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8226
- Title: Helicopter Safety Parity Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8226
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-21T08:05:54Z
- Update date including text: 2026-04-21T08:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8226",
    "number": "8226",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000002",
        "district": "12",
        "firstName": "Jerrold",
        "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
        "lastName": "Nadler",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Helicopter Safety Parity Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-21T08:05:54Z",
    "updateDateIncludingText": "2026-04-21T08:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:34:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8226ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8226\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Nadler (for himself, Ms. Malliotakis , Mr. Menendez , Mr. Goldman of New York , and Mr. Espaillat ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish safety equipment, training, and maintenance requirements for turbine-powered helicopters carrying 2 or more passengers for compensation or hire, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helicopter Safety Parity Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCertain helicopter operators conduct passenger service under part 135 of title 14, Code of Federal Regulations, that is substantially similar to part 121 of such title scheduled passenger operations.\n**(2)**\nThese operations avoid the more rigorous standards for pilot training, duty and rest, maintenance, and equipment required under part 121 of such title.\n**(3)**\nThe Federal Aviation Administration has acknowledged this gap and proposed rulemaking to close it, but such rulemaking has not been finalized.\n**(4)**\nPublic safety requires that rotorcraft providing passenger service comply with standards equivalent to those governing airlines.\n**(5)**\nThis Act builds on, and does not duplicate, the requirements of the Federal Aviation Administration Safety Management System final rule issued in 2024.\n**(6)**\nA series of helicopter accidents in recent years, including fatal crashes involving tour operators, charter services, and air taxi operations, have revealed recurring issues with pilot fatigue, inadequate maintenance, and insufficient equipment, including the April 2025 Hudson River helicopter crash, which demonstrated that inadequate maintenance oversight under part 135 of title 14, Code of Federal Regulations, can contribute to catastrophic failures, highlighting the need for harmonized standards with part 121 of such title.\n#### 3. Definitions\nIn this Act:\n**(1) Part 121 operations**\nThe term part 121 operations means operations conducted under part 121 of title 14, Code of Federal Regulations.\n**(2) Part 121 operators**\nThe term part 121 operators means operators conducting part 121 operations.\n**(3) Part 135 operations**\nThe term part 135 operations means operations conducted under part 135 of title 14, Code of Federal Regulations.\n**(4) Part 135 operators**\nThe term part 135 operators means operators conducting part 135 operations.\n**(5) Rotorcraft**\nThe term rotorcraft has the meaning given that term in section 1.1 of title 14, Code of Federal Regulations.\n#### 4. Safety equipment and operational standards for helicopter operations\n##### (a) Applicability\nThis section applies to all turbine-powered helicopters carrying 2 or more passengers for compensation or hire.\n##### (b) Requirements\nOperators subject to subsection (a) shall comply with safety equipment, training, and maintenance requirements equivalent to those applicable to part 121 operations, including\u2014\n**(1)**\nequipment capable of providing terrain awareness, or equivalent technology approved by the Administrator;\n**(2)**\nequipment capable of cockpit voice recording, or equivalent technology approved by the Administrator;\n**(3)**\nequipment capable of flight data recording, or equivalent technology approved by the Administrator; and\n**(4)**\ncompliance with standards under part 121 of title 14, Code of Federal Regulations, for pilot qualification, duty and rest, and maintenance programs.\n##### (c) Compliance timeline\n**(1) In general**\nOperators subject to this section shall achieve full compliance not later than 24 months after the date of enactment of this Act.\n**(2) Extension**\nThe Administrator may grant an extension of up to 6 additional months upon a showing of good faith progress toward compliance.\n##### (d) Exception\nThis section shall not apply to operations conducted exclusively for emergency medical services under subpart L of part 135 of title 14, Code of Federal Regulations.\n#### 5. Rulemaking\n##### (a) Final rule\nNot later than 18 months after the date of enactment of this Act, the Administrator of the Federal Aviation Administration shall issue final regulations to carry out this Act.\n##### (b) Termination of inconsistent exemptions\nThe Administrator shall rescind or modify any exemptions, interpretations, or guidance inconsistent with this Act.\n#### 6. Enforcement\nAn operator that fails to comply with the requirements of this Act shall be subject to the same penalties, certificate actions, and enforcement measures applicable to violations by part 121 operators under chapter 447 of title 49, United States Code.\n#### 7. Authorization of appropriations\nThere are authorized to be appropriated to the Federal Aviation Administration $50,000,000 for each of fiscal years 2026 through 2030 to carry out the requirements of this Act, including rulemaking, enforcement, oversight, and the hiring and training of aviation safety inspectors to strengthen maintenance and operational surveillance of rotorcraft operators.\n#### 8. Implementation plan\nNot later than 12 months after the date of enactment of this Act, the Administrator of the Federal Aviation Administration shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report describing\u2014\n**(1)**\nstaffing needs for implementation of this Act;\n**(2)**\nsteps taken to hire and train additional aviation safety inspectors; and\n**(3)**\nprogress in integrating rotorcraft operators into oversight systems consistent with part 121 of title 14, Code of Federal Regulations.\n#### 9. Effective date\nThe requirements of this Act shall take effect on the date that is 2 years after the date of enactment of this Act.",
      "versionDate": "2026-04-09",
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
        "updateDate": "2026-04-17T18:51:53Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8226ih.xml"
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
      "title": "Helicopter Safety Parity Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T09:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helicopter Safety Parity Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T09:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish safety equipment, training, and maintenance requirements for turbine-powered helicopters carrying 2 or more passengers for compensation or hire, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T09:18:56Z"
    }
  ]
}
```
