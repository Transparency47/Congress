# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/1
- Title: Electing officers of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 1
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-23T14:39:27Z
- Update date including text: 2025-01-23T14:39:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- 2025-01-03 15:39:50 - Floor: Considered as privileged matter. (consideration: CR H7-8)
- 2025-01-03 15:40:08 - Floor: On agreeing to the resolution Agreed to by voice vote. (text: CR H7-8)
- 2025-01-03 15:40:08 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to by voice vote. (text: CR H7-8)
- 2025-01-03 15:40:18 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-01-03: Submitted in House

## Actions

- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- 2025-01-03 15:39:50 - Floor: Considered as privileged matter. (consideration: CR H7-8)
- 2025-01-03 15:40:08 - Floor: On agreeing to the resolution Agreed to by voice vote. (text: CR H7-8)
- 2025-01-03 15:40:08 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to by voice vote. (text: CR H7-8)
- 2025-01-03 15:40:18 - Floor: Motion to reconsider laid on the table Agreed to without objection.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/1",
    "number": "1",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001136",
        "district": "9",
        "firstName": "Lisa",
        "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
        "lastName": "McClain",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Electing officers of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-01-23T14:39:27Z",
    "updateDateIncludingText": "2025-01-23T14:39:27Z"
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
      "actionTime": "15:40:18",
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
      "actionTime": "15:40:08",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to by voice vote. (text: CR H7-8)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-01-03",
      "actionTime": "15:40:08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to by voice vote. (text: CR H7-8)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-01-03",
      "actionTime": "15:39:50",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H7-8)",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionCode": "73000",
                "actionDate": "2025-01-03",
                "actionTime": "15:40:08",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "On agreeing to the Aguilar amendment (A001) Failed by voice vote.",
                "type": "Floor"
              },
              {
                "actionCode": "71000",
                "actionDate": "2025-01-03",
                "actionTime": "15:40:07",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Amendment (A001) offered by Mr. Aguilar. (consideration: CR H7-8; text: CR H8)",
                "type": "Floor"
              },
              {
                "actionCode": "71000",
                "actionDate": "2025-01-03",
                "actionTime": "15:40:07",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "House Amendment Offered",
                "type": "Floor"
              },
              {
                "actionCode": "73000",
                "actionDate": "2025-01-03",
                "actionTime": "15:40:08",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "House amendment not agreed to: On agreeing to the Aguilar amendment (A001) Failed by voice vote.",
                "type": "Floor"
              }
            ]
          },
          "count": "4"
        },
        "amendedBill": {
          "congress": "119",
          "number": "1",
          "originChamber": "House",
          "originChamberCode": "H",
          "title": "Electing officers of the House of Representatives.",
          "type": "HRES",
          "updateDateIncludingText": "2025-01-23"
        },
        "chamber": "House of Representatives",
        "congress": "119",
        "description": "An amendment to elect officers of the House.",
        "latestAction": {
          "actionDate": "2025-01-03",
          "actionTime": "15:40:08",
          "text": "On agreeing to the Aguilar amendment (A001) Failed by voice vote."
        },
        "number": "1",
        "sponsors": {
          "item": {
            "bioguideId": "A000371",
            "district": "33",
            "firstName": "Pete",
            "fullName": "Rep. Aguilar, Pete [D-CA-33]",
            "lastName": "Aguilar",
            "party": "D",
            "state": "CA"
          }
        },
        "submittedDate": "2025-01-03T05:00:00Z",
        "type": "HAMDT",
        "updateDate": "2025-01-06T19:45:32Z"
      }
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres1eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 1\nIn the House of Representatives, U. S.,\nJanuary 3, 2025\nRESOLUTION\nThat Kevin McCumber of the State of Illinois be, and is hereby, chosen Clerk of the House of Representatives.\nThat William McFarland of the State of Maryland be, and is hereby, chosen Sergeant-at-Arms of the House of Representatives.\nThat Catherine Szpindor of the Commonwealth of Virginia be, and is hereby, chosen Chief Administrative Officer of the House of Representatives.",
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
            "name": "Congressional officers and employees",
            "updateDate": "2025-01-15T18:16:43Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-15T18:16:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-08T18:56:16Z"
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
          "measure-id": "id119hres1",
          "measure-number": "1",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1v00",
            "update-date": "2025-01-23"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution provides that Kevin McCumber of Illinois is elected Clerk,\u00a0William McFarland of Maryland is elected Sergeant-at-Arms, and Catherine Szpindor of Virginia is elected Chief Administrative Officer of the House of Representatives.</p>"
        },
        "title": "Electing officers of the House of Representatives."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides that Kevin McCumber of Illinois is elected Clerk,\u00a0William McFarland of Maryland is elected Sergeant-at-Arms, and Catherine Szpindor of Virginia is elected Chief Administrative Officer of the House of Representatives.</p>",
      "updateDate": "2025-01-23",
      "versionCode": "id119hres1"
    },
    "title": "Electing officers of the House of Representatives."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides that Kevin McCumber of Illinois is elected Clerk,\u00a0William McFarland of Maryland is elected Sergeant-at-Arms, and Catherine Szpindor of Virginia is elected Chief Administrative Officer of the House of Representatives.</p>",
      "updateDate": "2025-01-23",
      "versionCode": "id119hres1"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres1eh.xml"
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
      "title": "Electing officers of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:44Z"
    },
    {
      "title": "Electing officers of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:39:44Z"
    }
  ]
}
```
