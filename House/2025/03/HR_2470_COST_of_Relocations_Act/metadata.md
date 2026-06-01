# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2470
- Title: COST of Relocations Act
- Congress: 119
- Bill type: HR
- Bill number: 2470
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-05-27T08:06:19Z
- Update date including text: 2026-05-27T08:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2470",
    "number": "2470",
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
    "title": "COST of Relocations Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:19Z",
    "updateDateIncludingText": "2026-05-27T08:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:08:15Z",
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IN"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
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
      "sponsorshipDate": "2025-03-27",
      "state": "DC"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NV"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "WI"
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
      "sponsorshipDate": "2025-08-05",
      "state": "GA"
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
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MO"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-20",
      "state": "PR"
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
      "sponsorshipDate": "2026-04-22",
      "state": "WA"
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
      "sponsorshipDate": "2026-04-27",
      "state": "OH"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CT"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2470ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2470\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Subramanyam (for himself, Mr. Beyer , Mr. Carson , Mr. Connolly , Ms. Elfreth , Mr. Evans of Pennsylvania , Mr. Garcia of California , Mr. Hoyer , Mr. Ivey , Mr. Lynch , Mrs. McClain Delaney , Ms. Norton , Mr. Raskin , Mr. Scott of Virginia , Ms. Titus , Ms. Tlaib , and Mr. Vindman ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require Federal agencies to conduct a benefit-cost analysis on relocations involving the movement of employment positions to different areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Congressional Oversight to Secure Transparency of Relocations Act or the COST of Relocations Act .\n#### 2. Benefit-cost analysis on certain relocations\n##### (a) In general\nExcept as provided in subsection (d), a Federal agency may not carry out a covered relocation unless, prior to any submission to the Office of Management and Budget or other reviewing entity regarding such covered relocation\u2014\n**(1)**\nsuch agency\u2014\n**(A)**\nconducts a benefit-cost analysis on the covered relocation; and\n**(B)**\nsubmits to the Office of Inspector General for such agency an unredacted report on the findings of the benefit-cost analysis and including such other information such Office of Inspector General determines necessary for compliance with subsection (c); and\n**(2)**\nsuch Office of Inspector General reviews the report and submits to Congress the report described in subsection (c).\n##### (b) Benefit-Cost analysis\n**(1) In general**\nThe benefit-cost analysis described in subsection (a)(1) shall be conducted in a manner consistent with the economic and social science principles articulated in the guidance applicable to relocations in the Office of Management and Budget Circular A\u20134, as in effect on September 17, 2003.\n**(2) Analysis report**\n**(A) Contents**\nThe report described in subsection (a)(1)(B) shall include, at a minimum\u2014\n**(i)**\nthe anticipated outcomes and improvements that will result from the proposed covered relocation, quantified in monetary or other appropriate measures to the extent practicable;\n**(ii)**\nan explanation of how the proposed covered relocation will result in the anticipated outcomes and improvements;\n**(iii)**\nthe metrics for measuring whether the proposed covered relocation results in the anticipated outcomes and improvements;\n**(iv)**\na detailed employee engagement plan;\n**(v)**\na list of stakeholders;\n**(vi)**\na timeline of past and future engagements with stakeholders regarding the proposed covered relocation;\n**(vii)**\nan assessment of how the proposed covered relocation may affect stakeholders\u2014\n**(I)**\nserved by the positions affected by the covered relocation; and\n**(II)**\nin the destination agency or region;\n**(viii)**\na comprehensive strategy for accomplishing the proposed covered relocation that includes\u2014\n**(I)**\nstaffing, resourcing, and financial needs;\n**(II)**\nan implementation timeline identifying milestones and the persons accountable for meeting such milestones;\n**(III)**\na risk assessment;\n**(IV)**\na risk mitigation plan; and\n**(V)**\ndocumentation of ongoing succession and recruiting planning processes;\n**(ix)**\nan analysis of the effect the proposed covered relocation may have on the ability of the Federal agency to carry out its mission during the covered relocation and thereafter; and\n**(x)**\nan assessment of the short- and long-term effects of the covered relocation on the mission of the Federal agency.\n**(B) Publication**\nA Federal agency shall make publicly available the report described in subsection (a)(1)(B) in a form that excludes any proprietary information or trade secrets of any person and other confidential information.\n##### (c) Inspector General report to Congress\nNot later than 90 days after the date on which a Federal agency submits a report under subsection (a)(1)(B), the Office of Inspector General for that agency shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate, the Committee on Environment and Public Works of the Senate, the Committee on Oversight and Government Reform of the House of Representatives, and the Committee on Transportation and Infrastructure of the House of Representatives a report on the findings of the review conducted under subsection (a)(2), including\u2014\n**(1)**\ndetailed descriptions of the data used in the benefit-cost analysis described in subsection (a)(1), including the types of data and the time periods covered by the data;\n**(2)**\nthe conclusions of the benefit-cost analysis and the analysis underlying such conclusions; and\n**(3)**\na comprehensive assessment of\u2014\n**(A)**\nthe extent to which the Federal agency adhered to the guidance in the Office of Management and Budget Circular A\u20134, as in effect on September 17, 2003, in conducting the benefit-cost analysis, including a determination whether such adherence is sufficient to justify the use of Federal funds for the proposed covered relocation involved; and\n**(B)**\nif the proposed covered relocation involves moving positions from inside the National Capital Region to outside the National Capital Region, the extent to which real estate options in the National Capital Region were compared to those in the destination as part of that analysis.\n##### (d) Other requirements not abrogated\nNothing in this Act shall be construed to abrogate, reduce, or eliminate any requirements imposed by law pertaining to any covered relocation of a Federal agency or component of a Federal agency.\n##### (e) Definitions\nIn this Act:\n**(1) Administrative redelegation of function**\nThe term administrative redelegation of function means a Federal agency establishing new positions within the agency that replace existing positions within the agency and perform the functions of the positions replaced.\n**(2) Covered relocation**\nThe term covered relocation means\u2014\n**(A)**\nan administrative redelegation of function which, by itself or in conjunction with other related redelegations, involves replacing the existing positions of more than the lesser of 5 percent or 100 of the employees of the relevant Federal agency with new positions located outside the commuting area of such employees;\n**(B)**\nmoving a Federal agency or any component of a Federal agency if such move, by itself or in conjunction with other related moves, involves moving the positions of more than the lesser of 5 percent or 100 of the employees of the Federal agency outside the commuting area of such employees or under the jurisdiction of another Federal agency; or\n**(C)**\na combination of related redelegations and moves which together involve the positions of more than the lesser of 5 percent or 100 of the employees of the relevant Federal agency being moved to or replaced with new positions located outside the commuting area of such employees or moved under the jurisdiction of another Federal agency.\n**(3) Employee**\nThe term employee means an employee or officer of a Federal agency.\n**(4) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 902 of title 5, United States Code.\n**(5) National Capital Region**\nThe term National Capital Region has the meaning given such term in section 8702 of title 40, United States Code.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-27",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1171",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "COST of Relocations Act",
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
        "updateDate": "2025-05-20T18:12:10Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2470ih.xml"
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
      "title": "COST of Relocations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COST of Relocations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Oversight to Secure Transparency of Relocations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require Federal agencies to conduct a benefit-cost analysis on relocations involving the movement of employment positions to different areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:47Z"
    }
  ]
}
```
