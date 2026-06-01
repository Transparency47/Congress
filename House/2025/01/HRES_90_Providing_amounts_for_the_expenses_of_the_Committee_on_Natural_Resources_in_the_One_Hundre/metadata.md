# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/90?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/90
- Title: Providing amounts for the expenses of the Committee on Natural Resources in the One Hundred Nineteenth Congress.
- Congress: 119
- Bill type: HRES
- Bill number: 90
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-04-11T13:34:06Z
- Update date including text: 2025-04-11T13:34:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-01-31 - Committee: Submitted in House
- Latest action: 2025-01-31: Submitted in House

## Actions

- 2025-01-31 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-01-31 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/90",
    "number": "90",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "W000821",
        "district": "4",
        "firstName": "Bruce",
        "fullName": "Rep. Westerman, Bruce [R-AR-4]",
        "lastName": "Westerman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Providing amounts for the expenses of the Committee on Natural Resources in the One Hundred Nineteenth Congress.",
    "type": "HRES",
    "updateDate": "2025-04-11T13:34:06Z",
    "updateDateIncludingText": "2025-04-11T13:34:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres90ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 90\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Westerman (for himself and Mr. Huffman ) submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nProviding amounts for the expenses of the Committee on Natural Resources in the One Hundred Nineteenth Congress.\n#### 1. Amounts for Committee expenses\nFor the expenses of the Committee on Natural Resources (hereafter in this resolution referred to as the Committee ), including the expenses of all staff salaries, there shall be paid, out of the applicable accounts of the House of Representatives for committee salaries and expenses, not more than $19,311,600 for the One Hundred Nineteenth Congress.\n#### 2. Session limitations\nOf the amount specified in section 1\u2014\n**(1)**\nnot more than $9,655,800 shall be available for expenses incurred during the period beginning at noon on January 3, 2025, and ending immediately before noon on January 3, 2026; and\n**(2)**\nnot more than $9,655,800 shall be available for expenses incurred during the period beginning at noon on January 3, 2026, and ending immediately before noon on January 3, 2027.\n#### 3. Vouchers\nPayments under this resolution shall be made on vouchers authorized by the Committee, signed by the Chairman of the Committee, and approved in the manner directed by the Committee on House Administration.\n#### 4. Regulations\nAmounts made available under this resolution shall be expended in accordance with regulations prescribed by the Committee on House Administration.",
      "versionDate": "2025-01-31",
      "versionType": "IH"
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
            "name": "Congressional committees",
            "updateDate": "2025-03-26T19:19:59Z"
          },
          {
            "name": "House Committee on Natural Resources",
            "updateDate": "2025-03-26T19:20:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-05T14:52:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hres90",
          "measure-number": "90",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-04-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres90v00",
            "update-date": "2025-04-11"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution provides amounts for the expenses of the House Committee on Natural Resources for the 119th\u00a0Congress.</p>"
        },
        "title": "Providing amounts for the expenses of the Committee on Natural Resources in the One Hundred Nineteenth Congress."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres90.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides amounts for the expenses of the House Committee on Natural Resources for the 119th\u00a0Congress.</p>",
      "updateDate": "2025-04-11",
      "versionCode": "id119hres90"
    },
    "title": "Providing amounts for the expenses of the Committee on Natural Resources in the One Hundred Nineteenth Congress."
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution provides amounts for the expenses of the House Committee on Natural Resources for the 119th\u00a0Congress.</p>",
      "updateDate": "2025-04-11",
      "versionCode": "id119hres90"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres90ih.xml"
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
      "title": "Providing amounts for the expenses of the Committee on Natural Resources in the One Hundred Nineteenth Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T09:18:35Z"
    },
    {
      "title": "Providing amounts for the expenses of the Committee on Natural Resources in the One Hundred Nineteenth Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T09:05:55Z"
    }
  ]
}
```
