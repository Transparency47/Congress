# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2839?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2839
- Title: AG2PI Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2839
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-04-14T21:31:33Z
- Update date including text: 2026-04-14T21:31:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2839",
    "number": "2839",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "AG2PI Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T21:31:33Z",
    "updateDateIncludingText": "2026-04-14T21:31:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:04:05Z",
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2839ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2839\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Feenstra (for himself and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to reauthorize the Genome to Phenome Initiative, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Genome to Phenome Initiative Reauthorization Act of 2025 or the AG2PI Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nUnderstanding crop and livestock genomes (genes) and phenomes (traits) has been a significant roadblock in converting what we know about genetics into useful improvements in agriculturally important species.\n**(2)**\nSignificant research is needed to fully characterize phenomes and how these plant and livestock traits relate to genes, disease resilience, and environmental factors.\n**(3)**\nThis information will help farmers and ranchers determine the best combinations of genetics and management practices to improve the resilience, productivity, and profitability of their businesses.\n**(4)**\nReauthorization of the Genome to Phenome Initiative to build on the work of the Agriculture Improvement Act of 2018 ( Public Law 115\u2013334 ) is critical.\n**(5)**\nIn addition, reauthorization will help support a broad network of researchers, including data scientists, engineers, agricultural economists, and social scientists, and will help develop the most promising of the new concepts generated via the seed grant program into full-fledged research projects.\n**(6)**\nThese efforts will ultimately promote efficient and sustainable agricultural production systems under current as well as future climactic conditions.\n#### 3. Reauthorization of Genome to Phenome Initiative\nSection 1671(g) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5924(g) ) is amended by striking 2023 and inserting 2030 .",
      "versionDate": "2025-04-10",
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
        "actionDate": "2026-03-05",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 17."
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
        "updateDate": "2025-05-07T13:29:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2839",
          "measure-number": "2839",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2025-08-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2839v00",
            "update-date": "2025-08-26"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Genome to Phenome Initiative Reauthorization Act of 2025 or the AG2PI Act of 2025</strong></p><p>This bill reauthorizes the Agricultural Genome to Phenome Initiative (AG2PI) of the National Institute of Food and Agriculture through FY2030. The AG2PI competitive grant program seeks to (1) expand knowledge concerning genomes and phenomes of crops and animals that are of importance to the U.S. agriculture sector, and (2) support and coordinate research.</p>"
        },
        "title": "AG2PI Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2839.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Genome to Phenome Initiative Reauthorization Act of 2025 or the AG2PI Act of 2025</strong></p><p>This bill reauthorizes the Agricultural Genome to Phenome Initiative (AG2PI) of the National Institute of Food and Agriculture through FY2030. The AG2PI competitive grant program seeks to (1) expand knowledge concerning genomes and phenomes of crops and animals that are of importance to the U.S. agriculture sector, and (2) support and coordinate research.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119hr2839"
    },
    "title": "AG2PI Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Genome to Phenome Initiative Reauthorization Act of 2025 or the AG2PI Act of 2025</strong></p><p>This bill reauthorizes the Agricultural Genome to Phenome Initiative (AG2PI) of the National Institute of Food and Agriculture through FY2030. The AG2PI competitive grant program seeks to (1) expand knowledge concerning genomes and phenomes of crops and animals that are of importance to the U.S. agriculture sector, and (2) support and coordinate research.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119hr2839"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2839ih.xml"
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
      "title": "AG2PI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AG2PI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Genome to Phenome Initiative Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Agriculture, Conservation, and Trade Act of 1990 to reauthorize the Genome to Phenome Initiative, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:19Z"
    }
  ]
}
```
