# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6089?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6089
- Title: Biomanufacturing Excellence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6089
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-05-22T08:08:05Z
- Update date including text: 2026-05-22T08:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6089",
    "number": "6089",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Biomanufacturing Excellence Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:05Z",
    "updateDateIncludingText": "2026-05-22T08:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "IN"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NC"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "NC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "DE"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MD"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "OK"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NC"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "GU"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6089ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6089\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Ms. Houlahan (for herself, Mr. Baird , Ms. Ross , and Mr. Rouzer ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo establish a Biopharmaceutical Center of Excellence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Biomanufacturing Excellence Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nBiotechnology is the designing and engineering of biological systems. Biotechnology allows scientists to grow everything from medicines to crops to materials, enabling biology by design .\n**(2)**\nBiotechnology holds the potential for the United States to transform its military capabilities, strengthen food security and agricultural resilience, and cure life-threatening diseases, but it holds that same potential for other countries. The countries that master biotechnology first will gain the ability to shape how those technologies are used for decades to come.\n**(3)**\nBiotechnology unlocks the capabilities of producing medicines via biological systems, known as biopharmaceutical manufacturing. Biopharmaceutical manufacturing will enable better and less invasive treatments that extend and improve lives.\n**(4)**\nBy investing in biomanufacturing, the United States Government would reduce dependency on foreign supply chains.\n**(5)**\nFor United States manufacturers, the biggest roadblock to commercialization is proving that their products and processes can scale and produce a return on investment. Biomanufacturing requires flexible and affordable infrastructure for development, to ensure that innovative products can rapidly move from the lab to commercial-scale production.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nto realize the potential of biotechnology, the United States Government should establish a biopharmaceutical manufacturing center of excellence;\n**(2)**\nthe center should facilitate and accelerate manufacturing innovation, support good manufacturing practices, and provide for collaboration among public, private, and nonprofit institutions; and\n**(3)**\nthe center should also facilitate training for workers to operate biotechnology tools and equipment and to bolster talent throughout the biotechnology sector.\n#### 3. Establishment of National Biopharmaceutical Center of Excellence\nThe National Institute of Standards and Technology Act ( 15 U.S.C. 271 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 36 as section 37; and\n**(2)**\nby inserting after section 35 the following:\n36. National Biopharmaceutical Center of Excellence (a) Establishment of Center of Excellence (1) In general The Director shall award a grant to or enter into an other transaction agreement with, on a competitive basis, an eligible entity to establish and operate a center of excellence to be known as the National Biopharmaceutical Manufacturing Center of Excellence (in this section referred to as the Center of Excellence ). (2) Objectives The objectives of the Center of Excellence include\u2014 (A) advancing the science of biopharmaceutical manufacturing, especially with respect to products of particular importance to the national security, health security, or economic security of the United States, including by\u2014 (i) developing and demonstrating flexible biopharmaceutical manufacturing technologies and systems; (ii) improving upstream and downstream processes for multiple biopharmaceutical manufacturing platforms or product modalities; (iii) improving biopharmaceutical manufacturing equipment and capabilities; and (iv) reducing supply bottlenecks and strengthening supply chain self-sufficiency through demonstration of innovative technologies; (B) supporting good manufacturing practices, quality by design, and standardization of chemistry, manufacturing, and controls to ensure effective and efficient manufacturing and to improve the regulation of innovative methods of manufacturing; (C) advancing workforce training and development by working with educational and community partners to bolster biotechnology talent; (D) developing the science of and deploying the infrastructure for innovative biopharmaceutical manufacturing by engaging with\u2014 (i) institutions of higher education; (ii) small, medium, and large pharmaceutical manufacturers; (iii) Federal, State, and local government agencies and institutes; (iv) non-profit organizations; (v) professional organizations; and (vi) any other entity the Director considers relevant; (E) sharing with the head of any Executive agency that oversees the planning, management, or coordination of Federal activities relating to biotechnology research generated by the Center of Excellence, including data regarding best practices for biopharmeceutical manufacturing; and (F) any other objective the Director considers relevant. (3) Funding The Director shall award the Center of Excellence funding for any of the following: (A) To facilitate the construction of facilities necessary to accomplish the objectives described in paragraph (2). (B) To conduct collaborative research on new technology for scaling biopharmaceutical manufacturing in the United States for commercial production. (C) To facilitate workforce training programs for biopharmaceutical manufacturing. (D) To fund relevant research and programs for the development of biopharmaceutical manufacturing. (b) Application; award (1) In general Not later than 180 days after the date of the enactment of this section, the Director shall solicit applications from eligible entities specified in paragraph (2) and award to or enter into with one such entity a grant or other transaction agreement to establish the Center of Excellence. (2) Eligibility An entity is eligible to submit an application pursuant to paragraph (1) if\u2014 (A) the entity is\u2014 (i) a public-private partnership; (ii) an institution of higher education; or (iii) a consortia of entities specified in clauses (i) or (ii); and (B) the entity is not a Federal entity. (3) Content of application An application submitted by an entity pursuant to paragraph (1) shall include\u2014 (A) examples from the entity of previous research, development, implementation, and demonstration of innovative practices of biopharmaceutical manufacturing; (B) a description of the manner by which the entity plans to advance the science of biopharmaceutical manufacturing, especially with respect to products of particular importance to the national security, health security, or economic security of the United States; (C) a description of the manner by which the entity plans to incorporate good manufacturing practices, quality by design, and standardization of chemistry, manufacturing, and controls, and similar guidance to ensure effective and efficient manufacturing and to make innovative methods of manufacturing more understandable to Executive agencies that are tasked with regulating such methods; (D) examples of trainings facilitated by the entity that prepare workers for the biotechnology sector; (E) a description of any existing partnerships with educational or community partners that help facilitate workforce training for the biotechnology sector; (F) a description of any experience participating in or leading biopharmaceutical manufacturing partnerships, including those with institutions of higher education, pharmaceutical manufacturers, non-profit organizations, and governmental agencies\u2014 (i) to organize and conduct research and development aimed at\u2014 (I) creating and standardizing new and more effective technology; (II) developing best practices and sharing knowledge about such technology; (III) creating intellectual property; and (IV) maintaining technological leadership in the United States; (ii) to support the deployment of innovative practices and infrastructure of biopharmaceutical manufacturing in the United States; and (iii) to support developing a skilled workforce ready to use innovations in the biopharmaceutical manufacturing sector; and (G) a description of how the entity intends to utilize any funds authorized under this section to build or expand facilities and infrastructure to achieve any of the objectives described in subsection (a)(2). (4) Selection Criteria In selecting an applicant for a grant or other transaction agreement under paragraph (1), the Director shall consider the following: (A) The potential of the applicant to establish a Center of Excellence that would achieve the objectives set forth in subsection (a)(2). (B) The past performance of the applicant in biopharmaceutical manufacturing workforce development and the potential of the applicant to support workforce development activities in various regions throughout the United States. (C) The extent to which the applicant proposes to leverage the activities of other biopharmaceutical manufacturing innovation, development, and scaling initiatives. (D) Whether the proposed location for the Center of Excellence is proximate to other biomanufacturing infrastructure, training facilities, or industrial clusters. (E) The time the applicant estimates is needed for the Center of Excellence to be fully operational and to start delivering impact. (F) The amount of co-investment committed by Federal, State, private, and other sources to establish the Center of Excellence. (G) Any additional criteria that the Director considers relevant. (c) Annual reports (1) Initial report Not later than one year after the date on which the Director awards to or enters into with an eligible entity a grant or other transaction agreement to establish the Center of Excellence under subsection (b)(1), the Director shall submit to Congress a report describing the progress on establishing the Center of Excellence, including\u2014 (A) the construction of facilities; (B) any activities, partnerships, and collaborations by the Center of Excellence; and (C) any other information regarding the formation of the Center of Excellence that the Director considers relevant. (2) Progress report Not later than one year after the date on which operations at the Center of Excellence officially begin, the Director shall submit to Congress a report describing\u2014 (A) the activities, partnerships, collaborations, and findings of the Center of Excellence; and (B) any other information regarding the Center of Excellence that the Director considers relevant. (3) Final report Not later than 5 years after the date on which operations at the Center of Excellence officially begin, the Director shall submit to Congress a report describing\u2014 (A) the activities, partnerships, collaborations, and findings of the Center of Excellence; and (B) any other information regarding the Center of Excellence that the Director considers relevant. (4) Publication The Director shall make the reports required by paragraphs (1), (2), and (3) available to the public in an easily accessible electronic format on a website of the Federal Government that includes information on biotechnology. (d) Intellectual Property The Director shall ensure that, prior to commencing operations, the Center of Excellence, in consultation with similar existing institutions, such as Manufacturing USA institutes (as defined in section 34(d)), establishes intellectual property guidelines for research conducted within or in collaboration with the Center of Excellence. (e) Authorization of Appropriations There is authorized to be appropriated to the Director to carry out this section $120,000,000 for fiscal year 2026. (f) Definitions In this section: (1) Biomanufacturing The term biomanufacturing means the application of biotechnology to manufacturing. (2) Biopharmaceutical The term biopharmaceutical means a pharmaceutical drug product manufactured using, extracted from, or synthesized from living cells or biological organisms. (3) Biotechnology The term biotechnology means the application of science or engineering, directly or indirectly, to\u2014 (A) a living organism; (B) a part or product of a living organism; or (C) a modified form of subparagraph (A) or (B). (4) Executive agency The term Executive agency \u2014 (A) has the meaning given that term in section 105 of title 5, United States Code; and (B) includes the Executive Office of the President and the Office of the Vice President. (5) Institution of higher education The term institution of higher education has the meaning given that term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ). .",
      "versionDate": "2025-11-18",
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
        "actionDate": "2025-11-18",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3188",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Biomanufacturing Excellence Act of 2025",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-11-20T17:10:52Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6089ih.xml"
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
      "title": "Biomanufacturing Excellence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T10:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Biomanufacturing Excellence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Biopharmaceutical Center of Excellence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T10:03:24Z"
    }
  ]
}
```
