# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8848?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8848
- Title: To amend title 10, United States Code, to include the National Guard Relief Foundation in the definition of "military welfare society" in certain laws administered by the Secretaries of the military departments.
- Congress: 119
- Bill type: HR
- Bill number: 8848
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-30T08:05:41Z
- Update date including text: 2026-05-30T08:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-15: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-15: Introduced in House

## Actions

- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8848",
    "number": "8848",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "To amend title 10, United States Code, to include the National Guard Relief Foundation in the definition of \"military welfare society\" in certain laws administered by the Secretaries of the military departments.",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:41Z",
    "updateDateIncludingText": "2026-05-30T08:05:41Z"
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
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
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
          "date": "2026-05-15T13:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "IL"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "title": "To amend title 10, United States Code, to include the National Guard Relief Foundation in the definition of \"military welfare society\" in certain laws administered by the Secretaries of the military departments.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-16T08:07:14Z"
    },
    {
      "title": "To amend title 10, United States Code, to include the National Guard Relief Foundation in the definition of \"military welfare society\" in certain laws administered by the Secretaries of the military departments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-16T08:07:14Z"
    }
  ]
}
```
