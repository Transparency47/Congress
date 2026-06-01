# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/57?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/57
- Title: MAPLE Act
- Congress: 119
- Bill type: S
- Bill number: 57
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-02-21T12:06:20Z
- Update date including text: 2025-02-21T12:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/57",
    "number": "57",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "MAPLE Act",
    "type": "S",
    "updateDate": "2025-02-21T12:06:20Z",
    "updateDateIncludingText": "2025-02-21T12:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T20:17:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ME"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-09",
      "state": "VT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-09",
      "state": "ME"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s57is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 57\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Welch (for himself, Ms. Collins , Mr. Schumer , Mr. Sanders , Mr. King , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Farm Security and Rural Investment Act of 2002 to include maple syrup under the seniors farmers\u2019 market nutrition program.\n#### 1. Short title\nThis Act may be cited as the Making Agricultural Products Locally Essential Act or the MAPLE Act .\n#### 2. Maple syrup under the seniors farmers\u2019 market nutrition program\nSection 4402(b)(1) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 3007(b)(1) ) is amended by inserting maple syrup, before and herbs .",
      "versionDate": "2025-01-09",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-02-19T16:44:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119s57",
          "measure-number": "57",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-02-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s57v00",
            "update-date": "2025-02-21"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Making Agricultural Products Locally Essential Act or the\u00a0MAPLE Act</strong></p><p>This bill includes maple syrup as one of the eligible\u00a0foods under the\u00a0Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>As background, the Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, herbs, and honey).</p>"
        },
        "title": "MAPLE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s57.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Making Agricultural Products Locally Essential Act or the\u00a0MAPLE Act</strong></p><p>This bill includes maple syrup as one of the eligible\u00a0foods under the\u00a0Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>As background, the Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, herbs, and honey).</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119s57"
    },
    "title": "MAPLE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Making Agricultural Products Locally Essential Act or the\u00a0MAPLE Act</strong></p><p>This bill includes maple syrup as one of the eligible\u00a0foods under the\u00a0Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>As background, the Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, herbs, and honey).</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119s57"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s57is.xml"
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
      "title": "MAPLE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MAPLE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Making Agricultural Products Locally Essential Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Farm Security and Rural Investment Act of 2002 to include maple syrup under the seniors farmers' market nutrition program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:20Z"
    }
  ]
}
```
