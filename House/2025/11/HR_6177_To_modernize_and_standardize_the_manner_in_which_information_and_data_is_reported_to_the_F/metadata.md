# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6177?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6177
- Title: Grid Research and Development Act
- Congress: 119
- Bill type: HR
- Bill number: 6177
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-02-04T04:26:31Z
- Update date including text: 2026-02-04T04:26:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6177",
    "number": "6177",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Grid Research and Development Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:31Z",
    "updateDateIncludingText": "2026-02-04T04:26:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:08:25Z",
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
          "date": "2025-11-20T15:08:20Z",
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
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IN"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "PA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6177ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6177\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Casten (for himself, Mr. Levin , Mr. Huffman , Mr. Subramanyam , Mr. Quigley , Mr. Garamendi , Ms. Castor of Florida , Mr. Carson , Mr. Moulton , and Mr. Foster ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo modernize and standardize the manner in which information and data is reported to the Federal Energy Regulatory Commission, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Grid Research and Development Act .\n#### 2. Modernization of reporting information and data under the Federal Power Act\n##### (a) In general\nThe Commission shall, by rule, modernize and standardize the manner in which information and data are reported, by transmitting utilities and Transmission Organizations, to the Commission under the Federal Power Act ( 16 U.S.C. 972 et seq. ) in accordance with this section.\n##### (b) Content of reports requirements\nIn carrying out subsection (a), the Commission shall require the information and data that will be reported, as it applies to projects, existing assets, or systems owned or operated by a transmitting utility or Transmission Organization, to include the following:\n**(1)**\nInformation and data relating to a project and the lifecycle of such project, including\u2014\n**(A)**\nproject milestones, including proposed, approved, and actual in-service dates;\n**(B)**\nproject classification information, including whether the project represents new construction, an upgrade, or a rebuild of existing infrastructure;\n**(C)**\nmajor development history, including original construction and last major upgrade dates;\n**(D)**\nthe location of any applicable project;\n**(E)**\nthe project nameplate capacity, length, and voltage; and\n**(F)**\nan identification of the applicable planning process through which the applicable project originated.\n**(2)**\nThe costs and economic justifications of a project, existing asset, or system owned or operated by a transmitting utility or Transmission Organization, as applicable, including\u2014\n**(A)**\noriginal projected and actual final costs of all new projects;\n**(B)**\noriginal projected and actual final costs of renewals and replacements of project works;\n**(C)**\noriginal projected and actual maintenance and operations expenses of the projects and existing assets on a current-year and five-year rolling average basis;\n**(D)**\ncost allocation shares where applicable, including identification of entities responsible for shared investments in projects;\n**(E)**\ncost-benefit analyses of projects;\n**(F)**\nwhether the project was subject to a competitive solicitation process and, if applicable, the outcome of that process; and\n**(G)**\nclassification of the project based on benefits provided, under the relevant transmission planning framework.\n**(3)**\nThe capital structure and the rate of return of a project, existing asset, or system owned or operated by a transmitting utility or Tranmission Organization, including\u2014\n**(A)**\nthe allowed return on equity, return on debt, and return on preferred stock;\n**(B)**\nthe authorized or actual capital structure, including the percentage of debt, equity, and preferred stock used in ratemaking;\n**(C)**\nthe resulting overall weighted average rate of return;\n**(D)**\nany Commission-approved incentive adders applied to the base return on equity, including rationale and duration; and\n**(E)**\nwhere applicable, information necessary to assess potential double leveraging effects arising from a holding company structure, as defined by the Commission.\n**(4)**\nFor information and data relating to a system owned or operated by a transmitting utility or Transmission Organization, as applicable, congestion-related costs or the costs incurred by ratepayers, power supplies, or distribution customers as a result of transmission system constraints that prevent the dispatch of least-cost generation resources.\n**(5)**\nTechnical and non-technical losses and inefficiencies.\n**(6)**\nA complete accounting of interconnection-related costs incurred by interconnection customers, transmitting utilities, or other entities, disaggregated by cost type and responsible party, including\u2014\n**(A)**\nstudy fees;\n**(B)**\nmilestones or reservation payments;\n**(C)**\ncosts of local interconnection attachment facilities;\n**(D)**\ngrid network upgrade costs; and\n**(E)**\nestimates of costs to a larger system.\n**(7)**\nThe projected and actual capacity and load of a system owned or operated by a transmitting utility or Transmission Organization and the projected and actual amount of energy delivered by such system.\n**(8)**\nInformation and data on the use of capital-efficient advanced technologies, including information on\u2014\n**(A)**\nhourly usage;\n**(B)**\nthe location of the technologies; and\n**(C)**\nthe types of technologies deployed.\n**(9)**\nAny additional metric the Commission determines necessary to improve ratepayer affordability and understanding of the transmission sector.\n##### (c) Content of interconnection reports\nIn carrying out subsection (a), the Commission shall require a transmitting utility or Transmission Organization to report, no less than quarterly, to the Commission information and data on interconnection queues and details relating to interconnection study models used.\n##### (d) Format of reports\n**(1) In general**\nPursuant to subsection (a), the Commission shall ensure the completeness, accuracy, and accessibility of information and data reported to the Commission under the Federal Power Act, as the Commission determines necessary, by\u2014\n**(A)**\nestablishing standardized reporting requirements that specify standards for describing and recording such information and data, and, if the Commission determines appropriate, providing templates or other tools to reduce administrative burden;\n**(B)**\nproviding a format for such information and data to be submitted in a manner that is fully searchable and machine-readable;\n**(C)**\nrequiring any form filed by a transmitting utility or a Transmission Organization contains no blank cells, unless clearly marked as exempt pursuant to paragraph (2);\n**(D)**\nrequiring any projections required under subsection (a) are defined, including key assumptions, methodologies, and any other information that could influence the result of the projection; and\n**(E)**\nrequiring the information and data reported under this section are made available to the public through a single, user-friendly web interface that allows users to search, filter, and download the data in a machine-readable format.\n**(2) Exemption**\n**(A) In general**\nA transmitting utility or a Transmission Organization may request an exemption from a requirement under paragraph (1) if such transmitting utility or Transmission Organization submits to the Commission a written statement explaining why such an exemption is needed.\n**(B) Determination**\nThe Commission may approve the request for an exemption if the Commission determines that the exemption is justified based on the written statement submitted under subparagraph (A).\n##### (e) FERC Form No. 1\n**(1) In general**\nNot later than 1 year after the date on which the Commission issues a rule under subsection (a), the Commission shall review covered forms.\n**(2) Completeness**\nUpon reviewing covered forms under paragraph (1), if the Commission determines that a covered form is incomplete, the Commission shall require the relevant transmitting utility or Transmission Organization to file a revised FERC Form No. 1 in a manner that complies with the requirements of subsection (d) and the requirements under section 141.1 of title 18, Code of Federal Regulations (or any successor regulations).\n**(3) Covered form defined**\nIn this subsection, the term covered form means a FERC Form No. 1 filed with the Commission by a transmitting utility or Transmission Organization during the 5-year period immediately preceding the date of enactment of this Act.\n**(4) Modernization and centralization of FERC Form No. 1**\nNot later than 2 years after the date of enactment of this Act, the Commission, in collaboration with the Administrator, shall make all historical and future FERC Form No. 1 filings publicly available through the centralized data repository established under section 3.\n#### 3. Development of centralized data repository\n##### (a) In general\nThe Commission, in collaboration with the Administrator, shall develop and maintain a searchable and publicly accessible data repository containing information and data the Commission determines necessary to carry out the requirements of the Federal Power Act and this Act, including information and data reported or filed by a transmitting utility or Transmission Organization\u2014\n**(1)**\nin FERC Form Nos. 1, 1\u2013F, 3\u2013Q, 714, 715, and 730, including information or data from these forms reported prior to the date of enactment of this Act; and\n**(2)**\npursuant to the requirements of this Act.\n##### (b) EIA expertise\nIn collaborating with the Commission under this section with respect to the data repository developed under subsection (a), the Administrator shall\u2014\n**(1)**\ndevelop and maintain schemas and metadata for Form No. 1 data consistent with section 3506(b)(6) of title 44, United States Code;\n**(2)**\nprovide user-friendly tools to explore, download, and analyze such data, including filtering by utility, year, region, and data category; and\n**(3)**\nensure such data is accessible to the public in both bulk and disaggregated forms, with Application Programming Interfaces and visualization tools where feasible.\n##### (c) Requirements\nThe Commissioner shall ensure that the data repository developed and maintained under subsection (a)\u2014\n**(1)**\nincludes the data in fully searchable and machine-readable format;\n**(2)**\nis capable of including high-quality data through schemas and accompanying metadata;\n**(3)**\nensures consistent identification of data elements or assets that satisfy regulatory requirements for data, established by the Commission, as reflected in machine-readable metadata;\n**(4)**\nuses standardized data formats across all Transmission Organizations and transmitting utilities;\n**(5)**\nis used by Transmission Organizations and transmitting utilities to file reports required under the Federal Power Act and this Act;\n**(6)**\nenables uploading of reports filed under the Federal Power Act or this Act;\n**(7)**\nis optimized for operability by Transmission Organizations and transmitting utilities to limit the administrative burden of, and ensure consistency in, such filings;\n**(8)**\nincludes interactive tools and visualization interfaces to allow users to explore trends in transmission buildout, interconnection timelines, and associated ratepayer costs;\n**(9)**\nincorporates Application Programming Interfaces or bulk download functionality to support third-party analysis and research; and\n**(10)**\nensures that publicly accessible data is aligned with the security of guidelines for Critical Energy/Electric Infrastructure Information, and includes appropriate data anonymization and cybersecurity protections, based on Commission guidance.\n#### 4. Grid research and analytics\n##### (a) Research and policy analysis\nThe Secretary, in collaboration with the Commission, using standardized methodologies and anonymized queue data collected under this Act, shall conduct research and publish periodic reports on the following topics:\n**(1)**\nPrimary drivers of increased costs to ratepayers associated with transmission and interconnection, including\u2014\n**(A)**\ntransmission capital expenditures;\n**(B)**\ninterconnection-related upgrade costs;\n**(C)**\ninterconnection study delays;\n**(D)**\nregional variations in cost allocation methodologies; and\n**(E)**\ncost recovery practices by utilities and grid operators.\n**(2)**\nValue delivered to ratepayers from transmission and interconnection investments, including through\u2014\n**(A)**\nimprovements to electric system reliability;\n**(B)**\navoided emissions or emissions reductions; and\n**(C)**\nenhancements to long-term system resilience and grid flexibility.\n**(3)**\nMechanisms to enhance ratepayer affordability, including\u2014\n**(A)**\nevaluation of performance-based regulation frameworks applied to transmission and interconnection-related investments;\n**(B)**\nassessment of alternative interconnection solutions such as grid-enhancing technologies, shared infrastructure models, or consolidated upgrades; and\n**(C)**\nevaluation of demand-side interventions that reduce the need for costly transmission or interconnection investments.\n**(4)**\nComparative scenario modeling of potential energy futures, to\u2014\n**(A)**\nidentify lowest-cost pathways to national grid expansion;\n**(B)**\nassess trade-offs among investment strategies; and\n**(C)**\ninform decision-making by utilities, regional planning entities, and Federal agencies.\n**(5)**\nSystemic cost impacts from interconnection inefficiencies, including analysis of how study delays, queue withdrawals, and increased construction periods contribute to higher system costs for ratepayers or generators.\n**(6)**\nOpportunities to increase system efficiency and unlock latent capacity through improved operational practices and deployment of advanced technologies, including\u2014\n**(A)**\nassessment of unused or underutilized grid capacity due to outdated planning assumptions or lack of dynamic optimization;\n**(B)**\nevaluation of technologies such as dynamic line ratings, topology optimization, flexible interconnection, or flow control devices; and\n**(C)**\nquantification of benefits to ratepayers and system operators from unlocking this capacity relative to traditional capital-intensive buildout.\n##### (b) Interconnection transparency and dashboard\n**(1) In general**\nThe Secretary shall, through one or more National Laboratories, develop, maintain, and continuously improve an Interconnection Data Dashboard (in this section referred to as the Dashboard ) that presents real-time and historical information relevant to interconnection of generators, loads, and other utilities or transmission systems.\n**(2) Purpose**\nThe Dashboard shall provide public stakeholders, regulators, utilities, developers, and researchers with transparent, up-to-date insights into the effectiveness, efficiency, affordability, and reliability of interconnection processes across all transmission planning regions.\n**(3) Data sources**\nThe Dashboard shall incorporate data collected under section 3 of this Act and from FERC Form No. 1 filings, relevant Commission filings, publicly available interconnection queue data, and additional datasets, as determined appropriate by the Secretary or the Commission.\n**(4) Capabilities**\nThe Secretary shall develop the Dashboard to be able to\u2014\n**(A)**\npresent anonymized interconnection queue data, including application volumes, withdrawal rates, project timelines, and milestones;\n**(B)**\nprovide visualization of average and median interconnection study durations, disaggregated by region and project type;\n**(C)**\nshow aggregated system upgrade costs, study backlogs, and queue performance metrics;\n**(D)**\nallow filtering by geographic location (e.g., State, balancing authority, latitude/longitude coordinate), utility, fuel type, and project size;\n**(E)**\npresent each interconnection project\u2019s current development status, such as application submitted, study phase, approved, under construction, or in-service;\n**(F)**\ndisplay physical asset characteristics for each interconnection project and system segment, including nameplate generation capacity, peak load served, and conductor capacity ratings;\n**(G)**\nidentify trends in queue reform outcomes, including impacts on throughput, delay reduction, and project completion rates;\n**(H)**\nsupport export of underlying data in machine-readable formats for public analysis; and\n**(I)**\nperform any other function the Secretary determines appropriate.\n**(5) Reporting**\nThe Secretary, in collaboration with National Laboratories and the Commission, shall publish annual reports summarizing findings from the Dashboard, based on data collected pursuant to section 3, without substituting for the more comprehensive cost-driver analysis required under subsection (a), including\u2014\n**(A)**\ninterregional comparisons of queue efficiency and project success rates;\n**(B)**\nsystemic drivers of delay or cost escalation;\n**(C)**\nestimated ratepayer impacts associated with interconnection bottlenecks; and\n**(D)**\nrecommendations for improving interconnection transparency and system performance.\n**(6) Public access**\nThe Dashboard shall be made available on a public website and designed for use by a broad range of users, including through visualizations, downloadable datasets, and API access, while maintaining protections for CEII.\n#### 5. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Energy Information Administration of the Department of Energy.\n**(2) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(3) FERC Form no. 1**\nThe term FERC Form No. 1 means the Form of Annual Report for Major electric utilities, licensees, and others, designated as FERC Form No. 1 and prescribed under section 141.1 of title 18, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(4) Metadata**\nThe term metadata has the meaning given such term in section 3502 of title 44, United States Code.\n**(5) Project**\nThe term project refers exclusively to transmission infrastructure projects planned, proposed, or undertaken by the transmitting utility. This includes projects initiated through\u2014\n**(A)**\nregional or local transmission planning processes;\n**(B)**\ninterconnection studies;\n**(C)**\nreliability-driven upgrades; and\n**(D)**\nother applicable pathways as determined by the Commission.\n**(6) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(7) Federal Power Act terms**\nThe terms transmitting utility , and Transmission Organization have the meanings given those terms in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-12-04T15:00:45Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6177ih.xml"
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
      "title": "Grid Research and Development Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Grid Research and Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modernize and standardize the manner in which information and data is reported to the Federal Energy Regulatory Commission, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T04:33:22Z"
    }
  ]
}
```
