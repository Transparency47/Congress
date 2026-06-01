# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6192?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6192
- Title: Fertilizer Research Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6192
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-16T08:07:44Z
- Update date including text: 2026-05-16T08:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2026-01-13 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6192",
    "number": "6192",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Fertilizer Research Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:44Z",
    "updateDateIncludingText": "2026-05-16T08:07:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:02:10Z",
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
                "date": "2026-01-13T19:58:48Z",
                "name": "Referred to"
              }
            },
            "name": "Forestry and Horticulture Subcommittee",
            "systemCode": "hsag15"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-13T19:58:48Z",
                "name": "Referred to"
              }
            },
            "name": "Conservation, Research, and Biotechnology Subcommittee",
            "systemCode": "hsag14"
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "IA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "IA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6192ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6192\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mrs. Hinson (for herself, Ms. Budzinski , Mr. Feenstra , Ms. Perez , and Mrs. Miller-Meeks ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Secretary of Agriculture to publish a report on the fertilizer industry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fertilizer Research Act of 2025 .\n#### 2. Fertilizer industry report\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture, in consultation with the Administrator of the Economic Research Service, shall publish on the website of the Department of Agriculture a report on the United States fertilizer industry, including\u2014\n**(1)**\na description of the impacts on the fertilizer industry that influence the prices that agricultural producers receive for their agricultural products at the location of the farm;\n**(2)**\na description of the current size and value, and the size and value over the previous 25 years, of the United States fertilizer market, including\u2014\n**(A)**\nany trends over the previous 25 years; and\n**(B)**\nsuch sizes and values by each type of fertilizer;\n**(3)**\na description of any patterns in pricing of fertilizer over the previous 25 years;\n**(4)**\na description of the importation of fertilizer into the United States, including\u2014\n**(A)**\na list of types of fertilizer that are imported into the United States, including the quantity of each type of fertilizer imported;\n**(B)**\na list of foreign companies and domestic companies that import into the United States fertilizer, including the quantity of fertilizer imported by each company;\n**(C)**\na list of the countries from which fertilizer is imported into the United States; and\n**(D)**\na description of the impacts that antidumping duties and countervailing duties have on prices of fertilizer paid at the retail level;\n**(5)**\nan overview of the manufacturing level, distribution channels, and retail level of the fertilizer supply chain, including transportation, logistics, and supply chain disruptions from natural disasters;\n**(6)**\na study of the concentration of the United States fertilizer industry in United States fertilizer companies, including an evaluation of the extent to which concentration has had any anticompetitive impacts;\n**(7)**\na description of the prices, crop-use efficiencies, and crop yields of emerging fertilizers and fertilizer technologies, including biological fertilizers and other recently developed tools, compared to conventional fertilizers and fertilizer technologies;\n**(8)**\nan assessment of the regulatory environment governing fertilizer production, distribution, and usage, including a description of areas in which regulatory burden is hampering domestic production, distribution, and usage of fertilizer;\n**(9)**\na description of the extent to which current public price reporting of fertilizer is transparent for market participants and the extent to which further public price reporting is needed to achieve transparency for market participants, including\u2014\n**(A)**\nan evaluation of the potential for the Secretary of Agriculture to establish a fertilizer reporting mechanism in which the fertilizer industry is required to report fertilizer prices at multiple levels of the supply chain on a daily, weekly, or monthly basis; and\n**(B)**\na recommendation to Congress on whether a reporting mechanism described in subparagraph (A) should be established; and\n**(10)**\na description of the projected growth of the United States fertilizer market and the anticipated economic and political risks to fertilizer production as a result of that growth.\n##### (b) Confidential information\nThe report published under subsection (a) shall not include any confidential business information.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-09-16",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "2808",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fertilizer Research Act of 2025",
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
        "updateDate": "2025-12-09T21:16:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119hr6192",
          "measure-number": "6192",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-20",
          "originChamber": "HOUSE",
          "update-date": "2025-12-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6192v00",
            "update-date": "2025-12-10"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fertilizer Research Act of 2025</strong></p><p>This bill directs the Department of Agriculture to publish on the department's website a report on the U.S. fertilizer industry. Among other things, the report must include</p><ul><li>a description of the impacts on the fertilizer industry that influence the prices that agricultural producers receive for their products;</li><li>a description of the size and value of the U.S. fertilizer market over the previous 25 years;</li><li>a description of the importation of fertilizer into the United States and the impacts that antidumping and countervailing duties have on retail fertilizer prices;</li><li>a study of market concentration of the U.S. fertilizer industry;</li><li>an assessment of the regulatory environment governing fertilizer production, distribution, and usage; and</li><li>a description of the extent to which current public price reporting of fertilizer is transparent for market participants and recommendations on whether further reporting is needed.\u00a0\u00a0\u00a0</li></ul>"
        },
        "title": "Fertilizer Research Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6192.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fertilizer Research Act of 2025</strong></p><p>This bill directs the Department of Agriculture to publish on the department's website a report on the U.S. fertilizer industry. Among other things, the report must include</p><ul><li>a description of the impacts on the fertilizer industry that influence the prices that agricultural producers receive for their products;</li><li>a description of the size and value of the U.S. fertilizer market over the previous 25 years;</li><li>a description of the importation of fertilizer into the United States and the impacts that antidumping and countervailing duties have on retail fertilizer prices;</li><li>a study of market concentration of the U.S. fertilizer industry;</li><li>an assessment of the regulatory environment governing fertilizer production, distribution, and usage; and</li><li>a description of the extent to which current public price reporting of fertilizer is transparent for market participants and recommendations on whether further reporting is needed.\u00a0\u00a0\u00a0</li></ul>",
      "updateDate": "2025-12-10",
      "versionCode": "id119hr6192"
    },
    "title": "Fertilizer Research Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fertilizer Research Act of 2025</strong></p><p>This bill directs the Department of Agriculture to publish on the department's website a report on the U.S. fertilizer industry. Among other things, the report must include</p><ul><li>a description of the impacts on the fertilizer industry that influence the prices that agricultural producers receive for their products;</li><li>a description of the size and value of the U.S. fertilizer market over the previous 25 years;</li><li>a description of the importation of fertilizer into the United States and the impacts that antidumping and countervailing duties have on retail fertilizer prices;</li><li>a study of market concentration of the U.S. fertilizer industry;</li><li>an assessment of the regulatory environment governing fertilizer production, distribution, and usage; and</li><li>a description of the extent to which current public price reporting of fertilizer is transparent for market participants and recommendations on whether further reporting is needed.\u00a0\u00a0\u00a0</li></ul>",
      "updateDate": "2025-12-10",
      "versionCode": "id119hr6192"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6192ih.xml"
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
      "title": "Fertilizer Research Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T08:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fertilizer Research Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T08:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to publish a report on the fertilizer industry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T08:33:34Z"
    }
  ]
}
```
