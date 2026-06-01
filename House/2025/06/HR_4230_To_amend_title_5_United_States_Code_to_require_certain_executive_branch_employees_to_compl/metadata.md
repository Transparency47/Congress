# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4230
- Title: the Appropriations Compliance and Training Act
- Congress: 119
- Bill type: HR
- Bill number: 4230
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2025-09-09T16:04:44Z
- Update date including text: 2025-09-09T16:04:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-27 - IntroReferral: Sponsor introductory remarks on measure. (CR E629)
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-27 - IntroReferral: Sponsor introductory remarks on measure. (CR E629)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4230",
    "number": "4230",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000009",
        "district": "9",
        "firstName": "Marcy",
        "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
        "lastName": "Kaptur",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "the Appropriations Compliance and Training Act",
    "type": "HR",
    "updateDate": "2025-09-09T16:04:44Z",
    "updateDateIncludingText": "2025-09-09T16:04:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
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
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E629)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:04:15Z",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CT"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MD"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "GA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MN"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "ME"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "WI"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NJ"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "HI"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "PA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "TX"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "IN"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MD"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "SC"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4230ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4230\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Ms. Kaptur (for herself, Ms. DeLauro , Mr. Hoyer , Mr. Bishop , Ms. McCollum , Ms. Wasserman Schultz , Ms. Pingree , Ms. Meng , Mr. Pocan , Ms. Lois Frankel of Florida , Mrs. Watson Coleman , Mrs. Torres of California , Mr. Case , Mr. Morelle , Mr. Levin , Ms. Dean of Pennsylvania , Ms. Escobar , Mr. Mrvan , and Mr. Ivey ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to require certain executive branch employees to complete annual training on appropriations law, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Appropriations Compliance and Training Act .\n#### 2. Mandatory appropriations law training\n##### (a) In general\nChapter 41 of title 5, United States Code, is amended by inserting after section 4105 the following new section (and conforming the table of contents at the beginning of such chapter accordingly):\n4106. Mandatory appropriations law training (a) Training (1) In general The head of each agency shall require any employee occupying a covered position at the agency to complete an annual training course on appropriations law. (2) Timing With respect to any employee occupying a covered position on the date of the enactment of this section, such training shall be completed not later than 1 year after such date and annually thereafter. With respect to any individual appointed to a covered position after such date of enactment, such training shall be completed not later than 60 days after such appointment and annually thereafter. (b) Course requirements (1) In general For purposes of carrying out the requirements of this section, the head of each agency shall\u2014 (A) use the appropriations law training course offered by the Government Accountability Office; (B) establish an appropriations law training course within the agency; or (C) use an appropriations law training course offered by any other agency or contractor. (2) Requirements If the head of an agency establishes a training course under paragraph (1)(B) or uses a training course offered by an agency or contractor under paragraph (1)(C), such course may not be implemented or used without prior approval of the Director of the Office of Management and Budget and the Comptroller General. Any such course shall at a minimum provide training on the following: (A) The constitutional and statutory framework governing the obligation and expenditure of appropriated funds, including the role of Congress and its power of the purse, the role of the Office of Management and Budget, and the role of executive agencies in the appropriations process; (B) Section 1301 of title 31 (commonly referred to as the Purpose Statute ). (C) Sections 1341, 1342, and 1511 through 1519 of title 31 (commonly referred to as the Antideficiency Act ). (D) The bona fide needs rule, including section 1502 of title 31. (E) The Impoundment Control Act of 1974 (parts A and B of title X of the Congressional Budget and Impoundment Control Act of 1974). (F) A comprehensive review of the direction provided in the current fiscal year\u2019s appropriation Act and accompanying report or explanatory statement (if any) relevant to the employing agency. (G) All possible penalties an employee may be subject to for violating appropriations law. (H) Any other relevant statutory or regulatory provisions concerning the proper use of appropriated funds. (c) Certification The head of each agency shall submit an annual report to the Office of Management and Budget listing each employee who has completed such training. The head shall make a permanent notation in the employee's official personnel record file each time such employee completes such training. (b) Noncompliance (1) In general If an employee fails to complete the required training under this section, after 45 days of noncompliance\u2014 (A) such employee\u2014 (i) shall be suspended from supervisory authority over budget execution or financial decision making, including obligation of funds; and (ii) may not, nowithstanding any other provision of law, receive any performance bonus or increase in basic rate of pay; and (B) the head of the agency shall place a notation of such noncompliance in the employee\u2019s official personnel record file. (2) Additional penalties If an employee remains in noncompliance after 60 days, such employee shall be suspended from accessing any agency information technology systems and computer networks, including email and financial management systems, until the employee completes the required training under this section. (c) Agency accountability The head of each agency shall be responsible for ensuring each employee occupying a covered position is in compliance with this section. Not later than 1 year after the date of the enactment of this section and annually thereafter, the head of each agency shall publish, on the agency\u2019s public website, statistics regarding compliance by such employees with the training required by this section. (d) Definition of covered position In this section, the term covered position means\u2014 (1) any position within the executive branch of the Government that is classified at or above grade 11 of the General Schedule (or equivalent); (2) any political position (as that term is defined in section 4(a) of Public Law 114\u2013136 ); and (3) any Senior Executive Service position (as that term is defined in section 3132(a)). .\n##### (b) Implementation\n**(1) Guidance**\nNot later than 90 days after the date of the enactment of this Act, the Director of the Office of Personnel Management, in consultation with the Comptroller General, shall issue implementation guidance and maintain a list of approved providers of training required by section 4106 of title 5, United States Code (as added by subsection (a)).\n**(2) Agency compliance plans**\nNot later than 120 days after the date of the enactment of this Act, the head of each executive branch agency shall submit to the Office of Management and Budget a plan for implementing the training required by such section 4106.",
      "versionDate": "2025-06-27",
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
        "updateDate": "2025-09-09T16:04:44Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4230ih.xml"
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
      "title": "the Appropriations Compliance and Training Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T06:13:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "the Appropriations Compliance and Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-17T06:13:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to require certain executive branch employees to complete annual training on appropriations law, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T06:08:49Z"
    }
  ]
}
```
