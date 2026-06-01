# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7880?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7880
- Title: Interstate Milk Freedom Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7880
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-07T16:12:18Z
- Update date including text: 2026-04-07T16:12:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7880",
    "number": "7880",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Interstate Milk Freedom Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-07T16:12:18Z",
    "updateDateIncludingText": "2026-04-07T16:12:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "ME"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "OH"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "WI"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "LA"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "PA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "TX"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "PA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "CO"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7880ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7880\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Massie (for himself, Ms. Pingree , Mr. Davidson , Mr. Grothman , Mr. Higgins of Louisiana , Mr. Perry , Mr. Roy , Mr. Smucker , Ms. Boebert , and Ms. Mace ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit Federal interference with the interstate traffic of unpasteurized milk and milk products that are packaged for direct human consumption.\n#### 1. Short title\nThis Act may be cited as the Interstate Milk Freedom Act of 2026 .\n#### 2. Interstate traffic of unpasteurized milk and milk products\n##### (a) In general\nNotwithstanding the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ), section 361 of the Public Health Service Act ( 42 U.S.C. 264 ), and any regulations or other guidance thereunder, a Federal department, agency, or court may not take any action (including any administrative, civil, criminal, or other action) that would prohibit, interfere with, regulate, or otherwise restrict the interstate traffic of milk, or a milk product, that is unpasteurized and packaged for direct human consumption, if\u2014\n**(1)**\nsuch prohibition, interference, regulation, or restriction is based on a determination that, solely because such milk or milk product is unpasteurized, such milk or milk product is adulterated, misbranded, or otherwise in violation of Federal law;\n**(2)**\nthe milk or milk product\u2019s State of origin allows (by law, regulation, or policy) unpasteurized milk or unpasteurized milk products to be distributed for direct human consumption by any means, including any form of retail sale, direct farm to consumer distribution, or cowshare;\n**(3)**\nthe milk or milk product is produced, packaged, and moved in compliance with the laws of such State of origin, including any such laws relating to labeling, warning, and packaging requirements; and\n**(4)**\nthe milk or milk product is moved from the State of origin with the intent to transport the milk or milk product to another State which allows the distribution of unpasteurized milk or unpasteurized milk products for direct human consumption, as described in paragraph (2), irrespective of whether the applicable laws of such other State are identical to the laws of the State of origin.\n##### (b) No preemption\nNothing in this Act preempts any State law.\n##### (c) Definitions\nIn this Act, the following definitions apply:\n**(1)**\nThe term cowshare means an undivided interest in a milk-producing animal (such as a cow, goat, sheep, or water buffalo, or a herd of such animals) created by a written contractual relationship between a consumer and a farmer\u2014\n**(A)**\nthat includes a legal bill of sale to the consumer for an interest in the animal or dairy herd and a boarding contract under which the consumer boards the animal or dairy herd in which the consumer has an interest with the farmer for care and milking; and\n**(B)**\nunder which the consumer is entitled to receive a share of milk from the animal or dairy herd.\n**(2)**\nThe term milk means the lacteal secretion, practically free from colostrum, obtained by the milking of one or more healthy animals.\n**(3)**\nThe term milk product \u2014\n**(A)**\nmeans a food product made from milk; and\n**(B)**\nincludes low-fat milk, skim milk, cream, half and half, dry milk, nonfat milk, dry cream, condensed or concentrated milk products, cultured or acidified milk or milk products, kefir, eggnog, yogurt, butter, cheese, whey, condensed or dry whey or whey products, ice cream, ice milk, and other frozen dairy desserts.\n**(4)**\nThe term packaged for direct human consumption with respect to milk or milk products\u2014\n**(A)**\nmeans packaged for the final consumer and intended for human consumption; and\n**(B)**\ndoes not apply if the milk or milk products are packaged for additional processing, including pasteurization, before being consumed by humans.\n**(5)**\nThe term pasteurized means the process of\u2014\n**(A)**\nheating milk or milk products to the applicable temperature specified in the tables contained in section 1240.61 of title 21, Code of Federal Regulations (as in effect on the date of enactment of this Act); and\n**(B)**\nholding the milk or milk product continuously at or above that temperature for at least the corresponding specified time in such tables.\n**(6)**\nThe term unpasteurized means not pasteurized.",
      "versionDate": "2026-03-09",
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
        "name": "Health",
        "updateDate": "2026-04-07T13:52:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-09",
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
          "measure-id": "id119hr7880",
          "measure-number": "7880",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-09",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7880v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2026-03-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Interstate Milk Freedom Act of 2026 </strong><br/><br/>This bill prohibits federal regulation of the interstate traffic of unpasteurized milk or milk products packaged for direct human consumption under specified circumstances.</p><p>Specifically, the prohibition applies if such products (1) would be considered in violation of federal law solely because they are unpasteurized; (2) are allowed by the state of origin to be distributed for direct human consumption by any means; (3) are produced, packaged, and moved in compliance with the laws of such state; and (4) are moved from the state of origin with the intent to transport them to another state that allows the distribution of such products for direct human consumption.</p>"
        },
        "title": "Interstate Milk Freedom Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7880.xml",
    "summary": {
      "actionDate": "2026-03-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Interstate Milk Freedom Act of 2026 </strong><br/><br/>This bill prohibits federal regulation of the interstate traffic of unpasteurized milk or milk products packaged for direct human consumption under specified circumstances.</p><p>Specifically, the prohibition applies if such products (1) would be considered in violation of federal law solely because they are unpasteurized; (2) are allowed by the state of origin to be distributed for direct human consumption by any means; (3) are produced, packaged, and moved in compliance with the laws of such state; and (4) are moved from the state of origin with the intent to transport them to another state that allows the distribution of such products for direct human consumption.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hr7880"
    },
    "title": "Interstate Milk Freedom Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Interstate Milk Freedom Act of 2026 </strong><br/><br/>This bill prohibits federal regulation of the interstate traffic of unpasteurized milk or milk products packaged for direct human consumption under specified circumstances.</p><p>Specifically, the prohibition applies if such products (1) would be considered in violation of federal law solely because they are unpasteurized; (2) are allowed by the state of origin to be distributed for direct human consumption by any means; (3) are produced, packaged, and moved in compliance with the laws of such state; and (4) are moved from the state of origin with the intent to transport them to another state that allows the distribution of such products for direct human consumption.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hr7880"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7880ih.xml"
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
      "title": "Interstate Milk Freedom Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Interstate Milk Freedom Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal interference with the interstate traffic of unpasteurized milk and milk products that are packaged for direct human consumption.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:21Z"
    }
  ]
}
```
