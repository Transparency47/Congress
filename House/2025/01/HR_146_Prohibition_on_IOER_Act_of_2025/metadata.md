# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/146?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/146
- Title: Prohibition on IOER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 146
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-09-05T14:43:15Z
- Update date including text: 2025-09-05T14:43:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/146",
    "number": "146",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Prohibition on IOER Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-05T14:43:15Z",
    "updateDateIncludingText": "2025-09-05T14:43:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:12:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr146ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 146\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Davidson introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Federal Reserve Act to prohibit Federal reserve banks from paying interest on excess reserves.\n#### 1. Short title\nThis Act may be cited as the Prohibition on IOER Act of 2025 .\n#### 2. Prohibition on payment of earnings on surplus reserves\nSection 19(b)(12) of the Federal Reserve Act ( 12 U.S.C. 461(b)(12) ) is amended\u2014\n**(1)**\nin the heading, by inserting required reserve before balances ;\n**(2)**\nin subparagraph (A), by inserting after Balances the following: of reserves required to be maintained by a depository institution under paragraph (2) that are ;\n**(3)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(4)**\nby inserting after subparagraph (B) the following:\n(C) Prohibition on other earnings A Federal reserve bank may not pay earnings on balances maintained at a Federal reserve bank by or on behalf of a depository institution except as provided under this paragraph. .",
      "versionDate": "2025-01-03",
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-09-05T14:42:35Z"
          },
          {
            "name": "Federal Reserve System",
            "updateDate": "2025-09-05T14:42:44Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-09-05T14:43:15Z"
          },
          {
            "name": "Interest, dividends, interest rates",
            "updateDate": "2025-09-05T14:42:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-02-03T15:20:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr146",
          "measure-number": "146",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr146v00",
            "update-date": "2025-02-05"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Prohibition on IOER Act of 2025</strong></p><p>This bill prohibits a Federal Reserve bank from paying interest to a depository institution on reserve balances in excess of minimum requirements.\u00a0</p>"
        },
        "title": "Prohibition on IOER Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr146.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prohibition on IOER Act of 2025</strong></p><p>This bill prohibits a Federal Reserve bank from paying interest to a depository institution on reserve balances in excess of minimum requirements.\u00a0</p>",
      "updateDate": "2025-02-05",
      "versionCode": "id119hr146"
    },
    "title": "Prohibition on IOER Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prohibition on IOER Act of 2025</strong></p><p>This bill prohibits a Federal Reserve bank from paying interest to a depository institution on reserve balances in excess of minimum requirements.\u00a0</p>",
      "updateDate": "2025-02-05",
      "versionCode": "id119hr146"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr146ih.xml"
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
      "title": "Prohibition on IOER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prohibition on IOER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T10:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Reserve Act to prohibit Federal reserve banks from paying interest on excess reserves.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T10:48:26Z"
    }
  ]
}
```
