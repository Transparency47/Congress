# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6969?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6969
- Title: Rural Investment for Producers and the Environment (RIPE) Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6969
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-05-22T08:07:45Z
- Update date including text: 2026-05-22T08:07:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6969",
    "number": "6969",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000622",
        "district": "19",
        "firstName": "Josh",
        "fullName": "Rep. Riley, Josh [D-NY-19]",
        "lastName": "Riley",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Rural Investment for Producers and the Environment (RIPE) Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:45Z",
    "updateDateIncludingText": "2026-05-22T08:07:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
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
      "actionDate": "2026-01-07",
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
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T15:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:39:24Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6969ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6969\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2026 Mr. Riley of New York (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to establish a program that provides payments to producers for carrying out conservation practices in selected eligible watersheds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Investment for Producers and the Environment (RIPE) Act of 2026 .\n#### 2. Demonstration Program\nChapter 5 of subtitle D of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3839bb et seq. ) is amended by inserting after section 1240M the following:\n1240N. Demonstration program (a) Definitions In this section: (1) Eligible watershed The term eligible watershed means a watershed with significant agricultural production, as determined by the Secretary, that is located in a State or a United States Territory. (2) Program The term program means the program established under subsection (b). (3) Selected practice The term selected practice means a practice that has one or more environmental benefit, including\u2014 (A) improved water quality and quantity, soil health, air quality, climate resiliency, and biodiversity; (B) increased agricultural yields; (C) restored or enhanced wildlife habitat; and (D) any other environmental benefit, as determined by the Secretary. (b) Demonstration program (1) In general The Secretary shall establish a program under which the Secretary enters into a contract with a producer to implement a selected practice on an eligible watershed, selected in accordance with paragraph (2), for the purpose of demonstrating the effects of implementing such selected practice. (2) Eligible watershed (A) In general Subject to subparagraph (B), not later than one year after the date of enactment of this section, the Secretary shall, in carrying out the program, select\u2014 (i) not more than 2 eligible watersheds in a State or territory; and (ii) not more than 30 eligible watersheds total. (B) Watersheds for Tribal lands In selecting an eligible watershed under subparagraph (A), the Secretary shall not include an eligible watershed that serves Tribal lands towards the limitation described in clause (i) of such subparagraph. (c) Contract terms (1) Payment In entering into a contract with a producer under the program, the Secretary shall provide direct payments to the producer for adopting and implementing a selected practice on an eligible watershed selected under subsection (b)(2). (2) Term A contract under this subsection shall be for a term of not less than 3 years and not more than 5 years. (3) Requirements Under a contract entered into under subsection (b), the Secretary shall\u2014 (A) provide to program participants the opportunity to enhance or adopt additional existing conservation practices to improve environmental outcomes given the best available and accessible technology and practices, as appropriate for the size and type of operation; (B) not prohibit a producer under the program from participating in, and receiving compensation from, an environmental services market; and (C) to the extent practical, use performance-based metrics and tools to\u2014 (i) assess outcomes of implementing selected practices; and (ii) support the payment amounts that are determined pursuant to subsection (d). (d) Payments to producers (1) Payment amounts In determining amounts for payments pursuant to subsection (c), the Secretary shall establish an amount on a per acre and per animal unit basis each year that reflects\u2014 (A) the cost of adopting, installing, completing, managing, and improving a selected practice; (B) income foregone by the producer, if applicable, to address\u2014 (i) increased economic risk; (ii) loss in revenue due to reductions in yield; and (iii) economic losses during transition to new practices; (C) compensation to ensure long-term continued management, maintenance, and improvement of the selected practice; and (D) the environmental benefit, any greenhouse gas emissions reductions, and carbon sequestration derived from implementing the selected practice. (2) Review of payment amount Not later than 1 year after the date of enactment of the Rural Investment for Producers and the Environment (RIPE) Act, and annually thereafter, the Secretary shall, after a producer adopts selected practices pursuant to the contract entered into under subsection (b), review, and adjust if determined necessary, payment amounts provided under subsection (c) with respect to accounting for agricultural producer costs, associated technology, and any other factors as determined by the Secretary. (3) Special rate for certain farmers and ranchers In the case of a producer that is a limited resource or socially disadvantaged farmer or rancher, the Secretary shall increase the amount that would otherwise be provided to a producer under this subsection to 15 percent above the otherwise applicable rate. (e) Duties of Secretary Not later than 1 year after the date of enactment of the Rural Investment for Producers and the Environment (RIPE) Act, the Secretary shall, to the maximum extent practical\u2014 (1) implement a simple application and acceptance process, administered by the Natural Resources Conservation Service, to approve applications, subject to the availability of funding, submitted by producers; (2) ensure 10 percent of funds are reserved for contracts with producers who are limited resource or socially disadvantaged farmers or ranchers through targeted outreach and education; (3) establish a minimum contract payment for contracts entered into with producers as an incentive to increase accessibility to the program; (4) provide technical assistance to the applicable producer, that has entered into a contract under this section, for implementing and developing a comprehensive conservation plan for any acres of land or animal units related to the eligible watershed selected by the Secretary under subsection (b)(2) that takes effect between the second year of the applicable contract and the end date of such contract; and (5) authorize technical assistance to be provided by\u2014 (A) State or local government, including conservation districts; (B) third-party providers, including agricultural producer associations; (C) commercial entities, including farmer cooperatives; and (D) nonprofit entities with technical expertise. (f) Reports Not later than December 30, and annually thereafter, the Secretary shall submit a report to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives summarizing the accomplishments of the program, including the number of operations, acres and animal units enrolled, the accrued environmental benefits, the additional and net greenhouse gas benefits accrued, participant demographics, and limitations to adoption, especially within the animal feeding industry. (g) Funding Of the funds from the Commodity Credit Corporation, the following funds shall be made available until expended: (1) $1,000,000 for fiscal year 2026, for the purpose of establishing program regulations, policy, and administrative procedures. (2) $150,000,000 for each of fiscal years 2027 through 2029. .",
      "versionDate": "2026-01-07",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-02-10T00:07:04Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6969ih.xml"
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
      "title": "Rural Investment for Producers and the Environment (RIPE) Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Investment for Producers and the Environment (RIPE) Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to establish a program that provides payments to producers for carrying out conservation practices in selected eligible watersheds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T06:48:20Z"
    }
  ]
}
```
