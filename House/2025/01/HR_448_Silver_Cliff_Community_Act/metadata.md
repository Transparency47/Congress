# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/448?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/448
- Title: Silver Cliff Community Act
- Congress: 119
- Bill type: HR
- Bill number: 448
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-02-19T21:43:20Z
- Update date including text: 2025-02-19T21:43:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/448",
    "number": "448",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Silver Cliff Community Act",
    "type": "HR",
    "updateDate": "2025-02-19T21:43:20Z",
    "updateDateIncludingText": "2025-02-19T21:43:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:01:30Z",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr448ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 448\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Pettersen (for herself and Ms. Boebert ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct the United States Postal Service to designate a single, unique ZIP Code for Silver Cliff, Colorado, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Silver Cliff Community Act .\n#### 2. Single, unique ZIP Code for Silver Cliff, Colorado\nNot later than 180 days after the date of the enactment of this Act, the United States Postal Service shall designate a single, unique ZIP Code, to be numbered 81249, applicable to the area encompassing only Silver Cliff, Colorado.",
      "versionDate": "2025-01-15",
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
        "updateDate": "2025-02-19T16:00:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr448",
          "measure-number": "448",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr448v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Silver Cliff Community Act</strong></p><p>This bill directs the U.S. Postal Service to designate ZIP Code 81249 to the area encompassing only Silver Cliff, Colorado.</p>"
        },
        "title": "Silver Cliff Community Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr448.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Silver Cliff Community Act</strong></p><p>This bill directs the U.S. Postal Service to designate ZIP Code 81249 to the area encompassing only Silver Cliff, Colorado.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr448"
    },
    "title": "Silver Cliff Community Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Silver Cliff Community Act</strong></p><p>This bill directs the U.S. Postal Service to designate ZIP Code 81249 to the area encompassing only Silver Cliff, Colorado.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr448"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr448ih.xml"
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
      "title": "Silver Cliff Community Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Silver Cliff Community Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the United States Postal Service to designate a single, unique ZIP Code for Silver Cliff, Colorado, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:22Z"
    }
  ]
}
```
