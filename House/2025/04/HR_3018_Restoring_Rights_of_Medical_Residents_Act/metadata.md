# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3018?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3018
- Title: Restoring Rights of Medical Residents Act
- Congress: 119
- Bill type: HR
- Bill number: 3018
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-05-21T13:01:29Z
- Update date including text: 2025-05-21T13:01:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3018",
    "number": "3018",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S000929",
        "district": "5",
        "firstName": "Victoria",
        "fullName": "Rep. Spartz, Victoria [R-IN-5]",
        "lastName": "Spartz",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Restoring Rights of Medical Residents Act",
    "type": "HR",
    "updateDate": "2025-05-21T13:01:29Z",
    "updateDateIncludingText": "2025-05-21T13:01:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:00:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3018ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3018\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mrs. Spartz introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Pension Funding Equity Act of 2004 to repeal the antitrust exemption applicable to graduate medical resident matching programs.\n#### 1. Short title\nThis Act may be cited as the Restoring Rights of Medical Residents Act .\n#### 2. Repealer\nSection 207 of the Pension Funding Equity Act of 2004 ( 15 U.S.C. 37B ) is repealed.\n#### 3. Effective date\nThis Act shall take effect on the March 18 that 1st occurs after the date of the enactment of this Act.",
      "versionDate": "2025-04-24",
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
        "name": "Commerce",
        "updateDate": "2025-05-21T13:01:29Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3018ih.xml"
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
      "title": "Restoring Rights of Medical Residents Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Rights of Medical Residents Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Pension Funding Equity Act of 2004 to repeal the antitrust exemption applicable to graduate medical resident matching programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:33:26Z"
    }
  ]
}
```
