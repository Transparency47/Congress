# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/453?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/453
- Title: Wildfire Intelligence Collaboration and Coordination Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 453
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-04-08T14:11:43Z
- Update date including text: 2026-04-08T14:11:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S794-795)
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S794-795)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/453",
    "number": "453",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Wildfire Intelligence Collaboration and Coordination Act of 2025",
    "type": "S",
    "updateDate": "2026-04-08T14:11:43Z",
    "updateDateIncludingText": "2026-04-08T14:11:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S794-795)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T18:06:43Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "AZ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s453is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 453\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Padilla (for himself, Mr. Sheehy , Mr. Daines , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo establish a Wildfire Intelligence Center, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Intelligence Collaboration and Coordination Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nwildfire management is a complex, multijurisdictional issue that requires an integration of efforts at all levels of society, including the Federal Government, State, Tribal, and local governments, and the private sector; and\n**(2)**\nthe report of the Wildland Fire Mitigation and Management Commission entitled On FIRE: The Report of the Wildland Fire Mitigation and Management Commission and dated September 2023 represents a consensus set of recommendations from 50 diverse experts to improve the outcomes from wildfire in the United States, finding that\u2014\n**(A)**\nrapidly changing ecosystems represent fundamental shifts in conditions that existing fire behavior models and existing fire management system are not designed to meet;\n**(B)**\nresearch, applied science programs, data management, and technology procurement and application relating to wildfire are housed within a wide array of Federal entities and academia, leading to a limited ability to set priorities and general inefficiencies;\n**(C)**\nvarious predictive services and decision-support functions exist to aid Federal managers and decisionmakers in the wildland fire community that, due to the different missions and jurisdictions of the Federal agencies involved and the fact that the services reside in several different Federal agencies, would benefit from improved interoperability and more coordinated priority setting and purchasing power; and\n**(D)**\nan interagency joint office should be established\u2014\n**(i)**\nwith membership from entities conducting research and addressing wildland fire management;\n**(ii)**\nwith dedicated and separate funding to fulfill the mission of comprehensive assessment and prediction of fire in the wildland and built environment interface through data aggregation and science-based decision-support services; and\n**(iii)**\nin close collaboration with the existing wildland fire management system in the United States.\n#### 3. Definitions\nIn this Act:\n**(1) Board**\nThe term Board means the Board for the Center appointed under section 4(e)(1).\n**(2) Center**\nThe term Center means the Wildfire Intelligence Center established by section 4(a).\n#### 4. Wildfire Intelligence Center\n##### (a) Establishment\nThere is established in the Department of Agriculture, the Department of Commerce, and the Department of the Interior a joint office, to be known as the Wildfire Intelligence Center , the duties of which are to study, plan, coordinate, and implement issues of joint concern among the Department of Agriculture, the Department of Commerce, and the Department of the Interior, including\u2014\n**(1)**\nserving as the development and operational center for the comprehensive assessment and prediction of fires that occur in the wildland and fires that move into the built environment to provide decision support services to inform land and fuels management, community outreach and risk reduction, post-wildfire recovery and rehabilitation, and fire management and response activities carried out by entities, including\u2014\n**(A)**\nthe Federal Government;\n**(B)**\nState, Tribal, and local governments;\n**(C)**\nland managers;\n**(D)**\nincident management teams;\n**(E)**\nthe National Interagency Coordination Center;\n**(F)**\ngeographic coordination centers;\n**(G)**\nland, air, and water managers;\n**(H)**\nburned area rehabilitation teams;\n**(I)**\npublic health entities; and\n**(J)**\nother entities identified by the Board;\n**(2)**\nfacilitating collaboration and information sharing across Federal and State departments and agencies, Tribal entities, academia, and the private sector on matters relating to wildland fires; and\n**(3)**\naddressing any other issues the Secretary of Agriculture, the Secretary of Commerce, and the Secretary of the Interior identify as issues of joint interest in support of the functions of the Center described in subsection (c).\n##### (b) Headquarters\nNot later than 1 year after the date of enactment of this Act, the Board shall select a permanent location for a physical headquarters of the Center within the United States.\n##### (c) Functions\nThe functions of the Center shall include the following:\n**(1)**\nProviding real-time, science-based, and data-rich scientific and technical analytical services, decision support, and predictive services across all phases of fire to inform pre-fire land and fuels management, pre-fire community and built environment risk reduction, active fire management and emergency response, and post-fire recovery in the built and natural environment.\n**(2)**\nAssessing and monitoring wildland fires and wildland fire conditions across all phases of fire, including ignition, behavior, and spread, climate, weather, drought, soil moisture, fuel conditions, smoke, aerosols, fire severity, debris flows, and erosion.\n**(3)**\nComprehensive modeling of wildland fire behavior and risks, including ignitions, wildland fire intensity and spread, air quality, and dependence on burn history, vegetation conditions, climate, and weather.\n**(4)**\nProviding and combining existing data, mapping, technological, and consultation services to support pre-, active, and post-fire activities, including\u2014\n**(A)**\ncreating and maintaining a real-time nationwide wildland fire risk catalog by leveraging existing risk mapping at land management agencies;\n**(B)**\nassisting with the creation of evacuation plans for at-risk communities;\n**(C)**\nassisting with the creation of public safety power shutoff plans;\n**(D)**\nassisting with the creation of wildland fire response strategies, plans, and treatment and mitigation measures;\n**(E)**\nproviding gridded and point data forecast and assessment products in support of operational and planning activities; and\n**(F)**\nproviding a testbed framework for testing and evaluation of new tools and products intended for decision support.\n**(5)**\nConsolidating air quality monitoring and forecasting data to support health risk information to help inform risks to public health and protect the public from smoke impacts associated with wildland fires, including providing planning guidance for safe and effective beneficial fire opportunities to prevent the risk of wildland fires.\n**(6)**\nProviding accessible tools and products that support emergency and land management decisions relating to wildland fire prevention, preparedness, and response, including risk assessment and contingency planning, which shall include the development of a data interface to assist and inform, in real-time, firefighters, first responders, and approved contractors in responding to wildland fires, including the use of any observations by the civil, military, and intelligence communities of the Federal Government and commercial Earth observations.\n**(7)**\nEstablishing an interoperable information technology infrastructure accessible by Federal agencies, State government offices, units of local government, and Tribal governments.\n**(8)**\nTo the extent feasible, establishing data interoperability through\u2014\n**(A)**\nthe development of common data standards;\n**(B)**\nthe provision of comprehensive searchable data inventories;\n**(C)**\nworking with Tribal governments in nation-to-nation partnership;\n**(D)**\nthe integration and sharing of information and resources of the Federal Government and State and local governments to support the essential functions of the Center;\n**(E)**\nthe development of data standards to protect confidential information that may be essential to the core functions of the Center;\n**(F)**\nregular updates and maintenance of research and technology essential to achieving the core functions of the Center; and\n**(G)**\nthe development and maintenance of a big-data architecture to compile, maintain, standardize, and evaluate data associated with the core functions of the Center.\n**(9)**\nIn coordination with relevant Federal agencies and coordinating bodies as determined by the Board, and in consultation with State government offices, units of local government, territories of the United States, and federally recognized Indian Tribes, developing and disseminating tools to support wildland fire planning, risk reduction and response guidance, guidelines, maps, and training materials to help inform State, territorial, local, and Tribal governments and decisionmakers with respect to\u2014\n**(A)**\nthe use and implementations of wildland fire risk assessments;\n**(B)**\nthe applied use of the database and information developed under paragraphs (7) and (8);\n**(C)**\nreducing losses from wildland fires;\n**(D)**\nincreasing benefits from wildland fires;\n**(E)**\nresources available for communities and responders working to improve wildland fire preparedness; and\n**(F)**\nenhancing communication management in emergency wildfire situations, land and resource management, and scientific studies.\n**(10)**\nWorking with Federal, State, and Tribal agencies to develop and improve National Wildland Coordinating Group wildland fire preparedness curricula and training modules for\u2014\n**(A)**\nState, territorial, local, and Tribal officials; and\n**(B)**\nFederal, State, territorial, local, and Tribal emergency managers and responders.\n##### (d) Administration\n**(1) In general**\nThe Secretary of Agriculture, the Secretary of Commerce, and the Secretary of the Interior shall cooperatively administer the Center.\n**(2) Transfer of funds**\n**(A) In general**\nSubject to subparagraph (B), the Secretary of Agriculture, the Secretary of Commerce, and the Secretary of the Interior may transfer funds between the Forest Service, National Oceanic and Atmospheric Administration, and the United States Geological Survey from funds provided to establish the Center and to carry out the duties of the Center.\n**(B) Notice required**\nNot less than 15 days prior to transferring funds under subparagraph (A), the Secretary of Agriculture, the Secretary of Commerce, or the Secretary of the Interior, as applicable, shall notify the Committee on Appropriations of the Senate and the Committee on Appropriations of the House of Representatives of the proposed transfer.\n##### (e) Board\n**(1) Number and appointment**\nThe Center shall be governed by a Board, composed of 14 members, as follows:\n**(A)**\n1 member who is a career employee of the Department of the Interior, to be appointed by the Secretary of the Interior.\n**(B)**\n1 member who is a career employee of the Bureau of Land Management, to be appointed by the Director of the Bureau of Land Management.\n**(C)**\n1 member who is a career employee of the Bureau of Indian Affairs, to be appointed by the Director of the Bureau of Indian Affairs.\n**(D)**\n1 member who is a career employee of the National Park Service, to be appointed by the Director of the National Park Service.\n**(E)**\n1 member who is a career employee of the United States Fish and Wildlife Service, to be appointed by the Director of the United States Fish and Wildlife Service.\n**(F)**\n1 member who is a career employee of the United States Geological Survey, to be appointed by the Director of the United States Geological Survey.\n**(G)**\n1 member who is a career employee of the Department of Agriculture, to be appointed by the Secretary of Agriculture.\n**(H)**\n1 member who is a career employee of the research and development areas of the Forest Service, to be appointed by the Chief of the Forest Service.\n**(I)**\n1 member who is a career employee in fire and aviation management of the Forest Service, to be appointed by the Chief of the Forest Service.\n**(J)**\n1 member who is a career employee of the National Oceanic and Atmospheric Administration, to be appointed by the Administrator of the National Oceanic and Atmospheric Administration.\n**(K)**\n1 member who is a career employee of the National Weather Service, to be appointed by the Director of the National Weather Service.\n**(L)**\n1 member who is a career employee of the Federal Emergency Management Agency, to be appointed by the Administrator of the Federal Emergency Management Agency.\n**(M)**\n1 member who is a career employee of the United States Fire Administration, to be appointed by the Administrator of the United States Fire Administration.\n**(N)**\n1 member who is a career employee of the Department of Defense, to be appointed by the Secretary of Defense.\n**(2) Terms**\nA member of the Board\u2014\n**(A)**\nshall be appointed for a term of 3 years; and\n**(B)**\nmay be reappointed for not more than 3 additional terms.\n**(3) Chairperson; Vice Chairperson**\nThe Chairperson and Vice Chairperson of the Board shall\u2014\n**(A)**\nbe selected by the members of the Board from among the members appointed under subparagraphs (F), (H), and (J) of paragraph (1); and\n**(B)**\nserve for a term of 1 year.\n**(4) Majority vote**\nVoting consensus by the Board shall be not less than 2/3 majority vote of the members present.\n**(5) Nonvoting status**\nAt the discretion of the Board, the Board may include nonvoting observers to the Board.\n##### (f) Executive Director\n**(1) In general**\nThe Center shall have an Executive Director, who shall be appointed by, and serve at the direction of, the Board.\n**(2) Private sector drought monitoring**\nThe Executive Director of the Center shall engage with entities in the private sector to improve drought monitoring, forecasting, communication, and response that may be essential to the core functions of the Center if the Executive Director of the Center determines that the engagement is appropriate, beneficial, and cost effective.\n**(3) Contracting authority**\n**(A) In general**\nThe Executive Director of the Center may enter into and perform contracts, leases, cooperative agreements, or other similar transactions that the Executive Director of the Center determines to be appropriate to carry out the functions of the Center.\n**(B) Report**\nNot later than 1 year after the date of enactment of this Act, the Board and the Executive Director of the Center shall submit to the appropriate committees of Congress a report that provides\u2014\n**(i)**\nan assessment of existing contracting authorities of the Executive Director of the Center; and\n**(ii)**\nrecommendations on whether new contracting authorities or modifications of existing contracting authorities are needed.\n##### (g) Detailees\nThe Secretary of Agriculture, the Secretary of Commerce, and the Secretary of the Interior may detail or assign to the Center such employees of the Department of Agriculture, the Department of Commerce, and the Department of the Interior, respectively, as are determined by the Secretary of Agriculture, the Secretary of Commerce, and the Secretary of the Interior, respectively, to be necessary to carry out the duties of the Center.\n##### (h) Interagency financing\nNotwithstanding section 708 of the Financial Services and General Government Appropriations Act, 2023 ( Public Law 117\u2013328 ; 136 Stat. 4706), or any other similar provision of law, interagency financing may be used to fund the Center.\n##### (i) Coordination with other agencies and entities\nThe Board shall coordinate with agencies represented on the Board and other relevant entities to achieve the core functions of the Center, including with\u2014\n**(1)**\nthe National Wildfire Coordinating Group;\n**(2)**\nState and Tribal governments;\n**(3)**\nany other agency\u2014\n**(A)**\nthat is responsible for the management of Federal or State land; or\n**(B)**\nthat has data, science, and technology expertise relevant to the Center; and\n**(4)**\nany other relevant Federal, State, Tribal, or nongovernmental entity that is representative of an element of the wildland fire community.",
      "versionDate": "2025-02-06",
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
            "updateDate": "2025-11-21T15:39:19Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-11-21T15:39:49Z"
          },
          {
            "name": "Air quality",
            "updateDate": "2025-11-21T15:38:44Z"
          },
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2025-11-21T15:38:58Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-11-21T15:39:26Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-11-21T15:40:09Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T14:11:43Z"
          },
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-11-21T15:38:16Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-11-21T15:38:39Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-11-21T15:39:11Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-11-21T15:38:09Z"
          },
          {
            "name": "Environmental technology",
            "updateDate": "2025-11-21T15:38:51Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-11-21T15:37:57Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-11-21T15:39:39Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-11-21T15:37:51Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-11-21T15:39:04Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-11-21T15:38:25Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-11-21T15:40:03Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-11-21T15:39:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-06T13:16:45Z"
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
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s453is.xml"
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
      "title": "Wildfire Intelligence Collaboration and Coordination Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wildfire Intelligence Collaboration and Coordination Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Wildfire Intelligence Center, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:43Z"
    }
  ]
}
```
