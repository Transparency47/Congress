# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4267?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4267
- Title: Get Your Money Back Act
- Congress: 119
- Bill type: HR
- Bill number: 4267
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2026-04-09T17:01:44Z
- Update date including text: 2026-04-09T17:01:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-30: Introduced in House

## Actions

- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4267",
    "number": "4267",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Get Your Money Back Act",
    "type": "HR",
    "updateDate": "2026-04-09T17:01:44Z",
    "updateDateIncludingText": "2026-04-09T17:01:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
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
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T18:02:25Z",
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
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4267ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4267\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Mrs. Sykes introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo direct the Secretary of the Treasury to continue to implement Direct File, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Get Your Money Back Act .\n#### 2. Direct File\n##### (a) Continuation of Direct File required\nNotwithstanding any other provision of law, the Secretary of the Treasury (or the Secretary\u2019s delegate) shall continue to implement the free direct e-file tax return system established by the Internal Revenue Service (commonly known as Direct File ).\n##### (b) Participation in Direct File required\nFor each taxable year beginning after December 31, 2025, the Secretary (or the Secretary\u2019s delegate) shall require each of the 50 States and the District of Columbia to participate in the free direct e-file tax return system described in subsection (a).",
      "versionDate": "2025-06-30",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-07-30T23:22:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-30",
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
          "measure-id": "id119hr4267",
          "measure-number": "4267",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-30",
          "originChamber": "HOUSE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4267v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-06-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Get Your Money Back Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to continue to\u00a0implement the Direct File program and, for tax years beginning after 2025, requires each U.S. state and the District of Columbia to participate in the Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p>"
        },
        "title": "Get Your Money Back Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4267.xml",
    "summary": {
      "actionDate": "2025-06-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Get Your Money Back Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to continue to\u00a0implement the Direct File program and, for tax years beginning after 2025, requires each U.S. state and the District of Columbia to participate in the Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr4267"
    },
    "title": "Get Your Money Back Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Get Your Money Back Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to continue to\u00a0implement the Direct File program and, for tax years beginning after 2025, requires each U.S. state and the District of Columbia to participate in the Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr4267"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4267ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Treasury to continue to implement Direct File, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T04:31:23Z"
    },
    {
      "title": "Get Your Money Back Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Get Your Money Back Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T04:23:23Z"
    }
  ]
}
```
