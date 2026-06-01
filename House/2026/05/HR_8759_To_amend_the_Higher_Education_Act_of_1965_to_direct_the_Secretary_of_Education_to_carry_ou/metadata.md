# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8759?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8759
- Title: To amend the Higher Education Act of 1965 to direct the Secretary of Education to carry out a program under which an institution of higher education may elect to cosign Federal student loans made to students attending the institution, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8759
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-13T08:06:24Z
- Update date including text: 2026-05-13T15:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8759",
    "number": "8759",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "To amend the Higher Education Act of 1965 to direct the Secretary of Education to carry out a program under which an institution of higher education may elect to cosign Federal student loans made to students attending the institution, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:24Z",
    "updateDateIncludingText": "2026-05-13T15:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:01:50Z",
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
      "title": "To amend the Higher Education Act of 1965 to direct the Secretary of Education to carry out a program under which an institution of higher education may elect to cosign Federal student loans made to students attending the institution, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T08:06:24Z"
    },
    {
      "title": "To amend the Higher Education Act of 1965 to direct the Secretary of Education to carry out a program under which an institution of higher education may elect to cosign Federal student loans made to students attending the institution, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T08:06:24Z"
    }
  ]
}
```
