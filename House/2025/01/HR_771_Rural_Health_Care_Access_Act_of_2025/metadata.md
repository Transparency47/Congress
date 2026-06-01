# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/771?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/771
- Title: Rural Health Care Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 771
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-06-07T08:06:13Z
- Update date including text: 2025-06-07T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/771",
    "number": "771",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Rural Health Care Access Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-07T08:06:13Z",
    "updateDateIncludingText": "2025-06-07T08:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:05:35Z",
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
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "PA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "IL"
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
      "sponsorshipDate": "2025-06-06",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr771ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 771\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Green of Tennessee (for himself, Mr. Thompson of Pennsylvania , Mr. Jackson of Texas , and Mrs. Miller of Illinois ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to permit States to designate without any mileage limitations facilities that are located in rural areas as critical access hospitals.\n#### 1. Short title\nThis Act may be cited as the Rural Health Care Access Act of 2025 .\n#### 2. Medicare Rural Hospital Flexibility Program\n##### (a) In general\nSection 1820 of the Social Security Act ( 42 U.S.C. 1395i\u20134 ) is amended\u2014\n**(1)**\nin subsection (c)(2)(B)(i)\u2014\n**(A)**\nby striking , and that\u2014 and inserting a semicolon; and\n**(B)**\nby striking subclauses (I) and (II); and\n**(2)**\nin subsection (h)(3), by inserting made before the date of the enactment of the Rural Health Care Access Act of 2025 after any redesignation .\n##### (b) Effective date\nThe amendment made by subsection (a)(1) shall apply with respect to any designation or redesignation made on or after the date of the enactment of this Act.",
      "versionDate": "2025-01-28",
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
            "name": "Health care coverage and access",
            "updateDate": "2025-03-27T15:28:10Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-03-27T15:28:10Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-27T15:28:10Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-03-27T15:28:10Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-03-27T15:28:10Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-27T15:28:10Z"
          },
          {
            "name": "Urban and suburban affairs and development",
            "updateDate": "2025-03-27T15:28:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-03T17:01:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr771",
          "measure-number": "771",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr771v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rural Health Care Access Act of 2025</strong><strong></strong></p><p>This bill eliminates certain criteria that hospitals must meet in order to qualify as critical access hospitals that receive special payment under Medicare.</p><p>Specifically, the bill eliminates the requirement that a hospital must either (1) be located more than 35 miles (15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area.</p>"
        },
        "title": "Rural Health Care Access Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr771.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Health Care Access Act of 2025</strong><strong></strong></p><p>This bill eliminates certain criteria that hospitals must meet in order to qualify as critical access hospitals that receive special payment under Medicare.</p><p>Specifically, the bill eliminates the requirement that a hospital must either (1) be located more than 35 miles (15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr771"
    },
    "title": "Rural Health Care Access Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Health Care Access Act of 2025</strong><strong></strong></p><p>This bill eliminates certain criteria that hospitals must meet in order to qualify as critical access hospitals that receive special payment under Medicare.</p><p>Specifically, the bill eliminates the requirement that a hospital must either (1) be located more than 35 miles (15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr771"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr771ih.xml"
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
      "title": "Rural Health Care Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Health Care Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to permit States to designate without any mileage limitations facilities that are located in rural areas as critical access hospitals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:36Z"
    }
  ]
}
```
