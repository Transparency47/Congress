# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/228?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/228
- Title: To amend the Internal Revenue Code of 1986 to increase and adjust for inflation the above-the-line deduction for teachers.
- Congress: 119
- Bill type: HR
- Bill number: 228
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-09-10T20:11:19Z
- Update date including text: 2025-09-10T20:11:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/228",
    "number": "228",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000568",
        "district": "9",
        "firstName": "H.",
        "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
        "lastName": "Griffith",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to increase and adjust for inflation the above-the-line deduction for teachers.",
    "type": "HR",
    "updateDate": "2025-09-10T20:11:19Z",
    "updateDateIncludingText": "2025-09-10T20:11:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:01:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr228ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 228\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Mr. Griffith introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase and adjust for inflation the above-the-line deduction for teachers.\n#### 1. Increase in deduction for certain expenses of elementary and secondary school teachers\n##### (a) In general\nSection 62(a)(2)(D) of the Internal Revenue Code of 1986 is amended by striking $250 and inserting $1000 .\n##### (b) Conforming amendments\nSection 62(d)(3) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 2015 and inserting 2025 ,\n**(2)**\nby striking $250 and inserting $1000 , and\n**(3)**\nby striking calendar year 2014 and inserting calendar year 2024 .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-01-07",
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
            "name": "Elementary and secondary education",
            "updateDate": "2025-09-10T20:10:51Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-09-10T20:11:19Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-09-10T20:11:01Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-09-10T20:11:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-05T15:47:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr228",
          "measure-number": "228",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr228v00",
            "update-date": "2025-02-21"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill increases the\u00a0above-the-line tax deduction for unreimbursed expenses incurred by an eligible educator for classroom supplies and certain professional development courses. (Above-the-line deductions are subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, an eligible educator may deduct up to $300 in 2025 (adjusted annually for inflation) for unreimbursed expenses for classroom supplies and certain professional development courses. An <em>eligible educator</em> is defined as a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who works at least 900 hours during a school year\u00a0in a school that provides elementary or secondary education. \u00a0</p><p>Under the bill, an eligible educator may deduct up to $1,000 in 2025 for unreimbursed expenses for classroom supplies and certain professional development. For tax years after 2025, the $1,000 limit on the tax deduction is adjusted annually for inflation.</p>"
        },
        "title": "To amend the Internal Revenue Code of 1986 to increase and adjust for inflation the above-the-line deduction for teachers."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr228.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases the\u00a0above-the-line tax deduction for unreimbursed expenses incurred by an eligible educator for classroom supplies and certain professional development courses. (Above-the-line deductions are subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, an eligible educator may deduct up to $300 in 2025 (adjusted annually for inflation) for unreimbursed expenses for classroom supplies and certain professional development courses. An <em>eligible educator</em> is defined as a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who works at least 900 hours during a school year\u00a0in a school that provides elementary or secondary education. \u00a0</p><p>Under the bill, an eligible educator may deduct up to $1,000 in 2025 for unreimbursed expenses for classroom supplies and certain professional development. For tax years after 2025, the $1,000 limit on the tax deduction is adjusted annually for inflation.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hr228"
    },
    "title": "To amend the Internal Revenue Code of 1986 to increase and adjust for inflation the above-the-line deduction for teachers."
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases the\u00a0above-the-line tax deduction for unreimbursed expenses incurred by an eligible educator for classroom supplies and certain professional development courses. (Above-the-line deductions are subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, an eligible educator may deduct up to $300 in 2025 (adjusted annually for inflation) for unreimbursed expenses for classroom supplies and certain professional development courses. An <em>eligible educator</em> is defined as a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who works at least 900 hours during a school year\u00a0in a school that provides elementary or secondary education. \u00a0</p><p>Under the bill, an eligible educator may deduct up to $1,000 in 2025 for unreimbursed expenses for classroom supplies and certain professional development. For tax years after 2025, the $1,000 limit on the tax deduction is adjusted annually for inflation.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hr228"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr228ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to increase and adjust for inflation the above-the-line deduction for teachers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T09:18:28Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to increase and adjust for inflation the above-the-line deduction for teachers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-08T09:05:29Z"
    }
  ]
}
```
