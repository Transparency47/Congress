# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/294?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/294
- Title: Dairy Farm Resiliency Act
- Congress: 119
- Bill type: HR
- Bill number: 294
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-10-29T08:05:58Z
- Update date including text: 2025-10-29T08:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- 2025-02-14 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- 2025-02-14 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/294",
    "number": "294",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Dairy Farm Resiliency Act",
    "type": "HR",
    "updateDate": "2025-10-29T08:05:58Z",
    "updateDateIncludingText": "2025-10-29T08:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:31:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:02:23Z",
                "name": "Referred to"
              }
            },
            "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
            "systemCode": "hsag16"
          },
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:02:23Z",
                "name": "Referred to"
              }
            },
            "name": "Livestock, Dairy, and Poultry Subcommittee",
            "systemCode": "hsag29"
          }
        ]
      },
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WI"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CT"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "WI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr294ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 294\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Langworthy (for himself, Mr. Van Orden , and Mr. Courtney ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Act of 2014 with respect to the dairy margin coverage program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dairy Farm Resiliency Act .\n#### 2. Dairy margin coverage program\n##### (a) Production history\nSection 1405(a)(1) of the Agricultural Act of 2014 ( 7 U.S.C. 9055(a)(1) ) is amended by striking during any one of the 2011, 2012, or 2013 calendar years and inserting in the most recent three-year history, as calculated once every five years .\n##### (b) Premiums for dairy margins\n**(1) Tier I**\nSection 1407(b) of the Agricultural Act of 2014 ( 7 U.S.C. 9057(b) ) is amended\u2014\n**(A)**\nin the heading, by striking 5,000,000 and inserting 6,000,000 ; and\n**(B)**\nin paragraph (1), by striking 5,000,000 and inserting 6,000,000 .\n**(2) Tier II**\nSection 1407(c) of the Agricultural Act of 2014 ( 7 U.S.C. 9057(c) ) is amended\u2014\n**(A)**\nin the heading, by striking 5,000,000 and inserting 6,000,000 ; and\n**(B)**\nin paragraph (1), by striking 5,000,000 and inserting 6,000,000 .",
      "versionDate": "2025-01-09",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-19T16:41:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr294",
          "measure-number": "294",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr294v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong> Dairy Farm Resiliency Act </strong></p><p>This bill updates the Dairy Margin Coverage (DMC) program.</p><p>As background, the DMC program was enacted in the 2018 farm bill to support dairy operations by allowing producers to buy a guaranteed margin for their milk production. The margin is the difference between the Department of Agriculture's (USDA's) national all milk price and a calculated feed cost, which provides producers optional risk protection on price and feed costs.</p><p>The bill\u00a0updates the current\u00a0requirements that a participating dairy producer have an established milk production history with USDA's Farm Service Agency. Specifically, the bill requires that a dairy operation's production history for DMC be based on the most recent three-year history and be recalculated every five years.</p><p>The bill also increases Tier I margin coverage for annual milk production to 6 million pounds or less (currently 5 million pounds or less) and Tier II margin coverage to over 6 million pounds (currently over 5 million pounds).</p>"
        },
        "title": "Dairy Farm Resiliency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr294.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong> Dairy Farm Resiliency Act </strong></p><p>This bill updates the Dairy Margin Coverage (DMC) program.</p><p>As background, the DMC program was enacted in the 2018 farm bill to support dairy operations by allowing producers to buy a guaranteed margin for their milk production. The margin is the difference between the Department of Agriculture's (USDA's) national all milk price and a calculated feed cost, which provides producers optional risk protection on price and feed costs.</p><p>The bill\u00a0updates the current\u00a0requirements that a participating dairy producer have an established milk production history with USDA's Farm Service Agency. Specifically, the bill requires that a dairy operation's production history for DMC be based on the most recent three-year history and be recalculated every five years.</p><p>The bill also increases Tier I margin coverage for annual milk production to 6 million pounds or less (currently 5 million pounds or less) and Tier II margin coverage to over 6 million pounds (currently over 5 million pounds).</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr294"
    },
    "title": "Dairy Farm Resiliency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong> Dairy Farm Resiliency Act </strong></p><p>This bill updates the Dairy Margin Coverage (DMC) program.</p><p>As background, the DMC program was enacted in the 2018 farm bill to support dairy operations by allowing producers to buy a guaranteed margin for their milk production. The margin is the difference between the Department of Agriculture's (USDA's) national all milk price and a calculated feed cost, which provides producers optional risk protection on price and feed costs.</p><p>The bill\u00a0updates the current\u00a0requirements that a participating dairy producer have an established milk production history with USDA's Farm Service Agency. Specifically, the bill requires that a dairy operation's production history for DMC be based on the most recent three-year history and be recalculated every five years.</p><p>The bill also increases Tier I margin coverage for annual milk production to 6 million pounds or less (currently 5 million pounds or less) and Tier II margin coverage to over 6 million pounds (currently over 5 million pounds).</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr294"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr294ih.xml"
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
      "title": "Dairy Farm Resiliency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dairy Farm Resiliency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Act of 2014 with respect to the dairy margin coverage program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:29Z"
    }
  ]
}
```
