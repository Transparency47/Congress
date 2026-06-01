# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3854?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3854
- Title: Advanced Weather Model Computing Development Act
- Congress: 119
- Bill type: S
- Bill number: 3854
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-03-02T19:53:34Z
- Update date including text: 2026-03-02T19:53:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3854",
    "number": "3854",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Advanced Weather Model Computing Development Act",
    "type": "S",
    "updateDate": "2026-03-02T19:53:34Z",
    "updateDateIncludingText": "2026-03-02T19:53:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T16:38:58Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3854is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3854\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Luj\u00e1n (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Secretary of Energy and the Administrator of the National Oceanic and Atmospheric Administration to conduct collaborative research to advance weather models in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advanced Weather Model Computing Development Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administration**\nThe term Administration means the National Oceanic and Atmospheric Administration.\n**(2) Administrator**\nThe term Administrator means the Administrator of the National Oceanic and Atmospheric Administration.\n**(3) Advanced computing techniques**\nThe term advanced computing techniques includes the hardware, software, and computational methods necessary to develop and deploy advanced weather models, such as artificial intelligence, high-performance computing, cloud computing, numerical methods, machine learning, data assimilation, large scale data analytics, predictive analysis techniques, and quantum computing.\n**(4) Advanced weather model**\nThe term advanced weather model means a model or suite of models used for the prediction of physical, biological, or chemical Earth system processes spanning weather, seasonal to subseasonal, or climate time scales.\n**(5) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation and the Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Science, Space, and Technology of the House of Representatives.\n**(6) Department**\nThe term Department means the Department of Energy.\n**(7) Institution of higher education**\nThe term institution of higher education has the meaning given that term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(8) National Laboratory**\nThe term National Laboratory has the meaning given that term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(9) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Coordination of research and development activities relating to improvement of advanced weather models\n##### (a) In general\nThe Secretary and the Administrator shall carry out collaborative research and development activities using advanced computing techniques that are focused on the improvement of advanced weather models relevant to the missions of the Department and the Administration.\n##### (b) Memorandum of understanding\n**(1) In general**\nThe Secretary and the Administrator shall carry out the activities under subsection (a) through the establishment of a memorandum of understanding or other appropriate interagency agreement.\n**(2) Use of process**\nThe memorandum or agreement, as the case may be, required under paragraph (1) shall require the use of a competitive, merit-reviewed process that considers applications from Federal agencies, National Laboratories, institutions of higher education, nonprofit institutions, and other appropriate entities (or a consortia thereof).\n##### (c) Activities\nIn carrying out the activities under subsection (a), the Secretary and the Administrator may\u2014\n**(1)**\nconduct collaborative research to develop new methods and optimization of advanced computing techniques;\n**(2)**\nexplore options for performance portability of optimized advanced weather model codes between the operational computing systems of the Administration and the high-performance computers of the Department;\n**(3)**\nadvance methods to accommodate, analyze, and extract information from large data sets of weather and climate information;\n**(4)**\nto the maximum extent practicable, and in compliance with national security policies, promote collaboration, open community-based software development, and data sharing between Federal agencies, National Laboratories, institutions of higher education, nonprofit institutions, and other appropriate entities by providing necessary access and secure data transfer capabilities; and\n**(5)**\nsupport maintenance of and improvements to scientific computing infrastructure that the Secretary and the Administrator determine appropriate.\n##### (d) Coordination\nIn carrying out the activities under subsection (a), the Secretary and the Administrator may\u2014\n**(1)**\ncarry out reimbursable agreements between the Department, the Administration, and other entities to maximize the effectiveness of research and development; and\n**(2)**\ncollaborate with other Federal agencies as appropriate.\n##### (e) Report\nNot later than 2 years after the date of enactment of this Act, the Secretary and the Administrator shall submit to the appropriate committees of Congress a report detailing the following:\n**(1)**\nInteragency coordination between each Federal agency involved in the activities carried out under this section, including activities described in subsection (c).\n**(2)**\nPotential opportunities to expand the technical capabilities of the Department and the Administration with respect to those activities.\n**(3)**\nCollaborative research achievements with respect to those activities.\n**(4)**\nAreas of future mutually beneficial gains as a result of those activities.\n**(5)**\nContinuation of coordination between the Department and the Administration on those activities.\n#### 4. Initiative on development of advanced weather models using advanced computing techniques\n##### (a) Computing research initiative\n**(1) In general**\nThe Administrator, in collaboration with the Secretary, shall carry out an initiative that may leverage advanced computing techniques and the expertise of the Department to develop and deploy advanced weather models to conduct proof of concept scenarios in comparison with current issued models (in this section referred to as the Initiative ).\n**(2) Process**\nThe Administrator, in collaboration with the Secretary, shall carry out the Initiative through a competitive, merit-reviewed process and consider applications from Federal agencies, National Laboratories, institutions of higher education, nonprofit institutions, and other appropriate entities (or a consortia thereof).\n**(3) Components**\nIn carrying out the Initiative, the Administrator, in collaboration with the Secretary, shall prevent duplication and coordinate research efforts in advanced computing techniques across the Administration, and may\u2014\n**(A)**\nleverage related efforts and data from the National Science and Technology Council, the Interagency Council for Advancing Meteorological Services, and other relevant interagency entities;\n**(B)**\nprovide sufficient capacity for long-term archive of and access to model output to support research and long-term study;\n**(C)**\ndetermine computing decisions based on an agile requirements framework;\n**(D)**\nsupport the training, recruitment, and retention of the next generation weather, water, and climate computing workforce through incentives and pathways for career development and employment opportunities;\n**(E)**\nsupport maintenance of and improvements to scientific computing infrastructure that the Administrator and the Secretary determine appropriate;\n**(F)**\nconduct comparative research between forecasts issued by the National Weather Service and operational models of the National Weather Service as compared to predictions and models developed to run using advanced computing techniques; and\n**(G)**\nshare relevant modeling system and application innovations developed through the Initiative, including applications based on the Unified Forecast System, through community-based activities.\n##### (b) Centers of excellence\n**(1) In general**\nThe Secretary, in collaboration with the Administrator, may establish at National Laboratories not more than 3 centers of excellence to support advanced weather models by researching, developing, and deploying advanced computing techniques in collaboration with research laboratories of the Administration and other relevant entities.\n**(2) Activities**\nEach center established under paragraph (1) may carry out activities that include the following:\n**(A)**\nLeveraging robust public-private partnership models to provide access to training, experience, and long-term development of workforce and infrastructure.\n**(B)**\nDeveloping and optimizing tools, libraries, algorithms, data structures, and other supporting software necessary for specific applications on high-performance computing systems.\n**(C)**\nApplying advanced computing techniques to improve the accuracy and resolution of advanced weather model predictions and to address current and future mission challenges.\n##### (c) Priority\nIn selecting National Laboratories at which to establish a center of excellence under subsection (b), the Secretary, in collaboration with the Administrator, shall give priority to Laboratories that\u2014\n**(1)**\nhave existing partnerships or relationships with the Administration;\n**(2)**\nhost significant artificial intelligence enabled high-performance computing systems;\n**(3)**\nhave a workforce with experience in advanced computing techniques;\n**(4)**\nare geographically proximate to one of the research laboratories of the Administration; and\n**(5)**\nhave a workforce with experience in weather and climate modeling or computation.\n##### (d) Multi-Year contracts\nThe Administrator and the Secretary may enter into multi-year contracts in accordance with section 3903 of title 41, United States Code, and shall ensure compliance with all provisions of that section, to support operational research and development related to advanced computing techniques.\n##### (e) Report\nNot later than 2 years after the date of enactment of this Act, the Administrator shall submit to the appropriate committees of Congress a report evaluating the following:\n**(1)**\nThe effectiveness of the Initiative, including applied research discoveries and advanced modeling improvements achieved through the Initiative.\n**(2)**\nPotential opportunities to expand capabilities of the Department and the Administration with respect to advanced computing techniques.\n**(3)**\nThe need for collaboration on advanced computing techniques between the Department and the Administration.\n##### (f) Sunset\nThe authority under this section shall terminate on the date that is 5 years after the date of enactment of this Act.\n#### 5. Research security\nThe activities authorized or required to be conducted under this Act shall be carried out in a manner consistent with subtitle D of title VI of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19231 et seq. ).",
      "versionDate": "2026-02-12",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-03-02T19:53:33Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3854is.xml"
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
      "title": "Advanced Weather Model Computing Development Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advanced Weather Model Computing Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Energy and the Administrator of the National Oceanic and Atmospheric Administration to conduct collaborative research to advance weather models in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T05:03:38Z"
    }
  ]
}
```
