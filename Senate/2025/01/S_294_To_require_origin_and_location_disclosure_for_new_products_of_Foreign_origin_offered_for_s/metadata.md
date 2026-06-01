# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/294?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/294
- Title: COOL Online Act
- Congress: 119
- Bill type: S
- Bill number: 294
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-10-09T03:26:19Z
- Update date including text: 2025-10-09T03:26:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/294",
    "number": "294",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "COOL Online Act",
    "type": "S",
    "updateDate": "2025-10-09T03:26:19Z",
    "updateDateIncludingText": "2025-10-09T03:26:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T17:42:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s294is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 294\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Baldwin (for herself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require origin and location disclosure for new products of Foreign origin offered for sale on the internet.\n#### 1. Short title\nThis Act may be cited as the Country Of Origin Labeling Online Act or the COOL Online Act .\n#### 2. Mandatory origin and location disclosure for new products of Foreign origin offered for sale on the internet\n##### (a) Mandatory disclosure\n**(1) In general**\n**(A) Disclosure**\nSubject to subparagraph (B), it shall be unlawful for a product that is marked or required to be marked under section 304 of the Tariff Act of 1930 ( 19 U.S.C. 1304 ) to be introduced, sold, advertised, or offered for sale in commerce on an internet website unless the internet website description of the product indicates in a conspicuous place\u2014\n**(i)**\nthe country of origin of the product (or, in the case of a multi-sourced product, the countries of origin), in a manner consistent with the regulations prescribed under such section 304; and\n**(ii)**\nthe country in which the seller of the product has its principal place of business.\n**(B) Exclusions**\n**(i) Agricultural products**\nThe disclosure requirements under clauses (i) and (ii) of subparagraph (A) shall not apply to\u2014\n**(I)**\na covered commodity (as defined in section 281 of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1638 ));\n**(II)**\na meat or meat food product subject to inspection under the Federal Meat Inspection Act ( 21 U.S.C. 601 et seq. );\n**(III)**\na poultry or poultry product subject to inspection under the Poultry Products Inspection Act ( 21 U.S.C. 451 et seq. ); or\n**(IV)**\nan egg product subject to regulation under the Egg Products Inspection Act ( 21 U.S.C. 1031 et seq. ).\n**(ii) Food and drugs**\nThe disclosure requirements under clauses (i) and (ii) of subparagraph (A) shall not apply to a food or drug (as those terms are defined in paragraphs (f) and (g), respectively, of section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ) that is subject to the jurisdiction of the Food and Drug Administration.\n**(iii) Used or previously-owned articles**\nThe disclosure requirements under clauses (i) and (ii) of subparagraph (A) shall not apply to any used or previously-owned article sold by an internet website marketplace or a seller on an internet website marketplace. For the purposes of the preceding sentence, the term used or previously-owned article means an article that was previously sold or offered for sale at retail.\n**(iv) Small seller**\nThe disclosure requirements under clauses (i) and (ii) of subparagraph (A) shall not apply to goods listed by a small seller. For the purposes of the preceding sentence, the term small seller means a seller with annual sales of less than $20,000 and fewer than 200 discrete sales.\n**(C) Multi-sourced products**\nFor purposes of subparagraph (A)(i), a product shall be considered to be a multi-sourced product if a seller offers for sale a finished product, identical versions of which are produced in multiple countries.\n**(2) Certain drug products**\nIt shall be unlawful for a drug that is not subject to section 503(b)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353(b)(1) ) and that is required to be marked under section 304 of the Tariff Act of 1930 ( 19 U.S.C. 1304 ) to be offered for sale in commerce to consumers on an internet website unless the internet website description of the drug indicates in a conspicuous place the name and place of business of the manufacturer, packer, or distributor that is required to appear on the label of the drug in accordance with section 502(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352(b) ).\n**(3) Obligation to provide**\nA manufacturer, importer, distributor, seller, supplier, or private labeler seeking to have a product introduced, sold, advertised, or offered for sale in commerce shall provide the information identified clauses (i) and (ii) of paragraph (1)(A) or paragraph (2), as applicable, to the relevant retailer.\n**(4) Safe harbor**\nA retailer or a seller on an internet website marketplace satisfies the disclosure requirements under clauses (i) and (ii) of paragraph (1)(A) or paragraph (2), as applicable, if the disclosure includes the country of origin and seller information provided by a third-party manufacturer, importer, distributor, seller, supplier, or private labeler of the product.\n##### (b) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (a) shall be treated as a violation of a rule prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person that violates subsection (a) shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) as though all applicable terms and provisions of that Act were incorporated and made part of this section.\n**(C) Authority preserved**\nNothing in this section may be construed to limit the authority of the Commission under any other provision of law.\n**(3) Interagency agreement**\nNot later than 6 months after the date of enactment of this section, the Commission, the U.S. Customs and Border Protection, and the Department of Agriculture shall\u2014\n**(A)**\nenter into a Memorandum of Understanding or other appropriate agreement for the purpose of providing consistent implementation of this section; and\n**(B)**\npublish such agreement to provide public guidance.\n**(4) Definition of Commission**\nIn this subsection, the term Commission means the Federal Trade Commission.\n##### (c) Limitation of liability\nA retailer or seller is not in violation of subsection (a) if\u2014\n**(1)**\na third-party manufacturer, distributor, seller, supplier, or private labeler provided the retailer or seller with a false or deceptive representation as to the country of origin of a product or its parts or processing; and\n**(2)**\nthe retailer or seller\u2014\n**(A)**\nrelied in good faith on that representation; and\n**(B)**\ntook immediate action to remove any such false or deceptive representations upon notice.\n##### (d) Authority preserved\nNothing in this section may be construed to limit the authority of the Department of Agriculture, the Food and Drug Administration, or U.S. Customs and Border Protection under any other provision of law.\n##### (e) Effective date\nThis section shall take effect 12 months after the date of the publication of the Memorandum of Understanding or agreement under subsection (b)(3).",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-03-20T18:36:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s294",
          "measure-number": "294",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s294v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Country of Origin Labeling Requirement Act or the COOL Online Act</b><br/> <br/> This bill requires sellers of imported products online to conspicuously disclose the country of origin of the products and the country where the seller's principal place of business is located. </p><p>This requirement does not apply to specified products, such as agricultural commodities, food or drugs, or previously owned items.</p><p>The Federal Trade Commission must enforce violations of this requirement as unfair or deceptive trade practices.</p>"
        },
        "title": "COOL Online Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s294.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Country of Origin Labeling Requirement Act or the COOL Online Act</b><br/> <br/> This bill requires sellers of imported products online to conspicuously disclose the country of origin of the products and the country where the seller's principal place of business is located. </p><p>This requirement does not apply to specified products, such as agricultural commodities, food or drugs, or previously owned items.</p><p>The Federal Trade Commission must enforce violations of this requirement as unfair or deceptive trade practices.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s294"
    },
    "title": "COOL Online Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Country of Origin Labeling Requirement Act or the COOL Online Act</b><br/> <br/> This bill requires sellers of imported products online to conspicuously disclose the country of origin of the products and the country where the seller's principal place of business is located. </p><p>This requirement does not apply to specified products, such as agricultural commodities, food or drugs, or previously owned items.</p><p>The Federal Trade Commission must enforce violations of this requirement as unfair or deceptive trade practices.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s294"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s294is.xml"
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
      "title": "COOL Online Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "COOL Online Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Country Of Origin Labeling Online Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require origin and location disclosure for new products of Foreign origin offered for sale on the internet.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:41Z"
    }
  ]
}
```
