# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/427?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/427
- Title: A resolution designating October 8, 2025, as "National Hydrogen and Fuel Cell Day".
- Congress: 119
- Bill type: SRES
- Bill number: 427
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-04-08T18:20:11Z
- Update date including text: 2026-04-08T18:20:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-09-30 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-09-30 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/427",
    "number": "427",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "A resolution designating October 8, 2025, as \"National Hydrogen and Fuel Cell Day\".",
    "type": "SRES",
    "updateDate": "2026-04-08T18:20:11Z",
    "updateDateIncludingText": "2026-04-08T18:20:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CT"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres427ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 427\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Graham (for himself, Mr. Blumenthal , Mr. Murphy , and Mr. Coons ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating October 8, 2025, as National Hydrogen and Fuel Cell Day .\nThat the Senate designates October 8, 2025, as National Hydrogen and Fuel Cell Day .",
      "versionDate": "2025-09-30",
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
            "name": "Alternative and renewable resources",
            "updateDate": "2025-11-19T20:33:21Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-19T20:33:43Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2025-11-19T20:33:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-11-17T17:13:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119sres427",
          "measure-number": "427",
          "measure-type": "sres",
          "orig-publish-date": "2025-09-30",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres427v55",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-09-30",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution designates October 8, 2025, as National Hydrogen and Fuel Cell Day.</p>"
        },
        "title": "A resolution designating October 8, 2025, as \"National Hydrogen and Fuel Cell Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres427.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates October 8, 2025, as National Hydrogen and Fuel Cell Day.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres427"
    },
    "title": "A resolution designating October 8, 2025, as \"National Hydrogen and Fuel Cell Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates October 8, 2025, as National Hydrogen and Fuel Cell Day.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres427"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres427ats.xml"
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
      "title": "A resolution designating October 8, 2025, as \"National Hydrogen and Fuel Cell Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T10:56:20Z"
    },
    {
      "title": "A resolution designating October 8, 2025, as \"National Hydrogen and Fuel Cell Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T10:56:20Z"
    }
  ]
}
```
