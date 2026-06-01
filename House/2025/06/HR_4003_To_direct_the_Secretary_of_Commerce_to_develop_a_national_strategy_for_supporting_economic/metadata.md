# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4003?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4003
- Title: Economic Opportunity for Border Communities Act
- Congress: 119
- Bill type: HR
- Bill number: 4003
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-04-14T20:59:02Z
- Update date including text: 2026-04-14T20:59:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-12 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-12 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4003",
    "number": "4003",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Economic Opportunity for Border Communities Act",
    "type": "HR",
    "updateDate": "2026-04-14T20:59:02Z",
    "updateDateIncludingText": "2026-04-14T20:59:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-13",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:08:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T20:53:19Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-12T14:08:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "AZ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4003ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4003\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Vasquez (for himself and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Commerce to develop a national strategy for supporting economic opportunity in border communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Economic Opportunity for Border Communities Act .\n#### 2. National strategy for supporting economic opportunity in border communities\n##### (a) Development of national strategy\nThe Secretary shall develop a national strategy for supporting economic opportunity in border communities.\n##### (b) Goals of national strategy\nThe goals of the national strategy developed under subsection (a) are the following:\n**(1)**\nIncreasing the number of jobs in border communities, with a focus on the following industries:\n**(A)**\nLogistics.\n**(B)**\nInternational trade.\n**(C)**\nManufacturing.\n**(D)**\nTransportation.\n**(E)**\nAgriculture.\n**(2)**\nStrengthening United States competitiveness in manufacturing.\n**(3)**\nReducing the costs of exports and imports.\n**(4)**\nIncreasing the number of opportunities for workforce development, including by providing vocational training for the industries described in paragraph (1).\n##### (c) Content of national strategy\nThe national strategy developed under subsection (a) shall include the following:\n**(1)**\nAssessment of incentives, including tax incentives, for economic development in border communities.\n**(2)**\nRecommendations for statutory or regulatory changes necessary to achieve the goals described in subsection (b).\n**(3)**\nCoordination with the Secretary of Housing and Urban Development and the Secretary of Agriculture to evaluate the role of rural housing, infrastructure, and economic development programs in supporting economic development in border communities.\n**(4)**\nCoordination with the Secretary of Transportation to evaluate the role of highway and railway infrastructure in supporting economic development in border communities.\n##### (d) Report\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall submit to Congress a report on the national strategy developed under subsection (a).\n##### (e) Definitions\nIn this section:\n**(1) Border community**\nThe term border community means a municipality not more than 15 miles from a land port of entry.\n**(2) Secretary**\nThe term Secretary means the Secretary of Commerce.",
      "versionDate": "2025-06-12",
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
        "name": "Commerce",
        "updateDate": "2025-07-07T13:56:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
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
          "measure-id": "id119hr4003",
          "measure-number": "4003",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-12",
          "originChamber": "HOUSE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4003v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Economic Opportunity for Border Communities Act</strong></p><p>This bill requires the Department of Commerce to develop a national strategy for supporting economic opportunity in border communities. The goals of the strategy include increasing the number of jobs in border communities, strengthening U.S. competitiveness in manufacturing, reducing the costs of exports and imports, and increasing opportunities for workforce development.</p><p>Border communities are municipalities located not more than 15 miles from a land port of entry. \u00a0</p>"
        },
        "title": "Economic Opportunity for Border Communities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4003.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Economic Opportunity for Border Communities Act</strong></p><p>This bill requires the Department of Commerce to develop a national strategy for supporting economic opportunity in border communities. The goals of the strategy include increasing the number of jobs in border communities, strengthening U.S. competitiveness in manufacturing, reducing the costs of exports and imports, and increasing opportunities for workforce development.</p><p>Border communities are municipalities located not more than 15 miles from a land port of entry. \u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr4003"
    },
    "title": "Economic Opportunity for Border Communities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Economic Opportunity for Border Communities Act</strong></p><p>This bill requires the Department of Commerce to develop a national strategy for supporting economic opportunity in border communities. The goals of the strategy include increasing the number of jobs in border communities, strengthening U.S. competitiveness in manufacturing, reducing the costs of exports and imports, and increasing opportunities for workforce development.</p><p>Border communities are municipalities located not more than 15 miles from a land port of entry. \u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr4003"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4003ih.xml"
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
      "title": "Economic Opportunity for Border Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Economic Opportunity for Border Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-24T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Commerce to develop a national strategy for supporting economic opportunity in border communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T05:48:23Z"
    }
  ]
}
```
