# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1033
- Title: Expressing support for the designation of the week beginning February 2, 2026, as "National Tribal Colleges and Universities Week".
- Congress: 119
- Bill type: HRES
- Bill number: 1033
- Origin chamber: House
- Introduced date: 2026-02-03
- Update date: 2026-04-10T13:31:58Z
- Update date including text: 2026-04-10T13:31:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-03: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-03 - IntroReferral: Submitted in House
- 2026-02-03 - IntroReferral: Submitted in House
- Latest action: 2026-02-03: Submitted in House

## Actions

- 2026-02-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-03 - IntroReferral: Submitted in House
- 2026-02-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1033",
    "number": "1033",
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
    "title": "Expressing support for the designation of the week beginning February 2, 2026, as \"National Tribal Colleges and Universities Week\".",
    "type": "HRES",
    "updateDate": "2026-04-10T13:31:58Z",
    "updateDateIncludingText": "2026-04-10T13:31:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
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
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-02-03T15:01:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1033ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1033\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 3, 2026 Ms. Davids of Kansas (for herself and Mr. Cole ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of the week beginning February 2, 2026, as National Tribal Colleges and Universities Week .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Tribal Colleges and Universities Week ; and\n**(2)**\ncalls on the people of the United States and interested groups to observe National Tribal Colleges and Universities Week with appropriate activities and programs to demonstrate support for Tribal Colleges and Universities.",
      "versionDate": "2026-02-03",
      "versionType": "IH"
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
        "name": "Native Americans",
        "updateDate": "2026-02-11T21:36:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-03",
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
          "measure-id": "id119hres1033",
          "measure-number": "1033",
          "measure-type": "hres",
          "orig-publish-date": "2026-02-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1033v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2026-02-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of National Tribal Colleges and Universities Week.</p>"
        },
        "title": "Expressing support for the designation of the week beginning February 2, 2026, as \"National Tribal Colleges and Universities Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1033.xml",
    "summary": {
      "actionDate": "2026-02-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National Tribal Colleges and Universities Week.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hres1033"
    },
    "title": "Expressing support for the designation of the week beginning February 2, 2026, as \"National Tribal Colleges and Universities Week\"."
  },
  "summaries": [
    {
      "actionDate": "2026-02-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National Tribal Colleges and Universities Week.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hres1033"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1033ih.xml"
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
      "title": "Expressing support for the designation of the week beginning February 2, 2026, as \"National Tribal Colleges and Universities Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T09:18:17Z"
    },
    {
      "title": "Expressing support for the designation of the week beginning February 2, 2026, as \"National Tribal Colleges and Universities Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T09:06:35Z"
    }
  ]
}
```
