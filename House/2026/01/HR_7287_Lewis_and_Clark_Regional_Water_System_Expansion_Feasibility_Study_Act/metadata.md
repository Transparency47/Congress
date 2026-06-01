# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7287?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7287
- Title: Lewis and Clark Regional Water System Expansion Feasibility Study Act
- Congress: 119
- Bill type: HR
- Bill number: 7287
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-04-30T08:06:29Z
- Update date including text: 2026-04-30T08:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-22 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-29 - Committee: Subcommittee Hearings Held
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-22 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-29 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7287",
    "number": "7287",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Lewis and Clark Regional Water System Expansion Feasibility Study Act",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:29Z",
    "updateDateIncludingText": "2026-04-30T08:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-29T18:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-04-22T19:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
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
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "IA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "MN"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7287ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7287\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Johnson of South Dakota (for himself and Mr. Feenstra ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of the Interior to conduct a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water to expand the capacity and reach of the Lewis and Clark Regional Water System in the States of Iowa, Minnesota, and South Dakota.\n#### 1. Short title\nThis Act may be cited as the Lewis and Clark Regional Water System Expansion Feasibility Study Act .\n#### 2. Definitions\nIn this Act:\n**(1) Non-Federal project entity**\nThe term non-Federal project entity means\u2014\n**(A)**\nthe Lewis and Clark Regional Water System, Inc.; and\n**(B)**\nany nonprofit successor entity to the corporation described in subparagraph (A).\n**(2) Proposed rural water supply project**\nThe term proposed rural water supply project means the proposed project to supply municipal, rural, and industrial water to expand the capacity and reach of the Lewis and Clark Regional Water System in the States of Iowa, Minnesota, and South Dakota.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Lewis and Clark Regional Water System expansion feasibility study\n##### (a) Study\n**(1) In general**\nThe Secretary, in coordination with the non-Federal project entity, shall carry out a study to determine the feasibility of the proposed rural water supply project.\n**(2) Feasibility report**\nAfter completion of the feasibility study for the proposed rural water supply project under paragraph (1), the Secretary shall\u2014\n**(A)**\ndevelop a feasibility report that includes a recommendation of the Secretary on\u2014\n**(i)**\nwhether the proposed rural water supply project should be authorized for construction; and\n**(ii)**\nthe appropriate non-Federal share of construction costs, which shall be\u2014\n**(I)**\nat least 25 percent of the total construction costs; and\n**(II)**\ndetermined based on an analysis of the financial capability-to-pay the allocated construction and operations, maintenance, and replacement costs of the recommended plan;\n**(B)**\nsubmit the report under subparagraph (A) to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives; and\n**(C)**\nmake the report under subparagraph (A) publicly available, along with associated feasibility study documents.\n**(3) Consultation and cooperation**\nIn addition to the non-Federal project entity, the Secretary shall consult and cooperate with appropriate Federal, State, Tribal, regional, and local authorities during the conduct of the feasibility study and development of the feasibility report under this subsection.\n##### (b) Cost-Sharing agreement for feasibility study costs\nThe Secretary shall enter into a cost-sharing agreement (or an appropriate financial assistance agreement, as determined by the Secretary) with the non-Federal project entity to conduct a study under subsection (a) that complies with the reclamation feasibility standards.\n##### (c) Federal share of feasibility study costs\nThe Federal share of the total costs of carrying out the feasibility study under subsection (a) shall not exceed 50 percent.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $10,000,000.\n##### (e) Termination of authority\nThe authority provided by this section expires on the date that is 10 years after the date of enactment of this Act.",
      "versionDate": "2026-01-30",
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
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "Iowa",
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "South Dakota",
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-03-30T18:14:37Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-03-30T18:14:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-02-17T18:22:09Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7287ih.xml"
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
      "title": "Lewis and Clark Regional Water System Expansion Feasibility Study Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T06:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lewis and Clark Regional Water System Expansion Feasibility Study Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-13T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Interior to conduct a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water to expand the capacity and reach of the Lewis and Clark Regional Water System in the States of Iowa, Minnesota, and South Dakota.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T06:33:43Z"
    }
  ]
}
```
