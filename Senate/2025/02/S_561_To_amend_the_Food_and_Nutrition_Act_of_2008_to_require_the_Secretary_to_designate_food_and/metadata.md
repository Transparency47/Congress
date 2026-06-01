# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/561?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/561
- Title: Healthy SNAP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 561
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-01-14T12:03:37Z
- Update date including text: 2026-01-14T12:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/561",
    "number": "561",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Healthy SNAP Act of 2025",
    "type": "S",
    "updateDate": "2026-01-14T12:03:37Z",
    "updateDateIncludingText": "2026-01-14T12:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
            "date": "2025-02-13T17:08:20Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-13T17:08:20Z",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ND"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AL"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "UT"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "WY"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s561is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 561\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Lee (for himself, Mr. Cramer , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act of 2008 to require the Secretary to designate food and food products to be made available under the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy SNAP Act of 2025 .\n#### 2. Food under supplemental nutrition assistance program\n##### (a) Definition of food\nSection 3(k)(1) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(k)(1) ) is amended\u2014\n**(1)**\nby striking except alcoholic beverages, tobacco and inserting designated by the Secretary under section 4(d), except any alcoholic beverages, tobacco, soft drinks, candy, ice cream, prepared desserts such as cakes, pies, cookies, or similar products ; and\n**(2)**\nby striking clauses and inserting paragraphs .\n##### (b) Designated food\nSection 4 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2013 ) is amended by adding at the end the following:\n(d) Designated food (1) In general Not later than 180 days after the date of enactment of this subsection, the Secretary shall designate by regulation the foods and food products that shall be included in the definition of the term food under section 3(k)(1). (2) Considerations In carrying out paragraph (1), the Secretary shall\u2014 (A) take into consideration food and food products that\u2014 (i) based on nutrition research, contain nutrients lacking in the diets of people in the United States; and (ii) promote the health of the population served by the supplemental nutrition assistance program, based on relevant nutrition science, public health concerns, and cultural eating patterns; and (B) to the maximum extent practicable, ensure that the fat, sugar, and salt content of the food and food products is appropriate. (3) Review of available foods As frequently as determined by the Secretary to be necessary to reflect the most recent scientific knowledge, but not less frequently than once every 5 years, the Secretary shall\u2014 (A) conduct a scientific review of the food and food products designated under paragraph (1); and (B) amend those foods and food products, as necessary, to reflect nutrition science, public health concerns, and cultural eating patterns. (4) Prepared meals Prepared meals described in section 3(k) shall have nutritional values consistent with regulations developed by the Secretary under this subsection. (5) Cultural Cuisines To allow for different cultural eating patterns, State agencies may, with the approval of the Secretary, substitute different food for food designated under paragraph (1) subject to the condition that the different food is nutritionally equivalent to the substituted food. .",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-14",
        "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture."
      },
      "number": "479",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Healthy SNAP Act of 2025",
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
        "updateDate": "2025-03-20T19:51:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119s561",
          "measure-number": "561",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s561v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Healthy SNAP Act of 2025</strong></p><p>This bill amends the Supplemental Nutrition Assistance Program (SNAP) to redefine the foods eligible for purchase with SNAP benefits.</p><p>Under the bill, SNAP benefits may not be used for soft drinks, candy, ice cream, or prepared desserts, such as cakes, pies, cookies, or similar products.</p><p>Further, the Department of Agriculture (USDA) must designate by regulation foods and food products to include in the SNAP definition of the term <em>food</em>. USDA must consider food and products that (1) based on nutrition research, contain nutrients lacking in the diets of people in the United States; and (2) promote the health of the population served by SNAP, based on relevant nutrition science, public health concerns, and cultural eating patterns. USDA must also, to the maximum extent practicable, ensure that the fat, sugar, and salt content of the food and food products are appropriate. At least every five years, USDA must review and amend the list.</p><p>In addition, prepared meals purchased with SNAP benefits must have nutritional values consistent with standards developed by USDA for the list of food and food products.</p><p>A state agency may substitute different foods for food USDA designated under this bill, with USDA approval, so long as the foods are nutritionally equivalent; this is permitted to allow for different cultural eating patterns.</p>"
        },
        "title": "Healthy SNAP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s561.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Healthy SNAP Act of 2025</strong></p><p>This bill amends the Supplemental Nutrition Assistance Program (SNAP) to redefine the foods eligible for purchase with SNAP benefits.</p><p>Under the bill, SNAP benefits may not be used for soft drinks, candy, ice cream, or prepared desserts, such as cakes, pies, cookies, or similar products.</p><p>Further, the Department of Agriculture (USDA) must designate by regulation foods and food products to include in the SNAP definition of the term <em>food</em>. USDA must consider food and products that (1) based on nutrition research, contain nutrients lacking in the diets of people in the United States; and (2) promote the health of the population served by SNAP, based on relevant nutrition science, public health concerns, and cultural eating patterns. USDA must also, to the maximum extent practicable, ensure that the fat, sugar, and salt content of the food and food products are appropriate. At least every five years, USDA must review and amend the list.</p><p>In addition, prepared meals purchased with SNAP benefits must have nutritional values consistent with standards developed by USDA for the list of food and food products.</p><p>A state agency may substitute different foods for food USDA designated under this bill, with USDA approval, so long as the foods are nutritionally equivalent; this is permitted to allow for different cultural eating patterns.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s561"
    },
    "title": "Healthy SNAP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Healthy SNAP Act of 2025</strong></p><p>This bill amends the Supplemental Nutrition Assistance Program (SNAP) to redefine the foods eligible for purchase with SNAP benefits.</p><p>Under the bill, SNAP benefits may not be used for soft drinks, candy, ice cream, or prepared desserts, such as cakes, pies, cookies, or similar products.</p><p>Further, the Department of Agriculture (USDA) must designate by regulation foods and food products to include in the SNAP definition of the term <em>food</em>. USDA must consider food and products that (1) based on nutrition research, contain nutrients lacking in the diets of people in the United States; and (2) promote the health of the population served by SNAP, based on relevant nutrition science, public health concerns, and cultural eating patterns. USDA must also, to the maximum extent practicable, ensure that the fat, sugar, and salt content of the food and food products are appropriate. At least every five years, USDA must review and amend the list.</p><p>In addition, prepared meals purchased with SNAP benefits must have nutritional values consistent with standards developed by USDA for the list of food and food products.</p><p>A state agency may substitute different foods for food USDA designated under this bill, with USDA approval, so long as the foods are nutritionally equivalent; this is permitted to allow for different cultural eating patterns.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s561"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s561is.xml"
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
      "title": "Healthy SNAP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T12:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act of 2008 to require the Secretary to designate food and food products to be made available under the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthy SNAP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    }
  ]
}
```
