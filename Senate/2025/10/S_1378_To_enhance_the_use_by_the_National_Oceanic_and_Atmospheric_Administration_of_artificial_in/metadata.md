# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1378?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1378
- Title: TAME Extreme Weather and Wildfires Act
- Congress: 119
- Bill type: S
- Bill number: 1378
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-02-04T05:06:15Z
- Update date including text: 2026-02-04T05:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-88.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-88.
- 2025-10-21 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 199.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-88.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-88.
- 2025-10-21 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 199.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1378",
    "number": "1378",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001194",
        "district": "",
        "firstName": "Brian",
        "fullName": "Sen. Schatz, Brian [D-HI]",
        "lastName": "Schatz",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "TAME Extreme Weather and Wildfires Act",
    "type": "S",
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
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 199.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-88.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-88.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-09",
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
        "item": [
          {
            "date": "2025-10-21T21:00:04Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-30T14:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-09T17:32:57Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sponsorshipDate": "2025-04-09",
      "state": "MT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NM"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1378is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1378\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Schatz (for himself, Mr. Sheehy , Mr. Luj\u00e1n , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo enhance the use by the National Oceanic and Atmospheric Administration of artificial intelligence for weather forecasting, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transformational Artificial intelligence to Modernize the Economy against Extreme Weather and Wildfires Act or the TAME Extreme Weather and Wildfires Act .\n#### 2. Artificial intelligence for weather forecasting\n##### (a) Definitions\nIn this section:\n**(1) Artificial intelligence**\nThe term artificial intelligence \u2014\n**(A)**\nhas the meaning given that term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ); and\n**(B)**\nincludes machine learning, neural networks, and natural language processing.\n**(2) Artificial intelligence weather model**\nThe term artificial intelligence weather model means a weather model based primarily on artificial intelligence technology to project future Earth system conditions based on machine learning using weather forecasting training datasets.\n**(3) Curate**\nThe term curate , with respect to a dataset, means\u2014\n**(A)**\nto collect and maintain the dataset\u2014\n**(i)**\nto ensure and document its quality; and\n**(ii)**\nto provide metadata on its provenance; and\n**(B)**\nto update the dataset periodically, as appropriate and practicable.\n**(4) Numerical weather model**\nThe term numerical weather model means a weather model based primarily on coupled Earth System processes that uses numerical computation to forecast future Earth system conditions.\n**(5) Observational data**\nThe term observational data means data and metadata from actual observations of environmental conditions, including remote sensing and in situ platforms.\n**(6) Seasonal, subseasonal, Under Secretary, weather enterprise**\nthe terms seasonal , subseasonal , Under Secretary , and weather enterprise have the meanings given those terms in section 2 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 ).\n**(7) Synthetic data**\nThe term synthetic data means data produced from a model or statistical method in order to fill gaps in observational data.\n**(8) Weather data**\nThe term weather data means information used to track and predict weather conditions and patterns, including forecasts, observations, and derivative products from such information.\n##### (b) Purpose\nThe purpose of this section is\u2014\n**(1)**\nto improve accuracy and timeliness of weather, water, and space weather forecasts and effective dissemination of critical information;\n**(2)**\nto strengthen analytic capacity to inform resource deployments in response to and to mitigate harm from weather, water, wildfires, and space weather hazards through the mandated exploration and use of artificial intelligence by Federal agencies;\n**(3)**\nto strengthen public-private partnerships to accelerate adoption and outcomes of the use of artificial intelligence in response to and to mitigate such harm; and\n**(4)**\nto strengthen public-private partnerships in highly technical, high-risk, and high-reward fields related to weather, water, wildfires, and space weather forecasts.\n##### (c) Earth system forecasting and information delivery\n**(1) Training datasets**\nNot later than 4 years after the date of the enactment of this Act, the Under Secretary, in consultation with the Secretary of Energy, the Administrator of the National Aeronautics and Space Administration, the Director of the National Science Foundation, the Director of the National Center for Atmospheric Research, the Interagency Council on Advancing Meteorological Services, other appropriate Federal advisory committees as determined by the Under Secretary, and such other technical experts as the Under Secretary considers appropriate, shall develop and curate comprehensive weather forecasting training datasets with relevant Earth system data, quality information, and metadata necessary for weather forecasting.\n**(2) Use of existing datasets**\nIn order to speed the development of the weather forecasting training datasets required under paragraph (1), the Under Secretary shall assess, and to the greatest extent practicable build on, existing Earth system reanalysis datasets of the Federal Government.\n**(3) Artificial intelligence weather model**\n**(A) Global model**\nIn carrying out this subsection, the Under Secretary, in consultation with appropriate Federal advisory committees as determined by the Under Secretary, may develop and test a global weather model based on artificial intelligence technologies utilizing data of the National Oceanic and Atmospheric Administration to the extent possible.\n**(B) Regional and local models**\nIn addition to a global weather model under subparagraph (A), the Under Secretary may experiment with regional and local weather models based on artificial intelligence technologies.\n**(4) Use of artificial intelligence to disseminate information**\nIn coordination with an artificial intelligence weather model or models developed under paragraph (3), the Under Secretary may explore the use of artificial intelligence to enhance the dissemination of information with respect to weather and wildfire risks and evaluate the effectiveness of communication for improved public understanding and preparedness.\n**(5) Continued support for observations, basic research, and numerical weather models**\nNotwithstanding the requirements of this subsection, the Under Secretary shall continue to support and advance the activities of the National Oceanic and Atmospheric Administration\u2014\n**(A)**\nto collect and acquire traditional and novel observational data relevant for artificial intelligence and numerical weather, water, and space weather forecasting;\n**(B)**\nto advance research on the Earth system and numerical weather model forecasting;\n**(C)**\nto develop and advance numerical Earth system modeling for predictions;\n**(D)**\nto develop weather model data post-processing techniques; and\n**(E)**\nto improve data assimilation techniques.\n**(6) Observing system coverage**\nIn carrying out this subsection, the Under Secretary may evaluate the use of cost functions in data-driven machine learning model training to balance inequities in observing system coverage and data poor areas.\n**(7) Uncertainty quantification research**\nIn carrying out this subsection, the Under Secretary may develop uncertainty quantification research for the purpose of accurate environmental risk and hazard communications of probabilistic predictions and forecasts.\n**(8) Report**\nNot later than 2 years after the date of the enactment of this Act, and not less frequently than every 2 years thereafter through 2035, the Under Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report on the activities conducted under this subsection.\n##### (d) Advanced artificial intelligence applications for weather forecasts and information delivery\nThe Under Secretary shall explore advanced applications of artificial intelligence to improve weather forecasts and information delivery, such as by\u2014\n**(1)**\nimproving data assimilation;\n**(2)**\naccounting for coupled Earth system processes;\n**(3)**\nimproving readiness and preparedness to combat wildfires, mitigation of the risk from wildfires, and improving safety for firefighters and communities at risk from wildfires;\n**(4)**\nusing artificial intelligence weather models to generate ensemble forecasts to more accurately assess flow-dependent forecast uncertainties; and\n**(5)**\nimproving impact-based decision support to diverse users and communities for greater societal benefits based on those forecasts.\n##### (e) Technical assistance on use of artificial intelligence weather, water, and space weather models\n**(1) In general**\nThe Under Secretary shall provide\u2014\n**(A)**\ntechnical assistance, data access, and support for forecasters, scientists, social scientists, and engineers to test and evaluate the use and effectiveness of the artificial intelligence models of the National Oceanic and Atmospheric Administration, including within the testbeds of the Administration;\n**(B)**\nbest practices on providing forecasts based on outputs from artificial intelligence weather models and numerical weather models, or a combination thereof; and\n**(C)**\nsupport for emergency managers to make operational decisions based on outputs from artificial intelligence weather models and numerical weather models, or a combination thereof.\n**(2) Assessment of weather models**\n**(A) In general**\nThe Under Secretary shall support the development of a common framework for the assessment of numerical weather models and artificial intelligence weather models by comparing model output and observational data over a period of time in the past through the use of such methodologies as the Under Secretary considers appropriate.\n**(B) Best practices**\nIn carrying out this paragraph, the Under Secretary may develop and disseminate best practices in collaboration with\u2014\n**(i)**\nthe National Institute of Standards and Technology, the National Aeronautics and Space Administration, the National Science Foundation, and the Department of Energy;\n**(ii)**\nacademic and research institutions; and\n**(iii)**\nthe private sector.\n**(3) Technical assistance**\nIn carrying out this subsection, the Under Secretary may provide technical assistance, best practices, and support required under paragraph (1) through the National Weather Service.\n**(4) Independent study on the impacts of artificial intelligence weather, water, and space weather models**\nThe Under Secretary may enter into an agreement with the National Academy of Sciences or another entity as determined appropriate by the Under Secretary to assess the impacts of artificial intelligence weather models on the weather enterprise and make recommendations to improve the integration of such models in operational forecasting.\n##### (f) Partnerships for transformational innovation\n**(1) In general**\nThe Under Secretary may explore novel structures for partnerships with private, academic, and international entities for research and development of transformative innovation in weather forecasting and other environmental forecasts\u2014\n**(A)**\nto further the understanding of weather, water, wildfires, and space weather, and their societal impact;\n**(B)**\nto advance the science of weather and water forecasting, including seasonal and subseasonal forecasting; and\n**(C)**\nto develop, evaluate, and transition artificial intelligence weather, water, and hazard forecasting applications to operations.\n**(2) Co-investment**\nSubject to applicable law, the Under Secretary may consider and adopt novel co-investment strategies with the private academic and international sectors to carry out paragraph (1), including\u2014\n**(A)**\nnon-Federal Government contributions to resource and support high-risk, high-return research and development in environmental forecasting, data science, artificial intelligence, and related fields;\n**(B)**\nshared rights to intellectual property from research and development activities under this subsection; and\n**(C)**\nother approaches to sharing resources and results under this subsection.\n##### (g) Availability of dataset\n**(1) In general**\nThe Under Secretary shall develop and implement a plan to make available to the public, at no cost and subject to applicable law and policy, the following:\n**(A)**\nOperational artificial intelligence weather models developed by the National Oceanic and Atmospheric Administration.\n**(B)**\nArtificial intelligence weather models that are not operational models, including experimental and developmental models, as the Under Secretary determines appropriate.\n**(C)**\nApplicable information and documentation for artificial intelligence weather models described in subparagraphs (A) and (B), including a description of intended model outputs.\n**(D)**\nSubject to subsection (i), all data owned by the Federal Government and data that the Under Secretary has the legal right to redistribute that are associated with artificial intelligence weather models made available to the public pursuant to the plan and used in operational forecasting by the Administration, including\u2014\n**(i)**\nrelevant metadata; and\n**(ii)**\ndata used for operational artificial intelligence weather models used by the Administration.\n**(2) Accommodations**\nIn developing and implementing the plan under paragraph (1), the Under Secretary may make such accommodations as the Under Secretary considers appropriate to ensure that the public release of any artificial intelligence weather model, information, documentation, or data pursuant to the plan does not jeopardize\u2014\n**(A)**\nnational security;\n**(B)**\nintellectual property or redistribution rights, including under titles 17 and 35, United States Code;\n**(C)**\nany trade secret or commercial or financial information subject to section 552(b)(4) of title 5, United States Code;\n**(D)**\nany models or data that are otherwise restricted by contract or other written agreement; or\n**(E)**\nthe mission of the Administration to protect lives and property.\n**(3) Report**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act, the Under Secretary shall submit to Congress a report, in both unclassified and classified form, regarding the risks to the economic and intellectual security of the United States from foreign countries of concern through access by those countries to weather data in the United States.\n**(B) Elements**\nThe report required under subparagraph (A) shall include\u2014\n**(i)**\na full analysis of the national, intellectual, and economic security implications for the United States with respect to intellectual property theft or cyber or human espionage through access to weather data; and\n**(ii)**\nconclusions of the Under Secretary and recommendations for legislative and administrative action, if any.\n**(C) Foreign country of concern defined**\nIn this paragraph, the term foreign country of concern has the meaning given that term in section 9901 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 ).\n##### (h) Retention of federal government expertise\nSubject to applicable law, the Under Secretary may consider novel methods to recruit, retrain, and retain expert personnel to support activities under this section, including by\u2014\n**(1)**\nusing methods to be competitive with salaries outside the Federal Government;\n**(2)**\ndeveloping staff exchange programs and training programs; and\n**(3)**\nleveraging diverse hiring strategies.\n##### (i) Protection of national security interests\n**(1) In general**\nNotwithstanding any other provision of this section, the Under Secretary, in consultation with the Secretary of Defense, as appropriate, may withhold models or data used under this section if the Under Secretary determines doing so to be necessary to protect the national security interests of the United States.\n**(2) Rule of construction**\nNothing in this section shall be construed to supersede any other provision of law governing the protection of the national security interests of the United States.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to the Under Secretary to carry out this section\u2014\n**(1)**\nfor fiscal year 2026, $311,000,000; and\n**(2)**\nfor each of fiscal years 2027 through 2030, $76,000,000.",
      "versionDate": "2025-04-09",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1378rs.xml",
      "text": "II\nCalendar No. 199\n119th CONGRESS\n1st Session\nS. 1378\n[Report No. 119\u201388]\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Schatz (for himself, Mr. Sheehy , Mr. Luj\u00e1n , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nOctober 21, 2025 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo enhance the use by the National Oceanic and Atmospheric Administration of artificial intelligence for weather forecasting, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transformational Artificial intelligence to Modernize the Economy against Extreme Weather and Wildfires Act or the TAME Extreme Weather and Wildfires Act .\n#### 2. Artificial intelligence for weather forecasting\n##### (a) Definitions\nIn this section:\n**(1) Artificial intelligence**\nThe term artificial intelligence \u2014\n**(A)**\nhas the meaning given that term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ); and\n**(B)**\nincludes machine learning, neural networks, and natural language processing.\n**(2) Artificial intelligence weather model**\nThe term artificial intelligence weather model means a weather model based primarily on artificial intelligence technology to project future Earth system conditions based on machine learning using weather forecasting training datasets.\n**(3) Curate**\nThe term curate , with respect to a dataset, means\u2014\n**(A)**\nto collect and maintain the dataset\u2014\n**(i)**\nto ensure and document its quality; and\n**(ii)**\nto provide metadata on its provenance; and\n**(B)**\nto update the dataset periodically, as appropriate and practicable.\n**(4) Numerical weather model**\nThe term numerical weather model means a weather model based primarily on coupled Earth System processes that uses numerical computation to forecast future Earth system conditions.\n**(5) Observational data**\nThe term observational data means data and metadata from actual observations of environmental conditions, including remote sensing and in situ platforms.\n**(6) Seasonal, subseasonal, Under Secretary, weather enterprise**\nthe terms seasonal , subseasonal , Under Secretary , and weather enterprise have the meanings given those terms in section 2 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 ).\n**(7) Synthetic data**\nThe term synthetic data means data produced from a model or statistical method in order to fill gaps in observational data.\n**(8) Weather data**\nThe term weather data means information used to track and predict weather conditions and patterns, including forecasts, observations, and derivative products from such information.\n##### (b) Purpose\nThe purpose of this section is\u2014\n**(1)**\nto improve accuracy and timeliness of weather, water, and space weather forecasts and effective dissemination of critical information;\n**(2)**\nto strengthen analytic capacity to inform resource deployments in response to and to mitigate harm from weather, water, wildfires, and space weather hazards through the mandated exploration and use of artificial intelligence by Federal agencies;\n**(3)**\nto strengthen public-private partnerships to accelerate adoption and outcomes of the use of artificial intelligence in response to and to mitigate such harm; and\n**(4)**\nto strengthen public-private partnerships in highly technical, high-risk, and high-reward fields related to weather, water, wildfires, and space weather forecasts.\n##### (c) Earth system forecasting and information delivery\n**(1) Training datasets**\nNot later than 4 years after the date of the enactment of this Act, the Under Secretary, in consultation with the Secretary of Energy, the Administrator of the National Aeronautics and Space Administration, the Director of the National Science Foundation, the Director of the National Center for Atmospheric Research, the Interagency Council on Advancing Meteorological Services, other appropriate Federal advisory committees as determined by the Under Secretary, and such other technical experts as the Under Secretary considers appropriate, shall develop and curate comprehensive weather forecasting training datasets with relevant Earth system data, quality information, and metadata necessary for weather forecasting.\n**(2) Use of existing datasets**\nIn order to speed the development of the weather forecasting training datasets required under paragraph (1), the Under Secretary shall assess, and to the greatest extent practicable build on, existing Earth system reanalysis datasets of the Federal Government.\n**(3) Artificial intelligence weather model**\n**(A) Global model**\nIn carrying out this subsection, the Under Secretary, in consultation with appropriate Federal advisory committees as determined by the Under Secretary, may develop and test a global weather model based on artificial intelligence technologies utilizing data of the National Oceanic and Atmospheric Administration to the extent possible.\n**(B) Regional and local models**\nIn addition to a global weather model under subparagraph (A), the Under Secretary may experiment with regional and local weather models based on artificial intelligence technologies.\n**(4) Use of artificial intelligence to disseminate information**\nIn coordination with an artificial intelligence weather model or models developed under paragraph (3), the Under Secretary may explore the use of artificial intelligence to enhance the dissemination of information with respect to weather and wildfire risks and evaluate the effectiveness of communication for improved public understanding and preparedness.\n**(5) Continued support for observations, basic research, and numerical weather models**\nNotwithstanding the requirements of this subsection, the Under Secretary shall continue to support and advance the activities of the National Oceanic and Atmospheric Administration\u2014\n**(A)**\nto collect and acquire traditional and novel observational data relevant for artificial intelligence and numerical weather, water, and space weather forecasting;\n**(B)**\nto advance research on the Earth system and numerical weather model forecasting;\n**(C)**\nto develop and advance numerical Earth system modeling for predictions;\n**(D)**\nto develop weather model data post-processing techniques; and\n**(E)**\nto improve data assimilation techniques.\n**(6) Observing system coverage**\nIn carrying out this subsection, the Under Secretary may evaluate the use of cost functions in data-driven machine learning model training to balance inequities in observing system coverage and data poor areas.\n**(7) Uncertainty quantification research**\nIn carrying out this subsection, the Under Secretary may develop uncertainty quantification research for the purpose of accurate environmental risk and hazard communications of probabilistic predictions and forecasts.\n**(8) Report**\nNot later than 2 years after the date of the enactment of this Act, and not less frequently than every 2 years thereafter through 2035, the Under Secretary shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report on the activities conducted under this subsection.\n##### (d) Advanced artificial intelligence applications for weather forecasts and information delivery\nThe Under Secretary shall explore advanced applications of artificial intelligence to improve weather forecasts and information delivery, such as by\u2014\n**(1)**\nimproving data assimilation;\n**(2)**\naccounting for coupled Earth system processes;\n**(3)**\nimproving readiness and preparedness to combat wildfires, mitigation of the risk from wildfires, and improving safety for firefighters and communities at risk from wildfires;\n**(4)**\nusing artificial intelligence weather models to generate ensemble forecasts to more accurately assess flow-dependent forecast uncertainties; and\n**(5)**\nimproving impact-based decision support to diverse users and communities for greater societal benefits based on those forecasts.\n##### (e) Technical assistance on use of artificial intelligence weather, water, and space weather models\n**(1) In general**\nThe Under Secretary shall provide\u2014\n**(A)**\ntechnical assistance, data access, and support for forecasters, scientists, social scientists, and engineers to test and evaluate the use and effectiveness of the artificial intelligence models of the National Oceanic and Atmospheric Administration, including within the testbeds of the Administration;\n**(B)**\nbest practices on providing forecasts based on outputs from artificial intelligence weather models and numerical weather models, or a combination thereof; and\n**(C)**\nsupport for emergency managers to make operational decisions based on outputs from artificial intelligence weather models and numerical weather models, or a combination thereof.\n**(2) Assessment of weather models**\n**(A) In general**\nThe Under Secretary shall support the development of a common framework for the assessment of numerical weather models and artificial intelligence weather models by comparing model output and observational data over a period of time in the past through the use of such methodologies as the Under Secretary considers appropriate.\n**(B) Best practices**\nIn carrying out this paragraph, the Under Secretary may develop and disseminate best practices in collaboration with\u2014\n**(i)**\nthe National Institute of Standards and Technology, the National Aeronautics and Space Administration, the National Science Foundation, and the Department of Energy;\n**(ii)**\nacademic and research institutions; and\n**(iii)**\nthe private sector.\n**(3) Technical assistance**\nIn carrying out this subsection, the Under Secretary may provide technical assistance, best practices, and support required under paragraph (1) through the National Weather Service.\n**(4) Independent study on the impacts of artificial intelligence weather, water, and space weather models**\nThe Under Secretary may enter into an agreement with the National Academy of Sciences or another entity as determined appropriate by the Under Secretary to assess the impacts of artificial intelligence weather models on the weather enterprise and make recommendations to improve the integration of such models in operational forecasting.\n##### (f) Partnerships for transformational innovation\n**(1) In general**\nThe Under Secretary may explore novel structures for partnerships with private, academic, and international entities for research and development of transformative innovation in weather forecasting and other environmental forecasts\u2014\n**(A)**\nto further the understanding of weather, water, wildfires, and space weather, and their societal impact;\n**(B)**\nto advance the science of weather and water forecasting, including seasonal and subseasonal forecasting; and\n**(C)**\nto develop, evaluate, and transition artificial intelligence weather, water, and hazard forecasting applications to operations.\n**(2) Co-investment**\nSubject to applicable law, the Under Secretary may consider and adopt novel co-investment strategies with the private academic and international sectors to carry out paragraph (1), including\u2014\n**(A)**\nnon-Federal Government contributions to resource and support high-risk, high-return research and development in environmental forecasting, data science, artificial intelligence, and related fields;\n**(B)**\nshared rights to intellectual property from research and development activities under this subsection; and\n**(C)**\nother approaches to sharing resources and results under this subsection.\n##### (g) Availability of dataset\n**(1) In general**\nThe Under Secretary shall develop and implement a plan to make available to the public, at no cost and subject to applicable law and policy, the following:\n**(A)**\nOperational artificial intelligence weather models developed by the National Oceanic and Atmospheric Administration.\n**(B)**\nArtificial intelligence weather models that are not operational models, including experimental and developmental models, as the Under Secretary determines appropriate.\n**(C)**\nApplicable information and documentation for artificial intelligence weather models described in subparagraphs (A) and (B), including a description of intended model outputs.\n**(D)**\nSubject to subsection (i), all data owned by the Federal Government and data that the Under Secretary has the legal right to redistribute that are associated with artificial intelligence weather models made available to the public pursuant to the plan and used in operational forecasting by the Administration, including\u2014\n**(i)**\nrelevant metadata; and\n**(ii)**\ndata used for operational artificial intelligence weather models used by the Administration.\n**(2) Accommodations**\nIn developing and implementing the plan under paragraph (1), the Under Secretary may make such accommodations as the Under Secretary considers appropriate to ensure that the public release of any artificial intelligence weather model, information, documentation, or data pursuant to the plan does not jeopardize\u2014\n**(A)**\nnational security;\n**(B)**\nintellectual property or redistribution rights, including under titles 17 and 35, United States Code;\n**(C)**\nany trade secret or commercial or financial information subject to section 552(b)(4) of title 5, United States Code;\n**(D)**\nany models or data that are otherwise restricted by contract or other written agreement; or\n**(E)**\nthe mission of the Administration to protect lives and property.\n**(3) Report**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act, the Under Secretary shall submit to Congress a report, in both unclassified and classified form, regarding the risks to the economic and intellectual security of the United States from foreign countries of concern through access by those countries to weather data in the United States.\n**(B) Elements**\nThe report required under subparagraph (A) shall include\u2014\n**(i)**\na full analysis of the national, intellectual, and economic security implications for the United States with respect to intellectual property theft or cyber or human espionage through access to weather data; and\n**(ii)**\nconclusions of the Under Secretary and recommendations for legislative and administrative action, if any.\n**(C) Foreign country of concern defined**\nIn this paragraph, the term foreign country of concern has the meaning given that term in section 9901 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 ).\n##### (h) Retention of federal government expertise\nSubject to applicable law, the Under Secretary may consider novel methods to recruit, retrain, and retain expert personnel to support activities under this section, including by\u2014\n**(1)**\nusing methods to be competitive with salaries outside the Federal Government;\n**(2)**\ndeveloping staff exchange programs and training programs; and\n**(3)**\nleveraging diverse hiring strategies.\n##### (i) Protection of national security interests\n**(1) In general**\nNotwithstanding any other provision of this section, the Under Secretary, in consultation with the Secretary of Defense, as appropriate, may withhold models or data used under this section if the Under Secretary determines doing so to be necessary to protect the national security interests of the United States.\n**(2) Rule of construction**\nNothing in this section shall be construed to supersede any other provision of law governing the protection of the national security interests of the United States.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to the Under Secretary to carry out this section\u2014\n**(1)**\nfor fiscal year 2026, $311,000,000; and\n**(2)**\nfor each of fiscal years 2027 through 2030, $76,000,000.",
      "versionDate": "2025-10-21",
      "versionType": "Reported in Senate"
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
            "updateDate": "2025-05-20T17:09:54Z"
          },
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2025-05-20T17:07:30Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-05-20T17:07:37Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-20T17:16:46Z"
          },
          {
            "name": "Floods and storm protection",
            "updateDate": "2025-05-20T17:14:54Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-20T17:15:35Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-20T17:16:33Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-05-20T17:15:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-19T16:01:44Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1378is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1378rs.xml"
        }
      ],
      "type": "Reported in Senate"
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
      "updateDate": "2025-10-23T11:18:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "TAME Extreme Weather and Wildfires Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Transformational Artificial intelligence to Modernize the Economy against Extreme Weather and Wildfires Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TAME Extreme Weather and Wildfires Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T02:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transformational Artificial intelligence to Modernize the Economy against Extreme Weather and Wildfires Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T02:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enhance the use by the National Oceanic and Atmospheric Administration of artificial intelligence for weather forecasting, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T02:33:19Z"
    }
  ]
}
```
