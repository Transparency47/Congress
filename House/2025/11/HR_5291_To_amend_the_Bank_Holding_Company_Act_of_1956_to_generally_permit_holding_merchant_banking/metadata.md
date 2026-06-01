# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5291?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5291
- Title: Merchant Banking Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 5291
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-09-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-16 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 35 - 17.
- 2025-11-04 - Calendars: Placed on the Union Calendar, Calendar No. 320.
- 2025-11-04 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-368.
- 2025-11-04 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-368.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-09-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-16 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 35 - 17.
- 2025-11-04 - Calendars: Placed on the Union Calendar, Calendar No. 320.
- 2025-11-04 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-368.
- 2025-11-04 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-368.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5291",
    "number": "5291",
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
    "title": "Merchant Banking Modernization Act",
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
      "actionDate": "2025-11-04",
      "calendarNumber": {
        "calendar": "U00320"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 320.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-11-04",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-368.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-11-04",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-368.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-16",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 35 - 17.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
            "date": "2025-11-04T18:49:15Z",
            "name": "Reported By"
          },
          {
            "date": "2025-09-16T14:41:55Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-10T14:06:15Z",
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
      "sponsorshipDate": "2025-09-15",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5291ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5291\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Williams of Texas introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Bank Holding Company Act of 1956 to generally permit holding merchant banking investments of up to 15 years.\n#### 1. Short title\nThis Act may be cited as the Merchant Banking Modernization Act .\n#### 2. Merchant banking activities\nSection 4(k)(7)(A) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843(k)(7)(A) ) is amended by inserting Under such regulations, the period of time generally permitted for holding merchant banking investments shall not be less than 15 years. For any merchant banking investment held on the date of enactment of the Merchant Banking Modernization Act , the holding period of time permitted shall not be less than 15 years from the initial date of the investment. after the period at the end.",
      "versionDate": "2025-09-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5291rh.xml",
      "text": "IB\nUnion Calendar No. 320\n119th CONGRESS\n1st Session\nH. R. 5291\n[Report No. 119\u2013368]\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Williams of Texas introduced the following bill; which was referred to the Committee on Financial Services\nNovember 4, 2025 Additional sponsor: Mr. Gottheimer\nNovember 4, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on September 10, 2025\nA BILL\nTo amend the Bank Holding Company Act of 1956 to generally permit holding merchant banking investments of up to 15 years.\n#### 1. Short title\nThis Act may be cited as the Merchant Banking Modernization Act .\n#### 2. Merchant banking investment holding period\nSection 4(k)(7)(A) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843(k)(7)(A) ) is amended by inserting Under such regulations, the period of time generally permitted for holding merchant banking investments shall not be less than 15 years. For any merchant banking investment held on the date of enactment of the Merchant Banking Modernization Act , the holding period of time permitted shall not be less than 15 years from the initial date of the investment. after the period at the end.",
      "versionDate": "2025-11-04",
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-01",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2663",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Merchant Banking Modernization Act",
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
            "updateDate": "2025-09-25T15:04:36Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-09-25T15:04:29Z"
          },
          {
            "name": "Business investment and capital",
            "updateDate": "2025-09-25T15:04:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-18T19:59:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-04",
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
          "measure-id": "id119hr5291",
          "measure-number": "5291",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-04",
          "originChamber": "HOUSE",
          "update-date": "2025-12-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5291v07",
            "update-date": "2025-12-05"
          },
          "action-date": "2025-11-04",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Merchant Banking Modernization Act</strong></p><p>This bill requires financial holding companies to be allowed to hold merchant banking investments\u00a0for a minimum of 15 years.</p><p>Currently, financial holding companies are generally prohibited from holding interests in nonfinancial companies, however, there are statutory exemptions for merchant banking activities\u2014financial services for private commercial entities. As a result of these financial services, the financial holding company may gain equity in these private commercial entities through portfolio holdings. Under current regulations, these holdings are subject to certain limitations, including a holding limit of 10 years, with the option of extending the period subject to review by the Federal Reserve Board.</p>"
        },
        "title": "Merchant Banking Modernization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5291.xml",
    "summary": {
      "actionDate": "2025-11-04",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Merchant Banking Modernization Act</strong></p><p>This bill requires financial holding companies to be allowed to hold merchant banking investments\u00a0for a minimum of 15 years.</p><p>Currently, financial holding companies are generally prohibited from holding interests in nonfinancial companies, however, there are statutory exemptions for merchant banking activities\u2014financial services for private commercial entities. As a result of these financial services, the financial holding company may gain equity in these private commercial entities through portfolio holdings. Under current regulations, these holdings are subject to certain limitations, including a holding limit of 10 years, with the option of extending the period subject to review by the Federal Reserve Board.</p>",
      "updateDate": "2025-12-05",
      "versionCode": "id119hr5291"
    },
    "title": "Merchant Banking Modernization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-04",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Merchant Banking Modernization Act</strong></p><p>This bill requires financial holding companies to be allowed to hold merchant banking investments\u00a0for a minimum of 15 years.</p><p>Currently, financial holding companies are generally prohibited from holding interests in nonfinancial companies, however, there are statutory exemptions for merchant banking activities\u2014financial services for private commercial entities. As a result of these financial services, the financial holding company may gain equity in these private commercial entities through portfolio holdings. Under current regulations, these holdings are subject to certain limitations, including a holding limit of 10 years, with the option of extending the period subject to review by the Federal Reserve Board.</p>",
      "updateDate": "2025-12-05",
      "versionCode": "id119hr5291"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5291ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5291rh.xml"
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
      "title": "Merchant Banking Modernization Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-11-05T03:53:12Z"
    },
    {
      "title": "Merchant Banking Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Merchant Banking Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Bank Holding Company Act of 1956 to generally permit holding merchant banking investments of up to 15 years.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T07:33:22Z"
    }
  ]
}
```
