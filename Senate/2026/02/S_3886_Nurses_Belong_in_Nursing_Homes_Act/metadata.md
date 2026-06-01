# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3886
- Title: Nurses Belong in Nursing Homes Act
- Congress: 119
- Bill type: S
- Bill number: 3886
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-03-03T16:06:04Z
- Update date including text: 2026-03-03T16:06:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3886",
    "number": "3886",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Nurses Belong in Nursing Homes Act",
    "type": "S",
    "updateDate": "2026-03-03T16:06:04Z",
    "updateDateIncludingText": "2026-03-03T16:06:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T20:12:35Z",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NJ"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NJ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NM"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3886is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3886\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Wyden (for himself, Mr. Kim , Mr. Booker , Ms. Warren , Mr. Luj\u00e1n , Mr. Murphy , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo establish total nurse staffing hours per resident day, to require 24-hour use of registered professional nurses in nursing homes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nurses Belong in Nursing Homes Act .\n#### 2. Nurse staffing requirements\n##### (a) Establishing total nurse staffing hours per resident day; requiring 24-Hour use of registered professional nurses in nursing homes; removal of waiver authority\n**(1) Medicare**\nSection 1819(b)(4) of the Social Security Act ( 42 U.S.C. 1395i\u20133(b)(4) ) is amended by striking subparagraph (C) and inserting the following:\n(C) Required nursing care (i) In general A skilled nursing facility must provide\u2014 (I) 24-hour licensed nursing services which are sufficient to meet the nursing needs of its residents; (II) not later than the date described in clause (iii), a minimum staffing requirement of at least 3.48 hours per resident day (or the number of hours per resident day recommended in the report most recently submitted by the Secretary under section 1128L(b)(2), provided that such number is at least 3.48 hours per resident day) of nursing care provided by a combination of a registered professional nurse, licensed practical nurse (or licensed vocational nurse), or certified nursing assistant that\u2014 (aa) provides direct care services to residents in a skilled nursing facility; and (bb) reflects an appropriate combination of competencies and skills that is sufficient to ensure the safety of each resident in the facility; and (III) the services of a registered professional nurse, such that such services are furnished\u2014 (aa) before the date described in clause (iii), at least 8 consecutive hours a day, 7 days a week; and (bb) on or after such date, 24 hours a day, 7 days a week. (ii) Definition of hours per resident day In this subparagraph, the term hours per resident day means the total number of hours worked by each type of staff described in clause (i)(II) divided by the total number of residents, as calculated by the Administrator of the Centers for Medicare & Medicaid Services. (iii) Date described For purposes of subclauses (II) and (III) of clause (i), the date described in this clause is the date that is 180 days after the date of enactment of the Nurses Belong in Nursing Homes Act . .\n**(2) Medicaid**\nSection 1919(b)(4) of the Social Security Act ( 42 U.S.C. 1396r(b)(4) ) is amended by striking subparagraph (C) and inserting the following:\n(C) Required nursing care (i) In general A nursing facility must provide\u2014 (I) 24-hour licensed nursing services which are sufficient to meet the nursing needs of its residents; (II) not later than the date described in section 1819(b)(4)(C)(iii), a minimum staffing requirement of at least 3.48 hours per resident day (or the number of hours per resident day recommended in the report most recently submitted by the Secretary under section 1128L(b)(2), provided that such number is at least 3.48 hours per resident day) of nursing care provided by a combination of a registered professional nurse, licensed practical nurse (or licensed vocational nurse), or certified nursing assistant that\u2014 (aa) provides direct care services to residents in a nursing facility; and (bb) reflects an appropriate combination of competencies and skills that is sufficient to ensure the safety of each resident in the facility; and (III) the services of a registered professional nurse, such that such services are furnished\u2014 (aa) before the date described in section 1819(b)(4)(C)(iii), at least 8 consecutive hours a day, 7 days a week; and (bb) on or after such date, 24 hours a day, 7 days a week. (ii) Definition of hours per resident day In this subparagraph, the term hours per resident day has the meaning given such term in section 1819(b)(4)(C)(ii). .\n##### (b) Study\nTitle XI of the Social Security Act ( 42 U.S.C. 1301 et seq. ) is amended by inserting after section 1128K the following new section:\n1128L. Study and reports recommending minimum staffing requirements for skilled nursing facilities and nursing facilities; promulgation of regulations (a) Study (1) In general Not later than 2 years after the date of enactment of this section, and not less frequently than once every 4 years thereafter, the Secretary shall direct the Assistant Secretary for Planning and Evaluation, the Comptroller General, or the Medicare Payment Advisory Commission, in consultation with the Medicaid and CHIP Payment and Access Commission (in this section referred to as the designated entity ), to complete a study analyzing nurse staffing requirements at skilled nursing facilities (as defined in section 1819(a)) and nursing facilities (as defined in section 1919(a)) to provide care to individuals seeking their services. (2) Contents With respect to each study required under paragraph (1), the designated entity shall\u2014 (A) consult with\u2014 (i) residents, family members of residents, or authorized representatives of residents; (ii) registered professional nurses, licensed practical nurses (or licensed vocational nurses), certified nursing assistants, and other categories of direct care professionals (as determined by the Secretary) who work at such skilled nursing facilities or nursing facilities; (iii) collective bargaining units or unions that represent direct care workers or direct care professionals who work at such skilled nursing facilities and nursing facilities; (iv) operators of nursing facilities and skilled nursing facilities; (v) researchers with expertise in the nursing home and long-term care workforce, including the disclosure of funding sources for previously conducted research and conflicts of interest; and (vi) long-term care ombudsmen; and (B) address the following: (i) Whether the minimum staffing requirements established in sections 1819(b)(4)(C)(i)(II) and 1919(b)(4)(C)(i)(II) should be maintained or increased (but in no event decreased below a minimum staffing requirement of at least 3.48 hours per resident day), based on the severity of the health conditions, complexity of health care needs, or other measures of patient acuity of residents at such skilled nursing facilities and nursing facilities, and, if so, how such minimum staffing requirements shall be increased. (ii) Whether other minimum hours per resident day minimum staffing requirements should be established for other categories of direct care professionals or direct care workers in addition to the requirements established in sections 1819(b)(4)(C)(i)(II) and 1919(b)(4)(C)(i)(II). (iii) A review of staffing, safety, and quality data, as well as staffing requirement exception data, to assess the adequacy of existing staffing practices in such nursing facilities and skilled nursing facilities. (b) Reports (1) To the Secretary The designated entity shall submit to the Secretary a report on the results of the study conducted under subsection (a), together with recommendations for such legislation and administrative action as the designated entity determines appropriate. (2) To Congress Not later than 180 days after receiving each report under paragraph (1), the Secretary shall submit to Congress a report on\u2014 (A) the findings and recommendations included in such report; and (B) any plan to implement such recommendations, including a justification for any recommendations the Secretary determines should not be implemented. (c) Regulations (1) In general Not later than 1 year after the Secretary submits an initial report under subsection (b)(2), the Secretary shall\u2014 (A) specify through regulations, consistent with such report, a minimum staffing requirement for nursing staff for skilled nursing facilities (as defined in section 1819(a)) and nursing facilities (as defined in section 1919(a)); and (B) require such skilled nursing facilities and such nursing facilities to comply with such staffing requirements, including by providing the minimum staffing sufficient to meet the needs of each resident in any such facility. (2) Update Not later than 1 year after the Secretary submits each subsequent report under subsection (b)(2), the Secretary shall, consistent with each such report, update the regulations described in paragraph (1)(A) as necessary. (d) Funding The Secretary shall provide for the transfer, from the Federal Hospital Insurance Trust Fund under section 1817 to the Centers for Medicare & Medicaid Services Program Management Account, of $50,000,000 for fiscal year 2027 for purposes of carrying out this section. Amounts transferred pursuant to the previous sentence shall remain available until expended. .\n##### (c) Rule of construction\nThe moratorium imposed under section 71111 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ) (relating to implementation of certain staffing standards for long-term care facilities under the Medicare and Medicaid programs) shall not be construed to apply to the amendments made by this section.\n#### 3. Permanent funding for the Survey and Certification Program for nursing homes and other health care entities\nPart A of Title XI of the Social Security Act ( 42 U.S.C. 1301 et seq. ) is amended by inserting after section 1150C the following new section:\n1150D. Funding for the Survey and Certification Program There is appropriated to the Secretary, out of the Federal Hospital Insurance Trust Fund under section 1817 and the Federal Supplementary Medical Insurance Trust Fund under section 1841 (in such proportions as the Secretary determines to be appropriate), $800,000,000 for fiscal year 2027 and each subsequent fiscal year for the purpose of conducting the Secretary's Survey and Certification Program, including under section 1864. Amounts appropriated under the preceding sentence shall remain available until expended. .\n#### 4. Investing in the nursing home workforce\n##### (a) Medicare\nSection 1819(h) of the Social Security Act ( 42 U.S.C. 1395i\u20133(h) ) is amended\u2014\n**(1)**\nin paragraph (2)(B)(ii)(IV)(ff), by inserting , provided that not less than half of such amounts are provided to the State in which the facility is located for the purposes described in paragraph (7), after collected may ; and\n**(2)**\nby adding at the end the following new paragraph:\n(7) Use of civil money penalty amounts to support the skilled nursing facility workforce (A) In general Subject to subparagraph (B), a State shall use the amounts provided to such State pursuant to paragraph (2)(B)(ii)(IV)(ff) for the fiscal year in which such amounts are provided for the following purposes: (i) Providing grants to entities such as educational institutions, advocacy organizations for skilled nursing facility residents, senior citizens, or individuals with disabilities, and unions that represent the skilled nursing facility workforce to support projects that use community-driven approaches to recruit, educate, and train individuals to expand the skilled nursing facility workforce. (ii) The funding of projects that develop new career pathway programs for the skilled nursing facility workforce. (iii) The repayment of student loans for qualified skilled nursing facility providers (as defined in subparagraph (C)) or the payment of tuition for such providers who commit to serving in a skilled nursing facility or a nursing facility (as defined in section 1919(a)) for not less than 3 years within a 10-year period. (B) Prohibitions on use of funds (i) Prohibition on providing funds to entities related to facilities A State may not provide any amounts provided to such State pursuant to paragraph (2)(B)(ii)(IV)(ff) to an entity that has a related party relationship with a nursing facility or skilled nursing facility in such State. (ii) Prohibition on using funds for reimbursement of costs incurred in completing nurse aide training and competency evaluation programs and nurse aide competency evaluation programs A State may not use any amounts provided to such State pursuant to paragraph (2)(B)(ii)(IV)(ff) to\u2014 (I) reimburse costs incurred in completing a nurse aide training and competency evaluation program or a nurse aide competency evaluation program under subsection (f)(2)(A); or (II) supplant the payment of such costs under such subsection. (C) Definitions In this paragraph: (i) Qualified skilled nursing facility provider The term qualified skilled nursing facility provider means\u2014 (I) a geriatrician or other physician, nurse practitioner, physician assistant, or other practitioner who provides services in a skilled nursing facility or nursing facility; or (II) a registered professional nurse, a licensed practical nurse (or a licensed vocational nurse), or a certified nursing assistant who provides direct care services to residents in a skilled nursing facility or nursing facility, as determined by the Secretary. (ii) Related party The term related party means an entity that, to a significant extent is associated or affiliated with, or has control of, or is controlled by, a nursing facility or skilled nursing facility. (D) Annual reporting (i) Report from States Not later than 1 year after the date of enactment of this paragraph, and annually thereafter, each State that receives amounts pursuant to paragraph (2)(B)(ii)(IV)(ff) shall submit to the Secretary a report describing\u2014 (I) how amounts received in the previous fiscal year were allocated; (II) the mechanisms to ensure such amounts benefit the development of the skilled nursing facility workforce; (III) how such amounts will impact measurable outcomes for residents of skilled nursing facilities and nursing facilities, such as staff vacancy rates, turnover rates, median hourly wages, staffing hours per resident, and resident quality outcomes; and (IV) how such State is ensuring compliance with subparagraph (B). (ii) Report to Congress Not later than 180 days after the Secretary receives the annual reports from States under clause (i), the Secretary shall submit to Congress a report describing the information contained in such reports. .\n##### (b) Medicaid\nSection 1919(h) of the Social Security Act ( 42 U.S.C. 1396r(h) ) is amended\u2014\n**(1)**\nin paragraph (2)(A)(ii)\u2014\n**(A)**\nin the second sentence, by striking Funds collected and inserting Subject to the last sentence of this clause, funds collected ; and\n**(B)**\nby inserting the following sentence at the end: Not less than half of the funds collected pursuant to this clause shall be used for the purposes described in paragraph (10). ;\n**(2)**\nin paragraph (3)(C)(ii)(IV)(ff), by inserting , provided that not less than half of such amounts are provided to the State in which the facility is located for the purposes described in paragraph (10), ; and\n**(3)**\nby adding at the end the following new paragraph:\n(10) Use of civil money penalty amounts to support the nursing facility workforce (A) In general Subject to subparagraph (B), a State shall use not less than half of the funds collected under paragraph (2)(A)(ii) and the amounts provided to such State pursuant to paragraph (3)(C)(ii)(IV)(ff) (collectively referred to in this paragraph as civil money penalty amounts ) for the fiscal year in which such amounts are collected or provided for the following activities: (i) Providing grants to entities such as educational institutions, advocacy organizations for nursing facility residents, senior citizens, or individuals with disabilities, and unions that represent the nursing facility workforce to support projects that use community-driven approaches to recruit, educate, and train individuals to expand the nursing facility workforce. (ii) The funding of projects that develop new career pathway programs for the nursing facility workforce. (iii) The repayment of student loans for qualified nursing facility providers (as defined in subparagraph (C)) or the payment of tuition for such providers who commit to serving in a skilled nursing facility (as defined in section 1819(a)) or a nursing facility for not less than 3 years within a 10-year period. (B) Prohibition on use of funds (i) Prohibition on providing funds to entities related to facilities A State may not provide any civil money penalty amounts to an entity that has a related party relationship with a nursing facility or skilled nursing facility in such State. (ii) Prohibition on using funds for reimbursement of costs incurred in completing nurse aide training and competency programs and nurse aide competency evaluation programs A State may not use any civil money penalty amounts to\u2014 (I) reimburse costs incurred in completing a nurse aid training and competency evaluation program or a nurse aide competency evaluation program under subsection (f)(2)(A); or (II) supplant the payment of such costs under such subsection. (C) Definitions In this paragraph: (i) Qualified nursing facility provider The term qualified nursing facility provider means\u2014 (I) a geriatrician or other physician, nurse practitioner, physician assistant, or other practitioner who provides services in a skilled nursing facility or nursing facility; or (II) a registered professional nurse, licensed practical nurse (or a licensed vocational nurse), or certified nursing assistant who provides direct care services to residents in a skilled nursing facility or nursing facility, as determined by the Secretary. (ii) Related party The term related party means an entity that, to a significant extent is associated or affiliated with, or has control of, or is controlled by, a nursing facility or skilled nursing facility. (D) Annual reporting (i) Report from States Not later than 1 year after the date of enactment of this paragraph, and annually thereafter, each State that receives any civil money penalty amounts shall submit to the Secretary a report describing\u2014 (I) how amounts received in the previous fiscal year were allocated; (II) the mechanisms to ensure such amounts benefit the development of the nursing facility workforce; (III) how such amounts will impact measurable outcomes for residents of skilled nursing facilities and nursing facilities, such as staff vacancy rates, turnover rates, median hourly wages, staffing hours per resident, and resident quality outcomes; and (IV) how such State is ensuring compliance with subparagraph (B). (ii) Report to Congress Not later than 180 days after the Secretary receives the annual reports from States under clause (i), the Secretary shall submit to Congress a report describing the information contained in such report. .\n#### 5. Codification of regulations regarding requirements for long-term services and supports and payment transparency reporting\nSections 438.72 and 442.43 of title 42, Code of Federal Regulations (as in effect on May 10, 2024), shall have the force and effect of law.",
      "versionDate": "2026-02-12",
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
        "name": "Health",
        "updateDate": "2026-03-03T16:06:04Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3886is.xml"
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
      "title": "Nurses Belong in Nursing Homes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-28T06:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nurses Belong in Nursing Homes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-28T06:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish total nurse staffing hours per resident day, to require 24-hour use of registered professional nurses in nursing homes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-28T06:48:22Z"
    }
  ]
}
```
