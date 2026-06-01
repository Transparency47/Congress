# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/300?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/300
- Title: Electing Members to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 300
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-04-10T15:15:00Z
- Update date including text: 2025-04-10T15:15:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 15:23:41 - Floor: Considered as privileged matter. (consideration: CR H1481-1482: 2)
- 2025-04-08 15:24:11 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H1482)
- 2025-04-08 15:24:11 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H1482)
- 2025-04-08 15:24:16 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 15:23:41 - Floor: Considered as privileged matter. (consideration: CR H1481-1482: 2)
- 2025-04-08 15:24:11 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H1482)
- 2025-04-08 15:24:11 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H1482)
- 2025-04-08 15:24:16 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/300",
    "number": "300",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Electing Members to certain standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-04-10T15:15:00Z",
    "updateDateIncludingText": "2025-04-10T15:15:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-04-08",
      "actionTime": "15:24:16",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-04-08",
      "actionTime": "15:24:11",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H1482)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-04-08",
      "actionTime": "15:24:11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H1482)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-04-08",
      "actionTime": "15:23:41",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H1481-1482: 2)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres300eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 300\nIn the House of Representatives, U. S.,\nApril 8, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committees of the House of Representatives:\nCommittee on Education and Workforce:\nMr. Fine.\nCommittee on Small Business:\nMr. Patronis.\nCommittee on Transportation and Infrastructure:\nMr. Patronis.",
      "versionDate": "2025-04-08",
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
            "updateDate": "2025-04-10T15:14:47Z"
          },
          {
            "name": "House Committee on Education and Workforce",
            "updateDate": "2025-04-10T15:14:21Z"
          },
          {
            "name": "House Committee on Small Business",
            "updateDate": "2025-04-10T15:13:55Z"
          },
          {
            "name": "House Committee on Transportation and Infrastructure",
            "updateDate": "2025-04-10T15:14:10Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-04-10T15:14:53Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-04-10T15:15:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-04-10T13:16:50Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres300eh.xml"
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
      "updateDate": "2025-04-09T08:06:47Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T08:06:47Z"
    }
  ]
}
```
