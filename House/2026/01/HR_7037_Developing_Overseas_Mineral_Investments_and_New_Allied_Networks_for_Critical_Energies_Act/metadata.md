# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7037?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7037
- Title: Developing Overseas Mineral Investments and New Allied Networks for Critical Energies Act
- Congress: 119
- Bill type: HR
- Bill number: 7037
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-05-14T08:08:07Z
- Update date including text: 2026-05-14T08:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 45 - 0.
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 45 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7037",
    "number": "7037",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Developing Overseas Mineral Investments and New Allied Networks for Critical Energies Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:07Z",
    "updateDateIncludingText": "2026-05-14T08:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 45 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
        "item": [
          {
            "date": "2026-05-13T15:37:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-13T15:02:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "MI"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MD"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "IN"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "VA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NV"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "AS"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-01-23",
      "state": "IA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "VA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "HI"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "KY"
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
      "sponsorshipDate": "2026-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "UT"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "OH"
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
      "sponsorshipDate": "2026-04-20",
      "state": "OK"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "CO"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NV"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7037ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7037\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mrs. Kim (for herself, Mr. Bera , Mr. Mast , Mr. Huizenga , Mr. Olszewski , Mr. Shreve , Mr. Wittman , Mr. Stanton , Mr. Lawler , Mr. Panetta , Ms. Titus , Mr. Moore of North Carolina , Mr. Castro of Texas , and Mrs. Radewagen ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo promote United States and allied energy and mineral security, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Developing Overseas Mineral Investments and New Allied Networks for Critical Energies Act or the DOMINANCE Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Findings and purpose.\nSec.\u20023.\u2002Definitions.\nTitle I\u2014MINERALS SECURITY PARTNERSHIP AUTHORIZATION\nSec.\u2002101.\u2002International cooperation to secure critical minerals supply chains.\nSec.\u2002102.\u2002Minerals Security Partnership authorization.\nSec.\u2002103.\u2002United States membership in the International Nickel Study Group.\nSec.\u2002104.\u2002Diplomatic strategy for securing critical minerals.\nSec.\u2002105.\u2002Mechanism to support critical mineral projects in foreign countries.\nTitle II\u2014ENERGY SECURITY COMPACTS\nSec.\u2002201.\u2002Energy Security Compacts.\nSec.\u2002202.\u2002Office of Energy Security Compacts.\nSec.\u2002203.\u2002Energy security compact structure.\nSec.\u2002204.\u2002Energy Security Compacts Council.\nSec.\u2002205.\u2002Congressional notification.\nSec.\u2002206.\u2002Government Accountability Office.\nTitle III\u2014DEPARTMENT OF STATE AUTHORIZATIONS\nSec.\u2002301.\u2002Assistant Secretary for Energy Security and Diplomacy.\nSec.\u2002302.\u2002Bureau of Energy Security and Diplomacy.\nSec.\u2002303.\u2002Critical Mineral Mining Fellowship Program.\nSec.\u2002304.\u2002Visiting Mining Scholars Program.\nSec.\u2002305.\u2002Amendment to the Mutual and Cultural Exchange Act of 1961.\nSec.\u2002306.\u2002Definitions.\n#### 2. Findings and purpose\n##### (a) Findings\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States is heavily dependent on the People\u2019s Republic of China for the production, processing, and refinement of many key critical minerals and materials;\n**(2)**\nthe Government of the People\u2019s Republic of China has weaponized its dominance of critical mineral production and has intentionally created overcapacity and sold products at below-market rates in order to gain market share and move up the value chain;\n**(3)**\nit is in the economic and national security interests of the United States to prevent further inroads by strategic competitors into key sectors such as energy infrastructure, critical and rare earth minerals, and other supply chains essential to United States industrial capacity and strategic security;\n**(4)**\na reliable, resilient, and diversified supply chain for energy and critical minerals is essential to meet the defense, manufacturing, technological, and energy needs of the United States;\n**(5)**\nenergy security is a fundamental component of United States national security, economic stability, and foreign policy strategy;\n**(6)**\nthe United States must utilize available trade enforcement mechanisms, as well as other appropriate policy tools, to counter coercive economic practices by strategic competitors and complement the growth of a robust domestic critical minerals industry;\n**(7)**\nUnited States strategic interests are best served by reducing reliance on adversarial nations for energy and critical minerals, ensuring reliable and affordable electricity for industrial and strategic supply chains, expanding commercial opportunities for United States energy technologies, and securing diversified and reliable access to critical minerals for the United States and allied economies; and\n**(8)**\nGovernment financing, development, and diplomatic tools should all be deployed in a manner that maximizes the mobilization of private capital, strengthens cooperation with allies and partners, and advances the statutory objectives of United States foreign policy, economic development, and national security\u2014thereby making the United States safer, stronger, and more prosperous.\n##### (b) Purpose\nThe purpose of this Act is to\u2014\n**(1)**\nreduce the dependence of the United States and partner countries on strategic competitors for energy, critical minerals, and related technologies;\n**(2)**\nsupport economic growth and energy-sector modernization in partner countries through responsible and transparent development of domestic energy and mineral resources;\n**(3)**\nadvance United States national security and foreign policy objectives through strategic investments, policy coordination, and expanded cooperation with allies and partners;\n**(4)**\nestablish a coordinated interagency mechanism to align United States diplomatic, development, trade, and financing tools;\n**(5)**\nstrengthen the commercial competitiveness of United States energy and critical mineral companies in global markets; and\n**(6)**\nsecure a diversified and resilient supply and processing capacity for critical minerals necessary for United States industry, energy systems, and defense requirements, as well as those of allied and partner countries.\n#### 3. Definitions\nIn this Act:\n**(1) Ally; allied country**\nThe term ally or allied country means\u2014\n**(A)**\nany country described in section 2350a(a)(2) of title 10, United States Code; and\n**(B)**\nany member country of an organization listed in such section.\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs, the Committee on Ways and Means, and the Committee on Appropriations of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations, the Committee on Finance, and the Committee on Appropriations of the Senate.\n**(3) Assistant Secretary**\nThe term Assistant Secretary means the Assistant Secretary for Energy Security and Diplomacy, as established in section 301.\n**(4) Country Compact Team**\nThe term Country Compact Team means a dedicated team formed by the Director for Energy Security Compacts to manage the day-to-day activities related to the development, negotiation, implementation, and monitoring of the Energy Security Compacts.\n**(5) Critical mineral**\nThe term critical mineral means any mineral on the list of critical minerals required by section 7002(c)(3) of the Energy Act of 2020 ( 30 U.S.C. 1606(c)(3) ) on or after January 1, 2026.\n**(6) Department**\nThe term Department means the Department of State.\n**(7) Partner country**\nThe term partner country means any country eligible for an Energy Security Compact under title II.\n**(8) Processed**\nThe term processed , with respect to a critical mineral, means the mineral has undergone the activities that occur after critical mineral ore is extracted from a mine up through its conversion into a metal, metal powder, or a master alloy.\n**(9) Secretary**\nThe term Secretary means the Secretary of State.\n**(10) Under Secretary**\nThe term Under Secretary means the Under Secretary for Economic Affairs.\nI\nMINERALS SECURITY PARTNERSHIP AUTHORIZATION\n#### 101. International cooperation to secure critical minerals supply chains\n##### (a) Statement of policy on critical mineral supply chains\nIt is the policy of the United States\u2014\n**(1)**\nto collaborate with allies and partners of the United States to build secure and resilient critical mineral supply chains, including in the mining, processing, reclamation and recycling, and valuation of critical minerals, as well as with respect to advanced manufacturing that includes critical minerals;\n**(2)**\nto prioritize the development and production of critical minerals domestically, including both to supply domestic needs and for export to allies and partners that participate in secure and resilient supply chains for critical minerals;\n**(3)**\nto reduce or eliminate reliance on critical mineral supply chains controlled by the People\u2019s Republic of China, the Russian Federation, Iran, or any other strategic competitor to the United States;\n**(4)**\nto work with allies and partners on enhancing evaluation capability, tracing, and technology in trusted countries that produce critical minerals to avoid the export of mined and processed critical minerals to adversaries of the United States;\n**(5)**\nto identify and implement market-based incentives for the purposes of facilitating the creation and maintenance of secure and resilient critical mineral supply chains, including for reclamation and recycling of critical mineral resources from waste streams, in collaboration with allies and partners;\n**(6)**\nto prioritize securing critical mineral supply chains in the United States foreign policy, including through the use of economic tools to invest responsibility in beneficiation and value-adding projects in partner countries in a manner that both benefits local populations and bolsters the supply of critical minerals to the United States;\n**(7)**\nto work with allies and partners to address the distortive effects of predatory economic, pricing, and market manipulation practices used by the People\u2019s Republic of China the Russian Federation, Iran, or any other strategic competitor of the United States;\n**(8)**\nto coordinate policy tools and investments with allies and partners to accelerate the development of transparent, traceable, diversified, and fair markets for critical minerals and rare earths; and\n**(9)**\nthat collaboration with allies and partners to build secure and resilient critical mineral supply chains shall not replace United States efforts to increase domestic development and production or recycling of critical minerals.\n##### (b) International negotiations relating to protecting critical mineral supply chains\n**(1) In general**\nThe President may negotiate an agreement with the governments of foreign countries for the purposes of establishing a coalition to\u2014\n**(A)**\nfacilitate the transparent mining, processing, supply, and procurement of critical minerals;\n**(B)**\nfacilitate advanced manufacturing that includes critical minerals; and\n**(C)**\nsecure an adequate supply of critical minerals and relevant products, manufacturing inputs, and components that are heavily dependent on critical mineral resources for the United States and other members of the coalition (in this title referred to as member countries ).\n**(2) Negotiating objectives**\nThe overall objectives for negotiating an agreement described in paragraph (1) shall be\u2014\n**(A)**\nto establish mechanisms for member countries to build secure, resilient, and transparent supply chains for critical minerals, including in\u2014\n**(i)**\nthe mining, refinement, processing, and valuation of critical minerals; and\n**(ii)**\nadvanced manufacturing of products, components, and materials that are dependent on critical minerals;\n**(B)**\nto improve economies of scale and joint cooperation with international partners in securing access to and means of production throughout the supply chains of critical minerals and manufacturing processes dependent on critical minerals;\n**(C)**\nto establish mechanisms, with appropriate market-based disciplines, that provide and maintain opportunities among member countries for creating industry economies of scale to attract joint investment among member countries, including\u2014\n**(i)**\ncooperation on joint projects, including cost-sharing on building appropriate infrastructure to access deposits of critical minerals; and\n**(ii)**\ncreation or enhancement of national and international programs to support the development of robust industries by providing appropriate sector-specific incentives, such as political risk and other insurance opportunities, financing, and other support, for\u2014\n**(I)**\ntransparent mining and processing of critical minerals;\n**(II)**\nmanufacturing of products, components, and materials that are dependent on critical minerals and are essential to consumer technology products or have important national security implications; and\n**(III)**\nassociated transportation needs that are tailored to the handling, movement, and logistics management of critical minerals and products, components, and materials that are dependent on critical minerals;\n**(D)**\nto establish market-based rules for member countries regarding adoption of qualifying tax and other incentives to stimulate investment to ensure a fair playing field among member countries;\n**(E)**\nto establish recommended best practices to protect\u2014\n**(i)**\nlabor rights;\n**(ii)**\nthe natural environment and ecosystems near critical mineral industrial sites;\n**(iii)**\nthe safety of communities near critical mineral industrial activities through consultation; and\n**(iv)**\nsupply chain diversity;\n**(F)**\nto advance economic growth in developing countries with critical mineral reserves, including for the benefit of the citizens of such countries;\n**(G)**\nto establish rules allowing for the establishment of a consortium that is resourced and empowered to bid and compete in acquiring and securing potential deposits of critical minerals in countries that are not member countries;\n**(H)**\nto establish a mechanism for joint resource mapping with procedures for equitable sharing of information on potential deposits of critical minerals not less frequently than annually;\n**(I)**\nto establish appropriate mechanisms for the recognition and enforcement by a member country of judgements relating to environmental and related harms caused by mining operations within such member country in contravention of the laws of such country; and\n**(J)**\nto improve supply chain security among member countries by providing for national treatment investment protections among member countries that are equal to, or better than, the standards set forth in the United States model bilateral investment treaty.\n**(3) Congressional consultation required**\nIn the course of negotiations described in paragraph (1), the Secretary shall, not less frequently than annually, consult with the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate, and shall keep such committees fully apprised of such negotiations.\n##### (c) Rule of construction\nNothing in this section shall be construed to alter any other provision of United States domestic law or regulation applicable to critical minerals.\n#### 102. Minerals Security Partnership authorization\n##### (a) In general\nThe Secretary, acting through the Under Secretary of State for Economic Growth, Energy, and the Environment, may lead United States participation in a Minerals Security Partnership , for the following purposes:\n**(1)**\nTo identify and support investment and advocate for commercial and military use critical mineral mining, processing, and refining projects that enable robust, secure, and transparent critical mineral supply chains, in consultation with the other Federal agencies, as appropriate.\n**(2)**\nTo coordinate with relevant regional bureaus to develop regional diplomatic engagement strategies related to critical minerals projects and to identify projects that are priorities.\n**(3)**\nTo coordinate with United States missions abroad on projects, programs, and investments that enable robust and secure critical mineral supply chains.\n**(4)**\nTo coordinate with current and prospective members of the Minerals Security Partnership.\n**(5)**\nTo establish a mechanism for information-sharing with members of the Minerals Security Partnership.\n**(6)**\nTo establish policies and procedures, and if necessary, to provide funding to facilitate cooperation on joint projects with members of the Minerals Security Partnership and any related organizations established by the Minerals Security Partnership (including the Mineral Security Partnership Forum), including those related to cost-sharing agreements, political risk insurance, financing, equity investments, pricing mechanisms, procurement, and other support, in coordination with other Federal agencies, as appropriate.\n**(7)**\nTo coordinate with Development Finance Institutions, Export Credit Agencies, multilateral banks, and private banks headquartered in Minerals Security Partnership member countries to promote information exchange and co-financing through the Minerals Security Partnership Finance Network.\n**(8)**\nTo identify individuals within the Bureau of Energy Security and Diplomacy to monitor and coordinate responses to trade measures or policies that may adversely affect United States and allied country supplies of critical minerals or investments in third-country critical mineral markets, especially investments supported by the Minerals Security Partnership.\n**(9)**\nTo establish procedures to prevent, review, and deter critical mineral asset sales to prohibited foreign entities (as such term is defined in section 7701 of the Internal Revenue Code) by companies within the jurisdiction of Minerals Security Partnership and Minerals Security Partnership Forum member countries.\n**(10)**\nTo establish a framework for the transparent evaluation of member countries\u2019 compliance and effectiveness in fulfilling the purposes listed in paragraphs (1) through (9) of this section.\n**(11)**\nTo identify and recommend priority countries for future engagement, including through an Energy Security Compact described in section 201 or any other relevant alliance between the United States and a foreign country related to securing and diversifying critical mineral supply chains.\n##### (b) Database\nAs part of the Minerals Security Partnership, the Secretary, acting through the Under Secretary, may establish and maintain a database of critical mineral projects for the purpose of providing high quality and up-to-date information to the private sector in order to spur greater investment, increase the resilience of global critical minerals supply chains, and boost United States supply of critical minerals.\n##### (c) Exchange of information with the Minerals Security Partnership\n**(1) Procedure**\nThe Secretary, acting through the Under Secretary, shall develop a procedure for the collection, handling, and transmission of commercial information or data that is provided by other Federal departments and agencies and transmitted to members of the Minerals Security Partnership.\n**(2) Limitations**\nThe procedure required in paragraph (1) shall include the following limitations:\n**(A)**\nAny information or data which is geological or geophysical information or a trade secret or commercial or financial information shall, prior to transmittal, be aggregated, accumulated, or otherwise reported in such a manner as to avoid, to the fullest extent feasible, identification of any person from whom the United States obtained such information.\n**(B)**\nThe limitations on disclosure described in the following:\n**(i)**\nsection 11(d) of the Energy Supply and Environmental Coordination Act of 1974 ( 15 U.S.C. 796(d) );\n**(ii)**\nsection 14(b) of the Federal Energy Administration Act of 1974 ( 15 U.S.C. 773(b) );\n**(iii)**\nsection 9 of title 13, United States Code;\n**(iv)**\nthe first section of the Act of January 27, 1938, entitled An Act to make confidential certain information furnished to the Bureau of Foreign and Domestic Commerce, and for other purposes ( 15 U.S.C. 176a );\n**(v)**\nsection 1905 of title 18, United States Code; and\n**(vi)**\nsection 252 of the Energy Policy and Conservation Act of 1975 ( 42 U.S.C. 6274 ).\n**(3) Exceptions**\n**(A) International energy emergency**\nNotwithstanding paragraph (2), the Secretary may make any information or data available to members of the Minerals Security Partnership during an international energy supply emergency.\n**(B) Presidential certification**\nNotwithstanding paragraph (2), the Secretary may make any information or data available to members of the Minerals Security Partnership if the President certifies, after opportunity for presentation of views by interested persons, that the Minerals Security Partnership has adopted and is implementing security measures such that such information or data will not be disclosed by member countries of the Minerals Security Partnership or the agencies or employees of such countries to any person or foreign country without having been aggregated, accumulated, or otherwise reported in such manner as to avoid identification of any person from whom the United States obtained such information or data.\n##### (d) Mineral Security Partnership staff\nThe Secretary shall prioritize staffing the Mineral Security Partnership with individuals who have the following qualifications:\n**(1)**\nSubstantive knowledge and experience in issues related to critical minerals supply chains and the application of such supply chains to strategic industries, including in the defense, energy, and technology sectors.\n**(2)**\nSubstantive knowledge and experience in large-scale multi-donor project financing and related technical and diplomatic arrangements, international coalition-building, development finance, and project management.\n**(3)**\nSubstantive knowledge and experience in trade and foreign policy, defense-industrial base policy, or national security-sensitive supply chain issues.\n##### (e) Private sector and civil society coordination\nThe Secretary, acting through the Under Secretary for Economic Growth, Energy, and the Environment, shall ensure close coordination between the Department, the private sector, and relevant civil society groups regarding the implementation of this section.\n##### (f) Project selection\n**(1) In general**\nThe United States, through participation in the Minerals Security Partnership, shall prioritize projects that advance the national and economic security interests of the United States and allies and partners of the United States.\n**(2) Criteria requirements**\nThe United States shall advocate for the Minerals Security Partnership to use environmental, societal, and governance standards, including as criteria for project selection, that are consistent with United States law or international agreements approved by Congress.\n**(3) Private sector collaboration**\nThe Department shall coordinate with the private sector to leverage expertise and ensure projects supported by the Minerals Security Partnership are catalyzed by private sector investments and commercial offtake, with priority to the United States, through the Minerals Investment Network for Vital Energy Security and Transformation (commonly known as MINVEST ).\n#### 103. United States membership in the International Nickel Study Group\n##### (a) United States membership\nThe President may accept the Terms of Reference of and maintain membership of the United States in the International Nickel Study Group.\n##### (b) Payments of assessed contributions\nFor fiscal year 2026 and each fiscal year thereafter, the United States assessed contributions to the International Nickel Study Group may be paid from amounts authorized to be appropriated under section 8 of the United Nations Participation Act of 1945 ( 22 U.S.C. 287e ).\n#### 104. Diplomatic strategy for securing critical minerals\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary, in consultation with the heads of other relevant Federal agencies, shall develop a strategy for securing the supply chains of a diverse set of critical minerals.\n##### (b) Elements\nThe strategy required by subsection shall\u2014\n**(1)**\ninclude\u2014\n**(A)**\na review of the roles and responsibilities of offices and positions within the Department engaged, as of the date of the enactment of this Act, in efforts to secure critical mineral supply chains; and\n**(B)**\nprocesses to ensure that such offices coordinate and deconflict such efforts;\n**(2)**\nleverage use of United States financial, commercial, and development assistance tools and resources to advance the critical mineral policies of the United States;\n**(3)**\ninclude targeted engagement plans for both countries that are allies or partners of the United States and countries with significant proven or estimated deposits of critical minerals or processing capacity for minerals critical to national security interests;\n**(4)**\nprovide for coordination with relevant Federal agencies to align trade policies to address both price volatility and incentivize the sourcing of critical minerals from trusted suppliers;\n**(5)**\nstrengthen collaboration with countries that are allies and partners of the United States, and leverage the leadership role of the United States in multilateral institutions engaged on critical mineral issues to shape international standards;\n**(6)**\nextend the diplomatic and commercial advocacy support of the United States to private sector entities throughout critical mineral supply chains; and\n**(7)**\nfacilitate coordination with countries that are allies and partners of the United States to\u2014\n**(A)**\nidentify best practices and develop coordinated standards for critical mineral projects;\n**(B)**\nprotect against inhumane labor practices; and\n**(C)**\nminimize adverse environmental and social impacts from the critical minerals supply chain.\n##### (c) Briefing required\nNot later than 210 days after the date of enactment of this Act, the Secretary shall provide a briefing on the strategy developed under subsection (a) to\u2014\n**(1)**\nthe Committee on Foreign Affairs and the Permanent Select Committee on Intelligence of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations and the Select Committee on Intelligence of the Senate.\n#### 105. Mechanism to support critical mineral projects in foreign countries\n##### (a) Sense of Congress\nIt is the sense of Congress that United States private sector entities competing for critical mineral projects abroad need support from the United States Government.\n##### (b) Support for critical mineral projects\nThe Secretary shall direct an appropriate official or office of the Department to establish a mechanism and process for the United States to provide support for critical mineral projects in foreign countries, which may include\u2014\n**(1)**\na mechanism for certifying that critical mineral projects uphold labor rights and minimize environmental impacts; and\n**(2)**\na process for United States private sector entities to engage with United States embassies in foreign countries for support when pursuing critical mineral projects in such countries.\nII\nENERGY SECURITY COMPACTS\n#### 201. Energy Security Compacts\n##### (a) In general\nThe Secretary is authorized to make available, from amounts authorized to be appropriated for fiscal year 2026 or any subsequent fiscal year for bilateral economic assistance (including amounts authorized to be appropriated to the Economic Resilience Initiative), amounts for the purpose of establishing multi-year agreements (to be known as Energy Security Compacts ) with partner countries to enhance the energy and economic security and stability of the United States and such partner countries, including through efforts to counter economic coercion through the diversification of critical mineral and energy supply chains.\n##### (b) Transfers\nFunds made available for the Economic Resilience Initiative or otherwise determined by the Secretary to be made available to support Energy Security Compacts may be transferred to, and merged with, funds appropriated for fiscal year 2026 or thereafter under the headings Trade and Development Agency , Millennium Challenge Corporation , United States International Development Finance\u2013Corporate Capital Account , United States International Development Finance\u2013Program Account , Development Finance Corporate Equity Investment Account , and Export-Import Bank of the United States\u2013Program Account by any Act providing appropriations for the Department of State and related programs.\n##### (c) Consultation and notification\nThe transfer authority provided by this section is in addition to any other transfer authority provided by law, and is subject to\u2014\n**(1)**\nprior consultation with\u2014\n**(A)**\nthe Committee on Appropriations and the Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Appropriations and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe regular notification procedures of such committees.\n##### (d) Assistance for the development and implementation of compacts\nThe Director for Energy Security Compacts may\u2014\n**(1)**\nenter into contracts for required technical support related to Energy Security Compacts;\n**(2)**\nmake grants to any partner country for the purpose of building the administrative or technical capacity necessary to facilitate the development and implementation of an Energy Security Compact between the United States and such country; and\n**(3)**\nform Country Compact Teams with a designated lead, who will regularly engage with the Council, to carry out the implementation of the Compact.\n##### (e) Limitations\n**(1) Prohibition on military assistance and training**\nAssistance under this section may not include military assistance or military training for a country.\n**(2) Prohibition on assistance relating to United States job loss or production displacement**\nAssistance under this section may not be provided for any project that is likely to cause a substantial loss of United States jobs or a substantial displacement of United States production.\n**(3) Prohibition on assistance relating to environmental, health, or safety hazards**\nAssistance under this section may not be provided for any project that is likely to cause a significant, unmitigable environmental, health, or safety hazard.\n**(4) Foreign Aid Transparency and Accountability Act Compliance**\nNone of the funds authorized to be appropriated or otherwise made available by this Act may be obligated or expended for an Energy Security Compact unless the compact and all associated activities comply with the monitoring, evaluation, performance measurement, and public reporting requirements of section 4 of the Foreign Aid Transparency and Accountability Act of 2016 ( 22 U.S.C. 2394c ).\n**(5) Limitation relating to the President and Vice President**\nNone of the funds authorized to be appropriated or otherwise made available by this Act may be obligated or expended to provide any grant, contract, loan, or other financial assistance to an entity in which the President, the Vice President, or an immediate family member (as such term is defined in section 1128(j) of the Social Security Act ( 42 U.S.C. 1320a\u20137(j) )) of the President or Vice President holds, directly or indirectly, any ownership interest or serves in any managerial, officer, director, or board capacity.\n##### (f) Report required\nNot less frequently than annually until the date that is five years after the date of the enactment of this Act, the Director for Energy Security Compacts shall submit to the appropriate congressional committees, the Executive Office of the President, the National Security Council, and the Secretary a report describing\u2014\n**(1)**\nthe current status of activities authorized under this title;\n**(2)**\nany obstacles to the implementation of such activities; and\n**(3)**\nany updates to the multiyear financial plan developed pursuant to section 203(c)(6).\n#### 202. Office of Energy Security Compacts\n##### (a) Establishment\nThe Secretary shall establish an Office of Energy Security Compacts, which shall perform such functions related to the administration and implementation of the Energy Security Compacts described in section 201 as the Assistant Secretary may prescribe.\n##### (b) Director for Energy Security Compact\nThe Office of Energy Security shall be led by a Director for Energy Security Compacts who shall be responsible to the Assistant Secretary for all matters pertaining to the administration and implementation of the Energy Security Compacts described under section 201 and such other related duties as the Secretary may from time to time designate.\n##### (c) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Director for Energy Security Compacts shall be responsible for supporting the Department\u2019s participation in and leadership of the Economic Resilience Initiative and the Energy Security Compacts Council, including for all matters pertaining to the following:\n**(1)**\nDrafting the contribution of the Secretary to the strategy identified in section 7030(d) of the Further Consolidated Appropriations Act, 2024 ( Public Law 119\u201337 ).\n**(2)**\nLeading the development, negotiation, and management of all Energy Security Compacts funded through the Economic Resilience Initiative.\n**(3)**\nConsulting and coordinating with agencies and departments that are members of the Energy Security Council to develop prospective Energy Security Compacts and implement ongoing Energy Security Compacts, as appropriate.\n**(4)**\nServing as the recipient for\u2014\n**(A)**\nsolicited proposals under the Energy Security Compact; and\n**(B)**\nunsolicited proposals for projects to be considered for inclusion in any Energy Security Compact by national, regional, and local governments and private corporations.\n**(5)**\nSigning joint agency agreements, transferring or receiving appropriated funds with any department, agency, or independent establishment of the United States Government (with the consent of the head of such department, agency, or establishment) for the purpose of developing, implementing, or otherwise participating in an Energy Security Compact described under section 301, including for the use as credit subsidy.\n**(6)**\nCoordinating with other donor entities, including countries that are allies and partners of the United States, the Minerals Security Partnership, and other multilateral fora, for the purposes of deconflicting, augmenting, and leveraging, where appropriate, Energy Security Compact workplans with the development and financing activities performed by others.\n##### (d) Personnel\nThe Director for Energy Security Compacts may\u2014\n**(1)**\ndetail staff to a collaborating agency head with relevant sectoral, financial, or regional expertise for the negotiation or implementation of an Energy Security Compact;\n**(2)**\nrequest core agency heads and collaborating agency heads detail personnel to the Office of Energy Security Compacts with relevant sectoral, financial, or regional expertise for the negotiation or implementation of an Energy Security Compact; and\n**(3)**\nappoint, without regard to the provisions of sections 3309 through 3318 of title 5, United States Code, candidates directly to positions in the competitive service, as defined in section 2102 of that title.\n##### (e) Termination\nThe authority provided under this section shall terminate on the date that is 10 years after the date of the enactment of this Act.\n##### (f) Report\nNot later than 180 days after the date of the enactment of this Act, the Under Secretary for Economic Affairs shall submit to the appropriate congressional committees a report that contains plans to attract and retain diplomatic, policy, legal, and technical expertise for civil service officers in the Office of Energy Security Compacts, including career promotion tracks to supervisory and non-supervisory GS\u201315 positions.\n#### 203. Energy security compact structure\n##### (a) In general\nEach Energy Security Compact should increase reliable access to energy, electricity, or critical minerals for both parties to the Energy Security Compact, for the purpose of stimulating economic growth, enabling follow-on private sector investment, supporting the commercial competitiveness of United States companies, or diversifying relevant supply chains.\n##### (b) Prior analysis required\nBefore establishing an Energy Security Compact, the Office of Energy Security Compacts, in collaboration with the Energy Security Compact Council, shall conduct a constraints analysis of the energy sector and supply-chain segments needed to strengthen the partner country\u2019s energy security, consistent with United States energy security risks and commercial opportunities.\n##### (c) Energy security compact elements\nEach Energy Security Compact shall contain\u2014\n**(1)**\na constraints analysis of the energy sector which identifies insufficiencies in the energy sector and supply-chain segments needed to ensure the partner country\u2019s energy security, consistent with United States energy security risks and commercial opportunities;\n**(2)**\nspecific objectives that the partner country and the United States expect to achieve during the term of the Energy Security Compact, including\u2014\n**(A)**\nincreased energy production, reliability, and affordability in the partner country;\n**(B)**\neconomic growth in the partner country that may reduce the need for foreign assistance;\n**(C)**\nimproved access to energy, in consultation with affected communities and civil society; and\n**(D)**\nimproved infrastructure that enables access to critical minerals mining and processing;\n**(3)**\nthe responsibilities of the partner country and the United States in the achievement of such objectives;\n**(4)**\nregular quantitative benchmarks to measure, where appropriate, progress toward achieving such objectives;\n**(5)**\nan identification of the intended impact of the activities carried out in accordance with the Energy Security Compact;\n**(6)**\na multiyear financial plan, updated annually until the expiration of the term of the Energy Security Compact, that\u2014\n**(A)**\nestimates the amount of contributions, commitments, and other participation to be provided by the Department, Core Agencies, Collaborating Agencies, the partner country, and other entities;\n**(B)**\nensures compacts with low-income countries incorporate and are complementary to development programs administered by other United States agencies and departments, so that United States funds are used to improve feasibility for private sector investment to further development goals;\n**(C)**\nidentifies proposed mechanisms to implement the plan and provide oversight of the plan; and\n**(D)**\ndescribes how the requirements described in paragraphs (1) through (5) will be met, including the role of the private sector in the achievement of such requirements;\n**(7)**\nas appropriate, a description of the current and potential participation of other donors, including countries that are allies and partners of the United States or collaborating agencies in the achievement of such objectives;\n**(8)**\na description of how oversight and transparency of the foreign assistance provided through the Economic Resilience Initiative will be maintained;\n**(9)**\nas appropriate, a process or processes for considering\u2014\n**(A)**\nsolicited proposals under the Energy Security Compact; and\n**(B)**\nunsolicited proposals by national, regional, and local units of government and private corporations;\n**(10)**\na requirement that open, fair, competitive, and transparent procedures are used in the administration of grants or cooperative agreements or the procurement of goods and services for the accomplishment of objectives under the Energy Security Compact;\n**(11)**\nthe strategy of the partner country to sustain progress made toward achieving such objectives after expiration of the Energy Security Compact;\n**(12)**\na description of the role of both core and collaborating agencies in any design, implementation, and monitoring of programs and activities funded through the Energy Security Compact; and\n**(13)**\na description of any contribution, as appropriate, from the partner country relative to its national budget and taking into account the prevailing economic conditions, toward meeting the objectives of the Energy Security Compact.\n##### (d) Eligibility\nA country shall be considered eligible for support under this section if\u2014\n**(1)**\nthe per capita income of the country is not greater than the World Bank loan threshold or the country is eligible for support from the International Bank for Reconstruction and Development or the International Development Association graduation process at the beginning of the year in which negotiations are initiated;\n**(2)**\nthe country has been identified as strategically or commercially important for the United States by the Director for Energy Security Compacts, Secretary, a member of the National Security Council, or the President;\n**(3)**\nthe Assistant Secretary determines that the country has the capacity and commitment to implement the Energy Security Compact; and\n**(4)**\nthe country is not a foreign country of concern, as such term is defined in section 10612(a) of Public Law 117\u2013167 ( 42 U.S.C. 19221(a) ).\n##### (e) Prohibition on taxation\nIn addition to the elements described in subsection (c), each Energy Security Compact shall contain a provision stating that assistance provided by the United States under the Energy Security Compact shall be exempt from taxation by the government of the partner country.\n##### (f) Approval\nEach Energy Security Compact shall be recommended by the Director for Energy Security Compacts and approved by the Secretary before the United States enters into such an Energy Security Compact.\n##### (g) Duration\nThe duration of each Energy Security Compact may not exceed 10 years.\n##### (h) Subsequent and concurrent compacts\nA partner country that has entered into, and has in effect, an Energy Security Compact under this section may enter into, and concurrently have in effect, additional Energy Security Compacts.\n##### (i) Report regarding increase or extension of assistance\nNot later than 15 days after making a determination to increase or extend assistance under an Energy Security Compact with a partner country, the Secretary, acting through the Director for Energy Security Compacts, shall submit to the appropriate congressional committees a written report that contains\u2014\n**(1)**\na justification for such a determination;\n**(2)**\na detailed summary of the proposed increase in, or extension of, assistance under the Energy Security Compact; and\n**(3)**\na copy of the full text of the amendment to the Energy Security Compact.\n#### 204. Energy Security Compacts Council\n##### (a) Establishment\nNot later than 90 days after the date of enactment of this Act, the President should establish an Energy Security Compacts Council (in this title referred to as the Council ) to coordinate and implement the Energy Security Compacts identified in this section.\n##### (b) Composition\nThe Council shall be chaired by the Secretary and be composed of principal officers of executive departments from the following agencies:\n**(1)**\nThe United States International Development Finance Corporation.\n**(2)**\nThe Department of Energy.\n**(3)**\nThe United States Trade and Development Agency.\n**(4)**\nThe Export-Import Bank of the United States.\n**(5)**\nThe Department of Commerce.\n**(6)**\nThe United States Trade Representative.\n**(7)**\nThe Department of Defense.\n**(8)**\nThe Department.\n**(9)**\nThe Department of the Interior.\n**(10)**\nAny other Federal agency or organization that the President determines to be appropriate.\n##### (c) Vacancies\nWhere there is a vacancy in the office of a principal officer of an executive department, the individual acting in that capacity shall serve as a member of the Council until a new principal officer of the executive department is appointed.\n##### (d) Delegation\nThe principal officer of an executive department may delegate a senior official (as described in section 1(d) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(d) )) to serve on the Council, as appropriate.\n##### (e) Duties\nThe Council shall\u2014\n**(1)**\nmeet not less frequently than quarterly;\n**(2)**\ncoordinate Energy Security Compact-related activities of the core and collaborating agencies;\n**(3)**\nmake annual recommendations to the Director for Energy Security Compacts, taking into account the stated priorities of the National Security Council and the President, regarding the prioritization of eligible countries for Energy Security Compact negotiation; and\n**(4)**\nmake recommendations to improve interagency collaboration for the purposes of promoting energy security and United States national security interests abroad.\n##### (f) Sunshine Act compliance\nMeetings of the Council are subject to section 5532b of title 5, United States Code (commonly referred to as the Government in the Sunshine Act ).\n#### 205. Congressional notification\nNot later than 30 days before entering into an Energy Security Compact, the Director for Energy Security Compacts shall\u2014\n**(1)**\nnotify and consult with the appropriate congressional committees regarding such Compact;\n**(2)**\ntransmit to the appropriate congressional committees the text of such Compact; and\n**(3)**\nprovide to the appropriate congressional committees an in-person briefing regarding such Compact.\n#### 206. Government Accountability Office\nThe Government Accountability Office shall, not later than 2 years after the date of the enactment of this Act and annually thereafter, submit to Congress an evaluation of the efficiency and development impact of projects supported by an Energy Security Compact.\nIII\nDEPARTMENT OF STATE AUTHORIZATIONS\n#### 301. Assistant Secretary for Energy Security and Diplomacy\n##### (a) Establishment\nThere is authorized to be in the Department an Assistant Secretary for Energy Security and Diplomacy who shall be responsible to the Under Secretary for Economic Affairs for all matters pertaining to the formulation and implementation of international energy, energy technology, critical minerals, and relevant supply chain policies in the conduct of foreign policy by the Department, including, as appropriate, to protect United States energy security interests, lead the coordination of energy programs carried out by United States Government agencies abroad, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Assistant Secretary shall maintain continuous observation and coordination of all matters pertaining to the development of policies to secure access to international energy markets and diversify critical mineral supply chains in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nRepresenting the Secretary in interagency efforts to develop the international energy policy of the United States.\n**(2)**\nLeading the analysis, formulation, and implementation of international policies aimed at protecting and advancing United States energy interests.\n**(3)**\nEffectively managing United States bilateral and multilateral relations and, as directed by the Secretary, representing the Secretary in relevant international fora and organizations, including the International Energy Agency, to bolster global energy security and advance the interests of the United States.\n**(4)**\nEnsuring that analyses of the national security and economic security implications of global energy developments are reflected in the decision-making processes within the Department.\n**(5)**\nIncorporating energy and critical mineral security priorities into the activities of the Department.\n**(6)**\nCoordinating energy activities of the Department with relevant Federal departments and agencies, including the Departments of Energy, Commerce, Defense, and Interior, and the United States International Development Finance Corporation to promote United States energy security and energy development to support United States national security readiness.\n**(7)**\nCoordinating the Department\u2019s engagement with foreign governments regarding protection of onshore and offshore critical energy infrastructure from sabotage or other deliberate interference by malign foreign actors.\n**(8)**\nAnalyzing and developing policies to counter the use of energy and critical minerals infrastructure and supply chain dependencies by adversaries to coerce, influence, or manipulate the United State and allied countries.\n**(9)**\nCoordinating energy security and other relevant functions within the Department, as appropriate.\n**(10)**\nWorking internationally to\u2014\n**(A)**\nsupport the development of energy technologies, natural resources, critical minerals, and supply chains for the benefit of the United States and United States allies and trading partners for their energy security and economic development needs;\n**(B)**\npromote secure and diversified energy and critical minerals supply chains, and a well-functioning global market for energy resources, energy technologies, critical minerals;\n**(C)**\ndevelop new policies and regulatory frameworks, multilateral initiatives, and other tools to protect allied onshore and offshore critical energy infrastructure from sabotage or other deliberate interference by malign foreign actors;\n**(D)**\ncounter the weaponization of energy and critical mineral dependencies by adversaries;\n**(E)**\nresolve international disputes regarding the exploration, development, production, or distribution of energy and critical minerals resources where United States strategic interests are present;\n**(F)**\nsupport the economic and commercial interests of United States persons operating in the energy markets of foreign countries; and\n**(G)**\nsupport and coordinate international efforts to alleviate energy poverty, enhance energy access and energy efficiency to promote United States strategic interests, and offer alternatives to adversary initiatives for United States allies and partners.\n**(11)**\nConducting public diplomacy with regard to United States international energy policy to strengthen transparency and good governance.\n**(12)**\nPerforming such other duties as the Under Secretary for Economic Affairs may from time to time designate.\n##### (c) Implementation report\nNot later than 180 days after the date of the enactment of this Act, the Assistant Secretary shall submit to the appropriate congressional committees a report on the status of efforts by the Department to establish the Bureau of Energy Security and Diplomacy required in section 302, including a description of current and projected staffing levels and resources deployed to execute the responsibilities described in paragraph (b).\n##### (d) Annual report\nNot later than one year after the date of the enactment of this Act, and annually thereafter for three years, the Assistant Secretary shall submit to Congress a report on the United States international energy strategy and the actions taken by the Bureau to fulfill such strategy.\n#### 302. Bureau of Energy Security and Diplomacy\n##### (a) Establishment\nThe Secretary shall establish a Bureau of Energy Security and Diplomacy, which shall perform such functions related to the formulation and implementation of international energy, energy technology, critical minerals, and relevant supply chain policies, as the Under Secretary for Economic Affairs may prescribe.\n##### (b) Assistant Secretary\nThe Assistant Secretary shall be the head of the Bureau.\n##### (c) Bureau employment\n**(1) Temporary expedited hiring authorities**\nFor a period of one year beginning on the date of the enactment of this Act, the Secretary may\u2014\n**(A)**\nappoint employees to the Bureau whose expertise aligns with the responsibilities listed in section 301(b) without regard to the provisions of title 5, United States Code, regarding appointments in the competitive service; and\n**(B)**\nfix the basic compensation of such employees without regard to chapter 51 and subchapter III of chapter 53 of such title regarding classification and General Schedule pay rates.\n**(2) Priority appointments**\nThe Secretary shall prioritize the appointment of employees to the Bureau\u2014\n**(A)**\nwho were separated from employment with the Bureau of Energy and Natural Resources in 2025 as a result of a reduction in force; and\n**(B)**\nwhose expertise aligns with the responsibilities listed in section 301(b).\n##### (d) Sense of Congress\nIt is the sense of Congress that the Assistant Secretary should be a standing participant in the Investment Committee or any other interagency working group established at or chaired by the White House National Security Council or National Economic Dominance Council to coordinate and implement United States policy regarding international critical mineral and energy supply chain diversification.\n#### 303. Critical Mineral Mining Fellowship Program\nThe Mutual Educational and Cultural Exchange Act of 1961 ( 22 U.S.C. 2451 et seq. ) is amended by adding at the end the following:\n116. Critical Mineral Mining Fellowship Program (a) Establishment There is authorized to be established the Critical Mineral Mining Fellowship Program (referred to in this section as the Fellowship Program ) within the J. William Fulbright Educational Exchange Program. (b) Purposes The purposes of the Fellowship Program are\u2014 (1) to advance foreign policy priorities of the United States by promoting studies, research, and international exchange in the mining industry; (2) to send United States citizens who are enrolled in or have received a degree from an accredited postsecondary institution in the United States to mining institutions in foreign countries, in order to build the capacity of the United States mining workforce; (3) to develop a robust and skilled workforce that can support and fill the gaps within the United States\u2019 growing domestic critical mineral supply chain; and (4) to reduce dependency on foreign energy and critical mineral supplies and enhance competitiveness of the United States within the global critical mineral marketplace. (c) Administration The Bureau of Educational and Cultural Affairs of the Department of State (referred to in this section as the Bureau ) shall administer the Fellowship Program in accordance with policy guidelines established by the Fulbright Foreign Scholarship Board (referred to in this section as the Board ), in consultation with binational Fulbright Commissions, mining industry leaders, institutions of higher education, governments of foreign countries, and United States Embassies in the foreign countries described in subparagraphs (A) and (B) of subsection (d)(4). (d) Selection of fellows (1) In general The Board shall select qualified individuals to participate in the Fellowship Program and ensure a broad geographic representation in order to develop region-specific specialties. (2) Number of fellows The Bureau shall determine the number of fellows selected each year. (3) Criteria for fellows (A) Participation requirements Each fellow shall\u2014 (i) have a conferred bachelor\u2019s or equivalent degree before the start of the Fellowship Program period; (ii) be a student currently enrolled in an institution of higher education in the United States completing an advanced degree in science, technology, engineering, mathematics, or a field relating to the mining industry; or (iii) have had a conferred postdoctoral degree for not longer than five years before the start of the Fellowship Program period. (B) Post-completion requirement Upon completion of the Fellowship Program, demonstrate intent to seek employment in a mining profession that directly benefits the growth, progress, and development of the mining industry in the United States Government, an academic institution, a private sector company, or any organization approved by the Bureau. (4) Eligible universities United States fellows shall attend universities approved by the Bureau, in consultation with the Committee on Foreign Affairs in the House of Representatives and the Committee on Foreign Relations of the Senate, that have a mining program and are located in a foreign country. To the extent practicable, the Bureau should prioritize fellow enrollment in higher education mining programs in\u2014 (A) member countries of the Minerals Security Partnership; or (B) any country identified by the Bureau, in consultation with the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate, as containing sufficiently qualified mining programs. (5) Outreach To the extent practicable, the Bureau shall conduct outreach at United States undergraduate and graduate institutions the Bureau determines are likely to produce a range of qualified applications for the Fellowship Programs. (e) Structure (1) Fellowship requirements To achieve the purposes described in subsection (b)\u2014 (A) each fellow selected pursuant to subsection (d)(1) is encouraged to arrange placement in a mining education program at an eligible university in a foreign country; (B) each fellow shall\u2014 (i) participate in advanced coursework, research projects, and practical training opportunities offered by the host institution; (ii) engage with faculty advisors and industry partners to gain hands-on experience through internships, laboratory work, and field studies relevant to the mining industry; (iii) serve as a cultural and academic ambassador of the United States, fostering mutual understanding in the academic and professional mining community of the foreign country; (iv) participate in professional development activities, such as conferences, workshops, and seminars, to expand knowledge of global best practices in mining engineering and related fields; and (v) build and strengthen networks with international peers, faculty, and industry professionals to facilitate ongoing collaboration and knowledge exchange; and (C) the Bureau shall, for each fellow, approve a work plan that identifies the target objectives for the fellow, including specific duties and responsibilities relating to those objectives. (2) Fellowship period (A) In general Each fellowship under this section shall continue for a period determined by the Bureau, which, whenever feasible, may not be less than one year. (B) Renewal A renewal for a second year may be granted only with the approval of the Bureau in consultation with a United States embassy or the Fulbright Commission. (f) Fellowship award The Bureau shall provide each fellow in the Fellowship Program with an allowance that is equal to the amount needed for the fellow\u2019s reasonable costs during the fellowship period, including\u2014 (1) mandatory university fees, including tuition, associated with graduate study; (2) living expenses, including housing, basic food costs, and daily transportation; (3) essential textbooks and other academic materials; (4) mandatory visa application, immigration fees, and other essential pre-departure requirements; (5) relocation expenses, including airline and rail travel; (6) research allowance, including essential travel to field sites and laboratory work; and (7) other reasonable costs approved by the Bureau. (g) Reports Not later than one year after the date of completion of the Fellowship Program by the initial cohort of fellows selected under subsection (d), and annually thereafter, the Secretary of State shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report providing information on the implementation of the Fellowship Program, including\u2014 (1) the demographics and geographical origins of the fellows who completed a Fellowship Program fellowship during the preceding 1-year period; (2) a description of the academic placements of the fellows and the relation of such placements to the development of United States region-specific specialties under the Fellowship Program, including participant feedback on program implementation and feedback on lessons learned; and (3) a plan for factoring lessons learned and acquired skills based knowledge into future Fellowship Program programming. .\n#### 304. Visiting Mining Scholars Program\nThe Mutual Educational and Cultural Exchange Act of 1961 ( 22 U.S.C. 2451 et seq. ), as amended by section 303 , is further amended by adding at the end the following:\n117. Visiting Mining Scholars Program (a) Establishment There is authorized to be established the Visiting Scholars Mining Program (referred to in this section as the Visiting Scholars Program ) within the J. William Fulbright Educational Exchange Program. (b) Purpose The purpose of the Visiting Scholars Program is to bring mining academics and professionals to the United States to\u2014 (1) build and expand the United States mining education programs at institutions of higher education; (2) bolster workforce development programs; and (3) advance research and development initiatives in the mining industry and adjacent fields. (c) Administration The Bureau of Educational and Cultural Affairs (referred to in this section as the Bureau ) shall administer the Visiting Scholars Program in accordance with policy guidelines established by the Fulbright Foreign Scholarship Board (referred to in this section as the \u2018Board\u2019), in consultation with binational Fulbright Commissions, mining industry leaders, institutions of higher education, foreign governments, and United States Embassies in the foreign countries described in clause (i) or (ii) of subsection (d)(3)(B). (d) Selection of visiting mining scholars (1) In general The Board shall select qualified individuals to participate in the Visiting Scholars Program, each of whom is not a citizen of the United States and\u2014 (A) is employed as a mining professional, practitioner, or operator in a foreign country; or (B) is employed as an academic working at an institution of higher education in a foreign country with a mining education program, as approved by a Fulbright Commission or United States embassy, in consultation with the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate. (2) Number of fellows The Bureau shall determine the number of fellows selected each year, which, whenever feasible, shall be not fewer than 10. (3) Eligible visiting mining scholars (A) Requirements Visiting mining scholars may not be citizens of the United States, and shall be\u2014 (i) a citizen of a country where another Fulbright Foreign Student Program operates; and (ii) a citizen of a country that has expertise or specialized knowledge or engages in practices that could benefit the mining industry. (B) Preferred countries To the extent practicable, the Board should prioritize selection of visiting mining scholars who live or work in\u2014 (i) a member country of the Minerals Security Partnership; or (ii) any country identified by the Bureau, in consultation with the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate, as containing individuals that have academic expertise or specialized knowledge or engage in practices that could benefit the mining industry. (4) Outreach To the extent practicable, the Bureau shall conduct outreach, in coordination with United States embassies, mining industry leaders, and mining institutions in foreign countries that are likely to produce a range of qualified applicants for the Visiting Scholars Program. (e) Structure (1) Program requirements To carry out the purpose described in subsection (b)\u2014 (A) each individual selected pursuant to subsection (d)(1) who is coming to the United States as a visiting mining scholar shall arrange placement in a United States academic institution approved by the Bureau; (B) each visiting mining scholar should\u2014 (i) consult with faculty members to provide technical assistance on how to develop or expand a mining education program at the host institution of higher education; (ii) assist in the development and review of mining education curricula, including course syllabi, laboratory modules, and fieldwork components; (iii) participate in collaborative research projects with faculty, students, and third-party research institutions, focusing on innovative mining technologies, sustainable mining practices, and resource management; (iv) facilitate partnerships between the host institution and mining organizations, government agencies, and other institutions to foster academic exchange, research collaboration, and workforce development; (v) mentor undergraduate and graduate students interested in mining education, offering guidance on academic projects and career development; and (vi) contribute to the development of outreach programs aimed at increasing awareness of the mining industry as a career path and to increase awareness of the types of mining professions available; and (C) the bureau shall, for each visiting mining scholar, approve a work plan that identifies the target objectives for the scholar, including specific duties and responsibilities relating to those objectives. (2) Eligible United States institutions Visiting mining scholars shall be placed in a United States institution of higher education approved by the Bureau that\u2014 (A) demonstrates a commitment to developing or expanding academic programs in the mining industry; (B) possesses existing faculty expertise or research activity in the mining industry or related extractive fields; (C) provides institutional support and resources, such as laboratory facilities, field sites, or equipment, relevant to mining education and research, including in geology; (D) demonstrates a commitment to integrate the visiting scholar into curriculum development, faculty training, or workforce pipeline initiatives in mining; (E) demonstrates a plan for sustaining mining or critical mineral resources programs beyond the duration of the visiting scholar\u2019s placement; (F) can provide evidence of student interest or regional workforce demand for mining education programs or training; and (G) agrees to provide mentoring, administrative support, and opportunities for the visiting scholar to engage with students, faculty, and local industry. (3) Scholarship period (A) In general The duration of each scholarship period under this section shall be determined by the Bureau and shall, whenever feasible, be not less than three months and not more than one year. (B) Exceptions Any exception to the duration of the scholarship period described in subparagraph (A) shall be submitted by the visiting mining scholar to and approved by the Bureau before such exception takes effect. (f) Scholarship award The Bureau shall provide each visiting mining scholar under this section with an allowance to cover the scholar\u2019s reasonable costs of living during the scholarship period. (g) Reports Not later than one year after the date of completion of the Visiting Mining Scholars Program by the initial cohort of scholars selected under subsection (d), and annually thereafter, the Secretary of State shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report providing information on the implementation of the Visiting Scholars Program, including\u2014 (1) the demographics and geographical origins of the cohort of scholars who completed a Visiting Scholars Program during the preceding 1-year period; (2) the United States universities that visiting scholars were placed in; (3) the foreign universities or other post-graduate institutions that the cohort of scholars were chosen from; (4) a description of academic placements selected, under the Visiting Scholars Program, including participant feedback on program implementation and feedback on lessons learned; and (5) a plan for factoring lessons learned into future programming. .\n#### 305. Amendment to the Mutual and Cultural Exchange Act of 1961\nSection 112(a) of the Mutual Educational and Cultural Exchange Act of 1961 ( 22 U.S.C. 2460(a) ) is amended\u2014\n**(1)**\nin paragraph (9), by striking ; and and inserting a semicolon;\n**(2)**\nin the first paragraph designated as paragraph (10), by striking the period at the end and inserting a semicolon;\n**(3)**\nby redesignating the second paragraph designated as paragraph (10) as paragraph (11);\n**(4)**\nin paragraph (11), as so redesignated, by striking the period at the end and inserting a semicolon; and\n**(5)**\nby adding at the end the following:\n(12) the Mining Fellowship Program established under section 116, which provides funding for studies, research, and international exchange for students seeking or completing advanced degrees from United States institutions of higher education in self-arranged placements with universities with mining education programs in foreign countries; and (13) the Visiting Mining Scholars Program established under section 117, which provides funding for international mining academics, practitioners, professionals and operators in self-arranged placements with universities in the United States. .\n#### 306. Definitions\nThe Mutual Educational and Cultural Exchange Act of 1961 ( 22 U.S.C. 2451 et seq. ), as amended by section 303 and section 304 , is further amended by adding at the end the following:\n118. Definitions In this Act: (1) Advanced degree The term advanced degree means a master\u2019s or doctoral degree from an institution of higher education. (2) Critical mineral The term critical mineral \u2014 (A) means any mineral on the list of critical minerals required by section 7002(c)(3) of the Energy Act of 2020 ( 30 U.S.C. 1606(c)(3) ) on or after January 1, 2026; and (B) includes gold and copper. (3) Institution of higher education The term institution of higher education , unless otherwise provided in this Act, has the meaning given such term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ). (4) Mining education program The term mining education program means an academic program related to the mining industry. (5) Mining industry The term mining industry means the mining industry of the United States, consisting of activities related to naturally occurring metal and nonmetal critical minerals, including the following: (A) Geological mapping, geophysical surveying, geochemical sampling, and management of geological data. (B) Mineral system analysis, exploration, and resource delineation, including exploratory drilling and resource estimation and classification. (C) Project development, feasibility studies, financing, and permitting. (D) Mine construction, extraction, and operational support activities. (E) Mineral processing, beneficiation, smelting, refining, chemical conversion, and separation. (F) Material conversion and advanced materials manufacturing. (G) Transportation, logistics, and handling of intermediate and finished material products. (H) Reclamation, remediation, reuse, recycling, and recovery of materials from primary and secondary sources, including mine waste and end-of-life products. (6) Mining profession The term mining profession means the body of jobs directly relevant to the mining industry. .",
      "versionDate": "2026-01-13",
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
        "name": "International Affairs",
        "updateDate": "2026-01-14T16:07:06Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7037ih.xml"
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
      "title": "Developing Overseas Mineral Investments and New Allied Networks for Critical Energies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T14:40:11Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Developing Overseas Mineral Investments and New Allied Networks for Critical Energies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-14T14:40:10Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote United States and allied energy and mineral security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-14T14:33:23Z"
    }
  ]
}
```
