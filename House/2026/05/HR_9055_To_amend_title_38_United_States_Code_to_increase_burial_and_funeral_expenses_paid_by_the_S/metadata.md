# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9055?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9055
- Title: To amend title 38, United States Code, to increase burial and funeral expenses paid by the Secretary of Veterans Affairs in the case of death from a service-connected disability, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9055
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:05:56Z
- Update date including text: 2026-05-30T09:28:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9055",
    "number": "9055",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "To amend title 38, United States Code, to increase burial and funeral expenses paid by the Secretary of Veterans Affairs in the case of death from a service-connected disability, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:56Z",
    "updateDateIncludingText": "2026-05-30T09:28:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
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
      "actionDate": "2026-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-29",
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
          "date": "2026-05-29T16:01:20Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MN"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend title 38, United States Code, to increase burial and funeral expenses paid by the Secretary of Veterans Affairs in the case of death from a service-connected disability, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:05:56Z"
    },
    {
      "title": "To amend title 38, United States Code, to increase burial and funeral expenses paid by the Secretary of Veterans Affairs in the case of death from a service-connected disability, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:05:56Z"
    }
  ]
}
```
