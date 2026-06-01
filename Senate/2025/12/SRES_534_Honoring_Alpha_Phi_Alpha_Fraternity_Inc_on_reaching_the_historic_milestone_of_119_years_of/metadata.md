# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/534?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/534
- Title: Original Resolution Honoring Alpha Phi Alpha
- Congress: 119
- Bill type: SRES
- Bill number: 534
- Origin chamber: Senate
- Introduced date: 2025-12-08
- Update date: 2025-12-10T21:25:41Z
- Update date including text: 2025-12-10T21:25:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-08: Introduced in Senate
- 2025-12-08 - IntroReferral: Introduced in Senate
- 2025-12-08 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S8532)
- Latest action: 2025-12-08: Introduced in Senate

## Actions

- 2025-12-08 - IntroReferral: Introduced in Senate
- 2025-12-08 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S8532)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-08",
    "latestAction": {
      "actionDate": "2025-12-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/534",
    "number": "534",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Original Resolution Honoring Alpha Phi Alpha",
    "type": "SRES",
    "updateDate": "2025-12-10T21:25:41Z",
    "updateDateIncludingText": "2025-12-10T21:25:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S8532)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-08",
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
          "date": "2025-12-08T22:22:47Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres534is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 534\nIN THE SENATE OF THE UNITED STATES\nDecember 8 (legislative day, December 4), 2025 Mr. Warnock submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring Alpha Phi Alpha Fraternity, Inc., on reaching the historic milestone of 119 years of brotherhood as Servants of All .\n#### 1. Short title\nThis resolution may be cited as the Original Resolution Honoring Alpha Phi Alpha .\n#### 2. Recognition\nThe Senate congratulates and commends Alpha Phi Alpha Fraternity, Inc., on 119 years of service.",
      "versionDate": "2025-12-08",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-10T21:25:40Z"
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
      "date": "2025-12-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres534is.xml"
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
      "title": "Original Resolution Honoring Alpha Phi Alpha",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T04:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Original Resolution Honoring Alpha Phi Alpha",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-10T04:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution honoring Alpha Phi Alpha Fraternity, Inc., on reaching the historic milestone of 119 years of brotherhood as \"Servants of All\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-10T04:18:22Z"
    }
  ]
}
```
