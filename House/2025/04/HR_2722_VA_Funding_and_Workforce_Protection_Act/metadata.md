# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2722?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2722
- Title: VA Funding and Workforce Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2722
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-05-21T08:08:41Z
- Update date including text: 2026-05-21T08:08:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2722",
    "number": "2722",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000402",
        "district": "26",
        "firstName": "Timothy",
        "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
        "lastName": "Kennedy",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "VA Funding and Workforce Protection Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:41Z",
    "updateDateIncludingText": "2026-05-21T08:08:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
            "date": "2026-05-20T13:27:55Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:47:10Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-04-08T14:06:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MI"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "OH"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "IL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CO"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "IL"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "GA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NJ"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "IL"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "AL"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "TX"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NV"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "GA"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MN"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "OH"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2722ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2722\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Kennedy of New York (for himself, Ms. Norton , Mr. Thanedar , Mrs. Dingell , Ms. Tlaib , Mr. Landsman , Ms. Ocasio-Cortez , Mrs. Ramirez , Mr. Neguse , Mr. Davis of Illinois , Mr. Mannion , Ms. Vel\u00e1zquez , Ms. Williams of Georgia , Mrs. McIver , Ms. Budzinski , Mr. Ruiz , Ms. Sewell , and Ms. Crockett ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo limit the deferral or transfer of Federal funds made available to the Department of Veterans Affairs, to limit layoffs and other personnel actions at the Department, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Funding and Workforce Protection Act .\n#### 2. Limitation on deferral or transfer of Federal funds made available for Department of Veterans Affairs\n##### (a) In general\nNotwithstanding any other provision of law, including the Impoundment Control Act of 1974, discretionary appropriations made available for the Department of Veterans Affairs (in this Act referred to as the Department ), including the Veterans Health Administration, may not be impounded, transferred, or reprogrammed unless specific statutory authority is enacted into law after the date of the enactment of this Act, with express reference to this Act, permitting such impoundment, transfer, or reprogramming.\n##### (b) Notification\nThe Secretary of the Department of Veterans Affairs (in this Act referred to as the Secretary ) shall notify the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate if the Secretary determines that the Department is within 30 days of having a shortfall of funding.\n#### 3. Personnel requirements for Department of Veterans Affairs\n##### (a) Exemption from hiring freeze\nThe Department shall be exempt from any hiring freeze issued by the President, the Secretary, or the Director of the Office of Personnel Management during the period beginning on January 20, 2025, and ending on January 20, 2029.\n##### (b) Reinstatement of veterans\nWith respect to any veteran (as that term is defined in section 101 of title 38, United States Code) who was a career employee of the Department and whom the Secretary removed from employment with the Department during the period beginning on January 20, 2025, and ending on the date of the enactment of this Act, the Secretary shall\u2014\n**(1)**\nreinstate such veteran to the position (or equivalent position) such veteran occupied on the date that is one day before the date of removal; and\n**(2)**\nexempt such veteran from separation under any reduction in force that occurs before January 20, 2029.\n##### (c) Limitation on layoffs\n**(1) In general**\nThe Secretary shall submit written notice, to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate, not later than 15 days before the date that the Department will remove any officer or employee under a reduction in force or an agency reorganization.\n**(2) Probationary employees**\n**(A) In general**\nNotwithstanding any other provision of law, no employee of the Department in probationary status may be removed from a position at the Department without the enactment into law after the date of the enactment of this section, with express reference to this section, permitting such removal.\n**(B) Notification**\nThe Secretary shall submit to Congress\u2014\n**(i)**\non the date the Secretary removes a probationary employee for poor performance, a report that includes the reasons for the removal, the employee\u2019s most recent performance appraisal, and the removal notice submitted to the employee; and\n**(ii)**\nnot later than 30 days after the date of the enactment of this Act and every 30 days thereafter, a list of any probationary employees at the Department that received a removal notice during the period covered by the report.\n#### 4. Certification of compliance\nNot later than 30 days after the date of the enactment of this Act, and annually thereafter, the Secretary shall certify (in writing), to the Committees on Appropriations of the House of Representatives and the Senate and the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate, that the Secretary is in compliance with the requirements of this Act.",
      "versionDate": "2025-04-08",
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
            "updateDate": "2026-04-06T15:51:20Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2026-04-06T15:51:11Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2026-04-06T15:51:24Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2026-04-06T15:51:15Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-04-06T15:50:44Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2026-04-06T15:51:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T18:33:36Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2722ih.xml"
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
      "title": "VA Funding and Workforce Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T10:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Funding and Workforce Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T10:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the deferral or transfer of Federal funds made available to the Department of Veterans Affairs, to limit layoffs and other personnel actions at the Department, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T10:03:23Z"
    }
  ]
}
```
