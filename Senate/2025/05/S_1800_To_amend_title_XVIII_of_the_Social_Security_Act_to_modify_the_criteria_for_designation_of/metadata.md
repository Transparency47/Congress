# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1800?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1800
- Title: Rural Health Sustainability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1800
- Origin chamber: Senate
- Introduced date: 2025-05-19
- Update date: 2025-05-30T13:08:54Z
- Update date including text: 2025-05-30T13:08:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in Senate
- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-19: Introduced in Senate

## Actions

- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1800",
    "number": "1800",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Rural Health Sustainability Act of 2025",
    "type": "S",
    "updateDate": "2025-05-30T13:08:54Z",
    "updateDateIncludingText": "2025-05-30T13:08:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T20:37:26Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1800is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1800\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2025 Mrs. Hyde-Smith introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to modify the criteria for designation of rural emergency hospitals.\n#### 1. Short title\nThis Act may be cited as the Rural Health Sustainability Act of 2025 .\n#### 2. Modification of criteria for designation of rural emergency hospitals\nSection 1861(kkk)(3) of the Social Security Act ( 42 U.S.C. 1395x(kkk)(3) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking as of the date of the enactment of this subsection and inserting as of January 1, 2014 ;\n**(2)**\nin subparagraph (A), by striking or at the end;\n**(3)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(C) was designated as rural by the Office of Rural Health Policy of the Health Resources and Services Administration. .",
      "versionDate": "2025-05-19",
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
        "updateDate": "2025-05-30T13:08:54Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1800is.xml"
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
      "title": "Rural Health Sustainability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-29T01:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Health Sustainability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to modify the criteria for designation of rural emergency hospitals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:03:31Z"
    }
  ]
}
```
