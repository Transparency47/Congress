# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3809?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3809
- Title: Weather Workforce Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 3809
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2025-11-18T09:05:28Z
- Update date including text: 2025-11-18T09:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3809",
    "number": "3809",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Weather Workforce Improvement Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:28Z",
    "updateDateIncludingText": "2025-11-18T09:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:01:15Z",
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
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "OK"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "IL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "FL"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NC"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "KS"
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
      "sponsorshipDate": "2025-07-17",
      "state": "VA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3809ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3809\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Flood (for himself, Mr. Lucas , Mr. Panetta , Mr. Sorensen , and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo waive certain legal requirements to permit the Director of the National Weather Service to expeditiously hire for positions that are critical for public safety, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Weather Workforce Improvement Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\naccurate and timely weather forecasting is of vital importance;\n**(2)**\nemployees of the National Weather Service, particularly employees responsible for the regular launching of weather balloons, are critical for public safety; and\n**(3)**\nstaffing positions relating to the regular launching of weather balloons should be prioritized and categorized as critical for public safety.\n#### 3. Staffing for positions of public safety at the National Weather Service\n##### (a) Direct hire authority\nThe Director of the National Weather Service may appoint, without regard to the provisions of subchapter I of chapter 33 (other than sections 3303, 3307, and 3328 of such chapter) of title 5, United States Code, qualified candidates to any of the following positions to satisfy critical staffing needs and fill vacancies at the Service:\n**(1)**\nEmployees performing public safety mission functions, including the following:\n**(A)**\nMeteorologists (classification series 1340).\n**(B)**\nGeneral physical scientists (classification series 1301).\n**(C)**\nHydrologists (classification series 1315).\n**(D)**\nComputer specialists (classification series 334).\n**(E)**\nElectronic technicians (classification series 856).\n**(2)**\nOther positions for which primary responsibilities include equipment operations, maintenance, and analysis, information technology, or engineering.\n##### (b) Sunset\nThe authority under subsection (a) shall expire on the earlier of\u2014\n**(1)**\nthe date that is 2 years after the date of the enactment of this Act; or\n**(2)**\nthe date on which all positions to satisfy to critical staffing needs and vacancies have been filled.\n##### (c) National Weather Service public safety designation\nThe Director of the Office of Personal Management shall designate the positions specified in subsection (a) as pertaining to public safety.\n##### (d) National Weather Service public safety priority; workforce assessment\n**(1) In general**\nTitle I of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8511 et seq. ), is amended\u2014\n**(A)**\nin section 101 ( 15 U.S.C. 8511 ), by adding at the end the following new sentence: The Under Secretary shall ensure the National Oceanic and Atmospheric Administration remains focused on providing accurate and timely weather forecasts that protect lives and property and enhance the national economy by disseminating to the public and core partners through nimble, flexible, and mobile methods critical weather information and impact-based decision support services. ;\n**(B)**\nby redesignating section 110 ( 15 U.S.C. 8519 ), as section 111; and\n**(C)**\nby inserting after section 109, the following new section:\n110. National Weather Service workforce assessment (a) Hiring assessment (1) In general Not later than 1 year after the date of the enactment of this section and annually thereafter, the Director of the National Weather Service shall submit to the Under Secretary, the Committee on Science, Space, and Technology of the House of Representatives, and the Committee on Commerce, Science, and Transportation of the Senate an assessment of the milestones, timelines, and service level expectations required for the hiring and timely on-boarding of employees of the National Weather Service. (2) Elements Each assessment under paragraph (1) may include determinations of the number of employees of the National Weather Service required at each forecasting office to provide services to protect lives and property and enhance the national economy in the geographic region of responsibility. (b) Health and morale assessment (1) In general Not later than 1 year after the date of the enactment of this section and annually thereafter, the Director of the National Weather Service shall submit to the Committee on Science, Space, and Technology of the House of Representatives, and the Committee on Commerce, Science, and Transportation of the Senate an assessment of medical impacts, including stress and long-term health impacts, on employees of the National Weather Service, including such employees\u2019 morale, related to required rotating shift work. (2) Coordination The Director of the National Weather Service is authorized to enter into a contract with a private sector entity to conduct the assessment required under paragraph (1). (3) Elements Each assessment under paragraph (1) may include the following: (A) Options for mitigating the impacts on employees identified in each such assessment. (B) Recommendations for improving benefits related to required rotating shift work. .\n**(2) Clerical amendment**\nThe table of contents in section 1(b) of Weather Research and Forecasting Innovation Act of 2017 is amended by striking the item relating to section 110 and inserting the following new items:\nSec. 110. National Weather Service workforce assessment. Sec. 111. Authorization of appropriations. .",
      "versionDate": "2025-06-06",
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
        "updateDate": "2025-06-30T13:12:11Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3809ih.xml"
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
      "title": "Weather Workforce Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Weather Workforce Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To waive certain legal requirements to permit the Director of the National Weather Service to expeditiously hire for positions that are critical for public safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:34:11Z"
    }
  ]
}
```
