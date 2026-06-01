# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6593?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6593
- Title: Domestic Organic Investment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6593
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-16T08:07:36Z
- Update date including text: 2026-05-16T08:07:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6593",
    "number": "6593",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "Domestic Organic Investment Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:36Z",
    "updateDateIncludingText": "2026-05-16T08:07:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:05:25Z",
                "name": "Referred to"
              }
            },
            "name": "Nutrition and Foreign Agriculture Subcommittee",
            "systemCode": "hsag03"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-13T20:05:25Z",
                "name": "Referred to"
              }
            },
            "name": "Conservation, Research, and Biotechnology Subcommittee",
            "systemCode": "hsag14"
          }
        ]
      },
      "systemCode": "hsag00",
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "WI"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6593ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6593\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. Salinas (for herself and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Marketing Act of 1946 to establish the Domestic Organic Investment Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Domestic Organic Investment Act of 2025 .\n#### 2. Domestic Organic Investment Program\nSubtitle A of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1621 et seq. ) is amended by adding at the end the following:\n210B. Domestic Organic Investment Program (a) Definitions In this section: (1) Certified organic product The term certified organic product means an agricultural product (as defined in section 2103 of the Organic Foods Production Act of 1990 ( 7 U.S.C. 6502 )) that is organically produced (as defined in that section). (2) Eligible entity (A) In general The term eligible entity means an entity described in subparagraph (B) that\u2014 (i) is owned and operated within\u2014 (I) a State; (II) the District of Columbia; (III) any territory or possession of the United States; or (IV) the jurisdiction of an Indian Tribe; and (ii) (I) is certified in accordance with subpart E of part 205 of title 7, Code of Federal Regulations (or successor regulations); or (II) is in transition to certification, as defined by the Secretary. (B) Entities described An entity referred to in subparagraph (A) is\u2014 (i) a producer, producer cooperative, or other commercial entity that produces or handles certified organic products; (ii) a unit of Tribal government; or (iii) such other entity as the Secretary may designate. (C) Exclusion The term eligible entity does not include an entity described in subparagraph (B) the operations of which are suspended or revoked under section 205.662 of title 7, Code of Federal Regulations (or a successor regulation). (3) Indian tribe The term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (4) Secretary The term Secretary means the Secretary of Agriculture, acting through the Administrator of the Agricultural Marketing Service. (5) Tribal government The term Tribal government means the governing body of an Indian Tribe. (b) Establishment and purpose The Secretary shall establish a program, to be known as the Domestic Organic Investment Program , that\u2014 (1) increases the capacity of the domestic organic product supply chain for producers, handlers, suppliers, and processors of certified organic products; (2) modernizes manufacturing, tracking, storage, and information technology systems specific to the purposes described in this subsection, such as process control or organic product ingredient tracking systems; (3) improves the capacity of eligible entities to comply with applicable regulatory requirements or quality standards required to access markets, such as requirements and standards relating to food safety and organic product certification; (4) expands capacity for storage, processing, aggregation, and distribution of certified organic products to create more and better markets for producers of certified organic products; (5) facilitates market development for domestically produced certified organic products currently being serviced by organic imports; and (6) addresses additional barriers and bottlenecks in the domestic organic product supply chain for producers, handlers, suppliers, and processors of certified organic products, as determined by the Secretary. (c) Grants For each fiscal year for which amounts are made available to carry out this section under subsection (j), the Secretary shall provide grants to support eligible entities in conducting activities in accordance with the purposes of the program described in subsection (b). (d) Applications (1) In general To be eligible to receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (2) Simplified process The Secretary shall implement a simplified application and award process under this section for use by any eligible entity seeking to carry out an equipment-only project. (3) Priority The Secretary may establish an annual priority for grants under this section based in part on\u2014 (A) imbalance of trade and reliance on organic imports; (B) National Organic Standards Board recommendations; and (C) identified organic processing and supply chain bottlenecks inhibiting market growth and efficiency. (4) Competitive process The Secretary\u2014 (A) shall conduct a competitive process to select applications submitted under this subsection; (B) may assess and rank applications with similar purposes as a group; and (C) before accepting any application under this subsection, shall make publicly available the criteria to be used in evaluating the applications. (e) Project types An eligible entity may use amounts received under this section to carry out, in accordance with such goals and deadlines for completion as the Secretary may establish, the following types of projects: (1) Certified organic product storage (including cold storage), aggregation, processing, and distribution capacity expansion. (2) Equipment-only. (f) Term Unless otherwise determined by the Secretary, a grant provided under this section shall have a term of not longer than 3 years. (g) Maximum amount (1) In general The amount of a grant provided under this section for a project described in subsection (e)(1) shall be not more than $2,000,000. (2) Equipment-only projects The amount of a grant provided under this section for a project described in subsection (e)(2) shall be not more than $100,000. (h) Matching funds (1) In general An eligible entity that receives a grant under this section to carry out a project described in subsection (e)(1) shall provide a non-Federal share equal to not less than 50 percent of the cost of the project. (2) Equipment-only projects An eligible entity that receives a grant under this section to carry out a project described in subsection (e)(2) shall provide a non-Federal share equal to not less than 25 percent of the cost of the project. (3) Rule for certain applications The Secretary may waive or lower the non-Federal share required under this subsection for beginning farmers and ranchers and veterans applying for a grant under this section. (i) Technical assistance The Secretary may provide to eligible entities technical assistance under this section, directly or through 1 or more cooperative agreements. (j) Authorization of appropriations In addition to amounts otherwise available, there are authorized to be appropriated to the Secretary such sums as are necessary to carry out this section for each of fiscal years 2026 through 2030, to remain available until expended. .",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-12-10",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3427",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Domestic Organic Investment Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-07T16:29:19Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6593ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Marketing Act of 1946 to establish the Domestic Organic Investment Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:21Z"
    },
    {
      "title": "Domestic Organic Investment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Domestic Organic Investment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:20Z"
    }
  ]
}
```
