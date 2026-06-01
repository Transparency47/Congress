# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2003?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2003
- Title: Affordable Loans for Students Act
- Congress: 119
- Bill type: HR
- Bill number: 2003
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-01-23T09:06:52Z
- Update date including text: 2026-01-23T09:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2003",
    "number": "2003",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Affordable Loans for Students Act",
    "type": "HR",
    "updateDate": "2026-01-23T09:06:52Z",
    "updateDateIncludingText": "2026-01-23T09:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:03:20Z",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NJ"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2003ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2003\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Lawler (for himself, Mrs. Luna , and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.\n#### 1. Short title\nThis Act may be cited as the Affordable Loans for Students Act .\n#### 2. Program authority\nSection 451(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1087a(a) ) is amended\u2014\n**(1)**\nby striking and (2) and inserting (2) ; and\n**(2)**\nby inserting ; and (3) to make loans under section 460A(b) after section 459A .\n#### 3. Program for the loan modification of eligible Federal loans held by the Secretary, and refinancing of other Federal student loans\n##### (a) Loan modification and refinancing\nPart D of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1087a et seq. ) is amended by adding at the end the following:\n460A. Program for the loan modification of eligible Federal loans held by the Secretary, and refinancing of other Federal student loans (a) Federal Direct Loan Modification The Secretary shall establish and implement, with respect to each borrower of an eligible Federal loans held by the Secretary, procedures to modify, without any action from the borrower, the terms of such loan so that beginning on the first July 1 after the date of enactment of the Affordable Loans for Students Act, the applicable rate of interest shall be 2.0 percent on the unpaid principal balance of the loan. (b) Refinancing eligible Federal loans not held by the Secretary as Federal Direct Consolidation Loans (1) In general The Secretary shall establish and implement, with respect to each borrower of an eligible Federal loan not held by the Secretary, procedures to refinance such loan in accordance with the requirements of paragraph (2) and without any action from the borrower, except that such borrower may opt out of such procedures with respect to such loan. (2) Procedures In refinancing an eligible Federal loan not held by the Secretary with respect to a borrower of such loan, the Secretary shall carry out the following: (A) The Secretary shall make a Federal Direct Consolidation Loan under this subsection, in an amount equal to the sum of the unpaid principal, accrued unpaid interest, and late charges of the eligible Federal loan not held by the Secretary. (B) The Secretary shall pay the proceeds of such Federal Direct Consolidation Loan to the holder of the eligible Federal non-direct loan, in order to discharge the borrower from any remaining obligation with respect to such eligible Federal loan not held by the Secretary. (3) Terms and conditions of refinanced loans (A) In general A Federal Direct Consolidation Loan made under this subsection shall have the same terms and conditions as a Federal Direct Consolidation Loan that was not made under this subsection, except\u2014 (i) that the Secretary may adjust such terms and conditions as necessary to enable the borrower to access loan forgiveness or other benefits available to the borrower under the loan before refinancing under this subsection, in any case where such benefits are more generous than provided under a Federal Direct Consolidation Loan; and (ii) as otherwise provided in this subsection. (B) No origination fees Notwithstanding section 455(c), the Secretary may not charge a borrower of a loan made under this subsection an origination fee for such loan. (C) Interest rate The applicable rate of interest for a loan made under this subsection shall be 2.0 percent on the unpaid principal balance of the loan. (D) No automatic extension of repayment period A loan made under this subsection shall not result in the extension of the duration of the repayment period of the original loan, and the borrower shall retain the same repayment term that was in effect on the original loan. Nothing in this paragraph shall be construed to prevent a borrower from electing a different repayment plan at any time in accordance with section 455(d)(3). (E) Rule of construction Nothing in this section shall be construed to\u2014 (i) prohibit a borrower of an eligible Federal loan not held by the Secretary from consolidating such a loan with any other loan eligible for consolidation under this section into a single consolidation loan under this section; or (ii) require such a borrower to consolidate any such loan with any other loan eligible for consolidation under this section into a single consolidation loan under this section. (c) Report Not later than 180 days after the second July 1 after the date of enactment of the Affordable Loans for Students Act, and on an annual basis thereafter, the Secretary shall submit a report to the authorizing committees that includes\u2014 (1) the total number of borrowers whose loans have been modified or refinanced under this section during the preceding year; and (2) the number of such borrowers who are delinquent in making payments on such a loan. (d) Definitions In this section: (1) Eligible Federal loan held by the Secretary The term eligible Federal loan held by the Secretary means\u2014 (A) any loan made under this part, and first disbursed before the first July 1 after the date of enactment of the Affordable Loans for Students Act; (B) any loan made, insured, or guaranteed under part B, and which is held by the Secretary; (C) any loan made under part E, and which is held by the Secretary; and (D) any loan made under subpart I of part A of title VII of the Public Health Service Act ( 42 U.S.C. 292 et seq. ), and which is held by the Secretary. (2) Eligible Federal loan not held by the Secretary The term eligible Federal loan not held by the Secretary means any loan\u2014 (A) made, insured, or guaranteed under part B, and which is not held by the Secretary; (B) made under part E, and which is not held by the Secretary; and (C) made under\u2014 (i) subpart I of part A of title VII of the Public Health Service Act ( 42 U.S.C. 292 et seq. ), and which is not held by the Secretary; (ii) subpart II of part A of title VII of the Public Health Service Act ( 42 U.S.C. 292q et seq. ); or (iii) part E of title VIII of the Public Health Service Act ( 42 U.S.C. 297a et seq. ). (3) Original loan The term original loan , used with respect to a Federal Direct Consolidation Loan made under subsection (b), means a loan for which a borrower\u2019s liability is discharged by such Federal Direct Consolidation Loan. .\n##### (d) Conforming amendments\nThe Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) is amended\u2014\n**(1)**\nin section 428C(a)(3)(B)(i)(V) ( 20 U.S.C. 1078\u20133(3)(B)(i)(V) )\u2014\n**(A)**\nby striking the period at the end of item (cc) and inserting a semicolon;\n**(B)**\nby striking the period at the end of item (dd) and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(ee) for the purpose of obtaining a Federal Direct Consolidation Loan under section 460A(b). .\n#### 4. Applicable rates of interest for loans made on or after the first July 1 after the date of enactment of the Affordable Loans for Students Act\nSection 455(b)(8) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(b)(8) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting and before the first July 1 after the date of enactment of the Affordable Loans for Students Act after July 1, 2013 ;\n**(2)**\nin subparagraph (A), by inserting and before the first July 1 after the date of enactment of the Affordable Loans for Students Act after July 1, 2013 ;\n**(3)**\nin subparagraph (B), by inserting and before the first July 1 after the date of enactment of the Affordable Loans for Students Act after July 1, 2013 ;\n**(4)**\nin subparagraph (C), by inserting and before the first July 1 after the date of enactment of the Affordable Loans for Students Act after July 1, 2013 ;\n**(5)**\nin subparagraph (D), by inserting and before the first July 1 after the date of enactment of the Affordable Loans for Students Act after July 1, 2013 ;\n**(6)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(7)**\nby inserting after subparagraph (E) the following:\n(F) New loans on or after the first July 1 after the date of enactment of the Affordable Loans for Students Act Notwithstanding the preceding subparagraphs of this paragraph, for Federal Direct Stafford Loans, Federal Direct Unsubsidized Stafford Loans, Federal Direct PLUS Loans, and Federal Direct Consolidation Loans for which the first disbursement is made, or the application is received, on or after the first July 1 after the date of enactment of the Affordable Loans for Students Act, the applicable rate of interest shall be 2.0 percent on the unpaid principal balance of the loan. .",
      "versionDate": "2025-03-10",
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
        "name": "Education",
        "updateDate": "2025-03-26T14:45:54Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2003ih.xml"
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
      "title": "Affordable Loans for Students Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Loans for Students Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to lower the interest rate on Federal student loans to 2 percent.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:52Z"
    }
  ]
}
```
