# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/230
- Title: To prohibit the implementation of the Approved Resource Management Plan Amendment for the Buffalo, Wyoming Field Office of the Bureau of Land Management.
- Congress: 119
- Bill type: HR
- Bill number: 230
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-03-25T16:33:21Z
- Update date including text: 2025-03-25T16:33:21Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/230",
    "number": "230",
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
    "title": "To prohibit the implementation of the Approved Resource Management Plan Amendment for the Buffalo, Wyoming Field Office of the Bureau of Land Management.",
    "type": "HR",
    "updateDate": "2025-03-25T16:33:21Z",
    "updateDateIncludingText": "2025-03-25T16:33:21Z"
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
          "date": "2025-01-07T16:01:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr230ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 230\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo prohibit the implementation of the Approved Resource Management Plan Amendment for the Buffalo, Wyoming Field Office of the Bureau of Land Management.\n#### 1. Restriction on Approved Resource Management Plan Amendment for Buffalo, Wyoming Field Office of Bureau of Land Management\nThe Secretary of the Interior may not implement, administer, or enforce the Approved Resource Management Plan Amendment for the Buffalo, Wyoming Field Office of the Bureau of Land Management referred to in the notice of availability published by the Bureau of Land Management titled Notice of Availability of the Record of Decision and Approved Resource Management Plan Amendment for the Buffalo Field Office, Wyoming (89 Fed. Reg. 93650; published November 27, 2024).",
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
            "updateDate": "2025-03-19T15:02:22Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2025-03-19T15:02:45Z"
          },
          {
            "name": "Coal",
            "updateDate": "2025-03-19T15:02:39Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-03-19T15:02:28Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-03-19T15:02:34Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2025-03-19T15:02:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-03-10T19:44:52Z"
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
          "measure-id": "id119hr230",
          "measure-number": "230",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-03-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr230v00",
            "update-date": "2025-03-25"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits the Bureau of Land Management (BLM) from implementing, administering, or enforcing its 2024 Approved Resource Management Plan Amendment for its Buffalo Field Office in Wyoming. The field office manages 780,291 acres of public lands and 4,731,140 acres of mineral estates within Campbell, Johnson, and Sheridan Counties in north-central Wyoming.</p><p>In 2015, the\u00a0BLM published a management plan for the field office that allowed leases of certain public lands or mineral estates\u00a0within the office's planning area for the development of coal.\u00a0</p><p>In 2018, the U.S. District Court for the District of Montana in\u00a0<em>Western Organization of Resource Councils v. Bureau of Land Management\u00a0</em>ordered the BLM to complete a new environmental impact statement\u00a0(EIS) for the management plan under the National Environmental Policy Act of 1969, which requires an agency to include all reasonable alternatives to its action and the environmental impacts resulting from the action. Specifically, the court ordered the\u00a0BLM to issue an EIS that considers an alternative of not leasing coal under the management plan as well as an alternative that limits the amount of coal potentially available for leasing.</p><p>In response to the court order, the BLM published an amendment to the plan on November 27, 2024. The amended plan made no acres within the office's planning area available for future coal leasing in order to reduce greenhouse gas emissions. However, it allowed existing coal leases to be developed.</p>"
        },
        "title": "To prohibit the implementation of the Approved Resource Management Plan Amendment for the Buffalo, Wyoming Field Office of the Bureau of Land Management."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr230.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the Bureau of Land Management (BLM) from implementing, administering, or enforcing its 2024 Approved Resource Management Plan Amendment for its Buffalo Field Office in Wyoming. The field office manages 780,291 acres of public lands and 4,731,140 acres of mineral estates within Campbell, Johnson, and Sheridan Counties in north-central Wyoming.</p><p>In 2015, the\u00a0BLM published a management plan for the field office that allowed leases of certain public lands or mineral estates\u00a0within the office's planning area for the development of coal.\u00a0</p><p>In 2018, the U.S. District Court for the District of Montana in\u00a0<em>Western Organization of Resource Councils v. Bureau of Land Management\u00a0</em>ordered the BLM to complete a new environmental impact statement\u00a0(EIS) for the management plan under the National Environmental Policy Act of 1969, which requires an agency to include all reasonable alternatives to its action and the environmental impacts resulting from the action. Specifically, the court ordered the\u00a0BLM to issue an EIS that considers an alternative of not leasing coal under the management plan as well as an alternative that limits the amount of coal potentially available for leasing.</p><p>In response to the court order, the BLM published an amendment to the plan on November 27, 2024. The amended plan made no acres within the office's planning area available for future coal leasing in order to reduce greenhouse gas emissions. However, it allowed existing coal leases to be developed.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr230"
    },
    "title": "To prohibit the implementation of the Approved Resource Management Plan Amendment for the Buffalo, Wyoming Field Office of the Bureau of Land Management."
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the Bureau of Land Management (BLM) from implementing, administering, or enforcing its 2024 Approved Resource Management Plan Amendment for its Buffalo Field Office in Wyoming. The field office manages 780,291 acres of public lands and 4,731,140 acres of mineral estates within Campbell, Johnson, and Sheridan Counties in north-central Wyoming.</p><p>In 2015, the\u00a0BLM published a management plan for the field office that allowed leases of certain public lands or mineral estates\u00a0within the office's planning area for the development of coal.\u00a0</p><p>In 2018, the U.S. District Court for the District of Montana in\u00a0<em>Western Organization of Resource Councils v. Bureau of Land Management\u00a0</em>ordered the BLM to complete a new environmental impact statement\u00a0(EIS) for the management plan under the National Environmental Policy Act of 1969, which requires an agency to include all reasonable alternatives to its action and the environmental impacts resulting from the action. Specifically, the court ordered the\u00a0BLM to issue an EIS that considers an alternative of not leasing coal under the management plan as well as an alternative that limits the amount of coal potentially available for leasing.</p><p>In response to the court order, the BLM published an amendment to the plan on November 27, 2024. The amended plan made no acres within the office's planning area available for future coal leasing in order to reduce greenhouse gas emissions. However, it allowed existing coal leases to be developed.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr230"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr230ih.xml"
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
      "title": "To prohibit the implementation of the Approved Resource Management Plan Amendment for the Buffalo, Wyoming Field Office of the Bureau of Land Management.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:25Z"
    },
    {
      "title": "To prohibit the implementation of the Approved Resource Management Plan Amendment for the Buffalo, Wyoming Field Office of the Bureau of Land Management.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-08T09:05:25Z"
    }
  ]
}
```
