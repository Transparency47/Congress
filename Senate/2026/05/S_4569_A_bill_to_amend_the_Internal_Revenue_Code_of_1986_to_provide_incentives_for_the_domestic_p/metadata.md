# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4569?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4569
- Title: A bill to amend the Internal Revenue Code of 1986 to provide incentives for the domestic production of printed circuit boards.
- Congress: 119
- Bill type: S
- Bill number: 4569
- Origin chamber: Senate
- Introduced date: 2026-05-19
- Update date: 2026-05-20T10:56:35Z
- Update date including text: 2026-05-20T10:56:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-19: Introduced in Senate
- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-19: Introduced in Senate

## Actions

- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Finance.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4569",
    "number": "4569",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to provide incentives for the domestic production of printed circuit boards.",
    "type": "S",
    "updateDate": "2026-05-20T10:56:35Z",
    "updateDateIncludingText": "2026-05-20T10:56:35Z"
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
          "date": "2026-05-19T20:09:22Z",
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
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "WV"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide incentives for the domestic production of printed circuit boards.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T10:56:35Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide incentives for the domestic production of printed circuit boards.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T10:56:35Z"
    }
  ]
}
```
