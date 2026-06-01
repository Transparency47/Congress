# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5332
- Title: Liquid Cooling for AI Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5332
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2026-03-20T08:06:56Z
- Update date including text: 2026-03-20T08:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5332",
    "number": "5332",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Liquid Cooling for AI Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-20T08:06:56Z",
    "updateDateIncludingText": "2026-03-20T08:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-11T13:00:20Z",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NJ"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "DE"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "IN"
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
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NC"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "NJ"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5332ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5332\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Obernolte (for himself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Comptroller General of the United States to conduct a technology assessment focused on liquid-cooling systems for artificial-intelligence compute clusters and high-performance computing facilities, require the development of Federal Government-wide best-practice guidance for Federal agencies, and for other purposes.\n#### 1. Short title and purpose\nThis Act may be cited as the Liquid Cooling for AI Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe 2024 United States Data Center Energy Usage Report published by Lawrence Berkeley National Laboratory indicates that data centers accounted for 4.4 percent of total United States electricity consumption in 2023, up from 1.9 percent in 2018. The report further projects that data centers could represent between 6.7 percent and 12.8 percent of total electricity consumption by 2028, due to the rapid growth of AI, cloud computing, and other digital technologies.\n**(2)**\nTraditional air-cooled systems are reaching limits to effectively remove heat from AI chips and hardware, and liquid cooling enhanced thermal performance is increasingly becoming a necessity for high-density AI servers and data centers due to the growing power consumption and heat generation of AI workloads.\n**(3)**\nLiquid\u2011cooling technologies, including direct\u2011to\u2011chip (DTC) liquid cooling and single\u2011phase or two\u2011phase immersion cooling, can improve thermal performance, enable higher densities, and reduce cooling system load when properly engineered and maintained.\n**(4)**\nEffective liquid\u2011cooling deployments require interoperable components and engineered subsystems, including coolant distribution units, secondary loops, manifolds, hoses, quick\u2011disconnects, valves, pumps, filters, leak detection and containment, corrosion control, and appropriate instrumentation and controls.\n**(5)**\nInterfaces for heat\u2011reuse are integral to liquid systems and can reduce thermal load on heat\u2011rejection equipment by transferring heat through plate heat exchangers or other devices to beneficial secondary uses where technically appropriate.\n**(6)**\nFederal agencies, including the Department of Energy, are considering the deployment of AI systems across government-owned facilities.\n**(7)**\nA comprehensive, independent assessment of emerging data center architectures and cooling technologies is essential to inform efficient and cost-effective deployment decisions across the Federal Government.\n#### 3. Liquid cooling deployment and scalability\n##### (a) GAO review\nNot later than 30 days after the date of the enactment of this Act, the Comptroller General of the United States shall initiate a review of the research and development needs, and the related market, technological, and regulatory conditions, affecting liquid cooling utilization by data centers.\n##### (b) Elements\nThe review required under subsection (a) shall include the following:\n**(1)**\nAn evaluation of liquid cooling research and development needs, and the costs and benefits for high performance computing.\n**(2)**\nA description of avoided costs of energy, including deferred and avoided new electric transmission and infrastructure upgrades and associated costs.\n**(3)**\nA description of increased compute capacity by enabling more energy to be used for computing workloads rather than cooling.\n**(4)**\nA survey and analysis of existing research on the positive and negative effects of liquid cooling on computing performance, resiliency, and cybersecurity.\n**(5)**\nAn assessment of market trends and adoption rates of liquid cooling in United States data centers over the past five years.\n**(6)**\nA comparison of direct\u2011to\u2011chip (DTC) liquid cooling and immersion cooling approaches across representative density bands, including relating to thermal performance, maintainability, interoperability, safety, failure modes, and lifecycle cost.\n**(7)**\nAn evaluation of coolant options, including water, water\u2011glycol, and engineered fluids, materials compatibility, corrosion control, bio growth mitigation, filtration, deaeration, and fluid monitoring and management.\n**(8)**\nRecommendations relating to whether liquid cooling should be considered as a primary cooling option over air cooling due to the thermal conditions of computing components in servers within data centers.\n**(9)**\nDevelopment of reference architectures and layouts for rack, row, and room\u2011level liquid distribution by density band and cooling approach.\n**(10)**\nA survey of existing opportunities for reusing waste heat produced by data centers.\n**(11)**\nAn evaluation of failure scenarios (such as pump failures or fluid leaks) and mitigation strategies, especially in shared co-location environments.\n##### (c) Requirements\n**(1) Recommendations**\nIn preparing the review required under subsection (a), the Comptroller General of the United States shall include recommendations, including considerations relating to the following:\n**(A)**\nThe Federal Government\u2019s utilization of and ongoing research on liquid cooling technologies.\n**(B)**\nBest practices and industry standards for the design and operation of liquid cooling technologies.\n**(C)**\nMethods to enhance the security, reliability, and resilience of computing equipment and data centers.\n**(D)**\nMethods to accelerate education on operational best practices.\n**(2) Stakeholder input**\nWith the goal of identifying the best practices and industry standards referred to in paragraph (1)(A), the Comptroller General of the United States shall consult with stakeholders from Federal, State, and local governments, the private sector, academia, and National Laboratories.\n**(3) Liquid cooling advisory organization**\n**(A) In general**\nIn furtherance of the review required under subsection (a), including the identification of best practices and industry standards referred to in paragraph (1)(A), the Secretary of Energy and the Comptroller General of the United States shall jointly designate a liquid cooling industry organization with which to consult and coordinate in the preparation of such review.\n**(B) Requirements**\nThe organization designated pursuant to subparagraph (A), whether preexisting or formed specifically for the purposes described in such subparagraph, shall satisfy the following criteria:\n**(i)**\nConsist of interested parties who have expertise in liquid cooling system applications in the development, operation, and functionality of AI factories or data centers, information technology equipment, or software, as well as representatives of hardware manufacturers, data center operators, or AI factory development.\n**(ii)**\nConsult with relevant stakeholders, including the Department of Energy, the National Laboratories, and any college, university, research institution, industry association, company, or public interest group with applicable expertise in any of the subject matters areas specified in clause (i).\n**(iii)**\nHave as its mission the development and promotion of liquid cooling for data centers and information technology.\n##### (d) Report\nNot later than 90 days after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Secretary of Energy and the appropriate congressional committees a written report containing the results, findings, and any associated recommendations of the review required under subsection (a).\n##### (e) Department of Energy review\nNot later than 180 days after receiving the report from the Comptroller General of the United States under subsection (d), the Secretary of Energy shall\u2014\n**(1)**\nevaluate such report and any associated recommendations; and\n**(2)**\nsubmit to the appropriate congressional committees an assessment of such report and any associated recommendations, including\u2014\n**(A)**\nrelevant considerations for Congress regarding the importance of liquid cooling for the United States to maintain its global lead in AI technologies; and\n**(B)**\nrecommendations for research and development on liquid cooling and heat-reuse.\n##### (f) Definitions\nIn this section:\n**(1) AI**\nThe term AI has the meaning given the term artificial intelligence in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Science, Space, and Technology and the Committee on Energy and Commerce of the House of Representatives.\n**(3) Direct\u2011to\u2011chip (DTC) liquid cooling**\nThe term direct-to-chip (DTC) liquid cooling means a liquid cooling method that involves circulating a coolant in direct contact with applicable heat-generating components, such as processors and memory modules, to efficiently absorb and transfer heat away.\n**(4) Heat\u2011reuse**\nThe term heat-reuse means the capture and transfer of waste heat from liquid loops for beneficial secondary use through appropriate interfaces and controls.\n**(5) Immersion cooling**\nThe term immersion cooling means a cooling technique that involves submerging electronic components in a dielectric fluid to absorb and dissipate heat within a preset temperature range.\n**(6) Liquid cooling**\nThe term liquid cooling means utilization of liquids to remove heat efficiently from electronic components.\n**(7) National Laboratory**\nThe term National Laboratory has the meaning given such term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).",
      "versionDate": "2025-09-11",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-09-26T18:03:23Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-09-26T18:04:24Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-09-26T18:03:29Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-26T18:04:44Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-09-26T18:04:38Z"
          },
          {
            "name": "Lighting, heating, cooling",
            "updateDate": "2025-09-26T18:03:37Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2025-09-26T18:03:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-24T15:16:45Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5332ih.xml"
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
      "title": "Liquid Cooling for AI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-23T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Liquid Cooling for AI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-23T04:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Comptroller General of the United States to conduct a technology assessment focused on liquid-cooling systems for artificial-intelligence compute clusters and high-performance computing facilities, require the development of Federal Government-wide best-practice guidance for Federal agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-23T04:18:18Z"
    }
  ]
}
```
