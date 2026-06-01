# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3795?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3795
- Title: Radar Next Program Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3795
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-04-03T21:19:16Z
- Update date including text: 2026-04-03T21:19:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3795",
    "number": "3795",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Radar Next Program Act of 2026",
    "type": "S",
    "updateDate": "2026-04-03T21:19:16Z",
    "updateDateIncludingText": "2026-04-03T21:19:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
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
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T19:42:20Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3795is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3795\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Ms. Cantwell (for herself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish the Radar Next Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Radar Next Program Act of 2026 .\n#### 2. Radar next program\n##### (a) In general\nThe Under Secretary, in consultation with the Director of the National Weather Service, shall establish a program to be known as the Radar Next Program (in this section referred to as the program ).\n##### (b) Requirements\nIn carrying out the program, the Under Secretary shall\u2014\n**(1)**\ndevelop performance and coverage requirements for the weather radar network of the United States, including for the territories of the United States;\n**(2)**\ncollaborate with the weather enterprise to determine potential solutions to update the weather radar network of the United States that meet the requirements developed under paragraph (1); and\n**(3)**\ndevelop a plan in accordance with subsection (c).\n##### (c) Plan\n**(1) In general**\nThe Under Secretary shall develop a plan to replace the Next Generation Weather Radar system of the National Weather Service in existence as of the date of the enactment of this Act (in this subsection referred to as the NEXRAD system ).\n**(2) Elements**\nThe plan developed under this subsection shall seek to continue and improve weather radar coverage in the United States and its territories and include the following:\n**(A)**\nEstimates of quantifiable improvements in performance, coverage, and accuracy to be made from potential options for replacement of the NEXRAD system.\n**(B)**\nDevelopment of a phased array radar to test and determine the specifications and requirements for such replacement.\n**(C)**\nExpected actions needed to implement the recommendations of the report published by the Environmental Information Services Working Group of the Science Advisory Board of the National Oceanic and Atmospheric Administration on November 15, 2023, and entitled A NESDIS Observing System Backbone Framework to assist in defining a radar backbone architecture that will best serve the United States.\n**(D)**\nEstablishment of a weather surveillance radar testbed for the following:\n**(i)**\nEvaluation of commercial radars with the potential to replace or supplement the NEXRAD system.\n**(ii)**\nProviding technical assistance for the use of small, gap-filling radars with private and local partners in regions where geographical topography prevents the full use of large systems or in locations where such systems may not be commercially viable.\n**(E)**\nConsultation and input solicited from academia, meteorologists, emergency managers, and public safety or utility officials regarding the specifications and requirements for replacement of the NEXRAD system.\n**(F)**\nPrioritized locations for initial deployment of the system that will replace the NEXRAD system.\n**(G)**\nExpected locations of the system that will replace the NEXRAD system, including sites located more than 75 miles away from an existing NEXRAD system station and additional appropriate locations.\n**(H)**\nExpected or planned improvements to data available for weather and water-related forecasts and warnings from the system that will replace the NEXRAD system.\n**(3) Procurement deadline**\nThe Under Secretary shall take such actions as may be necessary to ensure the plan developed under this subsection is fully implemented and executed by not later than September 30, 2040.\n##### (d) Radar-As-A-Service\n**(1) In general**\nThe Under Secretary may partner or contract with entities outside of the National Oceanic and Atmospheric Administration to fill data gaps in weather radar coverage using weather radars and data assimilation technologies in order to\u2014\n**(A)**\nsupplement data gaps in weather radar coverage, including at low levels and in wide areas, in existence as of the date of the enactment of this Act;\n**(B)**\nensure the continued performance of the weather radar network of the United States; and\n**(C)**\nbetter detect significant precipitation and severe weather over a greater area across a population.\n**(2) Considerations**\nIn carrying out paragraph (1), the Under Secretary may consider\u2014\n**(A)**\npartnering or contracting with entities that have participated in the testbed described in subsection (c)(2)(D), the National Mesonet Program, or cooperative research and development agreements; and\n**(B)**\nweather camera systems and services, including in consultation with the Federal Aviation Administration, as viable technologies to supplement weather forecasting and prediction needs.\n##### (e) Updates to congress\nThe Under Secretary shall provide to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives periodic updates on the implementation of this section.\n##### (f) Definitions\nIn this Act, the terms Under Secretary and weather enterprise have the meanings given such terms in section 2 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8501 ).",
      "versionDate": "2026-02-05",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-03-04",
        "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably."
      },
      "number": "3923",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Weather Research and Forecasting Innovation Reauthorization Act of 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-06",
        "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committees on Natural Resources, Energy and Commerce, and Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3816",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Weather Act Reauthorization Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-02-27T19:50:23Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3795is.xml"
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
      "title": "Radar Next Program Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T05:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Radar Next Program Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T05:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Radar Next Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T05:48:34Z"
    }
  ]
}
```
