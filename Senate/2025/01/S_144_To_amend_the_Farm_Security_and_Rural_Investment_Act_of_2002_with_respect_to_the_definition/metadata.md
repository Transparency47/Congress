# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/144?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/144
- Title: Farm to Fly Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 144
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-12-05T21:57:46Z
- Update date including text: 2025-12-05T21:57:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/144",
    "number": "144",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Farm to Fly Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:57:46Z",
    "updateDateIncludingText": "2025-12-05T21:57:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
        "item": {
          "date": "2025-01-16T22:11:13Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MN"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NE"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s144is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 144\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Moran (for himself, Ms. Klobuchar , Ms. Ernst , Ms. Duckworth , Mr. Ricketts , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Farm Security and Rural Investment Act of 2002 with respect to the definition of biofuels and sustainable aviation fuel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farm to Fly Act of 2025 .\n#### 2. Purposes and findings\n##### (a) Purposes\nThe purposes of this Act are as follows:\n**(1)**\nTo enable access for sustainable aviation fuels within Department of Agriculture bioenergy programs to foster alternative biofuels in national aviation, expanding the fuel supply, promoting clean energy sources, and supporting United States agriculture.\n**(2)**\nTo recognize the critical role the United States agricultural sector plays in the production of sustainable aviation fuel and the importance of such fuel to achieving the goals of the Sustainable Aviation Fuel Grand Challenge.\n##### (b) Findings\nCongress finds the following:\n**(1)**\nSustainable aviation fuels have the capacity to increase domestic energy security, support the agricultural sector, and foster the farm economy by accelerating the availability of a commercially viable and sustainable aviation biofuel industry in the United States.\n**(2)**\nSustainable aviation fuels provide a critical opportunity to support farmers of the United States and the rest of the agricultural sector in the sector\u2019s partnership with the aviation sector to support rural economic development.\n**(3)**\nFeedstocks have been identified for sustainable aviation fuels due to the collective abundance and perceived sustainability attributes of such feedstocks.\n**(4)**\nSustainable aviation fuels will increase domestic energy security and create new markets for farmers of the United States while providing a new energy resource for the aviation sector.\n#### 3. Definitions\nSection 9001 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8101 ) is amended\u2014\n**(1)**\nin paragraph (3)(B)\u2014\n**(A)**\nin clause (iv), by inserting and sustainable aviation fuel after diesel-equivalent fuel ;\n**(B)**\nby redesignating clauses (v) through (vii) as clauses (vi) through (viii), respectively; and\n**(C)**\nby inserting after clause (iv) the following:\n(v) biofuel, including sustainable aviation fuel, produced from an intermediate ingredient or feedstock; ; and\n**(2)**\nby adding at the end the following:\n(18) Sustainable aviation fuel (A) In general The term sustainable aviation fuel means liquid fuel, the portion of which is not kerosene, which\u2014 (i) meets the requirements of\u2014 (I) ASTM International Standard D7566; or (II) the Fischer Tropsch provisions of ASTM International Standard D1655, Annex A1; (ii) is not derived from coprocessing an applicable material (or materials derived from an applicable material) with a feedstock which is not biomass; (iii) is not derived from palm fatty acid distillates or petroleum; and (iv) has been certified in accordance with subparagraph (B)(iii) as having a lifecycle greenhouse gas emissions reduction percentage of at least 50 percent. (B) Other definitions For purposes of subparagraph (A): (i) Applicable material The term applicable material means\u2014 (I) monoglycerides, diglycerides, and triglycerides; (II) free fatty acids; and (III) fatty acid esters. (ii) Biomass The term biomass has the meaning given such term in section 45K(c)(3) of the Internal Revenue Code of 1986. (iii) Lifecycle greenhouse gas emissions reduction percentage The term lifecycle greenhouse gas emissions reduction percentage means, with respect to any sustainable aviation fuel, the percentage reduction in lifecycle greenhouse gas emissions achieved by such fuel as compared with petroleum-based jet fuel, as defined in accordance with\u2014 (I) the most recent Carbon Offsetting and Reduction Scheme for International Aviation which has been adopted by the International Civil Aviation Organization with the agreement of the United States; or (II) the most recent determinations under the Greenhouse gases, Regulated Emissions, and Energy use in Technologies (GREET) model developed by Argonne National Laboratory. .\n#### 4. Farm to Fly collaboration initiative\nThe Secretary of Agriculture shall take such actions as are necessary to carry out a comprehensive and integrated pursuit of all Department of Agriculture mission areas for the advancement of sustainable aviation fuels through\u2014\n**(1)**\nensuring leadership working across Department of Agriculture agencies to maximize effectiveness;\n**(2)**\nidentification of opportunities to maximize sustainable aviation fuels development and commercialization;\n**(3)**\nleveraging the capabilities of America\u2019s farmers, foresters, and the agricultural sector in capturing the opportunities presented by the emerging sustainable aviation fuels market;\n**(4)**\nsupporting rural economic development through improved sustainability for aviation; and\n**(5)**\nadvancing public-private partnerships through collaboration complementing Federal Government efforts.\n#### 5. Biorefinery, renewable chemical, and biobased product manufacturing assistance\nSection 9003 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8103 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by striking and at the end;\n**(B)**\nin paragraph (4), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(5) foster and advance sustainable aviation fuels. ; and\n**(2)**\nin subsection (b)(3)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby indenting the margins of clauses (i) through (iii) appropriately;\n**(ii)**\nby redesignating clauses (ii) and (iii) as clauses (iii) and (iv), respectively; and\n**(iii)**\nby inserting after clause (i) the following:\n(ii) sustainable aviation fuel; ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby indenting the margins of clauses (i) through (iii) appropriately;\n**(ii)**\nby redesignating clauses (ii) and (iii) as clauses (iii) and (iv), respectively; and\n**(iii)**\nby inserting after clause (i) the following:\n(ii) sustainable aviation fuel; .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-03-28",
        "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit."
      },
      "number": "1719",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Farm to Fly Act of 2025",
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
        "updateDate": "2025-02-20T16:30:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s144",
          "measure-number": "144",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s144v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Farm to Fly Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to integrate the advancement of sustainable aviation fuels into its programs.</p><p>Specifically, this bill includes sustainable aviation fuel as an advanced\u00a0biofuel for the purposes of several USDA\u00a0bioenergy programs that primarily provide support and incentives for renewable energy projects.</p><p>For purposes of these programs, the bill defines <em>sustainable aviation fuel</em> as liquid fuel, the portion of which is not kerosene, which (1) meets specific international standards, (2) is not derived from coprocessing specific materials (e.g., triglycerides) with a non-biomass feedstock, (3) is not derived from palm fatty acid distillates or petroleum, and (4) is certified as having a lifecycle greenhouse gas emissions reduction percentage of at least 50% compared with petroleum-based jet fuel (based on specific standards and agreements).</p><p>In addition, the bill specifically\u00a0includes fostering and advancing sustainable aviation fuels as part of the Biorefinery, Renewable Chemical, and Biobased Product Manufacturing Assistance Program.</p><p>Further, USDA must carry out a comprehensive and integrated pursuit of all USDA mission areas for the advancement of sustainable aviation fuels, including through</p><ul><li>the identification of opportunities to maximize the development and commercialization of the fuels,</li><li>supporting rural economic development through improved sustainability for aviation, and</li><li>advancing public-private partnerships.</li></ul>"
        },
        "title": "Farm to Fly Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s144.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farm to Fly Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to integrate the advancement of sustainable aviation fuels into its programs.</p><p>Specifically, this bill includes sustainable aviation fuel as an advanced\u00a0biofuel for the purposes of several USDA\u00a0bioenergy programs that primarily provide support and incentives for renewable energy projects.</p><p>For purposes of these programs, the bill defines <em>sustainable aviation fuel</em> as liquid fuel, the portion of which is not kerosene, which (1) meets specific international standards, (2) is not derived from coprocessing specific materials (e.g., triglycerides) with a non-biomass feedstock, (3) is not derived from palm fatty acid distillates or petroleum, and (4) is certified as having a lifecycle greenhouse gas emissions reduction percentage of at least 50% compared with petroleum-based jet fuel (based on specific standards and agreements).</p><p>In addition, the bill specifically\u00a0includes fostering and advancing sustainable aviation fuels as part of the Biorefinery, Renewable Chemical, and Biobased Product Manufacturing Assistance Program.</p><p>Further, USDA must carry out a comprehensive and integrated pursuit of all USDA mission areas for the advancement of sustainable aviation fuels, including through</p><ul><li>the identification of opportunities to maximize the development and commercialization of the fuels,</li><li>supporting rural economic development through improved sustainability for aviation, and</li><li>advancing public-private partnerships.</li></ul>",
      "updateDate": "2025-03-14",
      "versionCode": "id119s144"
    },
    "title": "Farm to Fly Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farm to Fly Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to integrate the advancement of sustainable aviation fuels into its programs.</p><p>Specifically, this bill includes sustainable aviation fuel as an advanced\u00a0biofuel for the purposes of several USDA\u00a0bioenergy programs that primarily provide support and incentives for renewable energy projects.</p><p>For purposes of these programs, the bill defines <em>sustainable aviation fuel</em> as liquid fuel, the portion of which is not kerosene, which (1) meets specific international standards, (2) is not derived from coprocessing specific materials (e.g., triglycerides) with a non-biomass feedstock, (3) is not derived from palm fatty acid distillates or petroleum, and (4) is certified as having a lifecycle greenhouse gas emissions reduction percentage of at least 50% compared with petroleum-based jet fuel (based on specific standards and agreements).</p><p>In addition, the bill specifically\u00a0includes fostering and advancing sustainable aviation fuels as part of the Biorefinery, Renewable Chemical, and Biobased Product Manufacturing Assistance Program.</p><p>Further, USDA must carry out a comprehensive and integrated pursuit of all USDA mission areas for the advancement of sustainable aviation fuels, including through</p><ul><li>the identification of opportunities to maximize the development and commercialization of the fuels,</li><li>supporting rural economic development through improved sustainability for aviation, and</li><li>advancing public-private partnerships.</li></ul>",
      "updateDate": "2025-03-14",
      "versionCode": "id119s144"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s144is.xml"
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
      "title": "Farm to Fly Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T02:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farm to Fly Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Farm Security and Rural Investment Act of 2002 with respect to the definition of biofuels and sustainable aviation fuel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:25Z"
    }
  ]
}
```
