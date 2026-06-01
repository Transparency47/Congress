# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/132
- Title: Western Water Accelerated Revenue Repayment Act
- Congress: 119
- Bill type: HR
- Bill number: 132
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-14T21:16:39Z
- Update date including text: 2025-02-14T21:16:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/132",
    "number": "132",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "B000825",
        "district": "3",
        "firstName": "Lauren",
        "fullName": "Rep. Boebert, Lauren [R-CO-4]",
        "lastName": "Boebert",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Western Water Accelerated Revenue Repayment Act",
    "type": "HR",
    "updateDate": "2025-02-14T21:16:39Z",
    "updateDateIncludingText": "2025-02-14T21:16:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-03T16:24:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr132ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 132\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Ms. Boebert introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Water Infrastructure Improvements for the Nation Act to extend certain contract prepayment authority.\n#### 1. Short title\nThis Act may be cited as the Western Water Accelerated Revenue Repayment Act .\n#### 2. Amendments to the WIIN Act\n##### (a) Offsets and water storage account\nSection 4011(d)(2) of the Water Infrastructure Improvements for the Nation Act ( Public Law 114\u2013322 ) is amended by inserting that are directed by project-specific statutes in effect prior to the date of passage of this Act to accounts other than the General Reclamation Fund before the semicolon.\n##### (b) Extension of prepayment authority\nSection 4013 of the Water Infrastructure Improvements for the Nation Act ( Public Law 114\u2013322 ) is amended\u2014\n**(1)**\nin paragraph (1), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (2), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) section 4011. .",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
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
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-02-05T16:03:48Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-02-05T16:03:57Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2025-02-05T16:04:04Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-02-05T16:04:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-01-31T16:21:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr132",
          "measure-number": "132",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr132v00",
            "update-date": "2025-02-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Western Water Accelerated Revenue Repayment Act</strong></p><p>This bill permanently authorizes a provision under the Water Infrastructure Improvements for the Nation (WIIN) Act that (1) allows certain water users (e.g., agriculture and municipal water users) in western states to prepay what they owe under contracts with the Bureau of Reclamation for delivering water through a lump sum payment or over a period of three years; and (2) requires a specified portion of the receipts generated from such prepayments be directed to the Reclamation Water Storage Account for the construction of water storage. Such prepayments do not alter certain requirements for the disposition of amounts that are directed by project-specific\u00a0statutes in effect prior to the passage of the\u00a0WIIN Act to accounts other than the General Reclamation Fund.</p>"
        },
        "title": "Western Water Accelerated Revenue Repayment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr132.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Western Water Accelerated Revenue Repayment Act</strong></p><p>This bill permanently authorizes a provision under the Water Infrastructure Improvements for the Nation (WIIN) Act that (1) allows certain water users (e.g., agriculture and municipal water users) in western states to prepay what they owe under contracts with the Bureau of Reclamation for delivering water through a lump sum payment or over a period of three years; and (2) requires a specified portion of the receipts generated from such prepayments be directed to the Reclamation Water Storage Account for the construction of water storage. Such prepayments do not alter certain requirements for the disposition of amounts that are directed by project-specific\u00a0statutes in effect prior to the passage of the\u00a0WIIN Act to accounts other than the General Reclamation Fund.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr132"
    },
    "title": "Western Water Accelerated Revenue Repayment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Western Water Accelerated Revenue Repayment Act</strong></p><p>This bill permanently authorizes a provision under the Water Infrastructure Improvements for the Nation (WIIN) Act that (1) allows certain water users (e.g., agriculture and municipal water users) in western states to prepay what they owe under contracts with the Bureau of Reclamation for delivering water through a lump sum payment or over a period of three years; and (2) requires a specified portion of the receipts generated from such prepayments be directed to the Reclamation Water Storage Account for the construction of water storage. Such prepayments do not alter certain requirements for the disposition of amounts that are directed by project-specific\u00a0statutes in effect prior to the passage of the\u00a0WIIN Act to accounts other than the General Reclamation Fund.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr132"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr132ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Western Water Accelerated Revenue Repayment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Western Water Accelerated Revenue Repayment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T10:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Water Infrastructure Improvements for the Nation Act to extend certain contract prepayment authority.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T10:48:25Z"
    }
  ]
}
```
