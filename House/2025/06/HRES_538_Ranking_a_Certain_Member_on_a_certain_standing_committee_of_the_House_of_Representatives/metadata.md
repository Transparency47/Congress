# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/538?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/538
- Title: Ranking a Certain Member on a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 538
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2025-07-09T13:59:31Z
- Update date including text: 2025-07-09T13:59:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 14:20:04 - Floor: Considered as privileged matter. (consideration: CR H2909)
- 2025-06-24 14:20:27 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H2909)
- 2025-06-24 14:20:27 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2909)
- 2025-06-24 14:20:33 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 14:20:04 - Floor: Considered as privileged matter. (consideration: CR H2909)
- 2025-06-24 14:20:27 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H2909)
- 2025-06-24 14:20:27 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2909)
- 2025-06-24 14:20:33 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/538",
    "number": "538",
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
    "title": "Ranking a Certain Member on a certain standing committee of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-07-09T13:59:31Z",
    "updateDateIncludingText": "2025-07-09T13:59:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-06-24",
      "actionTime": "14:20:33",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-06-24",
      "actionTime": "14:20:27",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H2909)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-06-24",
      "actionTime": "14:20:27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H2909)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-06-24",
      "actionTime": "14:20:04",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H2909)",
      "type": "Floor"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres538eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 538\nIn the House of Representatives, U. S.,\nJune 24, 2025\nRESOLUTION\nRanking a Certain Member on a certain standing committee of the House of Representatives.\nThat the following named Member be, and is hereby, ranked as follows on the following standing committee of the House of Representatives:\nCommittee on Oversight and Government Reform: Mr. Garcia of California, to rank before Ms. Norton.",
      "versionDate": "2025-06-24",
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
            "updateDate": "2025-07-09T13:59:31Z"
          },
          {
            "name": "House Committee on Oversight and Government Reform",
            "updateDate": "2025-07-09T13:59:24Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-07-09T13:58:58Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-07-09T13:59:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-07-08T13:06:05Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres538eh.xml"
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
      "title": "Ranking a Certain Member on a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T08:06:45Z"
    },
    {
      "title": "Ranking a Certain Member on a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T08:06:45Z"
    }
  ]
}
```
