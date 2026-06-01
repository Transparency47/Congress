# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1292?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1292
- Title: Ensuring the Safety of Our Mail Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1292
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-02-04T04:11:35Z
- Update date including text: 2026-02-04T04:11:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1292",
    "number": "1292",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "Ensuring the Safety of Our Mail Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T04:11:35Z",
    "updateDateIncludingText": "2026-02-04T04:11:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:05:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1292ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1292\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Calvert introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to increase the maximum penalty for mail theft.\n#### 1. Short title\nThis Act may be cited as the Ensuring the Safety of Our Mail Act of 2025 .\n#### 2. Increasing the maximum penalty for mail theft\nSection 1708 of title 18, United States Code, is amended by striking not more than five years and inserting not more than 10 years .",
      "versionDate": "2025-02-13",
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
            "name": "Crimes against property",
            "updateDate": "2025-06-13T18:55:45Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-06-13T18:55:45Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-06-13T18:55:45Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-06-13T18:55:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-14T12:56:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1292",
          "measure-number": "1292",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-04-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1292v00",
            "update-date": "2025-04-25"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ensuring the Safety of Our Mail Act of 2025</strong></p><p>This bill increases from 5 to 10 years the maximum prison term for a defendant who commits mail theft.<strong><br/></strong></p>"
        },
        "title": "Ensuring the Safety of Our Mail Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1292.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring the Safety of Our Mail Act of 2025</strong></p><p>This bill increases from 5 to 10 years the maximum prison term for a defendant who commits mail theft.<strong><br/></strong></p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr1292"
    },
    "title": "Ensuring the Safety of Our Mail Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring the Safety of Our Mail Act of 2025</strong></p><p>This bill increases from 5 to 10 years the maximum prison term for a defendant who commits mail theft.<strong><br/></strong></p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr1292"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1292ih.xml"
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
      "title": "Ensuring the Safety of Our Mail Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring the Safety of Our Mail Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to increase the maximum penalty for mail theft.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:12Z"
    }
  ]
}
```
