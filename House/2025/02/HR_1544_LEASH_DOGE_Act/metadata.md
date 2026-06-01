# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1544?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1544
- Title: LEASH DOGE Act
- Congress: 119
- Bill type: HR
- Bill number: 1544
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2025-07-17T19:29:53Z
- Update date including text: 2025-07-17T19:29:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1544",
    "number": "1544",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "LEASH DOGE Act",
    "type": "HR",
    "updateDate": "2025-07-17T19:29:53Z",
    "updateDateIncludingText": "2025-07-17T19:29:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:01:40Z",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MO"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "DC"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "LA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CT"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NJ"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "FL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NV"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "OR"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "MI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1544ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1544\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Subramanyam (for himself, Mr. Cleaver , Ms. Norton , Mr. Jackson of Illinois , Ms. Jacobs , Mr. Grijalva , Mr. Fields , Mr. Larson of Connecticut , Ms. Tlaib , Mrs. Watson Coleman , Mr. Krishnamoorthi , Ms. Lois Frankel of Florida , and Mr. Huffman ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct the head of the Department of Government Efficiency to submit a report to Congress on the personnel of the Department and present information to Congress on the activities carried out by the Department, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Legislative Enforcement Against Setbacks from Harmful DOGE Actions Act or the LEASH DOGE Act .\n#### 2. Requiring provision of information on employees and activities of Department of Government Efficiency\n##### (a) Report\nThe head of the United States DOGE Service (commonly referred to as the Department of Government Efficiency or DOGE ) shall submit a report to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate containing the following information:\n**(1)**\nA list of\u2014\n**(A)**\nall employees of the Department, including special Government employees, and a description of each employee\u2019s role; and\n**(B)**\nall employees of the Executive Office of the President, including any individual serving as a Senior Advisor to the President, whose duties include advising the President on the operations of the Department.\n**(2)**\nFor each such employee, a statement of whether the employee has undergone a background check and, if so, the results of the background check.\n**(3)**\nFor each such employee, a statement of whether the employee has a security clearance.\n**(4)**\nFor each such employee, a statement disclosing any conflict of interest held by the employee, including (if applicable) a description of a plan entered into by the employee to address such conflicts and the person with whom the employee entered into the plan.\n##### (b) Appearance at meetings of committees\n**(1) Appearance of head of DOGE required**\nThe head of DOGE and any Senior Advisor to the President described in subsection (a)(1)(B) shall appear at a closed meeting of the Committee on Oversight and Government Reform of the House of Representatives and a closed meeting of the Committee on Homeland Security and Governmental Affairs of the Senate to present information on the activities carried out by the Department as of the date of the meeting and on the activities the Department intends to carry out after such date.\n**(2) Information on access to personally identifiable information**\nThe head of DOGE and any Senior Advisor to the President described in subsection (a)(1)(B) shall include in the information presented at a meeting under this subsection a description of the extent to which employees of DOGE have obtained access to computer systems of the Federal Government, along with a description of the types of personally identifiable information contained in such systems for which such employees have obtained access.\n##### (c) Public website on DOGE information\n**(1) Establishment and operation**\nThe head of DOGE shall establish and operate a public website through which members of the public may obtain the following information in human-readable form:\n**(A)**\nA list of employees of DOGE, include special Government employees, their titles, and a description of their role in DOGE.\n**(B)**\nThe number of employees laid off and put on administrative leave within each office of the Federal Government.\n**(C)**\nA list of programs and activities within each office of the Government for which funding has been reduced, and the amount by which such funding has been reduced.\n**(D)**\nA list of programs and activities within each office of the Government for which funding has been paused, and a timeline on when a final decision will be made regarding that funding.\n**(E)**\nA list of programs and activities within each office of the Government for which funding has been eliminated.\n**(F)**\nA list of individuals, including their contact information, whom Federal employees, recipients of Federal financial assistance, and members of the public may contact with questions about the status of Federal personnel and Federal financial assistance.\n**(2) Updates**\nThe head of DOGE shall update the information provided on the website under this subsection not less frequently than once per week.\n#### 3. Treatment of employees of DOGE Agency Teams\n##### (a) Treatment as employee of DOGE\nFor purposes of this Act, an employee of an agency who serves on the DOGE Agency Team of the agency in accordance with section 3(c) of Executive Order 14158 shall be considered an employee of DOGE.\n##### (b) Provision of information\nThe head of each agency for which a DOGE Agency Team has been established in accordance with such Executive Order shall provide the head of DOGE with such information as may be necessary for the head of DOGE to carry out the requirements of this Act.\n#### 4. Deadlines; restrictions on use of funds\n##### (a) Deadlines\nNot later than March 31, 2025, the head of DOGE shall submit the report required under section 2(a), appear at meetings under section 2(b), and operate the public website under section 2(c).\n##### (b) Restrictions on use of funds\nIf the head of DOGE fails to comply with subsection (a)\u2014\n**(1)**\nany funds appropriated or otherwise made available for the Department of Government Efficiency, including amounts previously available for the United States Digital Service, may be used only to carry out activities initiated prior to January 20, 2025; and\n**(2)**\nno Federal funds may be used for any DOGE Agency Team established in accordance with section 3(c) of Executive Order 14158,\nuntil the head of DOGE submits the report required under section 2(a), appears at meetings under section 2(b), and operates the public website under section 2(c).",
      "versionDate": "2025-02-24",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T19:29:20Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-07-17T19:29:39Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-17T19:29:48Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-17T19:29:44Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-07-17T19:29:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-09T15:38:55Z"
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
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1544ih.xml"
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
      "title": "LEASH DOGE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LEASH DOGE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Legislative Enforcement Against Setbacks from Harmful DOGE Actions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the head of the Department of Government Efficiency to submit a report to Congress on the personnel of the Department and present information to Congress on the activities carried out by the Department, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:43Z"
    }
  ]
}
```
