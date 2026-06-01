# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4626?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4626
- Title: A bill to amend title 10, United States Code, to direct the Secretary of Defense to publish a list of dietary supplement ingredients prohibited for use by members of the Armed Forces, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4626
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:56:28Z
- Update date including text: 2026-05-22T10:56:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-05-21: Introduced in Senate

## Actions

- 2026-05-21 - IntroReferral: Introduced in Senate
- 2026-05-21 - IntroReferral: Read twice and referred to the Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4626",
    "number": "4626",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to amend title 10, United States Code, to direct the Secretary of Defense to publish a list of dietary supplement ingredients prohibited for use by members of the Armed Forces, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-22T10:56:28Z",
    "updateDateIncludingText": "2026-05-22T10:56:28Z"
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
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
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
          "date": "2026-05-21T16:33:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "title": "A bill to amend title 10, United States Code, to direct the Secretary of Defense to publish a list of dietary supplement ingredients prohibited for use by members of the Armed Forces, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:28Z"
    },
    {
      "title": "A bill to amend title 10, United States Code, to direct the Secretary of Defense to publish a list of dietary supplement ingredients prohibited for use by members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:56:28Z"
    }
  ]
}
```
