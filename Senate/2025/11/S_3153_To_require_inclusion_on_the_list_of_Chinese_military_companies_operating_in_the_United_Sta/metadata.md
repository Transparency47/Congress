# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3153
- Title: CLEAR Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3153
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2025-11-25T19:10:37Z
- Update date including text: 2025-11-25T19:10:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3153",
    "number": "3153",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "CLEAR Act of 2025",
    "type": "S",
    "updateDate": "2025-11-25T19:10:37Z",
    "updateDateIncludingText": "2025-11-25T19:10:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T18:07:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3153is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3153\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require inclusion on the list of Chinese military companies operating in the United States of Chinese entities on certain other lists maintained by the United States Government.\n#### 1. Short title\nThis Act may be cited as the Chinese List Entity Alignment and Review Act of 2025 or the CLEAR Act of 2025 .\n#### 2. Inclusion on list of Chinese military companies of Chinese entities on other lists\nSection 1260H(b)(3) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note) is amended\u2014\n**(1)**\nby striking The Secretary and inserting the following:\n(A) In general The Secretary ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) Review of entities on other lists The Secretary shall review, for inclusion in each annual revision under subparagraph (A) of the list required by paragraph (1), each entity added, during the year preceding preparation of the revision of the list, to any other list maintained by the United States Government of Chinese entities subject to restrictions or scrutiny relating to concerns about their activities or affiliations. .",
      "versionDate": "2025-11-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T19:10:37Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3153is.xml"
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
      "title": "CLEAR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CLEAR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chinese List Entity Alignment and Review Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require inclusion on the list of Chinese military companies operating in the United States of Chinese entities on certain other lists maintained by the United States Government.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:29Z"
    }
  ]
}
```
