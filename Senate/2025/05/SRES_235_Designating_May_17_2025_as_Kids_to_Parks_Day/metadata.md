# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/235
- Title: A resolution designating May 17, 2025, as "Kids to Parks Day".
- Congress: 119
- Bill type: SRES
- Bill number: 235
- Origin chamber: Senate
- Introduced date: 2025-05-19
- Update date: 2026-03-27T01:42:18Z
- Update date including text: 2026-03-27T01:42:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-19: Introduced in Senate
- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-19 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2966; text: CR S2974)
- Latest action: 2025-05-19: Introduced in Senate

## Actions

- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-19 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2966; text: CR S2974)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/235",
    "number": "235",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A resolution designating May 17, 2025, as \"Kids to Parks Day\".",
    "type": "SRES",
    "updateDate": "2026-03-27T01:42:18Z",
    "updateDateIncludingText": "2026-03-27T01:42:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2966; text: CR S2974)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-19",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "MS"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-19",
      "state": "ME"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NM"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "MT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres235ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 235\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2025 Mr. Wyden (for himself, Mrs. Hyde-Smith , Mr. King , Mr. Heinrich , Mr. Daines , and Mr. Wicker ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating May 17, 2025, as Kids to Parks Day .\nThat the Senate\u2014\n**(1)**\ndesignates May 17, 2025, as Kids to Parks Day ;\n**(2)**\nrecognizes the importance of outdoor recreation and the preservation of open spaces in promoting the health and education of the young people of the United States; and\n**(3)**\nencourages the people of the United States to observe Kids to Parks Day with safe family trips to parks.",
      "versionDate": "2025-05-19",
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
            "name": "Child health",
            "updateDate": "2025-06-20T15:45:00Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-20T15:45:00Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-06-20T15:45:00Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2025-06-20T15:45:00Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-06-20T15:45:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-18T15:18:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-19",
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
          "measure-id": "id119sres235",
          "measure-number": "235",
          "measure-type": "sres",
          "orig-publish-date": "2025-05-19",
          "originChamber": "SENATE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres235v55",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-05-19",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution designates May 17, 2025, as Kids to Parks Day.</p><p>The resolution recognizes the importance of outdoor recreation and the preservation of open spaces in promoting the health and education of the young people of the United States.</p>"
        },
        "title": "A resolution designating May 17, 2025, as \"Kids to Parks Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres235.xml",
    "summary": {
      "actionDate": "2025-05-19",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates May 17, 2025, as Kids to Parks Day.</p><p>The resolution recognizes the importance of outdoor recreation and the preservation of open spaces in promoting the health and education of the young people of the United States.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119sres235"
    },
    "title": "A resolution designating May 17, 2025, as \"Kids to Parks Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-19",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates May 17, 2025, as Kids to Parks Day.</p><p>The resolution recognizes the importance of outdoor recreation and the preservation of open spaces in promoting the health and education of the young people of the United States.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119sres235"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres235ats.xml"
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
      "title": "A resolution designating May 17, 2025, as \"Kids to Parks Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T10:56:16Z"
    },
    {
      "title": "A resolution designating May 17, 2025, as \"Kids to Parks Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T10:56:16Z"
    }
  ]
}
```
