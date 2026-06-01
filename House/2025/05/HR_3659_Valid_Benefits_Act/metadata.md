# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3659?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3659
- Title: Valid Benefits Act
- Congress: 119
- Bill type: HR
- Bill number: 3659
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-06-20T13:16:12Z
- Update date including text: 2025-06-20T13:16:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3659",
    "number": "3659",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Valid Benefits Act",
    "type": "HR",
    "updateDate": "2025-06-20T13:16:12Z",
    "updateDateIncludingText": "2025-06-20T13:16:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:00:25Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3659ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3659\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct Federal departments and agencies to verify eligibility for Federal benefits for individuals 105 years of age or older, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Valid Benefits Act .\n#### 2. Verification of eligibility for Federal benefits for certain elderly individuals\n##### (a) In general\nThe head of each Federal department or agency that provides Federal benefits to individuals who have attained 105 years of age or more shall take appropriate steps to ensure, on a semiannual basis, that each such individual remains eligible for such benefits.\n##### (b) Authority To issue regulations\nThe head of each Federal department or agency specified in paragraph (1) may issue regulations to implement this section.\n##### (c) Effective date\nThis section shall apply with respect to payments of Federal benefits made on or after December 31, 2025.",
      "versionDate": "2025-05-29",
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
        "name": "Social Welfare",
        "updateDate": "2025-06-20T13:16:12Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3659ih.xml"
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
      "title": "Valid Benefits Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Valid Benefits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T09:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct Federal departments and agencies to verify eligibility for Federal benefits for individuals 105 years of age or older, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T09:18:20Z"
    }
  ]
}
```
