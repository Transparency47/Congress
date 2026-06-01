# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9012?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9012
- Title: To amend the Internal Revenue Code of 1986 to allow 5-year carrybacks for the low-income housing tax credit.
- Congress: 119
- Bill type: HR
- Bill number: 9012
- Origin chamber: House
- Introduced date: 2026-05-22
- Update date: 2026-05-23T08:07:33Z
- Update date including text: 2026-05-27T05:58:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-22: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-05-22: Introduced in House

## Actions

- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-22",
    "latestAction": {
      "actionDate": "2026-05-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9012",
    "number": "9012",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to allow 5-year carrybacks for the low-income housing tax credit.",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:33Z",
    "updateDateIncludingText": "2026-05-27T05:58:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-22",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-22",
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
          "date": "2026-05-22T14:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-05-22",
      "state": "CA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Internal Revenue Code of 1986 to allow 5-year carrybacks for the low-income housing tax credit.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-23T08:07:33Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to allow 5-year carrybacks for the low-income housing tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-23T08:07:33Z"
    }
  ]
}
```
