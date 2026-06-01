# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3087?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3087
- Title: Civil Rights Cold Case Records Collection Reauthorization Act
- Congress: 119
- Bill type: HR
- Bill number: 3087
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2026-05-22T08:07:37Z
- Update date including text: 2026-05-22T08:07:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 36 - 4.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 36 - 4.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3087",
    "number": "3087",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Civil Rights Cold Case Records Collection Reauthorization Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:37Z",
    "updateDateIncludingText": "2026-05-22T08:07:37Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 36 - 4.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
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
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
            "date": "2026-05-20T13:22:34Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-29T14:02:00Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-06-10",
      "state": "DC"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "LA"
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
      "sponsorshipDate": "2025-06-13",
      "state": "GA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "PA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "IL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CT"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "MI"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "OH"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "PA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
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
      "sponsorshipDate": "2025-11-12",
      "state": "GA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "PR"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "IL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MS"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3087ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3087\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mrs. Watson Coleman (for herself, Mr. Lawler , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend the Civil Rights Cold Case Records Collection Act of 2018 to strengthen the powers of the Civil Rights Cold Case Records Review Board, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Civil Rights Cold Case Records Collection Reauthorization Act .\n#### 2. Clarifying the Authorities of the Civil Rights Cold Case Review Board\n##### (a) Civil Rights Cold Case Records Review Board presumption of release\nIt is the sense of Congress that all records of the Federal Government and State and local governments concerning civil rights cold cases should\u2014\n**(1)**\ncarry a presumption of immediate disclosure; and\n**(2)**\neventually be disclosed to enable the public to become fully informed about the history surrounding the cases.\n##### (b) Reimbursement for expenses incurred by State or local governments\nSection 3 of the Civil Rights Cold Case Records Collection Act of 2018 ( 44 U.S.C. 2107 note; Public Law 115\u2013426 ) is amended by adding at the end the following:\n(i) Reimbursement for expenses incurred by State or local governments Upon request of a State or local government to the Review Board, the Review Board may reimburse the State or local government in full for any expense incurred by the State or local government for digitizing, photocopying, or mailing a civil rights cold case record for the purpose of transmitting such record to the Archivist for inclusion in the Collection. .\n##### (c) Transmission to Collection of civil rights cold case records in possession of State or local government\nSection 3(a)(2)(A)(i) of the Civil Rights Cold Case Records Collection Act of 2018 ( 44 U.S.C. 2107 note; Public Law 115\u2013426 ) is amended by striking , except in the case of a State or local government .\n##### (d) No application of section 552(b)(6) to civil rights cold case records on or before January 1, 1990\nSection 9(a)(2) of the Civil Rights Cold Case Records Collection Act of 2018 ( 44 U.S.C. 2107 note; Public Law 115\u2013426 ) is amended by striking the period at the end and inserting , except in the case of information contained in a civil rights cold case record created on or before January 1, 1990. .\n#### 3. Civil Rights Cold Case Records Review Board Extension of Tenure\nSection 5(n)(1) of Civil Rights Cold Case Records Collection Act of 2018 ( 44 U.S.C. 2107 note; Public Law 115\u2013426 ) is amended\u2014\n**(1)**\nby striking 7 years and inserting 11 years ; and\n**(2)**\nby striking 7-year period and inserting 11-year period .",
      "versionDate": "2025-04-29",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-16",
        "actionTime": "12:21:39",
        "text": "Held at the desk."
      },
      "number": "1510",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Civil Rights Cold Case Records Collection Reauthorization Act",
      "type": "S"
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
            "name": "Advisory bodies",
            "updateDate": "2025-12-17T19:24:46Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-12-17T19:24:46Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-12-17T19:24:46Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-17T19:24:46Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-12-17T19:24:46Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-12-17T19:24:46Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-12-17T19:24:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-05-21T13:10:13Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3087ih.xml"
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
      "title": "Civil Rights Cold Case Records Collection Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Civil Rights Cold Case Records Collection Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Civil Rights Cold Case Records Collection Act of 2018 to strengthen the powers of the Civil Rights Cold Case Records Review Board, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:26Z"
    }
  ]
}
```
