# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2500
- Title: Research for Healthy Soils Act
- Congress: 119
- Bill type: S
- Bill number: 2500
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2025-09-16T13:19:53Z
- Update date including text: 2025-09-16T13:19:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2500",
    "number": "2500",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Research for Healthy Soils Act",
    "type": "S",
    "updateDate": "2025-09-16T13:19:53Z",
    "updateDateIncludingText": "2025-09-16T13:19:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T16:08:51Z",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2500is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2500\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Merkley (for himself, Mr. Booker , Mr. Whitehouse , Mr. Wyden , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to include as a high-priority research and extension area research on microplastics in land-applied biosolids on farmland, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Research for Healthy Soils Act .\n#### 2. Microplastics in land-applied biosolids on farmland\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Microplastics in land-applied biosolids on farmland Research and extension grants may be made under this section for the purposes of carrying out or enhancing research on the agricultural impacts of plastic or plastic-coated particles that are less than 5 millimeters in any dimension (referred to in this paragraph as microplastics ) in land-applied biosolids on farmland, including\u2014 (A) by conducting surveys and collecting data on microplastic concentration, particle size, and chemical composition in land-applied biosolids on farmland; (B) through the development or analysis of wastewater treatment techniques to filter out or biodegrade microplastics from biosolids intended to be used for agricultural purposes; (C) by conducting an analysis of the impact on agricultural crops and soil health of microplastics in land-applied biosolids on farmland; (D) by conducting research to better understand how wastewater processing impacts microplastics; and (E) by conducting research to better understand the fate, residence time, and transport of microplastics on farmland. .\n#### 3. Reauthorization of high-priority research and extension initiatives\nSection 1672 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925 ) is amended by striking 2023 each place it appears in subsection (e)(5), subsection (f)(5), paragraphs (1)(B), (2)(B), and (3) of subsection (g), and subsection (h) and inserting 2031 .",
      "versionDate": "2025-07-29",
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
        "updateDate": "2025-09-15T17:16:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-29",
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
          "measure-id": "id119s2500",
          "measure-number": "2500",
          "measure-type": "s",
          "orig-publish-date": "2025-07-29",
          "originChamber": "SENATE",
          "update-date": "2025-09-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2500v00",
            "update-date": "2025-09-16"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Research for Healthy Soils Act</strong></p><p>This bill includes research on the agricultural impacts of microplastics in land-applied biosolids on farmland as a Department of Agriculture (USDA) high-priority research and extension area and reauthorizes other research and extension activities.\u00a0<em>Microplastic</em> is a plastic or plastic-coated particle that is less than 5 millimeters in size.</p><p>The bill specifically allows grants for carrying out or enhancing research on microplastics (e.g., through the development or analysis of wastewater treatment techniques to filter out or biodegrade microplastics from biosolids intended to be used for agricultural purposes).</p><p>Further, the bill reauthorizes USDA grants to support competitive specialized research and extension activities, including high-priority areas, through FY2031. The bill also specifically reauthorizes through FY2031</p><ul><li>the Pulse Crop Health Initiative;</li><li>the Comprehensive Food Safety Training Network;</li><li>pollinator protection research and extension grants;</li><li>increased USDA capacity and infrastructure to address and conduct research on colony collapse disorder and other pollinator issues; and</li><li>a USDA-conducted nationwide honey bee pest, pathogen, health, and population status surveillance program.</li></ul>"
        },
        "title": "Research for Healthy Soils Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2500.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Research for Healthy Soils Act</strong></p><p>This bill includes research on the agricultural impacts of microplastics in land-applied biosolids on farmland as a Department of Agriculture (USDA) high-priority research and extension area and reauthorizes other research and extension activities.\u00a0<em>Microplastic</em> is a plastic or plastic-coated particle that is less than 5 millimeters in size.</p><p>The bill specifically allows grants for carrying out or enhancing research on microplastics (e.g., through the development or analysis of wastewater treatment techniques to filter out or biodegrade microplastics from biosolids intended to be used for agricultural purposes).</p><p>Further, the bill reauthorizes USDA grants to support competitive specialized research and extension activities, including high-priority areas, through FY2031. The bill also specifically reauthorizes through FY2031</p><ul><li>the Pulse Crop Health Initiative;</li><li>the Comprehensive Food Safety Training Network;</li><li>pollinator protection research and extension grants;</li><li>increased USDA capacity and infrastructure to address and conduct research on colony collapse disorder and other pollinator issues; and</li><li>a USDA-conducted nationwide honey bee pest, pathogen, health, and population status surveillance program.</li></ul>",
      "updateDate": "2025-09-16",
      "versionCode": "id119s2500"
    },
    "title": "Research for Healthy Soils Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Research for Healthy Soils Act</strong></p><p>This bill includes research on the agricultural impacts of microplastics in land-applied biosolids on farmland as a Department of Agriculture (USDA) high-priority research and extension area and reauthorizes other research and extension activities.\u00a0<em>Microplastic</em> is a plastic or plastic-coated particle that is less than 5 millimeters in size.</p><p>The bill specifically allows grants for carrying out or enhancing research on microplastics (e.g., through the development or analysis of wastewater treatment techniques to filter out or biodegrade microplastics from biosolids intended to be used for agricultural purposes).</p><p>Further, the bill reauthorizes USDA grants to support competitive specialized research and extension activities, including high-priority areas, through FY2031. The bill also specifically reauthorizes through FY2031</p><ul><li>the Pulse Crop Health Initiative;</li><li>the Comprehensive Food Safety Training Network;</li><li>pollinator protection research and extension grants;</li><li>increased USDA capacity and infrastructure to address and conduct research on colony collapse disorder and other pollinator issues; and</li><li>a USDA-conducted nationwide honey bee pest, pathogen, health, and population status surveillance program.</li></ul>",
      "updateDate": "2025-09-16",
      "versionCode": "id119s2500"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2500is.xml"
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
      "title": "Research for Healthy Soils Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Research for Healthy Soils Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food, Agriculture, Conservation, and Trade Act of 1990 to include as a high-priority research and extension area research on microplastics in land-applied biosolids on farmland, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:31Z"
    }
  ]
}
```
