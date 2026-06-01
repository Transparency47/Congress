# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1145
- Title: Farmers’ Market Expansion Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1145
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-12-18T12:03:18Z
- Update date including text: 2025-12-18T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1145",
    "number": "1145",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Farmers\u2019 Market Expansion Act of 2025",
    "type": "S",
    "updateDate": "2025-12-18T12:03:18Z",
    "updateDateIncludingText": "2025-12-18T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T16:36:45Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NM"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1145is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1145\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Tuberville (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Farm Security and Rural Investment Act of 2002 to include the provision of tree nuts under the seniors farmers\u2019 market nutrition program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmers\u2019 Market Expansion Act of 2025 .\n#### 2. Seniors farmers' market nutrition program\nSection 4402(b)(1) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 3007(b)(1) ) is amended by striking and herbs and inserting herbs, and tree nuts (including shelled tree nuts) .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-04-18",
        "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture."
      },
      "number": "2379",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Farmers\u2019 Market Expansion Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:14:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
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
          "measure-id": "id119s1145",
          "measure-number": "1145",
          "measure-type": "s",
          "orig-publish-date": "2025-03-26",
          "originChamber": "SENATE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1145v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Farmers\u2019 Market Expansion Act of 2025</strong></p><p>This bill includes tree nuts (including shelled tree nuts) as one of the eligible foods under the Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>The Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, honey, and herbs).</p>"
        },
        "title": "Farmers\u2019 Market Expansion Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1145.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farmers\u2019 Market Expansion Act of 2025</strong></p><p>This bill includes tree nuts (including shelled tree nuts) as one of the eligible foods under the Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>The Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, honey, and herbs).</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s1145"
    },
    "title": "Farmers\u2019 Market Expansion Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farmers\u2019 Market Expansion Act of 2025</strong></p><p>This bill includes tree nuts (including shelled tree nuts) as one of the eligible foods under the Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>The Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, honey, and herbs).</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s1145"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1145is.xml"
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
      "title": "Farmers\u2019 Market Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farmers\u2019 Market Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Farm Security and Rural Investment Act of 2002 to include the provision of tree nuts under the seniors farmers' market nutrition program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:31Z"
    }
  ]
}
```
