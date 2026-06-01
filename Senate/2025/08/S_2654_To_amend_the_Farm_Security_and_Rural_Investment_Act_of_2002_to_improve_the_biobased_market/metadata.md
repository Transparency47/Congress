# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2654?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2654
- Title: Biomanufacturing and Jobs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2654
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-12-05T22:01:31Z
- Update date including text: 2025-12-05T22:01:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2654",
    "number": "2654",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001208",
        "district": "",
        "firstName": "Elissa",
        "fullName": "Sen. Slotkin, Elissa [D-MI]",
        "lastName": "Slotkin",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Biomanufacturing and Jobs Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:01:31Z",
    "updateDateIncludingText": "2025-12-05T22:01:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T20:04:34Z",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "IA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NE"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2654is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2654\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Ms. Slotkin (for herself, Ms. Ernst , Mr. Ricketts , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Farm Security and Rural Investment Act of 2002 to improve the biobased markets program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Biomanufacturing and Jobs Act of 2025 .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nbiobased products provide additional markets for farm commodities, reducing the reliance of the United States on petroleum and increasing the use of renewable agricultural resources while driving rural economic development and growth;\n**(2)**\nUnited States farmers produce feedstock used to produce a variety of biobased products, including personal care products, industrial paints solvents, construction materials, and apparels and textiles;\n**(3)**\nthe BioPreferred Program of the Department of Agriculture is designed to increase the purchase and use of biobased products through a mandatory Federal purchasing initiative and a voluntary labeling initiative, thereby supporting additional markets for agricultural commodities and rural economic development;\n**(4)**\naccording to the Department of Agriculture, there are approximately 15,000 biobased products participating in the BioPreferred Program, with approximately 2,600 biobased products authorized to display the USDA Certified Biobased Product label under the voluntary labeling initiative;\n**(5)**\nthere were 3,940,000 people employed in the United States biobased products industry in 2021;\n**(6)**\nthe value-added contribution of the biobased products industry to the economy grew even through the COVID\u201319 pandemic, from $470,000,000,000 in 2017 to $489,000,000,000 in 2021; and\n**(7)**\neach job in the biobased products industry supports an estimated 1.4 jobs in other sectors of the economy.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto recognize the value that biobased products bring to agriculture in the United States;\n**(2)**\nto support domestic manufacturing of biobased products made from agricultural commodities, including corn and soybeans;\n**(3)**\nto expand the role of the Department of Agriculture in the promotion of biobased products;\n**(4)**\nto build on procurement programs administered by the Department of Agriculture to increase Federal purchasing of biobased products;\n**(5)**\nto strengthen domestic manufacturing of biobased products; and\n**(6)**\nto make a national commitment to the rural and agricultural economies of the United States.\n#### 3. Definitions\nSection 9001 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8101 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (4) through (6), (7) through (12), and (13) through (17) as paragraphs (7) through (9), (11) through (16), and (18) through (22), respectively;\n**(2)**\nby inserting after paragraph (3) the following:\n(4) Bio-attributed plastic The term bio-attributed plastic means a plastic product that is a bioproduct and not a biobased product. (5) Bio-attributed product (A) In general The term bio-attributed product means a product that is determined by the Secretary to be a commercial or industrial product (other than food or feed) that is produced from or composed of (in whole or in part) biological products, including a material or compound subsequently used to make a more complex compound or product. (B) Biological product For purposes of subparagraph (A), the term biological product includes a product that contains, in whole or in part, renewable agricultural material, a plant-based product, animal-derived material, or forestry material. (6) Biobased plastic The term biobased plastic means a plastic product that is a biobased product. ;\n**(3)**\nby inserting after paragraph (9) (as so redesignated) the following:\n(10) Bioproduct The term bioproduct means\u2014 (A) a biobased product; or (B) a bio-attributed product. ; and\n**(4)**\nby inserting after paragraph (16) (as so redesignated) the following:\n(17) Plant-based product The term plant-based product means a product (other than food or feed) that\u2014 (A) is composed, in whole or in significant part, of materials produced by plants or other organisms through photosynthesis; and (B) is a biobased product. .\n#### 4. Biobased markets program\nSection 9002 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8102 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)(i)\u2014\n**(I)**\nin subclause (II)(bb), by striking and at the end;\n**(II)**\nin subclause (III), by striking the period at the end and inserting ; and ; and\n**(III)**\nby adding at the end the following:\n(IV) on an annual basis, update the procurement requirement described in subclause (III) by increasing the number of biobased-only contracts or the volume purchased under those contracts from the previous year. ;\n**(ii)**\nin subparagraph (B), by striking clause (iii) and inserting the following:\n(iii) are available only at a price that exceeds the price premium established under paragraph (3)(B)(viii) for those items. ; and\n**(iii)**\nby adding at the end the following:\n(G) Guidance The Secretary, in coordination with the Office of Federal Procurement Policy, shall issue guidance to procuring agencies to consider product lifespan, savings, and efficacy when making procurement decisions under this subsection. ;\n**(B)**\nin paragraph (3)(B)\u2014\n**(i)**\nin clause (vii), by striking and at the end;\n**(ii)**\nby redesignating clause (viii) as clause (ix); and\n**(iii)**\nby inserting after clause (vii) the following:\n(viii) establish price premiums for different types of biobased products; and ; and\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking clause (ii); and\n**(II)**\nby redesignating clauses (iii) and (iv) as clauses (ii) and (iii), respectively;\n**(ii)**\nin subparagraph (B)(i)\u2014\n**(I)**\nin the matter preceding subclause (I)\u2014\n**(aa)**\nby inserting and the Secretary after Policy ; and\n**(bb)**\nby striking information concerning\u2014 and inserting a report that describes, for the year covered by the report\u2014 ;\n**(II)**\nin subclause (I), by inserting , including the actions taken by the procuring agency to establish and implement the biobased procurement program of the procuring agency under that paragraph before the semicolon;\n**(III)**\nin subclause (IV), by striking and at the end;\n**(IV)**\nin subclause (V), by striking and at the end; and\n**(V)**\nby adding at the end the following:\n(VI) (aa) the specific categories of biobased products that are unavailable to meet the procurement needs of the procuring agency; and (bb) the desired performance standards and other relevant specifications for those products; and (VII) if applicable, the procurement requirement or updated procurement requirement established under paragraph (2)(A)(i) that the procuring agency failed to meet and reasons for the failure; and ; and\n**(iii)**\nby adding at the end the following:\n(D) Verification The Office of Federal Procurement Policy, in consultation with the Secretary, shall\u2014 (i) annually collect the information required to be reported under subparagraph (B) and make the information publicly available; and (ii) annually verify, using the information collected under subparagraph (B), that each procuring agency under paragraph (2)(A)(i), as applicable, has established a procurement program in accordance with subclause (I) of that paragraph. (E) Training (i) In general Not later than 2 years after the date of enactment of this subparagraph, each procuring agency shall have completed training on biobased product purchasing for the appropriate staff of the procuring agency, including contracting officers, purchase card managers, and purchase card holders. (ii) Materials The Office of Federal Procurement Policy, in cooperation with the Secretary, shall provide training materials for procuring agencies conducting training pursuant to clause (i). (F) Federal catalog updates Not later than 2 years after the date of the enactment of this subparagraph, the Administrator for Federal Procurement Policy, in cooperation with the Secretary, shall\u2014 (i) direct the Administrator of General Services to update the Federal Procurement Data System described in section 1122(a)(4) of title 41, United States Code, or any successor system, to include biobased product designations; (ii) direct that the System for Award Management collect biobased product purchasing data; (iii) direct that Federal online procurement systems, including GSA Advantage! and FedMall, include designations for products that meet the guidelines under paragraph (3); (iv) require, to the maximum extent practicable, that Federal online procurement systems, including GSA Advantage! and FedMall, use North American Industry Classification System codes, North American Product Classification System-based product codes, and other product codes, as determined in consultation with the Secretary, when identifying products that meet the guidelines under paragraph (3); and (v) require agencies with online Federal sales platforms to include reporting of these purchases in their reporting on products that meet the guidelines under paragraph (3). ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (3), by adding at the end the following:\n(C) Unauthorized use Not later than 120 days after the date of enactment of this subparagraph, the Secretary shall, in coordination with the Inspector General of the Department of Agriculture, notify the public of how to report an instance of unauthorized use of the label described in paragraph (1). ; and\n**(B)**\nby adding at the end the following:\n(5) Public marketing and education The Secretary may conduct outreach to educate the public on and promote the use of biobased products, including by\u2014 (A) conducting outreach to small businesses producing biobased products that seek a label under this subsection; (B) providing information about biobased product procurement preferences to State procurement agencies; and (C) establishing public-private partnerships to further increase awareness and use of biobased products. (6) Acceptance and use of contributions (A) In general The Secretary may establish an account to accept contributions of non-Federal funds to carry out public marketing and education under paragraph (5). (B) Deposit and use of contributions Contributions of non-Federal funds received to carry out the activities under paragraph (5) shall\u2014 (i) be deposited into the account established under this paragraph for those activities; (ii) be available to and subject to the control of the Secretary, without further appropriation and until expended, to carry out those activities; and (iii) supplement any funding made available under subsection (k) and allocated by the Secretary for those activities. (7) Report Not later than December 31, 2025, and annually thereafter, the Secretary shall make publicly available on the website of the Department of Agriculture and submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that includes\u2014 (A) a list of the biobased products that were authorized to use the label described in paragraph (1) during the preceding fiscal year; (B) a description of the audit and compliance activities conducted under paragraph (3)(B) during the preceding fiscal year, including any findings of noncompliance and any actions taken by the Secretary to address the noncompliance; (C) (i) a description of the public marketing and education conducted by the Secretary under paragraph (5); and (ii) a plan for conducting public marketing and education under that paragraph for the following two fiscal years that is designed to increase the use of the label described in paragraph (1) and the purchase of biobased products; and (D) the total amount of contributions of non-Federal funds accepted into the account established under paragraph (6). ;\n**(3)**\nin subsection (f)(1), in the matter preceding subparagraph (A), by striking The Secretary and the Secretary of Commerce shall jointly and inserting The Secretary of Commerce, in consultation with the Secretary, shall ;\n**(4)**\nin subsection (j)(3)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (v), by striking ; and and inserting , including greenhouse gas emissions reduced and avoided; ;\n**(ii)**\nin clause (vi), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(vii) identifying available industry methodologies to establish a lifecycle greenhouse gas emissions assessment methodology for biobased products. ; and\n**(B)**\nin subparagraph (B), by striking this subparagraph and inserting the Biomanufacturing and Jobs Act of 2025 and every 5 years thereafter ;\n**(5)**\nin subsection (k), by striking 2023 each place it appears and inserting 2031 ; and\n**(6)**\nin subsection (l)\u2014\n**(A)**\nby striking In this section and inserting the following:\n(1) In general In this section ; and\n**(B)**\nby adding at the end the following:\n(2) Standard (A) In general To determine the contents of biobased products, the Secretary shall use\u2014 (i) the most recent version of the ASTM\u2013D\u20136866 standard of ASTM International; or (ii) any alternative standard that the Secretary determines appropriate. (B) Administrative Procedure Act In carrying out subparagraph (A)(ii), the Secretary shall, to the maximum extent practicable, comply with the requirements for a Federal agency issuing a rule under chapter 5 of title 5, United States Code (commonly referred to as the Administrative Procedure Act ). (C) Stakeholder input Prior to issuing any rule or guidance pursuant to this subsection, the Secretary shall consult with stakeholders that the Secretary determines relevant, such as farmers, feedstock suppliers and handlers, and biomanufacturers, regarding the potential impact of the rule or guidance on the relevant industry. .\n#### 5. Biobased Task Force\nTitle IX of the Farm Security and Rural Investment Act of 2002 is amended by inserting after section 9003 ( 7 U.S.C. 8103 ) the following:\n9004. Biobased task force (a) Establishment The Secretary shall establish a task force (referred to in this section as the task force )\u2014 (1) to coordinate programs and activities within the Department of Agriculture relating to the research, development, promotion, marketing, and analysis of biobased products, including to support the use of agricultural commodities and forest products in biobased products; (2) to maximize the resources allocated towards the research, development, promotion, marketing, and analysis of biobased products by the Department of Agriculture; (3) to determine the effectiveness of the programs and activities described in paragraph (1); and (4) to make recommendations for improvements to those programs and activities. (b) Membership The task force shall be composed of not less than 1 representative from each of the following mission areas or offices of the Department of Agriculture: (1) The rural development mission area. (2) The National Institute of Food and Agriculture. (3) The Economic Research Service. (4) The Agricultural Research Service. (5) The National Agricultural Statistics Service. (6) The Office of the Chief Scientist. (7) The Office of the Chief Economist. (8) The Office of Energy Policy and New Uses. (9) Any other mission area or office with responsibilities relating to the research, development, promotion, marketing, or analysis of biobased products. (c) Lead mission area The rural development mission area of the Department of Agriculture shall be the lead mission area for the task force. (d) Process for public input The task force shall establish a process for public input to help inform the determination of the task force under subsection (a)(3) of the effectiveness of the programs and activities described in subsection (a)(1). (e) Study and report (1) In general The task force shall conduct a study that\u2014 (A) identifies any existing programs and activities of the Department of Agriculture that may offer new opportunities to advance the research, development, promotion, marketing, and analysis of biobased products; and (B) describes those new opportunities and how those programs and activities may be used to advance and support the research, development, promotion, marketing, and analysis of biobased products. (2) Report Not later than 3 years after the date of enactment of the Biomanufacturing and Jobs Act of 2025 , the task force shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that describes\u2014 (A) a summary of the work conducted by the task force; (B) the findings of the study conducted under paragraph (1); and (C) recommendations for improvements to the programs and activities described in subsection (a)(1) and identified under paragraph (1)(A). (f) Termination The task force shall terminate on the date that is 4 years after the date of enactment of the Biomanufacturing and Jobs Act of 2025 . (g) Nonapplicability Chapter 10 of title 5, United States Code, shall not apply to the task force. .\n#### 6. Bioproduct labeling\n##### (a) In general\nTitle IX of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8101 et seq. ) is amended by inserting after section 9008 the following:\n9009. Bioproducts (a) Definition of covered term In this section, the term covered term means each of the following terms: (1) Bio-attributed plastic. (2) Bio-attributed product. (3) Biobased plastic. (4) Biobased product. (5) Intermediate ingredient or feedstock. (6) Plant-based product. (7) Renewable biomass. (8) Renewable chemical. (b) Alternate definitions For purposes of only this section, the Secretary, in consultation with the Administrator, may, for any covered term, adopt an alternative definition to the definition given the term under this title. (c) Prohibition It shall be unlawful to sell or label a product using a covered term that does not meet, as applicable\u2014 (1) the definition of that term under this title; or (2) the alternate definition adopted by the Secretary for that covered term under subsection (b). (d) Confidentiality For purposes of enforcing subsection (c), except as directed by the Secretary or the Attorney General, no officer, employee, or agent of the United States shall make available to the public any information, statistic, or document obtained from, or made available by, any person under this title other than in a manner that ensures that confidentiality is preserved regarding\u2014 (1) the identity of all relevant persons (including parties to a contract); and (2) proprietary business information. .",
      "versionDate": "2025-08-01",
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
        "actionDate": "2025-08-01",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4832",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Biomanufacturing and Jobs Act of 2025",
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
        "updateDate": "2025-09-05T17:11:03Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2654is.xml"
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
      "title": "Biomanufacturing and Jobs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Biomanufacturing and Jobs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Farm Security and Rural Investment Act of 2002 to improve the biobased markets program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:55Z"
    }
  ]
}
```
