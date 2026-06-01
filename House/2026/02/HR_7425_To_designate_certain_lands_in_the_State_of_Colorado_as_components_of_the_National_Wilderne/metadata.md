# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7425?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7425
- Title: To designate certain lands in the State of Colorado as components of the National Wilderness Preservation System, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 7425
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-10T09:05:39Z
- Update date including text: 2026-02-10T09:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7425",
    "number": "7425",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "D000197",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. DeGette, Diana [D-CO-1]",
        "lastName": "DeGette",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "To designate certain lands in the State of Colorado as components of the National Wilderness Preservation System, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-10T09:05:39Z",
    "updateDateIncludingText": "2026-02-10T09:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "title": "To designate certain lands in the State of Colorado as components of the National Wilderness Preservation System, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T09:05:39Z"
    },
    {
      "title": "To designate certain lands in the State of Colorado as components of the National Wilderness Preservation System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T09:05:39Z"
    }
  ]
}
```
