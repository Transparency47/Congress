# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3536?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3536
- Title: Stay in Your Lane Act
- Congress: 119
- Bill type: S
- Bill number: 3536
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-20T15:12:29Z
- Update date including text: 2026-01-20T15:12:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3536",
    "number": "3536",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Stay in Your Lane Act",
    "type": "S",
    "updateDate": "2026-01-20T15:12:29Z",
    "updateDateIncludingText": "2026-01-20T15:12:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T19:27:28Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3536is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3536\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Markey (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49, United States Code, with respect to the safety of driving automation systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stay in Your Lane Act .\n#### 2. Operational design domain restriction for driving systems\n##### (a) Safe domains for driving automation systems\n**(1) In general**\nSubchapter II of chapter 301 of title 49, United States Code, is amended by adding at the end the following:\n30130. Safe domains for driving automation systems (a) Definitions In this section: (1) Administrator The term Administrator means the Administrator of the National Highway Traffic Safety Administration. (2) Driving automation system The term driving automation system means the hardware and software that are collectively capable of simultaneously performing all of the lateral and longitudinal vehicle motor control subtasks of the dynamic driving task of a motor vehicle on a sustained basis. (3) Operational design domain The term operational design domain means operating conditions, as defined by the manufacturer, under which a driving automation system, or feature thereof, is specifically designed to function safely, including\u2014 (A) environmental, geographical, and time-of-day restrictions; and (B) the requisite presence or absence of certain traffic, road users, or roadway characteristics. (4) Safely The term safely , with respect to motor vehicle safety, means presenting no more than an inconsequential risk. (b) Operational design domain Each manufacturer of a driving automation system shall ensure that the driving automation system does not operate outside of its operational design domain. (c) Declarations (1) In general Each manufacturer of a driving automation system shall\u2014 (A) define the operational design domain as the conditions under which the driving automation system, or feature thereof, is designed to function safely; and (B) submit to the Administrator a declaration of that definition. (2) Publication Each manufacturer of a driving automation system shall make the declaration submitted by the manufacturer under paragraph (1)(B) available on a publicly accessible website of the manufacturer, which shall be the exact declaration submitted to the Administrator under that paragraph. .\n**(2) Clerical amendment**\nThe analysis for subchapter II of chapter 301 of title 49, United States Code, is amended by inserting after the item relating to section 30129 the following:\nSec. 30130. Safe domains for driving automation systems. .\n##### (b) Civil penalties\nSection 30165(a)(1) of title 49, United States Code, is amended, in the first sentence, by inserting 30130(b), after 30127, .\n##### (c) Limited definition of motor vehicle safety standard\nSection 30102(b) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby redesignating subparagraphs (C) through (H) as subparagraphs (D) through (I), respectively; and\n**(B)**\nby inserting after subparagraph (B) the following:\n(C) motor vehicle safety standard includes a requirement described in subsections (b) and (c)(1) of section 30130; ; and\n**(2)**\nin paragraph (2), by striking paragraph (1)(C), (D), (F), or (G) of this subsection and inserting subparagraph (D), (E), (G), or (H) of paragraph (1) .\n##### (d) Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-12-17",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-20T15:12:29Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3536is.xml"
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
      "title": "Stay in Your Lane Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T06:23:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stay in Your Lane Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:41Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49, United States Code, with respect to the safety of driving automation systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T06:18:41Z"
    }
  ]
}
```
