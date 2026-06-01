# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6552?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6552
- Title: Bank-Fintech Partnership Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 6552
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
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 456.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-531.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-531.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 456.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-531.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-531.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6552",
    "number": "6552",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Bank-Fintech Partnership Enhancement Act",
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
        "calendar": "U00456"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 456.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-531.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-531.",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.",
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
            "date": "2026-02-25T18:51:15Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T20:14:25Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T20:14:17Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:04:00Z",
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
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
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
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6552ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6552\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, and the Federal Deposit Insurance Corporation to study how partnerships between fintechs and banking organizations can support new banking organization formation and community bank health, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bank-Fintech Partnership Enhancement Act .\n#### 2. Study on bank-fintech partnerships\n##### (a) Study\nThe Board of Governors of the Federal Reserve System, the Comptroller of the Currency, and the Federal Deposit Insurance Corporation shall carry out a study of\u2014\n**(1)**\nhow partnerships between banking organizations, on the one hand, and financial technology companies, on the other hand, can support formation of new banking organizations and community bank health, including the extent to which these partnerships reduce time to market for products and services, lower compliance burdens, boost customer acquisition, improve technological capabilities, and provide access to more diverse funding sources; and\n**(2)**\nwhat changes to Federal laws governing banking organizations, or to rules or guidance adopted by the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, or the Federal Deposit Insurance Corporation, may help promote effective partnerships between banking organizations, on the one hand, and financial technology companies, on the other hand.\n##### (b) Report\nNot later than 6 months after the date of enactment of this Act, the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, and the Federal Deposit Insurance Corporation shall issue a report to Congress containing all findings and determinations made in carrying out the study required under subsection (a).\n##### (c) Banking organization defined\nIn this section, the term banking organization means a depository institution holding company or an insured depository institution, as such terms are defined, respectively, under section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ).",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6552rh.xml",
      "text": "IB\nUnion Calendar No. 456\n119th CONGRESS\n2d Session\nH. R. 6552\n[Report No. 119\u2013531]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsors: Mr. Gottheimer , Mr. Sessions , Mr. Davidson , Mr. Moskowitz , Mr. Moore of North Carolina , and Mr. Lawler\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo require the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, and the Federal Deposit Insurance Corporation to study how partnerships between fintechs and banking organizations can support new banking organization formation and community bank health, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bank-Fintech Partnership Enhancement Act .\n#### 2. Study on bank-fintech partnerships\n##### (a) Study\nThe Board of Governors of the Federal Reserve System, the Comptroller of the Currency, and the Federal Deposit Insurance Corporation shall carry out a study of\u2014\n**(1)**\nthe impact of partnerships between banking organizations, on the one hand, and financial technology companies, on the other hand, on the banking sector, competition, innovation, consumer protection, and the availability of financial products and services, including the extent to which these partnerships support the formation of new banking organizations, reduce time to market for products and services, lower compliance burdens, boost customer acquisition, improve technological capabilities, and provide access to more diverse funding sources; and\n**(2)**\nwhat changes to Federal laws governing banking organizations, or to rules or guidance adopted by the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, or the Federal Deposit Insurance Corporation, may help promote effective partnerships between banking organizations, on the one hand, and financial technology companies, on the other hand.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, and the Federal Deposit Insurance Corporation shall issue a report to Congress containing all findings and determinations made in carrying out the study required under subsection (a).\n##### (c) Banking organization defined\nIn this section, the term banking organization means a depository institution holding company or an insured depository institution, as such terms are defined, respectively, under section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ).\n#### 3. Study on credit union-fintech partnerships\n##### (a) Study\nThe National Credit Union Administration shall carry out a study of\u2014\n**(1)**\nthe impact of partnerships between credit unions, on the one hand, and financial technology companies, on the other hand, on the credit union sector, competition, innovation, consumer protection, and the availability of financial products and services, including the extent to which these partnerships support the formation of new credit unions, reduce time to market for products and services, lower compliance burdens, boost customer acquisition, improve technological capabilities, and provide access to more diverse funding sources; and\n**(2)**\nwhat changes to Federal laws governing credit unions, or to rules or guidance adopted by the National Credit Union Administration, may help promote effective partnerships between credit unions, on the one hand, and financial technology companies, on the other hand.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the National Credit Union Administration shall issue a report to Congress containing all findings and determinations made in carrying out the study required under subsection (a).",
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
            "name": "Congressional oversight",
            "updateDate": "2026-01-02T17:26:32Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-01-02T17:33:51Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2026-01-02T17:17:28Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-02T17:26:39Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-02T17:17:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T18:44:53Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6552ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6552rh.xml"
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
      "title": "Bank-Fintech Partnership Enhancement Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:23:18Z"
    },
    {
      "title": "Bank-Fintech Partnership Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bank-Fintech Partnership Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, and the Federal Deposit Insurance Corporation to study how partnerships between fintechs and banking organizations can support new banking organization formation and community bank health, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T09:03:20Z"
    }
  ]
}
```
