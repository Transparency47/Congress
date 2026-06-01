# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8809?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8809
- Title: To amend the Foreign Agents Registration Act of 1938, as amended to clarify the definition of "foreign principal" and ensure transparency in lobbying on behalf of foreign interests.
- Congress: 119
- Bill type: HR
- Bill number: 8809
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-15T08:08:01Z
- Update date including text: 2026-05-15T15:43:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-14: Introduced in House

## Actions

- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8809",
    "number": "8809",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "To amend the Foreign Agents Registration Act of 1938, as amended to clarify the definition of \"foreign principal\" and ensure transparency in lobbying on behalf of foreign interests.",
    "type": "HR",
    "updateDate": "2026-05-15T08:08:01Z",
    "updateDateIncludingText": "2026-05-15T15:43:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-14",
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
          "date": "2026-05-14T14:02:05Z",
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
      "title": "To amend the Foreign Agents Registration Act of 1938, as amended to clarify the definition of \"foreign principal\" and ensure transparency in lobbying on behalf of foreign interests.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:08:01Z"
    },
    {
      "title": "To amend the Foreign Agents Registration Act of 1938, as amended to clarify the definition of \"foreign principal\" and ensure transparency in lobbying on behalf of foreign interests.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:08:01Z"
    }
  ]
}
```
