# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6614?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6614
- Title: Chemical Disaster Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 6614
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-01-08T14:35:43Z
- Update date including text: 2026-01-08T14:35:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6614",
    "number": "6614",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001300",
        "district": "44",
        "firstName": "Nanette",
        "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
        "lastName": "Barrag\u00e1n",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Chemical Disaster Prevention Act",
    "type": "HR",
    "updateDate": "2026-01-08T14:35:43Z",
    "updateDateIncludingText": "2026-01-08T14:35:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:09:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6614ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6614\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Ms. Barrag\u00e1n introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the Administrator of the Environmental Protection Agency from reconsidering, revising, or replacing the final rule relating to the accidental release prevention requirements of the risk management programs under the Clean Air Act.\n#### 1. Short title\nThis Act may be cited as the Chemical Disaster Prevention Act .\n#### 2. Clean Air Act risk management programs\nDuring the period that begins on the date of enactment of this section and ends January 20, 2029, notwithstanding any other provision of law, the Administrator of the Environmental Protection Agency may not propose, finalize, or implement any action to reconsider, revise, or replace the final rule titled Accidental Release Prevention Requirements: Risk Management Programs Under the Clean Air Act; Safer Communities by Chemical Accident Prevention (89 Fed. Reg. 17622; March 11, 2024).",
      "versionDate": "2025-12-11",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-08T14:35:43Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6614ih.xml"
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
      "title": "Chemical Disaster Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chemical Disaster Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Administrator of the Environmental Protection Agency from reconsidering, revising, or replacing the final rule relating to the accidental release prevention requirements of the risk management programs under the Clean Air Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T05:48:23Z"
    }
  ]
}
```
