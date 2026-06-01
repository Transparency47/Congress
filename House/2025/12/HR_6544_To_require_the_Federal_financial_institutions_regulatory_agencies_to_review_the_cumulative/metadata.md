# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6544?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6544
- Title: REVIEW Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6544
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 30 - 23.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 452.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-527.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-527.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 30 - 23.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 452.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-527.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-527.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6544",
    "number": "6544",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "T000480",
        "district": "4",
        "firstName": "William",
        "fullName": "Rep. Timmons, William R. [R-SC-4]",
        "lastName": "Timmons",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "REVIEW Act of 2025",
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
      "actionDate": "2026-02-25",
      "calendarNumber": {
        "calendar": "U00452"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 452.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-25",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-527.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-25",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-527.",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 30 - 23.",
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
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
            "date": "2026-02-25T18:49:53Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T20:13:22Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T20:13:14Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-09T17:00:10Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6544ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6544\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Timmons introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Federal financial institutions regulatory agencies to review the cumulative impact of regulations issued by such agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Regulatory Efficiency, Verification, Itemization, and Enhanced Workflow Act of 2025 or the REVIEW Act of 2025 .\n#### 2. Review of regulations\nSection 2222 of the Economic Growth and Regulatory Paperwork Reduction Act of 1996 ( 12 U.S.C. 3311 ) is amended\u2014\n**(1)**\nby striking appropriate Federal banking agency each place such term appears and inserting Federal financial institutions regulatory agency ;\n**(2)**\nby striking appropriate Federal banking agencies each place such term appears and inserting Federal financial institutions regulatory agencies ;\n**(3)**\nin subsection (a)\u2014\n**(A)**\nby striking represented on the Council ; and\n**(B)**\nby striking once every 10 years and inserting once every 5 years ;\n**(4)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively (and adjusting the margins accordingly);\n**(B)**\nby striking In conducting and inserting the following:\n(1) Solicitation of public comment In conducting ; and\n**(C)**\nby adding at the end the following:\n(2) Internal review of cumulative impact Each Federal financial institutions regulatory agency shall conduct an internal review of the cumulative impact of regulations issued by the Federal financial institutions regulatory agency that\u2014 (A) assesses the effects of such regulations on consumers\u2019 access to financial products and services; (B) assesses the effects of such regulations on the availability of financial products and services to financial and nonfinancial firms; (C) assesses the impact of such regulations on credit availability and financial market liquidity in United States financial markets; (D) assesses the balance of benefits and costs of such regulations with respect to the safety and soundness of the United States financial system and overall economic activity in the United States; (E) to the extent practicable, quantifies the direct and indirect economic costs imposed by such regulations; and (F) includes recommendations to streamline, simplify, or eliminate duplicative, outdated, and unnecessarily burdensome regulations. ;\n**(5)**\nin subsection (c)\u2014\n**(A)**\nby striking subsection (b)(2) and inserting subsection (b)(1)(B), and the internal review under subsection (b)(2), ; and\n**(B)**\nby striking once every 10 years and inserting once every 5 years ;\n**(6)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1), by striking and at the end;\n**(B)**\nby redesignating paragraph (2) as paragraph (3);\n**(C)**\nby inserting after paragraph (1) the following:\n(2) a summary of the findings and determinations of each Federal financial institutions regulatory agency of the internal review conducted by the Federal financial institutions regulatory agency under subsection (b)(2); and ; and\n**(D)**\nin paragraph (3), as so redesignated, by striking the regulatory burdens associated with such issues by regulation and inserting the regulatory burdens associated with the issues identified by public comments received by the Council and the Federal financial institutions regulatory agencies, as well as the regulatory burdens identified by each Federal financial institutions regulatory agency through the internal reviews conducted under subsection (b)(2), by regulation ; and\n**(7)**\nby adding at the end the following:\n(f) Federal financial institutions regulatory agency defined The term Federal financial institutions regulatory agency has the meaning given that term in section 1003 of the Federal Financial Institutions Examination Council Act of 1978 ( 12 U.S.C. 3302 ). .",
      "versionDate": "2025-12-09",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6544rh.xml",
      "text": "IB\nUnion Calendar No. 452\n119th CONGRESS\n2d Session\nH. R. 6544\n[Report No. 119\u2013527]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Timmons introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 9, 2025\nA BILL\nTo require the Federal financial institutions regulatory agencies to review the cumulative impact of regulations issued by such agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Regulatory Efficiency, Verification, Itemization, and Enhanced Workflow Act of 2025 or the REVIEW Act of 2025 .\n#### 2. Review of regulations\nSection 2222 of the Economic Growth and Regulatory Paperwork Reduction Act of 1996 ( 12 U.S.C. 3311 ) is amended\u2014\n**(1)**\nby striking appropriate Federal banking agency each place such term appears and inserting Federal financial institutions regulatory agency ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking represented on the Council ; and\n**(B)**\nby striking once every 10 years and inserting once every 7 years ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively (and adjusting the margins accordingly);\n**(B)**\nby striking In conducting and inserting the following:\n(1) Solicitation of public comment In conducting ; and\n**(C)**\nby adding at the end the following:\n(2) Internal review of cumulative impact Each Federal financial institutions regulatory agency shall conduct an internal review of the cumulative impact of regulations issued by the Federal financial institutions regulatory agency that\u2014 (A) assesses the effects of such regulations on consumers\u2019 access to financial products and services; (B) assesses the effects of such regulations on the availability of financial products and services to financial and nonfinancial firms; (C) assesses the impact of such regulations on credit availability and financial market liquidity in United States financial markets; (D) assesses the balance of benefits and costs of such regulations with respect to the safety and soundness of the United States financial system and overall economic activity in the United States; (E) to the extent practicable, quantifies the direct and indirect economic costs imposed by such regulations; and (F) includes recommendations to streamline, simplify, or eliminate duplicative, outdated, and unnecessarily burdensome regulations. ;\n**(4)**\nin subsection (c)\u2014\n**(A)**\nby striking subsection (b)(2) and inserting subsection (b)(1)(B), and the internal review under subsection (b)(2), ; and\n**(B)**\nby striking once every 10 years and inserting once every 7 years ;\n**(5)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking appropriate Federal banking agencies and inserting Federal financial institutions regulatory agencies ; and\n**(ii)**\nby striking and at the end;\n**(B)**\nby redesignating paragraph (2) as paragraph (3);\n**(C)**\nby inserting after paragraph (1) the following:\n(2) a summary of the findings and determinations of each Federal financial institutions regulatory agency of the internal review conducted by the Federal financial institutions regulatory agency under subsection (b)(2); and ; and\n**(D)**\nin paragraph (3), as so redesignated, by striking the regulatory burdens associated with such issues by regulation and inserting the regulatory burdens associated with the issues identified by public comments received by the Council and the Federal financial institutions regulatory agencies, as well as the regulatory burdens identified by each Federal financial institutions regulatory agency through the internal reviews conducted under subsection (b)(2), by regulation ; and\n**(6)**\nby adding at the end the following:\n(f) Federal financial institutions regulatory agency defined The term Federal financial institutions regulatory agency has the meaning given that term in section 1003 of the Federal Financial Institutions Examination Council Act of 1978 ( 12 U.S.C. 3302 ). .",
      "versionDate": "2026-02-25",
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-02-19T16:29:59Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-19T16:30:06Z"
          },
          {
            "name": "Credit and credit markets",
            "updateDate": "2026-02-19T16:29:54Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2026-02-19T16:14:18Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-19T16:30:46Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-19T16:30:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T19:28:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-25",
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
          "measure-id": "id119hr6544",
          "measure-number": "6544",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6544v07",
            "update-date": "2026-04-17"
          },
          "action-date": "2026-02-25",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Regulatory Efficiency, Verification, Itemization, and Enhanced Workflow Act of 2025 or the REVIEW Act of 2025</strong></p><p>This bill increases the frequency and expands the scope of regulatory reviews conducted by federal financial agencies.</p><p>Currently, these regulatory reviews must occur every 10 years to\u00a0identify\u00a0outdated or unnecessary regulations imposed on insured depository institutions. The bill increases this frequency to every 7 years.\u00a0</p><p>Additionally, the bill expands these reviews to include an internal review of the cumulative impacts of regulations, including an assessment regarding (1)\u00a0access to financial products and services, (2) credit availability and market liquidity, and (3) costs and benefits of regulations with respect to financial safety and soundness and overall economic activity.\u00a0</p><p>The bill also codifies the National Credit Union Administration\u2019s inclusion in this review process.\u00a0</p>"
        },
        "title": "REVIEW Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6544.xml",
    "summary": {
      "actionDate": "2026-02-25",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Regulatory Efficiency, Verification, Itemization, and Enhanced Workflow Act of 2025 or the REVIEW Act of 2025</strong></p><p>This bill increases the frequency and expands the scope of regulatory reviews conducted by federal financial agencies.</p><p>Currently, these regulatory reviews must occur every 10 years to\u00a0identify\u00a0outdated or unnecessary regulations imposed on insured depository institutions. The bill increases this frequency to every 7 years.\u00a0</p><p>Additionally, the bill expands these reviews to include an internal review of the cumulative impacts of regulations, including an assessment regarding (1)\u00a0access to financial products and services, (2) credit availability and market liquidity, and (3) costs and benefits of regulations with respect to financial safety and soundness and overall economic activity.\u00a0</p><p>The bill also codifies the National Credit Union Administration\u2019s inclusion in this review process.\u00a0</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119hr6544"
    },
    "title": "REVIEW Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2026-02-25",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Regulatory Efficiency, Verification, Itemization, and Enhanced Workflow Act of 2025 or the REVIEW Act of 2025</strong></p><p>This bill increases the frequency and expands the scope of regulatory reviews conducted by federal financial agencies.</p><p>Currently, these regulatory reviews must occur every 10 years to\u00a0identify\u00a0outdated or unnecessary regulations imposed on insured depository institutions. The bill increases this frequency to every 7 years.\u00a0</p><p>Additionally, the bill expands these reviews to include an internal review of the cumulative impacts of regulations, including an assessment regarding (1)\u00a0access to financial products and services, (2) credit availability and market liquidity, and (3) costs and benefits of regulations with respect to financial safety and soundness and overall economic activity.\u00a0</p><p>The bill also codifies the National Credit Union Administration\u2019s inclusion in this review process.\u00a0</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119hr6544"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6544ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6544rh.xml"
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
      "title": "REVIEW Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:38:15Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Regulatory Efficiency, Verification, Itemization, and Enhanced Workflow Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:38:15Z"
    },
    {
      "title": "REVIEW Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REVIEW Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Regulatory Efficiency, Verification, Itemization, and Enhanced Workflow Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal financial institutions regulatory agencies to review the cumulative impact of regulations issued by such agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T09:03:24Z"
    }
  ]
}
```
