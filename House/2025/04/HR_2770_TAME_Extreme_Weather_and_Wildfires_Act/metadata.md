# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2770?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2770
- Title: TAME Extreme Weather and Wildfires Act
- Congress: 119
- Bill type: HR
- Bill number: 2770
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2026-02-04T05:06:15Z
- Update date including text: 2026-02-04T05:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2770",
    "number": "2770",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000472",
        "district": "18",
        "firstName": "Scott",
        "fullName": "Rep. Franklin, Scott [R-FL-18]",
        "lastName": "Franklin",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TAME Extreme Weather and Wildfires Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:15Z",
    "updateDateIncludingText": "2026-02-04T05:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:02:40Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2770ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2770\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Scott Franklin of Florida introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo direct the use of artificial intelligence by National Oceanic and Atmospheric Administration to adapt to extreme weather, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Transformational Artificial intelligence to Modernize the Economy against Extreme Weather and Wildfires Act or the TAME Extreme Weather and Wildfires Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Definitions.\nSec.\u20023.\u2002Earth system forecasting and information delivery.\nSec.\u20024.\u2002Advanced artificial intelligence applications for weather and information delivery.\nSec.\u20025.\u2002Technical assistance on use of artificial intelligence weather models.\nSec.\u20026.\u2002Fire environment modeling program.\nSec.\u20027.\u2002Partnerships for transformational innovation.\nSec.\u20028.\u2002Federal Government workforce expertise.\nSec.\u20029.\u2002Data access.\n#### 2. Definitions\nIn this Act:\n**(1) Artificial intelligence**\n**(A) In general**\nThe term artificial intelligence means a machine-based system that can, for a given set of human-defined objectives, make predictions, recommendations, or decisions influencing real or virtual environments, including by using machine-based and human-based inputs\u2014\n**(i)**\nto abstract such objectives into models through analysis in an automated manner; and\n**(ii)**\nto use model inferences to generate information or formulate options for action.\n**(B) Inclusions**\nThe term artificial intelligence includes machine learning, neural networks, and natural language processing.\n**(2) Artificial intelligence weather model**\nThe term artificial intelligence weather model means a weather model based primarily on artificial intelligence to project future Earth system conditions based on machine learning from an Earth system reanalysis dataset.\n**(3) Curate**\nThe term curate means to collect, maintain, and update periodically a dataset\u2014\n**(A)**\nto ensure and document its quality; and\n**(B)**\nto provide metadata on its provenance.\n**(4) Numerical weather model**\nThe term numerical weather model means a weather model based primarily on coupled Earth system processes and that uses numerical computation to forecast future Earth system conditions.\n**(5) Observational data**\nThe term observational data means data from actual observations of environmental conditions, including remote sensing and in situ platforms.\n**(6) Open license**\nThe term open license has the meaning given that term in section 3502(21) of title 44, United States Code.\n**(7) Reforecast analysis**\nThe term reforecast analysis means the assessment of a numerical weather model or artificial intelligence weather model by comparing model output and observational data over a period of time in the past.\n**(8) Synthetic data**\nThe term synthetic data means data produced from a model or statistical method in order to fill gaps in observational data.\n**(9) Training dataset**\nThe term training dataset means a dataset used to train an artificial intelligence model.\n**(10) Under Secretary**\nThe term Under Secretary means the Under Secretary of Commerce for Oceans and Atmosphere.\n**(11) Weather enterprise**\nThe term weather enterprise has the meaning given such term in section 2 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 ).\n#### 3. Earth system forecasting and information delivery\n##### (a) In general\nNot later than two years after the date of the enactment of this Act, the Under Secretary, in consultation with the Secretary of Energy, the Administrator of the National Aeronautics and Space Administration, the Director of the National Science Foundation, any appropriate Federal Advisory Committee, and such other technical experts as the Under Secretary considers appropriate, shall develop and curate comprehensive weather forecasting training datasets with relevant Earth system data, quality information, and metadata necessary for weather forecasting dataset that develops a long-term record of past weather in support of the following:\n**(1)**\nFurthering the understanding of weather, water, and space weather modeling and data.\n**(2)**\nAdvancing the science of weather forecasting, including seasonal and subseasonal forecasting.\n**(3)**\nDeveloping artificial intelligence weather forecasting applications.\n##### (b) Use of existing datasets\nIn order to speed the development of the weather forecasting training dataset required under subsection (a), the Under Secretary shall assess, and to the greatest extent practicable build on, existing weather forecasting training datasets of the Federal Government.\n##### (c) Artificial intelligence weather model\n**(1) In general**\nIn carrying out this section, the Under Secretary, in consultation with any appropriate Federal Advisory Committees, may develop and test a global weather model based on artificial intelligence, to be referred to as an artificial intelligence weather model .\n**(2) Weather ready nation**\nIn coordination with the activities carried out under paragraph (1), the Under Secretary may explore using artificial intelligence to enhance the dissemination of information and evaluation of effectiveness for improved public understanding, preparedness, and resilience.\n**(3) Reports**\nNot later than two years after the date of the enactment of this Act and not less frequently than annually thereafter, the Under Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report on the activities conducted under paragraph (1).\n##### (d) Cooperative institutes and contracting authority\nIn carrying out this section, subject to the availability of appropriations, the Under Secretary may competitively award contracts and funding opportunities, increase the scope of existing cooperative institutes of the National Oceanic and Atmospheric Administration, or competitively award a new cooperative institute.\n##### (e) Environmental impact\nThe Under Secretary shall develop and disseminate best practices to minimize environmental impacts from the use of artificial intelligence to carry out this section.\n##### (f) Continued support for observations, basic research, and numerical weather models\nNotwithstanding the requirements of this section, the Under Secretary shall continue to support and advance the activities of the National Oceanic and Atmospheric Administration carry out the following:\n**(1)**\nCollect and acquire traditional and novel observational data relevant for artificial intelligence and numerical weather models.\n**(2)**\nAdvance research on the Earth system and numerical weather models.\n**(3)**\nDevelop and advance numerical Earth system modeling for predictions.\n**(4)**\nDevelop weather model data post-processing techniques.\n**(5)**\nImprove data assimilation techniques.\n#### 4. Advanced artificial intelligence applications for weather and information delivery\nThe Under Secretary shall explore advanced applications of artificial intelligence to improve weather forecasts and information delivery, such as by carrying out the following:\n**(1)**\nImproving data assimilation techniques.\n**(2)**\nUsing artificial intelligence weather models to quickly emulate running numerical weather models to assess and improve the confidence in and reliability of weather forecasts and information delivery.\n**(3)**\nImproving impact-based decision support to communities for greater societal benefits based on weather forecasts.\n#### 5. Technical assistance on use of artificial intelligence weather models\n##### (a) In general\nThe Under Secretary shall regularly inventory and assess major non-Federal Government artificial intelligence weather models in order to provide the following:\n**(1)**\nTechnical evaluation and assistance on using such models.\n**(2)**\nBest practices on providing forecasts based on outputs from both artificial intelligence weather models and numerical weather models, or a combination thereof.\n**(3)**\nSupport for forecasters and social scientists to test and evaluate the use and effectiveness of artificial intelligence models, including within National Oceanic and Atmospheric Administration testbeds.\n**(4)**\nSupport for emergency managers to make operational decisions based on outputs from both artificial intelligence weather models and numerical weather models, or a combination thereof.\n##### (b) Reforecast analysis\n**(1) In general**\nThe Under Secretary shall support the development of a common framework for the assessment of numerical weather models and artificial intelligence weather models through reforecast analysis and related methodologies as the Under Secretary considers appropriate.\n**(2) Best practices**\nIn carrying out this subsection, the Under Secretary may develop and disseminate best practices in collaboration with the following:\n**(A)**\nThe National Institute for Standards and Technology.\n**(B)**\nThe National Aeronautics and Space Administration.\n**(C)**\nThe National Science Foundation.\n**(D)**\nThe Department of Energy.\n**(E)**\nAcademic and research institutions.\n**(F)**\nThe private sector.\n**(3) Report on use of analysis to improve models**\nNot later than one year after the date of the enactment of this Act, the Under Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report on the feasibility of using reforecast analysis techniques to improve seasonal and subseasonal models.\n##### (c) Weather forecast offices\nIn carrying out this section, the Under Secretary shall provide technical assistance, best practices, and support required under subsection (a) through weather forecast offices of the National Oceanic and Atmospheric Administration.\n##### (d) Independent study on the impacts of artificial intelligence weather, water, and space weather models\nThe Under Secretary may enter into an agreement with the National Academy of Sciences or any other entity determined appropriate by the Under Secretary to assess the impacts of artificial intelligence weather models on the weather enterprise and make recommendations to improve the integration of such models in operational forecasting.\n#### 6. Fire environment modeling program\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Under Secretary, in coordination with the Secretary of the Interior, the Secretary of Agriculture, and the Secretary of Homeland Security, and in consultation with the Administrator of the National Aeronautics and Space Administration, the Secretary of Energy, the Director of the National Science Foundation, any appropriate Federal advisory committees, and such other technical experts as the Under Secretary considers appropriate, shall develop a program to use artificial intelligence to analyze available observational data and synthetic data on the built and natural environments in order to carry out the following:\n**(1)**\nWarn at-risk communities, firefighters, and other responders, including by integrating social science informed research and development.\n**(2)**\nPredict and detect wildfires to the maximum extent practicable.\n**(3)**\nForecast wildland and built environment fire propagation and potential impacts based on an analysis of the elements influencing fire behavior, weather conditions, terrain, and observations of the fire environment.\n**(4)**\nDetect, monitor, and forecast smoke and other hazards associated with wildfires.\n##### (b) Training dataset\nIn carrying out this section, the Under Secretary may acquire observational data and synthetic data on the built and natural environments collected across the United States to develop and curate a related artificial intelligence-ready training dataset for purposes of training the artificial intelligence used in furtherance of this section.\n##### (c) Data acquisition\nIn carrying out this section, the Under Secretary may enter into contracts to acquire relevant data referred to in this section.\n##### (d) Weather integration\nIn carrying out this section, the Under Secretary shall integrate outputs from weather and other environmental models and observational data and synthetic data referred to in subsection (a).\n##### (e) Environmental impact\nThe Under Secretary shall develop and disseminate best practices to minimize environmental impacts from the use of artificial intelligence to carry out this section.\n#### 7. Partnerships for transformational innovation\n##### (a) In general\nThe Under Secretary shall explore novel structures for partnerships with private entities and academic entities for transformative innovation in weather forecasting and other environmental forecasts in order to carry out the following:\n**(1)**\nFurther the understanding of weather, water, wildfires, and space weather, and associated societal impact.\n**(2)**\nAdvance the science of weather and water forecasting, including seasonal and subseasonal forecasting.\n**(3)**\nDevelop, evaluate, and transition artificial intelligence weather, water, and hazard forecasting applications for operations.\n##### (b) Co-Investment\nIn carrying out this section, subject to applicable law, the Under Secretary shall consider and adopt novel co-investment strategies with the private sector and academic sector, including the following:\n**(1)**\nNon-Federal Government contributions to resource and support high-risk, high-return research and development in environmental forecasting, data science, artificial intelligence, and related fields.\n**(2)**\nShared rights to intellectual property from research and development activities under this section.\n**(3)**\nOther approaches to sharing resources and results under this section.\n#### 8. Federal Government workforce expertise\n##### (a) In general\nThe Under Secretary, to the maximum extent practicable, shall develop, recruit, and sustain a professional workforce for weather forecasting applications of artificial intelligence.\n##### (b) Collaboration\nThe Under Secretary shall leverage robust public-private partnership models to collaborate with private sector experts and provide employees with access to training, experience, and long-term development of workforce and infrastructure in order to utilize artificial intelligence to improve weather forecasts.\n#### 9. Data access\n##### (a) In general\nThe Under Secretary may make available to the public, as the Under Secretary determines appropriate, at no cost and with no restrictions on copying, publishing, distributing, citing, adapting, or otherwise using under an open license, any data or code developed under this Act.\n##### (b) Accommodations\nThe Under Secretary may make such accommodations as the Under Secretary considers appropriate to ensure that the public release of any model, information, documentation, or data pursuant to this Act does not jeopardize any of the following:\n**(1)**\nNational security.\n**(2)**\nIntellectual property or redistribution rights, including under titles 17 and 35, United States Code.\n**(3)**\nAny trade secret or commercial or financial information subject to section 552(b)(4) of title 5, United States Code.\n**(4)**\nAny models or data that are otherwise restricted by contract or other written agreement.\n**(5)**\nThe mission of the National Oceanic and Atmospheric Administration to protect lives and property.\n##### (c) Rule of construction\nNothing in this Act may be construed to supersede any other provision of law governing the protection of the national security interests of the United States.",
      "versionDate": "2025-04-09",
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
        "updateDate": "2025-05-19T15:56:50Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2770ih.xml"
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
      "title": "TAME Extreme Weather and Wildfires Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TAME Extreme Weather and Wildfires Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transformational Artificial intelligence to Modernize the Economy against Extreme Weather and Wildfires Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the use of artificial intelligence by National Oceanic and Atmospheric Administration to adapt to extreme weather, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T03:48:25Z"
    }
  ]
}
```
