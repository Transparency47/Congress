# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/526?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/526
- Title: Recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as "National Pollinator Week".
- Congress: 119
- Bill type: HRES
- Bill number: 526
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2026-04-06T19:13:30Z
- Update date including text: 2026-04-06T19:13:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-06-20 - IntroReferral: Submitted in House
- 2025-06-20 - IntroReferral: Submitted in House
- Latest action: 2025-06-20: Submitted in House

## Actions

- 2025-06-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-06-20 - IntroReferral: Submitted in House
- 2025-06-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/526",
    "number": "526",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\".",
    "type": "HRES",
    "updateDate": "2026-04-06T19:13:30Z",
    "updateDateIncludingText": "2026-04-06T19:13:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres526ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 526\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Mr. Panetta (for himself and Mr. Yakym ) submitted the following resolution; which was referred to the Committee on Agriculture\nRESOLUTION\nRecognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as National Pollinator Week .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Pollinator Week ;\n**(2)**\nacknowledges the significance that all types of pollinators play in sustaining agriculture, promoting biodiversity, and maintaining the overall health of natural ecosystems;\n**(3)**\nencourages the people of the United States to observe National Pollinator Week with appropriate ceremonies and conservation and educational activities; and\n**(4)**\nintends to\u2014\n**(A)**\ncontinue working to conserve native pollinator species and their various habitats; and\n**(B)**\nwork to improve the overall understanding of the importance of native pollinators.",
      "versionDate": "2025-06-20",
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
        "actionDate": "2025-06-18",
        "text": "Referred to the Committee on Environment and Public Works. (text: CR S3474-3475)"
      },
      "number": "289",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\".",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-07-03T13:57:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-20",
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
          "measure-id": "id119hres526",
          "measure-number": "526",
          "measure-type": "hres",
          "orig-publish-date": "2025-06-20",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres526v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-06-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Pollinator Week.</p>"
        },
        "title": "Recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres526.xml",
    "summary": {
      "actionDate": "2025-06-20",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Pollinator Week.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres526"
    },
    "title": "Recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-06-20",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Pollinator Week.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres526"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres526ih.xml"
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
      "title": "Recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T08:18:18Z"
    },
    {
      "title": "Recognizing the importance of pollinators to ecosystem health and agriculture in the United States by designating June 15 through June 22, 2025, as \"National Pollinator Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T08:05:18Z"
    }
  ]
}
```
