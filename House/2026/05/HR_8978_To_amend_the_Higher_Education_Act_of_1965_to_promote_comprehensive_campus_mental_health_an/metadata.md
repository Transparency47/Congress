# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8978?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8978
- Title: To amend the Higher Education Act of 1965 to promote comprehensive campus mental health and suicide prevention plans, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8978
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-22T08:07:28Z
- Update date including text: 2026-05-22T12:13:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-05-21: Introduced in House

## Actions

- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8978",
    "number": "8978",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001231",
        "district": "22",
        "firstName": "John",
        "fullName": "Rep. Mannion, John W. [D-NY-22]",
        "lastName": "Mannion",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To amend the Higher Education Act of 1965 to promote comprehensive campus mental health and suicide prevention plans, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:28Z",
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
          "date": "2026-05-21T14:05:25Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "PA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Higher Education Act of 1965 to promote comprehensive campus mental health and suicide prevention plans, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T08:07:28Z"
    },
    {
      "title": "To amend the Higher Education Act of 1965 to promote comprehensive campus mental health and suicide prevention plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T08:07:28Z"
    }
  ]
}
```
