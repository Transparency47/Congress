# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/162?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/162
- Title: Electing Members to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 162
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2025-03-05T19:01:03Z
- Update date including text: 2025-03-05T19:01:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - Committee: Submitted in House
- 2025-02-25 14:09:24 - Floor: Considered as privileged matter. (consideration: CR H791)
- 2025-02-25 14:09:42 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H791)
- 2025-02-25 14:09:42 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H791)
- 2025-02-25 14:09:47 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-02-25: Submitted in House

## Actions

- 2025-02-25 - Committee: Submitted in House
- 2025-02-25 14:09:24 - Floor: Considered as privileged matter. (consideration: CR H791)
- 2025-02-25 14:09:42 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H791)
- 2025-02-25 14:09:42 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H791)
- 2025-02-25 14:09:47 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/162",
    "number": "162",
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
    "updateDate": "2025-03-05T19:01:03Z",
    "updateDateIncludingText": "2025-03-05T19:01:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-02-25",
      "actionTime": "14:09:47",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-02-25",
      "actionTime": "14:09:42",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H791)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-02-25",
      "actionTime": "14:09:42",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H791)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-02-25",
      "actionTime": "14:09:24",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H791)",
      "type": "Floor"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres162eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 162\nIn the House of Representatives, U. S.,\nFebruary 25, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committees of the House of Representatives:\nCommittee on Agriculture:\nMs. Pingree, Mr. Carbajal.\nCommittee on Foreign Affairs:\nMr. Schneider, Ms. Dean of Pennsylvania.",
      "versionDate": "2025-02-25",
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
            "updateDate": "2025-03-05T19:00:50Z"
          },
          {
            "name": "House Committee on Agriculture",
            "updateDate": "2025-03-05T19:00:57Z"
          },
          {
            "name": "House Committee on Foreign Affairs",
            "updateDate": "2025-03-05T19:01:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-03-05T13:53:10Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres162eh.xml"
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
      "updateDate": "2025-02-26T09:05:54Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T09:05:54Z"
    }
  ]
}
```
