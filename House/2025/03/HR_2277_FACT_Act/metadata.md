# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2277?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2277
- Title: FACT Act
- Congress: 119
- Bill type: HR
- Bill number: 2277
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-06-02T20:35:41Z
- Update date including text: 2025-06-02T20:35:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2277",
    "number": "2277",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S000250",
        "district": "17",
        "firstName": "Pete",
        "fullName": "Rep. Sessions, Pete [R-TX-17]",
        "lastName": "Sessions",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "FACT Act",
    "type": "HR",
    "updateDate": "2025-06-02T20:35:41Z",
    "updateDateIncludingText": "2025-06-02T20:35:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
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
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
            "date": "2025-03-25T15:18:21Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-21T20:01:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "KY"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "VA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MD"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2277ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2277\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Sessions (for himself, Mr. Comer , and Mr. Connolly ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend the CARES Act to extend the Pandemic Response Accountability Committee through December 31, 2026, and to change the name of such Committee to the Fraud Prevention and Accountability Committee, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Accountability Committee for Transparency Act or the FACT Act .\n#### 2. Extension and name change of Pandemic Response Accountability Committee\n##### (a) In general\nSection 15010 of the CARES Act ( Public Law 116\u2013136 ; 134 Stat. 540; 5 U.S.C. 424 note) is amended\u2014\n**(1)**\nin subsection (b), by striking Pandemic Response Accountability Committee and inserting Fraud Prevention and Accountability Committee ; and\n**(2)**\nin subsection (k), by striking September 30, 2025 and inserting December 31, 2026 .\n##### (b) Technical and conforming amendments\nSection 15010 of the CARES Act ( Public Law 116\u2013136 ; 134 Stat. 540; 5 U.S.C. 424 note), as amended by the preceding subsection, is further amended\u2014\n**(1)**\nin the heading, by striking Pandemic Response Accountability Committe and inserting Fraud Prevention and Accountability Committee ; and\n**(2)**\nby striking section 6 of the Inspector General Act of 1978 (5 U.S.C. App.) and inserting section 406 of title 5, United States Code each place such phrase appears in such section;\n**(3)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)(C), by inserting Government before Reform ;\n**(B)**\nin paragraph (4), by striking section 11 of the Inspector General Act of 1978 (5 U.S.C. App) and inserting section 424 of title 5, United States Code ; and\n**(C)**\nin paragraph (5), by striking Pandemic Response Accountability Committee and inserting Fraud Prevention and Accountability Committee ; and\n**(4)**\nin subsection (e)(3)\u2014\n**(A)**\nin subparagraph (A), by striking section 6 of the Inspector General Act of 1978 (5 U.S.C. App) and inserting section 406 of title 5, United States Code ; and\n**(B)**\nin subparagraph (B), by striking section 4(b)(1) of the Inspector General Act of 1978 (5 U.S.C. App.) inserting section 404(b)(1) of title 5, United States Code .\n##### (c) References\nAny reference to the Pandemic Response Accountability Committee in any other Federal law, Executive order, rule, regulation, or delegation of authority, or any document of or pertaining to the Pandemic Response Accountability Committee, shall be deemed to refer to the Fraud Prevention and Accountability Committee.",
      "versionDate": "2025-03-21",
      "versionType": "Introduced in House"
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
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-06-02T20:35:30Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-02T20:35:41Z"
          },
          {
            "name": "Executive Office of the President",
            "updateDate": "2025-06-02T20:35:06Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-06-02T20:35:36Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-06-02T20:35:18Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-02T20:35:12Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-06-02T20:35:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-19T15:44:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hr2277",
          "measure-number": "2277",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2025-05-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2277v00",
            "update-date": "2025-05-30"
          },
          "action-date": "2025-03-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Federal Accountability Committee for Transparency Act or the FACT Act</strong></p><p>This bill delays termination of the Pandemic Response Accountability Committee\u00a0until December 31, 2026. (This committee, part of the Council of the Inspectors General on Integrity and Efficiency, was established to\u00a0promote transparency and support oversight of the coronavirus response and\u00a0certain coronavirus-related funds.)</p><p>The bill also renames the committee as the Fraud Prevention and Accountability Committee.</p>"
        },
        "title": "FACT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2277.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Accountability Committee for Transparency Act or the FACT Act</strong></p><p>This bill delays termination of the Pandemic Response Accountability Committee\u00a0until December 31, 2026. (This committee, part of the Council of the Inspectors General on Integrity and Efficiency, was established to\u00a0promote transparency and support oversight of the coronavirus response and\u00a0certain coronavirus-related funds.)</p><p>The bill also renames the committee as the Fraud Prevention and Accountability Committee.</p>",
      "updateDate": "2025-05-30",
      "versionCode": "id119hr2277"
    },
    "title": "FACT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Accountability Committee for Transparency Act or the FACT Act</strong></p><p>This bill delays termination of the Pandemic Response Accountability Committee\u00a0until December 31, 2026. (This committee, part of the Council of the Inspectors General on Integrity and Efficiency, was established to\u00a0promote transparency and support oversight of the coronavirus response and\u00a0certain coronavirus-related funds.)</p><p>The bill also renames the committee as the Fraud Prevention and Accountability Committee.</p>",
      "updateDate": "2025-05-30",
      "versionCode": "id119hr2277"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2277ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "FACT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FACT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Accountability Committee for Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the CARES Act to extend the Pandemic Response Accountability Committee through December 31, 2026, and to change the name of such Committee to the Fraud Prevention and Accountability Committee, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T08:18:43Z"
    }
  ]
}
```
