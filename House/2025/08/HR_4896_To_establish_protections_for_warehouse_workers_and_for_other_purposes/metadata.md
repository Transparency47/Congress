# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4896?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4896
- Title: Warehouse Worker Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 4896
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-04-10T08:06:13Z
- Update date including text: 2026-04-10T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4896",
    "number": "4896",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "N000188",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Norcross, Donald [D-NJ-1]",
        "lastName": "Norcross",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Warehouse Worker Protection Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:13Z",
    "updateDateIncludingText": "2026-04-10T08:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-05T14:04:00Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "RI"
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
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
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
      "sponsorshipDate": "2025-08-05",
      "state": "DC"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MI"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "WA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "IL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MN"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IN"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "GA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NH"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "OR"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4896ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4896\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. Norcross (for himself, Mr. Lawler , Ms. Stevens , Mr. Magaziner , Mr. Boyle of Pennsylvania , Mr. Sherman , Mr. Garc\u00eda of Illinois , Ms. Norton , Mrs. Dingell , Ms. Ocasio-Cortez , Mr. Thanedar , Ms. Jayapal , and Ms. S\u00e1nchez ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish protections for warehouse workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Warehouse Worker Protection Act .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nTitle I\u2014WAREHOUSE WORKER PROTECTIONS\nSec. 101. Warehouse worker protections.\nSec. 102. Definitions.\nSec. 103. Enforcement by the Secretary of Labor.\nSec. 104. Referral of complaints.\nSec. 105. Enforcement by the FTC.\nTitle II\u2014NATIONAL LABOR RELATIONS ACT\nSec. 201. Amendments to National Labor Relations Act.\nSec. 202. National Labor Relations Board report.\nTitle III\u2014OSHA STANDARDS\nSec. 301. Standard protecting covered employees from occupational risk factors causing musculoskeletal disorders.\nSec. 302. Standard for protecting covered employees from delays in medical treatment referrals following injuries or illnesses.\nSec. 303. Correction of serious, willful, or repeated violations pending contest and procedures for a stay.\nSec. 304. Definitions.\nTitle IV\u2014MISCELLANEOUS PROVISIONS\nSec. 401. Severability.\nSec. 402. Preemption.\nSec. 403. Authorization of appropriations.\nI\nWAREHOUSE WORKER PROTECTIONS\n#### 101. Warehouse worker protections\nThe Fair Labor Standards Act of 1938 is amended by inserting after section 4 ( 29 U.S.C. 204 ) the following:\n5. Establishment of fairness and transparency office (a) In general There is established in the Wage and Hour Division of the Department of Labor the Fairness and Transparency Office. (b) Director of the fairness and transparency office The President shall appoint a Director of the Fairness and Transparency Office to head the Fairness and Transparency Office. (c) Employees and advisory boards of the office (1) In general The Director\u2014 (A) may select, appoint, and employ, without regard to the provisions of sections 3309 through 3318 of title 5, United States Code, individuals directly to positions in the competitive service, as defined in section 2102 of such title, to carry out the duties of the Director under this Act; and (B) may fix the compensation of the individuals described in subparagraph (A) without regard to chapter 51 and subchapter III of chapter 53 of title 5, United States Code, relating to classification of positions and General Schedule pay rates, except that the rate of pay for such individuals may not exceed the rate payable for level V of the Executive Schedule under section 5316 of that title. (2) Fairness and transparency advisory board (A) In general The Director shall establish a Fairness and Transparency Advisory Board to advise and consult on the exercise of the functions of the Director under this Act and under the Warehouse Worker Protection Act. (B) Composition The Fairness and Transparency Advisory Board established under subparagraph (A) shall be composed of\u2014 (i) as the Director determines appropriate, covered employers and covered employees or representatives of covered employers and covered employees; and (ii) at least one of each of the following: (I) Worker protection experts. (II) Civil rights experts. (III) Health and safety experts. (IV) Workplace technology experts. (V) Disability law experts. (VI) Representatives of labor organizations. (VII) Representatives of worker advocacy organizations. (C) Appointments The Director shall\u2014 (i) appoint members to the advisory board established under subparagraph (A); and (ii) ensure a partisan balance in the membership of the advisory board. (D) Meetings The advisory board established under subparagraph (A) shall meet\u2014 (i) at the call of the Director; and (ii) not less than 2 times annually. (E) Compensation and travel expenses A member of the Fairness and Transparency Advisory Board established under subparagraph (A) who is not an officer or employee of the Federal Government shall\u2014 (i) be entitled to receive compensation at a rate fixed by the Director while attending meetings of the advisory board, including travel time; and (ii) receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code. (F) Exemption from the Federal advisory committee act The Fairness and Transparency Advisory Board established under subparagraph (A) shall be exempt from chapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act ). (G) Definitions of covered employee and covered employer In this paragraph, the terms covered employee and covered employer have the meanings given such terms in section 102(a) of the Warehouse Worker Protection Act. (3) Use of voluntary services The Director may, as may from time to time be needed, use any voluntary or uncompensated services. (4) Attorneys Attorneys appointed under this subsection or the Solicitor of Labor may appear for and represent the Director in any litigation. (d) Rulemaking (1) In general The Secretary, acting through the Director and the Administrator of the Wage and Hour Office, may issue orders and guidance or promulgate regulations as may be necessary or appropriate to enable the Secretary to carry out the purposes and objectives of the Warehouse Worker Protection Act, and to prevent evasions thereof. (2) Consultation In issuing orders and guidance or promulgating regulations under this subsection, the Secretary, acting through the Director and the Administrator of the Wage and Hour Office, may consult with the Occupational Safety and Health Administration and Federal agencies that have jurisdiction over labor and employment issues, including the Equal Employment Opportunity Commission, the National Labor Relations Board, the National Mediation Board, and the Merit Systems Protection Board. .\n#### 102. Definitions\n##### (a) Definitions\nIn this section:\n**(1) Adverse employment action**\nThe term adverse employment action , with respect to a covered employee, means a change by the covered employer of the covered employee in the compensation, terms, conditions, or privileges of the job of the covered employee that, from the perspective of a reasonable person, puts the covered employee in a materially adverse position than prior to the change, including termination, a reduction in benefits, disciplinary action, demotion, promotion, transfer, imposition of a work schedule more burdensome to the covered employee, reduction of scheduled hours, adjustment in ability for promotion, or other modifications to compensation, terms, conditions, or privileges of employment.\n**(2) Aggregated work speed data**\nThe term aggregated work speed data means employee work speed data that a covered employer has combined, or collected together, in a summary or other form so that the employee work speed data cannot, at any point, be identified or linked with any specific covered employee.\n**(3) Commerce**\nThe terms commerce , goods , enterprise , enterprise engaged in commerce or in the production of goods for commerce have the meanings given such terms in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(4) Covered facility**\nThe term covered facility means any warehouse distribution center described in the North American Industry Classification System code\u2014\n**(A)**\n493, for warehousing and storage;\n**(B)**\n423, for merchant wholesalers, durable goods;\n**(C)**\n424, for merchant wholesalers, nondurable goods;\n**(D)**\n454110, for electronic shopping and mail-order houses; or\n**(E)**\n492110, for couriers and express delivery services.\n**(5) Covered employee**\nThe term covered employee means an employee who\u2014\n**(A)**\nis employed by an employer for the performance of work at a covered facility; and\n**(B)**\nis subject to a quota while performing work at such covered facility.\n**(6) Covered employer**\n**(A) In general**\nThe term covered employer means an employer that\u2014\n**(i)**\nis engaged in commerce, in the production of goods for commerce, or in an enterprise engaged in commerce or in the production of goods for commerce, including such an employer that is a contractor, subcontractor, temporary service firm, staffing agency, independent contractor, employee leasing entity, or similar entity;\n**(ii)**\nemploys a covered employee for the performance of work at a covered facility; and\n**(iii)**\nemploys more than a total of 200 employees (including on a full- or part-time basis) for the performance of work at all covered facilities owned or operated by the employer.\n**(B) Rule of construction**\nFor purposes of determining the number of employees under subparagraph (A)(iii), the total number of employees employed for the performance of work as described in such subparagraph shall include all employees of any affiliate of the employer (as determined in accordance with section 121.103 of title 13, Code of Federal Regulations, as in effect on the date of enactment of this Act).\n**(7) Defined time period**\nThe term defined time period means any unit of time measurement equal to or less than one day, including hours, minutes, and seconds and any fraction thereof.\n**(8) Designated employee representative**\nThe term designated employee representative means any representative designated by a covered employee, including an employee representative that has a collective bargaining relationship with the covered employer of the covered employee.\n**(9) Director**\nThe term Director means the Director of the Fairness and Transparency Office established by section 5 of the Fair Labor Standards Act of 1938.\n**(10) Egregious misconduct**\nThe term egregious misconduct , with respect to a covered employee, means deliberate or grossly negligent conduct that endangers the safety or well-being of the covered employee, co-workers of the covered employer, customers, or other persons, including discrimination against or harassment of co-workers, customers, or other persons.\n**(11) Employ; employee; employer**\nThe terms employ ; employee ; and employer have the meanings given such terms in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(12) Employee work speed data**\nThe term employee work speed data means information a covered employer collects, stores, analyzes, or interprets relating to the performance of work by a covered employee of the covered employer for a quota, including information with respect to the\u2014\n**(A)**\nquantities of tasks performed by the covered employee;\n**(B)**\nquantities of items or materials handled or produced by the covered employee;\n**(C)**\nrates or speeds of tasks performed by the covered employee;\n**(D)**\nmeasurements or metrics of covered employee performance in relation to a quota; or\n**(E)**\ntime categorized with respect to the covered employee as performing tasks or not performing tasks.\n**(13) Quota**\nThe term quota means an express or implied performance standard or performance target, including such a standard or target used to rank or compare an employee in relation to the performance of another employee or in relation to the past performance of the employee, under which\u2014\n**(A)**\n**(i)**\nan employee is actually or effectively assigned, required, or expected within a defined time period (with or without any reasonable accommodation provided under Federal, State, or local law) to\u2014\n**(I)**\nperform\u2014\n**(aa)**\na quantified number of tasks; or\n**(bb)**\nat a specified productivity speed; or\n**(II)**\nhandle or produce a quantified amount of material without a certain number of errors or defects; and\n**(ii)**\nsuch assignment, requirement, or expectation is measured at the individual or group level for such defined time period;\n**(B)**\nactions by an employee are categorized and measured between time performing tasks and not performing tasks within a defined time period; or\n**(C)**\nincrements of time of a defined time period during which an employee is or is not doing a particular activity are measured, recorded, or tallied.\n**(14) Similarly situated covered employee**\nThe term similarly situated covered employee , with respect to a covered employee, means another covered employee who holds the same job or responsibilities as the covered employee.\n**(15) Tribal government**\nThe term Tribal government means the recognized governing body of an Indian Tribe.\n**(16) Workplace surveillance**\nThe term workplace surveillance means any employer surveillance (on- or off-duty) with respect to an employee, including the detection, monitoring, interception, collection, exploitation, preservation, protection, transmission, or retention of data concerning activities or communications with respect to the employee, including through the use of a product or service marketed, or that can be used, for such purposes, such as a computer, telephone, wire, radio, camera, sensor, electromagnetic, photoelectronic, handheld or wearable device, or photo-optical system.\n**(17) Work station**\nThe term work station means the area of a covered facility within which a covered employee is assigned to perform tasks for the longest duration of time during a day.\n##### (b) Communication with covered employees regarding quotas and workplace surveillance\n**(1) In general**\nOn the later of the date a covered employee is hired by a covered employer or 180 days after the date of enactment of this section, each covered employer shall provide to each covered employee of the covered employer\u2014\n**(A)**\na written description of each quota to which the covered employee is subject, including\u2014\n**(i)**\nas applicable, the quantified number of tasks to be performed or of materials to be produced or handled, or other performance measure, within the defined time period, for the quota;\n**(ii)**\nany potential discipline or adverse employment action that could result from failure to meet the quota;\n**(iii)**\nhow performance targets or performance standards for the quota are calculated;\n**(iv)**\nwhether there is any incentive or bonus program associated with meeting or exceeding the quota and, if applicable, how the incentive or bonus program operates; and\n**(v)**\nhow the quota is monitored, including a description of\u2014\n**(I)**\nwhat employee work speed data are being collected;\n**(II)**\nhow the employee work speed data are being collected, including a description of any workplace surveillance technology used on the covered employee by the covered employer;\n**(III)**\nwhere and when the employee work speed data are being collected;\n**(IV)**\nthe frequency of the collection;\n**(V)**\nwhere the storage of the employee work speed data is located;\n**(VI)**\nthe business purposes for which the employee work speed data are being used; and\n**(VII)**\nas applicable, the identity of any third party\u2014\n**(aa)**\nused for such workplace surveillance;\n**(bb)**\nto which data from such workplace surveillance is transferred; and\n**(cc)**\nfrom which data of the covered individual is or may be purchased or acquired; and\n**(B)**\na written description of and training with respect to how the covered employee may file a complaint regarding a violation of this section or a standard promulgated under title III of this Act.\n**(2) Changes to quota or workplace surveillance**\nEach covered employer shall provide to any applicable covered employee an updated written description of any information provided under paragraph (1) not less than 2 business days before any changes with respect to such information are made.\n**(3) Requirements for taking an adverse employment action on quota compliance**\n**(A) In general**\nA covered employer that takes an adverse employment action against a covered employee for work performance that does not meet requirements with respect to a quota shall provide\u2014\n**(i)**\na written explanation to the covered employee regarding the manner in which the covered employee failed to perform, including a description of the applicable quota and a comparison of such work performance to such quota; and\n**(ii)**\nif the adverse employment action was based on employee work speed data, a copy of the employee work speed data in a human-readable format that a reasonable individual can understand.\n**(B) Notice for actions unrelated to quota**\nA covered employer that, with respect to any covered employee who is subject to a quota, takes an adverse employment action against such covered employee for any reason that is unrelated to compliance with the quota shall provide to such covered employee a written confirmation that such action was unrelated to compliance with the quota.\n**(4) Termination**\n**(A) In general**\nA covered employer that seeks to terminate a covered employee shall, regardless of whether the termination relates to work performance with respect to a quota, provide to the covered employee a written notice of the intent to terminate the covered employee.\n**(B) Egregious misconduct**\nNotwithstanding subparagraph (A), a covered employer may terminate a covered employee without providing such written notice if the covered employee engaged in egregious misconduct.\n**(5) Descriptions**\nEach covered employer shall\u2014\n**(A)**\nprovide any written description, notice, explanation, or confirmation described in paragraph (1), (2), (3), or (4) to a covered employee\u2014\n**(i)**\nthrough a human representative of the covered employer at the work station of the covered employee; and\n**(ii)**\nin a manner required by the Director that\u2014\n**(I)**\nis accessible;\n**(II)**\nallows the covered employee to transport the data in the description, notice, explanation, or confirmation without hindrance;\n**(III)**\nis in plain language; and\n**(IV)**\nis in the primary language of the covered employee; and\n**(B)**\nmake such description, notice, explanation, or confirmation available to the covered employee electronically.\n##### (c) Protection from quotas\n**(1) Prohibited quotas**\nA covered employer may not require any quota for a covered employee that would\u2014\n**(A)**\nprevent\u2014\n**(i)**\ncompliance with any required meal or rest period or any other break required by Federal, State, or local law;\n**(ii)**\ncompliance with health and safety provisions required by Federal, State, or local law;\n**(iii)**\nthe use by the covered employee of bathroom facilities, including reasonable travel time to and from bathroom facilities that takes into account the architecture of the covered facility; or\n**(iv)**\ncompliance with a covered employee\u2019s right to reasonable accommodations or nondiscrimination as required by Federal, State, or local law;\n**(B)**\nset a performance target or performance standard that measures total output for the covered employee over an increment of time that is shorter than one day;\n**(C)**\nmeasure and evaluate the output or performance of a covered employee during any paid or unpaid break to which the covered employee is entitled under applicable law, contract, or industry standard, including breaks to use bathroom facilities and reasonable travel time to and from bathroom facilities;\n**(D)**\nprevent or discourage the covered employee from exercising any right under the National Labor Relations Act ( 29 U.S.C. 151 et seq. ) or any other Federal law;\n**(E)**\nprevent or discourage the covered employee from exercising any right guaranteed in an applicable collective bargaining agreement; or\n**(F)**\nviolate the generally accepted principles of work measurement as set forth in the Code of Work Measurement Ethics of the American Institute of Industrial Engineers and recognized by the Secretary.\n**(2) Adverse employment action**\nA covered employer may not take adverse employment action against a covered employee for failure to meet a quota that\u2014\n**(A)**\nviolates paragraph (1);\n**(B)**\nwas not described to the covered employee in accordance with subsection (b);\n**(C)**\nis based solely on ranking the performance of the covered employee in relation to the performance of another covered employee or in relation to the past performance of that covered employee; or\n**(D)**\nis based on continuously measuring, recording, or tallying increments of time within a defined time period during which a covered employee is or is not doing a particular activity.\n##### (d) Minimization\n**(1) Collection**\nIn establishing, maintaining, or using employee work speed data with respect to a quota for a covered employee, a covered employer may not collect, use, maintain, or transfer data on or of the covered employee except as strictly necessary to monitor the compliance of the covered employee with the quota.\n**(2) Employee access**\nIn establishing, maintaining, or using employee work speed data with respect to a quota for a covered employee, a covered employer may not disclose any information collected on a covered employee with respect to the quota to any other covered employee of the covered employer except as strictly necessary to fulfill a specific and reasonable business rationale of the covered employer.\n##### (e) Recordkeeping\n**(1) In general**\nEach covered employer shall\u2014\n**(A)**\nmaintain contemporaneous records, with respect to each covered employee of the covered employer, of\u2014\n**(i)**\nthe employee work speed data of each such covered employee;\n**(ii)**\nthe aggregated work speed data for similarly situated covered employees at the same place where each such covered employee performs work for the covered employer; and\n**(iii)**\nthe written descriptions of the quota of each such covered employee provided under subsection (b)(1);\n**(B)**\nmaintain such records for the duration of the employment of each relevant covered employee; and\n**(C)**\nmake such records available to the Secretary upon request.\n**(2) Supplementation and dispute of records**\n**(A) Supplementation of records**\nEach covered employer shall enable a covered employee, upon request of the covered employee at or after the time of any employee work speed data collection with respect to the covered employee, to supplement the employee work speed data by recording any reason the covered employee provides for any defined time period during which the covered employee was not performing work-related tasks, including because the covered employee was taking a paid or unpaid break, using a bathroom facility (including reasonable travel to and from the facility), reporting an injury or receiving attention due to an injury, exercising a right guaranteed under the National Labor Relations Act ( 29 U.S.C. 151 et seq. ) or another Federal law, or exercising a right guaranteed under an applicable covered bargaining agreement.\n**(B) Dispute process**\n**(i) In general**\nEach covered employer shall enable a covered employee, upon request of the covered employee at or after the time of any data collection with respect to the covered employee, to review and request correction of the employee work speed data in accordance with clause (ii).\n**(ii) Correction of employee work speed data**\nA covered employer that receives a request by a covered employee under clause (i) shall\u2014\n**(I)**\ninvestigate and determine whether the employee work speed data is inaccurate; and\n**(II)**\nif determined to be inaccurate\u2014\n**(aa)**\npromptly correct the inaccurate data and notify the covered employee of the covered employer\u2019s determination and correction; and\n**(bb)**\nreview and adjust, as appropriate, any adverse employment action that was, partially or solely, based on the inaccurate data and notify the covered employee of the adjustment.\n**(3) Retention of records**\n**(A) In general**\nAfter the termination of employment of a covered employee of a covered employer, the covered employer shall\u2014\n**(i)**\nfor not less than 3 years after the date of such termination, retain the records described in paragraph (1) with respect to the 6-month period prior to such date; and\n**(ii)**\nmake such records available to the Secretary upon request.\n**(4) Rule of construction**\nNothing in this subsection shall require a covered employer to keep records described in paragraph (1) with respect to employee work speed data if such covered employer does not otherwise monitor employee work speed data.\n##### (f) Right To request\n**(1) In general**\nA covered employer shall, upon receiving a request under paragraph (2) or (3), provide the relevant copies described in such paragraphs to, as the case may be, the covered employee, designated employee representative, or individual who was a covered employee\u2014\n**(A)**\nexcept as provided in subparagraph (B)(ii), at no cost to the covered employee, designated employee representative, or individual who was a covered employee;\n**(B)**\nwith respect to\u2014\n**(i)**\na covered employee, by a human representative of the covered employer; or\n**(ii)**\na designated employee representative or an individual who was a covered employee, by a human representative of the covered employer or through the mail (at the cost of the designated employee representative or individual, respectively); and\n**(C)**\nas soon as practicable but not later than\u2014\n**(i)**\n7 business days after receipt of a request for such copies with respect to employee work speed data or aggregate work speed data; or\n**(ii)**\n2 business days after receipt of a request for any other copy.\n**(2) Requests during employment**\nA covered employee, or a designated employee representative of such covered employee at the request of the covered employee, may request from the covered employer of the covered employee a copy of the written description described under subsection (b), a copy of the employee work speed data (in a human-readable format that a reasonable individual can understand) of the covered employee for the preceding 6-month period, and a copy of the aggregated work speed data (in a human-readable format that a reasonable individual can understand) for similarly situated covered employees at the same place where the covered employee performs work for the covered employer for the preceding 6-month period.\n**(3) Requests after employment termination**\nAn individual who was a covered employee with respect to a covered employer, or a designated employee representative with respect to such an individual, may, not later than 3 years after the date of termination of employment of the covered employee with the covered employer, request from the covered employer a copy of\u2014\n**(A)**\nthe written description described under subsection (b) effective on the date of termination of the covered employee;\n**(B)**\nthe employee work speed data (in a human-readable format that a reasonable individual can understand) of the covered employee for the 6-month period prior to such date of termination; and\n**(C)**\nthe aggregated work speed data (in a human-readable format that a reasonable individual can understand) for similarly situated covered employees at the same place where the covered employee performs work for the covered employer for such 6-month period.\n**(4) Rule of construction**\nNothing in this subsection shall require a covered employer to\u2014\n**(A)**\nmonitor employee work speed data; or\n**(B)**\nprovide information related to employee work speed data if the covered employer does not otherwise monitor such employee work speed data.\n##### (g) Posting of notices\n**(1) In general**\nEach covered employer shall post, in a conspicuous and accessible location, a notice in the covered facility of the covered employer regarding the rights of covered employees under this section, including what constitutes a permissible quota, the right to request quota descriptions and employee speed data information, and the right to make a complaint to Federal authorities regarding a violation of any right under this section.\n**(2) Requirements for notices**\nEach notice described in paragraph (1) shall be in a manner required by the Director that\u2014\n**(A)**\nis in plain language; and\n**(B)**\nis in English, Spanish, and any other language that constitutes the primary language of any covered employee at the covered facility.\n##### (h) Breaks for covered employees\n**(1) In general**\nEach covered employer shall\u2014\n**(A)**\nwith respect to each covered employee of such covered employer\u2014\n**(i)**\nprovide, for every 4 hours of work by such a covered employee, to the covered employee not less than one 15-minute rest break paid at the regular rate at which the covered employee is employed; and\n**(ii)**\nprovide, at the time the covered employer hires such a covered employee, notice to the covered employee, in plain language and the primary language of the covered employee, that\u2014\n**(I)**\nthe covered employee is entitled to the paid rest breaks described in clause (i);\n**(II)**\nretaliation by the covered employer against the covered employee for requesting or taking such paid rest breaks is prohibited; and\n**(III)**\nthe covered employee, or a designated employee representative of the covered employee, has a right to file a complaint with the Secretary for any violation by the covered employer of this subsection; and\n**(B)**\ndisplay, in a conspicuous and accessible location, a sign at each covered facility of the covered employer that includes, in English, Spanish, and any other language that constitutes the primary language of any covered employee at the covered facility, the information in the notice described in subparagraph (A)(ii).\n**(2) Notice**\nNot later than 180 days after the date of enactment of this section, the Secretary of Labor shall issue regulations with respect to the design and content of the sign described in paragraph (1)(B), including a sample design.\n**(3) Interaction with other laws**\nNothing in this subsection shall be construed to supersede or preempt any Federal, State, or local law or collective bargaining agreement requiring longer paid rest breaks than those required under paragraph (1)(A)(i).\n##### (i) Unlawful retaliation\n**(1) In general**\nA person, including a covered employer, an agent of a covered employer, or person acting as or on behalf of a covered employer conducting hiring or any related activity, or an officer or agent of any entity, business, corporation, partnership, or limited liability company, may not\u2014\n**(A)**\ndischarge or in any way retaliate, discriminate, or take any adverse employment action against any individual for exercising any right conferred under this section, or for being perceived as exercising such a right, including for\u2014\n**(i)**\nrequesting copies under subsection (f);\n**(ii)**\nfiling a complaint under subparagraph (A) of section 16(f) of the Fair Labor Standards Act of 1938 regarding a violation of this section or designating a representative in accordance with subparagraph (B) of such section to file such a complaint; or\n**(iii)**\ncommencing a proceeding under section 16(b) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216(b) ) for a violation of this section; or\n**(B)**\notherwise prevent an individual for exercising such a right or take any action against an individual that might deter a reasonable employee from asserting a right conferred under this section.\n**(2) Protections for good faith allegations**\nThe protections under paragraph (1) shall apply to any individual who mistakenly, but in good faith, alleges a violation of a requirement of this section.\n**(3) Explicit reference not required**\nA complaint or other communication by an individual, including a covered employee, may be the exercise of a right for purposes of paragraph (1) regardless of whether the complaint or communication is in writing or makes explicit reference to this Act.\n**(4) Rebuttable presumption**\nIf a person takes adverse action against a covered employee within 90 days of the covered employee engaging, or attempting to engage in, activities protected by paragraph (1), such conduct shall establish a rebuttable presumption that the adverse action is an adverse action in violation of such paragraph. Such presumption may be rebutted by clear and convincing evidence that\u2014\n**(A)**\nthe action was taken for other permissible reasons; and\n**(B)**\nthe engaging or attempting to engage in activities protected by paragraph (1) was not a motivating factor in the adverse action.\n##### (j) Quota task force\nNot later than 90 days after the date of the enactment of this section, the Director shall convene a task force with labor organizations, worker advocacy organizations, and covered employees to develop strategies for labor organizations and worker advocacy organizations to\u2014\n**(1)**\nassist in the enforcement of this section;\n**(2)**\ntrain covered employees with respect to new rights provided through this section; and\n**(3)**\nprovide the Director with recommendations on the implementation of regulations related to this section.\n#### 103. Enforcement by the Secretary of Labor\nThe Fair Labor Standards Act of 1938 is amended\u2014\n**(1)**\nin section 9 ( 29 U.S.C. 209 ), by striking or investigation and inserting , investigation, or inspection ;\n**(2)**\nin section 11 ( 29 U.S.C. 211 ), by adding at the end the following:\n(e) (1) The Secretary, acting through the Director of the Fairness and Transparency Division, shall, as provided in subsection (a) and paragraph (2), investigate violations of section 102 of the Warehouse Worker Protection Act, including any violations of any regulation or order issued with respect to that section. (2) In addition to powers otherwise provided to the Secretary under subsection (a), the Secretary, in investigating violations of section 102 of the Warehouse Worker Protection Act, may upon presenting appropriate credentials to the owner, operator, or agent in charge\u2014 (A) enter without delay and at reasonable times any covered facility of a covered employer; and (B) inspect and investigate during regular working hours and at other reasonable times, and within reasonable limits and in a reasonable manner, any such covered facility and all pertinent conditions, structures, machines, apparatus, devices, equipment, and materials therein, and to question privately any such covered employer, owner, operator, agent, or covered employee. (3) (A) In conducting an inspection during an investigation into a violation of section 102 of the Warehouse Worker Protection Act, the Secretary shall permit, at the request of a covered employee, a representative of a labor organization or a worker advocacy organization, or another designee of the covered employee, to accompany any inspectors during such inspection. (B) A covered employee may, regardless of the relationship between the covered employee and the labor organization, worker advocacy organization, or other designee, anonymously request to the Secretary that the Secretary permit a representative of such labor organization, worker advocacy organization, or other designee accompany inspectors during an inspection in accordance with paragraph (1). (f) (1) Not later than 30 days after an event described in paragraph (2), the Secretary shall open an investigation under this section (that includes an on-site inspection) into any covered employer to determine if such covered employer is violating section 102 of the Warehouse Worker Protection Act. (2) An event described in this paragraph is, with respect to a covered employer, either of the following: (A) The Secretary determines that the covered employer\u2014 (i) has an annual total of employee work hours that is not less than 40,000 hours; and (ii) has an annual employee injury rate, overall or at a worksite, that is not less than 1.5 times the warehousing industry\u2019s average annual injury rate, as determined by the Bureau of Labor Statistics in the most recent (as of such determination) publication regarding fatal and nonfatal occupational injuries and illnesses data. (B) The Secretary receives, during any one-year period, not less than\u2014 (i) 5 credible complaints from covered employees of the covered employer, individuals who were covered employees of the covered employer, or designated representatives of such covered employees or individuals, about violations under section 102 of the Warehouse Worker Protection Act at a worksite; or (ii) 10 credible complaints from covered employees of the covered employer, individuals who were covered employees of the covered employer, or designated representatives of such covered employees or individuals, about such violations at multiple worksites operated by the covered employer. (3) In conducting an investigation under paragraph (1), the Secretary shall select representatives of a labor organization or a worker advocacy organization who have specific knowledge of the relevant industry to conduct outreach to workers with respect to such investigation and aid and accompany investigators in such investigation. (g) For purposes of subsections (e) and (f), the terms \u2018covered employee\u2019, \u2018covered employer\u2019, and \u2018covered facility\u2019 have the meanings given such terms in section 102(a) of the Warehouse Worker Protection Act. .\n**(3)**\nin section 15(a) ( 29 U.S.C. 215(a) )\u2014\n**(A)**\nin paragraph (5), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (6), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(7) to violate any of the provisions of section 102 of the Warehouse Worker Protection Act. ; and\n**(4)**\nin section 16 ( 29 U.S.C. 216 )\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nby inserting or section 102 of the Warehouse Worker Protection Act after 18D each place it appears;\n**(ii)**\nin the second sentence\u2014\n**(I)**\nby striking of this Act shall and inserting shall ; and\n**(II)**\nby inserting and, in the case of a violation of section 102 of the Warehouse Worker Protection Act, of an amount for the direct or foreseeable pecuniary harms resulting from the violation and an amount equal to $10,000 per violation of subsection (b), (d), (e), (f), or (g) of such section or an amount equal to $25,000 per violation of subsection (c), (h), or (i) of such section before the period at the end of the sentence; and\n**(iii)**\nin the fifth sentence, by striking No and inserting Except with respect to an action brought regarding a violation of section 102 of the Warehouse Worker Protection Act, no ;\n**(B)**\nin subsection (e)\u2014\n**(i)**\nby redesignating paragraphs (3), (4), and (5) as paragraphs (4), (5), and (6), respectively;\n**(ii)**\nby inserting after paragraph (2), the following:\n(3) Any person who violates section 102 of the Warehouse Worker Protection Act shall be subject to a civil penalty\u2014 (A) in an amount not more than $76,987 per violation; or (B) for repeat or willful violations, in an amount not more than $769,870 per violation. ; and\n**(iii)**\nin paragraph (4)(C), as so redesignated, by striking section 15(a)(4) and inserting paragraph (4) or (7) of section 15(a) ; and\n**(C)**\nby adding at the end the following:\n(f) Administrative complaints regarding warehouse worker protections (1) In general A covered employee or an individual who was a covered employee may\u2014 (A) file a complaint of a violation of section 102 of the Warehouse Worker Protection Act with the Secretary; and (B) designate a representative of a labor organization or worker advocacy organization, regardless of the relationship between the covered employee or individual and the labor organization or worker advocacy organization, to\u2014 (i) file the complaint on behalf of the covered employee or individual; or (ii) represent the covered employee or individual for purposes of engagement with the Secretary regarding such complaint, including being present at employee interviews and participating in workplace inspections, conferences, and settlement negotiations. (2) Definition of covered employee For purposes of paragraph (1), the term covered employee has the meaning given such term in section 102(a) of the Warehouse Worker Protection Act. (g) Exemption from the federal arbitration act regarding warehouse worker protections (1) In general Notwithstanding chapter 1 of title 9, United States Code (commonly known as the Federal Arbitration Act ), no predispute arbitration agreement or predispute joint-action waiver (as those terms are defined in section 401 of title 9, United States Code) shall be valid or enforceable with respect to claims arising under this Act for violations of section 102 of the Warehouse Worker Protection Act. (2) Arbitration pursuant to a collective bargaining agreement Nothing in this subsection shall limit the enforceability of any arbitration provision in a collective bargaining agreement between a covered employer (as defined in section 102(a) of the Warehouse Worker Protection Act) and a labor organization. (h) Exception from class action prerequisites for actions regarding warehouse worker protections An employee who brings an action for a violation of section 102 of the Warehouse Worker Protection Act on behalf of employees similarly situated shall be considered to have satisfied paragraphs (1) through (4) of rule 23(a) of the Federal Rules of Civil Procedure for purposes of such an action. .\n#### 104. Referral of complaints\n##### (a) Memorandum of understanding\nThe Director of the Fairness and Transparency Office established by section 5 of the Fair Labor Standards Act of 1938 (as added by section 101) and the Administrator of the Wage and Hour Office of the Department of Labor shall jointly enter into a memorandum of understanding with the Assistant Secretary of Labor for Occupational Safety and Health to encourage efficient enforcement of relevant labor laws, including through information sharing, referral of complaints, and cross-training of inspectors and investigators. The memorandum of understanding shall encourage coordination of enforcement activity in States enforcing relevant labor law under a State plan that has been approved by the Secretary under section 18 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 667 ).\n##### (b) Referral of complaints and cross-Training\nThe Director of the Fairness and Transparency Office shall, to the greatest extent possible\u2014\n**(1)**\nencourage the referral of relevant complaints from and to the Equal Employment Opportunity Commission, the National Institute for Occupational Safety and Health, the Environmental Protection Agency, the National Labor Relations Board, and other Federal and State agencies that may conduct inspections related to occupational health and safety in covered facilities (as defined in section 102(a) of the Warehouse Worker Protection Act); and\n**(2)**\npromote cross-training of inspectors and investigators in the Equal Employment Opportunity Commission, National Institute for Occupational Safety and Health, Environmental Protection Agency, and such other Federal and State agencies for inspections related to working conditions in such covered facilities.\n#### 105. Enforcement by the FTC\n##### (a) Unfair or deceptive acts or practices\nA violation of section 102 shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the FTC\n**(1) In general**\nThe Federal Trade Commission (in this section referred to as the Commission) shall enforce section 102 and the regulations promulgated under this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person who violates section 102 shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n**(4) Rulemaking**\nThe Commission may promulgate in accordance with section 553 of title 5, United States Code, such rules as may be necessary to carry out this section.\nII\nNATIONAL LABOR RELATIONS ACT\n#### 201. Amendments to National Labor Relations Act\n##### (a) In general\nSection 8(a) of the National Labor Relations Act ( 29 U.S.C. 158 ) is amended\u2014\n**(1)**\nin paragraph (5) by striking the period at the end and inserting ; and ; and\n**(2)**\nby adding at the end the following:\n(6) to impose on an employee a quota that significantly discourages or prevents, or is intended to significantly discourage or prevent, an employee from exercising the rights guaranteed in section 7. .\n##### (b) Presumption of retaliation\nSection 8 of the such Act ( 29 U.S.C. 158 ) is amended by adding at the end the following:\n(h) Presumption of retaliation related to a quota Any action to impose a quota on an employee that is taken against the employee within 90 days of an employee exercising the rights guaranteed in section 7 shall establish a rebuttable presumption that the action is discrimination against the employee in violation of subsection (a)(6). .\n##### (c) Definitions\nSection 2 such Act ( 29 U.S.C. 152 ) is amended by adding at the end the following:\n(15) Quota (A) In general The term quota means a performance standard or performance target, including such a standard or target used to rank an employee in relation to the performance of another employee or in relation to the past performance of the employee, under which\u2014 (i) (I) an employee is actually or effectively assigned, required, or expected within a defined time period (with or without any reasonable accommodation provided under Federal, State, or local law) to\u2014 (aa) perform\u2014 (AA) a quantified number of tasks; or (BB) at a specified productivity speed; or (bb) handle or produce a quantified amount of material without a certain number of errors or defects; and (II) such assignment, requirement, or expectation is measured at the individual or group level for such defined time period; (ii) actions by an employee are categorized and measured between time performing tasks and not performing tasks within a defined time period; or (iii) increments of time of a defined time period during which an employee is or is not doing a particular activity are measured, recorded, or tallied. (B) Defined time period For purposes of subparagraph (A), the term defined time period means any unit of time measurement equal to or less than one day, including hours, minutes, and seconds and any fraction thereof. .\n#### 202. National Labor Relations Board report\nThe National Labor Relations Board shall\u2014\n**(1)**\nexamine cases in which a quota (as such term is defined in section 2 of the National Labor Relations Act ( 29 U.S.C. 152 )) was used as a reason to deny a worker rights under the National Labor Relations Act; and\n**(2)**\nas often as practicable, submit a report on such cases to\u2014\n**(A)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate; and\n**(B)**\nthe Committee on Education and Workforce of the House of Representatives.\nIII\nOSHA STANDARDS\n#### 301. Standard protecting covered employees from occupational risk factors causing musculoskeletal disorders\n##### (a) Proposed standard\nNot later than 3 years after the date of enactment of this Act, the Secretary shall, pursuant to section 6 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 655 ), publish in the Federal Register a proposed standard for ergonomic program management for covered employers with respect to covered employees, including requirements for\u2014\n**(1)**\nhazard identification and ergonomic job evaluations for covered employees, including requirements for covered employee and designated employee representative participation in such identification with the aim of maximizing such participation;\n**(2)**\nhazard control at covered facilities, which may rely on the principles of the hierarchy of controls and which may include measures such as equipment and workstation redesign, work pace reductions, or job rotation to less forceful or repetitive jobs;\n**(3)**\ntraining for covered employees regarding covered employer activities, occupational risk factors, and training on controls and recognition of symptoms of musculoskeletal disorders; and\n**(4)**\nmedical management for covered employees that includes\u2014\n**(A)**\nencouraging early reporting of musculoskeletal disorder symptoms;\n**(B)**\nfirst aid delivered by those operating under State licensing requirements; and\n**(C)**\nsystematic evaluation and early referral for medical attention.\n##### (b) Final standard\nNot later than 4 years after the date of enactment this Act, the Secretary shall, pursuant to section 6 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 655 ), publish in the Federal Register a final standard based on the proposed standard under subsection (a).\n#### 302. Standard for protecting covered employees from delays in medical treatment referrals following injuries or illnesses\n##### (a) Proposed standard\nNot later than 1 year after the date of enactment of this Act, the Secretary shall, pursuant to section 6 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 655 ), publish in the Federal Register a proposed standard requiring that\u2014\n**(1)**\nall covered employers have a person readily available at the covered facility of the covered employer who is adequately trained to render first aid and ensure that such person provides first aid to any injured or ill covered employee and, without delay, refers any such covered employee who reports an injury or illness that requires further medical treatment to an appropriate medical professional for such treatment; and\n**(2)**\nall covered employers provide to the covered employees of the covered employer occupational medicine consultation services through a physician who is board certified in occupational medicine, which services shall include\u2014\n**(A)**\nregular review of any health and safety program, medical management program, or ergonomics program of the covered employer;\n**(B)**\nreview of any work-related injury or illness of a covered employee;\n**(C)**\nproviding onsite health services for treatment of such injury or illness; and\n**(D)**\nconsultation referral to a local health care provider for treating such injury or illness.\n##### (b) Final standard\nNot later than 3 years after the date of enactment of this Act, the Secretary shall, pursuant to section 6 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 655 ), publish in the Federal Register a final standard based on the proposed standard under subsection (a).\n#### 303. Correction of serious, willful, or repeated violations pending contest and procedures for a stay\n##### (a) In general\nSection 10 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 659 ) is amended by adding at the end the following:\n(d) Correction of serious, willful, or repeated violations pending contest and procedures for a stay (1) Period permitted for correction of serious, willful, or repeated violations For each violation which the Secretary designates as serious, willful, or repeated, the period permitted for the correction of the violation shall begin to run upon receipt of the citation. (2) Filing of a motion of contest The filing of a notice of contest by an employer shall not operate as a stay of the period for correction of a violation designated as serious, willful, or repeated. (3) Criteria and rules of procedure for stays (A) Motion for a stay An employer that receives a citation alleging a violation designated as serious, willful, or repeated and that files a notice of contest to the citation asserting that the time set for abatement of the alleged violation is unreasonable or challenging the existence of the alleged violation may file with the Commission a motion to stay the period for the abatement of the violation. (B) Criteria In determining whether a stay should be issued on the basis of a motion filed under subparagraph (A), the Commission may grant a stay only if the employer has demonstrated\u2014 (i) a substantial likelihood of success on the areas contested under subparagraph (A); and (ii) that a stay will not adversely affect the health and safety of employees. (C) Rules of procedure The Commission shall develop rules of procedure for conducting a hearing on a motion filed under subparagraph (A) on an expedited basis. At a minimum, such rules shall provide the following: (i) That a hearing before an administrative law judge shall occur not later than 15 days following the filing of the motion for a stay (unless extended at the request of the employer), and shall provide for a decision on the motion not later than 15 days following the hearing (unless extended at the request of the employer). (ii) That a decision of an administrative law judge on a motion for stay is rendered on a timely basis. (iii) That if a party is aggrieved by a decision issued by an administrative law judge regarding the stay, such party has the right to file an objection with the Commission not later than 5 days after receipt of the administrative law judge\u2019s decision. Within 10 days after receipt of the objection, a Commissioner, if a quorum is seated pursuant to section 12(f), shall decide whether to grant review of the objection. If, within 10 days after receipt of the objection, no decision is made on whether to review the decision of the administrative law judge, the Commission declines to review such decision, or no quorum is seated, the decision of the administrative law judge shall become a final order of the Commission. If the Commission grants review of the objection, the Commission shall issue a decision regarding the stay not later than 30 days after receipt of the objection. If the Commission fails to issue such decision within 30 days, the decision of the administrative law judge shall become a final order of the Commission. (iv) For notification to employees or representatives of affected employees of requests for such hearings, and to provide an opportunity for affected employees or representatives of affected employees to participate as parties to such hearings. .\n##### (b) Conforming amendments\n**(1) In general**\nThe Occupational Safety and Health Act of 1970 is amended\u2014\n**(A)**\nin the first sentence of section 10(b) ( 29 U.S.C. 659(b) ), by inserting , with the exception of violations designated as serious, willful, or repeated, after (which period shall not begin to run ; and\n**(B)**\nin section 17 ( 29 U.S.C. 666 ) by striking subsection (d) and inserting the following:\n(d) Any employer who fails to correct a violation designated by the Secretary as serious, willful, or repeated and for which a citation has been issued under section 9(a) within the period permitted for its correction (and a stay has not been issued by the Commission under section 10(d)) may be assessed a civil penalty of not more than $7,000 for each day during which such failure or violation continues. Any employer who fails to correct any other violation for which a citation has been issued under section 9(a) of this title within the period permitted for its correction (which period shall not begin to run until the date of the final order of the Commission in the case of any review proceeding under section 10 initiated by the employer in good faith and not solely for delay of avoidance of penalties) may be assessed a civil penalty of not more than $7,000 for each day during which such failure or violation continues. .\n**(2) Adjustment under the Federal civil penalties inflation adjustment act of 1990**\n**(A) Catch-up**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Labor shall adjust the maximum amounts described in subsection (d) of section 17 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 666 ), as amended by paragraph (1)(B), so that each such amount equals the maximum amount of the civil penalty under such subsection (as in effect on the day before such date of enactment) as adjusted by section 4 of the Federal Civil Penalties Inflation Adjustment Act of 1990 ( 28 U.S.C. 2461 note).\n**(B) Subsequent adjustments**\nSubparagraph (A) and the amendment made by this paragraph (1)(B) shall not be construed to affect the application of the Federal Civil Penalties Inflation Adjustment Act of 1990 ( 28 U.S.C. 2461 note) to the civil penalty amount under section 17(d) of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 666 ) for any adjustment under section 4 of the Federal Civil Penalties Inflation Adjustment Act of 1990 ( 28 U.S.C. 2461 note) after the catch-up adjustment made by the Secretary of Labor under subparagraph (A).\n#### 304. Definitions\nFor purposes of sections 301 and 302, the terms covered employee , covered employer , covered facility , and designated employee representative have the meanings given such terms in section 102(a).\nIV\nMISCELLANEOUS PROVISIONS\n#### 401. Severability\nIf any provision of this Act (including an amendment made by this Act) or the application of such provision to any person, entity, government, or circumstance, is held to be unconstitutional, the remainder of this Act (including the amendments made by this Act), or the application of such provision to all other persons, entities, governments, or circumstances, shall not be affected thereby.\n#### 402. Preemption\n##### (a) Interaction with other laws\nNothing in this Act (including the amendments made by this Act) or the regulations promulgated under this Act shall be construed to supersede or preempt any law or ordinance of a State, or political subdivision of a State, that requires limitations on any quota for a covered employee of a covered employer that are comparable to or greater than the protections provided in this Act.\n##### (b) Collective bargaining agreements\nNothing in this Act (including the amendments made by this Act) or the regulations promulgated under this Act shall be construed to supersede or preempt employment terms or conditions agreed upon in collective bargaining agreements that are more beneficial to a covered employee.\n##### (c) OSHA\nNo action by the Director under this Act (including the amendments made by this Act) shall be construed as an exercise of statutory authority within the meaning of section 4(b)(1) of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 653(b)(1) ).\n##### (d) Definitions\nFor purposes of this section, the terms Director , covered employee , covered employer , designated employee representative , and quota have the meanings given such terms in section 102(a).\n#### 403. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act such sums as may be necessary for each of the fiscal years 2025 through 2035.",
      "versionDate": "2025-08-05",
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
        "actionDate": "2025-07-31",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2613",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Warehouse Worker Protection Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-12-10T19:13:49Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4896ih.xml"
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
      "title": "Warehouse Worker Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Warehouse Worker Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T05:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish protections for warehouse workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T05:48:28Z"
    }
  ]
}
```
