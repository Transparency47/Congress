# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3771?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3771
- Title: Protecting Coasts and Cities from Severe Weather Act
- Congress: 119
- Bill type: HR
- Bill number: 3771
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-10-11T08:05:20Z
- Update date including text: 2025-10-11T08:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3771",
    "number": "3771",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Protecting Coasts and Cities from Severe Weather Act",
    "type": "HR",
    "updateDate": "2025-10-11T08:05:20Z",
    "updateDateIncludingText": "2025-10-11T08:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:05:15Z",
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
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3771ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3771\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Kean introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo increase observations, understanding, and forecasting of coastal flooding and storm surge events, to address weather observation gaps in highly vulnerable areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Coasts and Cities from Severe Weather Act .\n#### 2. Coastal flooding and storm surge forecast improvement program\n##### (a) In general\nThe Under Secretary of Commerce for Oceans and Atmosphere (in this Act referred to as the Under Secretary ), in collaboration with the United States weather industry (as such term is defined in section 2 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 )) and academic partners, shall establish a coastal flooding and storm surge forecast improvement program (in this section refer to as the program ).\n##### (b) Goal\nThe goal of the program shall be to reduce the loss of life or property from coastal flooding, including high tide flooding, and storm surge events through the development and extension of accurate, effective, actionable, and probable forecasts and warnings.\n##### (c) Priority\nIn implementing the program, the Under Secretary shall prioritize activities that carry out the following:\n**(1)**\nImprove understanding and capacity for real-time operational prediction of the ocean\u2019s role in coastal flooding, including high tide flooding, and storm surge events.\n**(2)**\nImprove the capacity to mitigate, adapt to, or prevent the impacts of coastal flooding, including high tide flooding, and storm surge events, including by improving the understanding and capacity of coastal communities to perceive, comprehend, and respond to forecast information.\n**(3)**\nIncorporating data from in situ distributed sensors into predictive models and re-analyses.\n**(4)**\nDeveloping probabilistic coastal flooding, including high tide flooding, and storm surge estimates to complement worst-case scenario estimates, including for use in long-term planning and risk management by States, Tribal governments, localities, and emergency managers in coordination with the Federal Emergency Management Agency, as appropriate.\n**(5)**\nEstablishing skill metrics for coastal inundation forecasting that quantify the benefits of dynamical modeling, data assimilation, and machine learning improvements in the probabilistic forecast of coastal flooding, including high tide flooding, and storm surge risk and impacts.\n**(6)**\nImproving operational regional storm surge models and, in collaboration with the United States Geological Survey, wave prediction models to enhance probabilistic guidance and messaging.\n##### (d) Innovative observations and modeling\nThe Under Secretary shall ensure the program periodically examines, tests, and evaluates the value of incorporating enhanced model physics, hybrid dynamical or machine learning based prediction systems, and innovative observations, such as novel sensor technologies, observation networks, crewed or uncrewed systems, and hosted instruments on commercial aircrafts, vessels, and satellites, with respect to the improvement of coastal flooding, including high tide flooding, and storm surge forecasts, predictions, and warnings.\n##### (e) Program plan\nNot later than 180 days after the date of the enactment of this Act, the Under Secretary shall develop a plan that details the specific research, development, data acquisition, and technology transfer activities, as well as corresponding resources and timelines, necessary to achieve the goal of the program under subsection (b).\n##### (f) Annual budget for plan submission\nAfter the development of the plan pursuant to subsection (e), the Under Secretary shall, not less frequently than annually, submit to Congress a proposed budget corresponding with the activities identified in such plan.\n#### 3. Data voids in highly vulnerable areas of the United States\n##### (a) In general\nThe Under Secretary, in coordination with the Director of the National Weather Service and the Administrator of the Federal Emergency Management Agency, in consultation with the United States weather industry, academic partners, and in accordance with activities implemented through existing regional atmospheric, coastal, ocean, and Great Lakes observing systems, shall carry out activities to ensure equitable and comprehensive weather observation coverage, impact-based decision support services, and emergency information sharing in the United States, including the following:\n**(1)**\nIdentifying regions in the United States and the territories of the United States that are under-observed or highly vulnerable to weather impacts that threaten human life, health, and the economy.\n**(2)**\nIdentifying any challenges that contribute to the lack of operations under paragraph (1).\n**(3)**\nIncreasing weather observations and developing new weather observational capabilities, such as urban heat island mapping campaigns, with respect to the regions identified under paragraph (1).\n**(4)**\nEstablishing or supporting testbeds and deployments of decision-support services to Federal, State, and local emergency operations centers to develop and integrate new weather, water, and climate observation or emergency information sharing tools, with respect to the regions identified under paragraph (1).\n**(5)**\nTo the maximum extent practicable, advancing weather and water forecasting and climate modeling capabilities for the regions identified under paragraph (1).\n**(6)**\nUndertaking workforce development efforts for emergency management officials and meteorologists in the regions identified under paragraph (1).\n**(7)**\nUsing data-void-filling observations to better resolve extreme rainfall in complex topography.\n**(8)**\nContributing to a national integrated heat health information system.\n##### (b) Interagency partnership To support pilot projects\nIn carrying out this section, the Under Secretary, acting through the Director of the National Weather Service and the Administrator of the Federal Emergency Management Agency, shall establish an interagency partnership to support pilot projects that accelerate coordination and use of localized weather data in infrastructure and emergency management decisions by Federal, State, and local officials.\n##### (c) Priority\nAt least one pilot project under subsection (b) shall address key science challenges to using mesonet data in local decision making and development of new tools and training for owners and operators of critical infrastructure (as such term is defined in section 1016(e) of Public Law 107\u201356 ( 42 U.S.C. 5195c(e) )), such as dams, energy generation and distribution facilities, nuclear power plants, and transportation networks.",
      "versionDate": "2025-06-05",
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
        "updateDate": "2025-06-27T13:02:30Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3771ih.xml"
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
      "title": "Protecting Coasts and Cities from Severe Weather Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Coasts and Cities from Severe Weather Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase observations, understanding, and forecasting of coastal flooding and storm surge events, to address weather observation gaps in highly vulnerable areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:33:17Z"
    }
  ]
}
```
