# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2098
- Title: Deliver for Democracy Act
- Congress: 119
- Bill type: HR
- Bill number: 2098
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-12-16T09:05:37Z
- Update date including text: 2025-12-16T09:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2098",
    "number": "2098",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "A000055",
        "district": "4",
        "firstName": "Robert",
        "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
        "lastName": "Aderholt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Deliver for Democracy Act",
    "type": "HR",
    "updateDate": "2025-12-16T09:05:37Z",
    "updateDateIncludingText": "2025-12-16T09:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:00:45Z",
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
      "sponsorshipDate": "2025-03-14",
      "state": "MO"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NC"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MN"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "SC"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "OK"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MS"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "WI"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MD"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2098ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2098\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Aderholt (for himself, Mr. Cleaver , Mr. Johnson of Georgia , Mr. Davis of North Carolina , Mrs. Cherfilus-McCormick , Ms. Tenney , Ms. Craig , Mr. Wilson of South Carolina , Mr. Carter of Georgia , Mr. Cole , Mr. Costa , Mrs. Foushee , Mr. Lawler , and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require on-time delivery of periodicals to unlock additional rate authority, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deliver for Democracy Act .\n#### 2. Additional rate authority for periodicals\nNot later than 1 year after the date of enactment of this Act, the Postal Regulatory Commission shall amend section 3030.222 of title 39, Code of Federal Regulations, to provide that, for any fiscal year ending after the date of enactment of this Act, the Commission shall not authorize the United States Postal Service any additional rate authority with respect to periodicals under that section for the following fiscal year, unless the Commission determines that the United States Postal Service achieved\u2014\n**(1)**\na 95 percent on-time delivery performance for periodicals during the fiscal year of the determination, as measured by the service standards in effect on the date of enactment of this Act; or\n**(2)**\nan increase in the on-time delivery performance for periodicals during the fiscal year of the determination, as measured by the service standards in effect on the date of enactment of this Act, of not less than 2 percentage points, as compared to the on-time delivery performance percentage in the fiscal year before, on, or after the date of enactment of this Act in which the on-time delivery performance percentage is the highest measured, as measured by such service standards.\n#### 3. Annual progress report\n##### (a) Report required\n**(1) In general**\nSubject to subsections (c) and (d), the Postmaster General shall submit to the Postal Regulatory Commission and make publicly available an annual report on the progress of the United States Postal Service in including in the periodical service performance measurements of the Postal Service on-time performance data for in-county and out-of-county newspaper mail that is entered and accepted at each delivery unit for delivery.\n**(2) Stakeholder input**\nIn carrying out the report requirement under paragraph (1), the Postmaster General shall solicit feedback from relevant stakeholders.\n##### (b) Implementation of report requirement\nIf the relevant information is not available for each individually addressed piece of mail for purposes of a report required under subsection (a), the Postal Regulatory Commission, in consultation with the Postmaster General, shall develop a system for generating service performance data for use in the report by producing digital information for relevant mail bundles.\n##### (c) Termination of report requirement\nThe Postmaster General shall submit and make publicly available the report described in subsection (a) annually until the date on which the Postal Regulatory Commission determines that the United States Postal Service has incorporated the categories of mail described in subsection (a), or any other relevant mail categories used in the report in accordance with subsection (d), into the existing applicable service performance measurements.\n##### (d) Proxy information\n**(1) In general**\nIf the Postal Regulatory Commission and the Postmaster General jointly determine that identifying newspaper mail within the periodicals mail category is not practicable for purposes of a report under subsection (a), the Postal Regulatory Commission may determine what information with respect to the closest relevant mail category the Postmaster General may use in the report.\n**(2) Public report on determination**\nIf the Postal Regulatory Commission and the Postmaster General make the determination described in paragraph (1), the Postal Regulatory Commission and the Postmaster General shall make publicly available a report describing the process and rationale for the determination, including a description of\u2014\n**(A)**\nthe potential costs for the United States Postal Service and applicable businesses resulting from the report requirement under subsection (a);\n**(B)**\nthe ability of the Postmaster General to ascertain accurate results for inclusion in the report under subsection (a); and\n**(C)**\nany other factor contributing to the determination.\n#### 4. GAO study and report\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study of alternative pricing schemes and other options for the United States Postal Service that would improve the financial position of periodicals and other products that do not cover their costs and evaluate the potential impact of such alternative pricing schemes and other options.\n##### (b) Report\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Accountability of the House of Representatives a report on the study conducted under subsection (a).",
      "versionDate": "2025-03-14",
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
        "actionDate": "2025-03-12",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1002",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Deliver for Democracy Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T17:56:09Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2098ih.xml"
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
      "title": "Deliver for Democracy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deliver for Democracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require on-time delivery of periodicals to unlock additional rate authority, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:37Z"
    }
  ]
}
```
