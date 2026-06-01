# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8688?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8688
- Title: Forest Health and Wildfire Risk Reduction Act
- Congress: 119
- Bill type: HR
- Bill number: 8688
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-27T08:05:53Z
- Update date including text: 2026-05-27T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8688",
    "number": "8688",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Forest Health and Wildfire Risk Reduction Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:53Z",
    "updateDateIncludingText": "2026-05-27T08:05:53Z"
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
          "date": "2026-05-07T13:04:25Z",
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
                "date": "2026-05-12T21:00:00Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "WA"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8688ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8688\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Hurd of Colorado (for himself and Mr. Newhouse ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo codify the categorical exclusion proposed in the National Environmental Policy Act Implementing Procedures for the Bureau of Land Management related to tree density modification published on April 6, 2026.\n#### 1. Short title\nThis Act may be cited as the Forest Health and Wildfire Risk Reduction Act .\n#### 2. Codification of categorical exclusion\n##### (a) In general\nTree density modification activities described in subsection (b) are a category of actions hereby designated as being categorically excluded from the preparation of an environmental assessment or an environmental impact statement under section 102 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332 ).\n##### (b) Tree density modification activities designated for categorical exclusion\n**(1) Conditions**\nThe tree density modification activities designated under this section for categorical exclusion are covered actions carried out within a treatment area of less than 5,000 acres.\n**(2) Exclusion**\nThe categorical exclusion provided for under subsection (a) does not apply to\u2014\n**(A)**\nsilvicultural methods that are intended to regenerate whole stands, such as even-aged regeneration harvest, clearcutting, or variable retention harvest; or\n**(B)**\nvegetation management intended to convert forest or woodlands to non-forest vegetation cover.\n**(3) Limitations on actions**\nIn addition to the covered actions under paragraph (1), tree density modification activities to which the categorical exclusion under this section applies\u2014\n**(A)**\nmay include construction of up to 5 miles of new permanent road to facilitate covered actions, provided that all segments conform to applicable land use planning decisions with route-specific designations disclosed where travel management planning has been completed;\n**(B)**\nmay include maintenance and renovation of existing roads as needed;\n**(C)**\nmay include construction of temporary roads not to exceed a ratio of 2.5 miles per 1,000 acres of treatment area as needed, provided that the temporary roads\u2014\n**(i)**\nare not part of the permanent transportation system of the Bureau;\n**(ii)**\nare designed to standards appropriate for their intended use (safety, erosion control, sedimentation prevention, and resource protection);\n**(iii)**\nare not needed for long-term resource management; and\n**(iv)**\nare decommissioned and stabilized after use to minimize erosion and protect water quality; and\n**(D)**\nrequire the disclosure of design features, in documentation of finding that an action is excluded pursuant to the use of this categorical exclusion, that address the following resource considerations consistent with applicable land use plan decisions, or, where no plan requirements apply, specify how the following resource considerations are addressed:\n**(i)**\nSnag and downed wood\u2014amount to be created or retained.\n**(ii)**\nErosion control\u2014specifications or measures (e.g., water bars, dispersed slash).\n**(iii)**\nSoil compaction\u2014criteria for avoidance, minimization, or remediation.\n**(iv)**\nLogging systems\u2014types and scope of constraints (e.g., seasonal, location, extent, etc.).\n**(v)**\nSeasonal operations\u2014purpose and extent of operating restrictions.\n**(vi)**\nInvasive species\u2014measures to prevent or limit spread.\n**(vii)**\nRiparian areas\u2014buffer widths and/or operating restrictions.\n**(viii)**\nPrescribed fire\u2014operating constraints for underburning or pile burning.\n**(ix)**\nTemporary roads\u2014decommissioning standards.\n##### (c) Definitions\nIn this section:\n**(1) Bureau**\nThe term Bureau means the Bureau of Land Management.\n**(2) Covered actions**\nThe term covered actions means one or more of the following actions:\n**(A)**\nCutting, yarding, and the use of landings and skid trails to facilitate the removal of commercial and non-commercial trees.\n**(B)**\nChipping, grinding, or removal of residual slash.\n**(C)**\nGroup selection silvicultural treatment to promote regeneration of shade intolerant species and early successional habitat in an uneven-aged context not to exceed 2-acre individual patches and 10 percent of the treatment area (group selection openings will retain overstory legacy elements consistent with the applicable land use plan (for example, large fire resilient trees, snags)).\n**(D)**\nPile burning or underburning of fuels created by covered actions described in clauses (i) through (iii) and fuels within or in close proximity to those actions\u2019 treatment boundaries whether created by those actions or not.\n**(E)**\nSeeding or planting necessary to accelerate native species re-establishment.\n**(3) Group selection**\nThe term group selection means an uneven-aged harvest method where groups of trees are removed to promote spatial heterogeneity, regeneration of desired tree species, or the establishment of new cohorts.\n**(4) Permanent road**\nThe term permanent road means a road constructed or reconstructed and managed as part of the permanent transportation system of the Bureau.\n**(5) Temporary road**\nThe term temporary road means a road authorized by contract, permit, lease, written authorization, or emergency operation, not added to the permanent transportation system of the Bureau, and decommissioned after use.",
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
        "updateDate": "2026-05-21T15:16:41Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8688ih.xml"
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
      "title": "Forest Health and Wildfire Risk Reduction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-09T05:23:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Forest Health and Wildfire Risk Reduction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To codify the categorical exclusion proposed in the National Environmental Policy Act Implementing Procedures for the Bureau of Land Management related to tree density modification published on April 6, 2026.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-09T05:18:33Z"
    }
  ]
}
```
