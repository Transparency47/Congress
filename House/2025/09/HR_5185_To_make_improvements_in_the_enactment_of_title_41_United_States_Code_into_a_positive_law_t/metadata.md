# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5185?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5185
- Title: To make improvements in the enactment of title 41, United States Code, into a positive law title and to improve the Code.
- Congress: 119
- Bill type: HR
- Bill number: 5185
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2026-03-16T19:03:12Z
- Update date including text: 2026-03-16T19:03:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, subjects, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5185",
    "number": "5185",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To make improvements in the enactment of title 41, United States Code, into a positive law title and to improve the Code.",
    "type": "HR",
    "updateDate": "2026-03-16T19:03:12Z",
    "updateDateIncludingText": "2026-03-16T19:03:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
        "item": [
          {
            "date": "2025-09-10T20:35:41Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-08T16:00:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": {
          "name": "Public contracts and procurement",
          "updateDate": "2026-03-16T19:03:12Z"
        }
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-29T20:05:11Z"
      }
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make improvements in the enactment of title 41, United States Code, into a positive law title and to improve the Code.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T08:18:26Z"
    },
    {
      "title": "To make improvements in the enactment of title 41, United States Code, into a positive law title and to improve the Code.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T08:05:40Z"
    }
  ]
}
```
