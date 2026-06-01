# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2274
- Title: Court Shopping Deterrence Act
- Congress: 119
- Bill type: HR
- Bill number: 2274
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2026-04-03T15:55:24Z
- Update date including text: 2026-04-03T15:55:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2274",
    "number": "2274",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "R000612",
        "district": "6",
        "firstName": "John",
        "fullName": "Rep. Rose, John W. [R-TN-6]",
        "lastName": "Rose",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Court Shopping Deterrence Act",
    "type": "HR",
    "updateDate": "2026-04-03T15:55:24Z",
    "updateDateIncludingText": "2026-04-03T15:55:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
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
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:05:10Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2274ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2274\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Rose introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to provide that an appeal of an order granting a nationwide injunction issued by a district court of the United States shall lie to the Supreme Court.\n#### 1. Short title\nThis Act may be cited as the Court Shopping Deterrence Act .\n#### 2. Appeal of order granting a nationwide injunction\n##### (a) In General\nChapter 155 of title 28, United States Code, is amended by adding at the end the following:\n2285. Appeal of order granting a nationwide injunction (a) In general In the case that a district court of the United States grants a nationwide injunction, the appeal from the order granting such injunction shall lie to the Supreme Court. (b) Definition In this section, the term nationwide injunction means an order issued by a Federal court that purports to restrain the enforcement of a Federal statute, regulation, order, or similar authority against a non-party, unless the non-party is represented by a party acting in a representative capacity pursuant to the Federal Rules of Civil Procedure. .\n##### (b) Clerical amendment\nThe table of sections for chapter 155 of title 28, United States Code is amended by inserting after the item relating to section 2285 the following:\n2285. Appeal of order granting a nationwide injunction. .",
      "versionDate": "2025-03-21",
      "versionType": "Introduced in House"
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
            "name": "Federal district courts",
            "updateDate": "2026-03-05T15:54:25Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2026-03-05T15:54:25Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2026-03-05T15:54:25Z"
          },
          {
            "name": "Jurisdiction and venue",
            "updateDate": "2026-03-05T15:54:25Z"
          },
          {
            "name": "Supreme Court",
            "updateDate": "2026-03-05T15:54:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-04-01T16:21:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hr2274",
          "measure-number": "2274",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2274v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-03-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Court Shopping Deterrence Act</b></p> <p>This bill gives the U.S. Supreme Court exclusive jurisdiction to hear appeals from a nationwide injunction issued by a U.S. district court.</p>"
        },
        "title": "Court Shopping Deterrence Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2274.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Court Shopping Deterrence Act</b></p> <p>This bill gives the U.S. Supreme Court exclusive jurisdiction to hear appeals from a nationwide injunction issued by a U.S. district court.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr2274"
    },
    "title": "Court Shopping Deterrence Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Court Shopping Deterrence Act</b></p> <p>This bill gives the U.S. Supreme Court exclusive jurisdiction to hear appeals from a nationwide injunction issued by a U.S. district court.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr2274"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2274ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Court Shopping Deterrence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Court Shopping Deterrence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to provide that an appeal of an order granting a nationwide injunction issued by a district court of the United States shall lie to the Supreme Court.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:18:35Z"
    }
  ]
}
```
