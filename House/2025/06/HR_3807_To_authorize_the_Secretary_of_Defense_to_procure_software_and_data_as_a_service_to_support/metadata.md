# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3807?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3807
- Title: FAST Act
- Congress: 119
- Bill type: HR
- Bill number: 3807
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2025-09-15T18:24:57Z
- Update date including text: 2025-09-15T18:24:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3807",
    "number": "3807",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000246",
        "district": "4",
        "firstName": "Pat",
        "fullName": "Rep. Fallon, Pat [R-TX-4]",
        "lastName": "Fallon",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "FAST Act",
    "type": "HR",
    "updateDate": "2025-09-15T18:24:57Z",
    "updateDateIncludingText": "2025-09-15T18:24:57Z"
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
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
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
          "date": "2025-06-06T13:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3807ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3807\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Fallon (for himself and Mr. Vindman ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo authorize the Secretary of Defense to procure software and data as a service to support the development of artificial intelligence systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Flexible Acquisition of Software Technology Act or the FAST Act .\n#### 2. Procurement of software and data as a service to support artificial intelligence systems\n##### (a) Authorization\nFor purposes of supporting the development and implementation of artificial intelligence systems to meet the operational needs of the Department of Defense, the Secretary of Defense may\u2014\n**(1)**\nprocure software as a service or software as a product;\n**(2)**\nprocure data as a service or data as a supply;\n**(3)**\nmodify software to support such systems; and\n**(4)**\nresearch, develop, test, and evaluate such software.\n##### (b) Funding\nThe Secretary of Defense may carry out subsection (a) using amounts appropriated or otherwise made available to the Secretary for any purpose.\n##### (c) Regulations\nThe Secretary of Defense shall issue or modify regulations as necessary to implement this section, which shall include regulations\u2014\n**(1)**\nto govern the procurement and modification of software and data for artificial intelligence systems under subsection (a); and\n**(2)**\nto provide for the oversight of such procurements and modifications.\n##### (d) Definitions\nIn this section:\n**(1) Artificial intelligence system**\nThe term artificial intelligence system means a system that is capable of performing tasks that normally require human-like cognition, including learning, decision-making, and problem-solving.\n**(2) Data as a service**\nThe term data as a service means a data delivery model in which data is provided on a subscription basis and is accessed remotely over the internet.\n**(3) Data as a supply**\nThe term data as a supply means a data delivery model in which data is acquired on a nonsubscription basis and retained locally rather than accessed remotely over the internet.\n**(4) Software**\nThe term software has the meaning given the term computer software in part 2.101 of the Federal Acquisition Regulation (or any successor regulation) and includes noncommercial, commercial, and commercial off-the-shelf software.\n**(5) Software as a service**\nThe term software as a service means a software delivery model in which software is provided on a subscription basis and is accessed remotely over the internet.",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-15T18:24:57Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3807ih.xml"
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
      "title": "FAST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Flexible Acquisition of Software Technology Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Defense to procure software and data as a service to support the development of artificial intelligence systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T06:18:24Z"
    }
  ]
}
```
