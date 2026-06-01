# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/549?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/549
- Title: To amend the Internal Revenue Code of 1986 to repeal the clean fuel production credit.
- Congress: 119
- Bill type: HR
- Bill number: 549
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-04-07T10:40:48Z
- Update date including text: 2025-04-07T10:40:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/549",
    "number": "549",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to repeal the clean fuel production credit.",
    "type": "HR",
    "updateDate": "2025-04-07T10:40:48Z",
    "updateDateIncludingText": "2025-04-07T10:40:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:09:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr549ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 549\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Ms. Van Duyne introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the clean fuel production credit.\n#### 1. Repeal of clean fuel production credit\n##### (a) In general\nPart IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by striking section 45Z (and by striking the item relating to such section in the table of sections for such part).\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-16",
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
        "updateDate": "2025-02-19T20:23:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr549",
          "measure-number": "549",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr549v00",
            "update-date": "2025-04-07"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill repeals the business tax credit for clean fuel production beginning in 2025. (Under current law, the business tax credit for clean fuel production is available for the production and sale of qualified transportation fuel between 2025 and 2027.)</p>"
        },
        "title": "To amend the Internal Revenue Code of 1986 to repeal the clean fuel production credit."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr549.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill repeals the business tax credit for clean fuel production beginning in 2025. (Under current law, the business tax credit for clean fuel production is available for the production and sale of qualified transportation fuel between 2025 and 2027.)</p>",
      "updateDate": "2025-04-07",
      "versionCode": "id119hr549"
    },
    "title": "To amend the Internal Revenue Code of 1986 to repeal the clean fuel production credit."
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill repeals the business tax credit for clean fuel production beginning in 2025. (Under current law, the business tax credit for clean fuel production is available for the production and sale of qualified transportation fuel between 2025 and 2027.)</p>",
      "updateDate": "2025-04-07",
      "versionCode": "id119hr549"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr549ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to repeal the clean fuel production credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T11:03:21Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to repeal the clean fuel production credit.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-17T09:05:46Z"
    }
  ]
}
```
