# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/978?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/978
- Title: Expressing the profound sorrow of the House of Representatives on the death of the Honorable Doug LaMalfa.
- Congress: 119
- Bill type: HRES
- Bill number: 978
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-01-12T15:50:58Z
- Update date including text: 2026-01-12T15:50:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 12:03:48 - Floor: Considered as privileged matter. (consideration: CR H112)
- 2026-01-07 12:04:08 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H112)
- 2026-01-07 12:04:08 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H112)
- 2026-01-07 12:04:14 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 12:03:48 - Floor: Considered as privileged matter. (consideration: CR H112)
- 2026-01-07 12:04:08 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H112)
- 2026-01-07 12:04:08 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H112)
- 2026-01-07 12:04:14 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/978",
    "number": "978",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C000059",
        "district": "41",
        "firstName": "Ken",
        "fullName": "Rep. Calvert, Ken [R-CA-41]",
        "lastName": "Calvert",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Expressing the profound sorrow of the House of Representatives on the death of the Honorable Doug LaMalfa.",
    "type": "HRES",
    "updateDate": "2026-01-12T15:50:58Z",
    "updateDateIncludingText": "2026-01-12T15:50:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2026-01-07",
      "actionTime": "12:04:14",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2026-01-07",
      "actionTime": "12:04:08",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H112)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2026-01-07",
      "actionTime": "12:04:08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H112)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2026-01-07",
      "actionTime": "12:03:48",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H112)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres978eh.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 978\nIn the House of Representatives, U. S.,\nJanuary 7, 2026\nRESOLUTION\nThat the House has heard with profound sorrow of the death of the Honorable Doug LaMalfa, a Representative from the State of California.\nThat the Clerk communicate these resolutions to the Senate and transmit a copy thereof to the family of the deceased.\nThat when the House adjourns today, it adjourn as a further mark of respect to the memory of the deceased.",
      "versionDate": "2026-01-07",
      "versionType": "EH"
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
        "item": [
          {
            "name": "California",
            "updateDate": "2026-01-12T15:47:59Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2026-01-12T15:49:40Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2026-01-12T15:50:58Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2026-01-12T15:47:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-01-12T15:10:41Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres978eh.xml"
        }
      ],
      "type": "EH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Expressing the profound sorrow of the House of Representatives on the death of the Honorable Doug LaMalfa.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T09:07:21Z"
    },
    {
      "title": "Expressing the profound sorrow of the House of Representatives on the death of the Honorable Doug LaMalfa.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T09:07:20Z"
    }
  ]
}
```
