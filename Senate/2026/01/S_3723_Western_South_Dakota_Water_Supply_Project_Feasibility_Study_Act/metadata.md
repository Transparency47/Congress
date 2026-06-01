# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3723?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3723
- Title: Western South Dakota Water Supply Project Feasibility Study Act
- Congress: 119
- Bill type: S
- Bill number: 3723
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-03-30T18:12:53Z
- Update date including text: 2026-03-30T18:12:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S379)
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S379)
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3723",
    "number": "3723",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Western South Dakota Water Supply Project Feasibility Study Act",
    "type": "S",
    "updateDate": "2026-03-30T18:12:53Z",
    "updateDateIncludingText": "2026-03-30T18:12:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S379)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T16:53:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:20Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3723is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3723\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Thune (for himself and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of the Interior to conduct a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water from the Missouri River to the Western Dakota Regional Water System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Western South Dakota Water Supply Project Feasibility Study Act .\n#### 2. Definitions\nIn this Act:\n**(1) Non-Federal project entity**\nThe term non-Federal project entity means the Western Dakota Regional Water System, Inc., a nonprofit corporation.\n**(2) Proposed rural water supply project**\nThe term proposed rural water supply project means the proposed project to supply municipal, rural, and industrial water from the Missouri River to the Western Dakota Regional Water System.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Western South Dakota water supply project feasibility study\n##### (a) Study\n**(1) In general**\nThe Secretary, in coordination with the non-Federal project entity, shall carry out a study to determine the feasibility of the proposed rural water supply project.\n**(2) Feasibility report**\nAfter completion of the feasibility study for the proposed rural water supply project under paragraph (1), the Secretary shall\u2014\n**(A)**\ndevelop a feasibility report that includes a recommendation of the Secretary on\u2014\n**(i)**\nwhether the proposed rural water supply project should be authorized for construction; and\n**(ii)**\nthe appropriate non-Federal share of construction costs, which shall be\u2014\n**(I)**\nat least 25 percent of the total construction costs; and\n**(II)**\ndetermined based on an analysis of the financial capability-to-pay the allocated construction and operations, maintenance, and replacement costs of the recommended plan;\n**(B)**\nsubmit the report under subparagraph (A) to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives; and\n**(C)**\nmake the report under subparagraph (A) publicly available, along with associated feasibility study documents.\n**(3) Consultation and cooperation**\nIn addition to the non-Federal project entity, the Secretary shall consult and cooperate with appropriate Federal, State, Tribal, regional, and local authorities during the conduct of the feasibility study and development of the feasibility report under this subsection.\n##### (b) Cost-Sharing agreement for feasibility study costs\nThe Secretary shall enter into a cost-sharing agreement (or an appropriate financial assistance agreement, as determined by the Secretary) with the non-Federal project entity to conduct a study under subsection (a) that complies with the reclamation feasibility standards.\n##### (c) Federal share of feasibility study costs\nThe Federal share of the total costs of carrying out the feasibility study under subsection (a) shall not exceed 50 percent.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $10,000,000.\n##### (e) Termination of authority\nThe authority provided by this section expires on the date that is 10 years after the date of enactment of this Act.",
      "versionDate": "2026-01-29",
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
        "actionDate": "2026-03-17",
        "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held."
      },
      "number": "3725",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lewis & Clark Regional Water System Expansion Feasibility Study Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-30",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "7288",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Western South Dakota Water Supply Project Feasibility Study Act",
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
            "name": "Congressional oversight",
            "updateDate": "2026-03-30T18:12:47Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-03-30T18:12:23Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-30T18:12:52Z"
          },
          {
            "name": "Missouri River",
            "updateDate": "2026-03-30T18:12:28Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-03-30T18:12:36Z"
          },
          {
            "name": "South Dakota",
            "updateDate": "2026-03-30T18:12:18Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-03-30T18:12:41Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-03-30T18:12:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-02-23T21:55:50Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3723is.xml"
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
      "title": "Western South Dakota Water Supply Project Feasibility Study Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Western South Dakota Water Supply Project Feasibility Study Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Interior to conduct a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water from the Missouri River to the Western Dakota Regional Water System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T04:03:36Z"
    }
  ]
}
```
