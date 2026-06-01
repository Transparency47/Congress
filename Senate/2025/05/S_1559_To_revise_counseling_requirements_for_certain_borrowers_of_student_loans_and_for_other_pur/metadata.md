# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1559?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1559
- Title: Know Before You Owe Federal Student Loan Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1559
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2025-12-05T21:47:47Z
- Update date including text: 2025-12-05T21:47:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1559",
    "number": "1559",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Know Before You Owe Federal Student Loan Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:47:47Z",
    "updateDateIncludingText": "2025-12-05T21:47:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T15:50:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "MN"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1559is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1559\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Grassley (for himself and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo revise counseling requirements for certain borrowers of student loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Know Before You Owe Federal Student Loan Act of 2025 .\n#### 2. Pre-loan counseling and certification of loan amount\nSection 485(l) of the Higher Education Act of 1965 ( 20 U.S.C. 1092(l) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking Entrance Counseling and inserting Pre-Loan Counseling ;\n**(2)**\nin paragraph (1)(A)\u2014\n**(A)**\nin the matter preceding clause (i), by striking a disbursement to a first-time borrower of a loan and inserting the first disbursement of each new loan (or the first disbursement in each award year if more than one new loan is obtained in the same award year) ; and\n**(B)**\nin clause (ii)(I), by striking an entrance counseling and inserting a counseling ;\n**(3)**\nin paragraph (2)\u2014\n**(A)**\nby striking subparagraph (G) and inserting the following:\n(G) An estimate of the borrower's monthly payment amount compared to the borrower's estimated monthly income after taxes, after living expenses (using Consumer Expenditure Survey data from the Bureau of Labor Statistics), after estimated health insurance costs, and after any other relevant expenses, based on\u2014 (i) the best available data on starting wages for the borrower's program of study, if available; and (ii) the estimated total student loan debt of the borrower, including\u2014 (I) Federal debt; (II) to the best of the institution's knowledge, private loan debt already incurred; and (III) the estimated future debt required to complete the program of study. ; and\n**(B)**\nby adding at the end the following:\n(L) A statement that the borrower should borrow the minimum amount necessary to cover expenses and that the borrower does not have to accept the full amount of loans for which the borrower is eligible. (M) A warning that the higher the borrower\u2019s debt-to-income ratio is, the more difficulty the borrower is likely to experience in repaying the loan. (N) Options for reducing borrowing through scholarships, reduced expenses, work-study, or other work opportunities. (O) An explanation of the importance of graduating on time to avoid additional borrowing, what course load is necessary to graduate on time, and information on how adding an additional year of study impacts total indebtedness. ; and\n**(4)**\nby adding at the end the following:\n(3) Confirmation by student of loan amount provided (A) In general In addition to the other requirements of this subsection and in accordance with subparagraph (B), each eligible institution shall ensure that the student manually enter, either in writing or through electronic means, the exact dollar amount of Federal Direct Loan funding under part D that such student desires to borrow. (B) Timing The eligible institution shall ensure that the student carries out the activity described in subparagraph (A)\u2014 (i) in the course of the process used by the institution for students to accept a student loan award; (ii) prior to the institution certifying a Federal Direct Loan under part D for disbursement to a student (other than a Federal Direct Consolidation Loan or a Federal Direct PLUS loan made on behalf of a student); and (iii) after ensuring that the student has completed all of the pre-loan counseling requirements under this subsection. .\n#### 3. Required periodic disclosures during periods when loan payments are not required\nSection 433 of the Higher Education Act of 1965 ( 20 U.S.C. 1083 ) is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Required periodic disclosures during periods when loan payments are not required During any period of time when a borrower of one or more loans, made, insured, or guaranteed under this part or part D is not required to make a payment to an eligible lender on the borrower's loan from that eligible lender, such eligible lender shall provide such borrower with a quarterly statement that includes, in simple and understandable terms\u2014 (1) the original principal amount of each of the borrower's loans, and the original principal amount of those loans in the aggregate; (2) the borrower's current balance, as of the time of the statement, as applicable; (3) the interest rate on each loan; (4) the total amount the borrower has paid in interest on each loan; (5) the aggregate amount the borrower has paid for each loan, including the amount the borrower has paid in interest, the amount the borrower has paid in fees, and the amount the borrower has paid against the balance; (6) the lender's or loan servicer's address, toll-free phone number, and web page for payment and billing error purposes, including information about how a borrower can make voluntary payments when a loan is not in repayment status; (7) an explanation\u2014 (A) that the borrower has the option to pay the interest that accrues on each loan while the borrower is a student at an institution of higher education or during a period of deferment or forbearance, if applicable; and (B) if the borrower does not pay such interest while attending an institution or during a period of deferment or forbearance, any accumulated interest on the loan will be capitalized when the loan goes into repayment, resulting in more interest being paid over the life of the loan; (8) the amount of interest that has accumulated since the last statement based on the typical installment time period and the aggregate interest accrued to date; and (9) an explanation that making even small payments of any unspecified amount while the borrower is a student at an institution of higher education, or during a period of deferment or forbearance, if applicable, can help to offset interest accrual over the life of the loan. .\n#### 4. Conforming amendments\n##### (a) Program participation agreements\nSection 487(e)(2)(B)(ii)(IV) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(e)(2)(B)(ii)(IV) ) is amended\u2014\n**(1)**\nby striking Entrance and exit counseling and inserting Pre-loan and exit counseling ; and\n**(2)**\nby striking entrance and exit counseling and inserting pre-loan and exit counseling .\n##### (b) Regulatory relief and improvement\nSection 487A of the Higher Education Act of 1965 ( 20 U.S.C. 1094a ) is amended by striking entrance and exit interviews and inserting pre-loan and exit interviews each place the term appears.",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-05-08",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "3298",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Know Before You Owe Federal Student Loan Act of 2025",
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
        "updateDate": "2025-05-21T13:52:36Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1559is.xml"
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
      "title": "Know Before You Owe Federal Student Loan Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Know Before You Owe Federal Student Loan Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to revise counseling requirements for certain borrowers of student loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:28Z"
    }
  ]
}
```
