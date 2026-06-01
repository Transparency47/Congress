# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/85?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/85
- Title: Small Business Flexibility Act
- Congress: 119
- Bill type: HR
- Bill number: 85
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/85",
    "number": "85",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Small Business Flexibility Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
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
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
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
          "date": "2025-01-03T16:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr85ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 85\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to allow the pooling of tips among all employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Flexibility Act .\n#### 2. Tip pooling\nSection 3(m)(2) of the Fair Labor Standards Act ( 29 U.S.C. 203(m)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by striking employees who customarily and regularly receive tips and inserting pools of employees described in subparagraph (C) ; and\n**(2)**\nby adding at the end the following:\n(C) The pools of employees described in this subparagraph are as follows: (i) Employees who customarily and regularly receive tips. (ii) Employees who\u2014 (I) customarily and regularly receive tips and receive a cash wage paid by the employer that is not less than the wage in effect under section 6(a)(1); and (II) do not customarily and regularly receive tips. .",
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
        "item": {
          "name": "Wages and earnings",
          "updateDate": "2025-01-31T19:54:54Z"
        }
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-01-31T13:21:36Z"
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
          "measure-id": "id119hr85",
          "measure-number": "85",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr85v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Small Business Flexibility Act</strong></p><p>This bill provides\u00a0statutory authority for the pooling of tips among\u00a0two pools of employees. The first pool consists of employees who\u00a0customarily and regularly receive tips\u00a0(as is permitted under the current statute). The second pool consists of\u00a0(1) employees who\u00a0customarily and regularly receive tips and are paid at least minimum wage, and (2) employees who\u00a0do not customarily and regularly receive tips.\u00a0\u00a0</p>"
        },
        "title": "Small Business Flexibility Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr85.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Small Business Flexibility Act</strong></p><p>This bill provides\u00a0statutory authority for the pooling of tips among\u00a0two pools of employees. The first pool consists of employees who\u00a0customarily and regularly receive tips\u00a0(as is permitted under the current statute). The second pool consists of\u00a0(1) employees who\u00a0customarily and regularly receive tips and are paid at least minimum wage, and (2) employees who\u00a0do not customarily and regularly receive tips.\u00a0\u00a0</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hr85"
    },
    "title": "Small Business Flexibility Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Small Business Flexibility Act</strong></p><p>This bill provides\u00a0statutory authority for the pooling of tips among\u00a0two pools of employees. The first pool consists of employees who\u00a0customarily and regularly receive tips\u00a0(as is permitted under the current statute). The second pool consists of\u00a0(1) employees who\u00a0customarily and regularly receive tips and are paid at least minimum wage, and (2) employees who\u00a0do not customarily and regularly receive tips.\u00a0\u00a0</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hr85"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr85ih.xml"
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
      "title": "Small Business Flexibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Flexibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Labor Standards Act of 1938 to allow the pooling of tips among all employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T04:33:22Z"
    }
  ]
}
```
