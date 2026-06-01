# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2054?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2054
- Title: Flood Insurance Consumer Choice Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2054
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-07-07T13:34:09Z
- Update date including text: 2025-07-07T13:34:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2054",
    "number": "2054",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Flood Insurance Consumer Choice Act of 2025",
    "type": "S",
    "updateDate": "2025-07-07T13:34:09Z",
    "updateDateIncludingText": "2025-07-07T13:34:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T16:40:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2054is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2054\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo allow National Flood Insurance Program policyholders who leave the program to purchase a private insurance flood policy to return to the National Flood Insurance Program without penalty, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Flood Insurance Consumer Choice Act of 2025 .\n#### 2. Effect of private flood insurance coverage on continuous coverage requirements\nSection 1308 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4015 ) is amended by adding at the end the following:\n(n) Effect of private flood insurance coverage on continuous coverage requirements For purposes of applying any statutory, regulatory, or administrative continuous coverage requirement, including under section 1307(g)(1), the Administrator shall consider any period during which a property was continuously covered by a flood insurance policy through the private market that was used to satisfy the requirements under section 102(a) of the Flood Disaster Protection Act of 1973 ( 42 U.S.C. 4012a(a) ) to be a period of continuous coverage. .",
      "versionDate": "2025-06-12",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-07T13:34:09Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2054is.xml"
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
      "title": "Flood Insurance Consumer Choice Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Flood Insurance Consumer Choice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow National Flood Insurance Program policyholders who leave the program to purchase a private insurance flood policy to return to the National Flood Insurance Program without penalty, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T03:03:25Z"
    }
  ]
}
```
