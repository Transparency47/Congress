# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8801?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8801
- Title: To prohibit a congestion toll in the District of Columbia.
- Congress: 119
- Bill type: HR
- Bill number: 8801
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-22T08:07:44Z
- Update date including text: 2026-05-22T08:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 22 - 18.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 22 - 18.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8801",
    "number": "8801",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "To prohibit a congestion toll in the District of Columbia.",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:44Z",
    "updateDateIncludingText": "2026-05-22T08:07:44Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 22 - 18.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
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
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
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
        "item": [
          {
            "date": "2026-05-20T13:22:23Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-13T14:01:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To prohibit a congestion toll in the District of Columbia.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T08:07:46Z"
    },
    {
      "title": "To prohibit a congestion toll in the District of Columbia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T08:07:46Z"
    }
  ]
}
```
