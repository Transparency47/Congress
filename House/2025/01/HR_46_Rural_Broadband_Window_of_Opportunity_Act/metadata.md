# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/46?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/46
- Title: Rural Broadband Window of Opportunity Act
- Congress: 119
- Bill type: HR
- Bill number: 46
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-04-14T13:41:21Z
- Update date including text: 2025-04-14T13:41:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/46",
    "number": "46",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Rural Broadband Window of Opportunity Act",
    "type": "HR",
    "updateDate": "2025-04-14T13:41:21Z",
    "updateDateIncludingText": "2025-04-14T13:41:21Z"
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
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
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
          "date": "2025-01-03T16:27:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr46ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 46\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Bergman introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Federal Communications Commission to prioritize the timely processing of certain long-form applications in the Rural Digital Opportunity Fund Phase II auction.\n#### 1. Short title\nThis Act may be cited as the Rural Broadband Window of Opportunity Act .\n#### 2. Purpose\nThe purpose of this Act is to level the playing field for service providers participating in the Rural Digital Opportunity Fund that are disadvantaged by short construction seasons.\n#### 3. Application Processing Prioritization\nWith respect to the long-form applicants of the Rural Digital Opportunity Fund Phase II auction provided for in the Report and Order in the matter of Rural Digital Opportunity Fund and Connect America Fund adopted by the Federal Communications Commission (in this section referred to as the Commission ) on January 30, 2020 (FCC 20\u20135), the Commission shall prioritize the timely processing of long-form applications and any subsequent paperwork (in this section referred to as the applications ) submitted by the long-form applicants as follows: The Commission shall prioritize the timely processing of applications which are proposing to provide service in geographic areas which the Commission determines to have the shortest construction seasons (such as in areas characterized by long winters with heavy snowfall).",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-02-04T13:08:47Z"
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
          "measure-id": "id119hr46",
          "measure-number": "46",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr46v00",
            "update-date": "2025-04-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rural Broadband Window of Opportunity Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to prioritize the processing of applications for certain rural broadband expansion projects that are located in areas with the shortest construction seasons (e.g., areas with long winters and heavy snowfall).</p><p>Specifically, the FCC must prioritize processing such applications for the Rural Digital Opportunity Fund (RDOF) Phase II auction, which aims to facilitate the provision of broadband service to\u00a0areas\u00a0that are\u00a0partially served. (The RDOF program's first phase, which is focused on broadband service for wholly unserved areas, is underway.)</p>"
        },
        "title": "Rural Broadband Window of Opportunity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr46.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Broadband Window of Opportunity Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to prioritize the processing of applications for certain rural broadband expansion projects that are located in areas with the shortest construction seasons (e.g., areas with long winters and heavy snowfall).</p><p>Specifically, the FCC must prioritize processing such applications for the Rural Digital Opportunity Fund (RDOF) Phase II auction, which aims to facilitate the provision of broadband service to\u00a0areas\u00a0that are\u00a0partially served. (The RDOF program's first phase, which is focused on broadband service for wholly unserved areas, is underway.)</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr46"
    },
    "title": "Rural Broadband Window of Opportunity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Broadband Window of Opportunity Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to prioritize the processing of applications for certain rural broadband expansion projects that are located in areas with the shortest construction seasons (e.g., areas with long winters and heavy snowfall).</p><p>Specifically, the FCC must prioritize processing such applications for the Rural Digital Opportunity Fund (RDOF) Phase II auction, which aims to facilitate the provision of broadband service to\u00a0areas\u00a0that are\u00a0partially served. (The RDOF program's first phase, which is focused on broadband service for wholly unserved areas, is underway.)</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr46"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr46ih.xml"
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
      "title": "Rural Broadband Window of Opportunity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Broadband Window of Opportunity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Communications Commission to prioritize the timely processing of certain long-form applications in the Rural Digital Opportunity Fund Phase II auction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T06:49:43Z"
    }
  ]
}
```
