# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3446?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3446
- Title: FDIC Board Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 3446
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported by the Yeas and Nays: 26 - 23.
- 2025-09-08 - Calendars: Placed on the Union Calendar, Calendar No. 201.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-244.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-244.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported by the Yeas and Nays: 26 - 23.
- 2025-09-08 - Calendars: Placed on the Union Calendar, Calendar No. 201.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-244.
- 2025-09-08 - Committee: Reported by the Committee on Financial Services. H. Rept. 119-244.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3446",
    "number": "3446",
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
    "title": "FDIC Board Accountability Act",
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
      "actionDate": "2025-09-08",
      "calendarNumber": {
        "calendar": "U00201"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 201.",
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
      "text": "Reported by the Committee on Financial Services. H. Rept. 119-244.",
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
      "text": "Reported by the Committee on Financial Services. H. Rept. 119-244.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
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
      "text": "Ordered to be Reported by the Yeas and Nays: 26 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
            "date": "2025-09-08T16:53:22Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-23T16:58:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-22T16:57:49Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-15T14:05:20Z",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "KY"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3446ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3446\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Huizenga (for himself, Mr. Barr , Mr. Meuser , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Federal Deposit Insurance Act to revise the membership requirements for the Board of Directors of the Federal Deposit Insurance Corporation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FDIC Board Accountability Act .\n#### 2. FDIC Board of Directors\nSection 2 of the Federal Deposit Insurance Act ( 12 U.S.C. 1812 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by adding and at the end; and\n**(ii)**\nby striking subparagraphs (B) and (C) and inserting the following:\n(B) 4 of whom shall be appointed by the President, by and with the advice and consent of the Senate, from among individuals who are citizens of the United States, 1 of whom shall have State bank supervisory experience, and separately 1 of whom shall have demonstrated primary experience working in or supervising depository institutions having less than $10,000,000,000 in total assets. ; and\n**(B)**\nby adding at the end the following:\n(3) Non-voting status of the Director of the Bureau of Consumer Financial Protection The Director of the Bureau of Consumer Financial Protection shall serve as a non-voting observer to the Board of Directors of the Corporation. ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by adding at the end the following: No individual may be appointed as a member for more than two terms. ; and\n**(B)**\nby adding at the end the following:\n(4) Maximum length of service Notwithstanding any other provision of this Act, no person shall serve as a member for more than twelve years in total. ;\n**(3)**\nin subsection (d)(2)\u2014\n**(A)**\nby striking Consumer Financial Protection Bureau each place such term appears and inserting Bureau of Consumer Financial Protection ; and\n**(B)**\nby inserting or observer, as the case may be, after member ; and\n**(4)**\nin subsection (f)(2), by striking or of the Consumer Financial Protection Bureau .",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3446rh.xml",
      "text": "IB\nUnion Calendar No. 201\n119th CONGRESS\n1st Session\nH. R. 3446\n[Report No. 119\u2013244]\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Huizenga (for himself, Mr. Barr , Mr. Meuser , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Financial Services\nSeptember 8, 2025 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo amend the Federal Deposit Insurance Act to revise the membership requirements for the Board of Directors of the Federal Deposit Insurance Corporation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FDIC Board Accountability Act .\n#### 2. FDIC Board of Directors\nSection 2 of the Federal Deposit Insurance Act ( 12 U.S.C. 1812 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by adding and at the end; and\n**(ii)**\nby striking subparagraphs (B) and (C) and inserting the following:\n(B) 4 of whom shall be appointed by the President, by and with the advice and consent of the Senate, from among individuals who are citizens of the United States, 1 of whom shall have State bank supervisory experience, and separately 1 of whom shall have demonstrated primary experience working in or supervising depository institutions having less than $10,000,000,000 in total assets. ; and\n**(B)**\nby adding at the end the following:\n(3) Non-voting status of the Director of the Bureau of Consumer Financial Protection The Director of the Bureau of Consumer Financial Protection shall serve as a non-voting observer to the Board of Directors of the Corporation. ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by adding at the end the following: No individual may be appointed as a member for more than two terms. ; and\n**(B)**\nby adding at the end the following:\n(4) Maximum length of service Notwithstanding any other provision of this Act, no person shall serve as a member for more than twelve years in total. ;\n**(3)**\nin subsection (d)(2)\u2014\n**(A)**\nby striking Consumer Financial Protection Bureau each place such term appears and inserting Bureau of Consumer Financial Protection ; and\n**(B)**\nby inserting or observer, as the case may be, after member ; and\n**(4)**\nin subsection (f)(2), by striking or of the Consumer Financial Protection Bureau .",
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
            "name": "Advisory bodies",
            "updateDate": "2025-08-26T14:29:36Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-08-26T14:32:07Z"
          },
          {
            "name": "Federal Deposit Insurance Corporation (FDIC)",
            "updateDate": "2025-08-26T14:31:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-29T15:16:46Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3446ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3446rh.xml"
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
      "title": "FDIC Board Accountability Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-09T08:08:21Z"
    },
    {
      "title": "FDIC Board Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FDIC Board Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Deposit Insurance Act to revise the membership requirements for the Board of Directors of the Federal Deposit Insurance Corporation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:33:29Z"
    }
  ]
}
```
