# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/774?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/774
- Title: PASTURES Act
- Congress: 119
- Bill type: HR
- Bill number: 774
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-03-12T08:07:41Z
- Update date including text: 2025-03-12T08:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-28 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-28 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-28 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/774",
    "number": "774",
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
    "title": "PASTURES Act",
    "type": "HR",
    "updateDate": "2025-03-12T08:07:41Z",
    "updateDateIncludingText": "2025-03-12T08:07:41Z"
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
      "actionDate": "2025-02-28",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:00:25Z",
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
                "date": "2025-02-28T17:15:26Z",
                "name": "Referred to"
              }
            },
            "name": "Forestry and Horticulture Subcommittee",
            "systemCode": "hsag15"
          },
          {
            "activities": {
              "item": {
                "date": "2025-02-28T17:15:26Z",
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
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-28T16:00:20Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr774ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 774\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo limit the ability of the Secretary of Agriculture and the Secretary of the Interior to penalize an owner of livestock for grazing by such livestock on certain Federal lands on which grazing is permitted on or after the date of enactment of this Act and subsequently prohibited, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Agricultural Spaces Through Effective Ranching Strategies Act or the PASTURES Act .\n#### 2. Limitation on penalties for grazing livestock on certain covered lands\n##### (a) Limitation\nThe Secretary concerned may not impose a penalty on an owner of livestock for grazing by such livestock on covered lands on which a fence for the prevention of such grazing does not exist.\n##### (b) Fence expenses\nThe Secretary concerned shall be responsible for any expense related to the construction or maintenance of any fence constructed or maintained on covered lands for the prevention of grazing by livestock on such covered lands.\n##### (c) Definitions\nIn this section:\n**(1) Covered lands**\nThe term covered lands means National Forest System lands, lands administered by the United States Fish and Wildlife Service, or public lands\u2014\n**(A)**\non which grazing is permitted by grazing permit or lease on or after the date of enactment of this Act and subsequently prohibited; and\n**(B)**\nthat borders private property.\n**(2) Grazing permit or lease**\nThe term grazing permit or lease means\u2014\n**(A)**\na grazing permit as such term is defined in section 222.1 of title 36, Code of Federal Regulations (or successor regulations);\n**(B)**\na cooperative agreement referred to in section 29.2 of title 50, Code of Federal Regulations (or successor regulations) that permits grazing; or\n**(C)**\na grazing permit or lease described in section 4130.2 of title 43, Code of Federal Regulations (or successor regulations).\n**(3) Livestock**\nThe term livestock includes cattle, bison, horses, sheep, and goats.\n**(4) National Forest System**\nThe term National Forest System has the meaning given the term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609 ).\n**(5) Public lands**\nThe term public lands has the meaning given that term in section 103 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1702 ).\n**(6) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Agriculture, with respect to National Forest System lands; and\n**(B)**\nthe Secretary of the Interior, with respect to public lands and lands administered by the United States Fish and Wildlife Service.",
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
        "updateDate": "2025-02-26T21:24:33Z"
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
          "measure-id": "id119hr774",
          "measure-number": "774",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr774v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Agricultural Spaces Through Effective Ranching Strategies Act or the PASTURES Act</strong></p><p>This bill\u00a0prohibits\u00a0the Department of Agriculture (USDA) and the Department of the Interior from imposing penalties on livestock owners for grazing on certain public lands.\u00a0</p><p>Under the bill, covered lands are National Forest System lands, lands administered by the U.S. Fish and Wildlife Service, or public lands (1) on which\u00a0grazing is allowed by a permit or lease on or after the date of the bill's enactment and is then subsequently prohibited, and (2) that border private property.</p><p>Specifically, the departments may not impose a penalty on an owner of livestock (including cattle, bison, horses, sheep, and goats) for grazing on covered lands that do not have a fence to prevent grazing.</p><p>The bill specifies that USDA or Interior, depending on the covered land, is responsible for any expense related to the construction or maintenance of a fence for the prevention of grazing by livestock.</p>"
        },
        "title": "PASTURES Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr774.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Agricultural Spaces Through Effective Ranching Strategies Act or the PASTURES Act</strong></p><p>This bill\u00a0prohibits\u00a0the Department of Agriculture (USDA) and the Department of the Interior from imposing penalties on livestock owners for grazing on certain public lands.\u00a0</p><p>Under the bill, covered lands are National Forest System lands, lands administered by the U.S. Fish and Wildlife Service, or public lands (1) on which\u00a0grazing is allowed by a permit or lease on or after the date of the bill's enactment and is then subsequently prohibited, and (2) that border private property.</p><p>Specifically, the departments may not impose a penalty on an owner of livestock (including cattle, bison, horses, sheep, and goats) for grazing on covered lands that do not have a fence to prevent grazing.</p><p>The bill specifies that USDA or Interior, depending on the covered land, is responsible for any expense related to the construction or maintenance of a fence for the prevention of grazing by livestock.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr774"
    },
    "title": "PASTURES Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Agricultural Spaces Through Effective Ranching Strategies Act or the PASTURES Act</strong></p><p>This bill\u00a0prohibits\u00a0the Department of Agriculture (USDA) and the Department of the Interior from imposing penalties on livestock owners for grazing on certain public lands.\u00a0</p><p>Under the bill, covered lands are National Forest System lands, lands administered by the U.S. Fish and Wildlife Service, or public lands (1) on which\u00a0grazing is allowed by a permit or lease on or after the date of the bill's enactment and is then subsequently prohibited, and (2) that border private property.</p><p>Specifically, the departments may not impose a penalty on an owner of livestock (including cattle, bison, horses, sheep, and goats) for grazing on covered lands that do not have a fence to prevent grazing.</p><p>The bill specifies that USDA or Interior, depending on the covered land, is responsible for any expense related to the construction or maintenance of a fence for the prevention of grazing by livestock.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr774"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr774ih.xml"
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
      "title": "PASTURES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PASTURES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Agricultural Spaces Through Effective Ranching Strategies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the ability of the Secretary of Agriculture and the Secretary of the Interior to penalize an owner of livestock for grazing by such livestock on certain Federal lands on which grazing is permitted on or after the date of enactment of this Act and subsequently prohibited, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:37Z"
    }
  ]
}
```
