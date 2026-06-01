# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/104?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/104
- Title: Protecting Arizona from Federal Land Grabs Act
- Congress: 119
- Bill type: HR
- Bill number: 104
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-10-22T08:05:50Z
- Update date including text: 2025-10-22T08:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/104",
    "number": "104",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Protecting Arizona from Federal Land Grabs Act",
    "type": "HR",
    "updateDate": "2025-10-22T08:05:50Z",
    "updateDateIncludingText": "2025-10-22T08:05:50Z"
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
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
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
          "date": "2025-01-03T16:09:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr104ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 104\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend title 54, United States Code, to prohibit the extension or establishment of national monuments in Arizona except by express authorization of Congress, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Arizona from Federal Land Grabs Act .\n#### 2. Limitation on extension or establishment of national monuments in Arizona\nSubsection (d) of section 320301 of title 54, United States Code, is amended\u2014\n**(1)**\nby inserting or Arizona after Wyoming ; and\n**(2)**\nby inserting or Arizona after Wyoming .",
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
            "name": "Arizona",
            "updateDate": "2025-01-31T19:56:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-01-31T19:57:00Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-01-31T19:57:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-01-31T17:07:27Z"
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
          "measure-id": "id119hr104",
          "measure-number": "104",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr104v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Arizona from Federal Land Grabs Act</strong></p> <p>This bill prohibits any further extension or establishment of national monuments in Arizona except by express authorization of Congress. </p>"
        },
        "title": "Protecting Arizona from Federal Land Grabs Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr104.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Arizona from Federal Land Grabs Act</strong></p> <p>This bill prohibits any further extension or establishment of national monuments in Arizona except by express authorization of Congress. </p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr104"
    },
    "title": "Protecting Arizona from Federal Land Grabs Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Arizona from Federal Land Grabs Act</strong></p> <p>This bill prohibits any further extension or establishment of national monuments in Arizona except by express authorization of Congress. </p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr104"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr104ih.xml"
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
      "title": "Protecting Arizona from Federal Land Grabs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Arizona from Federal Land Grabs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 54, United States Code, to prohibit the extension or establishment of national monuments in Arizona except by express authorization of Congress, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:26Z"
    }
  ]
}
```
