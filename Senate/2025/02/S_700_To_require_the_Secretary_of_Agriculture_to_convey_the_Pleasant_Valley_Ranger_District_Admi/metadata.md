# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/700?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/700
- Title: A bill to require the Secretary of Agriculture to convey the Pleasant Valley Ranger District Administrative Site to Gila County, Arizona.
- Congress: 119
- Bill type: S
- Bill number: 700
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/700",
    "number": "700",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "A bill to require the Secretary of Agriculture to convey the Pleasant Valley Ranger District Administrative Site to Gila County, Arizona.",
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
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
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
            "date": "2026-02-04T22:05:35Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-25T15:24:00Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s700is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 700\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Kelly (for himself and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Agriculture to convey the Pleasant Valley Ranger District Administrative Site to Gila County, Arizona.\n#### 1. Conveyance of Pleasant Valley Ranger District Administrative Site to Gila County, Arizona\n##### (a) Definitions\nIn this section:\n**(1) County**\nThe term County means Gila County, Arizona.\n**(2) Map**\nThe term map means the map entitled Pleasant Valley Admin Site Proposal and dated September 23, 2021.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance required\nSubject to this section, if the County submits to the Secretary a written request for conveyance of the property described in subsection (c) not later than 180 days after the date of enactment of this Act, the Secretary shall convey to the County all right, title, and interest of the United States in and to the property described in subsection (c).\n##### (c) Description of property\n**(1) In general**\nThe property referred to in subsection (b) is the parcel of real property, including all land and improvements, generally depicted as Gila County Area on the map, consisting of approximately 232.9 acres of National Forest System land located in the Tonto National Forest in Arizona.\n**(2) Map**\n**(A) Minor errors**\nThe Secretary may correct minor errors in the map.\n**(B) Availability**\nA copy of the map shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n**(3) Survey**\nThe exact acreage and legal description of the National Forest System land to be conveyed under subsection (b) shall be determined by a survey satisfactory to the Secretary.\n##### (d) Terms and conditions\nThe conveyance under subsection (b) shall be\u2014\n**(1)**\nsubject to valid existing rights;\n**(2)**\nmade without consideration;\n**(3)**\nmade by quitclaim deed; and\n**(4)**\nsubject to such other terms and conditions as the Secretary considers to be appropriate to protect the interests of the United States.\n##### (e) Costs of conveyance\nAs a condition of the conveyance under subsection (b), the County shall pay all costs associated with the conveyance, including the cost of\u2014\n**(1)**\na survey, if necessary, under subsection (c)(3);\n**(2)**\nany environmental analysis or resource survey required under Federal law; and\n**(3)**\nany analysis required to comply with division A of subtitle III of title 54, United States Code (commonly referred to as the National Historic Preservation Act ).\n##### (f) Environmental conditions\nNotwithstanding section 120(h)(3)(A) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9620(h)(3)(A) ), the Secretary shall not be required to provide any covenant or warranty for the land and improvements conveyed to the County under subsection (b).\n##### (g) Use of land; reversion\n**(1) In general**\nThe land conveyed to the County under subsection (b) shall be used by the County only for the purposes of serving and supporting veterans of the Armed Forces.\n**(2) Reversion**\nIf any land conveyed under subsection (b) is used in a manner that is inconsistent with the requirements of paragraph (1), all right, title, and interest in and to the land shall revert to the United States, at the discretion of the Secretary.",
      "versionDate": "2025-02-25",
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
        "actionDate": "2026-02-04",
        "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably."
      },
      "number": "837",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To require the Secretary of Agriculture to convey the Pleasant Valley Ranger District Administrative Site to Gila County, Arizona.",
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
            "name": "Arizona",
            "updateDate": "2026-02-06T16:16:48Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-02-06T16:16:48Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-02-06T16:16:48Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-02-06T16:16:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T13:11:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119s700",
          "measure-number": "700",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s700v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill directs the Forest Service to convey specified property to Gila County, Arizona, upon the county's submission of a written request for such conveyance. The property, identified as the Gila County Area, consists of approximately 232.9 acres of National Forest System land located in the Tonto National Forest in Arizona.</p><p>The county must use the land for the purposes of serving and supporting veterans.\u00a0If any land conveyed under this bill ceases to be used for such purpose, all right, title, and interest in and to the land shall revert to the United States, at the discretion of the Forest Service.</p><p>The conveyance\u00a0must be made with a\u00a0quitclaim deed and without consideration (value, such as payment, provided in exchange for the property).</p><p>The Forest Service\u00a0must not be required to provide any covenant or warranty for the land and improvements conveyed to the county under such conveyance.</p><p>As a condition of the conveyance, the county must pay all the costs associated with the conveyance, including any (1) surveys, (2)\u00a0environmental analysis or resource survey required under federal law, and (3) analysis required to comply with certain provisions of the National Historic Preservation Act.</p>"
        },
        "title": "A bill to require the Secretary of Agriculture to convey the Pleasant Valley Ranger District Administrative Site to Gila County, Arizona."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s700.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill directs the Forest Service to convey specified property to Gila County, Arizona, upon the county's submission of a written request for such conveyance. The property, identified as the Gila County Area, consists of approximately 232.9 acres of National Forest System land located in the Tonto National Forest in Arizona.</p><p>The county must use the land for the purposes of serving and supporting veterans.\u00a0If any land conveyed under this bill ceases to be used for such purpose, all right, title, and interest in and to the land shall revert to the United States, at the discretion of the Forest Service.</p><p>The conveyance\u00a0must be made with a\u00a0quitclaim deed and without consideration (value, such as payment, provided in exchange for the property).</p><p>The Forest Service\u00a0must not be required to provide any covenant or warranty for the land and improvements conveyed to the county under such conveyance.</p><p>As a condition of the conveyance, the county must pay all the costs associated with the conveyance, including any (1) surveys, (2)\u00a0environmental analysis or resource survey required under federal law, and (3) analysis required to comply with certain provisions of the National Historic Preservation Act.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s700"
    },
    "title": "A bill to require the Secretary of Agriculture to convey the Pleasant Valley Ranger District Administrative Site to Gila County, Arizona."
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill directs the Forest Service to convey specified property to Gila County, Arizona, upon the county's submission of a written request for such conveyance. The property, identified as the Gila County Area, consists of approximately 232.9 acres of National Forest System land located in the Tonto National Forest in Arizona.</p><p>The county must use the land for the purposes of serving and supporting veterans.\u00a0If any land conveyed under this bill ceases to be used for such purpose, all right, title, and interest in and to the land shall revert to the United States, at the discretion of the Forest Service.</p><p>The conveyance\u00a0must be made with a\u00a0quitclaim deed and without consideration (value, such as payment, provided in exchange for the property).</p><p>The Forest Service\u00a0must not be required to provide any covenant or warranty for the land and improvements conveyed to the county under such conveyance.</p><p>As a condition of the conveyance, the county must pay all the costs associated with the conveyance, including any (1) surveys, (2)\u00a0environmental analysis or resource survey required under federal law, and (3) analysis required to comply with certain provisions of the National Historic Preservation Act.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s700"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s700is.xml"
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
      "title": "A bill to require the Secretary of Agriculture to convey the Pleasant Valley Ranger District Administrative Site to Gila County, Arizona.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:56Z"
    },
    {
      "title": "A bill to require the Secretary of Agriculture to convey the Pleasant Valley Ranger District Administrative Site to Gila County, Arizona.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T11:56:13Z"
    }
  ]
}
```
