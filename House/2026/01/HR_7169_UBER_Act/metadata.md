# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7169?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7169
- Title: UBER Act
- Congress: 119
- Bill type: HR
- Bill number: 7169
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-05-19T13:17:40Z
- Update date including text: 2026-05-19T13:17:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7169",
    "number": "7169",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001317",
        "district": "2",
        "firstName": "Josh",
        "fullName": "Rep. Brecheen, Josh [R-OK-2]",
        "lastName": "Brecheen",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "UBER Act",
    "type": "HR",
    "updateDate": "2026-05-19T13:17:40Z",
    "updateDateIncludingText": "2026-05-19T13:17:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "AL"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7169ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7169\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. Brecheen (for himself, Mr. Moore of Alabama , Mr. Fine , and Mr. Smith of New Jersey ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require English proficiency as a prerequisite for eligibility for ride share contracts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Understanding Basic English Requirements Act of 2026 or the UBER Act .\n#### 2. English proficiency and other driver requirements for ride share contract eligibility\n##### (a) Requirements\n**(1) In general**\nThe head of an executive agency may not award an agreement or a contract with any transportation network company or shared-use mobility company for services provided in the continental United States, Alaska, or Hawaii where unless each driver who will be performing work under the agreement or contract\u2014\n**(A)**\nis at least 21 years old;\n**(B)**\ncan read and speak English sufficiently to converse with the general public, law enforcement, and other officials, understand highway traffic signs, respond to official inquiries, and make entries on reports and records;\n**(C)**\ncan, by reason of experience, training, or both, safely operate the type of vehicle the driver drives;\n**(D)**\nhas a currently valid driver's license issued only by one State or jurisdiction; and\n**(E)**\nhas successfully completed a driver's road test.\n**(2) Exception for American Sign Language**\nThe requirement under paragraph (1)(B) does not apply to drivers who are deaf or hearing impaired and use American Sign Language.\n##### (b) Compliance certification and debarment\nA transportation network company or shared-use mobility company shall be required, for purposes of eligibility for an agreement or contract described in paragraph (1) of subsection (a), to certify to the head of the executive agency that all drivers for the company who will be performing work under such agreement or contract meet the requirements set forth in subsection (a)(1). Any company found to not be in compliance with such certification shall be debarred from receiving Federal contracts for a period of 5 years.\n##### (c) Definitions\nIn this section:\n**(1) Executive agency**\nThe term executive agency has the meaning given the term in section 133 of title 41, United States Code.\n**(2) Shared-use mobility company**\nThe term shared-use mobility company means a corporation, partnership, sole proprietorship, or other licensed and operating entity that provides transportation services that are shared among users, including taxis, limos, bikesharing, ridesharing (such as carpooling and vanpooling), ridesourcing, scooter sharing, or shuttle services.\n**(3) Transportation network company**\nThe term transportation network company means a corporation, partnership, sole proprietorship, or other licensed and operating entity that uses a digital network to connect a transportation network company (TNC) rider to a TNC driver who provides a prearranged ride. A TNC may not control, direct, or manage the personal vehicle or the TNC driver who connects to its digital network, except where agreed to by written contract.",
      "versionDate": "2026-01-21",
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
        "actionDate": "2025-11-06",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3121",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "UBER Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-05-15T17:15:39Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7169ih.xml"
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
      "title": "UBER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T03:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UBER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Understanding Basic English Requirements Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require English proficiency as a prerequisite for eligibility for ride share contracts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T03:18:41Z"
    }
  ]
}
```
