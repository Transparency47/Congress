# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1201?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1201
- Title: Electing Members to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 1201
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-04-29T12:43:30Z
- Update date including text: 2026-04-29T12:43:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Submitted in House
- 2026-04-21 12:06:37 - Floor: Considered as privileged matter.
- 2026-04-21 12:06:45 - Floor: On agreeing to the resolution Agreed to without objection.
- 2026-04-21 12:06:45 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2026-04-21 12:06:50 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2026-04-21: Submitted in House

## Actions

- 2026-04-21 - IntroReferral: Submitted in House
- 2026-04-21 12:06:37 - Floor: Considered as privileged matter.
- 2026-04-21 12:06:45 - Floor: On agreeing to the resolution Agreed to without objection.
- 2026-04-21 12:06:45 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.
- 2026-04-21 12:06:50 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1201",
    "number": "1201",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Electing Members to certain standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2026-04-29T12:43:30Z",
    "updateDateIncludingText": "2026-04-29T12:43:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2026-04-21",
      "actionTime": "12:06:50",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2026-04-21",
      "actionTime": "12:06:45",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2026-04-21",
      "actionTime": "12:06:45",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2026-04-21",
      "actionTime": "12:06:37",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter.",
      "type": "Floor"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1201eh.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1201\nIn the House of Representatives, U. S.,\nApril 21, 2026\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committees of the House of Representatives:\nCommittee on Homeland Security:\nMr. Joyce of Ohio.\nCommittee on Appropriations:\nMr. Shreve.",
      "versionDate": "2026-04-21",
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
            "updateDate": "2026-04-29T12:43:06Z"
          },
          {
            "name": "House Committee on Appropriations",
            "updateDate": "2026-04-29T12:43:29Z"
          },
          {
            "name": "House Committee on Homeland Security",
            "updateDate": "2026-04-29T12:43:24Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2026-04-29T12:43:13Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2026-04-29T12:43:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-04-27T19:16:59Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1201eh.xml"
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
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Titles from EH (Engrossed in House) bill text",
      "titleTypeCode": "259",
      "updateDate": "2026-04-23T03:53:24Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T08:07:17Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T08:07:17Z"
    }
  ]
}
```
