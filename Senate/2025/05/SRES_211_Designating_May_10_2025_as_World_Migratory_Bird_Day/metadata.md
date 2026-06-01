# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/211?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/211
- Title: A resolution designating May 10, 2025, as "World Migratory Bird Day".
- Congress: 119
- Bill type: SRES
- Bill number: 211
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-04-27T20:17:58Z
- Update date including text: 2026-04-27T20:17:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-08 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2831; text: CR S2843)
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-08 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2831; text: CR S2843)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/211",
    "number": "211",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "A resolution designating May 10, 2025, as \"World Migratory Bird Day\".",
    "type": "SRES",
    "updateDate": "2026-04-27T20:17:58Z",
    "updateDateIncludingText": "2026-04-27T20:17:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2831; text: CR S2843)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres211ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 211\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Heinrich (for himself and Mr. Boozman ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating May 10, 2025, as World Migratory Bird Day .\nThat the Senate\u2014\n**(1)**\ndesignates May 10, 2025, as World Migratory Bird Day ; and\n**(2)**\nencourages the people of the United States to celebrate and support the conservation of migratory birds and their habitats through education, stewardship, community engagement, and bird watching.",
      "versionDate": "2025-05-08",
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
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-06-02T14:33:00Z"
          },
          {
            "name": "Birds",
            "updateDate": "2025-06-02T14:31:58Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-02T14:33:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-05-21T13:43:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119sres211",
          "measure-number": "211",
          "measure-type": "sres",
          "orig-publish-date": "2025-05-08",
          "originChamber": "SENATE",
          "update-date": "2026-04-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres211v55",
            "update-date": "2026-04-27"
          },
          "action-date": "2025-05-08",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution designates May 10, 2025, as World Migratory Bird Day.</p>"
        },
        "title": "A resolution designating May 10, 2025, as \"World Migratory Bird Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres211.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates May 10, 2025, as World Migratory Bird Day.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119sres211"
    },
    "title": "A resolution designating May 10, 2025, as \"World Migratory Bird Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates May 10, 2025, as World Migratory Bird Day.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119sres211"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres211ats.xml"
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
      "title": "A resolution designating May 10, 2025, as \"World Migratory Bird Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T10:56:19Z"
    },
    {
      "title": "A resolution designating May 10, 2025, as \"World Migratory Bird Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T10:56:19Z"
    }
  ]
}
```
