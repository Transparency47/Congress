# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4637?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4637
- Title: A bill to increase by 5 the number of flex waivers available in each State for J-1 nonimmigrants and to establish a secondary physician match portal to assist alien physicians who are unable to find employment in their preferred State of residence to find employment in another State.
- Congress: 119
- Bill type: S
- Bill number: 4637
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:56:35Z
- Update date including text: 2026-05-22T10:56:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-21: Introduced in Senate

## Actions

- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4637",
    "number": "4637",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "A bill to increase by 5 the number of flex waivers available in each State for J-1 nonimmigrants and to establish a secondary physician match portal to assist alien physicians who are unable to find employment in their preferred State of residence to find employment in another State.",
    "type": "S",
    "updateDate": "2026-05-22T10:56:35Z",
    "updateDateIncludingText": "2026-05-22T10:56:35Z"
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
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
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
          "date": "2026-05-21T18:20:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "MN"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A bill to increase by 5 the number of flex waivers available in each State for J-1 nonimmigrants and to establish a secondary physician match portal to assist alien physicians who are unable to find employment in their preferred State of residence to find employment in another State.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:35Z"
    },
    {
      "title": "A bill to increase by 5 the number of flex waivers available in each State for J-1 nonimmigrants and to establish a secondary physician match portal to assist alien physicians who are unable to find employment in their preferred State of residence to find employment in another State.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:56:35Z"
    }
  ]
}
```
