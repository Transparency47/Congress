# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8833?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8833
- Title: To direct the Comptroller General of the United States to conduct a study to evaluate the activities of sister city partnerships operating within the United States, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8833
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-15T08:08:23Z
- Update date including text: 2026-05-15T15:58:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-05-14: Introduced in House

## Actions

- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8833",
    "number": "8833",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To direct the Comptroller General of the United States to conduct a study to evaluate the activities of sister city partnerships operating within the United States, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-15T08:08:23Z",
    "updateDateIncludingText": "2026-05-15T15:58:24Z"
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
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
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
          "date": "2026-05-14T14:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sponsorshipDate": "2026-05-14",
      "state": "AL"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To direct the Comptroller General of the United States to conduct a study to evaluate the activities of sister city partnerships operating within the United States, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:08:23Z"
    },
    {
      "title": "To direct the Comptroller General of the United States to conduct a study to evaluate the activities of sister city partnerships operating within the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:08:23Z"
    }
  ]
}
```
