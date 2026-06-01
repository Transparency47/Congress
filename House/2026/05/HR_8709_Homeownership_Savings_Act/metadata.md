# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8709?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8709
- Title: Homeownership Savings Act
- Congress: 119
- Bill type: HR
- Bill number: 8709
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-13T16:06:03Z
- Update date including text: 2026-05-13T16:06:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8709",
    "number": "8709",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Homeownership Savings Act",
    "type": "HR",
    "updateDate": "2026-05-13T16:06:03Z",
    "updateDateIncludingText": "2026-05-13T16:06:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:03:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8709ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8709\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Ms. Stevens introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow the establishment of homeownership savings accounts.\n#### 1. Short title\nThis Act may be cited as the Homeownership Savings Act .\n#### 2. Homeownership savings account\n##### (a) In general\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 223 the following new section:\n223A. Homeownership savings account (a) Deduction allowed In the case of an account beneficiary, there shall be allowed as a deduction for the taxable year an amount equal to the aggregate amount paid in cash during such taxable year by or on behalf of such individual to a homeownership savings account of such individual. (b) Limitations (1) Annual dollar limitation The amount allowable as a deduction under subsection (a) to an individual for the taxable year shall not exceed\u2014 (A) $3,000 in the case of a joint return, (B) $2,500 in the case of a head of household, or (C) $2,000 in the case of any other individual. (2) Limitation based on earned income (A) In general The amount allowable as a deduction under subsection (a) shall not exceed such individual\u2019s earned income for the taxable year. (B) Special rule for joint returns In the case of an individual whose earned income is less than the earned income of such individual\u2019s spouse and files a joint return for the taxable year, the amount allowable as a deduction under subsection (a) shall not exceed the excess (if any) of\u2014 (i) the earned income of the taxpayer for such taxable year, over (ii) the deduction allowable under subsection (a) to such individual\u2019s spouse for such taxable year. (C) Earned income For purposes of this paragraph, the term earned income has the meaning given such term in section 32(c)(2). (3) Limitation based on modified adjusted gross income (A) In general The maximum amount that may otherwise be allowable as a deduction under subsection (a) shall be reduced (but not below zero) by an amount which bears the same ratio to such maximum amount as\u2014 (i) in the case of a joint return\u2014 (I) the excess (if any) of the modified adjusted gross income of the account beneficiary for such taxable year over $242,000, bears to (II) $10,000, (ii) in the case of a head of household\u2014 (I) the excess (if any) of the modified adjusted gross income of the account beneficiary for such taxable year over $200,000, bears to (II) $20,000, or (iii) in the case of any other individual\u2014 (I) the excess (if any) of the modified adjusted gross income of the account beneficiary for such taxable year over $153,000, bears to (II) $15,000. (B) Modified adjusted gross income For purposes of this paragraph, the term modified adjusted gross income means the adjusted gross income of the taxpayer for the taxable year increased by any amount excluded from gross income under section 911, 931, or 933. (4) Denial of deduction to dependants No deduction shall be allowed under this section to any individual with respect to whom a deduction under section 151 is allowable to another taxpayer for a taxable year beginning in the calendar year in which such individual's taxable year begins. (c) Definitions and special rules For purposes of this section\u2014 (1) Homeownership savings account The term homeownership savings account means a trust created or organized in the United States exclusively for the purpose of paying the qualified homeownership expenses of the account beneficiary (and designated as a homeownership savings account at the time created or organized), but only if the written governing instrument creating the trust meets the following requirements: (A) No contribution will be accepted\u2014 (i) if such contribution would result in lifetime aggregate contributions to the account exceeding $40,000, (ii) unless it is in cash, or (iii) if such account beneficiary has not made the certification required under subparagraph (F) . (B) The trustee is a bank (as defined in section 408(n)) or another person who demonstrates to the satisfaction of the Secretary that the manner in which that person will administer the trust will be consistent with the requirements of this section. (C) No part of the trust assets will be invested in life insurance contracts. (D) The assets of the trust shall not be commingled with other property except in a common trust fund or common investment fund. (E) The account beneficiary has attained the age of 18. (F) The account beneficiary certifies, under penalty of perjury, at the time that the account is established that such account beneficiary would be a first-time homebuyer with respect to a purchase of a principal residence on the date of such establishment. (2) Qualified homeownership expenses The term qualified homeownership expenses means a down payment or closing costs relating to the purchase of the primary residence of the account beneficiary of a homeownership savings account if such account beneficiary is a first-time homebuyer. (3) No contribution for individual who is not a first-time homebuyer In the case of an individual who would not be a first-time homebuyer with respect to a purchase of a principal residence on the date of any contribution to a homeownership savings account, paragraph (1)(A)(i) shall be applied by substituting $0 for $40,000 . (4) First-time homebuyer The term first-time homebuyer means an individual if\u2014 (A) such individual is a first-time homebuyer (as defined in section 36(c)(1)), and (B) such individual has never purchased a residential property using an amount which was excluded from the gross income of such individual by reason of subsection (e)(1) . (5) Account beneficiary The term account beneficiary means the individual on whose behalf the homeownership savings account is established. (6) Certain rules to apply Rules similar to the following rules shall apply for purposes of this section: (A) Section 219(d)(2) (relating to no deduction for rollovers). (B) Section 219(f)(3) (relating to time when contributions deemed made). (C) Section 219(f)(5) (relating to employer payments). (D) Section 408(g) (relating to community property laws). (d) Tax treatment of accounts (1) In general A homeownership savings account is exempt from taxation under this subtitle unless such account has ceased to be a homeownership savings account. Notwithstanding the preceding sentence, any such account is subject to the taxes imposed by section 511 (relating to imposition of tax on unrelated business income of charitable, etc. organizations). (2) Account terminations (A) Acquisition of principal residence If the account beneficiary acquires an ownership interest in a principal residence\u2014 (i) each homeownership savings account of such beneficiary shall cease to be a homeownership savings account as of the close of the 60-day period beginning on the date of such acquisition, and (ii) the balance of such account as of such date shall be treated as distributed to such beneficiary. (B) Prohibited transactions, etc Rules similar to the rules of paragraphs (2) and (4) of section 408(e) shall apply to any homeownership savings account, and any amounts treated as distributed under such rules shall be treated as not used to pay qualified homeownership expenses. (e) Tax treatment of distributions (1) Amounts used for qualified homeownership expenses Any amount paid or distributed out of a homeownership savings account which is used exclusively to pay qualified homeownership expenses of any account beneficiary shall not be includible in gross income. (2) Inclusion of amounts not used for qualified homeownership expenses Any amount paid or distributed out of a homeownership savings account which is not used exclusively to pay the qualified homeownership expenses of the account beneficiary shall be included in the gross income of such beneficiary. (3) Excess contributions returned before due date of return (A) In general If any excess contribution is contributed for a taxable year to any homeownership savings account of an individual, paragraph (2) shall not apply to distributions from the homeownership savings accounts of such individual (to the extent such distributions do not exceed the aggregate excess contributions to all such accounts of such individual for such year) if\u2014 (i) such distribution is received by the individual on or before the last day prescribed by law (including extensions of time) for filing such individual's return for such taxable year, and (ii) such distribution is accompanied by the amount of net income attributable to such excess contribution. Any net income described in clause (ii) shall be included in the gross income of the individual for the taxable year in which it is received. (B) Excess contribution For purposes of subparagraph (A) , the term excess contribution means any contribution if\u2014 (i) after such contribution, the aggregate contribution to homeownership savings accounts of the account beneficiary exceeds the amount in effect under subsection (c)(1)(A)(i) , or (ii) if the amount of such contribution is not allowable as a deduction by reason of paragraph (2)(A) or (3)(a) of subsection (b) . (4) Additional tax for distributions not used for homeownership expenses (A) In general The tax imposed by this chapter for any taxable year on any taxpayer who receives a payment or distribution from a homeownership savings account which is includible in gross income shall be increased by 20 percent of the amount which is so includible. (B) Exceptions Subparagraph (A) shall not apply if the payment or distribution is\u2014 (i) made to the account beneficiary (or to the estate of such account beneficiary) on or after the death of such account beneficiary, or (ii) attributable to such account beneficiary\u2019s being disabled (within the meaning of section 72(m)(7)). (5) Rollover contribution An amount is described in this paragraph as a rollover contribution if it meets the following requirements: (A) In general Paragraph (2) shall not apply to any amount paid or distributed from a homeownership savings account to the account beneficiary to the extent the amount received is paid into a homeownership savings account for the benefit of such beneficiary not later than the 60th day after the day on which the beneficiary receives the payment or distribution. (B) Limitation This paragraph shall not apply to any amount described in subparagraph (A) received by an individual from a homeownership savings account if, at any time during the 1-year period ending on the day of such receipt, such individual received any other amount described in subparagraph (A) from a homeownership savings account which was not includible in the individual's gross income because of the application of this paragraph. (6) Special rules for death and divorce Rules similar to the rules of paragraphs (7) and (8) of section 223(f) shall apply for purposes of this section. (7) Disallowance of excluded amounts as deduction, credit, or exclusion No deduction, credit, or exclusion shall be allowed to the taxpayer under any other section of this chapter for any qualified homeownership expenses to the extent taken into account in determining the amount of the exclusion under paragraph (1) . (f) Salary reduction prohibited No employer shall directly reduce the wages or salary of an employee by reason of a contribution made by such employer to a homeownership savings account on behalf of such employee. (g) Inflation adjustment (1) In general In the case of any taxable year beginning after 2026, the dollar amounts in subsection (b) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost of living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (ii) thereof. (2) Rounding If any increase under paragraph (1) is not a multiple of $100, such increase shall be rounded to the nearest multiple of $100. (h) Reports (1) In general The trustee of a homeownership savings account shall make such reports regarding such account to the Secretary and to the account beneficiary with respect to contributions, distributions, and such other matters as the Secretary may require. (2) Rollover distributions In the case of any distribution described in subsection (e)(5) , the officer or employee having control of the homeownership savings account (or their designee) shall provide a report to the trustee of the homeownership savings account to which the distribution is made. Such report shall include information with respect to the contributions, distributions, and earnings of the homeownership savings account as of the date of the distribution described in such subsection, together with such other matters as the Secretary may require. (3) Time and manner The reports required by this subsection shall be filed at such time and in such manner and furnished to such individuals at such time and in such manner as the Secretary determines appropriate. .\n##### (b) Deduction allowed above the line\nSection 62(a) of such Code is amended by inserting after paragraph (21) the following new paragraph:\n(22) Homeownership savings accounts The deduction allowed by section 223A. .\n##### (c) Exclusions for employer contributions to homeownership savings accounts\n**(1) Exclusion from income tax**\n**(A) In general**\nPart III of subchapter B of chapter 1 of such Code is amended by inserting after section 139I the following new section:\n139J. Homeownership savings account contributions In the case of an account beneficiary (as defined in section 223A(c)(5)), gross income does not include amounts contributed by such account beneficiary\u2019s employer to any homeownership savings account (as defined in section 223A(c)(1)) of such account beneficiary if such contribution, taken in aggregate with all other contributions in all taxable years to homeownership savings accounts (as so defined) of such beneficiary, does not exceed the amount in effect under section 223A(c)(1)(A)(i). .\n**(B) Clerical amendment**\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Homeownership savings account contributions. .\n**(2) Exclusion from employment taxes**\n**(A) Social security taxes**\n**(i) In general**\nSection 3121(a) of such Code is amended by striking or at the end of paragraph (22)(B), by striking the period at the end of paragraph (23) and inserting , or , and by inserting after paragraph (23) the following new paragraph:\n(24) any payment made to or for the benefit of an employee if at the time of such payment it is reasonable to believe that the employee will be able to exclude such payment from income under section 139J. .\n**(ii) Conforming amendment to Social Security Act**\nSection 209(a) of the Social Security Act is amended by striking or at the end of paragraph (19), by striking ). at the end of paragraph (20) and inserting ; or , and by inserting after paragraph (20) the following new paragraph:\n(21) any reimbursement which is excludable from gross income under section 139J of the Internal Revenue Code of 1986. .\n**(B) Railroad retirement tax**\nSection 3231(e) of such Code is amended by adding at the end the following new paragraph:\n(13) Homeownership savings account contributions The term \u2018compensation\u2019 shall not include any payment made to or for the benefit of an employee if at the time of such payment it is reasonable to believe that the employee will be able to exclude such payment from income under section 139J. .\n**(C) Unemployment tax**\nSection 3306(b) of such Code is amended by striking or at the end of paragraph (19)(B), by striking the period at the end of paragraph (20) and inserting ; or , and by inserting after paragraph (20) the following new paragraph:\n(21) any payment made to or for the benefit of an employee if at the time of such payment it is reasonable to believe that the employee will be able to exclude such payment from income under section 139J. .\n**(D) Withholding tax**\nSection 3401(a) of such Code is amended by striking or at the end of paragraph (22), by striking the period at the end of paragraph (23) and inserting ; or , and by inserting after paragraph (23) the following new paragraph:\n(24) any payment made to or for the benefit of an employee if at the time of such payment it is reasonable to believe that the employee will be able to exclude such payment from income under section 139J. .\n**(3) Employer contributions required to be shown on W-2**\nSection 6051(a) of such Code is amended by striking and at the end of paragraph (16), by striking the period at the end of paragraph (17) and inserting , and , and by inserting after paragraph (17) the following new paragraph:\n(18) the amount contributed to any homeownership savings account (as defined in section 223A(c)(1)) of such employee. .\n##### (d) Tax on excess contributions\n**(1) In general**\nSection 4973(a) of such Code is amended by striking or at the end of paragraph (5), by inserting or at the end of paragraph (6), and by inserting after paragraph (6) the following new paragraph:\n(7) a homeownership savings account (within the meaning of section 223A). .\n**(2) Excess contribution**\nSection 4973 of such Code is amended by adding at the end the following new subsection:\n(i) Excess contributions to homeownership savings account (1) In general For purposes of this section, in the case of homeownership savings accounts (as defined in section 223A), the term excess contributions means the sum of\u2014 (A) the amount of any excess contribution (as defined in section 223A(e)(3)(B) for the taxable year, plus (B) the excess (if any) of\u2014 (i) the amount determined under this subsection for the preceding taxable year, over (ii) the distribution out of the homeownership savings accounts which were included in gross income under section 223A(e)(1) during the taxable year. (2) Treatment of returned excess contributions For purposes of this subsection, any contribution which is distributed out of the homeownership savings account in a distribution to which section 223A(e)(3)(A) applies shall be treated as an amount not contributed. .\n##### (e) Tax on prohibited transactions\n**(1)**\nSection 4975(c) of such Code is amended by adding at the end the following new paragraph:\n(8) Special rule for homeownership savings accounts An individual for whose benefit a homeownership savings account (within the meaning of section 223A(c)(1)) is established shall be exempt from the tax imposed by this section with respect to any transaction concerning such account (which would otherwise be taxable under this section) if, with respect to such transaction, the account ceases to be a homeownership savings account by reason of the application of section 223A(d)(2) to such account. .\n**(2)**\nSection 4975(e)(1) of such Code is amended by striking or at the end of subparagraph (F), by redesignating subparagraph (G) as subparagraph (H), and by inserting after subparagraph (F) the following new subparagraph:\n(G) a homeownership savings account described in section 223A(c). .\n##### (f) Penalty for failure to file reports\nSection 6693(a)(2) of such Code is amended by striking and at the end of subparagraph (E), by striking the period at the end of subparagraph (F) and inserting , and , and by inserting after subparagraph (F) the following new subparagraph:\n(G) Section 223A(h) (relating to homeownership savings accounts). .\n##### (g) Conforming amendments\n**(1)**\nSection 26(b)(2) of such Code is amended by striking and at the end of subparagraph (Y), by striking the period at the end of subparagraph (Z) and inserting , and , and by inserting after subparagraph (Z) the following new subparagraph:\n(AA) section 223A(e)(2) (relating to additional tax on homeownership savings account not used for qualified homeownership expenses). .\n**(2)**\nSection 408(e)(2)(ii) of such Code is amended by inserting or to a homeownership savings account under section 223A(e)(7) before the period.\n**(3)**\nSection 530(d)(9)(A)(ii) of such Code is amended by inserting , to a homeownership savings account under section 223A(e)(7), after section 408(e)(2) .\n**(4)**\nSection 877A of such Code is amended\u2014\n**(A)**\nin subsection (e)(2) by inserting a homeownership savings account (as defined in section 223A), after section 223), , and\n**(B)**\nin subsection (g)(6) by inserting 223A(e)(4), , after 529A(c)(3), .\n**(5)**\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 223 the following new item:\nSec. 223A. Homeownership savings account. .\n##### (h) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-05-07",
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
        "updateDate": "2026-05-13T16:06:03Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8709ih.xml"
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
      "title": "Homeownership Savings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Homeownership Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow the establishment of homeownership savings accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T08:18:35Z"
    }
  ]
}
```
