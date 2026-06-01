# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3705
- Title: Fog Observations and Geographic Forecasting Act
- Congress: 119
- Bill type: HR
- Bill number: 3705
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2025-12-18T09:07:13Z
- Update date including text: 2025-12-18T09:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-06-11 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-11 - Committee: Ordered to be Reported by the Yeas and Nays: 35 - 0.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-06-11 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-11 - Committee: Ordered to be Reported by the Yeas and Nays: 35 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3705",
    "number": "3705",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "Fog Observations and Geographic Forecasting Act",
    "type": "HR",
    "updateDate": "2025-12-18T09:07:13Z",
    "updateDateIncludingText": "2025-12-18T09:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
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
      "text": "Ordered to be Reported by the Yeas and Nays: 35 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-04",
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
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
            "date": "2025-06-11T14:10:50Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-04T14:02:00Z",
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
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
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
      "sponsorshipDate": "2025-06-17",
      "state": "VA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3705ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3705\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Babin (for himself and Ms. Lofgren ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo require the Under Secretary of Commerce for Oceans and Atmosphere to conduct a project to improve forecasts of coastal marine fog, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fog Observations and Geographic Forecasting Act .\n#### 2. Project to improve forecasts of coastal marine fog\n##### (a) In general\nThe Under Secretary of Commerce for Oceans and Atmosphere shall conduct a project to improve forecasts of coastal marine fog.\n##### (b) Goal\nThe goal of the project required under subsection (a) is to enhance vessel safety and reduce the economic impact of coastal marine fog events, with a focus on\u2014\n**(1)**\nincreasing the number of marine-based observations through additional Federal platforms and commercially acquired observations in locations where impacts from marine fog and reduced visibility have major safety and economic impacts, including through the use of\u2014\n**(A)**\nbuoys;\n**(B)**\nmeteorological stations measuring visibility, temperature, dewpoint, and wind speed and direction as a stand-alone or co-located with water level sensors, such as those that are part of the physical oceanographic observation system program of the National Oceanic and Atmospheric Administration;\n**(C)**\nstationary platforms or drifting instruments;\n**(D)**\nvessels;\n**(E)**\nunmanned systems;\n**(F)**\nremote sensing technologies, including rapid refresh hyperspectral satellite imagery; and\n**(G)**\nadvanced algorithms that extract actionable information from observational data, including early detection and regular monitoring of marine fog;\n**(2)**\nadvancing geographic coverage, resolution, skill, and accuracy of marine fog modeling, including, when feasible, additional locations and advancements in marine channel forecast capability;\n**(3)**\nimproving communication of marine fog advisories by the National Oceanic and Atmospheric Administration;\n**(4)**\ncommunicating risks posed by hazardous marine fog events in a way that maximizes informed decision making by the public; and\n**(5)**\nproviding decision support services based on environmental information that is actionable to the recipient of a marine fog advisory.\n##### (c) Stakeholder engagement\nIn implementing the project required under subsection (a), the Under Secretary shall meet with public and private stakeholders regarding the planning, development, and implementation of the project.\n##### (d) Tribal engagement\nThe Under Secretary shall meet with Indian tribes (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) regarding the planning, development, and implementation of the project required under subsection (a).\n##### (e) Project plan\nNot later than one year after the date of the enactment of this Act, the Under Secretary shall develop a plan for the project required under subsection (a) that details the specific research, development, and technology transfer activities, as well as corresponding resources and timelines, necessary to achieve the goal set forth under subsection (b).",
      "versionDate": "2025-06-04",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-21",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 197."
      },
      "number": "1278",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fog Observations and Geographic Forecasting Act",
      "type": "S"
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
            "updateDate": "2025-06-12T20:23:00Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-06-12T20:23:00Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-06-12T20:23:00Z"
          },
          {
            "name": "Hydrology and hydrography",
            "updateDate": "2025-06-12T20:23:00Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2025-06-12T20:23:00Z"
          },
          {
            "name": "Navigation, waterways, harbors",
            "updateDate": "2025-06-12T20:23:00Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-06-12T20:23:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-14T18:20:43Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3705ih.xml"
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
      "title": "Fog Observations and Geographic Forecasting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fog Observations and Geographic Forecasting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Under Secretary of Commerce for Oceans and Atmosphere to conduct a project to improve forecasts of coastal marine fog, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T08:18:26Z"
    }
  ]
}
```
