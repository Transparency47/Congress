# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/941?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/941
- Title: Small LENDER Act
- Congress: 119
- Bill type: HR
- Bill number: 941
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-05-13T17:49:23Z
- Update date including text: 2026-05-13T17:49:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported by the Yeas and Nays: 26 - 22.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported by the Yeas and Nays: 26 - 22.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/941",
    "number": "941",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001072",
        "district": "2",
        "firstName": "J.",
        "fullName": "Rep. Hill, J. French [R-AR-2]",
        "lastName": "Hill",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Small LENDER Act",
    "type": "HR",
    "updateDate": "2026-05-13T17:49:23Z",
    "updateDateIncludingText": "2026-05-13T17:49:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 26 - 22.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
        "item": [
          {
            "date": "2026-04-21T15:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-04T17:07:05Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MO"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "SC"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "PA"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "AR"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "MS"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "FL"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "IN"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TN"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr941ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 941\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Hill of Arkansas (for himself, Mr. Meuser , Mrs. Wagner , Mr. Huizenga , Mr. Timmons , Mr. Moore of North Carolina , and Mr. Williams of Texas ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Equal Credit Opportunity Act to provide for an effective date and a temporary safe harbor for compliance with certain small business lending data collection rules, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Lenders Exempt from New Data and Excessive Reporting Act or the Small LENDER Act .\n#### 2. Small business loan data collection\nSection 704B of the Equal Credit Opportunity Act ( 15 U.S.C. 1691c\u20132 ) is amended\u2014\n**(1)**\nin subsection (g), by adding at the end the following:\n(4) Compliance with covered rule (A) In general With respect to the covered rule, the Bureau shall provide a financial institution a 3-year period beginning on the date the covered rule was issued to comply with the rule. (B) Safe harbor After the end of the 3-year period described under subparagraph (A), the Bureau shall provide a 2-year safe harbor to a financial institution during which the financial institution is required to comply with the covered rule but is not subject to any penalties for failure to comply with the covered rule. (C) Covered rule defined In this paragraph, the term covered rule means the final rule of the Bureau titled Small Business Lending Under the Equal Credit Opportunity Act (Regulation B) (88 Fed. Reg. 35150, published May 31, 2023). ; and\n**(2)**\nin subsection (h)\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) Financial institution The term financial institution means\u2014 (A) any partnership, company, corporation, association (incorporated or unincorporated), trust, estate, cooperative organization, or other entity that engages in any financial activity; and (B) in each of the previous 2 calendar years originated not less than 500 credit transactions for small businesses. ; and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) Small business The term small business means any entity with gross annual revenues of $1,000,000 or less in the most recently completed fiscal year. .",
      "versionDate": "2025-02-04",
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-04-27T18:44:14Z"
          },
          {
            "name": "Business records",
            "updateDate": "2026-04-27T18:45:46Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-27T18:43:57Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2026-04-27T18:45:58Z"
          },
          {
            "name": "Small business",
            "updateDate": "2026-04-27T18:44:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-03-07T15:06:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr941",
          "measure-number": "941",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2026-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr941v00",
            "update-date": "2026-05-13"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Small Lenders Exempt from New Data and Excessive Reporting Act or the Small LENDER Act</strong></p><p>This bill modifies the requirements for financial institutions to\u00a0report certain information about small business credit applications to the Consumer Financial Protection Bureau (CFPB) and extends the timeline for compliance with the CFPB rule with respect to such reporting (i.e., Section 1071 final <a href=\"https://www.federalregister.gov/documents/2023/05/31/2023-07230/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b\">rule</a>). (For background about the CFPB rule and subsequent litigation see CRS Report <a href=\"https://www.congress.gov/crs-product/R47788\">R47788</a>.)</p><p>Under the bill, the reporting requirements apply only to financial institutions that originate at least 500 credit transactions to small businesses in each of the preceding two years. The bill further defines small businesses as those with gross annual revenue of $1 million or less.</p><p>The rule currently establishes a phase-in period that ultimately requires institutions that originate over 100 credit transactions to small businesses to comply with the reporting requirements. The rule also defines small businesses as those with gross annual revenue of $5 million or less.</p><p>Further, beginning on the date the final\u00a0CFPB rule was issued (May 31, 2023), the bill provides three years for applicable financial institutions to comply with the rule followed by a two-year safe harbor period during which such institutions are not subject to any penalties for failure to comply with the rule.</p>"
        },
        "title": "Small LENDER Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr941.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Small Lenders Exempt from New Data and Excessive Reporting Act or the Small LENDER Act</strong></p><p>This bill modifies the requirements for financial institutions to\u00a0report certain information about small business credit applications to the Consumer Financial Protection Bureau (CFPB) and extends the timeline for compliance with the CFPB rule with respect to such reporting (i.e., Section 1071 final <a href=\"https://www.federalregister.gov/documents/2023/05/31/2023-07230/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b\">rule</a>). (For background about the CFPB rule and subsequent litigation see CRS Report <a href=\"https://www.congress.gov/crs-product/R47788\">R47788</a>.)</p><p>Under the bill, the reporting requirements apply only to financial institutions that originate at least 500 credit transactions to small businesses in each of the preceding two years. The bill further defines small businesses as those with gross annual revenue of $1 million or less.</p><p>The rule currently establishes a phase-in period that ultimately requires institutions that originate over 100 credit transactions to small businesses to comply with the reporting requirements. The rule also defines small businesses as those with gross annual revenue of $5 million or less.</p><p>Further, beginning on the date the final\u00a0CFPB rule was issued (May 31, 2023), the bill provides three years for applicable financial institutions to comply with the rule followed by a two-year safe harbor period during which such institutions are not subject to any penalties for failure to comply with the rule.</p>",
      "updateDate": "2026-05-13",
      "versionCode": "id119hr941"
    },
    "title": "Small LENDER Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Small Lenders Exempt from New Data and Excessive Reporting Act or the Small LENDER Act</strong></p><p>This bill modifies the requirements for financial institutions to\u00a0report certain information about small business credit applications to the Consumer Financial Protection Bureau (CFPB) and extends the timeline for compliance with the CFPB rule with respect to such reporting (i.e., Section 1071 final <a href=\"https://www.federalregister.gov/documents/2023/05/31/2023-07230/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b\">rule</a>). (For background about the CFPB rule and subsequent litigation see CRS Report <a href=\"https://www.congress.gov/crs-product/R47788\">R47788</a>.)</p><p>Under the bill, the reporting requirements apply only to financial institutions that originate at least 500 credit transactions to small businesses in each of the preceding two years. The bill further defines small businesses as those with gross annual revenue of $1 million or less.</p><p>The rule currently establishes a phase-in period that ultimately requires institutions that originate over 100 credit transactions to small businesses to comply with the reporting requirements. The rule also defines small businesses as those with gross annual revenue of $5 million or less.</p><p>Further, beginning on the date the final\u00a0CFPB rule was issued (May 31, 2023), the bill provides three years for applicable financial institutions to comply with the rule followed by a two-year safe harbor period during which such institutions are not subject to any penalties for failure to comply with the rule.</p>",
      "updateDate": "2026-05-13",
      "versionCode": "id119hr941"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr941ih.xml"
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
      "title": "Small LENDER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:50Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small LENDER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Lenders Exempt from New Data and Excessive Reporting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Equal Credit Opportunity Act to provide for an effective date and a temporary safe harbor for compliance with certain small business lending data collection rules, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:59Z"
    }
  ]
}
```
