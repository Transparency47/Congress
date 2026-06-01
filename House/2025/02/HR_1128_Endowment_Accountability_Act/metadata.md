# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1128?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1128
- Title: Endowment Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 1128
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-03-31T14:52:11Z
- Update date including text: 2026-03-31T14:52:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1128",
    "number": "1128",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Endowment Accountability Act",
    "type": "HR",
    "updateDate": "2026-03-31T14:52:11Z",
    "updateDateIncludingText": "2026-03-31T14:52:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:01:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1128ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1128\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the rate of the excise tax based on investment income of private colleges and universities and to broaden the definition of applicable educational institution by lowering the threshold with respect to aggregate fair market value per student, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Endowment Accountability Act .\n#### 2. Excise tax based on investment income of private colleges and universities\n##### (a) Increase in rate of tax\nSection 4968(a) of the Internal Revenue Code of 1986 is amended by striking 1.4 percent and inserting 10 percent .\n##### (b) Lowering asset per student threshold for definition of applicable educational institution\nSection 4968(b)(1)(D) of such Code is amended by striking $500,000 and inserting $200,000 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-07",
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
        "updateDate": "2025-05-06T16:05:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1128",
          "measure-number": "1128",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1128v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Endowment Accountability Act</strong></p><p>This bill increases the excise tax on the net investment income of certain private university and college endowments.\u00a0The bill also expands the number of endowments subject to the excise tax by lowering the endowment asset amount per-student threshold.\u00a0\u00a0</p><p>Under current law, certain private\u00a0universities and colleges with 500 or more tuition-paying students (of which more than 50%\u00a0are located in the United States) and endowments that are at least $500,000 per student (per-student threshold) pay an excise tax in the amount of 1.4% on the net investment income from such endowments.</p><p>The bill increases the amount of the excise tax to 10% of the net investment income from such university and college endowments\u00a0and lowers the per-student threshold to $200,000.</p>"
        },
        "title": "Endowment Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1128.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Endowment Accountability Act</strong></p><p>This bill increases the excise tax on the net investment income of certain private university and college endowments.\u00a0The bill also expands the number of endowments subject to the excise tax by lowering the endowment asset amount per-student threshold.\u00a0\u00a0</p><p>Under current law, certain private\u00a0universities and colleges with 500 or more tuition-paying students (of which more than 50%\u00a0are located in the United States) and endowments that are at least $500,000 per student (per-student threshold) pay an excise tax in the amount of 1.4% on the net investment income from such endowments.</p><p>The bill increases the amount of the excise tax to 10% of the net investment income from such university and college endowments\u00a0and lowers the per-student threshold to $200,000.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr1128"
    },
    "title": "Endowment Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Endowment Accountability Act</strong></p><p>This bill increases the excise tax on the net investment income of certain private university and college endowments.\u00a0The bill also expands the number of endowments subject to the excise tax by lowering the endowment asset amount per-student threshold.\u00a0\u00a0</p><p>Under current law, certain private\u00a0universities and colleges with 500 or more tuition-paying students (of which more than 50%\u00a0are located in the United States) and endowments that are at least $500,000 per student (per-student threshold) pay an excise tax in the amount of 1.4% on the net investment income from such endowments.</p><p>The bill increases the amount of the excise tax to 10% of the net investment income from such university and college endowments\u00a0and lowers the per-student threshold to $200,000.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr1128"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1128ih.xml"
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
      "title": "Endowment Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Endowment Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to increase the rate of the excise tax based on investment income of private colleges and universities and to broaden the definition of applicable educational institution by lowering the threshold with respect to aggregate fair market value per student, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:18:18Z"
    }
  ]
}
```
