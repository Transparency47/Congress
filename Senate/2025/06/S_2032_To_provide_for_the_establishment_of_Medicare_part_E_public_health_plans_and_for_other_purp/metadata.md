# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2032?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2032
- Title: Choose Medicare Act
- Congress: 119
- Bill type: S
- Bill number: 2032
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2025-12-10T12:03:19Z
- Update date including text: 2025-12-10T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2032",
    "number": "2032",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Choose Medicare Act",
    "type": "S",
    "updateDate": "2025-12-10T12:03:19Z",
    "updateDateIncludingText": "2025-12-10T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T17:40:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "IL"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "RI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "HI"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NY"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MN"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "IL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2032is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2032\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Mr. Merkley (for himself, Mr. Murphy , Ms. Baldwin , Mr. Blumenthal , Mr. Booker , Ms. Duckworth , Mr. Reed , Mr. Schatz , Mrs. Gillibrand , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide for the establishment of Medicare part E public health plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Choose Medicare Act .\n#### 2. Public health plan\n##### (a) In general\nThe Social Security Act is amended by adding at the end the following:\n2201. Title XXII\u2014Medicare part E public health plans Public health plans.\u2014 (a) Establishment The Secretary shall establish public health plans (to be known as Medicare part E plans ) that are available in the individual market, small group market, and large group market. (b) Benefits (1) In general Each Medicare part E plan, regardless of whether the plan is offered in the individual market, small group market, or large group market, shall be a qualified health plan within the meaning of section 1301(a) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18021(a) ) that\u2014 (A) meets all requirements applicable to qualified health plans under subtitle D of title I of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18021 et seq. ) (other than the requirement under section 1301(a)(1)(C)(ii) of such Act) and title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg et seq. ); (B) provides coverage of\u2014 (i) the essential health benefits described in section 1302(b) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(b) ); and (ii) all items and services for which benefits are available under title XVIII; (C) provides gold-level coverage described in section 1302(d)(1)(C) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(d)(1)(C) ); and (D) provides coverage of abortions and all other reproductive services. (2) Preemption Notwithstanding section 1303(a)(1) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18023(a)(1) )\u2014 (A) a State may not prohibit a Medicare part E plan from offering the coverage described in paragraph (1)(D); and (B) no provision of State law that would prohibit such a plan from offering such coverage shall apply to such plan. (c) Eligibility; enrollment (1) Availability on the Exchanges The Medicare part E plans offered in the individual and small group markets shall be offered through the Federal and State Exchanges, including the Small Business Health Options Program Exchanges (commonly referred to as the SHOP Exchanges ). (2) Eligibility (A) In general Any individual who is a resident of the United States, as determined by the Secretary under subparagraph (C), and who is not an individual described in subparagraph (B), is eligible to enroll in a Medicare part E plan. (B) Exclusions An individual described in this subparagraph is any individual who is\u2014 (i) entitled to, or enrolled for, benefits under title XVIII; (ii) eligible for medical assistance under a State plan under title XIX; or (iii) enrolled for child health assistance or pregnancy-related assistance under a State plan under title XXI. (C) Regulations The Secretary shall promulgate a rule for determining residency for purposes of subparagraph (A). (3) Employer-sponsored plans (A) Employer enrollment Effective with respect to the first plan year that begins 1 year after the date of enactment of the Choose Medicare Act and each plan year thereafter, the Secretary shall provide options for Medicare part E plans in the small group market and large group market that are voluntary, and available to all employers. (B) Group health plans The Secretary, acting through the Administrator for the Centers for Medicare & Medicaid Services, at the request of a plan sponsor, shall serve as a third party administrator of a group health plan that is a Medicare part E plan offered by such sponsor. (C) Portability for employer-sponsored plans The Secretary shall develop a process for allowing individuals enrolled in a Medicare part E plan offered in the small group market or large group market to maintain health insurance coverage through a Medicare part E plan if the individual subsequently loses eligibility for enrollment in such a plan based on termination of the employment relationship. The ability to maintain such coverage shall exist regardless of whether the individual has the option to enroll in other health insurance coverage, including coverage offered in the individual market or through a subsequent employer. (d) Premiums The Secretary shall establish premium rates for the Medicare part E plans that\u2014 (1) are adjusted based on\u2014 (A) whether the plan is offered in the individual market, small group market, or large group market; and (B) the applicable rating area; (2) are at a level sufficient to fully finance\u2014 (A) the costs of health benefits provided by such plans; and (B) administrative costs related to operating the plans; and (3) comply with the requirements under section 2701 of the Public Health Service Act ( 42 U.S.C. 300gg ), including for such plans that are offered in the large group market. (e) Providers and reimbursement rates (1) In general The Secretary shall establish a rate schedule for reimbursing types of health care providers furnishing items and services under the Medicare part E plans at rates that are consistent with the negotiations described in paragraph (2) and are necessary to maintain network adequacy. (2) Manner of negotiation The Secretary shall negotiate the rates described in paragraph (1) in a manner that results in payment rates that are not lower, in the aggregate, than rates under title XVIII, and not higher, in the aggregate, than the average rates paid by other health insurance issuers offering health insurance coverage through an Exchange. (3) Participating providers (A) In general A health care provider that is a participating provider of services or supplier under the Medicare program under title XVIII on the date of enactment of the Choose Medicare Act shall be a participating provider for Medicare part E plans. (B) Additional providers The Secretary shall establish a process to allow health care providers not described in subparagraph (A) to become participating providers for Medicare part E plans. (4) Limitations on balance billing The limitations on balance billing pursuant to the provisions of section 1866(a)(1)(A) shall apply to participating providers for Medicare part E plans in the same manner as such provisions apply to participating providers under the Medicare program. (f) Encouraging use of alternative payment models The Secretary shall, as applicable, utilize alternative payment models, including those described in section 1833(z)(3)(C), in making payments for items and services (including prescription drugs) furnished under Medicare part E plans. The payment rates under such alternative payment models shall comply with the requirement for negotiated rates under subsection (e)(2). (g) Prescription drugs The Secretary shall apply the provisions of part E of title XI to prescription drugs under Medicare part E plans in the same manner as such provisions apply with respect to selected drugs under part E of title XI. (h) Appropriations (1) Start up funding For purposes of establishing the Medicare part E plans, there is appropriated to the Secretary, out of any funds in the Treasury not otherwise obligated, $2,000,000,000, for fiscal year 2026. (2) Initial reserves There is appropriated to the Secretary, out of any funds in the Treasury not otherwise obligated, such sums as may be necessary, based on projected enrollment in the Medicare part E plans in the first plan year in which such plans are offered, to provide reserves for the purpose of paying claims filed during the initial 90-day period of such plan year. (3) Clarification Any provision of law restricting the use of Federal funds with respect to any reproductive health service shall not apply to funds appropriated under paragraph (1) or (2). (i) Health insurance issuer With respect to any Medicare part E plan, the Secretary shall be considered a health insurance issuer, within the meaning of section 2791(b) of the Public Health Service Act ( 42 U.S.C. 300gg\u201391(b) ). .\n##### (b) Application of excise tax for noncompliance with negotiation requirements\nSection 5000D(e)(1) of the Internal Revenue Code of 1986 is amended by adding at the end the following new sentence: Such term shall apply to any drug treated in the same manner as a drug described in the preceding sentence by reason of section 2201(g) of the Social Security Act. .\n#### 3. Notice and navigator referral for employees under the Fair Labor Standards Act of 1938\n##### (a) In general\nSection 18B of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 218b ) is amended\u2014\n**(1)**\nin the heading, by striking to and inserting and navigator referral for ;\n**(2)**\nby redesignating subsection (b) as subsection (c);\n**(3)**\nby inserting after subsection (a) the following:\n(b) Navigator referral (1) In general An employer described in paragraph (3) shall refer each employee who is a full-time employee (as defined in section 4980H(c) of the Internal Revenue Code of 1986) to\u2014 (A) an entity that serves as a navigator under section 1311(i) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(i) ) for the Exchange operating in the State of the employer; or (B) if the Exchange operating in the State of the employer does not have an entity serving as such a navigator, another entity that shall carry out equivalent activities as such a navigator. (2) Referral The referral described in paragraph (1) shall occur\u2014 (A) at the time the employer hires the employee; or (B) on the effective date described in subsection (c)(2) with respect to an employee who is currently employed by the employer on such date. (3) Employer An employer described in this paragraph is any employer that\u2014 (A) does not provide an eligible employer-sponsored plan as defined in section 5000A(f)(2) of the Internal Revenue Code of 1986; or (B) provides such an eligible employer-sponsored plan, but the plan is determined\u2014 (i) to be unaffordable to the employee under clause (i) of section 36B(c)(2)(C) of such Code; or (ii) to not provide the required minimum value under clause (ii) of such section. ; and\n**(4)**\nin subsection (c), as so redesignated\u2014\n**(A)**\nin the heading, by striking Effective date and inserting Effective dates ;\n**(B)**\nby striking Subsection (a) and inserting the following:\n(1) Notice Subsection (a) ; and\n**(C)**\nby adding at the end the following:\n(2) Navigator referral Subsection (b) shall take effect with respect to employers in a State beginning on the date that is 2 years after the date of enactment of the Choose Medicare Act . .\n##### (b) Study\nNot later than January 1, 2030, the Comptroller General of the United States shall conduct a study on the impact of the requirements under section 18B of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 218b ), including the amendments made by subsection (a), on the rate of individuals without minimum essential coverage as defined in section 5000A(f) of the Internal Revenue Code of 1986 in the United States and in each State.\n##### (c) Funding for navigator program\nSection 1311(i)(6) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(i)(6) ) is amended\u2014\n**(1)**\nby striking Grants and inserting the following:\n(A) In general Grants ; and\n**(2)**\nby adding at the end the following:\n(B) Authorization of appropriations There is authorized to be appropriated such sums as may be necessary to address capacity limitations of entities serving as navigators through a grant under this subsection. .\n#### 4. Protecting against high out-of-pocket expenditures for Medicare fee-for-service benefits\nTitle XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) is amended by adding at the end the following new section:\n1899C. Protection against high out-of-pocket expenditures (a) In general Notwithstanding any other provision of this title, in the case of an individual entitled to, or enrolled for, benefits under part A or enrolled in part B, if the amount of the out-of-pocket cost-sharing of such individual for a year (beginning with 2027) equals or exceeds the annual out-of-pocket limit under subsection (b) for that year, the individual shall not be responsible for additional out-of-pocket cost-sharing incurred during that year. (b) Annual out-of-Pocket limit (1) In general The amount of the annual out-of-pocket limit under this subsection shall be\u2014 (A) for 2027, $6,700; or (B) for a subsequent year, the amount specified in this subsection for the preceding year increased or decreased by the percentage change in the medical care component of the Consumer Price Index for All Urban Consumers for the 12-month period ending with June of such preceding year. (2) Rounding If any amount determined under paragraph (1)(B) is not a multiple of $5, such amount shall be rounded to the nearest multiple of $5. (c) Out-of-Pocket cost-Sharing defined (1) In general Subject to paragraphs (2) and (3), in this section, the term out-of-pocket cost-sharing means, with respect to an individual, the amount of the expenses incurred by the individual that are attributable to\u2014 (A) deductibles, coinsurance, and copayments applicable under part A or B; or (B) for items and services that would have otherwise been covered under part A or B but for the exhaustion of those benefits. (2) Certain costs not included (A) Non-covered items and services Expenses incurred for items and services which are not covered under part A or B shall not be considered incurred expenses for purposes of determining out-of-pocket cost-sharing under paragraph (1). (B) Items and services not furnished on an assignment-related basis If an item or service is furnished to an individual under this title and is not furnished on an assignment-related basis, any additional expenses the individual incurs above the amount the individual would have incurred if the item or service was furnished on an assignment-related basis shall not be considered incurred expenses for purposes of determining out-of-pocket cost-sharing under paragraph (1). (3) Source of payment For purposes of paragraph (1), the Secretary shall consider expenses to be incurred by the individual without regard to whether the individual or another person, including a State program, an employer, a medicare supplemental policy, or other third-party coverage, has paid for such expenses. (d) Announcement of the annual out-of-Pocket limit The Secretary shall (beginning in 2026) announce (in a manner intended to provide notice to all interested parties) the annual out-of-pocket limit under this section that will be applicable for the succeeding year. .\n#### 5. Enhancement of premium assistance credit\n##### (a) Use of gold level plan for benchmark\n**(1) In general**\nClause (i) of section 36B(b)(2)(B) of the Internal Revenue Code of 1986 is amended by striking applicable second lowest cost silver plan and inserting applicable second lowest cost gold plan .\n**(2) Conforming amendment related to affordability**\nSection 36B(c)(4)(C)(i)(I) of such Code is amended by striking second lowest cost silver plan and inserting second lowest cost gold plan .\n**(3) Other conforming amendments**\nSubparagraphs (B) and (C) of section 36B(b)(3) of such Code are each amended by striking silver plan each place it appears in the text and the heading and inserting gold plan .\n##### (b) Permanent extension of eligibility rules\n**(1) In general**\nSection 36B(c)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin subparagraph (A), by striking but does not exceed 400 percent , and\n**(B)**\nby striking subparagraph (E).\n**(2) Determination of applicable percentage**\nSubparagraph (A) of section 36B(b)(3) of such Code is amended by striking all that precedes the table in clause (iii)(II) and inserting the following:\n(A) Applicable percentage For purposes of paragraph (2), except as provided in clause (ii), the applicable percentage for any taxable year shall be the percentage such that the applicable percentage for any taxpayer whose household income is within an income tier specified in the following table shall increase, on a sliding scale in a linear manner, from the initial premium percentage to the final premium percentage specified in such table for such income tier: .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 6. Enhancements for reduced cost sharing\n##### (a) Definition of eligible individual\nSection 1402(b)(1) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18071(b)(1) ) is amended by striking silver level and inserting gold level .\n##### (b) Modification of amount\n**(1) In general**\nSection 1402(c)(2) of the Patient Protection and Affordable Care Act is amended to read as follows:\n(2) Additional reduction The Secretary shall establish procedures under which the issuer of a qualified health plan to which this section applies shall further reduce cost-sharing under the plan in a manner sufficient to\u2014 (A) in the case of an eligible insured whose household income is not less than 100 percent but not more than 133 percent of the poverty line for a family of the size involved, increase the plan\u2019s share of the total allowed costs of benefits provided under the plan to 94 percent of such costs; (B) in the case of an eligible insured whose household income is more than 133 percent but not more than 150 percent of the poverty line for a family of the size involved, increase the plan\u2019s share of the total allowed costs of benefits provided under the plan to 92 percent of such costs; (C) in the case of an eligible insured whose household income is more than 150 percent but not more than 200 percent of the poverty line for a family of the size involved, increase the plan\u2019s share of the total allowed costs of benefits provided under the plan to 90 percent of such costs; (D) in the case of an eligible insured whose household income is more than 200 percent but not more than 300 percent of the poverty line for a family of the size involved, increase the plan\u2019s share of the total allowed costs of benefits provided under the plan to 85 percent of such costs; and (E) in the case of an eligible insured whose household income is more than 300 percent but not more than 400 percent of the poverty line for a family of the size involved, increase the plan\u2019s share of the total allowed costs of benefits provided under the plan to 80 percent of such costs. .\n**(2) Conforming amendment**\nClause (i) of section 1402(c)(1)(B) of such Act is amended to read as follows:\n(i) In general The Secretary shall ensure the reduction under this paragraph shall not result in an increase in the plan\u2019s share of the total allowed costs of benefits provided under the plan above\u2014 (I) 94 percent in the case of an eligible insured described in paragraph (2)(A); (II) 92 percent in the case of an eligible insured described in paragraph (2)(B); (III) 90 percent in the case of an eligible insured described in paragraph (2)(C); (IV) 85 percent in the case of an eligible insured described in paragraph (2)(D); and (V) 80 percent in the case of an eligible insured described in paragraph (2)(E). .\n##### (c) Effective date\nThe amendments made by this section shall apply to plan years beginning after December 31, 2025.\n#### 7. Reinsurance and affordability fund\nPart 5 of subtitle D of title I of the Patient Protection and Affordable Care Act is amended by inserting after section 1341 ( 42 U.S.C. 18061 ) the following:\n1341A. Reinsurance and affordability fund for the individual market in each State (a) In general The Secretary, in consultation with the National Association of Insurance Commissioners, shall establish a program to enable each State, for any plan year beginning in the 3-year period beginning January 1, 2026, to\u2014 (1) provide reinsurance payments to health insurance issuers with respect to individuals enrolled under individual health insurance coverage offered by such issuers; or (2) provide assistance (other than through payments described in paragraph (1)) to reduce out-of-pocket costs, such as copayments, coinsurance, premiums, and deductibles, of individuals enrolled under qualified health plans offered in the individual market through an Exchange. (b) Appropriations There is appropriated, out of any money in the Treasury not otherwise appropriated, $30,000,000,000 for the period of fiscal years 2026 to 2028 for purposes of establishing and administering the program established under this section. Such amount shall remain available until expended. .\n#### 8. Expanding rating rules to large group market\n##### (a) In general\nSection 2701(a) of the Public Health Service Act ( 42 U.S.C. 300gg(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking small ; and\n**(2)**\nby striking paragraph (5).\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to plans offered in the first plan year beginning after the date of enactment of this Act and any plan year thereafter.\n#### 9. Protection of consumers from excessive, unjustified, or unfairly discriminatory rates\n##### (a) Protection from excessive, unjustified, or unfairly discriminatory rates\nSection 2794 of the Public Health Service Act ( 42 U.S.C. 300gg\u201394 ) is amended by adding at the end the following new subsection:\n(e) Protection from excessive, unjustified, or unfairly discriminatory rates (1) Authority of States Nothing in this section shall be construed to prohibit a State from imposing requirements (including requirements relating to rate review standards and procedures and information reporting) on health insurance issuers with respect to rates that are in addition to the requirements of this section and are more protective of consumers than such requirements. (2) Consultation in rate review process In carrying out this section, the Secretary shall consult with the National Association of Insurance Commissioners and consumer groups. (3) Determination of who conducts reviews for each State The Secretary shall determine, after the date of enactment of this subsection and periodically thereafter, the following: (A) In which markets in each State the State insurance commissioner or relevant State regulator shall undertake the corrective actions under paragraph (4) , based on the Secretary\u2019s determination that the State insurance commissioner or relevant State regulator is adequately undertaking and utilizing such actions in that market. (B) In which markets in each State the Secretary shall undertake the corrective actions under paragraph (4) , in cooperation with the relevant State insurance commissioner or State regulator, based on the Secretary\u2019s determination that the State is not adequately undertaking and utilizing such actions in that market. (4) Corrective action for excessive, unjustified, or unfairly discriminatory rates In accordance with the process established under this section, the Secretary or the relevant State insurance commissioner or State regulator shall take corrective actions to ensure that any excessive, unjustified, or unfairly discriminatory rates are corrected prior to implementation, or as soon as possible thereafter, through mechanisms such as\u2014 (A) denying rates; (B) modifying rates; or (C) requiring rebates to consumers. (5) Noncompliance (A) In general Failure to comply with any corrective action taken by the Secretary under this subsection may result in the application of civil monetary penalties described in subparagraph (B) and, if the Secretary determines appropriate, make the plan involved ineligible for classification as a qualified health plan. (B) Civil monetary penalties (i) In general The provisions of section 1128A of the Social Security Act, other than subsection (a) and (b) and the first sentence of subsection (c)(1) of such section, shall apply to civil monetary penalties under this paragraph in the same manner as such provisions apply to a penalty or proceeding under section 1128A of the Social Security Act. (ii) Amount The provisions of subparagraph (C) of section 2723(b)(2) shall apply to civil monetary penalties under this paragraph in the same manner as such provisions apply to a penalty under such section. .\n##### (b) Clarification of Regulatory Authority\nSection 2794 of the Public Health Service Act ( 42 U.S.C. 300gg\u201394 ) is further amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the subsection heading, by striking premium and inserting rate ;\n**(B)**\nin paragraph (1), by striking unreasonable increases in premiums and inserting potentially excessive, unjustified, or unfairly discriminatory rates, including premiums, ; and\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nby striking an unreasonable premium increase and inserting a potentially excessive, unjustified, or unfairly discriminatory rate ;\n**(ii)**\nby striking the increase and inserting the rate ; and\n**(iii)**\nby striking such increases and inserting such rates ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by striking Premium and inserting Rate ;\n**(B)**\nby striking premium increases each place it appears and inserting rates ;\n**(C)**\nin paragraph (1)\u2014\n**(i)**\nin the paragraph heading, by striking Premium Increase and inserting Rate ; and\n**(ii)**\nin subparagraph (B), by striking excessive or unjustified and inserting excessive, unjustified, or unfairly discriminatory ; and\n**(D)**\nin paragraph (2)\u2014\n**(i)**\nin the paragraph heading, by striking Premium Increases and inserting Rates ; and\n**(ii)**\nin subparagraph (B), by striking premium and inserting rate .\n##### (c) Conforming amendment\nSection 1311(e)(2) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(e)(2) ) is amended by striking excessive or unjustified premium increases and inserting excessive, unjustified, or unfairly discriminatory rates .\n##### (d) Applicability to grandfathered health plans\nSection 1251(a)(5) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18011(a)(5) ) is amended\u2014\n**(1)**\nby striking Sections 2799A\u20131 and inserting the following:\n(A) In general Sections 2799A\u20131 ; and\n**(2)**\nby adding at the end the following:\n(B) Ensuring that consumers get value for their dollars Section 2794 of the Public Health Service Act shall apply to grandfathered health plans for plan years beginning on or after January 1, 2026. .\n##### (e) Effective date\nThe amendments made by this section shall take effect on the date of enactment of this Act and shall be implemented with respect to health plans beginning not later than January 1, 2026.\n#### 10. Sense of Congress\nIt is the sense of the Congress that\u2014\n**(1)**\nthe Federal Government, acting in its capacity as an insurer, employer, or health care provider, should serve as a model for the Nation to ensure coverage of all reproductive services; and\n**(2)**\nall restrictions on coverage of reproductive services in the private insurance market should end.",
      "versionDate": "2025-06-11",
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
        "actionDate": "2025-06-11",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3911",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Choose Medicare Act",
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
        "name": "Health",
        "updateDate": "2025-07-01T13:14:40Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2032is.xml"
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
      "title": "Choose Medicare Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Choose Medicare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the establishment of Medicare part E public health plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:30Z"
    }
  ]
}
```
