# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2646?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2646
- Title: Radar Gap Elimination Act
- Congress: 119
- Bill type: HR
- Bill number: 2646
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2025-10-18T08:05:36Z
- Update date including text: 2025-10-18T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2646",
    "number": "2646",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Radar Gap Elimination Act",
    "type": "HR",
    "updateDate": "2025-10-18T08:05:36Z",
    "updateDateIncludingText": "2025-10-18T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:00:05Z",
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
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NC"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NC"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "IA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2646ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2646\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Moore of North Carolina (for himself, Ms. Ross , and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo require the evaluation of certain criteria relating to locations for deployment of successor radar systems of the National Weather Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Radar Gap Elimination Act .\n#### 2. Radar Next Program\n##### (a) In general\nThe Under Secretary of Commerce for Oceans and Atmosphere, in consultation with the Director of the National Weather Service, shall establish a program to be known as the Radar Next Program (in this section referred to as the program ).\n##### (b) Requirements\nIn carrying out the program, the Under Secretary of Commerce for Oceans and Atmosphere shall carry out the following:\n**(1)**\nDevelop performance and coverage requirements for the weather radar network of the United States, including the territories of the United States.\n**(2)**\nCollaborate with the weather enterprise (as such term is defined in section 2 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 )) to determine potential solutions to update the weather radar network of the United States that meets the requirements developed under paragraph (1).\n**(3)**\nDevelop a plan in accordance with subsection (c).\n##### (c) Plan\n**(1) In general**\nThe Under Secretary of Commerce for Oceans and Atmosphere shall develop a plan to replace the Next Generation Weather Radar of the National Weather Service system in existence as of the date of the enactment of this Act (in this subsection referred to as the NEXRAD system ).\n**(2) Elements**\nThe plan developed under this subsection shall seek to continue and improve weather radar coverage in the United States and its territories, and include the following:\n**(A)**\nEstimates of quantifiable improvements in performance, coverage, and accuracy to be made from potential options for replacement of the NEXRAD system.\n**(B)**\nDevelopment of a proof-of-concept phased array radar to test and determine the specifications and requirements for such replacement.\n**(C)**\nExpected actions needed to implement the recommendations of the report published by the Environmental Information Services Working Group of the Science Advisory Board of the National Oceanic and Atmospheric Administration in November 2023 and entitled A NESDIS Observing System Backbone Framework to assist in defining a radar backbone architecture that will best serve the United States.\n**(D)**\nEstablishment of a weather surveillance radar testbed for the following:\n**(i)**\nEvaluation of commercial radars with the potential to replace or supplement the NEXRAD system.\n**(ii)**\nProviding technical assistance for the use of small, gap-filling radars with private and local partners in regions where geographical topography prevents the full use of large systems or in locations where such systems may not be commercially viable.\n**(E)**\nConsultation and input solicited from academia, meteorologists, emergency managers, and public safety or utility officials regarding the specifications and requirements for replacement of the NEXRAD system.\n**(F)**\nPrioritized locations for initial deployment of the system that will replace the NEXRAD system.\n**(G)**\nExpected locations of the system that will replace the NEXRAD system, including sites located more than 75 miles away from an existing NEXRAD system station and additional appropriate locations.\n**(H)**\nExpected or planned improvements to data available for weather and water-related forecasts and warnings from the system that will replace the NEXRAD system.\n**(3) Procurement deadline**\nThe Under Secretary of Commerce for Oceans and Atmosphere shall take such actions as may be necessary to ensure the plan developed under this subsection is fully implemented and executed by not later than September 30, 2040.\n##### (d) Radar-as-a-Service\n**(1) In general**\nThe Under Secretary of Commerce for Oceans and Atmosphere may partner or contract with entities outside of the National Oceanic and Atmospheric Administration to fill data gaps in weather radar coverage using diverse weather radars and data assimilation technologies in order to accomplish the following:\n**(A)**\nSupplement data gaps in weather radar coverage, including at low levels and wide areas, in existence as of the date of the enactment of this Act.\n**(B)**\nEnsure the continued performance of the United States\u2019 weather radar network.\n**(C)**\nBetter detect significant precipitation and severe weather over a greater area across a population.\n**(2) Considerations**\nIn carrying out paragraph (1), the Under Secretary of Commerce for Oceans and Atmosphere may consider the following:\n**(A)**\nPartnering or contracting with entities that have participated in the testbed described in subsection (c)(2)(D), the National Mesonet Program, or Cooperative Research and Development Agreements.\n**(B)**\nWeather camera systems and services, including in consultation with the Federal Aviation Administration, as viable technologies to supplement weather forecasting and prediction needs.\n##### (e) Updates to Congress\nThe Under Secretary of Commerce for Oceans and Atmosphere shall provide to the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate periodic updates on the implementation of this section.",
      "versionDate": "2025-04-03",
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
        "updateDate": "2025-05-20T14:14:34Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2646ih.xml"
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
      "title": "Radar Gap Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Radar Gap Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the evaluation of certain criteria relating to locations for deployment of successor radar systems of the National Weather Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T05:34:11Z"
    }
  ]
}
```
