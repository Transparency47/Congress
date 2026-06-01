# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5964?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5964
- Title: Integrated Resource Planning Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 5964
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-19T09:08:18Z
- Update date including text: 2025-12-19T09:08:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5964",
    "number": "5964",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Integrated Resource Planning Modernization Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:08:18Z",
    "updateDateIncludingText": "2025-12-19T09:08:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:07:05Z",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "HI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MI"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "NV"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5964ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5964\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Ms. Leger Fernandez (for herself, Mr. Case , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Energy, acting through the Office of Electricity, to publish guidelines and best practices for integrated resource planning of the electricity system, provide technical assistance with respect to such guidelines and best practices, and develop a grant program for modernizing integrated resource planning, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Integrated Resource Planning Modernization Act .\n#### 2. Development of guidelines and best practices for electric utility integrated resource planning\n##### (a) In general\nThe Secretary, in consultation with State public utility commissions, State energy offices, owners or operators of electric utilities (including investor-owned utilities, municipal utilities, and electric cooperatives), balancing area authorities, Transmission Organizations, and other relevant stakeholders, shall develop guidelines and best practices for integrated resource planning of the electricity system.\n##### (b) Requirements\n**(1) Key issues**\nThe guidelines and best practices developed under subsection (a) shall address key issues related to integrated resource planning. In developing the guidelines and best practices, the Secretary shall consider, at a minimum, the following issues, while retaining discretion to incorporate additional considerations and to refine the scope, level of detail, and implementation approaches for each issue as appropriate:\n**(A)**\nDeveloping capacity expansion modeling and resource adequacy analysis in an iterative manner to improve integrated resource planning by ensuring the expanded electricity system achieves resource adequacy while minimizing costs.\n**(B)**\nThe consideration of a wide range of alternatives for capacity expansion models to meet resource adequacy targets, including the traditional expansion of electricity generation and transmission capacity and the use of novel grid-enhancing technologies, small and large-scale storage, distributed energy resources, behind-the-meter interventions, and demand-side interventions.\n**(C)**\nExplicit consideration of electric transmission in capacity expansion modeling and its contribution to resource adequacy and reliability of electricity systems.\n**(D)**\nThe use of an interregional planning approach in capacity expansion modeling to evaluate the resource adequacy benefits of capacity resource sharing across regions, including through collaboration between States, balancing area authorities, electric utilities, Transmission Organizations, and other relevant stakeholders.\n**(E)**\nThe integration of technical, financial, and regulatory information from other fuel supply systems, such as the natural gas network.\n**(F)**\nThe use of scenario analysis developed using capacity expansion modeling and transmission expansion modeling to represent a full range of future characteristics of the electricity system, including the availability of different electricity generating and storage resources, and transmission infrastructure.\n**(G)**\nThe use of probabilistic models in resource adequacy analysis to account for variability and uncertainty in the supply and demand of electricity, including the impact of extreme weather event scenarios, forecasting errors, fuel prices, and other uncertainties on such supply and demand.\n**(H)**\nThe use of historical weather data and forward-looking meteorological projections, including with respect to extreme weather event scenarios, to account for the variability in electricity demand, electricity generation from individual or groups of electricity generators, and electricity system outages to assess resource adequacy.\n**(I)**\nThe use of multiple resource adequacy metrics for assessing resource adequacy to account for the magnitudes, frequencies, and durations of potential events that stress the electricity system.\n**(J)**\nThe use of scorecards that summarize the costs and a wide range of benefits of scenarios developed through the integrated resource planning process, including\u2014\n**(i)**\ncosts of infrastructure investments;\n**(ii)**\nenvironmental sustainability;\n**(iii)**\nresource adequacy and reliability;\n**(iv)**\neconomic impacts; and\n**(v)**\nother costs and benefits that are relevant to the decision-making objectives of States, electric utilities, balancing area authorities, Transmission Organizations, and other relevant stakeholders.\n**(K)**\nThe use of rigorous mechanisms for capacity accreditation to measure the capacity value of possible investments that support resource adequacy, including\u2014\n**(i)**\ncapacity values for both conventional and emerging generation resources, including distributed energy resources and behind-the-meter interventions;\n**(ii)**\ncapacity values for demand-side interventions; and\n**(iii)**\ncapacity values for transmission infrastructure upgrades and grid-enhancing technologies that enable the deliverability of generating capacity from remote or otherwise constrained generation resources.\n**(L)**\nThe use of probabilistic metrics to measure capacity values that account for probability distributions of the magnitudes, frequencies, and durations of potential events that affect the availability of\u2014\n**(i)**\nconventional and emerging generation resources, behind-the-meter interventions, and demand-side interventions; and\n**(ii)**\ntransmission infrastructure upgrades and grid-enhancing technologies that enable the deliverability of electricity from remote or otherwise constrained generation resources.\n**(2) State treatment of integrated resource plans**\nIn developing the guidelines and best practices under subsection (a), the Secretary shall consider providing guidance on how State public utility commissions and State energy offices may review and respond to integrated resource plans, including guidance on\u2014\n**(A)**\nopportunities for public engagement and comment, including well-designed stakeholder involvement processes with several opportunities for feedback and transparent access to data inputs, models, licenses, and other requirements for relevant stakeholders to replicate modeling outputs from integrated resource planning; and\n**(B)**\nthe connection between integrated resource planning outcomes and regulatory actions, such as procurement decisions, certificates of public convenience and necessity, and general rate cases.\n##### (c) Publication of guidelines and best practices\nNot later than 2 years after the date of enactment of this Act, the Secretary shall publish on a publicly accessible website of the Department of Energy the guidelines and best practices developed under subsection (a).\n##### (d) Periodic evaluations and revisions\nThe Secretary shall, not less frequently than once every 5 years\u2014\n**(1)**\nevaluate the guidelines and best practices published under this section; and\n**(2)**\nrevise such guidelines and best practices and publish such revised guidelines and best practices in accordance with this section.\n#### 3. Technical assistance\nThe Secretary shall provide to State public utility commissions, State energy offices, owners or operators of electric utilities, balancing area authorities, Transmission Organizations, and other relevant stakeholders training resources and technical assistance (including workshops, training sessions, and education materials) to increase understanding of the guidelines and best practices published under section 2.\n#### 4. Integrated resource planning modernization grants program\n##### (a) Establishment\nThe Secretary shall establish a program, to be known as the Integrated Resource Planning Modernization Grants Program , under which the Secretary shall, subject to the availability of appropriations, provide grants to States in accordance with this section.\n##### (b) State implementation plans\n**(1) In general**\nA State may apply for a grant under the Integrated Resource Planning Modernization Grants Program by submitting to the Secretary a plan describing how the State intends to use the grant in accordance with subsection (c).\n**(2) Progress report**\nNot later than 2 years after a State receives a grant under the Integrated Resource Planning Modernization Grants Program, the State shall submit to the Secretary a report describing how the grant has been used and the progress the State has made\u2014\n**(A)**\nin the case of a vertically integrated State, developing or updating the integrated resource planning requirements, statutes, or regulations of the State; and\n**(B)**\nin the case of a restructured State, coordinating with electric utilities, balancing area authorities, and Transmission Organizations to develop and implement a strategy to employ integrated resource planning in the State.\n##### (c) Use of grants\n**(1) Vertically integrated States**\nA vertically integrated State that receives a grant under the Integrated Resource Planning Modernization Grants Program\u2014\n**(A)**\nshall use the grant to\u2014\n**(i)**\ndevelop or update integrated resource planning requirements, statutes, or regulations of the State to be partly or fully consistent with guidelines and best practices published under section 2;\n**(ii)**\nsupport regulated electric utilities with complying with such requirements, statutes, or regulations; and\n**(iii)**\nsupport non-regulated electric utilities (including municipal utilities and electric cooperatives) that choose to participate in integrated resource planning that complies with such requirements, statutes, or regulations; and\n**(B)**\nmay use the grant to\u2014\n**(i)**\npay expenses associated with consultants (including private consultants and federally funded research and development centers), staffing, software and modeling, and stakeholder engagement activities necessary for the State public utility commission and State energy offices to develop or update integrated resource planning requirements, statutes, or regulations of the State as described in subparagraph (A)(i); and\n**(ii)**\nprovide amounts to electric utilities, balancing area authorities, and Transmission Organizations, which may be used to recover the costs of complying with such requirements, statutes, or regulations.\n**(2) Restructured States**\nA restructured State that receives a grant under the Integrated Resource Planning Modernization Grants Program\u2014\n**(A)**\nshall use the grant to coordinate with electric utilities, balancing area authorities, and Transmission Organizations to develop and implement a strategy to employ integrated resource planning in the State that is partly or fully consistent with the guidelines and best practices published under section 2; and\n**(B)**\nmay use such grant to\u2014\n**(i)**\npay expenses associated with consultants (including private consultants and federally funded research and development centers), staffing, software and modeling, and stakeholder engagement activities necessary for the State to develop and implement a strategy to employ integrated resource planning in the State as described in subparagraph (A); and\n**(ii)**\nprovide amounts to electric utilities, balancing area authorities, and Transmission Organizations, which may be used to recover the costs of implementing the strategy described in subparagraph (A).\n##### (d) First applications\nA State may apply for a grant provided under the Integrated Resource Planning Modernization Grants Program beginning not later than 6 months after the initial publication of the guidelines and best practices under section 2.\n##### (e) Deadline To use grant\nA State that receives a grant provided under the Integrated Resource Planning Modernization Grants Program shall use such grant by not later than the date that is 5 years after the date on which the State received the grant.\n##### (f) Grant formula\nThe Secretary shall determine the amount of a grant provided under the Integrated Resource Planning Modernization Grants Program based on\u2014\n**(1)**\nwhether the State already requires electric utilities to employ integrated resource planning;\n**(2)**\nthe comprehensiveness of the State\u2019s implementation plan submitted under subsection (b), including the extent to which the implementation plan incorporates components of the guidelines and best practices published under section 2;\n**(3)**\nthe number of electricity consumers in the State;\n**(4)**\nthe capacity and mix of electric generating and transmitting infrastructure in the State;\n**(5)**\nthe number and diversity of electric utilities, balancing area authorities, and Transmission Organizations engaged in the electricity system planning and operation activities of the State; and\n**(6)**\nany other factor the Secretary determines appropriate to support integrated resource planning.\n#### 5. Coordination with other Federal programs\nThe Secretary may coordinate with other Federal programs related to energy resilience and modernization of the electricity system to\u2014\n**(1)**\nmaximize the impact of grants provided under the Integrated Resource Planning Modernization Grants Program by aligning efforts and avoiding duplication; and\n**(2)**\nensure that the guidelines and best practices published under this Act complement and support other Federal initiatives aimed at enhancing the resilience and reliability of electricity systems.\n#### 6. Periodic reports\nNot later than 5 years after the date of enactment of this Act, and not less frequently than once every 5 years thereafter, the Secretary shall submit to the appropriate congressional committees a report that includes the following:\n**(1)**\nA description of how vertically integrated States and restructured States used grants provided under the Integrated Resource Planning Modernization Grants Program.\n**(2)**\nA breakdown of the expenses paid using such grants.\n**(3)**\nAn assessment of the effectiveness of the use of the grants in supporting the development of, and compliance with, integrated resource planning that is partly or fully consistent with the guidelines and best practices published under this Act, including examples of best practices and innovative approaches that were adopted.\n#### 7. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Commerce of the House of Representatives; and\n**(B)**\nthe Committee on Energy and Natural Resources of the Senate.\n**(2) Balancing area authority**\nThe term balancing area authority means the responsible entity that\u2014\n**(A)**\nintegrates resource plans in advance of real-time operations;\n**(B)**\nmaintains the balance between electricity demand, electricity supply, and scheduled interchange within the geographic area of the responsible entity; and\n**(C)**\nsupports interconnection frequency in real-time.\n**(3) Behind-the-meter intervention**\nThe term behind-the-meter intervention \u2014\n**(A)**\nmeans an action or technology that reduces or shifts electricity demand or provides local electricity generation or storage capacity at the site of a customer; and\n**(B)**\nincludes\u2014\n**(i)**\nan energy efficiency upgrade, a residential solar panel, an energy storage system, and the actions taken under a demand response program; and\n**(ii)**\ninterventions that help to reduce strain on the electricity system and improve the reliability of the electricity system during peak demand periods or emergencies.\n**(4) Capacity accreditation**\nThe term capacity accreditation means the process of determining a capacity value.\n**(5) Capacity expansion modeling**\nThe term capacity expansion modeling means mathematical modeling to identify the least cost investments in generation, storage, behind-the-meter interventions, distributed resource, and transmission infrastructure required to meet future electricity demand, subject to fuel prices, technology cost and performance, policy and regulation, and other constraints and conditions.\n**(6) Capacity value**\nThe term capacity value \u2014\n**(A)**\nmeans a measure of the contribution to resource adequacy by\u2014\n**(i)**\na conventional or emerging generating resource, behind-the-meter intervention, or demand-side intervention; or\n**(ii)**\na transmission infrastructure upgrade or grid-enhancing technology that enables the deliverability of electricity from remote or otherwise constrained generation resources; and\n**(B)**\nincludes probabilistic metrics such as effective load-carrying capacity, equivalent firm capacity, and equivalent conventional power.\n**(7) Distributed energy resource**\nThe term distributed energy resource means a small-scale electricity generation or storage system that is located close to the point of use, such as a rooftop solar panel, home energy storage system, or community wind power system.\n**(8) Electric cooperative**\nThe term electric cooperative means a not-for-profit entity that\u2014\n**(A)**\nprovides electricity to members of the entity; and\n**(B)**\nis owned and operated by such members.\n**(9) Grid-enhancing technology**\nThe term grid-enhancing technology \u2014\n**(A)**\nmeans a technology designed to improve the reliability, efficiency, or flexibility of the electricity system; and\n**(B)**\nincludes a smart grid technology, an energy storage system, and an advanced grid management system.\n**(10) Integrated resource planning**\nThe term integrated resource planning has the meaning given such term in section 3 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2602 ).\n**(11) Municipal utility**\nThe term municipal utility means a municipal corporation that operates facilities used to generate, purchase, transmit, or distribute electricity to consumers.\n**(12) Resource adequacy**\nThe term resource adequacy means the ability of the electricity system to maintain sufficient, available generating, storage, and transmitting capacity and supporting infrastructure to meet forecasted electricity demand and system reliability requirements under a range of expected and adverse weather-sensitive conditions, including peak load events, generation availability, and unplanned outages.\n**(13) Resource adequacy metric**\nThe term resource adequacy metric \u2014\n**(A)**\nmeans a quantitative measure of the resource adequacy of the electricity system; and\n**(B)**\nincludes metrics derived from probabilistic analysis, such as loss-of-load expectation, loss-of-load hours, loss-of-load days, loss-of-load years, loss-of-load probability, loss-of-load events, expected unserved energy, and normalized expected unserved energy.\n**(14) Restructured State**\nThe term restructured State means a State in which the electricity system has been functionally separated such that independent power producers provide generation services, while Transmission Organizations operate electricity markets and the bulk transmission of electricity, and investor-owned utilities typically retain responsibility for distribution services and deliver electricity to retail customers.\n**(15) Secretary**\nThe term Secretary means the Secretary of Energy, acting through the head of the Office of Electricity of the Department of Energy.\n**(16) Transmission Organization**\nThe term Transmission Organization has the meaning given such term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(17) Vertically integrated State**\nThe term vertically integrated State means a State in which the electricity system remains functionally aggregated such that a regulated electric utility owns and operates the assets used for generating, transmitting, and distributing electricity within a particular service area within the State.",
      "versionDate": "2025-11-07",
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
        "name": "Energy",
        "updateDate": "2025-11-19T12:45:11Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5964ih.xml"
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
      "title": "Integrated Resource Planning Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-12T15:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Integrated Resource Planning Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-12T15:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Energy, acting through the Office of Electricity, to publish guidelines and best practices for integrated resource planning of the electricity system, provide technical assistance with respect to such guidelines and best practices, and develop a grant program for modernizing integrated resource planning, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-12T15:03:16Z"
    }
  ]
}
```
