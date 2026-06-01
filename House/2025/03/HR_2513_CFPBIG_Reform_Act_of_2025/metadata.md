# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2513?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2513
- Title: CFPB–IG Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2513
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-02-17T17:17:29Z
- Update date including text: 2026-02-17T17:17:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2513",
    "number": "2513",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "CFPB\u2013IG Reform Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-17T17:17:29Z",
    "updateDateIncludingText": "2026-02-17T17:17:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
        "item": {
          "date": "2025-03-31T16:07:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-31T16:07:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "KY"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2513ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2513\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Meuser (for himself, Mr. Huizenga , Mr. Barr , Mr. Williams of Texas , Mrs. Kim , Mr. Donalds , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require Senate confirmation of Inspector General of the Bureau of Consumer Financial Protection, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bureau of Consumer Financial Protection-Inspector General Reform Act of 2025 or the CFPB\u2013IG Reform Act of 2025 .\n#### 2. Appointment of Inspector General\nChapter 4 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 401\u2014\n**(A)**\nin paragraph (1), by inserting the Bureau of Consumer Financial Protection, after the Export-Import Bank of the United States, ; and\n**(B)**\nin paragraph (3), by inserting the Director of the Bureau of Consumer Financial Protection; after the President of the Export-Import Bank of the United States; ; and\n**(2)**\nin section 415\u2014\n**(A)**\nin subsection (a)(1), by striking and the Bureau of Consumer Financial Protection ;\n**(B)**\nin subsection (c), by striking For purposes of implementing this section, the Chairman of the Board of Governors of the Federal Reserve System shall appoint the Inspector General of the Board of Governors of the Federal Reserve System and the Bureau of Consumer Financial Protection. The Inspector General of the Board of Governors of the Federal Reserve System and the Bureau of Consumer Financial Protection shall have all of the authorities and responsibilities provided by this Act with respect to the Bureau of Consumer Financial Protection, as if the Bureau were part of the Board of Governors of the Federal Reserve System. ; and\n**(C)**\nin subsection (g)(3), by striking and the Bureau of Consumer Financial Protection .\n#### 3. Requirements for the Inspector General for the Bureau of Consumer Financial Protection\n##### (a) Establishment\nSection 1011 of the Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5491 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by striking and Deputy Director and inserting , Deputy Director, and Inspector General ; and\n**(B)**\nby inserting after paragraph (5) the following:\n(6) Inspector General There is established the position of the Inspector General. ; and\n**(2)**\nin subsection (d), by striking or Deputy Director each place it appears and inserting , Deputy Director, or Inspector General .\n##### (b) Hearings\nSection 1016 of such Act is amended by inserting after subsection (c) the following:\n(d) Additional Requirement for Inspector General On a separate occasion from that described in subsection (a), the Inspector General of the Bureau shall appear, upon invitation, before the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services and the Committee on Energy and Commerce of the House of Representatives at semiannual hearings regarding the reports required under subsection (b) and the reports required under section 405 of title 5, United States Code. .\n##### (c) Funding for Office of Inspector General\nSection 1017(a)(2) of such Act is amended\u2014\n**(1)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(2)**\nby inserting after subparagraph (B) the following:\n(C) Funding for Office of Inspector General Each fiscal year, the Bureau shall dedicate 2 percent of the funds transferred pursuant to paragraph (1) to the Office of the Inspector General. .\n##### (d) Participation in the Council of Inspectors General on Financial Oversight\nSection 989E(a)(1) of such Act is amended by adding at the end the following:\n(J) The Bureau of Consumer Financial Protection. .\n##### (e) Deadline for appointment\nNot later than 60 days after the date of the enactment of this Act, the President shall appoint an Inspector General for the Bureau of Consumer Financial Protection in accordance with section 403 of title 5, United States Code.\n#### 4. Effective date\n##### (a) In general\nThe amendments made by this Act shall take effect on the date on which the first Inspector General of the Bureau of Consumer Financial Protection is confirmed by the Senate.\n##### (b) Appointment\nThe President may appoint, and the Senate may confirm, an Inspector General of the Bureau of Consumer Financial Protection before the amendments made by this Act take effect.\n##### (c) Transition\nThe Inspector General of the Board of Governors of the Federal Reserve System and the Bureau of Consumer Financial Protection shall, upon the date on which the first Inspector General of the Bureau of Consumer Financial Protection is confirmed by the Senate, become the Inspector General of the Board of Governors of the Federal Reserve System.",
      "versionDate": "2025-03-31",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-04-07T12:51:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119hr2513",
          "measure-number": "2513",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2026-02-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2513v00",
            "update-date": "2026-02-17"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bureau of Consumer Financial Protection-Inspector General Reform Act of 2025 or the CFPB-IG Act of 2025</strong></p><p>This bill establishes a separate Office of Inspector General for the Consumer Financial Protection Bureau (CFPB). Currently, such oversight of the CFPB is combined with the Office of Inspector General for the Board of Governors of the Federal Reserve System.</p>"
        },
        "title": "CFPB\u2013IG Reform Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2513.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bureau of Consumer Financial Protection-Inspector General Reform Act of 2025 or the CFPB-IG Act of 2025</strong></p><p>This bill establishes a separate Office of Inspector General for the Consumer Financial Protection Bureau (CFPB). Currently, such oversight of the CFPB is combined with the Office of Inspector General for the Board of Governors of the Federal Reserve System.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr2513"
    },
    "title": "CFPB\u2013IG Reform Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bureau of Consumer Financial Protection-Inspector General Reform Act of 2025 or the CFPB-IG Act of 2025</strong></p><p>This bill establishes a separate Office of Inspector General for the Consumer Financial Protection Bureau (CFPB). Currently, such oversight of the CFPB is combined with the Office of Inspector General for the Board of Governors of the Federal Reserve System.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr2513"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2513ih.xml"
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
      "title": "CFPB\u2013IG Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CFPB\u2013IG Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bureau of Consumer Financial Protection-Inspector General Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require Senate confirmation of Inspector General of the Bureau of Consumer Financial Protection, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:34Z"
    }
  ]
}
```
