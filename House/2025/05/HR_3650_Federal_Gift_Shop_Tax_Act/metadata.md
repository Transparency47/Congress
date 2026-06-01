# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3650?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3650
- Title: Federal Gift Shop Tax Act
- Congress: 119
- Bill type: HR
- Bill number: 3650
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-04-14T13:43:31Z
- Update date including text: 2026-04-14T13:43:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3650",
    "number": "3650",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Federal Gift Shop Tax Act",
    "type": "HR",
    "updateDate": "2026-04-14T13:43:31Z",
    "updateDateIncludingText": "2026-04-14T13:43:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:04:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3650ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3650\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo permit a State to impose a sales tax on qualifying purchases at any gift shop on Federal property, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Gift Shop Tax Act .\n#### 2. Sales tax in gift shops\n##### (a) In general\nA State may levy a sales tax on qualifying purchases made from any gift shop located on Federal property.\n##### (b) Definitions\nIn this section:\n**(1) Federal property**\nThe term Federal property means any building, land, or other real property owned, leased, or occupied by a department, agency, or instrumentality of the United States, or any other instrumentality wholly owned by the United States, including any facility or property of the Smithsonian Institution, the National Gallery of Art, the John F. Kennedy Center for the Performing Arts, and the United States Holocaust Memorial Museum.\n**(2) Qualifying purchase**\nThe term qualifying purchase means any purchase made in the gift shop or made online through the gift shop.\n**(3) State**\nThe term State means each State of the United States, the District of Columbia, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, the Commonwealth of Puerto Rico, the United States Virgin Islands, any other territory or possession of the United States, and any political subdivision of the foregoing.",
      "versionDate": "2025-05-29",
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
        "name": "Taxation",
        "updateDate": "2025-06-10T22:46:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-29",
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
          "measure-id": "id119hr3650",
          "measure-number": "3650",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-29",
          "originChamber": "HOUSE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3650v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-05-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Federal Gift Shop Tax Act</strong></p><p>This bill allows each U.S. state, the District of Columbia, American Samoa, Guam, the Northern\u00a0Mariana Islands, Puerto Rico, and the U.S. Virgin Islands (or a political subdivision of the state or territory)\u00a0to impose a sales tax on any purchase made in\u00a0person or online at\u00a0a gift shop located on federal property.</p>"
        },
        "title": "Federal Gift Shop Tax Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3650.xml",
    "summary": {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Gift Shop Tax Act</strong></p><p>This bill allows each U.S. state, the District of Columbia, American Samoa, Guam, the Northern\u00a0Mariana Islands, Puerto Rico, and the U.S. Virgin Islands (or a political subdivision of the state or territory)\u00a0to impose a sales tax on any purchase made in\u00a0person or online at\u00a0a gift shop located on federal property.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr3650"
    },
    "title": "Federal Gift Shop Tax Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Gift Shop Tax Act</strong></p><p>This bill allows each U.S. state, the District of Columbia, American Samoa, Guam, the Northern\u00a0Mariana Islands, Puerto Rico, and the U.S. Virgin Islands (or a political subdivision of the state or territory)\u00a0to impose a sales tax on any purchase made in\u00a0person or online at\u00a0a gift shop located on federal property.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr3650"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3650ih.xml"
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
      "title": "Federal Gift Shop Tax Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Gift Shop Tax Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To permit a State to impose a sales tax on qualifying purchases at any gift shop on Federal property, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T05:18:31Z"
    }
  ]
}
```
