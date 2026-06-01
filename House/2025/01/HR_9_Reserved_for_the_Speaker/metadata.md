# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9
- Title: Reserved for the Speaker.
- Congress: 119
- Bill type: HR
- Bill number: 9
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-14T09:05:49Z
- Update date including text: 2025-01-14T09:05:50Z
- Date accessed: 2026-06-01T02:17:27.658025+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- No actions returned by the Congress.gov actions endpoint.

## Actions

- No actions returned by the Congress.gov actions endpoint.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9",
    "number": "9",
    "originChamber": "House",
    "originChamberCode": "H",
    "sponsors": [
      {
        "bioguideId": "J000299",
        "district": 4,
        "firstName": "Mike",
        "fullName": "Rep. Johnson, Mike [R-LA-4]",
        "isByRequest": "N",
        "lastName": "Johnson",
        "party": "R",
        "state": "LA",
        "url": "https://api.congress.gov/v3/member/J000299?format=json"
      }
    ],
    "title": "Reserved for the Speaker.",
    "titles": {
      "count": 2,
      "url": "https://api.congress.gov/v3/bill/119/hr/9/titles?format=json"
    },
    "type": "HR",
    "updateDate": "2025-01-14T09:05:49Z",
    "updateDateIncludingText": "2025-01-14T09:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [],
  "pagination": {
    "count": 0
  },
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  }
}
```

## API Data: amendments

```json
{
  "amendments": [],
  "pagination": {
    "count": 0
  },
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  }
}
```

## API Data: committees

```json
{
  "committees": [],
  "pagination": {
    "count": 0
  },
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  }
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [],
  "pagination": {
    "count": 0
  },
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  }
}
```

## API Data: relatedbills

```json
{
  "pagination": {
    "count": 0
  },
  "relatedBills": [],
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  }
}
```

## API Data: subjects

```json
{
  "pagination": {
    "count": 0
  },
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  },
  "subjects": {
    "legislativeSubjects": []
  }
}
```

## API Data: summaries

```json
{
  "pagination": {
    "count": 0
  },
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  },
  "summaries": []
}
```

## API Data: text

```json
{
  "pagination": {
    "count": 0
  },
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  },
  "textVersions": []
}
```

## API Data: titles

```json
{
  "pagination": {
    "count": 2
  },
  "request": {
    "billNumber": "9",
    "billType": "hr",
    "billUrl": "https://api.congress.gov/v3/bill/119/hr/9?format=json",
    "congress": "119",
    "contentType": "application/json",
    "format": "json"
  },
  "titles": [
    {
      "title": "Reserved for the Speaker.",
      "titleType": "Display Title",
      "titleTypeCode": 45,
      "updateDate": "2025-01-14T09:05:49Z"
    },
    {
      "title": "Reserved for the Speaker.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": 6,
      "updateDate": "2025-01-14T09:05:49Z"
    }
  ]
}
```
