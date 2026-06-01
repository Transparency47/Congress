# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/600?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/600
- Title: Electing Members to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 600
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2025-09-08T17:17:20Z
- Update date including text: 2025-09-08T17:17:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 12:02:37 - Floor: Considered as privileged matter. (consideration: CR H3539: 5)
- 2025-07-22 12:03:01 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H3539)
- 2025-07-22 12:03:01 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H3539)
- 2025-07-22 12:03:07 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 12:02:37 - Floor: Considered as privileged matter. (consideration: CR H3539: 5)
- 2025-07-22 12:03:01 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H3539)
- 2025-07-22 12:03:01 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H3539)
- 2025-07-22 12:03:07 - Floor: Motion to reconsider laid on the table Agreed to without objection.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/600",
    "number": "600",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001082",
        "district": "1",
        "firstName": "Kevin",
        "fullName": "Rep. Hern, Kevin [R-OK-1]",
        "lastName": "Hern",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Electing Members to certain standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-09-08T17:17:20Z",
    "updateDateIncludingText": "2025-09-08T17:17:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-07-22",
      "actionTime": "12:03:07",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-07-22",
      "actionTime": "12:03:01",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H3539)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-07-22",
      "actionTime": "12:03:01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H3539)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-07-22",
      "actionTime": "12:02:37",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H3539: 5)",
      "type": "Floor"
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres600eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 600\nIn the House of Representatives, U. S.,\nJuly 22, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committees of the House of Representatives:\nCommittee on Foreign Affairs:\nMr. Fine.\nCommittee on Homeland Security:\nMr. Garbarino, Chair.",
      "versionDate": "2025-07-22",
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
            "name": "Congressional committees",
            "updateDate": "2025-09-08T17:17:06Z"
          },
          {
            "name": "House Committee on Foreign Affairs",
            "updateDate": "2025-09-08T17:16:53Z"
          },
          {
            "name": "House Committee on Homeland Security",
            "updateDate": "2025-09-08T17:17:00Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-09-08T17:17:14Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-09-08T17:17:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-09-03T20:19:25Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres600eh.xml"
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
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:31Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T14:13:31Z"
    }
  ]
}
```
