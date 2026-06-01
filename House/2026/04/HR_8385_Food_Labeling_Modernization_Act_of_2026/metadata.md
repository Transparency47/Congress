# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8385
- Title: Food Labeling Modernization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8385
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-04-27T20:31:28Z
- Update date including text: 2026-04-27T20:31:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8385",
    "number": "8385",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000034",
        "district": "6",
        "firstName": "Frank",
        "fullName": "Rep. Pallone, Frank [D-NJ-6]",
        "lastName": "Pallone",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Food Labeling Modernization Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-27T20:31:28Z",
    "updateDateIncludingText": "2026-04-27T20:31:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:04:30Z",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8385ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8385\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. Pallone (for himself and Ms. DeLauro ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to strengthen requirements related to nutrient information on food labels, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Food Labeling Modernization Act of 2026 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Additional requirements for front-of-package labeling for foods.\nSec.\u20023.\u2002Claims for conventional foods.\nSec.\u20024.\u2002Use of specific terms.\nSec.\u20025.\u2002Format of ingredient list.\nSec.\u20026.\u2002Declaration of phosphorus in the ingredient list.\nSec.\u20027.\u2002Caffeine content on information panel.\nSec.\u20028.\u2002Food allergen labeling.\nSec.\u20029.\u2002Information about major food allergens and gluten-containing grains.\nSec.\u200210.\u2002Submission and availability of food label information.\nSec.\u200211.\u2002Standards of identity.\nSec.\u200212.\u2002Study on fortification of corn masa flour.\nSec.\u200213.\u2002Sugar alcohols and isolated fibers.\nSec.\u200214.\u2002Formatting of information on principal display panels.\nSec.\u200215.\u2002Sale of food online.\nSec.\u200216.\u2002Definitions.\nSec.\u200217.\u2002Regulations; delayed applicability.\n#### 2. Additional requirements for front-of-package labeling for foods\n##### (a) Interpretive nutrition information\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) (1) Except as provided in subparagraphs (3), (4), and (5) of paragraph (q), if it is food (other than a dietary supplement) intended for human consumption and is offered for sale and otherwise required to bear nutrition labeling, unless its principal display panel bears interpretive nutrition information. (2) Final regulations regarding the interpretive nutrition information required under subparagraph (1) shall meet the following criteria: (A) There shall be a standardized symbol system that displays calorie information related to the serving size determined under paragraph (q)(1)(A), and interpretive nutrition information related to the content of added sugars, sodium, saturated fat, and any other nutrients that the Secretary determines the highlighting of which will assist consumers in maintaining healthy dietary practices, including by highlighting products containing high levels of such nutrients. (B) The system shall clearly distinguish between products of greater or lesser nutritional value. (C) The information shall\u2014 (i) appear in a consistent location on the principal display panels across products; (ii) have a prominent design that visually contrasts with existing packaging design; and (iii) be sufficiently large to be easily legible. (3) In promulgating regulations regarding the interpretive nutrition information required under subparagraph (1) and the standardized symbol system required under subparagraph (2)(A), the Secretary shall take into account published reports by the Health and Medicine Division of the National Academy of Sciences, Engineering, and Medicine regarding interpretive nutrition information, and base regulations on the following principles: (A) Consumers should be able to quickly and easily comprehend the meaning of the system as an indicator of a product\u2019s contribution to a healthy diet without requiring specific or sophisticated nutritional knowledge. (B) The nutrition information should be consistent with the Nutrition Facts Panel and with the recommendations of the Dietary Guidelines for Americans. (C) The information should aim to facilitate consumer selection of healthy product options, including among nutritionally at-risk subpopulations. (4) The Secretary should periodically evaluate the standardized symbol system required under subparagraph (2)(A) to assess its effectiveness in facilitating consumer selection of healthy product options and the extent to which manufacturers are offering healthier products as a result of the disclosure. (5) The implementation of this paragraph should be accompanied by appropriate consumer education and promotion campaigns determined by the Secretary. .\n##### (b) Percentage of wheat and grains in grain-Based products, and amount of real fruit, vegetable, and yogurt in products bearing fruit, vegetable, and yogurt claims\nSection 403 of the Federal Food, Drug, and Cosmetic Act, as amended by subsection (a), is further amended by adding at the end the following:\n(aa) If, in the case of food other than a dietary supplement, the principal display panel bears\u2014 (1) the term whole wheat , whole grain , made with whole grain , or multigrain ; (2) a declaration of the whole grain content by weight; (3) the term wheat on a wheat bread, pasta, or similar product that is typically made from wheat; or (4) any similar descriptive phrases, terms, or representations suggesting the product contains whole grains, unless the amounts of whole grains and refined grains, expressed as a percentage of total grains, are conspicuously disclosed in immediate proximity to the most prominent descriptive phrase, term, or representation using a font color and formatting of equivalent prominence to the descriptive phrase, term, or representation with respect to whole grain content, or unless 100 percent of the grains in the food are whole grains. (bb) (1) If, in the case of food other than a dietary supplement, the principal display panel bears\u2014 (A) the term fruit , fruity , froot , frooty , or fruit-flavored ; (B) representations, depictions, or images of such ingredients; or (C) any similar descriptive phrases, terms, or representations suggesting the product contains fruit or any specific type of fruit, unless the quantity per serving and form of fruit, including only the nutrient-dense forms, is declared on the principal display panel in a common household measure that is appropriate to the food, conspicuously, and in immediate proximity to the most prominent term, representation, depiction, or image of fruit. (2) The Secretary shall by regulation establish quantities below which such declaration shall state that the food does not contain any full serving of fruit. (3) In this paragraph, the term nutrient-dense , with respect to the form of an ingredient derived from a fruit, means the whole, cut, dried, pulp, puree, 100-percent juice, or fully reconstituted concentrate form, and not concentrates, powders, and other ingredients that are not whole, cut, dried, pulp, puree, 100-percent juice, or fully reconstituted concentrates. (cc) (1) If, in the case of food other than a dietary supplement, the principal display panel bears\u2014 (A) the term vegetable or veggie ; (B) representations, depictions, or images of such ingredients; or (C) any similar descriptive phrases, terms, or representations suggesting the product contains vegetables or any specific type of vegetable, unless the quantity per serving and form of vegetable, including only the nutrient-dense form, is declared on the principal display panel in a common household measure that is appropriate to the food, conspicuously, and in immediate proximity to the most prominent term, representation, depiction, or image of vegetable. (2) The Secretary shall by regulation establish quantities below which such declaration shall state that the food does not contain any full serving of vegetable. (3) In this paragraph, the term nutrient-dense , with respect to the form of an ingredient derived from a vegetable, means the whole, cut, dried, pulp, puree, 100-percent juice, or fully reconstituted concentrate form, and not concentrates, powders, and other ingredients that are not whole, cut, dried, pulp, puree, 100-percent juice, or fully reconstituted concentrates. (dd) (1) If, in the case of food other than a dietary supplement, the principal display panel bears the term yogurt , unless\u2014 (A) the quantity per serving of yogurt is declared on the principal display panel in a common household measure that is appropriate to the food, conspicuously, in immediate proximity to the term; or (B) the first ingredient is cultured milk, cultured cream, cultured partially skimmed milk, or cultured skim milk. (2) The Secretary shall by regulation establish quantities below which such declaration shall state that the food does not contain any full serving of yogurt. .\n##### (c) Report on sweeteners\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this Act as the Secretary ) shall submit to Congress a report that\u2014\n**(A)**\nevaluates whether\u2014\n**(i)**\nmanufacturers have increased the use of low- and no-calorie sweeteners; and\n**(ii)**\nthe use of low- and no-calorie sweeteners has risen to a level that could result in negative health consequences; and\n**(B)**\ndescribes actions that will be taken by the Secretary to address any increased use of low- and no-calorie sweeteners.\n**(2) Monitoring**\nOn completion of the report described in paragraph (1), the Secretary shall\u2014\n**(A)**\nperiodically monitor for increased use of low- and no-calorie sweeteners; and\n**(B)**\ntake action to address the use of low- and no-calorie sweeteners if the use has risen to a level that could result in negative health consequences.\n##### (d) Construction\nNothing in this section, including any amendment made by this section, shall be construed as\u2014\n**(1)**\naffecting any requirement in regulation in effect as of the date of the enactment of this Act with respect to matters that are required to be stated on the principal display panel of a package or container of food that is not required by an amendment made by this section; or\n**(2)**\nrestricting the authority of the Secretary of Health and Human Services to require additional information be disclosed on such a principal display panel.\n#### 3. Claims for conventional foods\n##### (a) Health-Related claims\n**(1) In general**\nSection 403(r)(1)(B) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(r)(1)(B) ) is amended by inserting after health-related condition the following: , describes the effect that a nutrient may have on the structure or function of the human body, characterizes the documented mechanism by which that nutrient acts to maintain such structure or function, or describes general well-being from consumption of that nutrient, .\n**(2) Substantiation of claim**\nSection 403(r) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(r) ) is amended\u2014\n**(A)**\nby redesignating subparagraph (7) as subparagraph (8); and\n**(B)**\nby inserting after subparagraph (6) the following:\n(7) If the Secretary requests that a claim under subparagraph (1)(B) for food (other than a dietary supplement) be substantiated, then not later than 90 days after the date on which the Secretary makes such request, the manufacturer shall provide to the Secretary all documentation in the manufacturer\u2019s possession relating to the claim. .\n**(3) Incompatible with maintaining healthy dietary practices**\nSection 403(r)(3)(A)(ii) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(r)(2)(B) ) is amended by striking increases to persons in the general population the risk of a disease or health-related condition which is diet related and inserting may not be compatible with maintaining healthy dietary practices .\n##### (b) Nutrient content claims\n**(1) In general**\nSection 403(r)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(r)(2) ) is amended by striking clause (B) and inserting the following:\n(B) If a claim described in subparagraph (1)(A) is made with respect to a nutrient in a food and the Secretary makes a determination that the food contains a nutrient at a level that may not be compatible with maintaining healthy dietary practices, the label or labeling of such food shall contain, prominently and in immediate proximity to such claim, a statement which indicates the food is high in such nutrient. .\n**(2) Revisions to regulations**\nIn promulgating the regulations required by section 17, the Secretary of Health and Human Services shall revise section 101.13(h) of title 21, Code of Federal Regulations, by\u2014\n**(A)**\nupdating the level of sodium requiring disclosure to align with the Daily Reference Value for sodium established in the final rule entitled Food Labeling: Revision of the Nutrition and Supplement Facts Labels published by the Food and Drug Administration on May 27, 2016 (81 Fed. Reg. 33741);\n**(B)**\nincluding a level of added sugars requiring disclosure based on the Daily Reference Value for added sugars established in the final rule described in subparagraph (A);\n**(C)**\neliminating the requirement that meal products containing more than 26 grams of fat and main dish products containing 19.5 grams of fat per labeled serving must disclose that fat is present in the food; and\n**(D)**\nauthorizing the use of express and implied low added sugar claims on products containing 3 grams of added sugars or less per reference amount customarily consumed (or per 50 grams if the reference amount customarily consumed is 30 grams or less or 2 tablespoons or less).\n##### (c) Trans fats\nSection 403(r)(2)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(r)(2)(A) ) is amended\u2014\n**(1)**\nby redesignating subclauses (v) and (vi) as subclauses (vi) and (vii), respectively; and\n**(2)**\nby inserting after subclause (iv) the following new subclause:\n(v) may not be made with respect to the level of trans fats in the food, except on the Nutrition Facts Panel, unless the food contains less than one gram of saturated fat per serving or, if the food contains more than one gram of saturated fat per serving, unless the label or labeling of the food discloses the level of saturated fat in the food in immediate proximity to such claim and with appropriate prominence which shall be no less than one-half the size of the claim with respect to the level of trans fats, .\n##### (d) Added sugars\nNot more than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services shall promulgate a final rule revising section 101.14 of title 21, Code of Federal Regulations, to include a disqualifying nutrient level for added sugars.\n#### 4. Use of specific terms\n##### (a) Use of the term natural\n**(1) In general**\nIn promulgating the regulations required by section 17, the Secretary of Health and Human Services shall include regulations\u2014\n**(A)**\nrelating to use of the term natural on the labeling of food (other than a dietary supplement);\n**(B)**\nspecifically addressing the use of such term on the principal display panel and the information panel; and\n**(C)**\nrequiring that any such use includes a prominent disclosure explaining what the term natural does and does not mean in terms of ingredients and manufacturing processes.\n**(2) Definition**\nThe regulations promulgated pursuant to paragraph (1) shall define the term natural \u2014\n**(A)**\nto exclude, at a minimum, the use of any artificial food or ingredient (including any artificial flavor or added color); and\n**(B)**\nbased on data, including data on consumers\u2019 understanding of the term as used in connection with food.\n**(3) Process**\nIn promulgating the regulations required by paragraph (1), the Secretary of Health and Human Services shall\u2014\n**(A)**\nconduct consumer surveys and studies and issue a timely call for relevant public submissions regarding relevant consumer research, including with respect to consumer understanding of the term natural in relation to the term organic ; and\n**(B)**\nfully consider the results of such surveys and studies, as well as such public submissions.\n##### (b) Use of term healthy\n**(1) Added sugars and whole grains**\n**(A) In general**\nIn promulgating the regulations required by section 17, the Secretary of Health and Human Services shall include regulations to revise the regulations under the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) relating to the use of the term healthy on the labeling of a food (other than a dietary supplement) to take into account the extent to which such food contains added sugars or whole grains.\n**(B) Requirement**\nIn making the revisions required by subparagraph (A) in the case of a food (other than a dietary supplement) that contains grains, the Secretary of Health and Human Services shall not consider the food to be healthy unless 100 percent of the grains are whole grains.\n**(2) Sodium**\nIn promulgating the regulations required by section 17, the Secretary of Health and Human Services shall revise the regulations under the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) relating to the use of the term healthy on the labeling of a food (other than a dietary supplement) to align labeling requirements related to sodium with the daily value for sodium in the most recent Dietary Guidelines for Americans.\n**(3) Principles for implementing regulations**\nIn promulgating regulations under paragraphs (1) and (2) regarding the use of the term healthy , the Secretary of Health and Human Services shall\u2014\n**(A)**\nconsider both food and nutrient criteria; and\n**(B)**\nif requiring food labeled as healthy to contain healthful ingredients\u2014\n**(i)**\nconsider only ingredients that make up the core of a healthy eating pattern; and\n**(ii)**\nconsider these ingredients only in their nutrient-dense forms (as such term in defined in paragraphs (bb) and (cc) of section 403 of the Federal Food, Drug, and Cosmetic Act, as added by section 2(b) of this Act).\n#### 5. Format of ingredient list\n##### (a) In general\nIn promulgating the regulations required by section 17, the Secretary of Health and Human Services shall include requirements for the format of the information required under section 403(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(i) )\u2014\n**(1)**\nfor the purpose of improving the readability of such information on the label of the food (other than a dietary supplement); and\n**(2)**\nthat are, as determined by the Secretary, necessary to assist consumers in maintaining healthy dietary practices.\n##### (b) Format requirements\nThe format requirements described in subsection (a) shall include requirements for font size, uppercase and lowercase characters, serif and noncondensed font types, high-contrast between text and background, and bullet points between adjacent ingredients with appropriate exemptions for small packages or other considerations.\n##### (c) Enforcement of ingredient list\nNot later than 2 years after the enactment of this Act, and every 2 years thereafter, the Secretary of Health and Human Services shall submit to Congress a report on the Secretary\u2019s enforcement of\u2014\n**(1)**\nsection 403(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(i) ), including with respect to the regulations described in subsection (a); and\n**(2)**\nregulations of the Food and Drug Administration on labeling of ingredients in section 101.4 of title 21, Code of Federal Regulations.\n#### 6. Declaration of phosphorus in the ingredient list\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ), as amended by section 2(b), is further amended by adding at the end the following:\n(ff) If it is a food intended for human consumption that is offered for sale and contains phosphorus, unless\u2014 (1) the phrase contains phosphorus , along with the quantity of phosphorus in the product, reported in milligrams per serving, is printed immediately after or is adjacent to the list of ingredients required under paragraphs (g) and (i), in a type size no smaller than the type size used in the list of ingredients; or (2) the quantity of phosphorus contained in the product, in milligrams, is reported in the Nutrition Facts Panel. .\n#### 7. Caffeine content on information panel\nSection 403(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(i) ) is amended\u2014\n**(1)**\nby striking and (2) and inserting (2) ;\n**(2)**\nby striking and if the food purports and inserting , (3) if the food purports ; and\n**(3)**\nby inserting , and (4) if the food is food other than a dietary supplement and contains at least 10 milligrams of caffeine from all sources per serving, a statement (with appropriate prominence near the statement of ingredients required by this paragraph) of the number of milligrams of caffeine contained in one serving of the food and the size of such serving after vegetable juice contained in the food .\n#### 8. Food allergen labeling\n##### (a) In general\nSection 201(qq) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(qq) ) is amended by adding at the end the following:\n(3) Any other food ingredient that the Secretary determines by regulation to be a major food allergen, based on the prevalence and severity of allergic reactions to the food ingredient. .\n##### (b) Update to Compliance Policy Guide\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services shall update the Food and Drug Administration\u2019s Compliance Policy Guide, section 555.250, to conform with applicable laws related to major food allergens and gluten-containing grains, including requirements under sections 9 and 10 of this Act.\n#### 9. Information about major food allergens and gluten-containing grains\n##### (a) In general\nSection 403(w) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(w) ) is amended\u2014\n**(1)**\nin subparagraph (1)\u2014\n**(A)**\nin the matter preceding clause (A), by inserting or gluten-containing grain after major food allergen ;\n**(B)**\nin clause (A)\u2014\n**(i)**\nby inserting , or the gluten-containing grain is derived after is derived ; and\n**(ii)**\nby striking is printed immediately after or is adjacent to the list of ingredients (in a type size no smaller than the type size used in the list of ingredients) required under subsections (g) and (i) and inserting is printed as specified in subparagraph (8) ; and\n**(C)**\nin clause (B)\u2014\n**(i)**\nin the matter preceding subclause (i)\u2014\n**(I)**\nby inserting or gluten-containing grain after of the major food allergen ;\n**(II)**\nby striking in the list of ingredients required under subsections (g) and (i) and inserting as so printed ; and\n**(III)**\nby inserting or the gluten-containing grain is derived, after is derived, ;\n**(ii)**\nin subclause (i), by inserting , or the gluten-containing grain is derived after is derived ; and\n**(iii)**\nin subclause (ii)\u2014\n**(I)**\nby inserting , or the gluten-containing grain is derived, after is derived ; and\n**(II)**\nby striking not a major food allergen under section 201(qq)(2)(A) or (B) and inserting the following:\nnot\u2014 (I) a major food allergen under section 201(qq)(2)(A) or (B); or (II) a gluten-containing grain. ;\n**(2)**\nin subparagraph (3), by striking The information and inserting Subject to subparagraph (8)(B), the information ;\n**(3)**\nin subparagraph (4), by inserting or gluten-containing grain after major food allergen ;\n**(4)**\nin subparagraph (7)\u2014\n**(A)**\nin clause (A)\u2014\n**(i)**\nby striking paragraph (6) and inserting subparagraph (6) ; and\n**(ii)**\nby striking allergen labeling requirements of this subsection and inserting allergen and gluten-containing grain labeling requirements of this paragraph ; and\n**(B)**\nin clause (B), by inserting or gluten-containing grain after major food allergen ; and\n**(5)**\nby adding at the end the following:\n(8) The information required by subparagraph (1) to be conveyed to the consumer shall be\u2014 (A) printed immediately after or adjacent to the list of ingredients (in a type size no smaller than the type size used in the list of ingredients) required under paragraphs (g) and (i); or (B) in the case of a nonpackaged food being offered for sale at retail, and not subject to the requirements of paragraphs (g) and (i), placed on a sign adjacent to the food (in a type size no smaller than the name of the food item). .\n##### (b) Hazard analysis and preventive controls\nSection 418 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 350g ) is amended\u2014\n**(1)**\nin subsection (b)(1)(A), by inserting gluten-containing grains, after allergens, ; and\n**(2)**\nin subsection (o)(3)(D), by inserting and gluten-containing grain after allergen .\n##### (c) Inspections relating to food allergens\nSection 205 of the Food Allergen Labeling and Consumer Protection Act of 2004 ( 21 U.S.C. 374a ) is amended by inserting and gluten-containing grains after allergens each place it appears.\n#### 10. Submission and availability of food label information\nThe Federal Food, Drug, and Cosmetic Act is amended by inserting after section 403C of such Act ( 21 U.S.C. 343\u20133 ) the following:\n403D. Submission and availability of food label information (a) Submissions (1) Requirement The Secretary shall require the manufacturer or importer of any food that is introduced or delivered for introduction into interstate commerce in package form to submit to the Secretary all information to be included in the label of the food, including\u2014 (A) the nutrition facts panel; (B) the ingredients list; (C) an image of the principal display panel; (D) major allergens and gluten-containing grains; (E) claims under section 403(r)(1)(A) (commonly known as nutrient-content claims ); (F) claims under section 403(r)(1)(B) (commonly known as health-related claims ); and (G) other relevant information required by law to be published in the labeling of the food. (2) Updates The Secretary shall require the manufacturer or importer of food to update or supplement the information submitted under paragraph (1) with respect to the food in order to keep the information up-to-date and complete. (3) Civil penalty Whoever knowingly violates paragraph (1) with respect to any food shall be liable to the United States for a civil penalty in an amount not to exceed $10,000 for each day on which such violation continues with respect to such food. (b) Public database The Secretary shall establish and maintain a public database containing the information submitted under this section that\u2014 (1) is available to the public through the website of the Food and Drug Administration; and (2) allows members of the public to easily search and sort information. .\n#### 11. Standards of identity\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services shall\u2014\n**(1)**\nreview standards of identity prescribed by regulation which require foods to contain\u2014\n**(A)**\nminimum levels of nutrients that the Secretary determines are strongly associated with public health concerns; or\n**(B)**\nminimum levels of ingredients containing high levels of such nutrients; and\n**(2)**\nreport to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate on the findings of such review.\n##### (b) Amendments\nIn promulgating the regulations required by section 17, the Secretary of Health and Human Services shall amend standards of identity regulations to\u2014\n**(1)**\nprovide for the use of salt substitutes where appropriate; and\n**(2)**\nrequire that yogurt, lowfat yogurt, and nonfat yogurt contain a minimum level of live and active cultures per gram.\n#### 12. Study on fortification of corn masa flour\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services shall submit a report to Congress on the effect of the final rule titled Food Additives Permitted for Direct Addition to Food for Human Consumption; Folic Acid published by the Food and Drug Administration on April 15, 2016 (81 Fed. Reg. 22176), on folic acid intake in the United States population by race and ethnicity, comparing actual exposure with modeled exposure estimates from the final rule.\n#### 13. Sugar alcohols and isolated fibers\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ), as amended by section 6, is further amended by adding at the end the following:\n(gg) If it is a food intended for human consumption that is offered for sale and contains allulose, polydextrose, sugar alcohols, or isolated fibers, unless such fact is prominently stated on the principal display panel of the packaging of the food. The Secretary shall by regulation establish quantities above which such labeling shall include a warning that the food contains a level of allulose, polydextrose, sugar alcohols, or isolated fibers per serving determined by the Secretary to cause deleterious health effects. .\n#### 14. Formatting of information on principal display panels\nThe Secretary of Health and Human Services shall\u2014\n**(1)**\nnot later than 2 years after the date of enactment of this Act, conduct a study on the legibility of food labeling to determine updated recommendations for text size and color contrast that make food labeling information visually accessible to the majority of consumers;\n**(2)**\nnot later than 1 year after the completion of the study under paragraph (1), issue proposed regulations revising section 101.2(c) of title 21, Code of Federal Regulations, to\u2014\n**(A)**\nset the scale of text size, taking into consideration the results of the study conducted under paragraph (1); and\n**(B)**\nestablish new requirements for text and background color contrast, taking into consideration the results of the study conducted under paragraph (1); and\n**(3)**\nnot later than 2 years after the completion of the study under paragraph (1), finalize such proposed regulations.\n#### 15. Sale of food online\n##### (a) In general\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ), as amended by section 13, is further amended by adding at the end the following:\n(hh) (1) If it is a food offered for sale online or by other remote written electronic means, unless all information required to appear on the label or labeling is available to consumers at the point of selection prior to purchasing the food. (2) The Secretary shall by regulation specify the format and manner in which the information required under subparagraph (1) is to be made available online to consumers. Such regulations shall include\u2014 (A) a requirement that the nutrition information shall be in the same format as the nutrition information required under paragraph (q); and (B) a requirement that the nutrition information required under paragraph (q), the ingredient information required under paragraphs (g) and (i), and the allergen information required under paragraph (w) shall\u2014 (i) appear on the first product information page that appears for the product on a mobile device, internet website, or other landing page; (ii) appear prominently and conspicuously (as compared with other words, statements, or designs on the mobile device, internet website, or other landing page) so as to render the information likely to be read and understood by the ordinary individual under customary conditions of online purchase; and (iii) not contain intervening marketing information. .\n##### (b) Prohibited acts\n**(1) In general**\nSection 301 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331 ) is amended by adding at the end the following:\n(jjj) In the case of a person providing a platform for, or otherwise assisting, the sale of food online or by other remote written electronic means, the prevention by the person of the provision to consumers of information required under section 403(z) or the charging by such person of an additional fee for the provision of such information. .\n**(2) Penalties**\nSection 303 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 333 ) is amended by adding at the end the following:\n(h) (1) Notwithstanding subsection (a), any person who violates section 301(jjj) shall be liable to the United States for a civil penalty in an amount not to exceed $10,000 for each such violation, and not to exceed $1,000,000 for all such violations adjudicated in a single proceeding. (2) The Secretary shall provide the person subject to a penalty under paragraph (1) with a warning and opportunity to correct the violation prior to issuing the first civil penalty under that paragraph. (3) In determining the amount of a civil penalty under paragraph (1), the Secretary shall take into consideration whether the person is making efforts to correct the violation for which such person is subject to such civil penalty. (4) No person shall be subject to criminal penalties as described in subsection (a) for a violation of section 301(jjj). .\n##### (c) Civil monetary penalties for violation of requirements for sale of food online\nSection 303 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 333 ), as amended by subsection (b)(2), is further amended by adding at the end the following:\n(i) (1) Notwithstanding subsection (a), any person who introduces into interstate commerce, delivers for introduction into interstate commerce, receives in interstate commerce, or manufactures a food that is misbranded as described in section 403(z), or misbrands the food as described in that section, shall be liable to the United States for a civil penalty in an amount not to exceed $10,000 for each such violation, and not to exceed $1,000,000 for all such violations adjudicated in a single proceeding. (2) The Secretary shall provide the person subject to a penalty under paragraph (1) with a warning and opportunity to correct the violation prior to issuing the first civil penalty under that paragraph. (3) In determining the amount of a civil penalty under paragraph (1), the Secretary shall take into consideration whether the person is making efforts to correct the violation for which such person is subject to such civil penalty. (4) No person shall be subject to criminal penalties as described in subsection (a) for a violation described in paragraph (1). .\n#### 16. Definitions\n##### (a) Definitions applicable in this Act\nIn this Act, the terms food and dietary supplement have the meanings given to such terms in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n##### (b) Definitions applicable in the Federal Food, Drug, and Cosmetic Act\nSection 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ) is amended by adding at the end the following:\n(tt) The term artificial , with respect to food or any ingredient of food, means\u2014 (1) food or an ingredient that is synthetically produced whether or not it has the same chemical structure as a naturally occurring food or ingredient; (2) food or an ingredient that has undergone chemical changes through the introduction of synthetic chemicals or processing aids (such as corn syrup, high-fructose corn syrup, high-maltose corn syrup, maltodextrin, chemically modified starch, and cocoa processed with alkali), excluding\u2014 (A) food or an ingredient that has undergone traditional processes used to make food edible, to preserve food, or to make food safe for human consumption (such as smoking, roasting, freezing, drying, and fermenting processes); or (B) food or an ingredient that has undergone traditional physical processes that do not fundamentally alter the raw product or which only separate a whole intact food into component parts (such as grinding grains, separating eggs into albumen and yolk, or pressing fruits to produce juice); or (3) any food or ingredient that the Secretary specifies by regulation to be artificial for purposes of this Act. (uu) The term synthetic , with respect to a substance in food or any ingredient of food, means a substance that is formulated or manufactured by a chemical process or by a process that chemically changes a substance extracted from a naturally occurring plant, animal, or mineral source, except that such term does not apply to a substance created by naturally occurring biological processes. (vv) The term gluten-containing grains means any one of the following grains (or any crossbred hybrid thereof): (1) Wheat, including any species belonging to the genus Triticum. (2) Rye, including any species belonging to the genus Secale. (3) Barley, including any species belonging to the genus Hordeum. (ww) The term gluten means the proteins that\u2014 (1) naturally occur in a gluten-containing grain; and (2) may cause adverse health effects in persons with celiac disease. (xx) The term online means on or by any system of data communication and transmission, such as the internet. (yy) The term online point of selection means any space in which consumers are allowed to purchase food online, including websites, e-commerce platforms, web applications, and mobile applications. .\n#### 17. Regulations; delayed applicability\n##### (a) Regulations\n**(1) Proposed regulations**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall issue proposed regulations to carry out sections 2, 3, 4, 5(a), 6, 7, 9, 10, 11, 13, 15, and 16(b) and the amendments made by such sections.\n**(2) Final regulations**\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall finalize the regulations proposed pursuant to paragraph (1).\n**(3) Failure to issue final regulation**\nIf the Secretary of Health and Human Services does not issue a final regulation as required by paragraph (2) by the deadline specified in such paragraph, the corresponding proposed regulation shall become final on such deadline.\n##### (b) Delayed applicability\nThe amendments made by sections 2, 3, 4, 5(a), 6, 7, 9, 10, 11, 13, 15, and 16(b) apply beginning on the date that is 3 years after the date of enactment of this Act.",
      "versionDate": "2026-04-20",
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
        "updateDate": "2026-04-27T20:31:28Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8385ih.xml"
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
      "title": "Food Labeling Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Food Labeling Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to strengthen requirements related to nutrient information on food labels, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:18:24Z"
    }
  ]
}
```
