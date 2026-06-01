# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5750?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5750
- Title: EQUALS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5750
- Origin chamber: House
- Introduced date: 2025-10-14
- Update date: 2026-04-21T01:06:18Z
- Update date including text: 2026-04-21T01:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-14: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-02 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 24 - 19.
- 2026-04-09 - Calendars: Placed on the Union Calendar, Calendar No. 524.
- 2026-04-09 - Committee: Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-604.
- 2026-04-09 - Committee: Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-604.
- Latest action: 2025-10-14: Introduced in House

## Actions

- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-02 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 24 - 19.
- 2026-04-09 - Calendars: Placed on the Union Calendar, Calendar No. 524.
- 2026-04-09 - Committee: Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-604.
- 2026-04-09 - Committee: Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-604.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5750",
    "number": "5750",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000603",
        "district": "26",
        "firstName": "Brandon",
        "fullName": "Rep. Gill, Brandon [R-TX-26]",
        "lastName": "Gill",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "EQUALS Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-21T01:06:18Z",
    "updateDateIncludingText": "2026-04-21T01:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-04-09",
      "calendarNumber": {
        "calendar": "U00524"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 524.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-04-09",
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
      "text": "Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-604.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-604.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 24 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-14",
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
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-14",
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
        "item": [
          {
            "date": "2026-04-09T16:06:38Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-02T17:41:51Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-14T18:00:20Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "KY"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "AL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5750ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5750\nIN THE HOUSE OF REPRESENTATIVES\nOctober 14, 2025 Mr. Gill of Texas introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to modify probationary periods with respect to positions in the competitive service, to establish trial periods for positions in the excepted service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring a Qualified Civil Service Act of 2025 or the EQUALS Act of 2025 .\n#### 2. Extension of probationary period for positions within the competitive service\n##### (a) In general\nSection 3321 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking The President and inserting Subject to subsections (c), (d), and (e), the President ;\n**(2)**\nby redesignating subsection (c) as subsection (f); and\n**(3)**\nby inserting after subsection (b) the following:\n(c) (1) (A) Except as provided in subparagraph (B) or otherwise specified in law, an individual\u2019s initial appointment to a position in the competitive service shall become final only after the individual has served a 2-year probationary period. (B) A preference eligible\u2019s initial appointment to a position in the competitive service shall become final only after the individual has served a 1-year probationary period. (2) During an employee\u2019s probationary period under paragraph (1), the employing agency shall evaluate the fitness of the employee and whether the employee\u2019s continued employment advances the public interest. An employee shall be terminated from the civil service on the last day of the employee\u2019s probationary period unless the employing agency certifies, to the Director of the Office of Personnel Management within the 30 days before such date, that finalizing the employee\u2019s appointment advances the public interest. Before an agency terminates an employee serving under a probationary period pursuant to this subsection, the agency shall provide notice (in writing) to the employee of the effective date of such termination. (3) The appointment of an employee serving under a probationary period may not become final until the employee has demonstrated to the employee\u2019s supervisor, through official performance and other metrics as determined by the agency head in conformance with guidance issued by the Office of Personnel Management, that the employee\u2019s continued employment in the civil service is in the public interest. (4) With respect to any certification under paragraph (2), the agency head may consider, in the head\u2019s sole and exclusive discretion\u2014 (A) the employee\u2019s performance and conduct; (B) the needs and interests of the agency; (C) whether the employee\u2019s continued employment would advance organizational goals of the agency or the Federal Government; and (D) whether the employee\u2019s continued employment would advance the efficiency of the civil service. (5) If the head of an agency fails to make a certification under paragraph (2) due to an administrative error, the head may petition the Director of the Office of Personnel Management, within 30 days after the date an employee was terminated from the civil service, to reinstate the employee. Any employee reinstated within such 30-day period shall be entitled to backpay in accordance with section 5596 of this title. (6) This subsection\u2014 (A) shall apply to an employee appointed under chapter 73 or 74 of title 38, notwithstanding section 7401 of such title; and (B) shall not apply to\u2014 (i) an employee serving a probationary period due to being initially promoted, transferred, or otherwise assigned to a position as a supervisor (as that term is defined in section 7103 of this title) or any other managerial position, unless such employee is required to concurrently serve both a probationary period in such position and a probationary period following initial appointment or reinstatement; (ii) an employee of the United States Postal Service or the Postal Regulatory Commission; or (iii) the Congress or any congressional agency. (d) (1) Except as provided in paragraph (2), the length of a probationary period established under subsection (a) shall\u2014 (A) with respect to any position that requires formal training, begin on the date of appointment to the position and end on the date that is 2 years after the date on which such formal training is completed; (B) with respect to any position that requires a license, begin on the date of appointment to the position and end on the date that is 2 years after the date on which such license is granted; and (C) with respect to any position not covered by subparagraph (A) or (B), be a period of 2 years beginning on the date of the appointment to the position. (2) With respect to any preference eligible, paragraph (1) shall be applied by substituting 1 year for 2 years . (3) In paragraph (1)\u2014 (A) the term formal training means, with respect to any position, a training program required by law, rule, or regulation, or otherwise required by the employing agency, to be completed by the employee before the employee is able to successfully execute the duties of the applicable position; and (B) the term license means a license, certification, or other grant of permission to engage in a particular activity. (e) The head of each agency shall, in the administration of this section, take appropriate measures to ensure that\u2014 (1) any announcement of a vacant position within the agency and any offer of appointment made to any individual with respect to any such position clearly states the terms and conditions of any applicable probationary period, including any formal training period and any license requirement; (2) any individual who is required to complete a probationary period under this section receives timely notice of any requirements, including performance requirements, that must be met in order to satisfactorily complete such period; (3) any supervisor or manager of an individual who is required to complete a probationary period under this section receives periodic notifications of the end date of such period not later than 1 year, 6 months, 3 months, and 30 days before such end date; and (4) if the head decides to retain an individual after the completion of a probationary period under this section, the head submits a certification to that effect, supported by a brief statement of the basis for the certification, in such form and manner as the President may by regulation prescribe. .\n##### (b) Technical amendment\nSection 3321(f) of title 5, United States Code (as redesignated by subsection (a)(2) of this section), is amended by striking Subsections (a) and (b) and inserting Subsections (a) through (e) .\n##### (c) Effective date\nThis section and the amendments made by this section\u2014\n**(1)**\nshall take effect 1 year after the date of the enactment of this Act; and\n**(2)**\nshall apply to any individual appointed to a position in the competitive service, or any individual who is initially promoted, transferred, or otherwise assigned to be a supervisor and who is required to serve a probationary period under section 3321(c)(6)(B)(i) of title 5, United States Code (as added by subsection (a) of this section), on or after the effective date in paragraph (1) of this subsection.\n#### 3. Trial period in excepted service\n##### (a) In general\nSubchapter I of chapter 33 of title 5, United States Code, is amended by inserting after section 3321 the following (and conforming the table of contents of such subchapter accordingly):\n3321a. Excepted service; trial period (a) (1) Except as provided in paragraph (2), an employee appointed to a position in the excepted service shall serve a 2-year trial period. (2) A preference eligible appointed to a position in the excepted service shall serve a 1-year trial period. (b) An employee serving under a trial period pursuant to subsection (a) and who is transferred, promoted, demoted, or reassigned to any other excepted service position before the end of such trial period shall complete the remainder of such trial period in the new position. (c) An individual who separates from the civil service for a period of more than 30 days after completing a trial period under this section and who is reappointed to an excepted service position shall complete a new trial period unless such individual is appointed to the same or a substantially similar position in the same agency the employee held immediately before separation. (d) This section shall not apply to any agency or employee described in section 3321(c)(6)(B). .\n##### (b) Effective date\nThis section and the amendments made by this section\u2014\n**(1)**\nshall take effect 1 year after the date of the enactment of this Act; and\n**(2)**\nshall apply to any individual appointed to a position in the excepted service on or after the effective date in paragraph (1) of this subsection.\n#### 4. FAA and TSA\nSection 40122(g)(2) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking and at the end of subparagraph (I);\n**(2)**\nby striking the period at the end of subparagraph (J) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(K) sections 3321 and 3321a relating to probationary and trial periods, respectively. .\n#### 5. Adverse actions\n##### (a) Actions based on unacceptable performance\nSection 4303(f) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking 1 year of current continuous employment and inserting , with respect to a preference eligible 1 year of current continuous employment, and with respect to any other employee 2 years of current continuous employment, ; and\n**(2)**\nin paragraph (3), by striking 1 year of current continuous employment and inserting , with respect to a preference eligible 1 year of current continuous employment, and with respect to any other employee 2 years of current continuous employment, .\n##### (b) Subchapter I of chapter 75 of title 5\nSection 7501(1) of title 5, United States Code, is amended\u2014\n**(1)**\nby striking or who has and inserting and who has ; and\n**(2)**\nby striking 1 year of current continuous employment and inserting , with respect to a preference eligible 1 year of current continuous employment, and with respect to any other employee 2 years of current continuous employment, .\n##### (c) Subchapter II of chapter 75 of title 5\nSection 7511(a)(1) of title 5, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking ; or and inserting ; and ; and\n**(B)**\nin clause (ii), by striking 1 year of current continuous service and inserting , with respect to a preference eligible 1 year of current continuous service, and with respect to any other employee 2 years of current continuous service, ; and\n**(2)**\nin subparagraph (C)(i), by striking ; or and inserting ; and .\n##### (d) Effective date; application\nThe amendments made by subsections (a), (b), and (c)\u2014\n**(1)**\nshall take effect 1 year after the date of the enactment of this Act; and\n**(2)**\nshall apply in the case of any individual appointed to a position in the competitive service or excepted service on or after the effective date in paragraph (1).\n#### 6. Regulations required\nNot later than 180 days after the date of the enactment of this Act, the Director of the Office of Personnel Management shall issue such regulations as are necessary to carry out this Act and the amendments made by this Act.",
      "versionDate": "2025-10-14",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr5750rh.xml",
      "text": "IB\nUnion Calendar No. 524\n119th CONGRESS\n2d Session\nH. R. 5750\n[Report No. 119\u2013604]\nIN THE HOUSE OF REPRESENTATIVES\nOctober 14, 2025 Mr. Gill of Texas introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nApril 9, 2026 Additional sponsors: Mr. Comer , Mr. Cloud , Mr. Moore of Alabama , and Mr. Harrigan\nApril 9, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on October 14, 2025\nA BILL\nTo amend title 5, United States Code, to modify probationary periods with respect to positions in the competitive service, to establish trial periods for positions in the excepted service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring a Qualified Civil Service Act of 2025 or the EQUALS Act of 2025 .\n#### 2. Extension of probationary period for positions within the competitive service\n##### (a) In general\nSection 3321 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking The President and inserting Subject to subsections (c), (d), and (e), the President ;\n**(2)**\nby redesignating subsection (c) as subsection (f); and\n**(3)**\nby inserting after subsection (b) the following:\n(c) (1) (A) Except as provided in subparagraph (B) or otherwise specified in law, an individual\u2019s initial appointment to a position in the competitive service shall become final only after the individual has served a 2-year probationary period. (B) A preference eligible\u2019s initial appointment to a position in the competitive service shall become final only after the individual has served a 1-year probationary period. (2) During an employee\u2019s probationary period under paragraph (1), the employing agency shall evaluate the fitness of the employee and whether the employee\u2019s continued employment advances the public interest. An employee shall be terminated from the civil service on the last day of the employee\u2019s probationary period unless the employing agency certifies, to the Director of the Office of Personnel Management within the 30 days before such date, that finalizing the employee\u2019s appointment advances the public interest. Before an agency terminates an employee serving under a probationary period pursuant to this subsection, the agency shall provide notice (in writing) to the employee of the effective date of such termination. (3) The appointment of an employee serving under a probationary period may not become final until the employee has demonstrated to the employee\u2019s supervisor, through official performance and other metrics as determined by the agency head in conformance with guidance issued by the Office of Personnel Management, that the employee\u2019s continued employment in the civil service is in the public interest. (4) With respect to any certification under paragraph (2), the agency head may consider, in the head\u2019s sole and exclusive discretion\u2014 (A) the employee\u2019s performance and conduct; (B) the needs and interests of the agency; (C) whether the employee\u2019s continued employment would advance organizational goals of the agency or the Federal Government; and (D) whether the employee\u2019s continued employment would advance the efficiency of the civil service. (5) If the head of an agency fails to make a certification under paragraph (2) due to an administrative error, the head may petition the Director of the Office of Personnel Management, within 30 days after the date an employee was terminated from the civil service, to reinstate the employee. Any employee reinstated within such 30-day period shall be entitled to backpay in accordance with section 5596 of this title. (6) This subsection\u2014 (A) shall apply to an employee appointed under chapter 73 or 74 of title 38, notwithstanding section 7401 of such title; and (B) shall not apply to\u2014 (i) an employee serving a probationary period due to being initially promoted, transferred, or otherwise assigned to a position as a supervisor (as that term is defined in section 7103 of this title) or any other managerial position, unless such employee is required to concurrently serve both a probationary period in such position and a probationary period following initial appointment or reinstatement; (ii) an employee of the United States Postal Service or the Postal Regulatory Commission; or (iii) the Congress or any congressional agency. (d) (1) Except as provided in paragraph (2), the length of a probationary period established under subsection (a) shall\u2014 (A) with respect to any position that requires formal training, begin on the date of appointment to the position and end on the date that is 2 years after the date on which such formal training is completed; (B) with respect to any position that requires a license, begin on the date of appointment to the position and end on the date that is 2 years after the date on which such license is granted; and (C) with respect to any position not covered by subparagraph (A) or (B), be a period of 2 years beginning on the date of the appointment to the position. (2) With respect to any preference eligible, paragraph (1) shall be applied by substituting 1 year for 2 years . (3) In paragraph (1)\u2014 (A) the term formal training means, with respect to any position, a training program required by law, rule, or regulation, or otherwise required by the employing agency, to be completed by the employee before the employee is able to successfully execute the duties of the applicable position; and (B) the term license means a license, certification, or other grant of permission to engage in a particular activity. (e) The head of each agency shall, in the administration of this section, take appropriate measures to ensure that\u2014 (1) any announcement of a vacant position within the agency and any offer of appointment made to any individual with respect to any such position clearly states the terms and conditions of any applicable probationary period, including any formal training period and any license requirement; (2) any individual who is required to complete a probationary period under this section receives timely notice of any requirements, including performance requirements, that must be met in order to satisfactorily complete such period; (3) any supervisor or manager of an individual who is required to complete a probationary period under this section receives periodic notifications of the end date of such period not later than 1 year, 6 months, 3 months, and 30 days before such end date; and (4) if the head decides to retain an individual after the completion of a probationary period under this section, the head submits a certification to that effect, supported by a brief statement of the basis for the certification, in such form and manner as the President may by regulation prescribe. .\n##### (b) Technical amendment\nSection 3321(f) of title 5, United States Code (as redesignated by subsection (a)(2) of this section), is amended by striking Subsections (a) and (b) and inserting Subsections (a) through (e) .\n##### (c) Effective date\nThis section and the amendments made by this section\u2014\n**(1)**\nshall take effect 1 year after the date of the enactment of this Act; and\n**(2)**\nshall apply to any individual appointed to a position in the competitive service, or any individual who is initially promoted, transferred, or otherwise assigned to be a supervisor and who is required to serve a probationary period under section 3321(c)(6)(B)(i) of title 5, United States Code (as added by subsection (a) of this section), on or after the effective date in paragraph (1) of this subsection.\n#### 3. Trial period in excepted service\n##### (a) In general\nSubchapter I of chapter 33 of title 5, United States Code, is amended by inserting after section 3321 the following (and conforming the table of contents of such subchapter accordingly):\n3321a. Excepted service; trial period (a) (1) Except as otherwise specified in law or provided in paragraph (2), an employee appointed to a position in the excepted service shall serve a 2-year trial period. (2) A preference eligible appointed to a position in the excepted service shall serve a 1-year trial period. (b) An employee serving under a trial period pursuant to subsection (a) and who is transferred, promoted, demoted, or reassigned to any other excepted service position before the end of such trial period shall complete the remainder of such trial period in the new position. (c) An individual who separates from the civil service for a period of more than 30 days after completing a trial period under this section and who is reappointed to an excepted service position shall complete a new trial period unless such individual is appointed to the same or a substantially similar position in the same agency the employee held immediately before separation. (d) This section shall not apply to any agency or employee described in section 3321(c)(6)(B). .\n##### (b) Effective date\nThis section and the amendments made by this section\u2014\n**(1)**\nshall take effect 1 year after the date of the enactment of this Act; and\n**(2)**\nshall apply to any individual appointed to a position in the excepted service on or after the effective date in paragraph (1) of this subsection.\n#### 4. Faa and tsa\nSection 40122(g)(2) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking and at the end of subparagraph (I);\n**(2)**\nby striking the period at the end of subparagraph (J) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(K) sections 3321 and 3321a relating to probationary and trial periods, respectively. .\n#### 5. Adverse actions\n##### (a) Actions based on unacceptable performance\nSection 4303(f) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking 1 year of current continuous employment and inserting , with respect to a preference eligible 1 year of current continuous employment, and with respect to any other employee 2 years of current continuous employment, ; and\n**(2)**\nin paragraph (3), by striking 1 year of current continuous employment and inserting , with respect to a preference eligible 1 year of current continuous employment, and with respect to any other employee 2 years of current continuous employment, .\n##### (b) Subchapter I of chapter 75 of title 5\nSection 7501(1) of title 5, United States Code, is amended\u2014\n**(1)**\nby striking or who has and inserting and who has ; and\n**(2)**\nby striking 1 year of current continuous employment and inserting , with respect to a preference eligible 1 year of current continuous employment, and with respect to any other employee 2 years of current continuous employment, .\n##### (c) Subchapter II of chapter 75 of title 5\nSection 7511(a)(1) of title 5, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking ; or and inserting ; and ; and\n**(B)**\nin clause (ii), by striking 1 year of current continuous service and inserting , with respect to a preference eligible 1 year of current continuous service, and with respect to any other employee 2 years of current continuous service, ; and\n**(2)**\nin subparagraph (C)(i), by striking ; or and inserting ; and .\n##### (d) Effective date; application\nThe amendments made by subsections (a), (b), and (c)\u2014\n**(1)**\nshall take effect 1 year after the date of the enactment of this Act; and\n**(2)**\nshall apply in the case of any individual appointed to a position in the competitive service or excepted service on or after the effective date in paragraph (1).\n#### 6. Regulations required\nNot later than 180 days after the date of the enactment of this Act, the Director of the Office of Personnel Management shall issue such regulations as are necessary to carry out this Act and the amendments made by this Act.",
      "versionDate": "2026-04-09",
      "versionType": "Reported in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employee hiring",
            "updateDate": "2025-12-05T19:47:34Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-12-05T19:47:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-14T01:46:18Z"
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
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5750ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr5750rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "EQUALS Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-04-10T06:08:23Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Ensuring a Qualified Civil Service Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-04-10T06:08:23Z"
    },
    {
      "title": "EQUALS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EQUALS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring a Qualified Civil Service Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to modify probationary periods with respect to positions in the competitive service, to establish trial periods for positions in the excepted service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:14Z"
    }
  ]
}
```
