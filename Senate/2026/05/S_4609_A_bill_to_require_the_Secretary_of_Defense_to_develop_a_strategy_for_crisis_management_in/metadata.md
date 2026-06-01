# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4609?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4609
- Title: A bill to require the Secretary of Defense to develop a strategy for crisis management in the South China Sea, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4609
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-21T10:56:34Z
- Update date including text: 2026-05-21T10:56:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4609",
    "number": "4609",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A bill to require the Secretary of Defense to develop a strategy for crisis management in the South China Sea, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-21T10:56:34Z",
    "updateDateIncludingText": "2026-05-21T10:56:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
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
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T21:39:23Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "UT"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to require the Secretary of Defense to develop a strategy for crisis management in the South China Sea, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T10:56:34Z"
    },
    {
      "title": "A bill to require the Secretary of Defense to develop a strategy for crisis management in the South China Sea, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T10:56:34Z"
    }
  ]
}
```
