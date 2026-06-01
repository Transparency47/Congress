# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/687?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/687
- Title: MERIT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 687
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-03-19T16:13:21Z
- Update date including text: 2025-03-19T16:13:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/687",
    "number": "687",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000583",
        "district": "11",
        "firstName": "Barry",
        "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
        "lastName": "Loudermilk",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "MERIT Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-19T16:13:21Z",
    "updateDateIncludingText": "2025-03-19T16:13:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:06:35Z",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AR"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "UT"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KS"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "PA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "AR"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AZ"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TN"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "OK"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "MD"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr687ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 687\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Loudermilk (for himself, Mr. Carter of Georgia , Mrs. Houchin , Mr. Crawford , Mr. Owens , Mr. Collins , Mrs. Luna , Mr. Webster of Florida , Mr. Mann , Mr. Scott Franklin of Florida , Mr. Meuser , Mr. Babin , Ms. Tenney , Mr. Baird , Mr. Steube , and Mr. Burchett ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to provide for an alternative removal for performance or misconduct for Federal employees.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Modern Employment Reform, Improvement, and Transformation Act of 2025 or the MERIT Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Termination of authority for chapter 43 performance-based actions.\nSec. 3. Adverse actions based on performance or conduct.\nSec. 4. Prohibition on grieving adverse actions and reductions in force.\nSec. 5. Actions against senior executives for performance or conduct.\nSec. 6. Actions against supervisors for performance or conduct.\nSec. 7. Modification of procedures for furlough.\nSec. 8. Reduction of annuity of employee convicted of a felony for which an adverse action is or would have been taken.\nSec. 9. Authority to recoup bonuses or awards paid to employees.\nSec. 10. Extension of probationary period for positions within the Senior Executive Service.\nSec. 11. Extension of probationary period for employees in the competitive service.\nSec. 12. Application.\n#### 2. Termination of authority for chapter 43 performance-based actions\n##### (a) Repeal\nSection 4303 of title 5, United States Code, is repealed.\n##### (b) Application\nSubsection (a) shall not apply to any performance-based action under section 4303 of title 5, United States Code, commenced before the effective date provided in section 12.\n##### (c) Conforming amendments\n**(1) Title 5**\nTitle 5, United States Code, is amended\u2014\n**(A)**\nin section 2302(e)(1)(A), by striking 3504, and 4303(e) and inserting and 3504 ;\n**(B)**\nin section 4302(c)(6), by striking but only after an opportunity to demonstrate acceptable performance ;\n**(C)**\nin section 7512, by striking subparagraph (D) and redesignating subparagraphs (E) and (F) as subparagraphs (D) and (E), respectively;\n**(D)**\nin section 7701(c)(1), by striking decision and all that follows through preponderance of the evidence and inserting decision is supported by a preponderance of the evidence ;\n**(E)**\nin section 9508(d), by striking (1) In applying and all that follows through (2) ; and\n**(F)**\nin section 9902(a)(2), by striking sections 4302 and 4303(e) and inserting section 4302 .\n**(2) Title 31**\nSection 732(d)(3) of title 31, United States Code, is amended by striking consistent with section 4303 of title 5 .\n##### (d) Clerical amendment\nThe table of sections for chapter 43 of title 5, United States Code, is amended by striking the item relating to section 4303.\n#### 3. Adverse actions based on performance or conduct\n##### (a) In general\nSection 7513 of title 5, United States Code, is amended to read as follows:\n7513. Cause and procedure (a) In general (1) Under regulations prescribed by the Office of Personnel Management, an agency may take an action described in paragraphs (1) through (4) of section 7512 against an employee if the agency determines by a preponderance of the evidence the performance or misconduct of the employee warrants such action. (2) (A) When making an initial decision on an action described in paragraphs (1) through (4) of section 7512, the deciding employee of the agency shall exclusively apply the following factors: (i) The nature and seriousness of the offense, and its relation to the employee\u2019s duties, position, and responsibilities, including whether the offense was intentional or technical or inadvertent, or was committed maliciously or for gain, or was frequently repeated. (ii) The employee\u2019s job level and type of employment, including supervisory or fiduciary role, and prominence of the position. (iii) The employee\u2019s past disciplinary records. (iv) The employee\u2019s past work record, including length of service, performance on the job, ability to get along with fellow workers, and dependability. (v) Mitigating circumstances surrounding the offense such as unusual job tensions personality problems, mental impairment, harassment, or bad faith, malice or provocation on the part of others involved in the matter. (B) The agency shall review the initial decision and uphold such decision if it is supported by substantial evidence. (b) Pay of certain employees subject to a reduction in grade (1) Notwithstanding any other provision of law, an employee subject to a reduction in grade shall, beginning on the date of such reduction, receive the annual rate of pay applicable to such grade. (2) An employee subject to a reduction in grade may not be placed on administrative leave during the period during which an appeal (if any) under this section is ongoing, and may only receive pay if the employee reports for duty or is approved to use accrued unused annual, sick, family medical, military, or court leave. (3) If an employee subject to a reduction in grade does not report for duty or receive approval to use accrued unused leave, such employee shall not receive pay or other benefits. (c) Procedure (1) (A) The aggregate period for written notice, response, and final decision of actions described in paragraphs (1) through (4) of section 7512 may not exceed 15 business days unless there are reasonable causes to believe the employee has committed a crime for which a sentence of imprisonment may be imposed. (B) The period for which an employee may respond to a notice of actions described in paragraphs (1) through (4) of section 7512 in writing and to furnish affidavits and other documentary evidence in support of the response shall be 7 business days. (2) The agency shall issue a final decision with respect to actions described in paragraphs (1) through (4) of section 7512 not later than 15 business days after the agency provides notice, including a file containing all the evidence in support of the proposed action, to the employee. The decision shall be in writing and shall include the specific reasons therefor. (d) PIP The agency may carry out such actions described in paragraphs (1) through (4) of section 7512 without first placing an employee on a performance improvement plan. (e) Employee rights An employee against whom actions described in paragraphs (1) through (4) of section 7512 is proposed is entitled to\u2014 (1) a written notice stating the specific reasons for the proposed action; (2) be represented by an attorney or other representative; and (3) a written decision and the specific reasons therefor at the earliest practicable date. (f) Hearing An agency may provide, by regulation, for a hearing which may be in lieu of or in addition to the opportunity to answer provided under subsection (c)(1)(b) of this section. (g) Appeal An employee against whom an action described in paragraphs (1) through (4) of section 7512 is taken is entitled to appeal to the Merit Systems Protection Board under section 7701 of this title not later than 10 business days after the effective date of the action. (h) Procedure Copies of the notice of proposed action, the answer of the employee when written, a summary thereof when made orally, the notice of decision and reasons therefor, and any order effecting an action described in paragraphs (1) through (4) of section 7512, together with any supporting material, shall be maintained by the agency and shall be furnished to the Board upon its request. Upon the affected employee\u2019s request, copies of the documents described in the preceding sentence shall be furnished to the employee, to the extent those documents were not provided under subsection (c). .\n##### (b) Discipline of supervisors based on retaliation against whistleblowers\nSection 7515(b)(2)(B) of title 5, United States Code, is amended\u2014\n**(1)**\nin clause (i), by striking not later than 14 days and inserting not more than 7 business days ; and\n**(2)**\nin clause (ii), by striking 14-day period and inserting 7-business-day period .\n##### (c) Application\nThe amendments made by subsections (a) and (b) shall not apply to any action under section 7513 or 7515 of title 5, United States Code, as amended by those subsections, respectively, commenced before the effective date provided in section 12.\n#### 4. Prohibition on grieving adverse actions and reductions in force\nSection 7121 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1), by striking the settlement of ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby redesignating paragraphs (1) through (5) as paragraphs (5) through (9), respectively; and\n**(B)**\nby inserting before paragraph (5), as so redesignated, the following:\n(1) an adverse action under subchapter II of chapter 75; (2) a furlough of more than 30 days by a reduction in force action under subchapter I of chapter 35; (3) a separation by a reduction in force action under subchapter I of chapter 35; (4) a demotion by a reduction in force action under subchapter I of chapter 35; ;\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking (1) Matters and all that follows through but not both. ; and\n**(ii)**\nin the second sentence, by striking Similar matters and inserting Matters similar to those covered under subchapter II of chapter 75 ; and\n**(B)**\nby striking paragraph (2); and\n**(4)**\nin subsection (f)\u2014\n**(A)**\nby striking the first sentence; and\n**(B)**\nin the second sentence, by striking In matters similar to those covered under sections 4303 and 7512 of this title and inserting In matters similar to those covered under subchapter II of chapter 75 .\n#### 5. Actions against senior executives for performance or conduct\n##### (a) Repeal of pay retention for career appointees removed from the Senior Executive Service\nSection 3594(c)(1)(B) of title 5, United States Code, is amended to read as follows:\n(B) (i) any career appointee placed under subsection (a) or (b)(2) of this section shall be entitled to receive basic pay at the highest of\u2014 (I) the rate of basic pay in effect for the position in which placed; (II) the rate of basic pay in effect at the time of the placement for the position the career appointee held in the civil service immediately before being appointed to the Senior Executive Service; or (III) the rate of basic pay in effect for the career appointee immediately before being placed under subsection (a) or (b) of this section; and (ii) any career appointee placed under subsection (b)(1) of this section shall be entitled to receive basic pay at the rate of basic pay in effect for the position in which placed; and .\n##### (b) Appraisal system requirements\nSection 4314(b) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (3), by inserting before the semicolon the following: or, as warranted, from the civil service ; and\n**(2)**\nin paragraph (4), by inserting before the period at the end the following: or, as warranted, from the civil service .\n##### (c) Suspension for 14 days or less\nParagraph (1) of section 7501 of title 5, United States Code, is amended to read as follows:\n(1) employee means\u2014 (A) an individual in the competitive service who is not serving a probationary period or trial period under an initial appointment or who has completed 1 year of current continuous employment in the same or similar positions under other than a temporary appointment limited to 1 year or less; or (B) a career appointee in the Senior Executive Service who\u2014 (i) has completed the probationary period prescribed under section 3393(d); or (ii) was covered by the provisions of subchapter II of this chapter immediately before appointment to the Senior Executive Service; and .\n##### (d) Modification of cause and procedure for suspension and termination\nSection 7543 of title 5, United States Code, is amended to read as follows:\n7543. Cause and procedure (a) Under regulations prescribed by the Office of Personnel Management, an agency may take an action covered by this subchapter against an employee if the agency determines by a preponderance of the evidence the performance or misconduct of the employee warrants such action. (b) When making an initial decision on an action covered by this subchapter, the deciding employee of the agency shall exclusively apply the following factors\u2014 (1) the nature and seriousness of the offense, and its relation to the employee\u2019s duties, position, and responsibilities, including whether the offense was intentional or technical or inadvertent, or was committed maliciously or for gain, or was frequently repeated; and (2) the employee\u2019s job level and type of employment, including supervisory or fiduciary role, and prominence of the position. (c) The agency shall review the initial decision and uphold such decision if it is supported by substantial evidence. (d) (1) (A) The aggregate period for written notice, response, and final decision of actions covered by this subchapter may not exceed 15 business days unless there are reasonable causes to believe the employee has committed a crime for which a sentence of imprisonment may be imposed. (B) The period for which an employee may respond to a notice of actions covered by this subchapter in writing and to furnish affidavits and other documentary evidence in support of the response shall be 7 business days. (2) The agency shall issue a final decision with respect to a covered actions not later than 15 business days after the agency provides notice, including a file containing all the evidence in support of the proposed action, to the employee. The decision shall be in writing and shall include the specific reasons therefor. (e) An employee against whom an action covered by this subchapter is proposed is entitled to\u2014 (1) a written notice stating the specific reasons for the proposed action; (2) be represented by an attorney or other representative; and (3) a written decision and the specific reasons therefor at the earliest practicable date. (f) An agency may provide, by regulation, for a hearing which may be in lieu of or in addition to the opportunity to answer provided under subsection (d)(1)(B) of this section. (g) An employee against whom an action is taken under this section is entitled to appeal to the Merit Systems Protection Board under section 7701 of this title not later than 10 business days after the effective date of the action. (h) Copies of the notice of proposed action, the answer of the employee when written, a summary thereof when made orally, the notice of decision and reasons therefor, and any order effecting an action covered by this subchapter, together with any supporting material, shall be maintained by the agency and shall be furnished to the Board upon its request. Upon the affected employee\u2019s request, copies of the documents described in the preceding sentence shall be furnished to the employee, to the extent those documents were not provided under subsection (c). (i) In this section, the term misconduct includes neglect of duty, malfeasance, or failure to accept a directed reassignment or to accompany a position in a transfer of function. .\n##### (e) Relation to other provisions of law\nSection 3592(b)(1) of title 5, United States Code, deso not apply to an action under section 7543(a), as amended in subsection (d).\n##### (f) Conforming amendments\nTitle 5, United States Code, is amended\u2014\n**(1)**\nin section 3592(b)(2)(B), by striking any disciplinary action and inserting any action under section 7543 ;\n**(2)**\nin section 3593(a)(2), by striking misconduct, neglect of duty, malfeasance, and inserting a removal under section 7543 ;\n**(3)**\nin section 3594, by adding at the end the following:\n(d) This section shall not apply to any career appointee who is subject to a personnel action under subchapter V of chapter 75. ; and\n**(4)**\nin section 7542, by striking or to a removal under section 3592 or 3595 and inserting the following: to a removal from the Senior Executive Service under section 3592 of this title, to a reduction in force as defined in section 3595(d) of this title, or to a transfer of function as described in section 3595(e) .\n##### (g) Application\nThe amendments made by this section shall not apply to any personnel action under subchapter V of chapter 75 of title 5, United States Code, commenced before the effective date of this Act.\n#### 6. Actions against supervisors for performance or conduct\nSubchapter II of title 5, United States Code, is amended\u2014\n**(1)**\nby redesignating sections 7514 and 7515 as sections 7516 and 7517, respectively; and\n**(2)**\nby inserting after section 7513 the following:\n7514. Supervisors (a) In general (1) The agency may take an action covered by this subchapter against a supervisor, as defined in section 7103(a)(10), if the agency determines by a preponderance of the evidence that the performance or misconduct of the supervisor warrants such action. (2) When making an initial decision on an action covered by this subchapter, the deciding employee of the agency shall exclusively apply the following factors: (A) The nature and seriousness of the offense, and its relation to the supervisor\u2019s duties, position, and responsibilities, including whether the offense was intentional or technical or inadvertent, or was committed maliciously or for gain, or was frequently repeated. (B) The supervisor\u2019s job level and type of employment, including supervisory or fiduciary role, and prominence of the position. (3) The agency shall review the initial decision and uphold such decision if it is supported by substantial evidence. (4) A supervisor against whom an action covered by this subchapter is proposed is entitled to\u2014 (A) a written notice stating the specific reasons for the proposed action; (B) be represented by an attorney or other representative; and (C) a written decision and the specific reasons therefor at the earliest practicable date. (5) The agency may carry out such action covered by this subchapter without first placing a supervisor on a performance improvement plan. (6) The procedures under chapter 43 shall not apply to an action covered by this subchapter. (b) Procedure (1) (A) The aggregate period for written notice, response, and final decision of actions covered by this subchapter may not exceed 15 business days unless there are reasonable causes to believe the employee has committed a crime for which a sentence of imprisonment may be imposed. (B) The period for which an employee may respond to a notice of actions covered by this subchapter in writing and to furnish affidavits and other documentary evidence in support of the response shall be 7 business days. (2) The agency shall issue a final decision with respect to a covered action not later than 15 business days after the agency provides notice, including a file containing all the evidence in support of the proposed action, to the employee. The decision shall be in writing and shall include the specific reasons therefor. (c) Reduction in grade (1) A reduction in grade under subsection (a) shall be carried out as a reduction in grade for which the covered individual is qualified, that the agency determines is appropriate, and that reduces the annual rate of pay of the supervisor. (2) Notwithstanding any other provision of law, any supervisor subject to a reduction in grade\u2014 (A) shall, beginning on the date of such demotion, receive the annual rate of pay applicable to such grade; (B) may not be placed on administrative leave during the period during which an appeal (if any) under this section is ongoing, and may only receive pay if the supervisor reports for duty or is approved to use accrued unused annual, sick, family medical, military, or court leave; and (C) who does not report for duty or receive approval to use accrued unused leave shall not receive pay or other benefits. (d) Definition In this section, the term supervisor has the meaning given that term under section 7103(a). .\n#### 7. Modification of procedures for furlough\n##### (a) Furlough of 14 days or less; emergency furlough\nSubchapter I of chapter 75 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 7501, as amended by section 5(c),\u2014\n**(A)**\nin paragraph (1) by striking and at the end;\n**(B)**\nby redesignating paragraph (2) as paragraph (4); and\n**(C)**\nby inserting the following after paragraph (1) the following:\n(2) furlough has the meaning given that term in section 7511(a)(5); (3) emergency furlough means a furlough due to a lapse in appropriations; ;\n**(2)**\nin section 7502, by striking This subchapter and all that follows through this title. and inserting the following:\nThis subchapter applies to\u2014 (1) a suspension for 14 days or less, but not a suspension under section 7521 or 7532 or any action initiated under section 1215; (2) a furlough for 14 days or less; and (3) an emergency furlough of any duration. ;\n**(3)**\nby redesignating section 7504 as section 7505; and\n**(4)**\nby inserting after section 7503, the following:\n7504. Furlough and emergency furlough cause and procedure (a) General Furlough (1) In general An employee may be subject to a furlough for such cause as will promote the efficiency of the service. Any employee furloughed under this section is entitled to the procedures established under the regulations promulgated under paragraph (2). (2) Procedures Not later than 180 days after the date of enactment of this section, the Office of Personnel Management shall promulgate regulations providing for\u2014 (A) the circumstances under which an employee may be furloughed under this section; (B) the procedures to be afforded furloughed employees, including, to the extent appropriate and practicable under the circumstances of the furlough action\u2014 (i) a written notice stating the specific reasons for the proposed action; (ii) be represented by an attorney or other representative; and (iii) a written decision and the specific reasons therefor at the earliest practicable date; and (C) the materials that shall be furnished to a furloughed employee and the Merit Systems Protection Board upon request of the employee or the Board. (b) Emergency furlough (1) In general An employee may be subject to an emergency furlough. (2) Procedures (A) Notice Under regulations prescribed by the Office of Personnel Management, any employee subject to an emergency furlough shall be afforded notice explaining the reasons for the emergency furlough. If the notice cannot be provided in advance of the emergency furlough, notice shall be provided as soon as reasonably practicable. (B) Other procedures No other procedures, including those provided under subsection (a) or any other provision of this title, shall be available to any employee subject to an emergency furlough under this subsection. (3) Definition For the purposes of this section, the term employee means any employee described under section 7501(1). .\n##### (b) Furlough of more than 14 days\nSubchapter II of chapter 75 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 7511(a)(5) by inserting before the period the following: , but does not include an emergency furlough as defined in section 7501 of title 5 .\n**(2)**\nin section 7512, as amended by section 2(c)\u2014\n**(A)**\nin paragraph (5) by striking a furlough of 30 days or less and inserting a furlough of more than 14 days but less than 31 days ;\n**(B)**\nin subparagraph (D), as redesignated by section 2(c), by striking or at the end;\n**(C)**\nin subparagraph (E), as redesignated by section 2(c), by striking the period at the end and inserting ; or ; and\n**(D)**\nby adding at the end the following:\n(F) an emergency furlough action under section 7504. ;\n**(3)**\nby inserting after section 7514, as added by section 6, the following:\n7515. Furlough cause and procedure (a) In general An employee may be subject to a furlough for such cause as will promote the efficiency of the service. Any employee furloughed under this section is entitled to the procedures established under the regulations promulgated under subsection (b). (b) Procedures Not later than 180 days after the date of enactment of this section, the Office of Personnel Management shall promulgate regulations providing for\u2014 (1) the circumstances under which an employee may be furloughed under this section; (2) the procedures provided under section 7513 to the extent appropriate and practicable under the circumstances of the furlough action; and (3) the materials that shall be furnished to a furloughed employee and the Merit Systems Protection Board upon request of the employee or the Board. (c) Appeal An employee against whom a furlough action is taken under this section is entitled to appeal to the Merit Systems Protection Board under section 7701 not later than 10 business days after the effective date of the action. .\n##### (d) Administrative Law Judges\nSection 7521(b) of title 5, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B) by striking or at the end;\n**(2)**\nin subparagraph (C) by striking the period at the end and inserting or ; and\n**(3)**\nby adding at the end the following:\n(D) an emergency furlough action under section 7504. .\n##### (e) Technical amendments\n**(1) Section 7503**\nThe heading of section 7503 of title 5, United States Code, is amended by striking Cause and procedure and inserting Suspension cause and procedure ,.\n**(2) Section 7513**\nSection 7513 of title 5, United States Code, is amended by striking Cause and procedure and inserting Cause and procedure for actions other than furlough .\n##### (f) Clerical amendments\n**(1) Subchapter I of chapter 75 of title 5**\nThe table of sections for subchapter I of chapter 75 of title 5, United States Code, is amended by striking the items relating to sections 7503 and 7504 and inserting the following:\n7503. Suspension cause and procedure. 7504. Furlough and emergency furlough cause and procedure. 7505. Regulations. .\n**(2) Subchapter II of chapter 75 of title 5**\nThe table of sections for subchapter II of chapter 75 of title 5, United States Code, is amended by striking the items relating to sections 7513 through 7515 and inserting the following:\n7513. Cause and procedure for actions other than furlough. 7514. Supervisors. 7515. Furlough cause and procedure. 7516. Regulations. 7517. Discipline of supervisors based on retaliation against whistleblowers. .\n##### (g) Application\nNotwithstanding section 12, the amendments made by this section shall take effect on the earlier of\u2014\n**(1)**\nthe date that is 180 days after the date of enactment of this Act; or\n**(2)**\nthe date on which the Office of Personnel Management promulgates regulations provided under sections 7504 and 7515 of title 5, United States Code, as added by this section.\n#### 8. Reduction of annuity of employee convicted of a felony for which an adverse action is or would have been taken\n##### (a) Reduction of annuity of employee convicted of a felony for which an adverse action is taken\n**(1) In general**\nSubchapter II of chapter 83 of title 5, United States Code, is amended by adding at the end the following:\n8323. Reduction of benefits of employees convicted of certain crimes (a) Reduction of annuity (1) In general The felonious service of a covered individual shall not be taken into account for purposes of calculating an annuity with respect to the individual under subchapter III of this chapter or chapter 84 if\u2014 (A) the covered individual is finally convicted of a felony; and (B) the head of the agency at which the individual was employed determines that the conviction was based on the acts or omissions of the covered individual that\u2014 (i) were taken or not taken in the performance of the covered individual\u2019s official duties at the agency; and (ii) are sufficient to support a removal action under section 7513, 7543, or any other provision of law against the covered individual. (2) Procedures A covered individual against whom a determination is made under paragraph (1) shall be afforded\u2014 (A) notice of the determination not later than 15 business days in advance of a final order under paragraph (3); and (B) an opportunity to respond to the determination by not later than 10 business days after receipt of the notice. (3) Final order The head of the agency shall issue a final order to carry out paragraph (1) not later than\u2014 (A) in the case of a covered individual who responds under paragraph (2)(B), 5 business days after receiving the response from the covered individual, to the maximum extent practicable; or (B) in the case of a covered individual who does not so respond, 15 business days after the date on which the head of the agency provided notice to the individual under paragraph (2)(A), to the maximum extent practicable. (4) Appeal A covered individual with respect to whom an annuity is to be reduced under this subsection may appeal the final order under paragraph (3) to the Merit Systems Protection Board in accordance with any regulations that the Board may prescribe for purposes of this subsection. An appeal may not be made under this paragraph later than that date that is 10 business days after the date on which an order is issued under paragraph (3). (b) Administrative requirements (1) In general Not later than 30 business days after the date on which the head of an agency issues a final order under subsection (a) or a final decision of the Merit Systems Protection Board is rendered (as the case may be) with respect to an individual, the applicable employing agency shall amend the covered individual\u2019s retirement records to reflect the period of service that is no longer creditable by operation of this section and transmit the amended records to the Director of the Office of Personnel Management. (2) Annuitants With respect to any covered individual who is an annuitant on the date on which a final order is so issued, the Director of the Office of Personnel Management shall, not later than 30 business days after the receipt of amended retirement records from an agency under paragraph (1), recalculate the annuity of the annuitant. (c) Lump-Sum annuity credit A covered individual with respect to whom an annuity is reduced under subsection (a) shall be entitled to be paid so much of the individual\u2019s lump-sum credit as is attributable to the period of felonious service. (d) Spouse exception The spouse of any covered individual referred to in subsection (a) shall be eligible for spousal annuity benefits that, but for subsection (a), would otherwise have been payable if the Attorney General of the United States or the attorney general of a State, a territory, or the District of Columbia determines that the spouse fully cooperated with authorities in the conduct of a criminal investigation and subsequent prosecution of the individual that resulted in the benefit reduction. (e) Application Nothing in this section shall be construed to affect or otherwise mitigate the application of any other section of this subchapter. (f) Definitions In this section\u2014 (1) the term covered individual means\u2014 (A) an individual who is removed from a position as an employee (as defined in section 2105) in the civil service for performance or misconduct under section 7513, 7543, or any other provision of law; or (B) an individual who\u2014 (i) is an employee (as defined in section 2105) subject to a removal action for performance or misconduct under section 7513, 7543, or any other provision of law; and (ii) voluntarily separates from service with the employing agency prior to the issuance of a final decision with respect to the removal action; (2) the term felonious service means, with respect to a covered individual, the period of service\u2014 (A) beginning on the date on which the head of the employing agency determines that the individual commenced engaging in the acts or omissions that gave rise to the removal action or proposed removal action described in paragraph (1); and (B) ending on the date that is the earlier of\u2014 (i) the date on which the individual is removed from or voluntarily separates from a position at the agency; or (ii) the date on which the individual ceases engaging in the acts or omissions that gave rise to the removal action or proposed removal action described in paragraph (1); (3) the term finally convicted or final conviction refers to a conviction of a felony\u2014 (A) that has not been appealed and is no longer appealable because the time for taking an appeal has expired; or (B) that has been appealed and the appeals process for which is completed; (4) the term lump-sum credit has the meaning given that term in section 8331(8) or 8401(19) (as the case may be); and (5) the term service has the meaning given that term in section 8331(12) or 8401(26) (as the case may be). .\n**(2) Clerical amendment**\nThe table of sections for subchapter II of chapter 83 of title 5, United States Code, is amended by adding at the end the following:\n8323. Reduction of benefits of employees convicted of certain crimes. .\n##### (b) Application\nSection 8323 of title 5, United States Code, as added by subsection (a), shall apply to acts or omissions described in subsection (a)(1)(B) of that section occurring after the date of enactment of this Act.\n##### (c) Regulations\nThe Office of Personnel Management may prescribe regulations to carry out this section and the amendments made by this section.\n#### 9. Authority to recoup bonuses or awards paid to employees\n##### (a) Adverse findings and employees under investigation\nChapter 45 of title 5, United States Code, is amended by adding at the end the following:\nIV Limitations on bonus authority 4531. Certain forms of misconduct (a) Definitions In this section: (1) Adverse finding (A) In general The term adverse finding means a determination by the head of the agency employing an employee that the conduct of the employee\u2014 (i) violated a policy of the agency for which the employee may be removed or suspended for a period of not less than 14 days; or (ii) violated a law for which the employee may be imprisoned for more than 1 year. (B) Basis A determination described in subparagraph (A) may be based on an investigation by, a determination of, or information provided by the Inspector General or another senior ethics official of an agency or the Comptroller General of the United States, as part of carrying out an activity, authority, or function of the Inspector General, senior ethics official, or Comptroller General, respectively, under a provision of law other than this section. (2) Agency The term agency has the meaning given the term in section 551. (3) Bonus The term bonus means any performance award or cash award under\u2014 (A) section 4505a; (B) section 5384; or (C) section 5754. (4) Employee The term employee means an employee of an agency. (b) Prohibition The head of an agency may not award a bonus to an employee of the agency until the date that is 5 years after the end of the fiscal year during which the head of an agency makes an adverse finding relating to the employee. (c) After bonus awarded (1) In general For a bonus awarded to an employee after the date of enactment of this section, if the head of the agency employing the employee makes an adverse finding relating to the employee during the fiscal year in which the bonus is awarded, the head of the agency, after notice and an opportunity for a hearing, shall issue an order directing the employee to repay the amount of the bonus. (2) Repayment plan An agency shall allow an employee who is required to repay a bonus under paragraph (1) to repay that bonus using a repayment plan. (3) Hearings A hearing under this subsection shall be conducted in accordance with regulations relating to hearings promulgated by the head of the agency under chapter 75. (d) Condition of receipt As a condition of receiving a bonus awarded after the date of enactment of this section, an employee shall sign a certification stating that the employee shall repay the bonus in accordance with a final order issued under subsection (c). (e) Appeal An employee determined to be ineligible for a bonus under subsection (b) or against whom an order is issued under subsection (c) may submit an appeal to the Merit Systems Protection Board under section 7701. .\n##### (b) Rulemaking\nThe head of each agency, as defined in section 551 of title 5, United States Code, may promulgate rules to carry out section 4531 of title 5, United States Code, as added by subsection (a).\n##### (c) Technical and conforming amendment\nThe table of sections for chapter 45 of title 5, United States Code, is amended by adding at the end the following:\n\u201cSUBCHAPTER IV\u2014Limitations on bonus authority\n\u201c4531. Certain forms of misconduct.\n#### 10. Extension of probationary period for positions within the Senior Executive Service\n##### (a) In general\nSection 3393(d) of title 5, United States Code, is amended by striking 1-year and inserting 2-year .\n##### (b) Conforming amendment\nSection 3592(a)(1) of title 5, United States Code, is amended by striking 1-year and inserting 2-year .\n##### (c) Application\nThe amendments made by this section shall apply in the case of any individual initially appointed as a career appointee under section 3393 of title 5, United States Code, on or after the effective date provided in section 12 of this Act.\n#### 11. Extension of probationary period for employees in the competitive service\n##### (a) Extension of probationary period\n**(1) In general**\nSection 3321 of title 5, United States Code, is amended\u2014\n**(A)**\nin subsection (a), by striking The President and inserting Subject to subsections (c) and (d), the President ;\n**(B)**\nby redesignating subsection (c) as subsection (e); and\n**(C)**\nby inserting after subsection (b) the following:\n(c) (1) The length of a probationary period established under paragraph (1) or (2) of subsection (a) shall\u2014 (A) with respect to any position that requires formal training, begin on the date of the appointment to the position and end on the date that is 2 years after the date on which the formal training is completed; (B) with respect to any position that requires a license, begin on the date of the appointment to the position and end on the date that is 2 years after the date of the appointment or the date on which the license is granted, whichever is later; and (C) with respect to any position not covered by subparagraph (A) or (B), be a period of 2 years beginning on the date of the appointment to the position. (2) For purposes of paragraph (1)\u2014 (A) the term formal training means, with respect to any position, a training program required by law, rule, or regulation, or otherwise required by the employing agency, to be completed by the employee before the employee is able to successfully execute the duties of the applicable position; and (B) the term license means a license, certification, or other grant of permission to engage in a particular activity. (d) The head of each agency shall, in the administration of this section, take appropriate measures to ensure that\u2014 (1) any announcement of a vacant position and any offer of appointment made to an individual with respect to a vacant position clearly states the terms and conditions of any applicable probationary period, including any formal training period and any license requirement; (2) any individual who is required to complete a probationary period under this section receives timely notice of any requirements, including performance requirements, that must be met in order to satisfactorily complete that period; (3) any supervisor or manager of an individual who is required to complete a probationary period under this section receives periodic notifications of the end date of that period not later than 1 year, 6 months, 3 months, and 30 days before the end date; and (4) if the agency head decides to retain an individual after the completion of a probationary period under this section, the agency head submits a certification to that effect to the President, supported by a brief statement of the basis for the certification, in such form and manner as the President may by regulation prescribe. .\n**(2) Technical amendment**\nSection 3321(e) of title 5, United States Code (as so redesignated by paragraph (1)), is amended by striking Subsections (a) and (b) and inserting Subsections (a) through (d) .\n**(3) Application**\nThis subsection and the amendments made by this subsection shall apply in the case of any appointment (as referred to in section 3321(a)(1) of title 5, United States Code) and any initial appointment (as referred to in section 3321(a)(2) of that title) taking effect on or after the effective date provided in section 12 of this Act.\n##### (b) Adverse actions\n**(1) Subchapter I of chapter 75 of title 5**\nSection 7501(1) of title 5, United States Code, as amended by sections 5(c) and 7(a)(1), is further amended\u2014\n**(A)**\nby striking or, except and inserting and, except ; and\n**(B)**\nby striking 1 year of current and inserting 2 years of current .\n**(2) Subchapter II of chapter 75 of title 5**\nSection 7511(a)(1) of title 5, United States Code, is amended\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i), by striking ; or and inserting ; and ; and\n**(ii)**\nin clause (ii), by striking 1 year the first place it appears and inserting 2 years ;\n**(B)**\nin subparagraph (B), by striking 1 year and inserting 2 years ; and\n**(C)**\nin subparagraph (C)(i), by striking ; or and inserting ; and .\n**(3) Application**\nThe amendments made by paragraphs (1) and (2) shall apply in the case of any individual whose period of continuous service commences on or after the effective date provided in section 12.\n##### (c) Regulations\nThe Office of Personnel Management may prescribe regulations to carry out this section and the amendments made by this section.\n#### 12. Application\n##### (a) Effective date\nUnless otherwise specifically provided for in this Act, the amendments made by this Act shall take effect on the date that is 1 year after the date of enactment of this Act.\n##### (b) Collective bargaining agreements\nNotwithstanding any other provision of law, the procedures established or amended by this Act shall supersede any collective bargaining agreement to the extent that the agreement is inconsistent with those procedures.\n##### (c) Definition of business day\nFor purposes of carrying out this Act and the amendments made by this Act, the term business day means any day other than a Saturday, Sunday, or legal public holiday under section 6103(a) of title 5, United States Code.",
      "versionDate": "2025-01-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-19T16:12:36Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2025-03-19T16:12:23Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-03-19T16:13:01Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-03-19T16:12:54Z"
          },
          {
            "name": "Employee performance",
            "updateDate": "2025-03-19T16:11:15Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-03-19T16:11:42Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-03-19T16:13:21Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-19T16:10:57Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-03-19T16:11:33Z"
          },
          {
            "name": "Income tax deferral",
            "updateDate": "2025-03-19T16:13:14Z"
          },
          {
            "name": "Merit Systems Protection Board",
            "updateDate": "2025-03-19T16:12:30Z"
          },
          {
            "name": "Office of Personnel Management (OPM)",
            "updateDate": "2025-03-19T16:12:43Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2025-03-19T16:13:08Z"
          },
          {
            "name": "Unemployment",
            "updateDate": "2025-03-19T16:12:48Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-03-19T16:11:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-28T20:32:28Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr687ih.xml"
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
      "title": "MERIT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MERIT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modern Employment Reform, Improvement, and Transformation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to provide for an alternative removal for performance or misconduct for Federal employees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:03Z"
    }
  ]
}
```
