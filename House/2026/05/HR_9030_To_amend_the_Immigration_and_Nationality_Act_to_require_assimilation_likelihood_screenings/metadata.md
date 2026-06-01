# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9030?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9030
- Title: To amend the Immigration and Nationality Act to require assimilation likelihood screenings.
- Congress: 119
- Bill type: HR
- Bill number: 9030
- Origin chamber: House
- Introduced date: 2026-05-26
- Update date: 2026-05-27T08:06:03Z
- Update date including text: 2026-05-27T09:43:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-26: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-26: Introduced in House

## Actions

- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9030",
    "number": "9030",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "To amend the Immigration and Nationality Act to require assimilation likelihood screenings.",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:03Z",
    "updateDateIncludingText": "2026-05-27T09:43:26Z"
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
          "date": "2026-05-26T15:01:00Z",
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
      "title": "To amend the Immigration and Nationality Act to require assimilation likelihood screenings.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:06:03Z"
    },
    {
      "title": "To amend the Immigration and Nationality Act to require assimilation likelihood screenings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:06:03Z"
    }
  ]
}
```
