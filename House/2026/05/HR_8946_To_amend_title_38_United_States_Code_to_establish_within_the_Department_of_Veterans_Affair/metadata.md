# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8946?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8946
- Title: To amend title 38, United States Code, to establish within the Department of Veterans Affairs a Veterans Affairs History Office, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8946
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-21T08:08:28Z
- Update date including text: 2026-05-21T15:43:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8946",
    "number": "8946",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "T000463",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. Turner, Michael R. [R-OH-10]",
        "lastName": "Turner",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "To amend title 38, United States Code, to establish within the Department of Veterans Affairs a Veterans Affairs History Office, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:28Z",
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
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
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
          "date": "2026-05-20T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "OH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend title 38, United States Code, to establish within the Department of Veterans Affairs a Veterans Affairs History Office, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:08:28Z"
    },
    {
      "title": "To amend title 38, United States Code, to establish within the Department of Veterans Affairs a Veterans Affairs History Office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T08:08:28Z"
    }
  ]
}
```
