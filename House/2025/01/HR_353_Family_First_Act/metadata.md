# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/353?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/353
- Title: Family First Act
- Congress: 119
- Bill type: HR
- Bill number: 353
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2026-02-06T16:14:15Z
- Update date including text: 2026-02-06T16:14:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/353",
    "number": "353",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Family First Act",
    "type": "HR",
    "updateDate": "2026-02-06T16:14:15Z",
    "updateDateIncludingText": "2026-02-06T16:14:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:00:15Z",
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
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr353ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 353\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Moore of Utah introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to enhance the child tax credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Family First Act .\nI\nChild Tax Credit and Tax Credit for Pregnant Mothers\n#### 101. Permanent expansion of child tax credit\n##### (a) In general\nSection 24 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking subsections (a) through (e) and inserting the following new subsections:\n(a) Allowance of credit (1) In general There shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the applicable percentage of the base credit amount. (2) Base credit amount For purposes of paragraph (1), the base credit amount shall be an amount equal to the sum of\u2014 (A) for each qualifying child who has not attained age 6 as of the close of the calendar year in which the taxable year of the taxpayer begins, $4,200, and (B) for each qualifying child of the taxpayer who is not described in subparagraph (A), $3,000. (b) Applicable percentage and limitation based on adjusted gross income (1) Applicable percentage For purposes of subsection (a), the applicable percentage shall be\u2014 (A) in the case of a taxpayer whose modified adjusted gross income is equal to or greater than $20,000, 100 percent, or (B) in the case of a taxpayer whose modified adjusted gross income is less than $20,000, an amount (expressed as a percentage) equal to the quotient of\u2014 (i) the modified adjusted gross income of the taxpayer, divided by (ii) $20,000. (2) Limitation The amount of the credit allowable under subsection (a) shall be reduced (but not below zero) by $50 for each $1,000 (or fraction thereof) by which the taxpayer's modified adjusted gross income exceeds\u2014 (A) in the case of a joint return, $400,000, or (B) in any other case, $200,000. (3) Modified adjusted gross income For purposes of this subsection, the term modified adjusted gross income means adjusted gross income increased by any amount excluded from gross income under section 911, 931, or 933. (4) Adjustment for inflation (A) In general In the case of a taxable year beginning after 2026, each of the $20,000 amounts in paragraph (1) shall be increased by an amount equal to\u2014 (i) $20,000, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting 2025 for 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any increase under this paragraph is not a multiple of $100, such increase shall be rounded to the next lowest multiple of $100. (c) Qualifying child For purposes of this section\u2014 (1) In general The term qualifying child means a qualifying child of the taxpayer (as defined in section 152(c)) who has not attained age 18 as of the close of the calendar year in which the taxable year of the taxpayer begins. (2) Exception for certain noncitizens The term qualifying child shall not include any individual who would not be a dependent if subparagraph (A) of section 152(b)(3) were applied without regard to all that follows resident of the United States . (d) Limitation on number of children The number of qualifying children of a taxpayer for which a credit may be allowed under this section for any taxable year shall not exceed 6. (e) Identification requirements (1) In general No credit shall be allowed under this section to a taxpayer who does not include on the return of tax for the taxable year\u2014 (A) the social security number of the taxpayer (and, in the case of a joint return, the social security number of at least 1 spouse), and (B) with respect to any qualifying child, the name and the social security number of such qualifying child. (2) Social security number defined For purposes of this subsection, the term social security number means, with respect to a return of tax, a social security number issued to an individual by the Social Security Administration, but only if the social security number is issued\u2014 (A) to a citizen of the United States or pursuant to subclause (I) (or that portion of subclause (III) that relates to subclause (I)) of section 205(c)(2)(B)(i) of the Social Security Act, and (B) before the due date of filing such return. ,\n**(2)**\nby striking subsections (h) through (j),\n**(3)**\nin subsection (k)\u2014\n**(A)**\nby striking paragraph (2) and inserting the following:\n(2) Puerto Rico In the case of any bona fide resident of Puerto Rico (within the meaning of section 937(a)), the credit determined under this section shall be allowable to such resident. , and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking and without regard to the application of this section to bona fide residents of Puerto Rico under subsection (i)(1) , and\n**(ii)**\nin subparagraph (C), by striking clause (ii) and inserting the following:\n(ii) Application of section in event of absence of approved plan In the case of a taxable year with respect to which a plan is not approved under subparagraph (B), rules similar to the rules of paragraph (2) shall apply with respect to bona fide residents of American Samoa (within the meaning of section 937(a)). , and\n**(4)**\nby redesignating subsection (k) (as amended by paragraph (3)) as subsection (h).\n##### (b) Treatment as fully refundable\n**(1) Credit moved to subpart relating to refundable credits**\n**(A) In general**\nThe Internal Revenue Code of 1986 is amended\u2014\n**(i)**\nby redesignating section 24, as amended by this section, as section 36C, and\n**(ii)**\nby moving such section, as so redesignated, from subpart A of part IV of subchapter A of chapter 1 to the location immediately after section 36B in subpart C of part IV of subchapter A of chapter 1.\n**(B) Technical amendment**\nSubsection (a) of section 36C of such Code, as moved and redesignated by subparagraph (A), is amended by striking this chapter and inserting this subtitle .\n**(C) Clerical amendments**\n**(i)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by striking the item relating to section 24.\n**(ii)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 36C. Child tax credit. .\n**(2) Conforming amendments**\n**(A)**\nSection 26(b)(2) of such Code is amended\u2014\n**(i)**\nby striking , and at the end of subparagraph (Y) and inserting a period,\n**(ii)**\nby inserting and at the end of subparagraph (X), and\n**(iii)**\nby striking subparagraph (Z).\n**(B)**\nSection 45R(f)(3)(B) of such Code is amended to read as follows:\n(B) Special rule Any amounts paid pursuant to an agreement under section 3121(l) (relating to agreements entered into by American employers with respect to foreign affiliates) which are equivalent to the taxes referred to in subparagraph (A) shall be treated as taxes referred to in such subparagraph. .\n**(C)**\nSection 48D(d)(4) of such Code is amended by striking section 24(k) and inserting section 36C(h) .\n**(D)**\nSection 152(f)(6)(B)(ii) of such Code is amended by striking section 24 and inserting section 36C .\n**(E)**\nSection 501(c)(26) of such Code is amended in the flush matter at the end by striking section 24(c)) and inserting section 36C(c)) .\n**(F)**\nSection 3402(f)(1)(C) of such Code is amended by striking section 24 (determined after application of subsection (j) thereof) and inserting section 36C .\n**(G)**\nSection 6103(l)(13)(A)(v) of such Code is amended by striking section 24 and inserting section 36C .\n**(H)**\nSection 6211(b)(4)(A) of such Code is amended\u2014\n**(i)**\nby striking 24 by reason of subsections (d) and (i)(1) thereof, ,\n**(ii)**\nby inserting and 36C after 36B, , and\n**(iii)**\nby striking , 6428, 6428A, 6428B, and 7527A .\n**(I)**\nSection 6213(g)(2) of such Code is amended\u2014\n**(i)**\nin subparagraph (I), by striking correct TIN required under section 24(e) and inserting correct social security number required under section 36C(e) ,\n**(ii)**\nin subparagraph (L)\u2014\n**(I)**\nby striking 24, or 32 and inserting 32, or 36C , and\n**(II)**\nby striking TIN each place it appears and inserting TIN or social security number , and\n**(iii)**\nin subparagraph (P)\u2014\n**(I)**\nby striking 24(g)(2) and inserting 36C(g)(2) , and\n**(II)**\nby striking section 24 and inserting section 36C .\n**(J)**\nSection 6402(m) of such Code is amended by striking section 24 (by reason of subsection (d) thereof) or 32 and inserting section 32 or 36C .\n**(K)**\nSection 6417(f) of such Code is amended by striking section 24(k) and inserting section 36C(h) .\n**(L)**\nSection 6695(g)(2) of such Code is amended by striking 24, 25A(a)(1), or 32 and inserting 25A(a)(1), 32, or 36C .\n**(M)**\nSection 1324(b)(2) of title 31, United States Code, is amended\u2014\n**(i)**\nby striking 24, , and\n**(ii)**\nby inserting 36C, after 36B, .\n**(N)**\nSection 1613(a)(11)(A) of the Social Security Act ( 42 U.S.C. 1382b(a)(11)(A) ) is amended by striking section 24 of the Internal Revenue Code of 1986 (relating to child tax credit) by reason of subsection (d) thereof and inserting section 36C of the Internal Revenue Code of 1986 (relating to child tax credit) .\n**(O)**\nChapter 77 of such Code is amended by striking section 7527A (and the item relating to such section in the table of sections for such chapter).\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 102. Tax credit for pregnant mothers\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36C (as redesignated by section 101) the following new section:\n36D. Credit for pregnant mothers (a) Allowance of credit In the case of an eligible taxpayer with a qualifying unborn child, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the applicable percentage of $2,800. (b) Applicable percentage (1) In general For purposes of subsection (a), the applicable percentage shall be\u2014 (A) in the case of a taxpayer whose modified adjusted gross income is equal to or greater than $10,000, 100 percent, or (B) in the case of a taxpayer whose modified adjusted gross income is less than $10,000, the amount (expressed as a percentage) equal to the quotient of\u2014 (i) the modified adjusted gross income of the taxpayer, divided by (ii) $10,000. (2) Limitation The amount of the credit allowable under subsection (a) shall be reduced (but not below zero) by $50 for each $1,000 (or fraction thereof) by which the taxpayer's modified adjusted gross income exceeds\u2014 (A) in the case of a joint return, $400,000, or (B) in any other case, $200,000. (3) Modified adjusted gross income For purposes of this subsection, the term modified adjusted gross income has the same meaning given such term in section 36C(b)(3). (4) Adjustment for inflation (A) In general In the case of a taxable year beginning after 2026, each of the $10,000 amounts in paragraph (1) shall be increased by an amount equal to\u2014 (i) $10,000, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting 2025 for 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any increase under this paragraph is not a multiple of $100, such increase shall be rounded to the next lowest multiple of $100. (c) Qualifying unborn child (1) In general For purposes of this section, the term qualifying unborn child means an unborn child whose gestational age is 20 weeks or greater, as certified by a physician in accordance with paragraph (2). (2) Certification (A) In general Upon the request of the mother, a physician may make a determination with respect to the gestational age of the unborn child. Any determination made under this paragraph shall be based on the reasonable medical judgment of the physician following such inquiries, examinations, and tests as a reasonably prudent physician would deem necessary for purposes of making such determination. (B) Form If the physician has made a determination pursuant to subparagraph (A) that the gestational age of the unborn child is 20 weeks or greater, such physician may, upon the request of the mother, provide the mother with a form which includes the following: (i) The gestational age and the expected due date of the unborn child. (ii) The name and social security number of the mother. (iii) If applicable, the name and social security number of the spouse of such mother. (iv) The name and contact information of the physician. (v) A written certification from such physician stating, under penalty of perjury pursuant to section 1746 of title 28, that\u2014 (I) the mother was determined to have been pregnant with the unborn child, according to standard medical practice, by such physician, and (II) such physician has determined that, in their reasonable medical judgment, the gestational age of the unborn child is 20 weeks or greater. (vi) A written certification from the mother of the unborn child stating, under penalty of perjury pursuant to section 1746 of title 28, United States Code, that she\u2014 (I) is the biological mother of such unborn child, or (II) initiated the pregnancy with the intention of bearing and retaining custody of and parental rights to such child (or acted to such effect). (C) Prohibition Notwithstanding any other provision of law, the certification described in this paragraph shall not be used for any purpose other than to determine the eligibility of the taxpayer for the credit allowed under this section. (d) Application (1) In general In the case of the involuntary death of an unborn child, or the death of an unborn child as a result of any treatment intended to save the life of the mother or any treatment of an ectopic pregnancy, occurring after 20 weeks gestation, the death of such child shall have no effect with respect to whether the credit is allowed under this section to an eligible taxpayer, provided that such taxpayer otherwise satisfies the applicable requirements under this section. (2) More than 1 unborn child during the same taxable year In the case of an eligible taxpayer who\u2014 (A) has more than 1 pregnancy during a taxable year, or (B) is determined to be pregnant with more than 1 qualifying unborn child, the credit under this section shall be allowed with respect to each qualifying unborn child. (3) Interaction with child tax credit The allowance of a credit under this section with respect to a qualifying unborn child shall have no effect in regards to the application of section 36C with respect to such child after the date of their birth. (e) Prohibition No credit shall be allowed under this section if an unborn child died as a result of an induced abortion, but not including any treatment intended to save the life of the mother or any treatment of an ectopic pregnancy. (f) Definitions In this section\u2014 (1) Eligible taxpayer The term eligible taxpayer means a taxpayer who\u2014 (A) with respect to an unborn child, is the mother who\u2014 (i) carries or carried such child in the womb, and (ii) is the biological mother of such child or initiated the pregnancy with the intention of bearing and retaining custody of and parental rights to such child (or acted to such effect), or (B) in the case of a joint return, is the spouse of such mother, but only if such taxpayer includes on the return of tax for the taxable year the social security number of such taxpayer (of at least 1 of such mother or spouse, in the case of a joint return). (2) Gestational age The term gestational age means the age of the unborn child, as calculated from the first day of the mother\u2019s last menstrual period. (3) Physician The term physician means an individual who is\u2014 (A) licensed to practice\u2014 (i) medicine and surgery, (ii) osteopathic medicine and surgery, or (iii) midwifery, or (B) otherwise legally authorized to\u2014 (i) perform births and to diagnose and attend miscarriages or stillbirths, and (ii) perform examinations to determine the gestational age of an unborn child, by the State in which such practice is performed. (4) Reasonable medical judgment The term reasonable medical judgment means a medical judgment that would be made by a reasonably prudent physician who is knowledgeable about the case and the treatment possibilities with respect to the medical conditions involved. (5) Social security number The term social security number has the meaning given such term by section 36C(e)(2). .\n##### (b) Clerical amendment\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36C the following new item:\nSec. 36D. Credit for pregnant mothers. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\nI\nOther amendments to the Internal Revenue Code of 1986\n#### 201. Simplification of earned income credit for taxpayers with children\n##### (a) Additional limitation\nSection 32(a)(2) of the Internal Revenue Code of 1986 is amended to read as follows:\n(2) Limitation The amount of the credit allowable to a taxpayer under paragraph (1) for any taxable year shall not exceed the lesser of\u2014 (A) the excess (if any) of\u2014 (i) the credit percentage of the earned income amount, over (ii) the phaseout percentage of so much of the adjusted gross income (or, if greater, the earned income) of the taxpayer for the taxable year as exceeds the phaseout amount, or (B) an amount equal to\u2014 (i) in the case of any taxpayer with no qualifying children\u2014 (I) who is not filing a joint return, $700, or (II) who is filing a joint return, $1,400, or (ii) in the case of any taxpayer with 1 or more qualifying children\u2014 (I) who is not filing a joint return, $4,300, or (II) who is filing a joint return, $5,000. .\n##### (b) Credit percentage and phaseout percentage\nThe table contained in section 32(b)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 1 qualifying child in the first row and inserting 1 or more qualifying children ,\n**(2)**\nby striking 15.98 in the first row and inserting 25 ,\n**(3)**\nby striking the second and third rows, and\n**(4)**\nby striking 7.65 in the third column of the last row and inserting 10 .\n##### (c) Earned income and phaseout amounts\nThe table contained in section 32(b)(2)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 1 qualifying child in the first row and inserting 1 or more qualifying children ,\n**(2)**\nby striking $6,330 in the first row and inserting $12,647 ,\n**(3)**\nby striking $11,610 in the first row and inserting $33,000 ,\n**(4)**\nby striking the second row,\n**(5)**\nby striking $4,220 in the last row and inserting $9,150 , and\n**(6)**\nby striking $5,280 in the last row and inserting $10,000 .\n##### (d) Joint returns\nSection 32(b)(2)(B) of the Internal Revenue Code of 1986 is amended by striking $5,000 and inserting \u201c$10,000, and the earned income amount determined under subparagraph (A) shall be increased\u2014\n(i) by $2,059, in the case of a taxpayer with 1 or more qualifying children, and (ii) by $9,151, in the case of a taxpayer with no qualifying children. .\n##### (e) Inflation adjustment\nSection 32(j)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 2015 and inserting 2026 ,\n**(2)**\nby striking clauses (i) and (ii) of subparagraph (B) thereof and redesignating clause (iii) of such subparagraph as clause (ii), and\n**(3)**\nby inserting before clause (ii) of subparagraph (B) thereof, as so redesignated, the following new clause:\n(i) in the case of amounts in subsection (b)(2), calendar year 2025 for calendar year 2016 , and .\n##### (f) Effective date\n**(1) In general**\nSubject to paragraph (2), the amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n**(2) Nonapplication to exempted children**\n**(A) In general**\nSubject to subparagraph (B), in the case of any eligible individual (as defined in section 32(c)(1) of the Internal Revenue Code of 1986) who has any qualifying children for the taxable year who are exempted children, section 32 of the Internal Revenue Code of 1986 shall be applied with respect to such eligible individual as if the amendments made by subsections (a) through (e) of this section had not been enacted.\n**(B) Separate application**\nIn the case of any eligible individual (as so defined) who has\u2014\n**(i)**\nany qualifying children for the taxable year who are not exempted children, and\n**(ii)**\nany qualifying children for such taxable year who are exempted children,\nsection 32 of the Internal Revenue Code of 1986 shall be applied separately with respect to the children described in clause (i) and (pursuant to the rules described in subparagraph (A)) the children described in clause (ii).\n**(C) Exempted child**\nFor purposes of this paragraph, the term exempted child means an individual who is described in subparagraph (A)(ii) or (B) of section 152(c)(3).\n#### 202. Elimination of additional exemption for dependents\n##### (a) In general\nSection 151(d)(5) of the Internal Revenue Code of 1986 is amended to read as follows:\n(5) Elimination of additional exemption for dependents for taxable years after 2025 In the case of a taxable year beginning after December 31, 2025\u2014 (A) In general For purposes of subsection (c), the term exemption amount means zero. (B) References For purposes of any other provision of this title, the reduction of the exemption amount to zero under subparagraph (A) shall not be taken into account in determining whether a deduction is allowed or allowable, or whether a taxpayer is entitled to a deduction, under this section. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 203. Elimination of head of household filing status\n##### (a) In general\nSection 1 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking subsection (b),\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin the heading, by striking and heads of households , and\n**(B)**\nby striking or the head of a household as defined in section 2(b) ,\n**(3)**\nin subsection (f), by striking (b), each place it appears,\n**(4)**\nin subsection (i)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)(i), by striking (b), ,\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (i), by adding and at the end,\n**(II)**\nby striking clause (ii), and\n**(III)**\nby redesignating clause (iii) as clause (ii), and\n**(iii)**\nin subparagraph (C), by striking subparagraph (B)(iii) and inserting subparagraph (B)(ii) ,\n**(B)**\nin paragraph (2), by striking (b), , and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking (b), ,\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby striking clause (ii), and\n**(II)**\nby redesignating clauses (iii) and (iv) as clauses (ii) and (iii), respectively, and\n**(iii)**\nin subparagraph (C), by striking clauses (i), (ii), and (iii) and inserting clauses (i) and (ii) , and\n**(5)**\nin subsection (j)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby striking subparagraph (B), and\n**(ii)**\nin subparagraph (C), by striking and heads of households in the heading,\n**(B)**\nin paragraph (3)(B)(ii), by striking or head of household , and\n**(C)**\nin paragraph (5)(B)\u2014\n**(i)**\nin clause (i)\u2014\n**(I)**\nby striking subclause (II), and\n**(II)**\nby redesignating subclauses (III) and (IV) as subclauses (II) and (III), respectively, and\n**(ii)**\nin clause (ii)\u2014\n**(I)**\nby striking subclause (II), and\n**(II)**\nby redesignating subclauses (III) and (IV) as subclauses (II) and (III), respectively.\n##### (b) Conforming amendments\n**(1)**\nSection 25B(b)(2) of the Internal Revenue Code of 1986 is amended to read as follows:\n(2) Other returns In the case of any taxpayer not described in paragraph (1), the applicable percentage shall be determined under paragraph (1) except that such paragraph shall be applied by substituting for each dollar amount therein (as adjusted under paragraph (3)) a dollar amount equal to 50 percent of such dollar amount. .\n**(2)**\nSection 25E(b)(2) of such Code is amended\u2014\n**(A)**\nin subparagraph (A), by adding and at the end, and\n**(B)**\nby striking subparagraphs (B) and (C) and inserting the following:\n(B) in the case of a taxpayer not described in subparagraph (A), $75,000. .\n**(3)**\nSection 30D(f)(10)(B) of such Code is amended\u2014\n**(A)**\nin clause (i), by adding and at the end, and\n**(B)**\nby striking clauses (ii) and (iii) and inserting the following:\n(ii) in the case of a taxpayer not described in clause (i), $150,000. .\n**(4)**\nSection 36B(b)(3)(B)(ii)(I)(aa) of such Code is amended by striking and heads of households .\n**(5)**\nSection 63(c) of such Code is amended\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)(ii), by adding or at the end,\n**(ii)**\nby striking subparagraph (B), and\n**(iii)**\nby redesignating subparagraph (C) as subparagraph (B),\n**(B)**\nin paragraph (4), by striking , (2)(C), each place it appears, and\n**(C)**\nin paragraph (7)\u2014\n**(i)**\nby striking subparagraph (A) and inserting the following:\n(A) Increase in standard deduction Paragraph (2)(B) shall be applied by substituting $12,000 for $3,000 . , and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (i), by striking paragraphs (2)(B) and (2)(C) and inserting paragraph (2)(B) , and\n**(II)**\nin clause (ii), by striking $18,000 and $12,000 amounts and inserting $12,000 amount .\n**(6)**\nSection 68(b) of such Code is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking subparagraph (B),\n**(ii)**\nin subparagraph (C), by striking or head of household , and\n**(iii)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (B) and (C), respectively, and\n**(B)**\nin paragraph (2), by striking subparagraphs (A), (B), and (C) and inserting subparagraphs (A) and (B) .\n**(7)**\nSection 904(b)(3)(E)(i)(I) of such Code is amended by striking (b), .\n**(8)**\nSection 6012(a)(1) of such Code is amended\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i), by striking is not a head of a household (as defined in section 2(b)), ,\n**(ii)**\nby striking clause (ii),\n**(iii)**\nby redesignating clauses (iii) and (iv) as clauses (ii) and (iii), respectively, and\n**(iv)**\nin the flush text at the end, by striking Clause (iv) and inserting Clause (iii) , and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking clause (i), (ii), or (iii) and inserting clause (i) or (ii) , and\n**(ii)**\nby striking clause (iv) and inserting clause (iii) .\n**(9)**\nSection 6433(b)(3)(B) of such Code is amended to read as follows:\n(B) Other returns In the case of any taxpayer who is not filing a joint return and who is not a surviving spouse (as defined in section 2(a)), the applicable dollar amount and the phaseout range shall be \u00bd of the amounts applicable under subparagraph (A) (as so adjusted). .\n**(10)**\nSection 6695(g) of such Code is amended to read as follows:\n(g) Failure To be diligent in determining eligibility for certain tax benefits Any person who is a tax return preparer with respect to any return or claim for refund who fails to comply with due diligence requirements imposed by the Secretary by regulations with respect to determining eligibility for, or the amount of, the credit allowable by section 25A(a)(1), 32, or 36C shall pay a penalty of $500 for each such failure. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 204. Exclusion of children from credit for expenses for household and dependent care services necessary for gainful employment\n##### (a) In general\nSection 21 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking subparagraph (A),\n**(ii)**\nin subparagraph (B), by inserting who has attained age 18 and before who is physically or mentally incapable , and\n**(iii)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (A) and (B), respectively, and\n**(B)**\nin paragraph (2), by striking subparagraph (B) and inserting the following:\n(B) Exception Employment-related expenses described in subparagraph (A) which are incurred for services outside the taxpayer's household shall be taken into account only if incurred for the care of a qualifying individual who regularly spends at least 8 hours each day in the taxpayer's household. ,\n**(2)**\nin subsection (d)(2), by striking subsection (b)(1)(C) and inserting subsection (b)(1)(B) , and\n**(3)**\nin subsection (e)(5)\u2014\n**(A)**\nin subparagraph (B), by striking is under the age of 13 or and inserting has attained age 18 and , and\n**(B)**\nin the flush text at the end, by striking subparagraph (A) or (B) of subsection (b)(1) (whichever is appropriate) and inserting subsection (b)(1)(A) .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 205. Limitation on deduction for State and local taxes of individuals\n##### (a) In general\nSection 164(b)(6) of the Internal Revenue Code of 1986 is amended by striking beginning after December 31, 2017, and before January 1, 2026 and inserting beginning after December 31, 2025 .\n##### (b) Clerical amendment\nThe heading for section 164(b)(6) of such Code is amended by striking 2018 through 2025 and inserting after 2025 .\n##### (c) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-01-13",
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
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1382",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Family First Act",
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
        "updateDate": "2025-02-14T18:45:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr353",
          "measure-number": "353",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2026-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr353v00",
            "update-date": "2026-02-06"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Family First Act</strong></p><p>This bill increases the child tax credit and provides a new tax credit for pregnant mothers. The bill also makes changes to the state and local tax (SALT) deduction, earned income tax credit (EITC), head of household filing status, tax exemption for dependents, and deduction for dependent care expenses.</p><p>This bill increases the child tax credit to as much as $4,200 for each child (depending on the child\u2019s age and the taxpayer's modified adjusted gross income) and makes the tax credit fully refundable. (Currently, a portion is refundable.) Under the bill, the child tax credit is limited to six children and phases out once a taxpayer\u2019s modified adjusted gross income exceeds a certain threshold.</p><p>The bill provides a new refundable tax credit for pregnant mothers of up to\u00a0$2,800 for each unborn child whose gestational age is 20 weeks or more.\u00a0The tax credit phases out once a taxpayer\u2019s modified adjusted gross income exceeds a certain threshold.</p><p>The bill permanently extends the $10,000 limit on the SALT deduction for individuals. (Currently, the SALT deduction limit for individuals expires in 2026.) \u00a0</p><p>The bill permanently eliminates the additional\u00a0personal exemption for dependents. (Under current law, an exemption for dependents is available starting in 2026.)</p><p>This bill also eliminates the</p><p>\u2022 \u00a0 \u00a0head of household filing status,\u00a0<br/>\u2022 \u00a0 \u00a0tax credit for dependent care expenses for children under 13 years old, and\u00a0<br/>\u2022 \u00a0 \u00a0different percentages that apply based on the number of qualifying children in the EITC calculation.</p>"
        },
        "title": "Family First Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr353.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Family First Act</strong></p><p>This bill increases the child tax credit and provides a new tax credit for pregnant mothers. The bill also makes changes to the state and local tax (SALT) deduction, earned income tax credit (EITC), head of household filing status, tax exemption for dependents, and deduction for dependent care expenses.</p><p>This bill increases the child tax credit to as much as $4,200 for each child (depending on the child\u2019s age and the taxpayer's modified adjusted gross income) and makes the tax credit fully refundable. (Currently, a portion is refundable.) Under the bill, the child tax credit is limited to six children and phases out once a taxpayer\u2019s modified adjusted gross income exceeds a certain threshold.</p><p>The bill provides a new refundable tax credit for pregnant mothers of up to\u00a0$2,800 for each unborn child whose gestational age is 20 weeks or more.\u00a0The tax credit phases out once a taxpayer\u2019s modified adjusted gross income exceeds a certain threshold.</p><p>The bill permanently extends the $10,000 limit on the SALT deduction for individuals. (Currently, the SALT deduction limit for individuals expires in 2026.) \u00a0</p><p>The bill permanently eliminates the additional\u00a0personal exemption for dependents. (Under current law, an exemption for dependents is available starting in 2026.)</p><p>This bill also eliminates the</p><p>\u2022 \u00a0 \u00a0head of household filing status,\u00a0<br/>\u2022 \u00a0 \u00a0tax credit for dependent care expenses for children under 13 years old, and\u00a0<br/>\u2022 \u00a0 \u00a0different percentages that apply based on the number of qualifying children in the EITC calculation.</p>",
      "updateDate": "2026-02-06",
      "versionCode": "id119hr353"
    },
    "title": "Family First Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Family First Act</strong></p><p>This bill increases the child tax credit and provides a new tax credit for pregnant mothers. The bill also makes changes to the state and local tax (SALT) deduction, earned income tax credit (EITC), head of household filing status, tax exemption for dependents, and deduction for dependent care expenses.</p><p>This bill increases the child tax credit to as much as $4,200 for each child (depending on the child\u2019s age and the taxpayer's modified adjusted gross income) and makes the tax credit fully refundable. (Currently, a portion is refundable.) Under the bill, the child tax credit is limited to six children and phases out once a taxpayer\u2019s modified adjusted gross income exceeds a certain threshold.</p><p>The bill provides a new refundable tax credit for pregnant mothers of up to\u00a0$2,800 for each unborn child whose gestational age is 20 weeks or more.\u00a0The tax credit phases out once a taxpayer\u2019s modified adjusted gross income exceeds a certain threshold.</p><p>The bill permanently extends the $10,000 limit on the SALT deduction for individuals. (Currently, the SALT deduction limit for individuals expires in 2026.) \u00a0</p><p>The bill permanently eliminates the additional\u00a0personal exemption for dependents. (Under current law, an exemption for dependents is available starting in 2026.)</p><p>This bill also eliminates the</p><p>\u2022 \u00a0 \u00a0head of household filing status,\u00a0<br/>\u2022 \u00a0 \u00a0tax credit for dependent care expenses for children under 13 years old, and\u00a0<br/>\u2022 \u00a0 \u00a0different percentages that apply based on the number of qualifying children in the EITC calculation.</p>",
      "updateDate": "2026-02-06",
      "versionCode": "id119hr353"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr353ih.xml"
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
      "title": "Family First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T23:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Family First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T23:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to enhance the child tax credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T23:33:18Z"
    }
  ]
}
```
