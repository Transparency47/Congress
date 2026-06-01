# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/678?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/678
- Title: A resolution prohibiting the use of funds for travel by Senators to or from their residence during Government shutdowns.
- Congress: 119
- Bill type: SRES
- Bill number: 678
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-04-24T15:46:57Z
- Update date including text: 2026-04-24T15:46:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S1826)
- 2026-04-16 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-16: Submitted in Senate

## Actions

- 2026-04-16 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S1826)
- 2026-04-16 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/678",
    "number": "678",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A resolution prohibiting the use of funds for travel by Senators to or from their residence during Government shutdowns.",
    "type": "SRES",
    "updateDate": "2026-04-24T15:46:57Z",
    "updateDateIncludingText": "2026-04-24T15:46:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Rules and Administration. (text: CR S1826)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-04-16T19:52:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres678is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 678\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mrs. Moody submitted the following resolution; which was referred to the Committee on Rules and Administration\nRESOLUTION\nProhibiting the use of funds for travel by Senators to or from their residence during Government shutdowns.\n#### 1. Prohibition on use of funds for travel by Senators to or from their residence during Government shutdowns\nAmounts made available to a Senator from the Senators\u2019 Official Personnel and Office Expense Account may not be obligated or expended to directly pay for, or reimburse a Senator for, the cost of travel by the Senator between the seat of Government and the primary residence of the Senator during a period during which there is a lapse in appropriations for 1 or more Federal agencies.",
      "versionDate": "2026-04-16",
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
        "name": "Congress",
        "updateDate": "2026-04-24T15:46:57Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres678is.xml"
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
      "title": "A resolution prohibiting the use of funds for travel by Senators to or from their residence during Government shutdowns.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T05:48:28Z"
    },
    {
      "title": "A resolution prohibiting the use of funds for travel by Senators to or from their residence during Government shutdowns.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T14:15:16Z"
    }
  ]
}
```
