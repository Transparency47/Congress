# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/361?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/361
- Title: Supporting Victims of Human Trafficking Act
- Congress: 119
- Bill type: S
- Bill number: 361
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2026-04-22T20:06:26Z
- Update date including text: 2026-04-22T20:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/361",
    "number": "361",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Supporting Victims of Human Trafficking Act",
    "type": "S",
    "updateDate": "2026-04-22T20:06:26Z",
    "updateDateIncludingText": "2026-04-22T20:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T20:52:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s361is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 361\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Ossoff (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo strengthen trafficking victim assistance grant funding.\n#### 1. Short title\nThis Act may be cited as the Supporting Victims of Human Trafficking Act .\n#### 2. Grants to assist victims of trafficking\nSection 107(b)(2) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7105(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nin the matter preceding clause (i), by striking shall and insert may ;\n**(B)**\nin clause (i), by striking three percent and inserting up to 7 percent ;\n**(C)**\nin clause (ii)\u2014\n**(i)**\nby striking 5 percent and inserting up to 10 percent ; and\n**(ii)**\nby inserting and strengthening program administration and budgeting after activities ; and\n**(D)**\nin clause (iii), by striking one percent and inserting up to 1 percent ; and\n**(2)**\nin subparagraph (C), strike 75 percent and insert 95 percent .",
      "versionDate": "2025-02-03",
      "versionType": "Introduced in Senate"
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
            "name": "Crime victims",
            "updateDate": "2025-06-09T15:40:27Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-06-09T15:40:27Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-06-09T15:40:27Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-06-09T15:40:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-05T15:04:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-03",
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
          "measure-id": "id119s361",
          "measure-number": "361",
          "measure-type": "s",
          "orig-publish-date": "2025-02-03",
          "originChamber": "SENATE",
          "update-date": "2026-04-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s361v00",
            "update-date": "2026-04-22"
          },
          "action-date": "2025-02-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supporting Victims of Human Trafficking Act</strong></p><p>This bill increases\u00a0the percentage of the total allocation made available for trafficking victim services grants that may be set aside for research and for training and technical assistance.\u00a0</p><p>Specifically, the bill increases from 3% to 7% the amount that may be set aside for research, evaluation, and statistics; and increases from 5% to 10% the amount that may be set aside for training and technical assistance. Further, the bill allows the amount set aside for training and technical assistance to be used for strengthening program administration and budgeting.</p><p>The bill also increases from 75% to 95% the federal share of project costs.</p>"
        },
        "title": "Supporting Victims of Human Trafficking Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s361.xml",
    "summary": {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Victims of Human Trafficking Act</strong></p><p>This bill increases\u00a0the percentage of the total allocation made available for trafficking victim services grants that may be set aside for research and for training and technical assistance.\u00a0</p><p>Specifically, the bill increases from 3% to 7% the amount that may be set aside for research, evaluation, and statistics; and increases from 5% to 10% the amount that may be set aside for training and technical assistance. Further, the bill allows the amount set aside for training and technical assistance to be used for strengthening program administration and budgeting.</p><p>The bill also increases from 75% to 95% the federal share of project costs.</p>",
      "updateDate": "2026-04-22",
      "versionCode": "id119s361"
    },
    "title": "Supporting Victims of Human Trafficking Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Victims of Human Trafficking Act</strong></p><p>This bill increases\u00a0the percentage of the total allocation made available for trafficking victim services grants that may be set aside for research and for training and technical assistance.\u00a0</p><p>Specifically, the bill increases from 3% to 7% the amount that may be set aside for research, evaluation, and statistics; and increases from 5% to 10% the amount that may be set aside for training and technical assistance. Further, the bill allows the amount set aside for training and technical assistance to be used for strengthening program administration and budgeting.</p><p>The bill also increases from 75% to 95% the federal share of project costs.</p>",
      "updateDate": "2026-04-22",
      "versionCode": "id119s361"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s361is.xml"
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
      "title": "Supporting Victims of Human Trafficking Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting Victims of Human Trafficking Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to strengthen trafficking victim assistance grant funding.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:43Z"
    }
  ]
}
```
