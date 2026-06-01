# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8948?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8948
- Title: To amend the Public Utility Regulatory Policies Act of 1978 to require States to consider measures that limit the amount of retail utility rate increases an electric utility can request to once every 365 days.
- Congress: 119
- Bill type: HR
- Bill number: 8948
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-21T08:08:10Z
- Update date including text: 2026-05-21T15:43:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8948",
    "number": "8948",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "To amend the Public Utility Regulatory Policies Act of 1978 to require States to consider measures that limit the amount of retail utility rate increases an electric utility can request to once every 365 days.",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:10Z",
    "updateDateIncludingText": "2026-05-21T15:43:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T15:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to require States to consider measures that limit the amount of retail utility rate increases an electric utility can request to once every 365 days.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:08:10Z"
    },
    {
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to require States to consider measures that limit the amount of retail utility rate increases an electric utility can request to once every 365 days.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T08:08:10Z"
    }
  ]
}
```
