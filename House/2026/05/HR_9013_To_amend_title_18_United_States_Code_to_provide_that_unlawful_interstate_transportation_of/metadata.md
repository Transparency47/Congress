# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9013?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9013
- Title: To amend title 18, United States Code, to provide that unlawful interstate transportation of fireworks is specified unlawful activity for purposes of laundering of monetary instruments.
- Congress: 119
- Bill type: HR
- Bill number: 9013
- Origin chamber: House
- Introduced date: 2026-05-22
- Update date: 2026-05-26T13:10:46Z
- Update date including text: 2026-05-27T05:58:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-22: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-05-22 - IntroReferral: Sponsor introductory remarks on measure. (CR E485)
- Latest action: 2026-05-22: Introduced in House

## Actions

- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-05-22 - IntroReferral: Sponsor introductory remarks on measure. (CR E485)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-22",
    "latestAction": {
      "actionDate": "2026-05-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9013",
    "number": "9013",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "To amend title 18, United States Code, to provide that unlawful interstate transportation of fireworks is specified unlawful activity for purposes of laundering of monetary instruments.",
    "type": "HR",
    "updateDate": "2026-05-26T13:10:46Z",
    "updateDateIncludingText": "2026-05-27T05:58:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-22",
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
      "actionDate": "2026-05-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2026-05-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E485)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-22",
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
          "date": "2026-05-22T14:31:30Z",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-05-22",
      "state": "HI"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend title 18, United States Code, to provide that unlawful interstate transportation of fireworks is specified unlawful activity for purposes of laundering of monetary instruments.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-23T08:07:28Z"
    },
    {
      "title": "To amend title 18, United States Code, to provide that unlawful interstate transportation of fireworks is specified unlawful activity for purposes of laundering of monetary instruments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-23T08:07:28Z"
    }
  ]
}
```
