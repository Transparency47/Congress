# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/490?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/490
- Title: Expressing support for the designation of the second Saturday in June as "Veterans Get Outside Day".
- Congress: 119
- Bill type: HRES
- Bill number: 490
- Origin chamber: House
- Introduced date: 2025-06-09
- Update date: 2026-03-27T16:08:16Z
- Update date including text: 2026-03-27T16:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-09: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-09 - IntroReferral: Submitted in House
- 2025-06-09 - IntroReferral: Submitted in House
- Latest action: 2025-06-09: Submitted in House

## Actions

- 2025-06-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-09 - IntroReferral: Submitted in House
- 2025-06-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/490",
    "number": "490",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "A000380",
        "district": "1",
        "firstName": "Gabe",
        "fullName": "Rep. Amo, Gabe [D-RI-1]",
        "lastName": "Amo",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Expressing support for the designation of the second Saturday in June as \"Veterans Get Outside Day\".",
    "type": "HRES",
    "updateDate": "2026-03-27T16:08:16Z",
    "updateDateIncludingText": "2026-03-27T16:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
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
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T16:03:05Z",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres490ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 490\nIN THE HOUSE OF REPRESENTATIVES\nJune 9, 2025 Mr. Amo (for himself and Mr. Moulton ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of the second Saturday in June as Veterans Get Outside Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Veterans Get Outside Day ; and\n**(2)**\nencourages the Department of Veterans Affairs, the Forest Service, and the Department of the Interior to coordinate and cooperate in promoting Veterans Get Outside Day along with National Get Outdoors Day.",
      "versionDate": "2025-06-09",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-24T18:08:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-09",
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
          "measure-id": "id119hres490",
          "measure-number": "490",
          "measure-type": "hres",
          "orig-publish-date": "2025-06-09",
          "originChamber": "HOUSE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres490v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-06-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of Veterans Get Outside Day and encourages the Department of Veterans Affairs, the Forest Service within the Department of Agriculture, and the Department of the Interior to coordinate to promote the day along with National Get Outdoors Day.</p>"
        },
        "title": "Expressing support for the designation of the second Saturday in June as \"Veterans Get Outside Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres490.xml",
    "summary": {
      "actionDate": "2025-06-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Veterans Get Outside Day and encourages the Department of Veterans Affairs, the Forest Service within the Department of Agriculture, and the Department of the Interior to coordinate to promote the day along with National Get Outdoors Day.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hres490"
    },
    "title": "Expressing support for the designation of the second Saturday in June as \"Veterans Get Outside Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-06-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Veterans Get Outside Day and encourages the Department of Veterans Affairs, the Forest Service within the Department of Agriculture, and the Department of the Interior to coordinate to promote the day along with National Get Outdoors Day.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hres490"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres490ih.xml"
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
      "title": "Expressing support for the designation of the second Saturday in June as \"Veterans Get Outside Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T08:18:16Z"
    },
    {
      "title": "Expressing support for the designation of the second Saturday in June as \"Veterans Get Outside Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-10T08:05:49Z"
    }
  ]
}
```
