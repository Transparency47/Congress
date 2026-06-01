# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1313?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1313
- Title: Condemning the hateful comments of Texas congressional candidate Maureen Galindo.
- Congress: 119
- Bill type: HRES
- Bill number: 1313
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-22T08:08:40Z
- Update date including text: 2026-05-22T08:08:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-05-21 - IntroReferral: Submitted in House
- Latest action: 2026-05-21: Submitted in House

## Actions

- 2026-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-05-21 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1313",
    "number": "1313",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Condemning the hateful comments of Texas congressional candidate Maureen Galindo.",
    "type": "HRES",
    "updateDate": "2026-05-22T08:08:40Z",
    "updateDateIncludingText": "2026-05-22T08:08:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
          "date": "2026-05-21T14:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "title": "Condemning the hateful comments of Texas congressional candidate Maureen Galindo.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T08:08:40Z"
    },
    {
      "title": "Condemning the hateful comments of Texas congressional candidate Maureen Galindo.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T08:08:40Z"
    }
  ]
}
```
