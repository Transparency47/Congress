# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3748?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3748
- Title: Terminate Unaccountable Spending, Abuse, Deception, and Fraud Act
- Congress: 119
- Bill type: S
- Bill number: 3748
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-23T23:11:02Z
- Update date including text: 2026-02-23T23:11:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3748",
    "number": "3748",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Terminate Unaccountable Spending, Abuse, Deception, and Fraud Act",
    "type": "S",
    "updateDate": "2026-02-23T23:11:02Z",
    "updateDateIncludingText": "2026-02-23T23:11:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T23:40:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3748is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3748\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo terminate the United States African Development Foundation.\n#### 1. Short title\nThis Act may be cited as the Terminate Unaccountable Spending, Abuse, Deception, and Fraud Act .\n#### 2. Termination of the United States African Development Foundation\n##### (a) Repeal\nThe African Development Foundation Act (title V of Public Law 96\u2013533 ; 22 U.S.C. 290h et seq. ) is repealed.\n##### (b) Conforming amendments\n**(1) Trade and development act of 2000**\nSection 127(b) of the Trade and Development Act of 2000 ( 19 U.S.C. 3737(b) ) is amended by striking paragraph (4).\n**(2) Foreign assistance act of 1961**\nSection 620(q)(2) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2370(q)(2) ) is amended by striking the African Development Foundation Act, .\n**(3) Global food security act of 2016**\nSection 4(8) of the Global Food Security Act of 2016 ( 22 U.S.C. 9303(8) ) is amended by striking the United States African Development Foundation, .",
      "versionDate": "2026-01-29",
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
        "name": "International Affairs",
        "updateDate": "2026-02-23T23:11:02Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3748is.xml"
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
      "title": "Terminate Unaccountable Spending, Abuse, Deception, and Fraud Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Terminate Unaccountable Spending, Abuse, Deception, and Fraud Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to terminate the United States African Development Foundation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:23Z"
    }
  ]
}
```
