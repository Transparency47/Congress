# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/598?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/598
- Title: FIR Act
- Congress: 119
- Bill type: HR
- Bill number: 598
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2026-02-17T21:46:32Z
- Update date including text: 2026-02-17T21:46:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-21 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-21 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/598",
    "number": "598",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "Z000018",
        "district": "1",
        "firstName": "Ryan",
        "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
        "lastName": "Zinke",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "FIR Act",
    "type": "HR",
    "updateDate": "2026-02-17T21:46:32Z",
    "updateDateIncludingText": "2026-02-17T21:46:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-28",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:12:32Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-21T17:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WA"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr598ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 598\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Mr. Zinke (for himself and Mr. Newhouse ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Forest and Rangeland Renewable Resources Planning Act of 1974 and the Federal Land Policy and Management Act of 1976 to provide that the Secretary of Agriculture and the Secretary of the Interior are not required to reinitiate consultation on a land management plan or land use plan under certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Forest Information Reform Act or as the FIR Act .\n#### 2. No additional consultation required\n##### (a) Forest Service plans\nSection 6(d)(2) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1604(d)(2) ) is amended to read as follows:\n(2) No additional consultation required under certain circumstances Notwithstanding any other provision of law, the Secretary shall not be required to reinitiate consultation under section 7(a)(2) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(a)(2) ) or section 402.16 of title 50, Code of Federal Regulations (or a successor regulation), on a land management plan approved, amended, or revised under this section when\u2014 (A) a new species is listed or critical habitat is designated under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ); or (B) new information reveals effects of the land management plan that may affect a species listed or critical habitat designated under that Act in a manner or to an extent not previously considered. .\n##### (b) Bureau of Land Management plans\nSection 202 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1712 ) is amended by adding at the end the following:\n(g) No additional consultation required under certain circumstances Notwithstanding any other provision of law, the Secretary shall not be required to reinitiate consultation under section 7(a)(2) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(a)(2) ) or section 402.16 of title 50, Code of Federal Regulations (or a successor regulation), on a land use plan approved, amended, or revised under this section when\u2014 (1) a new species is listed or critical habitat is designated under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ); or (2) new information reveals effects of the land use plan that may affect a species listed or critical habitat designated under that Act in a manner or to an extent not previously considered. .",
      "versionDate": "2025-01-21",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
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
        "actionDate": "2025-03-06",
        "text": "Committee on Agriculture, Nutrition, and Forestry Subcommittee on Conservation, Forestry, Natural Resources, and Biotechnology. Hearings held. With printed Hearing: S.Hrg. 119-27."
      },
      "number": "471",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fix Our Forests Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-04",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "168",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TORCH Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Endangered and threatened species",
            "updateDate": "2025-03-12T14:06:29Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-03-12T14:06:29Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-03-12T14:06:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-27T19:29:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr598",
          "measure-number": "598",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr598v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Forest Information Reform Act or the FIR Act</strong></p><p>This bill\u00a0specifies that neither the Forest Service nor the Bureau of Land Management\u00a0are\u00a0required to reinitiate consultation on a land management plan when a new species is listed as threatened or endangered, critical habitat is designated, or new information\u00a0reveals effects of the plan may affect a listed species or critical habitat in a manner or to an extent not previously considered.</p>"
        },
        "title": "FIR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr598.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Forest Information Reform Act or the FIR Act</strong></p><p>This bill\u00a0specifies that neither the Forest Service nor the Bureau of Land Management\u00a0are\u00a0required to reinitiate consultation on a land management plan when a new species is listed as threatened or endangered, critical habitat is designated, or new information\u00a0reveals effects of the plan may affect a listed species or critical habitat in a manner or to an extent not previously considered.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr598"
    },
    "title": "FIR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Forest Information Reform Act or the FIR Act</strong></p><p>This bill\u00a0specifies that neither the Forest Service nor the Bureau of Land Management\u00a0are\u00a0required to reinitiate consultation on a land management plan when a new species is listed as threatened or endangered, critical habitat is designated, or new information\u00a0reveals effects of the plan may affect a listed species or critical habitat in a manner or to an extent not previously considered.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr598"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr598ih.xml"
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
      "title": "FIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Forest Information Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Forest and Rangeland Renewable Resources Planning Act of 1974 and the Federal Land Policy and Management Act of 1976 to provide that the Secretary of Agriculture and the Secretary of the Interior are not required to reinitiate consultation on a land management plan or land use plan under certain circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T04:18:28Z"
    }
  ]
}
```
