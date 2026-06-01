# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1896?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1896
- Title: A bill to modify the provision of law on expedited review of export licenses for exports of advanced technologies to Australia, the United Kingdom, and Canada.
- Congress: 119
- Bill type: S
- Bill number: 1896
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-06-23T17:46:48Z
- Update date including text: 2025-06-23T17:46:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1896",
    "number": "1896",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "A bill to modify the provision of law on expedited review of export licenses for exports of advanced technologies to Australia, the United Kingdom, and Canada.",
    "type": "S",
    "updateDate": "2025-06-23T17:46:48Z",
    "updateDateIncludingText": "2025-06-23T17:46:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T18:48:59Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1896is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1896\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Cornyn (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo modify the provision of law on expedited review of export licenses for exports of advanced technologies to Australia, the United Kingdom, and Canada.\n#### 1. Modification of expedited review of export licenses for exports of advanced technologies to Australia, the United Kingdom, and Canada\nSection 1344 of the National Defense Authorization Act for Fiscal Year 2024 ( 22 U.S.C. 10423 ) is amended by adding at the end the following:\n(d) Export defined In this section, the term export includes, and applies with respect to, all transfers of defense articles and defense services described in subsection (a), including reexports, retransfers, third party transfers, temporary imports, and brokering activities of such articles and services. .",
      "versionDate": "2025-05-22",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-06-23T17:46:48Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1896is.xml"
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
      "title": "A bill to modify the provision of law on expedited review of export licenses for exports of advanced technologies to Australia, the United Kingdom, and Canada.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:48Z"
    },
    {
      "title": "A bill to modify the provision of law on expedited review of export licenses for exports of advanced technologies to Australia, the United Kingdom, and Canada.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T10:56:18Z"
    }
  ]
}
```
