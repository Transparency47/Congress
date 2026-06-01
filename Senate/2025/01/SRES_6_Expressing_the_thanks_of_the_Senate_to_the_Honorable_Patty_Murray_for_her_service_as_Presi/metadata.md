# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/6?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/6
- Title: A resolution expressing the thanks of the Senate to the Honorable Patty Murray for her service as President Pro Tempore of the United States Senate and to designate Senator Murray as President Pro Tempore Emerita of the United States Senate.
- Congress: 119
- Bill type: SRES
- Bill number: 6
- Origin chamber: Senate
- Introduced date: 2025-01-03
- Update date: 2025-01-30T22:47:23Z
- Update date including text: 2025-01-30T22:47:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in Senate
- 2025-01-03 - IntroReferral: Introduced in Senate
- 2025-01-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-01-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6-7; text: CR S6-7)
- Latest action: 2025-01-03: Introduced in Senate

## Actions

- 2025-01-03 - IntroReferral: Introduced in Senate
- 2025-01-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-01-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6-7; text: CR S6-7)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/6",
    "number": "6",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "A resolution expressing the thanks of the Senate to the Honorable Patty Murray for her service as President Pro Tempore of the United States Senate and to designate Senator Murray as President Pro Tempore Emerita of the United States Senate.",
    "type": "SRES",
    "updateDate": "2025-01-30T22:47:23Z",
    "updateDateIncludingText": "2025-01-30T22:47:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6-7; text: CR S6-7)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-03",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres6ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 6\nIN THE SENATE OF THE UNITED STATES\nJanuary 3, 2025 Mr. Schumer submitted the following resolution; which was considered and agreed to\nRESOLUTION\nExpressing the thanks of the Senate to the Honorable Patty Murray for her service as President Pro Tempore of the United States Senate and to desiginate Senator Murray as President Pro Tempore Emerita of the United States Senate.\nThat the United States Senate expresses its deepest gratitude to Senator Murray for her dedication and commitment during her service to the Senate as the President Pro Tempore.\nFurther, as a token of appreciation of the Senate for her long and faithful service, Senator Patty Murray is hearby designated President Pro Tempore Emerita of the United States Senate.",
      "versionDate": "",
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
            "name": "Congressional leadership",
            "updateDate": "2025-01-15T18:37:22Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-01-15T18:37:30Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-01-15T18:37:40Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-01-15T18:37:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-13T12:59:01Z"
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
          "measure-id": "id119sres6",
          "measure-number": "6",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "SENATE",
          "update-date": "2025-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres6v00",
            "update-date": "2025-01-30"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution thanks Senator Patty Murray (of Washington) for her service as the President Pro Tempore of the Senate and designates her as President Pro Tempore Emerita.</p>"
        },
        "title": "A resolution expressing the thanks of the Senate to the Honorable Patty Murray for her service as President Pro Tempore of the United States Senate and to designate Senator Murray as President Pro Tempore Emerita of the United States Senate."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres6.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution thanks Senator Patty Murray (of Washington) for her service as the President Pro Tempore of the Senate and designates her as President Pro Tempore Emerita.</p>",
      "updateDate": "2025-01-30",
      "versionCode": "id119sres6"
    },
    "title": "A resolution expressing the thanks of the Senate to the Honorable Patty Murray for her service as President Pro Tempore of the United States Senate and to designate Senator Murray as President Pro Tempore Emerita of the United States Senate."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution thanks Senator Patty Murray (of Washington) for her service as the President Pro Tempore of the Senate and designates her as President Pro Tempore Emerita.</p>",
      "updateDate": "2025-01-30",
      "versionCode": "id119sres6"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres6ats.xml"
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
      "title": "A resolution expressing the thanks of the Senate to the Honorable Patty Murray for her service as President Pro Tempore of the United States Senate and to designate Senator Murray as President Pro Tempore Emerita of the United States Senate.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-04T11:56:17Z"
    },
    {
      "title": "A resolution expressing the thanks of the Senate to the Honorable Patty Murray for her service as President Pro Tempore of the United States Senate and to designate Senator Murray as President Pro Tempore Emerita of the United States Senate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-04T11:56:17Z"
    }
  ]
}
```
