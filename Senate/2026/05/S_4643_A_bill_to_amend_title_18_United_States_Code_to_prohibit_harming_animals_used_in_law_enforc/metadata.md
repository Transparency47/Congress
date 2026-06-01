# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4643
- Title: A bill to amend title 18, United States Code, to prohibit harming animals used in law enforcement, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4643
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:56:35Z
- Update date including text: 2026-05-22T10:56:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-21: Introduced in Senate

## Actions

- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4643",
    "number": "4643",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A bill to amend title 18, United States Code, to prohibit harming animals used in law enforcement, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-22T10:56:35Z",
    "updateDateIncludingText": "2026-05-22T10:56:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-05-21T18:55:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "title": "A bill to amend title 18, United States Code, to prohibit harming animals used in law enforcement, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:35Z"
    },
    {
      "title": "A bill to amend title 18, United States Code, to prohibit harming animals used in law enforcement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:56:35Z"
    }
  ]
}
```
