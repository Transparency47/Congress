# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1394?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1394
- Title: CURD Act
- Congress: 119
- Bill type: HR
- Bill number: 1394
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-05-08T08:05:54Z
- Update date including text: 2026-05-08T08:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1394",
    "number": "1394",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001213",
        "district": "1",
        "firstName": "Bryan",
        "fullName": "Rep. Steil, Bryan [R-WI-1]",
        "lastName": "Steil",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "CURD Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:05:54Z",
    "updateDateIncludingText": "2026-05-08T08:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:32:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "WI"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "WI"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WI"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "IA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MI"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "IA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WI"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-10",
      "state": "VA"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MI"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "ID"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1394ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1394\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Steil (for himself and Mr. Costa ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to define the term natural cheese.\n#### 1. Short title\nThis Act may be cited as the Codifying Useful Regulatory Definitions Act or the CURD Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nThere is a need to define the term natural cheese in order to maintain transparency and consistency for consumers so that they may differentiate natural cheese from process cheese .\n**(2)**\nThe term natural cheese has been used within the cheese making industry for more than 50 years and is well-established.\n#### 3. Definition of natural cheese\n##### (a) Definition\nSection 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ) is amended by adding at the end the following:\n(ss) (1) The term natural cheese means cheese that is a ripened or unripened soft, semi-soft, or hard product, which may be coated, that is produced\u2014 (A) by\u2014 (i) coagulating wholly or partly the protein of milk, skimmed milk, partly skimmed milk, cream, whey cream, or buttermilk, or any combination of such ingredients, through the action of rennet or other suitable coagulating agents, and by partially draining the whey resulting from the coagulation, while respecting the principle that cheese-making results in a concentration of milk protein (in particular, the casein portion), and that consequently, the protein content of the cheese will be distinctly higher than the protein level of the blend of the above milk materials from which the cheese was made; or (ii) processing techniques involving coagulation of the protein of milk or products obtained from milk to produce an end-product with similar physical, chemical, and or\u00adgan\u00ado\u00adlep\u00adtic characteristics as the product described in subclause (i); and (iii) including the addition of safe and suitable non-milk derived ingredients of the type permitted in the standards of identity described in clause (B) as natural cheese; or (B) in accordance with standards of identity under part 133 of title 21, Code of Federal Regulations (or any successor regulations), other than the standards described in subparagraph (2) or any future standards adopted by the Secretary in accordance with subparagraph (2)(I). (2) Such term does not include\u2014 (A) pasteurized process cheeses as defined in section 133.169, 133.170, or 133.171 of title 21, Code of Federal Regulations (or any successor regulations); (B) pasteurized process cheese foods as defined in section 133.173 or 133.174 of title 21, Code of Federal Regulations (or any successor regulations); (C) pasteurized cheese spreads as defined in section 133.175, 133.176, or 133.178 of title 21, Code of Federal Regulations (or any successor regulations); (D) pasteurized process cheese spreads as defined in section 133.179 or 133.180 of title 21, Code of Federal Regulations (or any successor regulations); (E) pasteurized blended cheeses as defined in section 133.167 or 133.168 of title 21, Code of Federal Regulations (or any successor regulations); (F) any products comparable to any product described in any of clauses (A) through (E); (G) cold pack cheeses as defined in section 133.123, 133.124, or 133.125 title 21, Code of Federal Regulations (or any successor regulations); (H) grated American cheese food as defined in section 133.147 of title 21, Code of Federal Regulations (or any successor regulations); or (I) any other product the Secretary may designate as a process cheese. (3) For purposes of this paragraph, the term milk has the meaning given such term in section 133.3 of title 21, Code of Federal Regulations (or any successor regulations) and includes the lacteal secretions from animals other than cows. .\n##### (b) Labeling\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) If its label or labeling includes the term natural cheese as a factual descriptor of a category of cheese unless the food meets the definition of natural cheese under section 201(ss), except that nothing in this paragraph shall prohibit the use of the term natural or all-natural , or a similar claim or statement with respect to a food in a manner that is consistent with regulations, guidance, or policy statements issued by the Secretary. .\n##### (c) National uniformity\nSection 403A(a)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343\u20131(a)(2) ) is amended by striking or 403(x) and inserting 403(x), or 403(z) .",
      "versionDate": "2025-02-14",
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
        "actionDate": "2025-01-22",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "184",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CURD Act",
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
        "item": {
          "name": "Food supply, safety, and labeling",
          "updateDate": "2025-06-13T19:13:13Z"
        }
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-19T12:09:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1394",
          "measure-number": "1394",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1394v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Codifying Useful Regulatory Definitions Act or the</strong> <strong>CURD Act</strong></p><p>This bill establishes a statutory definition for <em>natural cheese</em>. Under the bill, <em>natural cheese</em> is defined as cheese (ripened or unripened soft, semi-soft, or hard) that is produced from animal milk or certain dairy ingredients and is produced in accordance with established cheese-making standards. The definition excludes pasteurized process cheeses, cheese foods, and cheese spreads.</p><p>A food that does not meet this definition is deemed misbranded and may not be sold if its label includes the term<em> natural cheese</em> as a factual descriptor of a category of cheese.</p>"
        },
        "title": "CURD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1394.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Codifying Useful Regulatory Definitions Act or the</strong> <strong>CURD Act</strong></p><p>This bill establishes a statutory definition for <em>natural cheese</em>. Under the bill, <em>natural cheese</em> is defined as cheese (ripened or unripened soft, semi-soft, or hard) that is produced from animal milk or certain dairy ingredients and is produced in accordance with established cheese-making standards. The definition excludes pasteurized process cheeses, cheese foods, and cheese spreads.</p><p>A food that does not meet this definition is deemed misbranded and may not be sold if its label includes the term<em> natural cheese</em> as a factual descriptor of a category of cheese.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hr1394"
    },
    "title": "CURD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Codifying Useful Regulatory Definitions Act or the</strong> <strong>CURD Act</strong></p><p>This bill establishes a statutory definition for <em>natural cheese</em>. Under the bill, <em>natural cheese</em> is defined as cheese (ripened or unripened soft, semi-soft, or hard) that is produced from animal milk or certain dairy ingredients and is produced in accordance with established cheese-making standards. The definition excludes pasteurized process cheeses, cheese foods, and cheese spreads.</p><p>A food that does not meet this definition is deemed misbranded and may not be sold if its label includes the term<em> natural cheese</em> as a factual descriptor of a category of cheese.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hr1394"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1394ih.xml"
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
      "title": "CURD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CURD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T02:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Codifying Useful Regulatory Definitions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T02:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to define the term natural cheese.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T02:48:20Z"
    }
  ]
}
```
