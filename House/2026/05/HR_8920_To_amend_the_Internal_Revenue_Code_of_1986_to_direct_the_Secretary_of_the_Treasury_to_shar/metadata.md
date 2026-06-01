# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8920?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8920
- Title: To amend the Internal Revenue Code of 1986 to direct the Secretary of the Treasury to share Individual Taxpayer Identification Number information with the Department of Homeland Security for the purpose of enforcing immigration laws.
- Congress: 119
- Bill type: HR
- Bill number: 8920
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-21T08:08:56Z
- Update date including text: 2026-05-21T15:58:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8920",
    "number": "8920",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to direct the Secretary of the Treasury to share Individual Taxpayer Identification Number information with the Department of Homeland Security for the purpose of enforcing immigration laws.",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:56Z",
    "updateDateIncludingText": "2026-05-21T15:58:22Z"
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2026-05-20T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sponsorshipDate": "2026-05-20",
      "state": "AL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Internal Revenue Code of 1986 to direct the Secretary of the Treasury to share Individual Taxpayer Identification Number information with the Department of Homeland Security for the purpose of enforcing immigration laws.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:08:56Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to direct the Secretary of the Treasury to share Individual Taxpayer Identification Number information with the Department of Homeland Security for the purpose of enforcing immigration laws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T08:08:56Z"
    }
  ]
}
```
