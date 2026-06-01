# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/888?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/888
- Title: Oregon Recreation Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 888
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/888",
    "number": "888",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Oregon Recreation Enhancement Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T19:07:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:12Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s888is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 888\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Wyden (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo designate certain land administered by the Bureau of Land Management and the Forest Service in the State of Oregon as wilderness and national recreation areas, to withdraw certain land located in Curry County and Josephine County, Oregon, from all forms of entry, appropriation, or disposal under the public land laws, location, entry, and patent under the mining laws, and operation under the mineral leasing and geothermal leasing laws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Oregon Recreation Enhancement Act .\n#### 2. Definitions\nIn this Act:\n**(1) Secretary**\nThe term Secretary means\u2014\n**(A)**\nthe Secretary of the Interior, with respect to public land administered by the Secretary of the Interior; or\n**(B)**\nthe Secretary of Agriculture, with respect to National Forest System land.\n**(2) State**\nThe term State means the State of Oregon.\n#### 3. Rogue Canyon and Molalla Recreation Areas, Oregon\n##### (a) Designation of rogue canyon and molalla recreation areas\nFor the purposes of protecting, conserving, and enhancing the unique and nationally important recreational, ecological, scenic, cultural, watershed, and fish and wildlife values of the areas, the following areas in the State are designated as recreation areas for management by the Secretary in accordance with subsection (c):\n**(1) Rogue canyon recreation area**\nThe approximately 98,150 acres of Bureau of Land Management land within the boundary generally depicted as the Rogue Canyon Recreation Area on the map entitled Rogue Canyon Recreation Area Wild Rogue Wilderness Additions and dated November 19, 2019, which is designated as the Rogue Canyon Recreation Area .\n**(2) Molalla recreation area**\nThe approximately 29,884 acres of Bureau of Land Management land within the boundary generally depicted on the map entitled Molalla Recreation Area and dated September 26, 2018, which is designated as the Molalla Recreation Area .\n##### (b) Maps and legal descriptions\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall prepare a map and legal description of each recreation area designated by subsection (a).\n**(2) Effect**\nThe maps and legal descriptions prepared under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct any minor errors in the maps and legal descriptions.\n**(3) Public availability**\nThe maps and legal descriptions prepared under paragraph (1) shall be available for public inspection in the appropriate offices of the Bureau of Land Management.\n##### (c) Administration\n**(1) Applicable law**\nThe Secretary shall administer each recreation area designated by subsection (a)\u2014\n**(A)**\nin a manner that conserves, protects, and enhances the purposes for which the recreation area is established; and\n**(B)**\nin accordance with\u2014\n**(i)**\nthis section;\n**(ii)**\nthe Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); and\n**(iii)**\nother applicable laws.\n**(2) Uses**\nThe Secretary shall only allow those uses of a recreation area designated by subsection (a) that are consistent with the purposes for which the recreation area is established.\n**(3) Wildfire risk assessment**\nNot later than 280 days after the date of enactment of this Act, the Secretary, in consultation with the Oregon Governor\u2019s Council on Wildfire Response, shall conduct a wildfire risk assessment that covers\u2014\n**(A)**\nthe recreation areas designated by subsection (a);\n**(B)**\nthe Wild Rogue Wilderness; and\n**(C)**\nany Federal land adjacent to an area described in subparagraph (A) or (B).\n**(4) Wildfire mitigation plan**\n**(A) In general**\nNot later than 1 year after the date on which the wildfire risk assessment is conducted under paragraph (3), the Secretary shall develop a wildfire mitigation plan, based on the wildfire risk assessment, that identifies, evaluates, and prioritizes treatments and other management activities that can be implemented on the Federal land covered by the wildfire risk assessment (other than Federal land designated as a unit of the National Wilderness Preservation System) to mitigate wildfire risk to communities located near the applicable Federal land.\n**(B) Plan components**\nThe wildfire mitigation plan developed under subparagraph (A) shall include\u2014\n**(i)**\nvegetation management projects (including mechanical treatments to reduce hazardous fuels and improve forest health and resiliency);\n**(ii)**\nevacuation routes for communities located near the applicable Federal land, which shall be developed in consultation with State and local fire agencies; and\n**(iii)**\nstrategies for public dissemination of emergency evacuation plans and routes.\n**(C) Applicable law**\nThe wildfire mitigation plan under subparagraph (A) shall be developed in accordance with\u2014\n**(i)**\nthis section; and\n**(ii)**\nany other applicable law.\n**(5) Road construction**\n**(A) In general**\nExcept as provided in subparagraph (B) or as the Secretary determines necessary for public safety, no new permanent or temporary roads shall be constructed (other than the repair and maintenance of existing roads) within a recreation area designated by subsection (a).\n**(B) Temporary roads**\nConsistent with the purposes of this Act, the Secretary may construct temporary roads within a recreation area designated by subsection (a) to implement the wildfire mitigation plan developed under paragraph (4), unless the temporary road would be within an area designated as a unit of the National Wilderness Preservation System.\n**(C) Effect**\nNothing in this paragraph affects the administration by the Secretary of the Molalla Forest Road in accordance with applicable resource management plans.\n**(6) Effect on wildfire management**\nNothing in this section alters the authority of the Secretary (in cooperation with other Federal, State, and local agencies, as appropriate) to conduct wildland fire operations within a recreation area designated by subsection (a), consistent with the purposes of this Act.\n**(7) Withdrawal**\nSubject to valid existing rights, all Federal surface and subsurface land within a recreation area designated by subsection (a) is withdrawn from all forms of\u2014\n**(A)**\nentry, appropriation, or disposal under the public land laws;\n**(B)**\nlocation, entry, and patent under the mining laws; and\n**(C)**\ndisposition under all laws pertaining to mineral leasing, geothermal leasing, or mineral materials.\n**(8) No effect on wilderness areas**\nAny wilderness area located within a recreation area designated by subsection (a) shall be administered in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ).\n##### (d) Adjacent management\nNothing in this section creates any protective perimeter or buffer zone around a recreation area designated by subsection (a).\n#### 4. Expansion of Wild Rogue Wilderness Area\n##### (a) Definitions\nIn this section:\n**(1) Map**\nThe term map means the map entitled Rogue Canyon Recreation Area Wild Rogue Wilderness Additions and dated November 19, 2019.\n**(2) Wilderness additions**\nThe term Wilderness additions means the land added to the Wild Rogue Wilderness under subsection (b)(1).\n##### (b) Expansion of wild rogue wilderness area\n**(1) Expansion**\nThe approximately 59,512 acres of Federal land in the State generally depicted on the map as Proposed Wilderness shall be added to and administered as part of the Wild Rogue Wilderness in accordance with the Endangered American Wilderness Act of 1978 ( 16 U.S.C. 1132 note; Public Law 95\u2013237 ), except that\u2014\n**(A)**\nthe Secretary of the Interior and the Secretary of Agriculture shall administer the Federal land under their respective jurisdiction; and\n**(B)**\nany reference in that Act to the Secretary of Agriculture shall be considered to be a reference to the Secretary of Agriculture or the Secretary of the Interior, as applicable.\n**(2) Map; legal description**\n**(A) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall prepare a map and legal description of the wilderness area designated by paragraph (1).\n**(B) Force of law**\nThe map and legal description filed under subparagraph (A) shall have the same force and effect as if included in this section, except that the Secretary may correct typographical errors in the map and legal description.\n**(C) Public availability**\nThe map and legal description filed under subparagraph (A) shall be on file and available for public inspection in the appropriate offices of the Bureau of Land Management and Forest Service.\n**(3) Fire, insects, and disease**\nThe Secretary may take such measures within the Wilderness additions as the Secretary determines to be necessary for the control of fire, insects, and disease, in accordance with section 4(d)(1) of the Wilderness Act ( 16 U.S.C. 1133(d)(1) ).\n**(4) Withdrawal**\nSubject to valid existing rights, the Wilderness additions are withdrawn from all forms of\u2014\n**(A)**\nentry, appropriation, or disposal under the public land laws;\n**(B)**\nlocation, entry, and patent under the mining laws; and\n**(C)**\ndisposition under all laws pertaining to mineral leasing, geothermal leasing, or mineral materials.\n**(5) Tribal rights**\nNothing in this subsection alters, modifies, enlarges, diminishes, or abrogates the treaty rights of any Indian Tribe.\n#### 5. Withdrawal of Federal land, Curry County and Josephine County, Oregon\n##### (a) Definitions\nIn this section:\n**(1) Eligible Federal land**\nThe term eligible Federal land means\u2014\n**(A)**\nany federally owned land or interest in land depicted on the Maps as within the Hunter Creek and Pistol River Headwaters Withdrawal Proposal or the Rough and Ready and Baldface Creeks Mineral Withdrawal Proposal; or\n**(B)**\nany land or interest in land located within such withdrawal proposals that is acquired by the Federal Government after the date of enactment of this Act.\n**(2) Maps**\nThe term Maps means\u2014\n**(A)**\nthe Bureau of Land Management map entitled Hunter Creek and Pistol River Headwaters Withdrawal Proposal and dated January 12, 2015; and\n**(B)**\nthe Bureau of Land Management map entitled Rough and Ready and Baldface Creeks Mineral Withdrawal Proposal and dated January 12, 2015.\n##### (b) Withdrawal\nSubject to valid existing rights, the eligible Federal land is withdrawn from all forms of\u2014\n**(1)**\nentry, appropriation, or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\noperation under the mineral leasing and geothermal leasing laws.\n##### (c) Availability of maps\nNot later than 30 days after the date of enactment of this Act, the Maps shall be made available to the public at each appropriate office of the Bureau of Land Management.\n##### (d) Existing uses not affected\nExcept with respect to the withdrawal under subsection (b), nothing in this section restricts recreational uses, hunting, fishing, forest management activities, or other authorized uses allowed on the date of enactment of this Act on the eligible Federal land in accordance with applicable law.",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in Senate"
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
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-12-12T20:07:38Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-12-12T20:07:38Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-12T20:07:38Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-12-12T20:07:38Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-12-12T20:07:38Z"
          },
          {
            "name": "Oregon",
            "updateDate": "2025-12-12T20:07:38Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-12T20:07:38Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2025-12-12T20:07:38Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-12T20:07:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T18:20:40Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s888is.xml"
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
      "title": "Oregon Recreation Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Oregon Recreation Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to designate certain land administered by the Bureau of Land Management and the Forest Service in the State of Oregon as wilderness and national recreation areas, to withdraw certain land located in Curry County and Josephine County, Oregon, from all forms of entry, appropriation, or disposal under the public land laws, location, entry, and patent under the mining laws, and operation under the mineral leasing and geothermal leasing laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:39Z"
    }
  ]
}
```
