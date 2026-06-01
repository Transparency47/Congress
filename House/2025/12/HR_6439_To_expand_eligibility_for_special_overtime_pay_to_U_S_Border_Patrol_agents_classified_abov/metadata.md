# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6439?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6439
- Title: Border Patrol Supervisors Retention Act
- Congress: 119
- Bill type: HR
- Bill number: 6439
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-01-07T17:06:05Z
- Update date including text: 2026-01-07T17:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6439",
    "number": "6439",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000594",
        "district": "23",
        "firstName": "Tony",
        "fullName": "Rep. Gonzales, Tony [R-TX-23]",
        "lastName": "Gonzales",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Border Patrol Supervisors Retention Act",
    "type": "HR",
    "updateDate": "2026-01-07T17:06:05Z",
    "updateDateIncludingText": "2026-01-07T17:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:06:30Z",
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
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MS"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MO"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
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
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6439ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6439\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Tony Gonzales of Texas (for himself, Mr. Guest , Mr. Kelly of Pennsylvania , Mr. Alford , Mr. Stauber , and Mr. McGuire ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo expand eligibility for special overtime pay to U.S. Border Patrol agents classified above grade GS\u201312.\n#### 1. Short title\nThis Act may be cited as the Border Patrol Supervisors Retention Act .\n#### 2. Establishment of higher rates of regularly scheduled overtime pay for certain U.S. Border Patrol agents\nSection 5550(h) of title 5, United States Code, is amended\u2014\n**(1)**\nin the subsection heading, by striking GS\u201312 Border Patrol agents and inserting Border Patrol agents classified from grade GS\u201312 through GS\u201315 ; and\n**(2)**\nin paragraph (1), by striking a position at grade GS\u201312 and inserting a position from grade GS\u201312 through GS\u201315 .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-07-10",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2249",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Border Patrol Supervisors Retention Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-07T17:06:05Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6439ih.xml"
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
      "title": "Border Patrol Supervisors Retention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Border Patrol Supervisors Retention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand eligibility for special overtime pay to U.S. Border Patrol agents classified above grade GS-12.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T08:18:31Z"
    }
  ]
}
```
