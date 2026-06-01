# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/427?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/427
- Title: Interstate Commerce Simplification Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 427
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-09T20:06:30Z
- Update date including text: 2025-12-09T20:06:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/427",
    "number": "427",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Interstate Commerce Simplification Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-09T20:06:30Z",
    "updateDateIncludingText": "2025-12-09T20:06:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WI"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WI"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr427ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 427\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Fitzgerald (for himself, Mr. Grothman , Mr. Tiffany , and Mr. Steil ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend Public Law 86\u2013272 to expand the prohibition of State taxation relating to certain solicitation of orders.\n#### 1. Short title\nThis Act may be cited as the Interstate Commerce Simplification Act of 2025 .\n#### 2. Amendment\nSection 101(d) of Public Law 86\u2013272 (73 Stat. 555) is amended\u2014\n**(1)**\nin paragraph (1) by striking and at the end,\n**(2)**\nin paragraph (2) by striking the period at the end and inserting ; and , and\n**(3)**\nby adding at the end the following:\n(3) the term solicitation of orders means any business activity that facilitates the solicitation of orders even if that activity may also serve some independently valuable business function apart from solicitation. .",
      "versionDate": "2025-01-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-10-22",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3027",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Interstate Commerce Simplification Act of 2025",
      "type": "S"
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
        "updateDate": "2025-02-21T12:41:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr427",
          "measure-number": "427",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr427v00",
            "update-date": "2025-04-15"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Interstate Commerce Simplification Act of 2025</strong></p><p>This bill expands the definition of <em>solicitation of orders</em> to include business activities that serve an independently valuable business function apart from the solicitation of orders for purposes of the limitation on a state\u2019s authority to impose a net income tax on an out-of-state seller.</p><p>Under current law, a state is prohibited from imposing a net income tax on income derived from within the state from interstate commerce if the only business activity within the state is the solicitation of orders for the sale of tangible personal property, provided that the orders are approved (or rejected) and filled by shipment or delivery from outside of the state. Further, the Supreme Court has held\u00a0that the term\u00a0<em>solicitation of orders</em> includes (1) activities that are strictly essential to making requests for purchases, and (2) ancillary activities that serve no independent business function apart from their connection to requests for purchases.</p><p>Under the bill, the definition of <em>solicitation of orders</em> is expanded to include business activities that facilitate the solicitation of orders even if such business activities serve an independently valuable business function apart from the solicitation.\u00a0</p>"
        },
        "title": "Interstate Commerce Simplification Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr427.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Interstate Commerce Simplification Act of 2025</strong></p><p>This bill expands the definition of <em>solicitation of orders</em> to include business activities that serve an independently valuable business function apart from the solicitation of orders for purposes of the limitation on a state\u2019s authority to impose a net income tax on an out-of-state seller.</p><p>Under current law, a state is prohibited from imposing a net income tax on income derived from within the state from interstate commerce if the only business activity within the state is the solicitation of orders for the sale of tangible personal property, provided that the orders are approved (or rejected) and filled by shipment or delivery from outside of the state. Further, the Supreme Court has held\u00a0that the term\u00a0<em>solicitation of orders</em> includes (1) activities that are strictly essential to making requests for purchases, and (2) ancillary activities that serve no independent business function apart from their connection to requests for purchases.</p><p>Under the bill, the definition of <em>solicitation of orders</em> is expanded to include business activities that facilitate the solicitation of orders even if such business activities serve an independently valuable business function apart from the solicitation.\u00a0</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119hr427"
    },
    "title": "Interstate Commerce Simplification Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Interstate Commerce Simplification Act of 2025</strong></p><p>This bill expands the definition of <em>solicitation of orders</em> to include business activities that serve an independently valuable business function apart from the solicitation of orders for purposes of the limitation on a state\u2019s authority to impose a net income tax on an out-of-state seller.</p><p>Under current law, a state is prohibited from imposing a net income tax on income derived from within the state from interstate commerce if the only business activity within the state is the solicitation of orders for the sale of tangible personal property, provided that the orders are approved (or rejected) and filled by shipment or delivery from outside of the state. Further, the Supreme Court has held\u00a0that the term\u00a0<em>solicitation of orders</em> includes (1) activities that are strictly essential to making requests for purchases, and (2) ancillary activities that serve no independent business function apart from their connection to requests for purchases.</p><p>Under the bill, the definition of <em>solicitation of orders</em> is expanded to include business activities that facilitate the solicitation of orders even if such business activities serve an independently valuable business function apart from the solicitation.\u00a0</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119hr427"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr427ih.xml"
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
      "title": "Interstate Commerce Simplification Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Interstate Commerce Simplification Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend Public Law 86-272 to expand the prohibition of State taxation relating to certain solicitation of orders.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:27Z"
    }
  ]
}
```
