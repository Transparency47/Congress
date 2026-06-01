# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1327?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1327
- Title: Supporting the designation of May 2026 as "Borderline Personality Disorder Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1327
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:06:01Z
- Update date including text: 2026-05-30T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-29 - IntroReferral: Submitted in House
- Latest action: 2026-05-29: Submitted in House

## Actions

- 2026-05-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-29 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1327",
    "number": "1327",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "E000299",
        "district": "16",
        "firstName": "Veronica",
        "fullName": "Rep. Escobar, Veronica [D-TX-16]",
        "lastName": "Escobar",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Supporting the designation of May 2026 as \"Borderline Personality Disorder Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-30T08:06:01Z",
    "updateDateIncludingText": "2026-05-30T08:06:01Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-05-29T16:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "PA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Supporting the designation of May 2026 as \"Borderline Personality Disorder Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:06:01Z"
    },
    {
      "title": "Supporting the designation of May 2026 as \"Borderline Personality Disorder Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:06:01Z"
    }
  ]
}
```
