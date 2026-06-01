# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9045
- Title: To direct the Secretary of Health and Human Services to identify, review, and implement effective interventions in Head Start programs, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9045
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:06:03Z
- Update date including text: 2026-05-30T09:28:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9045",
    "number": "9045",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "D000623",
        "district": "10",
        "firstName": "Mark",
        "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
        "lastName": "DeSaulnier",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To direct the Secretary of Health and Human Services to identify, review, and implement effective interventions in Head Start programs, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:03Z",
    "updateDateIncludingText": "2026-05-30T09:28:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-29",
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
          "date": "2026-05-29T16:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "title": "To direct the Secretary of Health and Human Services to identify, review, and implement effective interventions in Head Start programs, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:06:03Z"
    },
    {
      "title": "To direct the Secretary of Health and Human Services to identify, review, and implement effective interventions in Head Start programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:06:03Z"
    }
  ]
}
```
