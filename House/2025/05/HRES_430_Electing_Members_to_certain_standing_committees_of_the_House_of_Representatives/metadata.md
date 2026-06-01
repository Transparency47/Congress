# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/430?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/430
- Title: Electing Members to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 430
- Origin chamber: House
- Introduced date: 2025-05-20
- Update date: 2025-06-02T14:21:22Z
- Update date including text: 2025-06-02T14:21:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 12:12:17 - Floor: Considered as privileged matter.
- 2025-05-20 12:12:34 - Floor: On agreeing to the resolution Agreed to without objection.
- 2025-05-20 12:12:34 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2025-05-20 12:12:38 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-05-20: Introduced in House

## Actions

- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 12:12:17 - Floor: Considered as privileged matter.
- 2025-05-20 12:12:34 - Floor: On agreeing to the resolution Agreed to without objection.
- 2025-05-20 12:12:34 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2025-05-20 12:12:38 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/430",
    "number": "430",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "A000371",
        "district": "33",
        "firstName": "Pete",
        "fullName": "Rep. Aguilar, Pete [D-CA-33]",
        "lastName": "Aguilar",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Electing Members to certain standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-06-02T14:21:22Z",
    "updateDateIncludingText": "2025-06-02T14:21:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-05-20",
      "actionTime": "12:12:38",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-05-20",
      "actionTime": "12:12:34",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-05-20",
      "actionTime": "12:12:34",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-05-20",
      "actionTime": "12:12:17",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter.",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres430eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 430\nIn the House of Representatives, U. S.,\nMay 20, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committees of the House of Representatives:\nCommittee on Education and Workforce:\nMs. Ansari.\nCommittee on Homeland Security:\nMr. Green of Texas.\nCommittee on Natural Resources:\nMs. Lee of Nevada.\nCommittee on Science, Space, and Technology:\nMr. Foster.",
      "versionDate": "2025-05-20",
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
            "updateDate": "2025-06-02T14:21:07Z"
          },
          {
            "name": "House Committee on Homeland Security",
            "updateDate": "2025-06-02T14:20:20Z"
          },
          {
            "name": "House Committee on Natural Resources",
            "updateDate": "2025-06-02T14:20:30Z"
          },
          {
            "name": "House Committee on Science, Space, and Technology",
            "updateDate": "2025-06-02T14:21:22Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-06-02T14:20:10Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-06-02T14:20:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-28T13:32:29Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres430eh.xml"
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
      "updateDate": "2025-05-21T08:06:50Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T08:06:50Z"
    }
  ]
}
```
