# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7958?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7958
- Title: To amend the Immigration and Nationality Act to deem specified activities in support of terrorism as renunciation of United States nationality.
- Congress: 119
- Bill type: HR
- Bill number: 7958
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-03-18T08:06:41Z
- Update date including text: 2026-03-18T08:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-17: Introduced in House

## Actions

- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7958",
    "number": "7958",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "To amend the Immigration and Nationality Act to deem specified activities in support of terrorism as renunciation of United States nationality.",
    "type": "HR",
    "updateDate": "2026-03-18T08:06:41Z",
    "updateDateIncludingText": "2026-03-18T08:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T14:00:15Z",
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
      "title": "To amend the Immigration and Nationality Act to deem specified activities in support of terrorism as renunciation of United States nationality.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T08:06:41Z"
    },
    {
      "title": "To amend the Immigration and Nationality Act to deem specified activities in support of terrorism as renunciation of United States nationality.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T08:06:41Z"
    }
  ]
}
```
