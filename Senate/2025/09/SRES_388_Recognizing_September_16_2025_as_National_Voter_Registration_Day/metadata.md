# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/388?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/388
- Title: A resolution recognizing September 16, 2025, as "National Voter Registration Day".
- Congress: 119
- Bill type: SRES
- Bill number: 388
- Origin chamber: Senate
- Introduced date: 2025-09-15
- Update date: 2026-04-01T01:20:44Z
- Update date including text: 2026-04-01T01:20:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-15: Introduced in Senate
- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-09-15 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6623; text: CR S6602)
- Latest action: 2025-09-15: Introduced in Senate

## Actions

- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-09-15 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6623; text: CR S6602)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/388",
    "number": "388",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000355",
        "district": "",
        "firstName": "Mitch",
        "fullName": "Sen. McConnell, Mitch [R-KY]",
        "lastName": "McConnell",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A resolution recognizing September 16, 2025, as \"National Voter Registration Day\".",
    "type": "SRES",
    "updateDate": "2026-04-01T01:20:44Z",
    "updateDateIncludingText": "2026-04-01T01:20:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6623; text: CR S6602)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-15",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres388ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 388\nIN THE SENATE OF THE UNITED STATES\nSeptember 15, 2025 Mr. McConnell (for himself and Mr. Padilla ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nRecognizing September 16, 2025, as National Voter Registration Day .\nThat the Senate\u2014\n**(1)**\nrecognizes September 16, 2025, as National Voter Registration Day ; and\n**(2)**\nencourages each voting-eligible citizen of the United States\u2014\n**(A)**\nto register to vote;\n**(B)**\nto verify with the appropriate State or local election official that the name, address, and other personal information on record is current; and\n**(C)**\nto go to the polls on election day and vote if the voting-eligible citizen would like to do so.",
      "versionDate": "2025-09-15",
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-09-17T18:47:49Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-09-17T18:47:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-17T15:21:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-15",
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
          "measure-id": "id119sres388",
          "measure-number": "388",
          "measure-type": "sres",
          "orig-publish-date": "2025-09-15",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres388v55",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-09-15",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution recognizes September 16, 2025, as National Voter Registration Day and encourages those eligible to vote to register, verify their personal information on record with local election officials, and vote.</p>"
        },
        "title": "A resolution recognizing September 16, 2025, as \"National Voter Registration Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres388.xml",
    "summary": {
      "actionDate": "2025-09-15",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution recognizes September 16, 2025, as National Voter Registration Day and encourages those eligible to vote to register, verify their personal information on record with local election officials, and vote.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119sres388"
    },
    "title": "A resolution recognizing September 16, 2025, as \"National Voter Registration Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-09-15",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution recognizes September 16, 2025, as National Voter Registration Day and encourages those eligible to vote to register, verify their personal information on record with local election officials, and vote.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119sres388"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres388ats.xml"
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
      "title": "A resolution recognizing September 16, 2025, as \"National Voter Registration Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T10:56:18Z"
    },
    {
      "title": "A resolution recognizing September 16, 2025, as \"National Voter Registration Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T10:56:18Z"
    }
  ]
}
```
