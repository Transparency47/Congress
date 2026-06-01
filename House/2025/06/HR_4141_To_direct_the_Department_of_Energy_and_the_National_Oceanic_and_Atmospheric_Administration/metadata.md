# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4141
- Title: Advanced Weather Model Computing Development Act
- Congress: 119
- Bill type: HR
- Bill number: 4141
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2025-12-17T09:06:06Z
- Update date including text: 2025-12-17T09:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-25 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-25 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4141",
    "number": "4141",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001222",
        "district": "7",
        "firstName": "Max",
        "fullName": "Rep. Miller, Max L. [R-OH-7]",
        "lastName": "Miller",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Advanced Weather Model Computing Development Act",
    "type": "HR",
    "updateDate": "2025-12-17T09:06:06Z",
    "updateDateIncludingText": "2025-12-17T09:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:00:40Z",
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
          "date": "2025-06-25T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
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
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NC"
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
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4141ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4141\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Miller of Ohio (for himself and Mrs. Foushee ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Department of Energy and the National Oceanic and Atmospheric Administration to conduct collaborative research in order to advance numerical weather and climate prediction in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advanced Weather Model Computing Development Act .\n#### 2. Computing research initiative\n##### (a) In general\nSection 108 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8518 ) is amended by striking subsection (a)(3)(C) and all that follows through subsection (b)(7) and inserting the following:\n(b) Artificial intelligence investments The Under Secretary shall leverage artificial intelligence and machine learning technologies to facilitate, optimize, and further leverage advanced computing to accomplish critical missions of the National Oceanic and Atmospheric Administration. (c) Centers of excellence The Under Secretary may expand, and where applicable establish, centers of excellence to aid the adoption of next-generation artificial intelligence and machine learning enabled advanced computing capabilities. Each such center may carry out activities that include the following: (1) Leveraging robust public-private partnership models to provide access to training, experience, and long-term development of workforce and infrastructure. (2) Developing and optimizing tools, libraries, algorithms, data structures, and other supporting software necessary for specific applications on high performance computing systems. (3) Applying modern artificial intelligence, deep machine-learning, and advanced data analysis technologies to address current and future mission challenges. (4) To the maximum extent practicable, exploring quantum computing and related application partnerships with public, private, and academic entities to improve the accuracy and resolution of weather predictions. (d) Multi-Year contracts The Under Secretary may enter into multi-year contracts in accordance with section 3903 of title 41, United States Code, and shall ensure compliance with all contract clauses provided in such section to support operations, research, and development related to high performance and cloud computing infrastructure or systems with an unfunded contingent liability in the event of cancellation. (e) Report (1) In general Not later than two years after the date of the enactment of this subsection, the Under Secretary, in collaboration with the Secretary of Energy shall submit to the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Energy and Natural Resources of the Senate a report evaluating the following: (A) A best estimate of the overall value of high-resolution probabilistic forecast guidance for hazardous weather or water events using a next-generation weather forecast and warning framework. (B) The needs for cloud computing, quantum computing, or high-performance computing, visualization, and dissemination collaboration between the Department of Energy and the National Oceanic and Atmospheric Administration. (C) A timeline and guidance for implementation of the following: (i) High-resolution numerical weather prediction models. (ii) Methods for meeting the cloud computing, quantum computing, or high-performance computing, visualization, and dissemination needs identified under subparagraph (b). (2) Hazardous weather or water events defined In this subsection, the term hazardous weather or water events means weather or water events that have a high risk of loss of life or property, including the following: (A) Severe storms, such as hurricanes and short-fused, small-scale hazardous weather or hydrologic events produced by thunderstorms, including large hail, damaging winds, tornadoes, and flash floods. (B) Winter storms, such as freezing or frozen precipitation (including freezing rain, sleet, and snow), or combined effects of freezing or frozen precipitation and strong winds. (C) Other weather hazards, such as extreme heat or cold, wildfire, drought, dense fog, high winds, and river, coastal, or lakeshore flooding. .\n##### (b) Strategic plan on high-Performance computing and data management needs\n**(1) In general**\nThe Under Secretary shall make publicly available not later than one year after the date of the enactment of this Act, and update every five years thereafter until 2035, a 10-year strategic plan that outlines the high-performance computing and data management requirements and needs of the National Oceanic and Atmospheric Administration and actions and strategies to address such requirements and needs.\n**(2) Plan elements**\nAt a minimum, the strategic plan required by paragraph (1) shall include the following:\n**(A)**\nA 10-year prospective outlook of computing resources and upgrades needed to meet the mission needs of the National Oceanic and Atmospheric Administration for fisheries management, oceanographic forecasting, and ecological forecasting missions.\n**(B)**\nA discussion of the following:\n**(i)**\nComputing and processing resources of the Administration and a 10-year projected need for such resources, disaggregated by line office of the Administration.\n**(ii)**\nFacilities, commercial contracts, and partnerships (with other Federal agencies or other institutions or entities) of the Administration that are providing computing and data management support or capacity as of such date.\n**(iii)**\nThe use by the Administration of cloud computing and other emerging technologies, such as artificial intelligence and machine learning.\n**(iv)**\nAdditional technologies that have the potential to increase effectiveness and efficiency for data storage and processing power, including challenges to access and use of such technologies.\n**(v)**\nThe distribution of computing resources among the operations and research functions of the Administration.\n**(vi)**\nProducts and services of the Administration that have not become available to the public because of a lack of computing resources.\n**(vii)**\nCurrent and future workforce development needs, such as information technology and software engineering, of the Administration.\n**(viii)**\nThe high-performance computing requirements of the Administration, with a special focus on requirements that are common across line offices of the Administration.\n**(C)**\nTimelines, and performance measures for assessing progress toward attaining goals for the following:\n**(i)**\nComputing infrastructure and architecture of the Administration (including facilities, hardware, and software).\n**(ii)**\nUse by the Administration of technologies that will increase effectiveness and efficiency for data storage and processing power, including challenges to access and use of such technologies.\n**(D)**\nA 10-year life cycle analysis of the management of facilities, hardware, and engineering involved in the strategic plan that includes the following:\n**(i)**\nProgram formulation for project conception, implementation, and closure.\n**(ii)**\nTechnical infrastructure, products, processes, data, and personnel resources required to achieve defined cost, schedule, and performance objectives.\n**(E)**\nIf appropriate, a description of actions taken to implement the previous plan.\n**(3) Public involvement**\nIn developing the strategic plan required by paragraph (1), the Under Secretary shall invite comments and other feedback from the public to inform the strategic plan.\n**(4) Annual briefings**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act and annually thereafter until 2030, the Under Secretary shall brief Congress on the progress made toward the objectives of the strategic plan required by paragraph (1).\n**(B) Elements**\nEach briefing required by subparagraph (A) shall include the following:\n**(i)**\nAn evaluation of the progress made in implementing the strategic plan.\n**(ii)**\nSuch updates to the strategic plan as the Under Secretary considers appropriate.",
      "versionDate": "2025-06-25",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-07-17T11:05:48Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4141ih.xml"
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
      "title": "Advanced Weather Model Computing Development Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advanced Weather Model Computing Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Department of Energy and the National Oceanic and Atmospheric Administration to conduct collaborative research in order to advance numerical weather and climate prediction in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T02:48:17Z"
    }
  ]
}
```
