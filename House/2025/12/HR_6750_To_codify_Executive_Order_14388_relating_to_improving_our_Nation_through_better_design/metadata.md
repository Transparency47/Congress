# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6750?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6750
- Title: To codify Executive Order 14388 (relating to improving our Nation through better design).
- Congress: 119
- Bill type: HR
- Bill number: 6750
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-01-09T20:28:24Z
- Update date including text: 2026-01-09T20:28:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6750",
    "number": "6750",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "To codify Executive Order 14388 (relating to improving our Nation through better design).",
    "type": "HR",
    "updateDate": "2026-01-09T20:28:24Z",
    "updateDateIncludingText": "2026-01-09T20:28:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:04:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6750ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6750\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mrs. Houchin introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo codify Executive Order 14388 (relating to improving our Nation through better design).\n#### 1. Codification of Executive Order 14388\nExecutive Order 14388 (90 Fed Reg. 41759; relating to improving our Nation through better design) shall have the force and effect of law.",
      "versionDate": "2025-12-16",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-09T20:28:24Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6750ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify Executive Order 14388 (relating to improving our Nation through better design).",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T11:18:18Z"
    },
    {
      "title": "To codify Executive Order 14388 (relating to improving our Nation through better design).",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T09:06:42Z"
    }
  ]
}
```
