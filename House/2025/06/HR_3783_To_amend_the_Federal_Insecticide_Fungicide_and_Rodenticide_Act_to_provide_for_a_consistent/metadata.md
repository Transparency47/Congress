# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3783?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3783
- Title: Plant Biostimulant Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3783
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2026-02-21T09:05:37Z
- Update date including text: 2026-02-21T09:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3783",
    "number": "3783",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Plant Biostimulant Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-21T09:05:37Z",
    "updateDateIncludingText": "2026-02-21T09:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IN"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "IL"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "NC"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NE"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3783ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3783\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Panetta (for himself and Mr. Baird ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Insecticide, Fungicide, and Rodenticide Act to provide for a consistent definition for plant biostimulants.\n#### 1. Short title\nThis Act may be cited as the Plant Biostimulant Act of 2025 .\n#### 2. Defining plant biostimulants\n##### (a) In general\nSection 2 of the Federal Insecticide, Fungicide, and Rodenticide Act ( 7 U.S.C. 136 ) is amended\u2014\n**(1)**\nby striking subsection (v) and inserting the following:\n(v) Plant regulator (1) In general The term plant regulator means any substance or mixture of substances intended, through physiological action, for accelerating or retarding the rate of growth or rate of maturation, or for otherwise altering the behavior, of plants or the produce thereof. (2) Exclusions The term plant regulator does not include\u2014 (A) substances to the extent that they are intended as plant nutrients, trace elements, nutritional chemicals, plant inoculants, soil amendments, or vitamin hormone products; or (B) plant biostimulants that\u2014 (i) are of biological origin; or (ii) include chemical compounds that are synthetically derived, but are structurally similar and functionally identical to, substances of biological origin. ;\n**(2)**\nin subsection (hh)\u2014\n**(A)**\nin paragraph (2), by striking or at the end;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking substances. and inserting substances ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby inserting , or after volatilization ; and\n**(II)**\nby striking the period at the end and inserting a semicolon; and\n**(C)**\nby inserting before the undesignated matter following paragraph (3) the following:\n(4) a plant biostimulant; or (5) a nutritional chemical. ; and\n**(3)**\nby adding at the end the following:\n(pp) Plant biostimulant The term plant biostimulant means a substance, microorganism, or mixture thereof, that, when applied to seeds, plants, the rhizosphere, soil, or other growth media, act to support a plant\u2019s natural processes independently of the nutrient content of that substance, microorganism, or mixture thereof, and that thereby improves\u2014 (1) nutrient availability, uptake, or use efficiency; (2) tolerance to abiotic stress; and (3) consequent growth, development, quality, or yield. (qq) Nutritional chemical The term nutritional chemical \u2014 (1) means any substance or mixture of substances that interacts with plant nutrients in a manner which improves nutrient availability or aids the plant in acquiring or utilizing plant nutrients; and (2) includes some plant biostimulants. (rr) Vitamin hormone product The term vitamin hormone product means a product consisting of a mixture of plant hormones, plant nutrients, inoculants, or soil amendments. .\n##### (b) Regulations\nNot later than 120 days after the date of the enactment of this Act, the Administrator of Environmental Protection Agency shall revise the regulations under subchapter E of chapter I of title 40, Code of Federal Regulations (as in effect on the date of the enactment of this Act) to carry out the amendments made by subsection (a).\n#### 3. Soil health study\n##### (a) Study\nThe Secretary of Agriculture (referred to in this section as the Secretary ) shall conduct a study to assess the types of, and practices using, plant biostimulants (as defined in section 2 of the Federal Insecticide, Fungicide, and Rodenticide Act ( 7 U.S.C. 136 ), as added by section 2 of this Act) that best achieve the following:\n**(1)**\nIncreasing organic matter content.\n**(2)**\nReducing atmospheric volatilization.\n**(3)**\nPromotion of nutrient management practices.\n**(4)**\nLimiting or eliminating runoff or leaching of soil or nutrients such as phosphorus and nitrogen into groundwater or other water sources.\n**(5)**\nRestoring beneficial bioactivity or healthy nutrients to the soil.\n**(6)**\nAiding in carbon sequestration, nutrient use efficiency, and other climate-related benefits.\n**(7)**\nSupporting innovative approaches to improving agricultural sustainability, including the adoption of performance-based outcome standards and criteria.\n##### (b) Report\nNot later than 2 years after the date on which funds are first made available to conduct the study under subsection (a), the Secretary shall make publicly available, and submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate, a report that describes the results of the study.",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1907",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Plant Biostimulant Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2025-06-27T13:24:32Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3783ih.xml"
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
      "title": "Plant Biostimulant Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Plant Biostimulant Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Insecticide, Fungicide, and Rodenticide Act to provide for a consistent definition for plant biostimulants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T05:48:24Z"
    }
  ]
}
```
