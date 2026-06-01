# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1870?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1870
- Title: SPEED for BEAD Act
- Congress: 119
- Bill type: HR
- Bill number: 1870
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-02-02T19:47:39Z
- Update date including text: 2026-02-02T19:47:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1870",
    "number": "1870",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "SPEED for BEAD Act",
    "type": "HR",
    "updateDate": "2026-02-02T19:47:39Z",
    "updateDateIncludingText": "2026-02-02T19:47:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:06:20Z",
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
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "OH"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
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
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "ID"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "IN"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "SC"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "ND"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NC"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "TX"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "VA"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NC"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1870ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1870\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Hudson (for himself, Mr. Allen , Mr. Latta , Mr. Bilirakis , Mr. Carter of Georgia , Mr. Dunn of Florida , Mr. Joyce of Pennsylvania , Mr. Fulcher , Mr. Pfluger , Mrs. Cammack , Mr. Obernolte , Mrs. Houchin , Mr. Fry , Mr. Goldman of Texas , and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to improve the Broadband Equity, Access, and Deployment Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Program Efficiency and Expanding Deployment for BEAD Act or the SPEED for BEAD Act .\n#### 2. Grants for broadband deployment\n##### (a) Eligible community anchor institution\nSection 60102(a)(1)(E) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(a)(1)(E) ) is amended\u2014\n**(1)**\nby striking The term and inserting the following:\n(i) In general The term ; and\n**(2)**\nby adding at the end the following:\n(ii) Gigabit-level broadband service In this subparagraph, the term gigabit-level broadband service means reliable broadband service offered with download speeds of not less than 1,000 megabits per second. .\n##### (b) Program name\nSection 60102 of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702 ) is amended\u2014\n**(1)**\nin subsection (a)(2)(J), by striking Equity and inserting Expansion ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by striking Equity and inserting Expansion ; and\n**(B)**\nin paragraph (1), by striking Equity and inserting Expansion .\n##### (c) Funds usage\n**(1) Failure to use full allocation**\nSection 60102(c)(5)(C)(ii) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(c)(5)(C)(ii) ) is amended by striking deadline, the Assistant Secretary and all that follows through the end and inserting deadline, the Assistant Secretary shall transfer the unused amounts to the general fund of the Treasury. .\n**(2) Use of funds**\nSection 60102(f) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(f) ) is amended\u2014\n**(A)**\nin paragraph (4)(B), by striking the semicolon and inserting ; and ; and\n**(B)**\nby striking paragraphs (5) and (6) and inserting the following:\n(5) telecommunications workforce development programs. .\n##### (d) Project size reform\nSection 60102(g)(2) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(g)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end;\n**(2)**\nin subparagraph (C), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(D) if the eligible entity awards a subgrant on the basis of a project area defined by the eligible entity, incorporate a mechanism\u2014 (i) for a prospective subgrantee to remove from such project area a location that the prospective subgrantee determines would unreasonably increase costs or is otherwise necessary to remove; and (ii) to award a subgrant for any location removed pursuant to clause (i). .\n##### (e) Prohibition on certain conditions\nSection 60102(g) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(g) ) is amended by adding at the end the following:\n(4) Prohibition on certain conditions Neither the Assistant Secretary nor an eligible entity may establish or enforce, with respect to a process of bidding, a grant, or a subgrant under this section, a condition or other requirement, including a reporting requirement or bid scoring component or preference, of such process of bidding, grant, or subgrant (without regard to whether such condition or other requirement was approved as part of the initial proposal, or any other portion of the application process, of such eligible entity) that relates to\u2014 (A) prevailing wages or compliance with subchapter IV of chapter 31 of title 40, United States Code; (B) project labor agreements; (C) union workforces; (D) collective bargaining; (E) local hiring; (F) commitment to union neutrality; (G) labor peace agreements; (H) workforce composition or reporting of workforce composition; (I) climate change; (J) regulation of network management practices, including data caps; (K) open access; (L) a letter of credit from a subgrantee that\u2014 (i) has commercially deployed or operated a broadband network using technologies that are the same or similar to the technologies relevant to such process of bidding, grant, or subgrant; and (ii) is seeking\u2014 (I) funding in an amount that is less than 25 percent of the annual revenues of the subgrantee, including any entity that controls, is controlled by, or that is under common control with such subgrantee; or (II) to provide service to a number of locations that is less than 25 percent of the total number of locations served by the subgrantee, including any entity that controls, is controlled by, or that is under common control with such subgrantee; or (M) diversity, equity, and inclusion. .\n##### (f) All technologies eligible\nSection 60102(g) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(g) ), as amended by the preceding subsections of this section, is further amended by adding at the end the following:\n(5) All technologies eligible An eligible entity, in awarding subgrants for the deployment of a broadband network using grant funds received under this section, shall treat as satisfying the definition of the term reliable broadband service any broadband service that meets the performance criteria established under subsection (a)(2)(L) without regard to the type of technology by which such service is provided. .\n##### (g) No regulation of rates permitted\nSection 60102(h)(5)(D) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(h)(5)(D) ) is amended to read as follows:\n(D) No regulation of rates permitted (i) Rule of construction Nothing in this title may be construed to authorize the Assistant Secretary, the National Telecommunications and Information Administration, or an eligible entity to regulate, set, or otherwise mandate the rates charged for broadband service or the methodologies used to calculate such rates, for consumers generally or for any subset of consumers, including through the capping or freezing of such rates, the encouragement of another entity to regulate such rates, or the use of rates as part of an application scoring process. (ii) Prohibition An eligible entity may not regulate, set, or otherwise mandate pursuant to this section the rates charged for broadband service or the methodologies used to calculate such rates, including through the capping or freezing of such rates, the encouragement of another entity to regulate such rates, or the use of rates as part of an application scoring process, without regard to whether the regulation, setting, or mandating\u2014 (I) was approved, prior to the date of the enactment of this clause, as part of the initial proposal, or any other portion of the application process, of such entity; or (II) is carried out in conjunction with the requirement to offer a low-cost broadband service option under paragraph (4)(B). .",
      "versionDate": "2025-03-05",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-23T10:42:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1870",
          "measure-number": "1870",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2026-02-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1870v00",
            "update-date": "2026-02-02"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Streamlining Program Efficiency and Expanding Deployment for BEAD Act or the SPEED for BEAD Act</strong></p><p>This bill makes certain changes to the Broadband, Equity, Access, and Deployment (BEAD) Program, including by expanding the broadband technologies that may qualify for funding and prohibiting states from regulating broadband rates in connection with the program. \u00a0</p><p>(The BEAD Program is administered by the National Telecommunications and Information Administration (NTIA) and provides funding to eligible entities for broadband deployment, connectivity, mapping, and adoption projects. <em>Eligible entities</em> include U.S. states, territories, and the District of Columbia.)\u00a0</p><p>Specifically, the bill establishes that projects using any broadband technology (e.g., satellite, fixed wireless, or fiber) may qualify for funding,\u00a0provided the technology meets specified performance criteria. (Original BEAD rules established a preference for fiber projects.)</p><p>The bill also explicitly prohibits eligible entities from regulating, setting, or otherwise mandating pursuant to the BEAD Program (1) rates charged for broadband service, or (2) methodologies used to calculate such rates. The prohibition includes rate regulation carried out in conjunction with the existing requirement that subgrantees offer at least one low-cost broadband service option to certain subscribers. \u00a0\u00a0</p><p>Further, the bill prohibits the NTIA and eligible entities from establishing or enforcing conditions, preferences, or other requirements related to collective bargaining and labor agreements; climate change; diversity, equity, and inclusion; and other topics. The bill also modifies the purposes for which the funds may be used and the treatment of unused funds.\u00a0</p><p>Finally, the bill replaces the term <em>Equity</em> in the program\u2019s name with <em>Expansion</em>.</p>"
        },
        "title": "SPEED for BEAD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1870.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Streamlining Program Efficiency and Expanding Deployment for BEAD Act or the SPEED for BEAD Act</strong></p><p>This bill makes certain changes to the Broadband, Equity, Access, and Deployment (BEAD) Program, including by expanding the broadband technologies that may qualify for funding and prohibiting states from regulating broadband rates in connection with the program. \u00a0</p><p>(The BEAD Program is administered by the National Telecommunications and Information Administration (NTIA) and provides funding to eligible entities for broadband deployment, connectivity, mapping, and adoption projects. <em>Eligible entities</em> include U.S. states, territories, and the District of Columbia.)\u00a0</p><p>Specifically, the bill establishes that projects using any broadband technology (e.g., satellite, fixed wireless, or fiber) may qualify for funding,\u00a0provided the technology meets specified performance criteria. (Original BEAD rules established a preference for fiber projects.)</p><p>The bill also explicitly prohibits eligible entities from regulating, setting, or otherwise mandating pursuant to the BEAD Program (1) rates charged for broadband service, or (2) methodologies used to calculate such rates. The prohibition includes rate regulation carried out in conjunction with the existing requirement that subgrantees offer at least one low-cost broadband service option to certain subscribers. \u00a0\u00a0</p><p>Further, the bill prohibits the NTIA and eligible entities from establishing or enforcing conditions, preferences, or other requirements related to collective bargaining and labor agreements; climate change; diversity, equity, and inclusion; and other topics. The bill also modifies the purposes for which the funds may be used and the treatment of unused funds.\u00a0</p><p>Finally, the bill replaces the term <em>Equity</em> in the program\u2019s name with <em>Expansion</em>.</p>",
      "updateDate": "2026-02-02",
      "versionCode": "id119hr1870"
    },
    "title": "SPEED for BEAD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Streamlining Program Efficiency and Expanding Deployment for BEAD Act or the SPEED for BEAD Act</strong></p><p>This bill makes certain changes to the Broadband, Equity, Access, and Deployment (BEAD) Program, including by expanding the broadband technologies that may qualify for funding and prohibiting states from regulating broadband rates in connection with the program. \u00a0</p><p>(The BEAD Program is administered by the National Telecommunications and Information Administration (NTIA) and provides funding to eligible entities for broadband deployment, connectivity, mapping, and adoption projects. <em>Eligible entities</em> include U.S. states, territories, and the District of Columbia.)\u00a0</p><p>Specifically, the bill establishes that projects using any broadband technology (e.g., satellite, fixed wireless, or fiber) may qualify for funding,\u00a0provided the technology meets specified performance criteria. (Original BEAD rules established a preference for fiber projects.)</p><p>The bill also explicitly prohibits eligible entities from regulating, setting, or otherwise mandating pursuant to the BEAD Program (1) rates charged for broadband service, or (2) methodologies used to calculate such rates. The prohibition includes rate regulation carried out in conjunction with the existing requirement that subgrantees offer at least one low-cost broadband service option to certain subscribers. \u00a0\u00a0</p><p>Further, the bill prohibits the NTIA and eligible entities from establishing or enforcing conditions, preferences, or other requirements related to collective bargaining and labor agreements; climate change; diversity, equity, and inclusion; and other topics. The bill also modifies the purposes for which the funds may be used and the treatment of unused funds.\u00a0</p><p>Finally, the bill replaces the term <em>Equity</em> in the program\u2019s name with <em>Expansion</em>.</p>",
      "updateDate": "2026-02-02",
      "versionCode": "id119hr1870"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1870ih.xml"
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
      "title": "SPEED for BEAD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T10:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SPEED for BEAD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining Program Efficiency and Expanding Deployment for BEAD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Infrastructure Investment and Jobs Act to improve the Broadband Equity, Access, and Deployment Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T10:48:25Z"
    }
  ]
}
```
