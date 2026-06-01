# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2379
- Title: Farmers’ Market Expansion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2379
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-12-05T21:55:28Z
- Update date including text: 2025-12-05T21:55:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2379",
    "number": "2379",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Farmers\u2019 Market Expansion Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:55:28Z",
    "updateDateIncludingText": "2025-12-05T21:55:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:10:00Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NM"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2379ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2379\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Moore of Alabama (for himself and Mr. Vasquez ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Farm Security and Rural Investment Act of 2002 to include the provision of tree nuts (including shelled tree nuts) under the seniors farmers\u2019 market nutrition program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmers\u2019 Market Expansion Act of 2025 .\n#### 2. Seniors farmers' market nutrition program\nSection 4402(b)(1) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 3007(b)(1) ) is amended by striking and herbs and inserting herbs, and tree nuts (including shelled tree nuts) .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-03-26",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1145",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Farmers\u2019 Market Expansion Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:22:23Z"
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
          "measure-id": "id119hr2379",
          "measure-number": "2379",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-26",
          "originChamber": "HOUSE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2379v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Farmers\u2019 Market Expansion Act of 2025</strong></p><p>This bill includes tree nuts (including shelled tree nuts) as one of the eligible foods under the Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>The Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, honey, and herbs).</p>"
        },
        "title": "Farmers\u2019 Market Expansion Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2379.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Farmers\u2019 Market Expansion Act of 2025</strong></p><p>This bill includes tree nuts (including shelled tree nuts) as one of the eligible foods under the Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>The Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, honey, and herbs).</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119hr2379"
    },
    "title": "Farmers\u2019 Market Expansion Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Farmers\u2019 Market Expansion Act of 2025</strong></p><p>This bill includes tree nuts (including shelled tree nuts) as one of the eligible foods under the Senior Farmers' Market Nutrition Program (SFMNP).\u00a0</p><p>The Department of Agriculture's\u00a0SFMNP provides grants to participating states to provide low-income seniors with coupons/vouchers that\u00a0may be used at farmers\u2019 markets, roadside stands, and community supported agriculture programs to purchase eligible foods (i.e., fresh, nutritious, unprepared, locally-grown fruits, vegetables, honey, and herbs).</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119hr2379"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2379ih.xml"
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
      "title": "Farmers\u2019 Market Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farmers\u2019 Market Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Farm Security and Rural Investment Act of 2002 to include the provision of tree nuts (including shelled tree nuts) under the seniors farmers' market nutrition program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:26Z"
    }
  ]
}
```
