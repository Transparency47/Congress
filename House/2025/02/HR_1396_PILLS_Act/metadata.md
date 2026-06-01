# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1396?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1396
- Title: PILLS Act
- Congress: 119
- Bill type: HR
- Bill number: 1396
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-12-05T22:47:33Z
- Update date including text: 2025-12-05T22:47:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1396",
    "number": "1396",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "PILLS Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:47:33Z",
    "updateDateIncludingText": "2025-12-05T22:47:33Z"
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2025-02-14T18:34:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1396ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1396\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Ms. Tenney introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish the generic drugs and biosimilars production credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Producing Incentives for Long-term production of Lifesaving Supply of medicine Act or the PILLS Act .\n#### 2. Generic drugs and biosimilars production credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Generic drugs and biosimilars production credit (a) In general (1) Allowance of credit For purposes of section 38, the generic drugs and biosimilars production credit for any taxable year is an amount equal to the credit amount determined under subsection (b) with respect to each eligible component which is\u2014 (A) produced by the taxpayer in the United States, and (B) sold by such taxpayer to an unrelated person (as determined by the Secretary) during the taxable year. (2) Production and sale must be in trade or business Rules similar to the rules of section 45X(a)(2) shall apply. (3) Disallowance of credit The credit under this subsection shall not be allowed to any taxpayer which, at any time during the taxable year, was a foreign entity of concern (as defined in section 9901(8) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 )). (b) Credit amount For purposes of this section\u2014 (1) In general Subject to paragraph (4), the amount determined under this subsection with respect to any eligible component is an amount equal to the base credit percentage of the value added to such component by the taxpayer. (2) Value added The value added to a component by a taxpayer is an amount equal to\u2014 (A) the gross receipts received by the taxpayer from the sale of the eligible component, minus (B) the cost of eligible components purchased from an unrelated person in connection with the production of the component by the taxpayer. (3) Base credit percentage (A) In general Except as provided in subparagraphs (B) and (C), the base credit percentage is 30 percent. (B) Increased base credit percentage for certain eligible components The base credit percentage is 35 percent in the case of the final production of\u2014 (i) a drug substance, (ii) a drug product, or (iii) a biological product. (C) Domestic content bonus credit (i) In general In the case of an eligible component which contains domestic content, the base credit percentage determined under this paragraph (determined without regard to this subparagraph) shall be increased by an amount equal to\u2014 (I) the domestic content percentage, multiplied by (II) 0.20. (ii) Domestic content percentage For purposes of this subparagraph, the term domestic content percentage means the percentage of the total cost of the eligible components taken into account for purposes of paragraph (2) which is attributable to materials and components that were produced in the United States. (iii) Documentation rules (I) Record keeping No domestic content bonus credit shall be determined under this subparagraph unless the taxpayer provides documentation supporting the domestic content percentage (in such form and manner as the Secretary shall prescribe). (II) Certification by unrelated party In the case of materials or components provided to the taxpayer by an unrelated party, the Secretary shall accept certification (in such form and manner as the Secretary shall prescribe) by such unrelated party that the materials or components were produced in the United States. (4) Phase out (A) In general In the case of any eligible component sold after December 31, 2030, the amount determined under this subsection with respect to such component shall be equal to the product of\u2014 (i) the amount determined under paragraph (1) with respect to such component (determined without regard to this paragraph and after the application of paragraphs (2) and (3)), and (ii) the phase out percentage. (B) Phase out percentage For purposes of subparagraph (A), the phase out percentage is\u2014 (i) in the case of an eligible component sold during calendar year 2031, 75 percent, (ii) in the case of an eligible component sold during calendar year 2032, 50 percent, (iii) in the case of an eligible component sold during calendar year 2033, 25 percent, and (iv) in the case of an eligible component sold after December 31, 2033, 0 percent. (c) Definitions For purposes of this section\u2014 (1) Eligible component (A) In general Except as provided in subparagraphs (B) and (C), the term eligible component means\u2014 (i) an approved generic drug, (ii) a licensed biosimilar, and (iii) any drug substance, intermediate raw material, starting material, reagent, component, in-process material, inactive ingredient, container closure system, packaging, quality testing, or other material or service used, or sold with intention for use, in the production of an approved generic drug or a licensed biosimilar. (B) Exclusion of certain components The term eligible component shall not include a component any portion of the production of which occurred at a facility which is the subject of a warning letter\u2014 (i) which was issued by the Food and Drug Administration on or after September 1, 2009, and (ii) with respect to which the Food and Drug Administration has not issued a close-out letter. (C) Application with other credits The term eligible component shall not include any property which is produced at a facility if the basis of any property which is part of such facility is taken into account for purposes of the credit allowed under section 48F after the date of the enactment of this section. (2) Approved generic drug The term approved generic drug means\u2014 (A) a drug for which an approval of an application filed under section 505(j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j) ) is in effect, or (B) an authorized generic drug (as defined in section 314.3 of title 21, Code of Federal Regulations (or any successor regulation)). (3) Licensed biosimilar (A) In general The term licensed biosimilar means a biological product for which a biologics license has been issued under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ). (B) Biological product The term biological product has the meaning given such term in section 351(i)(1) of the Public Health Service Act ( 42 U.S.C. 262(i)(1) ). (4) Other terms The terms drug substance and drug product have the respective meanings given such terms in section 314.3 of title 21, Code of Federal Regulations (or any successor regulation). (5) Produced in the United States The term produced in the United States means that all the production of the material or component takes place in the United States, regardless of the origin of the subcomponents of such material or component. (6) Production The term production means all steps in the manufacture, propagation, and preparation of an eligible component, including synthesis, mixing, granulating, milling, molding, lyophilizing, tableting, encapsulating, coating, sterilizing, testing, filling, labeling, packaging, and storage prior to release by the manufacturer. (d) Special rules Rules similar to the rules of paragraphs (1), (3), and (4) of section 45X(d) shall apply. (e) Regulatory authority The Secretary shall prescribe such regulations and other guidance as are appropriate or necessary to carry out the purposes of this section. .\n##### (b) Elective payment\n**(1) In general**\nSection 6417(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(13) The generic drugs and biosimilars production credit determined under section 45BB. .\n**(2) Election with respect to other entities**\nParagraph (1) of section 6417(d) is amended\u2014\n**(A)**\nby redesignating subparagraph (E) as subparagraph (F),\n**(B)**\nby striking or (D) each place it appears in subparagraph (F), as so redesignated, and inserting (D), or (E) , and\n**(C)**\nby inserting after subparagraph (D) the following new subparagraph:\n(E) Election with respect to generic drugs and biosimilars production credit (i) In general If a taxpayer other than an entity described in subparagraph (A) makes an election under this subparagraph with respect to any taxable year in which such taxpayer has, after December 31, 2024, produced eligible components (as defined in section 45BB(c)(1)), such taxpayer shall be treated as an applicable entity for purposes of this section for such taxable year, but only with respect to the credit described in subsection (b)(13). (ii) Other rules The rules of clauses (ii) and (iii) of subparagraph (D) shall apply for purposes of this subparagraph. .\n##### (c) Transfer of credits\nSection 6418(f)(1)(A) of the Internal Revenue Code of 1986 is amended by adding at the end the following new clause:\n(xii) The generic drugs and biosimilars production credit determined under section 45BB. .\n##### (d) Conforming amendments\n**(1)**\nSection 38(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby striking plus at the end of paragraph (40),\n**(B)**\nby striking the period at the end of paragraph (41) and inserting , plus , and\n**(C)**\nby adding at the end the following new paragraph:\n(42) the generic drugs and biosimilars production credit determined under section 45BB(a). .\n**(2)**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 45BB. Generic drugs and biosimilars production credit. .\n##### (e) Effective date\nThe amendments made by this section shall apply to generic drugs and biologics produced after the date of enactment of this Act.\n#### 3. Generic drugs and biosimilars investment credit\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Generic drugs and biosimilars investment credit (a) Establishment of credit For purposes of section 46, the generic drugs and biosimilars investment credit for any taxable year is an amount equal to 25 percent of the qualified investment for such taxable year with respect to any qualified facility of an eligible taxpayer. (b) Qualified investment For purposes of this section\u2014 (1) In general The qualified investment for any taxable year is the basis of any qualified property placed in service by the taxpayer during such taxable year which is part of a qualified facility. (2) Qualified property (A) In general The term qualified property means property\u2014 (i) which is tangible property, (ii) with respect to which depreciation (or amortization in lieu of depreciation) is allowable, (iii) which is\u2014 (I) constructed, reconstructed, or erected by the taxpayer, or (II) acquired by the taxpayer if the original use of such property commences with the taxpayer, and (iv) which is used as an integral part of the qualified facility to produce eligible components. (B) Buildings and structural components (i) In general The term qualified property includes any building or its structural components which otherwise satisfies the requirements of subparagraph (A). (ii) Exception Clause (i) shall not apply with respect to a building or portion of a building used for offices, administrative services, or other functions unrelated to the production of eligible components. (3) Qualified facility The term qualified facility means a facility\u2014 (A) which is owned (in whole or in part) by the taxpayer, (B) which is located in the United States or any territory of the United States, and (C) the primary purpose of which is the production of eligible components. (4) Coordination with rehabilitation credit The qualified investment with respect to any qualified facility for any taxable year shall not include that portion of the basis of any property which is attributable to qualified rehabilitation expenditures (as defined in section 47(c)(2)). (5) Certain progress expenditure rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the date of the enactment of the Revenue Reconciliation Act of 1990) shall apply. (c) Definitions For purposes of this section\u2014 (1) Eligible taxpayer The term eligible taxpayer means any taxpayer which is not a foreign entity of concern (as defined in section 9901(8) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 )). (2) Eligible component The term eligible component has the meaning given such term in section 45BB(c)(1). (3) Production The term production has the meaning given such term in section 45BB(c)(6). (d) Termination of credit The credit allowed under this section shall not apply to property the construction of which begins after December 31, 2028. (e) Regulatory authority The Secretary shall prescribe such regulations and other guidance as are appropriate or necessary to carry out the purposes of this section. .\n##### (b) Elective payment\n**(1) In general**\nSection 6417(b) of the Internal Revenue Code of 1986, as amended by section 2(b) of this Act, is further amended by adding at the end the following new paragraph:\n(14) The generic drugs and biosimilars investment credit determined under section 48F. .\n**(2) Election with respect to other entities**\nParagraph (1) of section 6417(d) of such Code, as amended by this Act, is further amended\u2014\n**(A)**\nby redesignating subparagraph (F) as subparagraph (G),\n**(B)**\nby striking or (E) each place it appears in subparagraph (G), as so redesignated, and inserting (E), or (F) , and\n**(C)**\nby inserting after subparagraph (E) the following new subparagraph:\n(F) Election with respect to generic drugs and biosimilars investment credit If a taxpayer other than an entity described in subparagraph (A) makes an election under this subparagraph with respect to any taxable year in which such taxpayer has placed in service a qualified facility (as defined in section 48F(b)(3)), such taxpayer shall be treated as an applicable entity for purposes of this section for such taxable year, but only with respect to the credit described in subsection (b)(14). .\n##### (c) Transfer of credits\nSection 6418(f)(1)(A) of the Internal Revenue Code of 1986, as amended by this Act, is further amended by adding at the end the following new clause:\n(xiii) The generic drugs and biosimilars investment credit determined under section 48F. .\n##### (d) Conforming amendments\n**(1)**\nSection 46 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby striking and at the end of paragraph (6),\n**(B)**\nby striking the period at the end of paragraph (7) and inserting , and , and\n**(C)**\nby adding at the end the following new paragraph:\n(8) the generic drugs and biosimilars investment credit. .\n**(2)**\nSection 49(a)(1)(C) of such Code is amended\u2014\n**(A)**\nby striking and at the end of clause (vii),\n**(B)**\nby striking the period at the end of clause (viii) and inserting , and , and\n**(C)**\nby adding at the end the following new clause:\n(ix) the basis of any qualified property which is part of a qualified facility under section 48F. .\n**(3)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 is amended by inserting after the item relating to section 48E the following new item:\n48F. Generic drugs and biosimilars investment credit. .\n##### (e) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2026.",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PILLS Act",
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
        "name": "Taxation",
        "updateDate": "2025-07-07T19:11:14Z"
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
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1396ih.xml"
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
      "title": "PILLS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-29T08:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PILLS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-29T08:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Producing Incentives for Long-term production of Lifesaving Supply of medicine Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-29T08:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish the generic drugs and biosimilars production credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-29T08:48:19Z"
    }
  ]
}
```
