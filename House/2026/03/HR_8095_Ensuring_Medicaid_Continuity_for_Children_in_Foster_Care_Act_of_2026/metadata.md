# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8095?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8095
- Title: Ensuring Medicaid Continuity for Children in Foster Care Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8095
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-09T20:47:04Z
- Update date including text: 2026-04-09T20:47:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8095",
    "number": "8095",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Ensuring Medicaid Continuity for Children in Foster Care Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-09T20:47:04Z",
    "updateDateIncludingText": "2026-04-09T20:47:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:05:15Z",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8095ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8095\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Bilirakis (for himself and Ms. Brownley ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to ensure that children in foster care who are placed in a qualified residential treatment program are eligible for Medicaid.\n#### 1. Short title\nThis Act may be cited as the Ensuring Medicaid Continuity for Children in Foster Care Act of 2026 .\n#### 2. Exemption of children in foster care who are placed in a qualified residential treatment program from the Medicaid IMD exclusion\n##### (a) In general\nSection 1905(a) of the Social Security Act ( 42 U.S.C. 1396d(a) ) is amended. in the matter designated as subdivision (B) following the last numbered paragraph of such section, by inserting and services provided to any individual who is a child in foster care under the responsibility of a State who has been placed in a child care institution that is a qualified residential treatment program (as defined in section 472(k)(4)), without regard to whether payments are made on behalf of such child under section 472 after section 1915(l) .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply with respect to items and services furnished in calendar quarters beginning on or after October 1, 2026.",
      "versionDate": "2026-03-26",
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
        "name": "Health",
        "updateDate": "2026-04-02T19:06:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-26",
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
          "measure-id": "id119hr8095",
          "measure-number": "8095",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-26",
          "originChamber": "HOUSE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8095v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2026-03-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ensuring Medicaid Continuity for Children in Foster Care Act of 2026</strong></p><p>This bill allows states to receive federal Medicaid payment for services provided to foster care children in qualified residential treatment programs (i.e., programs with trauma-informed treatment models that address the needs of children with serious emotional or behavioral disorders or disturbances).</p>"
        },
        "title": "Ensuring Medicaid Continuity for Children in Foster Care Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8095.xml",
    "summary": {
      "actionDate": "2026-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring Medicaid Continuity for Children in Foster Care Act of 2026</strong></p><p>This bill allows states to receive federal Medicaid payment for services provided to foster care children in qualified residential treatment programs (i.e., programs with trauma-informed treatment models that address the needs of children with serious emotional or behavioral disorders or disturbances).</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr8095"
    },
    "title": "Ensuring Medicaid Continuity for Children in Foster Care Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring Medicaid Continuity for Children in Foster Care Act of 2026</strong></p><p>This bill allows states to receive federal Medicaid payment for services provided to foster care children in qualified residential treatment programs (i.e., programs with trauma-informed treatment models that address the needs of children with serious emotional or behavioral disorders or disturbances).</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr8095"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8095ih.xml"
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
      "title": "Ensuring Medicaid Continuity for Children in Foster Care Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Medicaid Continuity for Children in Foster Care Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to ensure that children in foster care who are placed in a qualified residential treatment program are eligible for Medicaid.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T08:18:22Z"
    }
  ]
}
```
