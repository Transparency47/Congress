# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7813?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7813
- Title: NOAA Weather Radio Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 7813
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-05-27T15:35:28Z
- Update date including text: 2026-05-27T15:35:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7813",
    "number": "7813",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001291",
        "district": "36",
        "firstName": "Brian",
        "fullName": "Rep. Babin, Brian [R-TX-36]",
        "lastName": "Babin",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "NOAA Weather Radio Modernization Act",
    "type": "HR",
    "updateDate": "2026-05-27T15:35:28Z",
    "updateDateIncludingText": "2026-05-27T15:35:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
        "item": [
          {
            "date": "2026-03-18T14:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-05T15:02:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NE"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "OK"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7813ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7813\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Mr. Babin (for himself, Mr. Flood , Mr. Sorensen , Mrs. Bice , and Mr. Amo ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the Weather Research and Forecasting Innovation Act of 2017 to require the Under Secretary of Commerce for Oceans and Atmosphere to expand and modernize the weather radio system of the National Oceanic and Atmospheric Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NOAA Weather Radio Modernization Act .\n#### 2. NOAA Weather Radio\n##### (a) In general\nThe Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 et seq. ) is amended by adding at the end the following new title:\nVII NOAA Weather Radio 701. NOAA Weather Radio (a) In general The Under Secretary shall establish or maintain a nationwide weather radio network, to be known as NOAA Weather Radio , that\u2014 (1) broadcasts weather information, including emergency weather watches, warnings, geological hazards, and other hazard information; (2) operates 24 hours a day, 7 days a week; and (3) is resilient to emergency hazards, such as loss of power and cellular service. (b) Coverage and reliability The Under Secretary shall ensure the reliability of NOAA Weather Radio by\u2014 (1) maintaining support for existing systems before new technologies are implemented, especially such systems that serve areas not covered by or having poor quality cellular service; and (2) ensuring consistent maintenance and operations monitoring, with timely repairs to broadcast transmitter site equipment and antennas. (c) Modernization initiative (1) In general To the maximum extent practicable, the Under Secretary shall expand the coverage of and modernize NOAA Weather Radio to ensure it remains valuable to the public, including by\u2014 (A) improving those methods of communicating the risks posed by hazardous weather events to the public that are most likely to result in informed decision-making regarding the mitigation of such risks; (B) improving communication of hazardous weather warnings and the urgency of such warnings, including to areas that experience a high frequency of such warnings; (C) enhancing the ability to amplify non-weather emergency messages for the integrated public alert and warning system (IPAWS) under section 1756 of the Homeland Security Act of 2002 ( 6 U.S.C. 321o\u20131 ) through NOAA Weather Radio, as necessary; (D) acquiring additional transmitters, as determined appropriate, to expand coverage to\u2014 (i) areas at high risk for rapid onset weather disasters that require short-fuse warnings; (ii) communities without\u2014 (I) broadband internet access service (as such term is defined in section 8.1(b) of title 47, Code of Federal Regulations (or a successor regulation)), and as depicted by a map created pursuant to section 802(c)(1)(C) of the Communications Act of 1934 ( 47 U.S.C. 642(c)(1)(C) ); (II) State or local emergency warning systems; or (III) satellite coverage; and (iii) Federal lands, such as land in the National Park System or the National Forest System and National Recreation Areas; (E) adding the capability to disseminate NOAA Weather Radio alerts\u2014 (i) by satellite; or (ii) through\u2014 (I) common internet protocols, such as the Cloud; or (II) other emerging technologies that satisfy the intent of this section. (F) conducting research and development to modernize geographically specific warnings. (2) Elements In carrying out paragraph (1), the Under Secretary shall\u2014 (A) upgrade telecommunications infrastructure of NOAA Weather Radio to accelerate the transition of broadcasts to internet protocol-based communications over non-copper media; (B) accelerate software upgrades to the Advanced Weather Interactive Processing System, or any relevant system successors, in order to implement partial county notifications and alerts; (C) enhance accessibility and usability of data and feeds of NOAA Weather Radio with feedback from relevant stakeholders, including the private sector; (D) develop options, including satellite backup capability and commercial provider partnerships, for continuity of service of NOAA Weather Radio in the event of an outage at a weather forecast office; (E) research and develop alternative options, including microwave capabilities, to transmit NOAA Weather Radio signals to transmitters that are remote or do not have internet protocol capability; (F) transition critical applications to the Integrated Dissemination Program, or any relevant program successors; and (G) work with the General Services Administration, and other relevant agencies, to develop new, alternative, or updated expedited mechanisms to secure priority space capacity, such as leased land and tower space, for NOAA Weather Radio critical infrastructure, including transmitters and antennas, that are best suited for the national security and public safety missions of NOAA Weather Radio. (3) Priority In carrying out paragraph (1), the Under Secretary shall prioritize practices, capabilities, and technologies recommended in accordance with the assessment under subsection (d) to maximize the accessibility of NOAA Weather Radio, particularly in areas of the United States described in subparagraph (D)(i) of such paragraph. (d) Assessment for management and distribution (1) In general Not later than one year after the date of the enactment of this section, the Under Secretary shall complete an assessment of access to NOAA Weather Radio. (2) Elements In conducting the assessment required under paragraph (1), the Under Secretary shall take into consideration and provide to the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate recommendations regarding the following: (A) Input from relevant stakeholders within the weather enterprise, including third-party platforms that provide online services, such as websites and mobile device applications. (B) The manner by which existing or new National Oceanic and Atmospheric Administration management systems may promote consistent, efficient, and compatible access to NOAA Weather Radio. (C) The ability of the National Oceanic and Atmospheric Administration to aggregate real-time broadcast feeds at one or more central locations, as a redundancy to the broadcast feed from the nearest weather forecast office. (D) Effective coordination between agencies with responsibilities relating to emergencies and natural disasters. (E) The potential effects of an electromagnetic pulse or geomagnetic disturbance on NOAA Weather Radio. (e) Definition In this section: (1) Geological hazard The term geological hazard means a tsunami, forest fire, mudflow, volcanic eruption, volcanic ash, landslide, geomagnetic storm, or other similar such hazard. (2) Short-fuse warning The term short-fuse warning means a warning relating to a tornado, severe thunderstorm, or flash flood. (f) Authorization of appropriations There are authorized to be appropriated to the Under Secretary\u2014 (1) for each of fiscal years 2026 through 2031, $20,000,000 to operate NOAA Weather Radio under subsections (a) and (b); and (2) for fiscal year 2026, $100,000,000, which shall remain available until expended, to carry out subsections (c) and (d). .\n##### (b) Weather ready all hazards award program\nSection 407 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8546 ) is\u2014\n**(1)**\ntransferred to title VII of such Act, as added by subsection (a);\n**(2)**\ninserted after section 701 of such Act, as added by subsection (a); and\n**(3)**\nredesignated as section 702.\n##### (c) Clerical amendments\nThe table of contents for the Weather Research and Forecasting Innovation Act of 2017 is amended\u2014\n**(1)**\nby striking the item relating to section 407; and\n**(2)**\nby adding at the end the following new items:\nTitle VII\u2014NOAA Weather Radio Sec. 701. NOAA Weather Radio. Sec. 702. National Oceanic and Atmospheric Administration Weather Ready All Hazards Award Program. .\n#### 3. National standards for weather warning systems in flash flood zones\n##### (a) In general\nThe Under Secretary of Commerce for Standards and Technology, in consultation with the Under Secretary of Commerce for Oceans and Atmosphere, may support the development of standards for flash flood emergency alert systems with respect to a 100-year floodplain (as such term is defined in section 100202(a) of the Biggert-Waters Flood Insurance Reform Act of 2012 ( 42 U.S.C. 4004(a) )).\n##### (b) Requirements\nIf the Under Secretary of Commerce for Standards and Technology supports the development of standards under subsection (a), the Under Secretary shall ensure that such standards\u2014\n**(1)**\nmeet the needs of communities without\u2014\n**(A)**\nbroadband internet access service (as such term is defined in section 8.1(b) of title 47, Code of Federal Regulations (or a successor regulation)) and as depicted by a map created pursuant to section 802(c)(1)(C) of the Communications Act of 1934 ( 47 U.S.C. 642(c)(1)(C) );\n**(B)**\nState or local emergency warning systems; or\n**(C)**\nsatellite coverage; and\n**(2)**\nwill result in reliable flash flood emergency alert systems with respect to a 100-year floodplain referred to in subsection (a), especially during hazardous events.\n##### (c) Report required\nIf the Under Secretary of Commerce for Standards and Technology supports the development of standards under subsection (a), the Under Secretary shall, not later than two years after the date of the enactment of this Act, submit to the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report that includes a summary of such standards.\n#### 4. Classification of and staffing plan for employees\n##### (a) In general\nTitle IV of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8541 et seq. ) is amended by inserting after section 406 the following new section:\n407. Classification of and staffing plan for employees (a) Classification of certain employees (1) In general Not later than 30 days after the date of the enactment of this section, the Under Secretary shall coordinate with the Director of the Office of Management and Budget to categorize each position in the National Oceanographic and Atmospheric Administration specified in paragraph (2) as a protective service occupation under the Standard Occupational Classification System. (2) Positions specified The positions specified in this paragraph are the following occupational positions in the National Oceanic and Atmospheric Administration, as defined by the Director of the Office of Personnel Management: (A) Meteorology Series (1340). (B) Hydrology Series (1315). (C) General Physical Science Series (1301). (D) Electronics Technical Series (0856). (E) Information Technology Management Series (GS\u20132210). (3) Requirements relating to staffing changes The Under Secretary may not carry out any staffing change in any of the occupational positions specified in paragraph (2) unless\u2014 (A) a period of 30 days has passed after the receipt by the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate of a report by the Under Secretary containing a description of the staffing change proposed to be taken and the facts and circumstances relied upon in support of such staffing change; or (B) each such committee before the expiration of such period has transmitted to the Under Secretary written notice to the effect that such committee has no objection to such proposed staffing change. (b) Five-year staffing plan for the National Oceanic and Atmospheric Administration Not later than 180 days after the date of the enactment of this section, the Under Secretary shall submit to Congress a five-year staffing plan for\u2014 (1) the National Weather Service; and (2) any positions within the National Oceanic and Atmospheric Administration that support forecasts and warnings to protect human life and property, including positions that involve\u2014 (A) collection of data for incorporation into watches and warnings; (B) operation and maintenance of equipment for collection of data described in subparagraph (A); (C) maintenance of information technology systems; (D) modeling for forecasts and warnings; and (E) research to improve forecasts, warnings, and communication of such warnings to better protect human life and property. .\n##### (b) Clerical amendment\nThe table of contents for the Weather Research and Forecasting Innovation Act of 2017 is amended by inserting after the item relating to section 406 the following new item:\nSec. 407. Classification of and staffing plan for employee. .\n#### 5. Staffing for positions of public safety at the National Weather Service\n##### (a) Assessment\n**(1) In general**\nNot later than 120 days after the date of the enactment of this Act, the Director of the National Weather Service shall submit to the Under Secretary of Commerce for Oceans and Atmosphere, the Committee on Science, Space, and Technology of the House of Representatives, and the Committee on Commerce, Science, and Transportation of the Senate an assessment of the critical staffing needs of the National Weather Service, including the needs of every Weather Forecast Office and every Center Weather Service Unit.\n**(2) Elements**\nThe assessment under paragraph (1) shall include the following elements:\n**(A)**\nThe number and corresponding occupational series of employees needed to fully staff each Weather Forecast Office and Center Weather Service Unit of the National Weather Service that maximize efficiency while considering the following:\n**(i)**\nSafety.\n**(ii)**\nMorale.\n**(iii)**\nChanging seasonal needs.\n**(iv)**\nForecasting complexity of the geographical area at issue.\n**(B)**\nHistorical staffing needs versus historical vacancies for each such Weather Forecast Office and Center Weather Service Unit.\n##### (b) Direct hire authority\n**(1) In general**\nThe Director of the National Weather Service may appoint, without regard to sections 3308 through 3319, 3327, and 3330 of title 5, United States Code, qualified candidates to any of the following positions to satisfy critical staffing needs and fill vacancies determined in accordance with the assessment under subsection (a):\n**(A)**\nEmployees performing public safety mission functions, including the following:\n**(i)**\nMeteorologists (classification series 1340).\n**(ii)**\nHydrologists (classification series 1315).\n**(iii)**\nGeneral physical scientists (classification series 1301).\n**(iv)**\nComputer specialists (classification series 2210).\n**(v)**\nElectronic technicians (classification series 0856).\n**(B)**\nOther positions for which primary responsibilities include equipment operations, maintenance, analysis, information technology, or engineering.\n**(2) Sunset**\nThe authority under paragraph (1) shall expire on the date on which all positions to satisfy critical staffing needs and vacancies under such paragraph have been filled.",
      "versionDate": "2026-03-05",
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
            "updateDate": "2026-03-30T16:33:03Z"
          },
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2026-03-30T16:32:57Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2026-03-30T16:38:52Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-03-30T16:46:14Z"
          },
          {
            "name": "News media and reporting",
            "updateDate": "2026-03-30T16:39:05Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-03-30T16:39:22Z"
          },
          {
            "name": "Spacecraft and satellites",
            "updateDate": "2026-03-30T16:39:16Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-03-30T16:46:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-03-09T19:39:56Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7813ih.xml"
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
      "title": "NOAA Weather Radio Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T11:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NOAA Weather Radio Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-06T11:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Weather Research and Forecasting Innovation Act of 2017 to require the Under Secretary of Commerce for Oceans and Atmosphere to expand and modernize the weather radio system of the National Oceanic and Atmospheric Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-06T11:03:31Z"
    }
  ]
}
```
