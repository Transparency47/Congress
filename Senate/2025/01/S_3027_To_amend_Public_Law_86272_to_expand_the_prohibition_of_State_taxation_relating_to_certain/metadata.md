# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3027
- Title: Interstate Commerce Simplification Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3027
- Origin chamber: Senate
- Introduced date: 2025-10-22
- Update date: 2026-04-08T16:35:46Z
- Update date including text: 2026-04-08T16:35:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-22: Introduced in Senate
- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-10-22: Introduced in Senate

## Actions

- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-22",
    "latestAction": {
      "actionDate": "2025-10-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3027",
    "number": "3027",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Interstate Commerce Simplification Act of 2025",
    "type": "S",
    "updateDate": "2026-04-08T16:35:46Z",
    "updateDateIncludingText": "2026-04-08T16:35:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-22",
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
          "date": "2025-10-22T15:08:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3027is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3027\nIN THE SENATE OF THE UNITED STATES\nOctober 22 (legislative day, October 21), 2025 Mr. Johnson introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend Public Law 86\u2013272 to expand the prohibition of State taxation relating to certain solicitation of orders.\n#### 1. Short title\nThis Act may be cited as the Interstate Commerce Simplification Act of 2025 .\n#### 2. Amendment\nSection 101(d) of Public Law 86\u2013272 (73 Stat. 555) is amended\u2014\n**(1)**\nin paragraph (1) by striking and at the end,\n**(2)**\nin paragraph (2) by striking the period at the end and inserting ; and , and\n**(3)**\nby adding at the end the following:\n(3) the term solicitation of orders means any business activity that facilitates the solicitation of orders even if that activity may also serve some independently valuable business function apart from solicitation. .",
      "versionDate": "",
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
        "actionDate": "2025-01-15",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "427",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Interstate Commerce Simplification Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-12-08T21:51:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-22",
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
          "measure-id": "id119s3027",
          "measure-number": "3027",
          "measure-type": "s",
          "orig-publish-date": "2025-10-22",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3027v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-10-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Interstate Commerce Simplification Act of 2025</strong></p><p>This bill expands the definition of <em>solicitation of orders</em> to include business activities that serve an independently valuable business function apart from the solicitation of orders for purposes of the limitation on a state\u2019s authority to impose a net income tax on an out-of-state seller.</p><p>Under current law, a state is prohibited from imposing a net income tax on income derived from within the state from interstate commerce if the only business activity within the state is the solicitation of orders for the sale of tangible personal property, provided that the orders are approved (or rejected) and filled by shipment or delivery from outside of the state. Further, the Supreme Court has held\u00a0that the term\u00a0<em>solicitation of orders</em> includes (1) activities that are strictly essential to making requests for purchases, and (2) ancillary activities that serve no independent business function apart from their connection to requests for purchases.</p><p>Under the bill, the definition of <em>solicitation of orders</em> is expanded to include business activities that facilitate the solicitation of orders even if such business activities serve an independently valuable business function apart from the solicitation.\u00a0</p>"
        },
        "title": "Interstate Commerce Simplification Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3027.xml",
    "summary": {
      "actionDate": "2025-10-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Interstate Commerce Simplification Act of 2025</strong></p><p>This bill expands the definition of <em>solicitation of orders</em> to include business activities that serve an independently valuable business function apart from the solicitation of orders for purposes of the limitation on a state\u2019s authority to impose a net income tax on an out-of-state seller.</p><p>Under current law, a state is prohibited from imposing a net income tax on income derived from within the state from interstate commerce if the only business activity within the state is the solicitation of orders for the sale of tangible personal property, provided that the orders are approved (or rejected) and filled by shipment or delivery from outside of the state. Further, the Supreme Court has held\u00a0that the term\u00a0<em>solicitation of orders</em> includes (1) activities that are strictly essential to making requests for purchases, and (2) ancillary activities that serve no independent business function apart from their connection to requests for purchases.</p><p>Under the bill, the definition of <em>solicitation of orders</em> is expanded to include business activities that facilitate the solicitation of orders even if such business activities serve an independently valuable business function apart from the solicitation.\u00a0</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3027"
    },
    "title": "Interstate Commerce Simplification Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Interstate Commerce Simplification Act of 2025</strong></p><p>This bill expands the definition of <em>solicitation of orders</em> to include business activities that serve an independently valuable business function apart from the solicitation of orders for purposes of the limitation on a state\u2019s authority to impose a net income tax on an out-of-state seller.</p><p>Under current law, a state is prohibited from imposing a net income tax on income derived from within the state from interstate commerce if the only business activity within the state is the solicitation of orders for the sale of tangible personal property, provided that the orders are approved (or rejected) and filled by shipment or delivery from outside of the state. Further, the Supreme Court has held\u00a0that the term\u00a0<em>solicitation of orders</em> includes (1) activities that are strictly essential to making requests for purchases, and (2) ancillary activities that serve no independent business function apart from their connection to requests for purchases.</p><p>Under the bill, the definition of <em>solicitation of orders</em> is expanded to include business activities that facilitate the solicitation of orders even if such business activities serve an independently valuable business function apart from the solicitation.\u00a0</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3027"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3027is.xml"
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
      "title": "Interstate Commerce Simplification Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Interstate Commerce Simplification Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-24T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend Public Law 86-272 to expand the prohibition of State taxation relating to certain solicitation of orders.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-24T02:18:20Z"
    }
  ]
}
```
