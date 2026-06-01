# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/484?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/484
- Title: A resolution designating October 2025 as "School Bus Safety Month".
- Congress: 119
- Bill type: SRES
- Bill number: 484
- Origin chamber: Senate
- Introduced date: 2025-11-05
- Update date: 2026-03-10T18:53:11Z
- Update date including text: 2026-03-10T18:53:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-05: Introduced in Senate
- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-11-05 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S7929; text: CR S7928)
- Latest action: 2025-11-05: Introduced in Senate

## Actions

- 2025-11-05 - IntroReferral: Introduced in Senate
- 2025-11-05 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-11-05 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S7929; text: CR S7928)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-05",
    "latestAction": {
      "actionDate": "2025-11-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/484",
    "number": "484",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "A resolution designating October 2025 as \"School Bus Safety Month\".",
    "type": "SRES",
    "updateDate": "2026-03-10T18:53:11Z",
    "updateDateIncludingText": "2026-03-10T18:53:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-05",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S7929; text: CR S7928)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-05",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres484ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 484\nIN THE SENATE OF THE UNITED STATES\nNovember 5, 2025 Mrs. Fischer (for herself and Mr. Peters ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating October 2025 as School Bus Safety Month .\nThat the Senate designates October 2025 as School Bus Safety Month .",
      "versionDate": "2025-11-05",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-11-18T19:09:18Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-11-18T19:09:11Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-11-18T19:09:40Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-11-18T19:09:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-17T18:17:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-05",
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
          "measure-id": "id119sres484",
          "measure-number": "484",
          "measure-type": "sres",
          "orig-publish-date": "2025-11-05",
          "originChamber": "SENATE",
          "update-date": "2026-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres484v55",
            "update-date": "2026-03-10"
          },
          "action-date": "2025-11-05",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution designates October 2025 as School Bus Safety Month.</p>"
        },
        "title": "A resolution designating October 2025 as \"School Bus Safety Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres484.xml",
    "summary": {
      "actionDate": "2025-11-05",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates October 2025 as School Bus Safety Month.</p>",
      "updateDate": "2026-03-10",
      "versionCode": "id119sres484"
    },
    "title": "A resolution designating October 2025 as \"School Bus Safety Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-11-05",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates October 2025 as School Bus Safety Month.</p>",
      "updateDate": "2026-03-10",
      "versionCode": "id119sres484"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres484ats.xml"
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
      "title": "A resolution designating October 2025 as \"School Bus Safety Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T11:56:13Z"
    },
    {
      "title": "A resolution designating October 2025 as \"School Bus Safety Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T11:56:13Z"
    }
  ]
}
```
