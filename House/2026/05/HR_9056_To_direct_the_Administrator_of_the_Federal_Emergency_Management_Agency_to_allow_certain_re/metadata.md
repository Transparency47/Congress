# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9056?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9056
- Title: To direct the Administrator of the Federal Emergency Management Agency to allow certain recipients of the Flood Mitigation Assistance Grant, and other grants, to be used for the payment of premiums for a community-based, parametric flood insurance policy, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9056
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:06:09Z
- Update date including text: 2026-05-30T09:28:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Financial Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9056",
    "number": "9056",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "To direct the Administrator of the Federal Emergency Management Agency to allow certain recipients of the Flood Mitigation Assistance Grant, and other grants, to be used for the payment of premiums for a community-based, parametric flood insurance policy, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:09Z",
    "updateDateIncludingText": "2026-05-30T09:28:24Z"
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
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
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
          "date": "2026-05-29T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NY"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To direct the Administrator of the Federal Emergency Management Agency to allow certain recipients of the Flood Mitigation Assistance Grant, and other grants, to be used for the payment of premiums for a community-based, parametric flood insurance policy, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:06:09Z"
    },
    {
      "title": "To direct the Administrator of the Federal Emergency Management Agency to allow certain recipients of the Flood Mitigation Assistance Grant, and other grants, to be used for the payment of premiums for a community-based, parametric flood insurance policy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:06:09Z"
    }
  ]
}
```
