# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/90?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/90
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to "Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts".
- Congress: 119
- Bill type: HJRES
- Bill number: 90
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-04-17T20:44:40Z
- Update date including text: 2026-04-17T20:44:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/90",
    "number": "90",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\".",
    "type": "HJRES",
    "updateDate": "2026-04-17T20:44:40Z",
    "updateDateIncludingText": "2026-04-17T20:44:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T20:20:00Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres90ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 90\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mrs. Bice submitted the following joint resolution; which was referred to the Committee on Agriculture\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts .\nThat Congress disapproves the final guidance submitted by the Commodity Futures Trading Commission relating to \u201cCommission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\u201d (89 Fed. Reg. 83378 (October 15, 2024)) and such rule shall have no force or effect.",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "9",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\".",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-22T17:46:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119hjres90",
          "measure-number": "90",
          "measure-type": "hjres",
          "orig-publish-date": "2025-04-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres90v00",
            "update-date": "2026-04-17"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the final guidance issued by the Commodity Futures Trading Commission (CFTC) titled <em>Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts</em> and published on October 15, 2024. The guidance provides factors for designated contract markets (i.e., CFTC-regulated derivatives exchanges) to consider when listing voluntary carbon credit derivative contracts, including characteristics of transparency and permanence.\u00a0</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres90.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final guidance issued by the Commodity Futures Trading Commission (CFTC) titled <em>Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts</em> and published on October 15, 2024. The guidance provides factors for designated contract markets (i.e., CFTC-regulated derivatives exchanges) to consider when listing voluntary carbon credit derivative contracts, including characteristics of transparency and permanence.\u00a0</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119hjres90"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\"."
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final guidance issued by the Commodity Futures Trading Commission (CFTC) titled <em>Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts</em> and published on October 15, 2024. The guidance provides factors for designated contract markets (i.e., CFTC-regulated derivatives exchanges) to consider when listing voluntary carbon credit derivative contracts, including characteristics of transparency and permanence.\u00a0</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119hjres90"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres90ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T08:18:34Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T08:06:30Z"
    }
  ]
}
```
