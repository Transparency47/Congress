# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8905?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8905
- Title: To amend the Immigration and Nationality Act to prohibit leaders of certain religious denominations from being admitted to the United States under section 101(a)(15)(R) of that Act, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8905
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-20T08:08:28Z
- Update date including text: 2026-05-20T16:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8905",
    "number": "8905",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To amend the Immigration and Nationality Act to prohibit leaders of certain religious denominations from being admitted to the United States under section 101(a)(15)(R) of that Act, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:28Z",
    "updateDateIncludingText": "2026-05-20T16:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
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
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
          "date": "2026-05-19T16:01:00Z",
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

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To amend the Immigration and Nationality Act to prohibit leaders of certain religious denominations from being admitted to the United States under section 101(a)(15)(R) of that Act, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:08:28Z"
    },
    {
      "title": "To amend the Immigration and Nationality Act to prohibit leaders of certain religious denominations from being admitted to the United States under section 101(a)(15)(R) of that Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:08:27Z"
    }
  ]
}
```
