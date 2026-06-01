# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/4?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/4
- Title: Authorizing the Clerk to inform the President of the election of the Speaker and the Clerk.
- Congress: 119
- Bill type: HRES
- Bill number: 4
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-15T18:21:13Z
- Update date including text: 2025-01-15T18:21:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- 2025-01-03 15:47:07 - Floor: Considered as privileged matter. (consideration: CR H8)
- 2025-01-03 15:47:17 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H8)
- 2025-01-03 15:47:17 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H8)
- 2025-01-03 15:47:37 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-01-03: Submitted in House

## Actions

- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- 2025-01-03 15:47:07 - Floor: Considered as privileged matter. (consideration: CR H8)
- 2025-01-03 15:47:17 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H8)
- 2025-01-03 15:47:17 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H8)
- 2025-01-03 15:47:37 - Floor: Motion to reconsider laid on the table Agreed to without objection.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/4",
    "number": "4",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "R000395",
        "district": "5",
        "firstName": "Harold",
        "fullName": "Rep. Rogers, Harold [R-KY-5]",
        "lastName": "Rogers",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Authorizing the Clerk to inform the President of the election of the Speaker and the Clerk.",
    "type": "HRES",
    "updateDate": "2025-01-15T18:21:13Z",
    "updateDateIncludingText": "2025-01-15T18:21:13Z"
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
      "actionTime": "15:47:37",
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
      "actionTime": "15:47:17",
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
      "actionTime": "15:47:17",
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
      "actionTime": "15:47:07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres4eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 4\nIn the House of Representatives, U. S.,\nJanuary 3, 2025\nRESOLUTION\nThat the Clerk be instructed to inform the President of the United States that the House of Representatives has elected Mike Johnson, a Representative from the State of Louisiana as Speaker, and Kevin McCumber, a citizen of the State of Illinois as Clerk, of the House of Representatives of the One Hundred Nineteenth Congress.",
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
            "name": "Congressional leadership",
            "updateDate": "2025-01-15T18:19:36Z"
          },
          {
            "name": "Congressional officers and employees",
            "updateDate": "2025-01-15T18:19:45Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-01-15T18:20:00Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-15T18:21:01Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-01-15T18:21:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-08T18:46:17Z"
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
          "measure-id": "id119hres4",
          "measure-number": "4",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres4v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution provides for the President to be informed that Rep. Mike Johnson of Louisiana has been elected as Speaker and Kevin McCumber has been elected as Clerk of the House of Representatives of the 119th Congress.</p>"
        },
        "title": "Authorizing the Clerk to inform the President of the election of the Speaker and the Clerk."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres4.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides for the President to be informed that Rep. Mike Johnson of Louisiana has been elected as Speaker and Kevin McCumber has been elected as Clerk of the House of Representatives of the 119th Congress.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hres4"
    },
    "title": "Authorizing the Clerk to inform the President of the election of the Speaker and the Clerk."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides for the President to be informed that Rep. Mike Johnson of Louisiana has been elected as Speaker and Kevin McCumber has been elected as Clerk of the House of Representatives of the 119th Congress.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hres4"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres4eh.xml"
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
      "title": "Authorizing the Clerk to inform the President of the election of the Speaker and the Clerk.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:38Z"
    },
    {
      "title": "Authorizing the Clerk to inform the President of the election of the Speaker and the Clerk.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:38Z"
    }
  ]
}
```
