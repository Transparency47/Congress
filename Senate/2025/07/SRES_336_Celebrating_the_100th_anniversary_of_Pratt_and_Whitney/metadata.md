# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/336?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/336
- Title: A resolution celebrating the 100th anniversary of Pratt & Whitney.
- Congress: 119
- Bill type: SRES
- Bill number: 336
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2026-04-07T13:07:48Z
- Update date including text: 2026-04-07T13:07:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Referred to the Committee on the Judiciary.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/336",
    "number": "336",
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
    "title": "A resolution celebrating the 100th anniversary of Pratt & Whitney.",
    "type": "SRES",
    "updateDate": "2026-04-07T13:07:48Z",
    "updateDateIncludingText": "2026-04-07T13:07:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T17:36:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres336is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 336\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Blumenthal (for himself and Mr. Murphy ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCelebrating the 100th anniversary of Pratt & Whitney.\nThat the Senate\u2014\n**(1)**\nproudly celebrates the achievements and legacy of Pratt & Whitney, recognizing a century of excellence in engineering, innovation, and public service;\n**(2)**\ncommends and thanks the countless skilled employees, past and present, who have been the bedrock of the success of Pratt & Whitney, including machinists, engineers, technicians, and veterans; and\n**(3)**\nencourages all citizens to join in honoring the extraordinary contributions of this iconic company to the State of Connecticut, the United States, and the world.",
      "versionDate": "2025-07-24",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-01",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "627",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Celebrating the 100th anniversary of Pratt & Whitney.",
      "type": "HRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-05T16:29:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-24",
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
          "measure-id": "id119sres336",
          "measure-number": "336",
          "measure-type": "sres",
          "orig-publish-date": "2025-07-24",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres336v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-07-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution celebrates the achievements and\u00a0legacy of the Connecticut company Pratt & Whitney on its 100<sup>th </sup>anniversary and recognizes the company\u00a0for its excellence in engineering, innovation, and public service.</p><p>It also commends and thanks the past and present skilled employees of Pratt & Whitney, including machinists, engineers, technicians, and veterans.</p>"
        },
        "title": "A resolution celebrating the 100th anniversary of Pratt & Whitney."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres336.xml",
    "summary": {
      "actionDate": "2025-07-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution celebrates the achievements and\u00a0legacy of the Connecticut company Pratt & Whitney on its 100<sup>th </sup>anniversary and recognizes the company\u00a0for its excellence in engineering, innovation, and public service.</p><p>It also commends and thanks the past and present skilled employees of Pratt & Whitney, including machinists, engineers, technicians, and veterans.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119sres336"
    },
    "title": "A resolution celebrating the 100th anniversary of Pratt & Whitney."
  },
  "summaries": [
    {
      "actionDate": "2025-07-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution celebrates the achievements and\u00a0legacy of the Connecticut company Pratt & Whitney on its 100<sup>th </sup>anniversary and recognizes the company\u00a0for its excellence in engineering, innovation, and public service.</p><p>It also commends and thanks the past and present skilled employees of Pratt & Whitney, including machinists, engineers, technicians, and veterans.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119sres336"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres336is.xml"
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
      "title": "A resolution celebrating the 100th anniversary of Pratt & Whitney.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T03:18:22Z"
    },
    {
      "title": "A resolution celebrating the 100th anniversary of Pratt & Whitney.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T10:56:18Z"
    }
  ]
}
```
