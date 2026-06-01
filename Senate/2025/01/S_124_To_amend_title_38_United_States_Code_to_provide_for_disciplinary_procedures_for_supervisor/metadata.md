# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/124
- Title: Restore VA Accountability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 124
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-04-15T11:03:26Z
- Update date including text: 2026-04-15T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/124",
    "number": "124",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Restore VA Accountability Act of 2025",
    "type": "S",
    "updateDate": "2026-04-15T11:03:26Z",
    "updateDateIncludingText": "2026-04-15T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
            "date": "2025-03-11T14:30:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-11T14:30:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-16T19:05:51Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AL"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AR"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ND"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NE"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SC"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TN"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "SD"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s124is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 124\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Moran (for himself, Mr. Tuberville , Mr. Cassidy , Mr. Banks , Mrs. Blackburn , Mr. Boozman , Mr. Sheehy , Mr. Cramer , Mr. Tillis , Mr. Ricketts , Mr. Scott of Florida , Mr. Risch , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for disciplinary procedures for supervisors and managers at the Department of Veterans Affairs and to modify the procedures of personnel actions against employees of the Department, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restore Department of Veterans Affairs Accountability Act of 2025 or the Restore VA Accountability Act of 2025 .\n#### 2. Supervisors: removal, demotion, or suspension based on performance or misconduct\n##### (a) Discipline of supervisors\n**(1) In general**\nTitle 38, United States Code, is amended by inserting after section 711 the following:\n712. Supervisors: removal, demotion, or suspension based on performance or misconduct (a) In general The Secretary may remove from civil service, demote, or suspend a covered individual who is an employee of the Department if the Secretary determines by substantial evidence that the performance or misconduct of the covered individual warrants such action. (b) Rights and procedures (1) (A) When making an initial decision under subsection (a) with respect to determining whether a covered individual should be removed, demoted, or suspended, the deciding employee of the Department shall exclusively apply the following factors: (i) The nature and seriousness of the offense, and its relation to the covered individual\u2019s duties, position, and responsibilities, including whether the offense was intentional or technical or inadvertent, or was committed maliciously or for gain, or was frequently repeated. (ii) The covered individual\u2019s job level and type of employment, including supervisory or fiduciary role, and prominence of the position. (B) The Secretary shall review the initial decision and uphold such decision if it is supported by substantial evidence. (2) A covered individual subject to an action under subsection (a) is entitled to\u2014 (A) advance notice of the action and a file containing all evidence in support of the proposed action; (B) be represented by an attorney or other representative of the covered individual\u2019s choice; and (C) grieve the action in accordance with an internal grievance process that the Secretary, in consultation with the Assistant Secretary for Accountability and Whistleblower Protection, shall establish for purposes of this subsection. (3) A final decision by the Secretary under paragraph (1)(B) that is not grieved, and a grievance decision under paragraph (2)(C), shall be final and conclusive. (4) The procedures under chapter 43 of title 5 shall not apply to a removal, demotion, or suspension under this section, and the Secretary may carry out such a removal, demotion, or suspension without first placing a covered individual on a performance improvement plan. (c) Timing (1) (A) The aggregate period for notice, response, and final decision by the Secretary of an action under this section may not exceed 15 business days. (B) The period for the response of a covered individual to a notice under subsection (b)(2)(A) shall be 7 business days. (C) The final decision by the Secretary under subsection (b)(1)(B) shall\u2014 (i) be issued not later than 15 business days after notice is provided under subsection (b)(2)(A); and (ii) be in writing and shall include the specific reasons for the decision. (D) The Secretary shall ensure that the grievance process established under paragraph (2)(C) takes fewer than 21 days after the final decision. (d) Judicial review (1) A covered individual adversely affected by a final decision under this section that is not grieved, or by a grievance decision under subsection (b)(2)(C), may obtain judicial review of such decision. (2) Any removal, demotion, or suspension under this section is not appealable to the Merit Systems Protection Board, or to any administrative judge or other person appointed by the Merit Systems Protection Board. (3) In any case in which judicial review is sought under paragraph (1), the court shall review the record and may set aside any Department action found to be\u2014 (A) arbitrary, capricious, an abuse of discretion, or otherwise not in accordance with a provision of law; (B) obtained without procedures required by a provision of law having been followed; or (C) unsupported by substantial evidence. (4) Except to the extent that an appeal under this subsection presents a constitutional issue, such court may not review a challenge to the penalty imposed against the covered individual or mitigate such penalty. (e) Demoted individuals (1) A demotion under subsection (a) shall be carried out as a reduction in grade for which the covered individual is qualified, that the Secretary determines is appropriate, and that reduces the annual rate of pay of the covered individual. (2) Notwithstanding any other provision of law, any covered individual so demoted\u2014 (A) shall, beginning on the date of such demotion, receive the annual rate of pay applicable to such grade; (B) may not be placed on administrative leave during the period during which an appeal (if any) under this section is ongoing, and may only receive pay if the covered individual reports for duty or is approved to use accrued unused annual, sick, family medical, military, or court leave; and (C) who does not report for duty or receive approval to use accrued unused leave shall not receive pay or other benefits. (f) Whistleblower protection (1) In the case of a covered individual seeking corrective action (or on behalf of whom corrective action is sought) from the Office of Special Counsel based on an alleged prohibited personnel practice described in section 2302(b) of title 5, the Secretary may not remove, demote, or suspend such covered individual under subsection (a) without the approval of the Special Counsel under section 1214(f) of title 5. (2) In the case of a covered individual who has made a whistleblower disclosure to the Assistant Secretary for Accountability and Whistleblower Protection, the Secretary may not remove, demote, or suspend such covered individual under subsection (a) until\u2014 (A) in the case in which the Assistant Secretary determines to refer the whistleblower disclosure under section 323(c)(1)(D) of this title to an office or other investigative entity, a final decision with respect to the whistleblower disclosure has been made by such office or other investigative entity; or (B) in the case in which the Assistant Secretary determines not to refer the whistleblower disclosure under such section, the Assistant Secretary makes such determination. (g) Termination of investigations by office of special counsel (1) Notwithstanding any other provision of law, the Special Counsel (established by section 1211 of title 5) may terminate an investigation of a prohibited personnel practice alleged by an employee or former employee of the Department after the Special Counsel provides to the employee or former employee a written statement of the reasons for the termination of the investigation. (2) Such statement may not be admissible as evidence in any judicial or administrative proceeding without the consent of such employee or former employee. (h) Application This section shall apply to any performance or misconduct of a covered individual beginning on the date of enactment of the Department of Veterans Affairs Accountability and Whistleblower Protection Act of 2017 ( Public Law 115\u201341 ). (i) Definitions In this section: (1) The term civil service has the meaning given that term in section 2101 of title 5. (2) The term covered individual means an employee of the Department who is a supervisor or management official as defined in section 7103(a) of title 5 occupying a position at the Department, including individuals appointed pursuant to this title, title 5, and hybrid employees appointed pursuant to section 7401 of this title, but does not include\u2014 (A) an individual occupying a senior executive position (as defined in section 713(d) of this title); (B) an individual appointed pursuant to section 7306, 7401(1), 7401(4), or 7405 of this title; (C) an individual who has not completed a probationary or trial period; or (D) a political appointee. (3) The term grade has the meaning given such term in section 7511(a) of title 5. (4) The term misconduct includes neglect of duty, malfeasance, or failure to accept a directed reassignment or to accompany a position in a transfer of function. (5) The term political appointee means an individual who is\u2014 (A) employed in a position described under sections 5312 through 5316 of title 5 (relating to the Executive Schedule); (B) a limited term appointee, limited emergency appointee, or noncareer appointee in the Senior Executive Service, as defined under paragraphs (5), (6), and (7), respectively, of section 3132(a) of title 5; or (C) employed in a position of a confidential or policy-determining character under schedule C of subpart C of part 213 of title 5, Code of Federal Regulations, or successor regulation. (6) The term suspend means the placing of an employee, for disciplinary reasons, in a temporary status without duties and pay for a period in excess of 14 days. (7) The term whistleblower disclosure has the meaning given such term in section 323(g) of this title. .\n**(2) Clerical amendment**\nThe table of contents for title 38, United States Code, is amended by inserting after the item relating to section 711 the following:\n712. Supervisors: removal, demotion, or suspension based on performance or misconduct. .\n#### 3. Senior executives: modification of procedures to remove, demote, or suspend based on performance or misconduct\nSection 713 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by inserting by substantial evidence after determines ; and\n**(B)**\nby adding at the end the following new paragraphs:\n(3) When making an initial decision under this subsection with respect to determining whether a covered individual should be reprimanded or suspended, involuntarily reassigned, demoted, or removed, the deciding employee of the Department shall exclusively apply the following factors: (A) The nature and seriousness of the offense, and its relation to the covered individual\u2019s duties, position, and responsibilities, including whether the offense was intentional or technical or inadvertent, or was committed maliciously or for gain, or was frequently repeated. (B) The covered individual\u2019s job level and type of employment, including supervisory or fiduciary role, and prominence of the position. (4) The Secretary shall review the initial decision and uphold such decision if it is supported by substantial evidence. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (3), by inserting after the final decision after 21 days ; and\n**(B)**\nby adding at the end the following:\n(7) Except to the extent that an appeal under this subsection presents a constitutional issue, such court may not review a challenge to the penalty imposed against the covered individual or mitigate such penalty. ; and\n**(3)**\nby redesignating subsection (d) as subsection (e); and\n**(4)**\nby inserting after subsection (c) the following new subsection (d):\n(d) Application This section shall apply to any misconduct or performance of a covered individual beginning on the date of the enactment of the Department of Veterans Affairs Accountability and Whistleblower Protection Act of 2017 ( Public Law 115\u201341 ). .\n#### 4. Modification of disciplinary procedures for employees of the Department of Veterans Affairs\n##### (a) Department of Veterans Affairs employee discipline modifications\nSection 714 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by inserting by substantial evidence after the Secretary determines ; and\n**(B)**\nby adding at the end the following:\n(3) (A) When making an initial decision under this subsection with respect to determining whether a covered individual should be removed, demoted, or suspended, the deciding employee of the Department shall exclusively apply the following factors: (i) The nature and seriousness of the offense, and its relation to the covered individual\u2019s duties, position, and responsibilities, including whether the offense was intentional or technical or inadvertent, or was committed maliciously or for gain, or was frequently repeated. (ii) The covered individual\u2019s job level and type of employment, including supervisory or fiduciary role, and prominence of the position. (iii) The covered individual\u2019s past disciplinary record. (iv) The covered individual\u2019s past work record, including length of service, performance on the job, ability to get along with fellow workers, and dependability. (v) Mitigating circumstances surrounding the offense such as unusual job tensions, personality problems, mental impairment, harassment, or bad faith, malice, or provocation on the part of others involved in the matter. (B) The Secretary shall review the initial decision and uphold such decision if it is supported by substantial evidence. ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby striking paragraph (1)(D); and\n**(B)**\nin paragraph (3), by inserting before the period the following: , and the Secretary may carry out such a removal, demotion, or suspension without first placing a covered individual on a performance improvement plan ;\n**(3)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (2), by adding at the end the following:\n(C) Except to the extent that an appeal under this subsection presents a constitutional issue, the administrative judge may not review a challenge to the penalty imposed against the covered individual. ;\n**(B)**\nin paragraph (3), by adding at the end the following:\n(D) Except to the extent that an appeal under this subsection presents a constitutional issue, the Merit Systems Protection Board may not review a challenge to the penalty imposed against the covered individual. ;\n**(C)**\nin paragraph (5), by adding at the end the following:\n(C) Except to the extent that an appeal under this subsection presents a constitutional issue, such Court may not review a challenge to the penalty imposed against the covered individual or mitigate such penalty. ; and\n**(D)**\nby striking paragraph (10);\n**(4)**\nby redesignating subsection (h) as subsection (j);\n**(5)**\nby inserting after subsection (g) the following:\n(h) Collective bargaining agreements The procedures in this section shall supersede any collective bargaining agreement to the extent that such agreement is inconsistent with such procedures. (i) Application This section shall apply to any performance or misconduct of a covered individual beginning on the date of the enactment of the Department of Veterans Affairs Accountability and Whistleblower Protection Act of 2017 ( Public Law 115\u201341 ). ; and\n**(6)**\nin paragraph (1) of subsection (j), as redesignated by paragraph (4)\u2014\n**(A)**\nin the matter before subparagraph (A), by inserting including individuals appointed pursuant to this title, title 5, and hybrid employees appointed pursuant to section 7401 of this title, after Department, ;\n**(B)**\nin subparagraph (D), by striking the period and inserting ; or ; and\n**(C)**\nby adding after subparagraph (D) the following:\n(E) a supervisor or management official as defined in section 7103(a) of title 5. .\n##### (b) Veterans Health Administration employee discipline modifications\nSection 7403(f)(3) of such title is amended\u2014\n**(1)**\nby striking Notwithstanding any other provision of this title or other law, and inserting (A) Notwithstanding any other provision of this title or other law, and consistent with subparagraph (B), ; and\n**(2)**\nby adding at the end the following:\n(B) With respect to any covered individual (as that term is defined in section 712 or 714) appointed to such positions, such matters shall be resolved, at Secretary\u2019s sole discretion, under\u2014 (i) section 712; (ii) section 714; or (iii) title 5 as though such individuals had been appointed under that title. .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-12-19",
        "text": "Referred to the Subcommittee on Oversight and Investigations."
      },
      "number": "472",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Restore VA Accountability Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-07T15:24:25Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-03-07T15:24:25Z"
          },
          {
            "name": "Employee performance",
            "updateDate": "2025-03-07T15:24:25Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-03-07T15:24:25Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-07T15:24:25Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-07T15:24:25Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-03-07T15:24:25Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-07T15:24:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-28T20:30:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "Senate",
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
          "measure-id": "id119s124",
          "measure-number": "124",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s124v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Restore Department of Veterans Affairs Accountability Act of 2025 or the Restore VA Accountability Act of 2025</strong></p><p>This bill modifies personnel action procedures regarding certain employees and executives of the Department of Veterans Affairs (VA).\u00a0</p><p>The bill authorizes the VA to remove from civil service, demote, or suspend VA employees that are supervisors or managers if the VA determines by substantial evidence that the performance or misconduct of such individual warrants such action. This authority does not apply to certain appointees or individuals in their probationary or trial period.</p><p>Supervisors or managers who are subject to a removal, demotion, or suspension under this bill are entitled to (1) advance notice of the action and supporting evidence, (2) representation by an attorney or representative, and (3) grieve the action in accordance with an internal grievance process.</p><p>The bill also provides protections from removal, demotion, or suspension for supervisor or managers who are\u00a0whistleblowers or are seeking corrective action for an alleged prohibited personnel practice such as discrimination.</p><p>The bill also modifies the procedures to remove, demote, or suspend VA employees or senior executives based on performance or misconduct, specifically by requiring the VA to determine by substantial evidence that the performance or misconduct of the individual warrants such removal, demotion, or suspension. Such procedures must apply retroactively, beginning on the date of enactment of the Department of Veterans Affairs Accountability and\u00a0Whistleblower Protection Act of 2017 (June 23, 2017).</p>"
        },
        "title": "Restore VA Accountability Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s124.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restore Department of Veterans Affairs Accountability Act of 2025 or the Restore VA Accountability Act of 2025</strong></p><p>This bill modifies personnel action procedures regarding certain employees and executives of the Department of Veterans Affairs (VA).\u00a0</p><p>The bill authorizes the VA to remove from civil service, demote, or suspend VA employees that are supervisors or managers if the VA determines by substantial evidence that the performance or misconduct of such individual warrants such action. This authority does not apply to certain appointees or individuals in their probationary or trial period.</p><p>Supervisors or managers who are subject to a removal, demotion, or suspension under this bill are entitled to (1) advance notice of the action and supporting evidence, (2) representation by an attorney or representative, and (3) grieve the action in accordance with an internal grievance process.</p><p>The bill also provides protections from removal, demotion, or suspension for supervisor or managers who are\u00a0whistleblowers or are seeking corrective action for an alleged prohibited personnel practice such as discrimination.</p><p>The bill also modifies the procedures to remove, demote, or suspend VA employees or senior executives based on performance or misconduct, specifically by requiring the VA to determine by substantial evidence that the performance or misconduct of the individual warrants such removal, demotion, or suspension. Such procedures must apply retroactively, beginning on the date of enactment of the Department of Veterans Affairs Accountability and\u00a0Whistleblower Protection Act of 2017 (June 23, 2017).</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119s124"
    },
    "title": "Restore VA Accountability Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restore Department of Veterans Affairs Accountability Act of 2025 or the Restore VA Accountability Act of 2025</strong></p><p>This bill modifies personnel action procedures regarding certain employees and executives of the Department of Veterans Affairs (VA).\u00a0</p><p>The bill authorizes the VA to remove from civil service, demote, or suspend VA employees that are supervisors or managers if the VA determines by substantial evidence that the performance or misconduct of such individual warrants such action. This authority does not apply to certain appointees or individuals in their probationary or trial period.</p><p>Supervisors or managers who are subject to a removal, demotion, or suspension under this bill are entitled to (1) advance notice of the action and supporting evidence, (2) representation by an attorney or representative, and (3) grieve the action in accordance with an internal grievance process.</p><p>The bill also provides protections from removal, demotion, or suspension for supervisor or managers who are\u00a0whistleblowers or are seeking corrective action for an alleged prohibited personnel practice such as discrimination.</p><p>The bill also modifies the procedures to remove, demote, or suspend VA employees or senior executives based on performance or misconduct, specifically by requiring the VA to determine by substantial evidence that the performance or misconduct of the individual warrants such removal, demotion, or suspension. Such procedures must apply retroactively, beginning on the date of enactment of the Department of Veterans Affairs Accountability and\u00a0Whistleblower Protection Act of 2017 (June 23, 2017).</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119s124"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s124is.xml"
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
      "title": "Restore VA Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restore VA Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restore Department of Veterans Affairs Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to provide for disciplinary procedures for supervisors and managers at the Department of Veterans Affairs and to modify the procedures of personnel actions against employees of the Department, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:22Z"
    }
  ]
}
```
