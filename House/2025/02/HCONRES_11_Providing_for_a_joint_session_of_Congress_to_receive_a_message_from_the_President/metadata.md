# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/11?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hconres/11
- Title: Providing for a joint session of Congress to receive a message from the President.
- Congress: 119
- Bill type: HCONRES
- Bill number: 11
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-03-03T16:59:36Z
- Update date including text: 2025-03-03T16:59:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Received in the Senate.
- 2025-02-11 - Committee: Submitted in House
- 2025-02-11 14:01:08 - Floor: Considered as privileged matter. (consideration: CR H630-631)
- 2025-02-11 14:01:55 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H631)
- 2025-02-11 14:01:55 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H631)
- 2025-02-11 14:02:00 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-02-19 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment by Unanimous Consent.
- 2025-02-19 - Floor: Resolution agreed to in Senate without amendment by Unanimous Consent. (consideration: CR S1038)
- 2025-02-20 - Floor: Message on Senate action sent to the House.
- Latest action: 2025-02-11: Submitted in House

## Actions

- 2025-02-11 - IntroReferral: Received in the Senate.
- 2025-02-11 - Committee: Submitted in House
- 2025-02-11 14:01:08 - Floor: Considered as privileged matter. (consideration: CR H630-631)
- 2025-02-11 14:01:55 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H631)
- 2025-02-11 14:01:55 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H631)
- 2025-02-11 14:02:00 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-02-19 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment by Unanimous Consent.
- 2025-02-19 - Floor: Resolution agreed to in Senate without amendment by Unanimous Consent. (consideration: CR S1038)
- 2025-02-20 - Floor: Message on Senate action sent to the House.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hconres/11",
    "number": "11",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Providing for a joint session of Congress to receive a message from the President.",
    "type": "HCONRES",
    "updateDate": "2025-03-03T16:59:36Z",
    "updateDateIncludingText": "2025-03-03T16:59:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-02-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment by Unanimous Consent. (consideration: CR S1038)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-02-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-02-11",
      "actionTime": "14:02:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-02-11",
      "actionTime": "14:01:55",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H631)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-02-11",
      "actionTime": "14:01:55",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H631)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-02-11",
      "actionTime": "14:01:08",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H630-631)",
      "type": "Floor"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres11rds.xml",
      "text": "III\n119th CONGRESS\n1st Session\nH. CON. RES. 11\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Received\nCONCURRENT RESOLUTION\nProviding for a joint session of Congress to receive a message from the President.\nThat the two Houses of Congress assemble in the Hall of the House of Representatives on Tuesday, March 4, 2025, at 9 p.m., for the purpose of receiving such communication as the President of the United States shall be pleased to make to them.",
      "versionDate": "2025-02-11",
      "versionType": "RDS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres11eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 11\nIN THE HOUSE OF REPRESENTATIVES\nCONCURRENT RESOLUTION\nProviding for a joint session of Congress to receive a message from the President.\nThat the two Houses of Congress assemble in the Hall of the House of Representatives on Tuesday, March 4, 2025, at 9 p.m., for the purpose of receiving such communication as the President of the United States shall be pleased to make to them.",
      "versionDate": "",
      "versionType": "EH"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres11enr.xml",
      "text": "IV\nOne Hundred Nineteenth Congress of the United States of America\nAt the First Session\nBegun and held at the City of Washington on Friday, the third day of January, two thousand and twenty-five\nH. CON. RES. 11\nFebruary 19, 2025 Agreed to\nCONCURRENT RESOLUTION\nProviding for a joint session of Congress to receive a message from the President.\nThat the two Houses of Congress assemble in the Hall of the House of Representatives on Tuesday, March 4, 2025, at 9 p.m., for the purpose of receiving such communication as the President of the United States shall be pleased to make to them.",
      "versionDate": "2025-02-19",
      "versionType": "ENR"
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
            "updateDate": "2025-02-24T19:35:30Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-02-24T19:35:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-21T14:54:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hconres11",
          "measure-number": "11",
          "measure-type": "hconres",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres11v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This concurrent resolution provides for a joint session of Congress on Tuesday, March 4, 2025, to receive a message from the President.</p>"
        },
        "title": "Providing for a joint session of Congress to receive a message from the President."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres11.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution provides for a joint session of Congress on Tuesday, March 4, 2025, to receive a message from the President.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hconres11"
    },
    "title": "Providing for a joint session of Congress to receive a message from the President."
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution provides for a joint session of Congress on Tuesday, March 4, 2025, to receive a message from the President.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hconres11"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres11rds.xml"
        }
      ],
      "type": "RDS"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres11eh.xml"
        }
      ],
      "type": "EH"
    },
    {
      "date": "2025-02-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres11enr.xml"
        }
      ],
      "type": "ENR"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Providing for a joint session of Congress to receive a message from the President.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T09:00:43Z"
    },
    {
      "title": "Providing for a joint session of Congress to receive a message from the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T09:00:43Z"
    }
  ]
}
```
