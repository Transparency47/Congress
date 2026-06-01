# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/108
- Title: Electing a Member to a certain standing committee of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 108
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-03-10T14:37:36Z
- Update date including text: 2025-03-10T14:37:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - Committee: Submitted in House
- 2025-02-05 12:18:04 - Floor: Considered as privileged matter. (consideration: CR H469)
- 2025-02-05 12:18:15 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H469)
- 2025-02-05 12:18:15 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H469)
- 2025-02-05 12:18:20 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-02-05: Submitted in House

## Actions

- 2025-02-05 - Committee: Submitted in House
- 2025-02-05 12:18:04 - Floor: Considered as privileged matter. (consideration: CR H469)
- 2025-02-05 12:18:15 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H469)
- 2025-02-05 12:18:15 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H469)
- 2025-02-05 12:18:20 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/108",
    "number": "108",
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
    "updateDate": "2025-03-10T14:37:36Z",
    "updateDateIncludingText": "2025-03-10T14:37:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-02-05",
      "actionTime": "12:18:20",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-02-05",
      "actionTime": "12:18:15",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H469)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-02-05",
      "actionTime": "12:18:15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H469)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-02-05",
      "actionTime": "12:18:04",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H469)",
      "type": "Floor"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres108eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 108\nIn the House of Representatives, U. S.,\nFebruary 5, 2025\nRESOLUTION\nRanking a Member on a certain standing committee of the House of Representatives.\nThat the following named Member be, and is hereby, elected to the following standing committee of the House of Representatives:\nCommittee on the Budget:\nMs. Chu to rank immediately after Ms. Jayapal.",
      "versionDate": "2025-02-05",
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
            "updateDate": "2025-02-19T14:40:27Z"
          },
          {
            "name": "House Committee on the Budget",
            "updateDate": "2025-02-19T14:37:38Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-02-19T14:40:18Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-02-19T14:37:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-18T17:39:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119hres108",
          "measure-number": "108",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres108v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution elects Representative Judy\u00a0Chu of California to the Committee on the Budget,\u00a0ranking immediately after Representative Pramila\u00a0Jayapal of Washington.</p>"
        },
        "title": "Electing a Member to a certain standing committee of the House of Representatives."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres108.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution elects Representative Judy\u00a0Chu of California to the Committee on the Budget,\u00a0ranking immediately after Representative Pramila\u00a0Jayapal of Washington.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hres108"
    },
    "title": "Electing a Member to a certain standing committee of the House of Representatives."
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution elects Representative Judy\u00a0Chu of California to the Committee on the Budget,\u00a0ranking immediately after Representative Pramila\u00a0Jayapal of Washington.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hres108"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres108eh.xml"
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
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T09:06:43Z"
    },
    {
      "title": "Electing a Member to a certain standing committee of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T09:06:43Z"
    }
  ]
}
```
