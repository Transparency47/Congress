# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/289
- Title: A resolution recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as "National Pollinator Week".
- Congress: 119
- Bill type: SRES
- Bill number: 289
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-04-06T16:33:39Z
- Update date including text: 2026-04-06T16:33:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Referred to the Committee on Environment and Public Works. (text: CR S3474-3475)
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Referred to the Committee on Environment and Public Works. (text: CR S3474-3475)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/289",
    "number": "289",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A resolution recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\".",
    "type": "SRES",
    "updateDate": "2026-04-06T16:33:39Z",
    "updateDateIncludingText": "2026-04-06T16:33:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Environment and Public Works. (text: CR S3474-3475)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
          "date": "2025-06-18T18:38:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres289is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 289\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Merkley submitted the following resolution; which was referred to the Committee on Environment and Public Works\nRESOLUTION\nRecognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as National Pollinator Week .\nThat the Senate\u2014\n**(1)**\nexpresses support for the designation of June 15 through June 22, 2025, as National Pollinator Week ;\n**(2)**\nacknowledges the significance that all types of pollinators play in sustaining agriculture, promoting biodiversity, and maintaining the overall health of natural ecosystems;\n**(3)**\nencourages the people of the United States to observe National Pollinator Week with appropriate ceremonies and conservation and educational activities; and\n**(4)**\nintends to\u2014\n**(A)**\ncontinue working to conserve native pollinator species and their various habitats; and\n**(B)**\nwork to improve the overall understanding of the importance of native pollinators.",
      "versionDate": "2025-06-18",
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
        "actionDate": "2025-06-20",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "526",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\".",
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
        "name": "Environmental Protection",
        "updateDate": "2025-07-03T13:57:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-18",
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
          "measure-id": "id119sres289",
          "measure-number": "289",
          "measure-type": "sres",
          "orig-publish-date": "2025-06-18",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres289v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-06-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution supports the designation of June 15-June 22, 2025, as National Pollinator Week.</p>"
        },
        "title": "A resolution recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres289.xml",
    "summary": {
      "actionDate": "2025-06-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports the designation of June 15-June 22, 2025, as National Pollinator Week.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119sres289"
    },
    "title": "A resolution recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-06-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports the designation of June 15-June 22, 2025, as National Pollinator Week.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119sres289"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres289is.xml"
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
      "title": "A resolution recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T04:18:20Z"
    },
    {
      "title": "A resolution recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T10:56:16Z"
    }
  ]
}
```
