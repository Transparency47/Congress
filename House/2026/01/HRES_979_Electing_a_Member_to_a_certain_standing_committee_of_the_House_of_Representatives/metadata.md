# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/979?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/979
- Title: Electing a Member to a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 979
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-01-12T15:46:10Z
- Update date including text: 2026-01-12T15:46:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 12:10:22 - Floor: Considered as privileged matter. (consideration: CR H112)
- 2026-01-07 12:10:31 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H112)
- 2026-01-07 12:10:31 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H112)
- 2026-01-07 12:10:35 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 12:10:22 - Floor: Considered as privileged matter. (consideration: CR H112)
- 2026-01-07 12:10:31 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H112)
- 2026-01-07 12:10:31 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H112)
- 2026-01-07 12:10:35 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/979",
    "number": "979",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Electing a Member to a certain standing committee of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2026-01-12T15:46:10Z",
    "updateDateIncludingText": "2026-01-12T15:46:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2026-01-07",
      "actionTime": "12:10:35",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2026-01-07",
      "actionTime": "12:10:31",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H112)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2026-01-07",
      "actionTime": "12:10:31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H112)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2026-01-07",
      "actionTime": "12:10:22",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H112)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres979eh.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 979\nIn the House of Representatives, U. S.,\nJanuary 7, 2026\nRESOLUTION\nElecting a Member to a certain standing committee of the House of Representatives.\nThat\nthe following named Member be, and is hereby, elected to the following standing committee of the House of Representatives:\nCommittee on Ethics\nMr. Knott.",
      "versionDate": "2026-01-07",
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
            "updateDate": "2026-01-12T15:44:42Z"
          },
          {
            "name": "House Committee on Ethics",
            "updateDate": "2026-01-12T15:46:03Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2026-01-12T15:38:54Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2026-01-12T15:46:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-01-12T15:11:57Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres979eh.xml"
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
      "updateDate": "2026-01-10T09:09:06Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T09:07:25Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T09:07:25Z"
    }
  ]
}
```
