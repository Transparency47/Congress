# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4622?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4622
- Title: A bill to amend the Fair Credit Reporting Act to prohibit the inclusion of medical debt on a consumer report, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4622
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:56:32Z
- Update date including text: 2026-05-22T10:56:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-05-21: Introduced in Senate

## Actions

- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4622",
    "number": "4622",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A bill to amend the Fair Credit Reporting Act to prohibit the inclusion of medical debt on a consumer report, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-22T10:56:32Z",
    "updateDateIncludingText": "2026-05-22T10:56:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
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
      "actionDate": "2026-05-21",
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
          "date": "2026-05-21T16:21:34Z",
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

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to amend the Fair Credit Reporting Act to prohibit the inclusion of medical debt on a consumer report, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:32Z"
    },
    {
      "title": "A bill to amend the Fair Credit Reporting Act to prohibit the inclusion of medical debt on a consumer report, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:56:32Z"
    }
  ]
}
```
