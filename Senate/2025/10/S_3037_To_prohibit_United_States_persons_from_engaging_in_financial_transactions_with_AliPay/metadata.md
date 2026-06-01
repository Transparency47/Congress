# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3037?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3037
- Title: No AliPay Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3037
- Origin chamber: Senate
- Introduced date: 2025-10-23
- Update date: 2025-12-04T18:01:41Z
- Update date including text: 2025-12-04T18:01:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-23: Introduced in Senate
- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-10-23: Introduced in Senate

## Actions

- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-23",
    "latestAction": {
      "actionDate": "2025-10-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3037",
    "number": "3037",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "No AliPay Act of 2025",
    "type": "S",
    "updateDate": "2025-12-04T18:01:41Z",
    "updateDateIncludingText": "2025-12-04T18:01:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-23",
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
      "actionDate": "2025-10-23",
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
          "date": "2025-10-23T15:07:44Z",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "AL"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3037is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3037\nIN THE SENATE OF THE UNITED STATES\nOctober 23, 2025 Mr. Scott of Florida (for himself, Mr. Tuberville , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit United States persons from engaging in financial transactions with AliPay.\n#### 1. Short title\nThis Act may be cited as the No AliPay Act of 2025 .\n#### 2. Prohibition on use of AliPay\n##### (a) In general\nA United States person may not conduct a financial transaction with AliPay (China) Internet Technology Company Limited (referred to in this Act as AliPay ), including by using any application or payment processing service operated by AliPay.\n##### (b) Definitions\nIn this section:\n**(1) Financial transaction**\nThe term financial transaction means\u2014\n**(A)**\na transaction that in any way or degree affects interstate or foreign commerce\u2014\n**(i)**\ninvolving the movement of funds by wire or other means; or\n**(ii)**\ninvolving one or more monetary instruments; or\n**(B)**\na transaction involving the use of a financial institution that is engaged in, or the activities of which affect, interstate or foreign commerce in any way or degree.\n**(2) United States person**\nThe term United States person means\u2014\n**(A)**\na national of the United States;\n**(B)**\nan alien lawfully admitted for permanent residence;\n**(C)**\nan entity organized under the laws of the United States or under the laws of any jurisdiction within the United States (including a foreign branch of such an entity); or\n**(D)**\nan individual who is physically present in the United States.",
      "versionDate": "2025-10-23",
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
        "updateDate": "2025-12-04T18:01:41Z"
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
      "date": "2025-10-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3037is.xml"
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
      "title": "No AliPay Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T06:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No AliPay Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-29T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit United States persons from engaging in financial transactions with AliPay.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-29T06:03:20Z"
    }
  ]
}
```
