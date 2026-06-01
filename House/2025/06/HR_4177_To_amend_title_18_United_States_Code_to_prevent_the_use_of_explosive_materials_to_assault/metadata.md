# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4177?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4177
- Title: COPS Act
- Congress: 119
- Bill type: HR
- Bill number: 4177
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-07-17T11:12:59Z
- Update date including text: 2025-07-17T11:12:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4177",
    "number": "4177",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "COPS Act",
    "type": "HR",
    "updateDate": "2025-07-17T11:12:59Z",
    "updateDateIncludingText": "2025-07-17T11:12:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4177ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4177\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Tony Gonzales of Texas introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prevent the use of explosive materials to assault, resist, or impede certain officers or employees.\n#### 1. Short title\nThis Act may be cited as the Curbing Offenses on Policing Services Act or the COPS Act .\n#### 2. Assaulting, resisting, or impeding certain officers or employees\nSection 111 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking under this title and inserting up to $200,000 ;\n**(B)**\nby striking one year and inserting two years ; and\n**(C)**\nby striking 8 years and inserting 10 years ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby inserting after including the following: explosive materials, as defined in section 841, or ;\n**(B)**\nby striking shall be fined under this title and inserting shall be fined up to $500,000, notwithstanding section 3571, ; and\n**(C)**\nby striking 20 years and inserting 25 years .",
      "versionDate": "2025-06-26",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-17T11:12:59Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4177ih.xml"
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
      "title": "COPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Curbing Offenses on Policing Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prevent the use of explosive materials to assault, resist, or impede certain officers or employees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-09T04:18:23Z"
    }
  ]
}
```
