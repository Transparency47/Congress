# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4435?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4435
- Title: Cosmetic Hazardous Ingredient Right to Know Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4435
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-05-26T19:53:57Z
- Update date including text: 2026-05-26T19:53:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4435",
    "number": "4435",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Cosmetic Hazardous Ingredient Right to Know Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-26T19:53:57Z",
    "updateDateIncludingText": "2026-05-26T19:53:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:06:10Z",
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
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NJ"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4435ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4435\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Ms. Schakowsky (for herself, Ms. Matsui , Mrs. Dingell , Mr. Evans of Pennsylvania , Mr. Khanna , Ms. Norton , Mr. Thanedar , Ms. Tlaib , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to increase transparency with respect to cosmetic ingredients, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cosmetic Hazardous Ingredient Right to Know Act of 2025 .\n#### 2. Cosmetic regulation\n##### (a) Definition\nSection 201(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(i) ) is amended by adding at the end the following: Such term includes such an article that is intended for consumer sale or professional use (as defined in section 617). .\n##### (b) Regulation\nChapter VI of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 361 et seq. ) is amended\u2014\n**(1)**\nby inserting before section 601 the following:\nA Adulterated and Misbranded Cosmetics ;\n**(2)**\nin section 602, by adding at the end the following:\n(g) If the fragrance and flavor ingredient information required to be disclosed pursuant to sections 615 and 616 is not disclosed in accordance with such sections. (h) If its packaging fails to include any fragrance or flavor ingredient present in such cosmetic or the website of the brand owner of such cosmetic fails to disclose any such fragrance or flavor ingredient. (i) If the website of the brand owner of the cosmetic fails to include a link to the Uniform Resource Locator (referred to in this chapter as a URL ) for any list specified in section 616(b) on which each ingredient present in such cosmetic appears. ;\n**(3)**\nin section 614, by amending subsection (b) to read as follows:\n(b) Limitations (1) In general Notwithstanding subsection (a), nothing in this section shall be construed to prevent any State (or a political subdivision thereof) from\u2014 (A) prohibiting the use or limiting the amount of an ingredient in a cosmetic product; (B) continuing to implement a requirement of such State (or a political subdivision thereof) that is in effect at the time of enactment of the Modernization of Cosmetics Regulation Act of 2022 for the reporting to the State (or a political subdivision thereof) of an ingredient in a cosmetic product; or (C) implementing a requirement of such State (or a political subdivision thereof) that provides for greater transparency, disclosure, or protection with respect to a cosmetic ingredient than the requirements established under the amendments made by the Cosmetic Hazardous Ingredient Right to Know Act of 2025 (or continuing to implement any such requirement that is in effect as of the date of the enactment of such Act). (2) Modernization of Cosmetics Regulation Act of 2022 Nothing in the amendments to this Act made by the Modernization of Cosmetics Regulation Act of 2022 shall be construed to preempt any State statute, public initiative, referendum, regulation, or other State action, except as expressly provided in subsection (a). .\n**(4)**\nby adding at the end the following:\nB Fragrances and Flavors 615. Website disclosure of ingredients (a) In general Effective beginning on the date that is 1 year after the date of the enactment of the Cosmetic Hazardous Ingredient Right to Know Act of 2025 , a brand owner shall disclose in an electronically readable format on the website of the brand owner, and make available to any relevant internet vendor, with respect to each cosmetic sold or offered for sale in interstate commerce by such brand owner, the following information: (1) A full listing of each ingredient present in such cosmetic, including each fragrance or flavor ingredient present in such cosmetic, in descending order of predominance. (2) Any ingredient present in such cosmetic, listed in descending order of predominance, followed by a link to the URL of any list under section 616(b) on which such ingredient appears. (3) The functional purpose served by each such fragrance or flavor ingredient. (4) A link to the hazard communication safety data sheet for any such cosmetic intended for professional use. (b) Updates In the case of an update to any of the lists specified in subsection (b) or (c) of section 616 with respect to a cosmetic sold or offered for sale in interstate commerce by a brand owner, the brand owner shall revise the disclosure made under subsection (a) to reflect such update not later than 7 months after the date on which such update is formally noticed by the authoritative body who administers the list. 616. Cosmetic ingredient product label disclosure (a) In general Effective beginning on the date that is 2 years after the date of the enactment of the Cosmetic Hazardous Ingredient Right to Know Act of 2025 , for purposes of section 602(h), the packaging or labeling of a cosmetic shall include\u2014 (1) A full listing of each ingredient present in such cosmetic (including each fragrance or flavor ingredient), listed in descending order of predominance. (2) In the case of a cosmetic in which any ingredient specified in subsection (b) is present, the following statement: For health impacts related to any ingredients in this product, visit: www.____. , with the uniform resource locator of the website of the brand owner placed in the blank space. (b) Ingredients specified The ingredients specified in this subsection are the following chemicals (including chemicals included in any list specified in this subsection after the date of the enactment of this subchapter): (1) Chemicals for which a reference dose or reference concentration has been developed based on neurotoxicity in the Environmental Protection Agency\u2019s Integrated Risk Information System. (2) Chemicals that are identified as carcinogenic to humans, likely to be carcinogenic to humans, or as group A, B1, or B2 carcinogens, in the Environmental Protection Agency\u2019s Integrated Risk Information System. (3) Persistent, bioaccumulative, and toxic Priority Chemicals identified by the Environmental Protection Agency\u2019s National Waste Minimization Program as of February 22, 2016. (4) Chemicals that are identified in volumes 1 through 4 of the Reports on Human Exposure to Environmental Chemicals issued by the Centers for Disease Control and Prevention (and any updates to such reports). (5) Toxic pollutants listed under section 20 307(a)(1) of the Federal Water Pollution Control Act and priority pollutants identified in appendix A to part 423 of title 40, Code of Federal Regulations (or successor regulations). (6) Chemicals classified as Persistent, Bioaccumulative and Toxic by the Toxics Release Inventory published by the Environmental Protection Agency pursuant to section 313 of the Emergency Planning and Community Right-to-Know Act of 1986. (7) Chemicals that are identified in the Agency for Toxic Substances and Disease Registry\u2019s Toxic Substances Portal. (8) Chemicals that are hazardous substances, as such term is defined in section 101(14) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980. (9) Reproductive and developmental toxicants identified by monographs issued by the National Toxicology Program Center for the Evaluation of Risks to Human Reproduction. (10) Chemicals that are identified as known to be, or reasonably anticipated to be human carcinogens by the most recent Report on Carcinogens prepared by the National Toxicology Program pursuant to section 301(b)(4) of the Public Health Service Act. (11) Chemicals identified as persistent, bioaccumulative, and toxic (PBT) chemicals by the Department of Ecology of the State of Washington (WAC 173\u2013333 (2006)). (12) Chemicals specified in Chapter 6.6 of the California Safe Drinking Water and Toxic Enforcement Act of 1986 (sections 25249.5 through 25249.14 of the California Health and Safety Code), List of Reproductive and Developmental Toxicants and Carcinogens. (13) Chemicals for which primary maximum contaminant levels have been established and adopted under section 64431, 64444, or 64444.5 of division 22 of title 26 of the California Code of Regulations and chemicals for which notification levels, as defined in section 116455 of the California Health and Safety Code, have been established by the California State Water Resources Control Board. (14) Chemicals identified as toxic air contaminants under section 93000 or 93001 of title 17 of the California Code of Regulations. (15) Substances classified as carcinogens, mutagens or reproductive toxicants in Appendices 1 through 6 of Annex XVII to Regulation (EC) No. 1907/2006 of the European Union\u2019s Registration, Evaluation, Authorisation and Restriction of Chemicals (REACH) law, as revised by the Commission Regulation (EU) 2020/2096 of 15 December 2020. (16) Chemicals included in the European Union Candidate List of Substances of Very High Concern in accordance with Article 59 of the REACH Regulation (EC) No. 1907/2006 on the basis of fulfilling the criteria defined in Article 57(f) for endocrine disrupting properties. (17) Chemicals included in such European Chemicals Agency Candidate List of Substances of Very High Concern on the basis of fulfilling the criteria defined in Article 57(d), Article 57(e), or Article 57(f) for persistent, bioaccumulative and toxic, or very persistent and very bioaccumulative, properties. (18) Chemicals classified by the European Union in Annex VI to Regulation (EC) No. 1272/2008 as respiratory sensitizer category 1. (19) Chemicals that are identified as persistent, bioaccumulative, and inherently toxic to the environment by the Canadian Environmental Protection Act Environmental Registry Domestic Substances List pursuant to subsection 66(1) of the Canadian Environmental Protection Act, 1999. (20) Group 1, 2A, or 2B carcinogens identified by the International Agency for Research on Cancer of the World Health Organization. (21) Chemicals that are identified on Part A of the list of Chemicals for Priority Action prepared by the Oslo and Paris Conventions for the Protection of the Marine Environment of the North-East Atlantic. (22) Chemicals that are skin sensitizers and irritants classified by Regulation (EC) No 1272/2008 of the European Parliament and of the Council of 16 December 2008 on classification, labelling and packaging of substances and mixtures, amending and repealing Directives 67/548/EEC and 1999/45/EC, and amending Regulation (EC) No 1907/2006. (c) Master list (1) In general Not later than 6 months after the date of the enactment of the Cosmetic Hazardous Ingredient Right to Know Act of 2025 , the Secretary shall\u2014 (A) establish a master list of the chemicals that appear on the lists specified in subsections (b) and (c); (B) post such master list on a publicly available website of the Food and Drug Administration; and (C) establish a voluntary electronic distribution list to which cosmetic manufacturers and other interested parties may subscribe to receive a copy of the master list and any subsequent updates. (2) Updates (A) In general The Secretary shall maintain the master list established under paragraph (1) and make updates to such list as necessary. (B) Notification Not later than 30 days after making an update pursuant to subparagraph (A), the Secretary shall notify subscribers to the electronic distribution list referred to in paragraph (1)(C) of that update. (C) Semi-annual updates Not less frequently than twice per year, the Secretary shall publish on a publicly available website of the Food and Drug Administration a list of updates to the master list made during the preceding 6-month period that includes summaries of any chemicals added to or removed from the lists specified in subsections (b) and (c). 617. Definitions In this subchapter: (1) Brand owner The term brand owner means the entity responsible for bringing a cosmetic to market for retail consumer sale or professional use. (2) Electronically readable format The term electronically readable format means, with respect to information, that the information provided\u2014 (A) is machine readable by automated systems, including, web browsers, accessibility software to aid the disabled, automated scripts, and other software programs or applications; (B) is not restricted from access by search engines; (C) is not restricted from access by a requirement for registration, the provision of personally identifiable information, or the use of CAPTCHA or similar challenge response test technologies, whether visual, auditory, or otherwise; and (D) conforms to the most current version of the Web Content Accessibility Guidelines adopted by the Web Content Accessibility Guidelines Working Group of the World Wide Web Consortium. (3) Flavor ingredient The term flavor ingredient means, with respect to a cosmetic, any intentionally added substance or complex mixture of aroma chemicals, flavor chemicals, natural essential oils, and other functional ingredient or ingredients, including the constituent ingredients of botanicals, for which the purpose is to impart a flavor or taste, or to counteract a flavor or taste. (4) Fragrance ingredient The term fragrance ingredient means, with respect to a cosmetic, any intentionally added substance or complex mixture of aroma chemicals, natural essential oils, and other functional ingredient or ingredients for which the purpose is to impart an odor or scent, or to counteract an odor. (5) Ingredient The term ingredient means a chemical in a cosmetic, including\u2014 (A) a chemical that has a technical or functional effect in the cosmetic, including the breakdown products of an intentionally added chemical that also have a functional or technical effect in the cosmetic; (B) a substance that is present by reason of having been added to a cosmetic during processing for the substance\u2019s technical or functional effect; (C) a fragrance, flavor, preservative, or colorant (and the components thereof); and (D) any individual component that the Secretary deems to be an ingredient for purposes of this subchapter. (6) Professional use The term professional use means\u2014 (A) the application of a cosmetic to a human customer or client that is intended only for use by an employee or contractor, in settings such as cosmetology, nail care, barbering, esthetics, spa, and other professions as determined by the Secretary through regulation; or (B) the use by, or application to, a human of a cosmetic purchased from a hair salon, nail salon, beauty salon, spa, or other establishment that provides cosmetic treatment services for humans. .",
      "versionDate": "2025-07-16",
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
        "name": "Health",
        "updateDate": "2025-09-11T15:34:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-16",
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
          "measure-id": "id119hr4435",
          "measure-number": "4435",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-16",
          "originChamber": "HOUSE",
          "update-date": "2026-05-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4435v00",
            "update-date": "2026-05-26"
          },
          "action-date": "2025-07-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Cosmetic Hazardous Ingredient Right to Know Act of 2025</strong></p><p>This bill requires cosmetic products to be labeled with a full list of their ingredients, including fragrance and flavor ingredients, and imposes other disclosure and labeling requirements related to certain potentially harmful ingredients. A cosmetic product that fails to meet such requirements may not be sold.</p><p>Under current law, a cosmetic product\u2019s packaging must generally include a list of its ingredients, but fragrance or flavor ingredients may be listed as <em>fragrance</em> or <em>flavor</em> in lieu of listing specific ingredient names.</p><p>Within two years of the bill\u2019s enactment, a cosmetic product's labeling or packaging must include a full list of its ingredients, including fragrance and flavor ingredients. Further, if the cosmetic includes certain ingredients, its labeling or packaging must also contain a specified statement directing consumers to the brand owner's website for information on health impacts of the product\u2019s ingredients. Ingredients that trigger this requirement include those identified on specified lists of harmful or potentially harmful chemicals, such as chemicals identified as carcinogenic by the Environmental Protection Agency. The Food and Drug Administration must maintain a public list of all such ingredients.</p><p>Within one year of enactment, a brand owner must disclose certain information on its website for each of its cosmetic products, including</p><ul><li>a full list of ingredients;</li><li>the functional purpose served by each fragrance or flavor ingredient; and</li><li>if any ingredient is identified on the specified lists of harmful or potentially harmful chemicals, a link to the relevant list.</li></ul>"
        },
        "title": "Cosmetic Hazardous Ingredient Right to Know Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4435.xml",
    "summary": {
      "actionDate": "2025-07-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cosmetic Hazardous Ingredient Right to Know Act of 2025</strong></p><p>This bill requires cosmetic products to be labeled with a full list of their ingredients, including fragrance and flavor ingredients, and imposes other disclosure and labeling requirements related to certain potentially harmful ingredients. A cosmetic product that fails to meet such requirements may not be sold.</p><p>Under current law, a cosmetic product\u2019s packaging must generally include a list of its ingredients, but fragrance or flavor ingredients may be listed as <em>fragrance</em> or <em>flavor</em> in lieu of listing specific ingredient names.</p><p>Within two years of the bill\u2019s enactment, a cosmetic product's labeling or packaging must include a full list of its ingredients, including fragrance and flavor ingredients. Further, if the cosmetic includes certain ingredients, its labeling or packaging must also contain a specified statement directing consumers to the brand owner's website for information on health impacts of the product\u2019s ingredients. Ingredients that trigger this requirement include those identified on specified lists of harmful or potentially harmful chemicals, such as chemicals identified as carcinogenic by the Environmental Protection Agency. The Food and Drug Administration must maintain a public list of all such ingredients.</p><p>Within one year of enactment, a brand owner must disclose certain information on its website for each of its cosmetic products, including</p><ul><li>a full list of ingredients;</li><li>the functional purpose served by each fragrance or flavor ingredient; and</li><li>if any ingredient is identified on the specified lists of harmful or potentially harmful chemicals, a link to the relevant list.</li></ul>",
      "updateDate": "2026-05-26",
      "versionCode": "id119hr4435"
    },
    "title": "Cosmetic Hazardous Ingredient Right to Know Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cosmetic Hazardous Ingredient Right to Know Act of 2025</strong></p><p>This bill requires cosmetic products to be labeled with a full list of their ingredients, including fragrance and flavor ingredients, and imposes other disclosure and labeling requirements related to certain potentially harmful ingredients. A cosmetic product that fails to meet such requirements may not be sold.</p><p>Under current law, a cosmetic product\u2019s packaging must generally include a list of its ingredients, but fragrance or flavor ingredients may be listed as <em>fragrance</em> or <em>flavor</em> in lieu of listing specific ingredient names.</p><p>Within two years of the bill\u2019s enactment, a cosmetic product's labeling or packaging must include a full list of its ingredients, including fragrance and flavor ingredients. Further, if the cosmetic includes certain ingredients, its labeling or packaging must also contain a specified statement directing consumers to the brand owner's website for information on health impacts of the product\u2019s ingredients. Ingredients that trigger this requirement include those identified on specified lists of harmful or potentially harmful chemicals, such as chemicals identified as carcinogenic by the Environmental Protection Agency. The Food and Drug Administration must maintain a public list of all such ingredients.</p><p>Within one year of enactment, a brand owner must disclose certain information on its website for each of its cosmetic products, including</p><ul><li>a full list of ingredients;</li><li>the functional purpose served by each fragrance or flavor ingredient; and</li><li>if any ingredient is identified on the specified lists of harmful or potentially harmful chemicals, a link to the relevant list.</li></ul>",
      "updateDate": "2026-05-26",
      "versionCode": "id119hr4435"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4435ih.xml"
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
      "title": "Cosmetic Hazardous Ingredient Right to Know Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cosmetic Hazardous Ingredient Right to Know Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to increase transparency with respect to cosmetic ingredients, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:33:20Z"
    }
  ]
}
```
