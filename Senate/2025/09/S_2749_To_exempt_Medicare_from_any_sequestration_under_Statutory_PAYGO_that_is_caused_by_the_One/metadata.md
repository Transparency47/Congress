# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2749?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2749
- Title: A bill to exempt Medicare from any sequestration under Statutory PAYGO that is caused by the One Big Beautiful Bill Act.
- Congress: 119
- Bill type: S
- Bill number: 2749
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2025-09-23T15:54:29Z
- Update date including text: 2025-09-23T15:54:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on the Budget.
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2749",
    "number": "2749",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
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
    "title": "A bill to exempt Medicare from any sequestration under Statutory PAYGO that is caused by the One Big Beautiful Bill Act.",
    "type": "S",
    "updateDate": "2025-09-23T15:54:29Z",
    "updateDateIncludingText": "2025-09-23T15:54:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "ssbu00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T23:16:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Budget Committee",
      "systemCode": "ssbu00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2749is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2749\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Mr. Whitehouse introduced the following bill; which was read twice and referred to the Committee on the Budget\nA BILL\nTo exempt Medicare from any sequestration under Statutory PAYGO that is caused by the One Big Beautiful Bill Act.\n#### 1. Exemption of Medicare from Statutory PAYGO sequestration caused by the One Big Beautiful Bill Act\nThe Medicare programs under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) shall be exempt from reduction under any sequestration order issued on or after the date of enactment of this Act under section 5 of the Statutory Pay-As-You-Go Act of 2010 ( 2 U.S.C. 934 ) that is attributable, in whole or in part, to the budgetary effects of the Act entitled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 , approved July 4, 2025 ( Public Law 119\u201321 ; 139 Stat. 72) (commonly known as the One Big Beautiful Bill Act ).",
      "versionDate": "2025-09-09",
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
        "updateDate": "2025-09-23T15:54:29Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2749is.xml"
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
      "title": "A bill to exempt Medicare from any sequestration under Statutory PAYGO that is caused by the One Big Beautiful Bill Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:48:33Z"
    },
    {
      "title": "A bill to exempt Medicare from any sequestration under Statutory PAYGO that is caused by the One Big Beautiful Bill Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-10T10:56:21Z"
    }
  ]
}
```
