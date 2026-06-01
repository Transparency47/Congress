# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2260?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2260
- Title: To designate the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the "Richard H. Poff Post Office Building".
- Congress: 119
- Bill type: HR
- Bill number: 2260
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-12-08T15:32:17Z
- Update date including text: 2025-12-08T15:32:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2260",
    "number": "2260",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000568",
        "district": "9",
        "firstName": "H.",
        "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
        "lastName": "Griffith",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the \"Richard H. Poff Post Office Building\".",
    "type": "HR",
    "updateDate": "2025-12-08T15:32:17Z",
    "updateDateIncludingText": "2025-12-08T15:32:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
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
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:02:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2260ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2260\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Griffith introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the Richard H. Poff Post Office Building .\n#### 1. Richard H. Poff Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, shall be known and designated as the Richard H. Poff Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Richard H. Poff Post Office Building .",
      "versionDate": "2025-03-21",
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
            "name": "Congressional tributes",
            "updateDate": "2025-08-13T13:41:44Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-08-13T13:41:44Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-08-13T13:41:44Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-08-13T13:41:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-05T17:54:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hr2260",
          "measure-number": "2260",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2260v00",
            "update-date": "2025-08-01"
          },
          "action-date": "2025-03-21",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the \"Richard H. Poff Post Office Building\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the \"Richard H. Poff Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2260.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the \"Richard H. Poff Post Office Building\".",
      "updateDate": "2025-08-01",
      "versionCode": "id119hr2260"
    },
    "title": "To designate the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the \"Richard H. Poff Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the \"Richard H. Poff Post Office Building\".",
      "updateDate": "2025-08-01",
      "versionCode": "id119hr2260"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2260ih.xml"
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
      "title": "To designate the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the \"Richard H. Poff Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T01:48:27Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 901 West Main Street in Radford, Virginia, as the \"Richard H. Poff Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T08:05:48Z"
    }
  ]
}
```
