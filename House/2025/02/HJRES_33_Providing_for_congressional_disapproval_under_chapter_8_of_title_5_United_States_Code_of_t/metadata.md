# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/33?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/33
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Communications Commission relating to "Addressing the Homework Gap Through the E-Rate Program".
- Congress: 119
- Bill type: HJRES
- Bill number: 33
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-11-21T12:04:28Z
- Update date including text: 2025-11-21T12:04:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/33",
    "number": "33",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000469",
        "district": "1",
        "firstName": "Russ",
        "fullName": "Rep. Fulcher, Russ [R-ID-1]",
        "lastName": "Fulcher",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Communications Commission relating to \"Addressing the Homework Gap Through the E-Rate Program\".",
    "type": "HJRES",
    "updateDate": "2025-11-21T12:04:28Z",
    "updateDateIncludingText": "2025-11-21T12:04:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres33ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 33\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Fulcher submitted the following joint resolution; which was referred to the Committee on Energy and Commerce\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Communications Commission relating to Addressing the Homework Gap Through the E\u2013Rate Program .\nThat Congress disapproves the rule submitted by the Federal Communications Commission relating to Addressing the Homework Gap Through the E\u2013Rate Program (89 Fed. Reg. 67303 (August 20, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-02-04",
      "versionType": "IH"
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
        "actionDate": "2025-05-09",
        "actionTime": "13:04:45",
        "text": "Held at the desk."
      },
      "number": "7",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Communications Commission relating to \"Addressing the Homework Gap Through the E-Rate Program\".",
      "type": "SJRES"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-02-06T21:46:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hjres33",
          "measure-number": "33",
          "measure-type": "hjres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres33v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the final rule issued by the Federal Communications Commission titled <em>Addressing the Homework Gap Through the E-Rate Program</em> and published on August 20, 2024. The rule permits schools and libraries participating in the Schools and Libraries Universal Service Support program (E-Rate) to purchase discounted Wi-Fi hotspots and associated mobile connectivity service for off-premises use by students, school staff, and library patrons. Under the rule, E-Rate participants must implement acceptable use policies that require hotspots to be used primarily for educational purposes. \u00a0</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Communications Commission relating to \"Addressing the Homework Gap Through the E-Rate Program\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres33.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Federal Communications Commission titled <em>Addressing the Homework Gap Through the E-Rate Program</em> and published on August 20, 2024. The rule permits schools and libraries participating in the Schools and Libraries Universal Service Support program (E-Rate) to purchase discounted Wi-Fi hotspots and associated mobile connectivity service for off-premises use by students, school staff, and library patrons. Under the rule, E-Rate participants must implement acceptable use policies that require hotspots to be used primarily for educational purposes. \u00a0</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hjres33"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Communications Commission relating to \"Addressing the Homework Gap Through the E-Rate Program\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Federal Communications Commission titled <em>Addressing the Homework Gap Through the E-Rate Program</em> and published on August 20, 2024. The rule permits schools and libraries participating in the Schools and Libraries Universal Service Support program (E-Rate) to purchase discounted Wi-Fi hotspots and associated mobile connectivity service for off-premises use by students, school staff, and library patrons. Under the rule, E-Rate participants must implement acceptable use policies that require hotspots to be used primarily for educational purposes. \u00a0</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hjres33"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres33ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Communications Commission relating to \"Addressing the Homework Gap Through the E-Rate Program\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T12:03:22Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Communications Commission relating to \"Addressing the Homework Gap Through the E-Rate Program\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T09:05:51Z"
    }
  ]
}
```
