# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3642?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3642
- Title: WALZ Act
- Congress: 119
- Bill type: S
- Bill number: 3642
- Origin chamber: Senate
- Introduced date: 2026-01-14
- Update date: 2026-02-11T17:15:46Z
- Update date including text: 2026-02-11T17:15:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in Senate
- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-14: Introduced in Senate

## Actions

- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3642",
    "number": "3642",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "WALZ Act",
    "type": "S",
    "updateDate": "2026-02-11T17:15:46Z",
    "updateDateIncludingText": "2026-02-11T17:15:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T20:12:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3642is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3642\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2026 Mr. Marshall introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo direct the Inspector General of the Department of Health and Human Services to investigate certain payment increases under State programs funded by the Department of Health and Human Services.\n#### 1. Short title\nThis Act may be cited as the Welfare Abuse and Laundering Zillions Act or the WALZ Act .\n#### 2. Requiring investigations of certain payment increases under State programs funded by the Department of Health and Human Services\nIn the case that the total amount paid to providers of services and suppliers under a State program that receives Federal financial assistance administered by the Secretary of Health and Human Services during any 6-month period increases by 10 percent or more as compared to that amount during the prior 6-month period, the Inspector General of the Department of Health and Human Services shall open an investigation into such program.",
      "versionDate": "2026-01-14",
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
        "name": "Health",
        "updateDate": "2026-02-11T17:15:46Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3642is.xml"
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
      "title": "WALZ Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WALZ Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Welfare Abuse and Laundering Zillions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Inspector General of the Department of Health and Human Services to investigate certain payment increases under State programs funded by the Department of Health and Human Services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:29Z"
    }
  ]
}
```
