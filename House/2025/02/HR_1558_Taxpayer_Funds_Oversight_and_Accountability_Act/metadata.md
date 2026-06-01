# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1558?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1558
- Title: Taxpayer Funds Oversight and Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 1558
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-04-30T12:28:55Z
- Update date including text: 2026-04-30T12:28:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-15 19:04:33 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Min asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1558, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-15 19:04:33 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Min asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1558, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1558",
    "number": "1558",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001078",
        "district": "11",
        "firstName": "Gerald",
        "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
        "lastName": "Connolly",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Taxpayer Funds Oversight and Accountability Act",
    "type": "HR",
    "updateDate": "2026-04-30T12:28:55Z",
    "updateDateIncludingText": "2026-04-30T12:28:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2025-09-15",
      "actionTime": "19:04:33",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Mr. Min asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1558, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:02:35Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MD"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "OH"
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
      "sponsorshipDate": "2025-02-25",
      "state": "NM"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "FL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "TX"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "VA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "AZ"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MO"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1558ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1558\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Connolly (for himself, Ms. Norton , Mr. Lynch , Mr. Krishnamoorthi , Mr. Khanna , Mr. Mfume , Ms. Brown , Ms. Stansbury , Mr. Garcia of California , Mr. Frost , Ms. Lee of Pennsylvania , Ms. Crockett , Ms. Randall , Mr. Subramanyam , Ms. Ansari , Mr. Bell , Ms. Simon , Mr. Min , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo modify the governmentwide financial management plan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taxpayer Funds Oversight and Accountability Act .\n#### 2. Chief financial officers; governmentwide financial management plan\n##### (a) Chief Financial Officer and Deputy Chief Financial Officer\nChapter 9 of title 31, United States Code, is amended\u2014\n**(1)**\nin section 902(a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking An and inserting It shall be the duty and responsibility of each agency Chief Financial Officer to oversee and provide leadership in the areas of budget formulation and execution, planning and performance, risk management, internal controls, financial systems, accounting, and other areas as the Director of the Office of Management and Budget may designate. In carrying out the preceding sentence, each ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (C), by inserting areas and before systems ; and\n**(ii)**\nin subparagraph (D)\u2014\n**(I)**\nin clause (iii), by striking and at the end;\n**(II)**\nin clause (iv), by striking performance; and inserting performance and integration of performance and cost information; and ; and\n**(III)**\nby adding at the end the following:\n(v) annual agency financial statements prepared in accordance with United States generally accepted accounting principles; ;\n**(C)**\nby redesignating paragraphs (5), (6), (7), and (8) as paragraphs (7), (8), (9), and (11) respectively;\n**(D)**\nby inserting after paragraph (4) the following:\n(5) oversee and provide leadership over the design, implementation, and operation of the internal controls of the agency over financial reporting and key financial management information identified under section 3512(e)(1); (6) prepare, in consultation with financial management and other appropriate experts, an agency plan to implement the 4-year financial management plan prepared by the Director of the Office of Management and Budget under section 3512(a)(2) of this title and to achieve and sustain effective financial management in the agency, which shall\u2014 (A) be completed within 90 days after the issuance of a governmentwide plan under such section 3512(a)(2); (B) be revised as determined necessary by the Chief Financial Officer; (C) include performance-based financial management metrics against which the financial management performance of the agency shall be assessed; and (D) be submitted upon completion or revision to the head of the agency, the Director of the Office of Management and Budget, the Comptroller General, and appropriate committees of Congress, and be made publicly available; ;\n**(E)**\nin paragraph (7), as so redesignated\u2014\n**(i)**\nby striking subparagraph (A);\n**(ii)**\nby redesignating subparagraphs (B) through (E) as subparagraphs (A) through (D), respectively; and\n**(iii)**\nin subparagraph (C), as so redesignated, by adding and at the end;\n**(F)**\nin paragraph (8), as so redesignated\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking and the Director of the Office of Management and Budget, and inserting , the Director of the Office of Management and Budget, the Comptroller General, and appropriate committees of Congress, which shall be made publicly available and ;\n**(ii)**\nin subparagraph (A), by striking agency; and inserting\nagency, including\u2014 (i) the progress of the agency in implementing the agency plan described in paragraph (5); (ii) the progress of the agency in implementing the governmentwide 4-year financial management plan prepared by the Director of the Office of Management and Budget under section 3512(a)(2) of this title; and (iii) the performance of the agency against financial management metrics established by the Director of the Office of Management and Budget; ; and\n**(iii)**\nin subparagraph (D)\u2014\n**(I)**\nby striking of the reports and inserting\nof\u2014 (i) the reports ;\n**(II)**\nin clause (i), as so designated, by striking the amendments made by the Federal Managers\u2019 Financial Integrity Act of 1982 (Public law 97\u2013255); and and inserting section 3512(d) of this title; ; and\n**(III)**\nby adding at the end the following:\n(ii) agency spending data published under the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note); and (iii) the reporting of the agency under the Federal Financial Management Improvement Act of 1996 ( 31 U.S.C. 3512 note); and ;\n**(G)**\nin paragraph (9), as so redesignated\u2014\n**(i)**\nby striking monitor the and insert manage the formulation and ; and\n**(ii)**\nby striking , and prepare and submit to the head of the agency timely performance reports; and and inserting a semicolon;\n**(H)**\nby inserting after paragraph (9), as so redesignated, the following:\n(10) be responsible for linking performance and cost information, including the preparation and submission to the head of the agency of timely performance reports that incorporate cost information; ;\n**(I)**\nin paragraph (11), as so redesignated\u2014\n**(i)**\nby inserting inflation and before costs ; and\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(J)**\nby adding at the end the following:\n(12) coordinate with senior agency personnel, including the Chief Data Officer, Chief Information Officer, Chief Performance Officer, Chief Acquisition Officer, Chief Risk Officer, and Chief Evaluation Officer of the agency on\u2014 (A) the exercise of authorities under this subsection; and (B) the strategic planning, performance measurement and reporting, and risk management functions of the agency. ; and\n**(2)**\nin section 903\u2014\n**(A)**\nin subsection (a), by inserting and who shall assist the agency Chief Financial Officer in the performance of each of the duties of the agency Chief Financial Officer under this chapter after matters ; and\n**(B)**\nby adding at the end the following:\n(c) Notwithstanding subchapter III of chapter 33 of title 5, in the event of a vacancy in the position of Chief Financial Officer of an agency, the Deputy Chief Financial Officer of the agency shall serve as the acting Chief Financial Officer. .\n##### (b) Governmentwide financial management plan\nSection 3512 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking a financial management status report and a governmentwide 5-year financial management plan and inserting a governmentwide 4-year financial management plan and a financial management status report ;\n**(B)**\nby striking paragraph (2);\n**(C)**\nby redesignating paragraph (3) as paragraph (2);\n**(D)**\nin paragraph (2), as so redesignated\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking 5-year and inserting 4-year ;\n**(II)**\nby striking shall describe and inserting the following:\nshall\u2014 (i) describe ;\n**(III)**\nin clause (i), as so designated, by striking 5 fiscal years to improve the financial management of the Federal Government. and inserting 4 fiscal years to improve the financial management of the Federal Government in a manner that is strategic, comprehensive, and cost-effective; and ; and\n**(IV)**\nby adding at the end the following:\n(ii) be developed in consultation with the Chief Financial Officers Council, the Chief Information Officers Council, the Chief Data Officer Council, the Chief Acquisition Officers Council, the Council of the Inspectors General on Integrity and Efficiency, the Government Accountability Office, and, as appropriate, other councils and financial management experts. ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin the matter preceding clause (i), by striking 5-year and inserting 4-year ;\n**(II)**\nin clause (iii)\u2014\n**(aa)**\nby striking for developing and inserting\nfor improving financial management systems, including\u2014 (I) developing ; and\n**(bb)**\nby adding at the end the following:\n(II) linking performance and cost information to facilitate effective and efficient decision making; (III) eliminating duplicative and unnecessary systems and activities; and (IV) identifying opportunities for agencies to share systems and services and encouraging agencies to do so where practicable; ;\n**(III)**\nby striking clause (iv);\n**(IV)**\nby redesignating clause (v) as clause (iv);\n**(V)**\nby inserting after clause (iv), as so redesignated, the following:\n(v) provide a strategy for reporting performance and cost information; ;\n**(VI)**\nin clause (vi), by striking 5-year and inserting 4-year ;\n**(VII)**\nin clause (vii), by striking identify and inserting provide a strategy for strengthening the Federal financial management workforce, including identification of ;\n**(VIII)**\nin clause (viii), by striking and at the end;\n**(IX)**\nby redesignating clause (ix) as clause (x);\n**(X)**\nby inserting after clause (viii) the following:\n(ix) include comprehensive financial management performance-based metrics against which the financial management performance of executive agencies can be assessed; and ; and\n**(XI)**\nin clause (x), as so redesignated, by striking 5-year and inserting 4-year ;\n**(E)**\nby inserting after paragraph (2) the following:\n(3) A financial management status report under this subsection shall include\u2014 (A) a description and analysis of the status of financial management in the executive branch, including the progress made towards implementing the governmentwide 4-year financial management plan, the status of remaining challenges, and, as necessary based on obligations or expenditures, any update or revision to the cost estimates included in the most recent governmentwide 4-year financial management plan; (B) a summary of the performance of agencies against the metrics developed and identified by the Director of the Office of Management and Budget in the governmentwide 4-year financial management plan; (C) a summary of the most recently completed financial statements\u2014 (i) of Federal agencies under section 3515 of this title; and (ii) of Government corporations; (D) a summary of the most recently completed financial statement audits and reports\u2014 (i) of Federal agencies under subsections (e) and (f) of section 3521 of this title; and (ii) of Government corporations; (E) a summary of reports on internal accounting and administrative control systems submitted to the President and Congress under subsection (d); (F) a listing of agencies whose financial management systems do not comply substantially with the requirements of section 803(a) of the Federal Financial Management Improvement Act of 1996 ( 31 U.S.C. 3512 note), and a summary statement of the efforts underway to remedy the noncompliance; and (G) any other information the Director considers appropriate to fully inform Congress regarding the financial management of the Federal Government. ;\n**(F)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking 15 months after the date of the enactment of this subsection and inserting 6 months after the date of the enactment of the Taxpayer Funds Oversight and Accountability Act ; and\n**(II)**\nby striking 5-year and inserting 4-year ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nby striking Not later than January 31 of each year thereafter and inserting At a minimum, concurrently with the submission of the budget of the United States Government under section 1105(a) of this title made in the first full fiscal year following any year in which the term of the President commences under section 101 of title 3 ;\n**(bb)**\nby striking financial management status report and a revised governmentwide 5-year and inserting governmentwide 4-year ; and\n**(cc)**\nby striking 5 fiscal years and all that follows through the period at the end and inserting 4 fiscal years. ; and\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nby striking revised governmentwide 5-year and inserting governmentwide 4-year ; and\n**(bb)**\nby striking paragraph (3)(B)(viii) and inserting paragraph (2)(B)(viii) ; and\n**(iii)**\nby adding at the end the following:\n(C) Each year, concurrently with the submission of the budget of the United States Government under section 1105(a) of this title, the Director of the Office of Management and Budget shall submit to the appropriate committees of Congress and the Comptroller General a financial management status report. ; and\n**(G)**\nby striking paragraph (5);\n**(2)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(C) a separate report on the results of the assessment and conclusion required under subsection (e)(2). ;\n**(3)**\nby redesignating subsections (e), (f), and (g) as subsections (f), (g), and (h), respectively; and\n**(4)**\nby inserting after subsection (d) the following:\n(e) The head of each executive agency shall\u2014 (1) in establishing the internal accounting and administrative controls under subsection (c), identify the key financial management information needed for effective financial management and decision making, which shall include\u2014 (A) the agency spending data required to be published under the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note); and (B) the information used by the agency to report on improper payments under section 3352 of this title; and (2) annually assess and make a conclusion on the effectiveness of the internal controls of the executive agency over financial reporting and key financial management information identified under paragraph (1). .\n##### (c) Audits by agencies\nSection 3521 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nby striking paragraphs (1) and (2);\n**(B)**\nby striking (e) Each financial and inserting (e)(1) Each financial ;\n**(C)**\nin paragraph (1), as so designated, by striking standards\u2014 and inserting standards. ; and\n**(D)**\nby inserting after paragraph (1), as so designated, the following:\n(2) As part of each audit under this subsection, the auditor shall\u2014 (A) evaluate the design of the internal control of the agency over financial management reporting and key financial information, as assessed and reported on by the head of the agency under section 3512(d)(2)(C) of this title; (B) determine whether those controls have been implemented; (C) for controls that are properly designed and implemented, perform sufficient tests of those controls to conclude whether the controls are operating effectively, including sufficient tests to support a low level of assessed control risk; and (D) communicate controls that the auditor concludes are not suitably designed and implemented or are not operating effectively, as appropriate under applicable generally accepted government auditing standards. (3) Audits under this subsection shall be conducted\u2014 (A) in the case of an agency having an Inspector General appointed under the Inspector General Act of 1978 (5 U.S.C. App.), by the Inspector General or by an independent external auditor, as determined by the Inspector General of the agency; and (B) in any other case, by an independent external auditor, as determined by the head of the agency. ; and\n**(2)**\nin subsection (h), by striking section 3512(a)(3)(B)(viii) and inserting section 3512(a)(2)(B)(viii) .\n##### (d) Technical and conforming amendment\nSection 3348(e) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (3), by adding or at the end;\n**(2)**\nby striking paragraph (4); and\n**(3)**\nby redesignating paragraph (5) as paragraph (4).",
      "versionDate": "2025-02-25",
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
        "actionDate": "2026-04-29",
        "text": "Committee Consideration and Mark-up Session Held"
      },
      "number": "8340",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Taxpayer Funds Oversight and Accountability Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-13",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "75",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improving Federal Financial Management Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2025-07-17T20:36:03Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-07-17T20:36:03Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T20:36:03Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-17T20:36:03Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-07-17T20:36:03Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-07-17T20:36:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-06T15:29:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
    "originChamber": "House",
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
          "measure-id": "id119hr1558",
          "measure-number": "1558",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-01-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1558v00",
            "update-date": "2026-01-27"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Taxpayer Funds Oversight and Accountability Act</strong><br/>\u00a0<br/>This bill requires the Office of Management and Budget (OMB) to take certain actions to improve financial management systems across the federal government and expands the responsibilities of federal agency Chief Financial Officers (CFOs).<br/>\u00a0<br/>The bill requires OMB to submit a four-year governmentwide financial management plan to Congress within six months of enactment and thereafter with the budget submitted in the first full fiscal year following the start of a presidential term. Such plans must address certain topics, including strategies for (1) improving financial management systems; (2) strengthening the financial management workforce; and (3) reporting performance and cost information. OMB must annually submit related status reports to Congress and the Government Accountability Office.\u00a0<br/>\u00a0<br/>Each agency CFO is assigned new responsibilities, including</p><ul><li>preparing the agency plan to implement OMB's governmentwide financial management plan;</li><li>overseeing and providing leadership in the areas of budget formulation and execution, planning and performance, risk management, internal controls, financial systems, accounting, and other areas designated by OMB;</li><li>coordinating with designated agency personnel on the strategic planning, performance measurement and reporting, and risk management functions of the agency;</li><li>managing the formulation and financial execution of the agency budget;</li><li>linking performance and cost information; and</li><li>preparing annual reports on progress in implementing the\u00a0governmentwide financial management plan and transmitting such reports to the agency head, OMB, and Congress.</li></ul><p>The bill establishes new requirements for audits of agency accounts, such as having auditors evaluate the design of the agency's internal controls over financial reporting.</p>"
        },
        "title": "Taxpayer Funds Oversight and Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1558.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Taxpayer Funds Oversight and Accountability Act</strong><br/>\u00a0<br/>This bill requires the Office of Management and Budget (OMB) to take certain actions to improve financial management systems across the federal government and expands the responsibilities of federal agency Chief Financial Officers (CFOs).<br/>\u00a0<br/>The bill requires OMB to submit a four-year governmentwide financial management plan to Congress within six months of enactment and thereafter with the budget submitted in the first full fiscal year following the start of a presidential term. Such plans must address certain topics, including strategies for (1) improving financial management systems; (2) strengthening the financial management workforce; and (3) reporting performance and cost information. OMB must annually submit related status reports to Congress and the Government Accountability Office.\u00a0<br/>\u00a0<br/>Each agency CFO is assigned new responsibilities, including</p><ul><li>preparing the agency plan to implement OMB's governmentwide financial management plan;</li><li>overseeing and providing leadership in the areas of budget formulation and execution, planning and performance, risk management, internal controls, financial systems, accounting, and other areas designated by OMB;</li><li>coordinating with designated agency personnel on the strategic planning, performance measurement and reporting, and risk management functions of the agency;</li><li>managing the formulation and financial execution of the agency budget;</li><li>linking performance and cost information; and</li><li>preparing annual reports on progress in implementing the\u00a0governmentwide financial management plan and transmitting such reports to the agency head, OMB, and Congress.</li></ul><p>The bill establishes new requirements for audits of agency accounts, such as having auditors evaluate the design of the agency's internal controls over financial reporting.</p>",
      "updateDate": "2026-01-27",
      "versionCode": "id119hr1558"
    },
    "title": "Taxpayer Funds Oversight and Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Taxpayer Funds Oversight and Accountability Act</strong><br/>\u00a0<br/>This bill requires the Office of Management and Budget (OMB) to take certain actions to improve financial management systems across the federal government and expands the responsibilities of federal agency Chief Financial Officers (CFOs).<br/>\u00a0<br/>The bill requires OMB to submit a four-year governmentwide financial management plan to Congress within six months of enactment and thereafter with the budget submitted in the first full fiscal year following the start of a presidential term. Such plans must address certain topics, including strategies for (1) improving financial management systems; (2) strengthening the financial management workforce; and (3) reporting performance and cost information. OMB must annually submit related status reports to Congress and the Government Accountability Office.\u00a0<br/>\u00a0<br/>Each agency CFO is assigned new responsibilities, including</p><ul><li>preparing the agency plan to implement OMB's governmentwide financial management plan;</li><li>overseeing and providing leadership in the areas of budget formulation and execution, planning and performance, risk management, internal controls, financial systems, accounting, and other areas designated by OMB;</li><li>coordinating with designated agency personnel on the strategic planning, performance measurement and reporting, and risk management functions of the agency;</li><li>managing the formulation and financial execution of the agency budget;</li><li>linking performance and cost information; and</li><li>preparing annual reports on progress in implementing the\u00a0governmentwide financial management plan and transmitting such reports to the agency head, OMB, and Congress.</li></ul><p>The bill establishes new requirements for audits of agency accounts, such as having auditors evaluate the design of the agency's internal controls over financial reporting.</p>",
      "updateDate": "2026-01-27",
      "versionCode": "id119hr1558"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1558ih.xml"
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
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Taxpayer Funds Oversight and Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify the governmentwide financial management plan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:31Z"
    }
  ]
}
```
