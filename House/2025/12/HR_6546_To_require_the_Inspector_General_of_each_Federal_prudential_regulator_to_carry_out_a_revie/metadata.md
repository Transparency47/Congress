# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6546?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6546
- Title: Merger Process Review Act
- Congress: 119
- Bill type: HR
- Bill number: 6546
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 453.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-528.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-528.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 453.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-528.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-528.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6546",
    "number": "6546",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000816",
        "district": "25",
        "firstName": "Roger",
        "fullName": "Rep. Williams, Roger [R-TX-25]",
        "lastName": "Williams",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Merger Process Review Act",
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
        "calendar": "U00453"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 453.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-528.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-528.",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.",
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
            "date": "2026-02-25T18:50:09Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T19:01:23Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T19:01:15Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-09T17:05:30Z",
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
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6546ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6546\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Williams of Texas introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Inspector General of each Federal prudential regulator to carry out a review every 3 years of the regulator\u2019s handling of insured depository institution merger applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Merger Process Review Act .\n#### 2. Inspector general review of the handling of insured depository institution merger applications\n##### (a) Review\nNot later than 1 year after the date of enactment of this Act, and every 3 years thereafter, the Inspector General of each Federal depository institution regulatory agency shall review the Federal depository institution regulatory agency\u2019s record of timeliness and efficiency in reviewing and acting upon insured depository institution merger applications. The review shall\u2014\n**(1)**\ninclude an evaluation of relevant quantifiable metrics, including mean and median application processing times;\n**(2)**\nidentify sources of delay that may hinder the timely consummation of proposals that meet the relevant statutory factors; and\n**(3)**\ninclude specific recommendations to improve the timeliness and efficiency of application processing, consistent with the Federal depository institution regulatory agency\u2019s statutory responsibilities.\n##### (b) Report\nEach Inspector General described under subsection (a) shall, at the conclusion of each review required under subsection (a), issue a report to Congress containing all findings and determinations made in carrying out the review.\n##### (c) Agency response\nIn response to each report issued to Congress under subsection (a), the appropriate Federal depository institution regulatory agency shall submit to Congress a written response, including a plan to implement the recommendations in the report, to the extent such implementation is appropriate.\n##### (d) Definitions\nIn this section:\n**(1) Application**\nThe term application means an application, notice, or other similar request for permission submitted to a Federal depository institution regulatory agency.\n**(2) Federal depository institution regulatory agency**\nThe term Federal depository institution regulatory agency means the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration Board.\n**(3) Insured depository institution**\nThe term insured depository institution \u2014\n**(A)**\nhas the meaning given that term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nmeans an insured credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) Insured depository institution merger application**\nThe term insured depository institution merger application means an application with respect to the acquisition of an insured depository institution, its equity interests, its assets, or its deposits under\u2014\n**(A)**\nsection 10(e) of the Home Owners\u2019 Loan Act ( 12 U.S.C. 1467a(e) );\n**(B)**\nsection 205(b) of the Federal Credit Union Act ( 12 U.S.C. 1785(b) );\n**(C)**\nsection 7(j) of the Federal Deposit Insurance Act ( 12 U.S.C. 1817(j) );\n**(D)**\nsection 18(c)(2) of the Federal Deposit Insurance Act ( 12 U.S.C. 1828(c)(2) );\n**(E)**\nsection 3 of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1842 ); and\n**(F)**\nsection 4 of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843 ).",
      "versionDate": "2025-12-09",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6546rh.xml",
      "text": "IB\nUnion Calendar No. 453\n119th CONGRESS\n2d Session\nH. R. 6546\n[Report No. 119\u2013528]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Williams of Texas introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsors: Mr. Davidson and Mr. Lawler\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 9, 2025\nA BILL\nTo require the Inspector General of each Federal prudential regulator to carry out a review every 3 years of the regulator\u2019s handling of insured depository institution merger applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Merger Process Review Act .\n#### 2. Inspector general review of the handling of insured depository institution merger applications\n##### (a) Review\nNot later than 1 year after the date of enactment of this Act, and every 3 years thereafter, the Inspector General of each Federal depository institution regulatory agency shall review the Federal depository institution regulatory agency\u2019s merger review procedures, including record of timeliness and efficiency in reviewing and acting upon insured depository institution merger applications. The review shall\u2014\n**(1)**\ninclude an evaluation of relevant quantifiable metrics, including mean and median application processing times;\n**(2)**\nidentify sources of delay that may hinder the timely consummation of proposals that meet the relevant statutory factors;\n**(3)**\nconsider the benefits and risks of utilizing different merger review approaches and procedures in compliance with the law;\n**(4)**\ninclude an evaluation of the impact of such merger review procedures and resulting approved mergers on safety and soundness, financial stability, competition, and the availability of financial products and services offered by insured depository institutions; and\n**(5)**\ninclude specific recommendations to improve the merger review process, including timeliness and efficiency of application processing, consistent with the Federal depository institution regulatory agency\u2019s statutory responsibilities.\n##### (b) Report\nEach Inspector General described under subsection (a) shall, at the conclusion of each review required under subsection (a), issue a report to Congress containing all findings and determinations made in carrying out the review, and publish such report online.\n##### (c) Agency response\nIn response to each report issued to Congress under subsection (a), the appropriate Federal depository institution regulatory agency shall submit to Congress and publish online a written response, including a plan to implement the recommendations in the report, to the extent such implementation is appropriate.\n##### (d) Definitions\nIn this section:\n**(1) Application**\nThe term application means an application, notice, or other similar request for permission submitted to a Federal depository institution regulatory agency.\n**(2) Federal depository institution regulatory agency**\nThe term Federal depository institution regulatory agency means the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration Board.\n**(3) Insured depository institution**\nThe term insured depository institution \u2014\n**(A)**\nhas the meaning given that term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nmeans an insured credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) Insured depository institution merger application**\nThe term insured depository institution merger application means an application with respect to the acquisition of an insured depository institution, its equity interests, its assets, or its deposits under\u2014\n**(A)**\nsection 10(e) of the Home Owners\u2019 Loan Act ( 12 U.S.C. 1467a(e) );\n**(B)**\nsection 205(b) of the Federal Credit Union Act ( 12 U.S.C. 1785(b) );\n**(C)**\nsection 7(j) of the Federal Deposit Insurance Act ( 12 U.S.C. 1817(j) );\n**(D)**\nsection 18(c)(2) of the Federal Deposit Insurance Act ( 12 U.S.C. 1828(c)(2) );\n**(E)**\nsection 3 of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1842 ); and\n**(F)**\nsection 4 of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843 ).",
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
            "updateDate": "2026-01-27T17:44:17Z"
          },
          {
            "name": "Business records",
            "updateDate": "2026-01-27T17:45:39Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-27T17:45:31Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-01-27T17:44:23Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-27T17:46:02Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-27T17:45:53Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-01-27T17:45:13Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-01-27T17:44:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T18:47:29Z"
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
          "measure-id": "id119hr6546",
          "measure-number": "6546",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6546v07",
            "update-date": "2026-04-10"
          },
          "action-date": "2026-02-25",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Merger Process Review Act</strong></p><p>This bill requires the appropriate Office of the Inspector General (OIG) that serves the Federal Reserve Board, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration to periodically review the merger applications received by that regulator.\u00a0</p><p>Specifically, every three years, the appropriate OIG must examine that regulator\u2019s merger approval procedures, including timeliness and efficiency, and report on its findings and recommendations. The regulator must then submit a plan to implement the appropriate recommendations.</p>"
        },
        "title": "Merger Process Review Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6546.xml",
    "summary": {
      "actionDate": "2026-02-25",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Merger Process Review Act</strong></p><p>This bill requires the appropriate Office of the Inspector General (OIG) that serves the Federal Reserve Board, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration to periodically review the merger applications received by that regulator.\u00a0</p><p>Specifically, every three years, the appropriate OIG must examine that regulator\u2019s merger approval procedures, including timeliness and efficiency, and report on its findings and recommendations. The regulator must then submit a plan to implement the appropriate recommendations.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6546"
    },
    "title": "Merger Process Review Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-25",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Merger Process Review Act</strong></p><p>This bill requires the appropriate Office of the Inspector General (OIG) that serves the Federal Reserve Board, the Office of the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration to periodically review the merger applications received by that regulator.\u00a0</p><p>Specifically, every three years, the appropriate OIG must examine that regulator\u2019s merger approval procedures, including timeliness and efficiency, and report on its findings and recommendations. The regulator must then submit a plan to implement the appropriate recommendations.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6546"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6546ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6546rh.xml"
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
      "title": "Merger Process Review Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:38:15Z"
    },
    {
      "title": "Merger Process Review Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Merger Process Review Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Inspector General of each Federal prudential regulator to carry out a review every 3 years of the regulator's handling of insured depository institution merger applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T09:03:23Z"
    }
  ]
}
```
