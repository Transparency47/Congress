# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/958?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/958
- Title: Train More Primary Care Doctors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 958
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-12-19T09:07:44Z
- Update date including text: 2025-12-19T09:07:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/958",
    "number": "958",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Train More Primary Care Doctors Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:44Z",
    "updateDateIncludingText": "2025-12-19T09:07:44Z"
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
          "date": "2025-02-04T17:01:50Z",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MO"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr958ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 958\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Nunn of Iowa (for himself and Mr. Cleaver ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to reauthorize funding for grants and contracts for primary care training and enhancement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Train More Primary Care Doctors Act of 2025 .\n#### 2. Primary care training and enhancement\nSection 747(c)(1) of the Public Health Service Act ( 42 U.S.C. 293k(c)(1) ) is amended by striking $48,924,000 for each of fiscal years 2021 through 2025 and inserting $49,924,000 for each of fiscal years 2025 through 2030 .",
      "versionDate": "2025-02-04",
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
            "name": "Employment and training programs",
            "updateDate": "2025-04-11T18:12:55Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-04-11T18:12:30Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-04-11T18:12:46Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-04-11T18:13:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-07T15:11:15Z"
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
          "measure-id": "id119hr958",
          "measure-number": "958",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr958v00",
            "update-date": "2025-04-28"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Train More Primary Care Doctors Act of 2025</strong></p><p>This bill reauthorizes through FY2030 the Health Resources and Services Administration\u2019s Primary Care Training and Enhancement program, which provides various grants to entities such as hospitals and schools for enhancing training and education for the primary care workforce.</p>"
        },
        "title": "Train More Primary Care Doctors Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr958.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Train More Primary Care Doctors Act of 2025</strong></p><p>This bill reauthorizes through FY2030 the Health Resources and Services Administration\u2019s Primary Care Training and Enhancement program, which provides various grants to entities such as hospitals and schools for enhancing training and education for the primary care workforce.</p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr958"
    },
    "title": "Train More Primary Care Doctors Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Train More Primary Care Doctors Act of 2025</strong></p><p>This bill reauthorizes through FY2030 the Health Resources and Services Administration\u2019s Primary Care Training and Enhancement program, which provides various grants to entities such as hospitals and schools for enhancing training and education for the primary care workforce.</p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr958"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr958ih.xml"
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
      "title": "Train More Primary Care Doctors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Train More Primary Care Doctors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to reauthorize funding for grants and contracts for primary care training and enhancement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:46Z"
    }
  ]
}
```
