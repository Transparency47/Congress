# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8997?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8997
- Title: To amend part E of title IV of the Social Security Act, to require States to guarantee legal representation to children and parents involved in child protection proceedings, under the program of Federal payments for foster care, prevention, and permanency, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8997
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-22T08:07:35Z
- Update date including text: 2026-05-22T12:13:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-05-21: Introduced in House

## Actions

- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8997",
    "number": "8997",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001205",
        "district": "5",
        "firstName": "Mary Gay",
        "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
        "lastName": "Scanlon",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "To amend part E of title IV of the Social Security Act, to require States to guarantee legal representation to children and parents involved in child protection proceedings, under the program of Federal payments for foster care, prevention, and permanency, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:35Z",
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2026-05-21T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "title": "To amend part E of title IV of the Social Security Act, to require States to guarantee legal representation to children and parents involved in child protection proceedings, under the program of Federal payments for foster care, prevention, and permanency, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T08:07:35Z"
    },
    {
      "title": "To amend part E of title IV of the Social Security Act, to require States to guarantee legal representation to children and parents involved in child protection proceedings, under the program of Federal payments for foster care, prevention, and permanency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T08:07:35Z"
    }
  ]
}
```
