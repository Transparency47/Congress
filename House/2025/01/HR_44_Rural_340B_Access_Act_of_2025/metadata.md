# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/44?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/44
- Title: Rural 340B Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 44
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-04-14T08:05:40Z
- Update date including text: 2026-04-14T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/44",
    "number": "44",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Rural 340B Access Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:40Z",
    "updateDateIncludingText": "2026-04-14T08:05:40Z"
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
          "date": "2025-01-03T16:25:20Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "MI"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NM"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "HI"
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
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr44ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 44\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Bergman (for himself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title III of the Public Health Service Act to include rural emergency hospitals in the definition of a covered entity for purposes of the 340B drug discount program.\n#### 1. Short title\nThis Act may be cited as the Rural 340B Access Act of 2025 .\n#### 2. Including rural emergency hospitals as covered entities for purposes of the 340B drug discount program\nSection 340B(a)(4) of the Public Health Service Act ( 42 U.S.C. 256b(a)(4) ) is amended by adding at the end the following new subparagraph:\n(P) An entity that is a rural emergency hospital (as defined in section 1861(kkk)(2) of the Social Security Act) that is owned or operated by a unit of State or local government, is a public or private non-profit corporation which is formally granted governmental powers by a unit of State or local government, or is a private non-profit rural emergency hospital which has a contract with a State or local government to provide health care services to low income individuals who are not entitled to benefits under title XVIII of the Social Security Act or eligible for assistance under the State plan under this title. .",
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
            "name": "Health care costs and insurance",
            "updateDate": "2025-02-06T15:15:42Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-02-06T15:15:28Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-02-06T15:15:33Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-02-06T15:15:38Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-02-06T15:15:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-03T15:02:55Z"
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
          "measure-id": "id119hr44",
          "measure-number": "44",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr44v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rural 340B Access Act of 2025</strong></p><p>This bill makes rural emergency hospitals (REHs) eligible to purchase drugs from manufacturers at discounted prices by participating in the Health Resources and Services Administration\u2019s (HRSA\u2019s) 340B drug pricing program. HRSA\u2019s 340B program requires drug manufacturers that participate in the Medicaid program to sell certain outpatient drugs at discounted prices to entities listed as eligible under current law. Additionally, in 2020, Congress established REHs as a new Medicare provider designation for hospitals in rural areas providing emergency department services, observation care, and other outpatient medical and health services for which the annual per patient average length of stay does not exceed 24 hours. The bill adds qualifying REHs to the list of entities that are eligible to participate in the 340B program.\u00a0</p>"
        },
        "title": "Rural 340B Access Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr44.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural 340B Access Act of 2025</strong></p><p>This bill makes rural emergency hospitals (REHs) eligible to purchase drugs from manufacturers at discounted prices by participating in the Health Resources and Services Administration\u2019s (HRSA\u2019s) 340B drug pricing program. HRSA\u2019s 340B program requires drug manufacturers that participate in the Medicaid program to sell certain outpatient drugs at discounted prices to entities listed as eligible under current law. Additionally, in 2020, Congress established REHs as a new Medicare provider designation for hospitals in rural areas providing emergency department services, observation care, and other outpatient medical and health services for which the annual per patient average length of stay does not exceed 24 hours. The bill adds qualifying REHs to the list of entities that are eligible to participate in the 340B program.\u00a0</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr44"
    },
    "title": "Rural 340B Access Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural 340B Access Act of 2025</strong></p><p>This bill makes rural emergency hospitals (REHs) eligible to purchase drugs from manufacturers at discounted prices by participating in the Health Resources and Services Administration\u2019s (HRSA\u2019s) 340B drug pricing program. HRSA\u2019s 340B program requires drug manufacturers that participate in the Medicaid program to sell certain outpatient drugs at discounted prices to entities listed as eligible under current law. Additionally, in 2020, Congress established REHs as a new Medicare provider designation for hospitals in rural areas providing emergency department services, observation care, and other outpatient medical and health services for which the annual per patient average length of stay does not exceed 24 hours. The bill adds qualifying REHs to the list of entities that are eligible to participate in the 340B program.\u00a0</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr44"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr44ih.xml"
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
      "title": "Rural 340B Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural 340B Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title III of the Public Health Service Act to include rural emergency hospitals in the definition of a covered entity for purposes of the 340B drug discount program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T06:49:42Z"
    }
  ]
}
```
