# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/457
- Title: Utah Wildfire Research Institute Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 457
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-04-15T13:59:35Z
- Update date including text: 2026-04-15T13:59:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/457",
    "number": "457",
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
    "title": "Utah Wildfire Research Institute Act of 2025",
    "type": "S",
    "updateDate": "2026-04-15T13:59:35Z",
    "updateDateIncludingText": "2026-04-15T13:59:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T18:11:43Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s457is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 457\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Lee (for himself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Southwest Forest Health and Wildfire Prevention Act of 2004 to require the establishment of an additional Institute under that Act.\n#### 1. Short title\nThis Act may be cited as the Utah Wildfire Research Institute Act of 2025 .\n#### 2. Additional Institute\n##### (a) In general\nSection 5(b)(2) of the Southwest Forest Health and Wildfire Prevention Act of 2004 ( 16 U.S.C. 6704(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end;\n**(2)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(D) the State of Utah. .\n##### (b) Conforming amendment\nSection 5(e)(1) of the Southwest Forest Health and Wildfire Prevention Act of 2004 ( 16 U.S.C. 6704(e)(1) ) is amended by striking and Colorado and inserting Colorado, and Utah .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-12-16",
        "text": "Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "1045",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Utah Wildfire Research Institute Act of 2025",
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
            "name": "Ecology",
            "updateDate": "2025-06-13T18:53:01Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-06-13T18:53:01Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-06-13T18:53:01Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-06-13T18:53:01Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-06-13T18:53:01Z"
          },
          {
            "name": "Utah",
            "updateDate": "2025-06-13T18:53:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-06T13:44:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s457",
          "measure-number": "457",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s457v00",
            "update-date": "2026-04-15"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Utah Wildfire Research Institute Act of 2025</strong></p><p>This bill requires the establishment of a Southwest Ecological Restoration Institute in Utah. Such institutes currently exist in Arizona, New Mexico, and Colorado and promote the use of adaptive ecosystem management to reduce the risk of wildfires and restore the health of forest and woodland ecosystems.</p>"
        },
        "title": "Utah Wildfire Research Institute Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s457.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Utah Wildfire Research Institute Act of 2025</strong></p><p>This bill requires the establishment of a Southwest Ecological Restoration Institute in Utah. Such institutes currently exist in Arizona, New Mexico, and Colorado and promote the use of adaptive ecosystem management to reduce the risk of wildfires and restore the health of forest and woodland ecosystems.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119s457"
    },
    "title": "Utah Wildfire Research Institute Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Utah Wildfire Research Institute Act of 2025</strong></p><p>This bill requires the establishment of a Southwest Ecological Restoration Institute in Utah. Such institutes currently exist in Arizona, New Mexico, and Colorado and promote the use of adaptive ecosystem management to reduce the risk of wildfires and restore the health of forest and woodland ecosystems.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119s457"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s457is.xml"
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
      "title": "A bill to amend the Southwest Forest Health and Wildfire Prevention Act of 2004 to require the establishment of an additional Institute under that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:34Z"
    },
    {
      "title": "Utah Wildfire Research Institute Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Utah Wildfire Research Institute Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    }
  ]
}
```
