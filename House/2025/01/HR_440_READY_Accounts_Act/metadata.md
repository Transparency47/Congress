# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/440?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/440
- Title: READY Accounts Act
- Congress: 119
- Bill type: HR
- Bill number: 440
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2026-02-10T09:05:23Z
- Update date including text: 2026-02-10T09:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/440",
    "number": "440",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "READY Accounts Act",
    "type": "HR",
    "updateDate": "2026-02-10T09:05:23Z",
    "updateDateIncludingText": "2026-02-10T09:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:02:10Z",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MD"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "NJ"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr440ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 440\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Lee of Florida (for herself, Mr. Moskowitz , Mr. Buchanan , and Mr. Scott Franklin of Florida ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) accounts.\n#### 1. Short title\nThis Act may be cited as the READY Accounts Act .\n#### 2. READY accounts\n##### (a) In general\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 224 as section 225 and by inserting after section 223 the following new section:\n224. Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) accounts (a) Deduction allowed In the case of an individual, there shall be allowed as a deduction for the taxable year an amount equal to the aggregate amount paid in cash during such taxable year by or on behalf of such individual to a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account such individual. (b) Limitation (1) In general The amount allowable as a deduction under subsection (a) to an individual for the taxable year shall not exceed $4,500. (2) Inflation adjustment (A) In general In the case of any taxable year beginning in a calendar year after 2025, the $4,500 dollar amount under paragraph (1) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting in subparagraph (A)(ii) thereof calendar year 2024 for calendar year 2016 . (B) Rounding If any amount as adjusted under paragraph (1) is not a multiple of $50, such dollar amount shall be rounded to the next lowest multiple of $50. (c) Residential Emergency Asset-Accumulation Deferred Taxation Yield (READY) account For purposes of this section\u2014 (1) In general The term Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account means a trust created or organized in the United States as a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account exclusively for the purpose of paying the qualified home disaster mitigation and recovery expenses of the account beneficiary, but only if the written governing instrument creating the trust meets the following requirements: (A) Except in the case of a rollover contribution described in subsection (e)(5), no contribution will be accepted\u2014 (i) unless it is in cash, or (ii) to the extent such contribution, when added to previous contributions to the trust for the calendar year, exceeds the dollar amount in effect under subsection (b)(1). (B) The trustee is a bank (as defined in section 408(n)) or another person who demonstrates to the satisfaction of the Secretary that the manner in which such person will administer the trust will be consistent with the requirements of this section. (C) No part of the trust assets will be invested in life insurance contracts. (D) The assets of the trust will not be commingled with other property except in a common trust fund or common investment fund. (E) The interest of an individual in the balance in his account is nonforfeitable. (2) Qualified home disaster mitigation and recovery expenses (A) In general The term qualified home disaster mitigation and recovery expenses means, with respect to an account beneficiary, amounts paid by such beneficiary for\u2014 (i) qualified disaster mitigation measures, or (ii) qualified disaster recovery costs, with respect to a qualified home of the taxpayer. (B) Qualified disaster mitigation measures For purposes of subparagraph (A)\u2014 (i) In general The term qualified disaster mitigation measures means any measure described in clause (ii) with respect to a qualified home of the taxpayer if\u2014 (I) such measure meets such criteria as the Secretary, in consultation with the Administrator of the Federal Emergency Management Agency, considers appropriate to mitigate damage from a natural or other disaster, and (II) is certified by a qualified industry professional as meeting such criteria. (ii) Mitigation measures The following measures are measures described in this clause: (I) Installing a roofing underlayment to sheathing. (II) Replacing a roof covering. (III) Applying a foam adhesive to reinforce the roof structure. (IV) Strengthening connection of roof deck to roof framing. (V) Strengthening roof-to-wall connections. (VI) Strengthening soffits. (VII) Strengthening attic ventilation openings. (VIII) Installing impact-resistant windows. (IX) Installing impact-resistant entry doors. (X) Elevating the residential home. (XI) Installing ground anchors. (XII) If the qualified home was built according to a building code from a prior year, achieving the current building code standard in the applicable State or locality. (XIII) Such other measures determined by the Secretary, in consultation with the Administrator of the Federal Emergency Management Agency, to be consistent with the purposes of this section. (iii) Qualified industry professional The term qualified industry professional means an individual who meets such rules and standards as determined appropriate by the Secretary, in consultation with the Administrator of the Federal Emergency Management Agency. (C) Qualified disaster recovery costs For purposes of subparagraph (A), the term qualified disaster recovery costs means costs for repairing damage to the qualified home of the taxpayer if such damage arises from fire, storm, or other casualty and such costs are not compensated for by insurance or otherwise. (D) Qualified home For purposes of this section, the term qualified home means, with respect to any taxable year, any structure which is\u2014 (i) owned by the taxpayer, and (ii) used by the taxpayer as the taxpayer's principal residence (within the meaning of section 121) for the taxable year. (3) Account beneficiary The term account beneficiary means the individual on whose behalf the Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account was established. (4) Certain rules to apply Rules similar to the following rules shall apply for purposes of this section: (A) Section 219(d)(2) (relating to no deduction for rollovers). (B) Section 219(f)(3) (relating to time when contributions deemed made). (C) Section 219(f)(5) (relating to employer payments). (D) Section 408(g) (relating to community property laws). (E) Section 408(h) (relating to custodial accounts). (d) Tax treatment of accounts (1) In general A Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account is exempt from taxation under this subtitle unless such account has ceased to be a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account. Notwithstanding the preceding sentence, any such account is subject to the taxes imposed by section 511 (relating to imposition of tax on unrelated business income of charitable, etc. organizations). (2) Account terminations Rules similar to the rules of paragraphs (2) and (4) of section 408(e) shall apply to Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) accounts, and any amount treated as distributed under such rules shall be treated as not used to pay qualified home disaster mitigation and recovery expenses. (e) Tax treatment of distributions (1) Amounts used for qualified home disaster mitigation and recovery expenses Any amount paid or distributed out of a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account which is used exclusively to pay qualified home disaster mitigation and recovery expenses of the account beneficiary shall not be includible in gross income. (2) Inclusion of amounts not used for qualified home disaster mitigation and recovery expenses Any amount paid or distributed out of a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account which is not used exclusively to pay the qualified home disaster mitigation and recovery expenses of the account beneficiary shall be included in the gross income of such beneficiary. (3) Excess contributions returned before due date of return (A) In general If any excess contribution is contributed for a taxable year to any Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account of an individual, paragraph (2) shall not apply to distributions from the Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) accounts of such individual (to the extent such distributions do not exceed the aggregate excess contributions to all such accounts of such individual for such year) if\u2014 (i) such distribution is received by the individual on or before the last day prescribed by law (including extensions of time) for filing such individual's return for such taxable year, and (ii) such distribution is accompanied by the amount of net income attributable to such excess contribution. Any net income described in clause (ii) shall be included in the gross income of the individual for the taxable year in which it is received. (B) Excess contribution For purposes of subparagraph (A), the term excess contribution means any contribution (other than a rollover contribution described in paragraph (5)) which is not deductible under this section. (4) Additional tax on distributions not used for qualified home disaster mitigation and recovery expenses The tax imposed by this chapter on the account beneficiary for any taxable year in which there is a payment or distribution from a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account of such beneficiary which is includible in gross income under paragraph (2) shall be increased by 20 percent of the amount which is so includible. (5) Rollover contribution An amount is described in this paragraph as a rollover contribution if it meets the requirements of subparagraphs (A) and (B). (A) In general Paragraph (2) shall not apply to any amount paid or distributed from a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account to the account beneficiary to the extent the amount received is paid into a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account for the benefit of such beneficiary not later than the 60th day after the day on which the beneficiary receives the payment or distribution. (B) Limitation This paragraph shall not apply to any amount described in subparagraph (A) received by an individual from a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account if, at any time during the 1-year period ending on the day of such receipt, such individual received any other amount described in subparagraph (A) from a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account which was not includible in the individual's gross income because of the application of this paragraph. (6) Transfer of account incident to divorce The transfer of an individual's interest in a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account to an individual's spouse or former spouse under a divorce or separation instrument described in clause (i) of section 121(d)(3)(C) shall not be considered a taxable transfer made by such individual notwithstanding any other provision of this subtitle, and such interest shall, after such transfer, be treated as a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account with respect to which such spouse is the account beneficiary. (7) Treatment after death of account beneficiary (A) Treatment if designated beneficiary is spouse If the account beneficiary's surviving spouse acquires such beneficiary's interest in a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account by reason of being the designated beneficiary of such account at the death of the account beneficiary, such Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account shall be treated as if the spouse were the account beneficiary. (B) Other cases If, by reason of the death of the account beneficiary, any person acquires the account beneficiary's interest in a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account in a case to which subparagraph (A) does not apply\u2014 (i) such account shall cease to be a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account as of the date of death, and (ii) an amount equal to the fair market value of the assets in such account on such date shall be includible if such person is not the estate of such beneficiary, in such person's gross income for the taxable year which includes such date, or if such person is the estate of such beneficiary, in such beneficiary's gross income for the last taxable year of such beneficiary. (f) Reports (1) In general The Secretary may require the trustee of a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account to make such reports regarding such account to the Secretary and to the account beneficiary with respect to contributions, distributions, the return of excess contributions, and such other matters as the Secretary determines appropriate. (2) Time and manner of reports The reports required by this subsection shall be filed at such time and in such manner and furnished to such individuals at such time and in such manner as may be required by the Secretary. (g) Regulations The Secretary shall prescribe such regulations as may be necessary or appropriate to carry out the purposes of this section and to prevent the abuse of such purposes. .\n##### (b) Excess contributions\n**(1) In general**\nSection 4973(a) of the Internal Revenue Code of 1986 is amended by striking or at the end of paragraph (5), by inserting or at the end of paragraph (6), and by inserting after paragraph (6) the following new paragraph:\n(7) a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account (within the meaning of section 224), .\n**(2) Excess contributions**\nSection 4973 of such Code is amended by adding at the end the following new subsection:\n(i) Excess contributions to READY accounts (1) In general For purposes of this section, in the case of a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account (within the meaning of section 224), the term excess contributions means the sum of\u2014 (A) the aggregate amount contributed for the taxable year to such accounts (other than rollover contributions described in section 224(e)(5)) which is not allowed as a deduction under section 224 fo such year, and, and (B) the amount determined under this subsection for the preceding taxable year, reduced by the sum of\u2014 (i) the distributions out of the accounts which were included in gross income under section 224(e)(2), and (ii) the excess (if any) of the maximum amount allowed as a deduction under section 224(b) for the taxable year over the amount contributed to the accounts for the taxable year. (2) Special rules For purposes of this subsection, any contribution which is distributed out of the Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account in a distribution to which section 223(e)(3) applies shall be treated as an amount not contributed. .\n##### (c) Application of prohibited transaction rules\n**(1) In general**\nSection 4975(e)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (F), by redesignating subparagraph (G) as subparagraph (H), and by inserting after subparagraph (F) the following new subparagraph:\n(G) a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account described in section 224, or .\n**(2) Special rule**\nSection 4975(c) of such Code is amended by adding at the end the following new paragraph:\n(8) Special rule for Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) accounts An individual for whose benefit a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account (within the meaning of section 224) is established shall be exempt from the tax imposed by this section with respect to any transaction concerning such account (which would otherwise be taxable under this section) if, with respect to such transaction, the account ceases to be a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account by reason of the application of section 224(d)(2) to such account. .\n##### (d) Conforming amendments\n**(1)**\nSection 26(b)(2) of the Internal Revenue Code of 1986 is amended by striking and at the end of subparagraph (Y), by striking the period at the end of subparagraph (Z) and inserting , and , and by inserting after subparagraph (Y) the following:\n(AA) section 224(e)(4). .\n**(2)**\nSection 62(a) of such Code is amended by inserting after paragraph (21) the following new paragraph:\n(22) Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account The deduction allowed by section 224. .\n**(3)**\nSection 165(h) of such Code is amended by adding at the end the following new paragraph:\n(6) Coordination with expenditures from READY accounts No deduction shall be allowed with respect to any loss described in subsection (a)(3) to the extent the taxpayer has made an expenditure from a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account (as defined in section 224) which is taken into account under section 224(c)(2)(C) as a cost with respect to such loss. .\n**(4)**\nSection 877A of such Code is amended\u2014\n**(A)**\nin subsection (e)(2) by inserting a Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account (as defined in section 224), after a health savings account (as defined in section 223), , and\n**(B)**\nin subsection (g)(6) by inserting 224(e)(4), after 223(f)(4), .\n**(5)**\nSection 6693(a)(2) of such Code is amended by striking and at the end of subparagraph (E), by striking the period at the end of subparagraph (F) and inserting , and , and by inserting after subparagraph (F) the following new subparagraph:\n(G) section 224(f) (relating to Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) accounts). .\n**(6)**\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended redesignating the item relating to section 224 as relating to section 225 and by inserting after the item relating to section 223 the following new item:\nSec. 224. Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) accounts. .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-06-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1940",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "READY Accounts Act",
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
        "name": "Taxation",
        "updateDate": "2025-02-15T14:42:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr440",
          "measure-number": "440",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr440v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>READY Accounts Act</strong></p><p>This bill establishes a new Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account, allows individuals to make tax-deductible contributions of up to $4,500 per year to such accounts (adjusted annually for inflation), and allows individuals to take tax-free distributions from such accounts to pay for qualified home disaster mitigation and recovery expenses related to a principal residence owned by the taxpayer.</p><p>Under the bill, qualified home disaster mitigation expenses include expenses certified by a qualified industry professional as meeting criteria to mitigate damage from a natural or other disaster, including</p><ul><li>installing a roofing underlayment to sheathing, impact-resistant windows, impact-resistant entry doors, or ground anchors;</li><li>replacing a roof covering;</li><li>applying a foam adhesive to reinforce the roof structure;</li><li>strengthening the connection of the\u00a0roof deck to roof framing, roof-to-wall connections, soffits, or attic ventilation openings;</li><li>elevating a residence; or</li><li>achieving the current building code standard.</li></ul><p>Qualified home disaster recovery expenses include costs for\u00a0repairing damage to a residence resulting from fire, storm, or other casualty (provided such costs are not reimbursed).</p><p>Distributions from a READY account used for anything other than qualified home disaster mitigation and recovery expenses must be included in gross income and are subject to a 20% penalty. (Some exceptions apply.)</p><p>Finally, the bill imposes a 6% tax on contributions in excess of the annual limit. (Some exceptions apply.)\u00a0</p>"
        },
        "title": "READY Accounts Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr440.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>READY Accounts Act</strong></p><p>This bill establishes a new Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account, allows individuals to make tax-deductible contributions of up to $4,500 per year to such accounts (adjusted annually for inflation), and allows individuals to take tax-free distributions from such accounts to pay for qualified home disaster mitigation and recovery expenses related to a principal residence owned by the taxpayer.</p><p>Under the bill, qualified home disaster mitigation expenses include expenses certified by a qualified industry professional as meeting criteria to mitigate damage from a natural or other disaster, including</p><ul><li>installing a roofing underlayment to sheathing, impact-resistant windows, impact-resistant entry doors, or ground anchors;</li><li>replacing a roof covering;</li><li>applying a foam adhesive to reinforce the roof structure;</li><li>strengthening the connection of the\u00a0roof deck to roof framing, roof-to-wall connections, soffits, or attic ventilation openings;</li><li>elevating a residence; or</li><li>achieving the current building code standard.</li></ul><p>Qualified home disaster recovery expenses include costs for\u00a0repairing damage to a residence resulting from fire, storm, or other casualty (provided such costs are not reimbursed).</p><p>Distributions from a READY account used for anything other than qualified home disaster mitigation and recovery expenses must be included in gross income and are subject to a 20% penalty. (Some exceptions apply.)</p><p>Finally, the bill imposes a 6% tax on contributions in excess of the annual limit. (Some exceptions apply.)\u00a0</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr440"
    },
    "title": "READY Accounts Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>READY Accounts Act</strong></p><p>This bill establishes a new Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) account, allows individuals to make tax-deductible contributions of up to $4,500 per year to such accounts (adjusted annually for inflation), and allows individuals to take tax-free distributions from such accounts to pay for qualified home disaster mitigation and recovery expenses related to a principal residence owned by the taxpayer.</p><p>Under the bill, qualified home disaster mitigation expenses include expenses certified by a qualified industry professional as meeting criteria to mitigate damage from a natural or other disaster, including</p><ul><li>installing a roofing underlayment to sheathing, impact-resistant windows, impact-resistant entry doors, or ground anchors;</li><li>replacing a roof covering;</li><li>applying a foam adhesive to reinforce the roof structure;</li><li>strengthening the connection of the\u00a0roof deck to roof framing, roof-to-wall connections, soffits, or attic ventilation openings;</li><li>elevating a residence; or</li><li>achieving the current building code standard.</li></ul><p>Qualified home disaster recovery expenses include costs for\u00a0repairing damage to a residence resulting from fire, storm, or other casualty (provided such costs are not reimbursed).</p><p>Distributions from a READY account used for anything other than qualified home disaster mitigation and recovery expenses must be included in gross income and are subject to a 20% penalty. (Some exceptions apply.)</p><p>Finally, the bill imposes a 6% tax on contributions in excess of the annual limit. (Some exceptions apply.)\u00a0</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr440"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr440ih.xml"
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
      "title": "READY Accounts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "READY Accounts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for Residential Emergency Asset-accumulation Deferred Taxation Yield (READY) accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T02:48:21Z"
    }
  ]
}
```
