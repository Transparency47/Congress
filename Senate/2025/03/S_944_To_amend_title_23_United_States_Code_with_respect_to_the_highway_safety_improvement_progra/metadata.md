# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/944?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/944
- Title: Sarah Debbink Langenkamp Active Transportation Safety Act
- Congress: 119
- Bill type: S
- Bill number: 944
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-05-01T18:35:47Z
- Update date including text: 2026-05-01T18:35:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/944",
    "number": "944",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Sarah Debbink Langenkamp Active Transportation Safety Act",
    "type": "S",
    "updateDate": "2026-05-01T18:35:47Z",
    "updateDateIncludingText": "2026-05-01T18:35:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-03-11T19:54:53Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-11T19:54:53Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TN"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MD"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "OR"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "RI"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "GA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "DE"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s944is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 944\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Van Hollen (for himself, Mr. Johnson , Ms. Baldwin , Mr. Hagerty , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title 23, United States Code, with respect to the highway safety improvement program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sarah Debbink Langenkamp Active Transportation Safety Act .\n#### 2. Highway safety improvement program\n##### (a) Highway safety improvement project\nSection 148(a)(4)(B) of title 23, United States Code, is amended\u2014\n**(1)**\nin clause (xxix), by striking through (xxviii) and inserting through (xxx) ;\n**(2)**\nby redesignating clause (xxix) as clause (xxxi); and\n**(3)**\nby inserting after clause (xxviii) the following:\n(xxix) The connection of 2 or more segments of existing bicyclist or pedestrian infrastructure. (xxx) The reduction of safety risks to vulnerable road users through a project or strategy described in a program of projects or strategies developed pursuant to subsection (l)(2)(B). .\n##### (b) Federal share of certain highway safety improvement projects\n**(1) In general**\nSection 148(j) of title 23, United States Code, is amended\u2014\n**(A)**\nby striking Except as provided in sections 120 and 130 and inserting the following:\n(1) In general Except as provided in sections 120 and 130 and paragraph (2) ; and\n**(B)**\nby adding at the end the following:\n(2) Exception Notwithstanding any other provision of law, the Federal share of the cost of a highway safety improvement project carried out with funds apportioned to a State under section 104(b)(3) may be up to 100 percent if the project is a project described in clause (xxix) or (xxx) of subsection (a)(4)(B). .\n**(2) Flexible financing**\nSection 133(h)(7) of title 23, United States Code, is amended\u2014\n**(A)**\nby redesignating subparagraph (C) as subparagraph (E); and\n**(B)**\nby striking subparagraph (B) and inserting the following:\n(B) Flexible financing Notwithstanding section 120\u2014 (i) the non-Federal share for a project under this subsection may be calculated on a project, multiple-project, or program basis; and (ii) the Federal share of the cost of an individual project under this subsection may be up to 100 percent. (C) Treatment as non-Federal share Notwithstanding any other provision of law, funds made available to carry out section 148 may be credited toward the non-Federal share of the costs of a project under this subsection if\u2014 (i) the project includes a Proven Safety Countermeasure for bicyclists or pedestrians, as determined by the Federal Highway Administration; (ii) the relevant State strategic highway safety plan includes an emphasis area related to vulnerable road users; or (iii) the proposed project\u2014 (I) was described in a program of projects or strategies developed pursuant to section 148(l); or (II) was identified by a local government, metropolitan planning organization, or regional transportation planning organization, including in a safety plan described in subparagraph (D), as addressing 1 or more areas of high risk to vulnerable road users during the consultation process required under section 148(l)(4)(B) and through a planning process and data-based analysis. (D) Safety plans described A safety plan referred to in subparagraph (C)(iii)(II) is\u2014 (i) a pedestrian or bicyclist safety plan; (ii) a Complete Streets plan; (iii) a local roadway safety plan; (iv) a Vision Zero Action Plan; (v) a transition plan described in section 35.150(d) of title 28, Code of Federal Regulations (or successor regulations) (commonly known as an ADA Transition Plan ); (vi) a Tribal transportation safety plan; (vii) a comprehensive safety action plan (as defined in section 24112(a) of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 402 note; Public Law 117\u201358 )); or (viii) any other safety plan, as determined by the Secretary. .\n**(3) Increased Federal share for proven safety countermeasures**\nSection 120(c)(1) of title 23, United States Code, is amended, in the first sentence, by inserting Proven Safety Countermeasures for bicyclists or pedestrians (as determined by the Federal Highway Administration), before breakaway utility poles .",
      "versionDate": "2025-03-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-10",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "2011",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sarah Debbink Langenkamp Active Transportation Safety Act",
      "type": "HR"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-31T15:35:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s944",
          "measure-number": "944",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-05-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s944v00",
            "update-date": "2026-05-01"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Sarah Debbink Langenkamp Active Transportation Safety Act</strong></p><p>This bill expands the Highway Safety Improvement Program (HSIP) to include additional bicyclist and pedestrian\u00a0safety measures and increases the federal cost share for certain safety projects.</p><p>Specifically, the bill allows HSIP to fund projects (1) for the connection of two or more segments of existing bicyclist or pedestrian infrastructure, or (2) that are based on a state's plan to improve the safety of vulnerable road users (e.g., bicyclists or pedestrians) in areas identified as high-risk. In addition, the bill allows an increased federal cost share of up to 100% for these projects.</p><p>The bill also allows an increased federal cost share of up to 100% for transportation projects that meet certain criteria, including\u00a0(1) the project includes a Federal Highway Administration Proven Safety Countermeasure for bicyclists or pedestrians (e.g., bicycle lanes, walkways, and crosswalk visibility enhancements), or (2) the relevant state strategic highway safety plan includes an emphasis area that is related to vulnerable road users.</p>"
        },
        "title": "Sarah Debbink Langenkamp Active Transportation Safety Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s944.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sarah Debbink Langenkamp Active Transportation Safety Act</strong></p><p>This bill expands the Highway Safety Improvement Program (HSIP) to include additional bicyclist and pedestrian\u00a0safety measures and increases the federal cost share for certain safety projects.</p><p>Specifically, the bill allows HSIP to fund projects (1) for the connection of two or more segments of existing bicyclist or pedestrian infrastructure, or (2) that are based on a state's plan to improve the safety of vulnerable road users (e.g., bicyclists or pedestrians) in areas identified as high-risk. In addition, the bill allows an increased federal cost share of up to 100% for these projects.</p><p>The bill also allows an increased federal cost share of up to 100% for transportation projects that meet certain criteria, including\u00a0(1) the project includes a Federal Highway Administration Proven Safety Countermeasure for bicyclists or pedestrians (e.g., bicycle lanes, walkways, and crosswalk visibility enhancements), or (2) the relevant state strategic highway safety plan includes an emphasis area that is related to vulnerable road users.</p>",
      "updateDate": "2026-05-01",
      "versionCode": "id119s944"
    },
    "title": "Sarah Debbink Langenkamp Active Transportation Safety Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sarah Debbink Langenkamp Active Transportation Safety Act</strong></p><p>This bill expands the Highway Safety Improvement Program (HSIP) to include additional bicyclist and pedestrian\u00a0safety measures and increases the federal cost share for certain safety projects.</p><p>Specifically, the bill allows HSIP to fund projects (1) for the connection of two or more segments of existing bicyclist or pedestrian infrastructure, or (2) that are based on a state's plan to improve the safety of vulnerable road users (e.g., bicyclists or pedestrians) in areas identified as high-risk. In addition, the bill allows an increased federal cost share of up to 100% for these projects.</p><p>The bill also allows an increased federal cost share of up to 100% for transportation projects that meet certain criteria, including\u00a0(1) the project includes a Federal Highway Administration Proven Safety Countermeasure for bicyclists or pedestrians (e.g., bicycle lanes, walkways, and crosswalk visibility enhancements), or (2) the relevant state strategic highway safety plan includes an emphasis area that is related to vulnerable road users.</p>",
      "updateDate": "2026-05-01",
      "versionCode": "id119s944"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s944is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Sarah Debbink Langenkamp Active Transportation Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sarah Debbink Langenkamp Active Transportation Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 23, United States Code, with respect to the highway safety improvement program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:15Z"
    }
  ]
}
```
