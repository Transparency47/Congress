# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/677?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/677
- Title: Border Airport Fairness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 677
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-12-05T21:46:55Z
- Update date including text: 2025-12-05T21:46:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/677",
    "number": "677",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Border Airport Fairness Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:46:55Z",
    "updateDateIncludingText": "2025-12-05T21:46:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T23:27:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "NY"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "TX"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s677is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 677\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Cruz (for himself, Mrs. Gillibrand , Mr. Cornyn , and Mr. Schumer ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the designation of certain airports as ports of entry.\n#### 1. Short title\nThis Act may be cited as the Border Airport Fairness Act of 2025 .\n#### 2. Designation of certain airports as ports of entry\n##### (a) In general\nThe President shall\u2014\n**(1)**\npursuant to the Act of August 1, 1914 (38 Stat. 623, chapter 223; 19 U.S.C. 2 ), designate each airport described in subsection (b) as a port of entry; and\n**(2)**\nterminate the application of the user fee requirement under section 236 of the Trade and Tariff Act of 1984 ( 19 U.S.C. 58b ) with respect to the airport.\n##### (b) Airports described\nAn airport described in this subsection is an airport that\u2014\n**(1)**\nis a primary airport (as defined in section 47102 of title 49, United States Code);\n**(2)**\nis located not more than 30 miles from the northern or southern international land border of the United States;\n**(3)**\nis associated, through a formal, legal instrument, including a valid contract or governmental ordinance, with a land border crossing or a seaport not more than 30 miles from the airport; and\n**(4)**\nthrough such association, meets the numerical criteria considered by U.S. Customs and Border Protection for establishing a port of entry, as set forth in\u2014\n**(A)**\nTreasury Decision 82\u201337 (47 Fed. Reg. 10137; relating to revision of customs criteria for establishing ports of entry and stations), as revised by Treasury Decisions 86\u201314 (51 Fed. Reg. 4559) and 87\u201365 (52 Fed. Reg. 16328); or\n**(B)**\nany successor guidance or regulation.",
      "versionDate": "2025-02-20",
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
        "actionDate": "2025-04-17",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2962",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Border Airport Fairness Act of 2025",
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
            "name": "Aviation and airports",
            "updateDate": "2025-07-10T17:35:03Z"
          },
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-07-10T17:35:03Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-07-10T17:35:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-12T22:56:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s677",
          "measure-number": "677",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s677v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Border Airport Fairness Act of </strong><strong>2025</strong></p><p>This bill requires the President to designate certain primary airports near the border as ports of entry and terminate the user fee requirement for customs services at these airports.</p>"
        },
        "title": "Border Airport Fairness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s677.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Border Airport Fairness Act of </strong><strong>2025</strong></p><p>This bill requires the President to designate certain primary airports near the border as ports of entry and terminate the user fee requirement for customs services at these airports.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s677"
    },
    "title": "Border Airport Fairness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Border Airport Fairness Act of </strong><strong>2025</strong></p><p>This bill requires the President to designate certain primary airports near the border as ports of entry and terminate the user fee requirement for customs services at these airports.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s677"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s677is.xml"
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
      "title": "Border Airport Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Border Airport Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the designation of certain airports as ports of entry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:42Z"
    }
  ]
}
```
