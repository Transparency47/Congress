# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6547?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6547
- Title: Least Cost Exception Act
- Congress: 119
- Bill type: HR
- Bill number: 6547
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 50 - 0.
- 2026-02-02 - Calendars: Placed on the Union Calendar, Calendar No. 405.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-474.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-474.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 50 - 0.
- 2026-02-02 - Calendars: Placed on the Union Calendar, Calendar No. 405.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-474.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-474.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6547",
    "number": "6547",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Least Cost Exception Act",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-02",
      "calendarNumber": {
        "calendar": "U00405"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 405.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-474.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-474.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 50 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
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
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
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
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
            "date": "2026-02-02T15:18:35Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T17:44:25Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T17:44:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:01:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-16",
      "state": "TN"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6547ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6547\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Flood introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Federal Deposit Insurance Act to provide an exception to the least-cost resolution requirement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Least Cost Exception Act .\n#### 2. Least cost resolution exception to avoid further concentration among global systemically important banking organizations\n##### (a) In general\nSection 13(c)(4) of the Federal Deposit Insurance Act ( 12 U.S.C. 1823(c)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by inserting except as provided in subparagraph (I), before the total amount ;\n**(2)**\nin subparagraph (E)(i), by inserting and except as provided in subparagraph (I), after appropriate, ; and\n**(3)**\nby adding at the end the following:\n(I) Least cost resolution exception (i) In general With respect to an exercise of authority by the Corporation described in subparagraph (A), the Corporation may, at the discretion of the Corporation, select an alternative method of exercising such authority that is not the least costly to the Deposit Insurance Fund, if\u2014 (I) the Corporation determines that the selected alternative complies with the requirements of clause (iii); and (II) the Corporation and the Board of Governors of the Federal Reserve System, after consultation with the Secretary of the Treasury, determine that the potential additional risks to the Deposit Insurance Fund of the selected alternative are outweighed by the reasonably expected benefits of limiting further concentration of the United States banking system in global systemically important banking organizations. (ii) Maximum cost to the Deposit Insurance Fund Not later than 1 year after the date of enactment of this subparagraph, the Corporation, by rule, shall specify the maximum amount of the net worth of the Deposit Insurance Fund that may be utilized to account for any determination under clause (i). (iii) Requirements described The requirements for the selected alternative described in clause (i) are as follows: (I) The selected alternative is least costly to the Deposit Insurance Fund of all alternatives that do not involve a transaction with a global systemically important banking organization and that do not exceed the cost of liquidating the insured depository institution. (II) The difference between the cost of the selected alternative and the cost of a covered alternative is less than the maximum cost to the Deposit Insurance Fund specified pursuant to the rule adopted under clause (ii). (III) In the case of a selected alternative that involves another person purchasing assets of the insured depository institution or assuming liabilities of the insured depository institution, such person agrees to pay an assessment to the Deposit Insurance Fund comprised of payments\u2014 (aa) made over a period to be determined by the Corporation, but which may not be less than 5 years; and (bb) that, taking into account a realistic discount rate, are in an aggregate amount equal to the difference calculated in subclause (II). (iv) Report to Congress Not later than 30 days after selecting an alternative described in clause (i), the Corporation shall issue a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate containing an analysis of the economic difference between the cost to the Deposit Insurance Fund of the selected alternative and the cost to the Deposit Insurance Fund of the least costly alternative that would have been selected absent the application of this subparagraph. (v) Definitions In this subparagraph: (I) Covered alternative The term covered alternative means a method of exercising authority described in subparagraph (A) that is the least costly to the Deposit Insurance Fund of all such methods that involve a sale of all or substantially all assets of the insured depository institution to, and assumption of all or substantially all liabilities of the insured depository institution by, a global systemically important banking organization. (II) Global systemically important banking organization The term global systemically important banking organization means a global systemically important BHC (as such term is defined in section 217.402 of title 12, Code of Federal Regulations, or any successor thereto) and any affiliate thereof. .\n##### (b) Rule of construction\nSection 13(c)(4)(H) of the Federal Deposit Insurance Act ( 12 U.S.C. 1823(c)(4)(H) ) does not apply to the amendments made by subsection (a).",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6547rh.xml",
      "text": "IB\nUnion Calendar No. 405\n119th CONGRESS\n2d Session\nH. R. 6547\n[Report No. 119\u2013474]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Flood introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 2, 2026 Additional sponsors: Mr. Foster , Mr. Rose , Mr. Moskowitz , and Mr. Lawler\nFebruary 2, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo amend the Federal Deposit Insurance Act to provide an exception to the least-cost resolution requirement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Least Cost Exception Act .\n#### 2. Least cost resolution exception to avoid further concentration among global systemically important banking organizations\n##### (a) In general\nSection 13(c)(4) of the Federal Deposit Insurance Act ( 12 U.S.C. 1823(c)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by inserting except as provided in subparagraph (I), before the total amount ;\n**(2)**\nin subparagraph (E)(i), by inserting and except as provided in subparagraph (I), after appropriate, ; and\n**(3)**\nby adding at the end the following:\n(I) Least cost resolution exception (i) In general With respect to an exercise of authority by the Corporation described in subparagraph (A), the Corporation may, at the discretion of the Corporation, select an alternative method of exercising such authority that is not the least costly to the Deposit Insurance Fund, if\u2014 (I) the Corporation determines that the selected alternative complies with the requirements of clause (iii); and (II) the Corporation and the Board of Governors of the Federal Reserve System, after consultation with the Secretary of the Treasury, determine that the potential additional risks to the Deposit Insurance Fund of the selected alternative are outweighed by the reasonably expected benefits of limiting further concentration of the United States banking system in global systemically important banking organizations. (ii) Maximum cost to the Deposit Insurance Fund Not later than 1 year after the date of enactment of this subparagraph, the Corporation, by rule, shall establish criteria for determining on a case-by-case basis the maximum allowable cost against the net worth of the Deposit Insurance Fund that may be utilized to account for any determination under clause (i). (iii) Requirements described The requirements for the selected alternative described in clause (i) are as follows: (I) The selected alternative is least costly to the Deposit Insurance Fund of all alternatives that do not involve a transaction with a global systemically important banking organization and that do not exceed the cost of liquidating the insured depository institution. (II) The difference between the cost of the selected alternative and the cost of a covered alternative is less than the maximum cost to the Deposit Insurance Fund specified pursuant to the rule adopted under clause (ii). (III) In the case of a selected alternative that involves another person purchasing assets of the insured depository institution or assuming deposit liabilities of the insured depository institution, such person agrees to pay an assessment to the Corporation comprised of payments\u2014 (aa) made over a period to be determined by the Corporation, but which may not be less than 5 years; and (bb) in an amount that takes into account, on a case-by-case basis, criteria the Corporation, by rule, shall establish, including a realistic discount rate, the aggregate amount equal to the difference calculated in subclause (II), and any bid inconsistent with the purposes of this Act, with such rule to be established by the Corporation not later than 1 year after the date of enactment of this subparagraph. (iv) Report to Congress Not later than 30 days after selecting an alternative described in clause (i), the Corporation shall issue a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate containing an analysis of the economic difference between the cost to the Deposit Insurance Fund of the selected alternative and the cost to the Deposit Insurance Fund of the least costly alternative that would have been selected absent the application of this subparagraph. (v) Cost determinations All cost determinations required under this subparagraph shall be made in accordance with subparagraphs (B) and (C). (vi) Definitions In this subparagraph: (I) Covered alternative The term covered alternative means a method of exercising authority described in subparagraph (A) that is the least costly to the Deposit Insurance Fund of all such methods that involve a sale of all or substantially all assets of the insured depository institution to, and assumption of all or substantially all deposit liabilities of the insured depository institution by, a global systemically important banking organization. (II) Global systemically important banking organization The term global systemically important banking organization means a global systemically important BHC (as such term is defined in section 217.402 of title 12, Code of Federal Regulations, or any successor thereto) and any affiliate thereof. .\n##### (b) Rule of construction\nSection 13(c)(4)(H) of the Federal Deposit Insurance Act ( 12 U.S.C. 1823(c)(4)(H) ) does not apply to the amendments made by subsection (a).",
      "versionDate": "2026-02-02",
      "versionType": "Reported in House"
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
        "actionDate": "2026-04-20",
        "text": "Placed on the Union Calendar, Calendar No. 535."
      },
      "number": "6955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Act",
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
            "name": "Accounting and auditing",
            "updateDate": "2026-01-02T16:29:38Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-01-02T16:41:52Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-01-02T16:41:57Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-02T16:45:37Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-01-02T16:27:16Z"
          },
          {
            "name": "Federal Deposit Insurance Corporation (FDIC)",
            "updateDate": "2026-01-02T16:41:23Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-01-02T16:41:35Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2026-01-02T16:41:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T18:48:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-02",
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
          "measure-id": "id119hr6547",
          "measure-number": "6547",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-02",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6547v07",
            "update-date": "2026-04-08"
          },
          "action-date": "2026-02-02",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Least Cost Exception Act</strong></p><p>This bill allows the Federal Deposit Insurance Corporation (FDIC) to waive the least-cost resolution requirement for failed insured depository institutions and use alternative methods of resolution, particularly alternatives that do not involve global systemically important banks (G-SIBs).</p><p>Under current law, the\u00a0FDIC must use the resolution method (such as a deposit payoff or the purchase and assumption of a bank\u2019s assets and liabilities) that costs the\u00a0FDIC's Deposit Insurance Fund the least to implement when an insured depository institution fails.</p><p>The bill provides an exception to this requirement if the following criteria are met:</p><ul><li>the alternative method is the least costly of all alternatives that do not involve a G-SIB and that do not exceed the cost of liquidation;</li><li>the difference in cost between the selected alternative and the cost of a resolution involving a purchase and assumption by a G-SIB is less than a maximum cost as established by rule;</li><li>if the alternative involves a person purchasing assets or assuming liabilities, that person must pay an assessment to the\u00a0FDIC; and</li><li>it is determined that the risks to the fund are outweighed by the benefits of limiting the concentration of U.S. banking under G-SIBs.</li></ul><p>FDIC must issue a report on any use of the exception established by this bill containing an analysis of the economic impact of cost differences between the selected alternative and the least-cost alternative.</p>"
        },
        "title": "Least Cost Exception Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6547.xml",
    "summary": {
      "actionDate": "2026-02-02",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Least Cost Exception Act</strong></p><p>This bill allows the Federal Deposit Insurance Corporation (FDIC) to waive the least-cost resolution requirement for failed insured depository institutions and use alternative methods of resolution, particularly alternatives that do not involve global systemically important banks (G-SIBs).</p><p>Under current law, the\u00a0FDIC must use the resolution method (such as a deposit payoff or the purchase and assumption of a bank\u2019s assets and liabilities) that costs the\u00a0FDIC's Deposit Insurance Fund the least to implement when an insured depository institution fails.</p><p>The bill provides an exception to this requirement if the following criteria are met:</p><ul><li>the alternative method is the least costly of all alternatives that do not involve a G-SIB and that do not exceed the cost of liquidation;</li><li>the difference in cost between the selected alternative and the cost of a resolution involving a purchase and assumption by a G-SIB is less than a maximum cost as established by rule;</li><li>if the alternative involves a person purchasing assets or assuming liabilities, that person must pay an assessment to the\u00a0FDIC; and</li><li>it is determined that the risks to the fund are outweighed by the benefits of limiting the concentration of U.S. banking under G-SIBs.</li></ul><p>FDIC must issue a report on any use of the exception established by this bill containing an analysis of the economic impact of cost differences between the selected alternative and the least-cost alternative.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6547"
    },
    "title": "Least Cost Exception Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-02",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Least Cost Exception Act</strong></p><p>This bill allows the Federal Deposit Insurance Corporation (FDIC) to waive the least-cost resolution requirement for failed insured depository institutions and use alternative methods of resolution, particularly alternatives that do not involve global systemically important banks (G-SIBs).</p><p>Under current law, the\u00a0FDIC must use the resolution method (such as a deposit payoff or the purchase and assumption of a bank\u2019s assets and liabilities) that costs the\u00a0FDIC's Deposit Insurance Fund the least to implement when an insured depository institution fails.</p><p>The bill provides an exception to this requirement if the following criteria are met:</p><ul><li>the alternative method is the least costly of all alternatives that do not involve a G-SIB and that do not exceed the cost of liquidation;</li><li>the difference in cost between the selected alternative and the cost of a resolution involving a purchase and assumption by a G-SIB is less than a maximum cost as established by rule;</li><li>if the alternative involves a person purchasing assets or assuming liabilities, that person must pay an assessment to the\u00a0FDIC; and</li><li>it is determined that the risks to the fund are outweighed by the benefits of limiting the concentration of U.S. banking under G-SIBs.</li></ul><p>FDIC must issue a report on any use of the exception established by this bill containing an analysis of the economic impact of cost differences between the selected alternative and the least-cost alternative.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6547"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6547ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6547rh.xml"
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
      "title": "Least Cost Exception Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-03T06:53:19Z"
    },
    {
      "title": "Least Cost Exception Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Least Cost Exception Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Deposit Insurance Act to provide an exception to the least-cost resolution requirement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T09:03:24Z"
    }
  ]
}
```
