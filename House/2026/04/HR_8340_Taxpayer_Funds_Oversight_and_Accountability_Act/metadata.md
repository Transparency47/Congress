# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8340?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8340
- Title: Taxpayer Funds Oversight and Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 8340
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-05-01T08:09:16Z
- Update date including text: 2026-05-01T08:09:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8340",
    "number": "8340",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Taxpayer Funds Oversight and Accountability Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:09:16Z",
    "updateDateIncludingText": "2026-05-01T08:09:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
            "date": "2026-04-29T13:07:25Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-16T14:02:20Z",
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
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "DC"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8340ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8340\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Min (for himself and Mr. Timmons ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo modify the governmentwide financial management plan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taxpayer Funds Oversight and Accountability Act .\n#### 2. Chief financial officers; governmentwide financial management plan\n##### (a) Chief financial officer and deputy chief financial officer\nChapter 9 of title 31, United States Code, is amended\u2014\n**(1)**\nin section 902(a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking An and inserting It shall be the duty and responsibility of each agency Chief Financial Officer to oversee and, unless otherwise specified in law, provide leadership in the areas of budget formulation and execution, planning and performance, risk management, internal controls, financial systems, accounting, and other areas as designated by the Deputy Director of Management under the authorities described in section 503. In carrying out the preceding sentence, each ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (C), by inserting areas and before systems ; and\n**(ii)**\nin subparagraph (D)\u2014\n**(I)**\nin clause (iii), by striking and at the end;\n**(II)**\nin clause (iv), by striking performance; and inserting performance and integration of performance and cost information; and ; and\n**(III)**\nby adding at the end the following:\n(v) annual agency financial statements prepared in accordance with applicable accounting standards as determined by the Director of the Office of Management and Budget consistent with section 3512; ;\n**(C)**\nby redesignating paragraphs (5), (6), (7), and (8) as paragraphs (7), (8), (9), and (11) respectively;\n**(D)**\nby inserting after paragraph (4) the following:\n(5) oversee and provide leadership over the design, implementation, and operation of the internal controls of the agency over financial reporting and key financial management information identified under section 3512(e)(1); (6) prepare, in consultation with financial management and other appropriate experts, an agency plan to implement the 4-year financial management plan prepared by the Director of the Office of Management and Budget under section 3512(a)(2) of this title and to achieve and sustain effective financial management in the agency, which shall\u2014 (A) be completed within 120 days after the issuance of a governmentwide plan under such section 3512(a)(2); (B) be revised as determined necessary by the Chief Financial Officer and the Director of the Office of Management and Budget; (C) include financial management metrics against which the financial management performance of the agency shall be assessed; and (D) be submitted upon completion or revision to the head of the agency, the Director of the Office of Management and Budget, the Comptroller General, and appropriate committees of Congress, and be made publicly available; ;\n**(E)**\nin paragraph (7), as so redesignated\u2014\n**(i)**\nby striking subparagraph (A);\n**(ii)**\nby redesignating subparagraphs (B) through (E) as subparagraphs (A) through (D), respectively; and\n**(iii)**\nin subparagraph (C), as so redesignated, by adding and at the end;\n**(F)**\nin paragraph (8), as so redesignated\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking and the Director of the Office of Management and Budget, and inserting , the Director of the Office of Management and Budget, the Comptroller General, and appropriate committees of Congress, which shall be made publicly available and ;\n**(ii)**\nin subparagraph (A), by striking agency; and inserting\nagency, including\u2014 (i) the progress of the agency in implementing the agency plan described in paragraph (5); (ii) the progress of the agency in implementing the governmentwide 4-year financial management plan prepared by the Director of the Office of Management and Budget under section 3512(a)(2) of this title; and (iii) the performance of the agency against financial management metrics established by the Director of the Office of Management and Budget; ; and\n**(iii)**\nin subparagraph (D)\u2014\n**(I)**\nby striking of the reports and inserting\nof\u2014 (i) the reports ;\n**(II)**\nin clause (i), as so designated, by striking the amendments made by the Federal Managers\u2019 Financial Integrity Act of 1982 (Public law 97\u2013255); and and inserting section 3512(d) of this title; ; and\n**(III)**\nby adding at the end the following:\n(ii) the reporting of the agency under the Federal Financial Management Improvement Act of 1996 ( 31 U.S.C. 3512 note); and ;\n**(G)**\nin paragraph (9), as so redesignated\u2014\n**(i)**\nby striking monitor the and insert manage the formulation and ; and\n**(ii)**\nby striking , and prepare and submit to the head of the agency timely performance reports; and and inserting a semicolon;\n**(H)**\nby inserting after paragraph (9), as so redesignated, the following:\n(10) coordinate with the responsible agency official to ensure performance and cost information are linked, including in the preparation and submission to the head of the agency of timely performance reports that incorporate cost information; ;\n**(I)**\nin paragraph (11), as so redesignated\u2014\n**(i)**\nby inserting inflation and before costs ; and\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(J)**\nby adding at the end the following:\n(12) coordinate with senior agency personnel, including those with statutory, regulatory, and related policy responsibility, which may include the Chief Data Officer, Chief Information Officer, Chief Performance Officer, Chief Acquisition Officer, Chief Risk Officer, and Chief Evaluation Officer of the agency on\u2014 (A) the exercise of authorities under this subsection; and (B) the strategic planning, performance measurement and reporting, and risk management functions of the agency. ; and\n**(2)**\nin section 903\u2014\n**(A)**\nin subsection (a), by inserting and who shall assist the agency Chief Financial Officer in the performance of each of the duties of the agency Chief Financial Officer under this chapter after matters ; and\n**(B)**\nby adding at the end the following:\n(c) Notwithstanding subchapter III of chapter 33 of title 5, in the event of a vacancy in the position of Chief Financial Officer of an agency, the Deputy Chief Financial Officer of the agency shall serve as the acting Chief Financial Officer. .\n##### (b) Governmentwide financial management plan\nSection 3512 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking a financial management status report and a governmentwide 5-year financial management plan and inserting a governmentwide 4-year financial management plan, to be included within the President\u2019s Management Agenda, and a financial management status report ;\n**(B)**\nby striking paragraph (2);\n**(C)**\nby redesignating paragraph (3) as paragraph (2);\n**(D)**\nin paragraph (2), as so redesignated\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking 5-year and inserting 4-year ;\n**(II)**\nby striking shall describe and inserting the following:\nshall\u2014 (i) describe ;\n**(III)**\nin clause (i), as so designated, by striking 5 fiscal years to improve the financial management of the Federal Government. and inserting 4 fiscal years to improve the financial management of the Federal Government in a manner that is strategic, comprehensive, and cost-effective; and ; and\n**(IV)**\nby adding at the end the following:\n(ii) be developed in consultation with the Chief Financial Officers Council and, as appropriate, other councils and financial management experts as determined by the Director of the Office of Management and Budget. in consultation with the Chief Financial Officers Council. ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin the matter preceding clause (i), by striking 5-year and inserting 4-year ;\n**(II)**\nin clause (iii)\u2014\n**(aa)**\nby striking for developing and inserting\nfor improving financial management systems, including\u2014 (I) developing ; and\n**(bb)**\nby adding at the end the following:\n(II) describing how performance and cost information are linked in order to facilitate effective and efficient decision making; (III) eliminating duplicative and unnecessary systems and activities; and (IV) identifying opportunities for agencies to share systems and services and encouraging agencies to do so where practicable; ;\n**(III)**\nby striking clause (iv);\n**(IV)**\nby redesignating clause (v) as clause (iv);\n**(V)**\nby inserting after clause (iv), as so redesignated, the following:\n(v) provide a strategy for reporting performance and cost information; ;\n**(VI)**\nin clause (vi), by striking 5-year and inserting 4-year ;\n**(VII)**\nin clause (vii), by striking identify and inserting provide a strategy for strengthening the Federal financial management workforce, including identification of ;\n**(VIII)**\nin clause (viii), by striking and at the end;\n**(IX)**\nby redesignating clause (ix) as clause (x);\n**(X)**\nby inserting after clause (viii) the following:\n(ix) include financial management metrics against which the performance of executive agencies can be assessed; and ; and\n**(XI)**\nin clause (x), as so redesignated, by striking 5-year and inserting 4-year ;\n**(E)**\nby inserting after paragraph (2) the following:\n(3) A financial management status report under this subsection shall include\u2014 (A) a description and analysis of the status of financial management in the executive branch, including the progress made towards implementing the governmentwide 4-year financial management plan, and the status of remaining challenges to implementing the governmentwide 4-year financial management plan; (B) a summary of the performance of agencies against the metrics developed and identified by the Director of the Office of Management and Budget in the governmentwide 4-year financial management plan; (C) a summary of the most recently completed financial statements\u2014 (i) of Federal agencies under section 3515 of this title; and (ii) of Government corporations; (D) a summary of the most recently completed financial statement audits and reports\u2014 (i) of Federal agencies under subsections (e) and (f) of section 3521 of this title; and (ii) of Government corporations; (E) a summary of reports on internal accounting and administrative control systems submitted to the President and Congress under subsection (d); (F) a listing of agencies whose financial management systems do not comply substantially with the requirements of section 803(a) of the Federal Financial Management Improvement Act of 1996 ( 31 U.S.C. 3512 note), and a summary statement of the efforts underway to remedy the noncompliance; and (G) any other information the Director considers appropriate to fully inform Congress regarding the financial management of the Federal Government. ;\n**(F)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking 15 months after the date of the enactment of this subsection and inserting 12 months after the date of the enactment of the Taxpayer Funds Oversight and Accountability Act ; and\n**(II)**\nby striking 5-year and inserting 4-year ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nby striking Not later than January 31 of each year thereafter and inserting At a minimum, concurrently with the submission of the budget of the United States Government under section 1105(a) of this title made in the first full fiscal year following any year in which the term of the President commences under section 101 of title 3 ;\n**(bb)**\nby striking financial management status report and a revised governmentwide 5-year and inserting governmentwide 4-year ; and\n**(cc)**\nby striking 5 fiscal years and all that follows through the period at the end and inserting 4 fiscal years. ; and\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nby striking revised governmentwide 5-year and inserting governmentwide 4-year ; and\n**(bb)**\nby striking paragraph (3)(B)(viii) and inserting paragraph (2)(B)(viii) ; and\n**(iii)**\nby adding at the end the following:\n(C) Each year, concurrently with the submission of the budget of the United States Government under section 1105(a) of this title, the Director of the Office of Management and Budget shall submit to the appropriate committees of Congress and the Comptroller General a financial management status report. ; and\n**(G)**\nby striking paragraph (5);\n**(2)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(C) a separate report on the results of the assessment and conclusion required under subsection (e)(2). ;\n**(3)**\nby redesignating subsections (e), (f), and (g) as subsections (f), (g), and (h), respectively; and\n**(4)**\nby inserting after subsection (d) the following:\n(e) The head of each executive agency shall\u2014 (1) in establishing the internal accounting and administrative controls under subsection (c), identify the key financial management information needed for effective financial management and decision making, which shall include a consideration of\u2014 (A) the agency spending data required to be published under the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note); and (B) the information used by the agency to report on improper payments under section 3352 of this title; and (2) annually assess and make a conclusion on the effectiveness of the internal controls of the executive agency over financial reporting and key financial management information identified under paragraph (1), consistent with guidance provided by the Director of the Office of Management and Budget. .\n##### (c) Technical and conforming amendment\nSection 3348(e) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (3), by adding or at the end;\n**(2)**\nby striking paragraph (4); and\n**(3)**\nby redesignating paragraph (5) as paragraph (4).",
      "versionDate": "2026-04-16",
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
        "actionDate": "2025-09-15",
        "actionTime": "19:04:33",
        "text": "ASSUMING FIRST SPONSORSHIP - Mr. Min asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1558, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection."
      },
      "number": "1558",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Taxpayer Funds Oversight and Accountability Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-28T16:15:20Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8340ih.xml"
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
      "title": "Taxpayer Funds Oversight and Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Taxpayer Funds Oversight and Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T03:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify the governmentwide financial management plan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T03:33:24Z"
    }
  ]
}
```
