# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8851?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8851
- Title: To amend title 51, United States Code, to direct the Secretary of Transportation to establish an electronic processing portal for licenses and other approvals related to commercial space launch activities, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8851
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-16T08:08:04Z
- Update date including text: 2026-05-16T10:58:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, titles

## Timeline

- 2026-05-15: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-05-15: Introduced in House

## Actions

- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-15",
    "latestAction": {
      "actionDate": "2026-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8851",
    "number": "8851",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001099",
        "district": "8",
        "firstName": "Mike",
        "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
        "lastName": "Haridopolos",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To amend title 51, United States Code, to direct the Secretary of Transportation to establish an electronic processing portal for licenses and other approvals related to commercial space launch activities, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:04Z",
    "updateDateIncludingText": "2026-05-16T10:58:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-15",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-15",
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
          "date": "2026-05-15T13:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "CA"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend title 51, United States Code, to direct the Secretary of Transportation to establish an electronic processing portal for licenses and other approvals related to commercial space launch activities, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-16T08:08:04Z"
    },
    {
      "title": "To amend title 51, United States Code, to direct the Secretary of Transportation to establish an electronic processing portal for licenses and other approvals related to commercial space launch activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-16T08:08:04Z"
    }
  ]
}
```
