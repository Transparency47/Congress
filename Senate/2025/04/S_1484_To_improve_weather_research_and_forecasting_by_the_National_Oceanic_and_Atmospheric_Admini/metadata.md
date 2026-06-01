# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1484?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1484
- Title: FORECAST Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1484
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-05-20T13:26:54Z
- Update date including text: 2025-05-20T13:26:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1484",
    "number": "1484",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "FORECAST Act of 2025",
    "type": "S",
    "updateDate": "2025-05-20T13:26:54Z",
    "updateDateIncludingText": "2025-05-20T13:26:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T21:35:53Z",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MS"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1484is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1484\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Markey (for himself, Mr. Wicker , Mr. Padilla , and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo improve weather research and forecasting by the National Oceanic and Atmospheric Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Forecasting Optimization for Robust Earth Climate Analysis and S2S Tracking Act of 2025 or the FORECAST Act of 2025 .\n#### 2. Improvements to weather research and forecasting\n##### (a) Improvements to subseasonal-to-Seasonal forecasting\nSection 1762 of the Food Security Act of 1985 ( 15 U.S.C. 8521 ) is amended\u2014\n**(1)**\nby amending subsection (c) to read as follows:\n(c) Functions (1) In general The Under Secretary and the heads of such other programs of the National Oceanic and Atmospheric Administration as the Under Secretary considers appropriate, shall\u2014 (A) conduct and support fundamental research to improve understanding of the sources and limitations of season-to-season predictability for temperature, precipitation, and other Earth system variables and applications; (B) collect and utilize observational data across the Earth system and other information in order to make usable, reliable, and timely foundational forecasts of subseasonal-to-seasonal temperature and precipitation; (C) prioritize the advancement of multi-model ensemble forecast systems and forecast verification and evaluation capacity, including\u2014 (i) the development of advanced coupled data assimilation methods using robust Earth system observational data; (ii) the development of improved coupled subseasonal-to-seasonal ensemble prediction systems; (iii) the improvement of exchanges and interactions between datasets across different models and Earth system observations to better understand local relationships between and drivers of ocean, land, snow, and ice observations; (iv) the provision of additional resources for the research and development of multi-model ensemble forecasts for purposes of advanced forecast modeling; and (v) the development of data management strategies to support operations and research activities; (D) leverage existing research and models from the weather and Earth system enterprises to improve the forecasts under subparagraph (B); (E) accelerate the operationalization of emerging modeling technologies developed within the research community, including pursuant to collaborations with other agencies and entities, as determined appropriate through increased funding for activities under section 102(b)(5) of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8512(b)(5) ), to support and assist the cross development of fully coupled subseasonal-to-seasonal forecast systems; (F) determine and provide information on how the subseasonal-to-seasonal temperature and precipitation, as forecasted under subparagraph (B) may relate to\u2014 (i) the number and severity of tornadoes, droughts, hurricanes, fires, floods, heat waves, marine heat waves, coastal inundation, winter storms, high-impact weather, or other relevant natural disasters; (ii) snowpack; (iii) sea ice conditions; and (iv) permafrost thaw and increased microbial decomposition; (G) develop an Internet clearinghouse to provide the forecasts under subparagraph (B) and the information under subparagraphs (B) and (F) on both national and regional levels; and (H) leverage emerging technologies, such as artificial intelligence, machine learning, and use of unmanned systems. (2) Alignment with report The Under Secretary and the heads of such other programs of the National Oceanic and Atmospheric Administration as the Under Secretary considers appropriate shall carry out the requirements under paragraph (1) in alignment with the findings of the report submitted to Congress by the Under Secretary pursuant to subsection (h) on July 12, 2018, entitled, Subseasonal and Seasonal Forecasting Innovation: Plans for the Twenty-First Century . (3) Earth system defined In this subsection, the term Earth system includes atmosphere, ocean, terrestrial, ice, and related processes, and data that influence or drive subseasonal-to-seasonal weather and climate. ; and\n**(2)**\nby amending subsection (j) to read as follows:\n(j) Authorization of appropriations (1) In general There are authorized to be appropriated to the Under Secretary, for each of fiscal years 2026 and 2027\u2014 (A) $28,500,000 to carry out this section; and (B) for activities under section 102(b)(5) of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8512(b)(5) ) pursuant to subsection (c)(1)(E), such sums as may be necessary to carry out such subsection. (2) Use of funds Amounts appropriated pursuant to an authorization under paragraph (1)(B) shall be used for the designated responsibilities of the modeling team of the National Oceanic and Atmospheric Administration within the Earth Prediction Innovation Center or an institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )), including activities that fall under the following focus areas: (A) High-performance computing. (B) Scientific innovation. (C) Management and planning. (D) External engagement and community. .\n##### (b) Weather and Earth System Modeling And Data Assimilation Workforce Innovation Program\n**(1) In general**\nTitle IV of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8541 et seq. ) is amended by adding at the end the following:\n415. Weather and Earth System Modeling and Data Assimilation Workforce Innovation Program (a) In general The Under Secretary shall establish a program, to be known as the Weather and Earth System Modeling and Data Assimilation Workforce Innovation Program (in this section referred to as the program ). (b) Education and recruitment In carrying out the program, the Under Secretary shall support the education and recruitment of personnel and establish a set of new workforce development programs to develop pathways for next-generation researchers, engineers, and practitioners who are skilled in and can operate or develop weather and Earth system technologies that exploit and advance emerging computing architectures, artificial intelligence and machine learning, unmanned systems, and next-generation data assimilation and observing systems, including through financial assistance for scholarships, fellowships, and research at institutions of higher education in areas relevant to improvement of data assimilation systems and weather and Earth system data modeling capabilities. (c) Human capital planning (1) In general In carrying out the program, the Under Secretary shall develop and, on an annual basis, revise a data assimilation and weather and Earth system modeling workforce human capital plan that identifies workforce needs to facilitate innovation in emerging weather technologies and data assimilation systems, including by identifying gaps in funding and expertise, hiring challenges, and policies to mitigate turnover that will help avoid mid-project staffing changes. (2) Submission of plan The Under Secretary shall submit the data assimilation and weather and Earth system modeling workforce human capital plan required under paragraph (1), and any revision to that plan, to the Secretary of Commerce and the Director of the Office of Management and Budget. (3) Use of plans (A) In general The Under Secretary shall use the data assimilation and weather and Earth system modeling workforce human capital plans required under paragraph (1) to carry out the education and recruitment required under subsection (b). (B) Pathways to hiring In carrying out the data assimilation and weather and Earth system modeling workforce human capital plan required under paragraph (1), the Under Secretary may use the pathways programs established under part 362 of title 5, Code of Federal Regulations (or a successor program), to facilitate the recruitment and hiring of personnel for data assimilation and weather and Earth system modeling activities. (4) Authority to provide funds If the Under Secretary, in preparing the data assimilation and weather and Earth system modeling workforce human capital plan pursuant to paragraph (1), identifies workforce gaps for the data assimilation and weather and Earth system modeling processes of the National Oceanic and Atmospheric Administration, the Under Secretary may\u2014 (A) use funds made available to the Administration to carry out such plan; and (B) establish agreements and awards with institutions of higher education or nonprofit entities to facilitate the integration of innovative data assimilation and weather and Earth system modeling technologies and systems into the larger weather enterprise. (d) Updates to direct hiring authority The Under Secretary, acting through the Director of the Office of Human Capital Services, shall make necessary updates to the eligibility requirements for the direct hiring authority program of the National Oceanic and Atmospheric Administration to include the program, the Weather Program Office Innovation for Next Generation Scientists Dissertation Fellowship, the Consortium for Advanced Data Assimilation Research and Education, and any other fellowship or internship programs determined by the Under Secretary to be relevant to the weather enterprise. (e) Report Not later than 2 years after the initial date on which the Under Secretary provides funds under subsection (c)(4) to an institution of higher education or a nonprofit entity, the Under Secretary shall, using information about the program collected from any such institution or entity in receipt of those funds, submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report on the effectiveness and impact of those funds in improving the quality and preparedness of the weather and Earth system modeling and data assimilation workforce. (f) Definitions In this section: (1) Earth system The term Earth system includes atmosphere, ocean, terrestrial, ice, and related processes, and data that influence or drive subseasonal-to-seasonal weather and climate. (2) Institution of higher education The term institution of higher education has the meaning given that term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ). (3) Nonprofit entity The term nonprofit entity has the meaning given that term in section 9901 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 ). (g) Authorization of appropriations There are authorized to be appropriated to the Under Secretary such sums as may be necessary to carry out the functions of the program, as determined by the Under Secretary. .\n**(2) Clerical amendment**\nThe table of contents in section 1(b) of the Weather Research and Forecasting Innovation Act of 2017 ( Public Law 115\u201325 ; 131 Stat. 91) is amended by inserting after the item relating to section 414 the following:\nSec. 415. Weather and Earth System Modeling and Data Assimilation Workforce Innovation Program. .",
      "versionDate": "2025-04-10",
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
        "updateDate": "2025-05-20T13:26:54Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1484is.xml"
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
      "title": "FORECAST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FORECAST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Forecasting Optimization for Robust Earth Climate Analysis and S2S Tracking Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve weather research and forecasting by the National Oceanic and Atmospheric Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:23Z"
    }
  ]
}
```
