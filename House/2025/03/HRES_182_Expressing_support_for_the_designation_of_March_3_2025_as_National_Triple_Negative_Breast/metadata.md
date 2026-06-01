# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/182?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/182
- Title: Expressing support for the designation of March 3, 2025, as "National Triple-Negative Breast Cancer Day".
- Congress: 119
- Bill type: HRES
- Bill number: 182
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-04-07T16:52:16Z
- Update date including text: 2026-04-07T16:52:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-03 - Committee: Submitted in House
- Latest action: 2025-03-03: Submitted in House

## Actions

- 2025-03-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-03 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/182",
    "number": "182",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001206",
        "district": "25",
        "firstName": "Joseph",
        "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
        "lastName": "Morelle",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Expressing support for the designation of March 3, 2025, as \"National Triple-Negative Breast Cancer Day\".",
    "type": "HRES",
    "updateDate": "2026-04-07T16:52:16Z",
    "updateDateIncludingText": "2026-04-07T16:52:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:00:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres182ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 182\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Morelle submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of March 3, 2025, as National Triple-Negative Breast Cancer Day .\nThat the House of Representatives supports the designation of National Triple-Negative Breast Cancer Day to create awareness of the devastating effect of these cancers on families in the United States and the need for strong action to eradicate triple-negative breast cancer.",
      "versionDate": "2025-03-03",
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
        "actionDate": "2026-03-03",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1098",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of March 3, 2026, as \"National Triple-Negative Breast Cancer Day\".",
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
        "name": "Health",
        "updateDate": "2025-03-07T14:36:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119hres182",
          "measure-number": "182",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres182v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of National Triple-Negative Breast Cancer Day. Triple-negative breast cancer is a distinct form of cancer that does not have the hormone and protein receptors commonly found in breast cancer.</p>"
        },
        "title": "Expressing support for the designation of March 3, 2025, as \"National Triple-Negative Breast Cancer Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres182.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National Triple-Negative Breast Cancer Day. Triple-negative breast cancer is a distinct form of cancer that does not have the hormone and protein receptors commonly found in breast cancer.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres182"
    },
    "title": "Expressing support for the designation of March 3, 2025, as \"National Triple-Negative Breast Cancer Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National Triple-Negative Breast Cancer Day. Triple-negative breast cancer is a distinct form of cancer that does not have the hormone and protein receptors commonly found in breast cancer.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres182"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres182ih.xml"
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
      "title": "Expressing support for the designation of March 3, 2025, as \"National Triple-Negative Breast Cancer Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:47Z"
    },
    {
      "title": "Expressing support for the designation of March 3, 2025, as \"National Triple-Negative Breast Cancer Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T09:06:07Z"
    }
  ]
}
```
