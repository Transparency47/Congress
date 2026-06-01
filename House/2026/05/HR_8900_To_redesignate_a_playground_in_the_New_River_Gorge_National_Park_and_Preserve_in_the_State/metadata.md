# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8900?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8900
- Title: To redesignate a playground in the New River Gorge National Park and Preserve in the State of West Virginia as the "Hearts of Gold Playground: In Honor of West Virginia Children and Families Impacted by Childhood Cancer".
- Congress: 119
- Bill type: HR
- Bill number: 8900
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-20T08:07:17Z
- Update date including text: 2026-05-20T16:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Natural Resources.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8900",
    "number": "8900",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "To redesignate a playground in the New River Gorge National Park and Preserve in the State of West Virginia as the \"Hearts of Gold Playground: In Honor of West Virginia Children and Families Impacted by Childhood Cancer\".",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:17Z",
    "updateDateIncludingText": "2026-05-20T16:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
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
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
          "date": "2026-05-19T16:04:05Z",
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
      "title": "To redesignate a playground in the New River Gorge National Park and Preserve in the State of West Virginia as the \"Hearts of Gold Playground: In Honor of West Virginia Children and Families Impacted by Childhood Cancer\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:07:17Z"
    },
    {
      "title": "To redesignate a playground in the New River Gorge National Park and Preserve in the State of West Virginia as the \"Hearts of Gold Playground: In Honor of West Virginia Children and Families Impacted by Childhood Cancer\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:07:17Z"
    }
  ]
}
```
