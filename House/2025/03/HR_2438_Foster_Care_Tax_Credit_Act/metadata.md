# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2438?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2438
- Title: Foster Care Tax Credit Act
- Congress: 119
- Bill type: HR
- Bill number: 2438
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-04-17T08:07:27Z
- Update date including text: 2026-04-17T08:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2438",
    "number": "2438",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Foster Care Tax Credit Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:27Z",
    "updateDateIncludingText": "2026-04-17T08:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:08:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-27T13:08:35Z",
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
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NE"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CO"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2438ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2438\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mrs. Houchin (for herself and Ms. Johnson of Texas ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to create a refundable tax credit for foster families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foster Care Tax Credit Act .\n#### 2. Foster care tax credit\n##### (a) Allowance of credit\n**(1) In general**\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Foster care tax credit (a) Allowance of credit In the case of an eligible taxpayer, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to $850. (b) Limitation (1) In general The amount of the credit allowable under subsection (a) (determined without regard to this subsection) shall be reduced (but not below zero) by the amount which bears the same ratio to such credit (as so determined) as\u2014 (A) the excess of\u2014 (i) the taxpayer's modified adjusted gross income for such taxable year, over (ii) the threshold amount, bears to (B) $17,000. (2) Threshold amount For purposes of paragraph (1), the term threshold amount means\u2014 (A) $250,000, in the case of a joint return, (B) $150,000, in the case of an individual who is not married, and (C) $125,000, in the case of a married individual filing a separate return. For purposes of this paragraph, marital status shall be determined under section 7703. (3) Modified adjusted gross income For purposes of this subsection, the term modified adjusted gross income means the adjusted gross income of the taxpayer for the taxable year increased by any amount excluded from gross income under section 911, 931, or 933. (c) Eligible taxpayer For purposes of this section\u2014 (1) In general The term eligible taxpayer means, with respect to any taxable year, any taxpayer\u2014 (A) with whom a qualifying foster child was placed for a period of not less than 1 month during such taxable year, and (B) for whom a credit under section 24 with respect to such eligible foster child is not allowed for such taxable year. (2) Qualifying foster child The term qualifying foster child means an eligible foster child (within the meaning of section 152(f)(1)(C))\u2014 (A) who has not attained age 17, and (B) who is a citizen, national, or resident of the United States. (3) Calendar month For purposes of this paragraph (1)(A), if a foster child resides in the home of the taxpayer for more than 15 consecutive days of a calendar month but fewer than the total number of days in such calendar month, such foster child shall be treated as residing in the home of the taxpayer for the full calendar month. (d) Restrictions on Taxpayers Who Improperly Claimed Credit in Prior Year (1) Taxpayers making prior fraudulent or reckless claims (A) In general No credit shall be allowed under this section for any taxable year in the disallowance period. (B) Disallowance period For purposes of subparagraph (A), the disallowance period is\u2014 (i) the period of 10 taxable years after the most recent taxable year for which there was a final determination that the taxpayer's claim of credit under this section was due to fraud, and (ii) the period of 2 taxable years after the most recent taxable year for which there was a final determination that the taxpayer's claim of credit under this section was due to reckless or intentional disregard of rules and regulations (but not due to fraud). (2) Taxpayers making improper prior claims In the case of a taxpayer who is denied credit under this section for any taxable year as a result of the deficiency procedures under subchapter B of chapter 63, no credit shall be allowed under this section for any subsequent taxable year unless the taxpayer provides such information as the Secretary may require to demonstrate eligibility for such credit. .\n**(2) Conforming amendments**\n**(A)**\nSection 6211(b)(4) of the Internal Revenue Code of 1986 is amended by inserting 36C, after 36B, .\n**(B)**\nSection 1324(b)(2) of title 31, United States Code, is amended by inserting 25E, after 25A, .\n**(C)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Foster care tax credit. .\n##### (b) Information returns relating to foster child placement\n**(1) In general**\nSubpart A of part III of subchapter A of chapter 61 of the Internal Revenue Code of 1986 is amended by inserting after section 6039J the following new section:\n6039K. Information reporting with respect to foster child placement (a) In general Every authorized placement agency and court which places a qualifying foster child with a person during a calendar year shall, at such time as the Secretary shall prescribe, make a return described in subsection (b). (b) Form and manner of return A return is described in this subsection if such return\u2014 (1) is in such form as the Secretary may prescribe, and (2) contains, with respect to each qualifying foster child placed during the calendar year\u2014 (A) the name, address, and TIN of each individual with whom such qualifying foster child was placed, (B) the name of the qualifying foster child, and (C) the dates during which such placement occurred. (c) Statements To be furnished to foster parents (1) In general Every person required to make a return under subsection (a) shall furnish to each individual whose name is required to be set forth under subsection (b)(2)(A) a written statement showing\u2014 (A) the name and address of the person required to make such return and the phone number of the information contact for such person, and (B) the information required to be shown on the return with respect to such individual. (2) Time for furnishing statements The written statement required under paragraph (1) shall be furnished on or before January 31 of the year following the calendar year for which the return under subsection (a) was required to be made. (d) Qualifying foster child For purposes of this section, the term qualifying foster child has the meaning given such term under section 36C(c)(2). .\n**(2) Assessable penalties**\n**(A)**\nSection 6724(d)(1)(B) of such Code is amended by striking or at the end of clause (xxv), by striking and at the end of clause (xxvi) and inserting or , and by inserting after clause (xxvi) the following new clause:\n(xxvii) section 6039K (relating to information returns with respect to foster child placement), .\n**(B)**\nSection 6724(d)(2) of such Code is amended by redesignating the second subparagraph (JJ) as subparagraph (KK), by striking or at the end of subparagraph (II), by striking the period at the end of the first subparagraph (JJ), by striking the period at the end of subparagraph (KK) (as so redesignated) and inserting a comma, and by inserting after such subparagraph (KK) the following new subparagraph:\n(LL) section 6039K(c) (relating to statements with respect to foster child placement). .\n**(3) Clerical amendment**\nThe table of sections of subpart A of part III of subchapter A of chapter 61 of such Code is amended by inserting after the item relating to section 6039J the following new item:\nSec. 6039K. Information reporting with respect to foster child placement. .\n##### (c) Election not To take child tax credit\nSection 24(h)(4) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(D) Election not to take credit A taxpayer may elect not to have this paragraph apply with respect to any dependent of the taxpayer to whom a credit would otherwise be allowed by reason of subparagraph (A). In any case in which a taxpayer makes an election under this subparagraph, the credit allowed under this section shall be treated as not allowed with respect to such dependent. .\n##### (d) Application of tax return preparer due diligence penalty\nSection 6695(g) of the Internal Revenue Code of 1986 is amended by striking or 32 and inserting 32, or 36C .\n##### (e) Effective date\nThe amendments made by this section shall apply to calendar months beginning after December 31, 2024, in taxable years beginning after such date.\n##### (f) Education\n**(1) In general**\nThe Secretary of Health and Human Services (or the Secretary's delegate), in coordination with the Secretary of the Treasury or such Secretary's delegate, shall identify provisions in the Internal Revenue Code of 1986 that can be used by or can benefit foster families, and shall increase outreach efforts to provide information and educational materials regarding such provisions to State and Indian tribal foster care agencies and to foster families.\n**(2) Authorization of appropriations**\nThere are authorized to be appropriated such sums as necessary for the purposes of carrying out paragraph (1).\n#### 3. Study and report on emergency and short-term foster placements\n##### (a) Study\nThe Secretary of Health and Human services, in coordination with the Secretary of the Treasury (or the Secretary's delegate), shall conduct a study on\u2014\n**(1)**\nthe costs and financial burdens on foster families who experience multiple emergency and short-term foster placements annually; and\n**(2)**\nchallenges to verifying and documenting the placement of children in emergency and short-term placement.\nFor purposes of this subsection, a short-term placement is a placement that lasts less than 1 week.\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall submit to Congress a report on the study conducted under subsection (a).",
      "versionDate": "2025-03-27",
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
        "updateDate": "2025-05-09T15:06:39Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2438ih.xml"
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
      "title": "Foster Care Tax Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foster Care Tax Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to create a refundable tax credit for foster families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:42Z"
    }
  ]
}
```
