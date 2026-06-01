# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1826?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1826
- Title: GRAIN DRY Act
- Congress: 119
- Bill type: S
- Bill number: 1826
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2025-12-05T21:57:44Z
- Update date including text: 2025-12-05T21:57:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1826",
    "number": "1826",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "GRAIN DRY Act",
    "type": "S",
    "updateDate": "2025-12-05T21:57:44Z",
    "updateDateIncludingText": "2025-12-05T21:57:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T15:23:56Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MN"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1826is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1826\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Ms. Ernst (for herself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food, Conservation, and Energy Act of 2008 to clarify propane storage as an eligible use for funds provided under the storage facility loan program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act or the GRAIN DRY Act .\n#### 2. Storage facility loans\nSection 1614(a) of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 8789(a) ) is amended\u2014\n**(1)**\nby striking funds for producers and inserting the following:\nfunds for\u2014 (1) producers ; and\n**(2)**\nin paragraph (1) (as so designated), by striking the period at the end and inserting the following:\n; or (2) agricultural producers to construct or upgrade storage facilities for propane that is primarily used for agricultural production (as such term is defined in section 4279.2 of title 7, Code of Federal Regulations (as in effect on the date of the enactment of this paragraph)). .",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-03-20",
        "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit."
      },
      "number": "1302",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "GRAIN DRY Act",
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
        "updateDate": "2025-06-23T17:57:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
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
          "measure-id": "id119s1826",
          "measure-number": "1826",
          "measure-type": "s",
          "orig-publish-date": "2025-05-21",
          "originChamber": "SENATE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1826v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act or the GRAIN DRY Act</strong></p><p>This bill specifies that funds provided under the Farm Storage Facility Loan Program may be used to construct or upgrade storage facilities for propane that is primarily used for agricultural production.</p><p>This Department of Agriculture loan program provides low-interest financing for agricultural producers to build or upgrade commodity storage facilities. Some agricultural producers use propane to power agricultural operations (e.g., grain dryers, irrigation engines, and barn heating).</p>"
        },
        "title": "GRAIN DRY Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1826.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act or the GRAIN DRY Act</strong></p><p>This bill specifies that funds provided under the Farm Storage Facility Loan Program may be used to construct or upgrade storage facilities for propane that is primarily used for agricultural production.</p><p>This Department of Agriculture loan program provides low-interest financing for agricultural producers to build or upgrade commodity storage facilities. Some agricultural producers use propane to power agricultural operations (e.g., grain dryers, irrigation engines, and barn heating).</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119s1826"
    },
    "title": "GRAIN DRY Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act or the GRAIN DRY Act</strong></p><p>This bill specifies that funds provided under the Farm Storage Facility Loan Program may be used to construct or upgrade storage facilities for propane that is primarily used for agricultural production.</p><p>This Department of Agriculture loan program provides low-interest financing for agricultural producers to build or upgrade commodity storage facilities. Some agricultural producers use propane to power agricultural operations (e.g., grain dryers, irrigation engines, and barn heating).</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119s1826"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1826is.xml"
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
      "title": "GRAIN DRY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GRAIN DRY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food, Conservation, and Energy Act of 2008 to clarify propane storage as an eligible use for funds provided under the storage facility loan program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:28Z"
    }
  ]
}
```
