# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4979?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4979
- Title: Tick Identification Pilot Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4979
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2026-05-13T08:06:44Z
- Update date including text: 2026-05-13T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4979",
    "number": "4979",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Tick Identification Pilot Program Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:44Z",
    "updateDateIncludingText": "2026-05-13T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "DC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "IN"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "RI"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4979ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4979\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Gottheimer (for himself and Mr. Kean ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, to award grants to States to implement a tick identification pilot program.\n#### 1. Short title\nThis Act may be cited as the Tick Identification Pilot Program Act of 2025 .\n#### 2. Tick identification pilot program\n##### (a) Establishment\nThe Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, may award grants to States to implement a tick identification program.\n##### (b) Priority\nIn awarding grants under this section, the Secretary shall give priority to States that\u2014\n**(1)**\nhave more reported cases of Lyme disease and other tick-borne diseases; and\n**(2)**\nsubmit an effective plan for implementation and maintenance of a tick identification program.\n##### (c) Program requirements\nAny program funded under this section shall\u2014\n**(1)**\nallow individuals to submit electronically photo images of ticks encountered;\n**(2)**\nrequire images of ticks to be submitted with the likely geographic location where the ticks were encountered, the date on which the ticks were encountered, and the likely physical location where the ticks were found (for example, on a pet, on a human, or loose);\n**(3)**\nafter review by a qualified professional, respond to the individual directly within 72 hours of the image being received with\u2014\n**(A)**\nif possible, identification of the species and life stage of the tick;\n**(B)**\nif possible, an estimate of the risk that the tick carried a tick-borne disease;\n**(C)**\na recommendation of the best practices for the individual who encountered the tick, including with respect to seeking medical evaluation and submitting the tick for testing; and\n**(D)**\nadditional education on best methods to avoid ticks and prevent contagion of tick-borne illnesses; and\n**(4)**\nmaintain a database of reported tick incidents, including\u2014\n**(A)**\nthe date, geographic location, and environment of the encounter;\n**(B)**\nany identifying information about the tick that was determined; and\n**(C)**\nbest practices that were disseminated to each reporting individual.\n##### (d) Application\nTo seek a grant under this section, a State shall submit an application at such time, in such form, and containing such information as the Secretary may prescribe.\n##### (e) Data collection; report\n**(1) Data collection**\nThe Secretary shall collect, with respect to each State program funded under this section and each fiscal year, the following data:\n**(A)**\nThe number of tick incidents reported.\n**(B)**\nFor each incident reported\u2014\n**(i)**\nthe date, geographic location, and environment of the encounter;\n**(ii)**\nany identifying information about the tick that was determined; and\n**(iii)**\nbest practices that were disseminated to each reporting individual.\n**(2) Report**\nNot later than 90 days after the first day of each of fiscal years 2026 through 2029, the Secretary shall prepare and submit to the Congress a report on the data collected under paragraph (1).\n##### (f) Definitions\nIn this section:\n**(1) Qualified professional**\nThe term qualified professional means a biologist with a background in vector biology.\n**(2) Secretary**\nThe term Secretary means the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention.",
      "versionDate": "2025-08-15",
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
        "name": "Health",
        "updateDate": "2025-09-19T15:25:48Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4979ih.xml"
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
      "title": "Tick Identification Pilot Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-19T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tick Identification Pilot Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, to award grants to States to implement a tick identification pilot program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-19T04:33:17Z"
    }
  ]
}
```
