# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2099?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2099
- Title: Restore Prescription Drugs Discount Act
- Congress: 119
- Bill type: S
- Bill number: 2099
- Origin chamber: Senate
- Introduced date: 2025-06-17
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in Senate
- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-17: Introduced in Senate

## Actions

- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2099",
    "number": "2099",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Restore Prescription Drugs Discount Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T20:28:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2099is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2099\nIN THE SENATE OF THE UNITED STATES\nJune 17, 2025 Mr. Paul introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo repeal the Robinson-Patman Act of 1936.\n#### 1. Short title\nThis Act may be cited as the Restore Prescription Drugs Discount Act .\n#### 2. Repeal\nThe Act of June 19, 1936 (commonly known as the Robinson\u2013Patman Act ; 49 Stat. 1526, chapter 592; 15 U.S.C. 13a et seq. ), and the amendments made by that Act, are repealed.",
      "versionDate": "2025-06-17",
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
        "name": "Health",
        "updateDate": "2025-07-09T12:54:27Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2099is.xml"
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
      "title": "Restore Prescription Drugs Discount Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-27T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restore Prescription Drugs Discount Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-27T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the Robinson-Patman Act of 1936.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T02:18:22Z"
    }
  ]
}
```
