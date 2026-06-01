# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3337?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3337
- Title: To designate the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the "Deputy Samuel Kent Brownlee Post Office".
- Congress: 119
- Bill type: HR
- Bill number: 3337
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-05-22T08:08:51Z
- Update date including text: 2026-05-22T08:08:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3337",
    "number": "3337",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the \"Deputy Samuel Kent Brownlee Post Office\".",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:51Z",
    "updateDateIncludingText": "2026-05-22T08:08:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "CO"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "CO"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "CO"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CO"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CO"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3337ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3337\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Evans of Colorado (for himself, Mr. Crank , Mr. Hurd of Colorado , Ms. Boebert , and Mr. Neguse ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the Deputy Samuel Kent Brownlee Post Office .\n#### 1. Deputy samuel kent brownlee post office\n##### (a) Designation\nThe facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, shall be known and designated as the Deputy Samuel Kent Brownlee Post Office .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Deputy Samuel Kent Brownlee Post Office .",
      "versionDate": "2025-05-13",
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
            "name": "Colorado",
            "updateDate": "2025-08-13T13:41:09Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-08-13T13:41:03Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-08-13T13:41:03Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-08-13T13:41:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-14T18:41:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-13",
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
          "measure-id": "id119hr3337",
          "measure-number": "3337",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-13",
          "originChamber": "HOUSE",
          "update-date": "2025-08-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3337v00",
            "update-date": "2025-08-01"
          },
          "action-date": "2025-05-13",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the \"Deputy Samuel Kent Brownlee Post Office\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the \"Deputy Samuel Kent Brownlee Post Office\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3337.xml",
    "summary": {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the \"Deputy Samuel Kent Brownlee Post Office\".",
      "updateDate": "2025-08-01",
      "versionCode": "id119hr3337"
    },
    "title": "To designate the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the \"Deputy Samuel Kent Brownlee Post Office\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the \"Deputy Samuel Kent Brownlee Post Office\".",
      "updateDate": "2025-08-01",
      "versionCode": "id119hr3337"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3337ih.xml"
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
      "title": "To designate the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the \"Deputy Samuel Kent Brownlee Post Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:48:26Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 3344 11th Avenue in Evans, Colorado, as the \"Deputy Samuel Kent Brownlee Post Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T08:06:00Z"
    }
  ]
}
```
