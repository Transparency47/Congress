# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/445?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/445
- Title: A resolution congratulating President Donald J. Trump for achieving peace in the Middle East.
- Congress: 119
- Bill type: SRES
- Bill number: 445
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2025-11-20T16:25:05Z
- Update date including text: 2025-11-20T16:25:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Referred to the Committee on Foreign Relations.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/445",
    "number": "445",
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
    "title": "A resolution congratulating President Donald J. Trump for achieving peace in the Middle East.",
    "type": "SRES",
    "updateDate": "2025-11-20T16:25:05Z",
    "updateDateIncludingText": "2025-11-20T16:25:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-09",
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
          "date": "2025-10-09T18:34:42Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres445is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 445\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Moreno (for himself and Mr. Risch ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCongratulating President Donald J. Trump for achieving peace in the Middle East.\nThat the Senate\u2014\n**(1)**\ncongratulates President Donald J. Trump for the momentous achievement of reaching a cease-fire between Israel and Hamas;\n**(2)**\ncalls on all peace-loving individuals and nations to embrace President Trump\u2019s peace plan; and\n**(3)**\ncelebrates the coming peace and prosperity that will benefit millions of individuals.",
      "versionDate": "2025-10-09",
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
        "updateDate": "2025-11-20T16:25:05Z"
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
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres445is.xml"
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
      "title": "A resolution congratulating President Donald J. Trump for achieving peace in the Middle East.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T02:48:18Z"
    },
    {
      "title": "A resolution congratulating President Donald J. Trump for achieving peace in the Middle East.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T10:56:16Z"
    }
  ]
}
```
