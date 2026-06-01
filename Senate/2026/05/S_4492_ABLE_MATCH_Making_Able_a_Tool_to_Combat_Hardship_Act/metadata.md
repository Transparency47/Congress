# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4492?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4492
- Title: ABLE MATCH (Making Able a Tool to Combat Hardship) Act
- Congress: 119
- Bill type: S
- Bill number: 4492
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-28T20:36:31Z
- Update date including text: 2026-05-28T20:36:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4492",
    "number": "4492",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "ABLE MATCH (Making Able a Tool to Combat Hardship) Act",
    "type": "S",
    "updateDate": "2026-05-28T20:36:31Z",
    "updateDateIncludingText": "2026-05-28T20:36:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T18:47:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4492is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4492\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mr. Van Hollen (for himself, Mr. Moran , Ms. Klobuchar , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide matching payments for ABLE account contributions by certain individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ABLE MATCH (Making Able a Tool to Combat Hardship) Act .\n#### 2. Matching payments for ABLE account contributions by certain individuals\n##### (a) In general\nSubchapter B of chapter 65 of the Internal Revenue Code of 1986 is amended by inserting after section 6433 the following new section:\n6433A. Matching payments for ABLE account contributions by certain individuals (a) In general (1) Allowance of match Any individual who is the designated beneficiary of an ABLE account as of the last day of the taxable year and who makes qualified ABLE account contributions for such taxable year shall be allowed a matching contribution for such taxable year in an amount equal to the applicable percentage of so much of the qualified ABLE account contributions made by such individual for the taxable year as does not exceed $2,000. (2) Payment of match (A) In general Except as provided in subparagraph (B), the matching contribution under this section shall be allowed as a credit which shall be payable by the Secretary as a contribution (as soon as practicable after the individual has filed a tax return making a claim for such matching contribution for the taxable year) to the ABLE account of the individual. (B) Exception In the case of an individual who elects the application of this subparagraph and with respect to whom the matching contribution determined under paragraph (1) is greater than zero but less than $50 for the taxable year, subparagraph (A) shall not apply and such matching contribution shall be treated as a credit allowed by subpart C of part IV of subchapter A of chapter 1. (b) Applicable percentage For purposes of this section\u2014 (1) In general Except as provided in paragraph (2), the applicable percentage is 100 percent. (2) Phaseout The percentage under paragraph (1) shall be reduced (but not below zero) by the number of percentage points which bears the same ratio to 100 percentage points as\u2014 (A) the excess of\u2014 (i) the taxpayer's modified adjusted gross income for such taxable year, over (ii) the applicable dollar amount, bears to (B) $20,000. If any reduction determined under this paragraph is not a whole percentage point, such reduction shall be rounded to the next lowest whole percentage point. (3) Applicable dollar amount The applicable dollar amount is\u2014 (A) in the case of a joint return, $56,000, (B) in the case of a head of household (as defined in section 2(b)), 3/4 of the amount applicable under subparagraph (A), and (C) in any other case, 1/2 of the amount applicable under subparagraph (A). (c) Qualified ABLE account contributions For purposes of this section\u2014 (1) In general The term qualified ABLE account contributions means, with respect to any taxable year, the amount of contributions made by the individual to the ABLE account of which such individual is the designated beneficiary. Such term shall not include any amount attributable to a payment under subsection (a)(2). (2) Reduction for certain distributions (A) In general The qualified ABLE account contributions determined under paragraph (1) for a taxable year shall be reduced (but not below zero) by the aggregate distributions received by the individual during the testing period from the ABLE account. (B) Testing period For purposes of subparagraph (A), the testing period, with respect to a taxable year, is the period which includes\u2014 (i) such taxable year, (ii) the 2 preceding taxable years, and (iii) the period after such taxable year and before the due date (including extensions) for filing the return of tax for such taxable year. (C) Excepted distributions There shall not be taken into account under subparagraph (A) the amount of distributions under a qualified ABLE program (within the meaning of section 529A) that is equal to amounts not included in gross income with respect to such distributions under section 529A(c)(1)(B) (relating to distributions for qualified disability expenses). (D) Treatment of distributions received by spouse of individual For purposes of determining distributions received by an individual under subparagraph (A) for any taxable year, any distribution received by the spouse of such individual shall be treated as received by such individual if such individual and spouse file a joint return for such taxable year and for the taxable year during which the spouse receives the distribution. (d) ABLE account For purposes of this section, the term ABLE account has the meaning given such term under section 529A. (e) Other definitions and special rules (1) Modified adjusted gross income For purposes of this section, the term modified adjusted gross income means adjusted gross income determined without regard to sections 911, 931, and 933. (2) Treatment of contributions In the case of any contribution under subsection (a)(2), such contribution shall not be taken into account with respect to the limitation under section 529A(b)(2)(B). (3) Erroneous credits (A) In general If any contribution is erroneously paid under subsection (a)(2), including a payment that is not made to an ABLE account, the amount of such erroneous payment shall be treated as an underpayment of tax (other than for purposes of part II of subchapter A of chapter 68) for the taxable year in which the Secretary determines the payment is erroneous. (B) Distribution of erroneous credits In the case of a contribution to which subparagraph (A) applies, section 72 shall not apply to the distribution of such contribution (and any income attributable thereto) if such distribution is received not later than the day prescribed by law (including extensions of time) for filing the individual\u2019s return for such taxable year. (4) Exception from reduction or offset Any payment made to any individual under this section shall not be\u2014 (A) subject to reduction or offset pursuant to subsection (c), (d), (e), or (f) of section 6402 or any similar authority permitting offset, or (B) reduced or offset by other assessed Federal taxes that would otherwise be subject to levy or collection. (5) Election not to have section apply A taxpayer may elect not to have this section apply for any taxable year. (f) Inflation adjustments (1) In general In the case of any taxable year beginning in a calendar year after 2027, the $56,000 amount in subsection (b)(3)(A) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2026 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding Any increase determined under paragraph (1) shall be rounded to the nearest multiple of $1,000. .\n##### (b) Treatment of Certain Possessions\n**(1) Payments to possessions with mirror code tax systems**\nThe Secretary of the Treasury shall pay to each possession of the United States which has a mirror code tax system amounts equal to the loss (if any) to that possession by reason of the amendments made by this section. Such amounts shall be determined by the Secretary of the Treasury based on information provided by the government of the respective possession.\n**(2) Payments to other possessions**\nThe Secretary of the Treasury shall pay to each possession of the United States which does not have a mirror code tax system amounts estimated by the Secretary of the Treasury as being equal to the aggregate benefits (if any) that would have been provided to residents of such possession by reason of the amendments made by this section if a mirror code tax system had been in effect in such possession. The preceding sentence shall not apply unless the respective possession has a plan, which has been approved by the Secretary of the Treasury, under which such possession will promptly distribute such payments to its residents.\n**(3) Coordination with credit allowed against United States income taxes**\nNo credit shall be allowed against United States income taxes under section 6433A of the Internal Revenue Code of 1986 (as added by this section) to any person\u2014\n**(A)**\nto whom a credit is allowed against taxes imposed by the possession by reason of the amendments made by this section, or\n**(B)**\nwho is eligible for a payment under a plan described in paragraph (2).\n**(4) Mirror code tax system**\nFor purposes of this subsection, the term mirror code tax system means, with respect to any possession of the United States, the income tax system of such possession if the income tax liability of the residents of such possession under such system is determined by reference to the income tax laws of the United States as if such possession were the United States.\n**(5) Treatment of payments**\nFor purposes of section 1324 of title 31, United States Code, the payments under this subsection shall be treated in the same manner as a refund due from a credit provision referred to in subsection (b)(2) of such section.\n##### (c) Coordination with savers' credit\nSection 25B(c)(1) of the Internal Revenue Code of 1986 is amended by inserting and such individual has made an election under section 6433A(e)(5) not to have section 6433A apply for such taxable year before the period at the end.\n##### (d) Deficiencies\nSection 6211(b)(4) of the Internal Revenue Code of 1986 is amended by striking and 6433 and inserting 6433, and 6433A .\n##### (e) Payment authority\nSection 1324(b)(2) of title 31, United States Code, is amended by striking or 6433 and inserting 6433, or 6433A .\n##### (f) Clerical amendment\nThe table of sections for subchapter B of chapter 65 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 6433 the following new item:\nSec. 6433A. Matching payments for ABLE account contributions by certain individuals. .\n##### (g) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.\n#### 3. Demographic reporting with respect to ABLE accounts\n##### (a) In general\nSection 529A(d)(1) of the Internal Revenue Code of 1986 is amended by adding at the end the following new sentence: In addition to the information required under the preceding sentence, each officer or employee having control of the qualified ABLE program of their designee shall include in reports provided to the Secretary demographic information (including race, gender, and disability type) relating to the designated beneficiaries of ABLE accounts under the program. .\n##### (b) Effective date\nThe amendment made by this section shall apply to reports made after the date of the enactment of this section.\n#### 4. Grants to promote use of ABLE accounts and the matching contribution credit\n##### (a) In general\nThe Secretary of the Treasury (or the Secretary's delegate) may award grants to States to enable States to promote ABLE accounts (as defined in section 529A(e) of the Internal Revenue Code of 1986) and matching payments for contributions to such accounts (as provided under section 6433A of such Code, as added by this Act).\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $5,000,000 for each of fiscal years 2027 through 2030.",
      "versionDate": "2026-05-12",
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
        "name": "Taxation",
        "updateDate": "2026-05-28T20:36:31Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4492is.xml"
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
      "title": "ABLE MATCH (Making Able a Tool to Combat Hardship) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ABLE MATCH (Making Able a Tool to Combat Hardship) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide matching payments for ABLE account contributions by certain individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:34Z"
    }
  ]
}
```
