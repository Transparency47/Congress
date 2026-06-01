# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8979?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8979
- Title: To effectively staff the high-need public elementary schools and secondary schools of the United States with school-based mental health services providers.
- Congress: 119
- Bill type: HR
- Bill number: 8979
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-22T08:08:19Z
- Update date including text: 2026-05-22T12:28:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-05-21: Introduced in House

## Actions

- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8979",
    "number": "8979",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001231",
        "district": "22",
        "firstName": "John",
        "fullName": "Rep. Mannion, John W. [D-NY-22]",
        "lastName": "Mannion",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To effectively staff the high-need public elementary schools and secondary schools of the United States with school-based mental health services providers.",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:19Z",
    "updateDateIncludingText": "2026-05-22T12:28:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-21",
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
          "date": "2026-05-21T14:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CT"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To effectively staff the high-need public elementary schools and secondary schools of the United States with school-based mental health services providers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T08:08:19Z"
    },
    {
      "title": "To effectively staff the high-need public elementary schools and secondary schools of the United States with school-based mental health services providers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T08:08:19Z"
    }
  ]
}
```
