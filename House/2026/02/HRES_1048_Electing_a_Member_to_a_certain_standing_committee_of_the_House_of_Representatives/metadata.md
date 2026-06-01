# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1048?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1048
- Title: Electing a Member to a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 1048
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-19T15:00:12Z
- Update date including text: 2026-02-19T15:00:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 00:00:00 - Floor: Submitted in House
- 2026-02-10 13:24:14 - Floor: Considered as privileged matter. (consideration: CR H2115)
- 2026-02-10 13:24:37 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H2115)
- 2026-02-10 13:24:37 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2115)
- 2026-02-10 13:24:40 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2026-02-10: Submitted in House

## Actions

- 2026-02-10 - IntroReferral: Submitted in House
- 2026-02-10 00:00:00 - Floor: Submitted in House
- 2026-02-10 13:24:14 - Floor: Considered as privileged matter. (consideration: CR H2115)
- 2026-02-10 13:24:37 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H2115)
- 2026-02-10 13:24:37 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2115)
- 2026-02-10 13:24:40 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1048",
    "number": "1048",
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
    "updateDate": "2026-02-19T15:00:12Z",
    "updateDateIncludingText": "2026-02-19T15:00:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2026-02-10",
      "actionTime": "13:24:40",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2026-02-10",
      "actionTime": "13:24:37",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H2115)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2026-02-10",
      "actionTime": "13:24:37",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2115)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2026-02-10",
      "actionTime": "13:24:14",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H2115)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2026-02-10",
      "actionTime": "00:00:00",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Floor"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1048eh.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1048\nIn the House of Representatives, U. S.,\nFebruary 10, 2026\nRESOLUTION\nElecting a Member to a certain standing committee of the House of Representatives.\nThat the following named Member be, and is hereby, elected to the following standing committee of the House of Representatives:\nCommittee on Science, Space, and Technology\nMr. Menefee, to rank immediately after Mr. Riley of New York.",
      "versionDate": "2026-02-10",
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
            "updateDate": "2026-02-19T15:00:12Z"
          },
          {
            "name": "House Committee on Science, Space, and Technology",
            "updateDate": "2026-02-19T14:57:52Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2026-02-19T14:59:58Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2026-02-19T14:57:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-02-18T15:53:52Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1048eh.xml"
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
      "updateDate": "2026-02-12T04:38:21Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T09:06:35Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-11T09:06:35Z"
    }
  ]
}
```
