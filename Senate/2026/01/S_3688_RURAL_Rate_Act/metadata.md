# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3688?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3688
- Title: RURAL Rate Act
- Congress: 119
- Bill type: S
- Bill number: 3688
- Origin chamber: Senate
- Introduced date: 2026-01-15
- Update date: 2026-02-11T17:28:38Z
- Update date including text: 2026-02-11T17:28:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in Senate
- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-15: Introduced in Senate

## Actions

- 2026-01-15 - IntroReferral: Introduced in Senate
- 2026-01-15 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3688",
    "number": "3688",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "RURAL Rate Act",
    "type": "S",
    "updateDate": "2026-02-11T17:28:38Z",
    "updateDateIncludingText": "2026-02-11T17:28:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T22:05:38Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3688is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3688\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2026 Mr. Sullivan introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to increase the floor for the practice expense and work geographic indices for certain areas.\n#### 1. Short title\nThis Act may be cited as the Rural Underpayment Remedy through Adjusted Local Rate Act or the RURAL Rate Act .\n#### 2. Increase of the floor for practice expense and work geographic indices for certain areas\nSection 1848(e)(1)(G) of the Social Security Act ( 42 U.S.C. 1395w\u20134(e)(1)(G) ) is amended\u2014\n**(1)**\nin the second sentence\u2014\n**(A)**\nby inserting and before January 1, 2026, after January 1, 2009, ; and\n**(B)**\nby inserting a period at the end; and\n**(2)**\nby adding at the end the following new sentence: For purposes of payment for services furnished in the State described in the first sentence on or after January 1, 2026, after calculating the practice expense and work geographic indices in clauses (i) and (iii) of subparagraph (A) and in subparagraph (B), the Secretary shall increase either such index to 1.67 if such index would otherwise be less than 1.67. .",
      "versionDate": "2026-01-15",
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
        "name": "Social Welfare",
        "updateDate": "2026-02-11T17:28:38Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3688is.xml"
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
      "title": "RURAL Rate Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RURAL Rate Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Underpayment Remedy through Adjusted Local Rate Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to increase the floor for the practice expense and work geographic indices for certain areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:18Z"
    }
  ]
}
```
