# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2084?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2084
- Title: Smoke Exposure Research Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2084
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2025-12-05T22:06:47Z
- Update date including text: 2025-12-05T22:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2084",
    "number": "2084",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Smoke Exposure Research Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:06:47Z",
    "updateDateIncludingText": "2025-12-05T22:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
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
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T13:12:49Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2084ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2084\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Thompson of California (for himself and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Agricultural Research Service to conduct research relating to the exposure of wine grapes to wildfire smoke, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Smoke Exposure Research Act of 2025 .\n#### 2. Wildfire smoke exposure research on wine grapes\n##### (a) Research\n**(1) In general**\nThe Secretary of Agriculture, acting through the Administrator of the Agricultural Research Service, shall\u2014\n**(A)**\nconduct research\u2014\n**(i)**\nto identify the compounds responsible for smoke exposure; and\n**(ii)**\nto establish standard methodologies for sampling and testing smoke-exposed wine grapes and smoke-affected wines, including fast and inexpensive screening methods;\n**(B)**\nestablish a reliable database of background levels of smoke exposure compounds that occur naturally in wine grapes;\n**(C)**\ndevelop risk assessment tools or mitigation methods to reduce or eliminate smoke exposure; and\n**(D)**\nstudy compounds that can act as a barrier between wine grapes and smoke compounds.\n**(2) Coordination**\nThe Secretary of Agriculture, acting through the Administrator of the Agricultural Research Service, shall carry out paragraph (1) in coordination with land-grant colleges and universities (as defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )) located in the States of California, Oregon, and Washington that have conducted research on the effects of smoke exposure on viticulture and enology operations and practices.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $6,500,000 for each of fiscal years 2026 through 2030, to remain available until expended.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S1745)"
      },
      "number": "1042",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Smoke Exposure Research Act",
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
        "updateDate": "2025-05-14T12:43:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2084",
          "measure-number": "2084",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-05-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2084v00",
            "update-date": "2025-05-30"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Smoke Exposure Research Act of 2025</strong></p><p>This bill directs the Agricultural Research Service (ARS) to conduct research relating to smoke exposure and wine grapes. This research must be done in coordination with land-grant colleges and universities that are located in California, Oregon, and Washington and have researched the effects of smoke exposure on viticulture and enology operations and practices.</p><p>Specifically, ARS must</p><ul><li>conduct research to identify the compounds responsible for smoke exposure,</li><li>conduct research to establish standard methodologies for sampling and testing smoke-exposed wine grapes and smoke-affected wines,</li><li>establish a reliable database of background levels of smoke exposure compounds that occur naturally in wine grapes,</li><li>develop risk assessment tools or mitigation methods to reduce or eliminate smoke exposure, and</li><li>study compounds that can act as a barrier between wine grapes and smoke compounds.</li></ul>"
        },
        "title": "Smoke Exposure Research Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2084.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Smoke Exposure Research Act of 2025</strong></p><p>This bill directs the Agricultural Research Service (ARS) to conduct research relating to smoke exposure and wine grapes. This research must be done in coordination with land-grant colleges and universities that are located in California, Oregon, and Washington and have researched the effects of smoke exposure on viticulture and enology operations and practices.</p><p>Specifically, ARS must</p><ul><li>conduct research to identify the compounds responsible for smoke exposure,</li><li>conduct research to establish standard methodologies for sampling and testing smoke-exposed wine grapes and smoke-affected wines,</li><li>establish a reliable database of background levels of smoke exposure compounds that occur naturally in wine grapes,</li><li>develop risk assessment tools or mitigation methods to reduce or eliminate smoke exposure, and</li><li>study compounds that can act as a barrier between wine grapes and smoke compounds.</li></ul>",
      "updateDate": "2025-05-30",
      "versionCode": "id119hr2084"
    },
    "title": "Smoke Exposure Research Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Smoke Exposure Research Act of 2025</strong></p><p>This bill directs the Agricultural Research Service (ARS) to conduct research relating to smoke exposure and wine grapes. This research must be done in coordination with land-grant colleges and universities that are located in California, Oregon, and Washington and have researched the effects of smoke exposure on viticulture and enology operations and practices.</p><p>Specifically, ARS must</p><ul><li>conduct research to identify the compounds responsible for smoke exposure,</li><li>conduct research to establish standard methodologies for sampling and testing smoke-exposed wine grapes and smoke-affected wines,</li><li>establish a reliable database of background levels of smoke exposure compounds that occur naturally in wine grapes,</li><li>develop risk assessment tools or mitigation methods to reduce or eliminate smoke exposure, and</li><li>study compounds that can act as a barrier between wine grapes and smoke compounds.</li></ul>",
      "updateDate": "2025-05-30",
      "versionCode": "id119hr2084"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2084ih.xml"
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
      "title": "Smoke Exposure Research Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Smoke Exposure Research Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Agricultural Research Service to conduct research relating to the exposure of wine grapes to wildfire smoke, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:32Z"
    }
  ]
}
```
