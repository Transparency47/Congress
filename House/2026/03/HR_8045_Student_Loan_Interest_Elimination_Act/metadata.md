# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8045
- Title: Student Loan Interest Elimination Act
- Congress: 119
- Bill type: HR
- Bill number: 8045
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-04-28T08:06:27Z
- Update date including text: 2026-04-28T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-24 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-24 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8045",
    "number": "8045",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001069",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Courtney, Joe [D-CT-2]",
        "lastName": "Courtney",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Student Loan Interest Elimination Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:27Z",
    "updateDateIncludingText": "2026-04-28T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-24T16:02:40Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "DC"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "PA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8045ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8045\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Mr. Courtney (for himself and Ms. Norton ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Higher Education Act of 1965 to eliminate interest on student loans, establish the Education Affordability Trust Fund, increase annual and aggregate loan limits, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Student Loan Interest Elimination Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTitle I\u2014Loan modification and refinancing for existing Federal student loans\nSec. 101. Program authority.\nSec. 102. Program for the loan\n                        modification of eligible Federal direct loans, and refinancing of other\n                        Federal student loan.\nTitle II\u2014Terms and conditions for new Federal student loans\nSec. 201. Applicable rates of interest for loans made on or after July 1, 2026.\nSec. 202. Termination of interest subsidized loans.\nSec. 203. Annual and aggregate loan limits.\nTitle III\u2014Trust Fund\nSec. 301. Supplemental Federal Pell Grant Program.\nSec. 302. Use of funds from the repayment of Federal student loans.\nSec. 303. Education Affordability Trust Fund.\nTitle IV\u2014General Provisions\nSec. 401. Implementation.\nI\nLoan modification and refinancing for existing Federal student loans\n#### 101. Program authority\nSection 451(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1087a(a) ) is amended\u2014\n**(1)**\nby striking There are hereby made available and inserting After using funds available from the Education Affordability Trust Fund in accordance with section 494A, there are hereby made available ;\n**(2)**\nby striking and (2) and inserting (2) ; and\n**(3)**\nby inserting ; and (3) to make loans under section 460A(b) after section 459A .\n#### 102. Program for the loan modification of eligible Federal Direct loans, and refinancing of other Federal student loans\n##### (a) Loan modification and refinancing\nPart D of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1087a et seq. ) is amended by adding at the end the following:\n460A. Program for the loan modification of eligible Federal Direct loans, and refinancing of other Federal student loans (a) Federal Direct Loan Modification The Secretary shall establish and implement, with respect to each borrower of an eligible Federal direct loan, procedures to\u2014 (1) modify, without any action from the borrower, the terms of such loan so that beginning on July 1, 2026, no interest shall accrue on such loan; and (2) allow the borrower, at any time, to opt out of the loan modification under paragraph (1) for such loan. (b) Refinancing eligible non-Federal direct loans as Federal Direct Consolidation Loans (1) In general The Secretary shall establish and implement, with respect to each borrower of an eligible non-Federal direct loan, procedures to\u2014 (A) refinance such loan in accordance with procedures listed in paragraph (2); and (B) allow the borrower, at any time, to opt out of the loan refinancing under subparagraph (A) for such loan. (2) Procedures In refinancing an eligible non-Federal direct loan with respect to a borrower of such loan, the Secretary shall carry out the following: (A) The Secretary shall make a Federal Direct Consolidation Loan under this subsection, in an amount equal to the sum of the unpaid principal, accrued unpaid interest, and late charges of the eligible non-Federal direct loan. (B) The Secretary shall pay the proceeds of such Federal Direct Consolidation Loan to the holder of the eligible non-Federal direct loan, in order to discharge the borrower from any remaining obligation with respect to such eligible non-Federal direct loan. (3) Terms and conditions of refinanced loans (A) In general A Federal Direct Consolidation Loan made under this subsection shall have the same terms and conditions as a Federal Direct Consolidation Loan that was not made under this subsection, except\u2014 (i) notwithstanding any other provision of this title, a borrower of a Federal Direct Consolidation Loan made under this subsection may repay such loan under any repayment plan or program described in section 455(d)(1); (ii) that the Secretary may adjust such terms and conditions as necessary to enable the borrower to access loan forgiveness or other benefits available to the borrower under the loan before refinancing under this subsection, in any case where such benefits are more generous than provided under a Federal Direct Consolidation Loan under this subsection; and (iii) as otherwise provided in this subsection. (B) No origination fees Notwithstanding section 455(c), the Secretary may not charge a borrower of a loan made under this subsection an origination fee for such loan. (C) Interest rates No interest shall accrue on a loan that is made under this subsection. (D) No automatic extension of repayment period A loan made under this subsection shall not result in the extension of the duration of the repayment period of the original loan, and the borrower shall retain the same repayment term that was in effect on the original loan. Nothing in this paragraph shall be construed to prevent a borrower from electing a different repayment plan at any time in accordance with section 455(d)(3). (E) Rule of construction Nothing in this section shall be construed to prevent a borrower of a Federal student loan described in subparagraph (B) or (C) of subsection (d)(2) from consolidating such loans with other loans eligible for consolidation under this section, or to require such a borrower to consolidate such loans with other Federal student loans into a single consolidation loan under this section. (c) Report Not later than 1 year after the date of the enactment of the Student Loan Interest Elimination Act , and on an annual basis thereafter, the Secretary shall submit a report to the authorizing committees that includes\u2014 (1) the total number of borrowers whose loans have been modified or refinanced under this section during the preceding year; and (2) the number of such borrowers who are delinquent in making payments on such a loan. (d) Definitions In this section: (1) Eligible Federal direct loan The term eligible Federal direct loan means\u2014 (A) a loan made under this part, and first disbursed before July 1, 2026; (B) a loan made, insured, or guaranteed under part B, and which is held by the Secretary; (C) a loan made under part E, and which is held by the Secretary; or (D) a loan made under subpart 1 of part A of title VII of the Public Health Service Act ( 42 U.S.C. 292 et seq. ), and which is held by the Secretary. (2) Eligible non-Federal direct loan The term eligible non-Federal direct loan means a loan\u2014 (A) made, insured, or guaranteed under part B, and which is not held by the Secretary; (B) made under part E, and which is not held by the Secretary; or (C) made under\u2014 (i) subpart I of part A of title VII of the Public Health Service Act ( 42 U.S.C. 292 et seq. ), and which is not held by the Secretary; (ii) subpart II of part A of title VII of the Public Health Service Act ( 42 U.S.C. 292q et seq. ), and in the case of a loan made under section 723 of such Act ( 42 U.S.C. 292s ), only if the borrower of the loan has completed the full period of service, practice, or training that was imposed as a condition on receipt of such loan; or (iii) part E of title VIII of the Public Health Service Act ( 42 U.S.C. 297a et seq. ), and in the case of a loan made under section 846A of such Act ( 42 U.S.C. 297n\u20131 ), only if the borrower has completed the 4 years of full-time employment as a faculty member at a school of nursing as described in subsection (c)(3) of such section 846A. (3) Original loan The term original loan , used with respect to a Federal Direct Consolidation Loan made under subsection (b), means a loan for which a borrower's liability is discharged by such Federal Direct Consolidation Loan. .\n##### (b) Income-Contingent repayment\nSection 455(e) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(e) ) is amended by adding at the end the following new paragraph:\n(9) Special rule for refinanced loans For purposes of paragraph (7), the period of time during which a borrower of a Federal Direct Consolidation Loan made under section 460A(b) has made monthly payments shall be calculated in the manner described in section 493C(f). .\n##### (c) Repayment Assistance Plan\nSection 455(q)(1) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(q)(1) ) is amended by adding at the end the following:\n(H) For purposes of subparagraph (E), the period of time during which a borrower of a Federal Direct Consolidation Loan made under section 460A(b) has made monthly payments shall be calculated in the manner described in section 493C(f). .\n##### (d) Income-Based repayment\n**(1) Exclusion from Excepted Consolidation Loan**\nSection 493C(a)(2)(B) of the Higher Education Act of 1965 ( 20 U.S.C. 1098e(a)(2)(B) ) is amended by inserting a Federal Direct Consolidation Loan under section 460A, and does not include after does not include .\n**(2) Calculation of qualifying payments**\nSection 493C of the Higher Education Act of 1965 ( 20 U.S.C. 1098e ) is amended by adding at the end the following:\n(f) Special rule for refinanced loans (1) Refinanced Federal Direct Consolidation Loans In calculating the period of time during which a borrower of a Federal Direct Consolidation Loan that is made under section 460A(b) has made monthly payments for the purposes of subsection (b)(7), the Secretary shall\u2014 (A) review the borrower\u2019s payment history to identify each component loan of such Federal Direct Consolidation Loan; (B) for each such component loan\u2014 (i) calculate the weighted factor of the component loan, which shall be the factor that represents the portion of such Federal Direct Consolidation Loan that is attributable to such component loan; and (ii) determine the number of qualifying monthly payments made on such component loan before consolidation; (C) calculate the number of qualifying monthly payments determined under subparagraph (B)(ii) with respect to a component loan that shall be deemed as qualifying monthly payments made on the Federal Direct Consolidation Loan by multiplying\u2014 (i) the weighted factor of such component loan as determined under subparagraph (B)(i); by (ii) the number of qualifying monthly payments made on such component loan as determined under subparagraph (B)(ii); and (D) calculate and inform the borrower of the total number of qualifying monthly payments with respect to the component loans of the Federal Direct Consolidation Loan that shall be deemed as qualifying monthly payments made on the refinanced Federal Consolidation Loan, by\u2014 (i) adding together the result of each calculation made under subparagraph (C) with respect to each such component loan; and (ii) rounding the number determined under clause (i) to the nearest whole number. (2) Component loan defined In this subsection, the term component loan , used with respect to a Federal Direct Consolidation Loan, means a loan for which the liability was discharged by the proceeds of such Federal Direct Consolidation Loan. .\n##### (e) Conforming amendments\nThe Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) is amended\u2014\n**(1)**\nin section 455(d)(1), by striking shall offer a borrower of a loan and inserting shall offer a borrower of a Federal Direct Consolidation Loan under section 460A (with respect to the Federal Direct Consolidation Loan under such section only, and without regard to when other loans may have been received), and shall offer a borrower of a loan ;\n**(2)**\nin section 455(d)(7)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking Beginning and inserting Subject to subparagraph (F), beginning ;\n**(B)**\nin subparagraph (C), by striking A borrower is required and inserting Subject to subparagraph (F), a borrower is required ;\n**(C)**\nin subparagraph (E)(ii)(II), by inserting (excluding such loans under section 460A) after a Federal Direct Consolidation Loan ; and\n**(D)**\nby adding at the end the following:\n(F) Consolidation Loans under section 460A Notwithstanding any other provision of this title, including this subsection, a borrower of a Federal Direct Consolidation Loan under section 460A shall be eligible to repay the Federal Direct Consolidation Loan under such section only under any repayment plan or program described under paragraph (1), without regard to when other loans may have been received. ; and\n**(3)**\nin section 428C(a)(3)(B)(i)(V) ( 20 U.S.C. 1078\u20133(3)(B)(i)(V) )\u2014\n**(A)**\nby striking the period at the end of item (cc) and inserting a semicolon;\n**(B)**\nby striking the period at the end of item (dd) and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(ee) for the purpose of obtaining a Federal Direct Consolidation Loan under section 460A(b). .\nII\nTerms and conditions for new Federal student loans\n#### 201. Applicable rates of interest for loans made on or after July 1, 2026\nSection 455(b)(8) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(b)(8) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting and before July 1, 2026 after July 1, 2013 ;\n**(2)**\nin subparagraph (A), by inserting and before July 1, 2026 after July 1, 2013 ;\n**(3)**\nin subparagraph (B), by inserting and before July 1, 2026 after July 1, 2013 ;\n**(4)**\nin subparagraph (C), by inserting and before July 1, 2026 after July 1, 2013 ;\n**(5)**\nin subparagraph (D), by inserting and before July 1, 2026 after July 1, 2013 ;\n**(6)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(7)**\nby inserting after subparagraph (E) the following:\n(F) New loans on or after July 1, 2026 Notwithstanding the preceding subparagraphs of this paragraph, for Federal Direct Unsubsidized Stafford Loans, Federal Direct PLUS Loans, and Federal Direct Consolidation Loans for which the first disbursement is made, or the application is received, on or after July 1, 2026, the applicable rate of interest shall be 0 percent on the unpaid principal balance of the loan. .\n#### 202. Termination of interest subsidized loans\n##### (a) Program authority\nSection 451(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1087a(a) ) is amended by adding at the end the following: No new Federal Direct Stafford Loans, as referenced under section 455(a)(2)(A), may be made under this part after June 30, 2026, and no funds are authorized to be appropriated, or may be expended, under this Act or any other Act to make such Federal Direct Stafford Loans for which the first disbursement is after June 30, 2026. .\n##### (b) Termination of authority\nSection 455(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(a) ) is amended by adding at the end the following:\n(9) Termination of authority to make interest subsidized loans to any student Notwithstanding any provision of this part or part B, for any period of instruction beginning on or after July 1, 2026\u2014 (A) a student shall not be eligible to receive a Federal Direct Stafford Loan under this part; and (B) the maximum annual amount of Federal Direct Unsubsidized Stafford Loans such a student may borrow in any academic year (as defined in section 481(a)(2)) or its equivalent shall be the maximum annual amount for such student determined under section 428H, plus an amount equal to the amount of Federal Direct Stafford Loans the student would have received in the absence of this paragraph. .\n#### 203. Annual and aggregate loan limits\nSection 455(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(a) ) is amended\u2014\n**(1)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (A), in the matter preceding clause (i), by striking and (8) and inserting , (8), and (9) ; and\n**(B)**\nin subparagraph (B), in the matter preceding clause (i), by striking and (8) and inserting , (8), and (9) ;\n**(2)**\nin paragraph (6), by striking paragraph (8) and inserting paragraphs (8) and (9) ; and\n**(3)**\nby adding at the end the following:\n(9) Adjustment for inflation (A) In general Each amount specified in paragraphs (4) and (6) shall, for any period of instruction beginning on or after July 1, 2027, be deemed increased by a percentage equal to the annual adjustment percentage. (B) Annual adjustment percentage defined In this paragraph, the term annual adjustment percentage , as applied to an academic year, means the estimated percentage change in the Consumer Price Index (as determined by the Secretary, using the definition in section 478(f) or the most recent calendar year ending prior to the beginning of that academic year). .\nIII\nTrust Fund\n#### 301. Supplemental Federal Pell Grant Program\nSection 401(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1070a(b) ) is amended by adding at the end the following:\n(10) Supplemental Pell Grants using excess Trust fund amounts For any award year for which the Secretary elects to use the excess amounts (or a portion of such excess amounts) described in section 494A(c) to carry out a Supplemental Pell Grant Program under this paragraph, the Secretary shall\u2014 (A) award each student that receives a Federal Pell Grant under this subpart for such award year, an additional Federal Pell Grant in an amount that\u2014 (i) bears the same relationship to such excess amount (or such portion) as the amount of the Federal Pell Grant such student receives under this subpart (excluding this paragraph) for such award year bears to the total amount awarded in Federal Pell Grants under this subpart (excluding this paragraph) for such award year; and (ii) may\u2014 (I) exceed the total maximum Federal Pell Grant available for such award year; and (II) be lower than the minimum Federal Pell Grant (as defined in section (a)(2)(F)) for such award year; and (B) ensure that\u2014 (i) in the case of a student awarded an additional Federal Pell Grant under subparagraph (A) for an award year, the total amount of Federal Pell Grants awarded to such student under this subpart (including such additional Federal Pell Grant) for such award year may exceed the total maximum Federal Pell Grant available for such award year; and (ii) any period of study covered by an additional Federal Pell Grant awarded under subparagraph (A) shall not be included in determining a student\u2019s duration limit under subsection (d)(5). .\n#### 302. Use of funds from the repayment of Federal student loans\nPart G of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1088 et seq. ) is amended by adding at the end the following:\n494A. Use of funds from the repayment of Federal student loans (a) In general The Secretary of Education shall, without further appropriation, deposit all amounts repaid on loans made, insured, or guaranteed under this title into the Education Affordability Trust Fund established under section 494B (referred to in this section as the Trust Fund ). (b) Use of Trust Fund assets (1) In general The Trust Fund Board shall transfer the assets from the investments of the Trust Fund to the Secretary of Education, to pay for the administrative costs of the Department of Education in making loans under part D, including loans under section 460A(b), to all eligible students (and the eligible parents of such students) in attendance at participating institutions of higher education selected by the Secretary, to enable such students to pursue their courses of study at such institutions, in the following amounts: (A) During any period of time when the Trust Fund has assets under management of $500,000,000 or more over a 180-day period, 100 percent of such assets. (B) During any period of time when the Trust Fund has assets of less than $500,000,000, but more than or equal to $400,000,000 over a 180-day period, 40 percent of such assets. (C) During any period of time when the Trust Fund has assets of less than $400,000,000 but more than or equal to $300,000,000 over a 180-day period, 10 percent of such assets. (D) During any period of time when the Trust Fund has assets of less than $300,000,000 over a 180-day period, 0 percent of such assets. (2) Assets defined In this subsection, the term assets means the amount that the return on investment from bond investments made by the Trust Fund exceeds the amount repaid on loans and deposited into the Trust Fund under subsection (a). (c) Use of excess amounts If the amounts required to be transferred under subsection (b) are in excess of the amounts needed to pay for the costs of the Department of Education described under subsection (b), the Secretary of Education may elect to use such excess amounts (or a portion of such excess amounts)\u2014 (1) to carry out the Supplemental Federal Pell Grant Program under section 401(b)(10); and (2) for the Postsecondary Student Success Program authorized under part B of title VII and for which the Department issued a notice inviting applications in the Federal Register on August 12, 2022 (87 Fed. Reg. 49811 et seq.), except that, notwithstanding the terms and condition of such program described in the notice\u2014 (A) any institution of higher education defined in section 101 or 102(a)(1)(B) is eligible to receive a grant under the program if\u2014 (i) the average cost of tuition to attend such institution for the 3 most recent academic years has not increased by more than 3 percent; (ii) the institution provides an assurance that the average cost of tuition to attend such institution for the succeeding 3 academic years will not increase by more than 3 percent; or (iii) the size of the endowment fund (as defined in section 312(c)) of the institution on the first day of the previous calendar year was not greater than $100,000,000; and (B) grants under the program will be awarded on a competitive basis, and the amount of any such grant will be not less than $600,000, and not more than $1,000,000. (d) Report and testimony to Congress If the Secretary of Education elects to use excess amounts described under subsection (c), the Secretary shall provide to Congress a report on the use of such amounts (and provide testimony on such use) not later than 180 days after making use of such funds. .\n#### 303. Education Affordability Trust Fund\nPart G of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1088 et seq. ) is further amended by adding at the end the following:\n494B. Education Affordability Trust Fund (a) Establishment There is established within the Department a trust fund to be known as the Education Affordability Trust Fund (referred to in this section as the Trust Fund ). (b) Board (1) In general The head of the Trust Fund shall be a 6-member Education Affordability Trust Fund Board (referred to in this section as the Board ). (2) Appointment of members The members of the Board shall be appointed by the President, by and with the advice and consent of the Senate, from among individuals who\u2014 (A) have experience and expertise in the management of financial investments; (B) have at least 10 years of experience in the financial investment field; (C) at least 3 of which have experience working with rural lenders, historically disenfranchised groups, or low-income communities; and (D) are not currently an elected official. (3) Disqualifications for appointments (A) Lobbying No individual required to register as a lobbyist under section 4 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1603 ) may be appointed to, or serve on, the Board. (B) Incompatible office No member of the Board may hold or may have held the position of Member of the House of Representatives or Senator, may hold the position of officer or employee of the House of Representatives, Senate, or instrumentality or other entity of the legislative branch, or may have held such a position within 4 years of the date of appointment. (4) Term (A) In general The members of the Board shall serve 6-year terms, staggered such that the terms of 2 members end every 2 years. (B) Political affiliation The 2 members serving terms that end at the same time may not be members of the same political party. (C) Members take office together With respect to the 2 individuals appointed to fill terms ending at the same time, neither individual may begin serving as a member of the Board until both have been appointed and confirmed by the Senate. (D) Authority to serve until a successor is appointed Upon the expiration of a term of a member of the Board, that member shall continue to serve until a successor is appointed. (E) Limitation An individual may only serve as a member of the Board for a maximum of 2 terms. (F) Removal for cause The President may remove a member of the Board only for inefficiency, neglect of duty, or malfeasance in office. (5) Deadline for initial appointments The initial members of the Board shall be appointed no later than 90 days after the date of enactment of this section. (6) Chair Each member of the Board shall serve as the Chair of the Board during the final year of the term for which the member is appointed. (7) Conflicts of interest Each member of the Board shall, with respect to entities in which the Trust Fund invests, either divest any interest in such entities or place such interests into a blind trust. (8) Meetings (A) In general The Board shall meet no less than once per quarter. (B) Participation by fund managers The fund manager appointed under subsection (c) shall attend not less than 2 meetings of the Board each year, to discuss forecasting and current investment performance. (C) Emergency meeting requirement If, once the assets under management of the Trust Fund have reached $500,000,000,000, the assets under management of the Trust Fund drop below $300,000,000,000, the Board shall immediately hold an emergency meeting to discuss ensuring the long-term solvency of the Trust Fund. (9) Voting Investment guidelines shall be adopted by a unanimous vote of the entire Board. All other decisions of the Board shall be decided by a majority vote. All decisions of the Board shall be entered upon the records of the Board. (10) Compensation While serving on the business of the Board (including travel time), a member of the Board shall be entitled to compensation at the per diem equivalent of the rate provided for level IV of the Executive Schedule under section 5315 of title 5, United States Code, and while so serving away from home and the member\u2019s regular place of business, a member may be allowed travel expenses, as authorized by the Chair of the Board. (c) Powers and responsibilities of the Board (1) Appointment of fund managers (A) In general The Board shall appoint independent fund managers from among individuals who have met such ethics vetting requirements as the Board may establish. (B) Failure to make a unanimous appointment If the Board fails to make an appointment under subparagraph (A), the Chair shall, not later 10 days after the date of such failure, make the appointment. (C) Initial fund managers The Board shall make the initial appointment of independent fund managers under subparagraph (A) not later than 60 days after the date on which all members of the Board are first appointed. (2) Other duties The Board shall\u2014 (A) retain independent advisers to assist it in the formulation and adoption of its investment guidelines; (B) pay the administrative expenses of the Trust Fund from the assets in the Trust Fund; and (C) discharge their duties (including the voting of proxies) with respect to the assets of the Trust Fund solely in the interest of the Trust Fund and through it, the participants and beneficiaries of the programs funded under this Act\u2014 (i) for the exclusive purpose of\u2014 (I) providing zero-interest Federal student loans to existing and future borrowers; and (II) defraying reasonable expenses of administering the functions of the Trust Fund; (ii) with the care, skill, prudence, and diligence under the circumstances then prevailing that a prudent person acting in a like capacity and familiar with such matters would use in the conduct of an enterprise of a like character and with like aims; (iii) by diversifying investments so as to minimize the risk of large losses and to avoid disproportionate influence over a particular industry or firm, unless under the circumstances it is clearly prudent not to do so; and (iv) in accordance with Trust Fund governing documents and instruments insofar as such documents and instruments are consistent with this Act. (3) Prohibitions with respect to members of the Board No member of the Board shall\u2014 (A) deal with the assets of the Trust Fund in the member\u2019s own interest or for the member\u2019s own account; (B) in an individual or in any other capacity act in any transaction involving the assets of the Trust Fund on behalf of a party (or represent a party) whose interests are adverse to the interests of the Trust Fund or the interests of borrowers; or (C) receive any consideration for the member\u2019s own personal account from any party dealing with the assets of the Trust Fund. (4) Audit and report (A) Audit The Board shall annually engage an independent qualified public accountant to audit the financial statements of the Trust Fund. (B) Report to Congress (i) In general The Board shall submit an annual management report to the Secretary of Education, the Secretary of the Treasury, the President, and the Congress not later than 180 days after the end of each fiscal year, including\u2014 (I) a statement of financial position, including the total amount in the Trust Fund; (II) a statement of operations; (III) a statement of cash flows; (IV) a breakdown of the investments made by the Trust Fund, including by type; (V) a statement on internal accounting and administrative control systems; (VI) the report resulting from an audit of the financial statements of the Trust Fund conducted under subparagraph (A); and (VII) any other comments and information necessary to inform the Congress about the operations and financial condition of the Trust Fund. (ii) Public availability of report The Board shall make each report required under this subparagraph available to the public, including on the website of the Department of Education. (5) Rules and administrative powers The Board shall have the authority to make rules to govern the operations of the Trust Fund, employ professional staff, and contract with outside advisers to provide legal, accounting, investment advisory, or other services necessary for the proper administration of this section. In the case of contracts with investment advisory services, compensation for such services may be on a fixed contract fee basis or on such other terms and conditions as are customary for such services. (6) Financial Disclosure Reports Each Member and employee of the Board shall file with the Secretary of Education and appropriate committees of Congress financial disclosure reports that comply with the requirements under subchapter I of chapter 131 of title 5, United States Code. (7) Funding The expenses of the Trust Fund and the Board incurred under this section shall be paid from the Trust Fund. (d) Duties of the fund managers (1) In general The fund managers shall invest the assets of the Trust Fund in a manner consistent with the investment guidelines adopted by the Board. (2) Instruments The fund managers shall invest the amounts in the Trust Fund in bonds that consist of the following: (A) Municipal bonds. (B) Bonds issued by the Department of the Treasury, which may not make up more than 40 percent of the total investments of the Trust Fund. (C) Other Federal bonds. (D) Bonds issued by the Federal Home Loan Mortgage Corporation, the Federal National Mortgage Association, or a Federal Home Loan Bank. (E) International bonds, which may not make up more than 10 percent of the total investments of the Trust Fund. (F) Corporate bonds, which may not make up more than 10 percent of the total investments of the Trust Fund. (3) Investment requirements (A) Ratings The investments of the Trust Fund shall consist\u2014 (i) only of investments rated at least Baa1 or BBB+ by Moody\u2019s, S&P, or Fitch Ratings; (ii) at least 80 percent of investments rated at least A3 or A- by Moody\u2019s, S&P, or Fitch Ratings; (iii) at least 60 percent of investments rated at least Aa1 or AA+ by Moody\u2019s, S&P, or Fitch Ratings; and (iv) at least 40 percent of investments rated at least Aaa or AAA by Moody\u2019s, S&P, or Fitch Ratings. (B) Diversification The investments of the Trust Fund shall be diversified to minimize the risk of large losses and to avoid disproportionate influence over a particular region, industry, or firm, unless under the circumstances it is clearly prudent not to do so. (C) Limitation on investing in certain countries The Trust Fund may not invest in entities or subsidiaries of entities that are\u2014 (i) based in any country that does not have diplomatic relations with the United States; (ii) based in any country, the government of which is subject to sanctions by the United States; or (iii) on a sanctions list of the Department of the Treasury. (4) Short-term initial investments During the 10-year period beginning on the date of enactment of this section, the fund managers shall prioritize investments in bonds with a maturity date of less than 10 years. (e) Means of financing For purposes of the Congressional Budget Act of 1974 ( 2 U.S.C. 621 et seq. ), the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 900 et seq. ), and chapter 11 of title 31, United States Code, and notwithstanding section 20 of Office of Management and Budget Circular No. A\u201311, or any successor thereto, earnings of the Trust Fund shall be calculated on an accrual basis. .\nIV\nGeneral Provisions\n#### 401. Implementation\nIn carrying out the amendments made by titles I, II, and III, the Secretary of Education may waive the application of\u2014\n**(1)**\nthe master calendar requirements under section 482 of the Higher Education Act of 1965 ( 20 U.S.C. 1089 ); and\n**(2)**\nnegotiated rulemaking under section 492 of the Higher Education Act of 1965 ( 20 U.S.C. 1098a ).",
      "versionDate": "2026-03-24",
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
        "actionDate": "2026-03-24",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4169",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Student Loan Interest Elimination Act",
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
        "updateDate": "2026-04-21T16:26:55Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8045ih.xml"
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
      "title": "Student Loan Interest Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T04:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Student Loan Interest Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to eliminate interest on student loans, establish the Education Affordability Trust Fund, increase annual and aggregate loan limits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T04:48:35Z"
    }
  ]
}
```
