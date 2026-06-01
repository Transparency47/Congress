# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/351?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/351
- Title: STEWARD Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 351
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2026-05-08T11:03:25Z
- Update date including text: 2026-05-08T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Committee consideration held. Business Meeting printed. S. Hrg. 119-267.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Ordered to be reported without amendment favorably.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-02-05 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 7.
- 2025-11-20 - Floor: Message on Senate action sent to the House.
- 2025-11-20 - Floor: Passed Senate without amendment by Voice Vote. (consideration: CR S8395-8398; text: CR S8395-8398)
- 2025-11-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.
- 2025-11-20 17:44:03 - Floor: Received in the House.
- 2025-11-20 18:18:27 - Floor: Held at the desk.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Committee consideration held. Business Meeting printed. S. Hrg. 119-267.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Ordered to be reported without amendment favorably.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-02-05 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-02-05 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 7.
- 2025-11-20 - Floor: Message on Senate action sent to the House.
- 2025-11-20 - Floor: Passed Senate without amendment by Voice Vote. (consideration: CR S8395-8398; text: CR S8395-8398)
- 2025-11-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.
- 2025-11-20 17:44:03 - Floor: Received in the House.
- 2025-11-20 18:18:27 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/351",
    "number": "351",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001047",
        "district": "",
        "firstName": "Shelley",
        "fullName": "Sen. Capito, Shelley Moore [R-WV]",
        "lastName": "Capito",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "STEWARD Act of 2025",
    "type": "S",
    "updateDate": "2026-05-08T11:03:25Z",
    "updateDateIncludingText": "2026-05-08T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-11-20",
      "actionTime": "18:18:27",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-11-20",
      "actionTime": "17:44:03",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Voice Vote. (consideration: CR S8395-8398; text: CR S8395-8398)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Voice Vote.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 7.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Committee consideration held. Business Meeting printed. S. Hrg. 119-267.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-30",
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
      "actionDate": "2025-01-30",
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
            "date": "2025-02-05T19:08:15Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T17:32:14Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-05T15:30:42Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-30T23:40:17Z",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "RI"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s351is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 351\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mrs. Capito (for herself, Mr. Whitehouse , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo establish a pilot grant program to improve recycling accessibility, to require the Administrator of the Environmental Protection Agency to carry out certain activities to collect and disseminate data on recycling and composting programs in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 or the STEWARD Act of 2025 .\n#### 2. Recycling infrastructure and accessibility improvements\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Curbside recycling**\nThe term curbside recycling means the process by which residential recyclable materials are picked up curbside.\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State (as defined in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ));\n**(B)**\na unit of local government;\n**(C)**\nan Indian Tribe; and\n**(D)**\na public-private partnership or entities seeking to establish a public-private partnership.\n**(4) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(5) Materials recovery facility**\n**(A) In general**\nThe term materials recovery facility means a dedicated facility where primarily residential recyclable materials, which are diverted from disposal by a generator and collected separately from municipal solid waste, are mechanically or manually sorted into commodities for further processing into specification-grade commodities for sale to end users.\n**(B) Exclusion**\nThe term materials recovery facility does not include a solid waste management facility that may process municipal solid waste to remove recyclable materials.\n**(6) Pilot grant program**\nThe term pilot grant program means the Recycling Infrastructure and Accessibility Program established under subsection (b).\n**(7) Recyclable material**\nThe term recyclable material means a material that is obsolete, previously used, off-specification, surplus, or incidentally produced for processing into a specification-grade commodity for which a reuse market currently exists or is being developed.\n**(8) Transfer station**\nThe term transfer station means a facility that\u2014\n**(A)**\nreceives and consolidates recyclable material from curbside recycling or drop-off facilities; and\n**(B)**\nloads the recyclable material onto tractor trailers, railcars, or barges for transport to a distant materials recovery facility or another recycling-related facility.\n**(9) Underserved community**\nThe term underserved community means a community, including an unincorporated area, without access to full recycling services because\u2014\n**(A)**\ntransportation, distance, or other reasons render utilization of available processing capacity at an existing materials recovery facility cost prohibitive; or\n**(B)**\nthe processing capacity of an existing materials recovery facility is insufficient to manage the volume of recyclable materials produced by that community.\n##### (b) Establishment\nNot later than 18 months after the date of enactment of this Act, the Administrator shall establish a pilot grant program, to be known as the Recycling Infrastructure and Accessibility Program , to award grants, on a competitive basis, to eligible entities to improve recycling accessibility in a community or communities within the same geographic area.\n##### (c) Goal\nThe goal of the pilot grant program is to fund eligible projects that will significantly improve accessibility to recycling systems through investments in infrastructure in underserved communities through the use of a hub-and-spoke model for recycling infrastructure development.\n##### (d) Applications\nTo be eligible to receive a grant under the pilot grant program, an eligible entity shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require.\n##### (e) Considerations\nIn selecting eligible entities to receive a grant under the pilot grant program, the Administrator shall consider\u2014\n**(1)**\nwhether the community or communities in which the eligible entity is seeking to carry out a proposed project has curbside recycling;\n**(2)**\nwhether the proposed project of the eligible entity will improve accessibility to recycling services in a single underserved community or multiple underserved communities; and\n**(3)**\n**(A)**\nif the eligible entity is a public-private partnership, the financial health of the private entity seeking to enter into that public-private partnership; or\n**(B)**\nif the eligible entity is seeking to establish a public-private partnership, the financial health of the private entities that would participate in the public-private partnership.\n##### (f) Priority\nIn selecting eligible entities to receive a grant under the pilot grant program, the Administrator shall give priority to eligible entities seeking to carry out a proposed project in a community in which there is not more than 1 materials recovery facility within a 75-mile radius of that community.\n##### (g) Use of funds\nAn eligible entity awarded a grant under the pilot grant program may use the grant funds for projects to improve recycling accessibility in communities, including in underserved communities, by\u2014\n**(1)**\nincreasing the number of transfer stations;\n**(2)**\nexpanding curbside recycling collection programs where appropriate; and\n**(3)**\nleveraging public-private partnerships to reduce the costs associated with collecting and transporting recyclable materials in underserved communities.\n##### (h) Prohibition on use of funds\nAn eligible entity awarded a grant under the pilot grant program may not use the grant funds for projects relating to recycling education programs.\n##### (i) Minimum and maximum grant amount\nA grant awarded to an eligible entity under the pilot grant program shall be in an amount\u2014\n**(1)**\nnot less than $500,000; and\n**(2)**\nnot more than $15,000,000.\n##### (j) Set-Aside\nThe Administrator shall set aside not less than 70 percent of the amounts made available to carry out the pilot grant program for each fiscal year to award grants to eligible entities to carry out a proposed project or program in a single underserved community or multiple underserved communities.\n##### (k) Federal share\nThe Federal share of the cost of a project or program carried out by an eligible entity using grant funds shall be not more than 95 percent.\n##### (l) Report\nNot later than 2 years after the date on which the first grant is awarded under the pilot grant program, the Administrator shall submit to Congress a report describing the implementation of the pilot grant program, which shall include\u2014\n**(1)**\na list of eligible entities that have received a grant under the pilot grant program;\n**(2)**\nthe actions taken by each eligible entity that received a grant under the pilot grant program to improve recycling accessibility with grant funds; and\n**(3)**\nto the extent information is available, a description of how grant funds received under the pilot grant program improved recycling rates in each community in which a project or program was carried out under the pilot grant program.\n##### (m) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Administrator to carry out the pilot grant program $30,000,000 for each of fiscal years 2025 through 2029, to remain available until expended.\n**(2) Administrative costs and technical assistance**\nOf the amounts made available under paragraph (1), the Administrator may use up to 5 percent\u2014\n**(A)**\nfor administrative costs relating to carrying out the pilot grant program; and\n**(B)**\nto provide technical assistance to eligible entities applying for a grant under the pilot grant program.\n#### 3. Recycling and composting data collection\n##### (a) Definitions\n**(1) In general**\nIn this section:\n**(A) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(B) Compost**\nThe term compost means a product that\u2014\n**(i)**\nis manufactured through the controlled aerobic, biological decomposition of biodegradable materials;\n**(ii)**\nhas been subjected to medium and high temperature organisms, which\u2014\n**(I)**\nsignificantly reduce the viability of pathogens and weed seeds; and\n**(II)**\nstabilize carbon in the product such that the product is beneficial to plant growth; and\n**(iii)**\nis typically used as a soil amendment, but may also contribute plant nutrients.\n**(C) Compostable material**\nThe term compostable material means material that is a feedstock for creating compost, including\u2014\n**(i)**\nwood;\n**(ii)**\nagricultural crops;\n**(iii)**\npaper, such as cardboard and other paper products;\n**(iv)**\ncertified compostable products associated with organic waste;\n**(v)**\nother organic plant material;\n**(vi)**\norganic waste, including food waste and yard waste; and\n**(vii)**\nsuch other material that is composed of biomass that can be continually replenished or renewed, as determined by the Administrator.\n**(D) Indian tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(E) Recyclable material**\nThe term recyclable material means a material that is obsolete, previously used, off-specification, surplus, or incidentally produced for processing into a specification-grade commodity for which a reuse market currently exists or is being developed.\n**(F) Recycling**\nThe term recycling means the series of activities\u2014\n**(i)**\nduring which recyclable materials are processed into specification-grade commodities and consumed as raw-material feedstock, in lieu of virgin materials, in the manufacturing of new products;\n**(ii)**\nthat may, with regard to recyclable materials and prior to the activities described in clause (i), include sorting, collection, processing, and brokering; and\n**(iii)**\nthat result, subsequent to processing described in clause (i), in consumption by a materials manufacturer, including for the manufacturing of new products.\n**(G) State**\nThe term State has the meaning given the term in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ).\n**(2) Definition of processing**\nIn subparagraphs (E) and (F) of paragraph (1), the term processing means any mechanical, manual, or other method that\u2014\n**(A)**\ntransforms a recyclable material into a specification-grade commodity; and\n**(B)**\nmay occur in multiple steps, with different phases, including sorting, occurring at different locations.\n##### (b) Reports on composting and recycling infrastructure capabilities\n**(1) In general**\nSubtitle D of the Solid Waste Disposal Act ( 42 U.S.C. 6941 et seq. ) is amended by adding at the end the following:\n4011. Reports on composting and recycling infrastructure capabilities (a) Definitions In this section: (1) Incorporation of certain terms The terms compost , compostable material , recyclable material , and recycling have the meanings given the terms in section 3(a) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 . (2) Composting facility The term composting facility means a location, structure, or device that transforms compostable materials into compost. (3) Indian tribe The term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (4) Materials recovery facility (A) In general The term materials recovery facility means a dedicated facility where primarily residential recyclable materials, which are diverted from disposal by the generator and collected separately from municipal solid waste, are mechanically or manually sorted into commodities for further processing into specification-grade commodities for sale to end users. (B) Exclusion The term materials recovery facility does not include a solid waste management facility that may process municipal solid waste to remove recyclable materials. (C) Definition of processing For purposes of this paragraph, the term processing has the meaning given the term in section 3(a)(2) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 . (b) Report (1) In general The Administrator shall request information and data from, collaborate with, or contract with, as necessary and appropriate, States, units of local government, and Indian Tribes, for the provision, preparation, and publication of a report, or to expand work under the National Recycling Strategy to include information and data, on compostable materials and efforts to reduce contamination rates for recycling, including\u2014 (A) an evaluation of existing Federal, State, and local laws that may present barriers to implementation of composting strategies; (B) a description and evaluation of composting infrastructure and programs within States, units of local government, and Indian Tribes; (C) an estimate of the costs and approximate land needed to expand composting programs; and (D) a review of the practices of manufacturers and companies that are moving to using compostable packaging and food service ware for the purpose of making the composting process the end-of-life use of those products. (2) Submission Not later than 2 years after the date of enactment of this section, the Administrator shall submit to Congress the report prepared under paragraph (1). (c) Inventory of materials recovery facilities Not later than 3 years after the date of enactment of this section, and every 4 years thereafter, the Administrator, in consultation with relevant Federal agencies and States, units of local government, and Indian Tribes, shall\u2014 (1) prepare an inventory or estimate of materials recovery facilities in the United States, including\u2014 (A) the number of materials recovery facilities in each State; and (B) a general description of the materials that each of those materials recovery facilities can process, including\u2014 (i) in the case of plastic, a description of\u2014 (I) the types of accepted resin, if applicable; and (II) the packaging or product format, such as a jug, a carton, or film; (ii) food packaging and service ware, such as a bottle, cutlery, or a cup; (iii) paper; (iv) aluminum, such as an aluminum beverage can, food can, aerosol can, or foil; (v) steel, such as a steel food or aerosol can; (vi) other scrap metal; (vii) glass; or (viii) any other material not described in any of clauses (i) through (vii) that a materials recovery facility processes; and (2) submit to Congress the inventory or estimate prepared under paragraph (1). (d) Information on recycling and composting systems The Administrator shall, as necessary and appropriate, collaborate or contract with States, units of local government, and Indian Tribes to estimate, with respect to the United States\u2014 (1) the number and types of recycling and composting programs; (2) the types and forms of materials accepted by recycling or composting programs; (3) the number of individuals\u2014 (A) with access to recycling and composting services to at least the extent of access to disposal services; and (B) who use, on a percentage basis, the recycling and composting services described in subparagraph (A); (4) the number of individuals with barriers to accessing recycling and composting services similar to their access to disposal services and the types of those barriers experienced; (5) the inbound contamination and capture rates of recycling and composting programs; (6) if applicable, other available recycling or composting programs; and (7) the average costs and benefits to States, units of local government, and Indian Tribes of recycling and composting programs. (e) Recycling reporting rates (1) Collection of data; development of rates The Administrator may use amounts made available under section 3(e) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 \u2014 (A) to biannually collect, in collaboration with States, to the extent practicable, information supplied on a voluntary basis to develop the estimated rates described in subparagraphs (B) and (C); (B) to develop a standardized estimated rate of recyclable materials in States that provide information under subparagraph (A) that have been successfully diverted from the waste stream and brought to a materials recovery facility or composting facility; and (C) to develop an estimated national recycling rate based on the information described in subparagraphs (A) and (B). (2) Use Using amounts made available under section 3(e) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 , the Administrator may use the information collected and rates developed under paragraph (1) to provide requesting States, units of local government, and Indian Tribes data and technical assistance\u2014 (A) to reduce the overall waste produced by the States, units of local government, and Indian Tribes; (B) to assist the States, units of local government, and Indian Tribes in understanding the nuances of the information collected relating to diversion activities; and (C) to increase recycling and composting rates of the States, units of local government, and Indian Tribes. (f) Report on end markets The Administrator, in collaboration or contract with, as necessary and appropriate, relevant Federal agencies, States, units of local government, or Indian Tribes, shall\u2014 (1) provide an update to the report submitted under section 306 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ; 134 Stat. 1096) to include an addendum on the end-market sale of all recyclable materials from materials recovery facilities that process recyclable materials, including, to the extent practicable\u2014 (A) the total, in dollars per ton, domestic sales of bales of recyclable materials; and (B) the total, in dollars per ton, international sales of bales of recyclable materials; (2) prepare a report on the end-market sale of compost from, to the extent practicable, compostable materials, including the total, in dollars per ton, of domestic sales of compostable materials; and (3) not later than 3 years after the date of enactment of this section, submit to Congress the update to the report prepared under paragraph (1) and the report prepared under paragraph (2). (g) Privileged or confidential information (1) In general Information collected under subsection (e)(1) or paragraph (1) or (2) of subsection (f) shall not include any privileged or confidential information described in section 552(b)(4) of title 5, United States Code. (2) Nondisclosure Information collected to carry out this section shall not be made public if the information meets the requirements of section 552(b) of title 5, United States Code. .\n**(2) Clerical amendment**\nThe table of contents in section 1001 of the Solid Waste Disposal Act ( Public Law 89\u2013272 ; 90 Stat. 2795; 98 Stat. 3268) is amended by inserting after the item relating to section 4010 the following:\nSec. 4011. Report on composting and recycling infrastructure capabilities. .\n##### (c) Federal agency activities related to recycling\nNot later than 2 years after the date of enactment of this Act, and every 2 years thereafter until 2033, the Comptroller General of the United States shall make publicly available a report\u2014\n**(1)**\ndetailing or, to the extent practicable, providing an estimate of\u2014\n**(A)**\nthe total annual recycling and composting rates reported by all Federal agencies; and\n**(B)**\nthe total annual percentage of products containing recyclable material, compostable material, or recovered materials purchased by all Federal agencies, including\u2014\n**(i)**\nthe total quantity of procured products containing recyclable material or recovered materials listed in the comprehensive procurement guidelines published under section 6002(e) of the Solid Waste Disposal Act ( 42 U.S.C. 6962(e) ); and\n**(ii)**\nthe total quantity of compostable material purchased by all Federal agencies;\n**(2)**\nidentifying the activities of each Federal agency that promote recycling or composting; and\n**(3)**\nidentifying activities that Federal agencies could carry out to further promote recycling or composting.\n##### (d) Study on the diversion of recyclable materials from a circular market\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Administrator shall develop a metric for determining the proportion of recyclable materials in commercial and municipal waste streams that are being diverted from a circular market.\n**(2) Study; report**\nNot later than 1 year after the development of a metric under paragraph (1), the Administrator shall conduct a study of, and submit to Congress a report on, the proportion of recyclable materials in commercial and municipal waste streams that, during each of the 10 calendar years preceding the year of submission of the report, were diverted from a circular market.\n**(3) Data**\nThe report under paragraph (2) shall provide data on specific recyclable materials, including aluminum, plastics, paper and paperboard, textiles, and glass, that were prevented from remaining in a circular market through disposal or elimination, and to what use those specific recyclable materials were lost.\n**(4) Evaluation**\nThe report under paragraph (2) shall include an evaluation of whether the establishment or improvement of recycling programs would\u2014\n**(A)**\nimprove recycling rates;\n**(B)**\nreduce the quantity of recyclable materials being unutilized in a circular market; and\n**(C)**\naffect prices paid by consumers for products using materials recycled in the circular market.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section and the amendments made by this section $4,000,000 for each of fiscal years 2025 through 2029.\n##### (f) Administration\n**(1) Unfunded mandates**\nThe Administrator or the Secretary of Commerce may not exercise any authority under this section or any amendment made by this section if exercising that authority would require a State, a unit of local government, or an Indian Tribe to carry out a mandate for which funding is not available.\n**(2) Nondisclosure**\nAny information collected to carry out this section shall not be made public if the information meets the requirements of section 552(b) of title 5, United States Code.",
      "versionDate": "2025-01-30",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s351rs.xml",
      "text": "II\nCalendar No. 7\n119th CONGRESS\n1st Session\nS. 351\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mrs. Capito (for herself, Mr. Whitehouse , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nFebruary 5, 2025 Reported by Mrs. Capito , without amendment\nA BILL\nTo establish a pilot grant program to improve recycling accessibility, to require the Administrator of the Environmental Protection Agency to carry out certain activities to collect and disseminate data on recycling and composting programs in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 or the STEWARD Act of 2025 .\n#### 2. Recycling infrastructure and accessibility improvements\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Curbside recycling**\nThe term curbside recycling means the process by which residential recyclable materials are picked up curbside.\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State (as defined in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ));\n**(B)**\na unit of local government;\n**(C)**\nan Indian Tribe; and\n**(D)**\na public-private partnership or entities seeking to establish a public-private partnership.\n**(4) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(5) Materials recovery facility**\n**(A) In general**\nThe term materials recovery facility means a dedicated facility where primarily residential recyclable materials, which are diverted from disposal by a generator and collected separately from municipal solid waste, are mechanically or manually sorted into commodities for further processing into specification-grade commodities for sale to end users.\n**(B) Exclusion**\nThe term materials recovery facility does not include a solid waste management facility that may process municipal solid waste to remove recyclable materials.\n**(6) Pilot grant program**\nThe term pilot grant program means the Recycling Infrastructure and Accessibility Program established under subsection (b).\n**(7) Recyclable material**\nThe term recyclable material means a material that is obsolete, previously used, off-specification, surplus, or incidentally produced for processing into a specification-grade commodity for which a reuse market currently exists or is being developed.\n**(8) Transfer station**\nThe term transfer station means a facility that\u2014\n**(A)**\nreceives and consolidates recyclable material from curbside recycling or drop-off facilities; and\n**(B)**\nloads the recyclable material onto tractor trailers, railcars, or barges for transport to a distant materials recovery facility or another recycling-related facility.\n**(9) Underserved community**\nThe term underserved community means a community, including an unincorporated area, without access to full recycling services because\u2014\n**(A)**\ntransportation, distance, or other reasons render utilization of available processing capacity at an existing materials recovery facility cost prohibitive; or\n**(B)**\nthe processing capacity of an existing materials recovery facility is insufficient to manage the volume of recyclable materials produced by that community.\n##### (b) Establishment\nNot later than 18 months after the date of enactment of this Act, the Administrator shall establish a pilot grant program, to be known as the Recycling Infrastructure and Accessibility Program , to award grants, on a competitive basis, to eligible entities to improve recycling accessibility in a community or communities within the same geographic area.\n##### (c) Goal\nThe goal of the pilot grant program is to fund eligible projects that will significantly improve accessibility to recycling systems through investments in infrastructure in underserved communities through the use of a hub-and-spoke model for recycling infrastructure development.\n##### (d) Applications\nTo be eligible to receive a grant under the pilot grant program, an eligible entity shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require.\n##### (e) Considerations\nIn selecting eligible entities to receive a grant under the pilot grant program, the Administrator shall consider\u2014\n**(1)**\nwhether the community or communities in which the eligible entity is seeking to carry out a proposed project has curbside recycling;\n**(2)**\nwhether the proposed project of the eligible entity will improve accessibility to recycling services in a single underserved community or multiple underserved communities; and\n**(3)**\n**(A)**\nif the eligible entity is a public-private partnership, the financial health of the private entity seeking to enter into that public-private partnership; or\n**(B)**\nif the eligible entity is seeking to establish a public-private partnership, the financial health of the private entities that would participate in the public-private partnership.\n##### (f) Priority\nIn selecting eligible entities to receive a grant under the pilot grant program, the Administrator shall give priority to eligible entities seeking to carry out a proposed project in a community in which there is not more than 1 materials recovery facility within a 75-mile radius of that community.\n##### (g) Use of funds\nAn eligible entity awarded a grant under the pilot grant program may use the grant funds for projects to improve recycling accessibility in communities, including in underserved communities, by\u2014\n**(1)**\nincreasing the number of transfer stations;\n**(2)**\nexpanding curbside recycling collection programs where appropriate; and\n**(3)**\nleveraging public-private partnerships to reduce the costs associated with collecting and transporting recyclable materials in underserved communities.\n##### (h) Prohibition on use of funds\nAn eligible entity awarded a grant under the pilot grant program may not use the grant funds for projects relating to recycling education programs.\n##### (i) Minimum and maximum grant amount\nA grant awarded to an eligible entity under the pilot grant program shall be in an amount\u2014\n**(1)**\nnot less than $500,000; and\n**(2)**\nnot more than $15,000,000.\n##### (j) Set-Aside\nThe Administrator shall set aside not less than 70 percent of the amounts made available to carry out the pilot grant program for each fiscal year to award grants to eligible entities to carry out a proposed project or program in a single underserved community or multiple underserved communities.\n##### (k) Federal share\nThe Federal share of the cost of a project or program carried out by an eligible entity using grant funds shall be not more than 95 percent.\n##### (l) Report\nNot later than 2 years after the date on which the first grant is awarded under the pilot grant program, the Administrator shall submit to Congress a report describing the implementation of the pilot grant program, which shall include\u2014\n**(1)**\na list of eligible entities that have received a grant under the pilot grant program;\n**(2)**\nthe actions taken by each eligible entity that received a grant under the pilot grant program to improve recycling accessibility with grant funds; and\n**(3)**\nto the extent information is available, a description of how grant funds received under the pilot grant program improved recycling rates in each community in which a project or program was carried out under the pilot grant program.\n##### (m) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Administrator to carry out the pilot grant program $30,000,000 for each of fiscal years 2025 through 2029, to remain available until expended.\n**(2) Administrative costs and technical assistance**\nOf the amounts made available under paragraph (1), the Administrator may use up to 5 percent\u2014\n**(A)**\nfor administrative costs relating to carrying out the pilot grant program; and\n**(B)**\nto provide technical assistance to eligible entities applying for a grant under the pilot grant program.\n#### 3. Recycling and composting data collection\n##### (a) Definitions\n**(1) In general**\nIn this section:\n**(A) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(B) Compost**\nThe term compost means a product that\u2014\n**(i)**\nis manufactured through the controlled aerobic, biological decomposition of biodegradable materials;\n**(ii)**\nhas been subjected to medium and high temperature organisms, which\u2014\n**(I)**\nsignificantly reduce the viability of pathogens and weed seeds; and\n**(II)**\nstabilize carbon in the product such that the product is beneficial to plant growth; and\n**(iii)**\nis typically used as a soil amendment, but may also contribute plant nutrients.\n**(C) Compostable material**\nThe term compostable material means material that is a feedstock for creating compost, including\u2014\n**(i)**\nwood;\n**(ii)**\nagricultural crops;\n**(iii)**\npaper, such as cardboard and other paper products;\n**(iv)**\ncertified compostable products associated with organic waste;\n**(v)**\nother organic plant material;\n**(vi)**\norganic waste, including food waste and yard waste; and\n**(vii)**\nsuch other material that is composed of biomass that can be continually replenished or renewed, as determined by the Administrator.\n**(D) Indian tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(E) Recyclable material**\nThe term recyclable material means a material that is obsolete, previously used, off-specification, surplus, or incidentally produced for processing into a specification-grade commodity for which a reuse market currently exists or is being developed.\n**(F) Recycling**\nThe term recycling means the series of activities\u2014\n**(i)**\nduring which recyclable materials are processed into specification-grade commodities and consumed as raw-material feedstock, in lieu of virgin materials, in the manufacturing of new products;\n**(ii)**\nthat may, with regard to recyclable materials and prior to the activities described in clause (i), include sorting, collection, processing, and brokering; and\n**(iii)**\nthat result, subsequent to processing described in clause (i), in consumption by a materials manufacturer, including for the manufacturing of new products.\n**(G) State**\nThe term State has the meaning given the term in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ).\n**(2) Definition of processing**\nIn subparagraphs (E) and (F) of paragraph (1), the term processing means any mechanical, manual, or other method that\u2014\n**(A)**\ntransforms a recyclable material into a specification-grade commodity; and\n**(B)**\nmay occur in multiple steps, with different phases, including sorting, occurring at different locations.\n##### (b) Reports on composting and recycling infrastructure capabilities\n**(1) In general**\nSubtitle D of the Solid Waste Disposal Act ( 42 U.S.C. 6941 et seq. ) is amended by adding at the end the following:\n4011. Reports on composting and recycling infrastructure capabilities (a) Definitions In this section: (1) Incorporation of certain terms The terms compost , compostable material , recyclable material , and recycling have the meanings given the terms in section 3(a) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 . (2) Composting facility The term composting facility means a location, structure, or device that transforms compostable materials into compost. (3) Indian tribe The term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (4) Materials recovery facility (A) In general The term materials recovery facility means a dedicated facility where primarily residential recyclable materials, which are diverted from disposal by the generator and collected separately from municipal solid waste, are mechanically or manually sorted into commodities for further processing into specification-grade commodities for sale to end users. (B) Exclusion The term materials recovery facility does not include a solid waste management facility that may process municipal solid waste to remove recyclable materials. (C) Definition of processing For purposes of this paragraph, the term processing has the meaning given the term in section 3(a)(2) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 . (b) Report (1) In general The Administrator shall request information and data from, collaborate with, or contract with, as necessary and appropriate, States, units of local government, and Indian Tribes, for the provision, preparation, and publication of a report, or to expand work under the National Recycling Strategy to include information and data, on compostable materials and efforts to reduce contamination rates for recycling, including\u2014 (A) an evaluation of existing Federal, State, and local laws that may present barriers to implementation of composting strategies; (B) a description and evaluation of composting infrastructure and programs within States, units of local government, and Indian Tribes; (C) an estimate of the costs and approximate land needed to expand composting programs; and (D) a review of the practices of manufacturers and companies that are moving to using compostable packaging and food service ware for the purpose of making the composting process the end-of-life use of those products. (2) Submission Not later than 2 years after the date of enactment of this section, the Administrator shall submit to Congress the report prepared under paragraph (1). (c) Inventory of materials recovery facilities Not later than 3 years after the date of enactment of this section, and every 4 years thereafter, the Administrator, in consultation with relevant Federal agencies and States, units of local government, and Indian Tribes, shall\u2014 (1) prepare an inventory or estimate of materials recovery facilities in the United States, including\u2014 (A) the number of materials recovery facilities in each State; and (B) a general description of the materials that each of those materials recovery facilities can process, including\u2014 (i) in the case of plastic, a description of\u2014 (I) the types of accepted resin, if applicable; and (II) the packaging or product format, such as a jug, a carton, or film; (ii) food packaging and service ware, such as a bottle, cutlery, or a cup; (iii) paper; (iv) aluminum, such as an aluminum beverage can, food can, aerosol can, or foil; (v) steel, such as a steel food or aerosol can; (vi) other scrap metal; (vii) glass; or (viii) any other material not described in any of clauses (i) through (vii) that a materials recovery facility processes; and (2) submit to Congress the inventory or estimate prepared under paragraph (1). (d) Information on recycling and composting systems The Administrator shall, as necessary and appropriate, collaborate or contract with States, units of local government, and Indian Tribes to estimate, with respect to the United States\u2014 (1) the number and types of recycling and composting programs; (2) the types and forms of materials accepted by recycling or composting programs; (3) the number of individuals\u2014 (A) with access to recycling and composting services to at least the extent of access to disposal services; and (B) who use, on a percentage basis, the recycling and composting services described in subparagraph (A); (4) the number of individuals with barriers to accessing recycling and composting services similar to their access to disposal services and the types of those barriers experienced; (5) the inbound contamination and capture rates of recycling and composting programs; (6) if applicable, other available recycling or composting programs; and (7) the average costs and benefits to States, units of local government, and Indian Tribes of recycling and composting programs. (e) Recycling reporting rates (1) Collection of data; development of rates The Administrator may use amounts made available under section 3(e) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 \u2014 (A) to biannually collect, in collaboration with States, to the extent practicable, information supplied on a voluntary basis to develop the estimated rates described in subparagraphs (B) and (C); (B) to develop a standardized estimated rate of recyclable materials in States that provide information under subparagraph (A) that have been successfully diverted from the waste stream and brought to a materials recovery facility or composting facility; and (C) to develop an estimated national recycling rate based on the information described in subparagraphs (A) and (B). (2) Use Using amounts made available under section 3(e) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 , the Administrator may use the information collected and rates developed under paragraph (1) to provide requesting States, units of local government, and Indian Tribes data and technical assistance\u2014 (A) to reduce the overall waste produced by the States, units of local government, and Indian Tribes; (B) to assist the States, units of local government, and Indian Tribes in understanding the nuances of the information collected relating to diversion activities; and (C) to increase recycling and composting rates of the States, units of local government, and Indian Tribes. (f) Report on end markets The Administrator, in collaboration or contract with, as necessary and appropriate, relevant Federal agencies, States, units of local government, or Indian Tribes, shall\u2014 (1) provide an update to the report submitted under section 306 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ; 134 Stat. 1096) to include an addendum on the end-market sale of all recyclable materials from materials recovery facilities that process recyclable materials, including, to the extent practicable\u2014 (A) the total, in dollars per ton, domestic sales of bales of recyclable materials; and (B) the total, in dollars per ton, international sales of bales of recyclable materials; (2) prepare a report on the end-market sale of compost from, to the extent practicable, compostable materials, including the total, in dollars per ton, of domestic sales of compostable materials; and (3) not later than 3 years after the date of enactment of this section, submit to Congress the update to the report prepared under paragraph (1) and the report prepared under paragraph (2). (g) Privileged or confidential information (1) In general Information collected under subsection (e)(1) or paragraph (1) or (2) of subsection (f) shall not include any privileged or confidential information described in section 552(b)(4) of title 5, United States Code. (2) Nondisclosure Information collected to carry out this section shall not be made public if the information meets the requirements of section 552(b) of title 5, United States Code. .\n**(2) Clerical amendment**\nThe table of contents in section 1001 of the Solid Waste Disposal Act ( Public Law 89\u2013272 ; 90 Stat. 2795; 98 Stat. 3268) is amended by inserting after the item relating to section 4010 the following:\nSec. 4011. Report on composting and recycling infrastructure capabilities. .\n##### (c) Federal agency activities related to recycling\nNot later than 2 years after the date of enactment of this Act, and every 2 years thereafter until 2033, the Comptroller General of the United States shall make publicly available a report\u2014\n**(1)**\ndetailing or, to the extent practicable, providing an estimate of\u2014\n**(A)**\nthe total annual recycling and composting rates reported by all Federal agencies; and\n**(B)**\nthe total annual percentage of products containing recyclable material, compostable material, or recovered materials purchased by all Federal agencies, including\u2014\n**(i)**\nthe total quantity of procured products containing recyclable material or recovered materials listed in the comprehensive procurement guidelines published under section 6002(e) of the Solid Waste Disposal Act ( 42 U.S.C. 6962(e) ); and\n**(ii)**\nthe total quantity of compostable material purchased by all Federal agencies;\n**(2)**\nidentifying the activities of each Federal agency that promote recycling or composting; and\n**(3)**\nidentifying activities that Federal agencies could carry out to further promote recycling or composting.\n##### (d) Study on the diversion of recyclable materials from a circular market\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Administrator shall develop a metric for determining the proportion of recyclable materials in commercial and municipal waste streams that are being diverted from a circular market.\n**(2) Study; report**\nNot later than 1 year after the development of a metric under paragraph (1), the Administrator shall conduct a study of, and submit to Congress a report on, the proportion of recyclable materials in commercial and municipal waste streams that, during each of the 10 calendar years preceding the year of submission of the report, were diverted from a circular market.\n**(3) Data**\nThe report under paragraph (2) shall provide data on specific recyclable materials, including aluminum, plastics, paper and paperboard, textiles, and glass, that were prevented from remaining in a circular market through disposal or elimination, and to what use those specific recyclable materials were lost.\n**(4) Evaluation**\nThe report under paragraph (2) shall include an evaluation of whether the establishment or improvement of recycling programs would\u2014\n**(A)**\nimprove recycling rates;\n**(B)**\nreduce the quantity of recyclable materials being unutilized in a circular market; and\n**(C)**\naffect prices paid by consumers for products using materials recycled in the circular market.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section and the amendments made by this section $4,000,000 for each of fiscal years 2025 through 2029.\n##### (f) Administration\n**(1) Unfunded mandates**\nThe Administrator or the Secretary of Commerce may not exercise any authority under this section or any amendment made by this section if exercising that authority would require a State, a unit of local government, or an Indian Tribe to carry out a mandate for which funding is not available.\n**(2) Nondisclosure**\nAny information collected to carry out this section shall not be made public if the information meets the requirements of section 552(b) of title 5, United States Code.",
      "versionDate": "2025-02-05",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s351es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 351\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo establish a pilot grant program to improve recycling accessibility, to require the Administrator of the Environmental Protection Agency to carry out certain activities to collect and disseminate data on recycling and composting programs in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 or the STEWARD Act of 2025 .\n#### 2. Recycling infrastructure and accessibility improvements\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Curbside recycling**\nThe term curbside recycling means the process by which residential recyclable materials are picked up curbside.\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State (as defined in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ));\n**(B)**\na unit of local government;\n**(C)**\nan Indian Tribe; and\n**(D)**\na public-private partnership or entities seeking to establish a public-private partnership.\n**(4) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(5) Materials recovery facility**\n**(A) In general**\nThe term materials recovery facility means a dedicated facility where primarily residential recyclable materials, which are diverted from disposal by a generator and collected separately from municipal solid waste, are mechanically or manually sorted into commodities for further processing into specification-grade commodities for sale to end users.\n**(B) Exclusion**\nThe term materials recovery facility does not include a solid waste management facility that may process municipal solid waste to remove recyclable materials.\n**(6) Pilot grant program**\nThe term pilot grant program means the Recycling Infrastructure and Accessibility Program established under subsection (b).\n**(7) Recyclable material**\nThe term recyclable material means a material that is obsolete, previously used, off-specification, surplus, or incidentally produced for processing into a specification-grade commodity for which a reuse market currently exists or is being developed.\n**(8) Transfer station**\nThe term transfer station means a facility that\u2014\n**(A)**\nreceives and consolidates recyclable material from curbside recycling or drop-off facilities; and\n**(B)**\nloads the recyclable material onto tractor trailers, railcars, or barges for transport to a distant materials recovery facility or another recycling-related facility.\n**(9) Underserved community**\nThe term underserved community means a community, including an unincorporated area, without access to full recycling services because\u2014\n**(A)**\ntransportation, distance, or other reasons render utilization of available processing capacity at an existing materials recovery facility cost prohibitive; or\n**(B)**\nthe processing capacity of an existing materials recovery facility is insufficient to manage the volume of recyclable materials produced by that community.\n##### (b) Establishment\nNot later than 18 months after the date of enactment of this Act, the Administrator shall establish a pilot grant program, to be known as the Recycling Infrastructure and Accessibility Program , to award grants, on a competitive basis, to eligible entities to improve recycling accessibility in a community or communities within the same geographic area.\n##### (c) Goal\nThe goal of the pilot grant program is to fund eligible projects that will significantly improve accessibility to recycling systems through investments in infrastructure in underserved communities through the use of a hub-and-spoke model for recycling infrastructure development.\n##### (d) Applications\nTo be eligible to receive a grant under the pilot grant program, an eligible entity shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require.\n##### (e) Considerations\nIn selecting eligible entities to receive a grant under the pilot grant program, the Administrator shall consider\u2014\n**(1)**\nwhether the community or communities in which the eligible entity is seeking to carry out a proposed project has curbside recycling;\n**(2)**\nwhether the proposed project of the eligible entity will improve accessibility to recycling services in a single underserved community or multiple underserved communities; and\n**(3)**\n**(A)**\nif the eligible entity is a public-private partnership, the financial health of the private entity seeking to enter into that public-private partnership; or\n**(B)**\nif the eligible entity is seeking to establish a public-private partnership, the financial health of the private entities that would participate in the public-private partnership.\n##### (f) Priority\nIn selecting eligible entities to receive a grant under the pilot grant program, the Administrator shall give priority to eligible entities seeking to carry out a proposed project in a community in which there is not more than 1 materials recovery facility within a 75-mile radius of that community.\n##### (g) Use of funds\nAn eligible entity awarded a grant under the pilot grant program may use the grant funds for projects to improve recycling accessibility in communities, including in underserved communities, by\u2014\n**(1)**\nincreasing the number of transfer stations;\n**(2)**\nexpanding curbside recycling collection programs where appropriate; and\n**(3)**\nleveraging public-private partnerships to reduce the costs associated with collecting and transporting recyclable materials in underserved communities.\n##### (h) Prohibition on use of funds\nAn eligible entity awarded a grant under the pilot grant program may not use the grant funds for projects relating to recycling education programs.\n##### (i) Minimum and maximum grant amount\nA grant awarded to an eligible entity under the pilot grant program shall be in an amount\u2014\n**(1)**\nnot less than $500,000; and\n**(2)**\nnot more than $15,000,000.\n##### (j) Set-Aside\nThe Administrator shall set aside not less than 70 percent of the amounts made available to carry out the pilot grant program for each fiscal year to award grants to eligible entities to carry out a proposed project or program in a single underserved community or multiple underserved communities.\n##### (k) Federal share\nThe Federal share of the cost of a project or program carried out by an eligible entity using grant funds shall be not more than 95 percent.\n##### (l) Report\nNot later than 2 years after the date on which the first grant is awarded under the pilot grant program, the Administrator shall submit to Congress a report describing the implementation of the pilot grant program, which shall include\u2014\n**(1)**\na list of eligible entities that have received a grant under the pilot grant program;\n**(2)**\nthe actions taken by each eligible entity that received a grant under the pilot grant program to improve recycling accessibility with grant funds; and\n**(3)**\nto the extent information is available, a description of how grant funds received under the pilot grant program improved recycling rates in each community in which a project or program was carried out under the pilot grant program.\n##### (m) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Administrator to carry out the pilot grant program $30,000,000 for each of fiscal years 2025 through 2029, to remain available until expended.\n**(2) Administrative costs and technical assistance**\nOf the amounts made available under paragraph (1), the Administrator may use up to 5 percent\u2014\n**(A)**\nfor administrative costs relating to carrying out the pilot grant program; and\n**(B)**\nto provide technical assistance to eligible entities applying for a grant under the pilot grant program.\n#### 3. Recycling and composting data collection\n##### (a) Definitions\n**(1) In general**\nIn this section:\n**(A) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(B) Compost**\nThe term compost means a product that\u2014\n**(i)**\nis manufactured through the controlled aerobic, biological decomposition of biodegradable materials;\n**(ii)**\nhas been subjected to medium and high temperature organisms, which\u2014\n**(I)**\nsignificantly reduce the viability of pathogens and weed seeds; and\n**(II)**\nstabilize carbon in the product such that the product is beneficial to plant growth; and\n**(iii)**\nis typically used as a soil amendment, but may also contribute plant nutrients.\n**(C) Compostable material**\nThe term compostable material means material that is a feedstock for creating compost, including\u2014\n**(i)**\nwood;\n**(ii)**\nagricultural crops;\n**(iii)**\npaper, such as cardboard and other paper products;\n**(iv)**\ncertified compostable products associated with organic waste;\n**(v)**\nother organic plant material;\n**(vi)**\norganic waste, including food waste and yard waste; and\n**(vii)**\nsuch other material that is composed of biomass that can be continually replenished or renewed, as determined by the Administrator.\n**(D) Indian tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(E) Recyclable material**\nThe term recyclable material means a material that is obsolete, previously used, off-specification, surplus, or incidentally produced for processing into a specification-grade commodity for which a reuse market currently exists or is being developed.\n**(F) Recycling**\nThe term recycling means the series of activities\u2014\n**(i)**\nduring which recyclable materials are processed into specification-grade commodities and consumed as raw-material feedstock, in lieu of virgin materials, in the manufacturing of new products;\n**(ii)**\nthat may, with regard to recyclable materials and prior to the activities described in clause (i), include sorting, collection, processing, and brokering; and\n**(iii)**\nthat result, subsequent to processing described in clause (i), in consumption by a materials manufacturer, including for the manufacturing of new products.\n**(G) State**\nThe term State has the meaning given the term in section 1004 of the Solid Waste Disposal Act ( 42 U.S.C. 6903 ).\n**(2) Definition of processing**\nIn subparagraphs (E) and (F) of paragraph (1), the term processing means any mechanical, manual, or other method that\u2014\n**(A)**\ntransforms a recyclable material into a specification-grade commodity; and\n**(B)**\nmay occur in multiple steps, with different phases, including sorting, occurring at different locations.\n##### (b) Reports on composting and recycling infrastructure capabilities\n**(1) In general**\nSubtitle D of the Solid Waste Disposal Act ( 42 U.S.C. 6941 et seq. ) is amended by adding at the end the following:\n4011. Reports on composting and recycling infrastructure capabilities (a) Definitions In this section: (1) Incorporation of certain terms The terms compost , compostable material , recyclable material , and recycling have the meanings given the terms in section 3(a) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 . (2) Composting facility The term composting facility means a location, structure, or device that transforms compostable materials into compost. (3) Indian tribe The term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (4) Materials recovery facility (A) In general The term materials recovery facility means a dedicated facility where primarily residential recyclable materials, which are diverted from disposal by the generator and collected separately from municipal solid waste, are mechanically or manually sorted into commodities for further processing into specification-grade commodities for sale to end users. (B) Exclusion The term materials recovery facility does not include a solid waste management facility that may process municipal solid waste to remove recyclable materials. (C) Definition of processing For purposes of this paragraph, the term processing has the meaning given the term in section 3(a)(2) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 . (b) Report (1) In general The Administrator shall request information and data from, collaborate with, or contract with, as necessary and appropriate, States, units of local government, and Indian Tribes, for the provision, preparation, and publication of a report, or to expand work under the National Recycling Strategy to include information and data, on compostable materials and efforts to reduce contamination rates for recycling, including\u2014 (A) an evaluation of existing Federal, State, and local laws that may present barriers to implementation of composting strategies; (B) a description and evaluation of composting infrastructure and programs within States, units of local government, and Indian Tribes; (C) an estimate of the costs and approximate land needed to expand composting programs; and (D) a review of the practices of manufacturers and companies that are moving to using compostable packaging and food service ware for the purpose of making the composting process the end-of-life use of those products. (2) Submission Not later than 2 years after the date of enactment of this section, the Administrator shall submit to Congress the report prepared under paragraph (1). (c) Inventory of materials recovery facilities Not later than 3 years after the date of enactment of this section, and every 4 years thereafter, the Administrator, in consultation with relevant Federal agencies and States, units of local government, and Indian Tribes, shall\u2014 (1) prepare an inventory or estimate of materials recovery facilities in the United States, including\u2014 (A) the number of materials recovery facilities in each State; and (B) a general description of the materials that each of those materials recovery facilities can process, including\u2014 (i) in the case of plastic, a description of\u2014 (I) the types of accepted resin, if applicable; and (II) the packaging or product format, such as a jug, a carton, or film; (ii) food packaging and service ware, such as a bottle, cutlery, or a cup; (iii) paper; (iv) aluminum, such as an aluminum beverage can, food can, aerosol can, or foil; (v) steel, such as a steel food or aerosol can; (vi) other scrap metal; (vii) glass; or (viii) any other material not described in any of clauses (i) through (vii) that a materials recovery facility processes; and (2) submit to Congress the inventory or estimate prepared under paragraph (1). (d) Information on recycling and composting systems The Administrator shall, as necessary and appropriate, collaborate or contract with States, units of local government, and Indian Tribes to estimate, with respect to the United States\u2014 (1) the number and types of recycling and composting programs; (2) the types and forms of materials accepted by recycling or composting programs; (3) the number of individuals\u2014 (A) with access to recycling and composting services to at least the extent of access to disposal services; and (B) who use, on a percentage basis, the recycling and composting services described in subparagraph (A); (4) the number of individuals with barriers to accessing recycling and composting services similar to their access to disposal services and the types of those barriers experienced; (5) the inbound contamination and capture rates of recycling and composting programs; (6) if applicable, other available recycling or composting programs; and (7) the average costs and benefits to States, units of local government, and Indian Tribes of recycling and composting programs. (e) Recycling reporting rates (1) Collection of data; development of rates The Administrator may use amounts made available under section 3(e) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 \u2014 (A) to biannually collect, in collaboration with States, to the extent practicable, information supplied on a voluntary basis to develop the estimated rates described in subparagraphs (B) and (C); (B) to develop a standardized estimated rate of recyclable materials in States that provide information under subparagraph (A) that have been successfully diverted from the waste stream and brought to a materials recovery facility or composting facility; and (C) to develop an estimated national recycling rate based on the information described in subparagraphs (A) and (B). (2) Use Using amounts made available under section 3(e) of the Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 , the Administrator may use the information collected and rates developed under paragraph (1) to provide requesting States, units of local government, and Indian Tribes data and technical assistance\u2014 (A) to reduce the overall waste produced by the States, units of local government, and Indian Tribes; (B) to assist the States, units of local government, and Indian Tribes in understanding the nuances of the information collected relating to diversion activities; and (C) to increase recycling and composting rates of the States, units of local government, and Indian Tribes. (f) Report on end markets The Administrator, in collaboration or contract with, as necessary and appropriate, relevant Federal agencies, States, units of local government, or Indian Tribes, shall\u2014 (1) provide an update to the report submitted under section 306 of the Save Our Seas 2.0 Act ( Public Law 116\u2013224 ; 134 Stat. 1096) to include an addendum on the end-market sale of all recyclable materials from materials recovery facilities that process recyclable materials, including, to the extent practicable\u2014 (A) the total, in dollars per ton, domestic sales of bales of recyclable materials; and (B) the total, in dollars per ton, international sales of bales of recyclable materials; (2) prepare a report on the end-market sale of compost from, to the extent practicable, compostable materials, including the total, in dollars per ton, of domestic sales of compostable materials; and (3) not later than 3 years after the date of enactment of this section, submit to Congress the update to the report prepared under paragraph (1) and the report prepared under paragraph (2). (g) Privileged or confidential information (1) In general Information collected under subsection (e)(1) or paragraph (1) or (2) of subsection (f) shall not include any privileged or confidential information described in section 552(b)(4) of title 5, United States Code. (2) Nondisclosure Information collected to carry out this section shall not be made public if the information meets the requirements of section 552(b) of title 5, United States Code. .\n**(2) Clerical amendment**\nThe table of contents in section 1001 of the Solid Waste Disposal Act ( Public Law 89\u2013272 ; 90 Stat. 2795; 98 Stat. 3268) is amended by inserting after the item relating to section 4010 the following:\nSec. 4011. Report on composting and recycling infrastructure capabilities. .\n##### (c) Federal agency activities related to recycling\nNot later than 2 years after the date of enactment of this Act, and every 2 years thereafter until 2033, the Comptroller General of the United States shall make publicly available a report\u2014\n**(1)**\ndetailing or, to the extent practicable, providing an estimate of\u2014\n**(A)**\nthe total annual recycling and composting rates reported by all Federal agencies; and\n**(B)**\nthe total annual percentage of products containing recyclable material, compostable material, or recovered materials purchased by all Federal agencies, including\u2014\n**(i)**\nthe total quantity of procured products containing recyclable material or recovered materials listed in the comprehensive procurement guidelines published under section 6002(e) of the Solid Waste Disposal Act ( 42 U.S.C. 6962(e) ); and\n**(ii)**\nthe total quantity of compostable material purchased by all Federal agencies;\n**(2)**\nidentifying the activities of each Federal agency that promote recycling or composting; and\n**(3)**\nidentifying activities that Federal agencies could carry out to further promote recycling or composting.\n##### (d) Study on the diversion of recyclable materials from a circular market\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Administrator shall develop a metric for determining the proportion of recyclable materials in commercial and municipal waste streams that are being diverted from a circular market.\n**(2) Study; report**\nNot later than 1 year after the development of a metric under paragraph (1), the Administrator shall conduct a study of, and submit to Congress a report on, the proportion of recyclable materials in commercial and municipal waste streams that, during each of the 10 calendar years preceding the year of submission of the report, were diverted from a circular market.\n**(3) Data**\nThe report under paragraph (2) shall provide data on specific recyclable materials, including aluminum, plastics, paper and paperboard, textiles, and glass, that were prevented from remaining in a circular market through disposal or elimination, and to what use those specific recyclable materials were lost.\n**(4) Evaluation**\nThe report under paragraph (2) shall include an evaluation of whether the establishment or improvement of recycling programs would\u2014\n**(A)**\nimprove recycling rates;\n**(B)**\nreduce the quantity of recyclable materials being unutilized in a circular market; and\n**(C)**\naffect prices paid by consumers for products using materials recycled in the circular market.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section and the amendments made by this section $4,000,000 for each of fiscal years 2025 through 2029.\n##### (f) Administration\n**(1) Unfunded mandates**\nThe Administrator or the Secretary of Commerce may not exercise any authority under this section or any amendment made by this section if exercising that authority would require a State, a unit of local government, or an Indian Tribe to carry out a mandate for which funding is not available.\n**(2) Nondisclosure**\nAny information collected to carry out this section shall not be made public if the information meets the requirements of section 552(b) of title 5, United States Code.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2145",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recycling Infrastructure and Accessibility Act of 2025",
      "type": "HR"
    },
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-02-12T14:03:56Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-12T14:04:10Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-02-12T14:04:03Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-02-12T14:03:39Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-02-12T14:03:48Z"
          },
          {
            "name": "Solid waste and recycling",
            "updateDate": "2025-02-12T14:03:26Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-12T14:03:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-02-05T16:39:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119s351",
          "measure-number": "351",
          "measure-type": "s",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2026-02-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s351v25",
            "update-date": "2026-02-26"
          },
          "action-date": "2025-02-05",
          "action-desc": "Reported to Senate",
          "summary-text": "<p><strong>Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 or the STEWARD Act of 2025</strong></p><p>This bill establishes requirements to expand recycling and composting efforts, including by creating (1) a pilot grant program, and (2) data collection and reporting requirements.</p><p>The bill directs the Environmental Protection Agency (EPA) to establish a pilot program that awards grants for improving recycling accessibility in communities, particularly in underserved communities. States, local governments, Indian tribes, and public-private partnerships may apply for those grants.</p><p>The bill also directs the EPA to\u00a0collect\u00a0data related to composting and recycling infrastructure from states, local governments, and Indian tribes. Within three years and every four years thereafter, the EPA must prepare an inventory of certain recycling facilities in the United States. The EPA must also develop a metric for determining the proportion of recyclable materials in commercial and municipal waste streams that are being diverted from a circular market.</p><p>The bill allows the EPA to develop (1) a standardized estimated rate of recyclable materials that have been brought to recycling or composting facilities, and (2) an estimated national recycling rate. The EPA may\u00a0use the rates and information collected to provide states, local government, and Indian tribes data and technical assistance, such as assistance to reduce their overall waste and to increase their recycling and composting rates.</p><p>The bill establishes a variety of reporting requirements for the EPA and directs the\u00a0Government Accountability Office to publish a report on certain federal agency activities related to recycling.</p>"
        },
        "title": "STEWARD Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s351.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 or the STEWARD Act of 2025</strong></p><p>This bill establishes requirements to expand recycling and composting efforts, including by creating (1) a pilot grant program, and (2) data collection and reporting requirements.</p><p>The bill directs the Environmental Protection Agency (EPA) to establish a pilot program that awards grants for improving recycling accessibility in communities, particularly in underserved communities. States, local governments, Indian tribes, and public-private partnerships may apply for those grants.</p><p>The bill also directs the EPA to\u00a0collect\u00a0data related to composting and recycling infrastructure from states, local governments, and Indian tribes. Within three years and every four years thereafter, the EPA must prepare an inventory of certain recycling facilities in the United States. The EPA must also develop a metric for determining the proportion of recyclable materials in commercial and municipal waste streams that are being diverted from a circular market.</p><p>The bill allows the EPA to develop (1) a standardized estimated rate of recyclable materials that have been brought to recycling or composting facilities, and (2) an estimated national recycling rate. The EPA may\u00a0use the rates and information collected to provide states, local government, and Indian tribes data and technical assistance, such as assistance to reduce their overall waste and to increase their recycling and composting rates.</p><p>The bill establishes a variety of reporting requirements for the EPA and directs the\u00a0Government Accountability Office to publish a report on certain federal agency activities related to recycling.</p>",
      "updateDate": "2026-02-26",
      "versionCode": "id119s351"
    },
    "title": "STEWARD Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025 or the STEWARD Act of 2025</strong></p><p>This bill establishes requirements to expand recycling and composting efforts, including by creating (1) a pilot grant program, and (2) data collection and reporting requirements.</p><p>The bill directs the Environmental Protection Agency (EPA) to establish a pilot program that awards grants for improving recycling accessibility in communities, particularly in underserved communities. States, local governments, Indian tribes, and public-private partnerships may apply for those grants.</p><p>The bill also directs the EPA to\u00a0collect\u00a0data related to composting and recycling infrastructure from states, local governments, and Indian tribes. Within three years and every four years thereafter, the EPA must prepare an inventory of certain recycling facilities in the United States. The EPA must also develop a metric for determining the proportion of recyclable materials in commercial and municipal waste streams that are being diverted from a circular market.</p><p>The bill allows the EPA to develop (1) a standardized estimated rate of recyclable materials that have been brought to recycling or composting facilities, and (2) an estimated national recycling rate. The EPA may\u00a0use the rates and information collected to provide states, local government, and Indian tribes data and technical assistance, such as assistance to reduce their overall waste and to increase their recycling and composting rates.</p><p>The bill establishes a variety of reporting requirements for the EPA and directs the\u00a0Government Accountability Office to publish a report on certain federal agency activities related to recycling.</p>",
      "updateDate": "2026-02-26",
      "versionCode": "id119s351"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s351is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s351rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s351es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "STEWARD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T11:03:25Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "STEWARD Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-11-21T13:38:24Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-11-21T13:38:24Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-02-07T04:38:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "STEWARD Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-02-07T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STEWARD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strategies To Eliminate Waste and Accelerate Recycling Development Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a pilot grant program to improve recycling accessibility, to require the Administrator of the Environmental Protection Agency to carry out certain activities to collect and disseminate data on recycling and composting programs in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T15:18:22Z"
    }
  ]
}
```
