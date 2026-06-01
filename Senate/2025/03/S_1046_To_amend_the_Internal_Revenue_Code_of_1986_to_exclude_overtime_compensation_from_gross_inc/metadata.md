# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1046?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1046
- Title: No Tax On Overtime Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1046
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-12-05T22:02:51Z
- Update date including text: 2025-12-05T22:02:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1046",
    "number": "1046",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "No Tax On Overtime Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:02:51Z",
    "updateDateIncludingText": "2025-12-05T22:02:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-13T18:56:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1046is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1046\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Hawley introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude overtime compensation from gross income for purposes of the income tax.\n#### 1. Short title\nThis Act may be cited as the No Tax On Overtime Act of 2025 .\n#### 2. Exclusion of overtime compensation from gross income\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Overtime compensation Gross income shall not include overtime compensation required under section 7 of the Fair Labor Standards Act of 1938. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Overtime compensation. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received after the date of the enactment of this Act.",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-15",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "405",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep Every Extra Penny Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-05-08T19:15:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
    "originChamber": "Senate",
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
          "measure-id": "id119s1046",
          "measure-number": "1046",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1046v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>No Tax On Overtime Act of 2025</strong></p><p>This bill excludes from gross income for federal income tax purposes overtime compensation paid for hours worked in excess of 40 hours per week (as required by the Fair Labor Standards Act of 1938).\u00a0Under current law, overtime compensation paid to a taxpayer is included in gross income for purposes of calculating federal income taxes.</p>"
        },
        "title": "No Tax On Overtime Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1046.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Tax On Overtime Act of 2025</strong></p><p>This bill excludes from gross income for federal income tax purposes overtime compensation paid for hours worked in excess of 40 hours per week (as required by the Fair Labor Standards Act of 1938).\u00a0Under current law, overtime compensation paid to a taxpayer is included in gross income for purposes of calculating federal income taxes.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s1046"
    },
    "title": "No Tax On Overtime Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Tax On Overtime Act of 2025</strong></p><p>This bill excludes from gross income for federal income tax purposes overtime compensation paid for hours worked in excess of 40 hours per week (as required by the Fair Labor Standards Act of 1938).\u00a0Under current law, overtime compensation paid to a taxpayer is included in gross income for purposes of calculating federal income taxes.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s1046"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1046is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude overtime compensation from gross income for purposes of the income tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:30Z"
    },
    {
      "title": "No Tax On Overtime Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Tax On Overtime Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:20Z"
    }
  ]
}
```
