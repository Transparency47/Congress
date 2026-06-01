# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9069?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9069
- Title: To limit the Department of Homeland Security from detaining children and individuals with a cognitive disability and to prohibit immigration enforcement actions at sensitive locations without a court-issued criminal warrant.
- Congress: 119
- Bill type: HR
- Bill number: 9069
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:06:07Z
- Update date including text: 2026-05-30T09:28:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9069",
    "number": "9069",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "To limit the Department of Homeland Security from detaining children and individuals with a cognitive disability and to prohibit immigration enforcement actions at sensitive locations without a court-issued criminal warrant.",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:07Z",
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
          "date": "2026-05-29T16:02:20Z",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "CO"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "title": "To limit the Department of Homeland Security from detaining children and individuals with a cognitive disability and to prohibit immigration enforcement actions at sensitive locations without a court-issued criminal warrant.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:06:07Z"
    },
    {
      "title": "To limit the Department of Homeland Security from detaining children and individuals with a cognitive disability and to prohibit immigration enforcement actions at sensitive locations without a court-issued criminal warrant.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:06:07Z"
    }
  ]
}
```
