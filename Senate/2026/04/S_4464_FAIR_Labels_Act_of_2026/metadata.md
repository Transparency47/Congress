# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4464?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4464
- Title: FAIR Labels Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4464
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-21T11:03:37Z
- Update date including text: 2026-05-21T11:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4464",
    "number": "4464",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "FAIR Labels Act of 2026",
    "type": "S",
    "updateDate": "2026-05-21T11:03:37Z",
    "updateDateIncludingText": "2026-05-21T11:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T18:02:15Z",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4464is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4464\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Ricketts (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Meat Inspection Act and the Poultry Products Inspection Act to ensure that consumers can make informed decisions in choosing between meat and poultry products and cell-cultivated protein products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair and Accurate Ingredient Representation on Labels Act of 2026 or the FAIR Labels Act of 2026 .\n#### 2. Revised memorandum of understanding between Secretary of Agriculture and Secretary of Health and Human Services regarding regulation of cell-cultivated protein product\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Agriculture and the Secretary of Health and Human Services shall jointly revise the Memorandum of Understanding entitled Formal Agreement Between FDA and USDA Regarding Oversight of Human Food Produced Using Animal Cell Technology Derived from Cell Lines of USDA-amenable Species entered into March 7, 2019, so that with respect to the regulation of cell-cultivated protein products\u2014\n**(1)**\nthe Secretary of Agriculture shall conduct such activities as are necessary to implement the amendments made by this Act; and\n**(2)**\nthe Secretary of Health and Human Services shall\u2014\n**(A)**\nconduct premarket consultation processes to evaluate production materials and processes and manufacturing controls, including oversight of tissue collection, cell lines and banks, and all components and inputs;\n**(B)**\noversee the initial cell collection and the development and maintenance of qualified cell banks;\n**(C)**\noversee the proliferation and differentiation of cells up to the time of harvest;\n**(D)**\nensure that the appropriate entities comply with applicable requirements of the Food and Drug Administration, including facility registration, the current good manufacturing practices and preventive controls regulation, and requirements applicable to substances that become a component of food or otherwise affect the characteristics of food;\n**(E)**\ndevelop additional requirements for cell bank and cell culturing facility conditions and processes to ensure that biological material exiting the culture process is safe; and\n**(F)**\nconduct appropriate inspections and follow-up activities, including taking enforcement action if necessary, to ensure that cell bank and cell culturing facilities are in compliance with applicable laws (including regulations).\n#### 3. Regulation of cell-cultivated protein products by Secretary of Agriculture\n##### (a) Cell-Cultivated protein products\n**(1) Definition**\nSection 1 of the Federal Meat Inspection Act ( 21 U.S.C. 601 ) is amended by adding at the end the following:\n(x) The term cell-cultivated protein product means any product capable of use as human food that\u2014 (1) is made wholly or in part from any cell culture or the DNA of an amenable species using animal cell culture technology; and (2) is grown or cultivated outside of the live animal from which the cell culture or DNA was acquired. .\n**(2) Misbranding**\nSection 1(n)(3) of the Federal Meat Inspection Act ( 21 U.S.C. 601(n)(3) ) is amended to read as follows:\n(3) if it is a cell-cultivated protein, unless its label\u2014 (A) clearly indicates in a prominent, conspicuous, and legible manner the words cell-cultivated , in type of uniform size and prominence, immediately adjacent to the name of the food so as to render it likely to be read and understood by the ordinary individual under customary conditions of purchase and use; (B) bears a statement that the cell-cultivated protein product is derived from sources other than meat, in type of uniform size and prominence, immediately adjacent to the name of the food; and (C) bears a disclaimer that clearly indicates that the cell-cultivated protein product in its final product form is not derived from, or does not contain, naturally produced meat from a live amenable species; .\n**(3) Applicability**\nSection 25 of the Federal Meat Inspection Act ( 21 U.S.C. 625 ) is amended\u2014\n**(A)**\nby striking Notwithstanding and inserting (a) Notwithstanding ; and\n**(B)**\nby adding at the end the following:\n(b) The requirements of this Act shall apply with respect to cell-cultivated protein products in the same manner as such requirements apply to meat and meat food products. .\n##### (b) Cell-Cultivated poultry products\n**(1) Definition**\nSection 4 of the Poultry Products Inspection Act ( 21 U.S.C. 453 ) is amended by adding at the following:\n(cc) The term cell-cultivated protein product means any product capable of use as human food that\u2014 (1) is made wholly or in part from any cell culture or the DNA of a live bird using animal cell culture technology; and (2) is grown or cultivated outside of the live bird from which the cell culture or DNA was acquired. .\n**(2) Misbranding**\nSection 4(h)(3) of the Poultry Products Inspection Act ( 21 U.S.C. 453(h)(3) ) is amended to read as follows:\n(3) if it is a cell-cultivated protein product, unless its label\u2014 (A) clearly indicates in a prominent, conspicuous, and legible manner the words cell-cultivated , in type of uniform size and prominence, immediately adjacent to the name of the food so as to render it likely to be read and understood by the ordinary individual under customary conditions of purchase and use; (B) bears a statement that the cell-cultivated protein product is derived from sources other than poultry, in type of uniform size and prominence, immediately adjacent to the name of the food; and (C) bears a disclaimer that clearly indicates that the cell-cultivated protein product in its final product form is not derived from, or does not contain, a live amenable bird; .\n**(3) Applicability**\nSection 18 of the Poultry Products Inspection Act ( 21 U.S.C. 467a ) is amended by adding at the end the following:\n(d) The requirements of this Act shall apply with respect to cell-cultivated protein products in the same manner as such requirements apply to poultry and poultry products. .\n##### (c) Plant-Based Alternative Protein Product\nThe Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) is amended\u2014\n**(1)**\nin section 201 ( 21 U.S.C. 321 ), by adding at the end the following:\n(tt) The term plant-based alternative protein product means any food product that\u2014 (1) is made wholly or in part from any plant species; (2) approximates the aesthetic qualities (primarily texture, flavor, and appearance) of meat, poultry, or a food product thereof; and (3) is manufactured to appear as meat, poultry, or a food product thereof. ; and\n**(2)**\nin section 403 ( 21 U.S.C. 343 ), by adding at the end the following:\n(z) If it is a plant-based alternative protein product, unless its label\u2014 (1) bears, in type of uniform size and prominence, the phrase plant-based alternative protein product and, immediately thereafter, the name of the food; and (2) in a prominently placed, conspicuous, and legible manner so as to render it likely to be read and understood by the ordinary individual under customary conditions of purchase and use, bears a statement that clearly indicates that the product is not derived from, or does not contain, naturally produced meat or poultry from a live animal or bird species. .\n##### (d) Standards of identity\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Agriculture, in consultation with the Secretary of Health and Human Services, shall develop common standards of identity for cell-cultivated protein products and plant-based alternative protein products that are consistent with the definitions specified in section 1 of the Federal Meat Inspection Act ( 21 U.S.C. 601 ), section 4 of the Poultry Products Inspection Act ( 21 U.S.C. 453 ), and section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 ), respectively, as amended by this section.",
      "versionDate": "2026-04-30",
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
        "actionDate": "2026-04-30",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8596",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAIR Labels Act of 2026",
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
        "updateDate": "2026-05-15T22:34:29Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4464is.xml"
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
      "title": "FAIR Labels Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FAIR Labels Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair and Accurate Ingredient Representation on Labels Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Meat Inspection Act and the Poultry Products Inspection Act to ensure that consumers can make informed decisions in choosing between meat and poultry products and cell-cultivated protein products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:33Z"
    }
  ]
}
```
