# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/813?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/813
- Title: SHOPP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 813
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2026-03-26T18:44:26Z
- Update date including text: 2026-03-26T18:44:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/813",
    "number": "813",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SHOPP Act of 2025",
    "type": "S",
    "updateDate": "2026-03-26T18:44:26Z",
    "updateDateIncludingText": "2026-03-26T18:44:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
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
        "item": [
          {
            "date": "2025-03-03T20:41:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-03T20:41:30Z",
            "name": "Referred To"
          }
        ]
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
      "sponsorshipDate": "2025-03-03",
      "state": "NM"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-09",
      "state": "ME"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "VA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s813is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 813\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Cornyn (for himself, Mr. Luj\u00e1n , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food, Conservation, and Energy Act of 2008 to provide families year-round access to nutrition incentives under the Gus Schumacher Nutrition Incentive Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting all Healthy Options when Purchasing Produce Act of 2025 or the SHOPP Act of 2025 .\n#### 2. Nutrition incentives under Gus Schumacher Nutrition Incentive Program\nSection 4405 of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 7517 ) is amended\u2014\n**(1)**\nin subsection (b)(2)(B)\u2014\n**(A)**\nby redesignating clauses (ix) and (x) as clauses (x) and (xi), respectively; and\n**(B)**\nby inserting after clause (viii) the following:\n(ix) increase the year-round availability of the incentive described in subparagraph (A)(ii)(II) by offering fresh frozen fruits or vegetables; ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A), by striking fruits and vegetables and inserting fruits, vegetables, and legumes ; and\n**(B)**\nin paragraph (3), by striking fresh fruits and vegetables each place it appears and inserting fresh or fresh frozen fruits, vegetables, and legumes .",
      "versionDate": "2025-03-03",
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
        "actionDate": "2025-03-28",
        "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture."
      },
      "number": "1782",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SHOPP Act of 2025",
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
        "updateDate": "2025-05-16T13:53:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119s813",
          "measure-number": "813",
          "measure-type": "s",
          "orig-publish-date": "2025-03-03",
          "originChamber": "SENATE",
          "update-date": "2026-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s813v00",
            "update-date": "2026-03-26"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supporting all Healthy Options when Purchasing Produce Act of 2025 or the SHOPP Act\u00a0of 2025</strong></p><p>This bill modifies the\u00a0Gus Schumacher Nutrition Incentive Program\u00a0(GusNIP) to include fresh frozen fruits and vegetables.</p><p>GusNIP is\u00a0a Department of Agriculture\u00a0(USDA) program that provides grants for projects that increase low-income consumers' purchases of fruits and vegetables. It\u00a0is made up of three competitive grant programs, including the GusNIP Nutrition Incentive Program, which provides grants for projects that provide incentives for Supplemental Nutrition Assistance Program (SNAP) participants to purchase\u00a0fruits and vegetables.</p><p>The bill\u00a0directs USDA, in awarding GusNIP Nutrition Incentive Program grants, to give priority to projects that\u00a0increase year-round availability of nutrition incentives by offering fresh frozen fruits or vegetables in the program.</p><p>In addition, the bill amends another GusNIP program,\u00a0the Produce Prescription Program, to include fresh frozen fruits and vegetables, as well as fresh and fresh frozen legumes. Currently, only fresh fruits and vegetables are covered under the program.</p><p>The\u00a0GusNIP Produce Prescription Program supports projects that demonstrate and evaluate the impact of fruit and vegetable prescriptions on\u00a0increasing procurement and consumption of fruits and vegetables, reducing individual and household food insecurity, and reducing healthcare usage and associated costs.</p>"
        },
        "title": "SHOPP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s813.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting all Healthy Options when Purchasing Produce Act of 2025 or the SHOPP Act\u00a0of 2025</strong></p><p>This bill modifies the\u00a0Gus Schumacher Nutrition Incentive Program\u00a0(GusNIP) to include fresh frozen fruits and vegetables.</p><p>GusNIP is\u00a0a Department of Agriculture\u00a0(USDA) program that provides grants for projects that increase low-income consumers' purchases of fruits and vegetables. It\u00a0is made up of three competitive grant programs, including the GusNIP Nutrition Incentive Program, which provides grants for projects that provide incentives for Supplemental Nutrition Assistance Program (SNAP) participants to purchase\u00a0fruits and vegetables.</p><p>The bill\u00a0directs USDA, in awarding GusNIP Nutrition Incentive Program grants, to give priority to projects that\u00a0increase year-round availability of nutrition incentives by offering fresh frozen fruits or vegetables in the program.</p><p>In addition, the bill amends another GusNIP program,\u00a0the Produce Prescription Program, to include fresh frozen fruits and vegetables, as well as fresh and fresh frozen legumes. Currently, only fresh fruits and vegetables are covered under the program.</p><p>The\u00a0GusNIP Produce Prescription Program supports projects that demonstrate and evaluate the impact of fruit and vegetable prescriptions on\u00a0increasing procurement and consumption of fruits and vegetables, reducing individual and household food insecurity, and reducing healthcare usage and associated costs.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119s813"
    },
    "title": "SHOPP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting all Healthy Options when Purchasing Produce Act of 2025 or the SHOPP Act\u00a0of 2025</strong></p><p>This bill modifies the\u00a0Gus Schumacher Nutrition Incentive Program\u00a0(GusNIP) to include fresh frozen fruits and vegetables.</p><p>GusNIP is\u00a0a Department of Agriculture\u00a0(USDA) program that provides grants for projects that increase low-income consumers' purchases of fruits and vegetables. It\u00a0is made up of three competitive grant programs, including the GusNIP Nutrition Incentive Program, which provides grants for projects that provide incentives for Supplemental Nutrition Assistance Program (SNAP) participants to purchase\u00a0fruits and vegetables.</p><p>The bill\u00a0directs USDA, in awarding GusNIP Nutrition Incentive Program grants, to give priority to projects that\u00a0increase year-round availability of nutrition incentives by offering fresh frozen fruits or vegetables in the program.</p><p>In addition, the bill amends another GusNIP program,\u00a0the Produce Prescription Program, to include fresh frozen fruits and vegetables, as well as fresh and fresh frozen legumes. Currently, only fresh fruits and vegetables are covered under the program.</p><p>The\u00a0GusNIP Produce Prescription Program supports projects that demonstrate and evaluate the impact of fruit and vegetable prescriptions on\u00a0increasing procurement and consumption of fruits and vegetables, reducing individual and household food insecurity, and reducing healthcare usage and associated costs.</p>",
      "updateDate": "2026-03-26",
      "versionCode": "id119s813"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s813is.xml"
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
      "title": "SHOPP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SHOPP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting all Healthy Options when Purchasing Produce Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food, Conservation, and Energy Act of 2008 to provide families year-round access to nutrition incentives under the Gus Schumacher Nutrition Incentive Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:53Z"
    }
  ]
}
```
