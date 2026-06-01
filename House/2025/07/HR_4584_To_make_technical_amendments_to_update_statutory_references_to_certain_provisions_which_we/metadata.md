# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4584?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4584
- Title: To make technical amendments to update statutory references to certain provisions which were formerly classified to chapters 14 and 19 of title 25, United States Code, and to correct related technical errors.
- Congress: 119
- Bill type: HR
- Bill number: 4584
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2026-02-03T19:50:17Z
- Update date including text: 2026-02-03T19:50:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, subjects, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4584",
    "number": "4584",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "B001322",
        "district": "5",
        "firstName": "Michael",
        "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
        "lastName": "Baumgartner",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "To make technical amendments to update statutory references to certain provisions which were formerly classified to chapters 14 and 19 of title 25, United States Code, and to correct related technical errors.",
    "type": "HR",
    "updateDate": "2026-02-03T19:50:17Z",
    "updateDateIncludingText": "2026-02-03T19:50:17Z"
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
      "actionDate": "2025-07-22",
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
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
            "date": "2025-09-10T20:33:31Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-22T14:05:10Z",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-09-12T16:11:49Z"
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
      "title": "To make technical amendments to update statutory references to certain provisions which were formerly classified to chapters 14 and 19 of title 25, United States Code, and to correct related technical errors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:44Z"
    },
    {
      "title": "To make technical amendments to update statutory references to certain provisions which were formerly classified to chapters 14 and 19 of title 25, United States Code, and to correct related technical errors.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:32Z"
    }
  ]
}
```
