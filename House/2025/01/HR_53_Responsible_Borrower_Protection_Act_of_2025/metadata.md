# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/53?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/53
- Title: Responsible Borrower Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 53
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-06-04T15:07:04Z
- Update date including text: 2025-06-04T15:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Financial Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/53",
    "number": "53",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Responsible Borrower Protection Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-04T15:07:04Z",
    "updateDateIncludingText": "2025-06-04T15:07:04Z"
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
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
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
          "date": "2025-01-03T16:10:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MO"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "VA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr53ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 53\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Ogles , Mr. Burlison , Mr. Weber of Texas , Mr. Cline , Mr. Bost , and Mr. Cloud ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo cancel certain proposed changes to credit fees charged by the Federal National Mortgage Association and the Federal Home Loan Mortgage Corporation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Responsible Borrower Protection Act of 2025 .\n#### 2. Cancellation of changes\nThe Federal Housing Finance Agency and the enterprises (as such term is defined in section 1303 of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4502 )) may not implement the changes to the single-family housing mortgage credit fee pricing framework of the enterprises announced by the Federal Housing Finance Agency on January 19, 2023 ( FHFA Announces Updates to the Enterprises\u2019 Single-Family Pricing Framework ), and set forth in Federal National Mortgage Association Lender Letter LL\u20132023\u201301 and Federal Home Loan Mortgage Corporation Bulletin 2023\u20131, and such changes, Lender Letter, and Bulletin shall have no force or effect.\n#### 3. Continuation of risk-based pricing\nThis Act may not be construed to prohibit the enterprises from applying risk-based pricing for credit fees for single-family housing mortgages.",
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
            "name": "Credit and credit markets",
            "updateDate": "2025-06-04T15:07:04Z"
          },
          {
            "name": "Government National Mortgage Association (Ginnie Mae)",
            "updateDate": "2025-06-04T15:01:10Z"
          },
          {
            "name": "Housing finance and home ownership",
            "updateDate": "2025-06-04T15:06:15Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-06-04T15:06:29Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-06-04T15:06:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-02-04T12:57:23Z"
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
          "measure-id": "id119hr53",
          "measure-number": "53",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr53v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Responsible Borrower Protection Act of 2025</strong></p><p>This bill prohibits the Federal Housing Finance Agency, the Federal National Mortgage Association (Fannie Mae), and the Federal Home Loan Mortgage Corporation (Freddie Mac) from implementing changes to the single-family home loan pricing framework for upfront fees on certain home loans, announced in January 2023. The changes revise the fee charts that provide percentage adjustments based on a borrower's credit score and other risk factors.\u00a0Overall, these changes increase the percentage adjustments, with variations based on the particular risk profile of the loan.</p>"
        },
        "title": "Responsible Borrower Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr53.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Responsible Borrower Protection Act of 2025</strong></p><p>This bill prohibits the Federal Housing Finance Agency, the Federal National Mortgage Association (Fannie Mae), and the Federal Home Loan Mortgage Corporation (Freddie Mac) from implementing changes to the single-family home loan pricing framework for upfront fees on certain home loans, announced in January 2023. The changes revise the fee charts that provide percentage adjustments based on a borrower's credit score and other risk factors.\u00a0Overall, these changes increase the percentage adjustments, with variations based on the particular risk profile of the loan.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr53"
    },
    "title": "Responsible Borrower Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Responsible Borrower Protection Act of 2025</strong></p><p>This bill prohibits the Federal Housing Finance Agency, the Federal National Mortgage Association (Fannie Mae), and the Federal Home Loan Mortgage Corporation (Freddie Mac) from implementing changes to the single-family home loan pricing framework for upfront fees on certain home loans, announced in January 2023. The changes revise the fee charts that provide percentage adjustments based on a borrower's credit score and other risk factors.\u00a0Overall, these changes increase the percentage adjustments, with variations based on the particular risk profile of the loan.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr53"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr53ih.xml"
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
      "title": "Responsible Borrower Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T12:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Responsible Borrower Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-29T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To cancel certain proposed changes to credit fees charged by the Federal National Mortgage Association and the Federal Home Loan Mortgage Corporation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T12:18:21Z"
    }
  ]
}
```
