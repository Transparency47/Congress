# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3405?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3405
- Title: PRC Financial Intermediary Review Act
- Congress: 119
- Bill type: S
- Bill number: 3405
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-01-07T16:56:08Z
- Update date including text: 2026-01-07T16:56:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3405",
    "number": "3405",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "PRC Financial Intermediary Review Act",
    "type": "S",
    "updateDate": "2026-01-07T16:56:08Z",
    "updateDateIncludingText": "2026-01-07T16:56:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T20:54:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3405is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3405\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. McCormick (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Securities and Exchange Commission to conduct a study regarding certain brokers and dealers that are controlled by or organized under the laws of the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the PRC Financial Intermediary Review Act .\n#### 2. Study and report\nNot later than 1 year after the date of the enactment of this Act, the Securities and Exchange Commission shall\u2014\n**(1)**\nconduct a study on the transparency of, and cooperation regarding\u2014\n**(A)**\nbrokers and dealers that are\u2014\n**(i)**\nmembers of a national securities association and registered with the Securities and Exchange Commission; and\n**(ii)**\ncontrolled by or organized under the laws of the People\u2019s Republic of China; and\n**(B)**\ninvestment advisers that are registered with the Securities and Exchange Commission and controlled by or organized under the laws of the People\u2019s Republic of China; and\n**(2)**\nsubmit to Congress a report that includes the results of the study conducted under paragraph (1).",
      "versionDate": "2025-12-09",
      "versionType": "Introduced in Senate"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-07T16:56:08Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3405is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "PRC Financial Intermediary Review Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PRC Financial Intermediary Review Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Securities and Exchange Commission to conduct a study regarding certain brokers and dealers that are controlled by or organized under the laws of the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-01T04:48:16Z"
    }
  ]
}
```
