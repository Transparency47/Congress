# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8908?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8908
- Title: To amend subsection (q) of section 505 of the Federal Food, Drug, and Cosmetic Act to clarify the process for denying certain petitions whose primary purpose is to delay the approval of an application submitted under subsection (b)(2) or (j) of such section 505, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8908
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-20T08:08:36Z
- Update date including text: 2026-05-20T16:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8908",
    "number": "8908",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001225",
        "district": "17",
        "firstName": "Eric",
        "fullName": "Rep. Sorensen, Eric [D-IL-17]",
        "lastName": "Sorensen",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "To amend subsection (q) of section 505 of the Federal Food, Drug, and Cosmetic Act to clarify the process for denying certain petitions whose primary purpose is to delay the approval of an application submitted under subsection (b)(2) or (j) of such section 505, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:36Z",
    "updateDateIncludingText": "2026-05-20T16:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
          "date": "2026-05-19T16:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "OK"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend subsection (q) of section 505 of the Federal Food, Drug, and Cosmetic Act to clarify the process for denying certain petitions whose primary purpose is to delay the approval of an application submitted under subsection (b)(2) or (j) of such section 505, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:08:36Z"
    },
    {
      "title": "To amend subsection (q) of section 505 of the Federal Food, Drug, and Cosmetic Act to clarify the process for denying certain petitions whose primary purpose is to delay the approval of an application submitted under subsection (b)(2) or (j) of such section 505, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:08:36Z"
    }
  ]
}
```
