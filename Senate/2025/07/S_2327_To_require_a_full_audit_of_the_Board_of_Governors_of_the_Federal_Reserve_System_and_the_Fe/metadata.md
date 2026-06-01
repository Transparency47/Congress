# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2327?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2327
- Title: Federal Reserve Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2327
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-04-06T16:44:47Z
- Update date including text: 2026-04-06T16:44:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-12-11 - Committee: Committee on Homeland Security and Governmental Affairs. Hearings held.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-12-11 - Committee: Committee on Homeland Security and Governmental Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2327",
    "number": "2327",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Federal Reserve Transparency Act of 2025",
    "type": "S",
    "updateDate": "2026-04-06T16:44:47Z",
    "updateDateIncludingText": "2026-04-06T16:44:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-12-11T17:42:21Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-17T17:19:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "TN"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "ID"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "IN"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2327is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2327\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Paul (for himself, Mr. Scott of Florida , Mrs. Blackburn , Mr. Risch , Mr. Cruz , Mr. Young , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require a full audit of the Board of Governors of the Federal Reserve System and the Federal reserve banks by the Comptroller General of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Reserve Transparency Act of 2025 .\n#### 2. Audit reform and transparency for the Board of Governors of the Federal Reserve System\n##### (a) In general\nNotwithstanding section 714 of title 31, United States Code, or any other provision of law, the Comptroller General of the United States shall complete an audit of the Board of Governors of the Federal Reserve System and the Federal reserve banks under subsection (b) of that section not later than 12 months after the date of enactment of this Act.\n##### (b) Report\n**(1) In general**\nNot later than 90 days after the date on which the audit required pursuant to subsection (a) is completed, the Comptroller General of the United States\u2014\n**(A)**\nshall submit to Congress a report on the audit; and\n**(B)**\nshall make the report described in subparagraph (A) available to the Speaker of the House, the majority and minority leaders of the House of Representatives, the majority and minority leaders of the Senate, the Chair and Ranking Member of the committee and each subcommittee of jurisdiction in the House of Representatives and the Senate, and any other Member of Congress who requests the report.\n**(2) Contents**\nThe report required under paragraph (1) shall include a detailed description of the findings and conclusion of the Comptroller General of the United States with respect to the audit that is the subject of the report, together with such recommendations for legislative or administrative action as the Comptroller General of the United States may determine to be appropriate.\n##### (c) Repeal of certain limitations\nSubsection (b) of section 714 of title 31, United States Code, is amended by striking the second sentence.\n##### (d) Technical and conforming amendments\n**(1) In general**\nSection 714 of title 31, United States Code, is amended\u2014\n**(A)**\nin subsection (d)(3), by striking or (f) each place the term appears;\n**(B)**\nin subsection (e), by striking the third undesignated paragraph of section 13 and inserting section 13(3) ; and\n**(C)**\nby striking subsection (f).\n**(2) Federal Reserve Act**\nSubsection (s) (relating to Federal Reserve Transparency and Release of Information ) of section 11 of the Federal Reserve Act ( 12 U.S.C. 248 ) is amended\u2014\n**(A)**\nin paragraph (4)(A), by striking has the same meaning as in section 714(f)(1)(A) of title 31, United States Code and inserting means a program or facility, including any special purpose vehicle or other entity established by or on behalf of the Board of Governors of the Federal Reserve System or a Federal reserve bank, authorized by the Board of Governors under section 13(3), that is not subject to audit under section 714(e) of title 31, United States Code ;\n**(B)**\nin paragraph (6), by striking or in section 714(f)(3)(C) of title 31, United States Code, the information described in paragraph (1) and information concerning the transactions described in section 714(f) of such title, and inserting the information described in paragraph (1) ; and\n**(C)**\nin paragraph (7), by striking and section 13(3)(C), section 714(f)(3)(C) of title 31, United States Code, and and inserting , section 13(3)(C), and .",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "24",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Federal Reserve Transparency Act of 2025",
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
            "name": "Accounting and auditing",
            "updateDate": "2026-01-05T17:42:21Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-01-05T17:42:21Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-05T17:42:21Z"
          },
          {
            "name": "Federal Reserve System",
            "updateDate": "2026-01-05T17:42:21Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-05T17:42:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-05T15:49:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-17",
    "originChamber": "Senate",
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
          "measure-id": "id119s2327",
          "measure-number": "2327",
          "measure-type": "s",
          "orig-publish-date": "2025-07-17",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2327v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-07-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Federal Reserve Transparency Act of 2025</strong></p><p>This bill directs the Government Accountability Office (GAO) to complete an audit of the Federal Reserve Board and Federal Reserve banks not later than 12 months after enactment. In addition, the bill allows the GAO to audit the Federal Reserve Board and Federal Reserve banks with respect to (1) international financial transactions; (2) deliberations, decisions,\u00a0or actions on monetary policy matters; (3) transactions made under the direction of the Federal Open Market Committee; and (4) discussions or communications among Federal Reserve officers, board members, and employees regarding any of these matters.\u00a0</p>"
        },
        "title": "Federal Reserve Transparency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2327.xml",
    "summary": {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Federal Reserve Transparency Act of 2025</strong></p><p>This bill directs the Government Accountability Office (GAO) to complete an audit of the Federal Reserve Board and Federal Reserve banks not later than 12 months after enactment. In addition, the bill allows the GAO to audit the Federal Reserve Board and Federal Reserve banks with respect to (1) international financial transactions; (2) deliberations, decisions,\u00a0or actions on monetary policy matters; (3) transactions made under the direction of the Federal Open Market Committee; and (4) discussions or communications among Federal Reserve officers, board members, and employees regarding any of these matters.\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2327"
    },
    "title": "Federal Reserve Transparency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Federal Reserve Transparency Act of 2025</strong></p><p>This bill directs the Government Accountability Office (GAO) to complete an audit of the Federal Reserve Board and Federal Reserve banks not later than 12 months after enactment. In addition, the bill allows the GAO to audit the Federal Reserve Board and Federal Reserve banks with respect to (1) international financial transactions; (2) deliberations, decisions,\u00a0or actions on monetary policy matters; (3) transactions made under the direction of the Federal Open Market Committee; and (4) discussions or communications among Federal Reserve officers, board members, and employees regarding any of these matters.\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2327"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2327is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Federal Reserve Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Reserve Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a full audit of the Board of Governors of the Federal Reserve System and the Federal reserve banks by the Comptroller General of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:22Z"
    }
  ]
}
```
