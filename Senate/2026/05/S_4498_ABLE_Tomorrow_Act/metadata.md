# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4498?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4498
- Title: ABLE Tomorrow Act
- Congress: 119
- Bill type: S
- Bill number: 4498
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-28T21:53:02Z
- Update date including text: 2026-05-28T21:53:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4498",
    "number": "4498",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "ABLE Tomorrow Act",
    "type": "S",
    "updateDate": "2026-05-28T21:53:02Z",
    "updateDateIncludingText": "2026-05-28T21:53:02Z"
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
          "date": "2026-05-12T19:05:25Z",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4498is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4498\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mr. Moran (for himself, Mr. Van Hollen , Mr. Tillis , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to make expiring ABLE provisions permanent, improve accessibility and education for families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ABLE Tomorrow Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPeople with disabilities are more than two and half times as likely to live in poverty than people without disabilities. In every State, people with disabilities experience higher poverty rates than both the rate for people without disabilities and the overall State poverty rate. Households containing an adult with a disability that limits their ability to work require more income to obtain the same standard of living as similar households without a member with a disability.\n**(2)**\nThe Stephen Beck, Jr., Achieving a Better Life Experience Act of 2014 provided for qualified ABLE programs, which provided eligible people with disabilities the opportunity to open tax-advantaged savings accounts which they can use for meeting qualified disability-related expenses without the risk of losing eligibility for certain benefits they need to maintain health, independence, and quality of life.\n**(3)**\nSince the establishment of ABLE accounts, legislative changes have been made to increase access to, uptake, and sustainability of the program, including increasing the disability onset age from before age 26 to before age 46 to qualify for an ABLE account, allowing working ABLE account holders to contribute additional amounts to the annual contribution limit, creating a Saver\u2019s credit allowance for ABLE contributions, and allowing for rollovers of 529 accounts.\n**(4)**\nAs of 2025, there were hundreds of thousands of ABLE accounts open in the United States with several million individuals with disabilities eligible for ABLE accounts. This number is expected to nearly double and as amendments made by the SECURE 2.0 Act of 2022 take effect beginning January 2026.\n#### 3. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto encourage and assist individuals with disabilities who have fewer resources to save using ABLE accounts;\n**(2)**\nto increase uptake and continued utilization of ABLE accounts by people with disabilities, especially those individuals receiving benefits under the Medicaid program established under title XIX of the Social Security Act and the program for supplemental security income benefits established under title XVI of such Act; and\n**(3)**\nto help ensure the success and financial stability of ABLE account holders and the whole of the ABLE account program.\n#### 4. Repeal of transfer to State upon death of designated beneficiary\nSection 529A(f) of such Code is amended to read as follows:\n(f) Prohibition on State adjustment or recovery of medical assistance Notwithstanding section 1917(b) of the Social Security Act or any other provision of law, no State may seek adjustment or recovery of any medical assistance correctly paid on behalf of a designated beneficiary under a State Medicaid Plan from the ABLE account of such designated beneficiary, regardless of whether the ABLE account is part of the designated beneficiary\u2019s estate. .\n#### 5. Modifications to contribution limitations\n##### (a) Repeal of limitation on rollovers\nSection 529(c)(3)(C)(i) of such Code is amended by striking the matter following subclause (III).\n##### (b) Exception to contribution limit for certain lump sum payments\n**(1) In general**\nSection 529A(b) of such Code is amended by adding at the end the following new paragraph:\n(8) Exception to contribution limit for certain lump sum payments (A) In general In the case of a contribution to a qualified ABLE program from a third-party trust, a contribution of amounts received by the designated beneficiary as proceeds of a life insurance contract, or an amount distributed from a qualified tuition program (as defined in section 529(b)(1)) that is not includible in gross income of the distributee under section 529(c)(3)(C)(i)(III), subsection (b)(2)(B) shall not apply. (B) Limitation Subparagraph (A) shall not apply with respect to any contribution if such subparagraph has applied to any other contribution in any taxable year to a qualified ABLE program of the qualified beneficiary. .\n**(2) Conforming amendments**\n**(A)**\nSection 529A(b)(2)(B) of such Code is amended by inserting paragraph (8) or after Except in the case of contributions under in the matter preceding clause (i).\n**(B)**\nSection 529A(b)(6) is amended by inserting and any contributions described in paragraph (8)(A) after State agency or instrumentality thereof .\n#### 6. Delay of suspension of benefits\nSection 103(b)(1) of the Stephen Beck, Jr., ABLE Act of 2014 is amended by inserting , and the suspension shall begin with the benefits payable for the 1st calendar month that begins after the 2-month period that begins with the date the individual receives notice from the Commissioner of Social Security that the benefits are to be so suspended before the period.\n#### 7. Protecting working ABLE individuals from losing benefits because of retirement plan rules\n##### (a) In general\nSection 414 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(dd) ABLE account contributions (1) In general An applicable employer plan (as defined in subsection (v)(6)(A)) which is a defined contribution plan shall not be treated as failing to meet any requirement of this title solely because the plan provides that an eligible ABLE individual may elect for a plan year that employer contributions which would otherwise be made under the terms of the plan for such plan year shall (in lieu of contribution to the plan) be contributed by the employer to a qualified ABLE program described in section 529A on behalf of such eligible ABLE individual. (2) Treatment of contributions (A) No deduction for amounts contributed to ABLE account Except as provided in subparagraph (B), a contribution to a qualified ABLE program pursuant to an election under paragraph (1) shall not be treated as a contribution to an applicable employer plan. (B) Application of nondiscrimination rules Under rules prescribed by the Secretary, for purposes of applying sections 401(a)(4), 401(k)(3), 401(k)(12), 401(k)(13), 401(m)(2), 403(b)(12), 408(k)(3), 408(p)(2)(A)(iii), 408(p)(2)(B), 410, and 416, contributions made to a qualified ABLE program pursuant to an election under paragraph (1) shall be treated as if such contributions were made to the plan. (3) Universal availability Paragraph (1) shall not apply unless the plan provides that the election described therein is available to all eligible ABLE individuals who are eligible to participate in the plan. (4) Cash or deferred arrangement A plan shall not fail to be treated as including a qualified cash or deferred arrangement described in section 401(k)(1) solely because such plan provides for the election described in paragraph (1). (5) Eligible ABLE individual For purposes of this subsection, the term eligible ABLE individual means an employee who, as of the first day of a plan year, is an eligible individual within the meaning of section 529A(e)(1) for the taxable year containing such first day of the plan year. (6) Treatment of permissive withdrawals An eligible ABLE individual may direct amounts eligible for withdrawal from an eligible contribution arrangement pursuant to section 414(w) to be contributed to a qualified ABLE program described in section 529A on behalf of such eligible ABLE individual. .\n##### (b) Treatment as beneficiary contribution\nSection 529A(b)(7) of the Internal Revenue Code of 1986 is amended by redesignating subparagraph (B) as subparagraph (C) and by inserting after subparagraph (A) the following new subparagraph:\n(B) Employer contributions Contributions made to a qualified ABLE program by an employer on behalf of a designated beneficiary described in this paragraph pursuant to paragraph (1) or (6) of section 414(a) shall be treated as made by the designated beneficiary. .\n##### (c) Clarification of availability of employer contributions\nSection 529A(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(7) Employer contributions An employer of an eligible individual may contribute to any qualified ABLE program for which the eligible individual is the designated beneficiary, including through a contribution matching a contribution made by such eligible individual to the qualified ABLE program. .\n##### (d) Deduction for contributions remitted by employer to a qualified ABLE program\nNot later than 1 year after the date of the enactment of this Act, the Secretary of the Treasury shall\u2014\n**(1)**\namend the regulations under section 162 of the Internal Revenue Code of 1986 to confirm that contributions made by an employer to a qualified ABLE program described in section 529A of such Code on behalf of an eligible ABLE individual described in section 414(dd)(5) of such Code who is an employee of such employer shall be considered a reasonable allowance for salaries or other compensation for personal service if such contribution for a year, taking into account all other contributions to such qualified ABLE program, does not exceed the maximum contribution described in section 529A(b)(2)(B) of such Code with respect to such individual; and\n**(2)**\nupdate the publications issued for employers to encourage employers offering a retirement plan with automatic enrollment to notify employees who elect not to contribute to the plan and who may be eligible to contribute to a qualified ABLE program to notify such employees of the possibility of a contribution under section 529A(b)(2)(B)(ii) of such Code.\n##### (e) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to plan and taxable years beginning after the date of the enactment of this Act.\n**(2) Clarifications**\nThe amendment made by subsection (c) and the amendments made pursuant to subsection (d)(1) shall apply to plan and taxable years beginning before, on, or after the date of the enactment of this Act.\n##### (f) Model amendment authority\nThe Secretary of the Treasury (or such Secretary's delegate) shall promulgate model amendments which plans may adopt to implement contributions to qualified ABLE programs pursuant to the amendments made by this section.\n#### 8. Directing agencies to inform people with disabilities about ABLE accounts\n##### (a) Social Security Administration\n**(1) In general**\nBeginning 180 days after the date of enactment of this Act, the Commissioner of Social Security shall provide the information described in paragraph (3) to any individual who is receiving any of the following on or after such date:\n**(A)**\nA supplemental security income benefit under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ).\n**(B)**\nA disability insurance benefit under section 223 of the Social Security Act ( 42 U.S.C. 423 ).\n**(C)**\nA monthly insurance benefit under section 202 of the Social Security Act ( 42 U.S.C. 402 ) based on such individual's disability (as defined in section 223(d) of such Act ( 42 U.S.C. 423(d) )).\n**(2) Provision of information upon redetermination or overpayment**\nBeginning 180 days after the date of enactment of this Act, the Commissioner of Social Security shall, in addition to providing the information described in paragraph (3) in accordance with paragraph (1), provide such information to any individual receiving a benefit described in paragraph (1)\u2014\n**(A)**\nwhenever such individual's eligibility for such benefit is redetermined; and\n**(B)**\nwhenever such individual is found to have received an overpayment of such benefits due to the individual having resources that exceed the amount established under subparagraph (A) or (B) of section 1611(a)(3) of the Social Security Act ( 42 U.S.C. 1382(a)(3) ), as applicable to the individual.\n**(3) Information on ABLE accounts**\nThe information described in this paragraph is the following:\n**(A)**\nInformation on the existence of\u2014\n**(i)**\nqualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986; and\n**(ii)**\nresources for people with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today.\n**(B)**\nInstructions on how to open an ABLE account (as defined in section 529A of the Internal Revenue Code of 1986).\n##### (b) Department of Veterans Affairs\n**(1) In general**\nChapter 63 of title 38, United States Code, is amended by adding at the end the following new section:\n6321. ABLE programs (a) In general The Secretary shall inform each veteran and eligible dependent who participates in or receives benefits or services through a program carried out under the laws administered by the Secretary about the existence of qualified ABLE programs and resources for people with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today, at the time such veteran or eligible dependent first participates in or receives such benefit or service through such program. (b) Definitions In this section: (1) Eligible dependent The term eligible dependent has the meaning given that term in section 6301(b) of this title. (2) Qualified ABLE program The term qualified ABLE program has the meaning given that term in section 529A of the Internal Revenue Code of 1986. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 63 of such title is amended by adding at the end the following new item:\n6321. ABLE programs. .\n##### (c) Department of Housing and Urban Development\n**(1) Definition**\nIn this subsection, the term covered housing program means\u2014\n**(A)**\nthe program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 ); and\n**(B)**\nthe tenant-based assistance program under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ).\n**(2) Requirement**\nThe Secretary of Housing and Urban Development shall ensure that when a family or an individual enrolls in a covered housing program or otherwise begins to occupy housing assisted by a covered housing program, the family or individual is informed about\u2014\n**(A)**\nthe existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986; and\n**(B)**\nresources for people with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today.\n##### (d) Chapter 85 of title 41, United states code\nSection 8503(d) of title 41, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) shall provide regulations providing that, when a qualified nonprofit agency that produces a product or services for the Federal Government under subsection (c) enrolls an individual in a program to produce the product or services, the agency shall inform the individual about\u2014 (A) the existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986; and (B) resources for people with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today. .\n##### (e) State Medicaid and CHIP agencies\n**(1) Medicaid**\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended\u2014\n**(A)**\nin paragraph (88), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (89), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (89) the following new paragraph:\n(90) provide that the State will inform any individual who enrolls for medical assistance under the State plan (or under a waiver of such plan) about the existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986, and resources for people with disabilities, such as the ABLE National Resources Center, the National Association of State Treasurers, and ABLE Today, when they first enroll for such assistance. .\n**(2) CHIP**\nSection 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ) is amended\u2014\n**(A)**\nby redesignating subparagraphs (I) through (W) as subparagraphs (J) through (X), respectively; and\n**(B)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) Section 1902(a)(90) (relating to the provision of information about ABLE accounts to individuals when they first enroll for medical assistance). .\n**(3) Effective date**\nThe amendments made by this subsection shall take effect on the date that is 180 days after the date of enactment of this Act.\n##### (f) State TANF agencies\n**(1) In general**\nSection 408(a) of the Social Security Act ( 42 U.S.C. 608(a) ) is amended by adding at the end the following new paragraph:\n(13) State requirement to provide information about ABLE accounts Beginning 180 days after the date of enactment of the ABLE Awareness Act, a State to which a grant is made under section 403 shall provide information about the existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986, and resources for people with disabilities, such as the ABLE National Resources Center, the National Association of State Treasurers, and ABLE Today, to any family receiving or applying for assistance under such grant. .\n**(2) State plan requirement**\nSection 402(a)(1)(B) of the Social Security Act ( 42 U.S.C. 602(a)(1)(B) ) is amended by adding at the end the following new clause:\n(vi) The document shall include information about how the State will provide information about qualified ABLE programs to individuals as required under section 408(a)(13). .\n##### (g) Nutrition assistance programs\nEach State shall inform people with disabilities (as defined in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 )) about the existence of qualified ABLE programs (as defined in section 529A of the Internal Revenue Code of 1986), and resources for people with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today, on enrollment in any means-tested nutrition assistance program of the Department of Agriculture or the Department of Defense, including\u2014\n**(1)**\nthe supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ); and\n**(2)**\nthe special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ).\n##### (h) Rehabilitation Act of 1973\nSection 101(a) of the Rehabilitation Act of 1973 ( 29 U.S.C. 721(a) ) is amended by adding at the end the following:\n(27) Information on ABLE programs The State plan shall provide that, when an individual with a disability (as defined in section 7(20)(A)) enrolls in a vocational rehabilitation program, the designated State unit shall inform the person about\u2014 (A) the existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986; and (B) resources for individuals with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today. .\n##### (i) Medicare\nBeginning 180 days after the date of enactment of this Act, the Secretary of Health and Human Services shall provide the information described in subsection (a)(3)(A) to any individual entitled to benefits under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) by reason of section 1811(2) of such Act ( 42 U.S.C. 1395c(2) ) at the time such individual becomes entitled to such benefits.\n##### (j) Head Start Act\n**(1) Head Start programs**\nSection 642(b) of the Head Start Act ( 42 U.S.C. 9837(b) ) is amended by adding at the end the following:\n(17) When a child is enrolled by the Head Start agency, inform the child's family about\u2014 (A) the existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986; and (B) resources for individuals with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today. .\n**(2) Early Head Start programs**\nSection 645A(b) of the Head Start Act ( 42 U.S.C. 9840a(b) ) is amended\u2014\n**(A)**\nby redesignating paragraph (12) as paragraph (13); and\n**(B)**\nby inserting after paragraph (11) the following:\n(12) when a child is enrolled by the entity, inform the child's family about\u2014 (A) the existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986; and (B) resources for individuals with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today; and .\n##### (k) Individuals with Disabilities Act\n**(1) In general**\nSection 612(a) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1412(a) ) is amended by adding at the end the following:\n(26) Information on ABLE programs The parents of each child receiving special education and related services under this part or early intervening services under section 613(f) are provided with information regarding\u2014 (A) the existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986; and (B) resources for individuals with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today. .\n**(2) Infants and toddlers with disabilities program**\nSection 635(a) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1435(a) ) is amended by adding at the end the following:\n(17) Policies and procedures to ensure that the parents of each infant or toddler with a disability who receives early intervention services under this part are provided with information regarding\u2014 (A) the existence of qualified ABLE programs as defined in section 529A of the Internal Revenue Code of 1986; and (B) resources for individuals with disabilities, such as the ABLE National Resource Center, the National Association of State Treasurers, and ABLE Today. .\n#### 9. ABLE awareness grants\n##### (a) In general\nThe Secretary may award grants to eligible entities for the purposes of promoting the availability of ABLE programs and their benefits and encouraging the establishment of ABLE accounts for eligible individuals.\n##### (b) Eligible entity\nFor purposes of this section, the term eligible entity means\u2014\n**(1)**\nany State, or any agency or instrumentality thereof;\n**(2)**\nan Indian tribal government or any subdivision thereof; or\n**(3)**\nany consortium of entities described in paragraph (1) or (2).\n##### (c) Awarding grants\n**(1) Application**\nAn eligible entity desiring a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing or accompanied by such information, as the Secretary may reasonably require.\n**(2) Data collection and reporting**\nThe Secretary may not award a grant under this section unless the eligible entity agrees to collect data on the number of ABLE accounts established as a result of activities carried out with the grant funds.\n##### (d) Use of funds\n**(1) In general**\nAn eligible entity receiving a grant under this section shall use the grant to increase awareness of ABLE accounts and to provide information on how to enroll in such accounts.\n**(2) Activities**\nAn eligible entity may use a grant under this section for\u2014\n**(A)**\nmedia buys;\n**(B)**\nconferences, meetings, canvassing, and recruitment; and\n**(C)**\nother activities to promote the availability and establishment of ABLE accounts.\n##### (e) Other terms\nFor purposes of this section:\n**(1) ABLE program; ABLE account; eligible individual**\nThe terms ABLE program , ABLE account , and eligible individual have the respective meaning given such terms under section 529A of the Internal Revenue Code of 1986.\n**(2) Secretary**\nThe term Secretary means the Secretary of the Treasury or the Secretary's delegate.\n**(3) State**\nThe term State includes any territory or possession of the United States.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $50,000,000 for each of fiscal years 2027 through 2031.",
      "versionDate": "2026-05-12",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4644",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ABLE Employment Flexibility Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2459",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ABLE Employment Flexibility Act",
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
        "updateDate": "2026-05-28T20:31:27Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4498is.xml"
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
      "title": "ABLE Tomorrow Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T03:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ABLE Tomorrow Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to make expiring ABLE provisions permanent, improve accessibility and education for families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T03:03:40Z"
    }
  ]
}
```
