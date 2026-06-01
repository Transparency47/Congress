# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/88?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/88
- Title: Supporting the designation of January 31, 2025, as "Earned Income Tax Credit Awareness Day".
- Congress: 119
- Bill type: HRES
- Bill number: 88
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-02-21T11:38:47Z
- Update date including text: 2025-02-21T11:38:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-01-31 - Committee: Submitted in House
- Latest action: 2025-01-31: Submitted in House

## Actions

- 2025-01-31 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-01-31 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/88",
    "number": "88",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001185",
        "district": "7",
        "firstName": "Terri",
        "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
        "lastName": "Sewell",
        "party": "D",
        "state": "AL"
      }
    ],
    "title": "Supporting the designation of January 31, 2025, as \"Earned Income Tax Credit Awareness Day\".",
    "type": "HRES",
    "updateDate": "2025-02-21T11:38:47Z",
    "updateDateIncludingText": "2025-02-21T11:38:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-01-31T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CT"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "WI"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "VA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NV"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "WA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres88ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 88\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. Sewell (for herself, Mr. Thompson of California , Mr. Larson of Connecticut , Mr. Davis of Illinois , Ms. Moore of Wisconsin , Mr. Boyle of Pennsylvania , Mr. Beyer , Mr. Panetta , Mr. Horsford , and Mr. Suozzi ) submitted the following resolution; which was referred to the Committee on Ways and Means\nRESOLUTION\nSupporting the designation of January 31, 2025, as Earned Income Tax Credit Awareness Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Earned Income Tax Credit Awareness Day ; and\n**(2)**\ncalls on Federal, State, and local agencies, community organizations, nonprofit organizations, employers, and other partners to help increase awareness about certain tax credits to ensure that all eligible workers have access to the full range of tax credit benefits available to them, including\u2014\n**(A)**\nthe earned income tax credit;\n**(B)**\nother refundable tax credits not described in subparagraph (A); and\n**(C)**\nfree tax filing assistance.",
      "versionDate": "2025-01-31",
      "versionType": "IH"
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
        "name": "Taxation",
        "updateDate": "2025-02-05T16:01:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hres88",
          "measure-number": "88",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-02-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres88v00",
            "update-date": "2025-02-21"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of Earned Income Tax Credit Awareness Day. The resolution also calls for increasing awareness of (1) the earned income tax credit, which is refundable; (2) other refundable federal tax credits; and (3) free tax filing assistance.</p>"
        },
        "title": "Supporting the designation of January 31, 2025, as \"Earned Income Tax Credit Awareness Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres88.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of Earned Income Tax Credit Awareness Day. The resolution also calls for increasing awareness of (1) the earned income tax credit, which is refundable; (2) other refundable federal tax credits; and (3) free tax filing assistance.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hres88"
    },
    "title": "Supporting the designation of January 31, 2025, as \"Earned Income Tax Credit Awareness Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of Earned Income Tax Credit Awareness Day. The resolution also calls for increasing awareness of (1) the earned income tax credit, which is refundable; (2) other refundable federal tax credits; and (3) free tax filing assistance.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hres88"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres88ih.xml"
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
      "title": "Supporting the designation of January 31, 2025, as \"Earned Income Tax Credit Awareness Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T09:18:36Z"
    },
    {
      "title": "Supporting the designation of January 31, 2025, as \"Earned Income Tax Credit Awareness Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T09:05:22Z"
    }
  ]
}
```
