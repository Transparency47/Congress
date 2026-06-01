# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6570?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6570
- Title: Merger Agreement Approvals Clarity and Predictability Act
- Congress: 119
- Bill type: HR
- Bill number: 6570
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 460.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-535.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-535.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 460.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-535.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-535.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6570",
    "number": "6570",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Merger Agreement Approvals Clarity and Predictability Act",
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
        "calendar": "U00460"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 460.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-535.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-535.",
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
            "date": "2026-02-25T18:52:36Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T18:59:47Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T18:59:38Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:02:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6570ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6570\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Fitzgerald introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Comptroller General of the United States to study the use of commitments and conditions in connection with insured depository institution merger applications by Federal depository institution regulatory agencies to ensure they align with statutory requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Merger Agreement Approvals Clarity and Predictability Act .\n#### 2. GAO study on use of commitments and conditions in connection with insured depository institution merger applications\n##### (a) Study\nThe Comptroller General of the United States shall carry out a study on the use of commitments and conditions by Federal depository institution regulatory agencies in connection with insured depository institution merger applications. The study shall\u2014\n**(1)**\ninclude an evaluation of relevant quantifiable metrics; and\n**(2)**\nreview the extent to which the use of commitments and conditions has aligned with statutory requirements, including a review of whether the use of commitments and conditions has been influenced by extrastatutory issues or considerations.\n##### (b) Report\nNot later than 6 months after the date of enactment of this Act, the Comptroller General shall issue a report to Congress containing all findings and determinations made in carrying out the study required under subsection (a).\n##### (c) Definitions\nIn this section:\n**(1) Application**\nThe term application means an application, notice, or other similar request for permission submitted to a Federal depository institution regulatory agency.\n**(2) Federal depository institution regulatory agency**\nThe term Federal depository institution regulatory agency means the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration Board.\n**(3) Insured depository institution**\nThe term insured depository institution \u2014\n**(A)**\nhas the meaning given that term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nmeans an insured credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) Insured depository institution merger application**\nThe term insured depository institution merger application means an application with respect to the acquisition of an insured depository institution, its equity interests, its assets, or its deposits under\u2014\n**(A)**\nsection 10(e) of the Home Owners\u2019 Loan Act ( 12 U.S.C. 1467a(e) );\n**(B)**\nsection 205(b) of the Federal Credit Union Act ( 12 U.S.C. 1785(b) );\n**(C)**\nsection 7(j) of the Federal Deposit Insurance Act ( 12 U.S.C. 1817(j) );\n**(D)**\nsection 18(c)(2) of the Federal Deposit Insurance Act ( 12 U.S.C. 1828(c)(2) );\n**(E)**\nsection 3 of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1842 ); and\n**(F)**\nsection 4 of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843 ).",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6570rh.xml",
      "text": "IB\nUnion Calendar No. 460\n119th CONGRESS\n2d Session\nH. R. 6570\n[Report No. 119\u2013535]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Fitzgerald introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsor: Mr. Lawler\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo require the Comptroller General of the United States to study the use of commitments and conditions in connection with insured depository institution merger applications by Federal depository institution regulatory agencies to ensure they align with statutory requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Merger Agreement Approvals Clarity and Predictability Act .\n#### 2. GAO study on use of commitments and conditions in connection with insured depository institution merger applications\n##### (a) Study\nThe Comptroller General of the United States shall carry out a study on the use of commitments, conditions, and other aspects of merger review procedures by Federal depository institution regulatory agencies in connection with insured depository institution merger applications. The study shall\u2014\n**(1)**\ninclude an evaluation of relevant quantifiable metrics;\n**(2)**\nreview the extent to which the use of commitments and conditions has aligned with statutory requirements, including a review of whether the use of commitments and conditions has been influenced by extrastatutory issues or considerations;\n**(3)**\nconsider the benefits and risks of utilizing different merger review approaches and procedures in compliance with the law; and\n**(4)**\ninclude an evaluation of the impact of such merger review procedures and resulting approved mergers on safety and soundness, financial stability, competition, and the availability of financial products and services offered by insured depository institutions.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General shall issue a report to Congress containing all findings and determinations made in carrying out the study required under subsection (a).\n##### (c) Definitions\nIn this section:\n**(1) Application**\nThe term application means an application, notice, or other similar request for permission submitted to a Federal depository institution regulatory agency.\n**(2) Federal depository institution regulatory agency**\nThe term Federal depository institution regulatory agency means the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the National Credit Union Administration Board.\n**(3) Insured depository institution**\nThe term insured depository institution \u2014\n**(A)**\nhas the meaning given that term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ); and\n**(B)**\nmeans an insured credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) Insured depository institution merger application**\nThe term insured depository institution merger application means an application with respect to the acquisition of an insured depository institution, its equity interests, its assets, or its deposits under\u2014\n**(A)**\nsection 10(e) of the Home Owners\u2019 Loan Act ( 12 U.S.C. 1467a(e) );\n**(B)**\nsection 205(b) of the Federal Credit Union Act ( 12 U.S.C. 1785(b) );\n**(C)**\nsection 7(j) of the Federal Deposit Insurance Act ( 12 U.S.C. 1817(j) );\n**(D)**\nsection 18(c)(2) of the Federal Deposit Insurance Act ( 12 U.S.C. 1828(c)(2) );\n**(E)**\nsection 3 of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1842 ); and\n**(F)**\nsection 4 of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843 ).",
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
            "name": "Congressional oversight",
            "updateDate": "2026-01-02T16:58:29Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-01-02T16:57:58Z"
          },
          {
            "name": "Federal Deposit Insurance Corporation (FDIC)",
            "updateDate": "2026-01-02T16:58:02Z"
          },
          {
            "name": "Government Accountability Office (GAO)",
            "updateDate": "2026-01-02T16:56:41Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-02T16:58:21Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-02T16:58:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T19:32:22Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6570ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6570rh.xml"
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
      "title": "Merger Agreement Approvals Clarity and Predictability Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:38:15Z"
    },
    {
      "title": "Merger Agreement Approvals Clarity and Predictability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T10:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Merger Agreement Approvals Clarity and Predictability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T10:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General of the United States to study the use of commitments and conditions in connection with insured depository institution merger applications by Federal depository institution regulatory agencies to ensure they align with statutory requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T10:03:27Z"
    }
  ]
}
```
