# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8834?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8834
- Title: To ensure that significantly more students graduate college with the international knowledge and experience essential for success in today's global economy through the establishment of the Senator Paul Simon Study Abroad Program in the Department of State.
- Congress: 119
- Bill type: HR
- Bill number: 8834
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-15T08:07:37Z
- Update date including text: 2026-05-15T15:58:25Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8834",
    "number": "8834",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001190",
        "district": "10",
        "firstName": "Bradley",
        "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
        "lastName": "Schneider",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "To ensure that significantly more students graduate college with the international knowledge and experience essential for success in today's global economy through the establishment of the Senator Paul Simon Study Abroad Program in the Department of State.",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:37Z",
    "updateDateIncludingText": "2026-05-15T15:58:25Z"
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
          "date": "2026-05-14T14:04:40Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
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
      "title": "To ensure that significantly more students graduate college with the international knowledge and experience essential for success in today's global economy through the establishment of the Senator Paul Simon Study Abroad Program in the Department of State.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:37Z"
    },
    {
      "title": "To ensure that significantly more students graduate college with the international knowledge and experience essential for success in today's global economy through the establishment of the Senator Paul Simon Study Abroad Program in the Department of State.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:07:37Z"
    }
  ]
}
```
