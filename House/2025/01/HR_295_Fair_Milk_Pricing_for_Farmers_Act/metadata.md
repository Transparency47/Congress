# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/295?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/295
- Title: Fair Milk Pricing for Farmers Act
- Congress: 119
- Bill type: HR
- Bill number: 295
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-02-18T14:45:29Z
- Update date including text: 2026-02-18T14:45:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/295",
    "number": "295",
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
    "title": "Fair Milk Pricing for Farmers Act",
    "type": "HR",
    "updateDate": "2026-02-18T14:45:29Z",
    "updateDateIncludingText": "2026-02-18T14:45:29Z"
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
          "date": "2025-01-09T14:35:00Z",
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
                "date": "2025-02-14T18:02:38Z",
                "name": "Referred to"
              }
            },
            "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
            "systemCode": "hsag16"
          },
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:02:38Z",
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
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "IN"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
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
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NY"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
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
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr295ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 295\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Langworthy (for himself, Mr. Van Orden , Mr. Morelle , Mr. Finstad , Ms. Tenney , Mr. Moolenaar , Mr. Costa , Mr. Newhouse , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Marketing Act of 1946 with respect to mandatory reporting of dairy products processing costs.\n#### 1. Short title\nThis Act may be cited as the Fair Milk Pricing for Farmers Act .\n#### 2. Mandatory reporting of dairy products processing costs\nSection 273 of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1637b ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)(ii), by striking and at the end;\n**(ii)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(C) for each manufacturer required to report under subparagraph (A) for any product, require that manufacturer to report production cost and product yield information, as determined by the Secretary, for all products processed in the same facility or facilities. ; and\n**(B)**\nin paragraph (2)(A), by inserting products and after those ; and\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin the subsection heading, by striking Electronic reporting and inserting Reporting ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin the heading, by striking Electronic reporting and inserting Reporting ; and\n**(ii)**\nby striking this section and inserting in its place subparagraphs (A) and (B) of subsection (b)(1) ;\n**(C)**\nin paragraph (2), by striking this section and inserting in its place subparagraphs (A) and (B) of subsection (b)(1) ; and\n**(D)**\nby adding at the end the following:\n(3) Dairy products processing costs Not later than 3 years after the date of enactment of this paragraph, and every 2 years thereafter, the Secretary shall publish a report containing the information obtained under subparagraph (C) of subsection (b)(1). .",
      "versionDate": "2025-01-09",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-13",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "581",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fair Milk Pricing for Farmers Act",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-19T15:15:54Z"
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
          "measure-id": "id119hr295",
          "measure-number": "295",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr295v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fair Milk Pricing for Farmers Act</strong></p><p>This bill requires manufacturers to report production cost and product yield information for all dairy products processed in the same facility or facilities to the Department of Agriculture (USDA) Dairy Product Mandatory Reporting Program. Further, USDA must publish a report containing the information obtained under these new requirements and publish a report every two years thereafter.</p><p>As background, under the Dairy Product Mandatory Reporting Program, USDA must collect certain dairy product sales information from manufacturers and release the data\u00a0on a weekly basis.</p>"
        },
        "title": "Fair Milk Pricing for Farmers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr295.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Milk Pricing for Farmers Act</strong></p><p>This bill requires manufacturers to report production cost and product yield information for all dairy products processed in the same facility or facilities to the Department of Agriculture (USDA) Dairy Product Mandatory Reporting Program. Further, USDA must publish a report containing the information obtained under these new requirements and publish a report every two years thereafter.</p><p>As background, under the Dairy Product Mandatory Reporting Program, USDA must collect certain dairy product sales information from manufacturers and release the data\u00a0on a weekly basis.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr295"
    },
    "title": "Fair Milk Pricing for Farmers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Milk Pricing for Farmers Act</strong></p><p>This bill requires manufacturers to report production cost and product yield information for all dairy products processed in the same facility or facilities to the Department of Agriculture (USDA) Dairy Product Mandatory Reporting Program. Further, USDA must publish a report containing the information obtained under these new requirements and publish a report every two years thereafter.</p><p>As background, under the Dairy Product Mandatory Reporting Program, USDA must collect certain dairy product sales information from manufacturers and release the data\u00a0on a weekly basis.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr295"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr295ih.xml"
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
      "title": "Fair Milk Pricing for Farmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Milk Pricing for Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Marketing Act of 1946 with respect to mandatory reporting of dairy products processing costs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T04:33:38Z"
    }
  ]
}
```
