# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/125
- Title: Electing a Member to a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 125
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-02-24T19:26:58Z
- Update date including text: 2025-02-24T19:26:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - Committee: Submitted in House
- 2025-02-11 14:02:11 - Floor: Considered as privileged matter. (consideration: CR H631)
- 2025-02-11 14:02:26 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H631)
- 2025-02-11 14:02:26 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H631)
- 2025-02-11 14:02:33 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-02-11: Submitted in House

## Actions

- 2025-02-11 - Committee: Submitted in House
- 2025-02-11 14:02:11 - Floor: Considered as privileged matter. (consideration: CR H631)
- 2025-02-11 14:02:26 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H631)
- 2025-02-11 14:02:26 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H631)
- 2025-02-11 14:02:33 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/125",
    "number": "125",
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
    "title": "Electing a Member to a certain standing committee of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-02-24T19:26:58Z",
    "updateDateIncludingText": "2025-02-24T19:26:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-02-11",
      "actionTime": "14:02:33",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-02-11",
      "actionTime": "14:02:26",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H631)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-02-11",
      "actionTime": "14:02:26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H631)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-02-11",
      "actionTime": "14:02:11",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H631)",
      "type": "Floor"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres125eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 125\nIn the House of Representatives, U. S.,\nFebruary 11, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Member be, and is hereby, elected to the following standing committee of the House of Representatives:\nCommittee on Ethics:\nMr. DeSaulnier.",
      "versionDate": "2025-02-11",
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
            "updateDate": "2025-02-24T19:26:20Z"
          },
          {
            "name": "House Committee on Ethics",
            "updateDate": "2025-02-24T19:26:32Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-02-24T19:26:51Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-02-24T19:26:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-21T14:46:10Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres125eh.xml"
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
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T09:00:56Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T09:00:56Z"
    }
  ]
}
```
