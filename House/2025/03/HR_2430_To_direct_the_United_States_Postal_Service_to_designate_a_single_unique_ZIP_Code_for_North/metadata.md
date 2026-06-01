# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2430?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2430
- Title: To direct the United States Postal Service to designate a single, unique ZIP Code for Northlake, Texas.
- Congress: 119
- Bill type: HR
- Bill number: 2430
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-06-30T22:22:56Z
- Update date including text: 2025-06-30T22:22:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2430",
    "number": "2430",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000603",
        "district": "26",
        "firstName": "Brandon",
        "fullName": "Rep. Gill, Brandon [R-TX-26]",
        "lastName": "Gill",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Northlake, Texas.",
    "type": "HR",
    "updateDate": "2025-06-30T22:22:56Z",
    "updateDateIncludingText": "2025-06-30T22:22:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:06:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2430ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2430\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Gill of Texas introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct the United States Postal Service to designate a single, unique ZIP Code for Northlake, Texas.\n#### 1. Single, unique ZIP Code for Northlake, Texas\nNot later than 270 days after the enactment of this section, the United States Postal service shall designate a single, unique ZIP Code applicable to the area encompassing solely Northlake, Texas.",
      "versionDate": "2025-03-27",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-21T17:53:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2430",
          "measure-number": "2430",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2025-06-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2430v00",
            "update-date": "2025-06-30"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill directs the U.S. Postal Service to designate a single, unique ZIP Code for Northlake, Texas.</p>"
        },
        "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Northlake, Texas."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2430.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the U.S. Postal Service to designate a single, unique ZIP Code for Northlake, Texas.</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2430"
    },
    "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Northlake, Texas."
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the U.S. Postal Service to designate a single, unique ZIP Code for Northlake, Texas.</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2430"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2430ih.xml"
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
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Northlake, Texas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T09:18:22Z"
    },
    {
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Northlake, Texas.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T08:06:55Z"
    }
  ]
}
```
