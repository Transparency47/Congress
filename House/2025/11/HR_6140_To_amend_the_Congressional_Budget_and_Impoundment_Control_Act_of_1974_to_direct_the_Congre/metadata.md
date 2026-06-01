# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6140?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6140
- Title: Congressional Budget Office Scheduling Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 6140
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-01-05T16:55:30Z
- Update date including text: 2026-01-05T16:55:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6140",
    "number": "6140",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "G000603",
        "district": "26",
        "firstName": "Brandon",
        "fullName": "Rep. Gill, Brandon [R-TX-26]",
        "lastName": "Gill",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Congressional Budget Office Scheduling Reform Act",
    "type": "HR",
    "updateDate": "2026-01-05T16:55:30Z",
    "updateDateIncludingText": "2026-01-05T16:55:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NC"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "WI"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NC"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "KS"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6140ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6140\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Gill of Texas (for himself, Mr. Edwards , Mr. Grothman , Mr. McDowell , Mr. Estes , and Mr. Stutzman ) introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to direct the Congressional Budget Office to publish a schedule of the availability of certain publications by the Office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Congressional Budget Office Scheduling Reform Act .\n#### 2. Publication of Congressional Budget Office schedule of publications\n##### (a) In general\nTitle IV of the Congressional Budget and Impoundment Control Act of 1974 is amended by inserting after section 402 the following:\n403. Congressional Budget Office schedule (a) Schedule Not later than December 31 of each calendar year, the Director of the Congressional Budget Office shall publish, on the Office\u2019s public website, a schedule setting forth the expected publication dates of major recurring reports. Such schedule shall include at a minimum the following: (1) The baseline for the budget year and subsequent updates. (2) The report on options to reduce the deficit. (3) The report on the accuracy of budgetary projections for the most recently completed fiscal year. (4) The report on programs or activities with unauthorized appropriations under section 202(e)(3). (b) Update The Director shall, as the Director deems necessary, update the schedule published under subsection (a) during the calendar year immediately following the calendar year such schedule was published. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of such Act is amended by inserting after the item relating to section 402 the following:\nSec. 403. Congressional Budget Office schedule. .",
      "versionDate": "2025-11-19",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-12-09T21:57:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-19",
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
          "measure-id": "id119hr6140",
          "measure-number": "6140",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-19",
          "originChamber": "HOUSE",
          "update-date": "2026-01-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6140v00",
            "update-date": "2026-01-05"
          },
          "action-date": "2025-11-19",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Congressional Budget Office Scheduling Reform Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to annually publish a schedule of the expected publication dates of its major recurring reports.</p><p>The schedule must\u00a0must include, at a minimum, the expected publication dates for</p><ul><li>the baseline for the budget year and subsequent updates,</li><li>the report on options to reduce the deficit,</li><li>the report on the accuracy of budgetary projections for the most recently completed fiscal year, and</li><li>the report on programs or activities with unauthorized appropriations.</li></ul><p>CBO must (1) publish the schedule on its public website no later than December 31 of each year, and (2) update the schedule during the following calendar year as necessary. \u00a0</p>"
        },
        "title": "Congressional Budget Office Scheduling Reform Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6140.xml",
    "summary": {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Budget Office Scheduling Reform Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to annually publish a schedule of the expected publication dates of its major recurring reports.</p><p>The schedule must\u00a0must include, at a minimum, the expected publication dates for</p><ul><li>the baseline for the budget year and subsequent updates,</li><li>the report on options to reduce the deficit,</li><li>the report on the accuracy of budgetary projections for the most recently completed fiscal year, and</li><li>the report on programs or activities with unauthorized appropriations.</li></ul><p>CBO must (1) publish the schedule on its public website no later than December 31 of each year, and (2) update the schedule during the following calendar year as necessary. \u00a0</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119hr6140"
    },
    "title": "Congressional Budget Office Scheduling Reform Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Budget Office Scheduling Reform Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to annually publish a schedule of the expected publication dates of its major recurring reports.</p><p>The schedule must\u00a0must include, at a minimum, the expected publication dates for</p><ul><li>the baseline for the budget year and subsequent updates,</li><li>the report on options to reduce the deficit,</li><li>the report on the accuracy of budgetary projections for the most recently completed fiscal year, and</li><li>the report on programs or activities with unauthorized appropriations.</li></ul><p>CBO must (1) publish the schedule on its public website no later than December 31 of each year, and (2) update the schedule during the following calendar year as necessary. \u00a0</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119hr6140"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6140ih.xml"
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
      "title": "Congressional Budget Office Scheduling Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Budget Office Scheduling Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to direct the Congressional Budget Office to publish a schedule of the availability of certain publications by the Office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:18:20Z"
    }
  ]
}
```
