# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3673?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3673
- Title: Small Business Investor Capital Access Act
- Congress: 119
- Bill type: HR
- Bill number: 3673
- Origin chamber: House
- Introduced date: 2025-06-03
- Update date: 2026-03-22T22:29:18Z
- Update date including text: 2026-03-22T22:29:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 2.
- 2025-09-08 - Calendars: Placed on the Union Calendar, Calendar No. 211.
- 2025-09-08 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-254.
- 2025-09-08 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-254.
- Latest action: 2025-06-03: Introduced in House

## Actions

- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 2.
- 2025-09-08 - Calendars: Placed on the Union Calendar, Calendar No. 211.
- 2025-09-08 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-254.
- 2025-09-08 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-254.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3673",
    "number": "3673",
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
    "title": "Small Business Investor Capital Access Act",
    "type": "HR",
    "updateDate": "2026-03-22T22:29:18Z",
    "updateDateIncludingText": "2026-03-22T22:29:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-09-08",
      "calendarNumber": {
        "calendar": "U00211"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 211.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-09-08",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-254.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-09-08",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-254.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 2.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
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
      "actionDate": "2025-06-03",
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
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-03",
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
            "date": "2025-09-08T17:49:11Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-22T15:44:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-03T16:03:45Z",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3673ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3673\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. Barr (for himself and Ms. Vel\u00e1zquez ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Investment Advisers Act of 1940 to increase the exemption from registration threshold for certain investment advisers of private funds to reflect the change in inflation.\n#### 1. Short title\nThis Act may be cited as the Small Business Investor Capital Access Act .\n#### 2. Inflation adjustment for the exemption threshold for certain investment advisers of private funds\nSection 203(m) of the Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20133(m) ) is amended by adding at the end the following:\n(5) Inflation adjustment The Commission shall adjust the dollar amount described under paragraph (1)\u2014 (A) upon enactment of this paragraph, to reflect the change in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor between the date of enactment of the Private Fund Investment Advisers Registration Act of 2010 and the date of enactment of this paragraph; and (B) annually thereafter, to reflect the change in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor. .",
      "versionDate": "2025-06-03",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3673rh.xml",
      "text": "IB\nUnion Calendar No. 211\n119th CONGRESS\n1st Session\nH. R. 3673\n[Report No. 119\u2013254]\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. Barr (for himself and Ms. Vel\u00e1zquez ) introduced the following bill; which was referred to the Committee on Financial Services\nSeptember 8, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on June 3, 2025\nA BILL\nTo amend the Investment Advisers Act of 1940 to increase the exemption from registration threshold for certain investment advisers of private funds to reflect the change in inflation.\n#### 1. Short title\nThis Act may be cited as the Small Business Investor Capital Access Act .\n#### 2. Inflation adjustment for the exemption threshold for certain investment advisers of private funds\nSection 203(m) of the Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20133(m) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking $150,000,000 and inserting $175,000,000 ; and\n**(2)**\nby adding at the end the following:\n(5) Inflation adjustment The Commission shall, every 5 years, adjust the dollar amount described under paragraph (1) to reflect the change in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor, and round such dollar amount to the nearest multiple of $1,000,000. .",
      "versionDate": "2025-09-08",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3880",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Small Business Investor Capital Access Act",
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-08-28T19:31:46Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-08-28T19:31:58Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-08-28T19:31:52Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-08-28T19:31:30Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-08-28T19:32:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-06-16T17:22:45Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3673ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3673rh.xml"
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
      "title": "Small Business Investor Capital Access Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-09T08:08:20Z"
    },
    {
      "title": "Small Business Investor Capital Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T07:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Investor Capital Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Investment Advisers Act of 1940 to increase the exemption from registration threshold for certain investment advisers of private funds to reflect the change in inflation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:21Z"
    }
  ]
}
```
