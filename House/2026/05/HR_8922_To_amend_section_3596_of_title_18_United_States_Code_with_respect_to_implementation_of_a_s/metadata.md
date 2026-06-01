# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8922?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8922
- Title: To amend section 3596 of title 18, United States Code, with respect to implementation of a sentence of death.
- Congress: 119
- Bill type: HR
- Bill number: 8922
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-21T08:08:22Z
- Update date including text: 2026-05-21T15:58:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8922",
    "number": "8922",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "To amend section 3596 of title 18, United States Code, with respect to implementation of a sentence of death.",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:22Z",
    "updateDateIncludingText": "2026-05-21T15:58:23Z"
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
          "date": "2026-05-20T15:03:40Z",
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
      "title": "To amend section 3596 of title 18, United States Code, with respect to implementation of a sentence of death.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:08:22Z"
    },
    {
      "title": "To amend section 3596 of title 18, United States Code, with respect to implementation of a sentence of death.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T08:08:22Z"
    }
  ]
}
```
