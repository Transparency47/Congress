# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/601?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/601
- Title: A bill to remove restrictions from a parcel of land in Paducah, Kentucky.
- Congress: 119
- Bill type: S
- Bill number: 601
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-04-14T19:20:23Z
- Update date including text: 2026-04-14T19:20:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/601",
    "number": "601",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A bill to remove restrictions from a parcel of land in Paducah, Kentucky.",
    "type": "S",
    "updateDate": "2026-04-14T19:20:23Z",
    "updateDateIncludingText": "2026-04-14T19:20:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
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
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
            "date": "2026-03-04T16:02:18Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-13T20:35:45Z",
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
              "date": "2025-12-09T18:12:45Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
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
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s601is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 601\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Paul (for himself and Mr. McConnell ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo remove restrictions from a parcel of land in Paducah, Kentucky.\n#### 1. Removal of restriction\n##### (a) In general\nThe Secretary of the Interior shall execute such instruments as may be necessary to remove all deed restrictions from the parcel of land described in subsection (c).\n##### (b) Deed restrictions\nThe deed restrictions referred to in subsection (a) are those restrictions, including easements, exceptions, reservations, terms, conditions, and covenants described in the quitclaim deed from the United States to the City of Paducah, Kentucky, executed on April 27, 2012, and recorded by the Clerk of the County Court of McCracken County, Kentucky on pages 247 through 260 of Deed Book 1229.\n##### (c) Land description\nThe parcel of land referred to in subsection (a) is the parcel\u2014\n**(1)**\ncomprised of approximately 3.62 acres located at 2956 Park Avenue, on the Paducah Memorial Army Reserve Center, Paducah, McCracken County, Kentucky, including the improvements thereon; and\n**(2)**\nconveyed by the Secretary of the Interior to the City of Paducah, Kentucky.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2026-03-04",
        "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably."
      },
      "number": "1276",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To remove restrictions from a parcel of land in Paducah, Kentucky.",
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
            "name": "Kentucky",
            "updateDate": "2025-05-20T19:09:27Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-05-20T19:09:27Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-05-20T19:09:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-07T20:36:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119s601",
          "measure-number": "601",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-12-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s601v00",
            "update-date": "2025-12-05"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill directs the Department of the Interior to remove all deed restrictions from approximately 3.62 acres located at 2956 Park Avenue, on the Paducah Memorial Army Reserve Center in\u00a0Paducah, Kentucky. The restrictions include easements, exceptions, reservations, terms, conditions, and covenants described in the quitclaim deed that was executed on April 27, 2012. The deed conveyed land from Interior to the City of\u00a0Paducah, Kentucky.</p>"
        },
        "title": "A bill to remove restrictions from a parcel of land in Paducah, Kentucky."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s601.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill directs the Department of the Interior to remove all deed restrictions from approximately 3.62 acres located at 2956 Park Avenue, on the Paducah Memorial Army Reserve Center in\u00a0Paducah, Kentucky. The restrictions include easements, exceptions, reservations, terms, conditions, and covenants described in the quitclaim deed that was executed on April 27, 2012. The deed conveyed land from Interior to the City of\u00a0Paducah, Kentucky.</p>",
      "updateDate": "2025-12-05",
      "versionCode": "id119s601"
    },
    "title": "A bill to remove restrictions from a parcel of land in Paducah, Kentucky."
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill directs the Department of the Interior to remove all deed restrictions from approximately 3.62 acres located at 2956 Park Avenue, on the Paducah Memorial Army Reserve Center in\u00a0Paducah, Kentucky. The restrictions include easements, exceptions, reservations, terms, conditions, and covenants described in the quitclaim deed that was executed on April 27, 2012. The deed conveyed land from Interior to the City of\u00a0Paducah, Kentucky.</p>",
      "updateDate": "2025-12-05",
      "versionCode": "id119s601"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s601is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to remove restrictions from a parcel of land in Paducah, Kentucky.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:33:33Z"
    },
    {
      "title": "A bill to remove restrictions from a parcel of land in Paducah, Kentucky.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:56:15Z"
    }
  ]
}
```
