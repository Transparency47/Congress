# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8820?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8820
- Title: To limit the use of certain funds for the deactivation of Expeditionary Combat Aviation Brigades, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8820
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-15T08:07:51Z
- Update date including text: 2026-05-15T15:43:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-14: Introduced in House

## Actions

- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8820",
    "number": "8820",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To limit the use of certain funds for the deactivation of Expeditionary Combat Aviation Brigades, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:51Z",
    "updateDateIncludingText": "2026-05-15T15:43:25Z"
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
          "date": "2026-05-14T14:04:00Z",
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
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "CO"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To limit the use of certain funds for the deactivation of Expeditionary Combat Aviation Brigades, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:51Z"
    },
    {
      "title": "To limit the use of certain funds for the deactivation of Expeditionary Combat Aviation Brigades, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:07:51Z"
    }
  ]
}
```
