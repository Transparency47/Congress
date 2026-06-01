# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4575?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4575
- Title: A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide funding for innovations in community policing, mental health care, and community safety, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 4575
- Origin chamber: Senate
- Introduced date: 2026-05-19
- Update date: 2026-05-20T10:56:36Z
- Update date including text: 2026-05-20T10:56:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-19: Introduced in Senate
- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-19: Introduced in Senate

## Actions

- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4575",
    "number": "4575",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide funding for innovations in community policing, mental health care, and community safety, and for other purposes.",
    "type": "S",
    "updateDate": "2026-05-20T10:56:36Z",
    "updateDateIncludingText": "2026-05-20T10:56:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
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
      "actionDate": "2026-05-19",
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
          "date": "2026-05-19T21:28:50Z",
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
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide funding for innovations in community policing, mental health care, and community safety, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T10:56:36Z"
    },
    {
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide funding for innovations in community policing, mental health care, and community safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T10:56:36Z"
    }
  ]
}
```
