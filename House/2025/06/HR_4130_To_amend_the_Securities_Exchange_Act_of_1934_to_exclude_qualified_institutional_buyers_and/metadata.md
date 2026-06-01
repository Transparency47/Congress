# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4130
- Title: Small Business Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 4130
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2026-04-08T20:34:53Z
- Update date including text: 2026-04-08T20:34:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 24.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 450.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-525.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-525.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 24.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 450.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-525.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-525.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4130",
    "number": "4130",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Small Business Relief Act",
    "type": "HR",
    "updateDate": "2026-04-08T20:34:53Z",
    "updateDateIncludingText": "2026-04-08T20:34:53Z"
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
        "calendar": "U00450"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 450.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-525.",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-525.",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 24.",
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
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
            "date": "2026-02-25T18:47:35Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T20:19:43Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T20:19:35Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-25T14:02:00Z",
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
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4130ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4130\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Garbarino introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Exchange Act of 1934 to exclude qualified institutional buyers and institutional accredited investors when calculating holders of a security for purposes of the mandatory registration threshold under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Relief Act .\n#### 2. Exclusions from mandatory registration threshold\n##### (a) In general\nSection 12(g)(1) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78l(g)(1) ) is amended\u2014\n**(1)**\nin paragraph (A)(i), by inserting after persons the following: (that are not a qualified institutional buyer or an institutional accredited investor) ; and\n**(2)**\nin paragraph (B), by inserting after persons the following: (that are not a qualified institutional buyer or an institutional accredited investor) .\n##### (b) Nonapplicability of general exemptive authority\nSection 36 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78mm ) shall not apply to the matter inserted by the amendments made by subsection (a).",
      "versionDate": "2025-06-25",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr4130rh.xml",
      "text": "IB\nUnion Calendar No. 450\n119th CONGRESS\n2d Session\nH. R. 4130\n[Report No. 119\u2013525]\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Garbarino introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsor: Mr. Sessions\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on June 25, 2025\nA BILL\nTo amend the Securities Exchange Act of 1934 to exclude qualified institutional buyers and institutional accredited investors when calculating holders of a security for purposes of the mandatory registration threshold under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Relief Act .\n#### 2. Exclusions from mandatory registration threshold\nSection 12(g)(1) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78l(g)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A)(i), by inserting after persons the following: (that are not a qualified institutional buyer or an institutional accredited investor) ; and\n**(2)**\nin subparagraph (B), by inserting after persons the following: (that are not a qualified institutional buyer or an institutional accredited investor) .",
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
            "name": "Business investment and capital",
            "updateDate": "2026-01-06T17:40:17Z"
          },
          {
            "name": "Business records",
            "updateDate": "2026-01-06T17:45:04Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-01-06T17:36:27Z"
          },
          {
            "name": "Securities",
            "updateDate": "2026-01-06T17:36:45Z"
          },
          {
            "name": "Small business",
            "updateDate": "2026-01-06T17:35:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-16T13:35:49Z"
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
          "measure-id": "id119hr4130",
          "measure-number": "4130",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4130v07",
            "update-date": "2026-04-08"
          },
          "action-date": "2026-02-25",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Small Business Relief Act</strong></p><p>This bill allows issuers of securities to have institutional investors and buyers in a class of securities without needing to comply with certain Securities and Exchange Commission (SEC) registration requirements.</p><p>Currently, issuers of securities must register with and periodically report to the SEC when, among other requirements, the number of investors in a class of securities exceeds a specific cap. Under the bill, qualified institutional buyers and institutional accredited investors do not count towards this\u00a0cap.</p>"
        },
        "title": "Small Business Relief Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4130.xml",
    "summary": {
      "actionDate": "2026-02-25",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Small Business Relief Act</strong></p><p>This bill allows issuers of securities to have institutional investors and buyers in a class of securities without needing to comply with certain Securities and Exchange Commission (SEC) registration requirements.</p><p>Currently, issuers of securities must register with and periodically report to the SEC when, among other requirements, the number of investors in a class of securities exceeds a specific cap. Under the bill, qualified institutional buyers and institutional accredited investors do not count towards this\u00a0cap.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr4130"
    },
    "title": "Small Business Relief Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-25",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Small Business Relief Act</strong></p><p>This bill allows issuers of securities to have institutional investors and buyers in a class of securities without needing to comply with certain Securities and Exchange Commission (SEC) registration requirements.</p><p>Currently, issuers of securities must register with and periodically report to the SEC when, among other requirements, the number of investors in a class of securities exceeds a specific cap. Under the bill, qualified institutional buyers and institutional accredited investors do not count towards this\u00a0cap.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr4130"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4130ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr4130rh.xml"
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
      "title": "Small Business Relief Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:53:29Z"
    },
    {
      "title": "Small Business Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T07:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Exchange Act of 1934 to exclude qualified institutional buyers and institutional accredited investors when calculating holders of a security for purposes of the mandatory registration threshold under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:48Z"
    }
  ]
}
```
