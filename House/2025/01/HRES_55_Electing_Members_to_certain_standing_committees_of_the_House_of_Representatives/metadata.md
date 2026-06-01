# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/55?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/55
- Title: Electing Members to certain standing committees of the House of Representatives.
- Congress: 119
- Bill type: HRES
- Bill number: 55
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-03-13T21:09:57Z
- Update date including text: 2025-03-13T21:09:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - Committee: Submitted in House
- 2025-01-22 - IntroReferral: Submitted in House
- 2025-01-22 12:16:39 - Floor: Considered as privileged matter. (consideration: CR H267)
- 2025-01-22 12:17:00 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H267)
- 2025-01-22 12:17:00 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H267)
- 2025-01-22 12:17:04 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- Latest action: 2025-01-22: Submitted in House

## Actions

- 2025-01-22 - Committee: Submitted in House
- 2025-01-22 - IntroReferral: Submitted in House
- 2025-01-22 12:16:39 - Floor: Considered as privileged matter. (consideration: CR H267)
- 2025-01-22 12:17:00 - Floor: On agreeing to the resolution Agreed to without objection. (text: CR H267)
- 2025-01-22 12:17:00 - Floor: Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H267)
- 2025-01-22 12:17:04 - Floor: Motion to reconsider laid on the table Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/55",
    "number": "55",
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
    "title": "Electing Members to certain standing committees of the House of Representatives.",
    "type": "HRES",
    "updateDate": "2025-03-13T21:09:57Z",
    "updateDateIncludingText": "2025-03-13T21:09:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H38310",
      "actionDate": "2025-01-22",
      "actionTime": "12:17:04",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37100",
      "actionDate": "2025-01-22",
      "actionTime": "12:17:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On agreeing to the resolution Agreed to without objection. (text: CR H267)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-01-22",
      "actionTime": "12:17:00",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On agreeing to the resolution Agreed to without objection. (text: CR H267)",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-01-22",
      "actionTime": "12:16:39",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered as privileged matter. (consideration: CR H267)",
      "type": "Floor"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres55eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 55\nIn the House of Representatives, U. S.,\nJanuary 22, 2025\nRESOLUTION\nElecting Members to certain standing committees of the House of Representatives.\nThat the following named Members be, and are hereby, elected to the following standing committees of the House of Representatives:\nCommittee on the Budget:\nMr. Doggett, Mr. Scott of Virginia, Mr. Peters of California, Mr. Panetta, Mrs. Watson Coleman, Ms. Plaskett, Ms. Escobar, Ms. Omar, Ms. Balint, Ms. Kaptur, Ms. Jayapal, Mr. Tonko, Mr. McGarvey, Mr. Amo.\nCommittee on House Administration:\nMr. Morelle, Ms. Sewell, Mrs. Torres of California, Ms. Johnson of Texas.\nCommittee on Natural Resources:\nMs. Vel\u00e1zquez, Mrs. Dingell, Mr. Soto, Ms. Brownley.\nCommittee on Oversight and Government Reform:\nMs. Pressley, Ms. Tlaib.",
      "versionDate": "2025-01-22",
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
            "updateDate": "2025-03-06T15:38:44Z"
          },
          {
            "name": "House Committee on House Administration",
            "updateDate": "2025-03-06T15:38:08Z"
          },
          {
            "name": "House Committee on Natural Resources",
            "updateDate": "2025-03-06T15:38:21Z"
          },
          {
            "name": "House Committee on Oversight and Government Reform",
            "updateDate": "2025-03-06T15:38:31Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-03-06T15:37:50Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-03-06T15:38:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-03-05T13:17:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hres55",
          "measure-number": "55",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres55v00",
            "update-date": "2025-03-13"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution elects designated Members of the House of Representatives to</p><ul><li>the Committee on the Budget,</li><li>the Committee on House Administration,</li><li>the Committee on Natural Resources, and</li><li>the Committee on Oversight and Government Reform.</li></ul>"
        },
        "title": "Electing Members to certain standing committees of the House of Representatives."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres55.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution elects designated Members of the House of Representatives to</p><ul><li>the Committee on the Budget,</li><li>the Committee on House Administration,</li><li>the Committee on Natural Resources, and</li><li>the Committee on Oversight and Government Reform.</li></ul>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hres55"
    },
    "title": "Electing Members to certain standing committees of the House of Representatives."
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution elects designated Members of the House of Representatives to</p><ul><li>the Committee on the Budget,</li><li>the Committee on House Administration,</li><li>the Committee on Natural Resources, and</li><li>the Committee on Oversight and Government Reform.</li></ul>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hres55"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres55eh.xml"
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
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-23T09:05:51Z"
    },
    {
      "title": "Electing Members to certain standing committees of the House of Representatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-23T09:05:51Z"
    }
  ]
}
```
