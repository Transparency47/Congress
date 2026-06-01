# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/229
- Title: To prohibit the implementation of the Rock Springs Field Office Record of Decision and Approved Resource Management Plan.
- Congress: 119
- Bill type: HR
- Bill number: 229
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-03-19T15:13:15Z
- Update date including text: 2025-03-19T15:13:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/229",
    "number": "229",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "To prohibit the implementation of the Rock Springs Field Office Record of Decision and Approved Resource Management Plan.",
    "type": "HR",
    "updateDate": "2025-03-19T15:13:15Z",
    "updateDateIncludingText": "2025-03-19T15:13:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr229ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 229\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo prohibit the implementation of the Rock Springs Field Office Record of Decision and Approved Resource Management Plan.\n#### 1. Prohibition on implementation\nThe Secretary of the Interior shall not implement, administer, or enforce the Rock Springs Field Office Record of Decision and Approved Resource Management Plan, published by the Bureau of Land Management and dated December 2024.",
      "versionDate": "2025-01-07",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-19T15:12:54Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-03-19T15:13:04Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-03-19T15:13:15Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2025-03-19T15:13:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-03-10T19:47:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr229",
          "measure-number": "229",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr229v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits the Bureau of Land Management\u00a0from implementing, administering, or enforcing the Rock Springs Field Office Record of Decision and Approved Resource Management Plan, which was published on December 20, 2024. The plan\u00a0includes\u00a0guidance for managing public lands administered by the office and located in Lincoln, Sweetwater, Uinta, Sublette, and Fremont Counties in southwestern Wyoming.</p>"
        },
        "title": "To prohibit the implementation of the Rock Springs Field Office Record of Decision and Approved Resource Management Plan."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr229.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the Bureau of Land Management\u00a0from implementing, administering, or enforcing the Rock Springs Field Office Record of Decision and Approved Resource Management Plan, which was published on December 20, 2024. The plan\u00a0includes\u00a0guidance for managing public lands administered by the office and located in Lincoln, Sweetwater, Uinta, Sublette, and Fremont Counties in southwestern Wyoming.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr229"
    },
    "title": "To prohibit the implementation of the Rock Springs Field Office Record of Decision and Approved Resource Management Plan."
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the Bureau of Land Management\u00a0from implementing, administering, or enforcing the Rock Springs Field Office Record of Decision and Approved Resource Management Plan, which was published on December 20, 2024. The plan\u00a0includes\u00a0guidance for managing public lands administered by the office and located in Lincoln, Sweetwater, Uinta, Sublette, and Fremont Counties in southwestern Wyoming.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr229"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr229ih.xml"
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
      "title": "To prohibit the implementation of the Rock Springs Field Office Record of Decision and Approved Resource Management Plan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T09:03:32Z"
    },
    {
      "title": "To prohibit the implementation of the Rock Springs Field Office Record of Decision and Approved Resource Management Plan.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-08T09:05:25Z"
    }
  ]
}
```
