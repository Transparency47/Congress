# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2295?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2295
- Title: WING Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2295
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2025-04-04T16:51:10Z
- Update date including text: 2025-04-04T16:51:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2295",
    "number": "2295",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "WING Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-04T16:51:10Z",
    "updateDateIncludingText": "2025-04-04T16:51:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:00:40Z",
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
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "OK"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CO"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "AS"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "GU"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2295ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2295\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Feenstra (for himself, Mrs. Bice , Mr. Neguse , Mr. Haridopolos , Mrs. Radewagen , Mrs. Miller-Meeks , Mr. Fitzpatrick , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo research the impact of obstructions on radar detection and prediction capabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Weather Innovation for the Next Generation Act of 2025 or the WING Act of 2025 .\n#### 2. Radar obstruction Research, Development, Test, and Evaluation Program\n##### (a) Establishment\nThe Director of the National Weather Service, in coordination with the Assistant Administrator for Oceanic and Atmospheric Research, shall establish a Research, Development, Test, and Evaluation Program (in this section referred to as the Program ) to ensure the continued performance of weather radar detection and prediction capabilities with physical obstructions in the line of sight of such radar.\n##### (b) Requirements\nIn carrying out the Program, the Director, in consultation with the Interagency Council for Advancing Meteorological Services, shall\u2014\n**(1)**\npartner with industry, academia, Federal, State, and local government entities, and any other entity the Director considers appropriate;\n**(2)**\nidentify and test existing or near-commercial technologies and solutions that mitigate the potential impact of obstructions on weather radar;\n**(3)**\nresearch additional solutions that could mitigate the effects of an obstruction on weather radar, including\u2014\n**(A)**\nsignal processing algorithms;\n**(B)**\nshort-term forecasting algorithms to replace contaminated data; and\n**(C)**\nthe use of dual polarization characteristics in mitigating the effects of wind turbines on weather radar; and\n**(4)**\ndevelop commercially viable technical mitigation solutions for obstructions to weather radar capabilities.\n##### (c) Priority\nIn carrying out the requirements described in subsection (b), the Director shall prioritize consideration of the following technology-based mitigation solutions:\n**(1)**\nMultifunction phased array radar.\n**(2)**\nThe replacement of contaminated data with commercial radar data.\n**(3)**\nThe utilization of data from private-sector-associated meteorological towers.\n**(4)**\nProviding wind farm boundaries and consolidated wind farm areas to display on local forecasting equipment.\n**(5)**\nInstalling and providing access to rain gauges.\n**(6)**\nAny other technology-based mitigation solution the Director determines could overcome beam blockage or ghost echoes.\n##### (d) Termination\nThe authority of the Director to carry out the Program shall terminate on the earlier of\u2014\n**(1)**\nSeptember 30, 2030; or\n**(2)**\none year after date on which the final recommendation required by subsection (e)(2) is submitted by the Director.\n##### (e) Report; recommendation\n**(1) In general**\nNot later than two years after the date of the enactment of this section and annually thereafter until the Program terminates pursuant to subsection (d), the Director shall submit to Congress a report on the implementation of the Program, including an evaluation of each technology-based mitigation solution identified for priority consideration pursuant to subsection (c), and a recommendation regarding additional identification and testing of new technologies based on such consideration.\n**(2) Final recommendation**\nNot later than five years after the date of the enactment of this section, the Director shall provide to Congress a recommendation on whether additional research, testing, and development through the Program established under subsection (a) is needed, and a determination of whether a cessation of field research, development, testing, and evaluation is appropriate.\n##### (f) Definitions\nIn this section:\n**(1) Beam blockage**\nThe term beam blockage means a signal that is partially or fully blocked due to an obstruction.\n**(2) Director**\nThe term Director means the Director of the National Weather Service.\n**(3) Ghost echo**\nThe term ghost echo means radar signal reflectivity or velocity return errors in radar data due to the close proximity of an obstruction.\n**(4) Obstruction**\nThe term obstruction includes\u2014\n**(A)**\na wind turbine that could limit the effectiveness of a weather radar system; and\n**(B)**\nany building that disrupts or limits the effectiveness of a weather radar system.",
      "versionDate": "2025-03-24",
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
        "updateDate": "2025-04-04T16:51:10Z"
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
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2295ih.xml"
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
      "title": "WING Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WING Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Weather Innovation for the Next Generation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To research the impact of obstructions on radar detection and prediction capabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:38Z"
    }
  ]
}
```
