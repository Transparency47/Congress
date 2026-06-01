# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1424?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1424
- Title: To amend the Internal Revenue Code of 1986 to increase the employer tax credit for paid family and medical leave.
- Congress: 119
- Bill type: HR
- Bill number: 1424
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-04-30T19:12:37Z
- Update date including text: 2026-04-30T19:12:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1424",
    "number": "1424",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001230",
        "district": "7",
        "firstName": "Ryan",
        "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
        "lastName": "Mackenzie",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to increase the employer tax credit for paid family and medical leave.",
    "type": "HR",
    "updateDate": "2026-04-30T19:12:37Z",
    "updateDateIncludingText": "2026-04-30T19:12:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:03:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1424ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1424\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Mackenzie introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the employer tax credit for paid family and medical leave.\n#### 1. Increase in employer credit for paid family and medical leave\n##### (a) Increase in credit percentages\nSection 45S(a)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 12.5 percent and inserting 25 percent ,\n**(2)**\nby striking 25 percent and inserting 50 percent , and\n**(3)**\nby striking 0.25 percentage points and inserting 0.50 percentage points .\n##### (b) Credit made permanent\nSection 45S of such Code is amended by striking subsection (f).\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-02-18",
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
        "updateDate": "2025-05-07T12:36:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1424",
          "measure-number": "1424",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2026-04-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1424v00",
            "update-date": "2026-04-30"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill increases the business tax credit for paid family and medical leave to up to 50% (from 25%) of the wages paid by an eligible employer to a qualifying employee while the employee is on family and medical leave.</p><p>Under current law, an eligible employer may claim a tax credit (through 2025) for between 12.5% and 25% of the wages paid to a qualified employee while the employee is on family and medical leave. The percentage of wages allowed as a tax credit increases proportionally, depending on what percentage of an employee\u2019s normal wages is paid to the employee while the employee is on family and medical leave.</p><p>The bill increases the tax credit to between 25% and 50% of the wages paid to an employee while the employee is on family and medical leave, depending on what percentage of an employee\u2019s normal wages is paid to the employee while the employee is on family and medical leave.</p><p>Under current law and the bill, an employer must pay at least 50% of the employee's normal wages while the employee is on leave to qualify for the tax credit.\u00a0</p>"
        },
        "title": "To amend the Internal Revenue Code of 1986 to increase the employer tax credit for paid family and medical leave."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1424.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases the business tax credit for paid family and medical leave to up to 50% (from 25%) of the wages paid by an eligible employer to a qualifying employee while the employee is on family and medical leave.</p><p>Under current law, an eligible employer may claim a tax credit (through 2025) for between 12.5% and 25% of the wages paid to a qualified employee while the employee is on family and medical leave. The percentage of wages allowed as a tax credit increases proportionally, depending on what percentage of an employee\u2019s normal wages is paid to the employee while the employee is on family and medical leave.</p><p>The bill increases the tax credit to between 25% and 50% of the wages paid to an employee while the employee is on family and medical leave, depending on what percentage of an employee\u2019s normal wages is paid to the employee while the employee is on family and medical leave.</p><p>Under current law and the bill, an employer must pay at least 50% of the employee's normal wages while the employee is on leave to qualify for the tax credit.\u00a0</p>",
      "updateDate": "2026-04-30",
      "versionCode": "id119hr1424"
    },
    "title": "To amend the Internal Revenue Code of 1986 to increase the employer tax credit for paid family and medical leave."
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases the business tax credit for paid family and medical leave to up to 50% (from 25%) of the wages paid by an eligible employer to a qualifying employee while the employee is on family and medical leave.</p><p>Under current law, an eligible employer may claim a tax credit (through 2025) for between 12.5% and 25% of the wages paid to a qualified employee while the employee is on family and medical leave. The percentage of wages allowed as a tax credit increases proportionally, depending on what percentage of an employee\u2019s normal wages is paid to the employee while the employee is on family and medical leave.</p><p>The bill increases the tax credit to between 25% and 50% of the wages paid to an employee while the employee is on family and medical leave, depending on what percentage of an employee\u2019s normal wages is paid to the employee while the employee is on family and medical leave.</p><p>Under current law and the bill, an employer must pay at least 50% of the employee's normal wages while the employee is on leave to qualify for the tax credit.\u00a0</p>",
      "updateDate": "2026-04-30",
      "versionCode": "id119hr1424"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1424ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to increase the employer tax credit for paid family and medical leave.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T11:03:25Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to increase the employer tax credit for paid family and medical leave.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T09:05:45Z"
    }
  ]
}
```
