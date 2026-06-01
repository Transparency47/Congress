# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8485?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8485
- Title: No Rogue Jurors Act
- Congress: 119
- Bill type: HR
- Bill number: 8485
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-04T19:44:25Z
- Update date including text: 2026-05-04T19:44:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8485",
    "number": "8485",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "L000595",
        "district": "5",
        "firstName": "Julia",
        "fullName": "Rep. Letlow, Julia [R-LA-5]",
        "lastName": "Letlow",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "No Rogue Jurors Act",
    "type": "HR",
    "updateDate": "2026-05-04T19:44:25Z",
    "updateDateIncludingText": "2026-05-04T19:44:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:01:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8485ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8485\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Ms. Letlow introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the provision of Federal funds to organizations that promote jury nullification, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Rogue Jurors Act .\n#### 2. Limitation on Federal funds for organizations that promote jury nullification\nNo Federal funds may be used to provide a grant, contract, award, or any other form of financial assistance to any organization, school, or entity that conducts training, produces materials, or engages in outreach (including under the title or framework of Equity & Root Cause Jury Training or any substantially similar designation) for the purpose of encouraging individuals to seek jury service in any Federal or District of Columbia court proceeding with the intent to vote contrary to the evidence or applicable law, including promoting the deliberate act of voting to acquit a defendant regardless of whether the elements of the charged offense have been established (commonly referred to as jury nullification ).",
      "versionDate": "2026-04-23",
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
        "name": "Law",
        "updateDate": "2026-05-04T19:44:25Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8485ih.xml"
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
      "title": "No Rogue Jurors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Rogue Jurors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-24T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the provision of Federal funds to organizations that promote jury nullification, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-24T08:18:46Z"
    }
  ]
}
```
