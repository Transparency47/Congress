# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/3?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/3
- Title: Authorizing the Speaker to appoint a committee to notify the President of the assembly of the Congress.
- Congress: 119
- Bill type: HRES
- Bill number: 3
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-15T18:19:16Z
- Update date including text: 2025-01-15T18:19:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- 2025-01-03 15:46:06 - Floor: Considered as privileged matter. (consideration: CR H8)
- 2025-01-03 15:46:16 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H8)
- 2025-01-03 15:46:16 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H8)
- 2025-01-03 15:46:36 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-01-03: Submitted in House

## Actions

- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- 2025-01-03 15:46:06 - Floor: Considered as privileged matter. (consideration: CR H8)
- 2025-01-03 15:46:16 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H8)
- 2025-01-03 15:46:16 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H8)
- 2025-01-03 15:46:36 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/3",
    "number": "3",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001176",
        "district": "1",
        "firstName": "Steve",
        "fullName": "Rep. Scalise, Steve [R-LA-1]",
        "lastName": "Scalise",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Authorizing the Speaker to appoint a committee to notify the President of the assembly of the Congress.",
    "type": "HRES",
    "updateDate": "2025-01-15T18:19:16Z",
    "updateDateIncludingText": "2025-01-15T18:19:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-01-03",
      "actionTime": "15:46:36",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-01-03",
      "actionTime": "15:46:16",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H8)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-01-03",
      "actionTime": "15:46:16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H8)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-01-03",
      "actionTime": "15:46:06",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H8)",
      "type": "Floor"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres3eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 3\nIn the House of Representatives, U. S.,\nJanuary 3, 2025\nRESOLUTION\nThat a committee of two Members be appointed by the Speaker on the part of the House of Representatives to join with a committee on the part of the Senate to notify the President of the United States that a quorum of each House has assembled and Congress is ready to receive any communication that he may be pleased to make.",
      "versionDate": "2025-01-03",
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
            "name": "Congressional operations and organization",
            "updateDate": "2025-01-15T18:19:03Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-01-15T18:19:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-08T18:42:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hres3",
          "measure-number": "3",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres3v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution provides for the House of Representatives (together with the Senate) to notify the President that a quorum of each chamber of Congress has assembled.</p>"
        },
        "title": "Authorizing the Speaker to appoint a committee to notify the President of the assembly of the Congress."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres3.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides for the House of Representatives (together with the Senate) to notify the President that a quorum of each chamber of Congress has assembled.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hres3"
    },
    "title": "Authorizing the Speaker to appoint a committee to notify the President of the assembly of the Congress."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides for the House of Representatives (together with the Senate) to notify the President that a quorum of each chamber of Congress has assembled.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hres3"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres3eh.xml"
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
      "title": "Authorizing the Speaker to appoint a committee to notify the President of the assembly of the Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:32Z"
    },
    {
      "title": "Authorizing the Speaker to appoint a committee to notify the President of the assembly of the Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:32Z"
    }
  ]
}
```
