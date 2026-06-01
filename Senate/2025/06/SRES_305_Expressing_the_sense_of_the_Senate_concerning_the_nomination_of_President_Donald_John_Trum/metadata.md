# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/305?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/305
- Title: A resolution expressing the sense of the Senate concerning the nomination of President Donald John Trump for the Nobel Peace Prize.
- Congress: 119
- Bill type: SRES
- Bill number: 305
- Origin chamber: Senate
- Introduced date: 2025-06-25
- Update date: 2025-07-21T15:36:51Z
- Update date including text: 2025-07-21T15:36:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in Senate
- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S3535-3536)
- Latest action: 2025-06-25: Introduced in Senate

## Actions

- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S3535-3536)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/305",
    "number": "305",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A resolution expressing the sense of the Senate concerning the nomination of President Donald John Trump for the Nobel Peace Prize.",
    "type": "SRES",
    "updateDate": "2025-07-21T15:36:51Z",
    "updateDateIncludingText": "2025-07-21T15:36:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S3535-3536)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T22:52:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres305is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 305\nIN THE SENATE OF THE UNITED STATES\nJune 25 (legislative day, June 24), 2025 Mr. Moreno submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate concerning the nomination of President Donald John Trump for the Nobel Peace Prize.\nThat the Senate\u2014\n**(1)**\ncalls on the Norwegian Nobel Committee to award President Donald John Trump the 2025 Nobel Peace Prize;\n**(2)**\nurges all peace-loving nations to join in that call; and\n**(3)**\nexpresses its deepest appreciation to President Trump for bringing an end both to the nuclear program of Iran and hostilities related thereto in only 12 days.",
      "versionDate": "2025-06-25",
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
        "name": "International Affairs",
        "updateDate": "2025-07-21T15:36:51Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres305is.xml"
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
      "title": "A resolution expressing the sense of the Senate concerning the nomination of President Donald John Trump for the Nobel Peace Prize.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T02:18:19Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate concerning the nomination of President Donald John Trump for the Nobel Peace Prize.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T10:56:16Z"
    }
  ]
}
```
