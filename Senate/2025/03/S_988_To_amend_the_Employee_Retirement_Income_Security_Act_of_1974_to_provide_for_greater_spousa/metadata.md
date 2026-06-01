# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/988?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/988
- Title: Women's Retirement Protection Act
- Congress: 119
- Bill type: S
- Bill number: 988
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-12-05T21:36:07Z
- Update date including text: 2025-12-05T21:36:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/988",
    "number": "988",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Women's Retirement Protection Act",
    "type": "S",
    "updateDate": "2025-12-05T21:36:07Z",
    "updateDateIncludingText": "2025-12-05T21:36:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
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
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T17:59:08Z",
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
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "WA"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "WA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "HI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "VA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s988is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 988\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Ms. Baldwin (for herself, Mrs. Murray , Ms. Cantwell , Mr. Blumenthal , Ms. Hirono , Ms. Klobuchar , Mr. Sanders , Mr. Wyden , Mr. Van Hollen , Mr. Kaine , Ms. Warren , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to provide for greater spousal protection under defined contribution plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Women's Retirement Protection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nApproximately 28 percent of non-retired adults have no defined benefit plan or retirement savings, according to 2023 data from the Board of Governors of the Federal Reserve System.\n**(2)**\nIn 2023, approximately 1/3 of the private sector workforce did not have access to a retirement plan at the workplace, and only half of the workforce actually participated in a retirement plan.\n**(3)**\nWomen\u2019s retirement preparedness often lags significantly behind their male counterparts', resulting in the median income for women aged 65 and older in 2022 being just 83 percent of the median income of men aged 65 and older, including income from social security, pension plans, investments, and earnings.\n**(4)**\nWomen aged 80 and older had the highest poverty rate among older persons in all age groups, with 14.7 percent of women aged 80 and older living in poverty while 10.3 percent of men in the same age group live in poverty.\n**(5)**\nWomen make up two-thirds of low-wage workers, even though they comprise less than half of all workers, and low-wage workers are less likely than other workers to participate in a retirement plan at work.\n**(6)**\nBecause of the pay gap, women working full-time, year-round typically lose $398,160 over a 40-year career thereby requiring the average woman to work almost a decade longer than her male counterpart to make up that career wage gap.\n**(7)**\nDue to the lower lifetime wages stemming from unequal pay and caregiving duties, the average Social Security benefit in 2023 for a woman was $1,638 a month, while for men such average monthly benefit was $2,020.\n**(8)**\nWhile the SECURE 2.0 Act of 2022 ( Public Law 117\u2013328 ) goes a long way to address this coverage gap, just 1 in 5 part-time workers who work a full year are eligible for a retirement plan, and women are almost twice as likely to work part-time as men.\n**(9)**\nWhile traditional defined benefit retirement plans have spousal protections, defined contribution retirement plans, which have become increasingly common, currently provide no similar spousal protections.\n**(10)**\nThe Thrift Savings Plan of the Federal Government, the largest defined contribution plan in the world with approximately 6,500,000 participants, requires its married participants to have their spouses' consent for withdrawals and loans.\n**(11)**\nThere were almost 990,000 divorces in the United States between 2020 and 2021. After the family home, retirement savings tends to be the largest asset to be divided in a divorce.\n**(12)**\nWhile fees and expenses associated with retirement plans have been in decline, participants have seen direct charges for processing qualified domestic relations orders increase significantly.\n#### 3. Increasing spousal protection under defined contribution plans\n##### (a) Amendment of Employee Retirement Income Security Act of 1974\n**(1) In general**\nPart 2 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1051 et seq. ) is amended by inserting after section 205 the following new section:\n205A. Additional spousal consent requirements (a) In general Each individual account plan to which section 205 does not apply shall provide that, except as provided in subsections (c) and (d), no distribution may be made under the plan unless the spousal consent requirements of subsection (e) are met. (b) Coordination with section 205 Nothing in this section shall be construed to exempt an individual account plan from the requirements of section 205 with respect to any participant. (c) Exceptions for certain distributions Subsection (a) shall not apply to\u2014 (1) any distribution that is\u2014 (A) a minimum required distribution described in section 4974(b) of the Internal Revenue Code of 1986; (B) permitted under section 203(e)(1) to be made without the consent of the participant; or (C) in an amount that is less than 25 percent of the account balance, but not more than once per account; (2) any distribution in the form of a qualified joint and survivor annuity (as defined in section 205(d)(1)), a qualified optional survivor annuity (as defined in section 205(d)(2)), a qualified preretirement survivor annuity (as defined in section 205(e)), or a series of substantially equal periodic payments (not less frequently than annually) made for the joint lives (or life expectancies) of the participant and the participant's spouse; or (3) in the case of a participant who does not elect a form of benefit described in paragraph (2) under the plan or who is participating in a plan that does not provide such a form of benefit, any distribution of the participant's entire nonforfeitable accrued benefit if 50 percent of such accrued benefit is transferred to an individual retirement plan (as defined in section 7701(a)(37) of the Internal Revenue Code of 1986) of the spouse of the participant. A transfer described in paragraph (3) to an individual retirement plan shall be treated in the same manner as a transfer under section 408(d)(6) of the Internal Revenue Code of 1986. (d) Exceptions for certain rollover contributions Subsection (a) shall not apply to any distribution, involving a participant who has a spouse, that is an eligible rollover distribution (as defined in section 402(f)(2)(A) of the Internal Revenue Code of 1986) made in the form of a direct trustee-to-trustee transfer within the meaning of section 401(a)(31) of the Internal Revenue Code of 1986\u2014 (1) to a plan to which this section or section 205 applies; or (2) to an individual retirement plan (as defined in section 7701(a)(37) of the Internal Revenue Code of 1986) if\u2014 (A) the beneficiary of such plan is the spouse of the participant, or the spousal consent requirements of subsection (e) are met with respect to any designation of 1 or more other beneficiaries; and (B) under the terms of the individual retirement plan, the beneficiary of such plan (whether the spouse or other beneficiary designated under paragraph (1)) may not be changed unless\u2014 (i) the spousal consent requirements of subsection (e) are met with respect to any such change, or (ii) the spousal consent under subparagraph (A) to the designation of a beneficiary other than the spouse expressly permits such designation to be changed without the further consent of the spouse. (e) Spousal consent requirements (1) In general For purposes of this section, except as provided in paragraph (2), the spousal consent requirements of this subsection are met with respect to any distribution or any designation or change of beneficiary if\u2014 (A) the plan provides to each participant, within a reasonable period of time before such distribution or designation or change of beneficiary is made and consistent with such regulations as the Secretary of the Treasury may prescribe, a written explanation of the rights of the participant and the participant's spouse under this section; (B) the spouse of the participant consents in writing to the distribution or designation or change of beneficiary; (C) in the case of a distribution, the written consent under subparagraph (B) is made during the consent period; and (D) the written consent under subparagraph (B)\u2014 (i) acknowledges the effect of such distribution or designation or change of beneficiary; and (ii) is witnessed by a plan representative or a notary public. (2) Exceptions under section 205 to apply The requirements of paragraph (1) (other than subparagraph (A) thereof) shall not apply with respect to any distribution or designation or change of beneficiary if a participant establishes to the satisfaction of the plan administrator that\u2014 (A) there is no spouse; (B) the participant and the participant's spouse have not been married for at least 1 year as of the date of the distribution or designation or change of beneficiary; or (C) such consent cannot be obtained because\u2014 (i) the spouse cannot be located; or (ii) of such other circumstances as the Secretary of the Treasury, in consultation with the Secretary of Labor, may by regulations prescribe. (3) Consent limited to spouse and event Any written consent by a spouse under paragraph (1), or the establishment by a participant that an exception under paragraph (2) (other than subparagraph (A) thereof) applies with respect to a spouse, shall be effective only with respect to that spouse and to the distribution or designation or change of beneficiary to which it relates. (4) Consent period For purposes of this subsection, the term consent period means, with respect to any distribution\u2014 (A) the 90-day period immediately preceding the date of such distribution; or (B) such other period as the Secretary of the Treasury may provide. (f) Discharge of plan from liability Rules similar to the rules of section 205(c)(6) shall apply for purposes of this section. .\n**(2) Clerical amendment**\nThe table of sections of part 2 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 is amended by inserting after the item relating to section 205 the following new item:\nSec. 205A. Additional spousal consent requirements. .\n**(3) Right of action**\nSection 502(a) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1132 ) is amended\u2014\n**(A)**\nby striking or at the end of paragraph (10);\n**(B)**\nby striking the period at the end of paragraph (11) and inserting ; or ; and\n**(C)**\nby adding at the end the following new paragraph:\n(12) by an individual for appropriate relief in the case of a violation of the individual's rights under section 205A. .\n##### (b) Conforming amendment to Internal Revenue Code of 1986\nSection 401(a) of the Internal Revenue Code of 1986 is amended by inserting after paragraph (17) the following new paragraph:\n(18) Additional spousal consent requirements (A) In general In the case of a defined contribution plan to which paragraph (11) does not apply, except as provided in subsections (c) and (d), a trust forming part of such plan shall not constitute a qualified trust under this section unless no distribution may be made under the plan unless the spousal consent requirements of subparagraph (E) are met. (B) Coordination with paragraph (11) Nothing in this paragraph shall be construed to exempt a defined contribution plan from the requirements of paragraph (11) with respect to any participant. (C) Exceptions for certain distributions Subparagraph (A) shall not apply to\u2014 (i) any distribution that is\u2014 (I) a minimum required distribution described in section 4974(b), (II) permitted under section 411(a)(11) to be made without the consent of the participant, or (III) in an amount that is less than 25 percent of the account balance, (ii) any distribution in the form of a qualified joint and survivor annuity (as defined in section 417(b)), a qualified optional survivor annuity (as defined in section 417(g)), a qualified preretirement survivor annuity (as defined in section 417(c)), or a series of substantially equal periodic payments (not less frequently than annually) made for the joint lives (or life expectancies) of the participant and the participant's spouse, or (iii) in the case of a participant who does not elect a form of benefit described in clause (ii) under the plan or who is participating in a plan that does not provide such a form of benefit, any distribution of the participant's entire nonforfeitable accrued benefit if 50 percent of such accrued benefit is transferred to an individual retirement plan of the spouse of the participant. A transfer described in clause (iii) to an individual retirement plan shall be treated in the same manner as a transfer under section 408(d)(6). (D) Exceptions for certain rollover contributions Subparagraph (A) shall not apply to any distribution, involving a participant who has a spouse, that is an eligible rollover distribution (as defined in section 402(f)(2)(A)) made in the form of a direct trustee-to-trustee transfer within the meaning of paragraph (31)\u2014 (i) to a plan to which this paragraph or paragraph (11) applies, or (ii) to an individual retirement plan if\u2014 (I) the beneficiary of such plan is the spouse of the participant, or the spousal consent requirements of subparagraph (E) are met with respect to any designation of 1 or more other beneficiaries, and (II) under the terms of the individual retirement plan, the beneficiary of such plan (whether the spouse or other beneficiary designated under subclause (I)) may not be changed unless\u2014 (aa) the spousal consent requirements of subparagraph (E) are met with respect to any such change, or (bb) the spousal consent under subclause (I) to the designation of a beneficiary other than the spouse expressly permits such designation to be changed without the further consent of the spouse. (E) Spousal consent requirements (i) In general For purposes of this paragraph, except as provided in clause (ii), the spousal consent requirements of this subparagraph are met with respect to any distribution or any designation or change of beneficiary if\u2014 (I) the plan provides to each participant, within a reasonable period of time before such distribution or designation or change of beneficiary is made and consistent with such regulations as the Secretary may prescribe, a written explanation of the rights of the participant and the participant's spouse under this paragraph, (II) the spouse of the participant consents in writing to the distribution or designation or change of beneficiary, (III) in the case of a distribution, the written consent under subclause (II) is made during the consent period, and (IV) the written consent under subclause (II)\u2014 (aa) acknowledges the effect of such distribution or designation or change of beneficiary, and (bb) is witnessed by a plan representative or a notary public. (ii) Exceptions under section 417 to apply The requirements of clause (i) (other than subclause (I) thereof) shall not apply with respect to any distribution or designation or change of beneficiary if a participant establishes to the satisfaction of the plan administrator that\u2014 (I) there is no spouse, (II) the participant and the participant's spouse have not been married for at least 1 year as of the date of the distribution or designation or change of beneficiary, or (III) such consent cannot be obtained because\u2014 (aa) the spouse cannot be located, or (bb) of such other circumstances as the Secretary, in consultation with the Secretary of Labor, may by regulations prescribe. (iii) Consent limited to spouse and event Any written consent by a spouse under clause (i), or the establishment by a participant that an exception under clause (ii) (other than subclause (I) thereof) applies with respect to a spouse, shall be effective only with respect to that spouse and to the distribution or designation or change of beneficiary to which it relates. (iv) Consent period For purposes of this subparagraph, the term consent period means, with respect to any distribution\u2014 (I) the 90-day period immediately preceding the date of such distribution, or (II) such other period as the Secretary may provide. .\n#### 4. Effective dates\n##### (a) Increasing spousal protection under defined contribution plans\nExcept as provided in subsection (b), the amendments made by section 3 shall apply to distributions and rollover contributions made in plan years beginning after the date that is 1 year after the date of the enactment of this Act.\n##### (b) Provisions relating to plan amendments\n**(1) In general**\nIf this paragraph applies to any plan or contract amendment, such plan or contract shall be treated as being operated in accordance with the terms of the plan during the period described in paragraph (2)(C).\n**(2) Amendments to which paragraph (1) applies**\n**(A) In general**\nParagraph (1) shall apply to any amendment to any plan or annuity contract which is made\u2014\n**(i)**\npursuant to the amendments made by section 3 or pursuant to any regulation issued under section 205A of the Employee Retirement Income Security Act of 1974 or section 401(a)(18) of the Internal Revenue Code of 1986, as added by section 3; and\n**(ii)**\non or before the last day of the first plan year beginning on or after the date that is 3 years after the date described in subsection (a).\nsection 414(d)\n5 years\n3 years\n**(B) Conditions**\nSubparagraph (A) shall not apply to any amendment unless\u2014\n**(i)**\nthe plan or contract is operated as if such plan or contract amendment were in effect for the period described in subparagraph (C); and\n**(ii)**\nsuch plan or contract amendment applies retroactively for such period.\n**(C) Period described**\nThe period described in this subparagraph is the period\u2014\n**(i)**\nbeginning on the effective date specified by the plan; and\n**(ii)**\nending on the date described in subparagraph (A)(ii) (or, if earlier, the date the plan or contract amendment is adopted).\n#### 5. Access to independent consumer information and understanding\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term consumer means any person who purchases or acquires any goods, products, services, or credit related to the retirement or later life economic security of the consumer; and\n**(2)**\nthe term financial product or service provider means any person who engages in the business of providing any retirement financial product or service to any consumer.\n##### (b) Required link to consumer awareness information\nIn any offer for the sale, exchange, or other transfer of a retirement financial product or service to a consumer carried out by a financial product or service provider, such provider shall provide, in a manner consistent with subsection (c), an easily accessible link to the website of the Bureau of Consumer Financial Protection (referred to in this section as the CFPB ) at which the consumer may access information, literature, guides, programs, tools, strategies, or any other resource produced by the CFPB or other Federal agency relating to retirement planning or later life economic security.\n##### (c) Determination\nIn order to ensure that the requirement under subsection (b) is effectively carried out, the Financial Literacy and Education Commission shall determine and publish on its website the appropriate link to the CFPB\u2019s website for access to the CFPB\u2019s and other Federal agencies\u2019 consumer education materials, the preferred format of such link, and any accompanying description of the CFPB and the consumer education materials associated with such link.\n#### 6. Grants to promote financial literacy for women\n##### (a) Authorization of grant awards\nThe Secretary of Labor, acting through the Director of the Women's Bureau, shall award grants on a competitive basis to eligible entities to enable such entities to improve the financial literacy of women who are working age or in retirement, to increase the likelihood of the women realizing a secure and stable retirement.\n##### (b) Definition of eligible entity\nIn this section, the term eligible entity means a community-based organization with proven experience and expertise in serving working-age or retired women.\n##### (c) Application\nAn eligible entity that desires to receive a grant under this section shall submit an application to the Secretary of Labor at such time, in such manner, and accompanied by such information as such Secretary may require.\n##### (d) Minimum grant amount\nThe Secretary of Labor shall award grants under this section in amounts of not less than $250,000.\n##### (e) Use of funds\nAn eligible entity that receives a grant under this section shall use the grant funds to develop and implement financial literacy education, and related activities including outreach, awareness building, and counseling to increase women's knowledge of retirement planning and consumer, economic, and personal financial concepts.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $100,000,000 for fiscal year 2026 and each succeeding fiscal year.\n#### 7. Grants to assist low-income women and survivors of domestic violence in obtaining qualified domestic relations orders\n##### (a) Authorization of grant awards\nThe Secretary of Labor, acting through the Director of the Women\u2019s Bureau and in conjunction with the Assistant Secretary of the Employee Benefits Security Administration, shall award grants, on a competitive basis, to eligible entities to enable such entities to assist low-income women and survivors of domestic violence in obtaining qualified domestic relations orders and ensuring that those women actually obtain the benefits to which they are entitled through those orders.\n##### (b) Definition of eligible entity\nIn this section, the term eligible entity means a community-based organization with proven experience and expertise in serving women and the financial and retirement needs of women.\n##### (c) Application\nAn eligible entity that desires to receive a grant under this section shall submit an application to the Secretary of Labor at such time, in such manner, and accompanied by such information as the Secretary of Labor may require.\n##### (d) Minimum grant amount\nThe Secretary of Labor shall award grants under this section in amounts of not less than $250,000.\n##### (e) Use of funds\nAn eligible entity that receives a grant under this section shall use the grant funds to develop programs to offer help to low-income women or survivors of domestic violence who need assistance in preparing, obtaining, and effectuating a qualified domestic relations order.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $100,000,000 for fiscal year 2026 and each succeeding fiscal year.",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on Financial Services, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2023",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Women's Retirement Protection Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-04-04T13:54:29Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s988is.xml"
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
      "title": "Women's Retirement Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Women's Retirement Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 to provide for greater spousal protection under defined contribution plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:27Z"
    }
  ]
}
```
