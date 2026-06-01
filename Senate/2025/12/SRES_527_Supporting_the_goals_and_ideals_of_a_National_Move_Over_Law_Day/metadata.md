# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/527
- Title: A resolution supporting the goals and ideals of a National Move Over Law Day.
- Congress: 119
- Bill type: SRES
- Bill number: 527
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-03-14T19:56:37Z
- Update date including text: 2026-03-14T19:56:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-12-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487; text: CR S8486)
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-12-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487; text: CR S8486)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/527",
    "number": "527",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A resolution supporting the goals and ideals of a National Move Over Law Day.",
    "type": "SRES",
    "updateDate": "2026-03-14T19:56:37Z",
    "updateDateIncludingText": "2026-03-14T19:56:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487; text: CR S8486)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-03",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres527ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 527\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Blumenthal (for himself and Mrs. Fischer ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nSupporting the goals and ideals of a National Move Over Law Day.\nThat the Senate\u2014\n**(1)**\nsupports the goals and ideals of a National Move Over Law Day; and\n**(2)**\nurges national, State, and regional incident management organizations\u2014\n**(A)**\nto spread awareness and promote the existence of, and adherence to, State move over laws; and\n**(B)**\nto educate the public further on the dangers and loss of life that occur if State move over laws are not faithfully observed.",
      "versionDate": "2025-12-03",
      "versionType": "ATS"
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
            "name": "Accidents",
            "updateDate": "2025-12-08T20:28:04Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-12-08T20:28:04Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2025-12-08T20:28:04Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-12-08T20:28:04Z"
          },
          {
            "name": "Worker safety and health",
            "updateDate": "2025-12-08T20:28:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-06T13:10:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-03",
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
          "measure-id": "id119sres527",
          "measure-number": "527",
          "measure-type": "sres",
          "orig-publish-date": "2025-12-03",
          "originChamber": "SENATE",
          "update-date": "2026-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres527v55",
            "update-date": "2026-03-14"
          },
          "action-date": "2025-12-03",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution expresses support for the goals and ideals of a National Move Over Law Day. It also urges national, state, and regional incident management organizations to spread awareness and promote the existence of, and adherence to, state move over laws.</p><p><em>Move over laws</em> generally require motorists to move at least one lane over when an emergency or rescue activity is taking place, including\u00a0on the shoulder or side of the roadway, or, if the motorist is unable to do so safely, to slow down and pass the scene with caution.</p>"
        },
        "title": "A resolution supporting the goals and ideals of a National Move Over Law Day."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres527.xml",
    "summary": {
      "actionDate": "2025-12-03",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution expresses support for the goals and ideals of a National Move Over Law Day. It also urges national, state, and regional incident management organizations to spread awareness and promote the existence of, and adherence to, state move over laws.</p><p><em>Move over laws</em> generally require motorists to move at least one lane over when an emergency or rescue activity is taking place, including\u00a0on the shoulder or side of the roadway, or, if the motorist is unable to do so safely, to slow down and pass the scene with caution.</p>",
      "updateDate": "2026-03-14",
      "versionCode": "id119sres527"
    },
    "title": "A resolution supporting the goals and ideals of a National Move Over Law Day."
  },
  "summaries": [
    {
      "actionDate": "2025-12-03",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution expresses support for the goals and ideals of a National Move Over Law Day. It also urges national, state, and regional incident management organizations to spread awareness and promote the existence of, and adherence to, state move over laws.</p><p><em>Move over laws</em> generally require motorists to move at least one lane over when an emergency or rescue activity is taking place, including\u00a0on the shoulder or side of the roadway, or, if the motorist is unable to do so safely, to slow down and pass the scene with caution.</p>",
      "updateDate": "2026-03-14",
      "versionCode": "id119sres527"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres527ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution supporting the goals and ideals of a National Move Over Law Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T11:56:19Z"
    },
    {
      "title": "A resolution supporting the goals and ideals of a National Move Over Law Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T11:56:19Z"
    }
  ]
}
```
