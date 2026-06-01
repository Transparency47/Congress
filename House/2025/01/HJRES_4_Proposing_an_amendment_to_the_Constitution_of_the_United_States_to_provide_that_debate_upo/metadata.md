# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/4?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/4
- Title: Proposing an amendment to the Constitution of the United States to provide that debate upon legislation pending before the Senate may not be brought to a close without the concurrence of a minimum of three-fifths of the Senators.
- Congress: 119
- Bill type: HJRES
- Bill number: 4
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-11-08T09:05:59Z
- Update date including text: 2025-11-08T09:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/4",
    "number": "4",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to provide that debate upon legislation pending before the Senate may not be brought to a close without the concurrence of a minimum of three-fifths of the Senators.",
    "type": "HJRES",
    "updateDate": "2025-11-08T09:05:59Z",
    "updateDateIncludingText": "2025-11-08T09:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:11:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "ME"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres4ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 4\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Fitzpatrick (for himself and Mr. Golden of Maine ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to provide that debate upon legislation pending before the Senate may not be brought to a close without the concurrence of a minimum of three-fifths of the Senators.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 The debate on any measure or motion pending before the Senate, excluding Presidential nominations, shall not be brought to a close except as provided under laws as in effect on January 3, 2025, unanimous consent, or the concurrence of a minimum of three-fifths of the Senators duly chosen and sworn. .",
      "versionDate": "2025-01-03",
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
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:54:59Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:55:09Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-01-15T18:55:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-07T12:23:42Z"
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
          "measure-id": "id119hjres4",
          "measure-number": "4",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres4v00",
            "update-date": "2025-01-23"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes amending the Constitution to limit how the Senate may end debate on a measure or motion. Specifically, the proposed amendment provides that debate may only be brought to a close as provided under laws as in effect on January 3, 2025; by unanimous consent; or with the concurrence of at least three-fifths of all Senators.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to provide that debate upon legislation pending before the Senate may not be brought to a close without the concurrence of a minimum of three-fifths of the Senators."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres4.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes amending the Constitution to limit how the Senate may end debate on a measure or motion. Specifically, the proposed amendment provides that debate may only be brought to a close as provided under laws as in effect on January 3, 2025; by unanimous consent; or with the concurrence of at least three-fifths of all Senators.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>",
      "updateDate": "2025-01-23",
      "versionCode": "id119hjres4"
    },
    "title": "Proposing an amendment to the Constitution of the United States to provide that debate upon legislation pending before the Senate may not be brought to a close without the concurrence of a minimum of three-fifths of the Senators."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes amending the Constitution to limit how the Senate may end debate on a measure or motion. Specifically, the proposed amendment provides that debate may only be brought to a close as provided under laws as in effect on January 3, 2025; by unanimous consent; or with the concurrence of at least three-fifths of all Senators.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>",
      "updateDate": "2025-01-23",
      "versionCode": "id119hjres4"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres4ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to provide that debate upon legislation pending before the Senate may not be brought to a close without the concurrence of a minimum of three-fifths of the Senators.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to provide that debate upon legislation pending before the Senate may not be brought to a close without the concurrence of a minimum of three-fifths of the Senators.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:39:36Z"
    }
  ]
}
```
