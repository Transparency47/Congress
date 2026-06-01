# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8901?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8901
- Title: To prohibit certain federally funded research collaborations with certain foreign entities, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8901
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-20T08:07:05Z
- Update date including text: 2026-05-20T16:13:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8901",
    "number": "8901",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "To prohibit certain federally funded research collaborations with certain foreign entities, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:05Z",
    "updateDateIncludingText": "2026-05-20T16:13:28Z"
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
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
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
          "date": "2026-05-19T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "title": "To prohibit certain federally funded research collaborations with certain foreign entities, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:07:05Z"
    },
    {
      "title": "To prohibit certain federally funded research collaborations with certain foreign entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:07:05Z"
    }
  ]
}
```
