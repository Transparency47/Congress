# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3991?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3991
- Title: Research for Healthy Soils Act
- Congress: 119
- Bill type: HR
- Bill number: 3991
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-04-28T08:06:11Z
- Update date including text: 2026-04-28T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3991",
    "number": "3991",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Research for Healthy Soils Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:11Z",
    "updateDateIncludingText": "2026-04-28T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:10:15Z",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-17",
      "state": "PA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3991ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3991\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Perez (for herself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to include as a high-priority research and extension area research on microplastics and per- and polyfluoroalkyl substances on farmland.\n#### 1. Short title\nThis Act may be cited as the Research for Healthy Soils Act .\n#### 2. Microplastics and per- and polyfluoroalkyl substances on farmland\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Microplastics and per- and polyfluoroalkyl substances on farmland Research and extension grants may be made under this section for the purposes of carrying out or enhancing research on the agricultural impacts of microplastics and per- and polyfluoroalkyl substances, including structural firefighting foam, in land-applied biosolids or compost on farmland, including by\u2014 (A) conducting surveys and collecting data on concentration, particle size, and chemical composition of such substances in land-applied biosolids on farmland; (B) the development or analysis of techniques, including wastewater treatment and composting, to filter out or biodegrade such substances from biosolids intended to be used for agricultural purposes; (C) conducting an analysis of the impact on agricultural crops and soil health of such substances in land-applied biosolids on farmland, including the uptake of such substances by various crops or livestock; (D) conducting research to better understand how wastewater processing impacts such substances; (E) conducting research to better understand the fate, residence time, and transport of such substances on farmland; and (F) conducting research on how to remediate soil and water systems contaminated with such substances. .\n#### 3. Reauthorization of high-priority research and extension initiatives\nSection 1672 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925 ) is amended by striking 2023 each place it appears in subsection (e)(5), subsection (f)(5), paragraphs (1)(B), (2)(B), and (3) of subsection (g), and subsection (h) and inserting 2031 .",
      "versionDate": "2025-06-12",
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
        "actionDate": "2026-04-21",
        "text": "Placed on the Union Calendar, Calendar No. 537."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
        "updateDate": "2025-07-11T17:35:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
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
          "measure-id": "id119hr3991",
          "measure-number": "3991",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-12",
          "originChamber": "HOUSE",
          "update-date": "2026-03-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3991v00",
            "update-date": "2026-03-23"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Research for Healthy Soils Act</strong></p><p>This bill includes research on the agricultural impacts of microplastics and PFAS\u00a0in land-applied biosolids or compost on farmland as a Department of Agriculture (USDA) high-priority research and extension area. <em>Microplastic</em><em>\u00a0</em>is a plastic or plastic-coated particle that is less than 5 millimeters in size. Perfluoroalky\u00a0and polyfluoroalkyl substances, commonly referred to as PFAS, are man-made and may have adverse human health effects.</p><p>The bill specifically allows grants for carrying out or enhancing research in this area (e.g., the development or analysis of techniques, including wastewater treatment and composting, to filter out or biodegrade such substances from biosolids intended to be used for agricultural purposes).</p><p>Further, the bill reauthorizes USDA grants to support competitive specialized research and extension activities, including high-priority areas, through FY2031.</p><p>The bill also specifically reauthorizes through\u00a0FY2031</p><ul><li>the Pulse Crop Health Initiative;</li><li>the Comprehensive Food Safety Training Network;</li><li>pollinator protection research and extension grants;</li><li>increased USDA capacity and infrastructure to address and conduct research on colony collapse disorder and other pollinator issues; and</li><li>a USDA-conducted nationwide honey bee pest, pathogen, health, and population status surveillance program.</li></ul>"
        },
        "title": "Research for Healthy Soils Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3991.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Research for Healthy Soils Act</strong></p><p>This bill includes research on the agricultural impacts of microplastics and PFAS\u00a0in land-applied biosolids or compost on farmland as a Department of Agriculture (USDA) high-priority research and extension area. <em>Microplastic</em><em>\u00a0</em>is a plastic or plastic-coated particle that is less than 5 millimeters in size. Perfluoroalky\u00a0and polyfluoroalkyl substances, commonly referred to as PFAS, are man-made and may have adverse human health effects.</p><p>The bill specifically allows grants for carrying out or enhancing research in this area (e.g., the development or analysis of techniques, including wastewater treatment and composting, to filter out or biodegrade such substances from biosolids intended to be used for agricultural purposes).</p><p>Further, the bill reauthorizes USDA grants to support competitive specialized research and extension activities, including high-priority areas, through FY2031.</p><p>The bill also specifically reauthorizes through\u00a0FY2031</p><ul><li>the Pulse Crop Health Initiative;</li><li>the Comprehensive Food Safety Training Network;</li><li>pollinator protection research and extension grants;</li><li>increased USDA capacity and infrastructure to address and conduct research on colony collapse disorder and other pollinator issues; and</li><li>a USDA-conducted nationwide honey bee pest, pathogen, health, and population status surveillance program.</li></ul>",
      "updateDate": "2026-03-23",
      "versionCode": "id119hr3991"
    },
    "title": "Research for Healthy Soils Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Research for Healthy Soils Act</strong></p><p>This bill includes research on the agricultural impacts of microplastics and PFAS\u00a0in land-applied biosolids or compost on farmland as a Department of Agriculture (USDA) high-priority research and extension area. <em>Microplastic</em><em>\u00a0</em>is a plastic or plastic-coated particle that is less than 5 millimeters in size. Perfluoroalky\u00a0and polyfluoroalkyl substances, commonly referred to as PFAS, are man-made and may have adverse human health effects.</p><p>The bill specifically allows grants for carrying out or enhancing research in this area (e.g., the development or analysis of techniques, including wastewater treatment and composting, to filter out or biodegrade such substances from biosolids intended to be used for agricultural purposes).</p><p>Further, the bill reauthorizes USDA grants to support competitive specialized research and extension activities, including high-priority areas, through FY2031.</p><p>The bill also specifically reauthorizes through\u00a0FY2031</p><ul><li>the Pulse Crop Health Initiative;</li><li>the Comprehensive Food Safety Training Network;</li><li>pollinator protection research and extension grants;</li><li>increased USDA capacity and infrastructure to address and conduct research on colony collapse disorder and other pollinator issues; and</li><li>a USDA-conducted nationwide honey bee pest, pathogen, health, and population status surveillance program.</li></ul>",
      "updateDate": "2026-03-23",
      "versionCode": "id119hr3991"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3991ih.xml"
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
      "title": "Research for Healthy Soils Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Research for Healthy Soils Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-24T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Agriculture, Conservation, and Trade Act of 1990 to include as a high-priority research and extension area research on microplastics and per- and polyfluoroalkyl substances on farmland.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T04:18:22Z"
    }
  ]
}
```
