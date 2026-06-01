# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2451?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2451
- Title: Pay Paraprofessionals and Support Staff Act
- Congress: 119
- Bill type: S
- Bill number: 2451
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2026-04-22T11:03:21Z
- Update date including text: 2026-04-22T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2451",
    "number": "2451",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Pay Paraprofessionals and Support Staff Act",
    "type": "S",
    "updateDate": "2026-04-22T11:03:21Z",
    "updateDateIncludingText": "2026-04-22T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
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
      "actionDate": "2025-07-24",
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
            "date": "2025-07-24T17:57:55Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-24T17:57:55Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "CA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "HI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-24",
      "state": "VT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NY"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2451is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2451\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Markey (for himself, Mr. Padilla , Ms. Hirono , Mr. Sanders , Mrs. Gillibrand , Mr. Welch , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo ensure that paraprofessionals and education support staff are paid a living wage.\n#### 1. Short title\nThis Act may be cited as the Pay Paraprofessionals and Support Staff Act .\n#### 2. Pay Paraprofessionals and Education Support Staff Act\n##### (a) Definitions\nIn this section:\n**(1) ESEA**\nThe terms English learner , local educational agency , paraprofessional , professional development , Secretary , and State have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Annual adjustment percentage**\nThe term annual adjustment percentage means, with respect to a fiscal year, a percentage equal to the estimated percentage change in the Consumer Price Index, as determined by the Secretary, for the most recent calendar year ending prior to the beginning of such fiscal year.\n**(3) Minimum salary for paraprofessional and education support staff**\n**(A) In general**\nThe term minimum salary for paraprofessional and education support staff means an amount, determined by the State, that all full-time equivalent employees employed by a local educational agency are required by the State to be compensated by such agency as their annual base salary, and which\u2014\n**(i)**\nis greater than the amount described in subparagraph (B); and\n**(ii)**\nincreases as the experience of such school staff increases.\n**(B) Indexing salary growth to inflation**\n**(i) Fiscal years 2026 through 2030**\nFor each of fiscal years 2026 through 2030, the amount described in this subparagraph is $45,000.\n**(ii) Fiscal years 2031 and after**\nFor each fiscal year in the fiscal year period 2031 through 2035 and in each subsequent 5 fiscal year period, the amount described this subparagraph shall be equal to the amount applicable for each fiscal year in the previous 5 fiscal year period, increased by the greater of\u2014\n**(I)**\nthe aggregate annual adjustment percentage over the previous 5 fiscal years; or\n**(II)**\n2 percent of the amount applicable under this subsection for the previous 5 fiscal year period.\n**(4) Minimum wage for paraprofessional and education support staff**\n**(A) In general**\nThe term minimum wage for paraprofessional and education support staff means an amount, determined by the State, that all part-time equivalent staff employed by a local educational agency are required by the State to be paid by such agency, and which\u2014\n**(i)**\nis greater than the amount described in subparagraph (B); and\n**(ii)**\nincreases as the experience of such school staff increases.\n**(B) Indexing salary growth to inflation**\n**(i) Fiscal years 2026 through 2030**\nFor each of fiscal years 2026 through 2030, the amount described in this subparagraph is $30.00 an hour.\n**(ii) Fiscal years 2031 and after**\nFor each fiscal year in the fiscal year period 2031 through 2035 and in each subsequent 5 fiscal year period, the amount described this subparagraph shall be equal to the amount applicable for each fiscal year in the previous 5 fiscal year period, increased by the greater of\u2014\n**(I)**\nthe aggregate annual adjustment percentage over the previous 5 fiscal years; or\n**(II)**\n2 percent of the amount applicable under this subsection for the previous 5 fiscal year period.\n##### (b) Purpose\nThe purpose of this section is to ensure that paraprofessionals and education support staff, who are the backbone of our Nation\u2019s public education system, are\u2014\n**(1)**\npaid a living wage, which means\u2014\n**(A)**\na minimum salary for paraprofessional and education support staff; or\n**(B)**\na minimum wage for paraprofessional and education support staff;\n**(2)**\ncompensated in a manner that recognizes some regions may have higher costs of living and therefore necessitate higher minimum salaries or wages;\n**(3)**\nrecognized as public servants who provide essential services that keep our Nation\u2019s public schools running and our students thriving; and\n**(4)**\nprovided safe working conditions and treated with the respect and dignity they deserve.\n##### (c) Authorization and appropriations\nIn addition to amounts otherwise available, there are authorized to be appropriated and there are appropriated out of any money in the Treasury not otherwise appropriated, to the Department of Education, to carry this section\u2014\n**(1)**\nfor fiscal year 2026, $25,000,000,000; and\n**(2)**\nfor each succeeding fiscal year, the amount appropriated under this section for the preceding fiscal year, increased by the annual adjustment percentage.\n##### (d) Authorization of grants\n**(1) Reservations**\nFrom the total amount appropriated under subsection (c) for a fiscal year, the Secretary shall reserve not more than\u2014\n**(A)**\n1 percent to provide grants, contracts, or cooperative agreements to regional educational laboratories (established under section 174 of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9564 )) or qualified nonprofit organizations to assist States that receive grants under this section carry out applied research or evaluations in providing paraprofessionals and education support staff with opportunities for personnel preparation, professional development, credentials, or certifications, such as to assist in the provision of special education and related services or to serve English learners; and\n**(B)**\n1 percent for technical assistance and program administration of this section.\n**(2) Grants**\nThe Secretary shall award grants to States from allotments under paragraph (3) to ensure that all local educational agencies have the resources necessary to pay paraprofessionals and education support staff a living wage, which means\u2014\n**(A)**\nthe minimum salary for paraprofessional and education support staff; or\n**(B)**\na minimum wage for paraprofessional and education support staff.\n**(3) Allotments**\nFrom the amounts appropriated under subsection (b) that are remaining after making the reservations described in paragraph (1) for a fiscal year, the Secretary shall allot to each State that has submitted an approved application under subsection (d), an amount that bears the same relationship to the remainder as the amount the State received under part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ) for the preceding fiscal year bears to the amount all States received under that subpart for the preceding fiscal year.\n##### (e) State application\nIn order to receive a grant under this section, a State shall submit an application to the Secretary at such time, in such manner, and including such information as the Secretary may reasonably require, including the following:\n**(1)**\nA timeline, consistent with the goals required under paragraph (2), to ensure that, not later than 4 years after the receipt of a grant under this section\u2014\n**(A)**\nthe annual base salary of a full-time equivalent employee employed by a local educational agency in the State is not less than the minimum salary for paraprofessional and education support staff, as determined by the State; and\n**(B)**\nall part-time equivalent staff employed by a local educational agency in the State are paid not less than the minimum wage for paraprofessional and education support staff, as determined by the State.\n**(2)**\nFor each fiscal year in the timeline specified in paragraph (1), statewide annual goals for increasing average salary or wage baselines of paraprofessionals and education support staff in a manner that\u2014\n**(A)**\nannually proposes a percentage increase in the average wage or salary of paraprofessionals and education support staff;\n**(B)**\nprovides for the first increase to occur not later than the second fiscal year a State receives a grant under this section; and\n**(C)**\nmakes significant progress toward ensuring that, by the end of the timeline described in subparagraph (A)\u2014\n**(i)**\nthe annual base salary of a full-time equivalent employee employed by a local educational agency in the State is not less than the minimum salary for paraprofessional and education support staff, as determined by the State; and\n**(ii)**\nall part-time equivalent staff employed by a local educational agency in the State are paid not less than the minimum wage for paraprofessional and education support staff, as determined by the State.\n**(3)**\nThe State\u2019s proposed formula to subgrant funds to local educational agencies as described in subsection (g) in a manner that ensures\u2014\n**(A)**\nlocal educational agencies that serve a high number or percentage of students from low-income backgrounds receive substantial subgrant allocations that enable such agencies to meet the requirements described in subparagraphs (A) and (B) of paragraph (1) not later than 2 years after the receipt of a subgrant; and\n**(B)**\nall remaining local educational agencies in the State meet the State\u2019s requirements in the timeline described in paragraph (1).\n##### (f) Improving paraprofessional and school staff wages and salaries\n**(1) State reservation**\nA State that receives a grant under this section may reserve not more than 2 percent of the total grant amount received by the State for technical assistance, administrative purposes, and statewide efforts to provide paraprofessionals and education support staff with opportunities for personnel preparation, professional development, credentials, or certifications, such as to assist in the provision of special education and related services or to serve English learners.\n**(2) Improving wages and salaries**\n**(A) In general**\nSubject to subparagraph (B), a State that receives a grant under this section shall ensure that, within a timeline determined by the State under subsection (e)(1) and approved by the Secretary\u2014\n**(i)**\nthe annual base salary of a full-time equivalent employee employed by a local educational agency in the State is not less than the minimum salary for paraprofessional and education support staff, as determined by the State; and\n**(ii)**\nall part-time equivalent staff employed by a local educational agency in the State are paid not less than the minimum wage for paraprofessional and education support staff, as determined by the State.\n**(B) Timing**\nThe Secretary shall ensure that, by not later than 4 years after the date of implementation of the final regulations issued under this Act, each State that receives a grant under this section meets the salary and wage requirements specified in subparagraph (A).\n##### (g) Subgrants to local educational agencies\n**(1) Allocation**\nEach State shall allocate not less than 98 percent of the grant funds awarded to the State under this section as subgrants to local educational agencies (including charter schools that are local educational agencies) in the State under the formula determined by the State under subsection (e)(3) and approved by the Secretary.\n**(2) Uses of subgrant funds**\nA local educational agency that receives a subgrant under paragraph (1)\u2014\n**(A)**\nshall use the subgrant funds to comply with the State\u2019s requirements in accordance with subsection (e) guaranteeing that no full-time equivalent employee of the agency is paid less than the minimum salary for paraprofessional and education support staff and no part-time equivalent employee of the agency is paid less than the minimum wage for paraprofessional and education support staff; and\n**(B)**\nmay use subgrant funds\u2014\n**(i)**\nto increase salaries or wages for teachers, paraprofessionals, specialized instructional support personnel, classified school employees, principals, other school leaders, school librarians, school bus drivers, and other staff across their careers; and\n**(ii)**\nto provide paraprofessionals and education support staff with opportunities for personnel preparation, professional development, credentials, or certifications, such as to assist in the provision of special education and related services or to serve English learners.\n**(3) Contracted staff**\n**(A) In general**\nA local educational agency that receives a subgrant under this section shall ensure that staff employed by such agency or in any contract such agency enters into, are paid an amount not less than the minimum salary for paraprofessionals and education support staff or the minimum wage for paraprofessionals and education support staff in the State.\n**(B) Monitoring**\nA State that receives a grant under this section shall monitor local educational agencies for compliance with subparagraph (A).\n##### (h) Rules\n**(1) Rule of construction for collective bargaining**\n**(A) In general**\nSubject to subparagraph (B), nothing in this Act shall be construed to alter or otherwise affect the rights, remedies, and procedures afforded to school or local educational agency employees under Federal, State, or local laws (including applicable regulations or court orders) or under the terms of collective bargaining agreements, memoranda of understanding, or other agreements between such employers and their employees.\n**(B) Compliance**\nSubparagraph (A) shall not be construed to exempt a State, local educational agency, or school from complying with salary or wage requirements in this Act or from negotiating in compliance with State labor laws to comply with this Act.\n**(2) Rule of construction for additional pay or other salary augmenting systems**\nNothing in this Act shall be construed to prevent States or local educational agencies from supplementing the annual base salary of teachers, paraprofessionals, education support staff, or other staff employed by such agencies\u2014\n**(A)**\nfor additional skills, knowledge, duties, and responsibilities;\n**(B)**\nby salary systems that increase teachers\u2019 compensation through supplemental pay that is not part of an annual base salary; or\n**(C)**\nthrough the provision of bonuses, stipends, or awards.\n**(3) No waiver authority**\nSection 8401 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7861 ) shall not apply to this Act.\n**(4) Supplement not supplant**\n**(A) In general**\nA State shall use Federal funds received under this Act only to supplement the funds that would, in the absence of such Federal funds, be made available from State and local sources for elementary and secondary education, and not to supplant State and local funds.\n**(B) Compliance**\nThe Secretary shall use funds described in subsection (d)(1)(B) to administer programs authorized under this subpart and to issue technical assistance to States and to monitor and enforce the requirements under such programs.",
      "versionDate": "2025-07-24",
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
        "actionDate": "2026-01-13",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "7032",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Pay Paraprofessionals and Support Staff Act",
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
        "name": "Education",
        "updateDate": "2025-09-17T16:27:24Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2451is.xml"
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
      "title": "Pay Paraprofessionals and Support Staff Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pay Paraprofessionals and Support Staff Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure that paraprofessionals and education support staff are paid a living wage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:20Z"
    }
  ]
}
```
