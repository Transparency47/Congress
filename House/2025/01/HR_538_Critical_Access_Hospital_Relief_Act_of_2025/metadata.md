# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/538?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/538
- Title: Critical Access Hospital Relief Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 538
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-10-25T08:05:40Z
- Update date including text: 2025-10-25T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/538",
    "number": "538",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Critical Access Hospital Relief Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:40Z",
    "updateDateIncludingText": "2025-10-25T08:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:08:30Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "AL"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr538ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 538\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Smith of Nebraska (for himself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to remove the 96-hour physician certification requirement for inpatient critical access hospital services.\n#### 1. Short title\nThis Act may be cited as the Critical Access Hospital Relief Act of 2025 .\n#### 2. Removing Medicare 96-hour physician certification requirement for inpatient critical access hospital services\n##### (a) In general\nSection 1814(a) of the Social Security Act ( 42 U.S.C. 1395f(a) ) is amended\u2014\n**(1)**\nin paragraph (6), by adding and at the end;\n**(2)**\nin paragraph (7), at the end of subparagraph (E), by striking ; and and inserting a period; and\n**(3)**\nby striking paragraph (8).\n##### (b) Application\nThe amendments made by subsection (a) shall apply with respect to items and services furnished on or after January 1, 2026.",
      "versionDate": "2025-01-16",
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
            "updateDate": "2025-02-19T21:28:07Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-02-19T21:28:07Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-02-19T21:28:07Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-02-19T21:28:07Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-02-19T21:28:07Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-02-19T21:28:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-13T19:57:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr538",
          "measure-number": "538",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr538v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Critical Access Hospital Relief Act of </strong><strong>2025</strong></p><p>This bill repeals the 96-hour physician-certification requirement for inpatient critical access hospital services under Medicare. Under current law, as a condition for Medicare payment for such services, a physician must certify that a patient may reasonably be expected to be discharged or transferred to a hospital within 96 hours after admission to the critical access hospital.</p>"
        },
        "title": "Critical Access Hospital Relief Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr538.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Critical Access Hospital Relief Act of </strong><strong>2025</strong></p><p>This bill repeals the 96-hour physician-certification requirement for inpatient critical access hospital services under Medicare. Under current law, as a condition for Medicare payment for such services, a physician must certify that a patient may reasonably be expected to be discharged or transferred to a hospital within 96 hours after admission to the critical access hospital.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr538"
    },
    "title": "Critical Access Hospital Relief Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Critical Access Hospital Relief Act of </strong><strong>2025</strong></p><p>This bill repeals the 96-hour physician-certification requirement for inpatient critical access hospital services under Medicare. Under current law, as a condition for Medicare payment for such services, a physician must certify that a patient may reasonably be expected to be discharged or transferred to a hospital within 96 hours after admission to the critical access hospital.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr538"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr538ih.xml"
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
      "title": "Critical Access Hospital Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T12:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Critical Access Hospital Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to remove the 96-hour physician certification requirement for inpatient critical access hospital services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T12:03:32Z"
    }
  ]
}
```
