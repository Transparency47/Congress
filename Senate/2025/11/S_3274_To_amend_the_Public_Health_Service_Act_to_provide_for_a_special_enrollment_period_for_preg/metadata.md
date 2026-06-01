# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3274
- Title: Healthy MOM Act
- Congress: 119
- Bill type: S
- Bill number: 3274
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-01-10T06:43:18Z
- Update date including text: 2026-01-10T06:43:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3274",
    "number": "3274",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000382",
        "district": "",
        "firstName": "Angela",
        "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
        "lastName": "Alsobrooks",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Healthy MOM Act",
    "type": "S",
    "updateDate": "2026-01-10T06:43:18Z",
    "updateDateIncludingText": "2026-01-10T06:43:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T20:37:13Z",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CT"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NV"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-11-20",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3274is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3274\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Ms. Alsobrooks (for herself, Ms. Baldwin , Mr. Blumenthal , Ms. Cortez Masto , Mr. Fetterman , Mrs. Gillibrand , Mr. King , Ms. Klobuchar , Mr. Merkley , Mrs. Murray , Mr. Van Hollen , Mr. Booker , Ms. Duckworth , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to provide for a special enrollment period for pregnant women, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Maternity and Obstetric Medicine Act or the Healthy MOM Act .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nPregnancy is a significant life event for millions of women in the United States each year.\n**(2)**\nFor more than 30 years, our Nation, through the Medicaid program, has recognized that pregnant women need immediate access to affordable care, and has allowed women who meet income-eligibility requirements to enroll in Medicaid coverage when they become pregnant.\n**(3)**\nCongress recognized the central importance of maternity coverage by classifying maternity and newborn care as one of the ten essential health benefits that must now be covered on most individual and small group health insurance plans under section 1302(b)(1) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18022(b)(1) ).\n**(4)**\nCongress has also recognized the significant challenge of maternal mortality and the need to eliminate disparities in maternal health outcomes for pregnancy-related and pregnancy-associated deaths, and to improve health outcomes for both mothers and babies through passage of the Preventing Maternal Deaths Act of 2018 ( Public Law 115\u2013344 ).\n**(5)**\nAccess to comprehensive maternity coverage allows women to access important pregnancy-related care, which is demonstrated to improve health outcomes for women and newborns and reduce financial costs for both consumers and insurers.\n**(6)**\nUninsured women, women with grandfathered and transitional health plans, self-funded student health plans, and catastrophic and high-deductible health plans may lack access to comprehensive and affordable maternity coverage.\n**(7)**\nEmployer health plans that exclude dependent daughters from maternity coverage leave young women without coverage for their pregnancy, even though Federal law has long held that treating pregnancy differently than other conditions is sex-based discrimination.\n**(8)**\nA special enrollment period is especially important for young adults, who are at high risk for unintended pregnancies, yet young adults are frequently enrolled in catastrophic coverage, which often has fewer benefits, more restrictions, and higher deductibles.\n**(9)**\nThis coverage would be an equalizer for communities of color. The maternal mortality rate varies drastically by race and ethnicity, and where a woman lives. The rising maternal mortality rate in the United States is driven predominantly by the disproportionately high African-American maternal mortality rate, which is four times more than the rate for White women.\n**(10)**\nAccording to the Centers for Disease Control and Prevention, about 700 women die each year in the United States from pregnancy-related complications. Black and American Indian/Alaska Native women are about three times more likely to die from a pregnancy-related cause than White women.\n**(11)**\nData demonstrates that 3 in 5 pregnancy related deaths could be prevented. Improving access to care is one way to help prevent deaths, regardless of race or ethnicity.\n**(12)**\nTimely maternity care improves the health of pregnant women, as well as birth outcomes and the health of babies throughout their lifetimes. Pregnancy-related maternal mortality is three to four times higher among women who receive no maternity care compared to women who do. Regular maternity care can detect or mitigate serious pregnancy-related health complications, including preeclampsia, placental abruption, complications from diabetes, complications from heart disease, and Graves\u2019 disease, all of which can result in morbidity or mortality for the mother or newborn.\n**(13)**\nThe Centers for Disease Control and Prevention reports that more than half of all maternal deaths occur at delivery or in the first postpartum year, whereas just more than one-third of pregnancy-related or pregnancy-associated deaths occur while a person is still pregnant. Yet, for women eligible for the Medicaid program on the basis of pregnancy, such Medicaid coverage lapses at the end of the month on which the 60th postpartum day lands.\n**(14)**\nTimely maternity care and adequate postpartum care can reduce short- and long-term health care costs. If a woman does not have access to affordable maternity care during her pregnancy, and she or her newborn experiences pregnancy complications that result in health problems after birth, their insurer may end up paying much higher costs than if the insurer had covered the woman\u2019s maternity care during her pregnancy. Intensive maternity care can reduce hospital and neonatal intensive care unit admissions among infants, resulting in cost savings of $1,768 to $5,560 per birth. For women with high-risk pregnancies, intensive maternity care saves $1.37 for every $1 invested in maternity care.\n##### (b) Purpose\nThe purpose of this Act is to protect the health of women and newborns by ensuring that all women eligible for coverage through the Exchanges established under title I of the Patient Protection and Affordable Care Act ( Public Law 111\u2013148 ) and women eligible for other individual or group health plan coverage can access affordable health coverage during their pregnancy.\n#### 3. Providing for a special enrollment period for pregnant individuals\n##### (a) Public Health Service Act\nSection 2702(b)(2) of the Public Health Service Act ( 42 U.S.C. 300gg\u20131(b)(2) ) is amended by inserting , including a special enrollment period for pregnant individuals, beginning on the date on which the pregnancy is reported to the health insurance issuer before the period at the end.\n##### (b) Patient Protection and Affordable Care Act\nSection 1311(c)(6) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(c)(6) ) is amended\u2014\n**(1)**\nin subparagraph (C), by striking and at the end;\n**(2)**\nby redesignating subparagraph (D) as subparagraph (E); and\n**(3)**\nby inserting after subparagraph (C) the following:\n(D) a special enrollment period for pregnant individuals, beginning on the date on which the pregnancy is reported to the Exchange; and .\n##### (c) Internal Revenue Code\nSection 9801(f) of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(4) For pregnant individuals (A) In general A group health plan shall permit an employee who is eligible, but not enrolled, for coverage under the terms of the plan (or a dependent of such an employee if the dependent is eligible, but not enrolled, for coverage under such terms) to enroll for coverage under the terms of the plan upon pregnancy, with the special enrollment period beginning on the date on which the pregnancy is reported to the group health plan or the pregnancy is confirmed by a health care provider. (B) Regulations The Secretary shall promulgate regulations with respect to the special enrollment period under subparagraph (A), including establishing a time period for pregnant individuals to enroll in coverage and effective date of such coverage. .\n##### (d) ERISA\nSection 701(f) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1181(f) ) is amended by adding at the end the following:\n(4) For pregnant individuals (A) In general A group health plan or health insurance issuer in connection with a group health plan shall permit an employee who is eligible, but not enrolled, for coverage under the terms of the plan (or a dependent of such an employee if the dependent is eligible, but not enrolled, for coverage under such terms) to enroll for coverage under the terms of the plan upon pregnancy, with the special enrollment period beginning on the date on which the pregnancy is reported to the group health plan or health insurance issuer or the pregnancy is confirmed by a health care provider. (B) Regulations The Secretary shall promulgate regulations with respect to the special enrollment period under subparagraph (A), including establishing a time period for pregnant individuals to enroll in coverage and effective date of such coverage. .\n##### (e) Effective date\nThe amendments made by this section shall apply with respect to plan years beginning on or after January 1, 2027.\n#### 4. Coverage of maternity care for dependent children\n##### (a) Public Health Service Act\nSection 2799A\u20137 of the Public Health Service Act ( 42 U.S.C. 300gg\u2013117 ) is amended by adding at the end the following:\n(d) Coverage of maternity care A group health plan, or health insurance issuer offering group or individual health insurance coverage, that provides coverage for dependents shall ensure that such plan or coverage includes coverage for maternity care associated with pregnancy, childbirth, and postpartum care for all participants, beneficiaries, and enrollees, including dependents, including coverage of labor and delivery. Such coverage shall be provided to all pregnant dependents regardless of age. .\n##### (b) ERISA\nSection 722 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185k ) is amended by adding at the end the following:\n(d) Coverage of maternity care A group health plan, or health insurance issuer offering group health insurance coverage, that provides coverage for dependents shall ensure that such plan or coverage includes coverage for maternity care associated with pregnancy, childbirth, and postpartum care for all participants, beneficiaries, and enrollees, including dependents, including coverage of labor and delivery. Such coverage shall be provided to all pregnant dependents regardless of age. .\n##### (c) Internal Revenue Code\nSection 9822 of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(d) Coverage of maternity care A group health plan that provides coverage for dependents shall ensure that such plan includes coverage for maternity care associated with pregnancy, childbirth, and postpartum care for all participants and beneficiaries, including dependents, including coverage of labor and delivery. Such coverage shall be provided to all pregnant dependents regardless of age. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to plan years beginning on or after January 1, 2027.\n#### 5. Federal employee health benefit plans\n##### (a) Coverage of pregnancy\n**(1) In general**\nThe Director of the Office of Personnel Management shall issue such regulations as are necessary to ensure that pregnancy is considered a change in family status and a qualifying life event for an individual who is eligible to enroll, but is not enrolled, in a health benefit plan under chapter 89 of title 5, United States Code.\n**(2) Effective date**\nThe requirement in paragraph (1) shall apply with respect to any contract entered into under section 8902 of title 5, United States Code, on or after the date that is 1 year after the date of enactment of this Act.\n##### (b) Designating certain FEHBP-Related services as excepted services under the Anti-Deficiency Act\n**(1) In general**\nSection 8905 of title 5, United States Code, is amended by adding at the end the following:\n(j) Any services by an officer or employee under this chapter relating to enrolling individuals in a health benefits plan under this chapter, or changing the enrollment of an individual already so enrolled due to an event described in section 5(a)(1) of the Healthy MOM Act, shall be deemed, for purposes of section 1342 of title 31, services for emergencies involving the safety of human life or the protection of property. .\n**(2) Application**\nThe amendment made by paragraph (1) shall apply to any lapse in appropriations beginning on or after the date of enactment of this Act.\n#### 6. Continuation of Medicaid income eligibility standard for pregnant individuals and infants\nSection 1902(l)(2)(A) of the Social Security Act ( 42 U.S.C. 1396a(l)(2)(A) ) is amended\u2014\n**(1)**\nin clause (i), by striking and not more than 185 percent ;\n**(2)**\nin clause (ii)\u2014\n**(A)**\nin subclause (I), by striking and after the comma;\n**(B)**\nin subclause (II), by striking the period at the end and inserting , and ; and\n**(C)**\nby adding at the end the following:\n(III) January 1, 2027, is the percentage provided under clause (v). ; and\n**(3)**\nby adding at the end the following new clause:\n(v) The percentage provided under clause (ii) for medical assistance provided on or after January 1, 2027, with respect to individuals described in subparagraph (A) or (B) of paragraph (1) shall not be less than\u2014 (I) the percentage specified for such individuals by the State in an amendment to the State plan under this title (whether approved or not) as of January 1, 2025; or (II) if no such percentage is specified as of January 1, 2025, the percentage established for such individuals under the State's authorizing legislation or provided for under the State's appropriations as of that date. .\n#### 7. Requiring and making permanent 12-month continuous coverage for pregnant and postpartum individuals under Medicaid and CHIP\n##### (a) Medicaid\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (88)(B)(iii), by striking and at the end;\n**(B)**\nin paragraph (89), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (89) the following new paragraph:\n(90) provide that the State plan is in compliance with subsection (e)(16). ; and\n**(2)**\nin subsection (e)(16)\u2014\n**(A)**\nin subparagraph (A), by striking At the option of the State, the State plan (or waiver of such State plan) may provide, and inserting A State plan (or waiver of such State plan) shall provide ;\n**(B)**\nin subparagraph (B), in the matter preceding clause (i), by striking by a State making an election under this paragraph and inserting under a State plan (or a waiver of such State plan) ; and\n**(C)**\nby striking subparagraph (C).\n##### (b) CHIP\n**(1) In general**\nSection 2107(e)(1)(K) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1)(K) ) is amended to read as follows:\n(K) Paragraphs (5) and (16) of section 1902(e) (relating to the requirement to provide medical assistance under the State plan or waiver consisting of full benefits during pregnancy and throughout the 12-month postpartum period under title XIX) such that the provision of assistance under the State child health plan or waiver for targeted low-income children or targeted low-income pregnant women during pregnancy and the 12-month postpartum period shall be required and shall include coverage of all items or services provided to a targeted low-income child or targeted low-income pregnant woman (as applicable) under the State child health plan or waiver. .\n**(2) Conforming**\nSection 2112(d)(2)(A) of the Social Security Act ( 42 U.S.C. 1397ll(d)(2)(A) ) is amended by striking the month in which the 60-day period and all that follows through pursuant to section 2107(e)(1), .\n##### (c) Effective date\n**(1) In general**\nSubject to paragraph (2), the amendments made by this section shall apply with respect to services furnished on or after the date that is 1 year after the date of the enactment of this Act.\n**(2) Exception for State legislation**\nIn the case of a State plan under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) or a State child health plan under title XXI of such Act ( 42 U.S.C. 1397ee et seq. ) that the Secretary of Health and Human Services determines requires State legislation in order for the plan to meet any requirement imposed by amendments made by this section, the respective plan shall not be regarded as failing to comply with the requirements of such title solely on the basis of its failure to meet such an additional requirement before the first day of the first calendar quarter beginning after the close of the first regular session of the State legislature that begins after the date of enactment of this Act. For purposes of the previous sentence, in the case of a State that has a 2-year legislative session, each year of the session shall be considered to be a separate regular session of the State legislature.\n#### 8. Relationship to other laws\nNothing in this Act (or an amendment made by this Act) shall be construed to invalidate or limit the remedies, rights, and procedures of any Federal law or the law of any State or political subdivision of any State or jurisdiction that provides greater or equal protection for enrollees in a group health plan or group or individual health insurance offered by a health insurance issuer.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, Education and Workforce, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6242",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Healthy MOM Act",
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
        "name": "Health",
        "updateDate": "2026-01-07T16:52:16Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3274is.xml"
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
      "title": "Healthy MOM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-20T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy MOM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy Maternity and Obstetric Medicine Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to provide for a special enrollment period for pregnant women, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T06:18:33Z"
    }
  ]
}
```
