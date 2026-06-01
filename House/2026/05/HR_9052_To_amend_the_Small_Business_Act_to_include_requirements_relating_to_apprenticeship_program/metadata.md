# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9052?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9052
- Title: To amend the Small Business Act to include requirements relating to apprenticeship program assistance for small business development centers, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 9052
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:06:06Z
- Update date including text: 2026-05-30T09:28:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Small Business.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9052",
    "number": "9052",
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
    "title": "To amend the Small Business Act to include requirements relating to apprenticeship program assistance for small business development centers, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:06Z",
    "updateDateIncludingText": "2026-05-30T09:28:24Z"
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
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
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
          "date": "2026-05-29T16:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "FL"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Small Business Act to include requirements relating to apprenticeship program assistance for small business development centers, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:06:06Z"
    },
    {
      "title": "To amend the Small Business Act to include requirements relating to apprenticeship program assistance for small business development centers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:06:06Z"
    }
  ]
}
```
