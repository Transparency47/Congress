# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2985?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2985
- Title: Modernizing Government Technology Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 2985
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2026-04-17T16:19:21Z
- Update date including text: 2026-04-17T16:19:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 42 - 0.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 42 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2985",
    "number": "2985",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Modernizing Government Technology Reform Act",
    "type": "HR",
    "updateDate": "2026-04-17T16:19:21Z",
    "updateDateIncludingText": "2026-04-17T16:19:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 42 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
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
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
            "date": "2026-02-04T14:56:22Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-24T15:00:05Z",
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
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "VA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2985ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2985\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Ms. Mace (for herself and Mr. Connolly ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend section 1078 of the National Defense Authorization Act for Fiscal Year 2018 to increase the effectiveness of the Technology Modernization Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernizing Government Technology Reform Act .\n#### 2. Realigning use of funds with original congressional intent\nSection 1078 of the National Defense Authorization Act for Fiscal Year 2018 ( Public Law 115\u201391 ; 40 U.S.C. 11301 note) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby amending paragraph (3) to read as follows:\n(3) Use of funds (A) In general The Administrator shall, in accordance with recommendations from the Board, use amounts in the Fund for the following: (i) To transfer such amounts, to remain available until expended, to the head of an agency for the acquisition, procurement, and operation of information technology, or the development of information technology when more efficient and cost effective, to\u2014 (I) modernize, retire, or replace legacy information technology systems used by the agency; (II) enhance cybersecurity and privacy at the agency; (III) improve long-term efficiency and effectiveness of agency information technology; or (IV) improve the ability of the agency to perform the mission of the agency and deliver services to the public. (ii) To provide services or work performed in support of\u2014 (I) the activities described in clause (i); and (II) the Board and the Director in carrying out the responsibilities described in subsection (c)(2). (iii) To fund only programs, projects, or activities, or to fund increases for any programs, projects, or activities that have not been denied or restricted by Congress. (iv) To transfer such amounts only for programs, projects, or activities that will be reimbursed to the Fund to the extent necessary to ensure total amounts in the Fund are no less than the amounts needed to keep the Fund operational until the Fund sunsets pursuant to subsection (g)(1). (B) Termination or suspension of funds The Administrator shall, in accordance with recommendations from the Board, suspend or terminate funding for any project with respect to which the head of an agency provided fraudulent or misleading statements about such project (including fraudulent statements about technical design, the business case, or program management with respect to the project) in the application or proposal for amounts from the Fund for such project. ;\n**(B)**\nin paragraph (5)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nby striking or (B) ; and\n**(bb)**\nby striking (3)(C) and inserting (3)(A)(ii) ; and\n**(II)**\nin clause (ii), by striking , consistent with any applicable reprogramming law or guidelines of the Committees on Appropriations of the Senate and the House of Representatives ; and\n**(ii)**\nin subparagraph (B)(i)\u2014\n**(I)**\nby striking paragraph (3)(C) and inserting paragraph (3)(A)(ii) ; and\n**(II)**\nby striking the solvency of the Fund, including operating expenses and inserting the following: total amounts in the Fund are no less than the amounts needed to keep the Fund operational until the Fund sunsets pursuant to subsection (g)(1) ;\n**(C)**\nin paragraph (6)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin the matter before clause (i), by striking subparagraphs (A) and (B) of paragraph (3) and inserting the following: paragraph (3)(A)(i) and before any services or work are provided under paragraph (3)(A)(ii)(I) ;\n**(II)**\nin clause (i)\u2014\n**(aa)**\nby striking unless approved by the Director ; and\n**(bb)**\nby striking ; and and inserting a semicolon;\n**(III)**\nby redesignating clause (ii) as clause (iv); and\n**(IV)**\nby inserting after clause (i) the following new clauses:\n(ii) which shall include terms of repayment that require the head of the agency to reimburse the Fund for funds transferred under paragraph (3)(A)(i) at a level that ensures total amounts in the Fund are no less than the amounts needed to keep the Fund operational until the Fund sunsets pursuant to subsection (g)(1); (iii) which shall include terms of repayment that require the head of the agency to fully reimburse the Fund for any services or work provided under paragraph (3)(A)(ii) in direct support of the project; and ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby striking clause (i) and inserting the following:\n(i) for any funds transferred to an agency under paragraph (3)(A)(i), in the absence of compelling circumstances documented by the Administrator at the time of transfer, that such funds shall be transferred only\u2014 (I) on an incremental basis, tied to metric-based development milestones achieved by the agency through the use of rapid, iterative, development processes; and (II) after the head of the agency has provided the Director any information the Director is required to report pursuant to paragraph (7)(A)(i); and ; and\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nby striking subparagraphs (A) and (B) of paragraph (3) and inserting paragraph (3)(A)(i) ; and\n**(bb)**\nby striking paragraph (6) and inserting this paragraph ;\n**(D)**\nin paragraph (7)\u2014\n**(i)**\nin subparagraph (A)(i)\u2014\n**(I)**\nby inserting the written agreement entered into under paragraph (6), after description of the project, ; and\n**(II)**\nby inserting (including documented market research into commercial products and services) after used ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nby striking establishing ; and\n**(bb)**\nby striking the cost savings associated with the projects funded both annually and over the life of the acquired products and services by the Fund; and inserting the following: the amount repaid to the Fund in accordance with the terms established in the written agreements described in paragraph (6); ;\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nby striking reliability of the cost savings and inserting total cost savings ; and\n**(bb)**\nby striking the semicolon and inserting ; and ; and\n**(III)**\nin clause (iii), by striking ; and and inserting a period; and\n**(IV)**\nby striking clause (iv);\n**(2)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (ii), by striking the greatest Governmentwide impact; and and inserting the following: the greatest impact on modernizing, retiring, or replacing Federal legacy information technology systems; and ;\n**(ii)**\nby redesignating clauses (i) through (iii) as clauses (ii) through (iv), respectively; and\n**(iii)**\nby inserting before clause (ii), as so redesignated, the following new clause:\n(i) the ability for the head of the agency to ensure repayment of funds transferred from the Fund to the head of the agency, in accordance with subsection (b); ;\n**(B)**\nin subparagraph (D), by striking to improve or replace multiple information technology systems and inserting the following: to modernize, retire, or replace legacy information technology systems under subsection (b)(3)(A)(i) ; and\n**(C)**\nin subparagraph (F), by inserting after subsection (b)(6) the following: or the identification of fraudulent or misleading statements about the project (including fraudulent statements about technical design, the business case, or program management with respect to the project) in the application or proposal for amounts from the Fund for the project ; and\n**(D)**\nin subparagraph (G), by inserting after operating costs of the Fund the following: to ensure total amounts in the Fund are no less than the amounts needed to keep the Fund operational until the Fund sunsets pursuant to subsection (g)(1) ;\n**(3)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (A), by striking subsection (b)(3)(A) and for products, services, and acquisition vehicles funded under subsection (b)(3)(B) and inserting subsection (b)(3) ;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting a semicolon; and\n**(C)**\nin subparagraph (C), by inserting after and reduce waste the following: and ensure total amounts in the Fund are no less than the amounts needed to keep the Fund operational until the Fund sunsets pursuant to subsection (g)(1) ;\n**(4)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively;\n**(5)**\nby inserting after subsection (d) the following new subsection:\n(e) Responsibilities of the Federal Chief Information Officer; agency Chief Information Officers (1) Agency inventory An agency Chief Information Officer, in coordination with stakeholders and other agency officials, shall provide to the Federal Chief Information Officer\u2014 (A) on or before the first September 30 that occurs after the date of the enactment of the Modernizing Government Technology Reform Act, a list of high-risk legacy information technology systems used, operated, or maintained by the agency, in accordance with the guidance issued under paragraph (4); and (B) on or before September 30 of each year after the first year in which the list is provided under subparagraph (A), any updates to such list. (2) Legacy Federal IT Inventory The Federal Chief Information Officer shall\u2014 (A) on or before the first December 30 that occurs after the date of the enactment of the Modernizing Government Technology Reform Act, compile a Legacy Federal IT Inventory on the basis of the each list provided by an agency Chief Information Officers under paragraph (1)(A) that includes information about each high-risk legacy information technology system used, operated, or maintained by an agency; and (B) on or before December 30 each year after the year in which the Legacy Federal IT Inventory is compiled, update such Inventory on the basis of each update to the list provided by an agency Chief Information Officer under paragraph (1)(B). (3) Prioritization List (A) Requirement The Federal Chief Information Officer shall\u2014 (i) not later than 90 days after the date on which the Federal Chief Information Officer receives the list required by paragraph (1)(A) from each agency Chief Information Officer, compile, on the basis of each such list, a list of 10 legacy information technology systems that present the greatest security, privacy, and operational risks to the Federal Government; and (ii) not later than 90 days after the date on which the Federal Chief Information Officer receives updates under paragraph (1)(B) from each agency Chief Information Officer, update the list required by subparagraph (A) on the basis of each updates to the list provided by agency Chief information Officers under paragraph (1)(B). (B) Report to Congress Not later than 14 days after the date on which the Federal Chief Information Officer compiles the list required by subparagraph (A), or updates such list, the Director shall submit to the Committee on Oversight and Government Reform of the House of Representatives, the Committee on Homeland Security and Governmental Affairs of the Senate, and the Comptroller General of the United States, a report (which may include a classified annex) containing\u2014 (i) such list (including any update made to such list under subparagraph (A)(ii)); and (ii) each list provided by an agency Chief Information Officer under paragraph (1)(A) (including any update made to any such list under paragraph (1)(B)). (4) Guidance (A) In general Not later than 180 days after enactment of this Act, the Director shall issue guidance on implementing the requirements of this subsection that shall, at a minimum\u2014 (i) prescribe an appropriate format for list to be provided under paragraph (1)(A); (ii) prescribe the information to be included in the Legacy Federal IT Inventory required by paragraph (2); (iii) provide guidance on how an agency Chief Information Officer should identify high-risk legacy information technology systems that, at least, requires agency Chief Information Officers, in coordination with other agency stakeholders, to identify as a high risk legacy information technology system any outdated or obsolete system of information technology that is critical to the agency such that the loss or degradation of the system would create a security, operational, or privacy risk to the agency or would otherwise impact the ability of the agency to perform the mission of the agency, effectively deliver programs, or conduct business; and (iv) provide guidance on how existing reporting structures can be used to submit the Legacy Federal IT inventory required by paragraph (2). (B) Updates The Director may update the guidance issued under subparagraph (A) as the Director determines necessary. (5) Definitions In this subsection: (A) Agency Chief Information Officer The term agency Chief Information Officer means a Chief Information Officer designated under section 3506(a)(2) of title 44, United States Code. (B) Federal chief information officer The term Federal Chief Information Officer means the Administrator of the Office of Electronic Government. ; and\n**(6)**\nin subsection (g)(1), as so redesignated, by striking On and after the date that is 2 years after the date on which the Comptroller General of the United States issues the third report required under subsection (b)(7)(B), and inserting After December 31, 2032, .",
      "versionDate": "2025-04-24",
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
        "actionDate": "2025-12-02",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3306",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Modernizing Government Technology Reform Act",
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
            "name": "Computer security and identity theft",
            "updateDate": "2026-03-16T16:46:42Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-03-16T16:46:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-16T16:46:42Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2026-03-16T16:46:42Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2026-03-16T16:46:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-29T15:38:50Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2985ih.xml"
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
      "title": "Modernizing Government Technology Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modernizing Government Technology Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 1078 of the National Defense Authorization Act for Fiscal Year 2018 to increase the effectiveness of the Technology Modernization Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:28Z"
    }
  ]
}
```
