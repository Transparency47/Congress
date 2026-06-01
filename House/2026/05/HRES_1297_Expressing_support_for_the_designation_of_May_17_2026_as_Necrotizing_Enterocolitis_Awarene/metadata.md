# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1297
- Title: Expressing support for the designation of May 17, 2026, as "Necrotizing Enterocolitis Awareness Day".
- Congress: 119
- Bill type: HRES
- Bill number: 1297
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-16T08:07:30Z
- Update date including text: 2026-05-16T08:07:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-15: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-15 - IntroReferral: Submitted in House
- Latest action: 2026-05-15: Submitted in House

## Actions

- 2026-05-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-15 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1297",
    "number": "1297",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of May 17, 2026, as \"Necrotizing Enterocolitis Awareness Day\".",
    "type": "HRES",
    "updateDate": "2026-05-16T08:07:30Z",
    "updateDateIncludingText": "2026-05-16T08:07:30Z"
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
      "actionCode": "1025",
      "actionDate": "2026-05-15",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
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
          "date": "2026-05-15T13:00:20Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [I-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "I",
      "sponsorshipDate": "2026-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "WV"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Expressing support for the designation of May 17, 2026, as \"Necrotizing Enterocolitis Awareness Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-16T08:07:30Z"
    },
    {
      "title": "Expressing support for the designation of May 17, 2026, as \"Necrotizing Enterocolitis Awareness Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-16T08:07:30Z"
    }
  ]
}
```
