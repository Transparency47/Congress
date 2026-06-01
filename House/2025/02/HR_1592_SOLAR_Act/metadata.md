# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1592?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1592
- Title: SOLAR Act
- Congress: 119
- Bill type: HR
- Bill number: 1592
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-04-14T21:46:19Z
- Update date including text: 2026-04-14T21:46:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1592",
    "number": "1592",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "SOLAR Act",
    "type": "HR",
    "updateDate": "2026-04-14T21:46:19Z",
    "updateDateIncludingText": "2026-04-14T21:46:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:45:11Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
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
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MN"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "IN"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1592ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1592\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Bost (for himself, Mr. Austin Scott of Georgia , Mr. Finstad , and Mr. Taylor ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo limit USDA funding for ground-mounted solar energy systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Our Lands and Resources Act or the SOLAR Act .\n#### 2. Limitation on USDA funding for ground-mounted solar energy systems\n##### (a) Definitions\n**(1) Conversion**\nThe term conversion means, with respect to covered farmland, any activity that results in the covered farmland failing to meet the requirements of a State (defined in section 343 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991 )) for agricultural production, activity, or use.\n**(2) Covered farmland**\nThe term covered farmland means farmland, as defined in section 1540(c)(1) of the Farmland Protection Policy Act ( 7 U.S.C. 4201(c)(1) ).\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) In general\nThe Secretary may not provide financial assistance for a project that would result in the conversion of covered farmland for solar energy production.\n##### (c) Exception\nSubsection (b) shall not apply to a project if the project\u2014\n**(1)**\nresults in the conversion of less than 5 acres of covered farmland;\n**(2)**\nresults in the conversion of less than 50 acres of covered farmland, and the majority of the energy produced by the project is for on-farm use; or\n**(3)**\nhas received a resolution of approval or support, or other similar instrument from each county and municipality in which the project is sited.\n##### (d) Covered farmland protection\n**(1) Farmland conservation plan required**\nA person who has applied to the Secretary for financial assistance for a project referred to in subsection (c)(3) shall\u2014\n**(A)**\ndevelop a farmland conservation plan for the project to\u2014\n**(i)**\nimplement best practices to protect future soil health and productivity, and mitigate soil erosion, compaction, and other effects of solar energy production during construction, operation, and decommissioning; and\n**(ii)**\nremediate and restore the soil health of the farmland to that of the farmland before the solar energy production project construction; and\n**(B)**\nensure sufficient funds, as determined by the Secretary, are provided for the decommissioning of the solar energy production system and the remediation and restoration of covered farmland to carry out the farmland conservation plan described in subparagraph (A).\n**(2) Obligation and disbursement of funds**\nThe Secretary may obligate financial assistance for a project described under paragraph (1), but shall not disburse the financial assistance until the Secretary has determined that the applicant for the financial assistance has complied with paragraph (1).\n**(3) Farmland conservation plan implementation**\nA person referred to in paragraph (1) shall carry out\u2014\n**(A)**\nthe provisions of the plan that are described in paragraph (1)(A)(i), on the receipt by the project of financial assistance from the Secretary and for the duration of solar energy production under the project; and\n**(B)**\nthe provisions of the plan that are described in paragraph (1)(A)(ii), on the cessation of solar energy production under the project.\n**(4) Compliance**\nAny project that fails to comply with paragraph (3) with respect to a project shall repay to the Secretary the full amount of the financial assistance provided by the Secretary to the person for the project.",
      "versionDate": "2025-02-26",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Agricultural conservation and pollution",
            "updateDate": "2025-07-24T14:36:20Z"
          },
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2025-07-24T14:36:02Z"
          },
          {
            "name": "Farmland",
            "updateDate": "2025-07-24T14:36:06Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-07-24T14:36:11Z"
          },
          {
            "name": "Soil pollution",
            "updateDate": "2025-07-24T14:36:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-02T14:33:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1592",
          "measure-number": "1592",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1592v00",
            "update-date": "2025-04-23"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Securing Our Lands and Resources Act or the SOLAR Act</strong></p><p>This bill prohibits the Department of Agriculture from providing financial assistance for certain projects that would result in the conversion of covered farmland for solar energy production.</p><p>Under the bill, <em>covered farmland</em> generally refers to prime farmland, unique farmland, and farmland that is of statewide or local importance. <em>Conversion</em> means any activity that results in the covered farmland no longer meeting certain requirements for agricultural production, activity, or use.</p><p>The bill includes an exception for certain smaller projects that\u00a0result in\u00a0the conversion of (1) less than 5 acres of covered farmland, or (2)\u00a0less than 50 acres of covered farmland if the majority of the energy produced by the project is for on-farm use.</p><p>The bill also includes an exception for projects that have the approval or support from the local county and municipality. For these projects, the applicant must (1) develop a farmland conservation plan for the project (e.g., implementing best practices to protect future soil health and productivity), and (2) ensure that sufficient funds are provided for the decommissioning of the solar energy production system and the remediation and restoration of the farmland.</p>"
        },
        "title": "SOLAR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1592.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing Our Lands and Resources Act or the SOLAR Act</strong></p><p>This bill prohibits the Department of Agriculture from providing financial assistance for certain projects that would result in the conversion of covered farmland for solar energy production.</p><p>Under the bill, <em>covered farmland</em> generally refers to prime farmland, unique farmland, and farmland that is of statewide or local importance. <em>Conversion</em> means any activity that results in the covered farmland no longer meeting certain requirements for agricultural production, activity, or use.</p><p>The bill includes an exception for certain smaller projects that\u00a0result in\u00a0the conversion of (1) less than 5 acres of covered farmland, or (2)\u00a0less than 50 acres of covered farmland if the majority of the energy produced by the project is for on-farm use.</p><p>The bill also includes an exception for projects that have the approval or support from the local county and municipality. For these projects, the applicant must (1) develop a farmland conservation plan for the project (e.g., implementing best practices to protect future soil health and productivity), and (2) ensure that sufficient funds are provided for the decommissioning of the solar energy production system and the remediation and restoration of the farmland.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119hr1592"
    },
    "title": "SOLAR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing Our Lands and Resources Act or the SOLAR Act</strong></p><p>This bill prohibits the Department of Agriculture from providing financial assistance for certain projects that would result in the conversion of covered farmland for solar energy production.</p><p>Under the bill, <em>covered farmland</em> generally refers to prime farmland, unique farmland, and farmland that is of statewide or local importance. <em>Conversion</em> means any activity that results in the covered farmland no longer meeting certain requirements for agricultural production, activity, or use.</p><p>The bill includes an exception for certain smaller projects that\u00a0result in\u00a0the conversion of (1) less than 5 acres of covered farmland, or (2)\u00a0less than 50 acres of covered farmland if the majority of the energy produced by the project is for on-farm use.</p><p>The bill also includes an exception for projects that have the approval or support from the local county and municipality. For these projects, the applicant must (1) develop a farmland conservation plan for the project (e.g., implementing best practices to protect future soil health and productivity), and (2) ensure that sufficient funds are provided for the decommissioning of the solar energy production system and the remediation and restoration of the farmland.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119hr1592"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1592ih.xml"
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
      "title": "SOLAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SOLAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Our Lands and Resources Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit USDA funding for ground-mounted solar energy systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:50Z"
    }
  ]
}
```
