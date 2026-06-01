# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8812?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8812
- Title: To require the Nuclear Regulatory Commission to allow the use of commercial-grade steel and concrete in non-safety-related structures at nuclear power plants, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8812
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-15T08:07:31Z
- Update date including text: 2026-05-15T15:58:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-14: Introduced in House

## Actions

- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8812",
    "number": "8812",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "D000032",
        "district": "19",
        "firstName": "Byron",
        "fullName": "Rep. Donalds, Byron [R-FL-19]",
        "lastName": "Donalds",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To require the Nuclear Regulatory Commission to allow the use of commercial-grade steel and concrete in non-safety-related structures at nuclear power plants, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:31Z",
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
          "date": "2026-05-14T14:01:45Z",
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
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To require the Nuclear Regulatory Commission to allow the use of commercial-grade steel and concrete in non-safety-related structures at nuclear power plants, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:31Z"
    },
    {
      "title": "To require the Nuclear Regulatory Commission to allow the use of commercial-grade steel and concrete in non-safety-related structures at nuclear power plants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:07:31Z"
    }
  ]
}
```
