# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/93?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/93
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Safety and Environmental Enforcement relating to "Restoration of Names That Honor American Greatness; Gulf of America".
- Congress: 119
- Bill type: SJRES
- Bill number: 93
- Origin chamber: Senate
- Introduced date: 2025-10-28
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in Senate
- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-10-28: Introduced in Senate

## Actions

- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/93",
    "number": "93",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Safety and Environmental Enforcement relating to \"Restoration of Names That Honor American Greatness; Gulf of America\".",
    "type": "SJRES",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:00:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres93is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 93\nIN THE SENATE OF THE UNITED STATES\nOctober 28, 2025 Mr. Whitehouse introduced the following joint resolution; which was read twice and referred to the Committee on Energy and Natural Resources\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Safety and Environmental Enforcement relating to Restoration of Names That Honor American Greatness; Gulf of America .\nThat Congress disapproves the rule submitted by the Bureau of Safety and Environmental Enforcement relating to Restoration of Names That Honor American Greatness; Gulf of America (90 Fed. Reg. 44322 (September 15, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2025-10-28",
      "versionType": "IS"
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-02T18:58:33Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres93is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Safety and Environmental Enforcement relating to \"Restoration of Names That Honor American Greatness; Gulf of America\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:33:17Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Safety and Environmental Enforcement relating to \"Restoration of Names That Honor American Greatness; Gulf of America\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T10:56:13Z"
    }
  ]
}
```
