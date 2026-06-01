# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4725?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4725
- Title: TRUTH in Labeling Act
- Congress: 119
- Bill type: HR
- Bill number: 4725
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-04-28T08:06:27Z
- Update date including text: 2026-04-28T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4725",
    "number": "4725",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "TRUTH in Labeling Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:27Z",
    "updateDateIncludingText": "2026-04-28T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:14:30Z",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CT"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IN"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CT"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4725ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4725\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Schakowsky (for herself, Ms. DeLauro , Mr. Doggett , Mr. Thanedar , and Mr. Carson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo strengthen requirements related to nutrient information on food labels.\n#### 1. Short title\nThis Act may be cited as the Transparency, Readability, Understandability, Truth, and Helpfulness in Labeling Act or the TRUTH in Labeling Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe average American consumes substantially more added sugars, sodium, and saturated fat than is recommended by the Dietary Guidelines for Americans published under section 301 of the National Nutrition Monitoring and Related Research Act of 1990 ( 7 U.S.C. 5341 ), potentially increasing their risk for hypertension, type-2 diabetes, and heart disease.\n**(2)**\nA large body of experimental and real-world evidence has demonstrated that front-of-package labels that highlight high levels of added sugars, sodium, and saturated fat can significantly improve the nutritional quality of foods that consumers purchase or select.\n**(3)**\nUse of the nutrition facts label is lower among individuals with lower educational attainment and lower incomes, and robust research shows that front-of-package labels can be particularly beneficial for busy shoppers and for those with less nutrition literacy.\n**(4)**\nFront-of-package nutrition labeling gives consumers quick and easy access to key information about the healthfulness of foods and can support healthier choices for consumers and their families.\n**(5)**\nStudies also show that front-of-package labeling can improve consumers\u2019 understanding of the relative healthfulness of different foods.\n**(6)**\nPublic health organizations advise that children should not consume non-nutritive sweeteners. Real-world evidence has demonstrated that front-of-package labeling policies that highlight high levels of sugar, sodium, and saturated fat, but that do not disclose the presence of non-nutritive sweeteners, are associated with the food industry reformulating products to have lower levels of sugar, sodium, and saturated fat, but increased levels of non-nutritive sweeteners.\n**(7)**\nReal-world evidence has demonstrated that front-of-package label policies that highlight high levels of sugar, sodium, and saturated fat, and disclose the presence of non-nutritive sweeteners (with an advisory that children should avoid them), are associated with the food industry reducing the amount of sugar, sodium, saturated fat, and non-nutritive sweeteners in their products.\n#### 3. Requirements for front-of-package labeling for foods\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this section as the Secretary ) shall finalize the proposed rule entitled Food Labeling: Front-of-Package Nutrition Information (90 Fed. Reg. 5426 (January 16, 2025)).\n##### (b) Requirements\n**(1) In general**\nThe final rule required by subsection (a) shall require a food (as defined in section 201(f) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(f) )) intended for human consumption and offered for sale to bear nutrition labeling that includes the following:\n**(A)**\nA label on the principal display panel that details and identifies high amounts of added sugars, sodium, or saturated fat, as applicable. Such principal display panel shall include a separate label for each such nutrient, as applicable. Such labels shall designate high amounts of added sugars, sodium, or saturated fat based on Daily Values for adults, children ages 1 to 3 years, and infants through age 12 months, as applicable. Such labels shall include the words High in and a conspicuous exclamation point icon.\n**(B)**\nIf applicable, a statement on the principle display panel that declares that the food contains non-nutritive sweeteners, with a factual statement that non-nutritive sweeteners are not recommended for children. Such statement shall appear adjacent to the one or more High in labels described in subparagraph (A), if applicable.\n**(2) Application to foods for children**\nNotwithstanding section 101.9(j)(5) of title 21, Code of Federal Regulations (as in effect on the date of enactment of this Act), the labeling requirements described in subparagraphs (A) and (B) of paragraph (1) shall apply to foods, other than infant formula, that are represented or purported to be specifically for infants through 12 months of age and children 1 through 4 years of age.\n##### (c) Daily Reference Values and percent Daily Values\n**(1) In general**\nIn carrying out subsections (a) and (b), the Secretary shall establish Daily Reference Values and percent Daily Values for added sugars, sodium, and saturated fat for infants through 12 months of age and update the Daily Reference Values and percent Daily Values for added sugars, sodium, and saturated fat for children 1 to 3 years in alignment with the recommendations in the 2020\u20132025 Dietary Guidelines for Americans published by the Secretary and the Secretary of Agriculture.\n**(2) No delay in finalizing rule**\n**(A) In general**\nIf the Secretary determines that establishing Daily Reference Values and percent Daily Values as described in paragraph (1) for inclusion in the final rule required by subsection (a) would prevent the issuance of such final rule by the deadline described in such subsection, the Secretary shall issue such final rule before establishing such Daily Reference Values and percent Daily Values.\n**(B) Revisions**\nIf the Secretary finalizes the rule as required by subsection (a) before establishing Daily Reference Values and percent Daily Values, as described in subparagraph (A), the Secretary, as soon as practicable after establishing such Daily Reference Values and percent Daily Values, shall revise such final rule to include such Daily Reference Values and percent Daily Values.\n##### (d) Limitation\nNothing in this section or in the final rule required by subsection (a) shall prevent the Secretary from revising paragraph (4) of section 101.61(b) of title 21, Code of Federal Regulations, to update the limit for the low sodium nutrient content claim to 115 milligrams per reference amount customarily consumed or paragraph (5) of such section to update the limit for the low sodium nutrient content claim to 115 milligrams per 100 grams, to align with current nutrition science.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2462",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TRUTH in Labeling Act",
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
        "name": "Health",
        "updateDate": "2025-09-16T14:25:19Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4725ih.xml"
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
      "title": "TRUTH in Labeling Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRUTH in Labeling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transparency, Readability, Understandability, Truth, and Helpfulness in Labeling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To strengthen requirements related to nutrient information on food labels.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T12:18:18Z"
    }
  ]
}
```
