# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1399?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1399
- Title: Prior Approval Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 1399
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2025-10-01T08:05:22Z
- Update date including text: 2025-10-01T08:05:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1399",
    "number": "1399",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "A000369",
        "district": "2",
        "firstName": "Mark",
        "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
        "lastName": "Amodei",
        "party": "R",
        "state": "NV"
      }
    ],
    "title": "Prior Approval Reform Act",
    "type": "HR",
    "updateDate": "2025-10-01T08:05:22Z",
    "updateDateIncludingText": "2025-10-01T08:05:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1399ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1399\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Amodei of Nevada introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to expand the ability of trade associations to solicit contributions from the stockholders and executive or administrative personnel of their member corporations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prior Approval Reform Act .\n#### 2. Removing requirement for prior approval\n##### (a) Solicitations\nSection 316(b)(4)(D) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30118(b)(4)(D) ) is amended by striking to the extent that and all that follows and inserting a period.\n##### (b) Effective Date\nThe amendment made by subsection (a) shall apply to solicitations made on or after January 1, 2025.",
      "versionDate": "2025-02-18",
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
            "name": "Corporate finance and management",
            "updateDate": "2025-07-09T13:33:03Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-07-09T13:33:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-02T15:07:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1399",
          "measure-number": "1399",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-06-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1399v00",
            "update-date": "2025-06-12"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Prior Approval Reform Act</strong></p><p>This bill allows a trade association or a separate segregated fund established by a trade association to solicit contributions from a member corporation's stockholders and executive or administrative personnel and their families without the approval of the member corporation. Such a solicitation may be made by more than one trade association in a calendar year.</p>"
        },
        "title": "Prior Approval Reform Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1399.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prior Approval Reform Act</strong></p><p>This bill allows a trade association or a separate segregated fund established by a trade association to solicit contributions from a member corporation's stockholders and executive or administrative personnel and their families without the approval of the member corporation. Such a solicitation may be made by more than one trade association in a calendar year.</p>",
      "updateDate": "2025-06-12",
      "versionCode": "id119hr1399"
    },
    "title": "Prior Approval Reform Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prior Approval Reform Act</strong></p><p>This bill allows a trade association or a separate segregated fund established by a trade association to solicit contributions from a member corporation's stockholders and executive or administrative personnel and their families without the approval of the member corporation. Such a solicitation may be made by more than one trade association in a calendar year.</p>",
      "updateDate": "2025-06-12",
      "versionCode": "id119hr1399"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1399ih.xml"
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
      "title": "Prior Approval Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prior Approval Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to expand the ability of trade associations to solicit contributions from the stockholders and executive or administrative personnel of their member corporations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:26Z"
    }
  ]
}
```
