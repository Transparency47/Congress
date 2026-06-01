# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/319?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/319
- Title: To authorize an additional district judgeship for the district of Idaho.
- Congress: 119
- Bill type: HR
- Bill number: 319
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-03-07T21:47:55Z
- Update date including text: 2025-03-07T21:47:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/319",
    "number": "319",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "S001148",
        "district": "2",
        "firstName": "Michael",
        "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
        "lastName": "Simpson",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "To authorize an additional district judgeship for the district of Idaho.",
    "type": "HR",
    "updateDate": "2025-03-07T21:47:55Z",
    "updateDateIncludingText": "2025-03-07T21:47:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:36:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr319ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 319\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Simpson (for himself and Mr. Fulcher ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize an additional district judgeship for the district of Idaho.\n#### 1. District judgeship for the district of Idaho\n##### (a) In general\nThe President shall appoint, by and with the advice and consent of the Senate, 1 additional district judge for the district of Idaho.\n##### (b) Technical and conforming amendment\nIn order that the table contained in section 133(a) of title 28, United States Code, will reflect the change in the number of judgeships authorized by subsection (a), such table is amended by striking the item relating to Idaho and inserting the following:\nIdaho 3 .",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-01-09",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "54",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to authorize an additional district judgeship for the district of Idaho.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Federal district courts",
            "updateDate": "2025-02-12T19:20:50Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2025-02-12T19:20:50Z"
          },
          {
            "name": "Judges",
            "updateDate": "2025-02-12T19:20:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-02-10T16:04:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr319",
          "measure-number": "319",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr319v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill increases from two to three the total number of U.S. district court judgeships for the District of Idaho. The President must appoint, with the advice and consent of the Senate, one additional judge for that judicial district.</p>"
        },
        "title": "To authorize an additional district judgeship for the district of Idaho."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr319.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases from two to three the total number of U.S. district court judgeships for the District of Idaho. The President must appoint, with the advice and consent of the Senate, one additional judge for that judicial district.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr319"
    },
    "title": "To authorize an additional district judgeship for the district of Idaho."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases from two to three the total number of U.S. district court judgeships for the District of Idaho. The President must appoint, with the advice and consent of the Senate, one additional judge for that judicial district.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr319"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr319ih.xml"
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
      "title": "To authorize an additional district judgeship for the district of Idaho.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T09:03:18Z"
    },
    {
      "title": "To authorize an additional district judgeship for the district of Idaho.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:28Z"
    }
  ]
}
```
