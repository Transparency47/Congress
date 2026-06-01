# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9044?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9044
- Title: To amend title V of the Public Health Service Act to reauthorize the Minority Fellowship Program.
- Congress: 119
- Bill type: HR
- Bill number: 9044
- Origin chamber: House
- Introduced date: 2026-05-26
- Update date: 2026-05-27T08:05:39Z
- Update date including text: 2026-05-27T09:58:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-26: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-26: Introduced in House

## Actions

- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-26",
    "latestAction": {
      "actionDate": "2026-05-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9044",
    "number": "9044",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To amend title V of the Public Health Service Act to reauthorize the Minority Fellowship Program.",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:39Z",
    "updateDateIncludingText": "2026-05-27T09:58:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-26",
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
      "actionDate": "2026-05-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-26",
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
          "date": "2026-05-26T15:02:00Z",
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
      "title": "To amend title V of the Public Health Service Act to reauthorize the Minority Fellowship Program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:05:39Z"
    },
    {
      "title": "To amend title V of the Public Health Service Act to reauthorize the Minority Fellowship Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:05:39Z"
    }
  ]
}
```
