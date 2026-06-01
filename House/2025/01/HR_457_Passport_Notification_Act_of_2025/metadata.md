# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/457
- Title: Passport Notification Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 457
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-04-02T16:18:54Z
- Update date including text: 2025-04-02T16:18:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/457",
    "number": "457",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Passport Notification Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-02T16:18:54Z",
    "updateDateIncludingText": "2025-04-02T16:18:54Z"
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
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
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
          "date": "2025-01-15T15:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr457ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 457\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo direct the Assistant Secretary of State for Consular Affairs to notify United States citizens regarding passport expiration and renewal, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Passport Notification Act of 2025 .\n#### 2. Required notification regarding passport expiration and renewal\n##### (a) Requirement\nFor each United States citizen in possession of a valid unexpired passport, not later than 180 days prior to the date on which such passport is scheduled to expire, the Assistant Secretary of State for Consular Affairs shall provide to the United States citizen\u2014\n**(1)**\na notification regarding such pending expiration date; and\n**(2)**\ninformation on the process for the renewal of such passport, including an identification of any relevant locations at which materials required for such renewal may be submitted.\n##### (b) Form\nEach notification required under subsection (a) may be submitted in electronic or paper form.\n##### (c) Applicability\nThe requirement under subsection (a) shall apply with respect to passports the expiration of which is scheduled to occur on or after the date that is 180 days after the date of the enactment of this Act.",
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
        "name": "Immigration",
        "updateDate": "2025-02-14T15:40:24Z"
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
          "measure-id": "id119hr457",
          "measure-number": "457",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr457v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Passport Notification Act of 2025</strong></p><p>This bill requires the Bureau of Consular Affairs to notify U.S. citizens at least 180 days prior to the date on which their passport is scheduled to expire. The notification must include information on the process for renewal and identify locations where renewal applications may be submitted. The notification may be in electronic or paper form.</p>"
        },
        "title": "Passport Notification Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr457.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Passport Notification Act of 2025</strong></p><p>This bill requires the Bureau of Consular Affairs to notify U.S. citizens at least 180 days prior to the date on which their passport is scheduled to expire. The notification must include information on the process for renewal and identify locations where renewal applications may be submitted. The notification may be in electronic or paper form.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr457"
    },
    "title": "Passport Notification Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Passport Notification Act of 2025</strong></p><p>This bill requires the Bureau of Consular Affairs to notify U.S. citizens at least 180 days prior to the date on which their passport is scheduled to expire. The notification must include information on the process for renewal and identify locations where renewal applications may be submitted. The notification may be in electronic or paper form.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr457"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr457ih.xml"
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
      "title": "Passport Notification Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Passport Notification Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Assistant Secretary of State for Consular Affairs to notify United States citizens regarding passport expiration and renewal, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T04:18:27Z"
    }
  ]
}
```
