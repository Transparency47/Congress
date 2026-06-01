# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/597?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/597
- Title: PURR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 597
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2025-12-16T09:05:17Z
- Update date including text: 2025-12-16T09:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/597",
    "number": "597",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000809",
        "district": "3",
        "firstName": "Steve",
        "fullName": "Rep. Womack, Steve [R-AR-3]",
        "lastName": "Womack",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "PURR Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-16T09:05:17Z",
    "updateDateIncludingText": "2025-12-16T09:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:02:40Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NE"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "KS"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "IN"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "MO"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "KS"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "KS"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NV"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NC"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NY"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "MO"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "AL"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr597ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 597\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Mr. Womack (for himself, Mr. Valadao , Mr. Smith of Nebraska , Mr. Harder of California , and Mr. Schmidt ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to clarify and update the authority of the Food and Drug Administration to ensure national uniformity in the regulation of the labels, labeling, and advertising of companion animal pet food, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Pet Food Uniform Regulatory Reform Act of 2025 or the PURR Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings.\nSec. 3. Pet food regulation.\nSec. 4. Responsibilities.\nSec. 5. Regulations.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe pet food industry is a growing sector in the United States. Pet food exports have increased by double digits over the last few years.\n**(2)**\nUnited States pet food manufacturers contribute to the national economy by buying nearly $7,000,000,000 worth of agricultural products from farmers, ranchers, and farm-product processors every year.\n**(3)**\nPet ownership has consistently grown in the United States, resulting in an increase in pet food sales and an accompanying increase in the interest by pet owners in how their companion animals\u2019 food is regulated and produced.\n**(4)**\nHistorically, pet food and livestock feed have been regulated under the same framework. However, as pet owners\u2019 relationships with their pets have changed, so too has their understanding of pets\u2019 nutritional needs and preferences. Pet food is specifically formulated to ensure complete nutrition for the long and healthy lives of companion animals. Owning a companion animal provides profound mental, social, and physical health benefits for pet owners such as reduced blood pressure and stress levels, and research indicates that companion animals can play a role in managing depression. Before the enactment of this Act, the regulatory framework that was originally created for livestock feed no longer met the needs of pets or their owners.\n**(5)**\nBefore the enactment of this Act, the regulatory framework governing pet food manufacture and sale, from ingredient approvals to labeling requirements, was multifaceted and wildly inconsistent. Regulatory regimes varied by State, were developed in part by a combination of nongovernmental entities and State government agencies, and were overseen by the Food and Drug Administration\u2019s Center for Veterinary Medicine.\n**(6)**\nCreating a more streamlined Federal regulatory process for new pet food ingredients allows for expedited advances for nutrition, greater innovation, and more functionality in a more predictable regulatory environment.\n**(7)**\nReplacing the patchwork of regulation of pet food with a uniform Federal regulatory framework improves marketplace certainty, allows for more consistent and predictable ingredient review and market introductions, and enhances companion animal nutrition.\n**(8)**\nThe nationwide availability of nutritious, safe, and affordable pet food is substantially improved through a unified comprehensive Federal system of oversight of the manufacture and sale of pet food.\n**(9)**\nThe manufacture of pet food and its marketing and sale is undertaken throughout the United States and its territories and is interstate commerce.\n#### 3. Pet food regulation\nChapter IV of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 341 et seq. ) is amended by adding at the end the following:\n425. Pet food (a) Definitions In this section: (1) The term companion animal means a domesticated canine or feline. (2) The terms generally recognized as safe and GRAS mean generally recognized as safe under section 201(s). (3) The term pet food means any food manufactured and distributed for consumption by companion animals, including treats, nutritional supplements, and pet food ingredients. (4) The term pet food ingredient means an ingredient intended for use in pet food. (5) The term pet food ingredient submission means a submission to the Food and Drug Administration for a pet food ingredient that is a petition under section 409 for any food additive, a petition under section 721 for a color additive, or a GRAS ingredient notification under subpart E of part 570 of subchapter E of chapter I of title 21, Code of Federal Regulations (or successor regulations). (b) Preemption (1) In general No State or a political subdivision of a State may directly or indirectly establish, maintain, implement, or enforce any authority or requirement relating to the labels, labeling, and advertising of pet food. (2) Rule of construction Nothing in this section shall be construed to restrict State food safety oversight activities, including any such activities relating to implementation of the FDA Food Safety Modernization Act, outbreak investigations, surveillance sampling, or investigations of consumer complaints. (c) GRAS ingredients (1) Ingredients deemed GRAS Ingredients that are intended for use in pet food, and are not specifically authorized for such use by the Food and Drug Administration as a food additive, a color additive, or otherwise as of the date of enactment of the PURR Act of 2025 , are deemed to be GRAS if\u2014 (A) such ingredients are identified in chapter 6 of the 2024 edition of the AAFCO Official Publication (or any subsequent amendments thereto or editions thereof) as acceptable for use in pet food (whether specifically for use in dog or cat food, or for use in animal food without restriction to species); and (B) there is no finding by the Food and Drug Administration that such ingredients are not GRAS. (2) Voluntary notification A pet food manufacturer is not required to notify the Food and Drug Administration of GRAS ingredients used in pet food, but may voluntarily notify the Food and Drug Administration of such GRAS ingredients that have not previously been recognized by the Food and Drug Administration as GRAS for use in pet food. (d) Timely review Not later than 90 days after receipt of a pet food ingredient submission, the Secretary shall review such submission and issue an action letter that\u2014 (1) approves such submission or, in the case of a GRAS ingredient notification, does not object to use; or (2) sets forth\u2014 (A) the specific deficiencies in such submission; and (B) where appropriate, the actions necessary\u2014 (i) for such submission to be approved; or (ii) in the case of a GRAS ingredient notification, to resolve any concerns of the Secretary. (e) Ingredients sometimes present (1) In general Pet food shall not be treated as misbranded by reason of stating in the pet food ingredient list on the product label that an ingredient of a type described in paragraph (2) is sometimes, but not always, present in the pet food. (2) Types of ingredients Paragraph (1) applies with respect to the following types of ingredients: (A) Fat or oil ingredients. (B) Flavor ingredients. (C) Grain ingredients (including grain protein ingredients). (3) Language to be used For an ingredient in pet food to be labeled as sometimes present for purposes of paragraph (1), such ingredient shall be identified by\u2014 (A) words such as or , and/or , or contains one or more of the following: ; or (B) other words indicating that the ingredient may not be present. (f) Order of ingredient listing (1) In general Pet food shall be treated as misbranded unless the ingredients required to be declared on the labeling of a pet food are listed by common or usual name in descending order of predominance by weight. (2) Exception If an ingredient in pet food is present in amounts of 2 percent or less by weight, then instead of identifying the ingredient in the order required by paragraph (1), the ingredient may be placed at the end of the pet food ingredient list following an appropriate quantifying statement, such as Contains __ percent or less of ______ or Less than __ percent of ______ , with the blank percentage filled in with a threshold level of 2 percent, or, if desired, 1.5 percent, 1.0 percent, or 0.5 percent, as applicable. (g) Permissible marketing claims Pet food shall not be treated as misbranded by reason of the following claims on labels and labeling and in advertising for pet food, without premarket approval of such claims by the Food and Drug Administration, if truthful, nonmisleading, and adequately substantiated: (1) Claims regarding hairball control. (2) Claims regarding tartar control, plaque removal, and bad breath odor. (3) Claims regarding the ability of pet food to support general urinary tract health. (4) Human grade claims for finished pet food (not for individual ingredients) if all of the following circumstances are met: (A) Every ingredient in the pet food and the finished product is\u2014 (i) stored, handled, processed, and transported in accordance with\u2014 (I) section 117 of title 21, Code of Federal Regulations (or successor regulations); and (II) the laws applicable to food for human consumption, including such laws relating to ingredients, process, or facility type; and (ii) manufactured in accordance with section 507 of title 21, Code of Federal Regulations (or successor regulations). (B) Each facility that manufactures the finished pet food or an ingredient in the finished pet food is registered pursuant to section 415 as a human food facility. (C) The human grade claims clearly indicate that the food is pet food, such as by stating dog food or cat treats . (5) Natural claims if all of the following circumstances are met: (A) Subject to subparagraph (C), the term natural refers to a food or ingredient derived solely from plant, animal, or mined sources\u2014 (i) in its unprocessed state; or (ii) having been subject to physical processing, heat processing, rendering, purification, extraction, hydrolysis, enzymolysis, or fermentation, but not having been produced by or subject to a chemically synthetic process and not containing any additives or processing aids that are chemically synthetic except in amounts as might occur unavoidably in good manufacturing practices. (B) The term natural is only used to reference the product as a whole when all of the ingredients and components of ingredients meet the description in subparagraph (A). (C) If the food or ingredient contains chemically synthesized vitamins, minerals, or other trace nutrients used as ingredients in pet food, a disclaimer\u2014 (i) discloses the addition of such vitamins, minerals, and other trace nutrients by name or category; (ii) is juxtaposed with the term natural ; and (iii) appears with the largest or most prominent use of the term natural on each panel of the label on which the term appears, in the same style and color print and at least one-half the size of the term natural. (D) A disclaimer under subparagraph (C) is not required when the term natural is used in reference to one ingredient and is not referring to the whole product. (h) Guidance on certain topics (1) In general The Secretary shall issue guidance with respect to pet food addressing each of the following topics: (A) Methods for substantiating nutritional adequacy of pet foods. (B) Pet food metabolizable energy protocols. (C) Affidavits for pet food testing protocol completion. (D) Data to support a calorie content claim. (E) Analytical variations (Avs). (F) Recommendations for use of menadione sodium bisulfite complex (MSBC) in animal feed. (2) Initial guidance (A) Timing Not later than 18 months after the date of enactment of the PURR Act of 2025 , the Secretary shall issue initial guidance under this subsection. (B) Basis The initial guidance under subparagraph (A) shall be based on the guidance contained in the 2024 edition of the AAFCO Official Publication . .\n#### 4. Responsibilities\nTitle X of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 391 et seq. ) is amended by adding at the end the following:\n1015. Responsibilities for pet food regulation (a) Delegation of responsibility The Secretary shall delegate to the Director of the Center for Veterinary Medicine responsibility for carrying out section 425 and, as appropriate, other responsibilities and authorities of the Food and Drug Administration with respect to pet food. (b) Duties The responsibilities of the Director of the Center for Veterinary Medicine shall include\u2014 (1) conducting and coordinating science-based reviews of pet food ingredient submissions; (2) submitting an annual report to the Congress on performance metrics, including performance on\u2014 (A) the review of submissions and issuance of action letters under section 425(d); (B) the issuance of initial guidance under section 425(h) and any subsequent revisions to such guidance; and (C) the proposal and finalization of initial regulations under section 5 of the PURR Act of 2025 and any subsequent revisions to such regulations; (3) educating pet owners, veterinarians, and the companion animal industry about pet food; (4) communicating and educating consumers on the safety of pet food; and (5) carrying out research to support and improve policies and regulatory decisions regarding pet food. (c) Definitions In this section, the terms companion animal , pet food , and pet food ingredient submission have the meanings given to those terms in section 425. .\n#### 5. Regulations\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall\u2014\n**(1)**\nnot later than one year after the date of enactment of this Act, issue proposed regulations to implement the amendments made by this Act; and\n**(2)**\nnot later than two years after the date of enactment of this Act, finalize such regulations.\n##### (b) Contents\nThe initial regulations promulgated to implement the amendments made by this Act shall include PF 1 through PF 12 of the Model Regulations for Pet Food and Specialty Pet Food Under the Model Bill in chapter 4 of the 2024 edition of the AAFCO Official Publication .",
      "versionDate": "2025-01-21",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-20T16:36:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr597",
          "measure-number": "597",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr597v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pet Food Uniform Regulatory Reform Act of 2025 or the PURR Act of 2025</strong></p><p>This bill establishes the Food and Drug Administration's Center for Veterinary Medicine (CVM) as the sole regulatory authority over pet food for dogs and cats. It also provides certain flexibilities for pet food manufacturers with respect to the types of ingredients they may use and the associated labeling and marketing\u00a0requirements.</p><p>The bill specifies that, with exceptions for certain existing oversight activities,\u00a0no state or local government may establish, implement, or enforce any authority or requirement relating to pet food marketing or labeling and instead provides for oversight by the CVM.</p><p>The bill requires the CVM to review and act on pet food ingredient submissions within 90 days.\u00a0Additionally, the bill provides a presumption that pet food ingredients are generally recognized as safe (GRAS) if they are recognized as acceptable per the Association of American Feed Control Officials and the\u00a0CVM does not find otherwise. Manufacturers may voluntarily notify the CVM of ingredients that are considered GRAS but that have not yet been specifically recognized as such.</p><p>The bill also allows manufacturers to state, without prior approval, that their products (1) sometimes, but not always, have certain ingredients (e.g., flavors); (2) have certain health benefits (e.g., tartar control); or (3) are human grade or natural, if certain conditions are met.</p><p>\u00a0</p><p>\u00a0</p>"
        },
        "title": "PURR Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr597.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pet Food Uniform Regulatory Reform Act of 2025 or the PURR Act of 2025</strong></p><p>This bill establishes the Food and Drug Administration's Center for Veterinary Medicine (CVM) as the sole regulatory authority over pet food for dogs and cats. It also provides certain flexibilities for pet food manufacturers with respect to the types of ingredients they may use and the associated labeling and marketing\u00a0requirements.</p><p>The bill specifies that, with exceptions for certain existing oversight activities,\u00a0no state or local government may establish, implement, or enforce any authority or requirement relating to pet food marketing or labeling and instead provides for oversight by the CVM.</p><p>The bill requires the CVM to review and act on pet food ingredient submissions within 90 days.\u00a0Additionally, the bill provides a presumption that pet food ingredients are generally recognized as safe (GRAS) if they are recognized as acceptable per the Association of American Feed Control Officials and the\u00a0CVM does not find otherwise. Manufacturers may voluntarily notify the CVM of ingredients that are considered GRAS but that have not yet been specifically recognized as such.</p><p>The bill also allows manufacturers to state, without prior approval, that their products (1) sometimes, but not always, have certain ingredients (e.g., flavors); (2) have certain health benefits (e.g., tartar control); or (3) are human grade or natural, if certain conditions are met.</p><p>\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr597"
    },
    "title": "PURR Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pet Food Uniform Regulatory Reform Act of 2025 or the PURR Act of 2025</strong></p><p>This bill establishes the Food and Drug Administration's Center for Veterinary Medicine (CVM) as the sole regulatory authority over pet food for dogs and cats. It also provides certain flexibilities for pet food manufacturers with respect to the types of ingredients they may use and the associated labeling and marketing\u00a0requirements.</p><p>The bill specifies that, with exceptions for certain existing oversight activities,\u00a0no state or local government may establish, implement, or enforce any authority or requirement relating to pet food marketing or labeling and instead provides for oversight by the CVM.</p><p>The bill requires the CVM to review and act on pet food ingredient submissions within 90 days.\u00a0Additionally, the bill provides a presumption that pet food ingredients are generally recognized as safe (GRAS) if they are recognized as acceptable per the Association of American Feed Control Officials and the\u00a0CVM does not find otherwise. Manufacturers may voluntarily notify the CVM of ingredients that are considered GRAS but that have not yet been specifically recognized as such.</p><p>The bill also allows manufacturers to state, without prior approval, that their products (1) sometimes, but not always, have certain ingredients (e.g., flavors); (2) have certain health benefits (e.g., tartar control); or (3) are human grade or natural, if certain conditions are met.</p><p>\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr597"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr597ih.xml"
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
      "title": "PURR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:49Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PURR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pet Food Uniform Regulatory Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to clarify and update the authority of the Food and Drug Administration to ensure national uniformity in the regulation of the labels, labeling, and advertising of companion animal pet food, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T10:18:20Z"
    }
  ]
}
```
