# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3230
- Title: Financial Institution Regulatory Tailoring Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 3230
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2026-01-22T20:26:16Z
- Update date including text: 2026-01-22T20:26:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.
- 2025-06-20 - Calendars: Placed on the Union Calendar, Calendar No. 132.
- 2025-06-20 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-165.
- 2025-06-20 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-165.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.
- 2025-06-20 - Calendars: Placed on the Union Calendar, Calendar No. 132.
- 2025-06-20 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-165.
- 2025-06-20 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-165.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3230",
    "number": "3230",
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
    "title": "Financial Institution Regulatory Tailoring Enhancement Act",
    "type": "HR",
    "updateDate": "2026-01-22T20:26:16Z",
    "updateDateIncludingText": "2026-01-22T20:26:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-06-20",
      "calendarNumber": {
        "calendar": "U00132"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 132.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-06-20",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-165.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-06-20",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-165.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 29 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
            "date": "2025-06-20T15:00:10Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-21T16:08:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-07T14:04:15Z",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3230ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3230\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Barr (for himself and Mr. Meuser ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo increase the asset thresholds at which financial institutions become subject to certain requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Financial Institution Regulatory Tailoring Enhancement Act .\n#### 2. Increased asset thresholds\n##### (a) Bureau Supervision\nSection 1025(a) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5515 ) is amended by striking $10,000,000,000 each place it occurs and inserting $50,000,000,000 .\n##### (b) Volker rule requirements\nSection 13(h)(1)(B)(i) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1851(h)(1)(B)(i) ) is amended by striking $10,000,000,000 and inserting $50,000,000,000 .\n##### (c) Qualified mortgage requirements\nSection 129C(b)(F)(i) of the Truth in Lending Act ( 15 U.S.C. 1639c(b)(F)(i) ) is amended by striking $10,000,000,000 and inserting $50,000,000,000 .\n##### (d) Leverage and risk-Based capital requirements\nSection 201(a)(3)(A) of the Economic Growth, Regulatory Relief, and Consumer Protection Act ( 12 U.S.C. 5371 note (a)(3)(A)) is amended by striking $10,000,000,000 and inserting $50,000,000,000 .",
      "versionDate": "2025-05-07",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3230rh.xml",
      "text": "IB\nUnion Calendar No. 132\n119th CONGRESS\n1st Session\nH. R. 3230\n[Report No. 119\u2013165]\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Barr (for himself and Mr. Meuser ) introduced the following bill; which was referred to the Committee on Financial Services\nJune 20, 2025 Additional sponsor: Mr. Sessions\nJune 20, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on May 7, 2025\nA BILL\nTo increase the asset thresholds at which financial institutions become subject to certain requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Financial Institution Regulatory Tailoring Enhancement Act .\n#### 2. Increased asset thresholds\n##### (a) Bureau supervision\nThe Consumer Financial Protection Act of 2010 is amended\u2014\n**(1)**\nin section 1025(a) ( 12 U.S.C. 5515(a) ), by striking $10,000,000,000 each place it occurs and inserting $50,000,000,000 ; and\n**(2)**\nin section 1026(a) ( 12 U.S.C. 5516(a) ), by striking $10,000,000,000 each place it occurs and inserting $50,000,000,000 .\n##### (b) Volker rule requirements\nSection 13(h)(1)(B)(i) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1851(h)(1)(B)(i) ) is amended by striking $10,000,000,000 and inserting $50,000,000,000 .\n##### (c) Qualified mortgage requirements\nSection 129C(b)(2)(F)(i) of the Truth in Lending Act ( 15 U.S.C. 1639c(b)(2)(F)(i) ) is amended by striking $10,000,000,000 and inserting $50,000,000,000 .\n##### (d) Leverage and risk-based capital requirements\nSection 201(a)(3)(A) of the Economic Growth, Regulatory Relief, and Consumer Protection Act ( 12 U.S.C. 5371 note) is amended by striking $10,000,000,000 and inserting $50,000,000,000 .",
      "versionDate": "2025-06-20",
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-05-29T14:30:55Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-05-29T14:30:47Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-05-29T14:36:07Z"
          },
          {
            "name": "Housing finance and home ownership",
            "updateDate": "2025-05-29T14:36:28Z"
          },
          {
            "name": "Securities",
            "updateDate": "2025-05-29T14:35:56Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-05-29T14:31:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-21T11:53:26Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3230ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3230rh.xml"
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
      "title": "Financial Institution Regulatory Tailoring Enhancement Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-06-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase the asset thresholds at which financial institutions become subject to certain requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:20Z"
    },
    {
      "title": "Financial Institution Regulatory Tailoring Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Financial Institution Regulatory Tailoring Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:24Z"
    }
  ]
}
```
