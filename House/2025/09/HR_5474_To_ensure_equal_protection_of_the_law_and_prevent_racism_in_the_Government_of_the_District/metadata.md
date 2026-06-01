# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5474?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5474
- Title: No DEI in DC Act
- Congress: 119
- Bill type: HR
- Bill number: 5474
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-02-24T09:05:26Z
- Update date including text: 2026-02-24T09:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5474",
    "number": "5474",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "No DEI in DC Act",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:26Z",
    "updateDateIncludingText": "2026-02-24T09:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AL"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5474ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5474\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Ms. Mace (for herself, Ms. Boebert , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo ensure equal protection of the law and prevent racism in the Government of the District of Columbia by prohibiting the Government of the District of Columbia from engaging in certain diversity, equity, or inclusion practices or conducting racial equity training, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Diversity, Equity, and Inclusion in the District of Columbia Act or the No DEI in DC Act .\n#### 2. Prohibition of diversity, equity, or inclusion practices\n##### (a) In general\nThe Government of the District of Columbia may not engage in any prohibited diversity, equity, or inclusion practice.\n##### (b) Funding prohibition\nNone of the funds available for obligation or expenditure by the District of Columbia government under any authority may be used to fund, directly or indirectly, any prohibited diversity, equity, or inclusion practice, or any entity which engages in any prohibited diversity, equity, or inclusion practice.\n##### (c) Definition\nIn this section, the term prohibited diversity, equity, or inclusion practice means\u2014\n**(1)**\ndiscriminating for or against any person on the basis of race, color, ethnicity, religion, biological sex, or national origin;\n**(2)**\nrequiring as a condition of employment, as a condition for promotion or advancement, or as a condition for speaking, making a presentation, or submitting written materials, that an employee undergo training, education, or coursework, or other pedagogy, that asserts that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged;\n**(3)**\nrequiring as a condition of employment, as a condition for promotion or advancement, or as a condition for speaking, making a presentation, or submitting written materials, the signing of or assent to a statement, code of conduct, work program, or plan, or similar device that requires assent by the employee that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged;\n**(4)**\ntaking or failing to take, or threatening to take or fail to take, any personnel action against any employee or applicant for employment because of the failure of the employee or applicant to\u2014\n**(A)**\ncomplete training with respect to diversity, equity, or inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy;\n**(B)**\ncomplete training that asserts or requires trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged;\n**(C)**\nsign or assent to (which may be by executing or acknowledging) a statement, code of conduct, work program, plan, or similar device with respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy;\n**(D)**\nsign or assent to (which may be by executing or acknowledging) a statement, code of conduct, work program, plan, or similar device that asserts or requires assent by the employee or applicant that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged;\n**(E)**\ntake any other action that would require the treatment of any individual advantageously or disadvantageously on the basis of that individual\u2019s race, color, ethnicity, religion, biological sex, or national origin; or\n**(F)**\nlimit, segregate, or classify employees or applicants for employment in any way that would deprive or tend to deprive any individual of an employment opportunity, or otherwise adversely affect the status of the individual as an employee, because of the race, color, ethnicity, religion, biological sex, or national origin of the individual;\n**(5)**\nmaintaining an office, commission, bureau, division, or other organization to further promote or enforce any activity described in paragraphs (1) through (4); or\n**(6)**\nretaining or employing a consultant or advisor to further promote or enforce any activity described in paragraphs (1) through (4).\n#### 3. Prohibition on DEI training\n##### (a) Prohibition on implementing DEI training\nNo training program or plan may be developed, implemented, distributed, published, established, or purchased by the Government of the District of Columbia\u2014\n**(1)**\nwith respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; or\n**(2)**\nthat asserts or requires the trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged.\n##### (b) Prohibition on requiring DEI training\nNo employee of the Government of the District of Columbia may be required to complete training under a program or plan established under this section\u2014\n**(1)**\nwith respect to diversity, equity, and inclusion, critical theory (relating to race, gender, or otherwise), intersectionality, sexual orientation or gender identity, or any substantially similar theory or policy; or\n**(2)**\nthat asserts or requires the trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged.\n##### (c) Prohibition on funding DEI training\nNone of the funds available for obligation or expenditure by the District of Columbia government under any authority may be used for the purposes of developing, implementing, distributing, publishing or purchasing a training course\u2014\n**(1)**\nrelating to\u2014\n**(A)**\ndiversity, equity, inclusion, and accessibility;\n**(B)**\na critical theory (relating to race, gender, or otherwise); or\n**(C)**\nintersectionality, sexual orientation, or gender identity; or\n**(2)**\nthat asserts or requires trainees to assert that a particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior, inferior, oppressive, oppressed, privileged, or unprivileged.\n#### 4. Conforming amendments to District of Columbia law\n##### (a) Repeal of laws relating to management of District of Columbia government employee pensions\n**(1) Definition of diverse emerging fund manager**\nSection 102(2B) of the Police Officers, Fire Fighters and Teachers Retirement Benefit Replacement Plan Act of 1998 (sec. 1\u2013901.02(2B), D.C. Official Code) is hereby repealed.\n**(2) Diverse emerging fund manager reporting requirement for District of Columbia Retirement Board**\nSection 142(b)(15) of such Act (sec. 1\u2013909.02(b)(15), D.C. Official Code) is hereby repealed.\n##### (b) Repeal of laws relating to organization and administration of District of Columbia government\n**(1) Small and local business enterprise development and assistance**\n**(A) Definitions**\nSection 2302 of the Small, Local, and Disadvantaged Business Enterprise Development and Assistance Act of 2005 (sec. 2\u2013218.02, D.C. Official Code) is amended by striking paragraphs (1F), (5), (5A), (7), and (8A).\n**(B) Disadvantaged business enterprises**\nSection 2333 of such Act (sec. 2\u2013218.33, D.C. Official Code) is hereby repealed.\n**(C) Equity impact enterprises**\nPart D\u2013i of such Act (sec. 2\u2013218.77, D.C. Official Code) is hereby repealed.\n**(2) Diversity requirement in solicitation of construction contracts**\nSection 606(b) of the Procurement Practices Reform Act of 2010 (sec. 2\u2013356.06(b), D.C. Official Code) is amended\u2014\n**(A)**\nby adding and at the end of paragraph (5);\n**(B)**\nin paragraph (6), by striking and Equity Impact Enterprises; and and inserting a period; and\n**(C)**\nby striking paragraph (7).\n**(3) Latino Community Office**\nThe District of Columbia Latino Community Development Act (sec. 2\u20131301 et seq., D.C. Official Code) is hereby repealed.\n**(4) Office on Asian and Pacific Islander Affairs**\nThe Office on Asian and Pacific Islander Affairs Establishment Act of 2001 (sec. 2\u20131371 et seq., D.C. Official Code) is hereby repealed.\n**(5) Office of Gay, Lesbian, Bisexual, Transgender, and Questioning Affairs**\nThe Office of Gay, Lesbian, Bisexual and Transgender Affairs Act of 2005 (sec. 2\u20131381 et seq., D.C. Official Code) is hereby repealed.\n**(6) Office and Commission on African-American Affairs**\nThe Office and Commission on African Affairs Act of 2006 (sec. 2\u20131391 et seq., D.C. Official Code) is hereby repealed.\n**(7) Racial equity training in Office of Human Rights**\nSection 206b of the Office of Human Rights Establishment Act of 1999 (section 2\u20131411.05b, D.C. Official Code) is hereby repealed.\n**(8) Office of Racial Equity and Commission on Racial Equality, Social Justice and Economic Inclusion**\nThe Racial Equity Achieves Results (REACH) Amendment Act of 2020 (sec. 2\u20131471.01 et seq., D.C. Official Code) is hereby repealed.\n##### (c) Laws relating to District of Columbia boards and commissions\n**(1) Commission for Women**\nThe District of Columbia Commission for Women Act of 1978 (sec. 3\u2013701 et seq., D.C. Official Code) is hereby repealed.\n**(2) Focus on LGBTQ patients in continuing education requirements for licenses issued by health occupations boards**\nSection 510(b) of the Health Occupations Revision Act of 1985 (sec. 3\u20131205.10(b), D.C. Official Code) is amended by striking paragraph (5).\n**(3) Commission on Reparations**\nThe Insurance Database Amendment Act of 2024 (sec. 3\u20131461 et seq., D.C. Official Code) is hereby repealed.\n##### (d) Laws relating to public care systems\n**(1) Priority for grants made by Office of Victim Services and Justice Grants**\nSection 3022(b)(2) of the Office of Victim Services and Justice Grants Transparency Act of 2022 (sec. 4\u2013571.01(b)(2), D.C. Official Code) is amended\u2014\n**(A)**\nin subparagraph (B), by striking clause (ii); and\n**(B)**\nin subparagraph (D), by striking clause (ii).\n**(2) Homeless Services Reform Act of 2005**\n**(A) Service needs of LGBTQ youth**\nSection 5 of such Act (sec. 4\u2013752.02, D.C. Official Code) is amended\u2014\n**(i)**\nin subsection (b)(1), by striking and the number of LGBTQ homeless youth in the District ; and\n**(ii)**\nby striking subsection (b\u20131).\n**(B) Continuum of care for LGBTQ youth**\nSection 7(b) of such Act (sec. 4\u2013753.01(b), D.C. Official Code) is amended by striking paragraph (6).\n**(C) Shelter intake policies for LGBTQ individuals**\nSection 8(c) of such Act (sec. 4\u2013753.02(c), D.C. Official Code) is amended\u2014\n**(i)**\nby striking paragraph (1B); and\n**(ii)**\nin paragraph (4), by striking age, and whether an individual is an LGBTQ homeless youth, and inserting and age, .\n**(D) Training standards relating to LGBTQ youth**\nSection 12a of such Act (sec. 4\u2013754.21a, D.C. Official Code) is amended\u2014\n**(i)**\nin the matter preceding paragraph (1), by striking with regard to the LGBTQ population ; and\n**(ii)**\nby striking paragraphs (2) through (4).\n**(E) Standards for providers of services to LGBTQ youth**\nSection 16a of such Act (sec. 4\u2013754.25a, D.C. Official Code) is hereby repealed.\n**(F) Transfer of clients**\nSection 20(a) of such Act (sec. 4\u2013754.34(a), D.C. Official Code) is amended by striking paragraph (3).\n**(G) Staff of Shelter Monitoring Units**\nSection 27d of the Homeless Services Reform Act of 2005 (sec. 4\u2013754.54, D.C. Official Code) is amended\u2014\n**(i)**\nin subsection (b), by striking , and in sensitivity to the diversity of persons who are homeless in the District ; and\n**(ii)**\nby striking subsection (c).\n**(H) Minimum number of beds for LGBTQ youth**\nSection 28 of such Act (sec. 4\u2013755.01, D.C. Official Code) is amended by striking subsection (c).\n**(3) Board of Directors of Child Abuse and Neglect Prevention Children\u2019s Trust Fund**\nSection 4(a) of the Child Abuse and Neglect Prevention Children\u2019s Trust Fund Act of 1993 (sec. 4\u20131341.03(a), D.C. Official Code) is amended by striking and shall reflect a diversity of gender and ethnicity .\n##### (e) Laws relating to police, firefighters, medical examiner, and forensic services\n**(1) Community representatives on Police Officers Standards and Training Board**\nSection 204(b)(9)(D) of the Omnibus Police Reform Amendment Act of 2000 (sec. 5\u2013107.03(b)(9)(D), D.C. Official Code) is amended by striking or LGBTQ social services, policy, or advocacy .\n**(2) Preventing white supremacy in policing**\nSubtitle R of title I of the Comprehensive Policing and Justice Reform Amendment Act of 2022 (sec. 5\u2013123.31 et seq., D.C. Official Code), is hereby repealed.\n##### (f) Laws relating to housing and building restrictions and regulations\n**(1) Local rent supplement program**\nSection 26c(f) of the District of Columbia Housing Authority Act of 1999 (sec. 6\u2013228(f), D.C. Official Code) is amended by striking paragraph (2).\n**(2) Community development objectives**\nSection 2(c)(6) of the District of Columbia Community Development Act of 1975 (sec. 6\u20131001(c)(6), D.C. Official Code) is amended by striking diversity and .\n##### (g) Laws relating to human health care and safety\n**(1) Treatment of LGBTQ seniors under Older Americans Act**\nSection 309 of the District of Columbia Act on the Aging (sec. 7\u2013503.09, D.C. Official Code) is hereby repealed.\n**(2) Report on health of LGBTQ community**\nSection 4902a of the Department of Health Functions Clarification Act of 2001 (sec. 7\u2013731.01, D.C. Official Code) is amended\u2014\n**(A)**\nby striking paragraph (3) of subsection (a);\n**(B)**\nby striking subsection (b); and\n**(C)**\nby striking paragraph (2) of subsection (c).\n**(3) Commission on Health Equity**\nThe Commission on Health Equity Amendment Act of 2016 (sec. 7\u2013756.01 et seq., D. C. Official Code) is hereby repealed.\n**(4) Perinatal Mental Health Task Force**\nSection 5042(a)(9) of the Perinatal Mental Health Task Force Establishment Act of 2022 (sec. 7\u20131234.02(a)(9), D.C. Official Code) is amended by striking , encompassing the ability to serve the diversity of perinatal experiences of unique populations, including Black birthing people, Hispanic birthing people, pregnant and postpartum people of color, perinatal immigrant populations, adolescents who are pregnant and parenting, LGBTQIA+ birthing people, child welfare involved birthing people, disabled, justice involved, incarcerated, and homeless birthing people, and their non-birthing partners .\n**(5) Certification of drug treatment providers**\nSection 10 of the Choice in Drug Treatment Act of 2000 (sec. 7\u20133009, D.C. Official Code) is amended by striking subsection (c).\n##### (h) Greenhouse gas emission reductions\nSection 109d of the District Department of the Environment Establishment Act of 2005 (sec. 8\u2013151.09d, D.C. Official Code) is amended\u2014\n**(1)**\nby striking subsection (c); and\n**(2)**\nby striking paragraph (3) of subsection (d).\n##### (i) Commemoration Task Force\nThe Commemoration Task Force Act of 2020 (sec. 9\u2013251 et seq., D.C. Official Code) is hereby repealed.\n##### (j) Laws relating to educational institutions\n**(1) Expansion to universal pre-k**\nSection 301(d)(2) of the Pre-K Enhancement and Expansion Amendment Act of 2008 (sec. 38\u2013273.01(d)(2), D.C. Official Code) is amended\u2014\n**(A)**\nin subparagraph (A), by adding and at the end;\n**(B)**\nin subparagraph (B), by striking ; and and inserting a period; and\n**(C)**\nby striking subparagraph (C).\n**(2) Title IX athletic equity**\n**(A) Nondiscrimination**\nSection 3 of the Title IX Athletic Equity Act of 2015 (sec. 38\u2013841.02, D.C. Official Code) is amended by striking sex, gender, or gender identity and inserting sex .\n**(B) Repeal of certain reporting requirements**\nSection 4 of such Act (sec. 38\u2013841.03, D.C. Official Code) is hereby repealed.\n**(3) Assessments of elementary and secondary school teaching workforce**\nSection 4195(f)(1) of the Teacher Preparation Act of 2021 (sec. 38\u20132254(f)(1), D.C. Official Code) is amended by striking , which shall include an assessment of the District's progress toward achieving diversity in its elementary and secondary public school teachers that matches the demographics of the District's corresponding student population .\n**(4) Office of the State Superintendent**\n**(A) Definition of LGBTQ**\nSection 2b of the State Education Office Establishment Act of 2000 (sec. 38\u20132601.02, D.C. Official Code) is amended by striking paragraph (2)(E).\n**(B) Report on LGBTQ youth**\nSection 3(b) of such Act (sec. 38\u20132602(b), D.C. Official Code) is amended\u2014\n**(i)**\nin paragraph (28), by striking subparagraph (C); and\n**(ii)**\nby striking paragraph (31).\n##### (k) Consideration of racial equity in taxation, budget, and financial management\n**(1) Budget and financial management**\nSection 47\u2013308.01, District of Columbia Official Code, is amended\u2014\n**(A)**\nin subsection (a), by striking paragraph (3A) of subsection (a); and\n**(B)**\nby striking subsection (h).\n**(2) Performance measures**\nSection 47\u2013308.02, D.C. Official Code, is amended by striking subsection (g).\n**(3) Performance accountability reports**\nSection 47\u2013308.03(c)(1), District of Columbia Official Code, is amended by striking , including those relating to achieving racial equity, .\n**(4) Duties of Tax Revision Commission**\nSection 47\u2013462(b)(5), District of Columbia Official Code, is amended by striking ; Such criteria and framework shall consider racial equity impacts; and inserting a period.\n##### (l) LGBTQ pride motor vehicle identification tags\n**(1) Issuance of tags**\nSection 2n of the District of Columbia Revenue Act of 1937 (sec. 50\u20131501.02n, D.C. Official Code) is hereby repealed.\n**(2) Use of proceeds**\nSection 3 of such Act (sec. 50\u20131501.03, D.C. Official Code) is amended\u2014\n**(A)**\nin subsection (a)(1), by striking subparagraph (R); and\n**(B)**\nin subsection (d), by striking paragraph (16).\n#### 5. Conforming elimination of certain offices and commissions in District of Columbia government; prohibition on funding\n##### (a) Elimination of certain offices and commissions\nThe following offices and commissions in the Government of the District of Columbia are hereby abolished:\n**(1)**\nThe Mayor\u2019s Office of Racial Equity.\n**(2)**\nThe Council Office of Racial Equity.\n**(3)**\nThe Council Commission on Racial Equity, Social Justice, and Economic Inclusion.\n**(4)**\nThe Commission on Reparations.\n**(5)**\nThe Mayor\u2019s Office on Latino Affairs.\n**(6)**\nThe Commission on Latino Community Development.\n**(7)**\nThe Mayor\u2019s Office on Caribbean Community Affairs.\n**(8)**\nThe Mayor\u2019s Office on African-American Affairs.\n**(9)**\nThe Commission on African-American Affairs.\n**(10)**\nThe Mayor\u2019s Office on African Affairs.\n**(11)**\nThe Mayor\u2019s Office on Asian and Pacific Islander Affairs.\n**(12)**\nThe Commission on Asian and Pacific Islander Affairs.\n**(13)**\nThe Commission on Asian and Pacific Islander Community Development.\n**(14)**\nThe Mayor\u2019s Office of Gay, Lesbian, Bisexual, Transgender and Questioning Affairs.\n**(15)**\nThe Commission for Women.\n**(16)**\nThe Commission on Health Equity.\n##### (b) Prohibition on establishing substantially similar offices or commissions\nThe Government of the District of Columbia may not establish a substantially similar successor office or commission to those referenced in subsection (a).\n##### (c) Prohibition of funding diversity, equity, and inclusion agencies\nNone of the funds available for obligation or expenditure by the District of Columbia government under any authority may be used for the purpose of maintaining in any agency an\u2014\n**(1)**\noffice relating to diversity, equity, inclusion, or accessibility or any substantially similar office;\n**(2)**\nmaintaining or employing a chief diversity officer or a substantially similar officer;\n**(3)**\ndeveloping, implementing, distributing, or publishing\u2014\n**(A)**\nplans, strategic plans, reports, or surveys relating to diversity, equity, inclusion, and accessibility; or\n**(B)**\naction plans, reports, or surveys relating to equity or substantially similar plans, reports, or surveys;\n**(4)**\ndeveloping, implementing, or maintaining in any agency an employee resource group or an affinity group based on race, color, ethnicity, religion, national origin, sexual orientation, or gender identity; or\n**(5)**\ndeveloping, implementing, or maintaining an equity team or a substantially similar team.\n#### 6. Enforcement; private right of action\n##### (a) Enforcement\nAny person alleging a violation of this Act, or any amendment made by this Act, may bring a civil action in the United States District Court for the District of Columbia.\n##### (b) Relief\nIn a civil action brought under subsection (a) in which the plaintiff prevails, the court may award\u2014\n**(1)**\na Writ of Mandamus or other equitable or declaratory relief;\n**(2)**\na minimum of $1,000 per violation per day;\n**(3)**\nreasonable attorney\u2019s fees and litigation costs;\n**(4)**\ncompensatory damages; and\n**(5)**\nall other appropriate relief.\n#### 7. Rule of construction\nNothing in this Act or, any amendment made by this Act, shall be construed to prevent the maintenance and funding of\u2014\n**(1)**\nany Equal Employment Opportunity office of the Government of the District of Columbia as historically organized and operated; or\n**(2)**\nan office of the Government of the District of Columbia enforcing the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or similar programs or offices as historically organized and operated.\n#### 8. Severability\nIf any provision of this Act or any amendment made by this Act, or the application of a provision of this Act or an amendment made by this Act to any person or circumstance, is held to be unconstitutional, the remainder of this Act, and the application of the provision or amendment to any person or circumstance, shall not be affected by the holding.\n#### 9. Effective date\nThis Act, and the amendments made by this Act, shall take effect on the date that is 90 days after the date of the enactment of this Act.",
      "versionDate": "2025-09-18",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-12-03T13:50:35Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5474ih.xml"
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
      "title": "To ensure equal protection of the law and prevent racism in the Government of the District of Columbia by prohibiting the Government of the District of Columbia from engaging in certain diversity, equity, or inclusion practices or conducting racial equity training, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T09:05:26Z"
    },
    {
      "title": "No DEI in DC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T03:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No DEI in DC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Diversity, Equity, and Inclusion in the District of Columbia Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T03:53:13Z"
    }
  ]
}
```
