# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2829?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2829
- Title: SERVICE Act
- Congress: 119
- Bill type: HR
- Bill number: 2829
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-05-14T08:08:31Z
- Update date including text: 2026-05-14T08:08:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2829",
    "number": "2829",
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
    "title": "SERVICE Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:31Z",
    "updateDateIncludingText": "2026-05-14T08:08:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:06:40Z",
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
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OR"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CT"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2829ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2829\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Courtney (for himself and Mr. DeSaulnier ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to improve the Public Service Loan Forgiveness program and reduce interest rates.\n#### 1. Short title\nThis Act may be cited as the Strengthening Efforts for Relief and Vital Incentives for Community Service and Engagement Act or the SERVICE Act .\n#### 2. Amendments to terms and conditions of public service loan forgiveness\n##### (a) Number of monthly payments\nParagraph (1) of section 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking a borrower who and inserting a borrower ;\n**(2)**\nby amending subparagraph (A) to read as follows:\n(A) who\u2014 (i) has made 96 qualifying monthly payments on the eligible Federal Direct Loan after October 1, 2007; and (ii) has been employed in a public service job during the period in which the borrower makes each of the 96 qualifying monthly payments; and ; and\n**(3)**\nby amending subparagraph (B) to read as follows:\n(B) without regard to the employment status of the borrower at the time of such cancellation. .\n##### (b) Redesignations\nSection 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ) is further amended by redesignating paragraphs (2), (3), and (4), as paragraphs (3), (6), and (7), respectively;\n##### (c) Monthly payments\nSection 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ) is further amended\u2014\n**(1)**\nby inserting after paragraph (1), as so amended, the following:\n(2) Monthly payments (A) Qualifying monthly payments For the purpose of determining under paragraph (1) the number of qualifying monthly payments made by a borrower on an eligible Federal Direct Loan, the Secretary shall consider the borrower to have made a qualifying monthly payment for each month that\u2014 (i) the borrower pays (as a lump sum or in multiple installments) an amount that is not less than the monthly payment amount due on the eligible Federal Direct Loan pursuant to any one or a combination of the following\u2014 (I) payments under an income-based repayment plan under section 493C; (II) payments under a standard repayment plan under subsection (d)(1)(A), based on a 10-year repayment period; (III) monthly payments under a repayment plan under subsection (d)(1) or (g) of not less than the monthly amount calculated under subsection (d)(1)(A), based on a 10-year repayment period; or (IV) payments under an income contingent repayment plan under subsection (d)(1)(D); or (ii) in lieu of a payment described in clause (i), the borrower is in one of the following periods of deferment or forbearance\u2014 (I) cancer treatment deferment under section 427(a)(2)(C)(iv), 428(b)(1)(M)(v), or 455(f)(3); (II) rehabilitation training program deferment under section 427(a)(2)(C)(i)(II), 428(b)(1)(M)(i)(II), or 455(f)(2)(A)(ii); (III) military service deferment under section 428(b)(1)(M)(iii) or 455(f)(2)(C); (IV) unemployment deferment under section 427(a)(2)(C)(ii), 428(b)(1)(M)(ii), 428B(d)(1)(A)(i), or 455(f)(2)(B); (V) deferment due to an economic hardship described in section 427(a)(2)(C)(iii), section 428(b)(1)(M)(iv), section 428B(d)(1)(A)(i), section 435(o), or section 455(f)(2)(D); (VI) Peace Corps service deferment under section 682.210(b)(2)(ii) or 682.210(k) of title 34, Code of Federal Regulations (or successor regulations), as made applicable to Direct Loan borrowers under section 685.204(j) of such title 34; (VII) post-active-duty student deferment under section 493D; (VIII) AmeriCorps forbearance under section 428(c)(3)(A)(i)(III); (IX) National Guard Duty forbearance under section 682.211(h)(2)(iii) or 685.205(a)(7) of title 34, Code of Federal Regulations (or successor regulations); (X) Department of Defense student loan repayment program forbearance under section 428(c)(3)(A)(i)(IV); (XI) administrative forbearance or mandatory administrative forbearance under section 428(c)(3)(D) or 428H(e)(7); or (XII) student loan debt burden forbearance under section 428(c)(3)(A)(i)(II). (B) Prepayments (i) In general Subject to clause (ii), if, for any month, a borrower makes a qualifying monthly payment on an eligible Federal Direct Loan in an amount that exceeds the monthly payment amount due on such loan for such month, the Secretary shall\u2014 (I) if the excess amount is less than the monthly payment amount due for the subsequent month on such loan, apply the excess amount toward the monthly payment amount due for such subsequent month; (II) if the excess amount is equal to the monthly payment amount due for the subsequent month on such loan, treat the excess amount as the monthly payment for such subsequent month; (III) if the excess amount is greater than the monthly payment amount due for the subsequent month on such loan, but less than the total monthly payment amounts due for the 2 subsequent months on such loan\u2014 (aa) treat the portion of the excess amount that covers the monthly payment amount due for the subsequent month as the monthly payment for such subsequent month; and (bb) apply the remainder of the excess amount toward the monthly payment amount due for the second subsequent month; (IV) if the excess amount is equal to or greater than the monthly payment amount due for the 2 subsequent months on such loan, but less than the total monthly payment amounts due for the 3 subsequent months on such loan\u2014 (aa) treat the portion of the excess amount that covers the monthly payment amounts due for the subsequent month and the second subsequent month as the monthly payments for such months; and (bb) apply any remainder of such excess amount toward the monthly payment amount due for the third subsequent month; (V) if the excess amount is equal to the monthly payment amounts due for the 3 subsequent months on such loan, treat the excess amount as the monthly payments for such months; (VI) if the excess amount is greater than the monthly payment amounts due for the 3 subsequent months on such loan\u2014 (aa) treat the portion of the excess amount that covers the monthly payment amounts due for the 3 subsequent months as the monthly payments for such months; and (bb) apply any remainder of such excess amount to the principal balance of the eligible Federal Direct loan; and (VII) notwithstanding subclauses (I) through (VI), if the borrower has a monthly payment amount due on such loan for such month that is equal to $0, apply any excess amount for such month to the principal balance of the eligible Federal Direct loan. (ii) Alternative application Prior to or at the time of making a payment that exceeds the monthly payment amount due on an eligible Federal Direct Loan for such month, a borrower may request that any excess amount for such month be applied to the principal balance of an eligible Federal Direct loan in lieu of such excess amount being applied in accordance with clause (i). (C) Buyback payment process (i) In general The Secretary shall establish a buyback payment process under which a qualified borrower of an eligible Federal Direct Loan may make a buyback payment in order to have eligible months of the borrower\u2019s public service employment period during which the borrower did not make a qualifying monthly payment on such loan be treated as if the borrower had made a qualifying monthly payment on such loan. (ii) Qualified borrower A borrower is a qualified borrower for the purposes of making a buyback payment in accordance with this subparagraph if the borrower\u2014 (I) has an eligible Federal Direct Loan that is not in default; (II) has been employed in a public service job for not less than a 96 month employment period, but during such employment period has made fewer than 96 qualifying monthly payments on an eligible Federal Direct Loan; and (III) requests to make a buyback payment in accordance with this subparagraph. (iii) Eligible month For the purposes of this subparagraph, an eligible month means a month during which a qualified borrower was employed in a public service job, was not in an in-school deferment or grace period, and did not make a qualifying monthly payment on an eligible Federal Direct Loan for such month\u2014 (I) because the borrower made a monthly payment on such eligible Federal Direct Loan pursuant to a repayment plan that is not a qualifying repayment plan; (II) because the borrower was in a period of deferment or forbearance other than a period described in clause (ii) of subparagraph (A); or (III) for another reason determined appropriate by the Secretary. (iv) Buyback payment requirements A buyback payment made in accordance with this subparagraph\u2014 (I) shall be made by a qualified borrower as a lump sum payment amount, and in an amount that equals the total amount the borrower would have paid in qualifying monthly payments on the eligible Federal Direct Loan for all eligible months the borrower is requesting to buyback, pursuant to a qualifying repayment plan applicable to the borrower, in accordance with section 685.219(g)(6) of title 34, Code of Federal Regulations (as such section is in effect on the date of enactment of this paragraph) or any other relevant regulations in effect on such date; (II) may not be made with respect to an eligible Federal Direct Loan that has been paid off, discharged, or cancelled; and (III) with respect to an eligible Federal Direct Loan that is a consolidation loan, may not be used to buyback eligible months that occurred before the date of the consolidation of such loan. (D) Hold harmless against retroactive determinations For purposes of determining under paragraph (1) the number of qualifying monthly payments made by a borrower, any payment or period of deferment or forbearance that is determined to be a qualifying monthly payment may not, at a later time, be determined not to be a qualifying monthly payment. ; and\n**(2)**\nin paragraph (6), as redesignated by section 2(b), by adding at the end the following:\n(C) Qualifying repayment plan The term qualifying repayment plan means any of the repayment plans listed in clause (i) of paragraph (2)(A). .\n##### (d) Loan cancellation\nParagraph (3) of section 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ), as redesignated by subsection (b), is amended to read as follows:\n(3) Loan cancellation amount Upon certification by a borrower of completion of 96 qualifying monthly payments by the borrower, the Secretary shall determine whether the borrower meets each of the requirements of paragraph (1), and\u2014 (A) if the Secretary determines that the borrower does meet such requirements, cancel the obligation to repay the balance of principal and interest due as of the time of such cancellation on the eligible Federal Direct Loans made to the borrower under this part, without further action by the borrower; or (B) if the Secretary determines that the borrower does not meet such requirements, notify the borrower of such determination in accordance with paragraph (4). .\n##### (e) Reconsideration process\nSection 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ), as redesignated by subsection (b), is further amended by inserting after paragraph (3), as so amended, the following:\n(4) Initial determination of ineligibility for loan cancellation In a case in which the Secretary determines that a borrower has not met the requirements of paragraph (1), the Secretary shall\u2014 (A) notify the borrower that\u2014 (i) the borrower\u2019s application has been denied, including the basis for such denial; (ii) the borrower is in a 90-day forbearance period described in subparagraph (B); and (iii) the Secretary will resume collection of the eligible Federal Direct Loans for which the borrower was seeking loan cancellation under this subsection after such 90-day forbearance period, unless the borrower opts to extend such forbearance period under paragraph (5)(A)(ii); and (B) grant the borrower a 90-day forbearance period, beginning on the date of the notice described in subparagraph (A) provided to the borrower, and during which\u2014 (i) payments of principal and interest need not be made on the eligible Federal Direct Loans for which the borrower was seeking loan cancellation under this subsection; and (ii) any interest accrued and not paid may not be capitalized. (5) Reconsideration process (A) Request for reconsideration Not later than 90 days after the date of the notice described in paragraph (4)(A) provided to the borrower\u2014 (i) the borrower may request, on a form approved by the Secretary, that the Secretary reconsider the basis for the Secretary\u2019s denial under paragraph (4)(A)(i); and (ii) if the Secretary grants the borrower\u2019s reconsideration request, offer the borrower an extension of the 90-day forbearance period described in paragraph (4)(B), which shall\u2014 (I) begin on the date of the borrower\u2019s reconsideration request under this subparagraph; and (II) end on the date of the notice provided to the borrower under subparagraph (C)(i)(I) of the Secretary\u2019s reconsideration decision. (B) Consideration of reconsideration request In evaluating a reconsideration request from a borrower, the Secretary shall consider any relevant evidence or supporting documentation that may assist the Secretary in determining whether the borrower meets each of the requirements of paragraph (1) to qualify for loan cancellation under this subsection. (C) Decision by the Secretary (i) In general Not later than 6 months after receipt of a borrower\u2019s reconsideration request, the Secretary shall\u2014 (I) notify the borrower of the reconsideration decision and the reason for the Secretary\u2019s determination; (II) in a case in which the reconsideration request is granted, adjust the borrower\u2019s number of qualifying monthly payments under paragraph (1) or cancel the loan under paragraph (3); and (III) in a case in which the Secretary denies the reconsideration request, with respect to a borrower who agrees to the forbearance extension described in subparagraph (A)(ii), include in the notice provided to the borrower under subclause (I), a reminder that the Secretary will resume collection of the eligible Federal Direct Loans for which the borrower was seeking loan cancellation under this subsection as of the date of such notice. (ii) Final decision After the Secretary makes a decision on the borrower\u2019s reconsideration request, the Secretary\u2019s decision is final, and the borrower will not receive additional reconsideration. .\n#### 3. Terms and conditions of employment\n##### (a) Independent contractors\nSection 455(m) is further amended by adding at the end the following:\n(8) Treatment of independent contractors For purposes of this subsection, each reference to employment and employed shall be treated as including work as an independent contractor. .\n##### (b) Definitions\nParagraph (6) of section 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ), as redesignated by section 2(b), is further amended by adding at the end the following:\n(D) Full-time The term full-time means, with respect to a public service job, working 1 or more such jobs\u2014 (i) a minimum average of 30 hours per week during the period being certified; (ii) a minimum of 30 hours per week throughout a contractual or employment period of at least 8 months in a 12-month period; and (iii) with respect to an individual who is in nontenure track employment at an institution of higher education, the equivalent of 30 hours per week as determined by multiplying each credit or contact hour taught by such individual per week by a number to be determined by the Secretary. (E) Independent contractor The term independent contractor means an individual who is not an employee and who is working in a public service job in a position or providing services which, under applicable State law, cannot be filled or provided by an employee of the public service job. .\n#### 4. Online portal and database of public service jobs\nSection 455(m) of the Higher Education Act of 1965 is further amended by adding at the end the following:\n(9) Online portal and database of public service jobs (A) Online portal (i) Borrowers The Secretary shall establish an online portal that provides to borrowers of eligible Federal Direct Loans the following information: (I) Instructions on how to access the database established under subparagraph (B) so that the borrower can determine whether the borrower is employed in a public service job. (II) An identification of the loans of the borrower that are eligible Federal Direct Loans, and an identification of the qualifying repayment plans for which such eligible Federal Direct Loans qualify. (III) With respect to each such eligible Federal Direct Loan\u2014 (aa) the number of qualifying monthly payments the borrower has made in accordance with paragraph (1); and (bb) the estimated number of qualifying monthly payments under such paragraph remaining on such loan before the borrower may be eligible for loan cancellation under this subsection. (IV) With respect to each loan of the borrower that is not eligible for loan cancellation under paragraph (3) of this subsection, an explanation of why the loan is not so eligible and instructions on how what, if anything, the borrower may do to make the loan so eligible. (V) Instructions for the submission of any forms associated with such loan cancellation, and an ability for the borrower to use the portal to electronically sign and submit such forms. (VI) In a case in which a borrower submits to the Secretary an application for loan cancellation under this subsection that is denied by the Secretary\u2014 (aa) a notice of such denial that meets each of the requirements of paragraph (4)(A), including an explanation of the 90-day forbearance period; (bb) a form that meets each of the requirements of paragraph (5)(A), which the borrower may use to request reconsideration of such denial, including accepting an extension of the 90-day forbearance period; and (cc) a notice of the Secretary\u2019s reconsideration decision, which meets each of the requirements of paragraph (5)(C). (VII) An explanation of the buyback payment process described in paragraph (2)(C), and a form to request such a buyback, including the eligible months for which the borrower may request a buyback, and the amount that the borrower would be required to pay for such buyback. (VIII) An explanation of how consolidating one or more Direct Loans into a Direct Consolidation Loan, including a Direct PLUS Loan made to a parent borrower, will affect the number of qualifying monthly payments attributed to the borrower. (ii) Appropriate contacts The Secretary shall ensure that an appropriate contact for a public service job of a borrower has the option to electronically sign and submit any forms associated with loan cancellation under paragraph (3) of this subsection. (iii) Information The Secretary shall ensure that any information provided through the online portal described in this subparagraph contains up-to-date information. (B) Database of public service jobs (i) In general The Secretary, in consultation with the Secretary of Labor, shall establish and regularly update a database that lists public service jobs. (ii) Public availability The database established under clause (i) shall be made available on a publicly accessible website of the Department of Education in an easily searchable format. .\n#### 5. Treatment of periods of deferment and forbearance\n##### (a) In general\nSection 455(f) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(f) ) is amended\u2014\n**(1)**\nin the subsection heading, by inserting and forbearance at the end;\n**(2)**\nin paragraph (1)(B), by striking capitalized or ; and\n**(3)**\nby adding at the end the following:\n(7) Forbearance With respect to a loan that is in a period of forbearance, interest on such loan may not be capitalized after the conclusion of such period. .\n##### (b) Application of amendment\nThe amendments made by subsection (a) shall apply to any period of deferment or forbearance in effect as of the date of the enactment of this Act, and any period of deferment or forbearance beginning on or after such date of enactment.\n#### 6. Treatment of consolidated and refinanced loans\nSection 455(m)(2) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m)(2) , as amended by the preceding provisions of this Act, is further amended by inserting after subparagraph (D) the following:\n(E) Determination of number of qualifying monthly payments for consolidation loans With respect to determining the number of qualifying monthly payments for a borrower seeking loan forgiveness under this subsection who consolidates one or more Direct Loans into a Direct Consolidation Loan, including a Direct PLUS Loan made to a parent borrower, the Secretary shall use the weighted average of the payments the borrower made on the Direct Loans prior to consolidating that met the criteria under this subsection. .\n#### 7. Loan forgiveness for teachers\n##### (a) In general\nThe Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) is further amended\u2014\n**(1)**\nin section 428J(g)(2) ( 20 U.S.C. 1078\u201310(g)(2) )\u2014\n**(A)**\nin subparagraph (A), by inserting or after the semicolon at the end;\n**(B)**\nby striking subparagraph (B); and\n**(C)**\nby redesignating subparagraph (C) as subparagraph (B); and\n**(2)**\nin section 460(g)(2) ( 20 U.S.C. 1087j(g)(2) )\u2014\n**(A)**\nin subparagraph (A), by inserting or after the semicolon at the end;\n**(B)**\nby striking subparagraph (B); and\n**(C)**\nby redesignating subparagraph (C) as subparagraph (B).\n##### (b) Conforming amendment\nSection 455(m)(7) of the Higher Education Act of 1965, as redesignated by section 2(b) of this Act, is amended by striking section 428J, 428K, 428L, or 460 and inserting section 428K or 428L .\n#### 8. GAO study on data matching agreements for public service loan forgiveness\n##### (a) In general\nThe Comptroller General of the United States shall conduct a study on the feasibility of establishing data matching agreements for public service loan forgiveness under section 455(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m) ) that would allow a borrower to forego requesting certification of employment from the appropriate contact for the public service job of the borrower. The study shall include an examination of the Department of Education and the Department of Defense\u2019s progress towards automatic data matching for military and veteran borrowers.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General shall submit a report to the Committee on Education and Workforce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate containing the findings and recommendations resulting from the study required under subsection (a).\n##### (c) Cooperation\nThe head of each relevant Federal agency, including the Secretary of Education, Secretary of Defense, and Commissioner of Internal Revenue, shall cooperate with the Comptroller General to facilitate the completion of the study required under subsection (a).",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-08-01",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4862",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LOAN Act",
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
        "name": "Education",
        "updateDate": "2025-05-19T14:40:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2829",
          "measure-number": "2829",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2829v00",
            "update-date": "2026-03-26"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Strengthening Efforts for Relief and Vital Incentives for Community Service and Engagement Act or the SERVICE Act</strong></p><p>This bill\u00a0makes changes to the Public Service Loan Forgiveness (PSLF) program.</p><p>Under the current PSLF program, the Department of Education (ED) must cancel the balance of interest and principal due on a borrower's Federal Direct Loans after the borrower makes 120 monthly loan payments while employed in a public service job and, at the time of loan forgiveness, the borrower is employed in a public service job.</p><p>Among other changes to the PSLF program, this bill\u00a0</p><ul><li>reduces from 120 to 96 the number of monthly payments required for loan forgiveness;</li><li>expands qualifying monthly payments, deferments, and forbearances allowed under the PSLF program;</li><li>removes the requirement that a borrower must be employed in a public service job at the time of loan forgiveness;</li><li>establishes a reconsideration process\u00a0for\u00a0borrowers who have their initial PSLF application denied; and</li><li>prohibits interest capitalization on loans after deferment or forbearance.</li></ul><p>The bill directs ED to (1) establish an online portal that provides borrowers with information on loans and the\u00a0PSLF program, and (2) establish and regularly update a database listing public service jobs.</p><p>The bill allows an eligible teacher to use the same teaching service to qualify for both the Teacher Loan Forgiveness program and the PSLF program.</p><p>The Government Accountability Office must study and report on the feasibility of establishing data matching agreements for PSLF that\u00a0allows borrowers to forgo requesting employment certification from their employer.</p>"
        },
        "title": "SERVICE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2829.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Efforts for Relief and Vital Incentives for Community Service and Engagement Act or the SERVICE Act</strong></p><p>This bill\u00a0makes changes to the Public Service Loan Forgiveness (PSLF) program.</p><p>Under the current PSLF program, the Department of Education (ED) must cancel the balance of interest and principal due on a borrower's Federal Direct Loans after the borrower makes 120 monthly loan payments while employed in a public service job and, at the time of loan forgiveness, the borrower is employed in a public service job.</p><p>Among other changes to the PSLF program, this bill\u00a0</p><ul><li>reduces from 120 to 96 the number of monthly payments required for loan forgiveness;</li><li>expands qualifying monthly payments, deferments, and forbearances allowed under the PSLF program;</li><li>removes the requirement that a borrower must be employed in a public service job at the time of loan forgiveness;</li><li>establishes a reconsideration process\u00a0for\u00a0borrowers who have their initial PSLF application denied; and</li><li>prohibits interest capitalization on loans after deferment or forbearance.</li></ul><p>The bill directs ED to (1) establish an online portal that provides borrowers with information on loans and the\u00a0PSLF program, and (2) establish and regularly update a database listing public service jobs.</p><p>The bill allows an eligible teacher to use the same teaching service to qualify for both the Teacher Loan Forgiveness program and the PSLF program.</p><p>The Government Accountability Office must study and report on the feasibility of establishing data matching agreements for PSLF that\u00a0allows borrowers to forgo requesting employment certification from their employer.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119hr2829"
    },
    "title": "SERVICE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Efforts for Relief and Vital Incentives for Community Service and Engagement Act or the SERVICE Act</strong></p><p>This bill\u00a0makes changes to the Public Service Loan Forgiveness (PSLF) program.</p><p>Under the current PSLF program, the Department of Education (ED) must cancel the balance of interest and principal due on a borrower's Federal Direct Loans after the borrower makes 120 monthly loan payments while employed in a public service job and, at the time of loan forgiveness, the borrower is employed in a public service job.</p><p>Among other changes to the PSLF program, this bill\u00a0</p><ul><li>reduces from 120 to 96 the number of monthly payments required for loan forgiveness;</li><li>expands qualifying monthly payments, deferments, and forbearances allowed under the PSLF program;</li><li>removes the requirement that a borrower must be employed in a public service job at the time of loan forgiveness;</li><li>establishes a reconsideration process\u00a0for\u00a0borrowers who have their initial PSLF application denied; and</li><li>prohibits interest capitalization on loans after deferment or forbearance.</li></ul><p>The bill directs ED to (1) establish an online portal that provides borrowers with information on loans and the\u00a0PSLF program, and (2) establish and regularly update a database listing public service jobs.</p><p>The bill allows an eligible teacher to use the same teaching service to qualify for both the Teacher Loan Forgiveness program and the PSLF program.</p><p>The Government Accountability Office must study and report on the feasibility of establishing data matching agreements for PSLF that\u00a0allows borrowers to forgo requesting employment certification from their employer.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119hr2829"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2829ih.xml"
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
      "title": "SERVICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-26T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SERVICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-26T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Efforts for Relief and Vital Incentives for Community Service and Engagement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-26T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to improve the Public Service Loan Forgiveness program and reduce interest rates.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-26T03:18:19Z"
    }
  ]
}
```
