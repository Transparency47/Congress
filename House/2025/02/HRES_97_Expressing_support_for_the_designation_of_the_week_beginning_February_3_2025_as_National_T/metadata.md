# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/97?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/97
- Title: Expressing support for the designation of the week beginning February 3, 2025, as "National Tribal Colleges and Universities Week".
- Congress: 119
- Bill type: HRES
- Bill number: 97
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-05-01T19:35:43Z
- Update date including text: 2025-05-01T19:35:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-04 - Committee: Submitted in House
- Latest action: 2025-02-04: Submitted in House

## Actions

- 2025-02-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-04 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/97",
    "number": "97",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "D000629",
        "district": "3",
        "firstName": "Sharice",
        "fullName": "Rep. Davids, Sharice [D-KS-3]",
        "lastName": "Davids",
        "party": "D",
        "state": "KS"
      }
    ],
    "title": "Expressing support for the designation of the week beginning February 3, 2025, as \"National Tribal Colleges and Universities Week\".",
    "type": "HRES",
    "updateDate": "2025-05-01T19:35:43Z",
    "updateDateIncludingText": "2025-05-01T19:35:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-04T17:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres97ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 97\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Ms. Davids of Kansas submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of the week beginning February 3, 2025, as National Tribal Colleges and Universities Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Tribal Colleges and Universities Week ; and\n**(2)**\nurges the people of the United States and interested groups to observe National Tribal Colleges and Universities Week with appropriate activities and programs to demonstrate support for Tribal colleges and universities.",
      "versionDate": "2025-02-04",
      "versionType": "IH"
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
        "actionDate": "2025-01-30",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S527; text: CR S525-526)"
      },
      "number": "49",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating the week beginning February 3, 2025, as \"National Tribal Colleges and Universities Week\".",
      "type": "SRES"
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
            "updateDate": "2025-04-09T18:44:12Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-09T18:44:12Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2025-04-09T18:44:12Z"
          },
          {
            "name": "Minority education",
            "updateDate": "2025-04-09T18:44:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-02-26T21:13:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "House",
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
          "measure-id": "id119hres97",
          "measure-number": "97",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres97v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Tribal Colleges and Universities Week. </p>"
        },
        "title": "Expressing support for the designation of the week beginning February 3, 2025, as \"National Tribal Colleges and Universities Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres97.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Tribal Colleges and Universities Week. </p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hres97"
    },
    "title": "Expressing support for the designation of the week beginning February 3, 2025, as \"National Tribal Colleges and Universities Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Tribal Colleges and Universities Week. </p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hres97"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres97ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the designation of the week beginning February 3, 2025, as \"National Tribal Colleges and Universities Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T12:03:28Z"
    },
    {
      "title": "Expressing support for the designation of the week beginning February 3, 2025, as \"National Tribal Colleges and Universities Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T09:06:11Z"
    }
  ]
}
```
