# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/754?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/754
- Title: Investing in Main Street Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 754
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-12-05T21:35:00Z
- Update date including text: 2025-12-05T21:35:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Small Business.
- 2025-02-24 16:48:28 - Floor: Mr. Williams (TX) moved to suspend the rules and pass the bill.
- 2025-02-24 16:48:50 - Floor: Considered under suspension of the rules. (consideration: CR H743-745)
- 2025-02-24 16:48:51 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 754.
- 2025-02-24 16:59:51 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H743)
- 2025-02-24 16:59:51 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H743)
- 2025-02-24 16:59:53 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-02-25 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Small Business.
- 2025-02-24 16:48:28 - Floor: Mr. Williams (TX) moved to suspend the rules and pass the bill.
- 2025-02-24 16:48:50 - Floor: Considered under suspension of the rules. (consideration: CR H743-745)
- 2025-02-24 16:48:51 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 754.
- 2025-02-24 16:59:51 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H743)
- 2025-02-24 16:59:51 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H743)
- 2025-02-24 16:59:53 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-02-25 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/754",
    "number": "754",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001080",
        "district": "28",
        "firstName": "Judy",
        "fullName": "Rep. Chu, Judy [D-CA-28]",
        "lastName": "Chu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Investing in Main Street Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:35:00Z",
    "updateDateIncludingText": "2025-12-05T21:35:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-02-24",
      "actionTime": "16:59:53",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-02-24",
      "actionTime": "16:59:51",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H743)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-02-24",
      "actionTime": "16:59:51",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H743)",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-02-24",
      "actionTime": "16:48:51",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 754.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-02-24",
      "actionTime": "16:48:50",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H743-745)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-02-24",
      "actionTime": "16:48:28",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Williams (TX) moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-02-25T17:47:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-28T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MN"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NJ"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr754ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 754\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Chu (for herself, Mr. Finstad , Mrs. McIver , and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Investment Act of 1958 to increase the amount that may be invested in small business investment companies.\n#### 1. Short title\nThis Act may be cited as the Investing in Main Street Act of 2025 .\n#### 2. Investment in small business investment companies\nSection 302(b) of the Small Business Investment Act of 1958 ( 15 U.S.C. 682(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking 5 percent and inserting 15 percent ; and\n**(2)**\nin paragraph (2), by striking 5 percent and inserting 15 percent .",
      "versionDate": "2025-01-28",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr754rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 754\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Received; read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nAN ACT\nTo amend the Small Business Investment Act of 1958 to increase the amount that may be invested in small business investment companies.\n#### 1. Short title\nThis Act may be cited as the Investing in Main Street Act of 2025 .\n#### 2. Investment in small business investment companies\nSection 302(b) of the Small Business Investment Act of 1958 ( 15 U.S.C. 682(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking 5 percent and inserting 15 percent ; and\n**(2)**\nin paragraph (2), by striking 5 percent and inserting 15 percent .",
      "versionDate": "2025-02-25",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr754eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 754\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo amend the Small Business Investment Act of 1958 to increase the amount that may be invested in small business investment companies.\n#### 1. Short title\nThis Act may be cited as the Investing in Main Street Act of 2025 .\n#### 2. Investment in small business investment companies\nSection 302(b) of the Small Business Investment Act of 1958 ( 15 U.S.C. 682(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking 5 percent and inserting 15 percent ; and\n**(2)**\nin paragraph (2), by striking 5 percent and inserting 15 percent .",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
        "actionDate": "2025-07-09",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2223",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Investing in Main Street Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-02-25T16:24:17Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-02-25T16:24:17Z"
          },
          {
            "name": "Business investment and capital",
            "updateDate": "2025-02-25T16:24:17Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-02-25T16:24:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-24T11:55:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr754",
          "measure-number": "754",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr754v00",
            "update-date": "2025-02-24"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Investing in Main Street Act of 2025</strong></p><p>This bill authorizes certain banking entities to invest up to 15% of their capital and surplus in one or more small business investment companies (SBICs) or in any entity established to invest solely in SBICs. The current limit is 5%.</p>"
        },
        "title": "Investing in Main Street Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr754.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Investing in Main Street Act of 2025</strong></p><p>This bill authorizes certain banking entities to invest up to 15% of their capital and surplus in one or more small business investment companies (SBICs) or in any entity established to invest solely in SBICs. The current limit is 5%.</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr754"
    },
    "title": "Investing in Main Street Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Investing in Main Street Act of 2025</strong></p><p>This bill authorizes certain banking entities to invest up to 15% of their capital and surplus in one or more small business investment companies (SBICs) or in any entity established to invest solely in SBICs. The current limit is 5%.</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr754"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr754ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr754rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr754eh.xml"
        }
      ],
      "type": "Engrossed in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Investing in Main Street Act of 2025",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-03-01T04:23:21Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Investing in Main Street Act of 2025",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "title": "Investing in Main Street Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:52Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Investing in Main Street Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Investment Act of 1958 to increase the amount that may be invested in small business investment companies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:55Z"
    }
  ]
}
```
