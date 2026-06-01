# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2605
- Title: A bill to amend title 10, United States Code, to improve recruitment and retention of the cyber workforce of the Department of Defense, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 2605
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-19T18:35:20Z
- Update date including text: 2025-09-19T18:35:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2605",
    "number": "2605",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "A bill to amend title 10, United States Code, to improve recruitment and retention of the cyber workforce of the Department of Defense, and for other purposes.",
    "type": "S",
    "updateDate": "2025-09-19T18:35:20Z",
    "updateDateIncludingText": "2025-09-19T18:35:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T18:49:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2605is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2605\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Rounds introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to improve recruitment and retention of the cyber workforce of the Department of Defense, and for other purposes.\n#### 1. Cyber workforce recruitment and retention\n##### (a) In general\nSection 1599f of title 10, United States Code, is amended to read as follows:\n1599f. Cyber workforce recruitment and retention (a) General authority (1) In general The Secretary of Defense may\u2014 (A) establish, as positions in the excepted service, such qualified positions in the Department of Defense as the Secretary considers necessary to carry out the cyber mission of the Department and are not in the Defense Civilian Intelligence Personnel System, including\u2014 (i) positions in the Defense Digital Executive Service established under subsection (c); and (ii) Defense Digital Senior Level positions designated under subsection (d); (B) carry out a program of personnel management authority provided in subsection (b) in order to facilitate recruitment of eminent experts in cyber for the Department; and (C) implement an interagency transfer agreement between qualified positions in the excepted service established under this section and positions in the competitive service in the Department, including the military departments. (2) Applicability Unless explicitly provided otherwise by law, the authority of the Secretary under this section applies without regard to any other provision of law relating to the appointment, number, classification, or compensation of employees that the Secretary determines is incompatible with the approach to talent management under this section. (b) Personnel management authority (1) In general The Secretary may\u2014 (A) without regard to any provision of title 5 governing the appointment of employees in the civil service, appoint individuals to qualified positions established under subsection (a)(1); and (B) subject to paragraphs (2) and (3), fix the compensation of employees appointed under subparagraph (A). (2) Rates of basic pay The Secretary\u2014 (A) shall fix the rates of basic pay for employees appointed under paragraph (1)(A)\u2014 (i) with the rates of pay provided for employees in comparable positions in the Federal Government; and (ii) subject to the same limitations on maximum rates of pay established for such employees by statute or regulation; and (B) may prescribe the rates of basic pay for employees appointed under paragraph (1)(A) at rates not in excess of a rate equal to 150 percent of the maximum rate of basic pay authorized for positions at Level I of the Executive Schedule under section 5312 of title 5. (3) Additional compensation (A) In general Subject to subparagraph (C), the Secretary may, with respect to an employee appointed under paragraph (1)(A), other than such an employee receiving the maximum rate of basic pay prescribed under paragraph (2)(B), provide the employee compensation (in addition to basic pay), including payments, benefits, sabbaticals, incentives, awards, and allowances\u2014 (i) in accordance with relevant provisions of other laws, including provisions of title 5; (ii) consistent with, and not in excess of the level authorized for, comparable positions in the Federal Government; and (iii) to the extent compatible with the approach to talent management under this section. (B) Allowances An employee appointed under paragraph (1)(A) shall be eligible for an allowance under section 5941 of title 5, in addition to such basic pay, on the same basis and at least to the same extent as if the employee was an employee covered by such section, including eligibility conditions, allowance rates, and all other terms and conditions in statute or regulation. (C) Maximum amount of additional compensation No additional compensation may be provided to an employee under this paragraph in any calendar year if, or to the extent that, the employee\u2019s total annual compensation in such calendar year will exceed the maximum amount of total annual compensation payable at the salary set in accordance with section 104 of title 3. (c) Defense Digital Executive Service The Secretary may establish a Defense Digital Executive Service for positions established under subsection (a)(1)(A)(i) that are comparable to Senior Executive Service positions. (d) Defense Digital Senior Level positions The Secretary may designate as a Defense Digital Senior Level position any defense cyber position that, as determined by the Secretary\u2014 (1) is classified above the grade of GG\u201315 of the excepted service; (2) does not satisfy functional or program management criteria for being designated as a position in the Defense Digital Executive Service; and (3) has no more than minimal supervisory responsibilities. (e) Two-Year probationary period The probationary period for all employees hired under the authority provided by this section shall be two years. (f) Incumbents of existing competitive service positions (1) In general An individual occupying a position on the date of the enactment of this section that is selected to be converted to a position in the excepted service under this section shall have the right to refuse such conversion. (2) Position conversion After the date on which an individual who refuses a conversion under paragraph (1) stops serving in the position selected to be converted, the position shall be converted to a position in the excepted service. (g) Implementation plan; effective date of authority (1) In general The authority provided by this section shall become effective 30 days after the date on which the Secretary submits to the congressional defense committees a plan for the implementation of such authority. (2) Elements The plan described in paragraph (1) shall include the following: (A) An assessment of the current scope of the positions covered by the authority provided by subsection (a). (B) A plan for the use of the authority. (C) An assessment of the anticipated workforce needs for the cyber mission of the Department across the future-years defense program. (D) Other matters as appropriate. (h) Collective bargaining agreements Nothing in subsection (a) may be construed to impair the continued effectiveness of a collective bargaining agreement with respect to an office, component, subcomponent, or equivalent of the Department that is a successor to an office, component, subcomponent, or equivalent of the Department covered by the agreement before the succession. (i) Regulations required The Secretary, in coordination with the Director of the Office of Personnel Management, shall prescribe regulations for the administration of this section. (j) Annual report (1) In general Not later than one year after the date of the enactment of this section and not less frequently than once each year thereafter until the date that is five years after the date of the enactment of this section, the Director of the Office of Personnel Management, in coordination with the Secretary, shall submit to the appropriate committees of Congress a detailed report on the administration of this section during the most recent one-year period. (2) Elements Each report required by paragraph (1) shall include, for the period covered by the report, the following: (A) A discussion of the process used in accepting applications, assessing candidates, ensuring adherence to veterans' preference, and selecting applicants for vacancies to be filled by an individual for a qualified position. (B) A description of the following: (i) How the Secretary plans to fulfill the critical need of the Department to recruit and retain employees in qualified positions. (ii) The measures that will be used to measure progress. (iii) Any actions taken during the reporting period to fulfill such critical need. (C) A discussion of how the planning and actions taken under subparagraph (B) are integrated into the strategic workforce planning of the Department. (D) The metrics on actions occurring during the reporting period, including the following: (i) The number of employees in qualified positions hired, disaggregated by occupation and grade and level or pay band. (ii) The placement of employees in qualified positions, disaggregated by military department, Defense Agency, or other component within the Department. (iii) The total number of veterans hired. (iv) The number of separations of employees in qualified positions, disaggregated by occupation and grade and level or pay band. (v) The number of retirements of employees in qualified positions, disaggregated by occupation and grade and level or pay band. (vi) The number and amounts of recruitment, relocation, and retention incentives paid to employees in qualified positions, disaggregated by occupation and grade and level or pay band. (vii) The number of employees in qualified positions who held an appointment related to cybersecurity at a Federal agency outside of the Department during the three-year period prior to being appointed under this section. (k) Comptroller General assessment (1) Availability of annual report The Director of the Office of Personnel Management shall make available to the Comptroller General of the United States each report required by subsection (j). (2) Assessment The Comptroller General shall\u2014 (A) assess any differences in recruitment and retention for cyber positions experienced by Federal agencies based on unique hiring and pay authorities for cyber professionals, including with respect to Senior Executive Service positions and Senior Level positions; and (B) not later than five years after the date of the enactment of this section, submit to the appropriate committees of Congress the results of that assessment. (l) Definitions In this section: (1) Appropriate committees of Congress The term appropriate committees of Congress means\u2014 (A) the Committee on Armed Services, the Committee on Homeland Security and Governmental Affairs, and the Committee on Appropriations of the Senate; and (B) the Committee on Armed Services, the Committee on Oversight and Government Reform, and the Committee on Appropriations of the House of Representatives. (2) Competitive service The term competitive service has the meaning given that term in section 2102 of title 5. (3) Excepted service The term excepted service has the meaning given that term in section 2103 of title 5. (4) Qualified position The term qualified position means a position, designated by the Secretary for the purpose of this section, in which the individual occupying such position performs, manages, or supervises functions that execute the cyber mission of the Department. (5) Senior Executive Service position The term Senior Executive Service position has the meaning given that term in section 3132(a) of title 5. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 81 of such title is amended by striking the item relating to section 1599f and inserting the following new item:\n1599f. Cyber workforce recruitment and retention. .",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-09-17",
        "text": "Considered by Senate. (consideration: CR S6667: 5)"
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T18:35:20Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2605is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to improve recruitment and retention of the cyber workforce of the Department of Defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:48Z"
    },
    {
      "title": "A bill to amend title 10, United States Code, to improve recruitment and retention of the cyber workforce of the Department of Defense, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T10:56:36Z"
    }
  ]
}
```
