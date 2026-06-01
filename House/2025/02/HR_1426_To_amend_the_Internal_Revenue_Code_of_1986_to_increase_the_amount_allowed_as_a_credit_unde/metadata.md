# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1426?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1426
- Title: To amend the Internal Revenue Code of 1986 to increase the amount allowed as a credit under the expenses for household and dependent care services credit and the employer-provided child care credit.
- Congress: 119
- Bill type: HR
- Bill number: 1426
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-05-06T13:21:38Z
- Update date including text: 2026-05-06T13:21:38Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1426",
    "number": "1426",
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
    "title": "To amend the Internal Revenue Code of 1986 to increase the amount allowed as a credit under the expenses for household and dependent care services credit and the employer-provided child care credit.",
    "type": "HR",
    "updateDate": "2026-05-06T13:21:38Z",
    "updateDateIncludingText": "2026-05-06T13:21:38Z"
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
          "date": "2025-02-18T18:03:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1426ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1426\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Mackenzie introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the amount allowed as a credit under the expenses for household and dependent care services credit and the employer-provided child care credit.\n#### 1. Increase in credit for expenses for household and dependent care services\n##### (a) In general\nSection 21(c) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (1), by striking $3,000 and inserting $6,000 , and\n**(2)**\nin paragraph (2), by striking $6,000 and inserting $12,000 .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 2. Increase in employer-provided child care credit\n##### (a) In general\nSection 45F(b) is amended by striking $150,000 and inserting $400,000 .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
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
        "updateDate": "2025-05-08T18:35:07Z"
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
          "measure-id": "id119hr1426",
          "measure-number": "1426",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2026-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1426v00",
            "update-date": "2026-05-06"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill doubles the maximum amount that an individual may claim as a federal tax credit for qualified child and dependent care expenses and increases the maximum amount an employer may claim as a federal business tax credit for providing certain child care services to employees.</p><p>Under the bill, the annual maximum amount allowed for the child and dependent care tax credit is increased to $6,000 (from $3,000) for individuals with one qualifying child or dependent, or to $12,000 (from $6,000) for individuals with two or more qualifying children or dependents. (Under current law, an individual may claim a nonrefundable tax credit for a portion\u00a0of qualified child and dependent care expenses paid so that the individual or the individual\u2019s spouse can work or look for work.)</p><p>Further, the bill increases to $400,000 (from $150,000) the annual maximum amount that an employer may claim as a tax credit for providing certain child care services to employees. (Under current law, an employer may claim a nonrefundable business tax credit for a percentage of qualified child care facility expenses and child care referral and resource expenses.)</p>"
        },
        "title": "To amend the Internal Revenue Code of 1986 to increase the amount allowed as a credit under the expenses for household and dependent care services credit and the employer-provided child care credit."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1426.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill doubles the maximum amount that an individual may claim as a federal tax credit for qualified child and dependent care expenses and increases the maximum amount an employer may claim as a federal business tax credit for providing certain child care services to employees.</p><p>Under the bill, the annual maximum amount allowed for the child and dependent care tax credit is increased to $6,000 (from $3,000) for individuals with one qualifying child or dependent, or to $12,000 (from $6,000) for individuals with two or more qualifying children or dependents. (Under current law, an individual may claim a nonrefundable tax credit for a portion\u00a0of qualified child and dependent care expenses paid so that the individual or the individual\u2019s spouse can work or look for work.)</p><p>Further, the bill increases to $400,000 (from $150,000) the annual maximum amount that an employer may claim as a tax credit for providing certain child care services to employees. (Under current law, an employer may claim a nonrefundable business tax credit for a percentage of qualified child care facility expenses and child care referral and resource expenses.)</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr1426"
    },
    "title": "To amend the Internal Revenue Code of 1986 to increase the amount allowed as a credit under the expenses for household and dependent care services credit and the employer-provided child care credit."
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill doubles the maximum amount that an individual may claim as a federal tax credit for qualified child and dependent care expenses and increases the maximum amount an employer may claim as a federal business tax credit for providing certain child care services to employees.</p><p>Under the bill, the annual maximum amount allowed for the child and dependent care tax credit is increased to $6,000 (from $3,000) for individuals with one qualifying child or dependent, or to $12,000 (from $6,000) for individuals with two or more qualifying children or dependents. (Under current law, an individual may claim a nonrefundable tax credit for a portion\u00a0of qualified child and dependent care expenses paid so that the individual or the individual\u2019s spouse can work or look for work.)</p><p>Further, the bill increases to $400,000 (from $150,000) the annual maximum amount that an employer may claim as a tax credit for providing certain child care services to employees. (Under current law, an employer may claim a nonrefundable business tax credit for a percentage of qualified child care facility expenses and child care referral and resource expenses.)</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr1426"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1426ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to increase the amount allowed as a credit under the expenses for household and dependent care services credit and the employer-provided child care credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T08:48:22Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to increase the amount allowed as a credit under the expenses for household and dependent care services credit and the employer-provided child care credit.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T08:06:12Z"
    }
  ]
}
```
