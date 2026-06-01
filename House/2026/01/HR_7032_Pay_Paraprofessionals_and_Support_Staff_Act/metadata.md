# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7032?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7032
- Title: Pay Paraprofessionals and Support Staff Act
- Congress: 119
- Bill type: HR
- Bill number: 7032
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-02-02T14:47:02Z
- Update date including text: 2026-02-02T14:47:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7032",
    "number": "7032",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "G000586",
        "district": "4",
        "firstName": "Jes\u00fas",
        "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
        "lastName": "Garc\u00eda",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Pay Paraprofessionals and Support Staff Act",
    "type": "HR",
    "updateDate": "2026-02-02T14:47:02Z",
    "updateDateIncludingText": "2026-02-02T14:47:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CT"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MN"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "OH"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "GA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "HI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NV"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "DC"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NM"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MI"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7032ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7032\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Garc\u00eda of Illinois (for himself, Mrs. Hayes , Mrs. Grijalva , Mr. Casar , Ms. Craig , Mr. Krishnamoorthi , Ms. Tlaib , Mr. Landsman , Mr. Johnson of Georgia , Ms. Budzinski , Mrs. Cherfilus-McCormick , Mr. Carbajal , Mr. Garcia of California , Mr. Carson , Ms. Chu , Ms. Tokuda , Ms. Titus , Mr. Evans of Pennsylvania , Ms. Norton , Ms. Stansbury , Mr. Boyle of Pennsylvania , Mrs. Ramirez , Mr. Thanedar , Ms. Garcia of Texas , Ms. Wilson of Florida , and Mr. Davis of Illinois ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo ensure that paraprofessionals and education support staff are paid a living wage.\n#### 1. Short title\nThis Act may be cited as the Pay Paraprofessionals and Support Staff Act .\n#### 2. Pay Paraprofessionals and Education Support Staff Act\n##### (a) Definitions\nIn this section:\n**(1) ESEA**\nThe terms English learner , local educational agency , paraprofessional , professional development , Secretary , and State have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Annual adjustment percentage**\nThe term annual adjustment percentage means, with respect to a fiscal year, a percentage equal to the estimated percentage change in the Consumer Price Index, as determined by the Secretary, for the most recent calendar year ending prior to the beginning of such fiscal year.\n**(3) Minimum salary for paraprofessional and education support staff**\n**(A) In general**\nThe term minimum salary for paraprofessional and education support staff means an amount, determined by the State, that all full-time equivalent employees employed by a local educational agency are required by the State to be compensated by such agency as their annual base salary, and which\u2014\n**(i)**\nis greater than the amount described in subparagraph (B); and\n**(ii)**\nincreases as the experience of such school staff increases.\n**(B) Indexing salary growth to inflation**\n**(i) Fiscal years 2026 through 2030**\nFor each of fiscal years 2026 through 2030, the amount described in this subparagraph is $45,000.\n**(ii) Fiscal years 2031 and after**\nFor each fiscal year in the fiscal year period 2031 through 2035 and in each subsequent 5 fiscal year period, the amount described this subparagraph shall be equal to the amount applicable for each fiscal year in the previous 5 fiscal year period, increased by the greater of\u2014\n**(I)**\nthe aggregate annual adjustment percentage over the previous 5 fiscal years; or\n**(II)**\n2 percent of the amount applicable under this subsection for the previous 5 fiscal year period.\n**(4) Minimum wage for paraprofessional and education support staff**\n**(A) In general**\nThe term minimum wage for paraprofessional and education support staff means an amount, determined by the State, that all part-time equivalent staff employed by a local educational agency are required by the State to be paid by such agency, and which\u2014\n**(i)**\nis greater than the amount described in subparagraph (B); and\n**(ii)**\nincreases as the experience of such school staff increases.\n**(B) Indexing salary growth to inflation**\n**(i) Fiscal years 2026 through 2030**\nFor each of fiscal years 2026 through 2030, the amount described in this subparagraph is $30.00 an hour.\n**(ii) Fiscal years 2031 and after**\nFor each fiscal year in the fiscal year period 2031 through 2035 and in each subsequent 5 fiscal year period, the amount described this subparagraph shall be equal to the amount applicable for each fiscal year in the previous 5 fiscal year period, increased by the greater of\u2014\n**(I)**\nthe aggregate annual adjustment percentage over the previous 5 fiscal years; or\n**(II)**\n2 percent of the amount applicable under this subsection for the previous 5 fiscal year period.\n##### (b) Purpose\nThe purpose of this section is to ensure that paraprofessionals and education support staff, who are the backbone of our Nation\u2019s public education system, are\u2014\n**(1)**\npaid a living wage, which means\u2014\n**(A)**\na minimum salary for paraprofessional and education support staff; or\n**(B)**\na minimum wage for paraprofessional and education support staff;\n**(2)**\ncompensated in a manner that recognizes some regions may have higher costs of living and therefore necessitate higher minimum salaries or wages;\n**(3)**\nrecognized as public servants who provide essential services that keep our Nation\u2019s public schools running and our students thriving; and\n**(4)**\nprovided safe working conditions and treated with the respect and dignity they deserve.\n##### (c) Authorization and appropriations\nIn addition to amounts otherwise available, there are authorized to be appropriated and there are appropriated out of any money in the Treasury not otherwise appropriated, to the Department of Education, to carry this section\u2014\n**(1)**\nfor fiscal year 2026, $25,000,000,000; and\n**(2)**\nfor each succeeding fiscal year, the amount appropriated under this section for the preceding fiscal year, increased by the annual adjustment percentage.\n##### (d) Authorization of grants\n**(1) Reservations**\nFrom the total amount appropriated under subsection (c) for a fiscal year, the Secretary shall reserve not more than\u2014\n**(A)**\n1 percent to provide grants, contracts, or cooperative agreements to regional educational laboratories (established under section 174 of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9564 )) or qualified nonprofit organizations to assist States that receive grants under this section carry out applied research or evaluations in providing paraprofessionals and education support staff with opportunities for personnel preparation, professional development, credentials, or certifications, such as to assist in the provision of special education and related services or to serve English learners; and\n**(B)**\n1 percent for technical assistance and program administration of this section.\n**(2) Grants**\nThe Secretary shall award grants to States from allotments under paragraph (3) to ensure that all local educational agencies have the resources necessary to pay paraprofessionals and education support staff a living wage, which means\u2014\n**(A)**\nthe minimum salary for paraprofessional and education support staff; or\n**(B)**\na minimum wage for paraprofessional and education support staff.\n**(3) Allotments**\nFrom the amounts appropriated under subsection (b) that are remaining after making the reservations described in paragraph (1) for a fiscal year, the Secretary shall allot to each State that has submitted an approved application under subsection (d), an amount that bears the same relationship to the remainder as the amount the State received under part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ) for the preceding fiscal year bears to the amount all States received under that subpart for the preceding fiscal year.\n##### (e) State application\nIn order to receive a grant under this section, a State shall submit an application to the Secretary at such time, in such manner, and including such information as the Secretary may reasonably require, including the following:\n**(1)**\nA timeline, consistent with the goals required under paragraph (2), to ensure that, not later than 4 years after the receipt of a grant under this section\u2014\n**(A)**\nthe annual base salary of a full-time equivalent employee employed by a local educational agency in the State is not less than the minimum salary for paraprofessional and education support staff, as determined by the State; and\n**(B)**\nall part-time equivalent staff employed by a local educational agency in the State are paid not less than the minimum wage for paraprofessional and education support staff, as determined by the State.\n**(2)**\nFor each fiscal year in the timeline specified in paragraph (1), statewide annual goals for increasing average salary or wage baselines of paraprofessionals and education support staff in a manner that\u2014\n**(A)**\nannually proposes a percentage increase in the average wage or salary of paraprofessionals and education support staff;\n**(B)**\nprovides for the first increase to occur not later than the second fiscal year a State receives a grant under this section; and\n**(C)**\nmakes significant progress toward ensuring that, by the end of the timeline described in subparagraph (A)\u2014\n**(i)**\nthe annual base salary of a full-time equivalent employee employed by a local educational agency in the State is not less than the minimum salary for paraprofessional and education support staff, as determined by the State; and\n**(ii)**\nall part-time equivalent staff employed by a local educational agency in the State are paid not less than the minimum wage for paraprofessional and education support staff, as determined by the State.\n**(3)**\nThe State\u2019s proposed formula to subgrant funds to local educational agencies as described in subsection (g) in a manner that ensures\u2014\n**(A)**\nlocal educational agencies that serve a high number or percentage of students from low-income backgrounds receive substantial subgrant allocations that enable such agencies to meet the requirements described in subparagraphs (A) and (B) of paragraph (1) not later than 2 years after the receipt of a subgrant; and\n**(B)**\nall remaining local educational agencies in the State meet the State\u2019s requirements in the timeline described in paragraph (1).\n##### (f) Improving paraprofessional and school staff wages and salaries\n**(1) State reservation**\nA State that receives a grant under this section may reserve not more than 2 percent of the total grant amount received by the State for technical assistance, administrative purposes, and statewide efforts to provide paraprofessionals and education support staff with opportunities for personnel preparation, professional development, credentials, or certifications, such as to assist in the provision of special education and related services or to serve English learners.\n**(2) Improving wages and salaries**\n**(A) In general**\nSubject to subparagraph (B), a State that receives a grant under this section shall ensure that, within a timeline determined by the State under subsection (e)(1) and approved by the Secretary\u2014\n**(i)**\nthe annual base salary of a full-time equivalent employee employed by a local educational agency in the State is not less than the minimum salary for paraprofessional and education support staff, as determined by the State; and\n**(ii)**\nall part-time equivalent staff employed by a local educational agency in the State are paid not less than the minimum wage for paraprofessional and education support staff, as determined by the State.\n**(B) Timing**\nThe Secretary shall ensure that, by not later than 4 years after the date of implementation of the final regulations issued under this Act, each State that receives a grant under this section meets the salary and wage requirements specified in subparagraph (A).\n##### (g) Subgrants to local educational agencies\n**(1) Allocation**\nEach State shall allocate not less than 98 percent of the grant funds awarded to the State under this section as subgrants to local educational agencies (including charter schools that are local educational agencies) in the State under the formula determined by the State under subsection (e)(3) and approved by the Secretary.\n**(2) Uses of subgrant funds**\nA local educational agency that receives a subgrant under paragraph (1)\u2014\n**(A)**\nshall use the subgrant funds to comply with the State\u2019s requirements in accordance with subsection (e) guaranteeing that no full-time equivalent employee of the agency is paid less than the minimum salary for paraprofessional and education support staff and no part-time equivalent employee of the agency is paid less than the minimum wage for paraprofessional and education support staff; and\n**(B)**\nmay use subgrant funds\u2014\n**(i)**\nto increase salaries or wages for teachers, paraprofessionals, specialized instructional support personnel, classified school employees, principals, other school leaders, school librarians, school bus drivers, and other staff across their careers; and\n**(ii)**\nto provide paraprofessionals and education support staff with opportunities for personnel preparation, professional development, credentials, or certifications, such as to assist in the provision of special education and related services or to serve English learners.\n**(3) Contracted staff**\n**(A) In general**\nA local educational agency that receives a subgrant under this section shall ensure that staff employed by such agency or in any contract such agency enters into, are paid an amount not less than the minimum salary for paraprofessionals and education support staff or the minimum wage for paraprofessionals and education support staff in the State.\n**(B) Monitoring**\nA State that receives a grant under this section shall monitor local educational agencies for compliance with subparagraph (A).\n##### (h) Rules\n**(1) Rule of construction for collective bargaining**\n**(A) In general**\nSubject to subparagraph (B), nothing in this Act shall be construed to alter or otherwise affect the rights, remedies, and procedures afforded to school or local educational agency employees under Federal, State, or local laws (including applicable regulations or court orders) or under the terms of collective bargaining agreements, memoranda of understanding, or other agreements between such employers and their employees.\n**(B) Compliance**\nSubparagraph (A) shall not be construed to exempt a State, local educational agency, or school from complying with salary or wage requirements in this Act or from negotiating in compliance with State labor laws to comply with this Act.\n**(2) Rule of construction for additional pay or other salary augmenting systems**\nNothing in this Act shall be construed to prevent States or local educational agencies from supplementing the annual base salary of teachers, paraprofessionals, education support staff, or other staff employed by such agencies\u2014\n**(A)**\nfor additional skills, knowledge, duties, and responsibilities;\n**(B)**\nby salary systems that increase teachers\u2019 compensation through supplemental pay that is not part of an annual base salary; or\n**(C)**\nthrough the provision of bonuses, stipends, or awards.\n**(3) No waiver authority**\nSection 8401 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7861 ) shall not apply to this Act.\n**(4) Supplement not supplant**\n**(A) In general**\nA State shall use Federal funds received under this Act only to supplement the funds that would, in the absence of such Federal funds, be made available from State and local sources for elementary and secondary education, and not to supplant State and local funds.\n**(B) Compliance**\nThe Secretary shall use funds described in subsection (d)(1)(B) to administer programs authorized under this subpart and to issue technical assistance to States and to monitor and enforce the requirements under such programs.",
      "versionDate": "2026-01-13",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2451",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Pay Paraprofessionals and Support Staff Act",
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
        "name": "Education",
        "updateDate": "2026-02-02T14:47:02Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7032ih.xml"
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
      "title": "Pay Paraprofessionals and Support Staff Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pay Paraprofessionals and Support Staff Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that paraprofessionals and education support staff are paid a living wage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:18Z"
    }
  ]
}
```
