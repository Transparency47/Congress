# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/626?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/626
- Title: Northwest Energy Security Act
- Congress: 119
- Bill type: HR
- Bill number: 626
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-12-05T21:48:22Z
- Update date including text: 2025-12-05T21:48:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/626",
    "number": "626",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "N000189",
        "district": "4",
        "firstName": "Dan",
        "fullName": "Rep. Newhouse, Dan [R-WA-4]",
        "lastName": "Newhouse",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Northwest Energy Security Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:48:22Z",
    "updateDateIncludingText": "2025-12-05T21:48:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-23T15:40:08Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-22T15:03:35Z",
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
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ID"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr626ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 626\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Newhouse (for himself, Mr. Baumgartner , Mr. Fulcher , and Mr. Bentz ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for operations of the Federal Columbia River Power System pursuant to a certain operation plan for a specified period of time, and for other purposes.\n#### 1. Short title\nThe Act may be cited as the Northwest Energy Security Act .\n#### 2. Definitions\nIn this Act:\n**(1) FCRPS**\nThe term FCRPS means those portions of the Federal Columbia River Power System that are the subject of the Supplemental Opinion.\n**(2) Secretaries**\nThe term Secretaries means\u2014\n**(A)**\nthe Secretary of the Interior, acting through the Commissioner of Reclamation;\n**(B)**\nthe Secretary of Energy, acting through the Administrator of the Bonneville Power Administration; and\n**(C)**\nthe Secretary of the Army, acting through the Chief of Engineers.\n**(3) Supplemental Opinion**\nThe term Supplemental Opinion means the document entitled Columbia River System Operations Environmental Impact Statement Record of Decision and dated September 2020.\n#### 3. Operation of FCRPS\nThe Secretaries shall operate the FCRPS in a manner consistent with the reasonable and prudent alternative described in the Supplemental Opinion.\n#### 4. Amendments to supplemental opinion\n##### (a) In general\nNotwithstanding section 3, the Secretaries may amend portions of the Supplemental Opinion and operate the FCRPS in accordance with those amendments if all of the Secretaries determine, in the sole discretion of each Secretary, that\u2014\n**(1)**\nthe amendment is necessary for public safety or transmission and grid reliability; or\n**(2)**\nthe actions, operations, or other requirements that the amendment would remove are no longer warranted.\n##### (b) Restriction on amendments\nThe process described in subsection (a) shall be the only method by which the Secretaries may operate the FCRPS in any way that is not consistent with the reasonable and prudent alternative set forth in the Supplemental Opinion.\n#### 5. Limitation on restricting FCRPS electrical generation; clarification\n##### (a) Restricting FCRPS electrical generation\nNo structural modification, action, study, or engineering plan that restricts electrical generation at any FCRPS hydroelectric dam, or that limits navigation on the Snake River in the State of Washington, Oregon, or Idaho, shall proceed unless such proposal is specifically and expressly authorized by a Federal statute enacted after the date of the enactment of this Act.\n##### (b) Clarification\nNothing in this section affects or interferes with the authority of the Secretaries to conduct operation and maintenance activities or make capital improvements necessary to meet authorized project purposes of FCRPS facilities.",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-01-22",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "182",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Northwest Energy Security Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2025-09-08T19:55:05Z"
          },
          {
            "name": "Dams and canals",
            "updateDate": "2025-09-08T19:54:35Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2025-09-08T19:55:11Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2025-09-08T19:54:58Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2025-09-08T19:54:31Z"
          },
          {
            "name": "Montana",
            "updateDate": "2025-09-08T19:54:53Z"
          },
          {
            "name": "Oregon",
            "updateDate": "2025-09-08T19:54:39Z"
          },
          {
            "name": "Washington State",
            "updateDate": "2025-09-08T19:54:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-05-02T17:43:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr626",
          "measure-number": "626",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-08-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr626v00",
            "update-date": "2025-08-07"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Northwest Energy Security Act</strong></p><p>This bill requires Federal Columbia River Power System (FCRPS) operations to be consistent with the preferred alternative in a\u00a02020 environmental impact statement (EIS)\u00a0decision that focuses on the operations, maintenance, and configuration of dams in the system rather than wild fish restoration. The system includes dams in the Columbia and Snake rivers in Oregon, Washington, Montana, and Idaho.</p><p>Specifically, the Bureau of Reclamation, the Bonneville Power Administration, and the U.S. Army Corps of Engineers must operate the FCRPS consistent with the <em>Columbia River System Operations Environmental Impact Statement Record of Decision</em> dated September 2020. Thus, Reclamation,\u00a0the Bonneville Power Administration, and the Army Corps must follow the EIS rather than the 2023 Resilient Columbia Basin Initiative\u2014and a\u00a0supplemental EIS proposed in 2024\u2014that focus on wild fish restoration in the Columbia Basin.</p><p>The EIS decision may be amended if each agency determines that (1) changes are necessary for public safety or electrical grid reliability, or (2) certain requirements in the decision are no longer necessary.</p><p>Further, the bill requires statutory authorization for any structural modification, action, study, or engineering plan that (1) restricts FCRPS hydroelectric dam generation; or (2) limits navigation on the Snake River in Washington, Oregon, or Idaho.</p>"
        },
        "title": "Northwest Energy Security Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr626.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Northwest Energy Security Act</strong></p><p>This bill requires Federal Columbia River Power System (FCRPS) operations to be consistent with the preferred alternative in a\u00a02020 environmental impact statement (EIS)\u00a0decision that focuses on the operations, maintenance, and configuration of dams in the system rather than wild fish restoration. The system includes dams in the Columbia and Snake rivers in Oregon, Washington, Montana, and Idaho.</p><p>Specifically, the Bureau of Reclamation, the Bonneville Power Administration, and the U.S. Army Corps of Engineers must operate the FCRPS consistent with the <em>Columbia River System Operations Environmental Impact Statement Record of Decision</em> dated September 2020. Thus, Reclamation,\u00a0the Bonneville Power Administration, and the Army Corps must follow the EIS rather than the 2023 Resilient Columbia Basin Initiative\u2014and a\u00a0supplemental EIS proposed in 2024\u2014that focus on wild fish restoration in the Columbia Basin.</p><p>The EIS decision may be amended if each agency determines that (1) changes are necessary for public safety or electrical grid reliability, or (2) certain requirements in the decision are no longer necessary.</p><p>Further, the bill requires statutory authorization for any structural modification, action, study, or engineering plan that (1) restricts FCRPS hydroelectric dam generation; or (2) limits navigation on the Snake River in Washington, Oregon, or Idaho.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119hr626"
    },
    "title": "Northwest Energy Security Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Northwest Energy Security Act</strong></p><p>This bill requires Federal Columbia River Power System (FCRPS) operations to be consistent with the preferred alternative in a\u00a02020 environmental impact statement (EIS)\u00a0decision that focuses on the operations, maintenance, and configuration of dams in the system rather than wild fish restoration. The system includes dams in the Columbia and Snake rivers in Oregon, Washington, Montana, and Idaho.</p><p>Specifically, the Bureau of Reclamation, the Bonneville Power Administration, and the U.S. Army Corps of Engineers must operate the FCRPS consistent with the <em>Columbia River System Operations Environmental Impact Statement Record of Decision</em> dated September 2020. Thus, Reclamation,\u00a0the Bonneville Power Administration, and the Army Corps must follow the EIS rather than the 2023 Resilient Columbia Basin Initiative\u2014and a\u00a0supplemental EIS proposed in 2024\u2014that focus on wild fish restoration in the Columbia Basin.</p><p>The EIS decision may be amended if each agency determines that (1) changes are necessary for public safety or electrical grid reliability, or (2) certain requirements in the decision are no longer necessary.</p><p>Further, the bill requires statutory authorization for any structural modification, action, study, or engineering plan that (1) restricts FCRPS hydroelectric dam generation; or (2) limits navigation on the Snake River in Washington, Oregon, or Idaho.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119hr626"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr626ih.xml"
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
      "title": "Northwest Energy Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Northwest Energy Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for operations of the Federal Columbia River Power System pursuant to a certain operation plan for a specified period of time, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:18:22Z"
    }
  ]
}
```
