# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1579?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1579
- Title: Broadband Buildout Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 1579
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2025-12-05T22:01:25Z
- Update date including text: 2025-12-05T22:01:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1579",
    "number": "1579",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Broadband Buildout Accountability Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:01:25Z",
    "updateDateIncludingText": "2025-12-05T22:01:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:02:05Z",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "FL"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "OH"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TX"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1579ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1579\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Pfluger (for himself, Mr. Carter of Georgia , Mr. Dunn of Florida , Mr. Balderson , Mr. Weber of Texas , and Mr. Fulcher ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo apply the Freedom of Information Act to actions and decisions of the Assistant Secretary of Commerce for Communications and Information in carrying out the Broadband Equity, Access, and Deployment Program.\n#### 1. Short title\nThis Act may be cited as the Broadband Buildout Accountability Act .\n#### 2. Applicability of FOIA to the Broadband Equity, Access, and Deployment Program\nSection 60102(o)(2) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(o)(2) ) is amended by inserting after Act\u2019) the following: , except for section 552 of that title (commonly referred to as the Freedom of Information Act ) .",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "713",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Broadband Buildout Accountability Act",
      "type": "S"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-06T20:59:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119hr1579",
          "measure-number": "1579",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1579v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Broadband Buildout Accountability Act</strong></p> <p>This bill makes actions or decisions of the National Telecommunications and Information Administration concerning the Broadband Equity, Access, and Deployment Program subject to the Freedom of Information Act, which governs the release of federal documents.</p>"
        },
        "title": "Broadband Buildout Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1579.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadband Buildout Accountability Act</strong></p> <p>This bill makes actions or decisions of the National Telecommunications and Information Administration concerning the Broadband Equity, Access, and Deployment Program subject to the Freedom of Information Act, which governs the release of federal documents.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hr1579"
    },
    "title": "Broadband Buildout Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadband Buildout Accountability Act</strong></p> <p>This bill makes actions or decisions of the National Telecommunications and Information Administration concerning the Broadband Equity, Access, and Deployment Program subject to the Freedom of Information Act, which governs the release of federal documents.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hr1579"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1579ih.xml"
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
      "title": "Broadband Buildout Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Broadband Buildout Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To apply the Freedom of Information Act to actions and decisions of the Assistant Secretary of Commerce for Communications and Information in carrying out the Broadband Equity, Access, and Deployment Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:33Z"
    }
  ]
}
```
