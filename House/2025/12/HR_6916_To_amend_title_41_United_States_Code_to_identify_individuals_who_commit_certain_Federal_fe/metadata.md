# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6916?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6916
- Title: Federal Program Integrity and Fraud Prevention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6916
- Origin chamber: House
- Introduced date: 2025-12-19
- Update date: 2026-05-18T15:28:10Z
- Update date including text: 2026-05-18T15:28:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-19: Introduced in House
- 2025-12-19 - IntroReferral: Introduced in House
- 2025-12-19 - IntroReferral: Introduced in House
- 2025-12-19 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 38 - 2.
- Latest action: 2025-12-19: Introduced in House

## Actions

- 2025-12-19 - IntroReferral: Introduced in House
- 2025-12-19 - IntroReferral: Introduced in House
- 2025-12-19 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 38 - 2.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-19",
    "latestAction": {
      "actionDate": "2025-12-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6916",
    "number": "6916",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Federal Program Integrity and Fraud Prevention Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-18T15:28:10Z",
    "updateDateIncludingText": "2026-05-18T15:28:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 38 - 2.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-19",
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
      "actionDate": "2025-12-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-19",
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
        "item": [
          {
            "date": "2026-03-18T13:01:55Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-19T19:30:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6916ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6916\nIN THE HOUSE OF REPRESENTATIVES\nDecember 19, 2025 Mr. Self (for himself and Ms. Randall ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 41, United States Code, to identify individuals who commit certain Federal felonies implicating Federal programs as an excluded source on the System for Award Management Exclusions list, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Program Integrity and Fraud Prevention Act of 2025 .\n#### 2. Exclusion of Felony Fraud Convicts to Protect Federal Funds\n##### (a) Procurement integrity\nChapter 47 of title 41, United States Code, is amended by adding at the end the following new section:\n4715. Protecting Federal funds from individuals convicted of certain Federal felonies (a) Prohibition (1) In general Except as provided in subsection (b), an individual who is convicted of a covered felony arising out of any agency contract, grant, cooperative agreement, loan, or other financial assistance shall be identified as an excluded source on the System for Award Management Exclusions list described in part 9 of title 48, Code of Federal Regulations, and part 180 of title 2 of such Code, or successor regulations. (2) Notification of conviction For each individual convicted of a covered felony, the Attorney General shall notify the Administrator of General Services in a timely manner of such conviction and the Administrator shall promptly enter the 3-year prohibition for such person into the System for Award Management, or any successor system. (b) Waiver Notwithstanding subsection (a), the agency head may exempt an individual described in subsection (a)(1) from the prohibition under such subsection for a case in which the agency head determines in writing that the exemption is warranted. The agency head shall transmit a copy of each such written exemption to Congress immediately after making such determination. (c) Definitions In this section: (1) Agency The term agency means an Executive department (as defined under section 101 of title 5), a military department (as defined under section 102 of title 5), a Government corporation (as defined under section 103 of title 5), and an independent establishment (as defined under section 104(1) of title 5). (2) Convicted The term convicted means\u2014 (A) a judgment of conviction has been entered against the individual by a Federal court; (B) there has been a finding of guilt against the individual by a Federal court; (C) a plea of guilty or nolo contendere by the individual has been accepted by a Federal court; or (D) the individual has entered into a first offender, deferred adjudication, deferred prosecution, or other arrangement or program in which judgment or conviction has been withheld. (3) Covered felony The term covered felony means a felony described under section 286, 287, 371, 641, 666, 1001, 1014, 1017, 1028, 1028A, 1030, 1031, 1040(a)(2), 1341, 1343, 1344, 1345, 1349, 1956, and 1957 of title 18 and section 16 of the Small Business Act ( 15 U.S.C. 645 ). (d) Rules of construction (1) Federal interests Nothing in this section may be construed to prohibit an agency from seeking or taking any other available criminal, civil, or administrative action to protect Federal Government interests, including the proposal or implementation of suspension or debarment actions pursuant to subpart 9.4 of title 48, Code of Federal Regulations, and part 180 of title 2 of such Code. (2) Exclusion Nothing in subsection (b) may be construed to affect any other statutory or regulatory waiver authority related to an exclusion. .\n##### (b) Clerical amendment\nThe table of sections for chapter 47 of title 41, United States Code, is amended by adding at the end the following:\n4715. Protecting Federal funds from individuals convicted of certain Federal felonies. .\n#### 3. Guidance\nNot later than 1 year after the date of the enactment of this Act, the Attorney General, in consultation with the Administrator of General Services, shall issue guidance for the implementation of, and compliance with, the requirements of section 4715 of title 41, United States Code, as added by section 2.",
      "versionDate": "2025-12-19",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal justice information and records",
            "updateDate": "2026-05-18T15:28:10Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-05-18T15:28:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-23T14:44:53Z"
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
      "date": "2025-12-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6916ih.xml"
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
      "title": "To amend title 41, United States Code, to identify individuals who commit certain Federal felonies implicating Federal programs as an excluded source on the System for Award Management Exclusions list, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-23T07:54:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Program Integrity and Fraud Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T06:38:21Z"
    },
    {
      "title": "Federal Program Integrity and Fraud Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-23T06:38:21Z"
    }
  ]
}
```
