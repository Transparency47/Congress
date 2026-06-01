# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4520?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4520
- Title: LNG Export Security Act
- Congress: 119
- Bill type: S
- Bill number: 4520
- Origin chamber: Senate
- Introduced date: 2026-05-13
- Update date: 2026-05-29T16:55:26Z
- Update date including text: 2026-05-29T16:55:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-13: Introduced in Senate
- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-05-13: Introduced in Senate

## Actions

- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4520",
    "number": "4520",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
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
    "title": "LNG Export Security Act",
    "type": "S",
    "updateDate": "2026-05-29T16:55:26Z",
    "updateDateIncludingText": "2026-05-29T16:55:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T20:51:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4520is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4520\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2026 Mr. Cornyn (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Natural Gas Act to include a definition of the term public interest , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the LNG Export Security Act .\n#### 2. Definition of the term public interest under the Natural Gas Act\nSection 2 of the Natural Gas Act ( 15 U.S.C. 717a ) is amended by adding at the end the following:\n(12) Public interest means the consideration of\u2014 (A) the development of\u2014 (i) natural gas facilities in the United States; and (ii) the domestic natural gas supply; (B) domestic economic interests; and (C) national security interests. .",
      "versionDate": "2026-05-13",
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
        "name": "Energy",
        "updateDate": "2026-05-29T16:55:26Z"
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
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4520is.xml"
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
      "title": "LNG Export Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LNG Export Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Natural Gas Act to include a definition of the term \"public interest\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:39Z"
    }
  ]
}
```
