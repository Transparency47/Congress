# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/235
- Title: National Museum of Play Recognition Act
- Congress: 119
- Bill type: HR
- Bill number: 235
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-03-03T18:26:31Z
- Update date including text: 2025-03-03T18:26:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/235",
    "number": "235",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "M001206",
        "district": "25",
        "firstName": "Joseph",
        "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
        "lastName": "Morelle",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "National Museum of Play Recognition Act",
    "type": "HR",
    "updateDate": "2025-03-03T18:26:31Z",
    "updateDateIncludingText": "2025-03-03T18:26:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:01:50Z",
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
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr235ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 235\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Mr. Morelle (for himself and Mr. Langworthy ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo recognize the Margaret Woodbury Strong Museum in Rochester, New York.\n#### 1. Short title\nThis Act may be cited as the National Museum of Play Recognition Act .\n#### 2. Designation of National Museum of Play in Rochester, New York\n##### (a) Congressional recognition\nCongress\u2014\n**(1)**\nrecognizes that the Margaret Woodbury Strong Museum, DBA Strong Museum, located in Rochester, New York, is the only museum of its kind that exists for the exclusive purpose of exploring the ways in which play encourages learning, creativity, and discovery, and how it illuminates cultural history; and\n**(2)**\nofficially designates the Margaret Woodbury Strong Museum as the National Museum of Play.\n##### (b) Effect of recognition; designation\nThe National Museum of Play recognized in subsection (a) is not a unit of the National Park System and the designation under subsection (a) shall not be construed to require or permit Federal funds to be expended for any purpose related to the Museum.",
      "versionDate": "2025-01-07",
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
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-03-03T18:26:24Z"
          },
          {
            "name": "New York State",
            "updateDate": "2025-03-03T18:26:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-02-03T12:04:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr235",
          "measure-number": "235",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr235v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>National Museum of Play Recognition Act</strong></p><p>This bill designates the Margaret Woodbury Strong Museum in Rochester, New York, as the National Museum of Play.</p>"
        },
        "title": "National Museum of Play Recognition Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr235.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>National Museum of Play Recognition Act</strong></p><p>This bill designates the Margaret Woodbury Strong Museum in Rochester, New York, as the National Museum of Play.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr235"
    },
    "title": "National Museum of Play Recognition Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>National Museum of Play Recognition Act</strong></p><p>This bill designates the Margaret Woodbury Strong Museum in Rochester, New York, as the National Museum of Play.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr235"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr235ih.xml"
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
      "title": "National Museum of Play Recognition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Museum of Play Recognition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To recognize the Margaret Woodbury Strong Museum in Rochester, New York.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T04:48:21Z"
    }
  ]
}
```
