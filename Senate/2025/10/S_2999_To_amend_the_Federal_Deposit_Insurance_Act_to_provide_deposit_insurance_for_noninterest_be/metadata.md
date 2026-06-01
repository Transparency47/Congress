# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2999?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2999
- Title: Main Street Depositor Protection Act
- Congress: 119
- Bill type: S
- Bill number: 2999
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2026-04-13T19:58:20Z
- Update date including text: 2026-04-13T19:58:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2026-02-05 - Committee: Committee on Banking, Housing, and Urban Affairs. Hearings held.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2026-02-05 - Committee: Committee on Banking, Housing, and Urban Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2999",
    "number": "2999",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H000601",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Hagerty, Bill [R-TN]",
        "lastName": "Hagerty",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Main Street Depositor Protection Act",
    "type": "S",
    "updateDate": "2026-04-13T19:58:20Z",
    "updateDateIncludingText": "2026-04-13T19:58:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Banking, Housing, and Urban Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-09",
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
        "item": [
          {
            "date": "2026-02-05T15:00:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-10-09T21:57:08Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2999is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2999\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Hagerty (for himself and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Federal Deposit Insurance Act to provide deposit insurance for noninterest-bearing transaction accounts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Main Street Depositor Protection Act .\n#### 2. Transaction account insurance\n##### (a) Depository institutions\n**(1) In general**\nSection 11(a)(1) of the Federal Deposit Insurance Act ( 12 U.S.C. 1821(a)(1) ) is amended by striking subparagraph (B) and inserting the following:\n(B) Net amount of insured deposit (i) In general The net amount due to any depositor at an insured depository institution shall not exceed the sum of\u2014 (I) the standard maximum deposit insurance amount as determined in accordance with subparagraphs (C), (D), (E), and (F) and paragraph (3); and (II) the net amount under clause (ii). (ii) Insurance for noninterest-bearing transaction accounts (I) In general Except as provided in subclause (III), the Corporation shall insure the net amount, in an amount that is not more than $10,000,000, that any depositor maintains, in the aggregate, in 1 or more noninterest-bearing transaction accounts at an insured depository institution. (II) Aggregation For the purpose of determining the net amount due to any depositor under subclause (I), the Corporation shall aggregate the amounts of all deposits in insured depository institutions that are subsidiaries of a single depository institution holding company. (III) Exclusion (aa) Definition In this subclause, the term foreign bank does not include any bank organized under the laws of any territory of the United States, Puerto Rico, Guam, American Samoa, or the Virgin Islands, the deposits of which are insured by the Corporation pursuant to this Act. (bb) Exclusion The Corporation may not insure under subclause (I) amounts maintained at\u2014 (AA) any insured depository institution that is a subsidiary of a bank holding company that is identified as a global systemically important BHC under section 217.402 of title 12, Code of Federal Regulations (or any successor regulation); or (BB) any insured branch of a foreign bank. .\n**(2) Technical and conforming amendment**\nSection 3(m) of the Federal Deposit Insurance Act ( 12 U.S.C. 1813(m) ) is amended\u2014\n**(A)**\nin paragraph (1), by inserting , including deposits in a noninterest-bearing transaction account, after deposits ; and\n**(B)**\nby adding at the end the following:\n(5) Noninterest-bearing transaction account The term noninterest-bearing transaction account means a deposit or account maintained at an insured depository institution\u2014 (A) with respect to which interest is neither accrued nor paid; (B) on which the depositor or account holder is permitted to make withdrawals by negotiable or transferable instrument, payment orders of withdrawal, telephone or other electronic media transfers, or other similar items for the purpose of making payments or transfers to third parties or others; and (C) on which the insured depository institution does not reserve the right to require advance notice of an intended withdrawal. .\n**(3) Assessments**\nDuring the transition period under subsection (c), no insured depository institution with total assets of $10,000,000,000 or less shall be required to pay\u2014\n**(A)**\nany special assessment under section 7(b)(5) or 13(c)(4)(G) of the Federal Deposit Insurance Act ( 12 U.S.C. 1817(b)(5) , 1823(c)(4)(G)) as a condition to insurance on a noninterest-bearing transaction account, as defined in paragraph (5) of section 3(m) of the Federal Deposit Insurance Act ( 12 U.S.C. 1813(m) ), as added by paragraph (2) of this subsection; or\n**(B)**\nany increase in assessments under section 7(b)(2) of the Federal Deposit Insurance Act ( 12 U.S.C. 1817(b)(2) ) solely to offset any impact on the reserve ratio arising out of the extension of insurance to noninterest-bearing transaction accounts in excess of the standard maximum deposit insurance amount as determined in accordance with subparagraphs (C), (D), (E), and (F) of paragraph (1) and paragraph (3) of section 11(a) of that Act ( 12 U.S.C. 1821(a) ).\n##### (b) Credit unions\n**(1) In general**\nSection 207(k)(1)(A) of the Federal Credit Union Act ( 12 U.S.C. 1787(k)(1)(A) ) is amended\u2014\n**(A)**\nby striking Subject to the provisions of paragraph (2), the net amount and inserting the following:\n(i) Net amount of insurance payable Subject to clause (ii) and the provisions of paragraph (2), the net amount ; and\n**(B)**\nby adding at the end the following:\n(ii) Insurance for noninterest-bearing transaction accounts (I) In general Notwithstanding clause (i), the Board shall insure the net amount, in an amount that is not more than $10,000,000, that any member, or any person with funds lawfully held in a member account, maintains, in the aggregate, in 1 or more noninterest-bearing transaction accounts at an insured credit union. (II) Exclusion The amount described in subclause (I) shall not be taken into account when computing the net amount due to a member, or to any person with funds lawfully held in a member account, described in that subclause under clause (i). .\n**(2) Technical and conforming amendments**\nSection 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ) is amended\u2014\n**(A)**\nin paragraph (5), by inserting such terms mean a noninterest-bearing transaction account, after Act, ;\n**(B)**\nin paragraph (8), by striking and at the end;\n**(C)**\nin paragraph (9), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(10) The term noninterest-bearing transaction account means an account of a member, or nonmember that is eligible to maintain an insured account, maintained at an insured credit union\u2014 (A) with respect to which interest is neither accrued nor paid; (B) on which the member or account holder is permitted to make withdrawals by negotiable or transferable instrument, payment orders of withdrawal, telephone or other electronic media transfers, or other similar items for the purpose of making payments or transfers to third parties or others; and (C) on which the insured credit union does not reserve the right to require advance notice of an intended withdrawal. .\n##### (c) Transition period\n**(1) Depository institutions**\n**(A) In general**\nNotwithstanding any other provision of law, insured deposits in noninterest-bearing transaction accounts, as described in clause (ii) of section 11(a)(1)(B) of the Federal Deposit Insurance Act ( 12 U.S.C. 1821(a)(1)(B) ), as added by subsection (a)(1) of this section, shall be included in the determination of the value of the estimated insured deposits described in sections 3(y)(3) and 7(b)(3)(B) of that Act ( 12 U.S.C. 1813(y)(3) , 1817(b)(3)(B)) in accordance with the plan required under subparagraph (B).\n**(B) Plan**\nNot later than 1 year after the date of enactment of this Act, the Federal Deposit Insurance Corporation shall publish in the Federal Register a plan for gradually increasing, during the period ending on the date that is 10 years after the date of enactment of this Act, the portion of insured deposits described in subparagraph (A) in the determination described in that subparagraph, reaching 100 percent at the end of the period.\n**(2) Credit unions**\n**(A) In general**\nNotwithstanding any other provision of law, insured shares in noninterest-bearing transaction accounts, as described in clause (ii) of section 207(k)(1)(A) of the Federal Credit Union Act ( 12 U.S.C. 1787(k)(1)(A) ), as added by subsection (b)(1) of this section, shall be included in the determination of the value of the aggregate amount of the insured shares, as defined in section 202(h) of that Act ( 12 U.S.C. 1782(h) ), in accordance with the plan required under subparagraph (B).\n**(B) Plan**\nNot later than 1 year after the date of enactment of this Act, the National Credit Union Administration Board shall publish in the Federal Register a plan for gradually increasing, during the period ending on the date that is 10 years after the date of enactment of this Act, the portion of insured shares described in subparagraph (A) in the determination described in that subparagraph, reaching 100 percent at the end of the period.\n**(C) Regulations**\nThe National Credit Union Administration Board may promulgate regulations to ensure that the National Credit Union Share Insurance Fund remains well-capitalized.\n##### (d) Regulations\nThe Federal Deposit Insurance Corporation and the National Credit Union Administration Board may promulgate regulations carrying out the amendments made by this section, including prohibiting insured depository institutions, as defined in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ), insured credit unions, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ), and third parties, as applicable, from evading the limitation of insurance established under those amendments to only\u2014\n**(1)**\nnoninterest-bearing transaction accounts;\n**(2)**\ndeposits or accounts at insured depository institutions not excluded under clause (ii)(III) of section 11(a)(1)(B) of the Federal Deposit Insurance Act ( 12 U.S.C. 1821(a)(1)(B) ), as added by subsection (a) of this section; and\n**(3)**\nshares, deposits, or accounts at insured credit unions.",
      "versionDate": "2025-10-09",
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
        "actionDate": "2026-03-25",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "4198",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Depositor Protection Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-25",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "8087",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Depositor Protection Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-02-18T15:29:43Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-02-18T15:23:44Z"
          },
          {
            "name": "Business records",
            "updateDate": "2026-02-18T15:37:14Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-02-18T15:31:13Z"
          },
          {
            "name": "Federal Deposit Insurance Corporation (FDIC)",
            "updateDate": "2026-02-18T15:29:35Z"
          },
          {
            "name": "Interest, dividends, interest rates",
            "updateDate": "2026-02-18T15:24:30Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-02-18T15:31:23Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-02-18T15:30:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-08T16:28:49Z"
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
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2999is.xml"
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
      "title": "Main Street Depositor Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Main Street Depositor Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Deposit Insurance Act to provide deposit insurance for noninterest-bearing transaction accounts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:22Z"
    }
  ]
}
```
