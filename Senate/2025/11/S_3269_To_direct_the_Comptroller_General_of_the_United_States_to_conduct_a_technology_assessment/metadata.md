# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3269?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3269
- Title: Liquid Cooling for AI Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3269
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-04-29T18:20:28Z
- Update date including text: 2026-04-29T18:20:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3269",
    "number": "3269",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Liquid Cooling for AI Act of 2025",
    "type": "S",
    "updateDate": "2026-04-29T18:20:28Z",
    "updateDateIncludingText": "2026-04-29T18:20:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
        "item": {
          "date": "2025-11-20T19:55:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-15T19:37:28Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "DE"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NC"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3269is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3269\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. McCormick (for himself, Mr. Coons , Mr. Budd , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Comptroller General of the United States to conduct a technology assessment focused on liquid cooling systems for artificial intelligence compute clusters and high-performance computing facilities, and for other purposes.\n#### 1. Short title and purpose\nThis Act may be cited as the Liquid Cooling for AI Act of 2025 .\n#### 2. Liquid cooling deployment and scalability\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe 2024 United States Data Center Energy Usage Report published by Lawrence Berkeley National Laboratory\u2014\n**(A)**\nindicates that data centers accounted for 4.4 percent of total United States electricity consumption in 2023, up from 1.9 percent in 2018; and\n**(B)**\nprojects that data centers could represent between 6.7 percent and 12.8 percent of total electricity consumption by 2028, due to the rapid growth of AI, cloud computing, and other digital technologies;\n**(2)**\ntraditional air-cooled systems are reaching limits to effectively remove heat from AI chips and hardware, and liquid cooling-enhanced thermal performance is increasingly becoming a necessity for high-density AI servers and data centers due to the growing power consumption and heat generation of AI workloads;\n**(3)**\nliquid cooling technologies, including direct-to-chip liquid cooling and single-phase or 2-phase immersion cooling, can improve thermal performance, enable higher densities, and reduce cooling system load when properly engineered and maintained;\n**(4)**\neffective liquid cooling deployments require interoperable components and engineered subsystems, including coolant distribution units, secondary loops, manifolds, hoses, quick-disconnects, valves, pumps, filters, leak detection and containment, corrosion control, and appropriate instrumentation and controls;\n**(5)**\ninterfaces for heat-reuse are integral to liquid systems and can reduce thermal load on heat-rejection equipment by transferring heat through plate heat exchangers or other devices to beneficial secondary uses where technically appropriate;\n**(6)**\nFederal agencies, including the Department of Energy, are considering the deployment of AI systems across Government-owned facilities; and\n**(7)**\na comprehensive, independent assessment of emerging data center architectures and cooling technologies is essential to inform efficient and cost-effective deployment decisions across the Federal Government.\n##### (b) Definitions\nIn this section:\n**(1) 2-phase**\nThe term 2-phase , with respect to a cooling process, means a process that leverages the heat-absorbing phase change from liquid to gas during the cooling cycle.\n**(2) AI**\nThe term AI has the meaning given the term artificial intelligence in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(3) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate;\n**(B)**\nthe Committee on Science, Space, and Technology of the House of Representatives; and\n**(C)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(4) Direct-to-chip liquid cooling**\nThe term direct-to-chip liquid cooling means a liquid cooling method that involves circulating a coolant in direct contact with applicable heat-generating components, such as processors and memory modules, to efficiently absorb and transfer heat away from those heat-generating components.\n**(5) Heat-reuse**\nThe term heat-reuse means the capture and transfer of waste heat from liquid loops for beneficial secondary use through appropriate interfaces and controls.\n**(6) Immersion cooling**\nThe term immersion cooling means a cooling technique that involves a dielectric fluid (single-phase or 2-phase) coming into direct contact with information technology components to capture and reject heat from an entire information technology system instead of a single component.\n**(7) Liquid cooling**\nThe term liquid cooling means utilization of liquids to remove heat efficiently from electronic components.\n**(8) National Laboratory**\nThe term National Laboratory has the meaning given the term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(9) Single-phase**\nThe term single-phase , with respect to a cooling process, means a process in which the coolant remains in the same liquid state throughout the entire cooling cycle.\n##### (c) GAO review\n**(1) In general**\nNot later than 30 days after the date of enactment of this Act, the Comptroller General of the United States shall initiate a review of\u2014\n**(A)**\nthe research and development needs relating to liquid cooling utilization by data centers; and\n**(B)**\nthe related market, technological, and regulatory conditions affecting that utilization.\n**(2) Elements**\nThe review required under paragraph (1) shall include the following:\n**(A)**\nAn evaluation of liquid cooling research and development needs, and the costs and benefits for high-performance computing.\n**(B)**\nA description of avoided costs of energy, including deferred and avoided new electric transmission and infrastructure upgrades and associated costs.\n**(C)**\nA description of increased compute capacity through the enabling of more use of energy for computing workloads rather than cooling.\n**(D)**\nA survey and analysis of existing research on the positive and negative effects of liquid cooling on computing performance, resiliency, and cybersecurity.\n**(E)**\nAn assessment of market trends and adoption rates of liquid cooling in United States data centers over the past 5 years and projections of future trends to account for the rapidly evolving industry and potential market outlook.\n**(F)**\nA comparison of single-phase and 2-phase direct-to-chip to single-phase and 2-phase immersion cooling across density bands, including relating to thermal performance, maintainability, interoperability, safety, failure modes, and lifecycle cost.\n**(G)**\nAn evaluation of\u2014\n**(i)**\ncoolant options, including water, water-glycol, and engineered fluids;\n**(ii)**\nmaterials compatibility;\n**(iii)**\ncorrosion control;\n**(iv)**\nbiogrowth mitigation;\n**(v)**\nfiltration;\n**(vi)**\nde-aeration;\n**(vii)**\nfluid monitoring and management;\n**(viii)**\nsingle-phase and 2-phase engineered fluids;\n**(ix)**\ntesting for total thermal performance;\n**(x)**\nheat transfer capacity; and\n**(xi)**\nenergy efficiency.\n**(H)**\nDevelopment of reference architectures and layouts for rack, row, and room-level liquid distribution by density band and cooling approach.\n**(I)**\nA survey of existing opportunities for reusing waste heat produced by data centers.\n**(J)**\nAn evaluation of failure scenarios (such as pump failures or fluid leaks) and mitigation strategies, especially in shared colocation environments.\n**(K)**\nRecommendations of the Comptroller General of the United States relating to\u2014\n**(i)**\nwhether liquid cooling should be considered as a primary cooling option over air cooling due to the thermal conditions of computing components in servers within data centers;\n**(ii)**\nthe utilization and ongoing research by the Federal Government of liquid cooling technologies;\n**(iii)**\nbest practices and industry standards for the design and operation of liquid cooling technologies;\n**(iv)**\nmethods to enhance the security, reliability, and resilience of computing equipment and data centers; and\n**(v)**\nmethods to accelerate education on operational best practices.\n**(3) Stakeholder input**\nFor purposes of recommending the best practices and industry standards described in paragraph (2)(K)(iii), the Comptroller General of the United States shall consult with stakeholders from Federal, State, and local governments, the private sector, academia, and National Laboratories.\n**(4) Liquid cooling advisory organization**\n**(A) In general**\nThe Secretary of Energy and the Comptroller General of the United States shall establish an advisory committee to consult and coordinate with in the preparation of the review under paragraph (2).\n**(B) Members**\nThe advisory committee established under subparagraph (A) shall consist of\u2014\n**(i)**\ninterested parties who\u2014\n**(I)**\nhave expertise in liquid cooling system applications in the development, operation, and functionality of AI factories or data centers, information technology equipment, or software; and\n**(II)**\nmay be members of liquid cooling industry organizations; and\n**(ii)**\nrepresentatives of hardware manufacturers, data center operators, fluid producers, or AI factory development.\n**(C) Consultation**\nThe advisory committee established under subparagraph (A) shall consult with relevant stakeholders, including the Department of Energy, the National Laboratories, and any college, university, research institution, industry association, company, or public interest group with applicable expertise in any of the subject matters areas described in subparagraph (C).\n**(D) Termination**\nThe advisory committee established under subparagraph (A) shall terminate on the date on which the Secretary of Energy submits a report and any recommendations under subsection (e).\n##### (d) Report\nNot later than 90 days after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Secretary of Energy and the appropriate congressional committees a report containing the results, findings, and any associated recommendations of the review required under subsection (c).\n##### (e) Department of Energy review\nNot later than 180 days after receiving the report from the Comptroller General of the United States under subsection (d), the Secretary of Energy shall submit to the appropriate congressional committees an assessment of the report and any associated recommendations, including\u2014\n**(1)**\nrelevant considerations for Congress regarding the importance of liquid cooling for the United States to maintain its global lead in AI technologies; and\n**(2)**\nrecommendations for research and development on liquid cooling and heat-reuse.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
            "updateDate": "2026-04-29T18:18:58Z"
          },
          {
            "name": "Building construction",
            "updateDate": "2026-04-29T18:20:28Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-04-29T18:18:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-29T18:19:40Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2026-04-29T18:18:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-29T18:19:57Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-29T18:19:47Z"
          },
          {
            "name": "Lighting, heating, cooling",
            "updateDate": "2026-04-29T18:20:22Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2026-04-29T18:19:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-01-06T19:24:38Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3269is.xml"
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
      "title": "Liquid Cooling for AI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Liquid Cooling for AI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Comptroller General of the United States to conduct a technology assessment focused on liquid cooling systems for artificial intelligence compute clusters and high-performance computing facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T05:48:20Z"
    }
  ]
}
```
