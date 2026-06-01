# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8682?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8682
- Title: Accelerating Forest Management Act
- Congress: 119
- Bill type: HR
- Bill number: 8682
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-27T08:05:38Z
- Update date including text: 2026-05-27T08:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-12 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-05-21 - Committee: Subcommittee Hearings Held
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-12 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-05-21 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8682",
    "number": "8682",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Accelerating Forest Management Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:38Z",
    "updateDateIncludingText": "2026-05-27T08:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:03:15Z",
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
                "date": "2026-05-21T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-05-12T21:00:56Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8682ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8682\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Downing introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo codify the categorical exclusion proposed in the National Environmental Policy Act Implementing Procedures for the Bureau of Land Management related to salvage harvesting published on April 6, 2026, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating Forest Management Act .\n#### 2. Codification of categorical exclusion\n##### (a) In general\nSalvage harvesting activities described in subsection (b) are a category of actions hereby designated as being categorically excluded from the preparation of an environmental assessment or an environmental impact statement under section 102 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332 ).\n##### (b) Salvage harvesting activities designated for categorical exclusions\n**(1) In general**\nThe salvage harvesting activities designated under this section for categorical exclusion are\u2014\n**(A)**\ncovered actions with respect to dead or dying trees resulting from fire, insects, disease, drought, or other disturbances within treatment areas\u2014\n**(i)**\nnot to exceed 1,000 acres where the disturbance affects 3,000 acres of Bureau-managed lands or less; and\n**(ii)**\nnot to exceed the lesser of 5,000 acres or 1/3 of the disturbance area where the disturbance exceeds 3,000 acres of Bureau-managed lands; and\n**(B)**\ncarried out in conformance with applicable land use planning decisions.\n**(2) Limitations**\nIn addition to the covered actions under paragraph (1), salvage harvesting activities to which the categorical exclusion applies under this section\u2014\n**(A)**\nmay include construction of up to 1 mile of new permanent road to facilitate covered actions, provided that all segments conform to applicable land use planning decisions with route-specific designations disclosed where travel management planning has been completed;\n**(B)**\nmay include maintenance and renovation of existing roads as needed;\n**(C)**\nmay include construction of temporary roads not to exceed a ratio of 2.25 miles per 1,000 acres of harvest area as needed, provided that the temporary roads\u2014\n**(i)**\nare not part of the permanent transportation system of the Bureau;\n**(ii)**\nare designed to standards appropriate for their intended use (safety, erosion control, sedimentation prevention, and resource protection);\n**(iii)**\nare not needed for long-term resource management; and\n**(iv)**\nare decommissioned and stabilized after use to minimize erosion and protect water quality; and\n**(D)**\nrequire the disclosure of design features, in documentation of finding that an action is excluded pursuant to the use of this categorical exclusion, that address the following resource considerations consistent with applicable land use plan decisions, or, where no plan requirements apply, specify how the following resource considerations are addressed:\n**(i)**\nSnag and downed wood\u2014amount to be created or retained.\n**(ii)**\nErosion control\u2014specifications or measures (e.g., water bars, dispersed slash).\n**(iii)**\nSoil compaction\u2014criteria for avoidance, minimization, or remediation.\n**(iv)**\nLogging systems\u2014types and scope of constraints (e.g., seasonal, location, extent, etc.).\n**(v)**\nSeasonal operations\u2014purpose and extent of operating restrictions.\n**(vi)**\nInvasive species\u2014measures to prevent or limit spread.\n**(vii)**\nRiparian areas\u2014buffer widths and/or operating restrictions.\n**(viii)**\nPrescribed fire\u2014operating constraints for underburning or pile burning.\n**(ix)**\nTemporary roads\u2014decommissioning standards.\n##### (c) Definitions\nIn this section:\n**(1) Bureau**\nThe term Bureau means the Bureau of Land Management.\n**(2) Covered actions**\nThe term covered actions means the one or more of the following actions:\n**(A)**\nCutting, yarding, and removal of dead or dying trees.\n**(B)**\nCutting, yarding, and removal of live trees needed for operations, landings, skid trails, or road clearing.\n**(C)**\nChipping/grinding or removal of residual slash.\n**(D)**\nJackpot burning, pile burning, and underburning.\n**(E)**\nSeeding or planting necessary to accelerate native species re-establishment.\n**(3) Dying tree**\nThe term dying tree means a standing tree severely damaged by disturbance (such as fire, wind, insects, disease, drought) and, in the judgment of a forestry professional or someone technically trained for the work, is likely to die within two years.\n**(4) Permanent road**\nThe term permanent road means a road constructed or reconstructed for use, as part of the permanent transportation system of the Bureau.\n**(5) Temporary road**\nThe term temporary road means a road authorized by contract, permit, lease, written authorization, or emergency operation, not added to the permanent system, and decommissioned after use.\n#### 3. Extension of Forest Ecosystem Health and Recovery Fund\nTitle I of the Department of the Interior, Environment, and Related Agencies Appropriations Act, 2010 ( Public Law 111\u201388 ) is amended in the text under the heading FOREST ECOSYSTEM HEALTH AND RECOVERY FUND by striking 2020 each place it appears and inserting 2033 .",
      "versionDate": "2026-05-07",
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
        "name": "Environmental Protection",
        "updateDate": "2026-05-21T17:48:06Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8682ih.xml"
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
      "title": "Accelerating Forest Management Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accelerating Forest Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify the categorical exclusion proposed in the National Environmental Policy Act Implementing Procedures for the Bureau of Land Management related to salvage harvesting published on April 6, 2026, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:18:31Z"
    }
  ]
}
```
