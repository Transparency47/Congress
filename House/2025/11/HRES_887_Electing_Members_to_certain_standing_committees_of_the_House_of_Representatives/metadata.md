# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/887?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/887
- Title: Electing Members to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 887
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2025-11-21T19:03:27Z
- Update date including text: 2025-11-21T19:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 12:13:40 - Floor: Considered as privileged matter. (consideration: CR H4718)
- 2025-11-18 12:14:09 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H4718)
- 2025-11-18 12:14:09 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4718)
- 2025-11-18 12:14:13 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 12:13:40 - Floor: Considered as privileged matter. (consideration: CR H4718)
- 2025-11-18 12:14:09 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H4718)
- 2025-11-18 12:14:09 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H4718)
- 2025-11-18 12:14:13 - Floor: Motion to reconsider laid on the table Agreed to without objection.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/887",
    "number": "887",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000312",
        "district": "2",
        "firstName": "James",
        "fullName": "Rep. McGovern, James P. [D-MA-2]",
        "lastName": "McGovern",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Electing Members to certain standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-11-21T19:03:27Z",
    "updateDateIncludingText": "2025-11-21T19:03:27Z"
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
      "actionTime": "12:14:13",
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
      "actionTime": "12:14:09",
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
      "actionTime": "12:14:09",
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
      "actionTime": "12:13:40",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres887eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 887\nIn the House of Representatives, U. S.,\nNovember 18, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committees of the House of Representatives:\nCommittee on Armed Services:\nMr. Conaway.\nCommittee on Education and Workforce:\nMrs. Grijalva.\nCommittee on Homeland Security:\nMr. Walkinshaw (to rank immediately after Ms. Pou).\nCommittee on Natural Resources:\nMrs. Grijalva (to rank immediately after Ms. Rivas).",
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
            "updateDate": "2025-11-21T19:02:54Z"
          },
          {
            "name": "House Committee on Education and Workforce",
            "updateDate": "2025-11-21T19:02:22Z"
          },
          {
            "name": "House Committee on Homeland Security",
            "updateDate": "2025-11-21T19:02:33Z"
          },
          {
            "name": "House Committee on Natural Resources",
            "updateDate": "2025-11-21T19:02:40Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-11-21T19:03:18Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-11-21T19:03:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-11-20T14:08:06Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres887eh.xml"
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
      "updateDate": "2025-11-19T09:23:16Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T09:06:56Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T09:06:56Z"
    }
  ]
}
```
