# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1438?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1438
- Title: Disaster Related Extension of Deadlines Act
- Congress: 119
- Bill type: S
- Bill number: 1438
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-01-05T21:58:48Z
- Update date including text: 2026-01-05T21:58:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1438",
    "number": "1438",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Disaster Related Extension of Deadlines Act",
    "type": "S",
    "updateDate": "2026-01-05T21:58:48Z",
    "updateDateIncludingText": "2026-01-05T21:58:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T17:41:47Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1438is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1438\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Warnock (for himself and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to make the postponement of certain deadlines by reason of disasters applicable to the limitation on credit or refund, and to take postponements into account for purposes of sending collection notices.\n#### 1. Short title\nThis Act may be cited as the Disaster Related Extension of Deadlines Act .\n#### 2. Postponement of certain deadlines by reason of disasters made applicable to limitation on credit or refund\n##### (a) Extension of time for filing return\n**(1) In general**\nSection 7508A of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(f) Application to limitation on credit or refund For purposes of section 6511(b)(2)(A), any period disregarded under this section with respect to the time prescribed for filing any return of tax shall be treated as an extension of time for filing such return. .\n**(2) Effective date**\nThe amendment made by this subsection shall apply to claims filed after the date of the enactment of this Act.\n##### (b) Collection notices\n**(1) In general**\nSection 6303(b) of such Code is amended\u2014\n**(A)**\nby striking Except and inserting the following:\n(1) In general Except , and\n**(B)**\nby adding at the end the following new paragraph:\n(2) Postponement by reason of disaster, significant fire, or terroristic or military actions For purposes of paragraph (1), the last date prescribed for payment of any tax shall be determined after taking into account any period disregarded under section 7508A. .\n**(2) Effective date**\nThe amendments made by this subsection shall apply to notices issued after the date of the enactment of this Act.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-12-26",
        "text": "Signed by President."
      },
      "number": "1491",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Disaster Related Extension of Deadlines Act",
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
        "updateDate": "2025-05-12T20:05:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119s1438",
          "measure-number": "1438",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2025-05-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1438v00",
            "update-date": "2025-05-22"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Disaster Related Extension of Deadlines Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to treat the postponement of the federal tax return deadline due to a federally declared disaster or certain other events as an extension of such deadline for purposes of calculating the limit on a tax refund. The bill also provides that the IRS\u2019s deadline for sending certain notices includes such postponement.</p><p>Under current law, a tax refund claim must be filed within three years of the date that the federal tax return is filed. (Some exceptions apply.) The tax refund amount generally is limited to federal taxes paid within the three years preceding the tax refund claim plus any extension of the federal tax return deadline (lookback period). The postponement of the federal tax return deadline is not an extension for purposes of the\u00a0lookback period. (Thus, certain tax payments made before the federal tax return is filed may be excluded from the lookback period.)</p><p>Under the bill, a federal tax return deadline postponed due to a federally declared disaster or certain other events must be treated as an extension of such deadline for purposes of the lookback period.</p><p>Under current law, the IRS is required to mail a notice and demand for tax payment within 60 days of an assessment but not before the tax payment due date.\u00a0</p><p>The bill provides that the tax payment due date includes the postponement of the tax payment deadline due to a federally declared disaster or certain other events.\u00a0</p>"
        },
        "title": "Disaster Related Extension of Deadlines Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1438.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disaster Related Extension of Deadlines Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to treat the postponement of the federal tax return deadline due to a federally declared disaster or certain other events as an extension of such deadline for purposes of calculating the limit on a tax refund. The bill also provides that the IRS\u2019s deadline for sending certain notices includes such postponement.</p><p>Under current law, a tax refund claim must be filed within three years of the date that the federal tax return is filed. (Some exceptions apply.) The tax refund amount generally is limited to federal taxes paid within the three years preceding the tax refund claim plus any extension of the federal tax return deadline (lookback period). The postponement of the federal tax return deadline is not an extension for purposes of the\u00a0lookback period. (Thus, certain tax payments made before the federal tax return is filed may be excluded from the lookback period.)</p><p>Under the bill, a federal tax return deadline postponed due to a federally declared disaster or certain other events must be treated as an extension of such deadline for purposes of the lookback period.</p><p>Under current law, the IRS is required to mail a notice and demand for tax payment within 60 days of an assessment but not before the tax payment due date.\u00a0</p><p>The bill provides that the tax payment due date includes the postponement of the tax payment deadline due to a federally declared disaster or certain other events.\u00a0</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119s1438"
    },
    "title": "Disaster Related Extension of Deadlines Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Disaster Related Extension of Deadlines Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to treat the postponement of the federal tax return deadline due to a federally declared disaster or certain other events as an extension of such deadline for purposes of calculating the limit on a tax refund. The bill also provides that the IRS\u2019s deadline for sending certain notices includes such postponement.</p><p>Under current law, a tax refund claim must be filed within three years of the date that the federal tax return is filed. (Some exceptions apply.) The tax refund amount generally is limited to federal taxes paid within the three years preceding the tax refund claim plus any extension of the federal tax return deadline (lookback period). The postponement of the federal tax return deadline is not an extension for purposes of the\u00a0lookback period. (Thus, certain tax payments made before the federal tax return is filed may be excluded from the lookback period.)</p><p>Under the bill, a federal tax return deadline postponed due to a federally declared disaster or certain other events must be treated as an extension of such deadline for purposes of the lookback period.</p><p>Under current law, the IRS is required to mail a notice and demand for tax payment within 60 days of an assessment but not before the tax payment due date.\u00a0</p><p>The bill provides that the tax payment due date includes the postponement of the tax payment deadline due to a federally declared disaster or certain other events.\u00a0</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119s1438"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1438is.xml"
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
      "title": "Disaster Related Extension of Deadlines Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disaster Related Extension of Deadlines Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to make the postponement of certain deadlines by reason of disasters applicable to the limitation on credit or refund, and to take postponements into account for purposes of sending collection notices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:17Z"
    }
  ]
}
```
