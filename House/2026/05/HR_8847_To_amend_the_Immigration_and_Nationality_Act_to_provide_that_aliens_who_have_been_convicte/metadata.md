# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8847?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8847
- Title: To amend the Immigration and Nationality Act to provide that aliens who have been convicted of or who have committed an offense that violates certain State or Federal hunting or fishing laws are inadmissible and deportable.
- Congress: 119
- Bill type: HR
- Bill number: 8847
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-16T08:07:23Z
- Update date including text: 2026-05-16T10:58:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8847",
    "number": "8847",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "To amend the Immigration and Nationality Act to provide that aliens who have been convicted of or who have committed an offense that violates certain State or Federal hunting or fishing laws are inadmissible and deportable.",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:23Z",
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
          "date": "2026-05-15T13:02:25Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "AL"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Immigration and Nationality Act to provide that aliens who have been convicted of or who have committed an offense that violates certain State or Federal hunting or fishing laws are inadmissible and deportable.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-16T08:07:23Z"
    },
    {
      "title": "To amend the Immigration and Nationality Act to provide that aliens who have been convicted of or who have committed an offense that violates certain State or Federal hunting or fishing laws are inadmissible and deportable.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-16T08:07:23Z"
    }
  ]
}
```
