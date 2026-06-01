# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/213?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/213
- Title: Electing Members to a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 213
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2025-03-18T13:35:58Z
- Update date including text: 2025-03-18T13:35:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: 
- 2025-03-11 - IntroReferral: Submitted in House
- 2025-03-11 17:55:44 - Floor: Considered as privileged matter. (consideration: CR H1127)
- 2025-03-11 17:55:44 - Floor: Submitted in House
- 2025-03-11 17:56:01 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H1127)
- 2025-03-11 17:56:01 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H1127)
- 2025-03-11 17:56:04 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Actions

- 2025-03-11 - IntroReferral: 
- 2025-03-11 - IntroReferral: Submitted in House
- 2025-03-11 17:55:44 - Floor: Considered as privileged matter. (consideration: CR H1127)
- 2025-03-11 17:55:44 - Floor: Submitted in House
- 2025-03-11 17:56:01 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H1127)
- 2025-03-11 17:56:01 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H1127)
- 2025-03-11 17:56:04 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": ""
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/213",
    "number": "213",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Electing Members to a certain standing committee of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-03-18T13:35:58Z",
    "updateDateIncludingText": "2025-03-18T13:35:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-03-11",
      "actionTime": "17:56:04",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-03-11",
      "actionTime": "17:56:01",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H1127)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-03-11",
      "actionTime": "17:56:01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H1127)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-03-11",
      "actionTime": "17:55:44",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H1127)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-03-11",
      "actionTime": "17:55:44",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Floor"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres213eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 213\nIn the House of Representatives, U. S.,\nMarch 11, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committee of the House of Representatives:\nCommittee on Ethics:\nMr. Rutherford, Mr. Garbarino, Mrs. Hinson, Mr. Moran.",
      "versionDate": "2025-03-11",
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
            "updateDate": "2025-03-18T13:35:58Z"
          },
          {
            "name": "House Committee on Ethics",
            "updateDate": "2025-03-18T13:35:42Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-03-18T13:32:39Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-03-18T13:35:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-03-13T15:15:51Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres213eh.xml"
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
      "title": "Electing Members to a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T08:06:41Z"
    },
    {
      "title": "Electing Members to a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T08:06:41Z"
    }
  ]
}
```
