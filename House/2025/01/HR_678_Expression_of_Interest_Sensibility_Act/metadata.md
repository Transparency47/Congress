# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/678?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/678
- Title: Expression of Interest Sensibility Act
- Congress: 119
- Bill type: HR
- Bill number: 678
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-01-27T19:55:36Z
- Update date including text: 2026-01-27T19:55:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/678",
    "number": "678",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Expression of Interest Sensibility Act",
    "type": "HR",
    "updateDate": "2026-01-27T19:55:36Z",
    "updateDateIncludingText": "2026-01-27T19:55:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:05:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr678ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 678\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Mineral Leasing Act to improve the assessment of expression of interest fees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expression of Interest Sensibility Act .\n#### 2. Fee for expression of interest\n##### (a) Deadline To issue lease\nSection 17(b)(1)(A) of the Mineral Leasing Act ( 30 U.S.C. 226(b)(1)(A) ) is amended by striking the remainder of the bonus bid, if any, and inserting , as applicable, the remainder of the bonus bid, the fee for the expression of interest under subsection (q)(2)(B), .\n##### (b) Expressions of interest\nSection 17(q) of the Mineral Leasing Act ( 30 U.S.C. 226(q) ) is amended\u2014\n**(1)**\nin the heading, by striking Fee for ;\n**(2)**\nby redesignating paragraph (2) as paragraph (3);\n**(3)**\nby amending paragraph (1) to read as follows:\n(1) Submission of expression of interest A person may, in accordance with procedures established by the Secretary to carry out this subsection, submit an expression of interest in leasing land available for disposition under this section for exploration for, and development of, oil or gas. (2) Assessment of fees (A) No bid If land covered by an expression of interest submitted under paragraph (1) is offered at a lease sale and no bid is received for such land, the Secretary shall assess at the time of the sale a fee for the expression of interest against the person that submitted the first expression of interest for the land. (B) Successful bid If land covered by an expression of interest submitted under paragraph (1) receives a successful bid at a lease sale, the Secretary shall assess a fee for the expression of interest against the successful bidder. ;\n**(4)**\nin paragraph (3), as so redesignated, by striking paragraph (1) and inserting paragraph (2) ; and\n**(5)**\nby adding at the end the following:\n(4) Term An expression of interest submitted under this section shall remain active for a term of not less than 5 years unless the land covered by the expression of interest is offered at a lease sale. .",
      "versionDate": "2025-01-23",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-02-25T14:13:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr678",
          "measure-number": "678",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2026-01-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr678v00",
            "update-date": "2026-01-27"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Expression of Interest Sensibility Act</strong></p><p>This bill limits when the Bureau of Land Management (BLM) may charge a fee for an expression of interest, which is an informal nomination to request that certain federal land be included in a lease sale for the exploration for, and development of, oil or gas.</p><p>The bill requires the BLM to charge a fee to a successful bidder when the agency offers the nominated land for sale. If the land covered by an expression of interest does not receive bids during the lease sale, the BLM must charge\u00a0a fee to the person that submitted the first expression of interest for the land. Thus, the BLM may not charge\u00a0fees when the land is not made available for a lease sale. (Currently, the\u00a0BLM charges\u00a0a fee when a person submits an expression of interest in leasing land, and the fee must be paid even if the land is not offered for sale.)</p><p>The bill also requires an expression of interest to remain active for a term of at least five years unless the land covered by the expression of interest is offered at a lease sale.</p>"
        },
        "title": "Expression of Interest Sensibility Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr678.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expression of Interest Sensibility Act</strong></p><p>This bill limits when the Bureau of Land Management (BLM) may charge a fee for an expression of interest, which is an informal nomination to request that certain federal land be included in a lease sale for the exploration for, and development of, oil or gas.</p><p>The bill requires the BLM to charge a fee to a successful bidder when the agency offers the nominated land for sale. If the land covered by an expression of interest does not receive bids during the lease sale, the BLM must charge\u00a0a fee to the person that submitted the first expression of interest for the land. Thus, the BLM may not charge\u00a0fees when the land is not made available for a lease sale. (Currently, the\u00a0BLM charges\u00a0a fee when a person submits an expression of interest in leasing land, and the fee must be paid even if the land is not offered for sale.)</p><p>The bill also requires an expression of interest to remain active for a term of at least five years unless the land covered by the expression of interest is offered at a lease sale.</p>",
      "updateDate": "2026-01-27",
      "versionCode": "id119hr678"
    },
    "title": "Expression of Interest Sensibility Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expression of Interest Sensibility Act</strong></p><p>This bill limits when the Bureau of Land Management (BLM) may charge a fee for an expression of interest, which is an informal nomination to request that certain federal land be included in a lease sale for the exploration for, and development of, oil or gas.</p><p>The bill requires the BLM to charge a fee to a successful bidder when the agency offers the nominated land for sale. If the land covered by an expression of interest does not receive bids during the lease sale, the BLM must charge\u00a0a fee to the person that submitted the first expression of interest for the land. Thus, the BLM may not charge\u00a0fees when the land is not made available for a lease sale. (Currently, the\u00a0BLM charges\u00a0a fee when a person submits an expression of interest in leasing land, and the fee must be paid even if the land is not offered for sale.)</p><p>The bill also requires an expression of interest to remain active for a term of at least five years unless the land covered by the expression of interest is offered at a lease sale.</p>",
      "updateDate": "2026-01-27",
      "versionCode": "id119hr678"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr678ih.xml"
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
      "title": "Expression of Interest Sensibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T08:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expression of Interest Sensibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T08:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Mineral Leasing Act to improve the assessment of expression of interest fees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T08:03:45Z"
    }
  ]
}
```
