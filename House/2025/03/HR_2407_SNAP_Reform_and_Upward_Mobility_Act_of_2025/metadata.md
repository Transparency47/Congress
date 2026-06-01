# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2407?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2407
- Title: SNAP Reform and Upward Mobility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2407
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-02-09T22:38:39Z
- Update date including text: 2026-02-09T22:38:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2407",
    "number": "2407",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001317",
        "district": "2",
        "firstName": "Josh",
        "fullName": "Rep. Brecheen, Josh [R-OK-2]",
        "lastName": "Brecheen",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "SNAP Reform and Upward Mobility Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-09T22:38:39Z",
    "updateDateIncludingText": "2026-02-09T22:38:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-03-27T13:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:11:00Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-27T13:07:20Z",
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
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "UT"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2407ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2407\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Brecheen (for himself, Mr. Kennedy of Utah , and Mr. Grothman ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo help individuals receiving assistance under the supplemental nutrition assistance program in obtaining self-sufficiency, to provide information on total spending on means-tested welfare programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SNAP Reform and Upward Mobility Act of 2025 .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nTITLE I\u2014Poverty measurement improvement\nSec. 101. Improving the measurement of poverty in the United States.\nSec. 102. Commission on valuation of government benefits.\nSec. 103. GAO reports on effect of supplementary data on calculation of poverty rates and related measures.\nSec. 104. Rule of construction.\nTITLE II\u2014Modifications to supplemental nutrition assistance program\nSec. 201. Work requirements.\nSec. 202. Employment and training program outcomes reporting.\nSec. 203. State matching funds.\nSec. 204. Eligibility.\nSec. 205. Compliance with fraud investigations.\nSec. 206. Authorized users of electronic benefit transfer cards.\nSec. 207. Reauthorization of medium- or high-risk retail food stores and wholesale food concerns.\nSec. 208. State activity reports.\nSec. 209. Disqualification by State agency.\nSec. 210. Retention of recaptured funds by States.\nI\nPoverty measurement improvement\n#### 101. Improving the measurement of poverty in the United States\n##### (a) Definitions\nIn this section:\n**(1) Federal benefit**\nThe term Federal benefit means a benefit, refundable tax credit, or other form of assistance provided under any of the following programs:\n**(A)**\nEarned Income Tax Credit (refundable portion).\n**(B)**\nChild Tax Credit (refundable portion).\n**(C)**\nSupplemental Security Income.\n**(D)**\nTemporary Assistance for Needy Families.\n**(E)**\nTitle IV\u2013E Foster Care.\n**(F)**\nTitle IV\u2013E Adoption Assistance.\n**(G)**\nMedicaid.\n**(H)**\nSCHIP.\n**(I)**\nIndian Health Services.\n**(J)**\nPPACA refundable premium assistance and cost sharing tax credit.\n**(K)**\nAssets for Independence program.\n**(L)**\nSupplemental Nutrition Assistance Food Program.\n**(M)**\nSchool Breakfast.\n**(N)**\nSchool Lunch.\n**(O)**\nWomen, Infants, and Children (WIC) Food Program.\n**(P)**\nChild and Adult Care Food Program.\n**(Q)**\nThe Food Distribution Program on Indian Reservations (FDPIR).\n**(R)**\nNutrition Program for the Elderly.\n**(S)**\nSeniors Farmers\u2019 Market Nutrition Program.\n**(T)**\nCommodity Supplemental Food Program.\n**(U)**\nSection 8 Housing.\n**(V)**\nPublic Housing.\n**(W)**\nHousing for Persons with Disabilities.\n**(X)**\nHome Investment Partnership Program.\n**(Y)**\nRural Housing Service.\n**(Z)**\nRural Housing Insurance Fund.\n**(AA)**\nLow-Income Home Energy Assistance Program.\n**(BB)**\nUniversal Service Fund Low Income Support Mechanism (subsidized phone services).\n**(CC)**\nPell Grants.\n**(DD)**\nSupplemental Educational Opportunity Grants.\n**(EE)**\nAmerican Opportunity Tax Credit (refundable portion).\n**(FF)**\nHealthy Start.\n**(GG)**\nJob Corps.\n**(HH)**\nHead Start (including Early Head Start).\n**(II)**\nWeatherization Assistance.\n**(JJ)**\nChafee Foster Care Independence Program.\n**(KK)**\nChild Care Subsidies from the Child Care and Development Fund.\n**(LL)**\nChild Care from the Temporary Assistance for Needy Families Block Grant.\n**(MM)**\nEmergency Assistance to Needy Families with Children.\n**(NN)**\nSenior Community Service Employment Program.\n**(OO)**\nMigrant and Seasonal Farm Workers Training Program.\n**(PP)**\nIndian and Native American Employment and Training Program.\n**(QQ)**\nIndependent Living Education and Training Vouchers.\n**(2) Resource unit**\nThe term resource unit means all co-resident individuals who are related by birth, marriage, or adoption, plus any co-resident unrelated children, foster children, and unmarried partners and their relatives.\n**(3) Market income**\nThe term market income means individual income from the following:\n**(A)**\nEarnings.\n**(B)**\nInterest.\n**(C)**\nDividends.\n**(D)**\nRents, royalties, and estates and trusts.\n**(E)**\nThe monetary value of employer-sponsored health insurance benefits.\n**(F)**\nOther forms of income, as determined by the Director.\n**(4) Entitlement and other income**\nThe term entitlement and other income means income from the following:\n**(A)**\nUnemployment (insurance) compensation.\n**(B)**\nWorkers\u2019 compensation.\n**(C)**\nSocial Security.\n**(D)**\nVeterans\u2019 payments and benefits.\n**(E)**\nSurvivor benefits.\n**(F)**\nDisability benefits (not including benefits under the Supplemental Security Income program).\n**(G)**\nPension or retirement income.\n**(H)**\nAlimony.\n**(I)**\nChild support.\n**(J)**\nFinancial assistance from outside of the household.\n**(K)**\nMedicare.\n**(5) Entitlement and earned unit income**\nThe term entitlement and earned unit income means the sum of all market income and entitlement and other income.\n**(6) Income tax data**\nThe term income tax data means return information, as such term is defined under section 6103(b)(2) of the Internal Revenue Code of 1986.\n**(7) Administering agency**\nThe term administering agency means a State or Federal agency responsible for administering a Federal benefit.\n**(8) Total resource unit income**\nThe term total resource unit income means, with respect to a resource unit, an amount equal to\u2014\n**(A)**\nthe sum of\u2014\n**(i)**\nall market income attributable to members of the unit;\n**(ii)**\nall entitlement and other income attributable to members of the unit; and\n**(iii)**\nan amount, or cash equivalent, of all Federal benefits received by members of the unit; minus\n**(B)**\nall State and Federal income and payroll taxes attributable to members of the unit.\n**(9) Earned resource unit income**\nThe term earned resource unit income means, with respect to a resource unit, all market income attributable to members of the unit.\n**(10) Personally identifiable information**\nThe term personally identifiable information means any information that identifies an individual or could reasonably be used to identify an individual that is\u2014\n**(A)**\ncollected pursuant to a survey conducted by the Bureau of the Census; or\n**(B)**\ndisclosed to the Bureau of the Census by an administering agency for the purpose of carrying out subsection (b).\n**(11) Director**\nThe term Director means the Director of the Bureau of the Census.\n##### (b) Verification of data collected in the Annual Social and Economic Supplement to the Current Population Survey\n**(1) In general**\nBeginning in fiscal year 2025, in order to more accurately determine the extent of poverty in the United States and the anti-poverty effectiveness of Federal benefit programs, the Director shall collect, in addition to the data collected under the Annual Social and Economic Supplement to the Current Population Survey, data from the appropriate administering agencies related to the following:\n**(A)**\nParticipation in any Federal benefit program and the monetary or cash equivalent value of such benefit for an individual, where possible, and otherwise for resource units or households.\n**(B)**\nThe total amount of market income for individuals.\n**(C)**\nThe total amount of entitlement and other income for individuals.\n**(D)**\nPayment of income taxes and payroll taxes for individuals.\n**(E)**\nTotal resource unit income.\n**(F)**\nTotal earned resource unit income.\n**(G)**\nAny other information about benefits or income received by individuals that the Director determines necessary to carry out this section and that is not included in the data relating to participation in Federal benefit programs or market income for individuals.\n**(2) Administering agency data**\nNot later than 6 months after receiving a request from the Director, the head of each administering agency shall make available to the Director such data (including income tax data) as the Director shall require for the purpose of carrying out this subsection and for the purposes outlined in section 6 of title 13, United States Code.\n**(3) Publication of data**\n**(A) Rates and other data**\n**(i) Report**\nThe Director shall submit to Congress, not later than January 1, 2026, a report detailing the implementation of this section, including\u2014\n**(I)**\nthe availability of related data;\n**(II)**\nthe quality of the data; and\n**(III)**\nthe methodology proposed for assigning dollar values to the receipt of noncash Federal benefits.\n**(ii) Tables and graphs**\nThe Director shall produce tables and graphs showing for each year the poverty rates and related data calculated using data collected under paragraph (1), including\u2014\n**(I)**\nthe total resource unit income for survey respondents;\n**(II)**\nthe total earned resource unit income for survey respondents;\n**(III)**\nthe total of all amounts described in subparagraphs (A) through (G) of paragraph (1) that are received by survey respondents;\n**(IV)**\na breakdown of the amount of income taxes and payroll taxes attributable to survey respondents; and\n**(V)**\nfor 2027 and subsequent years, poverty rates calculated using updated poverty thresholds as described in clause (iii).\n**(iii) Updated poverty thresholds**\nFor 2027 and subsequent years, the Director shall, in addition to the official poverty line (as defined by the Office of Management and Budget) and the supplemental poverty measure, provide an alternative poverty measure that uses the personal consumption expenditure price index (as published by the Bureau of Economic Analysis) and accounts for the data collected under paragraph (1). The Director shall provide a comparison of the official poverty line (as defined by the Office of Management and Budget), the supplemental poverty measure rate as defined by the Bureau of the Census, and the alternative poverty rate created using the alternative poverty measure under this section.\n**(iv) Rule of construction**\nThe Office of Management and Budget shall not use the additional data collected by the Director pursuant to paragraph (1) for purposes of defining the official poverty line.\n**(B) Confidentiality**\nConsistent with the provisions of sections 8, 9, and 23(c) of title 13, United States Code, the Director shall ensure the confidentiality of information furnished to the Director under this subsection.\n##### (c) Protection and disclosure of personally identifiable information\n**(1) In general**\nThe security, disclosure, and confidentiality provisions set forth in sections 9 and 23 of title 13, United States Code, shall apply to personally identifiable information obtained by the Bureau of the Census pursuant to this section.\n**(2) Restricted access to personally identifiable information**\nAccess to personally identifiable information collected to supplement the restricted-use Current Population Survey Annual Social and Economic Supplements in accordance with subsection (b)(1) shall be available only to those who have access to the Current Population Survey data with the permission of the Bureau of the Census and in accordance with any other applicable provision of law.\n**(3) Penalties**\nAny individual who knowingly accesses or discloses personally identifiable information in violation of this section shall be guilty of a felony and upon conviction thereof shall be fined in an amount of not more than $300,000 under title 18, United States Code, or imprisoned for not more than five years, or both.\n##### (d) State reporting of Federal data\nBeginning with the first full calendar year that begins after the date of enactment of this Act, with respect to any Federal benefit that is administered at the State level by a State administering agency, such State administering agency shall submit each year to the Federal administering agency responsible for administering the benefit at the Federal level a report that identifies each resource unit that received such benefits during such year by the personally identifiable information of the head of the resource unit and the amount, or cash equivalent, of such benefit received by such resource unit.\n#### 102. Commission on valuation of government benefits\n##### (a) Establishment\nThere is established within the United States Census Bureau a commission, to be known as the Commission on Valuation of Federal Benefits (referred to in this section as the Commission ).\n##### (b) Composition\n**(1) In general**\nThe Commission shall be composed of 8 members, of whom\u2014\n**(A)**\n2 members shall be appointed by the majority leader of the Senate;\n**(B)**\n2 members shall be appointed by the minority leader of the Senate;\n**(C)**\n2 members shall be appointed by the Speaker of the House of Representatives; and\n**(D)**\n2 members shall be appointed by the minority leader of the House of Representatives.\n**(2) Co-chairs**\nOf the members of the Commission\u2014\n**(A)**\n1 co-chair shall be designated by the majority leader of the Senate; and\n**(B)**\n1 co-chair shall be designated by the Speaker of the House of Representatives.\n**(3) Qualifications**\nEach member appointed to the Commission shall have experience in\u2014\n**(A)**\nquantitative policy research; and\n**(B)**\nwelfare or poverty studies.\n##### (c) Initial meeting\nNot later than 60 days after the date on which the last member is appointed under subsection (b), the Commission shall hold an initial meeting.\n##### (d) Quorum\nSix members of the Commission shall constitute a quorum.\n##### (e) No proxy voting\nProxy voting by members of the Commission shall be prohibited.\n##### (f) Staff\nThe Director of the Census Bureau shall appoint an executive director of the Commission.\n##### (g) Travel expenses\nMembers of the Commission shall serve without pay, but shall receive travel expenses in accordance with sections 5702 and 5703 of title 5, United States Code.\n##### (h) Duties of commission\n**(1) Recommendations**\n**(A) In general**\nThe Commission shall produce recommendations for the valuation of Federal benefits listed under section 101(a)(1) for the purpose of United States Census Bureau estimates of the Federal Poverty Level, including non-cash benefits.\n**(2) Report**\n**(A) In general**\nNot later than 270 days after the date of enactment of this Act, the Commission shall submit to Congress a report of the recommendations required under paragraph (1), including a detailed statement of methodology and reasoning behind recommendations.\n**(B) Public availability**\nThe report required by subparagraph (A) shall be made available on an internet website of the United States Government that is available to the public.\n##### (i) Powers of commission\nOn request by the executive director of the Commission, the head of a Federal agency shall furnish information to the Commission.\n##### (j) Termination of commission\nThe Commission shall terminate 90 days after the date on which the Commission submits the report under subsection (h)(2).\n##### (k) Authorization of appropriations\nThere is authorized to be appropriated $1,000,000 to carry out this section.\n#### 103. GAO reports on effect of supplementary data on calculation of poverty rates and related measures\nNot later than January 1, 2028, and every 2 years thereafter, the Comptroller General of the United States shall submit to Congress a report that compares the poverty rates and related measures calculated under the Annual Social and Economic Supplement to the Current Population Survey with the poverty rates and related measures calculated using the data collected under section 101(b)(1).\n#### 104. Rule of construction\nNothing in this title shall be construed to affect the eligibility of an individual or household for a Federal benefit.\nII\nModifications to supplemental nutrition assistance program\n#### 201. Work requirements\n##### (a) Declaration of policy\nSection 2 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 ) is amended by adding at the end the following: Congress further finds that it should also be the purpose of the supplemental nutrition assistance program to increase employment, to encourage healthy marriage, and to promote prosperous self-sufficiency, which means the ability of households to maintain an income above the poverty level without services and benefits from the Federal Government. .\n##### (b) Definition of food\nSection 3(k) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(k) ) is amended by striking means (1) and inserting means the following foods, food products, meals, and other items, only if the food, food product, meal, or other item is essential, as determined by the Secretary: (1) .\n##### (c) General work requirements\nSection 6(d)(1)(A) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(d)(1)(A) ) is amended, in the matter preceding clause (i), by striking 60 and inserting 65 .\n##### (d) Hour-Based work requirement\nSection 6(o) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(o) ) is amended\u2014\n**(1)**\nin paragraph (1)(C), by striking other than a supervised job search program or job search training program and inserting including an in-person supervised job search program ;\n**(2)**\nin paragraph (3)(A)(ii)(III), by striking 55 and inserting 64 ;\n**(3)**\nin paragraph (4)(A)\u2014\n**(A)**\nin the matter preceding clause (i), by striking area and inserting county or county equivalent ;\n**(B)**\nin clause (i), by striking or and inserting and ; and\n**(C)**\nby striking clause (ii) and inserting the following:\n(ii) is not located within a labor market area, as determined by data published by the Bureau of Labor Statistics, that has an unemployment rate of over 10 percent. ;\n**(4)**\nin paragraph (6)(D), by striking 15 percent and inserting 5 percent ;\n**(5)**\nby redesignating paragraph (7) as paragraph (8);\n**(6)**\nby inserting after paragraph (6) the following:\n(7) Work or work preparation hours requirement for married couples with children The total combined number of hours of work or work preparation activities under subparagraphs (A), (B), and (C) of paragraph (2) for both spouses in a married couple household with 1 or more children over the age of 6 shall not be greater than the total number of hours required under those subparagraphs for a single head of household. ; and\n**(7)**\nby inserting after paragraph (8) (as so redesignated) the following:\n(9) Minimum wage rule The limitation under subsection (d)(4)(F)(i) shall not apply to any work requirement, program, or activity required under this subsection. .\n#### 202. Employment and training program outcomes reporting\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture shall submit to Congress a report, using data from the most recent 5 fiscal years available, detailing the outcomes of beneficiaries of the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) (referred to in this section as SNAP ) who participate in employment and training programs (as defined in section 6(d)(4)(B) of that Act ( 7 U.S.C. 2015(d)(4)(B) )) for each of those 5 years that includes the following information:\n**(1)**\nThe number and percentage of SNAP beneficiaries in each State who participated in an employment and training program compared to the number and percentage of SNAP beneficiaries in each State who did not participate in an employment and training program.\n**(2)**\nThe number and percentage of SNAP beneficiaries in each State who obtained a job while participating in an employment and training program compared to the number and percentage of SNAP beneficiaries in each State who obtained a job but did not participate in an employment and training program.\n**(3)**\nThe number and percentage of SNAP beneficiaries in each State who retained a job for 6 months, 1 year, and 5 years after completing an employment and training program and obtaining a job compared to the number and percentage of SNAP beneficiaries in each State who retained a job for 6 months, 1 year, and 5 years but did not complete an employment and training program prior to obtaining that job.\n**(4)**\nThe increase or decrease in wages, if applicable, for SNAP beneficiaries in each State who retained a job for 6 months, 1 year, and 5 years after completing an employment and training program and obtaining a job compared to the increase or decrease in wages, if applicable, for SNAP beneficiaries in each State who retained a job for 6 months, 1 year, and 5 years but did not complete an employment and training program prior to obtaining that job.\n**(5)**\nThe number and percentage of SNAP beneficiaries who\u2014\n**(A)**\npreviously participated in an employment and training program;\n**(B)**\nafter that participation, obtained a job or stopped receiving SNAP benefits; and\n**(C)**\nafter regaining eligibility for SNAP benefits, reentered an employment or training program.\n**(6)**\nThe average duration that SNAP beneficiaries in each State participated in an employment and training program.\n**(7)**\nA breakdown of\u2014\n**(A)**\nthe types of employment and training activities offered by the employment and training program of each State; and\n**(B)**\nthe types of jobs that States are preparing employment and training program participants to obtain.\n#### 203. State matching funds\nSection 4 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2013 ) is amended by adding at the end the following:\n(d) State matching funds (1) In general Each State that participates in the supplemental nutrition assistance program shall, as a condition of participation, be required to contribute matching funds in an amount equal to, of the funds received from the Secretary by the State for program administration\u2014 (A) for fiscal year 2025, 10 percent; (B) for fiscal year 2026, 15 percent; (C) for fiscal year 2027, 20 percent; (D) for fiscal year 2028, 25 percent; (E) for fiscal year 2029, 30 percent; (F) for fiscal year 2030, 35 percent; (G) for fiscal year 2031, 40 percent; (H) for fiscal year 2032, 45 percent; and (I) for fiscal year 2033 and each fiscal year thereafter, 50 percent. (2) Additional contributions permitted Nothing in this subsection prevents a State from contributing matching funds in an amount greater than the amount required under paragraph (1) for the applicable fiscal year. .\n#### 204. Eligibility\nSection 5(a) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014(a) ) is amended\u2014\n**(1)**\nin the second sentence, by inserting that are limited to families whose income and resources satisfy financial need criteria established in accordance with subsections (c) and (g) by the State for receipt of the benefits after ( 42 U.S.C. 601 et seq. ) ; and\n**(2)**\nby inserting after the second sentence the following: To be deemed eligible for participation in the supplemental nutrition assistance program under this subsection, a household shall receive a cash or noncash means-tested public benefit for at least 6 consecutive months valued at not less than $50. .\n#### 205. Compliance with fraud investigations\nSection 6(d) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(d) ) is amended by adding at the end the following:\n(5) Compliance with fraud investigations To be eligible to participate in the supplemental nutrition assistance program, an individual shall cooperate with any investigation into fraud under that program, including full participation in any\u2014 (A) meeting requested by fraud investigators; and (B) administrative hearing. .\n#### 206. Authorized users of electronic benefit transfer cards\nSection 7(h) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(h) ) is amended by adding at the end the following:\n(15) Authorized users (A) In general A State agency shall register\u2014 (i) at least 1 member of a household issued an EBT card as an authorized user of the card; and (ii) an authorized representative of a household as an authorized user of the EBT card issued to the household. (B) Limit Not more than 5 individuals shall be registered as authorized users, including the authorized representative of a household, on an EBT card. (C) Unauthorized use (i) In general An EBT card shall not be used by any individual who is not an authorized user of the EBT card. (ii) 2 unauthorized uses If an EBT card has been used 2 times by an unauthorized user of the EBT card, the head of the household to which the EBT card is issued shall be required to review program rights and responsibilities with personnel of the State agency. (iii) 4 unauthorized uses If an EBT card has been used 4 times by an unauthorized user of the EBT card, the State agency shall suspend benefits for the household to which the EBT card is issued for 1 month. (iv) 6 unauthorized uses If an EBT card has been used 6 times by an unauthorized user of the EBT card, the State agency shall suspend benefits for the household to which the EBT card is issued for 3 months. (v) 7 or more unauthorized uses If an EBT card has been used 7 or more times by an unauthorized user of the EBT card, the State agency shall suspend benefits for the household to which the EBT card is issued for 1 month per unauthorized use. (vi) Administration Any action taken under clauses (ii) through (v) shall be consistent with sections 6(b) and 11(e)(10), as applicable. .\n#### 207. Reauthorization of medium- or high-risk retail food stores and wholesale food concerns\nSection 9(a)(2)(A) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2018(a)(2)(A) ) is amended by striking ; and and inserting , which, in the case of a retail food store or wholesale food concern for which there is a medium risk or high risk of fraudulent transactions, as determined by the fraud detection system of the Food and Nutrition Service, shall be annually; and .\n#### 208. State activity reports\nSection 11 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2020 ) is amended by adding at the end the following:\n(y) State activity reports The Secretary shall publish for each fiscal year a report describing the activity of each State in the supplemental nutrition assistance program, which shall contain, for the applicable fiscal year, substantially the same information as is contained in the report published by the Food and Nutrition Service entitled Supplemental Nutrition Assistance Program State Activity Report Fiscal Year 2016 and published September 2017. .\n#### 209. Disqualification by State agency\nSection 12 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2021 ) is amended by adding at the end the following:\n(j) Disqualification by State agency (1) In general Except as provided in paragraph (4), a State agency shall permanently disqualify from participation in the supplemental nutrition assistance program an approved retail food store or wholesale food concern convicted of\u2014 (A) trafficking in food instruments (including any voucher, draft, check, or access device (including an electronic benefit transfer card or personal identification number) issued in lieu of a food instrument under this Act); or (B) selling firearms, ammunition, explosives, or controlled substances (as defined in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 )) in exchange for food instruments (including any item described in subparagraph (A) issued in lieu of a food instrument under this Act). (2) Notice of disqualification The State agency shall\u2014 (A) provide the approved retail food store or wholesale food concern with notification of the disqualification; and (B) make the disqualification effective on the date of receipt of the notice of disqualification. (3) Prohibition of receipt of lost revenues A retail food store or wholesale food concern shall not be entitled to receive any compensation for revenues lost as a result of disqualification under this subsection. (4) Exceptions in lieu of disqualification (A) In general A State agency may permit a retail food store or wholesale food concern that, but for this paragraph, would be disqualified under paragraph (1), to continue to participate in the supplemental nutrition assistance program if the State agency determines, in its sole discretion, that\u2014 (i) disqualification of the retail food store or wholesale food concern, as applicable, would cause hardship to participants in the supplemental nutrition assistance program; or (ii) (I) the retail food store or wholesale food concern had, at the time of the violation under paragraph (1), an effective policy and program in effect to prevent violations described in paragraph (1); and (II) the ownership of the retail food store or wholesale food concern was not aware of, did not approve of, and was not involved in the conduct of the violation. (B) Civil penalty If a State agency under subparagraph (A) permits a retail food store or wholesale food concern to continue to participate in the supplemental nutrition assistance program in lieu of disqualification, the State agency shall assess a civil penalty in an amount determined by the State agency, except that\u2014 (i) the amount of the civil penalty shall not exceed $10,000 for each violation; and (ii) the amount of civil penalties imposed for violations investigated as part of a single investigation may not exceed $40,000. (C) Reporting (i) To the Secretary If a State agency under subparagraph (A) permits a retail food store or wholesale food concern to continue to participate in the supplemental nutrition assistance program in lieu of disqualification, the State agency shall annually submit to the Secretary a report describing the justification of the State agency for that action. (ii) To Congress The Secretary shall annually submit to Congress a report compiling the information contained in reports submitted to the Secretary under clause (i). .\n#### 210. Retention of recaptured funds by States\nSection 16(a) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025(a) ) is amended\u2014\n**(1)**\nin the second sentence, by striking The officials and inserting the following:\n(3) Prohibition The officials ;\n**(2)**\nin the first sentence\u2014\n**(A)**\nby redesignating paragraphs (1) through (9) as subparagraphs (A) through (I), respectively; and\n**(B)**\nby striking section 17(n): Provided, That the Secretary and inserting the following: \u201csection 17(n).\n(2) Administration on Indian reservations and in Native villages (A) In general The Secretary ;\n**(3)**\nin paragraph (2) (as so designated)\u2014\n**(A)**\nin subparagraph (A), by striking 35 percent and inserting 50 percent ; and\n**(B)**\nby adding at the end the following:\n(B) Use of retained amounts for fraud investigations The value of funds or allotments recovered or collected pursuant to sections 6(b) and 13(c) that are retained by a State under subparagraph (A) in excess of 35 percent shall be used by the State for investigations of fraud in the supplemental nutrition assistance program. ; and\n**(4)**\nby striking the subsection designation and all that follows through Subject to in the matter preceding paragraph (2) (as so designated) and inserting the following:\n(a) Administrative cost-Sharing (1) In general Subject to .",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-27",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1197",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SNAP Reform and Upward Mobility Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-08T19:52:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2407",
          "measure-number": "2407",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2407v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>SNAP Reform and Upward Mobility Act of 2025</strong></p><p>This bill amends how U.S. poverty levels are determined and modifies Supplemental Nutrition Assistance Program (SNAP)\u00a0eligibility and enforcement provisions.</p><p>The Bureau of the Census must (1) collect specified data regarding the receipt of federal benefits and individual income, and (2) use the data to provide an alternative poverty measure. The bill also establishes a commission to recommend the valuation of specific federal benefits for the purpose of estimating\u00a0the Federal Poverty Level.</p><p>The bill also expands the applicability of the general work requirements for SNAP recipients to include those who are ages 16-64\u00a0(currently 16-59) with exemptions.</p><p>This bill also expands the applicability of the work requirements for SNAP recipients\u00a0who are able-bodied adults without dependents (ABAWDs)\u00a0to include those who are ages 18-64\u00a0(currently 18-55). In general, ABAWDs\u00a0have work requirements in addition to the general SNAP work-related requirements\u00a0and are limited to receiving 3 months of SNAP benefits in a 36-month period,\u00a0unless the additional work-related requirements are met. Further, the bill allows married individuals with a dependent over the age of six\u00a0to jointly fulfill hour-based work requirements.</p><p>Additional\u00a0changes to SNAP include</p><ul><li>requiring states participating in SNAP to contribute specified matching funds, beginning at 10% for FY2025 and increasing annually until the matching requirement reaches 50% for FY2033 and each subsequent fiscal year;</li><li>requiring SNAP beneficiaries to participate in fraud investigations; and</li><li>establishing penalties (e.g., benefit suspensions) for unauthorized uses of electronic benefit transfer (EBT) cards.</li></ul>"
        },
        "title": "SNAP Reform and Upward Mobility Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2407.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>SNAP Reform and Upward Mobility Act of 2025</strong></p><p>This bill amends how U.S. poverty levels are determined and modifies Supplemental Nutrition Assistance Program (SNAP)\u00a0eligibility and enforcement provisions.</p><p>The Bureau of the Census must (1) collect specified data regarding the receipt of federal benefits and individual income, and (2) use the data to provide an alternative poverty measure. The bill also establishes a commission to recommend the valuation of specific federal benefits for the purpose of estimating\u00a0the Federal Poverty Level.</p><p>The bill also expands the applicability of the general work requirements for SNAP recipients to include those who are ages 16-64\u00a0(currently 16-59) with exemptions.</p><p>This bill also expands the applicability of the work requirements for SNAP recipients\u00a0who are able-bodied adults without dependents (ABAWDs)\u00a0to include those who are ages 18-64\u00a0(currently 18-55). In general, ABAWDs\u00a0have work requirements in addition to the general SNAP work-related requirements\u00a0and are limited to receiving 3 months of SNAP benefits in a 36-month period,\u00a0unless the additional work-related requirements are met. Further, the bill allows married individuals with a dependent over the age of six\u00a0to jointly fulfill hour-based work requirements.</p><p>Additional\u00a0changes to SNAP include</p><ul><li>requiring states participating in SNAP to contribute specified matching funds, beginning at 10% for FY2025 and increasing annually until the matching requirement reaches 50% for FY2033 and each subsequent fiscal year;</li><li>requiring SNAP beneficiaries to participate in fraud investigations; and</li><li>establishing penalties (e.g., benefit suspensions) for unauthorized uses of electronic benefit transfer (EBT) cards.</li></ul>",
      "updateDate": "2026-02-09",
      "versionCode": "id119hr2407"
    },
    "title": "SNAP Reform and Upward Mobility Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>SNAP Reform and Upward Mobility Act of 2025</strong></p><p>This bill amends how U.S. poverty levels are determined and modifies Supplemental Nutrition Assistance Program (SNAP)\u00a0eligibility and enforcement provisions.</p><p>The Bureau of the Census must (1) collect specified data regarding the receipt of federal benefits and individual income, and (2) use the data to provide an alternative poverty measure. The bill also establishes a commission to recommend the valuation of specific federal benefits for the purpose of estimating\u00a0the Federal Poverty Level.</p><p>The bill also expands the applicability of the general work requirements for SNAP recipients to include those who are ages 16-64\u00a0(currently 16-59) with exemptions.</p><p>This bill also expands the applicability of the work requirements for SNAP recipients\u00a0who are able-bodied adults without dependents (ABAWDs)\u00a0to include those who are ages 18-64\u00a0(currently 18-55). In general, ABAWDs\u00a0have work requirements in addition to the general SNAP work-related requirements\u00a0and are limited to receiving 3 months of SNAP benefits in a 36-month period,\u00a0unless the additional work-related requirements are met. Further, the bill allows married individuals with a dependent over the age of six\u00a0to jointly fulfill hour-based work requirements.</p><p>Additional\u00a0changes to SNAP include</p><ul><li>requiring states participating in SNAP to contribute specified matching funds, beginning at 10% for FY2025 and increasing annually until the matching requirement reaches 50% for FY2033 and each subsequent fiscal year;</li><li>requiring SNAP beneficiaries to participate in fraud investigations; and</li><li>establishing penalties (e.g., benefit suspensions) for unauthorized uses of electronic benefit transfer (EBT) cards.</li></ul>",
      "updateDate": "2026-02-09",
      "versionCode": "id119hr2407"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2407ih.xml"
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
      "title": "SNAP Reform and Upward Mobility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SNAP Reform and Upward Mobility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To help individuals receiving assistance under the supplemental nutrition assistance program in obtaining self-sufficiency, to provide information on total spending on means-tested welfare programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:28Z"
    }
  ]
}
```
