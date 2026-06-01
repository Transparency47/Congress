# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/479?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/479
- Title: Healthy SNAP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 479
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-01-16T09:06:27Z
- Update date including text: 2026-01-16T09:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/479",
    "number": "479",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001317",
        "district": "2",
        "firstName": "Josh",
        "fullName": "Rep. Brecheen, Josh [R-OK-2]",
        "lastName": "Brecheen",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Healthy SNAP Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-16T09:06:27Z",
    "updateDateIncludingText": "2026-01-16T09:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T18:10:15Z",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "AZ"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MD"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "UT"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "CO"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr479ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 479\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Brecheen (for himself, Mr. Grothman , Mr. Schweikert , Mr. Biggs of Arizona , Mr. Cloud , Mr. Gosar , Mrs. Miller of Illinois , and Mr. Meuser ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to require the Secretary to designate food and food products to be made available under the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy SNAP Act of 2025 .\n#### 2. Food under supplemental nutrition assistance program\n##### (a) Definition of food\nSection 3(k)(1) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(k)(1) ) is amended\u2014\n**(1)**\nby striking except alcoholic beverages, tobacco and inserting the following designated by the Secretary under section 4(d), except any alcoholic beverages, tobacco, soft drinks, candy, ice cream, prepared desserts such as cakes, pies, cookies, or similar products ; and\n**(2)**\nby striking clauses and inserting paragraphs .\n##### (b) Designated food\nSection 4 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2013 ) is amended by adding at the end the following:\n(d) Designated food (1) In general Not later than 180 days after the date of enactment of this subsection, the Secretary shall designate by regulation the foods and food products that shall be included in the definition of the term food under section 3(k)(1). (2) Considerations In carrying out paragraph (1), the Secretary shall\u2014 (A) take into consideration food and food products that\u2014 (i) based on nutrition research, contain nutrients lacking in the diets of people in the United States; and (ii) promote the health of the population served by the supplemental nutrition assistance program, based on relevant nutrition science, public health concerns, and cultural eating patterns; and (B) to the maximum extent practicable, ensure that the fat, sugar, and salt content of the food and food products is appropriate. (3) Review of available foods As frequently as determined by the Secretary to be necessary to reflect the most recent scientific knowledge, but not less frequently than once every 5 years, the Secretary shall\u2014 (A) conduct a scientific review of the food and food products designated under paragraph (1); and (B) amend those foods and food products, as necessary, to reflect nutrition science, public health concerns, and cultural eating patterns. (4) Prepared meals Prepared meals described in section 3(k) shall have nutritional values consistent with regulations developed by the Secretary under this subsection. (5) Cultural Cuisines To allow for different cultural eating patterns, State agencies may, with the approval of the Secretary, substitute different food for food designated under paragraph (1) subject to the condition that the different food is nutritionally equivalent to the substituted food. .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-02-13",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "561",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Healthy SNAP Act of 2025",
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
        "updateDate": "2025-02-19T16:51:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr479",
          "measure-number": "479",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr479v00",
            "update-date": "2025-02-21"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Healthy SNAP Act of 2025</strong></p><p>This bill amends the Supplemental Nutrition Assistance Program (SNAP) to redefine the foods eligible for purchase with SNAP benefits.</p><p>Under the bill, SNAP benefits may not be used for soft drinks, candy, ice cream, or prepared desserts, such as cakes, pies, cookies, or similar products.</p><p>Further, the Department of Agriculture (USDA) must designate by regulation foods and food products to include in the SNAP definition of the term <em>food</em>. USDA must consider food and products that (1) based on nutrition research, contain nutrients lacking in the diets of people in the United States; and (2) promote the health of the population served by SNAP, based on relevant nutrition science, public health concerns, and cultural eating patterns. USDA must also, to the maximum extent practicable, ensure that the fat, sugar, and salt content of the food and food products are appropriate. At least every five years, USDA must review and amend the list.</p><p>In addition, prepared meals purchased with SNAP benefits must have nutritional values consistent with standards developed by USDA for the list of food and food products.</p><p>A state agency may substitute different foods for food USDA designated under this bill, with USDA approval, so long as the foods are nutritionally equivalent; this is permitted to allow for different cultural eating patterns.</p>"
        },
        "title": "Healthy SNAP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr479.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthy SNAP Act of 2025</strong></p><p>This bill amends the Supplemental Nutrition Assistance Program (SNAP) to redefine the foods eligible for purchase with SNAP benefits.</p><p>Under the bill, SNAP benefits may not be used for soft drinks, candy, ice cream, or prepared desserts, such as cakes, pies, cookies, or similar products.</p><p>Further, the Department of Agriculture (USDA) must designate by regulation foods and food products to include in the SNAP definition of the term <em>food</em>. USDA must consider food and products that (1) based on nutrition research, contain nutrients lacking in the diets of people in the United States; and (2) promote the health of the population served by SNAP, based on relevant nutrition science, public health concerns, and cultural eating patterns. USDA must also, to the maximum extent practicable, ensure that the fat, sugar, and salt content of the food and food products are appropriate. At least every five years, USDA must review and amend the list.</p><p>In addition, prepared meals purchased with SNAP benefits must have nutritional values consistent with standards developed by USDA for the list of food and food products.</p><p>A state agency may substitute different foods for food USDA designated under this bill, with USDA approval, so long as the foods are nutritionally equivalent; this is permitted to allow for different cultural eating patterns.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hr479"
    },
    "title": "Healthy SNAP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthy SNAP Act of 2025</strong></p><p>This bill amends the Supplemental Nutrition Assistance Program (SNAP) to redefine the foods eligible for purchase with SNAP benefits.</p><p>Under the bill, SNAP benefits may not be used for soft drinks, candy, ice cream, or prepared desserts, such as cakes, pies, cookies, or similar products.</p><p>Further, the Department of Agriculture (USDA) must designate by regulation foods and food products to include in the SNAP definition of the term <em>food</em>. USDA must consider food and products that (1) based on nutrition research, contain nutrients lacking in the diets of people in the United States; and (2) promote the health of the population served by SNAP, based on relevant nutrition science, public health concerns, and cultural eating patterns. USDA must also, to the maximum extent practicable, ensure that the fat, sugar, and salt content of the food and food products are appropriate. At least every five years, USDA must review and amend the list.</p><p>In addition, prepared meals purchased with SNAP benefits must have nutritional values consistent with standards developed by USDA for the list of food and food products.</p><p>A state agency may substitute different foods for food USDA designated under this bill, with USDA approval, so long as the foods are nutritionally equivalent; this is permitted to allow for different cultural eating patterns.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hr479"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr479ih.xml"
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
      "title": "Healthy SNAP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthy SNAP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to require the Secretary to designate food and food products to be made available under the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T11:03:25Z"
    }
  ]
}
```
