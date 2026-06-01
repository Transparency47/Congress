# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/773?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/773
- Title: To amend the Food Security Act of 1985 to repeal certain provisions relating to the acceptance and use of contributions for public-private partnerships, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 773
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-02-18T20:24:16Z
- Update date including text: 2026-02-18T20:24:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/773",
    "number": "773",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "To amend the Food Security Act of 1985 to repeal certain provisions relating to the acceptance and use of contributions for public-private partnerships, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-18T20:24:16Z",
    "updateDateIncludingText": "2026-02-18T20:24:16Z"
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
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:15:11Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr773ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 773\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to repeal certain provisions relating to the acceptance and use of contributions for public-private partnerships, and for other purposes.\n#### 1. Acceptance and use of contributions\nSection 1241(f) of the Food Security Act of 1985 ( 16 U.S.C. 3841(f) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking for public-Private partnerships ;\n**(2)**\nby amending paragraph (1) to read as follows:\n(1) Authority to establish contribution accounts Subject to paragraph (2), the Secretary may establish a sub-account for each conservation program administered by the Secretary under subtitle D to accept contributions of non-Federal funds to support the purposes of the program. ;\n**(3)**\nin paragraph (2), by striking a covered program shall be deposited into the account and inserting a conservation program administered by the Secretary under subtitle D shall be deposited into the sub-account ; and\n**(4)**\nby striking paragraphs (3) through (10).",
      "versionDate": "2025-01-28",
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
        "updateDate": "2025-02-26T21:25:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr773",
          "measure-number": "773",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2026-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr773v00",
            "update-date": "2026-02-18"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill repeals provisions that allow the Natural Resources Conservation Service (NRCS) to accept and use contributions for public-private partnerships.\u00a0</p><p>Specifically, the bill repeals the public-private partnerships allowed under an act commonly known as\u00a0the Sponsoring USDA\u00a0Sustainability Targets in Agriculture to Incentivize Natural Solutions Act (the SUSTAINS Act). In addition, the bill allows NRCS\u00a0to continue to accept nonfederal contributions of funds to certain programs\u00a0(e.g.,\u00a0the Environmental Quality Incentives Program and the Conservation Stewardship Program)\u00a0in order to support the purposes of the programs.</p><p>As background,\u00a0Congress enacted provisions of the SUSTAINS Act as part of the Consolidated Appropriations Act,\u00a02023. Under the SUSTAINS Act\u00a0provisions,\u00a0the NRCS may accept contributions of nonfederal funds to support a broad range of conservation programs for the purposes of addressing issues related to climate change, carbon sequestration, wildlife habitat improvement, and protection of drinking water sources. NRCS may match these contributions. In addition, those contributing funds may designate the funds for use in a specific program or geographic area.</p>"
        },
        "title": "To amend the Food Security Act of 1985 to repeal certain provisions relating to the acceptance and use of contributions for public-private partnerships, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr773.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill repeals provisions that allow the Natural Resources Conservation Service (NRCS) to accept and use contributions for public-private partnerships.\u00a0</p><p>Specifically, the bill repeals the public-private partnerships allowed under an act commonly known as\u00a0the Sponsoring USDA\u00a0Sustainability Targets in Agriculture to Incentivize Natural Solutions Act (the SUSTAINS Act). In addition, the bill allows NRCS\u00a0to continue to accept nonfederal contributions of funds to certain programs\u00a0(e.g.,\u00a0the Environmental Quality Incentives Program and the Conservation Stewardship Program)\u00a0in order to support the purposes of the programs.</p><p>As background,\u00a0Congress enacted provisions of the SUSTAINS Act as part of the Consolidated Appropriations Act,\u00a02023. Under the SUSTAINS Act\u00a0provisions,\u00a0the NRCS may accept contributions of nonfederal funds to support a broad range of conservation programs for the purposes of addressing issues related to climate change, carbon sequestration, wildlife habitat improvement, and protection of drinking water sources. NRCS may match these contributions. In addition, those contributing funds may designate the funds for use in a specific program or geographic area.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119hr773"
    },
    "title": "To amend the Food Security Act of 1985 to repeal certain provisions relating to the acceptance and use of contributions for public-private partnerships, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill repeals provisions that allow the Natural Resources Conservation Service (NRCS) to accept and use contributions for public-private partnerships.\u00a0</p><p>Specifically, the bill repeals the public-private partnerships allowed under an act commonly known as\u00a0the Sponsoring USDA\u00a0Sustainability Targets in Agriculture to Incentivize Natural Solutions Act (the SUSTAINS Act). In addition, the bill allows NRCS\u00a0to continue to accept nonfederal contributions of funds to certain programs\u00a0(e.g.,\u00a0the Environmental Quality Incentives Program and the Conservation Stewardship Program)\u00a0in order to support the purposes of the programs.</p><p>As background,\u00a0Congress enacted provisions of the SUSTAINS Act as part of the Consolidated Appropriations Act,\u00a02023. Under the SUSTAINS Act\u00a0provisions,\u00a0the NRCS may accept contributions of nonfederal funds to support a broad range of conservation programs for the purposes of addressing issues related to climate change, carbon sequestration, wildlife habitat improvement, and protection of drinking water sources. NRCS may match these contributions. In addition, those contributing funds may designate the funds for use in a specific program or geographic area.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119hr773"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr773ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to repeal certain provisions relating to the acceptance and use of contributions for public-private partnerships, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:25Z"
    },
    {
      "title": "To amend the Food Security Act of 1985 to repeal certain provisions relating to the acceptance and use of contributions for public-private partnerships, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T09:05:53Z"
    }
  ]
}
```
