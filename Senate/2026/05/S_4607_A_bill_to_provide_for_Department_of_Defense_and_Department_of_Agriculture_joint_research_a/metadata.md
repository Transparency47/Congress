# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4607
- Title: A bill to provide for Department of Defense and Department of Agriculture joint research and development activities, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4607
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-21T10:56:32Z
- Update date including text: 2026-05-21T10:56:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4607",
    "number": "4607",
    "originChamber": "Senate",
    "policyArea": {},
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
    "title": "A bill to provide for Department of Defense and Department of Agriculture joint research and development activities, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-21T10:56:32Z",
    "updateDateIncludingText": "2026-05-21T10:56:32Z"
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
          "date": "2026-05-20T21:12:18Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NC"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to provide for Department of Defense and Department of Agriculture joint research and development activities, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T10:56:32Z"
    },
    {
      "title": "A bill to provide for Department of Defense and Department of Agriculture joint research and development activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T10:56:32Z"
    }
  ]
}
```
