# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9033
- Title: To amend title 38, United States Code, to enhance the sharing of health-care resources between the Department of Veterans Affairs and State Veterans Homes, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9033
- Origin chamber: House
- Introduced date: 2026-05-26
- Update date: 2026-05-27T08:05:31Z
- Update date including text: 2026-05-27T09:43:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-26: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-05-26: Introduced in House

## Actions

- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9033",
    "number": "9033",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "To amend title 38, United States Code, to enhance the sharing of health-care resources between the Department of Veterans Affairs and State Veterans Homes, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:31Z",
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
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
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
          "date": "2026-05-26T15:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "title": "To amend title 38, United States Code, to enhance the sharing of health-care resources between the Department of Veterans Affairs and State Veterans Homes, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:05:31Z"
    },
    {
      "title": "To amend title 38, United States Code, to enhance the sharing of health-care resources between the Department of Veterans Affairs and State Veterans Homes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:05:31Z"
    }
  ]
}
```
