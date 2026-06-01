# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9049?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9049
- Title: To amend the Federal Election Campaign Act of 1971 to require political committees to file separate reports for contributions of $1,000 or more which are received fewer than 20 days before the date of any election in which the committee makes a contribution to, or an expenditure or electioneering communication on behalf of or in opposition to, a candidate or political party in the election, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9049
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:05:51Z
- Update date including text: 2026-05-30T09:28:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9049",
    "number": "9049",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "To amend the Federal Election Campaign Act of 1971 to require political committees to file separate reports for contributions of $1,000 or more which are received fewer than 20 days before the date of any election in which the committee makes a contribution to, or an expenditure or electioneering communication on behalf of or in opposition to, a candidate or political party in the election, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:51Z",
    "updateDateIncludingText": "2026-05-30T09:28:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
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
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-29",
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
          "date": "2026-05-29T16:01:10Z",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "PA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "WI"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Federal Election Campaign Act of 1971 to require political committees to file separate reports for contributions of $1,000 or more which are received fewer than 20 days before the date of any election in which the committee makes a contribution to, or an expenditure or electioneering communication on behalf of or in opposition to, a candidate or political party in the election, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:05:51Z"
    },
    {
      "title": "To amend the Federal Election Campaign Act of 1971 to require political committees to file separate reports for contributions of $1,000 or more which are received fewer than 20 days before the date of any election in which the committee makes a contribution to, or an expenditure or electioneering communication on behalf of or in opposition to, a candidate or political party in the election, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:05:51Z"
    }
  ]
}
```
