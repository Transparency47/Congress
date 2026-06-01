# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/433?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/433
- Title: A resolution expressing support for the contributions and achievements of student parents in seeking and completing a postsecondary education and designating September 2025 as "National Student Parent Month".
- Congress: 119
- Bill type: SRES
- Bill number: 433
- Origin chamber: Senate
- Introduced date: 2025-10-06
- Update date: 2026-04-01T18:58:16Z
- Update date including text: 2026-04-01T18:58:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-06: Introduced in Senate
- 2025-10-06 - IntroReferral: Introduced in Senate
- 2025-10-06 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR S6957-6958)
- Latest action: 2025-10-06: Introduced in Senate

## Actions

- 2025-10-06 - IntroReferral: Introduced in Senate
- 2025-10-06 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR S6957-6958)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/433",
    "number": "433",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "A resolution expressing support for the contributions and achievements of student parents in seeking and completing a postsecondary education and designating September 2025 as \"National Student Parent Month\".",
    "type": "SRES",
    "updateDate": "2026-04-01T18:58:16Z",
    "updateDateIncludingText": "2026-04-01T18:58:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR S6957-6958)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-06",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres433ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 433\nIN THE SENATE OF THE UNITED STATES\nOctober 6, 2025 Mr. Moran (for himself and Ms. Hassan ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nExpressing support for the contributions and achievements of student parents in seeking and completing a postsecondary education and designating September 2025 as National Student Parent Month .\nThat the Senate\u2014\n**(1)**\nexpresses support for the contributions and achievements of student parents in seeking and completing a postsecondary education; and\n**(2)**\ndesignates September 2025 as National Student Parent Month .",
      "versionDate": "2025-10-06",
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
            "name": "Child care and development",
            "updateDate": "2025-11-21T16:51:04Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-21T16:50:42Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-11-21T16:50:20Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-11-21T16:50:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-11-17T17:17:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-06",
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
          "measure-id": "id119sres433",
          "measure-number": "433",
          "measure-type": "sres",
          "orig-publish-date": "2025-10-06",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres433v55",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-10-06",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution designates September 2025 as National Student Parent Month.</p>"
        },
        "title": "A resolution expressing support for the contributions and achievements of student parents in seeking and completing a postsecondary education and designating September 2025 as \"National Student Parent Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres433.xml",
    "summary": {
      "actionDate": "2025-10-06",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates September 2025 as National Student Parent Month.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119sres433"
    },
    "title": "A resolution expressing support for the contributions and achievements of student parents in seeking and completing a postsecondary education and designating September 2025 as \"National Student Parent Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-06",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates September 2025 as National Student Parent Month.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119sres433"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres433ats.xml"
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
      "title": "A resolution expressing support for the contributions and achievements of student parents in seeking and completing a postsecondary education and designating September 2025 as \"National Student Parent Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T10:56:15Z"
    },
    {
      "title": "A resolution expressing support for the contributions and achievements of student parents in seeking and completing a postsecondary education and designating September 2025 as \"National Student Parent Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T10:56:15Z"
    }
  ]
}
```
