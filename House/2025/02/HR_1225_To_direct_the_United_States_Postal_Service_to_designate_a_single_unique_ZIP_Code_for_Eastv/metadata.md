# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1225?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1225
- Title: To direct the United States Postal Service to designate a single, unique ZIP Code for Eastvale, California.
- Congress: 119
- Bill type: HR
- Bill number: 1225
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-06-06T18:16:26Z
- Update date including text: 2025-06-06T18:16:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1225",
    "number": "1225",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C000059",
        "district": "41",
        "firstName": "Ken",
        "fullName": "Rep. Calvert, Ken [R-CA-41]",
        "lastName": "Calvert",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Eastvale, California.",
    "type": "HR",
    "updateDate": "2025-06-06T18:16:26Z",
    "updateDateIncludingText": "2025-06-06T18:16:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:01:50Z",
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
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1225ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1225\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Calvert (for himself and Mrs. Torres of California ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct the United States Postal Service to designate a single, unique ZIP Code for Eastvale, California.\n#### 1. Single, unique ZIP code for Eastvale, California\nNot later than 180 days after the date of enactment of this section, the United States Postal Service shall designate a single, unique ZIP Code applicable to the area encompassing solely Eastvale, California.",
      "versionDate": "2025-02-12",
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
            "name": "California",
            "updateDate": "2025-05-02T14:58:24Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-05-02T14:58:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-24T12:53:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1225",
          "measure-number": "1225",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-06-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1225v00",
            "update-date": "2025-06-06"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill directs the U.S. Postal Service to designate a single, unique ZIP Code for Eastvale, California. </p>"
        },
        "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Eastvale, California."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1225.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the U.S. Postal Service to designate a single, unique ZIP Code for Eastvale, California. </p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119hr1225"
    },
    "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Eastvale, California."
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the U.S. Postal Service to designate a single, unique ZIP Code for Eastvale, California. </p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119hr1225"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1225ih.xml"
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
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Eastvale, California.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T11:18:21Z"
    },
    {
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Eastvale, California.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:06:23Z"
    }
  ]
}
```
