# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6542?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6542
- Title: First Home Savings Opportunity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6542
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-01-13T09:05:19Z
- Update date including text: 2026-01-13T09:05:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-12-09 - IntroReferral: Sponsor introductory remarks on measure. (CR H5062)
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-12-09 - IntroReferral: Sponsor introductory remarks on measure. (CR H5062)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6542",
    "number": "6542",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "First Home Savings Opportunity Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:19Z",
    "updateDateIncludingText": "2026-01-13T09:05:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H5062)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:03:10Z",
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
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "IA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MI"
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
      "sponsorshipDate": "2025-12-09",
      "state": "DC"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6542ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6542\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Subramanyam (for himself, Mrs. Hinson , Mr. Thanedar , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow the establishment of down payment savings accounts.\n#### 1. Short title\nThis Act may be cited as the First Home Savings Opportunity Act of 2025 .\n#### 2. Down payment savings account\n##### (a) In general\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 223 the following new section:\n223A. Down payment savings account (a) Deduction allowed In the case of an account beneficiary, there shall be allowed as a deduction for the taxable year an amount equal to the aggregate amount paid in cash during such taxable year by such individual to a down payment savings account of such individual. (b) Definitions and special rules For purposes of this section\u2014 (1) Down payment savings account The term down payment savings account means a trust created or organized in the United States exclusively for the purpose of paying the qualified down payment expenses of the account beneficiary (and designated as a down payment savings account at the time created or organized), but only if the written governing instrument creating the trust meets the following requirements: (A) No contribution will be accepted\u2014 (i) if such contribution is not made by the account beneficiary, (ii) if the account beneficiary had an ownership interest in a principal residence at any time during the 3-year period ending on the date of the contribution, or (iii) unless it is in cash. (B) The trustee is a bank (as defined in section 408(n)) or another person who demonstrates to the satisfaction of the Secretary that the manner in which that person will administer the trust will be consistent with the requirements of this section. (C) No part of the trust assets will be invested in life insurance contracts. (D) The assets of the trust shall not be commingled with other property except in a common trust fund or common investment fund. (E) The account beneficiary has attained the age of 18. (2) Qualified down payment expenses The term qualified down payment expenses means a down payment or closing costs for the purchase of the principal residence of the account beneficiary of a down payment savings account if such account beneficiary is a first-time homebuyer (as defined in section 36(c)) with respect to such purchase. (3) Account beneficiary The term account beneficiary means the individual on whose behalf the down payment savings account is established. (4) Certain rules to apply Rules similar to the following rules shall apply for purposes of this section: (A) Section 219(d)(2) (relating to no deduction for rollovers). (B) Section 219(f)(3) (relating to time when contributions deemed made). (C) Section 219(f)(5) (relating to employer payments). (D) Section 408(g) (relating to community property laws). (5) Principal residence The term principal residence has the same meaning as when used in section 121. (c) Limitations (1) Contribution limit The amount allowable as a deduction under subsection (a) to any individual for any taxable year shall not exceed the lesser of\u2014 (A) the taxpayer\u2019s earned income (as defined in section 32(c)(2)) for the taxable year, or (B) $10,000 ($20,000 in the case of a joint return). (2) Phaseout based on modified adjusted gross income (A) In general The deduction allowable under subsection (a) shall be reduced by an amount which bears the same ratio to the amount of such deduction as\u2014 (i) the excess (if any) of\u2014 (I) the taxpayer\u2019s modified adjusted gross income, over (II) $150,000 ($236,000 in the case of a joint return), bears to (ii) $50,000 ($79,000 in the case of a joint return). (B) Modified adjusted gross income For purposes of subparagraph (A), the term modified adjusted gross income means the adjusted gross income of the taxpayer for the taxable year increased by any amount excluded from gross income under section 911, 931, or 933. (3) Denial of deduction to dependents No deduction shall be allowed under this section to any individual with respect to whom a deduction under section 151 is allowable to another taxpayer for a taxable year beginning in the calendar year in which such individual's taxable year begins. (4) Inflation adjustment (A) In general In the case of any taxable year beginning after 2025, each of the dollar amounts in this subsection shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any increase under paragraph (1) is not a multiple of $100, such increase shall be rounded to the nearest multiple of $100. (d) Tax treatment of distributions (1) Amounts used for qualified down payment expenses Any amount paid or distributed out of a down payment savings account which is used exclusively to pay qualified down payment expenses of any account beneficiary shall not be includible in gross income. (2) Inclusion of amounts not used for qualified down payment expenses Any amount paid or distributed out of a down payment savings account which is not used exclusively to pay the qualified down payment expenses of the account beneficiary shall be included in the gross income of such beneficiary. (3) Excess contributions returned before due date of return (A) In general If any excess contribution is contributed for a taxable year to any down payment savings account of an individual, paragraph (2) shall not apply to distributions from the down payment savings accounts of such individual (to the extent such distributions do not exceed the aggregate excess contributions to all such accounts of such individual for such year) if\u2014 (i) such distribution is received by the individual on or before the last day prescribed by law (including extensions of time) for filing such individual's return for such taxable year, and (ii) such distribution is accompanied by the amount of net income attributable to such excess contribution. Any net income described in clause (ii) shall be included in the gross income of the individual for the taxable year in which it is received. (B) Excess contribution For purposes of subparagraph (A) , the term excess contribution means any contribution to a down payment savings account (other than a rollover contribution described in paragraph (5) ) which is not deductible under this section. (4) Additional tax for distributions not used for down payment expenses (A) In general The tax imposed by this chapter for any taxable year on any taxpayer who receives a payment or distribution from a down payment savings account which is includible in gross income shall be increased by 20 percent of the amount which is so includible. (B) Exceptions Subparagraph (A) shall not apply if the payment or distribution is\u2014 (i) made to the account beneficiary (or to the estate of such account beneficiary) on or after the death of such account beneficiary, or (ii) attributable to such account beneficiary\u2019s being disabled (within the meaning of section 72(m)(7)). (5) Rollover contribution An amount is described in this paragraph as a rollover contribution if it meets the following requirements: (A) In general Paragraph (2) shall not apply to any amount paid or distributed from a down payment savings account to the account beneficiary to the extent the amount received is paid into a down payment savings account for the benefit of such beneficiary not later than the 60th day after the day on which the beneficiary receives the payment or distribution. (B) Limitation This paragraph shall not apply to any amount described in subparagraph (A) received by an individual from a down payment savings account if, at any time during the 1-year period ending on the day of such receipt, such individual received any other amount described in subparagraph (A) from a down payment savings account which was not includible in the individual's gross income because of the application of this paragraph. (6) Special rules for death and divorce Rules similar to the rules of paragraphs (7) and (8) of section 223(f) shall apply for purposes of this section. (7) Disallowance of excluded amounts as deduction, credit, or exclusion No deduction, credit, or exclusion shall be allowed to the taxpayer under any other section of this chapter for any qualified down payment expenses to the extent taken into account in determining the amount of the exclusion under paragraph (1) . (8) Account termination Rules similar to the rules of paragraphs (2) and (4) of section 408(e) shall apply to down payment savings accounts, and any amount treated as distributed under such rules shall be treated as not used to pay qualified down payment expenses. (e) Reports (1) In general The trustee of a down payment savings account shall make such reports regarding such account to the Secretary and to the account beneficiary with respect to contributions, distributions, and such other matters as the Secretary may require. The reports required by this subsection shall be filed at such time and in such manner and furnished to such individuals at such time and in such manner as may be required. (2) Rollover distributions In the case of any distribution described in subsection (d)(5) , the officer or employee having control of the down payment savings account (or their designee) shall provide a report to the trustee of the down payment savings account to which the distribution is made. Such report shall be filed at such time and in such manner as the Secretary may require and shall include information with respect to the contributions, distributions, and earnings of the down payment savings account as of the date of the distribution described in such subsection, together with such other matters as the Secretary may require. .\n##### (b) Deduction allowed to non-Itemizers\nSection 63(b) of such Code is amended\u2014\n**(1)**\nin paragraph (6), by striking and and inserting a comma,\n**(2)**\nin paragraph (7), by striking the period at the end and inserting , and , and\n**(3)**\nby adding at the end the following new paragraph:\n(8) the deduction allowed by section 223A. .\n##### (c) Tax on prohibited transactions\n**(1)**\nSection 4975(c) of such Code is amended by adding at the end the following new paragraph:\n(8) Special rule for down payment savings accounts An individual for whose benefit a down payment savings account (within the meaning of section 223A(b)(1)) is established shall be exempt from the tax imposed by this section with respect to any transaction concerning such account (which would otherwise be taxable under this section) if, with respect to such transaction, the account ceases to be a down payment savings account by reason of the application of section 223(c)(8) to such account. .\n**(2)**\nSection 4975(e)(1) of such Code is amended by striking or at the end of subparagraph (F), by redesignating subparagraph (G) as subparagraph (H), and by inserting after subparagraph (F) the following new subparagraph:\n(G) a down payment savings account described in section 223A(b)(1). .\n##### (d) Penalty for failure To file reports\nSection 6693(a)(2) of such Code is amended by striking and at the end of subparagraph (E), by striking the period at the end of subparagraph (F) and inserting , and , and by inserting after subparagraph (F) the following new subparagraph:\n(G) Section 223A(g) (relating to down payment savings accounts). .\n##### (e) Conforming amendments\n**(1)**\nSection 26(b)(2) of such Code is amended by striking and at the end of subparagraph (Y), by striking the period at the end of subparagraph (Z) and inserting , and , and by inserting after subparagraph (Z) the following new subparagraph:\n(AA) section 223A(c)(2) (relating to additional tax on down payment savings account not used for qualified down payment expenses). .\n**(2)**\nSection 877A of such Code is amended\u2014\n**(A)**\nin subsection (e)(2) by inserting a down payment savings account (as defined in section 223A), after section 223), , and\n**(B)**\nin subsection (g)(6) by inserting 223(e)(4), , after 529A(c)(3), .\n**(3)**\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 223 the following new item:\nSec. 223A. Down payment savings account. .\n##### (f) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-12-09",
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
        "name": "Taxation",
        "updateDate": "2026-01-06T16:09:11Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6542ih.xml"
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
      "title": "First Home Savings Opportunity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "First Home Savings Opportunity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow the establishment of down payment savings accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:19Z"
    }
  ]
}
```
