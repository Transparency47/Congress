# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8854?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8854
- Title: To establish a pilot program for the Secretary of Housing and Urban Development to evaluate the effectiveness of insuring mortgages made to finance improvements to convert basement spaces into safely habitable dwelling units, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8854
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-16T08:07:39Z
- Update date including text: 2026-05-16T10:58:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-15: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-05-15: Introduced in House

## Actions

- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-15",
    "latestAction": {
      "actionDate": "2026-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8854",
    "number": "8854",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To establish a pilot program for the Secretary of Housing and Urban Development to evaluate the effectiveness of insuring mortgages made to finance improvements to convert basement spaces into safely habitable dwelling units, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:39Z",
    "updateDateIncludingText": "2026-05-16T10:58:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-15",
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
      "actionDate": "2026-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-15",
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
          "date": "2026-05-15T13:01:10Z",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
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
      "title": "To establish a pilot program for the Secretary of Housing and Urban Development to evaluate the effectiveness of insuring mortgages made to finance improvements to convert basement spaces into safely habitable dwelling units, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-16T08:07:39Z"
    },
    {
      "title": "To establish a pilot program for the Secretary of Housing and Urban Development to evaluate the effectiveness of insuring mortgages made to finance improvements to convert basement spaces into safely habitable dwelling units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-16T08:07:39Z"
    }
  ]
}
```
