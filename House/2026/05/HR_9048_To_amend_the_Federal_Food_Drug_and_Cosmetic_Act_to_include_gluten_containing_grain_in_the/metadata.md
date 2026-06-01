# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9048?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9048
- Title: To amend the Federal Food, Drug, and Cosmetic Act to include gluten-containing grain in the definition of a major food allergen.
- Congress: 119
- Bill type: HR
- Bill number: 9048
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:05:48Z
- Update date including text: 2026-05-30T09:28:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9048",
    "number": "9048",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "To amend the Federal Food, Drug, and Cosmetic Act to include gluten-containing grain in the definition of a major food allergen.",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:48Z",
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
          "date": "2026-05-29T16:04:15Z",
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
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MN"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to include gluten-containing grain in the definition of a major food allergen.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:05:48Z"
    },
    {
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to include gluten-containing grain in the definition of a major food allergen.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:05:48Z"
    }
  ]
}
```
