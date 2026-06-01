# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/14?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/14
- Title: Proposing an amendment to the Constitution of the United States to repeal the sixteenth article of amendment.
- Congress: 119
- Bill type: HJRES
- Bill number: 14
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-04-08T10:56:30Z
- Update date including text: 2025-04-08T10:56:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-04-07 - Floor: Message on Senate action sent to the House.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-04-07 - Floor: Message on Senate action sent to the House.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/14",
    "number": "14",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to repeal the sixteenth article of amendment.",
    "type": "HJRES",
    "updateDate": "2025-04-08T10:56:30Z",
    "updateDateIncludingText": "2025-04-08T10:56:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:40:50Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres14ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 14\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Davidson submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to repeal the sixteenth article of amendment.\n#### 1.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. The sixteenth article of amendment to the Constitution of the United States is hereby repealed, and the Congress shall have no power to lay and collect taxes on incomes, from whatever source derived, except in time of war declared by the Congress. 2. Section 1 of this article shall take effect beginning 2 years after ratification of this article. Not later than 180 days after such ratification, the Secretary of the Treasury shall submit a report to the Congress containing recommendations for any legislation that may be necessary to implement this article. .",
      "versionDate": "2025-01-09",
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
            "updateDate": "2025-01-22T16:55:52Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-01-22T16:55:37Z"
          },
          {
            "name": "Tax reform and tax simplification",
            "updateDate": "2025-01-22T16:55:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-01-16T16:18:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hjres14",
          "measure-number": "14",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-01-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres14v00",
            "update-date": "2025-01-17"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment repealing the Sixteenth Amendment to the Constitution. The Sixteenth Amendment to the Constitution, ratified in 1913, specifies that Congress may collect federal income taxes.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to repeal the sixteenth article of amendment."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres14.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment repealing the Sixteenth Amendment to the Constitution. The Sixteenth Amendment to the Constitution, ratified in 1913, specifies that Congress may collect federal income taxes.</p>",
      "updateDate": "2025-01-17",
      "versionCode": "id119hjres14"
    },
    "title": "Proposing an amendment to the Constitution of the United States to repeal the sixteenth article of amendment."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment repealing the Sixteenth Amendment to the Constitution. The Sixteenth Amendment to the Constitution, ratified in 1913, specifies that Congress may collect federal income taxes.</p>",
      "updateDate": "2025-01-17",
      "versionCode": "id119hjres14"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres14ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to repeal the sixteenth article of amendment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-10T09:18:17Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to repeal the sixteenth article of amendment.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:36Z"
    }
  ]
}
```
