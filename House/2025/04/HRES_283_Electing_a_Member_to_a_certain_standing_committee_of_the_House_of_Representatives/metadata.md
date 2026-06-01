# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/283?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/283
- Title: Electing a Member to a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 283
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-01-30T15:08:18Z
- Update date including text: 2026-01-30T15:08:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 14:34:09 - Floor: Considered as privileged matter. (consideration: CR H1399)
- 2025-04-01 14:34:37 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H1399)
- 2025-04-01 14:34:37 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2025-04-01 14:34:44 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 14:34:09 - Floor: Considered as privileged matter. (consideration: CR H1399)
- 2025-04-01 14:34:37 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H1399)
- 2025-04-01 14:34:37 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2025-04-01 14:34:44 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/283",
    "number": "283",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Electing a Member to a certain standing committee of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2026-01-30T15:08:18Z",
    "updateDateIncludingText": "2026-01-30T15:08:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-04-01",
      "actionTime": "14:34:44",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-04-01",
      "actionTime": "14:34:37",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H1399)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-04-01",
      "actionTime": "14:34:37",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-04-01",
      "actionTime": "14:34:09",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H1399)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres283eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 283\nIn the House of Representatives, U. S.,\nApril 1, 2025\nRESOLUTION\nElecting a Member to a certain standing committee of the House of Representatives.\nThat the following named Member be, and is hereby, elected to the following standing committee of the House of Representatives:\nCommittee on Foreign Affairs:\nMr. McCormick (to rank immediately after Mr. Self).",
      "versionDate": "2025-04-01",
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
            "updateDate": "2025-04-07T16:17:21Z"
          },
          {
            "name": "House Committee on Foreign Affairs",
            "updateDate": "2025-04-07T16:15:49Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-04-07T16:16:27Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-04-07T16:15:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-04-03T11:51:20Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres283eh.xml"
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
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Titles from EH (Engrossed in House) bill text",
      "titleTypeCode": "259",
      "updateDate": "2026-01-30T15:08:18Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:54Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:58:54Z"
    }
  ]
}
```
