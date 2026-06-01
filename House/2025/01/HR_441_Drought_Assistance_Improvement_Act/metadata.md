# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/441?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/441
- Title: Drought Assistance Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 441
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-03-06T09:06:37Z
- Update date including text: 2025-03-06T09:06:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- 2025-02-14 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- 2025-02-14 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/441",
    "number": "441",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000595",
        "district": "5",
        "firstName": "Julia",
        "fullName": "Rep. Letlow, Julia [R-LA-5]",
        "lastName": "Letlow",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Drought Assistance Improvement Act",
    "type": "HR",
    "updateDate": "2025-03-06T09:06:37Z",
    "updateDateIncludingText": "2025-03-06T09:06:37Z"
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
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:04:57Z",
                "name": "Referred to"
              }
            },
            "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
            "systemCode": "hsag16"
          },
          {
            "activities": {
              "item": {
                "date": "2025-02-14T18:04:57Z",
                "name": "Referred to"
              }
            },
            "name": "Livestock, Dairy, and Poultry Subcommittee",
            "systemCode": "hsag29"
          }
        ]
      },
      "systemCode": "hsag00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr441ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 441\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Letlow introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo improve drought related disaster assistance programs of the Department of Agriculture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drought Assistance Improvement Act .\n#### 2. Livestock forage disaster program\nSection 1501(c)(3)(D)(ii)(I) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(c)(3)(D)(ii)(I) ) is amended\u2014\n**(1)**\nby striking at least 8 consecutive and inserting the following:\nnot less than\u2014 (aa) 4 consecutive weeks during the normal grazing period for the county, as determined by the Secretary, shall be eligible to receive assistance under this paragraph in an amount equal to 1 monthly payment using the monthly payment rate determined under subparagraph (B); or (bb) 8 consecutive ; and\n**(2)**\nin item (bb) (as so designated), by striking 1 monthly payment and inserting 2 monthly payments .\n#### 3. Emergency assistance for livestock, honey bees, and farm-raised fish program\n##### (a) Documentation standards\nSection 1501(d) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(d) ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting drought, after adverse weather, ;\n**(2)**\nin paragraph (2), by inserting adverse weather or drought, after disease, ; and\n**(3)**\nby adding at the end the following:\n(5) Documentation standards For purposes of this subsection, the Secretary, in consultation with eligible producers of farm-raised fish, shall establish a documentation standard for each of the following: (A) Collecting data. (B) Production of crawfish, as related to reductions in harvest. (C) Defining loss conditions due to drought. .\n##### (b) Reduced crawfish harvest eligibility\nSubsection 1501(d)(2) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(d)(2) ) is further amended by inserting and loss of crawfish harvest due to adverse weather or drought after cattle tick fever .",
      "versionDate": "2025-01-15",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-19T16:50:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr441",
          "measure-number": "441",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr441v00",
            "update-date": "2025-02-20"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Drought Assistance Improvement Act</strong></p><p>This bill modifies access to two Farm Service Agency (FSA) administered programs: the Livestock Forage Disaster Program (LFP) and the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP).</p><p>The bill modifies the LFP to allow for one monthly payment when a county has four consecutive weeks of a D2 rating (severe drought) and two payments for eight consecutive weeks of D2. Currently, one payment is available for eight consecutive weeks of D2. As background, LFP makes payments to eligible livestock producers who have suffered grazing losses on drought-affected pastureland, including cropland planted specifically for grazing.</p><p>The bill also expands coverage under ELAP for losses caused by adverse weather or drought. The bill includes under ELAP the loss of a crawfish harvest due to adverse weather or drought. As background, ELAP provides payments to producers of livestock, honey bees, and farm-raised fish as compensation for losses due to disease, adverse weather, feed or water shortages, or other conditions that are not covered under other programs.</p><p>The FSA must\u00a0establish ELAP documentation standards for (1) collecting data, (2) the production of crawfish,\u00a0and (3) defining loss conditions due to drought.</p>"
        },
        "title": "Drought Assistance Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr441.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Drought Assistance Improvement Act</strong></p><p>This bill modifies access to two Farm Service Agency (FSA) administered programs: the Livestock Forage Disaster Program (LFP) and the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP).</p><p>The bill modifies the LFP to allow for one monthly payment when a county has four consecutive weeks of a D2 rating (severe drought) and two payments for eight consecutive weeks of D2. Currently, one payment is available for eight consecutive weeks of D2. As background, LFP makes payments to eligible livestock producers who have suffered grazing losses on drought-affected pastureland, including cropland planted specifically for grazing.</p><p>The bill also expands coverage under ELAP for losses caused by adverse weather or drought. The bill includes under ELAP the loss of a crawfish harvest due to adverse weather or drought. As background, ELAP provides payments to producers of livestock, honey bees, and farm-raised fish as compensation for losses due to disease, adverse weather, feed or water shortages, or other conditions that are not covered under other programs.</p><p>The FSA must\u00a0establish ELAP documentation standards for (1) collecting data, (2) the production of crawfish,\u00a0and (3) defining loss conditions due to drought.</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr441"
    },
    "title": "Drought Assistance Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Drought Assistance Improvement Act</strong></p><p>This bill modifies access to two Farm Service Agency (FSA) administered programs: the Livestock Forage Disaster Program (LFP) and the Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program (ELAP).</p><p>The bill modifies the LFP to allow for one monthly payment when a county has four consecutive weeks of a D2 rating (severe drought) and two payments for eight consecutive weeks of D2. Currently, one payment is available for eight consecutive weeks of D2. As background, LFP makes payments to eligible livestock producers who have suffered grazing losses on drought-affected pastureland, including cropland planted specifically for grazing.</p><p>The bill also expands coverage under ELAP for losses caused by adverse weather or drought. The bill includes under ELAP the loss of a crawfish harvest due to adverse weather or drought. As background, ELAP provides payments to producers of livestock, honey bees, and farm-raised fish as compensation for losses due to disease, adverse weather, feed or water shortages, or other conditions that are not covered under other programs.</p><p>The FSA must\u00a0establish ELAP documentation standards for (1) collecting data, (2) the production of crawfish,\u00a0and (3) defining loss conditions due to drought.</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr441"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr441ih.xml"
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
      "title": "Drought Assistance Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Drought Assistance Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve drought related disaster assistance programs of the Department of Agriculture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:39Z"
    }
  ]
}
```
