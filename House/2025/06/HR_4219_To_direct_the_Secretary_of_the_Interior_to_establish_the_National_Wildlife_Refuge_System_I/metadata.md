# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4219?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4219
- Title: National Wildlife Refuge System Invasive Species Strike Team Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4219
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-04-27T14:55:49Z
- Update date including text: 2026-04-27T14:55:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-06-27 - IntroReferral: Sponsor introductory remarks on measure. (CR E631)
- 2026-04-09 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-16 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-06-27 - IntroReferral: Sponsor introductory remarks on measure. (CR E631)
- 2026-04-09 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-16 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4219",
    "number": "4219",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "National Wildlife Refuge System Invasive Species Strike Team Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-27T14:55:49Z",
    "updateDateIncludingText": "2026-04-27T14:55:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E631)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-16T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-04-09T14:33:35Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4219ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4219\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Case (for himself and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to establish the National Wildlife Refuge System Invasive Species Strike Team Program.\n#### 1. Short title\nThis Act may be cited as the National Wildlife Refuge System Invasive Species Strike Team Act of 2025 .\n#### 2. National Wildlife Refuge System Invasive Species Strike Team Program\n##### (a) Purpose\nThe purpose of this Act is to legislatively authorize the National Wildlife Refuge System Invasive Species Strike Team Program within the United States Fish and Wildlife Service to eradicate, control, and reduce the adverse effects of invasive species on and adjacent to National Wildlife Refuge System lands and waters, primarily through prevention, biosecurity, early detection, and rapid response.\n##### (b) Invasive Species Strike Team Program\n**(1) In general**\nThe Secretary shall carry out a program to identify and respond to priority invasive species threats within and adjacent to National Wildlife Refuge System lands and waters in coordination with partners, to be known as the National Wildlife Refuge System Invasive Species Strike Team Program .\n**(2) Requirements**\nIn carrying out the Program, the Secretary shall\u2014\n**(A)**\nestablish at least 1 invasive species strike team within each region of the United States Fish and Wildlife Service trained in early detection and rapid response for multiple invasive species taxa to\u2014\n**(i)**\nconserve, manage, and, where appropriate, restore, habitat conditions that help native biological communities flourish on and adjacent to National Wildlife Refuge System lands and waters;\n**(ii)**\nconduct prevention, early detection surveillance, eradication, containment, mapping, monitoring, and active management of invasive species;\n**(iii)**\nuse integrated pest management techniques and tools;\n**(iv)**\nconduct inreach and outreach, including trainings and table-top exercises, including on the use of the Incident Command System, as part of their planning and operations; and\n**(v)**\nuse risk assessments, research, innovations, management outcomes, monitoring, and evaluation to improve the effectiveness of detection and response activities;\n**(B)**\nengage in partnerships and collaborations with\u2014\n**(i)**\nFederal, State, Tribal, and local governments;\n**(ii)**\nnongovernmental institutions;\n**(iii)**\nnonprofit organizations; and\n**(iv)**\nprivate individuals and entities to advance mutual priorities and promote efficiency and cost-savings;\n**(C)**\ncollaborate in the development of a set of consistent taxonomy standards and work with others to implement such standards among all Department of the Interior databases; and\n**(D)**\nutilize national and regional standardized reporting platforms, such as\u2014\n**(i)**\nthe National Agricultural Pest Information System;\n**(ii)**\nthe National Data Repository of the National Plant Diagnostic Network;\n**(iii)**\nthe Early Detection and Distribution Mapping System;\n**(iv)**\nthe Nonindigenous Aquatic Species Database of the United States Geological Survey;\n**(v)**\niMapInvasives; and\n**(vi)**\nState databases.\n**(3) Provision of assistance**\nIn carrying out the Program, the Secretary is authorized to\u2014\n**(A)**\nconduct outreach to Federal, State, Territorial, local, and Tribal governments, nongovernmental institutions, nonprofit organizations, and private individuals and entities to address the management of property adjacent to a unit of the National Wildlife Refuge System, including providing or entering into, upon request\u2014\n**(i)**\nfinancial assistance, including direct expenditures;\n**(ii)**\ntechnical assistance;\n**(iii)**\ncontracts; or\n**(iv)**\ngrants or cooperative agreements; and\n**(B)**\nupon the request of another Federal department or agency or a State, Tribal, or Territorial agency, enter into an agreement within the mission and authorities of the United States Fish and Wildlife Service with such department or agency to provide the expertise and use of invasive species strike teams established under paragraph (2) to respond to invasive species under the jurisdiction of such department or agency, or to rapidly respond to a newly detected invasive species.\n**(4) Coordination of management actions**\nThe Secretary shall encourage the National Wildlife Refuge System to coordinate invasive species management actions of each Invasive Species Strike Team with adjacent landowners and the State agencies within the State of which Invasive Species Strike Team activities may occur.\n**(5) Report**\n**(A) In general**\nThe Secretary shall submit to the Committee on Appropriations and the Committee on Natural Resources of the House of Representatives and the Committee on Appropriations and the Committee on Environment and Public Works of the Senate, and make available to the public on the website of the United States Fish and Wildlife Service, a report regarding the Program 2 years after enactment and 5 years after enactment.\n**(B) Contents of report**\nEach report submitted under subparagraph (A) shall include\u2014\n**(i)**\na summary of each Invasive Species Strike Team\u2019s work to address priority invasive species within the National Wildlife Refuge System; and\n**(ii)**\nprogress made by the Program toward the prevention, detection, control, or eradication of each priority invasive species.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $15,000,000 for each of fiscal years 2026 through 2030.\n##### (d) Definitions\nIn this section:\n**(1) Invasive species**\nThe term invasive species means, with regard to a particular ecosystem, a non-native organism whose introduction causes or is likely to cause economic or environmental harm or harm to human, animal, or plant health.\n**(2) Early detection**\nThe term early detection means a process of surveying for, reporting, and verifying the presence of a non-native species before the founding population becomes established or spreads so widely that eradication is no longer feasible.\n**(3) Priority invasive species**\nThe term priority invasive species means an invasive species that is a major concern and necessary to map, monitor, and manage based on the following factors:\n**(A)**\nPotential impact on other native species.\n**(B)**\nAbility to alter habitats.\n**(C)**\nAbility to harm human health.\n**(D)**\nSeverity of economic impact.\n**(4) Program**\nThe term Program means the National Wildlife Refuge System Invasive Species Strike Team Program authorized under subsection (b)(1).\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service.\n**(6) State**\nThe term State means each of the several States, the District of Columbia, and each territory and possession of the United States.",
      "versionDate": "2025-06-27",
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
            "name": "Congressional oversight",
            "updateDate": "2026-04-27T14:55:49Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-04-27T14:55:27Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-04-27T14:55:34Z"
          },
          {
            "name": "Pest management",
            "updateDate": "2026-04-27T14:55:04Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-04-27T14:55:41Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2026-04-27T14:55:12Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-04-27T14:55:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-30T22:22:12Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4219ih.xml"
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
      "title": "National Wildlife Refuge System Invasive Species Strike Team Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Wildlife Refuge System Invasive Species Strike Team Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to establish the National Wildlife Refuge System Invasive Species Strike Team Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T04:18:30Z"
    }
  ]
}
```
