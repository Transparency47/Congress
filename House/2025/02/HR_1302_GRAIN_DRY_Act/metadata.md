# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1302?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1302
- Title: GRAIN DRY Act
- Congress: 119
- Bill type: HR
- Bill number: 1302
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-04-14T14:59:08Z
- Update date including text: 2026-04-14T14:59:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-20 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-20 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1302",
    "number": "1302",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "GRAIN DRY Act",
    "type": "HR",
    "updateDate": "2026-04-14T14:59:08Z",
    "updateDateIncludingText": "2026-04-14T14:59:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-20",
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
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-20T20:38:40Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1302ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1302\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Finstad (for himself and Mr. Costa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Conservation, and Energy Act of 2008 to clarify propane storage as an eligible use for funds provided under the storage facility loan program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act or the GRAIN DRY Act .\n#### 2. Storage facility loans\nSection 1614(a) of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 8789(a) ) is amended\u2014\n**(1)**\nby striking funds for producers and inserting the following:\nfunds for\u2014 (1) producers ; and\n**(2)**\nin paragraph (1) (as so designated), by striking the period at the end and inserting the following:\n; or (2) agricultural producers to construct or upgrade storage facilities for propane that is primarily used for agricultural production (as such term is defined in section 4279.2 of title 7, Code of Federal Regulations (as in effect on the date of the enactment of this paragraph)). .",
      "versionDate": "2025-02-13",
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-21",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1826",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "GRAIN DRY Act",
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
        "updateDate": "2025-05-06T20:49:00Z"
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
          "measure-id": "id119hr1302",
          "measure-number": "1302",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1302v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act or the GRAIN DRY Act</strong></p><p>This bill specifies that funds provided under the Farm Storage Facility Loan Program may be used to construct or upgrade storage facilities for propane that is primarily used for agricultural production.</p><p>This Department of Agriculture loan program provides low-interest financing for agricultural producers to build or upgrade commodity storage facilities. Some agricultural producers use propane to power agricultural operations (e.g., grain dryers, irrigation engines, and barn heating).</p>"
        },
        "title": "GRAIN DRY Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1302.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act or the GRAIN DRY Act</strong></p><p>This bill specifies that funds provided under the Farm Storage Facility Loan Program may be used to construct or upgrade storage facilities for propane that is primarily used for agricultural production.</p><p>This Department of Agriculture loan program provides low-interest financing for agricultural producers to build or upgrade commodity storage facilities. Some agricultural producers use propane to power agricultural operations (e.g., grain dryers, irrigation engines, and barn heating).</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1302"
    },
    "title": "GRAIN DRY Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act or the GRAIN DRY Act</strong></p><p>This bill specifies that funds provided under the Farm Storage Facility Loan Program may be used to construct or upgrade storage facilities for propane that is primarily used for agricultural production.</p><p>This Department of Agriculture loan program provides low-interest financing for agricultural producers to build or upgrade commodity storage facilities. Some agricultural producers use propane to power agricultural operations (e.g., grain dryers, irrigation engines, and barn heating).</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1302"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1302ih.xml"
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
      "title": "GRAIN DRY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRAIN DRY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Growing Rural Agricultural Infrastructure Needs to Deliver Rising Yields Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Conservation, and Energy Act of 2008 to clarify propane storage as an eligible use for funds provided under the storage facility loan program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:22Z"
    }
  ]
}
```
