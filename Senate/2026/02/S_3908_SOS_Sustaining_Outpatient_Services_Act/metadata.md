# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3908?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3908
- Title: SOS: Sustaining Outpatient Services Act
- Congress: 119
- Bill type: S
- Bill number: 3908
- Origin chamber: Senate
- Introduced date: 2026-02-25
- Update date: 2026-03-30T20:21:50Z
- Update date including text: 2026-03-30T20:21:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-25: Introduced in Senate
- 2026-02-25 - IntroReferral: Introduced in Senate
- 2026-02-25 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-25: Introduced in Senate

## Actions

- 2026-02-25 - IntroReferral: Introduced in Senate
- 2026-02-25 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3908",
    "number": "3908",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "SOS: Sustaining Outpatient Services Act",
    "type": "S",
    "updateDate": "2026-03-30T20:21:50Z",
    "updateDateIncludingText": "2026-03-30T20:21:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T15:40:02Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3908is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3908\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2026 Mr. Hoeven (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to allow payments under the Medicare program for certain items and services furnished by off-campus outpatient departments of a provider to be determined under the prospective payment system for hospital outpatient department services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SOS: Sustaining Outpatient Services Act .\n#### 2. Allowing Medicare payments for certain items and services furnished by off-campus outpatient departments of a provider to be determined under the prospective payment system for hospital outpatient department services\nSection 1833(t)(1)(B) of the Social Security Act ( 42 U.S.C. 1395l(t)(1)(B) ) is amended\u2014\n**(1)**\nin clause (iv), by striking and at the end;\n**(2)**\nin clause (v)\u2014\n**(A)**\nby inserting before does not include the following: subject to clause (vi), ; and\n**(B)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new clause:\n(vi) includes, with respect to a year (beginning with 2027), any item or service\u2014 (I) that is furnished during such year by an off-campus outpatient department of a provider (as defined in subparagraph (B) of paragraph (21)); and (II) with respect to which the greatest total amount paid with respect to a physician specialty under the physician fee schedule under section 1848 for all such items or services furnished by physicians in such specialty during the previous year was less than $2,000,000. .",
      "versionDate": "2026-02-25",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-02-24",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7666",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SOS: Sustaining Outpatient Services Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-03-13T15:27:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-25",
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
          "measure-id": "id119s3908",
          "measure-number": "3908",
          "measure-type": "s",
          "orig-publish-date": "2026-02-25",
          "originChamber": "SENATE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3908v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2026-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>SOS: Sustaining Outpatient Services Act</b></p> <p>This bill allows for payment under the Medicare prospective payment system for hospital outpatient department services of certain items and services that are furnished at off-campus outpatient departments. Specifically, the bill allows for payment of items and services for which payments to physician specialists (under the Medicare physician fee schedule) did not exceed $2 million during the previous year.</p>"
        },
        "title": "SOS: Sustaining Outpatient Services Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3908.xml",
    "summary": {
      "actionDate": "2026-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>SOS: Sustaining Outpatient Services Act</b></p> <p>This bill allows for payment under the Medicare prospective payment system for hospital outpatient department services of certain items and services that are furnished at off-campus outpatient departments. Specifically, the bill allows for payment of items and services for which payments to physician specialists (under the Medicare physician fee schedule) did not exceed $2 million during the previous year.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s3908"
    },
    "title": "SOS: Sustaining Outpatient Services Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>SOS: Sustaining Outpatient Services Act</b></p> <p>This bill allows for payment under the Medicare prospective payment system for hospital outpatient department services of certain items and services that are furnished at off-campus outpatient departments. Specifically, the bill allows for payment of items and services for which payments to physician specialists (under the Medicare physician fee schedule) did not exceed $2 million during the previous year.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s3908"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3908is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SOS: Sustaining Outpatient Services Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SOS: Sustaining Outpatient Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to allow payments under the Medicare program for certain items and services furnished by off-campus outpatient departments of a provider to be determined under the prospective payment system for hospital outpatient department services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:28Z"
    }
  ]
}
```
