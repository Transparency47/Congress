# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/379
- Title: A resolution amending the Standing Rules of the Senate to authorize the Majority Leader to move to proceed to the en bloc consideration of certain nominations.
- Congress: 119
- Bill type: SRES
- Bill number: 379
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2026-04-07T16:27:56Z
- Update date including text: 2026-04-07T16:27:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S6472)
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S6472)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/379",
    "number": "379",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "A resolution amending the Standing Rules of the Senate to authorize the Majority Leader to move to proceed to the en bloc consideration of certain nominations.",
    "type": "SRES",
    "updateDate": "2026-04-07T16:27:56Z",
    "updateDateIncludingText": "2026-04-07T16:27:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Rules and Administration. (text: CR S6472)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-09-09T20:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres379is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 379\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Mr. Cornyn submitted the following resolution; which was referred to the Committee on Rules and Administration\nRESOLUTION\nAmending the Standing Rules of the Senate to authorize the Majority Leader to move to proceed to the en bloc consideration of certain nominations.\n#### 1. En bloc consideration of certain nominations\nRule XXXI of the Standing Rules of the Senate is amended by adding at the end the following:\n8.(a) In this paragraph, the term covered nomination means a nomination to a position that is not a position\u2014 (1) at level I of the Executive Schedule under section 5312 of title 5, United States Code; (2) as a judge of a court of appeals of the United States; or (3) as Chief Justice of the United States or as an Associate Justice of the Supreme Court of the United States. (b) It shall be in order for the Majority Leader to move to proceed to the en bloc consideration of not more than 10 covered nominations that were reported to the Senate by the same committee of the Senate and placed on the calendar. (c) Consideration of a motion to proceed under subparagraph (b), and the en bloc consideration of the nominations that are the subject of the motion, shall be conducted in the same manner as if it were a motion to proceed to the consideration of a single nomination. .",
      "versionDate": "2025-09-09",
      "versionType": "IS"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-09-23T14:44:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-09",
    "originChamber": "Senate",
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
          "measure-id": "id119sres379",
          "measure-number": "379",
          "measure-type": "sres",
          "orig-publish-date": "2025-09-09",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres379v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-09-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution generally permits the Senate to consider up to 10 nominations for most federal positions using a single motion to proceed (a proposal, typically offered by the Majority Leader, to bring a measure, nomination, or treaty to the Senate floor for debate and vote). However, certain nominations still require individual motions to proceed, namely nominations for Cabinet officials and other positions at Level I of the Executive Service, appellate judges, and Supreme Court Justices.</p>"
        },
        "title": "A resolution amending the Standing Rules of the Senate to authorize the Majority Leader to move to proceed to the en bloc consideration of certain nominations."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres379.xml",
    "summary": {
      "actionDate": "2025-09-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution generally permits the Senate to consider up to 10 nominations for most federal positions using a single motion to proceed (a proposal, typically offered by the Majority Leader, to bring a measure, nomination, or treaty to the Senate floor for debate and vote). However, certain nominations still require individual motions to proceed, namely nominations for Cabinet officials and other positions at Level I of the Executive Service, appellate judges, and Supreme Court Justices.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119sres379"
    },
    "title": "A resolution amending the Standing Rules of the Senate to authorize the Majority Leader to move to proceed to the en bloc consideration of certain nominations."
  },
  "summaries": [
    {
      "actionDate": "2025-09-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution generally permits the Senate to consider up to 10 nominations for most federal positions using a single motion to proceed (a proposal, typically offered by the Majority Leader, to bring a measure, nomination, or treaty to the Senate floor for debate and vote). However, certain nominations still require individual motions to proceed, namely nominations for Cabinet officials and other positions at Level I of the Executive Service, appellate judges, and Supreme Court Justices.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119sres379"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres379is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution amending the Standing Rules of the Senate to authorize the Majority Leader to move to proceed to the en bloc consideration of certain nominations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-10T13:18:21Z"
    },
    {
      "title": "A resolution amending the Standing Rules of the Senate to authorize the Majority Leader to move to proceed to the en bloc consideration of certain nominations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-10T10:56:23Z"
    }
  ]
}
```
