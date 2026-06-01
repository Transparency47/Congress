# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/721?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/721
- Title: Electing Members to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 721
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-09-24T14:01:28Z
- Update date including text: 2025-09-24T14:01:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 14:50:57 - Floor: Considered as privileged matter. (consideration: CR H4331)
- 2025-09-16 14:51:10 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H4331)
- 2025-09-16 14:51:10 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4331: 1)
- 2025-09-16 14:51:45 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 14:50:57 - Floor: Considered as privileged matter. (consideration: CR H4331)
- 2025-09-16 14:51:10 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H4331)
- 2025-09-16 14:51:10 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4331: 1)
- 2025-09-16 14:51:45 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/721",
    "number": "721",
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
    "updateDate": "2025-09-24T14:01:28Z",
    "updateDateIncludingText": "2025-09-24T14:01:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-09-16",
      "actionTime": "14:51:45",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-09-16",
      "actionTime": "14:51:10",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H4331)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-09-16",
      "actionTime": "14:51:10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4331: 1)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-09-16",
      "actionTime": "14:50:57",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H4331)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres721eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 721\nIn the House of Representatives, U. S.,\nSeptember 16, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committees of the House of Representatives:\nCommittee on Oversight and Government Reform:\nMr. Walkinshaw to rank immediately after Mr. Min.\nCommittee on Transportation and Infrastructure:\nMr. Frost.",
      "versionDate": "2025-09-16",
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
            "updateDate": "2025-09-22T19:02:24Z"
          },
          {
            "name": "House Committee on Transportation and Infrastructure",
            "updateDate": "2025-09-22T19:02:10Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-09-22T19:02:31Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-09-22T19:02:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-09-22T11:42:12Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres721eh.xml"
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
      "updateDate": "2025-09-17T08:07:13Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T08:07:13Z"
    }
  ]
}
```
