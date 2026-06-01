# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8949?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8949
- Title: To amend title 5, United States Code, to include certain overtime pay received by members of the Capitol Police in the computation of annuities for such members, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8949
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-21T08:07:56Z
- Update date including text: 2026-05-21T15:43:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8949",
    "number": "8949",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "W000831",
        "district": "11",
        "firstName": "James",
        "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
        "lastName": "Walkinshaw",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "To amend title 5, United States Code, to include certain overtime pay received by members of the Capitol Police in the computation of annuities for such members, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:56Z",
    "updateDateIncludingText": "2026-05-21T15:43:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T15:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-20T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "MD"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend title 5, United States Code, to include certain overtime pay received by members of the Capitol Police in the computation of annuities for such members, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:07:56Z"
    },
    {
      "title": "To amend title 5, United States Code, to include certain overtime pay received by members of the Capitol Police in the computation of annuities for such members, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T08:07:56Z"
    }
  ]
}
```
