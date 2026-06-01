# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/184?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/184
- Title: CURD Act
- Congress: 119
- Bill type: S
- Bill number: 184
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-12-05T21:45:12Z
- Update date including text: 2025-12-05T21:45:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/184",
    "number": "184",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "CURD Act",
    "type": "S",
    "updateDate": "2025-12-05T21:45:12Z",
    "updateDateIncludingText": "2025-12-05T21:45:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T17:38:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "OR"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ID"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "WI"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ID"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-22",
      "state": "VT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-15",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s184is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 184\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Johnson (for himself, Mr. Wyden , Mr. Risch , Ms. Baldwin , Mr. Crapo , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to define the term natural cheese.\n#### 1. Short title\nThis Act may be cited as the Codifying Useful Regulatory Definitions Act or the CURD Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nThere is a need to define the term natural cheese in order to maintain transparency and consistency for consumers so that they may differentiate natural cheese from process cheese .\n**(2)**\nThe term natural cheese has been used within the cheese making industry for more than 50 years and is well-established.\n#### 3. Definition of natural cheese\n##### (a) Definition\nSection 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ) is amended by adding at the end the following:\n(tt) (1) The term natural cheese means cheese that is a ripened or unripened soft, semi-soft, or hard product, which may be coated, that is produced\u2014 (A) by\u2014 (i) coagulating wholly or partly the protein of milk, skimmed milk, partly skimmed milk, cream, whey cream, or buttermilk, or any combination of such ingredients, through the action of rennet or other suitable coagulating agents, and by partially draining the whey resulting from the coagulation, while respecting the principle that cheese-making results in a concentration of milk protein (in particular, the casein portion), and that consequently, the protein content of the cheese will be distinctly higher than the protein level of the blend of the above milk materials from which the cheese was made; or (ii) processing techniques involving coagulation of the protein of milk or products obtained from milk to produce an end-product with similar physical, chemical, and organoleptic characteristics as the product described in subclause (i); and (iii) including the addition of safe and suitable non-milk derived ingredients of the type permitted in the standards of identity described in clause (B) as natural cheese; or (B) in accordance with standards of identity under part 133 of title 21, Code of Federal Regulations (or any successor regulations), other than the standards described in subparagraph (2) or any future standards adopted by the Secretary in accordance with subparagraph (2)(I). (2) Such term does not include\u2014 (A) pasteurized process cheeses as defined in section 133.169, 133.170, or 133.171 of title 21, Code of Federal Regulations (or any successor regulations); (B) pasteurized process cheese foods as defined in section 133.173 or 133.174 of title 21, Code of Federal Regulations (or any successor regulations); (C) pasteurized cheese spreads as defined in section 133.175, 133.176, or 133.178 of title 21, Code of Federal Regulations (or any successor regulations); (D) pasteurized process cheese spreads as defined in section 133.179 or 133.180 of title 21, Code of Federal Regulations (or any successor regulations); (E) pasteurized blended cheeses as defined in section 133.167 or 133.168 of title 21, Code of Federal Regulations (or any successor regulations); (F) any products comparable to any product described in any of clauses (A) through (E); (G) cold pack cheeses as defined in section 133.123, 133.124, or 133.125 title 21, Code of Federal Regulations (or any successor regulations); (H) grated American cheese food as defined in section 133.147 of title 21, Code of Federal Regulations (or any successor regulations); or (I) any other product the Secretary may designate as a process cheese. (3) For purposes of this paragraph, the term milk has the meaning given such term in section 133.3 of title 21, Code of Federal Regulations (or any successor regulations) and includes the lacteal secretions from animals other than cows. .\n##### (b) Labeling\nSection 403 of the Federal Food Drug and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) If its label or labeling includes the term natural cheese as a factual descriptor of a category of cheese unless the food meets the definition of natural cheese under section 201(tt), except that nothing in this paragraph shall prohibit the use of the term natural or all-natural , or a similar claim or statement with respect to a food in a manner that is consistent with regulations, guidance, or policy statements issued by the Secretary. .\n##### (c) National uniformity\nSection 403A(a)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343\u20131(a)(2) ) is amended by striking or 403(x) and inserting 403(x), or 403(z) .",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-02-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1394",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CURD Act",
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
      "legislativeSubjects": {
        "item": {
          "name": "Food supply, safety, and labeling",
          "updateDate": "2025-03-17T15:38:56Z"
        }
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T21:09:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119s184",
          "measure-number": "184",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s184v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Codifying Useful Regulatory Definitions Act or the</strong> <strong>CURD Act</strong></p><p>This bill establishes a statutory definition for <em>natural cheese</em>. Under the bill, <em>natural cheese</em> is defined as cheese (ripened or unripened soft, semi-soft, or hard) that is produced from animal milk or certain dairy ingredients and is produced in accordance with established cheese-making standards. The definition excludes pasteurized process cheeses, cheese foods, and cheese spreads.</p><p>A food that does not meet this definition is deemed misbranded and may not be sold if its label includes the term<em> natural cheese</em> as a factual descriptor of a category of cheese.</p>"
        },
        "title": "CURD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s184.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Codifying Useful Regulatory Definitions Act or the</strong> <strong>CURD Act</strong></p><p>This bill establishes a statutory definition for <em>natural cheese</em>. Under the bill, <em>natural cheese</em> is defined as cheese (ripened or unripened soft, semi-soft, or hard) that is produced from animal milk or certain dairy ingredients and is produced in accordance with established cheese-making standards. The definition excludes pasteurized process cheeses, cheese foods, and cheese spreads.</p><p>A food that does not meet this definition is deemed misbranded and may not be sold if its label includes the term<em> natural cheese</em> as a factual descriptor of a category of cheese.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119s184"
    },
    "title": "CURD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Codifying Useful Regulatory Definitions Act or the</strong> <strong>CURD Act</strong></p><p>This bill establishes a statutory definition for <em>natural cheese</em>. Under the bill, <em>natural cheese</em> is defined as cheese (ripened or unripened soft, semi-soft, or hard) that is produced from animal milk or certain dairy ingredients and is produced in accordance with established cheese-making standards. The definition excludes pasteurized process cheeses, cheese foods, and cheese spreads.</p><p>A food that does not meet this definition is deemed misbranded and may not be sold if its label includes the term<em> natural cheese</em> as a factual descriptor of a category of cheese.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119s184"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s184is.xml"
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
      "title": "CURD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CURD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Codifying Useful Regulatory Definitions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to define the term natural cheese.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:29Z"
    }
  ]
}
```
