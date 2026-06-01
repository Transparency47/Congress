# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8828?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8828
- Title: To direct the Attorney General to establish an official station for the United States attorney for the Western District of Washington in the county of Clark, Washington, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8828
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-15T08:07:40Z
- Update date including text: 2026-05-15T15:43:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-14: Introduced in House

## Actions

- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8828",
    "number": "8828",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "To direct the Attorney General to establish an official station for the United States attorney for the Western District of Washington in the county of Clark, Washington, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:40Z",
    "updateDateIncludingText": "2026-05-15T15:43:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "title": "To direct the Attorney General to establish an official station for the United States attorney for the Western District of Washington in the county of Clark, Washington, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:40Z"
    },
    {
      "title": "To direct the Attorney General to establish an official station for the United States attorney for the Western District of Washington in the county of Clark, Washington, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:07:40Z"
    }
  ]
}
```
