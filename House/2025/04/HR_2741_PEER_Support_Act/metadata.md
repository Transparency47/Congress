# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2741?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2741
- Title: PEER Support Act
- Congress: 119
- Bill type: HR
- Bill number: 2741
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-01-31T09:05:25Z
- Update date including text: 2026-01-31T09:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-08 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-08 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2741",
    "number": "2741",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001226",
        "district": "6",
        "firstName": "Andrea",
        "fullName": "Rep. Salinas, Andrea [D-OR-6]",
        "lastName": "Salinas",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "PEER Support Act",
    "type": "HR",
    "updateDate": "2026-01-31T09:05:25Z",
    "updateDateIncludingText": "2026-01-31T09:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
        "item": {
          "date": "2025-04-08T14:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-08T14:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "KS"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NJ"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "OR"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "TX"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NY"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "KS"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "TN"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "MN"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "WA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "VT"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "MA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "NY"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "GA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "OR"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
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
      "sponsorshipDate": "2026-01-30",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2741ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2741\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Ms. Salinas (for herself, Ms. Davids of Kansas , Mrs. Watson Coleman , Ms. Bonamici , and Mr. Doggett ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo address the behavioral health workforce shortages through support for peer support specialists, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Empathetic and Effective Recovery Support Act or the PEER Support Act .\n#### 2. Definition of peer support specialist\n##### (a) In general\nIn this Act, the term peer support specialist means an individual\u2014\n**(1)**\n**(A)**\nwho has lived experience of recovery from a mental health condition or substance use disorder and who specializes in supporting individuals with mental health conditions or substance use disorders; or\n**(B)**\nwho has lived experience as a parent or caregiver of an individual with a mental health condition or substance use disorder and who specializes in supporting families navigating mental health or substance use service systems; and\n**(2)**\nwho is certified as qualified to furnish peer support services, as described in subsection (b), under a process that is determined by the State in which such individual furnishes such services or determined appropriate by the Secretary of Health and Human Services.\n##### (b) Peer support services\nThe services described in this subsection shall be consistent with the National Practice Guidelines for Peer Supporters issued by the National Association of Peer Supporters (or a successor publication) and inclusive of the Core Competencies for Peer Workers in Behavioral Health Services of the Substance Abuse and Mental Health Services Administration.\n#### 3. Recognizing the peer support specialist profession\nNot later than January 1, 2026, the Director of the Office of Management and Budget shall revise the Standard Occupational Classification system to include an occupational category for peer support specialists.\n#### 4. Establishing the Office of Recovery\nPart A of title V of the Public Health Service Act ( 42 U.S.C. 290aa et seq. ) is amended by inserting after section 501C ( 42 U.S.C. 290aa\u20130b ) the following:\n501D. Office of Recovery (a) In general There is established, in the Substance Abuse and Mental Health Services Administration, an Office of Recovery (referred to in this section as the Office ). (b) Director The Office shall be headed by a Director who has demonstrated experience in, and lived experience with, mental health or substance use disorder recovery. (c) Responsibilities Through the Office of Recovery, the responsibilities of the Director shall include\u2014 (1) providing leadership in the identification of new and emerging issues related to recovery support services; (2) supporting technical assistance, data analysis, and evaluation functions in order to assist States, localities, territories, Indian Tribes, and Tribal organizations in developing recovery support services and identifying best practices with the objective of expanding the capacity of, and access to, recovery support services; (3) providing support for the training, education, integration, and professionalization of the peer support specialist workforce; (4) disseminating best practice recommendations with respect to peer support specialist training, certification, supervision, and practice to States and other entities that employ peer support specialists; (5) supporting peer support specialists with ongoing professional development and retention activities; and (6) developing recommendations on creating career pathways for peer support specialists. (d) Functions Beginning on the date of enactment of this section, the functions of the Office shall include the responsibilities described in subsection (c) and the functions of the Office of Recovery of the Substance Abuse and Mental Health Services Administration on the day before such date of enactment, including all of its personnel, assets, authorities, obligations, and liabilities, except as otherwise specified in this section. (e) Definition of peer support specialist In this section, the term peer support specialist has the meaning given such term in section 2 of the Providing Empathetic and Effective Recovery Support Act .\n#### 5. Research and recommendations on criminal background check process for peer support specialists\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in coordination with the Attorney General, shall develop a report on research and recommendations with respect to criminal background check processes for individuals becoming peer support specialists.\n##### (b) Contents\nThe report under subsection (a) shall include\u2014\n**(1)**\na summary of evidence-informed literature on the effectiveness of peer support specialists in improving the mental health and the substance use disorder recovery of other individuals;\n**(2)**\na survey of each State's laws (including regulations) that contain criminal background check requirements for serving as a peer support specialist, including\u2014\n**(A)**\nan analysis of criminal offenses that are included in State laws (including regulations) that prevent individuals from earning a peer support specialist certification or from practicing as a peer support specialist;\n**(B)**\nan analysis of requirements (if any) under the State plan under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) or under a waiver of such plan relating to background checks for providers participating under such plan or waiver and the extent to which any such requirements differ from similar requirements imposed under State law (including regulations);\n**(C)**\nan analysis of requirements (if any) of any State receiving a grant under part B of title XIX of the Public Health Service Act ( 42 U.S.C. 300x et seq. ) relating to background checks for providers participating in a program under, or otherwise providing services supported by, such grant;\n**(D)**\na review of State laws (including regulations) that provide exemptions from prohibitions regarding certification or practice of peer support specialists; and\n**(E)**\nan indication of each State that has gone through the process of amending or otherwise changing criminal background check laws (including regulations) for the certification and practice of peer support specialists; and\n**(3)**\nrecommendations to States on criminal background check processes that would reduce barriers to becoming certified as peer support specialists.\n##### (c) Availability\nNot later than 1 year after the date of enactment of this Act, the Secretary shall\u2014\n**(1)**\npost the report required under subsection (a) on the publicly accessible internet website of the Substance Abuse and Mental Health Services Administration; and\n**(2)**\ndistribute such report to\u2014\n**(A)**\nState agencies responsible for certification of peer support specialists;\n**(B)**\nthe Centers for Medicare & Medicaid Services;\n**(C)**\nState agencies responsible for carrying out a State plan under title XIX of the Social Security Act or under a waiver of such plan; and\n**(D)**\nState agencies responsible for carrying out a grant under part B of title XIX of the Public Health Service Act ( 42 U.S.C. 300x et seq. ).",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-04-08",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1329",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PEER Support Act",
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
        "name": "Health",
        "updateDate": "2025-05-15T15:49:18Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2741ih.xml"
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
      "title": "PEER Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T09:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PEER Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T09:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Empathetic and Effective Recovery Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T09:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address the behavioral health workforce shortages through support for peer support specialists, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T09:48:17Z"
    }
  ]
}
```
