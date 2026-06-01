# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/39?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/39
- Title: Ranking a Member on a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 39
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2025-02-07T01:15:22Z
- Update date including text: 2025-02-07T01:15:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - Committee: Submitted in House
- 2025-01-14 - IntroReferral: Submitted in House
- 2025-01-14 12:11:52 - Floor: Considered as privileged matter. (consideration: CR H125)
- 2025-01-14 12:12:06 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H125)
- 2025-01-14 12:12:06 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H125)
- 2025-01-14 12:12:10 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-01-14: Submitted in House

## Actions

- 2025-01-14 - Committee: Submitted in House
- 2025-01-14 - IntroReferral: Submitted in House
- 2025-01-14 12:11:52 - Floor: Considered as privileged matter. (consideration: CR H125)
- 2025-01-14 12:12:06 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H125)
- 2025-01-14 12:12:06 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H125)
- 2025-01-14 12:12:10 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/39",
    "number": "39",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Ranking a Member on a certain standing committee of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-02-07T01:15:22Z",
    "updateDateIncludingText": "2025-02-07T01:15:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-01-14",
      "actionTime": "12:12:10",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-01-14",
      "actionTime": "12:12:06",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H125)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-01-14",
      "actionTime": "12:12:06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H125)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-01-14",
      "actionTime": "12:11:52",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H125)",
      "type": "Floor"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres39eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 39\nIn the House of Representatives, U. S.,\nJanuary 14, 2025\nRESOLUTION\nRanking a Member on a certain standing committee of the House of Representatives.\nThat the following named Member be, and is hereby, ranked on the following standing committee of the House of Representatives:\nCommittee on Appropriations:\nMs. Maloy (to rank immediately after Mr. Strong).",
      "versionDate": "2025-01-14",
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
            "updateDate": "2025-01-22T14:45:39Z"
          },
          {
            "name": "House Committee on Appropriations",
            "updateDate": "2025-01-22T14:45:54Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-22T14:45:32Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-01-22T14:45:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-16T14:42:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hres39",
          "measure-number": "39",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres39v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution ranks Representative Celeste Maloy of Utah immediately after Representative Dale Strong of Alabama on the Committee on Appropriations.</p>"
        },
        "title": "Ranking a Member on a certain standing committee of the House of Representatives."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres39.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution ranks Representative Celeste Maloy of Utah immediately after Representative Dale Strong of Alabama on the Committee on Appropriations.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hres39"
    },
    "title": "Ranking a Member on a certain standing committee of the House of Representatives."
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution ranks Representative Celeste Maloy of Utah immediately after Representative Dale Strong of Alabama on the Committee on Appropriations.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hres39"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres39eh.xml"
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
      "title": "Ranking a Member on a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-15T09:05:29Z"
    },
    {
      "title": "Ranking a Member on a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-15T09:05:29Z"
    }
  ]
}
```
