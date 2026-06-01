# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/509?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/509
- Title: A resolution designating October 16, 2025, and October 16, 2026, as "World Food Day".
- Congress: 119
- Bill type: SRES
- Bill number: 509
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2026-04-03T15:40:49Z
- Update date including text: 2026-04-03T15:40:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-11-19 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8248; text: CR S8244-8245)
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-11-19 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8248; text: CR S8244-8245)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/509",
    "number": "509",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A resolution designating October 16, 2025, and October 16, 2026, as \"World Food Day\".",
    "type": "SRES",
    "updateDate": "2026-04-03T15:40:49Z",
    "updateDateIncludingText": "2026-04-03T15:40:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8248; text: CR S8244-8245)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "AR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres509ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 509\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Coons (for himself, Mr. Boozman , Ms. Klobuchar , and Mr. Moran ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating October 16, 2025, and October 16, 2026, as World Food Day .\nThat the Senate\u2014\n**(1)**\ndesignates October 16, 2025, and October 16, 2026, as World Food Day ;\n**(2)**\nencourages the people of the United States to observe the days with appropriate ceremonies and activities; and\n**(3)**\nreaffirms the commitment of the United States to combating global food insecurity and malnutrition through humanitarian support and investment in resilient agriculture to improve long-term food security.",
      "versionDate": "2025-11-19",
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
            "updateDate": "2025-12-02T19:19:42Z"
          },
          {
            "name": "Cultural exchanges and relations",
            "updateDate": "2025-12-02T19:19:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-11-24T16:24:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-19",
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
          "measure-id": "id119sres509",
          "measure-number": "509",
          "measure-type": "sres",
          "orig-publish-date": "2025-11-19",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres509v55",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-11-19",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution designates October 16, 2025, and October 16, 2026, as World Food Day.</p><p>It also reaffirms the commitment of the United States to combating global food insecurity and malnutrition through humanitarian support and investment in resilient agriculture to improve long-term food security.</p>"
        },
        "title": "A resolution designating October 16, 2025, and October 16, 2026, as \"World Food Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres509.xml",
    "summary": {
      "actionDate": "2025-11-19",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates October 16, 2025, and October 16, 2026, as World Food Day.</p><p>It also reaffirms the commitment of the United States to combating global food insecurity and malnutrition through humanitarian support and investment in resilient agriculture to improve long-term food security.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119sres509"
    },
    "title": "A resolution designating October 16, 2025, and October 16, 2026, as \"World Food Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-11-19",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates October 16, 2025, and October 16, 2026, as World Food Day.</p><p>It also reaffirms the commitment of the United States to combating global food insecurity and malnutrition through humanitarian support and investment in resilient agriculture to improve long-term food security.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119sres509"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres509ats.xml"
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
      "title": "A resolution designating October 16, 2025, and October 16, 2026, as \"World Food Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T11:56:28Z"
    },
    {
      "title": "A resolution designating October 16, 2025, and October 16, 2026, as \"World Food Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-20T11:56:28Z"
    }
  ]
}
```
