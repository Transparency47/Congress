# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2217?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2217
- Title: Independent Retirement Fairness Act
- Congress: 119
- Bill type: S
- Bill number: 2217
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2025-09-04T15:26:27Z
- Update date including text: 2025-09-04T15:26:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2217",
    "number": "2217",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Independent Retirement Fairness Act",
    "type": "S",
    "updateDate": "2025-09-04T15:26:27Z",
    "updateDateIncludingText": "2025-09-04T15:26:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-09",
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
      "actionDate": "2025-07-09",
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
          "date": "2025-07-09T15:01:02Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2217is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2217\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Cassidy introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 and the Internal Revenue Code of 1986 regarding pension plans for independent workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Independent Retirement Fairness Act .\n#### 2. Pooled employer plans for independent workers\nSection 3(43) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(43) ) is amended by adding at the end the following:\n(E) Treatment of independent workers as employees (i) In general (I) Independent workers For purposes of a pooled employer plan, an independent worker may be enrolled in the pooled employer plan as if the independent worker were an employee of an employer in the plan and shall be considered a participant for purposes of the plan. (II) Trade associations For purposes of a pooled employer plan, a trade association may be in a pooled employer plan as if the trade organization were an employer and may enroll an independent worker in the plan in accordance with subclause (I). (ii) Data harmonization For purposes of an independent worker who is a participant in a pooled employer plan, an employer of an independent worker or a trade organization that enrolls an independent worker may share data regarding the independent worker with any person as necessary to facilitate the establishment and maintenance of the pooled employer plan. (iii) Rule of construction regarding employment status The status of an independent worker as a participant in a pooled employer plan of an employer or a trade association and any contributions made to such a pooled employer plan by the employer on behalf of an independent worker shall not be construed to mean that the independent worker is an employee of the employer or trade association in the plan for purposes of any Federal, State, or local law. (iv) Definitions For purposes of this subparagraph: (I) Independent worker The term independent worker means an individual who, with respect to an employer, performs work for remuneration for the employer and is not an employee of the employer. (II) Trade association The term trade association includes any labor organization, worker cooperative, employee organization, association of workers in related or unrelated industries, or association of related companies or contractors. .\n#### 3. Simplified employee pensions for independent workers\n##### (a) In general\nSubsection (k) of section 408 of the Internal Revenue Code of 1986 is amended by redesignating paragraph (10) as paragraph (11) and by inserting after paragraph (9) the following new paragraph:\n(10) Independent workers (A) In general At the election of the employer, an independent worker may be treated for purposes of this subsection in the same manner as an employee, as provided in this paragraph. (B) Participation In the case of independent workers\u2014 (i) Participation An employer may elect to exclude such workers in applying paragraph (2). (ii) Employees electing Paragraph (6)(A)(ii) shall not apply. (C) Independent workers treated separately For purposes of applying paragraphs (3)(C), (5), and (6)(A)(iii), the employer may elect to treat independent workers separately from employees. (D) Not counted in employer size Independent workers shall not be taken into account as employees in applying paragraph (6)(B). (E) Contribution of bonuses Notwithstanding paragraphs (3)(C) and (5), in the case of any independent worker who is entitled to receive a cash bonus from the employer, at the election of the independent worker such bonus may be contributed to the account or annuity of the worker pursuant to the simplified employee pension and not paid to the worker in cash. Any bonus so contributed shall not be taken into account in determining the percentage of compensation contributed with respect to the worker. (F) Deposits into suspension account An account or annuity shall not fail to be treated as a simplified employee pension solely because the terms of the pension allow the employer, at the election of the independent worker, to deposit contributions into a suspension account instead of into the account or annuity, if such contributions are either\u2014 (i) returned to the independent worker in cash, or (ii) contributed into the account or annuity pursuant to the terms of the pension, within the same taxable year or not later than the last date on which contributions may be made for such taxable year. Amounts contributed to the account or annuity pursuant to the preceding sentence shall be treated for purposes of this subsection as if contributed directly to such account or annuity, and amounts returned to the independent worker in cash shall be treated as never contributed under the simplified employee pension. (G) Definitions For purposes of this paragraph\u2014 (i) Independent worker The term independent worker has the meaning given the term in section 3(43)(E) of the Employee Retirement Income Security Act of 1974. (ii) Suspension account The term suspension account has the meaning given the term in section 5 of the Independent Retirement Fairness Act . .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 4. Simplification of auditing requirements for groups of plans\nSection 202 of the Setting Every Community Up for Retirement Enhancement Act of 2019 ( 29 U.S.C. 6058 et seq. ) is amended by\u2014\n**(1)**\nby striking relate only and inserting the following:\n(A) relate only ; and\n**(2)**\nby striking the period and inserting the following:\n; and (B) be based on the same accounting principles applicable to opinions with respect to pooled employer plans (as defined in section 3(43) of such Act ( 29 U.S.C. 1002(43) )), except that such an opinion shall take into account the limitations on the use of the assets of a plan to pay benefits and expenses only with respect to such plan and shall take into account that plans in a group of plans described in subsection (c) may have separate trusts. .\n#### 5. Simplification of auditing for pooled employer plans\n##### (a) In general\nSection 3(43) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(43) ), as amended by section 2 of this Act, is further amended by adding at the end the following:\n(F) Audit requirement Any opinion required by section 103(a)(3) with respect to a pooled employer plan shall relate only to the portions of such a plan attributable to a participating employer for which such an opinion would be required if the participating employer maintained such portion as a single-employer plan separate from the pooled employer plan. .\n##### (b) Effective date\nThe amendment made by this section shall apply to plan years beginning after the date of enactment of this Act.\n#### 6. Pilot programs for the gig economy\n##### (a) In general\nThe Secretary of the Treasury and the Secretary of Labor shall, in cooperation and after reviewing a survey of relevant academic literature and consulting with relevant companies, establish pilot programs to encourage independent workers to save for retirement, including\u2014\n**(1)**\na program that allows an independent worker to round down any compensation paid to the independent worker to the nearest whole dollar amount and automatically contribute the amount of compensation in excess of such whole dollar amount as an elective employee contribution to a pooled employer plan in which the independent worker is enrolled, a solo 401(k) of the independent worker, or a suspension account; and\n**(2)**\na program that allows an independent worker to designate an amount that will be automatically deducted from the compensation paid to the independent worker for, as selected by the independent worker, each pay period or monthly, quarterly, semi-annually, or annually and automatically contributed as an elective employee contribution to a pooled employer plan in which the independent worker is enrolled, a solo 401(k) of the independent worker, or a suspension account.\n##### (b) Coordination with safe harbor plan rules\nAs provided by the Secretary of the Treasury (or such Secretary's delegate), the pilot programs under subsection (a) may be conducted in or through the use of safe harbor plans, and any such plan participating in such a pilot program shall not be treated as failing to meet any requirement applicable to such plan by reason of such participation. For purposes of the preceding sentence, the term safe harbor plan means any qualified cash or deferred arrangement which meets the requirements of paragraph (11), (12), (13), or (16) of section 401(k) of the Internal Revenue Code of 1986.\n##### (c) Definitions\nFor purposes of this section:\n**(1) Independent worker**\nThe term independent worker has the meaning given the term in section 3(43)(E) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(43)(E) ).\n**(2) Pooled employer plan**\nThe term pooled employer plan has the meaning given the term in section 3(43) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(43) ).\n**(3) Solo 401(k)**\nThe term solo 401(k) means a qualified cash or deferred arrangement (as defined in section 401(k)(2) of the Internal Revenue Code of 1986) covering a single participant (or a single participant and such individual's spouse).\n**(4) Suspension account**\nThe term suspension account means an account that is established and maintained on behalf of an independent worker that\u2014\n**(A)**\nallows for the deposit of amounts by the independent worker, including the amounts described in paragraphs (1) and (2) of subsection (a);\n**(B)**\nallows for the independent worker to withdraw amounts deposited in the account and\u2014\n**(i)**\ncontribute such withdrawn amounts to a pooled employer plan in which the independent worker is enrolled; or\n**(ii)**\ncontribute such withdrawn amounts into a simplified employee pension as provided under section 408(k)(10) of the Internal Revenue Code of 1986; and\n**(C)**\nprovides that any amount remaining in the account at the end of each year, after any withdrawals under subparagraph (B), shall be returned to the independent worker in a lump sum.",
      "versionDate": "2025-07-09",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-04T15:26:27Z"
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
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2217is.xml"
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
      "title": "Independent Retirement Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Independent Retirement Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 and the Internal Revenue Code of 1986 regarding pension plans for independent workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:31Z"
    }
  ]
}
```
