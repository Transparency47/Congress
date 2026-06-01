# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4606?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4606
- Title: A bill to amend the Internal Revenue Code of 1986 to permit certain population census tracts containing former military installations to be designated as qualified opportunity zones.
- Congress: 119
- Bill type: S
- Bill number: 4606
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-21T10:56:29Z
- Update date including text: 2026-05-21T10:56:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4606",
    "number": "4606",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to permit certain population census tracts containing former military installations to be designated as qualified opportunity zones.",
    "type": "S",
    "updateDate": "2026-05-21T10:56:29Z",
    "updateDateIncludingText": "2026-05-21T10:56:29Z"
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
          "date": "2026-05-20T21:01:48Z",
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
      "sponsorshipDate": "2026-05-20",
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
      "title": "A bill to amend the Internal Revenue Code of 1986 to permit certain population census tracts containing former military installations to be designated as qualified opportunity zones.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T10:56:29Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to permit certain population census tracts containing former military installations to be designated as qualified opportunity zones.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T10:56:29Z"
    }
  ]
}
```
