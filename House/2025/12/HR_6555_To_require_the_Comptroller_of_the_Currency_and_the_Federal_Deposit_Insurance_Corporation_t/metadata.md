# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6555?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6555
- Title: Enhancing Bank Resolution Participation Act
- Congress: 119
- Bill type: HR
- Bill number: 6555
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 459.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-534.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-534.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 459.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-534.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-534.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6555",
    "number": "6555",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Enhancing Bank Resolution Participation Act",
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
        "calendar": "U00459"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 459.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-534.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-534.",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.",
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
            "date": "2026-02-25T18:52:19Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T17:45:57Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T17:45:44Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:05:30Z",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6555ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6555\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Huizenga introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Comptroller of the Currency and the Federal Deposit Insurance Corporation to carry out a study on shelf charters and modified bidder qualification processes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing Bank Resolution Participation Act .\n#### 2. Study on shelf charters and modified bidder qualification processes\n##### (a) Study\nThe Comptroller of the Currency and the Federal Deposit Insurance Corporation shall, jointly, carry out a study of\u2014\n**(1)**\nthe use by the Comptroller of the Currency of shelf charters, including all conditional or preliminary shelf charter approvals granted between January 1, 2008, and the date of enactment of this Act;\n**(2)**\nthe use by the Federal Deposit Insurance Corporation of the modified bidder qualification process;\n**(3)**\nwhether shelf charters and modified bidder qualification processes were considered or used in connection with the receivership of any insured depository institution for which the Federal Deposit Insurance Corporation was appointed receiver in 2023; and\n**(4)**\nwith respect to such receiverships, the extent to which greater use of shelf charters and modified bidder qualification processes could have\u2014\n**(A)**\nexpanded the pool of participants in the acquisition of the assets or liabilities of such failed insured depository institutions;\n**(B)**\nresulted in greater competition and diversity in market outcomes;\n**(C)**\nprotected the Deposit Insurance Fund; or\n**(D)**\nstrengthened financial stability and reduced the need for any emergency determination by the Secretary of the Treasury under section 13(c)(4)(G) of the Federal Deposit Insurance Act ( 12 U.S.C. 1823(c)(4)(G) ) with respect to any such receivership.\n##### (b) Report\nNot later than 270 days after the date of enactment of this Act, the Comptroller of the Currency, and the Federal Deposit Insurance Corporation shall, jointly, submit a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate containing\u2014\n**(1)**\nall findings and determinations made in carrying out the study required under subsection (a); and\n**(2)**\nan identification of statutory or regulatory barriers to the use and effectiveness of shelf charters and modified bidder qualification processes in the resolution of failed banks, including recommendations for legislative and regulatory changes.\n##### (c) Consultation\nThe Comptroller of the Currency and the Federal Deposit Insurance Corporation shall consult with the Board of Governors of the Federal Reserve System in carrying out the study under subsection (a) and in preparing the report under subsection (b), including with respect to the application of the Bank Holding Company Act of 1956 to shelf charter proposals and to the participation of investors not organized as an insured depository institution in the modified bidder qualification process.\n##### (d) Definitions\nIn this section:\n**(1) Insured depository institution**\nThe term insured depository institution has the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ).\n**(2) Modified bidder qualification process**\nThe term modified bidder qualification process has the meaning given such term in the press release of the Federal Deposit Insurance Corporation titled FDIC Expands Bidder List for Troubled Institutions Plan Allows Those Without a Bank Charter to Participate in the Process published November 26, 2008.\n**(3) Shelf charter**\nThe term shelf charter has the meaning given such term in the report issued by the Comptroller of the Currency titled Activities Permissible for National Banks and Federal Savings Associations, Cumulative published October 2017.",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6555rh.xml",
      "text": "IB\nUnion Calendar No. 459\n119th CONGRESS\n2d Session\nH. R. 6555\n[Report No. 119\u2013534]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Huizenga introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsors: Mr. Gottheimer and Mr. Lawler\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo require the Comptroller of the Currency and the Federal Deposit Insurance Corporation to carry out a study on shelf charters and modified bidder qualification processes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing Bank Resolution Participation Act .\n#### 2. Study on shelf charters and modified bidder qualification processes\n##### (a) Study\nThe Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the Board of the Governors of the Federal Reserve System shall, jointly, carry out a study of\u2014\n**(1)**\nthe use by the Comptroller of the Currency of shelf charters, including all conditional or preliminary shelf charter approvals granted between January 1, 2008, and the date of enactment of this Act;\n**(2)**\nthe use by the Federal Deposit Insurance Corporation of the modified bidder qualification process;\n**(3)**\nthe application of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1841 et seq. ) and section 10 of the Home Owners\u2019 Loan Act ( 12 U.S.C. 1467a ) to shelf charter proposals;\n**(4)**\nwhether shelf charters and modified bidder qualification processes were considered or used in connection with the receivership of any insured depository institution for which the Federal Deposit Insurance Corporation was appointed receiver in 2023;\n**(5)**\nwith respect to such receiverships, the extent to which greater use of shelf charters and modified bidder qualification processes could have\u2014\n**(A)**\nexpanded the pool of participants in the acquisition of the assets or liabilities of such failed insured depository institutions;\n**(B)**\nresulted in greater competition and diversity in market outcomes;\n**(C)**\nprotected the Deposit Insurance Fund; or\n**(D)**\nstrengthened financial stability and reduced the need for any emergency determination by the Secretary of the Treasury under section 13(c)(4)(G) of the Federal Deposit Insurance Act ( 12 U.S.C. 1823(c)(4)(G) ) with respect to any such receivership;\n**(6)**\nthe impact of the use of shelf charters and modified bidder qualification processes since January 1, 2008, including on financial stability, the safety and soundness of affected insured depository institutions, and the availability of financial products and services provided to consumers by such institutions; and\n**(7)**\nany benefits and risks of private equity ownership of banks through the use of shelf charters and modified bidder qualification processes.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller of the Currency, the Federal Deposit Insurance Corporation, and the Board of the Governors of the Federal Reserve System shall, jointly, submit a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate containing\u2014\n**(1)**\nall findings and determinations made in carrying out the study required under subsection (a); and\n**(2)**\nan identification of statutory or regulatory barriers to the use and effectiveness of shelf charters and modified bidder qualification processes in the resolution of failed insured depository institutions, including recommendations for legislative and regulatory changes.\n##### (c) Definitions\nIn this section:\n**(1) Insured depository institution**\nThe term insured depository institution has the meaning given the term in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ).\n**(2) Modified bidder qualification process**\nThe term modified bidder qualification process has the meaning given such term in the press release of the Federal Deposit Insurance Corporation titled FDIC Expands Bidder List for Troubled Institutions Plan Allows Those Without a Bank Charter to Participate in the Process published November 26, 2008.\n**(3) Shelf charter**\nThe term shelf charter has the meaning given such term in the report issued by the Comptroller of the Currency titled Activities Permissible for National Banks and Federal Savings Associations, Cumulative published October 2017.",
      "versionDate": "2026-02-25",
      "versionType": "Reported in House"
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
            "updateDate": "2026-01-02T18:52:35Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-01-02T18:49:05Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-02T19:03:28Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-01-02T18:52:16Z"
          },
          {
            "name": "Financial crises and stabilization",
            "updateDate": "2026-01-02T18:48:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T19:29:36Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6555ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6555rh.xml"
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
      "title": "Enhancing Bank Resolution Participation Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:23:18Z"
    },
    {
      "title": "Enhancing Bank Resolution Participation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enhancing Bank Resolution Participation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller of the Currency and the Federal Deposit Insurance Corporation to carry out a study on shelf charters and modified bidder qualification processes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T09:03:25Z"
    }
  ]
}
```
