# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8858?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8858
- Title: To allow Americans to sue federal officials for constitutional violations of voting rights and election law.
- Congress: 119
- Bill type: HR
- Bill number: 8858
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-16T08:08:05Z
- Update date including text: 2026-05-16T10:58:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-15: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-15: Introduced in House

## Actions

- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8858",
    "number": "8858",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001196",
        "district": "6",
        "firstName": "Seth",
        "fullName": "Rep. Moulton, Seth [D-MA-6]",
        "lastName": "Moulton",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "To allow Americans to sue federal officials for constitutional violations of voting rights and election law.",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:05Z",
    "updateDateIncludingText": "2026-05-16T10:58:23Z"
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
          "date": "2026-05-15T13:00:25Z",
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
      "title": "To allow Americans to sue federal officials for constitutional violations of voting rights and election law.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-16T08:08:05Z"
    },
    {
      "title": "To allow Americans to sue federal officials for constitutional violations of voting rights and election law.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-16T08:08:05Z"
    }
  ]
}
```
