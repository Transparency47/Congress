# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9019?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9019
- Title: To direct the Secretary of Energy to report to Congress on the use of electric energy and water by certain data centers, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9019
- Origin chamber: House
- Introduced date: 2026-05-22
- Update date: 2026-05-23T08:07:21Z
- Update date including text: 2026-05-27T05:58:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-22: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-22: Introduced in House

## Actions

- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-22",
    "latestAction": {
      "actionDate": "2026-05-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9019",
    "number": "9019",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To direct the Secretary of Energy to report to Congress on the use of electric energy and water by certain data centers, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:21Z",
    "updateDateIncludingText": "2026-05-27T05:58:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-22",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-22",
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
          "date": "2026-05-22T14:30:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "title": "To direct the Secretary of Energy to report to Congress on the use of electric energy and water by certain data centers, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-23T08:07:21Z"
    },
    {
      "title": "To direct the Secretary of Energy to report to Congress on the use of electric energy and water by certain data centers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-23T08:07:21Z"
    }
  ]
}
```
