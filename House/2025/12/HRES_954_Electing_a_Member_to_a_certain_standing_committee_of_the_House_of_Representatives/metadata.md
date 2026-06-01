# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/954?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/954
- Title: Electing a Member to a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 954
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-01-05T16:54:17Z
- Update date including text: 2026-01-05T16:54:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 11:07:50 - Floor: Considered as privileged matter. (consideration: CR H5956)
- 2025-12-17 11:07:55 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H5956)
- 2025-12-17 11:07:55 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2025-12-17 11:07:57 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 11:07:50 - Floor: Considered as privileged matter. (consideration: CR H5956)
- 2025-12-17 11:07:55 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H5956)
- 2025-12-17 11:07:55 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2025-12-17 11:07:57 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/954",
    "number": "954",
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
    "updateDate": "2026-01-05T16:54:17Z",
    "updateDateIncludingText": "2026-01-05T16:54:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-12-17",
      "actionTime": "11:07:57",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-12-17",
      "actionTime": "11:07:55",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H5956)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-12-17",
      "actionTime": "11:07:55",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-12-17",
      "actionTime": "11:07:50",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H5956)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres954eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 954\nIn the House of Representatives, U. S.,\nDecember 17, 2025\nRESOLUTION\nElecting a Member to a certain standing committee of the House of Representatives.\nThat the following named Member be, and is hereby, elected to the following standing committee of the House of Representatives:\nCommittee on Science, Space, and Technology\nMr. Beyer.",
      "versionDate": "2025-12-17",
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
            "updateDate": "2026-01-05T16:53:55Z"
          },
          {
            "name": "House Committee on Science, Space, and Technology",
            "updateDate": "2026-01-05T16:54:17Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2026-01-05T16:53:48Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2026-01-05T16:54:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-01-05T14:28:51Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres954eh.xml"
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
      "updateDate": "2025-12-19T05:08:20Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T09:07:21Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T09:07:21Z"
    }
  ]
}
```
