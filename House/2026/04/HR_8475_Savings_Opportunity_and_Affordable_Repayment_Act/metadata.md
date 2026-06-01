# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8475?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8475
- Title: Savings Opportunity and Affordable Repayment Act
- Congress: 119
- Bill type: HR
- Bill number: 8475
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-21T08:08:00Z
- Update date including text: 2026-05-21T08:08:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8475",
    "number": "8475",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Savings Opportunity and Affordable Repayment Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:00Z",
    "updateDateIncludingText": "2026-05-21T08:08:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
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
      "sponsorshipDate": "2026-04-23",
      "state": "DC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "ME"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MI"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "VA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "WA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MN"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8475ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8475\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Ms. DeLauro (for herself, Ms. Simon , Ms. Norton , Ms. Pingree , Mr. Thanedar , Mr. Casar , Mr. Vindman , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to provide for a Savings Opportunity and Affordable Repayment plan as an income contingent repayment plan.\n#### 1. Short title\nThis Act may be cited as the Savings Opportunity and Affordable Repayment Act .\n#### 2. Savings Opportunity and Affordable Repayment plan\n##### (a) Amendments to the Higher Education Act of 1965\nThe Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) is amended\u2014\n**(1)**\nin section 428(b)(9)(A)\u2014\n**(A)**\nin clause (iv), by striking and after the semicolon;\n**(B)**\nin clause (v), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(vi) beginning on the date that is 180 days after the date of enactment of the Savings Opportunity and Affordable Repayment Act , an income contingent repayment plan known as the Savings Opportunity and Affordable Repayment plan , consistent with section 493E. ;\n**(2)**\nin section 428C(c)(2)(A)\u2014\n**(A)**\nin the first sentence, by striking or income-based and inserting income-based, or income contingent Savings Opportunity and Affordable Repayment (consistent with section 493E) ; and\n**(B)**\nin the second sentence, by striking or income-based and inserting income-based, or income contingent Savings Opportunity and Affordable Repayment ;\n**(3)**\nin section 455(d)\u2014\n**(A)**\nin paragraph (1), by striking subparagraph (D) and inserting the following:\n(D) except as provided in paragraph (6), an income contingent repayment plan\u2014 (i) with varying annual repayment amounts based on the income of the borrower, paid over an extended period of time prescribed by the Secretary, not to exceed 25 years, except that the plan described in this clause shall not be available to the borrower of a Federal Direct PLUS loan made on behalf of a dependent student; and (ii) which, beginning on the date that is 180 days after the date of enactment of the Savings Opportunity and Affordable Repayment Act , shall include the Savings Opportunity and Affordable Repayment plan , consistent with section 493E; and ; and\n**(B)**\nby adding at the end the following:\n(6) Phase outs (A) PAYE repayment plan (i) In general A borrower may choose the Pay As You Earn Repayment Plan, as described in section 685.209 of title 34, Code of Federal Regulations (as in effect on January 19, 2025), as an income contingent repayment plan pursuant to paragraph (1)(D)\u2014 (I) before the date that is 2 years after the date of enactment of the Savings Opportunity and Affordable Repayment Act , only if the borrower\u2014 (aa) has loans eligible for repayment under such plan, as described in such section as in effect on such date; and (bb) has a partial financial hardship when the borrower initially enters such plan, as described in such section as in effect on such date; and (II) on or after the date that is 2 years after the date of enactment of the Savings Opportunity and Affordable Repayment Act , only if the borrower meets the conditions described in subclause (I) and was repaying a loan under such plan before such date that is 2 years after the date of enactment of the Savings Opportunity and Affordable Repayment Act . (ii) Prohibition against re-enrollment Beginning on the date that is 2 years after the date of enactment of the Savings Opportunity and Affordable Repayment Act , a borrower who was repaying a loan under the Pay As You Earn Repayment Plan, as described in clause (i), and changes to a different repayment plan may not re-enroll in the Pay As You Earn Repayment Plan. (B) Income contingent repayment plan (i) In general A borrower may choose the ICR plan, as described in section 685.209 of title 34, Code of Federal Regulations (as in effect on January 19, 2025), as an income contingent repayment plan pursuant to paragraph (1)(D)\u2014 (I) before the date that is 2 years after the date of enactment of the Savings Opportunity and Affordable Repayment Act , only if the borrower has loans eligible for repayment under such plan, as described in such section as in effect on such date, except as provided in clause (iii); and (II) on or after the date that is 2 years after the date of enactment of the Savings Opportunity and Affordable Repayment Act , only if the borrower has loans eligible for repayment under such plan, as described in such section as in effect on such date, except as provided in clause (iii), and was repaying a loan under such plan before such date that is 2 years after the date of enactment of the Savings Opportunity and Affordable Repayment Act . (ii) Prohibition against re-enrollment Beginning on the date that is 2 years after the date of enactment of the Savings Opportunity and Affordable Repayment Act , a borrower who was repaying a loan under the ICR plan, as described in clause (i), and changes to a different repayment plan may not re-enroll in the ICR plan. (iii) Eligible loans for purposes of ICR repayment In addition to the loans eligible for repayment under the ICR plan as described in section 685.209 of title 34, Code of Federal Regulations (as in effect on January 19, 2025), an eligible loan for purposes of repayment under the ICR plan may include\u2014 (I) a Federal Direct PLUS Loan made on behalf of a dependent student; (II) a Federal Direct Consolidation Loan for which the proceeds were used to discharge the liability on a Federal Direct PLUS Loan or a loan under section 428B made on behalf of a dependent student; (III) a loan under section 428B made on behalf of a dependent student; or (IV) a loan under section 428C for which the proceeds were used to discharge the liability on a Federal Direct PLUS Loan or a loan under section 428B made on behalf of a dependent student. ;\n**(4)**\nby inserting after section 493D the following:\n493E. Savings Opportunity and Affordable Repayment plan (a) Definitions In this section: (1) Eligible loan The term eligible loan means a loan made, insured, or guaranteed under part B or D. (2) Monthly payment obligation (A) In general The term monthly payment obligation , when used with respect to a borrower, means that for such borrower the monthly payment amount due on the total amount of eligible loans made to such borrower that is equal to, except as provided in subparagraph (B)\u2014 (i) $0 for the portion of the borrower's, and the borrower's spouse's (if applicable), adjusted gross income (as defined in section 62 of the Internal Revenue Code of 1986) that is less than or equal to 250 percent of the poverty line applicable to the borrower's family size as determined under section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ); plus (ii) 5 percent of the portion of the borrower's, and the borrower's spouse's (if applicable), adjusted gross income (as defined in section 62 of the Internal Revenue Code of 1986) that is greater than 250 percent of the poverty line applicable to the borrower's family size as determined under section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ), prorated by the percentage that is the result of dividing the borrower's original total loan balance attributable to eligible loans received for the borrower's undergraduate study by the original total loan balance attributable to all eligible loans, divided by 12; plus (iii) for loans not subject to clause (ii), 10 percent of the portion of the borrower's, and the borrower's spouse's (if applicable), adjusted gross income (as defined in section 62 of the Internal Revenue Code of 1986) that is greater than 250 percent of the poverty line applicable to the borrower's family size as determined under section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ), prorated by the percentage that is the result of dividing the borrower's original total loan balance minus the original total loan balance of loans subject to clause (ii) by the borrower's original total loan balance attributable to all eligible loans, divided by 12. (B) Minimal payment obligation If the calculation of the monthly payment amount due under subparagraph (A) for a borrower is\u2014 (i) less than $5, then the monthly payment obligation for such borrower is equal to $0; and (ii) equal to or greater than $5 but less than $10, then the monthly payment obligation for such borrower is equal to $10. (b) Savings Opportunity and Affordable Repayment authorized Notwithstanding any other provision of this Act, the Secretary shall carry out a Savings Opportunity and Affordable Repayment plan program that complies with the following: (1) A borrower of any eligible loan may elect to have the borrower's aggregate monthly payment for all such loans not exceed the monthly payment obligation of such borrower. (2) The holder of such eligible loan shall apply\u2014 (A) 50 percent of the borrower's monthly payment under this subsection toward outstanding principal; and (B) 50 percent of the borrower's monthly payment under this subsection\u2014 (i) first toward accrued charges and collection costs on the loan; (ii) then toward outstanding interest; and (iii) then toward outstanding principal. (3) During all periods of repayment on all loans being repaid under the Savings Opportunity and Affordable Repayment plan, the Secretary shall not charge the borrower's account any accrued interest that is not covered by the borrower's monthly payment obligation. (4) Any principal due and not paid under paragraph (2) shall be deferred. (5) In the case of a borrower repaying under the Savings Opportunity and Affordable Repayment plan, the Secretary shall cancel the remaining balance due on all eligible loans for a borrower in the case the borrower\u2014 (A) is repaying only eligible loans received for undergraduate study in a program that is not more than a 2-year program of study, or a consolidation loan that repaid only loans received for such study, after the borrower has satisfied 120 monthly payments or the equivalent (as described in paragraph (6)), over a period of at least 10 years; and (B) is repaying at least one eligible loan not described in subparagraph (A), after the borrower has satisfied 180 monthly payments or the equivalent (as described in paragraph (6)), over a period of at least 15 years. (6) A monthly payment or the equivalent shall be satisfied by any of the following: (A) A month in which the borrower\u2014 (i) makes a monthly payment that is equal to not less than the monthly payment obligation of the borrower; or (ii) has a monthly payment obligation of $0. (B) A month in which the borrower receives a deferment or forbearance of repayment under any of the following: (i) A cancer treatment deferment under section 455(f)(3). (ii) A rehabilitation training program deferment. (iii) An unemployment deferment. (iv) An economic hardship deferment, which includes volunteer service in the Peace Corps as an economic hardship condition. (v) A military service deferment. (vi) A post-active duty student deferment. (vii) A national service forbearance. (viii) A National Guard duty forbearance. (ix) A Department of Defense Student Loan Repayment forbearance. (x) An administrative forbearance under a period\u2014 (I) during which the Secretary has authorized forbearance due to a national military mobilization or other local or national emergency; (II) necessary for the Secretary to collect and process documentation supporting the borrower's request for a deferment, forbearance, change in repayment plan, or consolidation loan; or (III) determined necessary by the Secretary. (xi) A bankruptcy forbearance if the borrower made the required payments on a confirmed bankruptcy plan. (C) A month in which the borrower receives a deferment or forbearance of repayment not described in subparagraph (B), but for which the borrower makes an additional payment equal to or greater than their monthly payment obligation (including a monthly payment obligation of $0), for a deferment or forbearance that ended within 3 years of the date of such additional payment and occurred on or after the date that is 180 days after the date of enactment of the Savings Opportunity and Affordable Repayment Act . (D) A month in which the borrower\u2014 (i) makes a payment pursuant to a repayment plan under section 493C or section 455(d)(1)(E), or another income continent repayment plan under section 455(d)(1)(D), or had a monthly payment obligation under such a plan of $0; (ii) makes a payment under the standard repayment plan, as described in section 428(b)(9)(A)(i); or (iii) makes a payment under a repayment plan with payments that are as least as much as they would have been under the standard repayment plan, as described in section 428(b)(9)(A)(i). (7) A borrower who is repaying an eligible loan pursuant to this section may elect, at any time, to terminate repayment pursuant to this section and repay such loan under any other repayment plan for which the borrower is eligible. (8) A borrower who is repaying an eligible loan pursuant to this section may\u2014 (A) pay in multiple installments that equal the full scheduled monthly payment obligation of such borrower; or (B) pay a lump sum or monthly payment amount that is equal to or greater than the full scheduled monthly payment obligation of such borrower in advance of the borrower's scheduled payment due date for a period of months not to exceed the period from the Secretary's receipt of the payment until the borrower's next annual repayment plan recertification date. (c) Eligibility determinations (1) In general The Secretary shall establish procedures for annually determining the borrower's eligibility for repayment under this section, including verification of a borrower's annual income and the annual amount due on the total amount of eligible loans, and such other procedures as are necessary to effectively implement repayment under this section. (2) Procedures for eligibility The Secretary shall\u2014 (A) consider, but is not limited to, the procedures established in accordance with section 455(e)(1); and (B) carry out, with respect to borrowers of any eligible loan, procedures for repayment plans that are equivalent to the procedures carried out under section 455(e)(8) with respect to other income contingent repayment plans. (3) Failure to timely certify information If the Secretary requires information from the borrower to recalculate the borrower's monthly payment obligation under this section, and the borrower does not provide the necessary documentation to the Secretary by the time the Secretary requires such documentation, the Secretary shall remove the borrower from the Savings Opportunity and Affordable Repayment plan under this section and place the borrower on an alternative repayment plan under which the borrower's required monthly payment is the amount the borrower would have paid on a 10-year standard repayment plan based on the current eligible loan balances and interest rates on the eligible loans at the time the borrower is removed from the plan under this section. (4) Procedures (A) Approval for the disclosure of tax information A borrower shall provide approval for the disclosure of applicable tax information to the Secretary to initially enter repayment, or recertify the borrower's intent to repay, under this section either as part of the process of completing a Direct Loan Master Promissory Note or a Direct Consolidation Loan Application and Promissory Note in accordance with sections 455(e)(8) and 493C(c)(2) or on an application form approved by the Secretary. (B) Failure to provide approval If a borrower does not provide approval for the disclosure of applicable tax information pursuant to subparagraph (A), the borrower shall provide documentation of the borrower\u2019s income and family size to the Secretary. (C) Inability to obtain information from the IRS If the Secretary has received approval for disclosure of applicable tax information pursuant to subparagraph (A), but cannot obtain the borrower\u2019s income and family size from the Internal Revenue Service, the borrower and, if applicable, the borrower\u2019s spouse, shall provide documentation of income and family size to the Secretary. (D) Calculation of payment amount After the Secretary obtains sufficient information to calculate the borrower\u2019s monthly payment obligation, the Secretary shall\u2014 (i) calculate the borrower\u2019s monthly payment obligation; and (ii) establish the 12-month period during which the borrower will be obligated to make payments in the amount of the monthly payment obligation. (E) Repayment disclosure The Secretary shall send to each borrower a repayment disclosure that\u2014 (i) specifies the borrower\u2019s calculated monthly payment obligation; (ii) explains how the payment was calculated; (iii) informs the borrower of the terms and conditions of repayment under this section; and (iv) informs the borrower of how to contact the Secretary if the calculated monthly payment obligation amount is not reflective of the borrower\u2019s current income or family size. (F) Request for recalculation (i) In general If a borrower believes that the calculated monthly payment obligation amount is not reflective of the borrower\u2019s current income or family size, the borrower may request that the Secretary recalculate the monthly payment obligation amount. (ii) Alternative documentation To support a request under clause (i), the borrower shall submit alternative documentation of income or family size not based on tax information to account for circumstances such as a decrease in income since the borrower last filed a tax return, the borrower\u2019s separation from a spouse with whom the borrower had previously filed a joint tax return, the birth or impending birth of a child, or other comparable circumstances. (G) Forbearance If a borrower provides alternative documentation under subparagraph (F) or if the Secretary receives documentation from the borrower or the borrower's spouse under subparagraph (C), the Secretary shall grant forbearance to provide time for the Secretary to recalculate the borrower\u2019s monthly payment obligation based on the documentation. (H) 3 monthly payments remaining Once a borrower has 3 monthly payments remaining under a 12-month period specified under subparagraph (D), the Secretary shall follow the procedures described in subparagraphs (C) through (G). (I) Resetting of 12-month period At any point during a 12-month period specified under subparagraph (D), a borrower may request that the Secretary recalculate the borrower\u2019s monthly payment obligation earlier than would have otherwise been the case to account for a change in the borrower\u2019s circumstances, such as a loss of income or employment or divorce. In such a case, the 12-month period specified under subparagraph (D) shall be reset based on the borrower\u2019s new information. (J) Tracking forgiveness The Secretary shall track a borrower\u2019s progress toward eligibility for loan cancellation under subsection (b)(5) and cancel loans that meet the criteria under such subsection without the need for an application or documentation from the borrower. (d) Married borrowers (1) Calculation based solely on borrower's information In the case of a married borrower, the Secretary shall calculate the amount of the borrower's monthly payment obligation under this section solely on the basis of the borrower's eligible loan debt and adjusted gross income (as defined in section 62 of the Internal Revenue Code of 1986) if\u2014 (A) the borrower files a separate Federal income tax return; or (B) the borrower files a joint Federal income tax return and certifies that the borrower is currently separated from the borrower's spouse or is currently unable to reasonably access the spouse's income. (2) Calculation including spouse's information In the case of a married borrower not described in subparagraph (A) or (B), the Secretary shall\u2014 (A) include the spouse's income in the calculation of the borrower's monthly payment obligation under this section; and (B) if the spouse has eligible loan debt, adjust the borrower's monthly payment obligation under this section by\u2014 (i) dividing the outstanding principal and interest balance of the borrower's eligible loans by the couple's combined outstanding principal and interest balance on eligible loans; and (ii) multiplying the borrower's payment amount as calculated under subsection (a)(5) by the percentage determined under clause (i). ; and\n**(5)**\nin section 494(a)(2)(A)\u2014\n**(A)**\nin the matter preceding clause (i), by inserting or a Savings Opportunity and Affordable Repayment plan for a loan under part B after part D ; and\n**(B)**\nin clause (ii)(I), by inserting or section 493E(c)(2)(B) after section 493C(c)(2)(B) .",
      "versionDate": "2026-04-23",
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
        "actionDate": "2025-04-01",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1220",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Savings Opportunity and Affordable Repayment Act",
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
        "name": "Education",
        "updateDate": "2026-05-13T20:17:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-23",
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
          "measure-id": "id119hr8475",
          "measure-number": "8475",
          "measure-type": "hr",
          "orig-publish-date": "2026-04-23",
          "originChamber": "HOUSE",
          "update-date": "2026-05-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8475v00",
            "update-date": "2026-05-18"
          },
          "action-date": "2026-04-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Savings Opportunity and Affordable Repayment Act</strong></p><p>This bill creates a new income-driven repayment plan for student loans\u00a0called the Savings Opportunity and Affordable Repayment (SOAR) plan. The SOAR plan has similar provisions to, but further expands on, the Department of Education's (ED's) final rule published on July 10, 2023, that created the Saving on a Valuable Education (SAVE) plan. The SAVE plan was blocked by federal courts.</p><p>The bill directs ED to carry out a SOAR plan program that complies with specified requirements. The bill allows all federal student loan types to be eligible for repayment under\u00a0the SOAR plan, including Parent PLUS Loans and Federal Family Education Loans.</p><p>Under the SOAR plan, a federal student loan borrower whose income is at or below 250% of the federal poverty level (FPL) has $0 monthly payments. A borrower whose income is over 250% of the FPL pays 5% of their discretionary income on loans obtained for undergraduate study and 10% of their discretionary income\u00a0for all other outstanding loans (e.g., loans obtained for graduate study).</p><p>Additionally, under the SOAR plan, holders of eligible federal student loans (e.g., ED or private lenders) must apply 50% of the borrower's monthly payment toward outstanding principal. The other 50% must be applied in the following order: (1) accrued charges and collection costs on the loan, (2) outstanding interest, and (3) outstanding principal.</p><p>ED must forgive any loan balance that remains outstanding after a specified maximum repayment period (e.g., 10 years or 15 years).</p>"
        },
        "title": "Savings Opportunity and Affordable Repayment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8475.xml",
    "summary": {
      "actionDate": "2026-04-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Savings Opportunity and Affordable Repayment Act</strong></p><p>This bill creates a new income-driven repayment plan for student loans\u00a0called the Savings Opportunity and Affordable Repayment (SOAR) plan. The SOAR plan has similar provisions to, but further expands on, the Department of Education's (ED's) final rule published on July 10, 2023, that created the Saving on a Valuable Education (SAVE) plan. The SAVE plan was blocked by federal courts.</p><p>The bill directs ED to carry out a SOAR plan program that complies with specified requirements. The bill allows all federal student loan types to be eligible for repayment under\u00a0the SOAR plan, including Parent PLUS Loans and Federal Family Education Loans.</p><p>Under the SOAR plan, a federal student loan borrower whose income is at or below 250% of the federal poverty level (FPL) has $0 monthly payments. A borrower whose income is over 250% of the FPL pays 5% of their discretionary income on loans obtained for undergraduate study and 10% of their discretionary income\u00a0for all other outstanding loans (e.g., loans obtained for graduate study).</p><p>Additionally, under the SOAR plan, holders of eligible federal student loans (e.g., ED or private lenders) must apply 50% of the borrower's monthly payment toward outstanding principal. The other 50% must be applied in the following order: (1) accrued charges and collection costs on the loan, (2) outstanding interest, and (3) outstanding principal.</p><p>ED must forgive any loan balance that remains outstanding after a specified maximum repayment period (e.g., 10 years or 15 years).</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr8475"
    },
    "title": "Savings Opportunity and Affordable Repayment Act"
  },
  "summaries": [
    {
      "actionDate": "2026-04-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Savings Opportunity and Affordable Repayment Act</strong></p><p>This bill creates a new income-driven repayment plan for student loans\u00a0called the Savings Opportunity and Affordable Repayment (SOAR) plan. The SOAR plan has similar provisions to, but further expands on, the Department of Education's (ED's) final rule published on July 10, 2023, that created the Saving on a Valuable Education (SAVE) plan. The SAVE plan was blocked by federal courts.</p><p>The bill directs ED to carry out a SOAR plan program that complies with specified requirements. The bill allows all federal student loan types to be eligible for repayment under\u00a0the SOAR plan, including Parent PLUS Loans and Federal Family Education Loans.</p><p>Under the SOAR plan, a federal student loan borrower whose income is at or below 250% of the federal poverty level (FPL) has $0 monthly payments. A borrower whose income is over 250% of the FPL pays 5% of their discretionary income on loans obtained for undergraduate study and 10% of their discretionary income\u00a0for all other outstanding loans (e.g., loans obtained for graduate study).</p><p>Additionally, under the SOAR plan, holders of eligible federal student loans (e.g., ED or private lenders) must apply 50% of the borrower's monthly payment toward outstanding principal. The other 50% must be applied in the following order: (1) accrued charges and collection costs on the loan, (2) outstanding interest, and (3) outstanding principal.</p><p>ED must forgive any loan balance that remains outstanding after a specified maximum repayment period (e.g., 10 years or 15 years).</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr8475"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8475ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Savings Opportunity and Affordable Repayment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:38:29Z"
    },
    {
      "title": "Savings Opportunity and Affordable Repayment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:38:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to provide for a Savings Opportunity and Affordable Repayment plan as an income contingent repayment plan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:33:25Z"
    }
  ]
}
```
