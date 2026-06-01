# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6494?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6494
- Title: Territories Health Equity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6494
- Origin chamber: House
- Introduced date: 2025-12-05
- Update date: 2026-02-24T19:41:19Z
- Update date including text: 2026-02-24T19:41:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-05: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-05: Introduced in House

## Actions

- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-05",
    "latestAction": {
      "actionDate": "2025-12-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6494",
    "number": "6494",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000610",
        "district": "",
        "firstName": "Stacey",
        "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
        "lastName": "Plaskett",
        "party": "D",
        "state": "VI"
      }
    ],
    "title": "Territories Health Equity Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-24T19:41:19Z",
    "updateDateIncludingText": "2026-02-24T19:41:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-05",
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
          "date": "2025-12-05T16:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-05T16:00:45Z",
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
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "AS"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "PR"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "GU"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "MP"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6494ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6494\nIN THE HOUSE OF REPRESENTATIVES\nDecember 5, 2025 Ms. Plaskett (for herself, Mrs. Radewagen , Mr. Hern\u00e1ndez , Mr. Moylan , and Ms. King-Hinds ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to make improvements to the treatment of the United States territories under the Medicare and Medicaid programs, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Territories Health Equity Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTitle I\u2014MEDICAID\nCAP\nSec. 102. Elimination of specific Federal medical assistance percentage (FMAP) limitation for Puerto Rico.\nSec. 103. Permitting Medicaid DSH allotments for territories.\nTitle II\u2014MEDICARE\nSubtitle A\u2014Part A\nSec. 201. Calculation of Medicare DSH payments for IPPS hospitals in Puerto Rico.\nSec. 202. Rebasing target amount for hospitals in territories.\nSec. 203. Medicare DSH target adjustment for hospitals in territories.\nSubtitle B\u2014Part B\nSec. 211. Eliminating late enrollment penalties under Part B of the Medicare program for certain individuals residing in Puerto Rico.\nSubtitle C\u2014Medicare Advantage (Part C)\nSec. 221. Adjustment in benchmark for low-base payment counties in Puerto Rico.\nSubtitle D\u2014Part D\nSec. 231. Automatic eligibility of certain low-income territorial residents for premium and cost-sharing subsidies under the Medicare program; sunset of enhanced allotment program.\nTitle III\u2014MISCELLANEOUS\nSec. 301. Medicaid and CHIP territory transparency and information.\nSec. 302. Report on exclusion of territories from exchanges.\nSec. 303. Access to coverage for individuals in certain areas without any available exchange plans.\nI\nMEDICAID\n#### 101. Elimination of general Medicaid funding limitations ( CAP ) for territories\n##### (a) In general\nSection 1108 of the Social Security Act ( 42 U.S.C. 1308 ) is amended\u2014\n**(1)**\nin subsection (f), in the matter preceding paragraph (1), by striking subsections (g) and (h) and inserting subsections (g), (h), and (j) ;\n**(2)**\nin subsection (g)(2), in the matter preceding subparagraph (A), by inserting subsection (j) and after subject to ;\n**(3)**\nin subsection (i), by striking paragraph (4); and\n**(4)**\nby adding at the end the following new subsection:\n(j) Sunset of medicaid funding limitations for puerto rico, the virgin islands, guam, the northern mariana islands, and american samoa Subsections (f) and (g) shall not apply to Puerto Rico, the Virgin Islands, Guam, the Northern Mariana Islands, and American Samoa beginning with fiscal year 2026. .\n##### (b) Conforming amendments\n**(1)**\nSection 1902(j) of the Social Security Act ( 42 U.S.C. 1396a(j) ) is amended by striking , the limitation in section 1108(f),, .\n**(2)**\nSection 1903(u) of the Social Security Act ( 42 U.S.C. 1396b(u) ) is amended by striking paragraph (4).\n##### (c) Effective date\nThe amendments made by this section shall apply beginning with fiscal year 2026.\n#### 102. Elimination of specific Federal medical assistance percentage (FMAP) limitation for Puerto Rico\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended\u2014\n**(1)**\nin subsection (b)(2), by inserting for fiscal years before fiscal year 2026 after American Samoa ; and\n**(2)**\nin subsection (ff)(2), by striking 2027 and inserting 2025 .\n#### 103. Permitting medicaid DSH allotments for territories\nSection 1923(f) of the Social Security Act ( 42 U.S.C. 1396r\u20134(f) ) is amended\u2014\n**(1)**\nin paragraph (6), by adding at the end the following new subparagraph:\n(C) Territories (i) Fiscal year 2026 For fiscal year 2026, the DSH allotment for Puerto Rico, the Virgin Islands, Guam, the Northern Mariana Islands, and American Samoa shall bear the same ratio to $300,000,000 as the ratio of the number of individuals who are low-income or uninsured and residing in such respective territory (as estimated from time to time by the Secretary) bears to the sums of the number of such individuals residing in all of the territories. (ii) Subsequent fiscal year For each subsequent fiscal year, the DSH allotment for each such territory is subject to an increase in accordance with paragraph (3). ; and\n**(2)**\nin paragraph (9), by inserting before the period at the end the following: , and includes, beginning with fiscal year 2026, Puerto Rico, the Virgin Islands, Guam, the Northern Mariana Islands, and American Samoa .\nII\nMEDICARE\nA\nPart A\n#### 201. Calculation of medicare DSH payments for IPPS hospitals in Puerto Rico\nSection 1886(d)(9)(D)(iii) of the Social Security Act ( 42 U.S.C. 1395ww(d)(9)(D)(iii) ) is amended to read as follows:\n(iii) Subparagraph (F) (relating to disproportionate share payments), including application of subsection (r), except that for this purpose\u2014 (I) the sum described in clause (ii) of this subparagraph shall be substituted for the sum referred to in paragraph (5)(F)(ii)(I); and (II) for discharges occurring on or after October 1, 2025, subclause (I) of paragraph (5)(F)(vi) shall be applied by substituting for the numerator described in such subclause the number of subsection (d) Puerto Rico hospital\u2019s patient days for the cost reporting period involved which were made up of patients who (for such days) were entitled to benefits under part A of this title and were\u2014 (aa) entitled to supplementary security income benefits (excluding any State supplementation) under title XVI; (bb) eligible for medical assistance under a State plan under title XIX; or (cc) receiving aid or assistance under any plan of the State approved under title I, X, XIV, or XVI. .\n#### 202. Rebasing target amount for hospitals in territories\nSection 1886(b)(3) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3) ) is amended by adding at the end the following new subparagraph:\n(M) (i) For each cost reporting period beginning on or after October 1, 2025, in the case of a hospital located in a territory of the United States, there shall be substituted for the target amount otherwise determined under subparagraph (A) the rebased target amount (as defined in clause (ii)), if such substitution results in an amount of payment under this section to the hospital for such period that is greater than the amount of payment that would be made under this section to the hospital for such period if this subparagraph were not to apply. (ii) For purposes of this subparagraph, the term rebased target amount has the meaning given the term target amount in subparagraph (A), except that\u2014 (I) for a cost reporting period beginning on or after October 1, 2025, and before September 30, 2030, there shall be substituted for the preceding 12-month cost reporting period the 12-month cost reporting period beginning during fiscal year 2017; (II) for a cost reporting period beginning on or after October 1, 2030, there shall be substituted for the preceding 12-month cost reporting period the cost reporting period for which the target amount determined under subparagraph (A) is the highest among the 5 cost reporting periods for which the Secretary has the most recent settled cost reports; (III) any reference in subparagraph (A)(i) to the first such cost reporting period is deemed a reference to the first cost reporting period following the 12-month cost reporting period beginning during fiscal year 2017; and (IV) the applicable percentage increase shall only be applied under subparagraph (B)(ii) for cost reporting periods beginning on or after October 1, 2025. .\n#### 203. Medicare DSH target adjustment for hospitals in territories\nSection 1886(b)(3) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3) ), as amended by section 202, is further amended by adding at the end the following new subparagraph:\n(N) (i) For each cost reporting period beginning on or after October 1, 2025, in the case of a hospital that is located in a territory of the United States other than Puerto Rico and that would be a subsection (d) hospital if it were located in one of the 50 States, the target amount shall be increased by\u2014 (I) in the case that such hospital has a disproportionate patient percentage of not less than 15 percent and not greater than 40 percent, 10 percent; and (II) in the case that such hospital has a disproportionate patient percentage of greater than 40 percent, 10 percent plus 60 percent of the number of percentage points by which such hospital\u2019s disproportionate patient percentage exceeds 40 percent. (ii) For purposes of this subparagraph, the term disproportionate patient percentage has the meaning given such term in subsection (d)(5)(F)(vi), except that in applying such meaning any reference under such subsection to individuals entitled to supplementary security income under title XVI shall be deemed for purposes of this subparagraph to include individuals\u2014 (I) eligible for medical assistance under a State plan under title XIX; or (II) receiving aid or assistance under any plan of the territory approved under title I, X, XIV, or XVI. .\nB\nPart B\n#### 211. Eliminating late enrollment penalties under Part B of the medicare program for certain individuals residing in Puerto Rico\n##### (a) In general\nSection 1839(b) of the Social Security Act ( 42 U.S.C. 1395r(b) ) is amended in the second sentence by inserting or months occurring in the 5-year period beginning on the date on which the individual becomes entitled to benefits under part A if such individual was residing in Puerto Rico as of such date and such date is after the date that is 4 years before the date of the enactment of the Territories Health Equity Act of 2025 before the period at the end of such sentence.\n##### (b) Application\nThe amendment made by subsection (a) shall apply with respect to premiums paid for months beginning on or after the date of the enactment of this Act.\nC\nMedicare Advantage (Part C)\n#### 221. Adjustment in benchmark for low-base payment counties in Puerto Rico\nSection 1853(n) of the Social Security Act ( 42 U.S.C. 1395w\u201323(n) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking and (5) and inserting (5), and (6) ;\n**(2)**\nin paragraph (4), by striking In no case and inserting Subject to paragraph (6), in no case ; and\n**(3)**\nby adding at the end the following new paragraph:\n(6) Special rules for blended benchmark amount for territories (A) In general Subject to paragraph (2), the blended benchmark amount for an area in a territory for a year (beginning with 2026) shall not be less than 80 percent of the national average of the base payment amounts specified in subparagraph (2)(E) for such year for areas within the 50 States and the District of Columbia. (B) Limitation In no case shall the blended benchmark amount for an area in a territory for a year under subparagraph (A) exceed the lowest blended benchmark amount for any area within the 50 States and the District of Columbia for such year. .\nD\nPart D\n#### 231. Automatic eligibility of certain low-income territorial residents for premium and cost-sharing subsidies under the medicare program; sunset of enhanced allotment program\n##### (a) Automatic eligibility of certain low-Income territorial residents for premium and cost-Sharing subsidies under the medicare program\n**(1) In general**\nSection 1860D\u201314(a)(3) of the Social Security Act ( 42 U.S.C. 1395w\u2013114(a)(3) ) is amended\u2014\n**(A)**\nin subparagraph (B)(v)\u2014\n**(i)**\nin subclause (I), by striking and at the end;\n**(ii)**\nin subclause (II), by striking the period and inserting ; and ; and\n**(iii)**\nby inserting after subclause (II) the following new subclause:\n(III) with respect to plan years beginning on or after January 1, 2026, shall provide that any part D eligible individual who is enrolled for medical assistance under the State Medicaid plan of a territory (as defined in section 1935(f)) under title XIX (or a waiver of such a plan) shall be treated as a subsidy eligible individual described in paragraph (1). ; and\n**(B)**\nin subparagraph (F), by adding at the end the following new sentence: The previous sentence shall not apply with respect to eligibility determinations for premium and cost-sharing subsidies under this section made on or after January 1, 2026. .\n**(2) Conforming amendment**\nSection 1860D\u201331(j)(2)(D) of the Social Security Act ( 42 U.S.C. 1395w\u2013141(j)(2)(D) ) is amended by adding at the end the following new sentence: The previous sentence shall not apply with respect to amounts made available to a State under this paragraph on or after January 1, 2026. .\n##### (b) Sunset of enhanced allotment program\n**(1) In general**\nSection 1935(e) of the Social Security Act ( 42 U.S.C. 1396u\u20135(e) ) is amended\u2014\n**(A)**\nin paragraph (1)(A), by inserting after such State the following: before January 1, 2026 ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), in the matter preceding clause (i), by inserting after a year the following: (before 2026) ; and\n**(ii)**\nin subparagraph (B)(iii), by striking a subsequent year and inserting each of fiscal years 2010 through 2025 .\n**(2) Territory defined**\nSection 1935 of the Social Security Act ( 42 U.S.C. 1396u\u20135 ) is amended by adding at the end the following new subsection:\n(f) Territory defined In this section, the term territory means Puerto Rico, the Virgin Islands, Guam, the Northern Mariana Islands, and American Samoa. .\nIII\nMISCELLANEOUS\n#### 301. Medicaid and CHIP territory transparency and information\n##### (a) Publication of information on federal expenditures under medicaid and CHIP in the territories\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Health and Human Services shall publish, and periodically update, on the internet site of the Centers for Medicare & Medicaid Services information on Medicaid and CHIP carried out in the territories of the United States. Such information shall include, with respect to each such territory\u2014\n**(1)**\nthe income levels established by the territory for purposes of eligibility of an individual to receive medical assistance under Medicaid or child health assistance under CHIP;\n**(2)**\nthe number of individuals enrolled in Medicaid and CHIP in such territory;\n**(3)**\nany State plan amendments in effect to carry out Medicaid or CHIP in such territory;\n**(4)**\nany waiver of the requirements of title XIX or title XXI issued by the Secretary to carry out Medicaid or CHIP in the territory, including a waiver under section 1115 of the Social Security Act ( 42 U.S.C. 1315 ), any application for such a waiver, and any documentation related to such application (including correspondence);\n**(5)**\nthe amount of the Federal and non-Federal share of expenditures under Medicaid and CHIP in such territory;\n**(6)**\nthe systems in place for the furnishing of health care items and services under Medicaid and CHIP in such territory;\n**(7)**\nthe design of CHIP in such territory; and\n**(8)**\nother information regarding the carrying out of Medicaid and CHIP in the territory that is published on such internet site with respect to carrying out Medicaid and CHIP in each State and the District of Columbia.\n##### (b) Definitions\nIn this section:\n**(1) CHIP**\nThe term CHIP means the State Children\u2019s Health Insurance Program under title XXI of the Social Security Act.\n**(2) Medicaid**\nThe term Medicaid means the Medicaid program under title XIX of the Social Security Act.\n**(3) Territory**\nThe term territory of the United States includes Puerto Rico, the Virgin Islands of the United States, Guam, the Northern Mariana Islands, and American Samoa.\n#### 302. Report on exclusion of territories from exchanges\n##### (a) In general\nNot later than February 1, 2026, the Secretary of Health and Human Services shall submit to Congress a report that details the adverse impacts in each territory from the practical exclusion of the territories from the provisions of part II of subtitle D of title I of the Patient Protection and Affordable Care Act insofar as such provisions provide for the establishment of an American Health Benefit Exchange or the administration of a federally facilitated Exchange in each State and in the District of Columbia for the purpose of making health insurance more affordable and accessible for individuals and small businesses.\n##### (b) Information in report\nThe report shall include information on the following:\n**(1)**\nAn estimate of the total number of uninsured and underinsured individuals residing in each territory with respect to health insurance coverage.\n**(2)**\nA description of the number of health insurance issuers in each territory and the health insurance plans these issuers offer.\n**(3)**\nAn estimate of the number of individuals residing in each territory who are denied premium and cost-sharing assistance that would otherwise be available to them for obtaining health insurance coverage through an Exchange if they resided in one of the 50 States or in the District of Columbia.\n**(4)**\nAn estimate of the amount of Federal assistance described in paragraph (3) that is not being made available to residents of each territory.\n**(5)**\nAn estimate of the number of small employers in each territory that would be eligible to purchase health insurance coverage through a Small Business Health Options Program (SHOP) Marketplace that would operate as part of an Exchange if the employers were in one of the 50 States or in the District of Columbia.\n#### 303. Access to coverage for individuals in certain areas without any available exchange plans\nPart 2 of subtitle D of title I of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031 et seq. ) is amended by adding at the end the following:\n1314. Access to coverage for individuals in certain areas without any available exchange plans (a) In general (1) Coverage through dc exchange Not later than 3 months after the date of enactment of this section, the Secretary, in consultation with the Secretary of the Treasury and the Director of the Office of Personnel Management, shall establish a mechanism to ensure that, for any plan year beginning on or after the date described in subsection (c), any individual described in paragraph (2) has access to health insurance coverage which is at least as broad as the coverage available to Members of Congress and congressional staff (as defined in section 1312(d)(3)(D)) through the Exchange operating in the District of Columbia. Such individuals shall be eligible for any premium tax credit under section 36B of the Internal Revenue Code of 1986, reduced cost sharing under section 1402, and advance determination and payment of such credits or such reductions under section 1412 to be administered by the Secretary, in consultation with the Secretary of the Treasury and the Director of the Office of Personnel Management. The District of Columbia, its residents, and small businesses shall be held harmless from any increased costs resulting from the enactment of this section. (2) Individual described An individual described in this paragraph is any individual who\u2014 (A) is not eligible to enroll in an employer-sponsored health plan (excluding such a plan that would not be considered minimum essential coverage due to the application of subparagraph (C) of section 36B(c)(2) of the Internal Revenue Code of 1986 if such subparagraph applied to such plan); and (B) is a bona fide resident of any possession of the United States (as determined under section 937(a) of such Code) in which the Secretary certifies that no qualified health plan is offered through an Exchange established under this title. (3) Possession of the united states For purposes of this section, the term possession of the United States shall include such possessions as are specified in section 937(a)(1) of the Internal Revenue Code of 1986. (b) Treatment of possessions (1) Payments to possessions (A) Mirror code possession The Secretary of the Treasury shall periodically (but not less frequently than annually) pay to each possession of the United States with a mirror code tax system amounts equal to the loss to that possession by reason of the application of this section (determined without regard to paragraph (2)) with respect to taxable years beginning after the date described in subsection (c). Such amounts shall be determined by the Secretary of the Treasury based on information provided by the government of the respective possession. (B) Other possessions The Secretary of the Treasury shall periodically (but not less frequently than annually) pay to each possession of the United States which does not have a mirror code tax system amounts estimated by the Secretary of the Treasury as being equal to the aggregate benefits that would have been provided to residents of such possession by reason of the application of this section for any taxable years beginning after the date described in subsection (c) if a mirror code tax system had been in effect in such possession. The preceding sentence shall not apply with respect to any possession of the United States unless such possession has a plan, which has been approved by the Secretary of the Treasury, under which such possession will promptly distribute such payments to the residents of such possession. (2) Coordination with credit allowed against united states income taxes No credit shall be allowed against United States income taxes for any taxable year under section 36B of the Internal Revenue Code of 1986 to any person\u2014 (A) to whom a credit is allowed against taxes imposed by the possession by reason of this section (determined without regard to this paragraph) for such taxable year, or (B) who is eligible for a payment under a plan described in paragraph (1)(B) with respect to such taxable year. (3) Mirror code tax system For purposes of this subsection, the term mirror code tax system means, with respect to any possession of the United States, the income tax system of such possession if the income tax liability of the residents of such possession under such system is determined by reference to the income tax laws of the United States as if such possession were the United States. (4) Treatment of payments For purposes of section 1324(b)(2) of title 31, United States Code, or any similar rule of law, the payments under this subsection shall be treated in the same manner as a refund due from the credit allowed under section 36B of the Internal Revenue Code of 1986. (c) Date described The date described in this subsection is the date on which the Secretary establishes the mechanism described in subsection (a)(1). .",
      "versionDate": "2025-12-05",
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
        "updateDate": "2026-01-05T16:21:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-05",
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
          "measure-id": "id119hr6494",
          "measure-number": "6494",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-05",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6494v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-12-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Territories Health Equity Act of 2025</strong></p><p>This bill alters provisions relating to the treatment of U.S. territories under Medicaid, Medicare, and Medicare Advantage.</p><p>For example, the bill</p><ul><li>eliminates Medicaid funding limitations for U.S. territories beginning in FY2026,</li><li>exempts an individual from late-enrollment penalties for Medicare medical services if the individual resided in Puerto Rico as of the date of eligibility and the individual enrolls within five years of such date, and</li><li>establishes minimum criteria for certain elements used in Medicare Advantage payment calculations for areas within U.S. territories.</li></ul><p>The bill also allows residents of U.S. territories who are unable to obtain health insurance through their employer or a health insurance exchange to instead obtain coverage that is at least as broad as the coverage available to Members of Congress and their staff through the District of Columbia exchange.</p>"
        },
        "title": "Territories Health Equity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6494.xml",
    "summary": {
      "actionDate": "2025-12-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Territories Health Equity Act of 2025</strong></p><p>This bill alters provisions relating to the treatment of U.S. territories under Medicaid, Medicare, and Medicare Advantage.</p><p>For example, the bill</p><ul><li>eliminates Medicaid funding limitations for U.S. territories beginning in FY2026,</li><li>exempts an individual from late-enrollment penalties for Medicare medical services if the individual resided in Puerto Rico as of the date of eligibility and the individual enrolls within five years of such date, and</li><li>establishes minimum criteria for certain elements used in Medicare Advantage payment calculations for areas within U.S. territories.</li></ul><p>The bill also allows residents of U.S. territories who are unable to obtain health insurance through their employer or a health insurance exchange to instead obtain coverage that is at least as broad as the coverage available to Members of Congress and their staff through the District of Columbia exchange.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6494"
    },
    "title": "Territories Health Equity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Territories Health Equity Act of 2025</strong></p><p>This bill alters provisions relating to the treatment of U.S. territories under Medicaid, Medicare, and Medicare Advantage.</p><p>For example, the bill</p><ul><li>eliminates Medicaid funding limitations for U.S. territories beginning in FY2026,</li><li>exempts an individual from late-enrollment penalties for Medicare medical services if the individual resided in Puerto Rico as of the date of eligibility and the individual enrolls within five years of such date, and</li><li>establishes minimum criteria for certain elements used in Medicare Advantage payment calculations for areas within U.S. territories.</li></ul><p>The bill also allows residents of U.S. territories who are unable to obtain health insurance through their employer or a health insurance exchange to instead obtain coverage that is at least as broad as the coverage available to Members of Congress and their staff through the District of Columbia exchange.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6494"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6494ih.xml"
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
      "title": "Territories Health Equity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Territories Health Equity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XVIII and XIX of the Social Security Act to make improvements to the treatment of the United States territories under the Medicare and Medicaid programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:21Z"
    }
  ]
}
```
