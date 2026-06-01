# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9009?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9009
- Title: To repeal the Hughes Amendment to the Firearm Owners' Protection Act.
- Congress: 119
- Bill type: HR
- Bill number: 9009
- Origin chamber: House
- Introduced date: 2026-05-22
- Update date: 2026-05-23T08:07:39Z
- Update date including text: 2026-05-27T05:58:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-22: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-22: Introduced in House

## Actions

- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Introduced in House
- 2026-05-22 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9009",
    "number": "9009",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "P000622",
        "district": "1",
        "firstName": "Jimmy",
        "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
        "lastName": "Patronis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To repeal the Hughes Amendment to the Firearm Owners' Protection Act.",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:39Z",
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
          "date": "2026-05-22T14:30:20Z",
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
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "GA"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "WI"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "TX"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To repeal the Hughes Amendment to the Firearm Owners' Protection Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-23T08:07:39Z"
    },
    {
      "title": "To repeal the Hughes Amendment to the Firearm Owners' Protection Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-23T08:07:39Z"
    }
  ]
}
```
