# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1669?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1669
- Title: CRAWDAD Act
- Congress: 119
- Bill type: S
- Bill number: 1669
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-01-05T15:55:09Z
- Update date including text: 2026-01-05T15:55:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1669",
    "number": "1669",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "CRAWDAD Act",
    "type": "S",
    "updateDate": "2026-01-05T15:55:09Z",
    "updateDateIncludingText": "2026-01-05T15:55:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T22:17:51Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1669is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1669\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Kennedy (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo improve drought-related disaster assistance programs of the Department of Agriculture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Crawfish Recovery Assistance from Weather Disasters And Droughts Act or the CRAWDAD Act .\n#### 2. Emergency assistance for livestock, honey bees, and farm-raised fish program\nSection 1501(d) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(d) ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting drought, after adverse weather, ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby inserting adverse weather, drought, after disease, ; and\n**(B)**\nby inserting and losses of crawfish harvest due to adverse weather or drought after cattle tick fever ; and\n**(3)**\nby adding at the end the following:\n(5) Documentation standards For purposes of this subsection, the Secretary, in consultation with eligible producers of farm-raised fish, shall establish a documentation standard for each of the following: (A) Collecting data. (B) Production of crawfish, as related to reductions in harvest. (C) Defining loss conditions due to drought. .\n#### 3. Livestock forage disaster program\nSection 1501(c)(1)(A)(i) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(c)(1)(A)(i) ) is amended, in the matter preceding subclause (I), by striking means livestock and inserting means livestock, whether weaned or unweaned, .",
      "versionDate": "2025-05-07",
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
        "updateDate": "2025-06-05T13:34:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-07",
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
          "measure-id": "id119s1669",
          "measure-number": "1669",
          "measure-type": "s",
          "orig-publish-date": "2025-05-07",
          "originChamber": "SENATE",
          "update-date": "2026-01-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1669v00",
            "update-date": "2026-01-05"
          },
          "action-date": "2025-05-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Crawfish Recovery Assistance from Weather Disasters And Droughts Act or the CRAWDAD Act</strong></p><p>This bill modifies access to the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP) and the Livestock Forage Disaster Program (LFP).\u00a0The Farm Service Agency (FSA) administers these programs.</p><p>The bill expands coverage under ELAP for losses caused by adverse weather or drought. The bill includes under ELAP the loss of a crawfish harvest due to adverse weather or drought. (This program provides payments to producers of livestock, honey bees, and farm-raised fish as compensation for losses due to disease, adverse weather, feed or water shortages, or other conditions that are not covered under other programs.)</p><p>The FSA must\u00a0establish ELAP documentation standards for (1) collecting data, (2) the production of crawfish,\u00a0and (3) defining loss conditions due to drought.</p><p>The bill also specifies that eligibility under LFP for livestock producers applies to producers with weaned or unweaned livestock.\u00a0Currently, unweaned livestock are not eligible for the program. (LFP makes payments to eligible livestock producers who have suffered grazing losses on drought-affected pastureland, including cropland planted specifically for grazing.)</p>"
        },
        "title": "CRAWDAD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1669.xml",
    "summary": {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Crawfish Recovery Assistance from Weather Disasters And Droughts Act or the CRAWDAD Act</strong></p><p>This bill modifies access to the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP) and the Livestock Forage Disaster Program (LFP).\u00a0The Farm Service Agency (FSA) administers these programs.</p><p>The bill expands coverage under ELAP for losses caused by adverse weather or drought. The bill includes under ELAP the loss of a crawfish harvest due to adverse weather or drought. (This program provides payments to producers of livestock, honey bees, and farm-raised fish as compensation for losses due to disease, adverse weather, feed or water shortages, or other conditions that are not covered under other programs.)</p><p>The FSA must\u00a0establish ELAP documentation standards for (1) collecting data, (2) the production of crawfish,\u00a0and (3) defining loss conditions due to drought.</p><p>The bill also specifies that eligibility under LFP for livestock producers applies to producers with weaned or unweaned livestock.\u00a0Currently, unweaned livestock are not eligible for the program. (LFP makes payments to eligible livestock producers who have suffered grazing losses on drought-affected pastureland, including cropland planted specifically for grazing.)</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119s1669"
    },
    "title": "CRAWDAD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Crawfish Recovery Assistance from Weather Disasters And Droughts Act or the CRAWDAD Act</strong></p><p>This bill modifies access to the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP) and the Livestock Forage Disaster Program (LFP).\u00a0The Farm Service Agency (FSA) administers these programs.</p><p>The bill expands coverage under ELAP for losses caused by adverse weather or drought. The bill includes under ELAP the loss of a crawfish harvest due to adverse weather or drought. (This program provides payments to producers of livestock, honey bees, and farm-raised fish as compensation for losses due to disease, adverse weather, feed or water shortages, or other conditions that are not covered under other programs.)</p><p>The FSA must\u00a0establish ELAP documentation standards for (1) collecting data, (2) the production of crawfish,\u00a0and (3) defining loss conditions due to drought.</p><p>The bill also specifies that eligibility under LFP for livestock producers applies to producers with weaned or unweaned livestock.\u00a0Currently, unweaned livestock are not eligible for the program. (LFP makes payments to eligible livestock producers who have suffered grazing losses on drought-affected pastureland, including cropland planted specifically for grazing.)</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119s1669"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1669is.xml"
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
      "title": "CRAWDAD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CRAWDAD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Crawfish Recovery Assistance from Weather Disasters And Droughts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve drought-related disaster assistance programs of the Department of Agriculture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:41Z"
    }
  ]
}
```
