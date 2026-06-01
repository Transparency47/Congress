# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4633
- Title: USPS Act
- Congress: 119
- Bill type: HR
- Bill number: 4633
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-10-25T08:05:43Z
- Update date including text: 2025-10-25T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4633",
    "number": "4633",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "USPS Act",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:43Z",
    "updateDateIncludingText": "2025-10-25T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:10:20Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MO"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TN"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4633ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4633\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Bost (for himself, Mr. Weber of Texas , Mr. Graves , and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 39, United States Code, to establish procedures for post offices that suspend operations due to an emergency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Upending Secret Postal Shutdowns Act or the USPS Act .\n#### 2. Post office emergency closure procedures\nSection 404 of title 39, United States Code, is amended by adding at the end the following:\n(f) (1) If any post office temporarily suspends operations due to an emergency\u2014 (A) on the first day of such suspension, the Postal Service shall place a sign or other physical notice of the suspension at the post office and publish a notice of the suspension on the Postal Service public website; and (B) not later than 5 days after the first date of such suspension, the Postal Service shall notify relevant public officials. (2) For purposes of paragraph (1)(B)\u2014 (A) the notice required under such paragraph shall include the reasons for the suspension, the interim solution for mail delivery, and expected end date of the suspension; and (B) the term relevant public officials means, with respect to a post office\u2014 (i) each Member of the House of Representatives (including a Delegate or Resident Commissioner to Congress) representing a congressional district which includes all or part of the geographic area served by such post office; (ii) each Senator representing a State which includes all or part of the geographic area served by such post office; and (iii) the head of each unit of local government with jurisdiction over all or part of the geographic area served by such post office. (3) (A) If a suspension of operations due to an emergency lasts for 30 days, the Postal Service shall open a 30-day public review period under which individuals served by the post office and or relevant public officials may provide comments to the Postal Service. (B) If a suspension of operations due to an emergency lasts for 60 days\u2014 (i) the Postal Regulatory Commission shall conduct a review of the suspension; and (ii) the Postal Service shall begin the process to relocate the operations of the suspended post office, consistent with the procedures for post office relocation under this title. (C) In carrying out any relocation under subparagraph (A)(ii), the Postal Service shall\u2014 (i) solicit input from the head of each unit local government with jurisdiction over all or part of the geographic area served by such post office; and (ii) open a 30-day public comment review period for a new proposed location. (4) In consultation with the Postmaster General, the postmaster for each post office shall promulgate and establish an action plan in the case of an emergency suspension of post office operations. (5) Not later than January 1 of each calendar year beginning with calendar year 2026 the Postal Service shall submit a report to Congress on emergency suspensions of operations of post offices during the most recently ended calendar year. Such report shall include, for each instance of an emergency suspension of operations of a post office, the location of the post office, the duration of the emergency suspension, and the reason for the emergency suspension. (6) In this subsection, the term emergency means a natural disaster, termination of a lease or rental agreement, lack of qualified personnel to operate the office, irreparable damage when no suitable alternate quarters are available in the community, severe damage to, or destruction of a post office, health and safety concerns, mold, challenges to the sanctity of the mail, or the lack of adequate measures to safeguard the post office or its revenue. .",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-09-17T21:58:37Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4633ih.xml"
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
      "title": "USPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Upending Secret Postal Shutdowns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 39, United States Code, to establish procedures for post offices that suspend operations due to an emergency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:26Z"
    }
  ]
}
```
