# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4302?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4302
- Title: Improving Atmospheric River Forecasts Act
- Congress: 119
- Bill type: HR
- Bill number: 4302
- Origin chamber: House
- Introduced date: 2025-07-07
- Update date: 2025-09-15T15:50:13Z
- Update date including text: 2025-09-15T15:50:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-07: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-07-07: Introduced in House

## Actions

- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-07",
    "latestAction": {
      "actionDate": "2025-07-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4302",
    "number": "4302",
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
    "title": "Improving Atmospheric River Forecasts Act",
    "type": "HR",
    "updateDate": "2025-09-15T15:50:13Z",
    "updateDateIncludingText": "2025-09-15T15:50:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-07",
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
      "actionDate": "2025-07-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-07",
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
          "date": "2025-07-07T14:00:40Z",
          "name": "Referred To"
        }
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
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-07-07",
      "state": "CA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-07-07",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
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
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4302ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4302\nIN THE HOUSE OF REPRESENTATIVES\nJuly 7, 2025 Mr. Obernolte (for himself, Mr. Fong , and Mr. Whitesides ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo accelerate subseasonal to seasonal prediction skills related to precipitation forecasts for water management in the western United States, improve atmospheric river forecasts across the country, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Atmospheric River Forecasts Act .\n#### 2. Subseasonal to seasonal forecasting pilot projects\n##### (a) Improving subseasonal and seasonal forecasts\nSubsection (h) of section 1762 of the Food Security Act of 1985 ( 15 U.S.C. 8521 ) is amended to read as follows:\n(h) Subseasonal to seasonal forecasting pilot projects (1) Establishment The Under Secretary shall establish at least one pilot project within the U.S. Weather Research Program of the Oceanic and Atmospheric Research office of the National Oceanic and Atmospheric Administration to support improved subseasonal to seasonal precipitation forecasts for water management in the western United States. (2) Objectives In carrying out this subsection, the Under Secretary shall ensure that a pilot project under paragraph (1) addresses key science challenges to improving forecasts and developing related products described in subsection (c) for water management in the western United States, including the following: (A) Improving model resolution, both horizontal and vertical, to resolve issues associated with mountainous terrain, such as intensity of precipitation and relative fraction of rain versus snow precipitation. (B) Improving fidelity in modeling of\u2014 (i) the atmospheric boundary layer in mountainous regions; and (ii) atmospheric rivers. (C) Resolving challenges in predicting winter atmospheric circulation and storm tracks, including periods of blocked versus unblocked flow over the eastern North Pacific Ocean and western United States. (D) Advancing scientific understanding of the roles of atmospheric rivers in subseasonal to seasonal precipitation, and developing tools to predict periods of active or inactive atmospheric river landfalls and inland penetration over the western United States. (3) Activities A pilot project under this subsection shall be carried out in coordination with the Assistant Administrator for the Office of Oceanic and Atmospheric Research and the Director of the National Weather Service and include activities that carry out the following: (A) Best implement recommendations of the National Weather Service\u2019s 2019 Report, entitled Subseasonal and Seasonal Forecasting Innovation: Plans for the Twenty-First Century . (B) Achieve measurable objectives for operational forecast improvement. (C) Engage with, and leverage the resources of, institutions of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )) with experience in western precipitation science, as well as entities within the National Oceanic and Atmospheric Administration in existence as of the date of the enactment of this subsection, including the Western Regional Climate Center and the National Centers for Environmental Information. (4) Authorization of appropriations From amounts made available to Operations, Research, and Facilities at the National Oceanic and Atmospheric Administration, there is authorized to be appropriated $15,000,000 for each of fiscal years 2026 through 2030 to carry out this subsection. (5) Sunset The authority under this subsection shall terminate on the date that is five years after the date of the enactment of this subsection. .\n#### 3. Atmospheric rivers forecast improvement program\n##### (a) In general\nThe Under Secretary, in collaboration with the United States weather industry and academic partners, shall establish an atmospheric river forecast improvement program (in this section referred to as the program ).\n##### (b) Goal\nThe goal of the program shall be to reduce the loss of life and property and economic losses from atmospheric rivers through the research, development, and extension of accurate, effective, and actionable forecasts and warnings, including by carrying out the following:\n**(1)**\nEstablishing atmospheric river forecast skill metrics that include assessing the benefits of dynamical modeling, data assimilation, and machine learning improvements in the probabilistic forecasts of landfall location, extreme wind and precipitation, and cascading impacts.\n**(2)**\nDeveloping an atmospheric river forecast system within a unified forecast system, and advancing next-generation coupled modeling systems, with the capability of providing seasonal to short-range atmospheric river forecasts that include forecast of snow accumulation and other hydrologic components.\n**(3)**\nAdvancing scientific understanding of the roles of atmospheric rivers in subseasonal to seasonal precipitation and probabilistic predictions at subseasonal and seasonal scales.\n**(4)**\nDeveloping tools and improved forecast products to predict periods of active or inactive atmospheric river landfalls and inland penetration over the United States with a focus on addressing stakeholder and public needs related to perceiving, comprehending, and responding to atmospheric river forecast improvements.\n**(5)**\nEnhancing the transition of research to operations through the National Oceanic and Atmospheric Administration\u2019s testbeds, including the evaluation of physical and social science, technology, and other research to develop products and services for implementation and use by relevant stakeholders.\n**(6)**\nIncorporating into atmospheric river modeling and forecasting, as appropriate, social, behavioral, risk, communication, and economic sciences.\n##### (c) Innovative observations, data assimilation, and modeling\nThe Under Secretary shall ensure the program periodically examines, tests, and evaluates the value of incorporating innovative observations, data, and measurements with respect to the improvement of atmospheric river analysis, modeling, forecasts, predictions, and warnings.\n##### (d) Program plan\nNot later than 270 days after the date of the enactment of this Act, the Under Secretary, in consultation with the Secretary of the Air Force or the Commander of the 53rd Weather Reconnaissance Squadron of the Air Force Reserve Command, shall develop a plan that details the specific research, development, data acquisition, partnerships with the weather industry and academic partners, and technology transfer activities, as well as corresponding resources, and timelines, necessary to achieve the goal of the program under subsection (b). Such plan shall be made available to the public on release.\n##### (e) Annual budget for plan submittal\nAfter the development of the plan pursuant to subsection (d), the Under Secretary shall, not less frequently than annually, submit to Congress a proposed budget corresponding with the activities identified in such plan.\n##### (f) Improved modeling\nIn carrying out the program, the Under Secretary may carry out the following:\n**(1)**\nDevelop, test, and operationalize prototype high-resolution Atmospheric River Analysis and Forecasting System models through research and operations partnerships with institutions of higher education and other partners outside the National Oceanic and Atmospheric Administration.\n**(2)**\nEnhance data assimilation of current and new satellite and ocean observations that is useful for atmospheric river analysis and forecasting predictions.\n**(3)**\nImprove data processing techniques related to atmospheric river analysis and forecasting predictions.\n**(4)**\nUse artificial intelligence and machine learning methods as applicable to atmospheric river analysis and forecasting predictions.\n**(5)**\nEnsure the surface and subsurface observations of the ocean meet the needs of atmospheric river analysis and forecasting predictions on different time scales.\n**(6)**\nTo the maximum extent practicable, improve or establish baseline weather monitoring services in areas that have historically experienced, or are predicted to experience, atmospheric rivers.\n##### (g) Conduct of reconnaissance\nThe Under Secretary shall acquire and sustain adequate aircraft, scientific equipment, and personnel to meet mission requirements of the National Hurricane Operations Plan and the National Winter Seasons Operation plan, and to carry out the following:\n**(1)**\nEnsure atmospheric river air reconnaissance observations are available throughout the expected seasons of tropical cyclones and atmospheric rivers.\n**(2)**\nTo the maximum extent practicable and in accordance with paragraph (4), ensure data and information collected are made available for research and operations purposes.\n**(3)**\nParticipate in research and operations partnerships that guide flight planning and use research methods to improve and expand the capabilities and effectiveness of atmospheric river reconnaissance over time.\n**(4)**\nDevelop data management strategies to ensure that data and metadata are adequately stewarded, maintained, and archived.\n**(5)**\nUndertake such other additional activities as the Under Secretary, in consultation with the Secretary of the Air Force, considers appropriate to improve and grow the hurricane hunter and atmospheric river reconnaissance mission.\n##### (h) Improved atmospheric river hazard communication\nThe Under Secretary may conduct research and development activities to carry out the following:\n**(1)**\nAs appropriate, develop and refine methods to categorize the intensity of weather and oceans hazards, including tropical cyclones and atmospheric rivers, on a quantitative scale and the effectiveness of such scale in hazard communication.\n**(2)**\nDevelop best practices for communication of atmospheric river events and hazards across regions of the United States.\n**(3)**\nGather information from areas prone to hurricanes and atmospheric rivers regarding levels of knowledge and preparedness, including responses to early forecasts and warnings by the National Oceanic and Atmospheric Administration.\n**(4)**\nExplore strategies and effectiveness of communicating that hurricane and atmospheric river events are beneficial at lower intensities versus hazardous at higher intensity.\n##### (i) Definitions\nIn this section, the terms seasonal , subseasonal , Under Secretary , and weather industry have the meanings given such terms in section 2 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 ).",
      "versionDate": "2025-07-07",
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
            "name": "Atmospheric science and weather",
            "updateDate": "2025-09-15T15:31:33Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-09-15T15:50:13Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-09-15T15:41:20Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-09-15T15:42:06Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-09-15T15:37:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-11T17:17:11Z"
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
      "date": "2025-07-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4302ih.xml"
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
      "title": "Improving Atmospheric River Forecasts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Atmospheric River Forecasts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To accelerate subseasonal to seasonal prediction skills related to precipitation forecasts for water management in the western United States, improve atmospheric river forecasts across the country, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:33:34Z"
    }
  ]
}
```
