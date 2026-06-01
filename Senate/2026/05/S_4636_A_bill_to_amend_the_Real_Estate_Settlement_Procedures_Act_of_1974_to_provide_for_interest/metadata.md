# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4636?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4636
- Title: A bill to amend the Real Estate Settlement Procedures Act of 1974 to provide for interest on escrow balances.
- Congress: 119
- Bill type: S
- Bill number: 4636
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:56:33Z
- Update date including text: 2026-05-22T10:56:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-05-21: Introduced in Senate

## Actions

- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4636",
    "number": "4636",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A bill to amend the Real Estate Settlement Procedures Act of 1974 to provide for interest on escrow balances.",
    "type": "S",
    "updateDate": "2026-05-22T10:56:33Z",
    "updateDateIncludingText": "2026-05-22T10:56:33Z"
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
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
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
          "date": "2026-05-21T18:17:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "MA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to amend the Real Estate Settlement Procedures Act of 1974 to provide for interest on escrow balances.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:33Z"
    },
    {
      "title": "A bill to amend the Real Estate Settlement Procedures Act of 1974 to provide for interest on escrow balances.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:56:33Z"
    }
  ]
}
```
