# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2781?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2781
- Title: Protecting Consumers from Unreasonable Credit Rates Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2781
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2025-09-29T12:50:29Z
- Update date including text: 2025-09-29T12:50:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S6577)
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S6577)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2781",
    "number": "2781",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Protecting Consumers from Unreasonable Credit Rates Act of 2025",
    "type": "S",
    "updateDate": "2025-09-29T12:50:29Z",
    "updateDateIncludingText": "2025-09-29T12:50:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S6577)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T17:56:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2781is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2781\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Durbin (for himself, Mr. Blumenthal , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Truth in Lending Act to establish a national usury rate for consumer credit transactions.\n#### 1. Short title\nThis Act may be cited as the Protecting Consumers from Unreasonable Credit Rates Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nattempts have been made to prohibit usurious interest rates in America since colonial times;\n**(2)**\nat the Federal level, in 2006, Congress enacted a Federal 36-percent annualized usury cap for servicemembers and their families for covered credit products, as defined by the Department of Defense, which curbed payday, car title, and tax refund lending around military bases;\n**(3)**\nnotwithstanding such attempts to curb predatory lending, high-cost lending persists in all 50 States due to loopholes in State laws, safe harbor laws for specific forms of credit, and the exportation of unregulated interest rates permitted by preemption;\n**(4)**\ndue to the lack of a comprehensive Federal usury cap, consumers have paid as much as approximately $12,000,000,000 on high-cost overdraft loans, $8,600,000,000 on storefront and online payday loans, $3,800,000,000 on car title loans, and additional amounts in unreported revenues on high-cost online installment loans;\n**(5)**\ncash-strapped consumers pay on average approximately 400-percent annual interest for payday loans, 300-percent annual interest for car title loans, 17,000-percent for bank overdraft loans, and triple-digit rates for online installment loans;\n**(6)**\na national maximum interest rate that includes all forms of fees and closes all loopholes is necessary to eliminate such predatory lending; and\n**(7)**\nalternatives to predatory lending that encourage small dollar loans with minimal or no fees, installment payment schedules, and affordable repayment periods should be encouraged.\n#### 3. National maximum interest rate\nChapter 2 of the Truth in Lending Act ( 15 U.S.C. 1631 et seq. ) is amended by adding at the end the following:\n140B. Maximum rates of interest (a) In general Notwithstanding any other provision of law, no creditor may make an extension of credit to a consumer with respect to which the fee and interest rate, as defined in subsection (b), exceeds 36 percent. (b) Fee and interest rate defined (1) In general For purposes of this section, the fee and interest rate includes all charges payable, directly or indirectly, incident to, ancillary to, or as a condition of the extension of credit, including\u2014 (A) any payment compensating a creditor or prospective creditor for\u2014 (i) an extension of credit or making available a line of credit, such as fees connected with credit extension or availability such as numerical periodic rates, annual fees, cash advance fees, and membership fees; or (ii) any fees for default or breach by a borrower of a condition upon which credit was extended, such as late fees, insufficient funds fees, overdraft fees, and over-limit fees; (B) all fees which constitute a finance charge, as defined by rules of the Bureau in accordance with this title; (C) credit insurance premiums, whether optional or required; (D) all charges and costs for ancillary products or optional services offered in connection with or incidental to the credit transaction; and (E) any costs payable in connection with products that involve\u2014 (i) the provision of funds to the consumer in an amount that is based, by estimate or otherwise, on the wages that the consumer has accrued in a given pay cycle; and (ii) repayment to the third-party provider via automatic means at or after the end of the pay cycle. (2) Tolerances (A) In general With respect to a credit obligation that is payable in at least 3 fully amortizing installments over at least 90 days, the term fee and interest rate does not include\u2014 (i) application or participation fees that in total do not exceed the greater of $30 or, if there is a limit to the credit line, 5 percent of the credit limit, up to $120, if\u2014 (I) such fees are excludable from the finance charge pursuant to section 106 and regulations issued thereunder; (II) such fees cover all credit extended or renewed by the creditor for 12 months; and (III) the minimum amount of credit extended or available on a credit line is equal to $300 or more; (ii) a late fee charged as authorized by State law and by the agreement that does not exceed either $8 per late payment or $8 per month; or (iii) a creditor-imposed insufficient funds fee charged when a borrower tenders payment on a debt with a check drawn on insufficient funds that does not exceed $15. (B) Adjustments for inflation The Bureau may adjust the amounts of the tolerances established under this paragraph for inflation over time, consistent with the primary goals of protecting consumers and ensuring that the 36-percent fee and interest rate limitation is not circumvented. (c) Calculations (1) Open end credit plans For an open end credit plan\u2014 (A) the fee and interest rate shall be calculated each month, based upon the sum of all fees and finance charges described in subsection (b) charged by the creditor during the preceding 1-year period, divided by the average daily balance; and (B) if the credit account has been open less than 1 year, the fee and interest rate shall be calculated based upon the total of all fees and finance charges described in subsection (b)(1) charged by the creditor since the plan was opened, divided by the average daily balance, and multiplied by the quotient of 12 divided by the number of full months that the credit plan has been in existence. (2) Other credit plans For purposes of this section, in calculating the fee and interest rate, the Bureau shall require the method of calculation of annual percentage rate specified in section 107(a)(1), except that the amount referred to in that section 107(a)(1) as the finance charge shall include all fees, charges, and payments described in subsection (b)(1) of this section. (3) Adjustments authorized The Bureau may make adjustments to the calculations in paragraphs (1) and (2), but the primary goals of such adjustment shall be to protect consumers and to ensure that the 36-percent fee and interest rate limitation is not circumvented. (d) Definition of creditor As used in this section, the term creditor has the same meaning as in section 702(e) of the Equal Credit Opportunity Act ( 15 U.S.C. 1691a(e) ). (e) No exemptions permitted The exemption authority of the Bureau under section 105 shall not apply to the rates established under this section or the disclosure requirements under section 127(b)(6). (f) Disclosure of fee and interest rate for credit other than open end credit plans In addition to the disclosure requirements under section 127(b)(6), the Bureau may prescribe regulations requiring disclosure of the fee and interest rate established under this section. (g) Relation to State law Nothing in this section may be construed to preempt any provision of State law that provides greater protection to consumers than is provided in this section. (h) Civil liability and enforcement In addition to remedies available to the consumer under section 130(a), any payment compensating a creditor or prospective creditor, to the extent that such payment is a transaction made in violation of this section, shall be null and void, and not enforceable by any party in any court or alternative dispute resolution forum, and the creditor or any subsequent holder of the obligation shall promptly return to the consumer any principal, interest, charges, and fees, and any security interest associated with such transaction. Notwithstanding any statute of limitations or repose, a violation of this section may be raised as a matter of defense by recoupment or setoff to an action to collect such debt or repossess related security at any time. (i) Violations Any person that violates this section, or seeks to enforce an agreement made in violation of this section, shall be subject to, for each such violation, 1 year in prison and a fine in an amount equal to the greater of\u2014 (1) three times the amount of the total accrued debt associated with the subject transaction; or (2) $50,000. (j) State attorneys general An action to enforce this section may be brought by the appropriate State attorney general in any United States district court or any other court of competent jurisdiction within 3 years from the date of the violation, and such attorney general may obtain injunctive relief. .\n#### 4. Disclosure of fee and interest rate for open end credit plans\nSection 127(b)(6) of the Truth in Lending Act ( 15 U.S.C. 1637(b)(6) ) is amended by striking the total finance charge expressed and all that follows through the end of the paragraph and inserting the fee and interest rate, displayed as FAIR , established under section 141. .",
      "versionDate": "2025-09-11",
      "versionType": "Introduced in Senate"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-29T12:50:29Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2781is.xml"
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
      "title": "Protecting Consumers from Unreasonable Credit Rates Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Consumers from Unreasonable Credit Rates Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Truth in Lending Act to establish a national usury rate for consumer credit transactions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T03:48:15Z"
    }
  ]
}
```
