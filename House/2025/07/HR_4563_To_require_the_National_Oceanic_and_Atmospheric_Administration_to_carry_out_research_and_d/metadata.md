# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4563?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4563
- Title: Fixing Gaps in Hurricane Preparedness Act
- Congress: 119
- Bill type: HR
- Bill number: 4563
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2025-09-17T12:17:22Z
- Update date including text: 2025-09-17T12:17:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4563",
    "number": "4563",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Fixing Gaps in Hurricane Preparedness Act",
    "type": "HR",
    "updateDate": "2025-09-17T12:17:22Z",
    "updateDateIncludingText": "2025-09-17T12:17:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:03:05Z",
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4563ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4563\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Mr. Frost (for himself and Mr. Webster of Florida ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo require the National Oceanic and Atmospheric Administration to carry out research and development to improve the understanding of how the public receives, interprets, and responds to and values hurricane forecasts and warnings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fixing Gaps in Hurricane Preparedness Act .\n#### 2. Hurricane social, behavioral, and economic sciences\n##### (a) In general\nThe Administrator of the National Oceanic and Atmospheric Administration (in this section referred to as the Administrator ), in consultation with the Director of the National Science Foundation, shall carry out research and development to improve the understanding of how the public receives, interprets, and responds to and values hurricane forecasts and warnings.\n##### (b) Research and development\nIn conducting the research and development in accordance with subsection (a), the Administrator shall\u2014\n**(1)**\nconduct a comprehensive review of what is known about how the public receives, interprets, and responds to and makes decisions regarding hurricane forecasts and warnings, including\u2014\n**(A)**\nhow the connections between weather observations, downstream models, and processes affect the decision tools or products derived from such hurricane forecasts and warnings;\n**(B)**\nhow such hurricane forecasts and warnings generated by decision tools and products are used by emergency managers, governments, and other users to benefit the public and stakeholder groups;\n**(C)**\nhow past experiences with hurricanes impacts decision making;\n**(D)**\nhow the source of such hurricane forecasts and warnings affects interpretation;\n**(E)**\nhow tropical cyclone warnings and watches are received and interpreted;\n**(F)**\nhow understanding of and response to such hurricane forecasts and warnings vary across demographic groups, including the elderly, people with disabilities, and other vulnerable populations;\n**(G)**\nlanguage barriers; and\n**(H)**\nhow understanding and response to such hurricane forecasts and warnings varies across geographic areas, including rural, urban, and suburban;\n**(2)**\nidentify data gaps based on the review conducted pursuant to paragraph (1);\n**(3)**\ntaking into the account the data gaps identified pursuant to paragraph (2), carry out social and behavioral research, including data collection, to improve the understanding of how the public, including vulnerable populations, receive, interpret, and respond to hurricane forecasts and warnings and to inform evidence-based updates to existing hurricane forecasts and warnings;\n**(4)**\ncarry out research, including data collection, to evaluate and quantify the economic value of extending lead times of tropical cyclone warnings and watches, including to vulnerable populations;\n**(5)**\nidentify affected populations and gather data to conduct baseline assessments;\n**(6)**\nconduct retrospective assessments of previous hurricane forecasts and warnings and improvements to better understand the key components of the value of the forecasts and warnings provided;\n**(7)**\nconduct ex ante assessments based on potential forecasts and warnings improvements and expected actions or behavior changes;\n**(8)**\nconduct cost benefit analysis of forecasts and warnings improvement alternatives;\n**(9)**\nconduct risk assessments for pre-, during, and post-storm periods in regions and communities with significant elderly populations, including retirement communities;\n**(10)**\nestablish policies and procedures for the collection, archiving, and stewardship of data on community response, including the response of vulnerable populations, to high-impact tropical systems; and\n**(11)**\nintegrate and consider research and development described in this subsection in the development or enhancement of hurricane products, information, and services.\n##### (c) Pilot study\n**(1) In general**\nNot later than 180 days, the Administrator shall seek to enter into an agreement with an appropriate entity, as determined by the Administrator, to conduct a pilot study using a mixed methods approach, such as surveys, focus groups, and interviews, to gather information from hurricane prone population areas regarding their levels of preparedness for hurricanes. The surveys shall evaluate the following:\n**(A)**\nPossession of disaster supplies.\n**(B)**\nEvacuation decisions.\n**(C)**\nLevels of trust of tropical cyclone information from various sources.\n**(D)**\nAccess to tropical cyclone warnings in a survey participant\u2019s first language.\n**(E)**\nDetermination regarding a survey participant\u2019s reasoning that may hinder the ability of such a participant to evacuate or willingness to evacuate.\n**(F)**\nAny additional information the Administrator determines necessary.\n**(2) Additional criteria**\nThe pilot study described in paragraph (1) shall define its methodology and be made publicly available on a website of the National Oceanic and Atmospheric Administration.",
      "versionDate": "2025-07-21",
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
        "updateDate": "2025-09-17T12:17:22Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4563ih.xml"
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
      "title": "Fixing Gaps in Hurricane Preparedness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fixing Gaps in Hurricane Preparedness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the National Oceanic and Atmospheric Administration to carry out research and development to improve the understanding of how the public receives, interprets, and responds to and values hurricane forecasts and warnings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:51Z"
    }
  ]
}
```
