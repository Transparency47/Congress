# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8596?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8596
- Title: FAIR Labels Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8596
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-23T08:07:30Z
- Update date including text: 2026-05-23T08:07:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-30 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-30 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8596",
    "number": "8596",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "A000379",
        "district": "4",
        "firstName": "Mark",
        "fullName": "Rep. Alford, Mark [R-MO-4]",
        "lastName": "Alford",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "FAIR Labels Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:30Z",
    "updateDateIncludingText": "2026-05-23T08:07:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-30T13:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "GA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "ID"
    },
    {
      "bioguideId": "S001195",
      "district": "8",
      "firstName": "Jason",
      "fullName": "Rep. Smith, Jason [R-MO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "MO"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "WI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "NE"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "KS"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "VA"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "ID"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8596ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8596\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Alford (for himself, Mr. Flood , Mr. Carter of Georgia , Mr. Pfluger , Mr. Simpson , Mr. Smith of Missouri , Mr. Jackson of Texas , and Mr. Wied ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Federal Meat Inspection Act and the Poultry Products Inspection Act to ensure that consumers can make informed decisions in choosing between meat and poultry products and cell-cultivated protein products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair and Accurate Ingredient Representation on Labels Act of 2026 or the FAIR Labels Act of 2026 .\n#### 2. Revised memorandum of understanding between Secretary of Agriculture and Secretary of Health and Human Services regarding regulation of cell-cultivated protein product\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Agriculture and the Secretary of Health and Human Services shall jointly revise the Memorandum of Understanding entitled Formal Agreement Between FDA and USDA Regarding Oversight of Human Food Produced Using Animal Cell Technology Derived from Cell Lines of USDA-amenable Species entered into March 7, 2019, so that with respect to the regulation of cell-cultivated protein products\u2014\n**(1)**\nthe Secretary of Agriculture shall conduct such activities as are necessary to implement the amendments made by this Act; and\n**(2)**\nthe Secretary of Health and Human Services shall\u2014\n**(A)**\nconduct premarket consultation processes to evaluate production materials and processes and manufacturing controls, including oversight of tissue collection, cell lines and banks, and all components and inputs;\n**(B)**\noversee the initial cell collection and the development and maintenance of qualified cell banks;\n**(C)**\noversee the proliferation and differentiation of cells up to the time of harvest;\n**(D)**\nensure that the appropriate entities comply with applicable requirements of the Food and Drug Administration, including facility registration, the current good manufacturing practices and preventive controls regulation, and requirements applicable to substances that become a component of food or otherwise affect the characteristics of food;\n**(E)**\ndevelop additional requirements for cell bank and cell culturing facility conditions and processes to ensure that biological material exiting the culture process is safe; and\n**(F)**\nconduct appropriate inspections and follow-up activities, including taking enforcement action if necessary, to ensure that cell bank and cell culturing facilities are in compliance with applicable laws (including regulations).\n#### 3. Regulation of cell-cultivated protein products by Secretary of Agriculture\n##### (a) Cell-cultivated protein products\n**(1) Definition**\nSection 1 of the Federal Meat Inspection Act ( 21 U.S.C. 601 ) is amended by adding at the end the following:\n(x) The term cell-cultivated protein product means any product capable of use as human food that\u2014 (1) is made wholly or in part from any cell culture or the DNA of an amenable species using animal cell culture technology; and (2) is grown or cultivated outside of the live animal from which the cell culture or DNA was acquired. .\n**(2) Misbranding**\nSection 1(n)(3) of the Federal Meat Inspection Act ( 21 U.S.C. 601(n)(3) ) is amended to read as follows:\n(3) if it is a cell-cultivated protein, unless its label\u2014 (A) clearly indicates in a prominent, conspicuous, and legible manner the words cell-cultivated , in type of uniform size and prominence, immediately adjacent to the name of the food so as to render it likely to be read and understood by the ordinary individual under customary conditions of purchase and use; (B) bears a statement that the cell-cultivated protein product is derived from sources other than meat, in type of uniform size and prominence, immediately adjacent to the name of the food; and (C) bears a disclaimer that clearly indicates that the cell-cultivated protein product in its final product form is not derived from, or does not contain, naturally produced meat from a live amenable species; .\n**(3) Applicability**\nSection 25 of the Federal Meat Inspection Act ( 21 U.S.C. 625 ) is amended\u2014\n**(A)**\nby striking Notwithstanding and inserting (a) Notwithstanding ; and\n**(B)**\nby adding at the end the following:\n(b) The requirements of this Act shall apply with respect to cell-cultivated protein products in the same manner as such requirements apply to meat and meat food products. .\n##### (b) Cell-cultivated poultry products\n**(1) Definition**\nSection 4 of the Poultry Products Inspection Act ( 21 U.S.C. 453 ) is amended by adding at the following:\n(cc) The term cell-cultivated protein product means any product capable of use as human food that\u2014 (1) is made wholly or in part from any cell culture or the DNA of a live bird using animal cell culture technology; and (2) is grown or cultivated outside of the live bird from which the cell culture or DNA was acquired. .\n**(2) Misbranding**\nSection 4(h)(3) of the Poultry Products Inspection Act ( 21 U.S.C. 453(h)(3) ) is amended to read as follows:\n.\n(3) if it is a cell-cultivated protein product, unless its label\u2014 (A) clearly indicates in a prominent, conspicuous, and legible manner the words cell-cultivated , in type of uniform size and prominence, immediately adjacent to the name of the food so as to render it likely to be read and understood by the ordinary individual under customary conditions of purchase and use; (B) bears a statement that the cell-cultivated protein product is derived from sources other than poultry, in type of uniform size and prominence, immediately adjacent to the name of the food; and (C) bears a disclaimer that clearly indicates that the cell-cultivated protein product in its final product form is not derived from, or does not contain, a live amenable bird; .\n**(3) Applicability**\nSection 18 of the Poultry Products Inspection Act ( 21 U.S.C. 467a ) is amended by adding at the end the following:\n(d) The requirements of this Act shall apply with respect to cell-cultivated protein products in the same manner as such requirements apply to poultry and poultry products. .\n##### (c) Plant-Based Alternative Protein Product\nThe Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) is amended\u2014\n**(1)**\nin section 201 ( 21 U.S.C. 321 ), by adding at the end the following:\n(tt) The term plant-based alternative protein product means any food product that\u2014 (1) is made wholly or in part from any plant species; (2) approximates the aesthetic qualities (primarily texture, flavor, and appearance) of meat, poultry, or a food product thereof; and (3) is manufactured to appear as meat, poultry, or a food product thereof. ; and\n**(2)**\nin section 403 ( 21 U.S.C. 343 ), by adding at the end the following:\n(z) If it is a plant-based alternative protein product, unless its label\u2014 (1) bears, in type of uniform size and prominence, the phrase plant-based alternative protein product and, immediately thereafter, the name of the food; and (2) in a prominently placed, conspicuous, and legible manner so as to render it likely to be read and understood by the ordinary individual under customary conditions of purchase and use, bears a statement that clearly indicates that the product is not derived from, or does not contain, naturally produced meat or poultry from a live animal or bird species. .\n##### (d) Standards of identity\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Agriculture, in consultation with the Secretary of Health and Human Services, shall develop common standards of identity for cell-cultivated protein products and plant-based alternative protein products that are consistent with the definitions specified in section 1 of the Federal Meat Inspection Act ( 21 U.S.C. 601 ), section 4 of the Poultry Products Inspection Act ( 21 U.S.C. 453 ), and section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 ), respectively, as amended by this section.",
      "versionDate": "2026-04-30",
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
        "actionDate": "2026-04-30",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "4464",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAIR Labels Act of 2026",
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
        "updateDate": "2026-05-15T16:01:11Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8596ih.xml"
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
      "title": "FAIR Labels Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-02T03:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR Labels Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-02T03:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair and Accurate Ingredient Representation on Labels Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-02T03:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Meat Inspection Act and the Poultry Products Inspection Act to ensure that consumers can make informed decisions in choosing between meat and poultry products and cell-cultivated protein products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-02T03:33:29Z"
    }
  ]
}
```
