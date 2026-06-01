# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2808?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2808
- Title: Fertilizer Research Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2808
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2808",
    "number": "2808",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Fertilizer Research Act of 2025",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-16",
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
        "item": [
          {
            "date": "2025-09-16T15:15:38Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-16T15:15:38Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WI"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "IA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MS"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "KS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2808is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2808\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Mr. Grassley (for himself, Ms. Baldwin , Ms. Ernst , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo require the Secretary of Agriculture to publish a report on the fertilizer industry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fertilizer Research Act of 2025 .\n#### 2. Fertilizer industry report\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture, in consultation with the Administrator of the Economic Research Service, shall publish on the website of the Department of Agriculture a report on the United States fertilizer industry, including\u2014\n**(1)**\na description of the impacts on the fertilizer industry that influence the prices that agricultural producers receive for their agricultural products at the location of the farm;\n**(2)**\na description of the current size and value, and the size and value over the previous 25 years, of the United States fertilizer market, including\u2014\n**(A)**\nany trends over the previous 25 years; and\n**(B)**\nsuch sizes and values by each type of fertilizer;\n**(3)**\na description of any patterns in pricing of fertilizer over the previous 25 years;\n**(4)**\na description of the importation of fertilizer into the United States, including\u2014\n**(A)**\na list of types of fertilizer that are imported into the United States, including the quantity of each type of fertilizer imported;\n**(B)**\na list of foreign companies and domestic companies that import into the United States fertilizer, including the quantity of fertilizer imported by each company;\n**(C)**\na list of the countries from which fertilizer is imported into the United States; and\n**(D)**\na description of the impacts that antidumping duties and countervailing duties have on prices of fertilizer paid at the retail level;\n**(5)**\nan overview of the manufacturing level, distribution channels, and retail level of the fertilizer supply chain, including transportation, logistics, and supply chain disruptions from natural disasters;\n**(6)**\na study of the concentration of the United States fertilizer industry in United States fertilizer companies, including an evaluation of the extent to which concentration has had any anticompetitive impacts;\n**(7)**\na description of the prices, crop-use efficiencies, and crop yields of emerging fertilizers and fertilizer technologies, including biological fertilizers and other recently developed tools, compared to conventional fertilizers and fertilizer technologies;\n**(8)**\nan assessment of the regulatory environment governing fertilizer production, distribution, and usage, including a description of areas in which regulatory burden is hampering domestic production, distribution, and usage of fertilizer;\n**(9)**\na description of the extent to which current public price reporting of fertilizer is transparent for market participants and the extent to which further public price reporting is needed to achieve transparency for market participants, including\u2014\n**(A)**\nan evaluation of the potential for the Secretary of Agriculture to establish a fertilizer reporting mechanism in which the fertilizer industry is required to report fertilizer prices at multiple levels of the supply chain on a daily, weekly, or monthly basis; and\n**(B)**\na recommendation to Congress on whether a reporting mechanism described in subparagraph (A) should be established; and\n**(10)**\na description of the projected growth of the United States fertilizer market and the anticipated economic and political risks to fertilizer production as a result of that growth.\n##### (b) Confidential information\nThe report published under subsection (a) shall not include any confidential business information.",
      "versionDate": "2025-09-16",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "6192",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fertilizer Research Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-29T18:24:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-16",
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
          "measure-id": "id119s2808",
          "measure-number": "2808",
          "measure-type": "s",
          "orig-publish-date": "2025-09-16",
          "originChamber": "SENATE",
          "update-date": "2025-09-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2808v00",
            "update-date": "2025-09-30"
          },
          "action-date": "2025-09-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fertilizer Research Act of 2025</strong></p><p>This bill directs the Department of Agriculture to publish on the department's website a report on the U.S. fertilizer industry. Among other things, the report must include</p><ul><li>a description of the impacts on the fertilizer industry that influence the prices that agricultural producers receive for their products;</li><li>a description of the size and value of the U.S. fertilizer market over the previous 25 years;</li><li>a description of the importation of fertilizer into the United States and the impacts that antidumping and countervailing duties have on retail fertilizer prices;</li><li>a study of market concentration of the U.S. fertilizer industry;</li><li>an assessment of the regulatory environment governing fertilizer production, distribution, and usage; and</li><li>a description of the extent to which current public price reporting of fertilizer is transparent for market participants and recommendations on whether further reporting is needed.\u00a0\u00a0\u00a0</li></ul>"
        },
        "title": "Fertilizer Research Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2808.xml",
    "summary": {
      "actionDate": "2025-09-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fertilizer Research Act of 2025</strong></p><p>This bill directs the Department of Agriculture to publish on the department's website a report on the U.S. fertilizer industry. Among other things, the report must include</p><ul><li>a description of the impacts on the fertilizer industry that influence the prices that agricultural producers receive for their products;</li><li>a description of the size and value of the U.S. fertilizer market over the previous 25 years;</li><li>a description of the importation of fertilizer into the United States and the impacts that antidumping and countervailing duties have on retail fertilizer prices;</li><li>a study of market concentration of the U.S. fertilizer industry;</li><li>an assessment of the regulatory environment governing fertilizer production, distribution, and usage; and</li><li>a description of the extent to which current public price reporting of fertilizer is transparent for market participants and recommendations on whether further reporting is needed.\u00a0\u00a0\u00a0</li></ul>",
      "updateDate": "2025-09-30",
      "versionCode": "id119s2808"
    },
    "title": "Fertilizer Research Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fertilizer Research Act of 2025</strong></p><p>This bill directs the Department of Agriculture to publish on the department's website a report on the U.S. fertilizer industry. Among other things, the report must include</p><ul><li>a description of the impacts on the fertilizer industry that influence the prices that agricultural producers receive for their products;</li><li>a description of the size and value of the U.S. fertilizer market over the previous 25 years;</li><li>a description of the importation of fertilizer into the United States and the impacts that antidumping and countervailing duties have on retail fertilizer prices;</li><li>a study of market concentration of the U.S. fertilizer industry;</li><li>an assessment of the regulatory environment governing fertilizer production, distribution, and usage; and</li><li>a description of the extent to which current public price reporting of fertilizer is transparent for market participants and recommendations on whether further reporting is needed.\u00a0\u00a0\u00a0</li></ul>",
      "updateDate": "2025-09-30",
      "versionCode": "id119s2808"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2808is.xml"
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
      "title": "Fertilizer Research Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fertilizer Research Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture to publish a report on the fertilizer industry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:48:19Z"
    }
  ]
}
```
