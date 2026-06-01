# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2059?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2059
- Title: Keeping Obstetrics Local Act
- Congress: 119
- Bill type: S
- Bill number: 2059
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2059",
    "number": "2059",
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
    "title": "Keeping Obstetrics Local Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
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
        "item": [
          {
            "date": "2025-06-12T16:56:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-12T16:56:12Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NH"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "WA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CO"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "VA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "RI"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NV"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-12",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NM"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "GA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "VT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NJ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "WA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-12",
      "state": "ME"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "CA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2059is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2059\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Wyden (for himself, Ms. Hassan , Ms. Cantwell , Mr. Bennet , Mr. Warner , Mr. Whitehouse , Ms. Cortez Masto , Ms. Warren , Mr. Sanders , Ms. Smith , Mr. Luj\u00e1n , Mr. Warnock , Mr. Welch , Ms. Duckworth , Mr. Booker , Mr. Merkley , Mrs. Murray , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend titles XIX and XXI of the Social Security Act to enhance financial support for rural and safety net hospitals providing maternity, labor, and delivery services to vulnerable populations, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Keeping Obstetrics Local Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Enhancing financial support for rural and safety net hospitals that provide obstetric services\nSec. 101. State studies and HHS report on costs of providing maternity, labor, and delivery services.\nSec. 102. Requiring adequate payment rates under Medicaid for maternity, labor, and delivery services at eligible hospitals.\nSec. 103. Increased Federal financial participation for maternity, labor, and delivery services furnished by eligible hospitals.\nSec. 104. Labor and delivery services anchor payments.\nSec. 105. Application of adequate payment requirement and increased Federal financial participation requirements to CHIP.\nSec. 106. Disregarding increased and additional payments to hospitals for purposes of other supplemental payments and upper payment limits.\nTITLE II\u2014Expand Coverage of Maternal Health Care\nSec. 201. Requiring 12-month continuous, full benefit coverage for pregnant individuals under Medicaid and CHIP.\nSec. 202. Health homes for pregnant and postpartum women.\nSec. 203. Guidance on supporting and improving access to Medicaid and CHIP coverage of services provided by doulas and certain maternal health professionals.\nSec. 204. Medicaid and CHIP increased financial support for depression and anxiety screening during the perinatal and postpartum periods.\nSec. 205. Presumptive eligibility for pregnant individuals.\nTITLE III\u2014Invest in the Maternal Health Care Workforce\nSec. 301. Emergency obstetric workforce support.\nSec. 302. Streamlined screening and enrollment of providers of maternity, labor, and delivery services in neighboring States.\nTITLE IV\u2014Requiring Public Communication of Obstetrics Data and Unit Closures\nSec. 401. Timely notifications of impending hospital obstetric unit closures.\nSec. 402. Collection of data relating to hospital labor and delivery services.\nI\nEnhancing financial support for rural and safety net hospitals that provide obstetric services\n#### 101. State studies and HHS report on costs of providing maternity, labor, and delivery services\n##### (a) State study\n**(1) In general**\nNot later than 24 months after the date of enactment of this Act, and every 5 years thereafter, each State (as such term is defined in section 1101(a)(1) of the Social Security Act ( 42 U.S.C. 1301(a)(1) ) for purposes of titles XIX and XXI of such Act) shall conduct a study on the costs of providing maternity, labor, and delivery services in applicable hospitals (as defined in paragraph (3)) and submit the results of such study to the Secretary of Health and Human Services (referred to in this section as the Secretary ).\n**(2) Content of study**\nA State study required under paragraph (1) shall include the following information (to the extent practicable) with respect to maternity, labor, and delivery services furnished by applicable hospitals located in the State:\n**(A)**\nAn estimate of the cost of providing maternity, labor, and delivery services at applicable hospitals, based on the expenditures a representative sample of such hospitals incurred for providing such services during the 2 most recent years for which data is available.\n**(B)**\nAn estimate of the cost of providing maternity, labor, and delivery services at applicable hospitals that ceased providing labor and delivery services within the past 5 years, based on the expenditures a representative sample of such hospitals incurred for providing such services during the 2 most recent years for which data is available.\n**(C)**\nTo the extent data allows, an analysis of the extent to which geographic location, community demographics, and local economic factors (as defined by the Secretary) affect the cost of providing maternity, labor, and delivery services at applicable hospitals, including the cost of services that support the provision of maternity, labor, and delivery services.\n**(D)**\nThe amounts applicable hospitals are paid for maternity, labor, and delivery services, by geographic location and hospital size, under\u2014\n**(i)**\nMedicare;\n**(ii)**\nthe State Medicaid program, including payment amounts for such services under fee-for-service payment arrangements and under managed care (as applicable);\n**(iii)**\nthe State CHIP plan, including payment amounts for such services under fee-for-service payment arrangements and under managed care (as applicable); and\n**(iv)**\nprivate health insurance.\n**(E)**\nA comparative payment rate analysis\u2014\n**(i)**\ncomparing payment rates for maternity, labor, and delivery services (inclusive of all payments received by applicable hospitals for furnishing maternity, labor, and delivery services) under the State Medicaid fee-for-service program to such payment rates for such services under Medicare (as described in section 447.203(b)(3) of title 42, Code of Federal Regulations), other Federally funded or State-funded programs (including, to the extent data is available, Medicaid managed care rates), and to the payment rates for such services, to the extent data is available, of private health insurers within geographic areas of the State; and\n**(ii)**\nanalyzing different payment methods for such services, such as the use of bundled payments, quality incentives, and low-volume adjustments.\n**(F)**\nAn evaluation, using such methodology and parameters established by the Secretary, of whether each hospital located in the State that furnishes maternity, labor, and delivery services is expected to experience in the next 3 years significant changes in particular expenditures or types of reimbursement for maternity, labor, and delivery services.\n**(3) Applicable hospital defined**\nFor purposes of this subsection, the term applicable hospital means any hospital located in a State that meets either of the following criteria:\n**(A)**\nThe hospital provides labor and delivery services and more than 50 percent of the hospital\u2019s births (in the most recent year for which such data is available) are financed by the Medicaid program or CHIP.\n**(B)**\nThe hospital\u2014\n**(i)**\nis located in a rural area (as defined by the Federal Office of Rural Health Policy for the purpose of rural health grant programs administered by such Office);\n**(ii)**\nbased on the most recent 2 years of data available (as determined by the Secretary), furnished services for less than an average of 300 births per year; and\n**(iii)**\nprovides labor and delivery services.\n**(4) Assistance to small hospitals in compiling cost information**\nThere are appropriated to the Secretary for fiscal year 2026, $10,000,000 for the purpose of providing grants and technical assistance to a hospital described in paragraph (3)(B) to enable such hospital to compile detailed information for use in the State studies required under paragraph (1), to remain available until expended.\n**(5) HHS report on State studies**\nFor each year in which a State is required to conduct a study under paragraph (1), the Secretary shall issue, not later than 12 months after the date on which the State submits to the Secretary the data described in such paragraph, a publicly available report that compiles and details the results of such study and includes the information described in paragraph (2).\n##### (b) HHS report on national data collection findings\nNot later than 3 years after the date of enactment of this Act, the Secretary shall submit to Congress, and make publicly available, a report analyzing the first studies conducted by States under subsection (a)(1), including recommendations for improving data collection on the cost of providing maternity, labor, and delivery services.\n##### (c) Implementation funding\nIn addition to the amount appropriated under subsection (a)(4), there are appropriated, out of any funds in the Treasury not otherwise obligated, $3,000,000 for fiscal year 2026, to remain available until expended, to the Secretary of Health and Human Services for purposes of implementing this section.\n#### 102. Requiring adequate payment rates under Medicaid for maternity, labor, and delivery services at eligible hospitals\n##### (a) Fee-for-Service payments\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)(13)\u2014\n**(A)**\nby striking and at the end of subparagraph (B);\n**(B)**\nby adding and at the end of subparagraph (C); and\n**(C)**\nby adding at the end the following new subparagraph:\n(D) for each fiscal year beginning with fiscal year 2027, payment for maternity, labor, and delivery services (as defined in subsection (uu)) furnished during such fiscal year in an eligible hospital (as defined in such subsection) at a rate that is not less than the minimum payment rate specified for the fiscal year in paragraph (4) of such subsection; ; and\n**(2)**\nby adding at the end the following new subsection:\n(uu) Maternity, labor, and delivery services and eligible hospitals defined For purposes of subsection (a)(13)(D)\u2014 (1) Maternity, labor, and delivery services (A) In general The term maternity, labor, and delivery services means such inpatient hospital services and outpatient hospital services, including behavioral health services, that are provided in relation to maternity care or labor and delivery, identified by appropriate ICD and CPT codes, as the Secretary shall specify after consultation with professional or medical societies with expertise in pregnancy, childbirth, and postpartum care. (B) Scope Such term shall not be limited in application, for any eligible hospital, only to services that relate to a birth that occurs in the hospital. (C) Rulemaking Not later than July 1, 2026, the Secretary shall issue an interim final rule specifying which services shall be considered maternity, labor, and delivery services for purposes of this subsection and subsection (a)(13)(D). (2) Eligible hospital (A) In general The term eligible hospital means, with respect to a State and fiscal year\u2014 (i) a hospital that is located in a rural area (as defined by the Federal Office of Rural Health Policy for the purpose of rural health grant programs administered by such Office); (ii) a critical access hospital (as defined in section 1861(mm)(1)); (iii) a hospital operated by the Indian Health Service or an Indian Tribe under the Indian Self-Determination and Education Assistance Act; (iv) a hospital for which, in the most recent 12-month period for which data is available, at least 50 percent of all births for which the hospital provided maternity, labor, and delivery services during such fiscal year were qualifying births; or (v) a hospital that is able to demonstrate, through a process to be determined by the Secretary, that, for the applicable fiscal year, the hospital projects that at least 50 percent of all births for which the hospital will provide maternity, labor, and delivery services during such fiscal year will be qualifying births. (B) Identification of eligible hospitals Each State, subject to the approval of the Secretary, shall identify the hospitals in the State that are eligible hospitals with respect to a fiscal year. (3) Qualifying birth For purposes of paragraph (2), the term qualifying birth means a birth for which any maternity, labor, and delivery services associated with the birth\u2014 (A) were paid for under a State plan under this title (or under a waiver of such a plan) or under a State child health plan under title XXI (or under a waiver of such a plan); (B) were paid for under title XVIII; (C) were provided by the Indian Health Service or a Native Hawaiian health care system (as defined in section 12 of the Native Hawaiian Health Care Improvement Act); or (D) were provided to a patient who does not have minimum essential coverage (as defined in section 5000A(f) of the Internal Revenue Code of 1986) and were not fully paid for by such patient. (4) Minimum payment rate specified The minimum payment rate specified in this paragraph is, with respect to an eligible hospital and maternal, labor, and delivery services\u2014 (A) for fiscal year 2027, 150 percent of the payment rate that would apply for such services and hospital under title XVIII; and (B) for each period of 5 fiscal years beginning with fiscal years 2028 through 2032, a payment rate that is determined for such period by the Secretary to accurately reflect the costs incurred by eligible hospitals in providing such services, informed by the results of the most recent State studies submitted to the Secretary under section 101(a) of the Keeping Obstetrics Local Act . .\n##### (b) Under Medicaid managed care plans\nSection 1932(f) of the Social Security Act ( 42 U.S.C. 1396u\u20132(f) ) is amended\u2014\n**(1)**\nin the heading, by inserting and maternity, labor, and delivery services at eligible hospitals after services ; and\n**(2)**\nby striking described in section 1902(a)(13)(C) and inserting described in subparagraph (C) of section 1902(a)(13) or maternity, labor, and delivery services described in subparagraph (D) of such section that are furnished by an eligible hospital (as defined in section 1905(uu)) .\n#### 103. Increased Federal financial participation for maternity, labor, and delivery services furnished by eligible hospitals\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended\u2014\n**(1)**\nin subsection (b), by striking and (ii) and inserting (ii), and (kk) ; and\n**(2)**\nby adding at the end the following new subsection:\n(kk) Maternity, labor, and delivery services (1) In general Notwithstanding subsection (b), with respect to State expenditures for medical assistance for maternity, labor, and delivery services furnished by an eligible hospital (as such terms are defined in section 1902(uu)) in a fiscal quarter that begins on or after October 1, 2026\u2014 (A) the Federal medical assistance percentage applicable to the enhanced payment rate amount of such expenditures (as determined for the State and quarter under paragraph (2)(A)) shall be equal to 100 percent; and (B) subject to paragraph (3), the Federal medical assistance percentage applicable to the base payment rate amount of such expenditures (as determined for the State and quarter under paragraph (2)(B)) shall be equal to the enhanced FMAP determined for the State and quarter under section 2105(b). (2) Determination of enhanced payment rate amount and base payment rate amount (A) Enhanced payment rate amount (i) In general For purposes of paragraph (1)(A), the enhanced payment rate amount for a State and fiscal quarter is equal to the amount of State expenditures for medical assistance for maternity, labor, and delivery services furnished by an eligible hospital (as such terms are defined in section 1902(uu)) in such fiscal quarter that is attributable to the amount by which the minimum payment rate required under section 1902(a)(13)(D) (or, by application, section 1932(f)) exceeds the base payment rate applicable to such services, as determined for the State, quarter, and services under clause (ii). (ii) Base payment rate For purposes of clause (i), the base payment rate determined for a State, a fiscal quarter, and maternity, labor, and delivery services (as defined in section 1902(uu)) shall be equal to\u2014 (I) the payment rate applicable to such services under the State plan (or under a waiver of such plan) as of January 1, 2025; increased by (II) the percentage increase in the medical care component of the consumer price index for all urban consumers from January of 2025 to the month ending on the day before the 1st day of such fiscal quarter. (B) Base payment rate amount For purposes of paragraph (1)(B), the base payment rate amount for a State and fiscal quarter is equal to\u2014 (i) the total amount of State expenditures for medical assistance for maternity, labor, and delivery services furnished by an eligible hospital (as such terms are defined in section 1902(uu)) in such fiscal quarter; minus (ii) the enhanced payment rate amount determined for the State and fiscal quarter under subparagraph (A). (3) Application of higher match Subparagraph (B) of paragraph (1) shall not apply in the case of State expenditures described in such subparagraph if the application of such subparagraph would result in a lower Federal medical assistance percentage for such expenditures than would otherwise apply without the application of such paragraph. (4) Exclusion of expenditures from territorial caps Any payment made to a territory for medical assistance that is subject to the Federal medical assistance percentage specified in paragraph (1)(A) or the enhanced FMAP referred to in paragraph (1)(B) shall not be taken into account for purposes of applying payment limits under subsections (f) and (g) of section 1108. .\n#### 104. Labor and delivery services anchor payments\n##### (a) State requirement\nSection 1902(a)(13)(A) of the Social Security Act ( 42 U.S.C. 1396a(a)(13)(A) ) is amended\u2014\n**(1)**\nin clause (iii), by striking and at the end;\n**(2)**\nin clause (iv), by striking the semicolon at the end and inserting , and ; and\n**(3)**\nby adding at the end the following new clause:\n(v) in the case of hospitals, such rates take into account (in a manner consistent with section 1923A) the situation of low volume obstetric hospitals (as such term is defined in such section); .\n##### (b) Requiring anchor payments for low volume obstetric hospitals\nTitle XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) is amended by inserting the following after section 1923:\n1923A. Anchor payments for labor and delivery services provided by low volume obstetric hospitals (a) Implementation of requirement A State plan under this title shall not be considered to meet the requirement of section 1902(a)(13)(A)(v) (insofar as it requires payments to hospitals to take into account the situation of low volume obstetric hospitals), as of October 1, 2026, unless the State has submitted to the Secretary, by not later than such date, an amendment to such plan that provides for an annual anchor payment to such hospitals, consistent with subsection (c). (b) Definitions In this section: (1) Antenatal transfer The term antenatal transfer means, with respect to a hospital, a pregnant individual who was expected to receive labor and delivery services at the hospital but who is transferred to a different hospital because of a need for labor and delivery services that are not available at the transferring hospital. (2) Delivery volume The term delivery volume means, with respect to a hospital and a fiscal year, the total number of births occurring in, and antenatal transfers made by, such hospital during such year. (3) Labor and delivery revenue floor The term labor and delivery revenue floor means, with respect to a low volume obstetric hospital and a fiscal year, the amount equal to the sum of\u2014 (A) the product of\u2014 (i) the delivery volume for such hospital and fiscal year; and (ii) the per delivery amount for such fiscal year; and (B) the standby capacity amount for such fiscal year. (4) Labor and delivery services The term labor and delivery services means such inpatient and outpatient hospital services related to labor and delivery, including services related to antenatal transfers, identified by appropriate ICD and CPT codes, as the Secretary shall specify in consultation with professional or medical societies with expertise in this area. (5) Low volume obstetric hospital The term low volume obstetric hospital means, with respect to a hospital and a fiscal year, a hospital\u2014 (A) that is an eligible hospital (as defined in section 1902(uu)(2)); (B) in which the average number of births for which the hospital provided labor and delivery services during the preceding 3 fiscal years is less than 300 births per year; (C) that did not provide labor and delivery services in the preceding fiscal year, but in which the average number of births for which the hospital provided labor and delivery services during the most recent 3 fiscal years in which the hospital provided labor and delivery services is less than 300 births per year; (D) that is not described in subparagraphs (B) or (C) but, in the applicable fiscal year, provides labor and delivery services for fewer than 300 births; or (E) that is not described in subparagraphs (B) through (D) but is certified by the State in which the hospital is located as meeting such criteria as the Secretary shall establish for identifying hospitals that are essential to meeting the needs of an underserved population, such as serving a population with limited English proficiency, serving specific racial or ethnic populations, or other factors. (6) Medicaid labor and delivery revenue floor The term Medicaid labor and delivery revenue floor means, with respect to a low volume obstetric hospital and a fiscal year, the product of\u2014 (A) the labor and delivery revenue floor for such hospital and fiscal year; and (B) the percentage of the delivery volume of such hospital in such fiscal year that were paid for under a State plan under this title (or under a waiver of such a plan) or under a State child health plan under title XXI (or under a waiver of such a plan). (7) Per delivery amount (A) In general The term per delivery amount means, with respect to a fiscal year, an amount, as determined under subparagraph (B), that represents the marginal cost to a low volume obstetric hospital of a birth or an antenatal transfer. (B) Determination of per delivery amount (i) Fiscal year 2028 For fiscal year 2028, the per delivery amount shall be $10,000. (ii) Indexing Subject to clause (iii), for each fiscal year after fiscal year 2028, the per delivery amount shall be the amount that applied under this subparagraph for the preceding fiscal year increased by the percentage increase in the medical care component of the consumer price index for all urban consumers for the 12-month period ending with September of such preceding fiscal year. (iii) Periodic revision of per delivery amount Not less than once every 5 fiscal years, the Secretary shall collect and analyze data on the costs of labor and delivery services at low volume obstetric hospitals and, through rulemaking, shall establish a new per delivery amount for purposes of this section to ensure that such amount accurately reflects the marginal cost to a low volume obstetric hospital of a birth or an antenatal delivery. (8) Standby capacity amount (A) In general The term standby capacity amount means, with respect to a fiscal year, an amount, as determined under subparagraph (B), that represents the minimum level of expenditures by a low volume obstetric hospital that is necessary to ensure that adequate personnel, equipment, and facilities are available at all times to provide labor and delivery services. (B) Determination of standby capacity amount (i) Fiscal year 2028 For fiscal year 2028, the standby capacity amount shall be $1,200,000. (ii) Indexing Subject to clause (iii), for each fiscal year after fiscal year 2028, the standby capacity amount shall be the amount that applied under this subparagraph for the preceding fiscal year increased by the percentage increase in the medical care component of the consumer price index for all urban consumers for the 12-month period ending with September of such preceding fiscal year. (iii) Periodic revision of standby capacity amount Not less than once every 5 fiscal years, the Secretary shall collect and analyze data on the costs of labor and delivery services at low volume obstetric hospitals and, through rulemaking, shall establish a new standby capacity amount for purposes of this section to ensure that such amount accurately reflects the minimum level of expenditures by a low volume obstetric hospital that is necessary to ensure that adequate personnel, equipment, and facilities are available at all times to provide labor and delivery services. (c) Anchor payment for low volume obstetric hospitals Not later than 3 months after the end of each fiscal year beginning with fiscal year 2028, each State shall pay to each low volume obstetric hospital in the State an amount that is equal to the amount (if any) by which\u2014 (1) the Medicaid labor and delivery revenue floor for the hospital and fiscal year; exceeds (2) the total amount of all payments made to the low volume obstetric hospital under the State plan under this title (or under a waiver of such plan) and under the State child health plan under title XXI (or under a waiver of such plan) (other than payments under this section) for labor and delivery services provided by such hospital during such fiscal year. (d) Requirements for receipt of payments No anchor payment shall be made to a low volume obstetric hospital under this section for a fiscal year unless the hospital can satisfy the following requirements: (1) Skills maintenance and training activities The hospital demonstrates to the satisfaction of the State that the hospital conducts and completes skills maintenance and training activities, including continuing education and training to support maintenance of obstetric skills, that satisfy such requirements as the Secretary, taking into consideration nationally recognized obstetrics skills, maintenance, and training standards such as standards published by the American College of Obstetricians and Gynecologists and the Association of Women\u2019s Health, Obstetric, and Neonatal Nurses, shall specify for the purposes of this section. (2) Continued provision of labor and delivery services (A) In general The hospital and the State enter into a contract under which, in exchange for such payment under this section for a fiscal year, the hospital agrees to continue to provide labor and delivery services\u2014 (i) for the period that begins with such fiscal year and ends on the last day of the second fiscal year that follows such fiscal year; and (ii) at a level that is not less than the level at which the hospital provided such services in the fiscal year to which such payment relates, unless the hospital can demonstrate that the need for services in the community has decreased and that the new level of services will be adequate to meet that need. (B) Recovery of payment in the event of breach of contract by hospital The terms of the contract between a hospital and a State required under subparagraph (A) shall provide that if the hospital does not provide labor and delivery services as required under the contract throughout the period described in such subparagraph for any reason (including in the event of the hospital\u2019s bankruptcy or closure) the State may recover the full amount of the payment under this section to which the contract relates and in the event of the hospital\u2019s bankruptcy, the State shall be given preferred creditor status for purposes of the collection of such payment. (3) Utilization of funds for labor and delivery services (A) In general The hospital and the State enter into a contract under which, in exchange for such payment under this section, the hospital agrees to utilize funds received under such payment for the provision of labor and delivery services in the community served by the hospital. (B) Recovery of payment in the event of breach of contract by hospital The terms of the contract between a hospital and a State required under subparagraph (A) shall provide that if the hospital does not utilize payment funds for labor and delivery services as required under the contract for any reason (including in the event of the hospital\u2019s bankruptcy or closure) the State may recover the full amount of the payment under this section to which the contract relates and in the event of the hospital\u2019s bankruptcy, the State shall be given preferred creditor status for purposes of the collection of such payment. (e) Treatment of payments; recovery of payments (1) In general Payments made by a State under this section for a fiscal year\u2014 (A) shall be in addition to any other payments made to hospitals for labor and delivery services under the State plan (or a waiver of such plan) under this title, under the State child health assistance plan under title XXI (or under a waiver of such plan), or under title XVIII for the fiscal year, including disproportionate share hospital payments under section 1923 or section 1886(d)(5)(F) and other supplemental payments that are not made under this section; and (B) shall be treated as medical assistance for which payment is made under section 1903(a), except that the Federal medical assistance percentage applicable to amounts expended by a State for such payments shall be equal to the enhanced FMAP determined for the State and fiscal year under section 2105(b). (2) Payments recovered by a State If a State recovers any amount of a payment made by a State under this section (whether pursuant to paragraphs (2)(B) or (3)(B) of subsection (d) or otherwise), the amount so recovered shall be treated as an overpayment recovered by the State under section 1903(d). .\n##### (c) Conforming amendments\nTitle XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) is amended as follows:\n**(1)**\nIn section 1903\u2014\n**(A)**\nin subsection (d)(6)(B)\u2014\n**(i)**\nby striking related to the total amount and inserting the following: \u201crelated to\u2014\n(i) the total amount ;\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following new clause:\n(ii) the total amount of payments made to individual providers (by provider) under section 1923A during such fiscal year. ; and\n**(B)**\nin subsection (bb)(2)(B)\u2014\n**(i)**\nin the header, by inserting and low volume obstetric hospital after DSH ; and\n**(ii)**\nby inserting or a payment made to a low volume obstetric hospital under section 1923A before the period.\n**(2)**\nIn section 1905\u2014\n**(A)**\nin subsection (cc), by striking section 1923 the second place it appears and inserting section 1923 or 1923A ; and\n**(B)**\nin subsection (ii)(2)(A), by inserting or payments to low volume obstetric hospitals described in section 1923A before the semicolon.\n#### 105. Application of adequate payment requirement and increased Federal financial participation requirements to CHIP\nSection 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (B) through (U) as subparagraphs (C) through (V), respectively; and\n**(2)**\nby inserting after subparagraph (A) the following new subparagraph:\n(B) Section 1902(a)(13)(D) and section 1905(kk) (relating to the minimum payment rate required for maternity, labor, and delivery services furnished by an eligible hospital and Federal financial participation for State expenditures for such services). .\n#### 106. Disregarding increased and additional payments to hospitals for purposes of other supplemental payments and upper payment limits\nA hospital\u2019s eligibility for any Federally funded supplemental payment (including a disproportionate share payment under section 1886(d)(5)(F) or 1923 of the Social Security Act ( 42 U.S.C. 1395ww(d)(5)(F) , 1396r\u20134)), the determination of the amount of such payment, and the application of any Federal limitation on the aggregate amount of payments that a State may make to the hospital (including any upper payment limitation), shall be determined without regard to the amount of any increase to a payment received by a hospital or any additional payment made to a hospital that is attributable to the amendments made by this title.\nII\nExpand Coverage of Maternal Health Care\n#### 201. Requiring 12-month continuous, full benefit coverage for pregnant individuals under Medicaid and CHIP\n##### (a) Medicaid\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (10), in the matter following subparagraph (G), by striking (VII) the medical assistance made available to an individual described in subsection (l)(1)(A) who is eligible for medical assistance only because of subparagraph (A)(i)(IV) or (A)(ii)(IX) shall be limited to medical assistance for services related to pregnancy (including prenatal, delivery, postpartum, and family planning services), medical assistance for services related to other conditions which may complicate pregnancy, and medical assistance for vaccines described in section 1905(a)(4)(E) and the administration of such vaccines during the period described in such section, and inserting (VII) [Repealed], ;\n**(B)**\nin paragraph (86), by striking and at the end;\n**(C)**\nin paragraph (87), by striking the period at the end and inserting ; and ; and\n**(D)**\nby inserting after paragraph (87) the following new paragraph:\n(88) provide that the State plan is in compliance with subsection (e)(16). ; and\n**(2)**\nin subsection (e)(16)\u2014\n**(A)**\nin subparagraph (A), by striking At the option of the State, the State plan (or waiver of such State plan) may provide and inserting A State plan (or waiver of such State plan) shall provide ;\n**(B)**\nin subparagraph (B), in the matter preceding clause (i), by striking by a State making an election under this paragraph and inserting under a State plan (or a waiver of such State plan) ; and\n**(C)**\nin subparagraph (C)\u2014\n**(i)**\nby striking A State making an election under this paragraph and inserting In the case of a State ; and\n**(ii)**\nby striking shall also make the election and inserting the State shall provide coverage .\n##### (b) CHIP\n**(1) In general**\nSubparagraph (K) of section 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ), as redesignated by section 105, is amended to read as follows:\n(K) Paragraphs (5) and (16) of section 1902(e) (relating to the requirement to provide medical assistance under the State plan or waiver consisting of full benefits during pregnancy and throughout the 12-month period that begins on the last day of the individual\u2019s pregnancy and ends on the last day of the month in which such 12-month period ends). .\n**(2) Conforming amendment**\nSection 2112(d)(2)(A) of the Social Security Act ( 42 U.S.C. 1397ll(d)(2)(A) ) is amended by striking the month in which the 60-day period and all that follows through pursuant to section 2107(e)(1), .\n##### (c) Effective date\n**(1) In general**\nSubject to paragraphs (2) and (3), the amendments made by subsections (a) and (b) shall take effect on the 1st day of the 1st calendar quarter that begins on or after the date that is 1 year after the date of enactment of this Act.\n**(2) Exception for State legislation**\nIn the case of a State plan under title XIX of the Social Security Act or a State child health plan under title XXI of such Act that the Secretary of Health and Human Services determines requires State legislation in order for the respective plan to meet any requirement imposed by amendments made by this subsection, the respective plan shall not be regarded as failing to comply with the requirements of such title solely on the basis of its failure to meet such an additional requirement before the 1st day of the 1st calendar quarter beginning after the close of the 1st regular session of the State legislature that begins after the date of enactment of this Act. For purposes of the previous sentence, in the case of a State that has a 2-year legislative session, each year of the session shall be considered to be a separate regular session of the State legislature.\n**(3) State option for earlier effective date**\nA State may elect to have subsection (e)(16) of section 1902 of the Social Security Act ( 42 U.S.C. 1396a ) and subparagraph (K) of section 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ), as redesignated by section 105 and amended by subsection (b) of this section, take effect with respect to the State on the 1st day of any fiscal quarter that begins before the date described in paragraph (1) and apply to amounts payable to the State for expenditures for medical assistance, child health assistance, or pregnancy-related assistance to pregnant or postpartum individuals furnished on or after such day.\n#### 202. Health homes for pregnant and postpartum women\n##### (a) Medicaid\nTitle XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) is amended by inserting after section 1945A the following new section:\n1945B. State option to provide coordinated care through a health home for pregnant and postpartum individuals (a) State option (1) In general Notwithstanding section 1902(a)(1) (relating to statewideness) and section 1902(a)(10)(B) (relating to comparability), beginning January 1, 2028, a State, at its option as a State plan amendment, may provide for medical assistance under this title to an eligible individual who chooses to\u2014 (A) enroll in a maternity health home under this section by selecting a designated provider, a team of health care professionals operating with such a provider, or a health team as the individual\u2019s maternity health home for purposes of providing the individual with pregnancy and postpartum coordinated care services; or (B) receive such services from a designated provider, a team of health care professionals operating with such a provider, or a health team that has voluntarily opted to participate in a maternity health home for eligible individuals under this section. (2) Eligible individual defined In this section, the term eligible individual means an individual\u2014 (A) who is eligible for medical assistance under the State plan (or under a waiver of such plan) for all items and services covered under the State plan (or under a waiver of such plan); (B) who is not enrolled in a health home under section 1945 or 1945A; and (C) either\u2014 (i) who is pregnant; or (ii) whose pregnancy has ended and is within the 12-month period that begins on the last day of the individual\u2019s pregnancy and ends on the last day of the month in which such 12-month period ends. (b) Qualification standards The Secretary shall establish standards for qualification as a maternity health home or as a designated provider, a team of health care professionals operating with such a provider, or a health team eligible for participation in a maternity health home for purposes of this section. In establishing such standards, the Secretary shall consider best practices and models of care used by recipients of grants under section 330P of the Public Health Service Act. Such standards shall include requiring a designated provider, a team of health care professionals operating with such a provider, and a health team designated as a maternity health home to demonstrate to the State the ability to do the following: (1) Coordinate prompt care and access to necessary maternity care services, including services provided by specialists, and programs for an eligible individual during the individual\u2019s pregnancy and the 365-day period beginning on the last day of such pregnancy. (2) Develop an individualized, comprehensive, patient-centered care plan for each eligible individual that accommodates patient preferences and, if applicable, reflects adjustments to the payment methodology described in subsection (c)(2)(B). (3) Develop and incorporate into each eligible individual\u2019s care plan, in a culturally and linguistically appropriate manner consistent with the needs of the eligible individual, ongoing home care, community-based primary care, inpatient care, social support services, health-related social needs services, behavioral health services, local hospital emergency care, and, in the event of a change in income that would result in the eligible individual losing eligibility for medical assistance under the State plan (or under a waiver of such plan), care management and planning related to a change in the eligible individual\u2019s health insurance coverage. (4) Coordinate with pediatric care providers, as appropriate. (5) Collect and report information under subsection (f)(1). (c) Payments (1) In general A State shall provide a designated provider, a team of health care professionals operating with such a provider, or a health team designated as a maternity health home with payments for the provision of health home services to each eligible individual that selects such provider, team of health care professionals, or health team as the eligible individual\u2019s health home. Payments made to a designated provider, a team of health care professionals operating with such a provider, or a health team for such services shall be treated as medical assistance for purposes of section 1903(a), except that, during the first 8 fiscal year quarters that the State plan amendment is in effect, the Federal medical assistance percentage applicable to such payments shall be equal to 90 percent. (2) Methodology The State shall specify in the State plan amendment the methodology the State will use for determining payment for the provision of pregnancy and postpartum coordinated care services or treatment during an eligible individual\u2019s pregnancy and the 365-day period beginning on the last day of such pregnancy. Such methodology for determining payment\u2014 (A) may be based on\u2014 (i) a per-member per-month basis for each eligible individual enrolled in a maternity health home; (ii) a prospective payment model, in the case of payments to Federally qualified health centers or a rural health clinics; or (iii) an alternate model of payment proposed by the State and approved by the Secretary; (B) may be adjusted to reflect, with respect to each eligible individual\u2014 (i) the severity of the risks associated with the individual\u2019s pregnancy; (ii) the severity of the risks associated with the individual\u2019s postpartum health care needs; and (iii) the level or amount of time of care coordination required with respect to the individual; and (C) shall be established consistent with section 1902(a)(30)(A). (d) Coordinating care (1) Hospital notification A State with a State plan amendment approved under this section shall require each hospital that is a participating provider under the State plan (or under a waiver of such plan) to establish procedures in the case of an eligible individual who seeks treatment in the emergency department of such hospital for\u2014 (A) providing the individual with culturally and linguistically appropriate information supplied by the State describing the respective treatment models and opportunities for the individual to access a maternity health home and its associated benefits; and (B) notifying the maternity health home in which the individual is enrolled, or the designated provider, team of health care professionals operating with such a provider, or health team treating the individual, of the individual\u2019s treatment in the emergency department and of the protocols for the maternity health home, designated provider, or team to be involved in the individual\u2019s emergency care or post-discharge care. (2) Education with respect to availability of a maternity health home (A) In general In order for a State plan amendment to be approved under this section, a State shall include in the State plan amendment a description of the State\u2019s process for\u2014 (i) educating providers participating in the State plan (or a waiver of such plan) on the availability of maternity health homes for eligible individuals, including the process by which such providers can participate in or refer an eligible individual to an approved maternity health home or a designated provider, team of health care professionals operating such a provider, or health team designated as a maternity health home; and (ii) educating eligible individuals, in a culturally and linguistically appropriate manner, on the availability of maternity health homes. (B) Outreach The process established by the State under subparagraph (A) shall include the participation of entities or other public or private organizations or entities that provide outreach and information on the availability of health care items and services to families of individuals eligible to receive medical assistance under the State plan (or a waiver of such plan). (3) Mental health coordination A State with a State plan amendment approved under this section shall consult and coordinate, as appropriate, with the Secretary in addressing issues regarding the prevention, identification, and treatment of mental health conditions and substance use disorders among eligible individuals. (4) Social and support services A State with a State plan amendment approved under this section shall consult and coordinate, as appropriate, with the Secretary in establishing means to connect eligible individuals receiving pregnancy and postpartum coordinated care services under this section with social and support services, including services made available under maternal, infant, and early childhood home visiting programs established under section 511 and services made available under section 330H or title X of the Public Health Service Act. (5) Coordination with grant program for integrated services for pregnant and postpartum women A State with a State plan amendment approved under this section shall consult and coordinate, as appropriate, with the Secretary with respect to the provision of medical assistance to eligible individuals enrolled in a maternity health home under this section and grantees delivering integrated health care services to pregnant and postpartum women under section 330P of the Public Health Service Act (including, if applicable, the State). (e) Monitoring A State shall include in the State plan amendment\u2014 (1) a methodology for tracking reductions in inpatient days and reductions in the total cost of care resulting from improved care coordination and management under this section; (2) a proposal for use of health information technology in providing an eligible individual with pregnancy and postpartum coordinated care services as specified under this section and improving service delivery and coordination across the care continuum; and (3) a methodology for tracking prompt and timely access to medically necessary care for eligible individuals from out-of-State providers. (f) Data collection (1) Provider reporting requirements In order to receive payments from a State under subsection (c), a maternity health home, or a designated provider, a team of health care professionals operating with such a provider, or a health team designated as a maternity health home, shall report to the State, at such time and in such form and manner as may be required by the State, including through a health information exchange or other public health data sharing entity, the following information: (A) With respect to each such designated provider, team of health care professionals operating with such a provider, and health team designated as a maternity health home, the name, National Provider Identification number, address, and specific health care services offered to be provided to any eligible individual who has selected such provider, team of health care professionals, or health team as the eligible individual\u2019s maternity health home. (B) Information on all other applicable measures for determining the quality of services provided by such provider, team of health care professionals, or health team. (C) Information concerning the factors described in paragraph (2)(A)(vi) received from health risk assessments of eligible individuals conducted and completed by the designated provider, team of health care professionals operating with such a provider, or health team designated as a maternity health home. (D) Such other information as the Secretary shall specify in guidance. (2) State reporting requirements (A) Comprehensive report A State with a State plan amendment approved under this section shall report to the Secretary (and, upon request, to the Medicaid and CHIP Payment and Access Commission), at such time, but at a minimum annually, and in such form and manner determined by the Secretary to be reasonable and minimally burdensome, the following information: (i) Information described in paragraph (1). (ii) The number and, to the extent available and while maintaining all relevant privacy and confidentially protections, disaggregated demographic information (including information on geography) of eligible individuals who have enrolled in a maternity health home pursuant to this section. (iii) The number of maternity health homes in the State designated under this section. (iv) The medical conditions or factors that contribute to severe maternal morbidity among eligible individuals enrolled in maternity health homes in the State. (v) The extent to which such individuals receive health care items and services under the State plan before, during, and after an individual\u2019s enrollment in such a maternity health home. (vi) Where applicable, mortality data and data for the associated causes of pregnancy-related death for eligible individuals enrolled in a maternity health home under this section, in accordance with subsection (g). For deaths occurring postpartum, such data shall distinguish between deaths occurring up to 42 days postpartum and deaths occurring between 43 days to up to 1 year postpartum. Where applicable, data reported under this clause shall be reported alongside comparable data from a State\u2019s maternal mortality review committee, as established in accordance with section 317K(d) of the Public Health Service Act, for purposes of further identifying and comparing statewide trends in maternal mortality among populations participating in the maternity health home under this section. (B) Implementation report Not later than 18 months after a State has a State plan amendment approved under this section, the State shall submit to the Secretary, and make publicly available on the appropriate State website, a report on how the State is implementing the option established under this section, including through any best practices adopted by the State. (g) Confidentiality A State with a State plan amendment under this section shall establish confidentiality protections for the purposes of subsection (f)(2)(A) to ensure, at a minimum, that there is no disclosure by the State of any identifying information about any specific eligible individual enrolled in a maternity health home or any maternal mortality case, and that all relevant confidentiality and privacy protections, including the requirements under section 1902(a)(7)(A), are maintained. (h) Rule of construction Nothing in this section shall be construed to require\u2014 (1) an eligible individual to enroll in a maternity health home under this section; or (2) a designated provider or health team to act as a maternity health home and provide services in accordance with this section if the provider or health team does not voluntarily agree to act as a maternity health home. (i) Planning grants (1) In general Beginning January 1, 2027, from the amount appropriated under paragraph (2), the Secretary shall award planning grants to States for purposes of developing and submitting a State plan amendment under this section. The Secretary shall award a grant to each State that applies for a grant under this subsection and meets the application criteria established by the Secretary, and the Secretary may determine the amount of the grant based on the merits of the application and the goal of the State to prioritize health outcomes for eligible individuals. A planning grant awarded to a State under this subsection shall remain available until expended. (2) Appropriation There are authorized to be appropriated to the Secretary $50,000,000 for fiscal year 2027, for the purposes of making grants under this subsection, to remain available until expended. (3) Limitation The total amount of payments made to States under this subsection shall not exceed $50,000,000. (j) Additional definitions In this section: (1) Designated provider The term designated provider means a physician (including an obstetrician-gynecologist or, if applicable, a certified nurse midwife, or certified professional midwife who meets or exceeds the education and training standards of the International Confederation of Midwives and who is licensed to practice within the State), a hospital, clinical practice or clinical group practice, rural health clinic, community health center, community mental health center, or any other entity or provider that is determined by the State and approved by the Secretary to be qualified to be a maternity health home on the basis of documentation evidencing that the entity or provider has the systems, expertise, and infrastructure in place to provide pregnancy and postpartum coordinated care services. Such term may include providers who are employed by, or affiliated with, a hospital. (2) Health team The term health team has the meaning given such term for purposes of section 3502 of Public Law 111\u2013148 . (3) Maternity health home The term maternity health home means a designated provider (including a provider that operates in coordination with a team of health care professionals) or a health team that is selected by an eligible individual to provide pregnancy and postpartum coordinated care services. (4) Pregnancy and postpartum coordinated care services (A) In general The term pregnancy and postpartum coordinated care services means items and services related to the coordination of care for comprehensive and timely high-quality, culturally and linguistically appropriate, services described in subparagraph (B) that are provided by a designated provider, a team of health care professionals operating with such a provider, or a health team designated as a maternity health home. (B) Services described (i) In general The services described in this subparagraph shall include with respect to a State electing the State plan amendment option under this section, any medical assistance for items and services for which payment is available under the State plan or under a waiver of such plan. (ii) Other items and services In addition to medical assistance described in clause (i), the services described in this subparagraph shall include the following: (I) Any item or service for which medical assistance is otherwise available under the State plan (or a waiver of such plan) related to the treatment of an individual during the individual\u2019s pregnancy and the 1-year period beginning on the last day of such pregnancy, including mental health and substance use disorder services. (II) Comprehensive care management. (III) Care coordination (including with pediatricians as appropriate), health promotion, and providing access to the full range of maternal, obstetric, and gynecologic services, including services from out-of-State providers. (IV) Comprehensive transitional care, including appropriate follow-up, from inpatient to other settings. (V) Patient and family support (including authorized representatives). (VI) Referrals to community and social support services, if relevant. (VII) Use of health information technology to link services, as feasible and appropriate. (5) Team of health care professionals The term team of health care professionals means a team of health care professionals (as described in the State plan amendment under this section) that may\u2014 (A) include\u2014 (i) physicians, including gynecologist-obstetricians, certified nurse midwives, or certified professional midwives who meet or exceed the education and training standards of the International Confederation of Midwives and who are licensed to practice within the State, family physicians, primary care physicians, pediatricians, and other professionals such as physicians assistants, advance practice nurses, nurses, nurse care coordinators, dietitians, nutritionists, social workers, behavioral health professionals, physical counselors, physical therapists, occupational therapists, or any professionals that assist in prenatal care, delivery, or postpartum care for which medical assistance is available under the State plan or a waiver of such plan and determined to be appropriate by the State and approved by the Secretary; (ii) an entity or individual who is designated to coordinate such care delivered by the team; and (iii) when appropriate and if otherwise eligible to furnish items and services that are reimbursable as medical assistance under the State plan or under a waiver of such plan, doulas, community health workers, translators and interpreters, and other individuals with culturally appropriate and trauma-informed expertise; and (B) provide care at a facility that is freestanding, virtual, or based at a hospital, community health center, community mental health center, rural health clinic, clinical practice or clinical group practice, academic health center, or any entity determined to be appropriate by the State and approved by the Secretary. .\n##### (b) Applicability to CHIP\nSection 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ), as amended by section 105, is amended by adding at the end the following new subparagraph:\n(W) Section 1945B (relating to optional health homes for pregnant and postpartum individuals). .\n#### 203. Guidance on supporting and improving access to Medicaid and CHIP coverage of services provided by doulas and certain maternal health professionals\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall issue and publish guidance for States concerning options for supporting and improving access to coverage and payment under a State plan under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) or under a waiver of such plan, and under a State child health plan under title XXI of such Act ( 42 U.S.C. 1397aa et seq. ) or under a waiver of such plan, for services provided by doulas, certified nurse midwives, certified midwives, or certified professional midwives, who meet or exceed the education and training standards of the International Confederation of Midwives and who are licensed to practice within the State and certain maternal health professionals (specified by the Secretary)\u2014\n**(1)**\nin rural areas;\n**(2)**\nacross a continuum of care; and\n**(3)**\namong varied provider settings and payment and care models, including managed care.\n#### 204. Medicaid and CHIP increased financial support for depression and anxiety screening during the perinatal and postpartum periods\n##### (a) Medicaid\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ), as amended by section 103, is further amended\u2014\n**(1)**\nin the first sentence of subsection (b), by striking subsection (a)(4)(D) and inserting subsections (a)(4)(D) and (ll) ; and\n**(2)**\nby adding at the end the following:\n(ll) Increased FMAP for depression and anxiety screening during the perinatal and postpartum periods (1) In general For purposes of clause (5) of the first sentence of subsection (b), services described in this subsection are screening services provided to an individual who is eligible for such assistance on the basis of being pregnant that include at a minimum\u2014 (A) during the perinatal period, at least 1 screening for depression and anxiety symptoms using a standardized, validated tool; and (B) during the postpartum period, a full assessment of mood and emotional well-being, including screening for postpartum depression and anxiety, using a standardized, validated tool. (2) Exclusion from territorial caps The additional amount paid to a territory for expenditures for medical assistance for services described in paragraph (1) as a result of the application of clause (5) of the first sentence of subsection (b) shall not be taken into account for purposes of applying payment limits under subsections (f) and (g) of section 1108. .\n##### (b) CHIP\nSection 2105(c) of the Social Security Act ( 42 U.S.C. 1397ee(c) ) is amended by adding at the end the following new paragraph:\n(13) Enhanced payment for depression and anxiety screening during the perinatal and postpartum periods Notwithstanding subsection (b), the enhanced FMAP with respect to payments under subsection (a) for expenditures under the State child health plan (or a waiver of such plan) shall be increased by 1 percentage point with respect to expenditures for services described in section 1905(ll)(1) that are provided under the plan (or waiver) to an individual who is eligible for such assistance on the basis of being pregnant (including pregnancy-related assistance provided to a targeted low-income pregnant woman (as defined in section 2112(d)), pregnancy-related assistance provided to an individual who is eligible for such assistance through application of section 1903(v)(4)(A)(i) under section 2107(e)(1), or any other assistance under the plan (or waiver) provided to an individual who is eligible for such assistance on the basis of being pregnant) and during the 12-month period that begins on the last day of the individual\u2019s pregnancy and ends on the last day of the month in which such 12-month period ends (including any such assistance provided during the month in which such period ends). .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the first day of the first fiscal quarter that begins on or after the date that is 1 year after the date of enactment of this section.\n#### 205. Presumptive eligibility for pregnant individuals\n##### (a) In general\n**(1) Requirement**\nSection 1920(a) of the Social Security Act ( 42 U.S.C. 1396r\u20131(a) ) is amended by striking may provide and inserting shall provide .\n**(2) Application**\nSection 1920 of the Social Security Act ( 42 U.S.C. 1396r\u20131 ) is amended by adding at the end the following new subsection:\n(f) Application A State shall provide to a pregnant woman a presumptive eligibility period in accordance with this section without regard to whether the individual would otherwise qualify for a presumptive eligibility period the State has elected to provide under section 1920A, 1920B, or 1920C. .\n##### (b) Conforming amendments\n**(1)**\nSection 1902(a)(47) of the Social Security Act ( 42 U.S.C. 1396a(a)(47) ) is amended to read as follows:\n(47) provide\u2014 (A) (i) for making ambulatory prenatal care available to pregnant women during a presumptive eligibility period in accordance with section 1920; and (ii) at the option of the State\u2014 (I) for making medical assistance for items and services described in subsection (a) of section 1920A available to children during a presumptive eligibility period in accordance with such section; (II) for making medical assistance available to individuals described in subsection (a) of section 1920B during a presumptive eligibility period in accordance with such section; and (III) for making medical assistance available to individuals described in subsection (a) of section 1920C during a presumptive eligibility period in accordance with such section; and (B) that any hospital that is a participating provider under the State plan may elect to be a qualified entity for purposes of determining, on the basis of preliminary information, whether any individual is eligible for medical assistance under the State plan or under a waiver of the plan for purposes of providing the individual with medical assistance during a presumptive eligibility period, in the same manner, and subject to the same requirements, as apply with respect to populations described in section 1920, 1920A, 1920B, or 1920C (without regard to whether the State has elected to provide for a presumptive eligibility period under sections 1920A, 1920B, or 1920C), subject to such guidance as the Secretary shall establish; .\n**(2)**\nSection 1920(e) of the Social Security Act ( 42 U.S.C. 1396r\u20131(e) ) is amended\u2014\n**(A)**\nby striking If the State has elected the option to provide a presumptive eligibility period under this section or section 1920A, the and inserting The ; and\n**(B)**\nby striking 1920A, subject to and inserting 1920A (if the State has elected the option), subject to .\n**(3)**\nSection 2107(e)(1)(R) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1)(R) ) is amended by inserting 1920 (relating to presumptive eligibility for pregnant women and section before 1920A .\n**(4)**\nSection 2112(c) of the Social Security Act ( 42 U.S.C. 1397ll(c) ) is amended\u2014\n**(A)**\nin the heading, by striking Option To Provide ; and\n**(B)**\nby striking may elect and inserting shall elect .\nIII\nInvest in the Maternal Health Care Workforce\n#### 301. Emergency obstetric workforce support\n##### (a) In general\nSection 203A of the Public Health Service Act ( 42 U.S.C. 204a ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), in the matter preceding subparagraph (A), by inserting and urgent maternal health care needs after public health care needs ;\n**(B)**\nin paragraph (3), by inserting or urgent maternal health care need after public health care need ;\n**(C)**\nin paragraph (5)\u2014\n**(i)**\nin subparagraph (C), by striking or at the end;\n**(ii)**\nin subparagraph (D), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following:\n(E) any urgent need, not rising to the level of an emergency described in subparagraph (D), that, in the judgment of the Secretary, if not addressed, could result in an emergency that would be appropriate for the deployment of the Commissioned Corps. ; and\n**(D)**\nby adding at the end the following:\n(6) Urgent maternal health care need (A) In general For purposes of this section and section 214, the term urgent maternal health care need , with respect to an area, means a maternal health care need, as determined by the Secretary, in consultation with the Attorney General, arising as a result of the closure or imminent closure of a hospital or other health care facility in such area, or the loss of workers employed by such hospital or health care facility who are trained to provide maternal health care services. (B) Considerations In determining whether there is an urgent maternal health care need for purposes of subparagraph (A) with respect to an area, the Secretary shall consider whether such closure, imminent closure, or loss of workers has impacted access by individuals in such area to a full range of maternal health care services, including prenatal services, labor and delivery services, postnatal services, maternal and postpartum mental health services, behavioral health services, and reproductive health services. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting or urgent maternal health care needs after public health care needs ; and\n**(B)**\nin each of paragraphs (2) and (4)(B), by inserting or urgent maternal health care need after public health care need ; and\n**(3)**\nin subsection (c), by inserting or urgent maternal health care need after public health care need .\n##### (b) Detail of personnel\nSection 214 of the Public Health Service Act ( 42 U.S.C. 215 ) is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (f);\n**(2)**\nby inserting after subsection (d) the following:\n(e) (1) Upon the request of an eligible entity with respect to a hospital or other health care facility the closure, imminent closure, or loss of workers of which led to an urgent maternal health care need in an area, personnel may be detailed by the Secretary for the purpose of assisting such eligible entity in work related to such urgent maternal health care need. (2) (A) Personnel detailed under paragraph (1) shall be paid from applicable appropriations of the Service. (B) In the case of detail of personnel under paragraph (1) to be paid from applicable Service appropriations, the Secretary may condition such detail on an agreement by the eligible entity concerned that such eligible entity concerned shall reimburse the United States for a portion of the amount of such payments made by the Service. (C) The services of personnel while detailed pursuant to this subsection shall be considered as having been performed in the Service for purposes of the computation of basic pay, promotion, retirement, compensation for injury or death, and the benefits provided by section 212. (3) The Secretary may condition a detail of personnel under paragraph (1) on an agreement by the eligible entity concerned that such eligible entity concerned shall\u2014 (A) in the case of an imminent closure or a loss of workers, as determined by the Secretary\u2014 (i) maintain the maternal health care services in the applicable area to the maximum extent practicable, including by hiring temporary workers, until the date on which the personnel are detailed to such area; and (ii) submit to the Secretary a plan for hiring and retaining health practitioners in the short- and long-term, both during periods in which personnel are detailed to such applicable area and periods in which personnel are not detailed to such applicable area; (B) in the case of a closure, submit to the Secretary a plan for working with, as applicable, State and local agencies and local stakeholders to transition patients to alternate sources of safe maternal health care services; and (C) commit to an assessment by the Secretary of the workplace practices of such eligible entity concerned, if applicable. (4) In this subsection\u2014 (A) the term eligible entity means\u2014 (i) a State; (ii) a political subdivision of a State; or (iii) a Tribal, nonprofit, or other health care entity; and (B) the term personnel means an employee or officer of the Commissioned Corps. ; and\n**(3)**\nin subsection (f) (as so redesignated), by inserting or an urgent maternal health care need before the period at the end.\n##### (c) Funding for commissioned corps of the public health service\nSection 203 of the Public Health Service Act ( 42 U.S.C. 204 ) is amended by adding at the end the following:\n(e) Operations of the Commissioned Corps of the Public Health Service (1) In general The Secretary shall carry out duties and responsibilities relating to the operations of the Commissioned Corps of the Service, including the following: (A) Enhance the processes and systems of the Service\u2019s Headquarters operations. (B) Maximize the force management, required training opportunities (as determined by the Secretary under section 203A(a)(1)), operational capacity, and mission readiness of the Regular Corps, the Ready Reserve Corps, and the Public Health Emergency Response Strike Teams, a subcomponent of the Regular Corps. (C) Recruit and retain qualified professionals suited to serving underserved and vulnerable communities by\u2014 (i) improving onboarding timelines, providing officer placements to align with mission needs, ensuring adequate officer morale and wellness resources, and incentivizing recruiters and recruits; and (ii) expanding training opportunities, including training of personnel to deliver maternal health care services, providing credentialing support for high demand skill sets, and enriching leadership and research potential. (D) Improve deployment processes and prepare mission teams to execute routine and emergent public health events. (E) Establish a legislative liaison office to carry out legislative affairs functions under the direction of the Secretary. (2) Authorization of appropriations In addition to amounts otherwise authorized to be appropriated for the Commissioned Corps of the Service, there is authorized to be appropriated to the Secretary to carry out paragraph (1) $150,000,000 for fiscal year 2027 and each fiscal year thereafter. .\n#### 302. Streamlined screening and enrollment of providers of maternity, labor, and delivery services in neighboring States\n##### (a) Application to Medicaid\nSection 1902(kk) of the Social Security Act ( 42 U.S.C. 1396a(kk) ) is amended by adding at the end the following new paragraph:\n(10) Streamlined enrollment process for eligible out-of-State providers of maternity, labor, and delivery services (A) In general The State adopts and implements a process that enables an eligible out-of-State provider to enroll as a provider in the State plan without imposing any screening requirements that are in addition to the requirements imposed on in-State providers. An eligible out-of-State provider that enrolls in the State plan through such process shall be so enrolled for a 5-year period (unless the provider is terminated or excluded from participation during such period) and may revalidate such enrollment through such process for subsequent 5-year periods. (B) Eligible out-of-State provider In this paragraph, the term eligible out-of-State provider means, with respect to a State, a provider\u2014 (i) that furnishes maternity, labor, and delivery services (as defined in subsection (uu)(1)), or provides orders or referrals for such services, for which payment is available under the State plan of the State; (ii) that is located in a neighboring State (as defined by the Secretary); (iii) with respect to which the Secretary has determined there is a limited risk of fraud, waste, or abuse for purposes of determining the level of screening to be conducted under section 1866(j)(2)(B); (iv) that has been screened under such section 1866(j)(2)(B) for purposes of enrolling in the Medicare program under title XVIII or the State plan of the State in which such provider is located; and (v) that has not been excluded from participation in the Medicare program under such title or the Medicaid program under this title. .\n##### (b) Conforming amendments\n**(1)**\nSection 1902(a)(77) of the Social Security Act ( 42 U.S.C. 1396a(a)(77) ) is amended by inserting enrollment, after screening, .\n**(2)**\nSection 1902(kk) of such Act ( 42 U.S.C. 1396a(kk) ), as amended by subsection (a), is further amended\u2014\n**(A)**\nin the subsection heading, by inserting Enrollment, after Screening, ; and\n**(B)**\nin paragraph (9), by striking Nothing and inserting Except as provided in paragraph (10), nothing .\n##### (c) Application to CHIP\nSection 2107(e)(1)(G) of such Act ( 42 U.S.C. 1397gg(e)(1)(G) ) is amended by inserting enrollment, after screening, .\n##### (d) Guidance on screening and enrolling out-of-State providers of maternity, labor, and delivery services\nNot later than January 1, 2028, the Secretary of Health and Human Services shall issue (and update as the Secretary determines necessary) guidance to State Medicaid and CHIP directors on best practices for screening and enrolling out-of-State providers of maternity, labor, and delivery services in accordance with paragraph (10) of section 1902(kk) of the Social Security Act ( 42 U.S.C. 1396a(kk) ) and section 2107(e)(1)(G) of such Act ( 42 U.S.C. 1397gg(e)(1)(G) ) (as added and amended by this section) and including best practices for screening and enrolling out-of-State providers in managed care plans.\n##### (e) Effective date\nThe amendments made by this section take effect on January 1, 2028.\nIV\nRequiring Public Communication of Obstetrics Data and Unit Closures\n#### 401. Timely notifications of impending hospital obstetric unit closures\n##### (a) In general\nSection 1866(a)(1) of the Social Security Act ( 42 U.S.C. 1395cc(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (X), by striking and at the end;\n**(2)**\nin subparagraph (Y)(ii)(V), by striking the period and inserting , and ; and\n**(3)**\nby inserting after subparagraph (Y) the following new subparagraph:\n(Z) beginning 180 days after the date of the enactment of this subparagraph, in the case of a hospital, not less than 180 days prior to the closure of any obstetric unit of the hospital, to submit to the Secretary, any relevant local and State agencies, and the community a notification, which shall include\u2014 (i) a report analyzing the impact the closure will have on the community, including data on any adverse outcomes and increase in costs relating to obstetric services for such community; (ii) steps the hospital will take to identify other health care providers that can alleviate any service gaps as a result of the closure; (iii) the cause of the closure of such obstetric unit; (iv) data regarding historic transportation costs related to obstetric services in such community; and (v) any additional information as may be required by the Secretary. .\n##### (b) State requirement To post reports\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ), as amended by section 201(a)(1), is further amended\u2014\n**(1)**\nin paragraph (87), by striking and at the end;\n**(2)**\nin paragraph (88), by striking the period at the end and inserting ; and ; and\n**(3)**\nby inserting after paragraph (88) the following new paragraph:\n(89) provide that the State will make publicly available, on the website of any relevant State agency, any report received by the State from a hospital pursuant to section 1866(a)(1)(Z)(i). ; and\n#### 402. Collection of data relating to hospital labor and delivery services\nSection 1866(a)(1) of the Social Security Act ( 42 U.S.C. 1395cc(a)(1) ), as amended by section 401, is amended\u2014\n**(1)**\nin subparagraph (Y)(ii)(V), by striking and at the end;\n**(2)**\nin subparagraph (Z), by striking the period and inserting , and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(AA) in the case of a hospital, to include in cost reports submitted under this title for cost reporting periods beginning on or after July 1, 2026\u2014 (i) the number of births that occurred at such hospital during the cost reporting period, delineated by the number of cesarean births and vaginal births; (ii) the number of antenatal and postpartum transfers from the hospital to other hospitals; (iii) data on the number and characteristics of the staff providing labor and delivery services at such hospital; (iv) the expenses the hospital incurred for providing labor and delivery services at such hospital, including nursing care, anesthesia, and operating room services; (v) the amount the hospital spent for on-call coverage for labor and delivery services by physicians and midwives; and (vi) the amount and sources of revenue received by such hospital for labor and delivery services, including payments received for\u2014 (I) items and services furnished to individuals eligible for coverage under a State plan under title XIX (or a waiver of such a plan); (II) items and services furnished to individuals with other forms of health insurance or third-party coverage; and (III) items and services furnished to individuals without health insurance or other source of third party coverage. .",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-06-12",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3942",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keeping Obstetrics Local Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-16",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2085",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Postpartum Lifeline Act",
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
        "name": "Health",
        "updateDate": "2025-07-09T12:59:56Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2059is.xml"
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
      "title": "Keeping Obstetrics Local Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keeping Obstetrics Local Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles XIX and XXI of the Social Security Act to enhance financial support for rural and safety net hospitals providing maternity, labor, and delivery services to vulnerable populations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-03T04:18:27Z"
    }
  ]
}
```
