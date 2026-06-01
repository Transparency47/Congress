# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7756?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7756
- Title: First-time Homebuyer Savings Account Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7756
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-19T20:11:08Z
- Update date including text: 2026-03-19T20:11:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7756",
    "number": "7756",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "First-time Homebuyer Savings Account Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-19T20:11:08Z",
    "updateDateIncludingText": "2026-03-19T20:11:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:01:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7756ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7756\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Barrett introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish tax-advantaged homeowner savings accounts.\n#### 1. Short title\nThis Act may be cited as the First-time Homebuyer Savings Account Act of 2026 .\n#### 2. Homeowner savings account\n##### (a) In general\nPart VII of subchapter B of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by inserting after section 225 the following new section:\n225A. Homeowner savings account (a) Deduction allowed In the case of an eligible individual, there shall be allowed as a deduction for the taxable year an amount equal to the aggregate amount paid in cash during such taxable year by or on behalf of such individual to a homeowner savings account of such individual. (b) Definitions For purposes of this section\u2014 (1) Homeowner savings account The term homeowner savings account means a trust created or organized in the United States as a homeowner savings account exclusively for the purpose of paying qualified homeowner expenses of the account beneficiary, but only if the written governing instrument creating the trust meets the following requirements: (A) Except in the case of a rollover contribution, no contribution will be accepted\u2014 (i) unless it is in cash, (ii) to the extent such contribution, when added to previous contributions to the trust for the calendar year, exceeds the amount in effect for the calendar year under subparagraph (A) of section 219(b)(5) (determined without regard to subparagraph (B) thereof), and (iii) to the extent that after such contribution the amount held in the account would exceed an amount equal to 20 percent of the amount published under paragraph (6) for the year in which the contribution is made. (B) The trustee is a bank (as defined in section 408(n)), an insurance company (as defined in section 816), or another person who demonstrates to the satisfaction of the Secretary that the manner in which such person will administer the trust will be consistent with the requirements of this section. (C) No part of the trust assets will be invested in life insurance contracts. (D) The assets of the trust will not be commingled with other property except in a common trust fund or common investment fund. (E) The interest of an individual in the balance in his account is nonforfeitable. (2) Eligible individual The term eligible individual means an individual if such individual (and, if married, such individual\u2019s spouse) had no present ownership interest in a principal residence during the 3-year period ending on the present date. (3) Qualified homeowner expenses The term qualified homeowner expenses means amounts paid or incurred to\u2014 (A) purchase or construct the principal residence of the individual if such individual had no present ownership interest in a principal residence during the 3-year period ending on the date of the purchase or beginning of construction of the principal residence, or (B) make alterations, repairs, or improvements which meet the requirements of section 143(k)(4) (determined without regard to the dollar limitation provided in such section) to such principal residence so purchased or constructed. (4) Account beneficiary The term account beneficiary means the individual on whose behalf the homeowner savings account was established. (5) Principal residence The term principle residence has the same meaning as when used in section 121. (6) Publication of national average single family home price The Secretary of the Treasury shall, not later than December 31 of each calendar year, publish the estimated national average price of a single family home for the following calendar year. (7) Rollover contribution The term rollover contribution means an amount paid or distributed from a homeowner savings account to the account beneficiary to the extent that\u2014 (A) the amount received is paid into a homeowner savings account for the benefit of such beneficiary not later than the 60th day after the day on which the beneficiary receives the payment or distribution, and (B) such account beneficiary did not receive any other amount described in subparagraph (A) from a homeowner savings account which was not includible in the individual\u2019s gross income because of subsection (d)(2)(B) during the 1-year period ending on the date of such receipt. (c) Treatment of contributions (1) Contribution limit The aggregate amount of contributions for any taxable year to all homeowner savings accounts maintained for the benefit of an individual shall not exceed the lesser of\u2014 (A) the amount in effect for the taxable year in which such contributions are made under subparagraph (A) of section 219(b)(5) (determined without regard to subparagraph (B) thereof), (B) an amount equal to the compensation includible in the individual\u2019s gross income for such taxable year, or (C) the amount that would result in the amount held in the account exceeding an amount equal to 20 percent of the amount published under subsection (b)(6) for the year in which the contribution is made. (2) Limitation based on modified adjusted gross income The amount determined under paragraph (1)(A) for any taxable year shall be reduced (but not below zero) by the amount which bears the same ratio to such amount as\u2014 (A) the excess of\u2014 (i) the taxpayer\u2019s adjusted gross income for such taxable year, over (ii) the applicable dollar amount (as defined in section 219(g)(3)(B), determined after the application of section 219(g)(8)), bears to (B) $10,000 ($20,000 in the case of a joint return or a married individual filing a separate return). The rules of subparagraphs (B) and (C) of section 219(g)(2) shall apply to any reduction under this paragraph. (3) Spousal contribution (A) In general In the case of an individual to whom this paragraph applies for the taxable year, the limitation of paragraph (1) shall be equal to the lesser of\u2014 (i) the compensation includible in such individual's gross income for the taxable year, plus (ii) the compensation includible in the gross income of such individual's spouse for the taxable year reduced by the amount allowed as a deduction under subsection (a) to such spouse for such taxable year. (B) Individual to whom subparagraph (A) applies Subparagraph (A) shall apply to any individual if\u2014 (i) such individual files a joint return for the taxable year, and (ii) the amount of compensation (if any) includible in such individual's gross income for the taxable year is less than the compensation includible in the gross income of such individual's spouse for the taxable year. (d) Treatment of distributions (1) Amounts used for qualified homeowner expenses Any amount paid or distributed out of a homeowner savings account which is used exclusively to pay qualified homeowner expenses shall not be includible in gross income. (2) Inclusion of amounts not used for qualified homeowner expenses Any amount paid or distributed out of a homeowner savings account which is not\u2014 (A) used exclusively to pay the qualified homeowner expenses of the account beneficiary, (B) an exempted distribution, or (C) a rollover contribution, shall be included in the gross income of such beneficiary and the amount of any tax imposed by this chapter shall be increased by 10 percent on any amount so includible. (3) Exempted distribution For purposes of this subsection, the term exempted distribution means an amount paid or distributed out of a homeowner savings account by reason of\u2014 (A) an emergency, including\u2014 (i) the loss of a job or major source of income, or (ii) a major health event leading to substantial medical expenses, (B) a life event, including\u2014 (i) acquiring a present ownership interest in a principal residence by reason of marriage, (ii) death of the account beneficiary, or (iii) the account beneficiary residing outside the United States, or (C) such other circumstances as the Secretary determines appropriate by regulation. (4) Excess contributions returns before due date of return (A) In general If any excess contribution is contributed for a taxable year to any homeowner savings account of an individual, paragraph (2) shall not apply to distributions from the homeowner savings accounts of such individual (to the extent such distributions do not exceed the aggregate excess contributions to all such accounts of such individual for such year) if\u2014 (i) such distribution is received by the individual on or before the last day prescribed by law (including extensions of time) for filing such individual's return for such taxable year, and (ii) such distribution is accompanied by the amount of net income attributable to such excess contribution. Any net income described in clause (ii) shall be included in the gross income of the individual for the taxable year in which it is received. (B) Excess contribution defined For purposes of subparagraph (A), the term excess contribution means any contribution (other than a rollover contribution) which is not excludable from gross income under this section. (e) Tax treatment of accounts (1) In general A homeowner savings account is exempt from taxation under this subtitle unless such account has ceased to be a homeowner savings account. Notwithstanding the preceding sentence, any such account is subject to the taxes imposed by section 511 (relating to imposition of tax on unrelated business income of charitable, etc. organizations). (2) Account termination Rules similar to the rules of paragraphs (2) and (4) of section 408(e) shall apply to homeowner savings accounts, and any amount treated as distributed under such rules shall be treated as not used to pay qualified homeowner expenses. (f) Custodial account For purposes of this section, a custodial account shall be treated as a trust if the assets of such account are held by a bank (as defined in section 408(n)) or another person who demonstrates, to the satisfaction of the Secretary, that the manner in which he will administer the account will be consistent with the requirements of this section, and if the custodial account would, except for the fact that it is not a trust, constitute an account described in subsection (b)(1). For purposes of this title, in the case of a custodial account treated as a trust by reason of the preceding sentence, the custodian of such account shall be treated as the trustee thereof. .\n##### (b) Tax on excess contributions\n**(1) In general**\nSection 4973(a) of such Code is amended\u2014\n**(A)**\nin paragraph (5), by striking or ,\n**(B)**\nin paragraph (6), by inserting or after the comma, and\n**(C)**\nby inserting after paragraph (6) the following new paragraph:\n(7) a homeowner savings account (within the meaning of section 225A(b)(1)), .\n**(2) Definition of excess contribution in 4973**\nSection 4973 of such Code is amended by adding at the end the following new subsection:\n(i) Excess contributions to homeowner savings account For purposes of this section, in the case of a homeowner savings account (within the meaning of section 225A(b)(1)), the term excess contribution means the amount by which the amount contributed for the taxable year to such account exceeds the contribution limit under 225A(c)(1). .\n##### (c) Clerical amendment\nThe table of sections for part VII of subchapter B of chapter 1 of subtitle A of such Code is amended by inserting after the item relating to section 225 the following new item:\nSec. 225A. Homeowner savings account. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-03-19T20:11:08Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7756ih.xml"
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
      "title": "First-time Homebuyer Savings Account Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T08:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "First-time Homebuyer Savings Account Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T08:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish tax-advantaged homeowner savings accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T08:03:27Z"
    }
  ]
}
```
