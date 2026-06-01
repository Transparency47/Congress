# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4109
- Title: Recycling and Composting Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 4109
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-05-19T08:05:43Z
- Update date including text: 2026-05-19T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-24 - Committee: Referred to the Subcommittee on Environment.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-24 - Committee: Referred to the Subcommittee on Environment.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4109",
    "number": "4109",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Recycling and Composting Accountability Act",
    "type": "HR",
    "updateDate": "2026-05-19T08:05:43Z",
    "updateDateIncludingText": "2026-05-19T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-05-14T15:07:19Z",
                "name": "Reported by"
              },
              {
                "date": "2026-05-14T15:06:57Z",
                "name": "Markup by"
              },
              {
                "date": "2025-06-24T15:06:31Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "TN"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "NY"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "LA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "KS"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "PA"
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
      "sponsorshipDate": "2026-01-20",
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
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4109ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4109\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Neguse (for himself, Mr. Burchett , and Mr. Foster ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Administrator of the Environmental Protection Agency to carry out certain activities to improve recycling and composting programs in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Recycling and Composting Accountability Act .\n#### 2. Definitions\n##### (a) In general\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Compost**\nThe term compost means a product that\u2014\n**(A)**\nis manufactured through the controlled aerobic, biological decomposition of biodegradable materials;\n**(B)**\nhas been subjected to medium and high temperature organisms, which\u2014\n**(i)**\nsignificantly reduce the viability of pathogens and weed seeds; and\n**(ii)**\nstabilize carbon in the product such that the product is beneficial to plant growth; and\n**(C)**\nis typically used as a soil amendment, but may also contribute plant nutrients.\n**(3) Compostable material**\nThe term compostable material means material that is a feedstock for creating compost, including\u2014\n**(A)**\nwood;\n**(B)**\nagricultural crops;\n**(C)**\npaper, such as cardboard and other paper products;\n**(D)**\ncertified compostable products associated with organic waste;\n**(E)**\nother organic plant material;\n**(F)**\norganic waste, including food waste and yard waste; and\n**(G)**\nsuch other material that is composed of biomass that can be continually replenished or renewed, as determined by the Administrator.\n**(4) Indian tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(5) Recyclable material**\nThe term recyclable material means a material that is obsolete, previously used, off-specification, surplus, or incidentally produced for processing into a specification-grade commodity for which a reuse market currently exists or is being developed.\n**(6) Recycling**\nThe term recycling means the series of activities\u2014\n**(A)**\nduring which recyclable materials are processed into specification-grade commodities and consumed as raw-material feedstock, in lieu of virgin materials, in the manufacturing of new products;\n**(B)**\nthat may, with regard to recyclable materials and prior to the activities described in subparagraph (A), include sorting, collection, processing, and brokering; and\n**(C)**\nthat result, subsequent to processing described in subparagraph (A), in consumption by a materials manufacturer, including for the manufacturing of new products.\n**(7) State**\nThe term State has the meaning given the term in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ).\n##### (b) Definition of processing\nIn paragraphs (5) and (6) of subsection (a), the term processing means any mechanical, manual, or other method that\u2014\n**(1)**\ntransforms a recyclable material into a specification-grade commodity; and\n**(2)**\nmay occur in multiple steps, with different phases, including sorting, occurring at different locations.\n#### 3. Reports on composting and recycling infrastructure capabilities\n##### (a) In general\nSubtitle D of the Solid Waste Disposal Act ( 42 U.S.C. 6941 et seq. ) is amended by adding at the end the following:\n4011. Reports on composting and recycling infrastructure capabilities (a) Definitions In this section: (1) Recycling and Composting Accountability Act terms The terms compost , compostable material , recyclable material , and recycling have the meanings given such terms in section 2 of the Recycling and Composting Accountability Act . (2) Composting facility The term composting facility means a location, structure, or device that transforms compostable materials into compost. (3) Indian tribe The term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (4) Materials recovery facility (A) In general The term materials recovery facility means a dedicated facility where primarily residential recyclable materials, which are diverted from disposal by the generator and collected separately from municipal solid waste, are mechanically or manually sorted into commodities for further processing into specification-grade commodities for sale to end users. (B) Exclusion The term materials recovery facility does not include a solid waste management facility that may process municipal solid waste to remove recyclable materials. (C) Definition of processing For purposes of this paragraph, the term processing has the meaning given such term in section 2(b) of the Recycling and Composting Accountability Act . (b) Report (1) In general The Administrator shall request information and data from, collaborate with, or contract with, as necessary and appropriate, States, units of local government, and Indian Tribes, for the provision, preparation, and publication of a report, or to expand work under the National Recycling Strategy to include information and data, on compostable materials and efforts to reduce contamination rates for recycling, including\u2014 (A) an evaluation of existing Federal, State, and local laws that may present barriers to implementation of composting strategies; (B) a description and evaluation of composting infrastructure and programs within States, units of local government, and Indian Tribes; (C) an estimate of the costs and approximate land needed to expand composting programs; and (D) a review of the practices of manufacturers and companies that are moving to using compostable packaging and food service ware for the purpose of making the composting process the end-of-life use of those products. (2) Submission Not later than 2 years after the date of enactment of this section, the Administrator shall submit to Congress the report prepared under paragraph (1). (c) Inventory of materials recovery facilities Not later than 3 years after the date of enactment of this section, and every 4 years thereafter, the Administrator, in consultation with relevant Federal agencies and States, units of local government, and Indian Tribes, shall\u2014 (1) prepare an inventory or estimate of materials recovery facilities in the United States, including\u2014 (A) the number of materials recovery facilities in each State; and (B) a general description of the materials that each of those materials recovery facilities can process, including\u2014 (i) in the case of plastic, a description of\u2014 (I) the types of accepted resin, if applicable; and (II) the packaging or product format, such as a jug, a carton, or film; (ii) food packaging and service ware, such as a bottle, cutlery, or a cup; (iii) paper; (iv) aluminum, such as an aluminum beverage can, food can, aerosol can, or foil; (v) steel, such as a steel food or aerosol can; (vi) other scrap metal; (vii) glass; or (viii) any other material not described in any of clauses (i) through (vii) that a materials recovery facility processes; and (2) submit to Congress the inventory or estimate prepared under paragraph (1). (d) Information on recycling and composting systems The Administrator shall, as necessary and appropriate, collaborate or contract with States, units of local government, and Indian Tribes to estimate, with respect to the United States\u2014 (1) the number and types of recycling and composting programs; (2) the types and forms of materials accepted by recycling or composting programs; (3) the number of individuals\u2014 (A) with access to recycling and composting services to at least the extent of access to disposal services; and (B) who use, on a percentage basis, the recycling and composting services described in subparagraph (A); (4) the number of individuals with barriers to accessing recycling and composting services similar to their access to disposal services and the types of those barriers experienced; (5) the inbound contamination and capture rates of recycling and composting programs; (6) if applicable, other available recycling or composting programs; and (7) the average costs and benefits to States, units of local government, and Indian Tribes of recycling and composting programs. (e) Recycling reporting rates (1) Collection of data; development of rates The Administrator may use amounts made available under section 6 of the Recycling and Composting Accountability Act \u2014 (A) to biannually collect, in collaboration with States, to the extent practicable, information supplied on a voluntary basis to develop the estimated rates described in subparagraphs (B) and (C); (B) to develop a standardized estimated rate of recyclable materials in States that provide information under subparagraph (A) that have been successfully diverted from the waste stream and brought to a materials recovery facility or composting facility; and (C) to develop an estimated national recycling rate based on the information described in subparagraphs (A) and (B). (2) Use Using amounts made available under section 6 of the Recycling and Composting Accountability Act , the Administrator may use the information collected and rates developed under paragraph (1) to provide requesting States, units of local government, and Indian Tribes data and technical assistance\u2014 (A) to reduce the overall waste produced by the States, units of local government, and Indian Tribes; (B) to assist the States, units of local government, and Indian Tribes in understanding the nuances of the information collected relating to diversion activities; and (C) to increase recycling and composting rates of the States, units of local government, and Indian Tribes. (f) Report on end markets The Administrator, in collaboration or contract with, as necessary and appropriate, relevant Federal agencies, States, units of local government, or Indian Tribes, shall\u2014 (1) provide an update to the report submitted under section 306 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ; 134 Stat. 1096) to include an addendum on the end-market sale of all recyclable materials from materials recovery facilities that process recyclable materials, including, to the extent practicable\u2014 (A) the total, in dollars per ton, domestic sales of bales of recyclable materials; and (B) the total, in dollars per ton, international sales of bales of recyclable materials; (2) prepare a report on the end-market sale of compost from, to the extent practicable, compostable materials, including the total, in dollars per ton, of domestic sales of compostable materials; and (3) not later than 3 years after the date of enactment of this section, submit to Congress the update to the report prepared under paragraph (1) and the report prepared under paragraph (2). (g) Privileged or confidential information (1) In general Information collected under subsection (e)(1) or paragraph (1) or (2) of subsection (f) shall not include any privileged or confidential information described in section 552(b)(4) of title 5, United States Code. (2) Nondisclosure Information collected to carry out this section shall not be made public if the information meets the requirements of section 552(b) of title 5, United States Code. .\n##### (b) Clerical amendment\nThe table of contents in section 1001 of the Solid Waste Disposal Act is amended by inserting after the item relating to section 4010 the following:\nSec. 4011. Report on composting and recycling infrastructure capabilities. .\n#### 4. Federal agency activities related to recycling\nNot later than 2 years after the date of enactment of this Act, and every 2 years thereafter until 2033, the Comptroller General of the United States shall make publicly available a report\u2014\n**(1)**\ndetailing or, to the extent practicable, providing an estimate of\u2014\n**(A)**\nthe total annual recycling and composting rates reported by all Federal agencies; and\n**(B)**\nthe total annual percentage of products containing recyclable material, compostable material, or recovered materials purchased by all Federal agencies, including\u2014\n**(i)**\nthe total quantity of procured products containing recyclable material or recovered materials listed in the comprehensive procurement guidelines published under section 6002(e) of the Solid Waste Disposal Act ( 42 U.S.C. 6962(e) ); and\n**(ii)**\nthe total quantity of compostable material purchased by all Federal agencies;\n**(2)**\nidentifying the activities of each Federal agency that promote recycling or composting; and\n**(3)**\nidentifying activities that Federal agencies could carry out to further promote recycling or composting.\n#### 5. Study on the diversion of recyclable materials from a circular market\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Administrator shall develop a metric for determining the proportion of recyclable materials in commercial and municipal waste streams that are being diverted from a circular market.\n##### (b) Study; report\nNot later than 1 year after the development of a metric under subsection (a), the Administrator shall conduct a study of, and submit to Congress a report on, the proportion of recyclable materials in commercial and municipal waste streams that, during each of the 10 calendar years preceding the year of submission of the report, were diverted from a circular market.\n##### (c) Data\nThe report under subsection (b) shall provide data on specific recyclable materials, including aluminum, plastics, paper and paperboard, textiles, and glass, that were prevented from remaining in a circular market through disposal or elimination, and to what use those specific recyclable materials were lost.\n##### (d) Evaluation\nThe report under subsection (b) shall include an evaluation of whether the establishment or improvement of recycling programs would\u2014\n**(1)**\nimprove recycling rates;\n**(2)**\nreduce the quantity of recyclable materials being unutilized in a circular market; and\n**(3)**\naffect prices paid by consumers for products using materials recycled in the circular market.\n#### 6. Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this Act and the amendments made by this Act $4,000,000 for each of fiscal years 2025 through 2029.\n#### 7. Administration\n##### (a) Unfunded mandates\nThe Administrator or the Secretary of Commerce may not exercise any authority under this Act or any amendment made by this Act if exercising that authority would require a State, a unit of local government, or an Indian Tribe to carry out a mandate for which funding is not available.\n##### (b) Nondisclosure\nAny information collected to carry out this Act shall not be made public if the information meets the requirements of section 552(b) of title 5, United States Code.",
      "versionDate": "2025-06-24",
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
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
        "name": "Environmental Protection",
        "updateDate": "2025-07-15T10:57:24Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4109ih.xml"
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
      "title": "Recycling and Composting Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recycling and Composting Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Environmental Protection Agency to carry out certain activities to improve recycling and composting programs in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:23Z"
    }
  ]
}
```
