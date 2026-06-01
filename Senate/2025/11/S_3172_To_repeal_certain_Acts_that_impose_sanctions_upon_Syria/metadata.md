# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3172
- Title: A bill to repeal certain Acts that impose sanctions upon Syria.
- Congress: 119
- Bill type: S
- Bill number: 3172
- Origin chamber: Senate
- Introduced date: 2025-11-10
- Update date: 2025-11-20T17:35:12Z
- Update date including text: 2025-11-20T17:35:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in Senate
- 2025-11-10 - IntroReferral: Introduced in Senate
- 2025-11-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-11-10: Introduced in Senate

## Actions

- 2025-11-10 - IntroReferral: Introduced in Senate
- 2025-11-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3172",
    "number": "3172",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "A bill to repeal certain Acts that impose sanctions upon Syria.",
    "type": "S",
    "updateDate": "2025-11-20T17:35:12Z",
    "updateDateIncludingText": "2025-11-20T17:35:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-10",
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
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T22:11:46Z",
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
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "OK"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3172is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3172\nIN THE SENATE OF THE UNITED STATES\nNovember 10, 2025 Mrs. Shaheen (for herself, Mr. Mullin , and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo repeal certain Acts that impose sanctions upon Syria.\n#### 1. Repeals\n##### (a) Syria Accountability and Lebanese Sovereignty Restoration Act of 2003\nThe Syria Accountability and Lebanese Sovereignty Restoration Act of 2003 ( Public Law 108\u2013175 ; 22 U.S.C. 2151 note) is repealed.\n##### (b) Syria Human Rights Accountability Act of 2012\nThe Syria Human Rights Accountability Act of 2012 (title VII of Public Law 112\u2013158 ; 22 U.S.C. 8701 et seq. ) is repealed.",
      "versionDate": "2025-11-10",
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
        "updateDate": "2025-11-20T17:35:12Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3172is.xml"
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
      "title": "A bill to repeal certain Acts that impose sanctions upon Syria.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:17Z"
    },
    {
      "title": "A bill to repeal certain Acts that impose sanctions upon Syria.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T11:56:16Z"
    }
  ]
}
```
