# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8714?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8714
- Title: Skill Savings Account Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8714
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-15T18:25:51Z
- Update date including text: 2026-05-15T18:25:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8714",
    "number": "8714",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Skill Savings Account Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-15T18:25:51Z",
    "updateDateIncludingText": "2026-05-15T18:25:51Z"
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
          "date": "2026-05-07T13:05:50Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8714ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8714\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Thompson of Pennsylvania (for himself and Ms. Bonamici ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish skill savings accounts.\n#### 1. Short title\nThis Act may be cited as the Skill Savings Account Act of 2026 .\n#### 2. Skill savings account\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139L the following new section:\n139M. Skill savings account (a) Exclusion from gross income Gross income of an eligible employee does not include\u2014 (1) amounts contributed to a skill savings account of such employee by such employee or the employer of such employee, or (2) any amount paid or distributed out of a skill savings account which is used exclusively to pay the qualified education expenses of the account beneficiary. (b) Eligible employee For purposes of this section, the term eligible employee means an individual, with respect to any taxable year\u2014 (1) employed in the United States during such taxable year, and (2) who is not a dependent (as defined in section 152) of any other taxpayer for such taxable year. (c) Limitation on exclusion Subsection (a) shall not apply to so much of any contribution to a skill savings account of an employee for a taxable year as exceeds\u2014 (1) in the case of a contribution by an employer, the excess of\u2014 (A) $5,250, over (B) the amount (if any) excluded from the gross income of such employee under section 127(a)(1) for such taxable year, and (2) in the case of a contribution by the employee, any amount which taken in aggregate with all contributions made by such employee during the taxable year exceeds $10,000. (d) Skill savings account For purposes of this section, the term skill savings account means a trust created or organized in the United States as a skill savings account exclusively for the purpose of paying the qualified education expenses of the account beneficiary, but only if the written governing instrument creating the trust meets the following requirements: (1) No contribution will be accepted unless it is in cash. (2) The trustee is a bank (as defined in section 408(n)), an insurance company (as defined in section 816), or another person who demonstrates to the satisfaction of the Secretary that the manner in which such person will administer the trust will be consistent with the requirements of this section. (3) The assets of the trust will not be commingled with other property except in a common trust fund or common investment fund. (4) No part of the trust assets will be invested in life insurance contracts. (5) The interest of an individual in the balance in his account is nonforfeitable. (e) Qualified education expenses For purposes of this section, the term qualified education expenses means amounts paid or incurred by the employee if such amount would be educational assistance (as defined in section 127(c)(1)) if such amount were paid by the employer of such employee. (f) Amounts not used for qualified education expenses (1) In general Any amount paid or distributed from a skill savings account which is not used exclusively to pay the qualified education expenses of the account beneficiary shall be included in the gross income of such account beneficiary. (2) Additional tax on distributions not used for qualified educational expenses The tax imposed by this chapter on the account beneficiary who has not attained age 65 for any taxable year in which there is a payment or distribution from a skill savings account of such beneficiary which is includible in gross income under paragraph (1) shall be increased by 20 percent of the amount which is so includible. (3) Excess contribution returned before due date of return If any excess contribution is contributed for a taxable year to any skill savings account of an individual, paragraph (1) shall not apply to distributions from the skill savings accounts of such individual (to the extent such distributions do not exceed the aggregate excess contributions to all such accounts of such individual for such year) if\u2014 (A) such distribution is received by the individual on or before the last day prescribed by law (including extensions of time) for filing such individual's return for such taxable year, and (B) such distribution is accompanied by the amount of net income attributable to such excess contribution. Any net income described in subparagraph (B) shall be included in the gross income of the individual for the taxable year in which it is received. (4) Excess contribution For purposes of paragraph (3), the term excess contribution means any contribution which is not excludable from gross income under subsection (a). (g) Tax treatment of account A skill savings account is exempt from taxation under this subtitle unless such account has ceased to be a skill savings account. Notwithstanding the preceding sentence, any such account is subject to the taxes imposed by section 511. (h) Employee; employer For purposes of this section, the terms employee and employer shall be applied as such terms are applied in section 127. (i) Reporting The Secretary may require the trustee of a skill savings account to make such reports (at such time and in such manner as the Secretary determines appropriate) regarding such account to the Secretary and to the account beneficiary with respect to contributions, distributions, the return of excess contributions, and such other matters as the Secretary determines appropriate. .\n##### (b) Implementing regulations\nNot later than 1 year after the date of the enactment of this Act, the Secretary of the Treasury shall issue such implementing regulations as the Secretary determines appropriate to implement the amendments made by this section.\n##### (c) Excess contributions\nSection 4973 of such Code is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (5), by striking or ,\n**(B)**\nin paragraph (6), by inserting or after the comma, and\n**(C)**\nby inserting after paragraph (6) the following new paragraph:\n(7) a skill savings account (within the meaning of section 127A(d)). , and\n**(2)**\nby adding at the end the following new subsection:\n(i) Skill savings account For purposes of this section, in the case of skill savings accounts (within the meaning of section 127A(d)), the term excess contribution means the sum of\u2014 (1) the aggregate amount contributed for the taxable year to the accounts which is not excludable from gross income under section 139M(a), and (2) the amount determined under this subsection for the preceding taxable year, reduced by the sum of\u2014 (A) the distributions out of the accounts which were included in gross income under section 139M(f)(1), and (B) the excess (if any) of\u2014 (i) the maximum amount excludable from gross income under section 139 (a)(1) for the taxable year, over (ii) the amount contributed to the accounts for the taxable year. For purposes of this subsection, any contribution which is distributed out of the skill savings account in a distribution to which section 139M(f)(1) applies shall be treated as an amount not contributed. .\n##### (d) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139L the following new item:\nSec. 139M. Skill savings account. .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
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
        "updateDate": "2026-05-15T18:25:51Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8714ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Skill Savings Account Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T05:23:27Z"
    },
    {
      "title": "Skill Savings Account Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish skill savings accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T05:18:28Z"
    }
  ]
}
```
