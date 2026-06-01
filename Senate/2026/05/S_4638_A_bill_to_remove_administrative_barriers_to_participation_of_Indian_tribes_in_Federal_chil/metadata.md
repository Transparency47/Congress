# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4638?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4638
- Title: A bill to remove administrative barriers to participation of Indian tribes in Federal child welfare programs, and increase Federal funding for tribal child welfare programs, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4638
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:56:28Z
- Update date including text: 2026-05-22T10:56:28Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4638",
    "number": "4638",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A bill to remove administrative barriers to participation of Indian tribes in Federal child welfare programs, and increase Federal funding for tribal child welfare programs, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-22T10:56:28Z",
    "updateDateIncludingText": "2026-05-22T10:56:28Z"
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
          "date": "2026-05-21T18:35:36Z",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "HI"
    },
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
      "title": "A bill to remove administrative barriers to participation of Indian tribes in Federal child welfare programs, and increase Federal funding for tribal child welfare programs, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:28Z"
    },
    {
      "title": "A bill to remove administrative barriers to participation of Indian tribes in Federal child welfare programs, and increase Federal funding for tribal child welfare programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:56:28Z"
    }
  ]
}
```
