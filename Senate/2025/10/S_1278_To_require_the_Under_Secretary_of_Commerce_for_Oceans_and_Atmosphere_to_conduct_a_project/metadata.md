# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1278?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1278
- Title: Fog Observations and Geographic Forecasting Act
- Congress: 119
- Bill type: S
- Bill number: 1278
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-02-04T05:06:16Z
- Update date including text: 2026-02-04T05:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-86.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-86.
- 2025-10-21 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 197.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-86.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-86.
- 2025-10-21 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 197.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1278",
    "number": "1278",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "Fog Observations and Geographic Forecasting Act",
    "type": "S",
    "updateDate": "2026-02-04T05:06:16Z",
    "updateDateIncludingText": "2026-02-04T05:06:16Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 197.",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-86.",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-86.",
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
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
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
            "date": "2025-10-21T20:00:32Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-30T14:00:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-03T16:06:49Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1278is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1278\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Cruz (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Under Secretary of Commerce for Oceans and Atmosphere to conduct a project to improve forecasts of coastal marine fog, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fog Observations and Geographic Forecasting Act .\n#### 2. Project to improve forecasts of coastal marine fog\n##### (a) In general\nThe Under Secretary of Commerce for Oceans and Atmosphere shall conduct a project to improve forecasts of coastal marine fog.\n##### (b) Goal\nThe goal of the project required under subsection (a) is to enhance vessel safety and reduce the economic impact of coastal marine fog events, with a focus on\u2014\n**(1)**\nincreasing the number of marine-based observations through additional Federal platforms and commercially acquired observations in locations where impacts from marine fog and reduced visibility have major safety and economic impacts, including through the use of\u2014\n**(A)**\nbuoys;\n**(B)**\nmeteorological stations measuring visibility, temperature, dewpoint, and wind speed and direction as a stand-alone or co-located with water level sensors, such as those that are part of the physical oceanographic observation system program of the National Oceanic and Atmospheric Administration;\n**(C)**\nstationary platforms or drifting instruments;\n**(D)**\nvessels;\n**(E)**\nunmanned systems;\n**(F)**\nremote sensing technologies, including rapid refresh hyperspectral satellite imagery; and\n**(G)**\nadvanced algorithms that extract actionable information from observational data, including early detection and regular monitoring of marine fog;\n**(2)**\nadvancing geographic coverage, resolution, skill, and accuracy of marine fog modeling, including, when feasible, additional locations and advancements in marine channel forecast capability;\n**(3)**\nimproving communication of marine fog advisories by the National Oceanic and Atmospheric Administration;\n**(4)**\ncommunicating risks posed by hazardous marine fog events in a way that maximizes informed decision making by the public; and\n**(5)**\nproviding decision support services based on environmental information that is actionable to the recipient of a marine fog advisory.\n##### (c) Stakeholder engagement\nIn implementing the project required under subsection (a), the Under Secretary shall meet with public and private stakeholders regarding the planning, development, and implementation of the project.\n##### (d) Tribal engagement\nThe Under Secretary shall meet with Indian tribes (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) regarding the planning, development, and implementation of the project required under subsection (a).\n##### (e) Project plan\nNot later than one year after the date of the enactment of this Act, the Under Secretary shall develop a plan for the project required under subsection (a) that details the specific research, development, and technology transfer activities, as well as corresponding resources and timelines, necessary to achieve the goal set forth under subsection (b).",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1278rs.xml",
      "text": "II\nCalendar No. 197\n119th CONGRESS\n1st Session\nS. 1278\n[Report No. 119\u201386]\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Cruz (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nOctober 21, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo require the Under Secretary of Commerce for Oceans and Atmosphere to conduct a project to improve forecasts of coastal marine fog, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fog Observations and Geographic Forecasting Act .\n#### 2. Project to improve forecasts of coastal marine fog\n##### (a) In general\nThe Under Secretary of Commerce for Oceans and Atmosphere shall conduct a project to improve forecasts of coastal marine fog.\n##### (b) Goal\nThe goal of the project required under subsection (a) is to enhance vessel safety and reduce the economic impact of coastal marine fog events, with a focus on\u2014\n**(1)**\nincreasing the number of marine-based observations through additional Federal platforms and commercially acquired observations in locations where impacts from marine fog and reduced visibility have major safety and economic impacts, including through the use of\u2014\n**(A)**\nbuoys;\n**(B)**\nmeteorological stations measuring visibility, temperature, dewpoint, and wind speed and direction as a stand-alone or co-located with water level sensors, such as those that are part of the physical oceanographic observation system program of the National Oceanic and Atmospheric Administration;\n**(C)**\nstationary platforms or drifting instruments;\n**(D)**\nvessels;\n**(E)**\nunmanned systems;\n**(F)**\nremote sensing technologies, including rapid refresh hyperspectral satellite imagery; and\n**(G)**\nadvanced algorithms that extract actionable information from observational data, including early detection and regular monitoring of marine fog;\n**(2)**\nadvancing geographic coverage, resolution, skill, and accuracy of marine fog modeling, including, when feasible, additional locations and advancements in marine channel forecast capability;\n**(3)**\nimproving communication of marine fog advisories by the National Oceanic and Atmospheric Administration;\n**(4)**\ncommunicating risks posed by hazardous marine fog events in a way that maximizes informed decision making by the public; and\n**(5)**\nproviding decision support services based on environmental information that is actionable to the recipient of a marine fog advisory.\n##### (c) Stakeholder engagement\nIn implementing the project required under subsection (a), the Under Secretary shall meet with public and private stakeholders regarding the planning, development, and implementation of the project.\n##### (d) Tribal engagement\nThe Under Secretary shall meet with Indian tribes (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) regarding the planning, development, and implementation of the project required under subsection (a).\n##### (e) Project plan\nNot later than one year after the date of the enactment of this Act, the Under Secretary shall develop a plan for the project required under subsection (a) that details the specific research, development, and technology transfer activities, as well as corresponding resources and timelines, necessary to achieve the goal set forth under subsection (b).",
      "versionDate": "2025-10-21",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-06-11",
        "text": "Ordered to be Reported by the Yeas and Nays: 35 - 0."
      },
      "number": "3705",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fog Observations and Geographic Forecasting Act",
      "type": "HR"
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
            "updateDate": "2025-06-12T20:19:28Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-06-12T20:19:40Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-06-12T20:22:26Z"
          },
          {
            "name": "Hydrology and hydrography",
            "updateDate": "2025-06-12T20:22:16Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2025-06-12T20:19:10Z"
          },
          {
            "name": "Navigation, waterways, harbors",
            "updateDate": "2025-06-12T20:19:18Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-06-12T20:19:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-02T15:35:38Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1278is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1278rs.xml"
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
      "title": "Fog Observations and Geographic Forecasting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:15Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Fog Observations and Geographic Forecasting Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fog Observations and Geographic Forecasting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Under Secretary of Commerce for Oceans and Atmosphere to conduct a project to improve forecasts of coastal marine fog, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:21Z"
    }
  ]
}
```
