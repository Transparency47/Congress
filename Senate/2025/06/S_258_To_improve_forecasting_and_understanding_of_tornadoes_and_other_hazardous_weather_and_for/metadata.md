# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/258
- Title: TORNADO Act
- Congress: 119
- Bill type: S
- Bill number: 258
- Origin chamber: Senate
- Introduced date: 2025-01-27
- Update date: 2025-10-09T03:26:18Z
- Update date including text: 2025-10-09T03:26:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-27: Introduced in Senate
- 2025-01-27 - IntroReferral: Introduced in Senate
- 2025-01-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- 2025-06-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-26.
- 2025-06-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-26.
- 2025-06-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 88.
- Latest action: 2025-01-27: Introduced in Senate

## Actions

- 2025-01-27 - IntroReferral: Introduced in Senate
- 2025-01-27 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- 2025-06-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-26.
- 2025-06-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-26.
- 2025-06-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 88.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-27",
    "latestAction": {
      "actionDate": "2025-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/258",
    "number": "258",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "W000437",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Wicker, Roger F. [R-MS]",
        "lastName": "Wicker",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "TORNADO Act",
    "type": "S",
    "updateDate": "2025-10-09T03:26:18Z",
    "updateDateIncludingText": "2025-10-09T03:26:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 88.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-26.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-06-02",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-26.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-27",
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
      "actionDate": "2025-01-27",
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
            "date": "2025-06-02T20:36:23Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T15:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-27T18:16:46Z",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "MS"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "IA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "KS"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "MT"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "IN"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "TX"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-01-27",
      "state": "MI"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-01-27",
      "state": "GA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s258is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 258\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2025 Mr. Wicker (for himself, Mrs. Hyde-Smith , Mr. Grassley , Mr. Moran , Mr. Sheehy , Mr. Young , Mr. Cruz , Mr. Peters , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo improve forecasting and understanding of tornadoes and other hazardous weather, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tornado Observations Research and Notification Assessment for Development of Operations Act or the TORNADO Act .\n#### 2. Definitions\nIn this Act:\n**(1) Hazardous weather and water events**\nThe term hazardous weather and water events means weather and water events that have a high risk of loss of life or property, including\u2014\n**(A)**\nsevere storms, such as hurricanes and short-fused, small-scale hazardous weather or hydrologic events produced by thunderstorms, including large hail, damaging winds, tornadoes, and flash floods;\n**(B)**\nwinter storms, such as freezing or frozen precipitation (including freezing rain, sleet, and snow), or combined effects of freezing or frozen precipitation and strong winds; and\n**(C)**\nother weather hazards, such as extreme heat or cold, wildfire, drought, dense fog, high winds, river flooding, and lakeshore flooding.\n**(2) Historically Black college or university**\nThe term historically Black college or university has the meaning given the term part B institution in section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 ).\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n**(5) National laboratory**\nThe term National Laboratory has the meaning given the term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(6) Under Secretary**\nThe term Under Secretary means the Under Secretary of Commerce for Oceans and Atmosphere.\n#### 3. Hazardous weather and water event risk communication\n##### (a) In general\nThe Under Secretary shall maintain and improve the system of the National Oceanic and Atmospheric Administration by which the risks of hazardous weather and water events are communicated to the general public, with the goal of informing action and encouraging response to prevent loss of life and property.\n##### (b) Hazard risk communication improvement and simplification\n**(1) In general**\nThe Under Secretary shall maintain a hazard risk communication office (in this subsection referred to as the Office ), for the purposes of simplifying and improving the communication of hazardous weather and water event risks.\n**(2) Terminology**\nThe Office shall identify, eliminate, or modify unnecessary, redundant, or confusing terms for hazardous weather and water event communications and add new terminology, as appropriate.\n**(3) Communications improvement**\nThe Office shall improve the form, content, and methods of hazardous weather and water event communications to more clearly inform action and increase the likelihood that the public takes such action to prevent the loss of life or property.\n**(4) Evaluations**\nThe Office shall, in coordination with the performance branch of the National Weather Service, develop metrics for that branch to track and evaluate the degree to which hazardous weather and water event communications inform action and encourage response.\n**(5) Support plan**\n**(A) In general**\nThe Office shall develop a plan for the purpose of supporting the activities described in paragraph (3).\n**(B) Periodic update and elements**\nThe plan developed under subparagraph (A) shall be periodically updated and informed by internal and extramural research and the results of the evaluation of hazardous weather and water event communications conducted under paragraph (4).\n**(6) Methods**\nIn carrying out this subsection, the Office shall develop and implement recommendations that\u2014\n**(A)**\nare based on the best and most recent understanding from social, behavioral, risk, and communication science research;\n**(B)**\nare validated by social, behavioral, risk, and communication science, taking into account the importance of methods that support reproduction and replication of scientific studies, use of rigorous statistical analyses, and, as applicable, data analysis supported by artificial intelligence and machine learning technologies;\n**(C)**\naccount for the needs of various demographics, vulnerable populations, and geographic regions;\n**(D)**\naccount for the differences between various types of weather and water hazards;\n**(E)**\nrespond to the needs of Federal, State, and local government partners and media partners; and\n**(F)**\naccount for necessary changes in the infrastructure, technology, and protocols for creating and disseminating federally operated watches and warnings.\n**(7) Coordination**\nIn implementing this subsection, the Office shall coordinate with\u2014\n**(A)**\nFederal partners, including National Laboratories, Cooperative Institutes, and regional integrated sciences and assessments programs;\n**(B)**\nState and local government partners;\n**(C)**\nIndian Tribes;\n**(D)**\ninstitutions of higher education; and\n**(E)**\nmedia partners.\n**(8) Timeliness and consistency**\nThe Office shall develop best practices and guidance for ensuring timely and consistent communication across public facing platforms that disseminate hazardous weather and water event information.\n##### (c) Hazard communication research and engagement\n**(1) In general**\nThe Under Secretary shall establish or maintain a research program\u2014\n**(A)**\nto modernize the creation and communication of risk-based, statistically reliable, probabilistic hazard information, with the goal of informing effective actions and encouraging responses to hazardous weather and water events; and\n**(B)**\nto improve the fundamental social, behavioral, risk, and communication science regarding hazardous weather and water event communication.\n**(2) Coordination**\nIn carrying out the research program required by paragraph (1), the Under Secretary shall coordinate and communicate with States, Indian Tribes, localities, and emergency managers on research priorities and results.\n**(3) Pilot program for tornado hazard communication required**\n**(A) In general**\nTo further research into hazard communication, the Under Secretary, in collaboration with one or more eligible institutions, shall establish a pilot program for tornado hazard communication to test the effectiveness of implementing the research conducted under this subsection with respect to tornadoes.\n**(B) Eligible institution defined**\nIn this paragraph, the term eligible institution means any of the following:\n**(i)**\nA historically Black college or university located in an area of persistent poverty that is subjected to frequent severe weather, such as tornadoes, hurricanes, and floods.\n**(ii)**\nAn institution of higher education in close proximity to a Weather Forecast Office of the National Weather Service.\n##### (d) Data management\nThe Under Secretary shall establish, maintain, and improve a central repository system for the National Oceanic and Atmospheric Administration for social, behavioral, risk, and economic data related to the communication of hazardous weather and water events, including data developed or received pursuant to paragraphs (3), (4), and (5) of subsection (b).\n##### (e) Digital watermarking\nThe Under Secretary shall develop methods to reduce the likelihood of unauthorized tampering with online hazardous weather and water event risk communication, such as developing digital watermarks.\n#### 4. Warn-on-forecast strategic plan\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Under Secretary shall prepare and submit to Congress a strategic plan for developing and prioritizing the implementation of high-resolution probabilistic forecast guidance for hazardous weather and water events using a next-generation weather forecast and warning framework.\n##### (b) Plan elements\nThe strategic plan required by subsection (a) shall include the following:\n**(1)**\nA discussion of\u2014\n**(A)**\nthe priorities and needs of vulnerable populations and National Weather Service partners; and\n**(B)**\nhigh-performance computing, visualization, and dissemination needs.\n**(2)**\nA timeline and guidance for implementation of\u2014\n**(A)**\nhigh-resolution numerical weather prediction models;\n**(B)**\nmethods for meeting the high-performance computing, visualization, and dissemination needs discussed under paragraph (1)(B);\n**(C)**\nreal-time high-resolution probabilistic forecasts;\n**(D)**\nimproved observations, including through radars, satellites, and uncrewed aerial systems;\n**(E)**\na flexible framework to communicate clear and simple hazardous weather and water event information to the public; and\n**(F)**\nsocial, behavioral, risk, and communication research to improve the forecaster operational environment and societal information reception and response.\n#### 5. Tornado rating system\n##### (a) In general\nThe Under Secretary shall, in collaboration with such stakeholders as the Under Secretary considers appropriate\u2014\n**(1)**\nevaluate the system used as of the date of the enactment of this Act to rate the severity of tornadoes; and\n**(2)**\ndetermine whether updates to that system are required to ensure that the ratings accurately reflect the severity of tornadoes.\n##### (b) Update required\nIf the Under Secretary determines under subsection (a) that updates to the tornado rating system are necessary, the Under Secretary shall update the system.\n#### 6. Post-storm surveys and assessments\n##### (a) In general\nThe Under Secretary shall perform one or more post-storm surveys and assessments following each hazardous weather or water event determined by the Under Secretary to be of sufficient societal importance to warrant a post-event survey and assessment.\n##### (b) Coordination\nThe Under Secretary shall coordinate with Federal, State, and local governments, Indian Tribes, private entities, and relevant institutions of higher education when conducting post-storm surveys and assessments under subsection (a) in order to optimize data collection, sharing, and integration.\n##### (c) Data availability\nThe Under Secretary shall make the data obtained from each post-storm survey and assessment conducted under subsection (a) available to the public as soon as practicable after conducting the survey and assessment.\n##### (d) Improvement\nThe Under Secretary shall\u2014\n**(1)**\ninvestigate the role of uncrewed aerial systems in data collection during post-storm surveys and assessments conducted under subsection (a);\n**(2)**\nidentify gaps in and update tactics and procedures to enhance the efficiency and reliability of data obtained from post-storm surveys and assessments; and\n**(3)**\nincrease the number of post-storm community impact studies, including by\u2014\n**(A)**\nsurveying individual responses;\n**(B)**\nconducting review of the accuracy of prior risk evaluations;\n**(C)**\nevaluating the efficacy of prior mitigation activity; and\n**(D)**\ngathering survivability statistics.\n##### (e) Support for employees\nThe Under Secretary shall provide training, resources, and access to professional counseling to support the emotional and mental health and well-being of employees conducting post-storm surveys and assessments under subsection (a).\n#### 7. VORTEX-USA program\n##### (a) In general\nSection 103 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8513 ) is amended\u2014\n**(1)**\nin the section heading, by striking Tornado warning improvement and extension and inserting VORTEX-USA ;\n**(2)**\nin subsection (a), by striking establish a tornado warning improvement and extension program and inserting maintain a program for rapidly improving tornado forecast and warnings ;\n**(3)**\nby redesignating subsections (d) and (e) as subsections (f) and (g), respectively;\n**(4)**\nby inserting after subsection (c) the following:\n(d) Warnings The program required by subsection (a) shall\u2014 (1) continue the research necessary to develop and deploy probabilistic weather forecast guidance technology for tornadoes; and (2) incorporate, as appropriate, hazard communication research. (e) Research (1) In general The Under Secretary shall, through the program required by subsection (a), award grants for research that focuses on improving\u2014 (A) the social, behavioral, risk, communication, and economic sciences related to vulnerabilities, risk communication, and delivery of information critical for saving lives and property related to tornadoes; and (B) the physical sciences, engineering, and technology related to tornado formation, the interactions of tornadoes with the built and natural environment, and the interaction of tornadoes and hurricanes. (2) Priority institutions (A) In general In awarding grants under paragraph (1), the Under Secretary may prioritize awarding grants to minority-serving institutions. (B) Definition of minority-serving institution In this paragraph, the term minority-serving institution means\u2014 (i) a part B institution (as defined in section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 )); (ii) a Hispanic-serving institution (as defined in section 502(a) of that Act ( 20 U.S.C. 1101a(a) )); (iii) a Tribal College or University (as defined in section 316(b) of that Act ( 20 U.S.C. 1059c(b) )); (iv) an Alaska Native-serving institution (as defined in section 317(b) of that Act ( 20 U.S.C. 1059d(b) )); (v) a Native Hawaiian-serving institution (as defined in section 317(b) of that Act ( 20 U.S.C. 1059d(b) )); (vi) a Predominantly Black Institution (as defined in section 318(b) of that Act ( 20 U.S.C. 1059e(b) )); (vii) an Asian American and Native American Pacific Islander-serving institution (as defined in section 320(b) of that Act ( 20 U.S.C. 1059g(b) )); or (viii) a Native American-serving, nontribal institution (as defined in section 319(b) of that Act ( 20 U.S.C. 1059f(b) )). ; and\n**(5)**\nby adding at the end the following:\n(h) Authorization of appropriations There is authorized to be appropriated to the Under Secretary to carry out this section $11,000,000 for each of fiscal years 2025 through 2032, of which not less than $2,000,000 each fiscal year shall be used for grants awarded under subsection (e). .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Weather Research and Forecasting Innovation Act of 2017 ( Public Law 115\u201325 ; 131 Stat. 91) is amended by striking the item relating to section 103 and inserting the following:\nSec. 103. VORTEX-USA program. .\n#### 8. Government Accountability Office report on hazardous weather and water alert dissemination\n##### (a) In general\nNot later than 540 days after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report that examines the information technology infrastructure of the National Weather Service of the National Oceanic and Atmospheric Administration, specifically regarding the system for timely public notification of hazardous weather and water event alerts and updates.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nAn analysis of the information technology infrastructure of the National Weather Service, including software and hardware capabilities and limitations, including an examination of server and data storage methods, broadband, data management, and data sharing.\n**(2)**\nAn identification of secondary and tertiary fail-safes for the timely distribution of hazardous weather and water event alerts to the public.\n**(3)**\nA determination of the extent to which public notifications are delayed and an identification of corrective measures that do not add additional notification time.\n**(4)**\nAn assessment of whether collaboration with other Federal Government offices, States, or private entities could reduce delays in notifications to the public.\n**(5)**\nA description of actions being undertaken to better identify critical steps in the hazards notification process that may be vulnerable to disruption or failure in the event of communication, technologic, or computational failure.\n#### 9. Elimination of certain report requirements\n##### (a) Weather Research and Forecasting Innovation Act of 2017\n**(1) In general**\nSection 403 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8543 ) is amended by striking subsection (d).\n**(2) Technical amendment**\nSection 403(a) of such Act ( 15 U.S.C. 8543(a) ) is amended by inserting the after Director of .\n##### (b) National Oceanic and Atmospheric Administration Authorization Act of 1992\nSection 106 of the National Oceanic and Atmospheric Administration Authorization Act of 1992 ( Public Law 102\u2013567 ; 106 Stat. 4274) is amended by striking subsection (c) ( 15 U.S.C. 1537 ).",
      "versionDate": "2025-01-27",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s258rs.xml",
      "text": "II\nCalendar No. 88\n119th CONGRESS\n1st Session\nS. 258\n[Report No. 119\u201326]\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2025 Mr. Wicker (for himself, Mrs. Hyde-Smith , Mr. Grassley , Mr. Moran , Mr. Sheehy , Mr. Young , Mr. Cruz , Mr. Peters , Mr. Warnock , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nJune 2, 2025 Reported by Mr. Cruz , with amendments Omit the parts struck through and insert the parts printed in italic\nA BILL\nTo improve forecasting and understanding of tornadoes and other hazardous weather, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tornado Observations Research and Notification Assessment for Development of Operations Act or the TORNADO Act .\n#### 2. Definitions\nIn this Act:\n**(1) Hazardous weather and water events**\nThe term hazardous weather and water events means weather and water events that have a high risk of loss of life or property, including\u2014\n**(A)**\nsevere storms, such as hurricanes and short-fused, small-scale hazardous weather or hydrologic events produced by thunderstorms, including large hail, damaging winds, tornadoes, and flash floods;\n**(B)**\nwinter storms, such as freezing or frozen precipitation (including freezing rain, sleet, and snow), or combined effects of freezing or frozen precipitation and strong winds; and\n**(C)**\nother weather hazards, such as extreme heat or cold, wildfire, drought, dense fog, high winds, river flooding, and lakeshore flooding.\n**(2) Historically Black college or university**\nThe term historically Black college or university has the meaning given the term part B institution in section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 ).\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n**(5) National laboratory**\nThe term National Laboratory has the meaning given the term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(6) Under Secretary**\nThe term Under Secretary means the Under Secretary of Commerce for Oceans and Atmosphere.\n#### 3. Hazardous weather and water event risk communication\n##### (a) In general\nThe Under Secretary shall maintain and improve the system of the National Oceanic and Atmospheric Administration by which the risks of hazardous weather and water events are communicated to the general public, with the goal of informing action and encouraging response to prevent loss of life and property.\n##### (b) Hazard risk communication improvement and simplification\n**(1) In general**\nThe Under Secretary shall maintain a hazard risk communication office (in this subsection referred to as the Office ), for the purposes of simplifying and improving the communication of hazardous weather and water event risks.\n**(2) Terminology**\nThe Office shall identify, eliminate, or modify unnecessary, redundant, or confusing terms for hazardous weather and water event communications and add new terminology, as appropriate.\n**(3) Communications improvement**\nThe Office shall improve the form, content, and methods of hazardous weather and water event communications to more clearly inform action and increase the likelihood that the public takes such action to prevent the loss of life or property.\n**(4) Evaluations**\nThe Office shall, in coordination with the performance branch of the National Weather Service, develop metrics for that branch to track and evaluate the degree to which hazardous weather and water event communications inform action and encourage response.\n**(5) Support plan**\n**(A) In general**\nThe Office shall develop a plan for the purpose of supporting the activities described in paragraph (3).\n**(B) Periodic update and elements**\nThe plan developed under subparagraph (A) shall be periodically updated and informed by internal and extramural research and the results of the evaluation of hazardous weather and water event communications conducted under paragraph (4).\n**(6) Methods**\nIn carrying out this subsection, the Office shall develop and implement recommendations that\u2014\n**(A)**\nare based on the best and most recent understanding from social, behavioral, risk, and communication science research;\n**(B)**\nare validated by social, behavioral, risk, and communication science, taking into account the importance of methods that support reproduction and replication of scientific studies, use of rigorous statistical analyses, and, as applicable, data analysis supported by artificial intelligence and machine learning technologies;\n**(C)**\naccount for the needs of various demographics, vulnerable populations, and geographic regions;\n**(D)**\naccount for the differences between various types of weather and water hazards;\n**(E)**\nrespond to the needs of Federal, State, and local government partners and media partners; and\n**(F)**\naccount for the need for enhanced or earlier communication of a hazardous weather event to inform action and encourage response when the event occurs in a geographic area where the event is historically abnormal; and\n**(F) (G)**\naccount for necessary changes in the infrastructure, technology, and protocols for creating and disseminating federally operated watches and warnings.\n**(7) Coordination**\nIn implementing this subsection, the Office shall coordinate with\u2014\n**(A)**\nFederal partners, including National Laboratories, Cooperative Institutes, and regional integrated sciences and assessments programs;\n**(B)**\nState and local government partners;\n**(C)**\nIndian Tribes;\n**(D)**\ninstitutions of higher education; and\n**(E)**\nmedia partners.\n**(8) Timeliness and consistency**\nThe Office shall develop best practices and guidance for ensuring timely and consistent communication across public facing platforms that disseminate hazardous weather and water event information.\n##### (c) Hazard communication research and engagement\n**(1) In general**\nThe Under Secretary shall establish or maintain a research program\u2014\n**(A)**\nto modernize the creation and communication of risk-based, statistically reliable, probabilistic hazard information, with the goal of informing effective actions and encouraging responses to hazardous weather and water events; and\n**(B)**\nto improve the fundamental social, behavioral, risk, and communication science regarding hazardous weather and water event communication.\n**(2) Coordination**\nIn carrying out the research program required by paragraph (1), the Under Secretary shall coordinate and communicate with States, Indian Tribes, localities, and emergency managers on research priorities and results.\n**(3) Pilot program for tornado hazard communication required**\n**(A) In general**\nTo further research into hazard communication, the Under Secretary, in collaboration with one or more eligible institutions, shall establish a pilot program for tornado hazard communication to test the effectiveness of implementing the research conducted under this subsection with respect to tornadoes.\n**(B) Eligible institution defined**\nIn this paragraph, the term eligible institution means any of the following:\n**(i)**\nA historically Black college or university located in an area of persistent poverty that is subjected to frequent severe weather, such as tornadoes, hurricanes, and floods.\n**(ii)**\nAn institution of higher education in close proximity to a Weather Forecast Office of the National Weather Service.\n##### (d) Data management\nThe Under Secretary shall establish, maintain, and improve a central repository system for the National Oceanic and Atmospheric Administration for social, behavioral, risk, and economic data related to the communication of hazardous weather and water events, including data developed or received pursuant to paragraphs (3), (4), and (5) of subsection (b).\n##### (e) Digital watermarking\nThe Under Secretary shall develop methods to reduce the likelihood of unauthorized tampering with online hazardous weather and water event risk communication, such as developing digital watermarks.\n#### 4. Warn-on-forecast strategic plan\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Under Secretary shall prepare and submit to Congress a strategic plan for developing and prioritizing the implementation of high-resolution probabilistic forecast guidance for hazardous weather and water events using a next-generation weather forecast and warning framework.\n##### (b) Plan elements\nThe strategic plan required by subsection (a) shall include the following:\n**(1)**\nA discussion of\u2014\n**(A)**\nthe priorities and needs of vulnerable populations and National Weather Service partners; and\n**(B)**\nhigh-performance computing, visualization, and dissemination needs.\n**(2)**\nA timeline and guidance for implementation of\u2014\n**(A)**\nhigh-resolution numerical weather prediction models;\n**(B)**\nmethods for meeting the high-performance computing, visualization, and dissemination needs discussed under paragraph (1)(B);\n**(C)**\nreal-time high-resolution probabilistic forecasts;\n**(D)**\nimproved observations, including through radars, satellites, and uncrewed aerial systems;\n**(E)**\na flexible framework to communicate clear and simple hazardous weather and water event information to the public; and\n**(F)**\nimproved coordination among offices of the National Weather Service, such as the National Hurricane Center, the River Forecast Centers, and forecast offices of the National Weather Service, to reduce the occurrence of disparate weather predictions and to better communicate the relationship between overlapping weather forecasts for different periods of time; and\n**(F) (G)**\nsocial, behavioral, risk, and communication research to improve the forecaster operational environment and societal information reception and response.\n#### 5. Tornado rating system\n##### (a) In general\nThe Under Secretary shall, in collaboration with such stakeholders as the Under Secretary considers appropriate\u2014\n**(1)**\nevaluate the system used as of the date of the enactment of this Act to rate the severity of tornadoes; and\n**(2)**\ndetermine whether updates to that system are required to ensure that the ratings accurately reflect the severity of tornadoes.\n##### (b) Update required\nIf the Under Secretary determines under subsection (a) that updates to the tornado rating system are necessary, the Under Secretary shall update the system.\n#### 6. Post-storm surveys and assessments\n##### (a) In general\nThe Under Secretary shall perform one or more post-storm surveys and assessments following each hazardous weather or water event determined by the Under Secretary to be of sufficient societal importance to warrant a post-event survey and assessment.\n##### (b) Coordination\nThe Under Secretary shall coordinate with Federal, State, and local governments, Indian Tribes, private entities, and relevant institutions of higher education when conducting post-storm surveys and assessments under subsection (a) in order to optimize data collection, sharing, and integration.\n##### (c) Data availability\nThe Under Secretary shall make the data obtained from each post-storm survey and assessment conducted under subsection (a) available to the public as soon as practicable after conducting the survey and assessment.\n##### (d) Improvement\nThe Under Secretary shall\u2014\n**(1)**\ninvestigate the role of uncrewed aerial systems in data collection during post-storm surveys and assessments conducted under subsection (a);\n**(2)**\nidentify gaps in and update tactics and procedures to enhance the efficiency and reliability of data obtained from post-storm surveys and assessments; and\n**(3)**\nincrease the number of post-storm community impact studies, including by\u2014\n**(A)**\nsurveying individual responses;\n**(B)**\nconducting review of the accuracy of prior risk evaluations;\n**(C)**\nevaluating the efficacy of prior mitigation activity; and\n**(D)**\ngathering survivability statistics.\n##### (e) Support for employees\nThe Under Secretary shall provide training, resources, and access to professional counseling to support the emotional and mental health and well-being of employees conducting post-storm surveys and assessments under subsection (a).\n#### 7. VORTEX-USA program\n##### (a) In general\nSection 103 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8513 ) is amended\u2014\n**(1)**\nin the section heading, by striking Tornado warning improvement and extension and inserting VORTEX-USA ;\n**(2)**\nin subsection (a), by striking establish a tornado warning improvement and extension program and inserting maintain a program for rapidly improving tornado forecast and warnings ;\n**(3)**\nby redesignating subsections (d) and (e) as subsections (f) and (g), respectively;\n**(4)**\nby inserting after subsection (c) the following:\n(d) Warnings The program required by subsection (a) shall\u2014 (1) continue the research necessary to develop and deploy probabilistic weather forecast guidance technology for tornadoes; and (2) incorporate, as appropriate, hazard communication research. (e) Research (1) In general The Under Secretary shall, through the program required by subsection (a), award grants for research that focuses on improving\u2014 (A) the social, behavioral, risk, communication, and economic sciences related to vulnerabilities, risk communication, and delivery of information critical for saving lives and property related to tornadoes; and (B) the physical sciences, engineering, and technology related to tornado formation, the interactions of tornadoes with the built and natural environment, and the interaction of tornadoes and hurricanes. (2) Priority institutions (A) In general In awarding grants under paragraph (1), the Under Secretary may prioritize awarding grants to minority-serving institutions. (B) Definition of minority-serving institution In this paragraph, the term minority-serving institution means\u2014 (i) a part B institution (as defined in section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 )); (ii) a Hispanic-serving institution (as defined in section 502(a) of that Act ( 20 U.S.C. 1101a(a) )); (iii) a Tribal College or University (as defined in section 316(b) of that Act ( 20 U.S.C. 1059c(b) )); (iv) an Alaska Native-serving institution (as defined in section 317(b) of that Act ( 20 U.S.C. 1059d(b) )); (v) a Native Hawaiian-serving institution (as defined in section 317(b) of that Act ( 20 U.S.C. 1059d(b) )); (vi) a Predominantly Black Institution (as defined in section 318(b) of that Act ( 20 U.S.C. 1059e(b) )); (vii) an Asian American and Native American Pacific Islander-serving institution (as defined in section 320(b) of that Act ( 20 U.S.C. 1059g(b) )); or (viii) a Native American-serving, nontribal institution (as defined in section 319(b) of that Act ( 20 U.S.C. 1059f(b) )). ; and\n**(5)**\nby adding at the end the following:\n(h) Authorization of appropriations There is authorized to be appropriated to the Under Secretary to carry out this section $11,000,000 for each of fiscal years 2025 through 2032, of which not less than $2,000,000 each fiscal year shall be used for grants awarded under subsection (e). .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Weather Research and Forecasting Innovation Act of 2017 ( Public Law 115\u201325 ; 131 Stat. 91) is amended by striking the item relating to section 103 and inserting the following:\nSec. 103. VORTEX-USA program. .\n#### 8. Government Accountability Office report on hazardous weather and water alert dissemination\n##### (a) In general\nNot later than 540 days after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report that examines the information technology infrastructure of the National Weather Service of the National Oceanic and Atmospheric Administration, specifically regarding the system for timely public notification of hazardous weather and water event alerts and updates.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nAn analysis of the information technology infrastructure of the National Weather Service, including software and hardware capabilities and limitations, including an examination of server and data storage methods, broadband, data management, and data sharing.\n**(2)**\nAn identification of secondary and tertiary fail-safes for the timely distribution of hazardous weather and water event alerts to the public.\n**(3)**\nA determination of the extent to which public notifications are delayed and an identification of corrective measures that do not add additional notification time.\n**(4)**\nAn assessment of whether collaboration with other Federal Government offices, States, or private entities could reduce delays in notifications to the public.\n**(5)**\nA description of actions being undertaken to better identify critical steps in the hazards notification process that may be vulnerable to disruption or failure in the event of communication, technologic, or computational failure.\n#### 9. Elimination of certain report requirements\n##### (a) Weather Research and Forecasting Innovation Act of 2017\n**(1) In general**\nSection 403 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8543 ) is amended by striking subsection (d).\n**(2) Technical amendment**\nSection 403(a) of such Act ( 15 U.S.C. 8543(a) ) is amended by inserting the after Director of .\n##### (b) National Oceanic and Atmospheric Administration Authorization Act of 1992\nSection 106 of the National Oceanic and Atmospheric Administration Authorization Act of 1992 ( Public Law 102\u2013567 ; 106 Stat. 4274) is amended by striking subsection (c) ( 15 U.S.C. 1537 ).",
      "versionDate": "2025-06-02",
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
            "name": "Atmospheric science and weather",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-08T14:34:51Z"
          },
          {
            "name": "Earth sciences",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Floods and storm protection",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-05-08T14:34:50Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-05-08T14:34:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-01T19:32:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-27",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s258",
          "measure-number": "258",
          "measure-type": "s",
          "orig-publish-date": "2025-01-27",
          "originChamber": "SENATE",
          "update-date": "2025-06-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s258v00",
            "update-date": "2025-06-03"
          },
          "action-date": "2025-01-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Tornado Observations Research and Notification Assessment for Development of Operations Act or the TORNADO Act</strong></p><p>This bill requires the National Oceanic and Atmospheric Administration (NOAA) to evaluate and improve its communications about hurricanes, tornadoes, winter storms, and other hazardous weather events.</p><p>Specifically, NOAA must establish a Risk Communication Office to evaluate the effectiveness of NOAA's communications and to identify ways to provide simpler and clearer information to the public about hazardous weather events. NOAA must also (1) establish a research program to modernize its communication systems, and (2) establish a pilot program to implement the research with respect to communications about tornadoes.</p><p>Additionally, the bill requires NOAA to develop a strategic plan for implementing the Warn-on-Forecast System, which aims to provide more advanced warnings of thunderstorm-related events (e.g., tornadoes). The bill also requires NOAA to evaluate its tornado rating system and to conduct post-storm assessments of significant events.</p><p>The bill also provides statutory authority for NOAA's Verification of the Origins of Rotation in Tornadoes Experiment (known as VORTEX-USA), a collaborative project between meteorologists and social scientists to study the conditions that contribute to dangerous tornadoes in the Southeast and the best ways to communicate these events to the public.</p><p>Finally, the Government Accountability Office must report on the National Weather Service's communication technology, particularly with respect to timely notices of hazardous weather events.</p>"
        },
        "title": "TORNADO Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s258.xml",
    "summary": {
      "actionDate": "2025-01-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Tornado Observations Research and Notification Assessment for Development of Operations Act or the TORNADO Act</strong></p><p>This bill requires the National Oceanic and Atmospheric Administration (NOAA) to evaluate and improve its communications about hurricanes, tornadoes, winter storms, and other hazardous weather events.</p><p>Specifically, NOAA must establish a Risk Communication Office to evaluate the effectiveness of NOAA's communications and to identify ways to provide simpler and clearer information to the public about hazardous weather events. NOAA must also (1) establish a research program to modernize its communication systems, and (2) establish a pilot program to implement the research with respect to communications about tornadoes.</p><p>Additionally, the bill requires NOAA to develop a strategic plan for implementing the Warn-on-Forecast System, which aims to provide more advanced warnings of thunderstorm-related events (e.g., tornadoes). The bill also requires NOAA to evaluate its tornado rating system and to conduct post-storm assessments of significant events.</p><p>The bill also provides statutory authority for NOAA's Verification of the Origins of Rotation in Tornadoes Experiment (known as VORTEX-USA), a collaborative project between meteorologists and social scientists to study the conditions that contribute to dangerous tornadoes in the Southeast and the best ways to communicate these events to the public.</p><p>Finally, the Government Accountability Office must report on the National Weather Service's communication technology, particularly with respect to timely notices of hazardous weather events.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119s258"
    },
    "title": "TORNADO Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Tornado Observations Research and Notification Assessment for Development of Operations Act or the TORNADO Act</strong></p><p>This bill requires the National Oceanic and Atmospheric Administration (NOAA) to evaluate and improve its communications about hurricanes, tornadoes, winter storms, and other hazardous weather events.</p><p>Specifically, NOAA must establish a Risk Communication Office to evaluate the effectiveness of NOAA's communications and to identify ways to provide simpler and clearer information to the public about hazardous weather events. NOAA must also (1) establish a research program to modernize its communication systems, and (2) establish a pilot program to implement the research with respect to communications about tornadoes.</p><p>Additionally, the bill requires NOAA to develop a strategic plan for implementing the Warn-on-Forecast System, which aims to provide more advanced warnings of thunderstorm-related events (e.g., tornadoes). The bill also requires NOAA to evaluate its tornado rating system and to conduct post-storm assessments of significant events.</p><p>The bill also provides statutory authority for NOAA's Verification of the Origins of Rotation in Tornadoes Experiment (known as VORTEX-USA), a collaborative project between meteorologists and social scientists to study the conditions that contribute to dangerous tornadoes in the Southeast and the best ways to communicate these events to the public.</p><p>Finally, the Government Accountability Office must report on the National Weather Service's communication technology, particularly with respect to timely notices of hazardous weather events.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119s258"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s258is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s258rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "TORNADO Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Tornado Observations Research and Notification Assessment for Development of Operations Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "title": "TORNADO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TORNADO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T14:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tornado Observations Research and Notification Assessment for Development of Operations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T14:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve forecasting and understanding of tornadoes and other hazardous weather, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T14:18:26Z"
    }
  ]
}
```
