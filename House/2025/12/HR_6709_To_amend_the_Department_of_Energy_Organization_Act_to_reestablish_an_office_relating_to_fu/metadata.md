# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6709?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6709
- Title: Office of Fusion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6709
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-03-04T09:06:24Z
- Update date including text: 2026-03-04T09:06:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6709",
    "number": "6709",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Office of Fusion Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:24Z",
    "updateDateIncludingText": "2026-03-04T09:06:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-15T17:02:50Z",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "FL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "OR"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6709ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6709\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Mr. Beyer (for himself, Mr. Obernolte , and Mrs. Trahan ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Department of Energy Organization Act to reestablish an office relating to fusion.\n#### 1. Short title\nThis Act may be cited as the Office of Fusion Act of 2025 .\n#### 2. Reestablishment of Department of Energy office relating to fusion\n##### (a) Office of Fusion\nTitle II of the Department of Energy Organization Act is amended by inserting after section 215 ( 42 U.S.C. 7144b ) the following:\n216. Office of Fusion (a) Establishment The Secretary shall establish the Office of Fusion (referred to in this section as the Office ) within the Department to advance near-term and long-term fusion energy science and technology to meet the energy, environmental, and economic needs of the United States. (b) Purposes The purposes of the Office shall be\u2014 (1) to enhance the economic and energy security of the United States; (2) to maintain United States leadership in fusion energy technologies; (3) to advance fusion energy, in partnership with the private sector, to accelerate research, development, demonstration, deployment, and market adoption of fusion technologies; (4) to manage public-private partnerships with the United States fusion industry to accelerate successful deployment of first commercial fusion power plants, with a goal to start construction of more than 1 private-sector fusion power plant not later than December 31, 2028; (5) to ensure an adequate national fusion supply chain infrastructure, including manufacturing capabilities; (6) to serve in a coordination role to align the capabilities of the Office of Science for basic research, the Advanced Research Projects Agency\u2014Energy for early technology development, and the National Nuclear Security Administration for fusion-relevant technologies to serve a single goal of accelerating commercial plant deployment while meeting high standards for safety; (7) to expand international fusion energy cooperation to support commercialization of fusion energy; (8) to ensure the availability of a well-trained workforce to support the fusion industry; (9) to provide technical expertise to regulators of fusion machines at the Federal, State, and international levels; and (10) to partner with other agencies to support programs and initiatives to facilitate international market opportunities for the United States commercial fusion industry. (c) Director The head of the Office shall be a Director selected by the Secretary. (d) Consolidation of fusion offices The Secretary shall\u2014 (1) transfer all programs previously stewarded by the Fusion Energy Sciences program of the Office of Science as of November 19, 2025, to the Office; and (2) develop a timeline for transferring the programs identified under paragraph (1). (e) Consultation In carrying out the duties of the Office, the Director shall consult with the private sector, National Laboratories, institutions of higher education, and the public as to how to optimize the organization of the various programs within the Department. (f) Fusion demonstration program vision (1) In general Not later than one year after the date of enactment of the Office of Fusion Act of 2025 , the Secretary and the Director shall submit to Congress a commercial deployment roadmap that\u2014 (A) identifies key barriers; and (B) describes specific activities to overcome those barriers and meet key deployment milestones, including activities such as early-stage technology development, regulatory streamlining, demonstration projects, and supply chain manufacturing. (2) Periodic report The Secretary and the Director shall submit to Congress an updated roadmap under paragraph (1)\u2014 (A) every 4 years; or (B) appended to another periodic energy report, as determined by the Secretary and the Director. (g) Coordination and Nonduplication (1) In general To the maximum extent practicable, the Director shall ensure that the activities of the Office are coordinated with, and do not duplicate the efforts of, other programs and laboratories within the Department and other relevant research agencies. (2) Technology transfer coordination To the extent appropriate, the Director may coordinate with the Chief Commercialization Officer appointed under section 1001(a)(4) of the Energy Policy Act of 2005 ( 42 U.S.C. 16391(a)(4) ). .\n##### (b) Fusion energy under Assistant Secretary\nSection 203(a)(2) of the Department of Energy Organization Act ( 42 U.S.C. 7133(a)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (C), (D), and (E) as subparagraphs (D), (E), and (F), respectively; and\n**(2)**\nby inserting after subparagraph (B) the following:\n(C) fusion energy resources; .\n##### (c) Clerical amendment\nThe table of contents for the Department of Energy Organization Act ( Public Law 95\u201391 ; 91 Stat. 565; 119 Stat. 764; 133 Stat. 2199) is amended by inserting after the item relating to section 215 the following:\nSec. 216. Office of Fusion. .",
      "versionDate": "2025-12-15",
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S8672)"
      },
      "number": "3437",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Office of Fusion Act of 2025",
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
        "name": "Energy",
        "updateDate": "2026-01-08T16:57:24Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6709ih.xml"
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
      "title": "Office of Fusion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:54:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Office of Fusion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:54:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Department of Energy Organization Act to reestablish an office relating to fusion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:48:42Z"
    }
  ]
}
```
