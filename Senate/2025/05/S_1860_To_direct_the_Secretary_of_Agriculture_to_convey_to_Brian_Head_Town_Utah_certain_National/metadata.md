# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1860?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1860
- Title: Brian Head Town Land Conveyance Act
- Congress: 119
- Bill type: S
- Bill number: 1860
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1860",
    "number": "1860",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Brian Head Town Land Conveyance Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
        "item": [
          {
            "date": "2025-12-17T14:30:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-22T15:07:48Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:40Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1860is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1860\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Lee (for himself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of Agriculture to convey to Brian Head Town, Utah, certain National Forest System land.\n#### 1. Short title\nThis Act may be cited as the Brian Head Town Land Conveyance Act .\n#### 2. Conveyance of Federal land to Brian Head Town, Utah\n##### (a) Definitions\nIn this section:\n**(1) Federal land**\nThe term Federal land means\u2014\n**(A)**\nthe parcel of approximately 24 acres of National Forest System land within the boundary of the Dixie National Forest, as generally depicted as NFS Lands Selected for Transfer on the map entitled Forest Service to Brian Head Land Transfer and dated April 28, 2025; and\n**(B)**\nany improvements to the National Forest System land described in subparagraph (A).\n**(2) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n**(3) Town**\nThe term Town means Brian Head Town, Utah.\n##### (b) Conveyance\nAs soon as practicable after the date of enactment of this Act, the Secretary shall convey to the Town, without consideration and subject to any terms and conditions that the Secretary determines to be appropriate, all right, title, and interest of the United States in and to the Federal land, to be used by the Town for a public works facility or any other uses determined to be necessary by the Town.\n##### (c) Boundary modification\nOn the conveyance of the Federal land to the Town under subsection (b), the Secretary shall modify the boundary of the Dixie National Forest to reflect the conveyance of the Federal land.",
      "versionDate": "2025-05-22",
      "versionType": "Introduced in Senate"
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
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-15T21:05:23Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-12-15T21:05:28Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-12-15T21:05:18Z"
          },
          {
            "name": "Utah",
            "updateDate": "2025-12-15T21:05:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-18T15:44:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-22",
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
          "measure-id": "id119s1860",
          "measure-number": "1860",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1860v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Brian Head Town Land Conveyance Act</strong></p><p>This bill directs the Forest Service to convey approximately 24 acres of land within the Dixie National Forest to Brian Head Town, Utah, along with any improvements made to the land. The town must use the land for a public works facility or any other uses determined to be necessary by the town. The Forest Service must convey the land to the town without consideration (such as payment).\u00a0</p>"
        },
        "title": "Brian Head Town Land Conveyance Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1860.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Brian Head Town Land Conveyance Act</strong></p><p>This bill directs the Forest Service to convey approximately 24 acres of land within the Dixie National Forest to Brian Head Town, Utah, along with any improvements made to the land. The town must use the land for a public works facility or any other uses determined to be necessary by the town. The Forest Service must convey the land to the town without consideration (such as payment).\u00a0</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s1860"
    },
    "title": "Brian Head Town Land Conveyance Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Brian Head Town Land Conveyance Act</strong></p><p>This bill directs the Forest Service to convey approximately 24 acres of land within the Dixie National Forest to Brian Head Town, Utah, along with any improvements made to the land. The town must use the land for a public works facility or any other uses determined to be necessary by the town. The Forest Service must convey the land to the town without consideration (such as payment).\u00a0</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s1860"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1860is.xml"
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
      "title": "Brian Head Town Land Conveyance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Brian Head Town Land Conveyance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Agriculture to convey to Brian Head Town, Utah, certain National Forest System land.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:40Z"
    }
  ]
}
```
