# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/182?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/182
- Title: Northwest Energy Security Act
- Congress: 119
- Bill type: S
- Bill number: 182
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2026-04-08T17:54:19Z
- Update date including text: 2026-04-08T17:54:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/182",
    "number": "182",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Northwest Energy Security Act",
    "type": "S",
    "updateDate": "2026-04-08T17:54:19Z",
    "updateDateIncludingText": "2026-04-08T17:54:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T16:36:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MT"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ID"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "WY"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s182is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 182\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Risch (for himself, Mr. Daines , Mr. Sheehy , Mr. Crapo , Ms. Lummis , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo provide for operations of the Federal Columbia River Power System pursuant to a certain operation plan for a specified period of time, and for other purposes.\n#### 1. Short title\nThe Act may be cited as the Northwest Energy Security Act .\n#### 2. Definitions\nIn this Act:\n**(1) FCRPS**\nThe term FCRPS means those portions of the Federal Columbia River Power System that are the subject of the Supplemental Opinion.\n**(2) Secretaries**\nThe term Secretaries means\u2014\n**(A)**\nthe Secretary of the Interior, acting through the Commissioner of Reclamation;\n**(B)**\nthe Secretary of Energy, acting through the Administrator of the Bonneville Power Administration; and\n**(C)**\nthe Secretary of the Army, acting through the Chief of Engineers.\n**(3) Supplemental Opinion**\nThe term Supplemental Opinion means the document entitled Columbia River System Operations Environmental Impact Statement Record of Decision and dated September 2020.\n#### 3. Operation of FCRPS\nThe Secretaries shall operate the FCRPS in a manner consistent with the reasonable and prudent alternative described in the Supplemental Opinion.\n#### 4. Amendments to supplemental opinion\n##### (a) In general\nNotwithstanding section 3, the Secretaries may amend portions of the Supplemental Opinion and operate the FCRPS in accordance with those amendments if all of the Secretaries determine, in the sole discretion of each Secretary, that\u2014\n**(1)**\nthe amendment is necessary for public safety or transmission and grid reliability; or\n**(2)**\nthe actions, operations, or other requirements that the amendment would remove are no longer warranted.\n##### (b) Restriction on amendments\nThe process described in subsection (a) shall be the only method by which the Secretaries may operate the FCRPS in any way that is not consistent with the reasonable and prudent alternative set forth in the Supplemental Opinion.\n#### 5. Limitation on restricting FCRPS electrical generation; clarification\n##### (a) Restricting FCRPS electrical generation\nNo structural modification, action, study, or engineering plan that restricts electrical generation at any FCRPS hydroelectric dam, or that limits navigation on the Snake River in the State of Washington, Oregon, or Idaho, shall proceed unless such proposal is specifically and expressly authorized by a Federal statute enacted after the date of the enactment of this Act.\n##### (b) Clarification\nNothing in this section affects or interferes with the authority of the Secretaries to conduct operation and maintenance activities or make capital improvements necessary to meet authorized project purposes of FCRPS facilities.",
      "versionDate": "2025-01-22",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-23",
        "text": "Referred to the Subcommittee on Water Resources and Environment."
      },
      "number": "626",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Northwest Energy Security Act",
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
            "name": "Alternative and renewable resources",
            "updateDate": "2025-09-08T19:55:57Z"
          },
          {
            "name": "Dams and canals",
            "updateDate": "2025-09-08T19:55:57Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2025-09-08T19:55:57Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2025-09-08T19:55:57Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2025-09-08T19:55:57Z"
          },
          {
            "name": "Montana",
            "updateDate": "2025-09-08T19:55:57Z"
          },
          {
            "name": "Oregon",
            "updateDate": "2025-09-08T19:55:57Z"
          },
          {
            "name": "Washington State",
            "updateDate": "2025-09-08T19:55:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-05-02T13:47:37Z"
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
          "measure-id": "id119s182",
          "measure-number": "182",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s182v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Northwest Energy Security Act</strong></p><p>This bill requires Federal Columbia River Power System (FCRPS) operations to be consistent with the preferred alternative in a\u00a02020 environmental impact statement (EIS)\u00a0decision that focuses on the operations, maintenance, and configuration of dams in the system rather than wild fish restoration. The system includes dams in the Columbia and Snake rivers in Oregon, Washington, Montana, and Idaho.</p><p>Specifically, the Bureau of Reclamation, the Bonneville Power Administration, and the U.S. Army Corps of Engineers must operate the FCRPS consistent with the <em>Columbia River System Operations Environmental Impact Statement Record of Decision</em> dated September 2020. Thus, Reclamation,\u00a0the Bonneville Power Administration, and the Army Corps must follow the EIS rather than the 2023 Resilient Columbia Basin Initiative\u2014and a\u00a0supplemental EIS proposed in 2024\u2014that focus on wild fish restoration in the Columbia Basin.</p><p>The EIS decision may be amended if each agency determines that (1) changes are necessary for public safety or electrical grid reliability, or (2) certain requirements in the decision are no longer necessary.</p><p>Further, the bill requires statutory authorization for any structural modification, action, study, or engineering plan that (1) restricts FCRPS hydroelectric dam generation; or (2) limits navigation on the Snake River in Washington, Oregon, or Idaho.</p>"
        },
        "title": "Northwest Energy Security Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s182.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Northwest Energy Security Act</strong></p><p>This bill requires Federal Columbia River Power System (FCRPS) operations to be consistent with the preferred alternative in a\u00a02020 environmental impact statement (EIS)\u00a0decision that focuses on the operations, maintenance, and configuration of dams in the system rather than wild fish restoration. The system includes dams in the Columbia and Snake rivers in Oregon, Washington, Montana, and Idaho.</p><p>Specifically, the Bureau of Reclamation, the Bonneville Power Administration, and the U.S. Army Corps of Engineers must operate the FCRPS consistent with the <em>Columbia River System Operations Environmental Impact Statement Record of Decision</em> dated September 2020. Thus, Reclamation,\u00a0the Bonneville Power Administration, and the Army Corps must follow the EIS rather than the 2023 Resilient Columbia Basin Initiative\u2014and a\u00a0supplemental EIS proposed in 2024\u2014that focus on wild fish restoration in the Columbia Basin.</p><p>The EIS decision may be amended if each agency determines that (1) changes are necessary for public safety or electrical grid reliability, or (2) certain requirements in the decision are no longer necessary.</p><p>Further, the bill requires statutory authorization for any structural modification, action, study, or engineering plan that (1) restricts FCRPS hydroelectric dam generation; or (2) limits navigation on the Snake River in Washington, Oregon, or Idaho.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s182"
    },
    "title": "Northwest Energy Security Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Northwest Energy Security Act</strong></p><p>This bill requires Federal Columbia River Power System (FCRPS) operations to be consistent with the preferred alternative in a\u00a02020 environmental impact statement (EIS)\u00a0decision that focuses on the operations, maintenance, and configuration of dams in the system rather than wild fish restoration. The system includes dams in the Columbia and Snake rivers in Oregon, Washington, Montana, and Idaho.</p><p>Specifically, the Bureau of Reclamation, the Bonneville Power Administration, and the U.S. Army Corps of Engineers must operate the FCRPS consistent with the <em>Columbia River System Operations Environmental Impact Statement Record of Decision</em> dated September 2020. Thus, Reclamation,\u00a0the Bonneville Power Administration, and the Army Corps must follow the EIS rather than the 2023 Resilient Columbia Basin Initiative\u2014and a\u00a0supplemental EIS proposed in 2024\u2014that focus on wild fish restoration in the Columbia Basin.</p><p>The EIS decision may be amended if each agency determines that (1) changes are necessary for public safety or electrical grid reliability, or (2) certain requirements in the decision are no longer necessary.</p><p>Further, the bill requires statutory authorization for any structural modification, action, study, or engineering plan that (1) restricts FCRPS hydroelectric dam generation; or (2) limits navigation on the Snake River in Washington, Oregon, or Idaho.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s182"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s182is.xml"
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
      "title": "Northwest Energy Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T01:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Northwest Energy Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T01:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for operations of the Federal Columbia River Power System pursuant to a certain operation plan for a specified period of time, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T01:48:16Z"
    }
  ]
}
```
