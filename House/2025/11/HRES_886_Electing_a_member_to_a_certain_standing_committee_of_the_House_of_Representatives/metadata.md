# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/886
- Title: Electing a member to a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 886
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2025-11-21T19:05:42Z
- Update date including text: 2025-11-21T19:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 12:13:13 - Floor: Considered as privileged matter. (consideration: CR H4718)
- 2025-11-18 12:13:35 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H4718)
- 2025-11-18 12:13:35 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4718)
- 2025-11-18 12:13:39 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 12:13:13 - Floor: Considered as privileged matter. (consideration: CR H4718)
- 2025-11-18 12:13:35 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H4718)
- 2025-11-18 12:13:35 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4718)
- 2025-11-18 12:13:39 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/886",
    "number": "886",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000450",
        "district": "5",
        "firstName": "Virginia",
        "fullName": "Rep. Foxx, Virginia [R-NC-5]",
        "lastName": "Foxx",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Electing a member to a certain standing committee of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-11-21T19:05:42Z",
    "updateDateIncludingText": "2025-11-21T19:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-11-18",
      "actionTime": "12:13:39",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-11-18",
      "actionTime": "12:13:35",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H4718)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-11-18",
      "actionTime": "12:13:35",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4718)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-11-18",
      "actionTime": "12:13:13",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H4718)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres886eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 886\nIn the House of Representatives, U. S.,\nNovember 18, 2025\nRESOLUTION\nElecting a member to a certain standing committee of the House of Representatives.\nThat the following named Member be, and is hereby, elected to the following standing committee of the House of Representatives:\nCommittee on Homeland Security:\nMr. Fong.",
      "versionDate": "2025-11-18",
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
            "updateDate": "2025-11-21T19:05:04Z"
          },
          {
            "name": "House Committee on Homeland Security",
            "updateDate": "2025-11-21T19:04:34Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-11-21T19:05:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-11-20T14:07:10Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres886eh.xml"
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
      "title": "Electing a member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Titles from EH (Engrossed in House) bill text",
      "titleTypeCode": "259",
      "updateDate": "2025-11-19T09:23:16Z"
    },
    {
      "title": "Electing a member to a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T09:07:20Z"
    },
    {
      "title": "Electing a member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T09:07:20Z"
    }
  ]
}
```
