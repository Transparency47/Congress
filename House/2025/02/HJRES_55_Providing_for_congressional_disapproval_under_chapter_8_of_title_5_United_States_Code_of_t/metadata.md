# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/55?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/55
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Financial Crimes Enforcement Network relating to "Anti-Money Laundering Regulations for Residential Real Estate Transfers".
- Congress: 119
- Bill type: HJRES
- Bill number: 55
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-12-06T06:59:02Z
- Update date including text: 2025-12-06T06:59:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/55",
    "number": "55",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001116",
        "district": "9",
        "firstName": "Andrew",
        "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
        "lastName": "Clyde",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\".",
    "type": "HJRES",
    "updateDate": "2025-12-06T06:59:02Z",
    "updateDateIncludingText": "2025-12-06T06:59:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:06:35Z",
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
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres55ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 55\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Clyde submitted the following joint resolution; which was referred to the Committee on Financial Services\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Financial Crimes Enforcement Network relating to Anti-Money Laundering Regulations for Residential Real Estate Transfers .\nThat Congress disapproves the rule submitted by the Financial Crimes Enforcement Network relating to Anti-Money Laundering Regulations for Residential Real Estate Transfers (89 Fed. Reg. 70258 (August 29, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "15",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution disapproving the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\".",
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
        "updateDate": "2025-02-21T13:17:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hjres55",
          "measure-number": "55",
          "measure-type": "hjres",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-09-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres55v00",
            "update-date": "2025-09-29"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the final rule issued by the Financial Crimes Enforcement Network (FinCEN) titled <em>Anti-Money Laundering Regulations for Residential Real Estate Transfers </em>and published on August 29, 2024. This rule requires persons involved in real estate closings and settlements to report to FinCEN any non-financed (i.e., cash) transfers of residential property to certain legal entities and trusts.</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres55.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Financial Crimes Enforcement Network (FinCEN) titled <em>Anti-Money Laundering Regulations for Residential Real Estate Transfers </em>and published on August 29, 2024. This rule requires persons involved in real estate closings and settlements to report to FinCEN any non-financed (i.e., cash) transfers of residential property to certain legal entities and trusts.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119hjres55"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule issued by the Financial Crimes Enforcement Network (FinCEN) titled <em>Anti-Money Laundering Regulations for Residential Real Estate Transfers </em>and published on August 29, 2024. This rule requires persons involved in real estate closings and settlements to report to FinCEN any non-financed (i.e., cash) transfers of residential property to certain legal entities and trusts.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119hjres55"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres55ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T09:18:38Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:06:51Z"
    }
  ]
}
```
