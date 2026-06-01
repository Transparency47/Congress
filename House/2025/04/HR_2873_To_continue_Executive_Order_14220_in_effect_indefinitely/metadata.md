# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2873?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2873
- Title: To continue Executive Order 14220 in effect indefinitely.
- Congress: 119
- Bill type: HR
- Bill number: 2873
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-05-15T19:22:22Z
- Update date including text: 2026-05-15T19:22:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2873",
    "number": "2873",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "To continue Executive Order 14220 in effect indefinitely.",
    "type": "HR",
    "updateDate": "2026-05-15T19:22:22Z",
    "updateDateIncludingText": "2026-05-15T19:22:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2873ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2873\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mrs. Miller-Meeks introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo continue Executive Order 14220 in effect indefinitely.\n#### 1. Executive Order 14220\nExecutive Order 14220, entitled Addressing the Threat to National Security From Imports of Copper (90 Fed. Reg. 11001; February 25, 2025), and any action taken or regulation issued by any agency pursuant to such Executive Order shall remain in effect.",
      "versionDate": "2025-04-10",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-22T21:03:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2873",
          "measure-number": "2873",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2873v00",
            "update-date": "2026-05-15"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill provides statutory authority for <a href=\"https://www.federalregister.gov/documents/2025/02/28/2025-03439/addressing-the-threat-to-national-security-from-imports-of-copper\">Executive Order 14220</a> and any action taken or regulation issued by any agency pursuant to the order. This executive order, issued by President Donald J. Trump on\u00a0February 25, 2025,\u00a0directed the Department of Commerce to investigate the effects of copper imports on national security under Section 232 of the Trade Expansion Act of 1962. Section 232 authorizes the President to take action (e.g., impose tariffs) if Commerce determines that imports of a good threaten U.S. national security.\u00a0</p>"
        },
        "title": "To continue Executive Order 14220 in effect indefinitely."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2873.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides statutory authority for <a href=\"https://www.federalregister.gov/documents/2025/02/28/2025-03439/addressing-the-threat-to-national-security-from-imports-of-copper\">Executive Order 14220</a> and any action taken or regulation issued by any agency pursuant to the order. This executive order, issued by President Donald J. Trump on\u00a0February 25, 2025,\u00a0directed the Department of Commerce to investigate the effects of copper imports on national security under Section 232 of the Trade Expansion Act of 1962. Section 232 authorizes the President to take action (e.g., impose tariffs) if Commerce determines that imports of a good threaten U.S. national security.\u00a0</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119hr2873"
    },
    "title": "To continue Executive Order 14220 in effect indefinitely."
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides statutory authority for <a href=\"https://www.federalregister.gov/documents/2025/02/28/2025-03439/addressing-the-threat-to-national-security-from-imports-of-copper\">Executive Order 14220</a> and any action taken or regulation issued by any agency pursuant to the order. This executive order, issued by President Donald J. Trump on\u00a0February 25, 2025,\u00a0directed the Department of Commerce to investigate the effects of copper imports on national security under Section 232 of the Trade Expansion Act of 1962. Section 232 authorizes the President to take action (e.g., impose tariffs) if Commerce determines that imports of a good threaten U.S. national security.\u00a0</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119hr2873"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2873ih.xml"
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
      "title": "To continue Executive Order 14220 in effect indefinitely.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:24Z"
    },
    {
      "title": "To continue Executive Order 14220 in effect indefinitely.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T08:06:50Z"
    }
  ]
}
```
