# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/9?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/9
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to "Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts".
- Congress: 119
- Bill type: SJRES
- Bill number: 9
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2025-12-05T22:55:11Z
- Update date including text: 2025-12-05T22:55:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/9",
    "number": "9",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\".",
    "type": "SJRES",
    "updateDate": "2025-12-05T22:55:11Z",
    "updateDateIncludingText": "2025-12-05T22:55:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
          "date": "2025-01-30T23:35:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres9is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 9\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Kennedy (for himself and Mr. Sheehy ) introduced the following joint resolution; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts .\nThat Congress disapproves the final guidance submitted by the Commodity Futures Trading Commission relating to Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts (89 Fed. Reg. 83378 (October 15, 2024)) and such rule shall have no force or effect.",
      "versionDate": "2025-01-30",
      "versionType": "IS"
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
        "actionDate": "2025-04-18",
        "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development."
      },
      "number": "90",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\".",
      "type": "HJRES"
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
        "updateDate": "2025-02-21T14:43:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119sjres9",
          "measure-number": "9",
          "measure-type": "sjres",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-06-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres9v00",
            "update-date": "2025-06-04"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution nullifies the final guidance issued by the Commodity Futures Trading Commission (CFTC) titled <em>Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts</em> and published on October 15, 2024. The guidance provides factors for designated contract markets (i.e., CFTC-regulated derivatives exchanges) to consider when listing voluntary carbon credit derivative contracts, including characteristics of transparency and permanence.\u00a0</p>"
        },
        "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres9.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the final guidance issued by the Commodity Futures Trading Commission (CFTC) titled <em>Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts</em> and published on October 15, 2024. The guidance provides factors for designated contract markets (i.e., CFTC-regulated derivatives exchanges) to consider when listing voluntary carbon credit derivative contracts, including characteristics of transparency and permanence.\u00a0</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119sjres9"
    },
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the final guidance issued by the Commodity Futures Trading Commission (CFTC) titled <em>Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts</em> and published on October 15, 2024. The guidance provides factors for designated contract markets (i.e., CFTC-regulated derivatives exchanges) to consider when listing voluntary carbon credit derivative contracts, including characteristics of transparency and permanence.\u00a0</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119sjres9"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres9is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T04:48:20Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Commodity Futures Trading Commission relating to \"Commission Guidance Regarding the Listing of Voluntary Carbon Credit Derivative Contracts\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:56:22Z"
    }
  ]
}
```
