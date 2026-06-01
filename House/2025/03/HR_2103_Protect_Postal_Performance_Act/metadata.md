# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2103?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2103
- Title: Protect Postal Performance Act
- Congress: 119
- Bill type: HR
- Bill number: 2103
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-05-30T08:05:34Z
- Update date including text: 2026-05-30T08:05:34Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2103",
    "number": "2103",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001315",
        "district": "13",
        "firstName": "Nikki",
        "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
        "lastName": "Budzinski",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Protect Postal Performance Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:34Z",
    "updateDateIncludingText": "2026-05-30T08:05:34Z"
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
          "date": "2025-03-14T13:04:10Z",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "WY"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "ME"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NH"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MN"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "TN"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CO"
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
      "sponsorshipDate": "2025-08-15",
      "state": "NY"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "KS"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MO"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "WA"
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
      "sponsorshipDate": "2026-03-24",
      "state": "GA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MN"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "ME"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-06",
      "state": "VA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "DE"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CT"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MI"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "PA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2103ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2103\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Ms. Budzinski (for herself, Ms. Hageman , Mr. Golden of Maine , Mr. Bergman , and Mr. Pappas ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo modify the procedures used by the United States Postal Service for the closure or consolidation of any post office or any processing and distribution center, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Postal Performance Act .\n#### 2. Limitation on closure and consolidations of post offices\nSection 404(d) of title 39, United States Code, is amended\u2014\n**(1)**\nin paragraph (4)\u2014\n**(A)**\nby striking The Postal Service and insert (A) The Postal Service ; and\n**(B)**\nby adding at the end the following:\n(B) During such 60-day period, the Postal Service shall carry out a public hearing on the closure or consolidation, which may be attended in-person or virtually by any members of the public affected by the closure or consolidation. (C) Not later than 7 days after such hearing, the Postal Service shall publish a summary of the hearing on the Postal Service\u2019s public website, and include in such summary a description of any comments made or otherwise submitted at such hearing and the percentage of such comments that were in support or against the closure or consolidation. (D) Notwithstanding any other provision of this title, the applicable post office may not be closed or consolidated until the date that is 180 days after the date the summary is published under subparagraph (C). ; and\n**(2)**\nby adding at the end the following:\n(7) Notwithstanding any other provision of this title, a post office may not be closed or consolidated if such post office\u2014 (A) is not located within 15 miles of any other post office; or (B) is the closest post office for a population of 15,000 individuals or more. .\n#### 3. Postal Service processing and distribution centers; transportation optimization\n##### (a) In general\nChapter 4 of title 39, United States Code, is amended by adding after section 416 the following:\n417. Postal Service processing and distribution centers (a) In general The United States Postal Service may not close, consolidate, downgrade, or take any other similar action with respect to any processing and distribution center in a State if such action would result in no such center being located in that State in any geographically non-contiguous region of that State inhabited by more than 100,000 permanent residents. In this subsection, the term geographically non-contiguous region means an area of a State that is physically separated from the main body of the State by a significant body of water or land controlled by another State. (b) Limitation on changes to mail processing facilities (1) In general Notwithstanding any other provision of law, the Postal Service may not implement or otherwise carry out any changes to the operations of its mail processing facilities (including consolidation or partial consolidation, aggregation of processing, distribution, or delivery operations) until on or after the date that the Postal Regulatory Commission issues an advisory opinion on the proposed facility changes. (2) Deadline The Postal Regulatory Commission shall issue the advisory opinion required under paragraph (1) not later than 120 business days after the date the Postal Service submits to the Commission a proposed change to any such facility. (3) Other requirements The Commission shall issue an advisory opinion for each processing and distribution center at which the Postal Service has proposed changes, downsizing, and consolidations. (4) Report If an advisory opinion by the Commission under this subsection determines that a proposed change will lead to slower on-time mail delivery, the Postal Service shall publish a report on the Postal Service\u2019s public website on practices and procedures the Postal Service will implement to ensure mail delivery remains on time. No such changes may be implemented or otherwise carried out for the period of 180 days beginning on the date such report is so published. (c) Prohibiting on carrying out mail processing facility review Notwithstanding any other provision of law, the Postal Service may not carry out the United States Postal Service Mail Processing Facility Review (or any successor program), and no Federal funds (including amounts in the Postal Service Fund under section 2003) may be obligated or expended to carry out such Review. (d) Limitation of the closure of processing and distribution centers in regions that are not meeting on-Time delivery benchmarks During any calendar year, the Postal Service may not close, consolidate, or otherwise move any operations or services from any processing and distribution center located within any Postal Service district that, during anytime within the immediately preceding calendar year, failed to meet\u2014 (1) at least 93 percent on-time delivery rate for two-day single first-class mail; and (2) at least 90.3 percent on-time delivery rate for three to five-day first-class mail. (e) Definitions In this section\u2014 (1) the term processing and distribution center means a central mail facility that\u2014 (A) distributes and dispatches part or all of both incoming mail and outgoing mail for a designated service area; (B) provides instructions on the preparation of collection mail, dispatch schedules, and sorting plan requirements to mailers; and (C) is a sectional center facility, a general mail facility, or a dedicated mail processing facility without a station or branch; and (2) the term State means the 50 States and the District of Columbia. 418. Local transportation optimization and regional transportation optimization changes (a) In general The Postal Service may not implement or otherwise carry out any local transportation optimization (in this section referred to as LTO ) and regional transportation optimization (in this section referred to as RTO ) efforts that will decrease the number of times mail is either picked up or dropped off for any post office in the country. (b) PRC opinion The Postal Service may not proceed with changing drop off and pick up schedules at post offices as part of the LTO or RTO plans without requesting a Postal Regulatory Commission opinion. (c) Limitation If the Postal Regulatory Commission does not recommend implementing these changes in an opinion under subsection (b), the Postal Service may not move forward with LTO or RTO optimization efforts anywhere in the United States. .\n##### (b) Clerical amendment\nThe table of sections for such chapter is amended by adding after the item relating to section 416 the following:\n417. Postal Service processing and distribution centers. 418. Local transportation optimization and regional transportation optimization changes. .",
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
        "actionDate": "2026-01-15",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3657",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Postal Performance Act",
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
        "updateDate": "2025-05-20T17:57:05Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2103ih.xml"
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
      "title": "Protect Postal Performance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T14:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Postal Performance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T14:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify the procedures used by the United States Postal Service for the closure or consolidation of any post office or any processing and distribution center, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T14:18:39Z"
    }
  ]
}
```
