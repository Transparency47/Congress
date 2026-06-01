# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8751?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8751
- Title: To designate a senior official responsible for the management and oversight of all programs and activities of the Department of Defense related to the transition of members of the Armed Forces to civilian or reserve status, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8751
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-13T08:06:01Z
- Update date including text: 2026-05-13T15:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8751",
    "number": "8751",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "To designate a senior official responsible for the management and oversight of all programs and activities of the Department of Defense related to the transition of members of the Armed Forces to civilian or reserve status, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:01Z",
    "updateDateIncludingText": "2026-05-13T15:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:00:45Z",
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

## API Data: titles

```json
{
  "titles": [
    {
      "title": "To designate a senior official responsible for the management and oversight of all programs and activities of the Department of Defense related to the transition of members of the Armed Forces to civilian or reserve status, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T08:06:01Z"
    },
    {
      "title": "To designate a senior official responsible for the management and oversight of all programs and activities of the Department of Defense related to the transition of members of the Armed Forces to civilian or reserve status, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T08:06:01Z"
    }
  ]
}
```
