# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8823?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8823
- Title: To amend the Federal Employees' Compensation Act to allow the Secretary of Labor to suspend payments to medical providers who have been convicted of fraud.
- Congress: 119
- Bill type: HR
- Bill number: 8823
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-15T08:08:01Z
- Update date including text: 2026-05-15T15:58:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-05-14: Introduced in House

## Actions

- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Education and Workforce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8823",
    "number": "8823",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001230",
        "district": "7",
        "firstName": "Ryan",
        "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
        "lastName": "Mackenzie",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "To amend the Federal Employees' Compensation Act to allow the Secretary of Labor to suspend payments to medical providers who have been convicted of fraud.",
    "type": "HR",
    "updateDate": "2026-05-15T08:08:01Z",
    "updateDateIncludingText": "2026-05-15T15:58:25Z"
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
          "date": "2026-05-14T14:05:10Z",
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
      "title": "To amend the Federal Employees' Compensation Act to allow the Secretary of Labor to suspend payments to medical providers who have been convicted of fraud.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:08:01Z"
    },
    {
      "title": "To amend the Federal Employees' Compensation Act to allow the Secretary of Labor to suspend payments to medical providers who have been convicted of fraud.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:08:01Z"
    }
  ]
}
```
