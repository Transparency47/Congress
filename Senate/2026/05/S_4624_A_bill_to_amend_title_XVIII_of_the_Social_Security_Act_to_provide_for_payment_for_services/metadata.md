# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4624?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4624
- Title: A bill to amend title XVIII of the Social Security Act to provide for payment for services of radiologist assistants under the Medicare program, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4624
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:56:29Z
- Update date including text: 2026-05-22T10:56:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-21: Introduced in Senate

## Actions

- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Finance.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4624",
    "number": "4624",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001236",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Boozman, John [R-AR]",
        "lastName": "Boozman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "A bill to amend title XVIII of the Social Security Act to provide for payment for services of radiologist assistants under the Medicare program, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-22T10:56:29Z",
    "updateDateIncludingText": "2026-05-22T10:56:29Z"
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
          "date": "2026-05-21T16:28:57Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NM"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to amend title XVIII of the Social Security Act to provide for payment for services of radiologist assistants under the Medicare program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:29Z"
    },
    {
      "title": "A bill to amend title XVIII of the Social Security Act to provide for payment for services of radiologist assistants under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:56:29Z"
    }
  ]
}
```
