# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/558?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/558
- Title: Tip Tax Termination Act
- Congress: 119
- Bill type: HR
- Bill number: 558
- Origin chamber: House
- Introduced date: 2025-01-20
- Update date: 2025-04-02T13:53:39Z
- Update date including text: 2025-04-02T13:53:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-20: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-20: Introduced in House

## Actions

- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-20",
    "latestAction": {
      "actionDate": "2025-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/558",
    "number": "558",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Tip Tax Termination Act",
    "type": "HR",
    "updateDate": "2025-04-02T13:53:39Z",
    "updateDateIncludingText": "2025-04-02T13:53:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-20",
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
      "actionDate": "2025-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-20",
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
          "date": "2025-01-20T15:00:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr558ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 558\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2025 Mr. Bacon introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide that certain tips shall not be subject to income taxes for a period of 5 years.\n#### 1. Short title\nThis Act may be cited as the Tip Tax Termination Act .\n#### 2. Exclusion from gross income of certain tipped wages\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Certain tipped wages (a) In general Gross income shall not include so much of the eligible tips received by an individual during the taxable year as does not exceed $20,000. (b) Eligible tips For purposes of this section, the term eligible tips means amounts received while performing services which constitute employment in a position which generally relies on tips as part of wages, including cosmetology, hospitality, and food service. (c) Denial of double benefit (1) In general Except as provided in paragraph (2), any amount which is excluded from gross income under this section shall not be taken into account in determining any deduction or credit under this chapter. (2) Exception for child tax credit; earned income credit The amount excluded from gross income under this section shall be taken into account for purposes of determining the credits under sections 24 and 32. (d) Termination This section shall not apply to tips received after December 31, 2029. .\n##### (b) Withholding\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall modify the tables and procedures prescribed under section 3402(a) of the Internal Revenue Code of 1986 to take into account amounts excludible from gross income under section 139J of such Code (as added by this Act).\n##### (c) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Certain tipped wages. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts received after December 31, 2024.",
      "versionDate": "2025-01-20",
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
        "updateDate": "2025-02-19T20:32:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-20",
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
          "measure-id": "id119hr558",
          "measure-number": "558",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-20",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr558v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-01-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Tip Tax Termination Act\u00a0</strong></p><p>This bill excludes from gross income for federal\u00a0tax purposes up to $20,000 of eligible tips received during the tax year.\u00a0The bill also requires the Internal Revenue Service to modify the tables and procedures used to withhold federal income tax from wages to take into account eligible tips excluded from gross income.\u00a0</p><p>The bill defines\u00a0<em>eligible tips</em> as amounts received while performing services in a position that generally relies on tips as part of wages, including cosmetology, hospitality, and food service.</p><p>Further, under the bill, the amount of eligible tips excluded from gross income must not be included in determining federal tax deductions or credits, except for purposes of calculating the child tax credit and earned income tax credit.</p><p>Finally, the exclusion from gross income only applies to eligible tips received before 2030. </p>"
        },
        "title": "Tip Tax Termination Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr558.xml",
    "summary": {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tip Tax Termination Act\u00a0</strong></p><p>This bill excludes from gross income for federal\u00a0tax purposes up to $20,000 of eligible tips received during the tax year.\u00a0The bill also requires the Internal Revenue Service to modify the tables and procedures used to withhold federal income tax from wages to take into account eligible tips excluded from gross income.\u00a0</p><p>The bill defines\u00a0<em>eligible tips</em> as amounts received while performing services in a position that generally relies on tips as part of wages, including cosmetology, hospitality, and food service.</p><p>Further, under the bill, the amount of eligible tips excluded from gross income must not be included in determining federal tax deductions or credits, except for purposes of calculating the child tax credit and earned income tax credit.</p><p>Finally, the exclusion from gross income only applies to eligible tips received before 2030. </p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr558"
    },
    "title": "Tip Tax Termination Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tip Tax Termination Act\u00a0</strong></p><p>This bill excludes from gross income for federal\u00a0tax purposes up to $20,000 of eligible tips received during the tax year.\u00a0The bill also requires the Internal Revenue Service to modify the tables and procedures used to withhold federal income tax from wages to take into account eligible tips excluded from gross income.\u00a0</p><p>The bill defines\u00a0<em>eligible tips</em> as amounts received while performing services in a position that generally relies on tips as part of wages, including cosmetology, hospitality, and food service.</p><p>Further, under the bill, the amount of eligible tips excluded from gross income must not be included in determining federal tax deductions or credits, except for purposes of calculating the child tax credit and earned income tax credit.</p><p>Finally, the exclusion from gross income only applies to eligible tips received before 2030. </p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr558"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr558ih.xml"
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
      "title": "Tip Tax Termination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tip Tax Termination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide that certain tips shall not be subject to income taxes for a period of 5 years.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T05:18:25Z"
    }
  ]
}
```
