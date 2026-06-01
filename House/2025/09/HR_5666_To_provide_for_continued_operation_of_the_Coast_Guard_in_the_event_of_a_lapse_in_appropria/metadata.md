# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5666?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5666
- Title: To provide for continued operation of the Coast Guard in the event of a lapse in appropriation.
- Congress: 119
- Bill type: HR
- Bill number: 5666
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-10-16T13:05:03Z
- Update date including text: 2025-10-16T13:05:03Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5666",
    "number": "5666",
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
    "title": "To provide for continued operation of the Coast Guard in the event of a lapse in appropriation.",
    "type": "HR",
    "updateDate": "2025-10-16T13:05:03Z",
    "updateDateIncludingText": "2025-10-16T13:05:03Z"
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
          "date": "2025-09-30T16:01:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5666ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5666\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo provide for continued operation of the Coast Guard in the event of a lapse in appropriation.\n#### 1. Continued operation of Coast Guard\nIn the case of a lapse in appropriations for the Coast Guard, there are appropriated such amounts as may be necessary for the operation of the Coast Guard for the lesser of\u2014\n**(1)**\n30 days; or\n**(2)**\nthe duration of the lapse in appropriation.",
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
        "updateDate": "2025-10-16T13:00:22Z"
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
          "measure-id": "id119hr5666",
          "measure-number": "5666",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2025-10-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5666v00",
            "update-date": "2025-10-16"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill provides appropriations for\u00a0the Coast Guard if there is a lapse in appropriations for the Coast Guard. Specifically, the bill provides the appropriations that are necessary for the operation of the Coast Guard for the lesser of (1) 30 days, or (2) the duration of the lapse in appropriations.</p>"
        },
        "title": "To provide for continued operation of the Coast Guard in the event of a lapse in appropriation."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5666.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides appropriations for\u00a0the Coast Guard if there is a lapse in appropriations for the Coast Guard. Specifically, the bill provides the appropriations that are necessary for the operation of the Coast Guard for the lesser of (1) 30 days, or (2) the duration of the lapse in appropriations.</p>",
      "updateDate": "2025-10-16",
      "versionCode": "id119hr5666"
    },
    "title": "To provide for continued operation of the Coast Guard in the event of a lapse in appropriation."
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides appropriations for\u00a0the Coast Guard if there is a lapse in appropriations for the Coast Guard. Specifically, the bill provides the appropriations that are necessary for the operation of the Coast Guard for the lesser of (1) 30 days, or (2) the duration of the lapse in appropriations.</p>",
      "updateDate": "2025-10-16",
      "versionCode": "id119hr5666"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5666ih.xml"
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
      "title": "To provide for continued operation of the Coast Guard in the event of a lapse in appropriation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-15T02:18:15Z"
    },
    {
      "title": "To provide for continued operation of the Coast Guard in the event of a lapse in appropriation.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:06:06Z"
    }
  ]
}
```
