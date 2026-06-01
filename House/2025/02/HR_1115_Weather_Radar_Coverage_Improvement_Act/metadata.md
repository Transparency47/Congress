# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1115?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1115
- Title: Weather Radar Coverage Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 1115
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-02-04T04:26:32Z
- Update date including text: 2026-02-04T04:26:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1115",
    "number": "1115",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001087",
        "district": "1",
        "firstName": "Eric",
        "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
        "lastName": "Crawford",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Weather Radar Coverage Improvement Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:32Z",
    "updateDateIncludingText": "2026-02-04T04:26:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:04:40Z",
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
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1115ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1115\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Crawford (for himself and Mr. Moran ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo develop the next generation of weather radar, authorize supplemental gap radar coverage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Weather Radar Coverage Improvement Act\n#### 2. Next generation phased array radar\n##### (a) In general\nThe Under Secretary, in consultation with the Director of the National Weather Service, shall develop a plan to replace the Next Generation Weather Radar of the National Weather Service ( NEXRAD ) system in existence as of the date of the enactment of this section.\n##### (b) Procurement deadline\nThe Under Secretary shall take such actions as may be necessary to ensure the replacement described in subsection (a) is completed by not later than September 30, 2040.\n##### (c) Elements\nThe plan developed pursuant to subsection (a) shall include the following:\n**(1)**\nEstimates of quantifiable improvements in coverage and accuracy to be made from replacement of the NEXRAD system referred to in such subsection.\n**(2)**\nDevelopment of a prototype digital phased array radar to test and determine the specifications and requirements for such replacement.\n**(3)**\nEstablishment of a weather surveillance phased array radar testbed for the following:\n**(A)**\nEvaluation of commercial radars with the potential to replace or supplement the NEXRAD system.\n**(B)**\nProviding technical assistance for the use of small, gap filling radars in regions where geographical topography prevents full utilization of larger systems.\n**(4)**\nConsultation and input solicited from meteorologists, emergency managers, and public safety officials regarding the specifications and requirements for replacement of the NEXRAD system referred in such subsection.\n##### (d) Radar-as-a-Service\n**(1) In general**\nIn order to supplement gaps in radar coverage in existence as of the date of the enactment of this section and ensure the continued performance of weather radar capabilities, the Director of the National Weather Service may utilize and contract with third party entities to fill such radar gaps using diverse weather radars and data assimilation technologies to better detect significant precipitation and severe weather over a greater area across the population.\n**(2) Priority**\nIn carrying out the activities under paragraph (1), the Director of the National Weather Service shall prioritize utilizing and contracting with third party entities that have participated in the testbed established in accordance with subsection (c)(3).\n**(3) Weather camera systems**\nIn carrying out the activities under paragraph (1), the Director of the National Weather Service may consider weather camera systems and services as viable technologies to supplement gaps in radar coverage.\n##### (e) Updates to Congress\nThe Under Secretary shall provide to the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate periodic updates on the implementation of this section.\n##### (f) Definition\nIn this section, the term Under Secretary has the meaning given such term in section 2 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 ).",
      "versionDate": "2025-02-07",
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
        "updateDate": "2025-03-12T12:53:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
    "originChamber": "House",
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
          "measure-id": "id119hr1115",
          "measure-number": "1115",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2025-03-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1115v00",
            "update-date": "2025-03-28"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Weather Radar Coverage Improvement Act</strong></p><p>This bill requires the National Oceanic and Atmospheric Administration to develop a plan to replace the Next Generation Weather Radar (NEXRAD) system of the National Weather Service by September 30, 2040. (The NEXRAD system is a network of weather radars used to detect precipitation and wind.)</p><p>Under the bill, the plan must incorporate certain elements, including estimates of improvements to coverage and accuracy made possible by replacement of the system\u00a0and an evaluation of the potential use of commercial radars to replace or supplement the system.\u00a0</p><p>The bill also authorizes the National Weather Service to contract with third parties to fill gaps in radar coverage so as to better detect significant weather events over a larger area.\u00a0</p>"
        },
        "title": "Weather Radar Coverage Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1115.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Weather Radar Coverage Improvement Act</strong></p><p>This bill requires the National Oceanic and Atmospheric Administration to develop a plan to replace the Next Generation Weather Radar (NEXRAD) system of the National Weather Service by September 30, 2040. (The NEXRAD system is a network of weather radars used to detect precipitation and wind.)</p><p>Under the bill, the plan must incorporate certain elements, including estimates of improvements to coverage and accuracy made possible by replacement of the system\u00a0and an evaluation of the potential use of commercial radars to replace or supplement the system.\u00a0</p><p>The bill also authorizes the National Weather Service to contract with third parties to fill gaps in radar coverage so as to better detect significant weather events over a larger area.\u00a0</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119hr1115"
    },
    "title": "Weather Radar Coverage Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Weather Radar Coverage Improvement Act</strong></p><p>This bill requires the National Oceanic and Atmospheric Administration to develop a plan to replace the Next Generation Weather Radar (NEXRAD) system of the National Weather Service by September 30, 2040. (The NEXRAD system is a network of weather radars used to detect precipitation and wind.)</p><p>Under the bill, the plan must incorporate certain elements, including estimates of improvements to coverage and accuracy made possible by replacement of the system\u00a0and an evaluation of the potential use of commercial radars to replace or supplement the system.\u00a0</p><p>The bill also authorizes the National Weather Service to contract with third parties to fill gaps in radar coverage so as to better detect significant weather events over a larger area.\u00a0</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119hr1115"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1115ih.xml"
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
      "title": "Weather Radar Coverage Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Weather Radar Coverage Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To develop the next generation of weather radar, authorize supplemental gap radar coverage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T04:19:38Z"
    }
  ]
}
```
