# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4532?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4532
- Title: Small Business Wildfire Smoke Recovery Act
- Congress: 119
- Bill type: S
- Bill number: 4532
- Origin chamber: Senate
- Introduced date: 2026-05-14
- Update date: 2026-05-29T15:29:56Z
- Update date including text: 2026-05-29T15:29:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in Senate
- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2026-05-14: Introduced in Senate

## Actions

- 2026-05-14 - IntroReferral: Introduced in Senate
- 2026-05-14 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4532",
    "number": "4532",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Small Business Wildfire Smoke Recovery Act",
    "type": "S",
    "updateDate": "2026-05-29T15:29:56Z",
    "updateDateIncludingText": "2026-05-29T15:29:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T16:56:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4532is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4532\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2026 Ms. Cortez Masto introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo include smoke in the definition of disaster in the Small Business Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Wildfire Smoke Recovery Act .\n#### 2. Definition of disaster\nSection 3(k)(2) of the Small Business Act ( 15 U.S.C. 632(k)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end;\n**(2)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(D) smoke. .",
      "versionDate": "2026-05-14",
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
        "name": "Commerce",
        "updateDate": "2026-05-29T15:29:56Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4532is.xml"
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
      "title": "Small Business Wildfire Smoke Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Business Wildfire Smoke Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to include smoke in the definition of disaster in the Small Business Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:44Z"
    }
  ]
}
```
