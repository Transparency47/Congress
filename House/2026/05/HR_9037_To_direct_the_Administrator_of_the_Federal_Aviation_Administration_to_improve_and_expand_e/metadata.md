# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9037?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9037
- Title: To direct the Administrator of the Federal Aviation Administration to improve and expand electronic filing capabilities for Federal Aviation Administration Form 337, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9037
- Origin chamber: House
- Introduced date: 2026-05-26
- Update date: 2026-05-27T08:06:15Z
- Update date including text: 2026-05-27T09:43:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-26: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-05-26: Introduced in House

## Actions

- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-26",
    "latestAction": {
      "actionDate": "2026-05-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9037",
    "number": "9037",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To direct the Administrator of the Federal Aviation Administration to improve and expand electronic filing capabilities for Federal Aviation Administration Form 337, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:15Z",
    "updateDateIncludingText": "2026-05-27T09:43:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-26",
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
          "date": "2026-05-26T15:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "title": "To direct the Administrator of the Federal Aviation Administration to improve and expand electronic filing capabilities for Federal Aviation Administration Form 337, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:06:15Z"
    },
    {
      "title": "To direct the Administrator of the Federal Aviation Administration to improve and expand electronic filing capabilities for Federal Aviation Administration Form 337, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:06:15Z"
    }
  ]
}
```
