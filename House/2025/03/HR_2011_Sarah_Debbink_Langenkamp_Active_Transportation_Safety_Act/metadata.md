# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2011?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2011
- Title: Sarah Debbink Langenkamp Active Transportation Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 2011
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-05-01T17:51:31Z
- Update date including text: 2026-05-01T17:51:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-10 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-10 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2011",
    "number": "2011",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "R000606",
        "district": "8",
        "firstName": "Jamie",
        "fullName": "Rep. Raskin, Jamie [D-MD-8]",
        "lastName": "Raskin",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Sarah Debbink Langenkamp Active Transportation Safety Act",
    "type": "HR",
    "updateDate": "2026-05-01T17:51:31Z",
    "updateDateIncludingText": "2026-05-01T17:51:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-10T22:06:13Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
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
      "sponsorshipDate": "2025-03-24",
      "state": "DC"
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "IN"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "WI"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "WI"
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
      "sponsorshipDate": "2025-08-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2011ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2011\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Raskin (for himself, Mr. Steil , Mr. Thompson of California , and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, with respect to the highway safety improvement program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sarah Debbink Langenkamp Active Transportation Safety Act .\n#### 2. Highway safety improvement program\n##### (a) Highway safety improvement project\nSection 148(a)(4)(B) of title 23, United States Code, is amended\u2014\n**(1)**\nin clause (xxix), by striking through (xxviii) and inserting through (xxx) ;\n**(2)**\nby redesignating clause (xxix) as clause (xxxi); and\n**(3)**\nby inserting after clause (xxviii) the following:\n(xxix) The connection of 2 or more segments of existing bicyclist or pedestrian infrastructure. (xxx) The reduction of safety risks to vulnerable road users through a project or strategy described in a program of projects or strategies developed pursuant to subsection (l)(2)(B). .\n##### (b) Federal share of certain highway safety improvement projects\n**(1) In general**\nSection 148(j) of title 23, United States Code, is amended\u2014\n**(A)**\nby striking Except as provided in sections 120 and 130 and inserting the following:\n(1) In general Except as provided in sections 120 and 130 and paragraph (2) ; and\n**(B)**\nby adding at the end the following:\n(2) Exception Notwithstanding any other provision of law, the Federal share of the cost of a highway safety improvement project carried out with funds apportioned to a State under section 104(b)(3) may be up to 100 percent if the project is a project described in clause (xxix) or (xxx) of subsection (a)(4)(B). .\n**(2) Flexible financing**\nSection 133(h)(7) of title 23, United States Code, is amended\u2014\n**(A)**\nby redesignating subparagraph (C) as subparagraph (E); and\n**(B)**\nby striking subparagraph (B) and inserting the following:\n(B) Flexible financing Notwithstanding section 120\u2014 (i) the non-Federal share for a project under this subsection may be calculated on a project, multiple-project, or program basis; and (ii) the Federal share of the cost of an individual project under this subsection may be up to 100 percent. (C) Treatment as non-Federal share Notwithstanding any other provision of law, funds made available to carry out section 148 may be credited toward the non-Federal share of the costs of a project under this subsection if\u2014 (i) the project includes a Proven Safety Countermeasure for bicyclists or pedestrians, as determined by the Federal Highway Administration; (ii) the relevant State strategic highway safety plan includes an emphasis area related to vulnerable road users; or (iii) the proposed project\u2014 (I) was described in a program of projects or strategies developed pursuant to paragraph section 148 (l); or (II) was identified by a local government, metropolitan planning organization, or regional transportation planning organization, including in a safety plan described in subparagraph (B), as addressing 1 or more areas of high risk to vulnerable road users during the consultation process required under paragraph (xx)(B) and through a planning process and data-based analysis. (D) Safety plans described A safety plan referred to in subparagraph (A)(ii)(II) is\u2014 (i) a pedestrian or bicyclist safety plan; (ii) a Complete Streets plan; (iii) a local roadway safety plan; (iv) a Vision Zero Action Plan; (v) a transition plan described in section 35.150(d) of title 28, Code of Federal Regulations (or successor regulations) (commonly known as an ADA Transition Plan ); (vi) a Tribal transportation safety plan; (vii) a comprehensive safety action plan (as defined in section 24112(a) of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 402 note; Public Law 117\u201358 )); or (viii) any other safety plan, as determined by the Secretary. .\n**(3) Increased Federal share for proven safety countermeasures**\nSection 120(c)(1) of title 23, United States Code, is amended, in the first sentence, by inserting Proven Safety Countermeasures for bicyclists or pedestrians (as determined by the Federal Highway Administration), before breakaway utility poles .",
      "versionDate": "2025-03-10",
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
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "944",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sarah Debbink Langenkamp Active Transportation Safety Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-26T15:19:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
    "originChamber": "House",
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
          "measure-id": "id119hr2011",
          "measure-number": "2011",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2026-05-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2011v00",
            "update-date": "2026-05-01"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sarah Debbink Langenkamp Active Transportation Safety Act</strong></p><p>This bill expands the Highway Safety Improvement Program (HSIP) to include additional bicyclist and pedestrian\u00a0safety measures and increases the federal cost share for certain safety projects.</p><p>Specifically, the bill allows HSIP to fund projects (1) for the connection of two or more segments of existing bicyclist or pedestrian infrastructure, or (2) that are based on a state's plan to improve the safety of vulnerable road users (e.g., bicyclists or pedestrians) in areas identified as high-risk. In addition, the bill allows an increased federal cost share of up to 100% for these projects.</p><p>The bill also allows an increased federal cost share of up to 100% for transportation projects that meet certain criteria, including\u00a0(1) the project includes a Federal Highway Administration Proven Safety Countermeasure for bicyclists or pedestrians (e.g., bicycle lanes, walkways, and crosswalk visibility enhancements), or (2) the relevant state strategic highway safety plan includes an emphasis area that is related to vulnerable road users.</p>"
        },
        "title": "Sarah Debbink Langenkamp Active Transportation Safety Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2011.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sarah Debbink Langenkamp Active Transportation Safety Act</strong></p><p>This bill expands the Highway Safety Improvement Program (HSIP) to include additional bicyclist and pedestrian\u00a0safety measures and increases the federal cost share for certain safety projects.</p><p>Specifically, the bill allows HSIP to fund projects (1) for the connection of two or more segments of existing bicyclist or pedestrian infrastructure, or (2) that are based on a state's plan to improve the safety of vulnerable road users (e.g., bicyclists or pedestrians) in areas identified as high-risk. In addition, the bill allows an increased federal cost share of up to 100% for these projects.</p><p>The bill also allows an increased federal cost share of up to 100% for transportation projects that meet certain criteria, including\u00a0(1) the project includes a Federal Highway Administration Proven Safety Countermeasure for bicyclists or pedestrians (e.g., bicycle lanes, walkways, and crosswalk visibility enhancements), or (2) the relevant state strategic highway safety plan includes an emphasis area that is related to vulnerable road users.</p>",
      "updateDate": "2026-05-01",
      "versionCode": "id119hr2011"
    },
    "title": "Sarah Debbink Langenkamp Active Transportation Safety Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sarah Debbink Langenkamp Active Transportation Safety Act</strong></p><p>This bill expands the Highway Safety Improvement Program (HSIP) to include additional bicyclist and pedestrian\u00a0safety measures and increases the federal cost share for certain safety projects.</p><p>Specifically, the bill allows HSIP to fund projects (1) for the connection of two or more segments of existing bicyclist or pedestrian infrastructure, or (2) that are based on a state's plan to improve the safety of vulnerable road users (e.g., bicyclists or pedestrians) in areas identified as high-risk. In addition, the bill allows an increased federal cost share of up to 100% for these projects.</p><p>The bill also allows an increased federal cost share of up to 100% for transportation projects that meet certain criteria, including\u00a0(1) the project includes a Federal Highway Administration Proven Safety Countermeasure for bicyclists or pedestrians (e.g., bicycle lanes, walkways, and crosswalk visibility enhancements), or (2) the relevant state strategic highway safety plan includes an emphasis area that is related to vulnerable road users.</p>",
      "updateDate": "2026-05-01",
      "versionCode": "id119hr2011"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2011ih.xml"
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
      "title": "Sarah Debbink Langenkamp Active Transportation Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sarah Debbink Langenkamp Active Transportation Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, with respect to the highway safety improvement program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:43Z"
    }
  ]
}
```
