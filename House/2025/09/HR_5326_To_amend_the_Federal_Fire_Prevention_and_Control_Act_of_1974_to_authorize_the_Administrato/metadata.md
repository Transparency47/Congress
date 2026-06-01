# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5326?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5326
- Title: FLAME Act
- Congress: 119
- Bill type: HR
- Bill number: 5326
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-26T15:35:02Z
- Update date including text: 2025-09-26T15:35:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5326",
    "number": "5326",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "M001232",
        "district": "6",
        "firstName": "April",
        "fullName": "Rep. McClain Delaney, April [D-MD-6]",
        "lastName": "McClain Delaney",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "FLAME Act",
    "type": "HR",
    "updateDate": "2025-09-26T15:35:02Z",
    "updateDateIncludingText": "2025-09-26T15:35:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MO"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "OR"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IN"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MN"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MO"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "KS"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "LA"
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
      "sponsorshipDate": "2025-09-11",
      "state": "MD"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "OH"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MD"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CO"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MD"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5326ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5326\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mrs. McClain Delaney (for herself, Mr. Bell , Ms. Bonamici , Mr. Carson , Ms. Craig , Mr. Cleaver , Ms. Davids of Kansas , Mr. Fields , Mr. Hoyer , Mr. Krishnamoorthi , Mr. Landsman , Ms. Lofgren , Mr. Min , Mr. Mfume , Mr. Neguse , Mr. Raskin , and Mr. Stanton ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the Federal Fire Prevention and Control Act of 1974 to authorize the Administrator of the United States Fire Administration to cancel or delay certain courses and programs offered by the Academy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Firefighter Learning And Management Education Act or the FLAME Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe National Academy for Fire Prevention and Control (in this section referred to as the Academy ) of the United States Fire Administration, and the Emergency Management Institute, are located at the National Emergency Training Center in Emmitsburg, Maryland.\n**(2)**\nCongress directed the establishment of the Academy in accordance with section 7 of the Federal Fire Prevention and Control Act of 1974 ( 15 U.S.C. 2206 ) to advance the professional development of fire service personnel .\n**(3)**\nThe Academy is the American fire service war college and provides critical training and education programs for our nation\u2019s first responders.\n**(4)**\nTens of thousands of career and volunteer firefighters from departments across the country benefit from courses at the Academy annually.\n**(5)**\nIn 2017, an overwhelming majority of students at the Academy reported that their coursework helped improve their individual skills and enhanced their local fire department\u2019s readiness.\n**(6)**\nIn fiscal year 2023, more than 40,000 firefighters participated in courses with the Academy. After participating in these courses, 90 percent of supervisors shared that their firefighters were better prepared to respond to emergencies as a result of their training at the Academy.\n**(7)**\nAt a time when wildfires have ravaged\u2014and continue to threaten\u2014communities across the nation, the collaboration and education managed by the Academy has never been more important to secure the future of fire services.\n**(8)**\nGiven the importance of the programs at the Academy, it is critical to clarify the authority of the Academy to cancel courses and programming, and to require proper notice be given to Congress before any large-scale closures happen.\n#### 3. Authorization to cancel or delay certain courses and programs offered by the National Academy for Fire Prevention and Control\n##### (a) Powers of Administrator of the United States Fire Administration relating to large-Scale cancellation actions; congressional review\nSection 7 of the Federal Fire Prevention and Control Act of 1974 ( 15 U.S.C. 2206 ) is amended\u2014\n**(1)**\nby redesignating subsection (n) as subsection (r); and\n**(2)**\nby inserting after subsection (m) the following new subsections:\n(n) Large-Scale cancellation action (1) In general The Administrator is authorized to implement a large-scale cancellation action relating to a covered course or program. (2) Notice to Congress Not later than 60 days before the date on which the Administrator implements a large-scale cancellation action pursuant to paragraph (1), or in the event of an exigent circumstance, as soon as practicable thereafter, the Administrator shall submit to Congress a notice that includes the following: (A) An identification of the covered courses or programs to be cancelled. (B) An identification of the fire departments and agencies with personnel registered for the covered courses or programs to be cancelled. (C) The total number of personnel registered for the covered courses or programs to be cancelled, disaggregated by the number of such personnel in each of such fire departments or agencies. (D) A justification for each such cancellation. (3) Notice to students If the Administrator implements under paragraph (1) a large-scale cancellation action relating to a covered course or program, the Administrator, not later than 45 days before the intended start date of such course or program, or in the event of an exigent circumstance, as soon as practicable thereafter, shall inform each student enrolled in such covered course or program, and the fire chief or other appropriate head of each fire department of such students, of such cancellation. (o) Other cancellation If the Superintendent cancels a covered course or program, the Superintendent, not later than 30 days before the intended start date of such course or program, or in the event of an exigent circumstance, as soon as practicable thereafter, shall inform each student enrolled in such covered course or program, and the fire chief or other appropriate head of each fire department of such students, of such cancellation. (p) Reimbursement of certain expenses (1) In general Not later than 90 days after the Administrator of FEMA receives an itemization under paragraph (3) from a fire department relating to a covered course or program that is cancelled, the Administrator of FEMA, subject to paragraph (2), shall reimburse such fire department for any covered expense related to such course or program. (2) Good cause A reimbursement under paragraph (1) shall not apply with respect to a covered course or program that is cancelled if such covered course or program is cancelled for good cause. (3) Itemization of expenses Not later than 30 days after the intended start date of the course or program that was cancelled, the fire chief or other appropriate head of a fire department affected by such cancellation may submit to the Administrator of FEMA an application for reimbursement that includes an itemization of each covered expense such fire department incurred. (q) Definitions In this section: (1) Backfill expense The term backfill expense means an expense incurred for the following: (A) Staffing adjustments. (B) Overtime compensation. (2) Covered course or program The term covered course or program means a course or program that is offered by the Academy\u2014 (A) in-person and on-campus; (B) in-person and off-campus; or (C) through synchronous or asynchronous virtual instruction. (3) Covered expense The term covered expense means any expense that a fire department incurred for the planned participation of the personnel of such fire department in a covered course or program, including the following: (A) Any travel expense. (B) Any backfill expense. (4) Good cause The term good cause includes the following: (A) The closure of a facility of the Academy. (B) The illness or unavailability of an instructor of the Academy. (C) A national emergency that impedes access to a facility of the Academy by a student or faculty member of the Academy. (5) Large-scale cancellation action The term large-scale cancellation action means an action taken by the Administrator whereby the Administrator cancels at one time at least 25 percent of the total number of covered courses or programs planned to be offered by the Academy in a fiscal year. .\n##### (b) GAO study\n**(1) In general**\nNot later than March 30, 2026, the Comptroller General of the United States shall submit to the Committee on Science, Space, and Technology and the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a study that includes the matters specified in paragraph (2).\n**(2) Matters specified**\nThe matters specified in this paragraph are the following:\n**(A)**\nAny impact of any large-scale cancellation action by the National Academy for Fire Prevention and Control during calendar year 2025 of covered courses or programs (as such terms are defined in subsection (r) of section 7 of the Federal Fire Prevention and Control Act of 1974 ( 15 U.S.C. 2206 ) as added by subsection (b)) offered by the Academy on the preparedness of fire departments for a national emergency.\n**(B)**\nAny negative consequences of such cancellations.\n**(C)**\nHow the National Academy for Fire Prevention and Control contributes to establishing a common approach, including interoperability of fire and emergency response, for firefighters and first responders to provide mutual aid and combat fires, natural disasters, medical emergencies, and other similar events, and the value of such common approach.\n**(D)**\nThe number of students who have attended a course or program at the National Academy for Fire Prevention and Control during the immediately preceding 3 calendar years, disaggregated by the following:\n**(i)**\nAny such courses or programs that are offered in-person and at the National Academy for Fire Prevention and Control campus.\n**(ii)**\nAny such courses or programs that are offered in-person and not at the National Academy for Fire Prevention and Control campus.\n**(iii)**\nAny such courses or program that are offered by synchronous virtual instruction.\n**(iv)**\nAny such courses or program that are offered by asynchronous virtual instruction.\n**(E)**\nAn identification and description of the most in-demand courses.",
      "versionDate": "2025-09-11",
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
        "name": "Emergency Management",
        "updateDate": "2025-09-26T15:35:02Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5326ih.xml"
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
      "title": "FLAME Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T03:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FLAME Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Firefighter Learning And Management Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Fire Prevention and Control Act of 1974 to authorize the Administrator of the United States Fire Administration to cancel or delay certain courses and programs offered by the Academy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T03:48:19Z"
    }
  ]
}
```
