# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/90?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/90
- Title: Health Coverage Choice Act
- Congress: 119
- Bill type: HR
- Bill number: 90
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-10T18:34:18Z
- Update date including text: 2025-12-10T18:34:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/90",
    "number": "90",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Health Coverage Choice Act",
    "type": "HR",
    "updateDate": "2025-12-10T18:34:18Z",
    "updateDateIncludingText": "2025-12-10T18:34:18Z"
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
          "date": "2025-01-03T16:05:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr90ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 90\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act to provide for a definition of short-term limited duration insurance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health Coverage Choice Act .\n#### 2. Definition of short-term limited duration insurance\nSection 2791(b) of the Public Health Service Act ( 42 U.S.C. 300gg\u201391(b) ) is amended by adding at the end the following new paragraph:\n(6) Short-term limited duration insurance The term short-term limited duration insurance means health insurance coverage provided under a contract with a health insurance issuer that\u2014 (A) has an expiration date specified in the contract that is less than 12 months after the original effective date of the contract; and (B) has a duration of not more than 3 years (taking into account renewals or extensions) after the original effective date of the contract. .",
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
        "actionDate": "2025-11-25",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6299",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Removing Insurance Gaps for Health Treatment (RIGHT) Act of 2025",
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
            "name": "Health care costs and insurance",
            "updateDate": "2025-02-05T21:00:10Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-02-05T21:00:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-03T15:04:55Z"
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
          "measure-id": "id119hr90",
          "measure-number": "90",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr90v00",
            "update-date": "2025-02-06"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Health Coverage Choice Act</strong></p><p>This bill extends the maximum duration of short-term, limited-duration health insurance plans. The bill increases the maximum authorized initial term of such plans to a period that is less than 12 months (with a total duration of no more than 36 months, including renewals).</p><p>Current regulations limit the initial term to no more than three months and the maximum coverage duration to no more than four months, including renewals or extensions.</p>"
        },
        "title": "Health Coverage Choice Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr90.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Health Coverage Choice Act</strong></p><p>This bill extends the maximum duration of short-term, limited-duration health insurance plans. The bill increases the maximum authorized initial term of such plans to a period that is less than 12 months (with a total duration of no more than 36 months, including renewals).</p><p>Current regulations limit the initial term to no more than three months and the maximum coverage duration to no more than four months, including renewals or extensions.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr90"
    },
    "title": "Health Coverage Choice Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Health Coverage Choice Act</strong></p><p>This bill extends the maximum duration of short-term, limited-duration health insurance plans. The bill increases the maximum authorized initial term of such plans to a period that is less than 12 months (with a total duration of no more than 36 months, including renewals).</p><p>Current regulations limit the initial term to no more than three months and the maximum coverage duration to no more than four months, including renewals or extensions.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr90"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr90ih.xml"
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
      "title": "Health Coverage Choice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Coverage Choice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act to provide for a definition of short-term limited duration insurance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T07:48:41Z"
    }
  ]
}
```
