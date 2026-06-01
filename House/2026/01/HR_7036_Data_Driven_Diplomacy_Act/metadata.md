# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7036?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7036
- Title: Data Driven Diplomacy Act
- Congress: 119
- Bill type: HR
- Bill number: 7036
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-02-02T22:20:16Z
- Update date including text: 2026-02-02T22:20:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7036",
    "number": "7036",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Data Driven Diplomacy Act",
    "type": "HR",
    "updateDate": "2026-02-02T22:20:16Z",
    "updateDateIncludingText": "2026-02-02T22:20:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7036ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7036\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Huizenga introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo increase collaboration within the Department of State between the Office of Opinion Research of the Bureau of Intelligence and Research and the Bureau of Global Public Affairs.\n#### 1. Short title\nThis Act may be cited as the Data Driven Diplomacy Act .\n#### 2. Coordination with the Office of Opinion Research\nThe Assistant Secretary for Global Public Affairs shall request the Office of Opinion Research of the Bureau of Intelligence and Research of the Department of State to conduct public opinion surveys that inform the Bureau of Global Public Affairs of the Department of State on cultural context, target audiences, and shifting attitudes towards the United States and United States interests in regions where United States funded media outlets operate or could operate in the future.",
      "versionDate": "2026-01-13",
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
        "name": "International Affairs",
        "updateDate": "2026-01-16T18:53:37Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7036ih.xml"
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
      "title": "Data Driven Diplomacy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Data Driven Diplomacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase collaboration within the Department of State between the Office of Opinion Research of the Bureau of Intelligence and Research and the Bureau of Global Public Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:33:30Z"
    }
  ]
}
```
