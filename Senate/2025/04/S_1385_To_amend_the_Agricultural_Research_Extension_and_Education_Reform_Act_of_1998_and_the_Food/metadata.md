# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1385
- Title: Organic Science and Research Investment Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1385
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-03-26T11:03:17Z
- Update date including text: 2026-03-26T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1385",
    "number": "1385",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Organic Science and Research Investment Act of 2025",
    "type": "S",
    "updateDate": "2026-03-26T11:03:17Z",
    "updateDateIncludingText": "2026-03-26T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-09",
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
            "date": "2025-04-09T19:42:25Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-09T19:42:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "OR"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "WI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "VT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "OR"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-09",
      "state": "ME"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NM"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1385is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1385\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Fetterman (for himself, Mr. Schiff , Mrs. Gillibrand , Mr. Booker , Mr. Merkley , Ms. Baldwin , Ms. Smith , Mr. Welch , Mr. Padilla , Mr. Wyden , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Research, Extension, and Education Reform Act of 1998 and the Food, Agriculture, Conservation, and Trade Act of 1990 to direct the Agricultural Research Service to expand organic research, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Organic Science and Research Investment Act of 2025 .\n#### 2. Coordinating and expanding Organic Research Initiative\nTitle IV of the Agricultural Research, Extension, and Education Reform Act of 1998 is amended by inserting before section 404 ( 7 U.S.C. 7624 ) the following:\n401. Coordinating and expanding Organic Research Initiative (a) Definitions In this section: (1) Initiative The term Initiative means the Coordinating and Expanding Organic Research Initiative established under subsection (b). (2) Secretary The term Secretary means the Secretary, acting through the Under Secretary for Research, Education, and Economics, in consultation with the Office of the Chief Scientist. (b) Establishment The Secretary shall establish, and appoint the members of, an initiative, to be known as the Coordinating and Expanding Organic Research Initiative , to coordinate and expand the resources that the Agricultural Research Service, the National Institute of Food and Agriculture, the Economic Research Service, and the National Agricultural Statistics Service dedicate to organic agricultural research. (c) Duties The Initiative shall carry out the following duties: (1) Coordinating all research conducted by the Secretary that is applicable to organic agricultural producers and transitioning-to-organic agricultural producers. (2) Reviewing and assessing the completed and ongoing organic and transitioning-to-organic agricultural research of the Secretary. (3) Developing iterative strategic plans for future organic and transitioning-to-organic agricultural research of the Secretary. (4) Conducting the surveys and submitting to the Secretary the reports under subsection (e)(1). (d) Appointment of members (1) In general The Secretary shall appoint not fewer than 12, and not more than 18, members to the Initiative. (2) Eligibility To be eligible for appointment to the Initiative under paragraph (1), an individual shall\u2014 (A) be in the competitive service or the Senior Executive Service (as defined in sections 2102 and 2101a of title 5, United States Code); and (B) have expertise in organic agriculture from a science, research, or technical assistance division of a Department agency. (3) Representation In appointing members to the Initiative, the Secretary shall ensure that\u2014 (A) not fewer than 1/4 of the members are appointed from each of\u2014 (i) the Agricultural Research Service; and (ii) the National Institute of Food and Agriculture; and (B) not fewer than 1 member is appointed from each of\u2014 (i) the Office of the Chief Scientist; (ii) the National Organic Program of the Agricultural Marketing Service; (iii) the Economic Research Service; and (iv) the National Agricultural Statistics Service. (4) Chair The Secretary shall designate a member of the Initiative appointed from the Office of the Chief Scientist to serve as the Chair of the Initiative. (5) Term A member of the Initiative\u2014 (A) shall serve for a term of 5 years; and (B) may be reappointed to the Initiative. (e) Surveys; reports (1) In general Not later than 3 years after the establishment of the Initiative, and every 5 years thereafter, in coordination with the roadmap for agricultural research, education, and extension described in section 7504 of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 7614a ), the Initiative shall\u2014 (A) conduct a survey of all research relating to organic agriculture of the Secretary; and (B) submit to the Secretary a report containing the findings of the survey conducted under subparagraph (A), which shall include sections relating to each of the 4 agencies described in subsection (b). (2) Recommendations The Initiative shall include in each report submitted under paragraph (1)(B) recommendations relating to\u2014 (A) expanding the research conducted by the Secretary that\u2014 (i) is applicable to agricultural producers that adhere to the requirements under the national organic program established under the Organic Foods Production Act of 1990 ( 7 U.S.C. 6501 et seq. ); and (ii) would explore the new or enhanced research opportunities that could lead to new discoveries, foster innovation, improve technologies, and promote integrated systems approaches to assist\u2014 (I) organic agricultural producers; (II) consumers of organic food products; (III) organic marketing and distribution channels; (IV) transitioning-to-organic agricultural producers, including with respect to barriers to transitioning to organic production and producers who have considered transitioning to organic production but decided not to do so; and (V) the organic food industry; (B) strategies to increase the coordination and effectiveness of projects carried out by the Secretary that are applicable to organic production and that would improve the efficiency, productivity, profitability, and ecosystem services of organic crop and livestock production, including strategies relating to\u2014 (i) developing new public plant cultivars and livestock breeds that are regionally adapted and appropriate for organic production; (ii) expanding the applicability and cost-effectiveness of integrated, ecologically based pest, weed, and disease management for crop and livestock systems; (iii) developing integrated organic production systems that\u2014 (I) enhance ecosystem services relating to organic crop and livestock production; and (II) optimize agricultural resilience to the impacts of climate change and other stresses, including soil conservation and soil health, biodiversity, water management, carbon sequestration, and greenhouse gas mitigation; (iv) improving the remote sensing and monitoring capabilities for ecosystem services relating to organic crop and livestock production, including soil conservation and soil health, biodiversity, water management, carbon sequestration, and greenhouse gas mitigation; (v) developing grazing, pasture, forage, and livestock manure management techniques that are regionally adapted and appropriate for organic production; (vi) enhancing irrigation and water management techniques used in organic crop and livestock production; (vii) enhancing food safety relating to organic crops and livestock products, including guidance on compliance with the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ); (viii) developing new products and new uses of organic crops and livestock products; (ix) enhancing the quality of organically produced food, including taste, appearance, and nutritional value, after being processed into organic crop and livestock products, through genetic, processing, and related research topics; and (x) other similar, relevant topics, as determined by the Initiative; and (C) the development of data and applied research-based information useful to organic and conventional crop producers, associations of those producers, and other interested beneficiaries in evaluating the organic and conventional crops industries from a regional and national perspective. (3) Review of prior report The Initiative shall include in each report submitted under paragraph (1)(B)\u2014 (A) a review of the recommendations described in paragraph (2) included in the prior report submitted under paragraph (1)(B); and (B) the actions taken by the Secretary to implement those recommendations. (f) Consultation (1) In general In carrying out this section, the Initiative shall engage in consultation, including with\u2014 (A) the National Organic Standards Board; and (B) land-grant colleges and universities. (2) Organic and conventional industries In preparing each report under subsection (e)(1)(B), the Initiative shall consult, on an ongoing basis, with a diverse array of\u2014 (A) organic and conventional farmers, ranchers, handlers; and (B) organizations that serve those farmers, ranchers, and handlers. (g) Consideration by Secretary In preparing the annual budget recommendations for the Department, the Secretary shall take into consideration the findings and recommendations contained in the most recently submitted report under subsection (e)(1)(B). (h) Report by Secretary In the budget material submitted to Congress by the Secretary of Agriculture in connection with the budget of the United States Government submitted by the President under section 1105 of title 31, United States Code, for each fiscal year, the Secretary of Agriculture shall include a report describing how the Secretary addressed each recommendation of the Initiative contained in the most recently submitted report under subsection (e)(1)(B). .\n#### 3. Organic research and extension initiative\nSection 1672B of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925b ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby striking subsection (e) and inserting subsection (f) ; and\n**(ii)**\nby striking 2023 and inserting 2030 ;\n**(B)**\nin paragraph (7), by striking and at the end;\n**(C)**\nin paragraph (8), by striking the period at the end and inserting a semicolon; and\n**(D)**\nby adding at the end the following:\n(9) facilitating the identification and adoption of traditional ecological knowledge in accordance with subsection (e); (10) developing cultural practices and other allowable alternatives to substances recommended for removal from the National List of Allowed and Prohibited Substances of the National Organic Program of the Agricultural Marketing Service; and (11) identifying how organic agriculture can adapt to and mitigate climate change through reducing greenhouse gas emissions, building landscape resiliency, establishing regenerative agriculture systems, and facilitating other related ecosystem services. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by striking Types and Process, and inserting Term, Types, and Process; ;\n**(B)**\nby inserting (3) after Paragraphs ; and\n**(C)**\nby striking ( 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157(b) ) ;\n**(3)**\nby striking subsection (e) and inserting the following:\n(e) Indigenous traditional ecological knowledge Any grants made under this section for the purposes of facilitating the identification and adoption of indigenous traditional ecological knowledge shall be subject to the following requirements: (1) A 1994 Institution (as defined in section 532 of the Equity in Educational Land-Grant Status Act of 1994 ( 7 U.S.C. 301 note; Public Law 103\u2013382 )) or an Alaska Native-serving institution or Native Hawaiian-serving institution (as those terms are defined in section 317(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059d(b) )) shall have the role of project director. (2) The free, prior, and informed consent of any Indian Tribes (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) or Native Hawaiian organizations that possess the applicable indigenous traditional ecological knowledge shall be obtained. (3) Appropriate attribution to the sources of the applicable indigenous traditional ecological knowledge shall be identified. ; and\n**(4)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (F), by striking and at the end;\n**(ii)**\nin subparagraph (G), by striking 2023 and each fiscal year thereafter. and inserting 2023; ; and\n**(iii)**\nby adding at the end the following:\n(H) $60,000,000 for fiscal year 2026; (I) $70,000,000 for fiscal year 2027; (J) $80,000,000 for fiscal year 2028; (K) $90,000,000 for fiscal year 2029; and (L) $100,000,000 for fiscal year 2030 and each fiscal year thereafter. ; and\n**(B)**\nin paragraph (2), by striking 2023 and inserting 2030 .\n#### 4. Researching the transition to organic\nTitle XVI of the Food, Agriculture, Conservation, and Trade Act of 1990 is amended by inserting after section 1673 ( 7 U.S.C. 5926 ) the following:\n1674. Researching the transition to organic (a) Competitive specialized research and extension grants authorized The Secretary of Agriculture (referred to in this section as the Secretary ), in consultation with the National Agricultural Research, Extension, Education, and Economics Advisory Board, may make competitive grants to support research, education, and extension activities relating to the transition of nonorganic production systems into organic agricultural production systems for the purposes of\u2014 (1) overcoming barriers to transitioning to organic agricultural production; (2) documenting and understanding the effects of organic practices on ecosystem services, including soil health and fertility, greenhouse gas mitigation and sequestration, water management, biodiversity-related services, and pest management; and (3) developing improved technologies, methods, models, and metrics to document, describe, and optimize ecosystem services of transitioning agricultural production into organic management. (b) Grant administration Paragraphs (4), (7), (8), and (11)(B) of subsection (b) of the Competitive, Special, and Facilities Research Grant Act ( 7 U.S.C. 3157(b) ) shall apply with respect to the making of grants under this section. (c) Partnerships encouraged Following the completion of a peer review process for grant proposals received under this section, the Secretary may provide a priority to the grant proposals, found in the peer review process to be scientifically meritorious, that\u2014 (1) actively partner with producers or conduct on-farm research; and (2) actively involve\u2014 (A) 1890 Institutions (as defined in section 2 of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7601 )); (B) 1994 Institutions (as defined in section 532 of the Equity in Educational Land-Grant Status Act of 1994 ( 7 U.S.C. 301 note; Public Law 103\u2013382 )); (C) Hispanic-serving institutions (as defined in section 502 of the Higher Education Act of 1965 ( 20 U.S.C. 1101a )); or (D) Alaska Native-serving institutions or Native Hawaiian-serving institutions (as those terms are defined in section 317(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059d(b) )). (d) Authorization of appropriations There are authorized to be appropriated to carry out this section\u2014 (1) $10,000,000 for each of fiscal years 2026 and 2027; and (2) $20,000,000 for fiscal year 2028 and each fiscal year thereafter. .\n#### 5. Organic production and market data initiatives\nSection 7407 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 5925c ) is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e);\n**(2)**\nby inserting after subsection (c) the following:\n(d) Economic impact analysis of organic farming and certification (1) In general The Secretary, acting through the Administrator of the Economic Research Service (referred to in this subsection as the Secretary ), shall conduct an economic impact analysis of organic agricultural management conducted in accordance with the national organic program established under the Organic Foods Production Act of 1990 ( 7 U.S.C. 6501 et seq. ). (2) Requirements The analysis under paragraph (1) shall\u2014 (A) take into consideration information about farming and ranching operations of a variety of sizes, with regional differences, and that have a diversity of production practices and methods; and (B) consider the direct and indirect economic impacts of organic agriculture on rural and urban communities, including\u2014 (i) the vitality of the local economy; (ii) the labor market; (iii) environmental quality; (iv) social dynamics; (v) land ownership; and (vi) any other information, data, or analysis that the Secretary determines to be necessary to make the analysis comprehensive, accurate, and useful. (3) Plan Not later than 1 year after the date of enactment of the Organic Science and Research Investment Act of 2025 , the Secretary shall submit a plan to conduct the analysis under paragraph (1) to\u2014 (A) the Committee on Agriculture, Nutrition, and Forestry of the Senate; and (B) the Committee on Agriculture of the House of Representatives. (4) Submission Not later than 3 years after the date on which the Secretary submits the plan under paragraph (3), the Secretary shall submit to the committees described in that paragraph a report describing the results of the analysis conducted under paragraph (1). ; and\n**(3)**\nin subsection (e) (as so redesignated)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by striking and at the end;\n**(ii)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(C) $10,000,000 for the period of fiscal years 2025 through 2030. ; and\n**(B)**\nin paragraph (2), by striking $5,000,000 for each of fiscal years 2008 through 2023 and inserting $10,000,000 for each of fiscal years 2025 through 2030 .",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-10-06",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "5703",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Organic Science and Research Investment Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-07T13:23:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119s1385",
          "measure-number": "1385",
          "measure-type": "s",
          "orig-publish-date": "2025-04-09",
          "originChamber": "SENATE",
          "update-date": "2026-01-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1385v00",
            "update-date": "2026-01-16"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Organic Science and Research Investment Act of 2025</strong></p><p>This bill expands Department of Agriculture (USDA) support for organic agricultural\u00a0research.</p><p>USDA must establish the Coordinating and Expanding Organic Research Initiative for USDA resources dedicated to organic agricultural research. Every five years, the initiative must survey USDA's organic agricultural research and produce a report, including findings and recommendations on expanding research and increasing project coordination and effectiveness. USDA must take the findings and recommendations into consideration when preparing USDA's annual budget recommendations.</p><p>In carrying out its work, the initiative must consult with the National Organic Standards Board and land-grant colleges and universities. In preparing each report, the initiative must consult organic and conventional farmers, ranchers, handlers and the organizations that serve them.</p><p>The bill also reauthorizes\u00a0the\u00a0National Institute of Food and Agriculture\u2019s\u00a0Organic Agriculture Research and Extension Initiative through FY2030 and increases funding for the initiative. Further, eligible grant projects are expanded to include\u00a0(1) facilitating the identification and adoption of traditional ecological knowledge and cultural practices, and\u00a0(2) identifying how organic agriculture can adapt to and mitigate climate change.</p><p>The bill also reauthorizes, and extends funding for, USDA's organic production and market data initiatives through FY2030. The Economic Research Service must conduct an economic impact analysis of organic agricultural management conducted in accordance with the National Organic Program.</p><p>USDA may make competitive grants to support research, education, and extension activities relating to the transition from nonorganic production systems\u00a0into organic agricultural production systems.</p>"
        },
        "title": "Organic Science and Research Investment Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1385.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Organic Science and Research Investment Act of 2025</strong></p><p>This bill expands Department of Agriculture (USDA) support for organic agricultural\u00a0research.</p><p>USDA must establish the Coordinating and Expanding Organic Research Initiative for USDA resources dedicated to organic agricultural research. Every five years, the initiative must survey USDA's organic agricultural research and produce a report, including findings and recommendations on expanding research and increasing project coordination and effectiveness. USDA must take the findings and recommendations into consideration when preparing USDA's annual budget recommendations.</p><p>In carrying out its work, the initiative must consult with the National Organic Standards Board and land-grant colleges and universities. In preparing each report, the initiative must consult organic and conventional farmers, ranchers, handlers and the organizations that serve them.</p><p>The bill also reauthorizes\u00a0the\u00a0National Institute of Food and Agriculture\u2019s\u00a0Organic Agriculture Research and Extension Initiative through FY2030 and increases funding for the initiative. Further, eligible grant projects are expanded to include\u00a0(1) facilitating the identification and adoption of traditional ecological knowledge and cultural practices, and\u00a0(2) identifying how organic agriculture can adapt to and mitigate climate change.</p><p>The bill also reauthorizes, and extends funding for, USDA's organic production and market data initiatives through FY2030. The Economic Research Service must conduct an economic impact analysis of organic agricultural management conducted in accordance with the National Organic Program.</p><p>USDA may make competitive grants to support research, education, and extension activities relating to the transition from nonorganic production systems\u00a0into organic agricultural production systems.</p>",
      "updateDate": "2026-01-16",
      "versionCode": "id119s1385"
    },
    "title": "Organic Science and Research Investment Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Organic Science and Research Investment Act of 2025</strong></p><p>This bill expands Department of Agriculture (USDA) support for organic agricultural\u00a0research.</p><p>USDA must establish the Coordinating and Expanding Organic Research Initiative for USDA resources dedicated to organic agricultural research. Every five years, the initiative must survey USDA's organic agricultural research and produce a report, including findings and recommendations on expanding research and increasing project coordination and effectiveness. USDA must take the findings and recommendations into consideration when preparing USDA's annual budget recommendations.</p><p>In carrying out its work, the initiative must consult with the National Organic Standards Board and land-grant colleges and universities. In preparing each report, the initiative must consult organic and conventional farmers, ranchers, handlers and the organizations that serve them.</p><p>The bill also reauthorizes\u00a0the\u00a0National Institute of Food and Agriculture\u2019s\u00a0Organic Agriculture Research and Extension Initiative through FY2030 and increases funding for the initiative. Further, eligible grant projects are expanded to include\u00a0(1) facilitating the identification and adoption of traditional ecological knowledge and cultural practices, and\u00a0(2) identifying how organic agriculture can adapt to and mitigate climate change.</p><p>The bill also reauthorizes, and extends funding for, USDA's organic production and market data initiatives through FY2030. The Economic Research Service must conduct an economic impact analysis of organic agricultural management conducted in accordance with the National Organic Program.</p><p>USDA may make competitive grants to support research, education, and extension activities relating to the transition from nonorganic production systems\u00a0into organic agricultural production systems.</p>",
      "updateDate": "2026-01-16",
      "versionCode": "id119s1385"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1385is.xml"
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
      "title": "Organic Science and Research Investment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Organic Science and Research Investment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Research, Extension, and Education Reform Act of 1998 and the Food, Agriculture, Conservation, and Trade Act of 1990 to direct the Agricultural Research Service to expand organic research, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:20Z"
    }
  ]
}
```
