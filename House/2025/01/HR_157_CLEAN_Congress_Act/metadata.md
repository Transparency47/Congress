# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/157
- Title: CLEAN Congress Act
- Congress: 119
- Bill type: HR
- Bill number: 157
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-10T19:41:39Z
- Update date including text: 2025-02-10T19:41:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/157",
    "number": "157",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "CLEAN Congress Act",
    "type": "HR",
    "updateDate": "2025-02-10T19:41:39Z",
    "updateDateIncludingText": "2025-02-10T19:41:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:09:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr157ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 157\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Fitzpatrick introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit a single bill or joint resolution presented by Congress to the President from containing multiple subjects and to require the equal application of laws to Members of Congress.\n#### 1. Short title\nThis Act may be cited as the Citizen Legislature Anti-Corruption Reform of Congress Act or the CLEAN Congress Act .\n#### 2. Prohibiting multiple subjects in single bill\n##### (a) In general\nEach bill, order, resolution, or vote submitted by Congress to the President under section 7 of article I of the Constitution of the United States shall embrace no more than one subject, and that subject shall be clearly and descriptively expressed in the title of the bill, order, resolution or vote.\n##### (b) Effective date\nSubsection (a) shall apply with respect to the One Hundred Nineteenth Congress and each succeeding Congress.\n#### 3. Requiring equal application of laws to Members of Congress\n##### (a) In general\nNotwithstanding any other provision of law, any provision of law that provides an exception in its application to a Member of Congress or an employee of the office of a Member of Congress shall have no effect.\n##### (b) Clarification relating to exercise of official or representational duties\nSubsection (a) shall not be construed to apply to provisions of law or rules which permit Members of Congress or employees of offices of Members of Congress to carry out official duties that are tied directly to lawmaking, including provisions or rules permitting Members and employees to enter and use the United States Capitol, the United States Capitol grounds, and other buildings and facilities.\n##### (c) Definition\nIn this section, the term Member of Congress means a Senator or a Representative in, or Delegate or Resident Commissioner to, the Congress.",
      "versionDate": "2025-01-03",
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
            "name": "Congressional officers and employees",
            "updateDate": "2025-02-05T16:06:22Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-02-05T16:06:30Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-02-05T16:06:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-03T18:26:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr157",
          "measure-number": "157",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr157v00",
            "update-date": "2025-02-10"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Citizen Legislature Anti-Corruption Reform of Congress Act or the CLEAN Congress Act</b></p> <p>This bill (1) requires bills, orders, resolutions, or votes submitted by Congress to the President to include only one subject that is clearly and descriptively expressed in the measure's title; and (2) makes ineffective any provision of law that excludes its application to a Member of Congress or to an employee in a Member's office.</p>"
        },
        "title": "CLEAN Congress Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr157.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Citizen Legislature Anti-Corruption Reform of Congress Act or the CLEAN Congress Act</b></p> <p>This bill (1) requires bills, orders, resolutions, or votes submitted by Congress to the President to include only one subject that is clearly and descriptively expressed in the measure's title; and (2) makes ineffective any provision of law that excludes its application to a Member of Congress or to an employee in a Member's office.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr157"
    },
    "title": "CLEAN Congress Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Citizen Legislature Anti-Corruption Reform of Congress Act or the CLEAN Congress Act</b></p> <p>This bill (1) requires bills, orders, resolutions, or votes submitted by Congress to the President to include only one subject that is clearly and descriptively expressed in the measure's title; and (2) makes ineffective any provision of law that excludes its application to a Member of Congress or to an employee in a Member's office.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr157"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr157ih.xml"
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
      "title": "CLEAN Congress Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAN Congress Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Citizen Legislature Anti-Corruption Reform of Congress Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit a single bill or joint resolution presented by Congress to the President from containing multiple subjects and to require the equal application of laws to Members of Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T04:48:34Z"
    }
  ]
}
```
