# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/111
- Title: To amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for health insurance premiums.
- Congress: 119
- Bill type: HR
- Bill number: 111
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-14T19:31:17Z
- Update date including text: 2025-02-14T19:31:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/111",
    "number": "111",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
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
    "title": "To amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for health insurance premiums.",
    "type": "HR",
    "updateDate": "2025-02-14T19:31:17Z",
    "updateDateIncludingText": "2025-02-14T19:31:17Z"
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
          "date": "2025-01-03T16:20:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr111ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 111\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for health insurance premiums.\n#### 1. Deduction for health insurance premiums\n##### (a) In general\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 224 as section 225 and by inserting after section 223 the following new section:\n224. Deduction for health insurance premiums In the case of an individual, there shall be allowed as a deduction for the taxable year amounts paid by the taxpayer for insurance which constitutes medical care (as defined in section 213(d)) for the taxpayer and the taxpayer\u2019s spouse and dependents. No amount allowed as a deduction under the preceding sentence shall be taken into account in determining any deduction or credit otherwise allowable to the taxpayer (or any other taxpayer) under this chapter. .\n##### (b) Deduction allowed whether or not individual itemizes other deductions\nSubsection (a) of section 62 of such Code is amended by inserting before the last sentence at the end the following new paragraph:\n(22) Deduction for health insurance premiums The deduction allowed by section 224. .\n##### (c) Clerical amendment\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended by redesignating the item relating to section 224 as an item relating to section 225 and by inserting after the item relating to section 223 the following new item:\nSec. 224. Deduction for health insurance premiums. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
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
            "name": "Health care costs and insurance",
            "updateDate": "2025-02-14T19:31:07Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-02-14T19:31:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-01-31T16:17:03Z"
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
          "measure-id": "id119hr111",
          "measure-number": "111",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr111v00",
            "update-date": "2025-02-04"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill provides a tax deduction for health insurance premiums paid to provide medical insurance coverage for an individual, the individual\u2019s spouse, and the individual\u2019s dependents. Under the bill, the tax deduction may be claimed as an adjustment to income (also known as an above-the-line tax deduction), which does not require the individual to itemize deductions.\u00a0</p>"
        },
        "title": "To amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for health insurance premiums."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr111.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides a tax deduction for health insurance premiums paid to provide medical insurance coverage for an individual, the individual\u2019s spouse, and the individual\u2019s dependents. Under the bill, the tax deduction may be claimed as an adjustment to income (also known as an above-the-line tax deduction), which does not require the individual to itemize deductions.\u00a0</p>",
      "updateDate": "2025-02-04",
      "versionCode": "id119hr111"
    },
    "title": "To amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for health insurance premiums."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides a tax deduction for health insurance premiums paid to provide medical insurance coverage for an individual, the individual\u2019s spouse, and the individual\u2019s dependents. Under the bill, the tax deduction may be claimed as an adjustment to income (also known as an above-the-line tax deduction), which does not require the individual to itemize deductions.\u00a0</p>",
      "updateDate": "2025-02-04",
      "versionCode": "id119hr111"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr111ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for health insurance premiums.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T05:18:23Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for health insurance premiums.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:50Z"
    }
  ]
}
```
