# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/6?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hconres/6
- Title: Majority Rule Resolution
- Congress: 119
- Bill type: HCONRES
- Bill number: 6
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-03-25T17:52:02Z
- Update date including text: 2025-03-25T17:52:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-28 - Committee: Submitted in House
- Latest action: 2025-01-28: Submitted in House

## Actions

- 2025-01-28 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-28 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hconres/6",
    "number": "6",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Majority Rule Resolution",
    "type": "HCONRES",
    "updateDate": "2025-03-25T17:52:02Z",
    "updateDateIncludingText": "2025-03-25T17:52:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-28",
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

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-01-28T16:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres6ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 6\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Williams of Georgia submitted the following concurrent resolution; which was referred to the Committee on Rules\nCONCURRENT RESOLUTION\nProviding for certain procedures for bringing debate to a close on any question in the House of Representatives and Senate, and for other purposes.\n#### 1. Short title\nThis resolution may be cited as the Majority Rule Resolution .\n#### 2. Procedures for consideration of bills and resolutions\n##### (a) In general\nNotwithstanding any provision of the Rules of the House of Representatives or the Standing Rules of the Senate, the House of Representatives and the Senate may not require that more than a majority of the Members of either House of Congress voting, a quorum being present, is required to bring debate to a close on any question in such House.\n##### (b) Rules of House of Representatives and Senate\nThis section is enacted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the Senate and House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of the bill or joint resolution involved, and supersede other rules only to the extent that it is inconsistent with such rules; and\n**(2)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.",
      "versionDate": "2025-01-28",
      "versionType": "IH"
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
            "name": "House of Representatives",
            "updateDate": "2025-03-25T17:51:57Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-25T17:51:51Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-03-25T17:52:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-31T14:26:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hconres6",
          "measure-number": "6",
          "measure-type": "hconres",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres6v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Majority Rule Resolution</strong></p><p>This concurrent resolution provides that the House of Representatives and the Senate may not require more than a simple majority of those voting, a quorum being present, in order to bring debate to a close in such chamber.</p>"
        },
        "title": "Majority Rule Resolution"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres6.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Majority Rule Resolution</strong></p><p>This concurrent resolution provides that the House of Representatives and the Senate may not require more than a simple majority of those voting, a quorum being present, in order to bring debate to a close in such chamber.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hconres6"
    },
    "title": "Majority Rule Resolution"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Majority Rule Resolution</strong></p><p>This concurrent resolution provides that the House of Representatives and the Senate may not require more than a simple majority of those voting, a quorum being present, in order to bring debate to a close in such chamber.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hconres6"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres6ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Majority Rule Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T11:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Majority Rule Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-29T11:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for certain procedures for bringing debate to a close on any question in the House of Representatives and Senate, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T11:48:17Z"
    }
  ]
}
```
