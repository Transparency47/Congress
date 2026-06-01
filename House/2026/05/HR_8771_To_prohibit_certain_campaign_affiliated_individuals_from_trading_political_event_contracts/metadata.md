# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8771?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8771
- Title: To prohibit certain campaign-affiliated individuals from trading political event contracts while in possession of material nonpublic campaign information, to require covered prediction market platforms to maintain safeguards against insider trading and market manipulation, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8771
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-13T08:06:17Z
- Update date including text: 2026-05-13T08:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8771",
    "number": "8771",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To prohibit certain campaign-affiliated individuals from trading political event contracts while in possession of material nonpublic campaign information, to require covered prediction market platforms to maintain safeguards against insider trading and market manipulation, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:17Z",
    "updateDateIncludingText": "2026-05-13T08:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "title": "To prohibit certain campaign-affiliated individuals from trading political event contracts while in possession of material nonpublic campaign information, to require covered prediction market platforms to maintain safeguards against insider trading and market manipulation, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T08:06:17Z"
    },
    {
      "title": "To prohibit certain campaign-affiliated individuals from trading political event contracts while in possession of material nonpublic campaign information, to require covered prediction market platforms to maintain safeguards against insider trading and market manipulation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T08:06:17Z"
    }
  ]
}
```
