# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/148?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/148
- Title: Keep Your Coins Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 148
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-05-08T08:06:51Z
- Update date including text: 2026-05-08T08:06:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/148",
    "number": "148",
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
    "title": "Keep Your Coins Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:51Z",
    "updateDateIncludingText": "2026-05-08T08:06:51Z"
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
          "date": "2025-01-03T16:15:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AK"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "GA"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr148ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 148\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Davidson introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit Federal agencies from restricting the use of convertible virtual currency by a person to purchase goods or services for the person\u2019s own use, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keep Your Coins Act of 2025 .\n#### 2. Prohibition on restricting use of convertible virtual currency by a person to retain full control over convertible virtual currency\n##### (a) In general\nThe head of a Federal agency may not prohibit, restrict, or otherwise impair the ability of a covered user to\u2014\n**(1)**\nuse convertible virtual currency or its equivalent for such user\u2019s own purposes, such as to purchase real or virtual goods and services for the user\u2019s own use; or\n**(2)**\nself-custody digital assets using a self-hosted wallet or other means to conduct transactions for any lawful purpose.\n##### (b) Definitions\nIn this section:\n**(1) Convertible virtual currencies**\nThe term convertible virtual currency means a medium of exchange that\u2014\n**(A)**\nhas an equivalent value as currency (as defined in section 1010.100 of title 31, Code of Federal Regulations (or successor regulations)); or\n**(B)**\nacts as a substitute for currency but may not possess all the attributes (including legal tender status) specified under such section 1010.100 (or successor regulations).\n**(2) Covered user**\nThe term covered user means a person that obtains convertible virtual currency to purchase goods or services on that person\u2019s own behalf, without regard to the method in which such covered user obtained such convertible virtual currency.\n**(3) Self-hosted wallet**\nThe term self-hosted wallet means a digital interface\u2014\n**(A)**\nused to secure and transfer convertible virtual currency; and\n**(B)**\nunder which the owner of convertible virtual currency retains independent control over such convertible virtual currency that is secured by such digital interface.",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-15",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2284",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Keep Your Coins Act of 2025",
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
            "updateDate": "2025-09-02T21:05:00Z"
          },
          {
            "name": "Currency",
            "updateDate": "2025-09-02T21:05:00Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2025-09-02T21:05:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-02-03T15:22:24Z"
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
          "measure-id": "id119hr148",
          "measure-number": "148",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr148v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keep Your Coins Act of 2025</strong></p><p>This bill prohibits federal agencies from restricting a person's use of convertible virtual currency for their own purposes or to conduct transactions through a self-hosted wallet. \u00a0</p>"
        },
        "title": "Keep Your Coins Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr148.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep Your Coins Act of 2025</strong></p><p>This bill prohibits federal agencies from restricting a person's use of convertible virtual currency for their own purposes or to conduct transactions through a self-hosted wallet. \u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr148"
    },
    "title": "Keep Your Coins Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep Your Coins Act of 2025</strong></p><p>This bill prohibits federal agencies from restricting a person's use of convertible virtual currency for their own purposes or to conduct transactions through a self-hosted wallet. \u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr148"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr148ih.xml"
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
      "title": "Keep Your Coins Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Your Coins Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal agencies from restricting the use of convertible virtual currency by a person to purchase goods or services for the person's own use, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:28Z"
    }
  ]
}
```
