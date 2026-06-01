# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3837?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3837
- Title: EO 14218 Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3837
- Origin chamber: House
- Introduced date: 2025-06-09
- Update date: 2025-07-18T16:08:47Z
- Update date including text: 2025-07-18T16:08:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-06-09: Introduced in House

## Actions

- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3837",
    "number": "3837",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "EO 14218 Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-18T16:08:47Z",
    "updateDateIncludingText": "2025-07-18T16:08:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
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
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T16:02:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3837ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3837\nIN THE HOUSE OF REPRESENTATIVES\nJune 9, 2025 Mr. Burchett introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo codify Executive Order 14218 (relating to ending taxpayer subsidization of open borders).\n#### 1. Short title\nThis Act may be cited as the EO 14218 Act of 2025 .\n#### 2. Codification of Executive Order EO 14218, ending taxpayer subsidization of open borders\nExecutive Order 14218 (90 Fed. Reg. 10581; relating to ending taxpayer subsidization of open borders) shall have the force and effect of law.",
      "versionDate": "2025-06-09",
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
        "name": "Immigration",
        "updateDate": "2025-07-18T16:08:47Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3837ih.xml"
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
      "title": "EO 14218 Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EO 14218 Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify Executive Order 14218 (relating to ending taxpayer subsidization of open borders).",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T05:48:17Z"
    }
  ]
}
```
