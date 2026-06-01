# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4571?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4571
- Title: A bill to require the Environmental Protection Agency to establish a tropospheric ozone research program, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4571
- Origin chamber: Senate
- Introduced date: 2026-05-19
- Update date: 2026-05-20T10:56:37Z
- Update date including text: 2026-05-20T10:56:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-19: Introduced in Senate
- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-05-19: Introduced in Senate

## Actions

- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4571",
    "number": "4571",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "A bill to require the Environmental Protection Agency to establish a tropospheric ozone research program, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-20T10:56:37Z",
    "updateDateIncludingText": "2026-05-20T10:56:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-19",
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
          "date": "2026-05-19T20:28:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "HI"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to require the Environmental Protection Agency to establish a tropospheric ozone research program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T10:56:37Z"
    },
    {
      "title": "A bill to require the Environmental Protection Agency to establish a tropospheric ozone research program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T10:56:37Z"
    }
  ]
}
```
