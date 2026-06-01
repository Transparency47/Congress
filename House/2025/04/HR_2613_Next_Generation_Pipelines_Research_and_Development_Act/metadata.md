# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2613?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2613
- Title: Next Generation Pipelines Research and Development Act
- Congress: 119
- Bill type: HR
- Bill number: 2613
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2025-11-06T16:50:11Z
- Update date including text: 2025-11-06T16:50:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-29 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-29 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2613",
    "number": "2613",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "W000814",
        "district": "14",
        "firstName": "Randy",
        "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
        "lastName": "Weber",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Next Generation Pipelines Research and Development Act",
    "type": "HR",
    "updateDate": "2025-11-06T16:50:11Z",
    "updateDateIncludingText": "2025-11-06T16:50:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
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
      "actionDate": "2025-04-02",
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
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
            "date": "2025-04-29T21:09:55Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-02T22:03:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2613ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2613\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Weber of Texas (for himself and Ms. Ross ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo improve public-private partnerships and increase Federal research, development, and demonstration related to the evolution of next generation pipeline systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Next Generation Pipelines Research and Development Act .\n#### 2. Definitions\nIn this Act:\n**(1) Department**\nThe term Department means the Department of Energy.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\nan institution of higher education (as such term is defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )), including historically Black colleges and universities (within the meaning of the term part B institution in section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 )), Tribal colleges and universities (as such term is defined in section 316 of the Higher Education Act of 1965 ( 20 U.S.C. 1059c )), and minority serving institutions (including the entities described in any of paragraphs (1) through (7) of section 371(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1067q(a) ));\n**(B)**\na nonprofit research organization;\n**(C)**\na National Laboratory (as such term is defined in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ));\n**(D)**\na private commercial entity;\n**(E)**\na partnership or consortium of two or more entities described in subparagraphs (A) through (D) that leverages existing Department efforts; or\n**(F)**\nany other entity the Secretary determines appropriate.\n**(3) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(4) Technical standards**\nThe term technical standard has the meaning given such term in section 12(d)(5) of the National Technology Transfer and Advancement Act of 1995 ( 15 U.S.C. 272 note).\n#### 3. Coordination\nIn carrying out this Act\u2014\n**(1)**\nthe Secretary shall avoid unnecessary duplication and achieve shared mission goals by coordinating with the Administrator of the Pipeline and Hazardous Materials Safety Administration of the Department of Transportation and across all relevant program offices at the Department of Energy, including\u2014\n**(A)**\nthe Office of Science;\n**(B)**\nthe Office of Fossil Energy and Carbon Management;\n**(C)**\nthe Office of Energy Efficiency and Renewable Energy;\n**(D)**\nthe Office of Cybersecurity, Energy Security, and Emergency Response;\n**(E)**\nthe Advanced Research Projects Agency\u2013Energy;\n**(F)**\nthe Office of Clean Energy Demonstrations; and\n**(G)**\nany other cross-cutting program office determined appropriate;\n**(2)**\nthe Secretary of Transportation shall ensure participation of and coordination with the Secretary of Energy of\u2014\n**(A)**\nthe Pipeline and Hazardous Materials Safety Administration of the Department of Transportation; and\n**(B)**\nany other program office of the Department of Transportation determined appropriate; and\n**(3)**\nthe Secretary shall coordinate with the Director of the National Institute of Standards and Technology, the Secretary of the Interior, and the heads of other relevant Federal agencies, as appropriate.\n#### 4. Advanced pipeline materials and technologies demonstration initiative\n##### (a) In general\nSubtitle E of title III of division D of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ) is amended by adding at the end the following new section:\n40344. Advanced pipeline materials and technologies demonstration initiative (a) Establishment of initiative The Secretary shall establish a demonstration initiative (in this section referred to as the Initiative ) under which the Secretary, through a competitive merit review process, shall award financial assistance to eligible entities to carry out demonstration projects on low- to mid-technology readiness level subjects to achieve deployment of technologies that\u2014 (1) are applicable to pipelines and associated infrastructure, including liquefied natural gas facilities and underground and above ground gas and liquid fuel storage facilities; and (2) involve the development of next generation pipeline systems, components, and related technologies. (b) Demonstration project focus areas In carrying out the Initiative, the Secretary shall select demonstration projects that best advance research undertaken by the Department and the Department of Transportation and incorporate a range of technology focus areas, which may include the following: (1) Advanced leak detection and mitigation tools and technologies. (2) Novel materials, including alloy and nonmetallic materials, to improve integrity for new and existing pipelines, such as pipeline coatings, sleeves, and liners, and corrosion resistant materials, including maximum and minimum flow rates and immunity to electrical discharge processes. (3) Technologies and methods for retrofitting existing pipelines, resolving material compatibility issues, and minimizing leakage, such as field protective coatings and material treatment. (4) Advanced manufacturing approaches for producing, fitting, and coupling pipelines, including the fabrication of higher performance pipeline materials and new extrusion technologies or methods to join ultra-high strength and corrosion resistant materials at a scale for distribution. (5) Advanced sensor technologies and processes that enable real-time or in situ monitoring of pipeline assets to assess and mitigate leaks, both internal and external to the pipeline, which may include the following: (A) Wireless sensors, such as surface acoustic wave sensors. (B) Advanced and cost-effective electrochemical sensors. (C) Distributed fiber optic sensors. (D) Autonomous sensor systems, including uncrewed aircraft. (E) Optical methods. (F) Multi-use platforms for diverse sources. (G) Hybrid data-analysis platforms. (6) Advanced computational, data analytics, and machine learning models to achieve the following: (A) Multiscale modeling, characterization, and optimization of transmission and distribution systems and components to aid in planning for optimized and resilient infrastructure. (B) Correlation between sensor and emissions data at all operational points and across a variety of scales to assure system integrity spanning large areas. (C) Accurate material lifecycle predictions and simulation platforms to forecast pipeline health. (D) Secure real time autonomous monitoring and repair capabilities. (E) Mapping and monitoring of structural health parameters, such as corrosion. (7) Self-healing and self-repair functionalities, including by chemical treatment methods. (8) Autonomous robotic and patch technologies for inspection and repair. (9) Dynamic compressor technologies, including retrofit kits for existing compressor systems. (10) Strategies and technologies for integrated cybersecurity considerations and countering cyberattacks. (11) Technologies and methods to reduce potential environmental impacts, including at the atmospheric and subsurface level, associated with pipelines, liquefied natural gas facilities, and gas and liquid fuel storage facilities, such as equipment failure. (12) Tools to evaluate geographical pipeline data for the feasibility of repurposing existing infrastructure for safe and effective transport and use of alternative fuels, blends, and carbon dioxide. (13) Tools and technologies applicable to improving the safety, operation, and efficiency of liquefied natural gas facilities and gas and liquid fuel storage facilities. (c) Selection requirements In selecting eligible entities for demonstration projects under the Initiative, the Secretary shall, to the maximum extent practicable, take the following actions: (1) Encourage regional diversity among eligible entities, including participation by such entities located in rural States. (2) Prioritize technological diversity among eligible entities. (3) Prioritize a diverse mix of energy, substances, fuel sources, and byproducts, including the following: (A) Gas and liquid hydrocarbons, including natural gas, renewable natural gas, methane, ethane, and liquefied natural gas. (B) Carbon dioxide. (C) Hydrogen. (D) Biofuels. (E) Water. (F) Substances in the hydrogen supply chain, including ammonia and liquid organic hydrogen carriers. (G) Blends of gases or liquids, including hydrogen blends. (H) Any other source the Secretary determines appropriate. (4) Prioritize projects that leverage and are complementary to existing energy infrastructure. (5) Prioritize projects that leverage matching funds from non-Federal sources. (6) Ensure that selected projects are coordinated with or expand on the existing technology demonstration programs of the Department. (7) Evaluate projects and topics for technical performance and economic feasibility as part of lifecycle assessments for return on investment impact. (8) Prioritize projects that can quantifiably reduce the environmental impacts of pipelines and associated infrastructure on air, water, or soil quality in all regions of the United States, especially in underserved and rural communities. (d) Location To the maximum extent practicable, demonstration projects under the Initiative shall be located on sites with existing research infrastructure or with the ability to coordinate with existing Department user facilities and research centers. (e) Authorization of appropriations Out of funds authorized to be appropriated for\u2014 (1) the Office of Energy Efficiency and Renewable Energy, and (2) the Office of Fossil Energy and Carbon Management, pursuant to paragraphs (1) and (6), respectively, of section 10771 of subtitle O of title VI of the Research and Development, Competition, and Innovation Act (enacted as division B of Public Law 117\u2013167 ), there is authorized to be appropriated to the Secretary of Energy to carry out this section $45,000,000 for fiscal year 2026, and $50,000,000 for each of fiscal years 2027 through 2030. (f) Sunset This section shall terminate five years after the date of the enactment of this section. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Infrastructure Investment and Jobs Act is amended by inserting after the item relating to section 40343 the following new item:\nSec. 40344. Advanced pipeline materials and technologies demonstration initiative. .\n#### 5. Joint research and development program\n##### (a) In general\nSubject to the availability of appropriations, the Secretary, in consultation with the Secretary of Transportation and the Director of the National Institute of Standards and Technology, and in coordination with the demonstration initiative established pursuant to section 40344 of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ), as added by section 4, shall establish within the Department a joint research and development program (referred to in this Act as the Joint Program ) to carry out research projects that\u2014\n**(1)**\ndevelop cost-effective advanced materials and technologies for pipeline transportation systems at different scales;\n**(2)**\nenable the commercialization of innovative materials and technologies for pipeline transportation systems;\n**(3)**\nsupport the development of technical standards of innovative materials and technologies for pipeline transportation systems; and\n**(4)**\nare at a low technology readiness level and not pursued by the Pipeline Safety Research Program of the Pipeline and Hazardous Materials Safety Administration of the Department of Transportation.\n##### (b) Memorandum of understanding\nNot later than one year after the date of the enactment of this Act, the Secretary shall enter into or update an existing memorandum of understanding with the Secretary of Transportation and the Director of the National Institute of Standards and Technology to administer the Joint Program. Such memorandum shall require each participating agency to\u2014\n**(1)**\nidentify unique research capabilities to contribute while avoiding duplication of existing efforts; and\n**(2)**\ninclude cost sharing and cost reimbursement abilities among participating agencies, including any reviews, approvals, trainings, or resource outlays that will be required.\n##### (c) Infrastructure\nIn carrying out the Joint Program, the Secretary, the Secretary of Transportation, and the Director of the National Institute of Standards and Technology shall\u2014\n**(1)**\nuse existing research infrastructure at\u2014\n**(A)**\nDepartment of Energy facilities, including National Laboratories;\n**(B)**\nDepartment of Transportation initiatives, including any such initiatives carried out through the Pipeline and Hazardous Materials Safety Administration; and\n**(C)**\nthe National Institute of Standards and Technology; and\n**(2)**\ndevelop new infrastructure for potential projects, if appropriate.\n##### (d) Goals and metrics\nThe Secretary, the Secretary of Transportation, and the Director of the National Institute of Standards and Technology shall develop goals and metrics for each agency, respectively, in meeting technological progress under the Joint Program, consistent with existing United States energy safety, resilience, and security policies.\n##### (e) Selection of projects\nTo the maximum extent practicable, the Secretary, the Secretary of Transportation, and the Director of the National Institute of Standards and Technology shall ensure the following with respect to the Joint Program:\n**(1)**\nProjects are carried out under conditions that represent a variety of geographies, physical conditions, and market constraints.\n**(2)**\nProjects represent an appropriate balance of the following:\n**(A)**\nLarger, higher-cost projects.\n**(B)**\nSmaller, lower-cost projects.\n**(3)**\nTo the maximum extent practicable, projects are transferred between participating agencies based on the stage of research and capabilities of each agency.\n##### (f) Priority\nIn carrying out the Joint Program, the Secretary, the Director of the National Institute of Standards and Technology, and the Secretary of Transportation shall, through consultation with the demonstration initiative established pursuant to section 40344 of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ), as added by section 4, identify and advance areas of research most needed for demonstration projects under such demonstration initiative, give priority to research and demonstration projects that\u2014\n**(1)**\nare likely to be of value to such demonstration initiative; and\n**(2)**\nare done in coordination with, or advance knowledge critical to, the National Pipeline Modernization Center established pursuant to section 6.\n##### (g) Relation to existing law\nNothing in this section may be construed to change existing agency roles, responsibilities, or areas of expertise as described in section 12 of the Pipeline Safety Improvement Act of 2002 ( Public Law 107\u2013355 ; 49 U.S.C. 60101 note).\n##### (h) Sunset\nThis section shall terminate five years after the date of the enactment of this section.\n#### 6. National Pipeline Modernization Center\n##### (a) In general\nIn carrying out the demonstration initiative established pursuant to section 40344 of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ), as added by section 4, and the Joint Program and subject to the availability of appropriations, the Secretary shall establish a National Pipeline Modernization Center (referred to in this Act as the Center ), which shall focus on collaborating with industry and stakeholders to coordinate and carry out research, development, and demonstration projects focused on commercializing cost-effective products and procedures aligned with the goals and priorities set forth by the Department.\n##### (b) Selection\nThe Secretary shall administer the Center in conjunction with an eligible entity pursuant to an agreement between the Department and such entity. Such entity shall be selected on a competitive, merit-reviewed basis.\n##### (c) Existing centers\nIn administering the Center, the Secretary shall prioritize higher education energy-related research centers in existence as of the date of the enactment of this Act.\n##### (d) Period of performance\nAn agreement under subsection (b) shall be for a period of not more than five years, subject to the availability of appropriations.\n##### (e) Location\nThe Center shall be located in proximity to critical transportation infrastructure connecting to an existing national pipeline transportation system and other Department monitoring assets, as determined by the Secretary.\n##### (f) Coordination with training and qualifications center\nIn carrying out the functions described in subsection (a), the Center shall coordinate and collaborate with training centers of the Pipeline and Hazardous Materials Safety Administration of the Department of Transportation to facilitate knowledge sharing among, and enhanced training opportunities for, Federal and State pipeline safety inspectors and investigators.\n##### (g) Duplication\nThe Secretary shall ensure the coordination of, and avoid unnecessary duplication of, the activities under this section with the National Center of Excellence for Liquefied Natural Gas Safety established pursuant to section 111 of the Protecting our Infrastructure of Pipelines and Enhancing Safety Act of 2020 ( 49 U.S.C. 60103 note; enacted as division R of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 )).\n#### 7. NIST pipeline metrology\n##### (a) In general\nSubject to the availability of appropriations, the Director of the National Institute of Standards and Technology shall carry out a program of measurement research, development, demonstration, and standardization to\u2014\n**(1)**\nensure the integrity of pipeline facilities; and\n**(2)**\nsupport pipeline safety, security, efficiency, sustainability, and resilience.\n##### (b) Testing\nThe Director of the National Institute of Standards and Technology, in collaboration with the Secretary of the Department of Transportation and in consultation with the private sector and international standards organizations, shall support testing, evaluation, and research infrastructure to support the activities described in subsection (a).\n##### (c) Allocation of appropriations\nFrom amounts appropriated or otherwise made available for the National Institute of Standards and Technology, the Director of the National Institute of Standards and Technology shall allocate up to $2,500,000 for each of fiscal years 2026 through 2030 to carry out this section.\n#### 8. Authorization of appropriations\n##### (a) In general\nOut of funds authorized to be appropriated for the Office of Energy Efficiency and Renewable Energy and the Office of Fossil Energy and Carbon Management pursuant to paragraphs (1) and (6), respectively, of section 10771 of subtitle O of title VI of the Research and Development, Competition, and Innovation Act (enacted as division B of Public Law 117\u2013167 ), there is authorized to be appropriated to the Secretary to carry out\u2014\n**(1)**\nsection 5, $20,000,000 for fiscal year 2026, and $30,000,000 for each of fiscal years 2027 through 2030; and\n**(2)**\nsection 6, $10,000,000 for fiscal year 2026, and $15,000,000 for each of fiscal years 2027 through 2030.\n##### (b) Offset\nSection 10771 of subtitle O of title VI of the Research and Development, Competition, and Innovation Act (enacted as division B of Public Law 117\u2013167 ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking 2026 and inserting 2030 ; and\n**(B)**\nin subparagraph (B), by striking 1,200,000,000 and inserting $1,100,000,000 ; and\n**(2)**\nin subsection (6)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking 2026 and inserting 2030 ;\n**(B)**\nin subparagraph (A), by striking 600,000,000 and inserting $445,000,000 ;\n**(C)**\nin subparagraph (B)\u2014\n**(i)**\nby striking 200,000,000 and inserting $100,000,000 ; and\n**(ii)**\nby striking and after the semicolon;\n**(D)**\nin subparagraph (C)\u2014\n**(i)**\nby striking 1,000,000,000 and inserting $900,000,000 ; and\n**(ii)**\nby striking the period and inserting ; and ; and\n**(E)**\nby adding at the end the following new subparagraph:\n(D) $455,000,000 to carry out pipeline research, development, demonstration, and commercial application activities. .",
      "versionDate": "2025-04-02",
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
            "updateDate": "2025-05-12T16:21:54Z"
          },
          {
            "name": "Air quality",
            "updateDate": "2025-05-12T16:37:14Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-05-12T16:48:56Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-05-12T16:24:53Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2025-05-12T16:21:06Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-05-12T16:22:38Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-05-12T16:29:16Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-05-12T16:20:48Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-05-12T16:32:17Z"
          },
          {
            "name": "Pipelines",
            "updateDate": "2025-05-12T16:21:36Z"
          },
          {
            "name": "Pollution liability",
            "updateDate": "2025-05-12T16:22:16Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-05-12T16:55:38Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-05-12T16:23:04Z"
          },
          {
            "name": "Soil pollution",
            "updateDate": "2025-05-12T16:37:21Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2025-05-12T16:29:52Z"
          },
          {
            "name": "Technology transfer and commercialization",
            "updateDate": "2025-05-12T16:28:33Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-05-12T16:37:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-04-09T14:18:14Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2613ih.xml"
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
      "title": "Next Generation Pipelines Research and Development Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Next Generation Pipelines Research and Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve public-private partnerships and increase Federal research, development, and demonstration related to the evolution of next generation pipeline systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:48:16Z"
    }
  ]
}
```
