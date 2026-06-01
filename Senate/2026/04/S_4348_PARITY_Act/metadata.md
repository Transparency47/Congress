# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4348?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4348
- Title: PARITY Act
- Congress: 119
- Bill type: S
- Bill number: 4348
- Origin chamber: Senate
- Introduced date: 2026-04-20
- Update date: 2026-05-12T15:51:33Z
- Update date including text: 2026-05-12T15:51:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in Senate
- 2026-04-20 - IntroReferral: Introduced in Senate
- 2026-04-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-20: Introduced in Senate

## Actions

- 2026-04-20 - IntroReferral: Introduced in Senate
- 2026-04-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4348",
    "number": "4348",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "PARITY Act",
    "type": "S",
    "updateDate": "2026-05-12T15:51:33Z",
    "updateDateIncludingText": "2026-05-12T15:51:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T21:38:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4348is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4348\nIN THE SENATE OF THE UNITED STATES\nApril 20, 2026 Mr. Banks introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo repeal the 90/10 rule as it pertains to proprietary schools under title IV of the Higher Education Act of 1965.\n#### 1. Short title\nThis Act may be cited as the Promoting Access and Revenue Integrity Through Institutional Transparency Act or the PARITY Act .\n#### 2. Regulatory relief\nSection 487 of the Higher Education Act of 1965 ( 20 U.S.C. 1094 ) is amended\u2014\n**(1)**\nin subsection (a), by repealing paragraph (24); and\n**(2)**\nby repealing subsection (d).",
      "versionDate": "2026-04-20",
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
        "name": "Education",
        "updateDate": "2026-05-12T15:51:33Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4348is.xml"
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
      "title": "PARITY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:36Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PARITY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Access and Revenue Integrity Through Institutional Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the 90/10 rule as it pertains to proprietary schools under title IV of the Higher Education Act of 1965.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:50Z"
    }
  ]
}
```
