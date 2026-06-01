# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6833?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6833
- Title: ARCA Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6833
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-21T08:07:57Z
- Update date including text: 2026-05-21T08:07:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6833",
    "number": "6833",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "ARCA Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:57Z",
    "updateDateIncludingText": "2026-05-21T08:07:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
            "date": "2026-05-20T13:26:44Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:49:47Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-18T14:03:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6833ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6833\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Barrett introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to reorganize the acquisition structure of the Department of Veterans Affairs and to establish the Director of Cost Assessment and Program Evaluation in the Department, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Acquisition Reform and Cost Assessment Act of 2025 or the ARCA Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Department of Veterans Affairs acquisition organization.\nSec. 3. Department of Veterans Affairs major acquisition program managers.\nSec. 4. Department of Veterans Affairs acquisition and procurement reorganization matters.\nSec. 5. Independent verification and validation of major acquisition programs of Department of Veterans Affairs.\nSec. 6. Department of Veterans Affairs cost assessment and program evaluation.\nSec. 7. Improvements to hiring of entry-level acquisition positions in the Department of Veterans Affairs.\nSec. 8. Independent analysis of acquisition process of Department of Veterans Affairs.\nSec. 9. Requirements development process.\nSec. 10. Conforming amendments.\nSec. 11. Clerical amendments.\n#### 2. Department of Veterans Affairs acquisition organization\n##### (a) Definitions\nChapter 81 of title 38, United States Code, is amended by inserting after subchapter VI the following new subchapter:\nVII Acquisition organization, cost assessment, and program evaluation 8181. Definition of major acquisition program In this subchapter, the term major acquisition program means a program of the Department to acquire services, supplies, technology, systems, or a combination thereof, with an estimated total program cost, estimated by the Secretary, that exceeds\u2014 (1) $1,000,000,000 (adjusted pursuant to section 1908 of title 41) for the total life cycle cost of the program; or (2) $200,000,000 (adjusted pursuant to section 1908 of title 41) annually. .\n##### (b) Assistant Secretary for Acquisition\nSection 308 of such title is amended\u2014\n**(1)**\nin subsection (a)(1), by striking seven and inserting eight ; and\n**(2)**\nin subsection (b)(10), by striking Procurement functions and inserting Acquisition functions .\n##### (c) Acquisition organization\nSubchapter VI of chapter 81 of such title, as added by subsection (a), is amended by adding at the end the following new section:\n8182. Acquisition organization (a) Assistant Secretary for Acquisition; Chief Acquisition Officer (1) The Secretary shall designate one of the Assistant Secretaries specified in subsection (a)(1) of section 308 of this title as the Assistant Secretary of Veterans Affairs for Acquisition, who shall focus solely on the administration of functions specified in subsection (b)(10) of such section. (2) Pursuant to section 1702(a) of title 41, the Secretary shall designate the Assistant Secretary of Veterans Affairs for Acquisition as the Chief Acquisition Officer of the Department. (b) Office of Acquisition (1) There is in the Department an Office of Acquisition. (2) The head of the Office of Acquisition shall be the Assistant Secretary of Veterans Affairs for Acquisition designated pursuant to subsection (a). (3) The Secretary shall take such actions as may be necessary to ensure that major acquisition program offices of the Department align under the Office of Acquisition and report directly to the Assistant Secretary of Veterans Affairs for Acquisition. (4) The budget of the Office of Acquisition, including budgets for major acquisition programs, shall be established in the budget justification materials submitted to Congress in support of the budget of the Department (as submitted with the budget of the President under section 1105(a) of title 31). (c) Deputy Assistant Secretary for Logistics (1) Pursuant to section 308(d) of this title, the Secretary shall appoint a Deputy Assistant Secretary of Veterans Affairs for Logistics, who shall report to the Assistant Secretary for Acquisition. (2) The Deputy Assistant Secretary of Veterans Affairs for Logistics shall be responsible for administration of logistics and supply chain operations of the Department. (d) Deputy Assistant Secretary for Procurement (1) Pursuant to section 308(d) of this title, the Secretary shall appoint a Deputy Assistant Secretary of Veterans Affairs for Procurement, who shall report to the Assistant Secretary for Acquisition. (2) The Deputy Assistant Secretary of Veterans Affairs for Procurement shall be responsible for all procurement and contracting organizations of the Department. (e) Deputy Assistant Secretary for Acquisition, Program Management, and Performance (1) Pursuant to section 308(d) of this title, the Secretary shall appoint a Deputy Assistant Secretary of Veterans Affairs for Acquisition, Program Management, and Performance, who shall report to the Assistant Secretary for Acquisition. (2) The Deputy Assistant Secretary for Acquisition, Program Management, and Performance shall be responsible for the following: (A) Lifecycle management. (B) Requirements planning. (C) Programming and budgeting. (D) Policy. (E) Performance standards. (F) Governance. (G) Enhancing the capabilities of the acquisition workforce. (f) Program Executive Officers (1) The Assistant Secretary for Acquisition shall appoint no fewer than four Program Executive Officers, each responsible for overseeing major acquisition programs in one of the following areas: (A) Medical. (B) Information technology. (C) Professional services. (D) Other areas not included in subparagraphs (A) through (C). (2) Each Program Executive Officer shall report directly to the Assistant Secretary for Acquisition and shall supervise the managers of major acquisition programs within their respective area, as appointed under section 8183 of this title. (3) Each Program Executive Officer shall be\u2014 (A) certified in project management at level three by\u2014 (i) the Department; (ii) the Federal Acquisition Institute pursuant to section 1201 of title 41; or (iii) the Department of Defense pursuant to section 1701a of title 10; or (B) hold an equivalent certification by a private sector project management certification organization, as determined appropriate by the Secretary. .\n#### 3. Department of Veterans Affairs major acquisition program managers\nSubchapter VI of chapter 81 of title 38, United States Code, as added by section 2, is amended by adding at the end the following new section:\n8183. Major acquisition program managers (a) Appointments Not later than 30 days after any date on which the Secretary approves a major acquisition program to commence, the applicable Program Executive Officer shall appoint a manager to be responsible for administering such program. (b) Qualifications Each manager appointed pursuant to subsection (a) shall be\u2014 (1) certified in project management at level three by\u2014 (A) the Department; (B) the Federal Acquisition Institute pursuant to section 1201 of title 41; or (C) the Department of Defense pursuant to section 1701a of title 10; or (2) hold an equivalent certification by a private sector project management certification organization, as determined appropriate by the Secretary. (c) Duties Each manager appointed pursuant to subsection (a) for a major acquisition program shall\u2014 (1) report to the Assistant Secretary for Acquisition through the Program Executive Officer responsible for the major acquisition program; and (2) shall be responsible for, with respect to the major acquisition program\u2014 (A) developing, in coordination with the Program Executive Officer, a plan to administer the major acquisition program, which shall be known as the program baseline for the major acquisition program, that includes\u2014 (i) a description of each acquisition phase of the major acquisition program; (ii) for each such acquisition phase, requirements for advancing the major acquisition program to a subsequent acquisition phase; and (iii) estimates of the cost, schedule, and performance of the major acquisition program that account for the entire life cycle of the major acquisition program; (B) ensuring the major acquisition program is in compliance with such requirements and providing all program documentation, including program baseline documentation, cost, schedule, performance and risk assessments, and other relevant materials, to designated officials and relevant governance boards; (C) developing resource requests and justifications necessary to satisfy such requirements; and (D) on a continuous basis, assessing and managing risks to satisfying the requirements of such program baseline relating to cost and schedule. (d) Program decision authority The Secretary shall ensure that\u2014 (1) program decision authority for oversight of a major acquisition program is the Assistant Secretary for Acquisition; and (2) program management offices for major acquisition programs are independent of the Veterans Benefits Administration, the Veterans Health Administration, the National Cemetery Administration, and staff offices of the Department by reporting directly to the Assistant Secretary for Acquisition. (e) Program decision authority notification required Not later than 30 days after any date on which a major acquisition program concludes an acquisition phase, the manager of such program appointed pursuant to subsection (a) shall notify the program decision authority under subsection (c). .\n#### 4. Department of Veterans Affairs acquisition and procurement reorganization matters\n##### (a) Organizational consolidation\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall organizationally consolidate under the Assistant Secretary of Veterans Affairs for Acquisition every activity of the Department of Veterans Affairs, including the Veterans Benefits Administration, the Veterans Health Administration, and the National Cemetery Administration, that relates to\u2014\n**(1)**\nacquisition;\n**(2)**\nprocurement and contracting; or\n**(3)**\nlogistics and supply chain.\n##### (b) Relocation\nSubsection (a) shall not be construed to require the physical relocation of employees of the Department.\n##### (c) Plan and briefing\n**(1) In general**\nNot later than 90 days after commencing organizational consolidation under subsection (a), the Secretary shall\u2014\n**(A)**\nsubmit to the Committee on Veterans' Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives a written plan to carry out such organizational consolidation; and\n**(B)**\nprovide such committees a briefing on such plan.\n**(2) Contents**\nThe plan submitted pursuant to paragraph (1)(A) shall include the following:\n**(A)**\nA timeline.\n**(B)**\nA plan for communication and training activities for relevant Department personnel.\n**(C)**\nA plan for modification of relevant Department policy and guidance.\n**(D)**\nSuch other matters as the Secretary considers relevant and appropriate.\n#### 5. Independent verification and validation of major acquisition programs of Department of Veterans Affairs\n##### (a) Contracting authority\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall seek to enter into one or more contracts using competitive procedures with one or more entities to carry out the functions described in subsection (c).\n##### (b) Eligibility\n**(1) In general**\nAn entity is not eligible to be awarded a contract under this section unless the Chief Acquisition Officer of the Department of Veterans Affairs determines, at the time of evaluation of offers submitted under subsection (a), that the entity is currently performing or has performed, during the preceding three-year period, not fewer than three prime contracts from either governmental or commercial health care organizations for\u2014\n**(A)**\nthe independent verification and validation services or equivalent services, including systems engineering and technical advisory (SETA) support of major acquisition programs; or\n**(B)**\nthe independent verification and validation or systems engineering and technical advisory (SETA) support of the development or acquisition of major acquisition programs or defense systems, in accordance with guidance of the Department of Defense relating to such acquisition programs or such business systems.\n**(2) Past performance**\nFor any contract used to demonstrate eligibility under paragraph (1), an entity must have performed the work at a satisfactory or better level as indicated by the past performance information in the Contractor Performance Assessment Reporting System, or successor system.\n**(3) Demonstration of lack of conflict of interest**\nThe Secretary shall revoke the eligibility of an entity under this subsection if an entity does not demonstrate clear and unmitigable evidence that the entity does not have a conflict of interest with respect to the effective performance of functions under subsection (c).\n**(4) No mitigation plans acceptable**\nThe Secretary may not accept from an entity a plan to mitigate a conflict of interest in order to ameliorate any limitation or prohibition under this subsection.\n##### (c) Functions\nThe functions specified in this subsection are the following:\n**(1)**\nThe independent verification and validation of each major acquisition program project\u2014\n**(A)**\nwhen such major acquisition program is initiated, with respect to its design and the development of its requirements and acquisition;\n**(B)**\nat the conclusion of such program; and\n**(C)**\nat any other intervals during such program selected by the Chief Acquisition Officer of the Department.\n**(2)**\nThe independent verification and validation of other programs or projects of the Department selected by the Chief Acquisition Officer of the Department, at intervals selected by the Chief Acquisition Officer.\n##### (d) Funding\nThe Chief Financial Officer of the Department shall ensure that each organizational subdivision of the Department that enters into a contract under subsection (a) proportionally contributes amounts to fund each such contract.\n##### (e) Definitions\nIn this section:\n**(1) Covered contract**\nThe term covered contract means any prime or subcontract with the Department, including\u2014\n**(A)**\ninformation technology support or software or system design, development, sustainment, or maintenance services;\n**(B)**\nprofessional or management consulting services; or\n**(C)**\nadvisory and assistance services.\n**(2) Independent verification and validation**\nThe term independent verification and validation means a comprehensive inspection, a review, analysis, and testing, or an assessment of systems, software, or hardware, as applicable, performed by an entity awarded a contract under subsection (a)\u2014\n**(A)**\nto verify that the requirements of a program, project or system, or a development phase of such a program or project, are correctly defined; and\n**(B)**\nto validate cost, schedule, and performance baselines of current programs and measure program effectiveness.\n#### 6. Department of Veterans Affairs cost assessment and program evaluation\n##### (a) In general\nSubchapter VI of chapter 81 of title 38, United States Code, as added by section 2 and amended by section 3, is further amended by adding at the end the following new section:\n8184. Cost assessment and program evaluation (a) Director of Cost Assessment and Program Evaluation There is in the Department a Director of Cost Assessment and Program Evaluation, who shall report directly to the Secretary. (b) Responsibilities The responsibilities of the Director are as follows: (1) To develop policies and procedures for cost estimation and analysis of major acquisition programs of the Department. (2) To conduct independent cost estimates and analyses for major acquisition programs to support acquisition decisions, or any other acquisitions as directed by the Secretary. (3) To provide an independent cost estimate to the Assistant Secretary for Acquisition in advance of a decision to proceed with full-scale acquisition for a major acquisition program or any other program as directed by the Director. (4) To evaluate the effectiveness of major acquisition programs in meeting Department objectives. (5) Not less frequently than once each year, to submit to the Secretary and the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives an annual report on cost estimation and program evaluation activities, including recommendations to improve acquisition efficiency. Such report shall include a list of all acquisitions where the independent cost estimate for a major acquisition program exceeded the budget request for the program by more than 5 percent. (c) Support and resources The Chief Financial Officer of the Department shall provide to the Secretary such support and resources as may be necessary for the Secretary to ensure the effective establishment and functioning of the Director of Cost Assessment and Program Evaluation. .\n##### (b) Report on monitoring of operating and support costs for major acquisition programs\n**(1) Report to Secretary of Veterans Affairs**\nNot later than one year after the date of the enactment of this Act, and not less frequently than once each year thereafter until December 31, 2028, the Director of Cost Assessment and Program Evaluation of the Department of Veterans Affairs shall submit to the Secretary of Veterans Affairs a report on systems and methods for tracking and assessing operating and support costs of major acquisition programs (as defined in section 8181 of title 38, United States Code, as added by section 2), including recommendations for establishing cost baselines.\n**(2) Transmittal to Congress**\nNot later than 30 days after receiving a report pursuant to paragraph (1), the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives the report received by the Secretary.\n#### 7. Improvements to hiring of entry-level acquisition positions in the Department of Veterans Affairs\n##### (a) Priority use of internship programs for hiring into entry-Level positions in acquisitions\nThe Secretary of Veterans Affairs shall prioritize the use of acquisition internship programs to hire employees to entry-level positions relating to acquisition in the Department of Veterans Affairs.\n##### (b) Annual number of participants in acquisition internship programs\n**(1) In general**\nNot later than September 30 of the first fiscal year beginning after the date of the enactment of this Act, the Secretary shall take such actions as may be necessary to ensure that the annual number of participants in acquisition internship programs of the Department is\u2014\n**(A)**\nnot fewer than twice the number of participants in such programs during fiscal year 2025; and\n**(B)**\nnot more than 4 times the number of participants in such programs during such fiscal year.\n**(2) Termination**\nThe requirements of paragraph (1) shall terminate on the date on which the Secretary certifies to the appropriate committees of Congress that the projected number of graduates of acquisition internship programs is sufficient to satisfy the human capital needs of the Department with respect to acquisition, taking into account the rate of attrition and projected retirements of personnel.\n**(3) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives.\n#### 8. Independent analysis of acquisition process of Department of Veterans Affairs\n##### (a) Systems engineering analysis\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans' Affairs shall enter into a memorandum of understanding with the Executive Director of the Acquisition Research Center of the Department of Defense to conduct a systems engineering analysis of the acquisition process of the Department of Veterans Affairs.\n##### (b) Report\nNot later than one year after the date in which the Secretary enters into the memorandum of understanding required by subsection (a), the Secretary shall submit to Committee on Veterans' Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives a report on the findings of the Executive Director with respect to the analysis conducted under such subsection.\n#### 9. Requirements development process\n##### (a) In general\nSubchapter VI of chapter 81 of title 38, United States Code, as added by section 2 and amended by sections 3 and 6, is further amended by adding at the end the following new section:\n8185. Requirements development process (a) Establishment of process (1) The Secretary shall establish a standardized requirements development process for major acquisition programs. (2) The process established pursuant to paragraph (1) shall\u2014 (A) define and validate mission-driven requirements for major acquisition programs exceeding $200,000,000 annually or $1,000,000,000 in lifecycle costs, in coordination with the Assistant Secretary for Acquisition; (B) incorporate data-driven needs assessments, stakeholder input from relevant administrations, staff offices, and other elements of the Department and veterans service organizations, and alignment with statutory mandates, such as section 8121 of this title; and (C) ensure iterative validation of requirements through independent verification and validation, as described in section 8185 of this title, to confirm cost, schedule, and performance baselines. (b) Limitation on personnel The Secretary shall implement the process established pursuant to subsection (a) using staff within the Office of Acquisition and other relevant offices of the Department, as established under section 8182 of this title, without creating new positions, unless a subsequent cost-benefit analysis, validated by the Director of Cost Assessment and Program Evaluation, justifies additional resources. .\n##### (b) Report\nNot later than 180 days after the enactment of this Act, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives a report detailing the requirements process established pursuant to section 8187 of such title, as added by subsection (a) and a plan for implementation of such process, including timelines for integration with major acquisition program baselines.\n#### 10. Conforming amendments\nSubchapter VI of chapter 81 of title 38, United States Code, is amended\u2014\n**(1)**\nin section 8171, by striking paragraphs (5) and (6); and\n**(2)**\nby striking section 8172.\n#### 11. Clerical amendments\nThe table of sections at the beginning of chapter 81 of title 38, United States Code, is amended\u2014\n**(1)**\nby striking the item relating to section 8172; and\n**(2)**\nby adding at the end the following:\nSUBCHAPTER VII\u2014Acquisition review, cost assessment, and program evaluation 8181. Definition of major acquisition program. 8182. Acquisition reorganization. 8183. Major acquisition program managers. 8184. Cost assessment and program evaluation. 8185. Requirements development process. .",
      "versionDate": "2025-12-18",
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
        "actionDate": "2025-12-15",
        "actionTime": "16:19:13",
        "text": "Held at the desk."
      },
      "number": "1591",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ARCA Act of 2025",
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
        "updateDate": "2026-04-27T22:36:30Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6833ih.xml"
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
      "title": "To amend title 38, United States Code, to reorganize the acquisition structure of the Department of Veterans Affairs and to establish the Director of Cost Assessment and Program Evaluation in the Department, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T08:01:10Z"
    },
    {
      "title": "ARCA Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ARCA Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Acquisition Reform and Cost Assessment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T07:53:23Z"
    }
  ]
}
```
