# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8930?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8930
- Title: To assess the biotechnology workforce needs of certain Federal agencies, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8930
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-21T08:08:13Z
- Update date including text: 2026-05-21T15:43:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8930",
    "number": "8930",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To assess the biotechnology workforce needs of certain Federal agencies, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:13Z",
    "updateDateIncludingText": "2026-05-21T15:43:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-05-20T15:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "GA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "TX"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To assess the biotechnology workforce needs of certain Federal agencies, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:08:13Z"
    },
    {
      "title": "To assess the biotechnology workforce needs of certain Federal agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T08:08:13Z"
    }
  ]
}
```
