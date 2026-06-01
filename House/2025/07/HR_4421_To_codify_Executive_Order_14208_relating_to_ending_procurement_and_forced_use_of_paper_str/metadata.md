# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4421?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4421
- Title: Better Straws Act
- Congress: 119
- Bill type: HR
- Bill number: 4421
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-02-03T09:05:32Z
- Update date including text: 2026-02-03T09:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4421",
    "number": "4421",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Better Straws Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:32Z",
    "updateDateIncludingText": "2026-02-03T09:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:00:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4421ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4421\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Ms. Tenney introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo codify Executive Order 14208 relating to ending procurement and forced use of paper straws.\n#### 1. Short title\nThis Act may be cited as the Better Straws Act .\n#### 2. Codification of Executive order 14208\nExecutive Order 14208 (90 Fed. Reg. 9585; relating to ending procurement and forced use of paper straws) shall have the force and effect of law.",
      "versionDate": "2025-07-15",
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
        "updateDate": "2025-12-09T20:58:56Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4421ih.xml"
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
      "title": "To codify Executive Order 14208 relating to ending procurement and forced use of paper straws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T09:05:32Z"
    },
    {
      "title": "Better Straws Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-11T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Better Straws Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-11T06:08:14Z"
    }
  ]
}
```
