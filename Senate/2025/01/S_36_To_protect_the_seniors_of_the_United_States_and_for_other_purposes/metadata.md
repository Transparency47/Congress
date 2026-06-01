# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/36?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/36
- Title: Protect Our Seniors Act
- Congress: 119
- Bill type: S
- Bill number: 36
- Origin chamber: Senate
- Introduced date: 2025-01-08
- Update date: 2025-03-07T20:11:44Z
- Update date including text: 2025-03-07T20:11:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-08: Introduced in Senate
- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-01-08: Introduced in Senate

## Actions

- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-08",
    "latestAction": {
      "actionDate": "2025-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/36",
    "number": "36",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Protect Our Seniors Act",
    "type": "S",
    "updateDate": "2025-03-07T20:11:44Z",
    "updateDateIncludingText": "2025-03-07T20:11:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-08",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-08",
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
          "date": "2025-01-08T20:50:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s36is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 36\nIN THE SENATE OF THE UNITED STATES\nJanuary 8, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo protect the seniors of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Our Seniors Act .\n#### 2. Point of order for reductions in Medicare and Social Security benefits\nSection 301 of the Congressional Budget Act of 1974 ( 2 U.S.C. 632 ) is amended by adding at the end the following:\n(j) Medicare and Social Security point of order (1) In general It shall not be in order in the Senate to consider any bill or resolution (or amendment, motion, or conference report on that bill or resolution) that would reduce benefits under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) or benefits payable under title II of that Act ( 42 U.S.C. 401 et seq. ). (2) Waiver Paragraph (1) may be waived or suspended in the Senate only by the affirmative vote of two-thirds of the Members, duly chosen and sworn. .\n#### 3. Medicare point of order\nSection 301 of the Congressional Budget Act of 1974 ( 2 U.S.C. 632 ), as amended by section 3, is further amended by adding at the end the following:\n(k) Medicare point of order (1) In general It shall not be in order in the Senate to consider any bill or resolution (or amendment, motion, or conference report on that bill or resolution) for which the total budgetary effects of the measure, as determined by the Congressional Budget Office, use a decrease in outlays, or an increase in revenue, under the health insurance programs under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) to offset a cost of a provision of the measure that is not for the purpose of carrying out those programs. (2) Waiver Paragraph (1) may be waived or suspended in the Senate only by the affirmative vote of two-thirds of the Members, duly chosen and sworn. An affirmative vote of two-thirds of the Members of the Senate, duly chosen and sworn, shall be required to sustain an appeal of the ruling of the Chair on a point of order raised under paragraph (1). .",
      "versionDate": "2025-01-08",
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
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-05T16:08:37Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-03-05T16:08:27Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-03-05T16:08:42Z"
          },
          {
            "name": "Social security and elderly assistance",
            "updateDate": "2025-03-05T16:08:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-02-28T14:57:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-08",
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
          "measure-id": "id119s36",
          "measure-number": "36",
          "measure-type": "s",
          "orig-publish-date": "2025-01-08",
          "originChamber": "SENATE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s36v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protect Our Seniors Act</strong></p><p>This bill establishes Senate budget enforcement procedures (known as points of order) against measures that (1) reduce Medicare or Social Security benefits, or (2) use revenue or savings from the Medicare program to offset the cost of provisions unrelated to carrying out Medicare.</p><p>Points of order are prohibitions against certain\u00a0categories of legislation or congressional action. A point of order raised on the grounds established under the bill may be waived or suspended only by an affirmative vote of two-thirds of the Senators.</p>"
        },
        "title": "Protect Our Seniors Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s36.xml",
    "summary": {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Our Seniors Act</strong></p><p>This bill establishes Senate budget enforcement procedures (known as points of order) against measures that (1) reduce Medicare or Social Security benefits, or (2) use revenue or savings from the Medicare program to offset the cost of provisions unrelated to carrying out Medicare.</p><p>Points of order are prohibitions against certain\u00a0categories of legislation or congressional action. A point of order raised on the grounds established under the bill may be waived or suspended only by an affirmative vote of two-thirds of the Senators.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119s36"
    },
    "title": "Protect Our Seniors Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Our Seniors Act</strong></p><p>This bill establishes Senate budget enforcement procedures (known as points of order) against measures that (1) reduce Medicare or Social Security benefits, or (2) use revenue or savings from the Medicare program to offset the cost of provisions unrelated to carrying out Medicare.</p><p>Points of order are prohibitions against certain\u00a0categories of legislation or congressional action. A point of order raised on the grounds established under the bill may be waived or suspended only by an affirmative vote of two-thirds of the Senators.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119s36"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s36is.xml"
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
      "title": "Protect Our Seniors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Our Seniors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the seniors of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:20Z"
    }
  ]
}
```
