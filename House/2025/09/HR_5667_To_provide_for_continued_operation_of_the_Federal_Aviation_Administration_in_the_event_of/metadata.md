# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5667?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5667
- Title: To provide for continued operation of the Federal Aviation Administration in the event of a lapse in appropriations.
- Congress: 119
- Bill type: HR
- Bill number: 5667
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-10-20T13:41:14Z
- Update date including text: 2025-10-20T13:41:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5667",
    "number": "5667",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "To provide for continued operation of the Federal Aviation Administration in the event of a lapse in appropriations.",
    "type": "HR",
    "updateDate": "2025-10-20T13:41:14Z",
    "updateDateIncludingText": "2025-10-20T13:41:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5667ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5667\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo provide for continued operation of the Federal Aviation Administration in the event of a lapse in appropriations.\n#### 1. Continued operation of Federal Aviation Administration\nIn the case of a lapse in appropriation for the Federal Aviation Administration, there are appropriated such amounts as may be necessary for the operation of such Administration for the lesser of\u2014\n**(1)**\n30 days; or\n**(2)**\nthe duration of the lapse in appropriations.",
      "versionDate": "2025-09-30",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-10-20T13:25:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119hr5667",
          "measure-number": "5667",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2025-10-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5667v00",
            "update-date": "2025-10-20"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill provides appropriations for the Federal Aviation Administration (FAA) if there is a lapse in appropriations for the FAA. Specifically, the bill provides the appropriations that are necessary for the operation of the FAA for the lesser of (1) 30 days, or (2) the duration of the lapse in appropriations.</p>"
        },
        "title": "To provide for continued operation of the Federal Aviation Administration in the event of a lapse in appropriations."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5667.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides appropriations for the Federal Aviation Administration (FAA) if there is a lapse in appropriations for the FAA. Specifically, the bill provides the appropriations that are necessary for the operation of the FAA for the lesser of (1) 30 days, or (2) the duration of the lapse in appropriations.</p>",
      "updateDate": "2025-10-20",
      "versionCode": "id119hr5667"
    },
    "title": "To provide for continued operation of the Federal Aviation Administration in the event of a lapse in appropriations."
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides appropriations for the Federal Aviation Administration (FAA) if there is a lapse in appropriations for the FAA. Specifically, the bill provides the appropriations that are necessary for the operation of the FAA for the lesser of (1) 30 days, or (2) the duration of the lapse in appropriations.</p>",
      "updateDate": "2025-10-20",
      "versionCode": "id119hr5667"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5667ih.xml"
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
      "title": "To provide for continued operation of the Federal Aviation Administration in the event of a lapse in appropriations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T08:05:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for continued operation of the Federal Aviation Administration in the event of a lapse in appropriations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T08:05:13Z"
    }
  ]
}
```
