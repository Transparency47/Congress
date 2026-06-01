# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9023?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9023
- Title: To amend the Surface Mining Control and Reclamation Act of 1977 to strengthen control of the environmental impacts of surface coal mining, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9023
- Origin chamber: House
- Introduced date: 2026-05-26
- Update date: 2026-05-27T08:05:53Z
- Update date including text: 2026-05-27T09:58:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-26: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-05-26: Introduced in House

## Actions

- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-26",
    "latestAction": {
      "actionDate": "2026-05-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9023",
    "number": "9023",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "To amend the Surface Mining Control and Reclamation Act of 1977 to strengthen control of the environmental impacts of surface coal mining, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:53Z",
    "updateDateIncludingText": "2026-05-27T09:58:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-26",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-26",
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
          "date": "2026-05-26T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "PA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "PA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Surface Mining Control and Reclamation Act of 1977 to strengthen control of the environmental impacts of surface coal mining, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:05:53Z"
    },
    {
      "title": "To amend the Surface Mining Control and Reclamation Act of 1977 to strengthen control of the environmental impacts of surface coal mining, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:05:53Z"
    }
  ]
}
```
