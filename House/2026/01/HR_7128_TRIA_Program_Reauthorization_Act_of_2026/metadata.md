# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7128?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7128
- Title: TRIA Program Reauthorization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7128
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-05-21T20:22:52Z
- Update date including text: 2026-05-21T20:22:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-01-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 2.
- 2026-03-19 - Calendars: Placed on the Union Calendar, Calendar No. 482.
- 2026-03-19 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-561.
- 2026-03-19 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-561.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-01-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 2.
- 2026-03-19 - Calendars: Placed on the Union Calendar, Calendar No. 482.
- 2026-03-19 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-561.
- 2026-03-19 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-561.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7128",
    "number": "7128",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "TRIA Program Reauthorization Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T20:22:52Z",
    "updateDateIncludingText": "2026-05-21T20:22:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-03-19",
      "calendarNumber": {
        "calendar": "U00482"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 482.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-03-19",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-561.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-03-19",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-561.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-16",
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
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
            "date": "2026-03-19T16:37:41Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-22T17:46:53Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-16T20:02:05Z",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "MO"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7128ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7128\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Flood (for himself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo extend the Terrorism Risk Insurance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the TRIA Program Reauthorization Act of 2026 .\n#### 2. Extension\nSection 108(a) of the Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note) is amended by striking 2027 and inserting 2034 .\n#### 3. Improvements to certification process\nSection 102(1) of the Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nin clause (i), by striking or at the end;\n**(B)**\nin clause (ii), by striking $5,000,000. and inserting $25,000,000; or ; and\n**(C)**\nby adding at the end the following:\n(iii) the Secretary did not certify such act as an act of terrorism before the expiration of the 90-day period following the publication of a notice in the Federal Register under subparagraph (D)(i). ; and\n**(2)**\nby striking subparagraph (D) and inserting the following:\n(D) Notice requirements (i) In general The Secretary shall, not later than 30 days after beginning the process of determining whether to certify an act as an act of terrorism, publish a notice in the Federal Register that informs the public that the Secretary is in the process of determining whether to certify an act as an act of terrorism. (ii) Additional notice permitted The Secretary may, as the Secretary determines appropriate, notify the public, through publication in the Federal Register, or otherwise, that an act is not being evaluated by the Secretary to determine whether it should be certified as an act of terrorism. .\n#### 5. Technical amendments\n##### (a) In general\nSection 103(e)(7)(E)(i) of the Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note) is amended\u2014\n**(1)**\nin subclause (I)\u2014\n**(A)**\nby striking 2022 and inserting 2029 ; and\n**(B)**\nby striking 2024 and inserting 2031 ;\n**(2)**\nin subclause (II)\u2014\n**(A)**\nby striking 2023 and inserting 2030 ;\n**(B)**\nby striking 2029 and inserting 2036 ; and\n**(C)**\nby striking 2024 and inserting 2031 ; and\n**(3)**\nin subclause (III)\u2014\n**(A)**\nby striking 2029 and inserting 2036 ; and\n**(B)**\nby striking 2024 and inserting 2031 .\n##### (b) Clarification\nThe Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note) is amended by striking Terrorism Insurance Program each place it appears and inserting Terrorism Risk Insurance Program .",
      "versionDate": "2026-01-16",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7128rh.xml",
      "text": "IB\nUnion Calendar No. 482\n119th CONGRESS\n2d Session\nH. R. 7128\n[Report No. 119\u2013561]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Flood (for himself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Financial Services\nMarch 19, 2026 Additional sponsors: Mr. Cleaver , Ms. Vel\u00e1zquez , and Ms. Pressley\nMarch 19, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on January 16, 2026\nA BILL\nTo extend the Terrorism Risk Insurance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the TRIA Program Reauthorization Act of 2026 .\n#### 2. Extension\nSection 108(a) of the Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note) is amended by striking 2027 and inserting 2034 .\n#### 3. Improvements to certification process\nSection 102(1) of the Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nin clause (i), by striking or at the end;\n**(B)**\nin clause (ii), by striking exceed $5,000,000. and inserting:\nexceed\u2014 (I) with respect to an act that occurred in a year before 2029, $5,000,000; and (II) with respect to an act that occurred in 2029, or any year thereafter, $10,000,000; or ; and\n**(C)**\nby adding at the end the following:\n(iii) the Secretary did not certify such act as an act of terrorism before the expiration of the 90-day period following the publication of a notice in the Federal Register under subparagraph (D)(i). ; and\n**(2)**\nby striking subparagraph (D) and inserting the following:\n(D) Notice requirements (i) In general The Secretary shall, not later than 30 days after beginning the process of determining whether to certify an act as an act of terrorism, publish a notice in the Federal Register that informs the public that the Secretary is in the process of determining whether to certify the act as an act of terrorism. (ii) Additional notice permitted The Secretary may, as the Secretary determines appropriate, notify the public, through publication in the Federal Register, or otherwise, that an act is not being evaluated by the Secretary to determine whether it should be certified as an act of terrorism. .\n#### 4. Technical amendments\n##### (a) In general\nSection 103(e)(7)(E)(i) of the Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note) is amended\u2014\n**(1)**\nin subclause (I)\u2014\n**(A)**\nby striking 2022 and inserting 2029 ; and\n**(B)**\nby striking 2024 and inserting 2031 ;\n**(2)**\nin subclause (II)\u2014\n**(A)**\nby striking 2023 and inserting 2030 ;\n**(B)**\nby striking 2029 and inserting 2036 ; and\n**(C)**\nby striking 2024 and inserting 2031 ; and\n**(3)**\nin subclause (III)\u2014\n**(A)**\nby striking 2029 and inserting 2036 ; and\n**(B)**\nby striking 2024 and inserting 2031 .\n##### (b) Technical correction\nThe Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note) is amended by striking Terrorism Insurance Program each place it appears in text or headings and inserting Terrorism Risk Insurance Program .",
      "versionDate": "2026-03-19",
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
        "actionDate": "2026-04-27",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "4395",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Terrorism Risk Insurance Program Reauthorization Act of 2026",
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
            "name": "Disaster relief and insurance",
            "updateDate": "2026-01-27T20:44:55Z"
          },
          {
            "name": "Insurance industry and regulation",
            "updateDate": "2026-01-27T17:26:44Z"
          },
          {
            "name": "Life, casualty, property insurance",
            "updateDate": "2026-01-27T20:45:03Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-01-27T20:45:10Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2026-01-27T17:26:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-24T17:19:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-19",
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
          "measure-id": "id119hr7128",
          "measure-number": "7128",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-19",
          "originChamber": "HOUSE",
          "update-date": "2026-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7128v07",
            "update-date": "2026-04-17"
          },
          "action-date": "2026-03-19",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>TRIA Program Reauthorization Act of 2026</strong></p><p>This bill reauthorizes the Terrorism Risk Insurance Program through 2034. The program covers a portion of the losses incurred by private insurers for property and casualty insurance coverage for terrorism risk.</p><p>The bill also increases the amount of property and casualty insurance losses required for certification under the program beginning in 2029 and provides statutory authority for Department of the Treasury public notification requirements regarding the determination process for whether an act qualifies as an act of terrorism under this program.</p>"
        },
        "title": "TRIA Program Reauthorization Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7128.xml",
    "summary": {
      "actionDate": "2026-03-19",
      "actionDesc": "Reported to House",
      "text": "<p><strong>TRIA Program Reauthorization Act of 2026</strong></p><p>This bill reauthorizes the Terrorism Risk Insurance Program through 2034. The program covers a portion of the losses incurred by private insurers for property and casualty insurance coverage for terrorism risk.</p><p>The bill also increases the amount of property and casualty insurance losses required for certification under the program beginning in 2029 and provides statutory authority for Department of the Treasury public notification requirements regarding the determination process for whether an act qualifies as an act of terrorism under this program.</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119hr7128"
    },
    "title": "TRIA Program Reauthorization Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-19",
      "actionDesc": "Reported to House",
      "text": "<p><strong>TRIA Program Reauthorization Act of 2026</strong></p><p>This bill reauthorizes the Terrorism Risk Insurance Program through 2034. The program covers a portion of the losses incurred by private insurers for property and casualty insurance coverage for terrorism risk.</p><p>The bill also increases the amount of property and casualty insurance losses required for certification under the program beginning in 2029 and provides statutory authority for Department of the Treasury public notification requirements regarding the determination process for whether an act qualifies as an act of terrorism under this program.</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119hr7128"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7128ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7128rh.xml"
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
      "title": "TRIA Program Reauthorization Act of 2026",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "title": "TRIA Program Reauthorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRIA Program Reauthorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To extend the Terrorism Risk Insurance Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T09:18:22Z"
    }
  ]
}
```
