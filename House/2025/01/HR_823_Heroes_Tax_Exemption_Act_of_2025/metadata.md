# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/823?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/823
- Title: Heroes’ Tax Exemption Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 823
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-06-25T16:59:14Z
- Update date including text: 2025-06-25T16:59:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/823",
    "number": "823",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Heroes\u2019 Tax Exemption Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-25T16:59:14Z",
    "updateDateIncludingText": "2025-06-25T16:59:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:06:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr823ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 823\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exempt servicemembers from the income tax.\n#### 1. Short title\nThis Act may be cited as the Heroes\u2019 Tax Exemption Act of 2025 .\n#### 2. Exemption from income tax for servicemembers\n##### (a) In general\nPart III of subchapter B of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Income earned by servicemembers Gross income shall not include any amount earned by an active duty member of the Armed Forces. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of subtitle A of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Income earned by servicemembers. .\n##### (c) Effective date\nThe amendments made by this section shall apply to income earned after the second October 1 occurring after date of the enactment of this Act.",
      "versionDate": "2025-01-28",
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
        "updateDate": "2025-04-07T16:16:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr823",
          "measure-number": "823",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr823v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Heroes\u2019 Tax Exemption Act of 2025</strong></p><p>This bill excludes\u00a0amounts earned by an active duty member of the Armed Forces from gross income for federal tax purposes.</p>"
        },
        "title": "Heroes\u2019 Tax Exemption Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr823.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Heroes\u2019 Tax Exemption Act of 2025</strong></p><p>This bill excludes\u00a0amounts earned by an active duty member of the Armed Forces from gross income for federal tax purposes.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr823"
    },
    "title": "Heroes\u2019 Tax Exemption Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Heroes\u2019 Tax Exemption Act of 2025</strong></p><p>This bill excludes\u00a0amounts earned by an active duty member of the Armed Forces from gross income for federal tax purposes.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr823"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr823ih.xml"
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
      "title": "Heroes\u2019 Tax Exemption Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heroes\u2019 Tax Exemption Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exempt servicemembers from the income tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T06:49:21Z"
    }
  ]
}
```
