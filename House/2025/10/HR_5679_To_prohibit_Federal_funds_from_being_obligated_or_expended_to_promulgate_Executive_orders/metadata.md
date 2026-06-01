# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5679?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5679
- Title: TRUMP Act
- Congress: 119
- Bill type: HR
- Bill number: 5679
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2025-10-21T13:32:23Z
- Update date including text: 2025-10-21T13:32:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-10-03: Introduced in House

## Actions

- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5679",
    "number": "5679",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001119",
        "district": "2",
        "firstName": "Angie",
        "fullName": "Rep. Craig, Angie [D-MN-2]",
        "lastName": "Craig",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "TRUMP Act",
    "type": "HR",
    "updateDate": "2025-10-21T13:32:23Z",
    "updateDateIncludingText": "2025-10-21T13:32:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:31:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5679ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5679\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Ms. Craig introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit Federal funds from being obligated or expended to promulgate Executive orders during a lapse in discretionary appropriations.\n#### 1. Short title\nThis Act may be cited as the Termination of Reckless Unchecked Mandates from this President Act or the TRUMP Act .\n#### 2. Limitation on Executive orders during lapse in appropriations\nDuring any period of a lapse in discretionary appropriations beginning on or after the date of the enactment of this Act, no Federal funds may be obligated or expended to promulgate or issue any Executive order or presidential memorandum.",
      "versionDate": "2025-10-03",
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
        "updateDate": "2025-10-21T13:24:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
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
          "measure-id": "id119hr5679",
          "measure-number": "5679",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-03",
          "originChamber": "HOUSE",
          "update-date": "2025-10-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5679v00",
            "update-date": "2025-10-21"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Termination of Reckless Unchecked Mandates from this President Act or the TRUMP Act</strong></p><p>This bill prohibits federal funds from being obligated or expended to promulgate or issue any executive order or presidential memorandum during a lapse in discretionary appropriations (i.e., government shutdown).\u00a0</p>"
        },
        "title": "TRUMP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5679.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Termination of Reckless Unchecked Mandates from this President Act or the TRUMP Act</strong></p><p>This bill prohibits federal funds from being obligated or expended to promulgate or issue any executive order or presidential memorandum during a lapse in discretionary appropriations (i.e., government shutdown).\u00a0</p>",
      "updateDate": "2025-10-21",
      "versionCode": "id119hr5679"
    },
    "title": "TRUMP Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Termination of Reckless Unchecked Mandates from this President Act or the TRUMP Act</strong></p><p>This bill prohibits federal funds from being obligated or expended to promulgate or issue any executive order or presidential memorandum during a lapse in discretionary appropriations (i.e., government shutdown).\u00a0</p>",
      "updateDate": "2025-10-21",
      "versionCode": "id119hr5679"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5679ih.xml"
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
      "title": "To prohibit Federal funds from being obligated or expended to promulgate Executive orders during a lapse in discretionary appropriations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T08:05:13Z"
    },
    {
      "title": "TRUMP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRUMP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Termination of Reckless Unchecked Mandates from this President Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:14Z"
    }
  ]
}
```
