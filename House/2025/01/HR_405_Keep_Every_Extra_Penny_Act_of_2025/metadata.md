# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/405?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/405
- Title: Keep Every Extra Penny Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 405
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-05T22:00:37Z
- Update date including text: 2025-12-05T22:00:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/405",
    "number": "405",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000469",
        "district": "1",
        "firstName": "Russ",
        "fullName": "Rep. Fulcher, Russ [R-ID-1]",
        "lastName": "Fulcher",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Keep Every Extra Penny Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:00:37Z",
    "updateDateIncludingText": "2025-12-05T22:00:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:02:35Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr405ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 405\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Fulcher (for himself and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude overtime compensation from gross income for purposes of the income tax.\n#### 1. Short title\nThis Act may be cited as the Keep Every Extra Penny Act of 2025 .\n#### 2. Exclusion of overtime compensation from gross income\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Overtime compensation Gross income shall not include overtime compensation required under section 7 of the Fair Labor Standards Act of 1938. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Overtime compensation. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received after the date of the enactment of this Act.",
      "versionDate": "2025-01-15",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1046",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Tax On Overtime Act of 2025",
      "type": "S"
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
        "updateDate": "2025-02-19T19:10:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr405",
          "measure-number": "405",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr405v00",
            "update-date": "2025-03-25"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keep Every Extra Penny Act of 2025</strong></p><p>This bill excludes from gross income for federal income tax purposes overtime compensation paid for hours worked in excess of 40 hours per week (as required by the Fair Labor Standards Act of 1938).\u00a0Under current law, overtime compensation paid to a taxpayer is included in gross income for purposes of calculating federal income taxes.</p>"
        },
        "title": "Keep Every Extra Penny Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr405.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep Every Extra Penny Act of 2025</strong></p><p>This bill excludes from gross income for federal income tax purposes overtime compensation paid for hours worked in excess of 40 hours per week (as required by the Fair Labor Standards Act of 1938).\u00a0Under current law, overtime compensation paid to a taxpayer is included in gross income for purposes of calculating federal income taxes.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr405"
    },
    "title": "Keep Every Extra Penny Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep Every Extra Penny Act of 2025</strong></p><p>This bill excludes from gross income for federal income tax purposes overtime compensation paid for hours worked in excess of 40 hours per week (as required by the Fair Labor Standards Act of 1938).\u00a0Under current law, overtime compensation paid to a taxpayer is included in gross income for purposes of calculating federal income taxes.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr405"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr405ih.xml"
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
      "title": "Keep Every Extra Penny Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Every Extra Penny Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude overtime compensation from gross income for purposes of the income tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:48:24Z"
    }
  ]
}
```
