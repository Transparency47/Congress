# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2583?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2583
- Title: NOAA Weather Radio Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 2583
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-18T19:10:31Z
- Update date including text: 2025-09-18T19:10:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2583",
    "number": "2583",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "NOAA Weather Radio Modernization Act",
    "type": "S",
    "updateDate": "2025-09-18T19:10:31Z",
    "updateDateIncludingText": "2025-09-18T19:10:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
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
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T17:47:22Z",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "WA"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "AK"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "HI"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "KS"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2583is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2583\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Cruz (for himself, Ms. Cantwell , Mr. Sullivan , Mr. Schatz , Mr. Moran , and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Under Secretary of Commerce for Oceans and Atmosphere to expand and modernize the weather radio system of the National Oceanic and Atmospheric Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NOAA Weather Radio Modernization Act .\n#### 2. NOAA Weather Radio\n##### (a) In general\nThe Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 et seq. ) is amended by adding at the end the following:\nVII NOAA Weather Radio 701. NOAA Weather Radio (a) In general The Under Secretary shall establish or maintain a nationwide weather radio network, to be known as NOAA Weather Radio , that\u2014 (1) broadcasts weather information, including emergency weather watches, warnings, and other hazard information; (2) operates 24 hours a day, 7 days a week; and (3) is resilient to emergency hazards, such as loss of power and cellular service. (b) Coverage and reliability The Under Secretary shall ensure the reliability of NOAA Weather Radio by\u2014 (1) maintaining support for existing systems, especially those serving areas not covered by or having poor quality cellular service; and (2) ensuring consistent maintenance and operations monitoring, with timely repairs to broadcast transmitter site equipment and antennas. (c) Modernization initiative (1) In general To the maximum extent practicable, the Under Secretary shall expand the coverage of and modernize NOAA Weather Radio to ensure it remains valuable to the public, including by\u2014 (A) improving those methods of communicating the risks posed by hazardous weather events to the public that are most likely to result in informed decisionmaking regarding the mitigation of such risks; (B) improving communication of hazardous weather warnings and the urgency of such warnings to areas that experience a high frequency of such warnings; (C) enhancing the ability to amplify non-weather emergency messages through NOAA Weather Radio as necessary; (D) acquiring additional transmitters as required to expand coverage to\u2014 (i) areas at high risk for rapid onset weather disasters that require short-fuse warnings; (ii) communities without\u2014 (I) mobile broadband internet access service (as defined in section 8.1(b) of title 47, Code of Federal Regulations (or a successor regulation)) and as depicted by a map created under section 802(c)(1)(C) of the Communications Act of 1934 ( 47 U.S.C. 642(c)(1)(C) ); (II) State or local emergency warning systems; or (III) satellite coverage; and (iii) Federal lands, such as land in the National Park System or the National Forest System and National Recreation Areas; (E) adding the capability to disseminate NOAA Weather Radio alerts by satellite or through the cloud; and (F) modernizing the messaging system to enable more geographically specific warnings. (2) Elements In carrying out paragraph (1), the Under Secretary shall\u2014 (A) upgrade telecommunications infrastructure of NOAA Weather Radio to accelerate the transition of broadcasts to internet protocol-based communications over non-copper media; (B) accelerate software upgrades to the Advanced Weather Interactive Processing System, or any relevant system successors, in order to implement partial county notifications and alerts; (C) enhance accessibility and usability of data and feeds of NOAA Weather Radio with feedback from relevant stakeholders, including the private sector; (D) develop options, including satellite backup capability and commercial provider partnerships, for continuity of service of NOAA Weather Radio in the event of an outage at a weather forecast office; (E) research and develop alternative options to transmit NOAA Weather Radio signals to transmitters that are remote or do not have internet protocol capability; (F) transition critical applications to the Integrated Dissemination Program, or any relevant program successors; and (G) work with the General Services Administration, and other relevant agencies, to develop new, alternative, or updated expedited mechanisms to secure priority space capacity, such as leased land and tower space, for NOAA Weather Radio transmitters and antennas that are best suited for the national security and public safety missions of NOAA Weather Radio. (3) Priority In carrying out paragraph (1), the Under Secretary shall prioritize practices, capabilities, and technologies recommended in accordance with the assessment under subsection (d) to maximize the accessibility of NOAA Weather Radio, particularly in areas of the United States described in paragraph (1)(D)(i). (d) Assessment for management and distribution (1) In general Not later than one year after the date of the enactment of this section, the Under Secretary shall complete an assessment of access to NOAA Weather Radio. (2) Elements In conducting the assessment required under paragraph (1), the Under Secretary shall take into consideration and provide recommendations regarding the following: (A) The need for continuous, adequate, and operational real-time broadcasts of NOAA Weather Radio. (B) Input from relevant stakeholders that provide access to NOAA Weather Radio, including third-party platforms that provide online services, such as websites and mobile device applications. (C) The manner by which existing or new management systems may promote consistent, efficient, and compatible access to NOAA Weather Radio. (D) The ability of the National Oceanic and Atmospheric Administration to aggregate real-time broadcast feeds at one or more central locations, as a redundancy to the broadcast feed from the nearest weather forecast office. (E) Effective coordination between agencies with responsibilities relating to emergencies and natural disasters. (F) The potential effects of an electromagnetic pulse or geomagnetic disturbance on NOAA Weather Radio. (e) Authorization of appropriations There are authorized to be appropriated to the Under Secretary\u2014 (1) for each of fiscal years 2026 through 2031, $25,000,000 to operate NOAA Weather Radio under subsections (a) and (b); and (2) for fiscal year 2026, $100,000,000, which shall remain available until expended, to carry out subsections (c) and (d). .\n##### (b) Weather ready all hazards award program\nSection 407 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8546 ) is\u2014\n**(1)**\ntransferred to title VII of that Act, as added by subsection (a);\n**(2)**\ninserted after section 701 of that Act, as added by subsection (a); and\n**(3)**\nredesignated as section 702.\n##### (c) Clerical amendments\nThe table of contents for the Weather Research and Forecasting Innovation Act of 2017 is amended\u2014\n**(1)**\nby striking the item relating to section 407; and\n**(2)**\nby adding at the end the following:\nTITLE VII\u2014NOAA Weather Radio Sec. 701. NOAA Weather Radio. Sec. 702. National Oceanic and Atmospheric Administration Weather Ready All Hazards Award Program. .\n#### 3. National standards for weather warning systems in flash flood zones\n##### (a) In general\nThe Under Secretary of Commerce for Standards and Technology, in consultation with the Under Secretary of Commerce for Oceans and Atmosphere, shall develop standards for flash flood emergency alert systems within the 100-year floodplain (as defined in section 100202(a) of the Biggert-Waters Flood Insurance Reform Act of 2012 ( 42 U.S.C. 4004(a) )).\n##### (b) Requirements\nThe Director shall ensure that standards developed under subsection (a)\u2014\n**(1)**\nmeet the needs of communities without\u2014\n**(A)**\nmobile broadband internet access service (as defined in section 8.1(b) of title 47, Code of Federal Regulations (or a successor regulation)) and as depicted by a map created under section 802(c)(1)(C) of the Communications Act of 1934 ( 47 U.S.C. 642(c)(1)(C) );\n**(B)**\nState or local emergency warning systems; or\n**(C)**\nsatellite coverage; and\n**(2)**\nwill result in reliable systems, especially during hazardous events.\n##### (c) Report required\nNot later than 2 years after the date of the enactment of this Act, the Under Secretary of Commerce for Standards and Technology shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a report that includes a summary of the standards developed under subsection (a).\n#### 4. Classification of and staffing plan for employees and protection from hiring freezes\n##### (a) In general\nTitle IV of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8541 et seq. ) is amended by adding at the end the following:\n415. Classification of and staffing plan for employees and protection from hiring freezes (a) Classification of certain employees (1) In general Not later than 30 days after the date of the enactment of this section, the Director of the Office of Management and Budget shall categorize each position in the National Oceanographic and Atmospheric Administration specified in paragraph (2) as a protective service occupation under the Standard Occupational Classification System. (2) Positions specified The positions specified in this paragraph are the following positions in the National Oceanic and Atmospheric Administration, as defined by the Director of the Office of Personnel Management: (A) Meteorology Series (1340). (B) Hydrology Series (1315). (C) General Physical Science Series (1301). (D) Oceanographer Series (1360). (E) Electronics Technical Series (0856). (F) Information Technology Management Series (GS\u20132210). (G) Professional Mariners (as defined in section 269B of the National Oceanic and Atmospheric Administration Commissioned Officer Corps Act of 2002 ( 33 U.S.C. 3079b )) who are involved in the collection of data to support forecasts and warnings to protect human life and property (including Series 0865, 9901, 9916, 9920, 9923\u201324, 9927\u201328, 9931\u201334, 9944, 9954, 9960, 9965, 9968, 9971, 9973, and 9984). (b) 10-Year staffing plan for the National Oceanic and Atmospheric Administration Not later than 180 days after the date of the enactment of this section, the Under Secretary shall submit to Congress a 10-year staffing plan for\u2014 (1) the National Weather Service; and (2) any positions within the National Oceanic and Atmospheric Administration that support forecasts and warnings to protect human life and property, including positions that involve\u2014 (A) collection of data for incorporation into watches and warnings; (B) operation and maintenance of equipment for collection of data described in subparagraph (A); (C) maintenance of information technology systems; (D) modeling for forecasts and warnings; and (E) research to improve forecasts, warnings, and communication of those warnings to better protect human life and property. .\n##### (b) Clerical amendment\nThe table of contents for the Weather Research and Forecasting Innovation Act of 2017 is amended by inserting after the item relating to section 414 the following:\nSec. 415. Classification of and staffing plan for employees and protection from hiring freezes. .",
      "versionDate": "2025-07-31",
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
        "updateDate": "2025-09-18T19:10:31Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2583is.xml"
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
      "title": "NOAA Weather Radio Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NOAA Weather Radio Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Under Secretary of Commerce for Oceans and Atmosphere to expand and modernize the weather radio system of the National Oceanic and Atmospheric Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:30Z"
    }
  ]
}
```
