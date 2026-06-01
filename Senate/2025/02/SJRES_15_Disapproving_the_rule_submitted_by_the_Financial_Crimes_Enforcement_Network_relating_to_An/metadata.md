# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/15?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/15
- Title: A joint resolution disapproving the rule submitted by the Financial Crimes Enforcement Network relating to "Anti-Money Laundering Regulations for Residential Real Estate Transfers".
- Congress: 119
- Bill type: SJRES
- Bill number: 15
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2025-12-06T06:43:30Z
- Update date including text: 2025-12-06T06:43:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/15",
    "number": "15",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A joint resolution disapproving the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\".",
    "type": "SJRES",
    "updateDate": "2025-12-06T06:43:30Z",
    "updateDateIncludingText": "2025-12-06T06:43:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T19:55:55Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres15is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 15\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Lee introduced the following joint resolution; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nJOINT RESOLUTION\nDisapproving the rule submitted by the Financial Crimes Enforcement Network relating to Anti-Money Laundering Regulations for Residential Real Estate Transfers .\nThat Congress disapproves the final rule submitted by the Financial Crimes Enforcement Network relating to Anti-Money Laundering Regulations for Residential Real Estate Transfers (89 Fed. Reg. 70258 (August 29, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-02-12",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "55",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\".",
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
        "updateDate": "2025-02-11T13:06:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119sjres15",
          "measure-number": "15",
          "measure-type": "sjres",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-09-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres15v00",
            "update-date": "2025-09-24"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution nullifies the final rule issued by the Financial Crimes Enforcement Network (FinCEN) titled <em>Anti-Money Laundering Regulations for Residential Real Estate Transfers </em>and published on August 29, 2024. This rule requires persons involved in real estate closings and settlements to report to FinCEN any non-financed (i.e., cash) transfers of residential property to certain legal entities and trusts.</p>"
        },
        "title": "A joint resolution disapproving the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres15.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the final rule issued by the Financial Crimes Enforcement Network (FinCEN) titled <em>Anti-Money Laundering Regulations for Residential Real Estate Transfers </em>and published on August 29, 2024. This rule requires persons involved in real estate closings and settlements to report to FinCEN any non-financed (i.e., cash) transfers of residential property to certain legal entities and trusts.</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119sjres15"
    },
    "title": "A joint resolution disapproving the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the final rule issued by the Financial Crimes Enforcement Network (FinCEN) titled <em>Anti-Money Laundering Regulations for Residential Real Estate Transfers </em>and published on August 29, 2024. This rule requires persons involved in real estate closings and settlements to report to FinCEN any non-financed (i.e., cash) transfers of residential property to certain legal entities and trusts.</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119sjres15"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres15is.xml"
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
      "title": "A joint resolution disapproving the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:26Z"
    },
    {
      "title": "A joint resolution disapproving the rule submitted by the Financial Crimes Enforcement Network relating to \"Anti-Money Laundering Regulations for Residential Real Estate Transfers\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T11:56:46Z"
    }
  ]
}
```
