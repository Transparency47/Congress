# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/18?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/18
- Title: A resolution providing for sufficient time for legislation to be read.
- Congress: 119
- Bill type: SRES
- Bill number: 18
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-05-27T14:12:53Z
- Update date including text: 2025-05-27T14:12:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S80)
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S80)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/18",
    "number": "18",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A resolution providing for sufficient time for legislation to be read.",
    "type": "SRES",
    "updateDate": "2025-05-27T14:12:53Z",
    "updateDateIncludingText": "2025-05-27T14:12:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Rules and Administration. (text: CR S80)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T20:22:32Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres18is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 18\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Paul submitted the following resolution; which was referred to the Committee on Rules and Administration\nRESOLUTION\nProviding for sufficient time for legislation to be read.\n#### 1. Time for reading of legislation\n##### (a) In general\nIt shall not be in order for the Senate to consider any bill, resolution, message, conference report, amendment between the Houses, amendment, treaty, or other measure or matter until 1 session day has passed since introduction for every 20 pages included in the measure or matter in the usual form plus 1 session day for any number of remaining pages less than 20 in the usual form.\n##### (b) Point of order\n**(1) In general**\nAny Senator may raise a point of order that consideration of any bill, resolution, message, conference report, amendment, treaty, or other measure or matter is not in order under subsection (a). A motion to table the point of order shall not be in order.\n**(2) Waiver**\nParagraph (1) may be waived or suspended only by an affirmative vote of three-fifths of the Members, duly chosen and sworn. All motions to waive under this paragraph shall be debatable collectively for not to exceed 3 hours equally divided between the Senator raising the point of order and the Senator moving to waive the point of order or their designees. A motion to waive the point of order shall not be amendable.\n##### (c) Constitutional authority\nThis resolution is adopted pursuant to the power granted to each House of Congress to determine the Rules of its Proceedings in article I, section 5, clause 2 of the Constitution of the United States.",
      "versionDate": "2025-01-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-22T15:36:46Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-01-22T15:36:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-17T13:01:33Z"
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
          "measure-id": "id119sres18",
          "measure-number": "18",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres18v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution permits Senators to object to the consideration of a measure unless a required amount of time has passed since the measure's introduction. Specifically, the resolution requires that one session day elapse for every 20 pages included in the measure (plus one session day for any number of remaining pages less than 20).\u00a0An objection raised on these grounds may be waived or suspended only by an affirmative vote of three-fifths of the Senators.</p>"
        },
        "title": "A resolution providing for sufficient time for legislation to be read."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres18.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution permits Senators to object to the consideration of a measure unless a required amount of time has passed since the measure's introduction. Specifically, the resolution requires that one session day elapse for every 20 pages included in the measure (plus one session day for any number of remaining pages less than 20).\u00a0An objection raised on these grounds may be waived or suspended only by an affirmative vote of three-fifths of the Senators.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119sres18"
    },
    "title": "A resolution providing for sufficient time for legislation to be read."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution permits Senators to object to the consideration of a measure unless a required amount of time has passed since the measure's introduction. Specifically, the resolution requires that one session day elapse for every 20 pages included in the measure (plus one session day for any number of remaining pages less than 20).\u00a0An objection raised on these grounds may be waived or suspended only by an affirmative vote of three-fifths of the Senators.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119sres18"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres18is.xml"
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
      "title": "A resolution providing for sufficient time for legislation to be read.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-14T01:18:46Z"
    },
    {
      "title": "A resolution providing for sufficient time for legislation to be read.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T11:56:22Z"
    }
  ]
}
```
