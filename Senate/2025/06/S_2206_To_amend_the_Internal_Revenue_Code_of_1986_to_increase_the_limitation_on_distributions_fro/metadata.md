# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2206?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2206
- Title: A bill to amend the Internal Revenue Code of 1986 to increase the limitation on distributions from 529 accounts for qualified higher education expenses.
- Congress: 119
- Bill type: S
- Bill number: 2206
- Origin chamber: Senate
- Introduced date: 2025-06-30
- Update date: 2025-07-17T19:16:58Z
- Update date including text: 2025-07-17T19:16:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-30: Introduced in Senate
- 2025-06-30 - IntroReferral: Introduced in Senate
- 2025-06-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-30: Introduced in Senate

## Actions

- 2025-06-30 - IntroReferral: Introduced in Senate
- 2025-06-30 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2206",
    "number": "2206",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to increase the limitation on distributions from 529 accounts for qualified higher education expenses.",
    "type": "S",
    "updateDate": "2025-07-17T19:16:58Z",
    "updateDateIncludingText": "2025-07-17T19:16:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-30",
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
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T23:17:44Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2206is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2206\nIN THE SENATE OF THE UNITED STATES\nJune 30, 2025 Mr. Schmitt introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the limitation on distributions from 529 accounts for qualified higher education expenses.\n#### 1. Increase in limitation for qualified higher education expenses from 529 accounts\n##### (a) In general\nThe last sentence of section 529(e)(3) of the Internal Revenue Code of 1986 is amended by striking $10,000 and inserting $20,000 .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-06-30",
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
        "name": "Taxation",
        "updateDate": "2025-07-17T19:16:58Z"
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
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2206is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the limitation on distributions from 529 accounts for qualified higher education expenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:18Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the limitation on distributions from 529 accounts for qualified higher education expenses.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T21:28:33Z"
    }
  ]
}
```
