# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/365?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/365
- Title: Bolts Ditch Act
- Congress: 119
- Bill type: S
- Bill number: 365
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/365",
    "number": "365",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Bolts Ditch Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T22:25:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s365is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 365\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Bennet (for himself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to allow for additional entities to be eligible to complete the maintenance work on Bolts Ditch and the Bolts Ditch Headgate within the Holy Cross Wilderness, Colorado.\n#### 1. Short title\nThis Act may be cited as the Bolts Ditch Act .\n#### 2. Additional entities allowed to maintain Bolts Ditch and the Bolts Ditch Headgate\nSection 1101(a) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 604) is amended by inserting before the period at the end the following: , the Eagle River Water and Sanitation District, a Colorado Special District, or the Upper Eagle Regional Water Authority, an authority organized under the laws of the State of Colorado .",
      "versionDate": "2025-02-03",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-15",
        "text": "Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "1729",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Bolts Ditch Act",
      "type": "HR"
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
            "name": "Colorado",
            "updateDate": "2025-06-18T13:51:45Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2025-06-18T13:51:45Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2025-06-18T13:51:45Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-06-18T13:51:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T20:22:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-03",
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
          "measure-id": "id119s365",
          "measure-number": "365",
          "measure-type": "s",
          "orig-publish-date": "2025-02-03",
          "originChamber": "SENATE",
          "update-date": "2025-07-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s365v00",
            "update-date": "2025-07-18"
          },
          "action-date": "2025-02-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Bolts Ditch Act</strong></p><p>This bill allows additional entities\u2014the Eagle River Water and Sanitation District and the Upper Eagle Regional Water Authority\u2014to access and use the Bolts Ditch and its headgate within the Holy Cross Wilderness in Colorado for the purposes of the diversion of water and use, maintenance, and repair of such ditch and headgate.</p>"
        },
        "title": "Bolts Ditch Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s365.xml",
    "summary": {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Bolts Ditch Act</strong></p><p>This bill allows additional entities\u2014the Eagle River Water and Sanitation District and the Upper Eagle Regional Water Authority\u2014to access and use the Bolts Ditch and its headgate within the Holy Cross Wilderness in Colorado for the purposes of the diversion of water and use, maintenance, and repair of such ditch and headgate.</p>",
      "updateDate": "2025-07-18",
      "versionCode": "id119s365"
    },
    "title": "Bolts Ditch Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Bolts Ditch Act</strong></p><p>This bill allows additional entities\u2014the Eagle River Water and Sanitation District and the Upper Eagle Regional Water Authority\u2014to access and use the Bolts Ditch and its headgate within the Holy Cross Wilderness in Colorado for the purposes of the diversion of water and use, maintenance, and repair of such ditch and headgate.</p>",
      "updateDate": "2025-07-18",
      "versionCode": "id119s365"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s365is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Bolts Ditch Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T03:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bolts Ditch Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to allow for additional entities to be eligible to complete the maintenance work on Bolts Ditch and the Bolts Ditch Headgate within the Holy Cross Wilderness, Colorado.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:26Z"
    }
  ]
}
```
