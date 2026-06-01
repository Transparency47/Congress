# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8929?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8929
- Title: To amend title 1, United States Code, to expand the scope of documents the Secretary of State is required to transmit to the Congress, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8929
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-21T08:07:54Z
- Update date including text: 2026-05-21T15:58:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8929",
    "number": "8929",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "To amend title 1, United States Code, to expand the scope of documents the Secretary of State is required to transmit to the Congress, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:54Z",
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
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
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
          "date": "2026-05-20T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "TX"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend title 1, United States Code, to expand the scope of documents the Secretary of State is required to transmit to the Congress, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:07:54Z"
    },
    {
      "title": "To amend title 1, United States Code, to expand the scope of documents the Secretary of State is required to transmit to the Congress, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T08:07:54Z"
    }
  ]
}
```
