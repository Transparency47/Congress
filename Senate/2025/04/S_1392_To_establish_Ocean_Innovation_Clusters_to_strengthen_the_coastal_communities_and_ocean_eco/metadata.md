# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1392?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1392
- Title: Ocean Regional Opportunity and Innovation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1392
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-02-10T12:03:17Z
- Update date including text: 2026-02-10T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1392",
    "number": "1392",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Ocean Regional Opportunity and Innovation Act of 2025",
    "type": "S",
    "updateDate": "2026-02-10T12:03:17Z",
    "updateDateIncludingText": "2026-02-10T12:03:17Z"
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
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
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
            "date": "2025-04-09T20:23:44Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-09T20:23:44Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "WA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "WA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "RI"
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "AK"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MS"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1392is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1392\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Ms. Murkowski (for herself, Ms. Cantwell , Mrs. Murray , Mr. Whitehouse , Mr. Merkley , Mr. Padilla , Mr. King , and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish Ocean Innovation Clusters to strengthen the coastal communities and ocean economy of the United States through technological research and development, job training, and cross-sector partnerships, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ocean Regional Opportunity and Innovation Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Blue Economy**\nThe term Blue Economy means the value and impact of sustainable industries related to the Great Lakes, oceans, bays, estuaries, and coasts on the economy of the United States, including living resources, marine construction, marine transportation, offshore energy development and siting including for renewable energy, offshore mineral production, ship and boat building, tourism, recreation, subsistence, commercial, recreational, and charter fishing, seafood processing, and other fishery-related businesses, kelp and shellfish aquaculture, coastal resilience, and other industries the Secretary of Commerce considers appropriate.\n**(2) Director of Sea Grant**\nThe term Director of Sea Grant means the Director of the National Sea Grant College Program appointed under section 204(d)(1) of the National Sea Grant College Program Act ( 33 U.S.C. 1123(d)(1) ).\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Native Hawaiian organization**\nThe term Native Hawaiian organization has the meaning given the term in section 6207 of the Native Hawaiian Education Act ( 20 U.S.C. 7517 ).\n**(5) Ocean Innovation Center for Cross-Sector Collaboration**\nThe term Ocean Innovation Center for Cross-Sector Collaboration means a physical space for collaboration developed and managed in accordance with section 3(i).\n**(6) Ocean Innovation Cluster**\nThe term Ocean Innovation Cluster means an eligible entity designated by the Secretary of Commerce under section 3.\n#### 3. Ocean Innovation Clusters\n##### (a) Designation\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Commerce, in consultation with the Director of Sea Grant, the Assistant Secretary of Commerce for Oceans and Atmosphere, and the Assistant Secretary of Commerce for Economic Development, shall designate not fewer than 7 eligible entities as Ocean Innovation Clusters.\n##### (b) Eligible entities\nFor purposes of this section, an eligible entity is an entity\u2014\n**(1)**\nthat is composed, in a concentrated geographic region, of 1 or more\u2014\n**(A)**\nbusiness organizations;\n**(B)**\nacademic institutions, including minority- and Tribal-serving institutions;\n**(C)**\nnot-for-profit organizations;\n**(D)**\nFederal, State, or local governmental entities, agencies, or instrumentalities;\n**(E)**\nIndian Tribes; or\n**(F)**\nNative Hawaiian organizations;\n**(2)**\nthat is led by a not-for-profit organization; and\n**(3)**\nthat works to deliver services in the concentrated geographic region where the entity is located, enhance collaboration, promote innovation, and contribute to the equitable and sustainable growth of the Blue Economy across all sectors.\n##### (c) Priority\nIn designating entities as Ocean Innovation Clusters under subsection (a), the Secretary of Commerce shall prioritize entities with a history of supporting cross-sector growth and development of the Blue Economy.\n##### (d) Geographic diversity\nThe Secretary of Commerce shall designate not fewer than 1 Ocean Innovation Cluster under subsection (a) in\u2014\n**(1)**\neach of the regions covered by the 5 regional offices of the National Marine Fisheries Service;\n**(2)**\nthe Great Lakes region; and\n**(3)**\nthe Gulf of Mexico region.\n##### (e) Considerations\nIn designating an eligible entity as an Ocean Innovation Cluster under subsection (a), the Secretary of Commerce shall consider the following:\n**(1)**\nThe economic development potential of the coastal community or region in which the entity is located.\n**(2)**\nThe ability of the entity to incorporate and bring growth and opportunity to broad geographic areas, including urban, rural, and underserved areas.\n**(3)**\nWhether the entity serves a diverse, multigenerational, ocean-dependent population consisting of groups with different socioeconomic and educational attainment levels, industries, and Indian Tribes.\n**(4)**\nThe ability of the entity to cultivate and leverage partnerships with private industry, academia, nongovernmental organizations, Federal, State, and local governments, and Indian Tribes to collaborate on shared outcomes.\n**(5)**\nThe relative potential for the designation of the entity as an Ocean Innovation Cluster to reverse a decline, or accelerate growth, in ocean sector jobs.\n**(6)**\nThe ability of the entity to carry out projects that support economic and climate resilience through economic diversification and long-term recovery from natural disasters.\n**(7)**\nThe extent, rural and underserved nature, and economic underutilization of the coastline and ocean area that projects carried out by the entity could affect.\n##### (f) Partnership management\n**(1) Partnership liaisons**\n**(A) Designation**\nThe Director of Sea Grant, the Assistant Secretary of Commerce for Oceans and Atmosphere, and the Assistant Secretary of Commerce for Economic Development shall each designate 1 partnership manager from within their respective agencies to serve as a partnership liaison between each Ocean Innovation Cluster and Sea Grant, the National Oceanic and Atmospheric Administration, and the Economic Development Administration, respectively.\n**(B) Function**\nEach partnership liaison designated under subparagraph (A) shall ensure that Ocean Innovation Clusters\u2014\n**(i)**\nhave direct communication with the agency of the liaison; and\n**(ii)**\nallow for collaboration and alignment with Federal objectives in each region regarding the Blue Economy.\n**(2) Interagency coordination**\n**(A) Secretary of Commerce**\nThe Secretary of Commerce shall coordinate with the Director of Sea Grant, the Assistant Secretary of Commerce for Oceans and Atmosphere, the Assistant Secretary of Commerce for Economic Development, the Department of Energy, the Maritime Administration of the Department of Transportation, the Environmental Protection Agency, the Bureau of Ocean Energy Management of the Department of the Interior, the Department of Agriculture, the Coast Guard, and such other Federal agencies, including bureaus of the Department of Commerce, as the Secretary of Commerce considers appropriate to increase technical knowledge exchange and opportunities for cross-sector collaboration with those agencies.\n**(B) Secretary of Energy**\nWith respect to matters relating to the nexus of the Blue Economy and the responsibilities and expertise of the Department of Energy, the Secretary of Energy\u2014\n**(i)**\nshall provide advice and recommendations to the Secretary of Commerce in order to increase technical knowledge exchange and opportunities for cross-sector collaboration; and\n**(ii)**\nmay provide such advice and recommendations without any formal request from the Department of Commerce.\n##### (g) Development of economic impact metrics of Ocean Innovation Clusters\nThe Administrator of the National Oceanic and Atmospheric Administration, the Director of the Bureau of Economic Analysis of the Department of Commerce, and the heads of other relevant Federal agencies shall use and refine the Marine Economy Satellite Account to measure the value to and impact of Ocean Innovation Clusters on the Blue Economy.\n##### (h) Areas of focus\nThe Director of Sea Grant, the Assistant Secretary of Commerce for Oceans and Atmosphere, and the Assistant Secretary of Commerce for Economic Development shall coordinate with each Ocean Innovation Cluster in the following areas of focus:\n**(1)**\nIncreasing pathways for new entrants into the Blue Economy for individuals and entities.\n**(2)**\nIntellectual property management.\n**(3)**\nEnhancing the sustainability of seafood supply chains, including with respect to food, transportation, processing, health and beauty products, animal feed, medical biotechnology, bioplastics, biofuels, and other value-added products, to strive for full use of harvested natural resources.\n**(4)**\nProviding significant and sustainable economic opportunity through advanced research, cross-sector science, and technology development.\n**(5)**\nContributing new knowledge, processes, technology, and support for stakeholders in the Blue Economy, especially to advance sustainability in specific sectors.\n**(6)**\nWorking with Federal, State, local, and Tribal agencies to clearly communicate laws, regulations, and agency practices affecting industry needs, planning, or growth opportunities.\n**(7)**\nCreating investable opportunities through the development of economies of scale to enhance growth opportunities, job creation, sustainability, and expansion for small businesses within the Blue Economy.\n**(8)**\nWorkforce development and training, business planning, identifying existing and needed technology and economic infrastructure, and coordinated research and development among small businesses, government, and industry.\n**(9)**\nResearch, development, and implementation of ocean energy, bioprospecting, and other innovative and sustainable ocean resource development endeavors.\n##### (i) Ocean Innovation Centers for Cross-Sector Collaboration\n**(1) In general**\nIn order to foster collaboration and innovation and strengthen regional ocean sector economies while creating employment opportunities, the Director of Sea Grant, the Assistant Secretary of Commerce for Oceans and Atmosphere, and the Assistant Secretary of Commerce for Economic Development shall collaborate with cross-sector partners to jointly develop or designate at least 1 physical space for collaboration as an Ocean Innovation Center for Cross-Sector Collaboration within each of the 7 regions with an Ocean Innovation Cluster.\n**(2) Management**\nAn Ocean Innovation Cluster or a group of Ocean Innovation Clusters shall manage the Ocean Innovation Center for Cross-Sector Collaboration of the region in which the Cluster or Clusters is located.\n**(3) Functions**\nEach Ocean Innovation Center for Cross-Sector Collaboration shall\u2014\n**(A)**\nserve as a hub for partners within Ocean Innovation Clusters to work toward the areas of focus in described in subsection (h);\n**(B)**\nsupport a community of entrepreneurs focused on strengthening vibrant marine-dependent communities and the Blue Economy;\n**(C)**\ncreate workspaces and laboratories designed to promote collaboration, including through shared meeting rooms, access to technology, common spaces, and offices;\n**(D)**\nstrengthen relationships among industry sectors through shared scientific, staffing, and business resources;\n**(E)**\ndevelop the critical networks with cross-sector partners that entrepreneurs need to grow effectively; and\n**(F)**\ndevelop the next generation of Blue Economy workers by providing internships, apprenticeships, or training, as appropriate, including for underrepresented and Tribal communities and local trade schools.\n#### 4. Grants for Ocean Innovation Clusters\nThe Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3701 et seq. ) is amended by adding at the end the following:\n31. Grants for Ocean Innovation Clusters (a) In general The Secretary, in consultation with the Director of Sea Grant, the Assistant Secretary of Commerce for Oceans and Atmosphere, and the Assistant Secretary of Commerce for Economic Development, may award grants, on a competitive basis, to Ocean Innovation Clusters for the purposes described in subsection (b). (b) Purposes The Secretary may award grants under subsection (a) for the operation and administration of one or more Ocean Innovation Clusters under the Ocean Regional Opportunity and Innovation Act of 2025 , with the goal that Ocean Innovation Clusters will become membership-based, self-sustaining entities. (c) Input In awarding a grant under subsection (a), the Secretary shall provide an opportunity for input from the Director of Sea Grant, the Assistant Secretary of Commerce for Oceans and Atmosphere, and the Assistant Secretary of Commerce for Economic Development. (d) Term of grants (1) In general The term of a grant awarded under subsection (a) shall be 2 years. (2) Renewal The Secretary may renew a grant awarded under subsection (a) for additional periods of such duration as the Secretary determines to be appropriate and necessary for the Ocean Innovation Cluster that received the grant to provide regional economic benefits. (e) Limitations on grant amounts A grant awarded under subsection (a) may not exceed $10,000,000. (f) Authorization of appropriations There is authorized to be appropriated to the Secretary to award grants under subsection (a) $10,000,000 for each of fiscal years 2026 through 2030. (g) Definitions In this section: (1) Director of Sea Grant The term Director of Sea Grant means the Director of the National Sea Grant College Program appointed under section 204(d)(1) of the National Sea Grant College Program Act ( 33 U.S.C. 1123(d)(1) ). (2) Ocean Innovation Cluster The term Ocean Innovation Cluster has the meaning given that term in section 2 of the Ocean Regional Opportunity and Innovation Act of 2025 . .",
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
        "actionDate": "2025-04-28",
        "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management."
      },
      "number": "3048",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ocean Regional Opportunity and Innovation Act of 2025",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-28T14:13:20Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1392is.xml"
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
      "title": "Ocean Regional Opportunity and Innovation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ocean Regional Opportunity and Innovation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish Ocean Innovation Clusters to strengthen the coastal communities and ocean economy of the United States through technological research and development, job training, and cross-sector partnerships, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:24Z"
    }
  ]
}
```
