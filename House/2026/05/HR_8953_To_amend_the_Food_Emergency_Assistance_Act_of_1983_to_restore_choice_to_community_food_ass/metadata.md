# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8953?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8953
- Title: To amend the Food Emergency Assistance Act of 1983 to restore choice to community food assistance providers to request identification, at their discretion, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8953
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-22T08:07:36Z
- Update date including text: 2026-05-22T12:13:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-05-21: Introduced in House

## Actions

- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Agriculture.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8953",
    "number": "8953",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "To amend the Food Emergency Assistance Act of 1983 to restore choice to community food assistance providers to request identification, at their discretion, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:36Z",
    "updateDateIncludingText": "2026-05-22T12:13:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-21",
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
          "date": "2026-05-21T14:07:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "title": "To amend the Food Emergency Assistance Act of 1983 to restore choice to community food assistance providers to request identification, at their discretion, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T08:07:36Z"
    },
    {
      "title": "To amend the Food Emergency Assistance Act of 1983 to restore choice to community food assistance providers to request identification, at their discretion, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T08:07:36Z"
    }
  ]
}
```
