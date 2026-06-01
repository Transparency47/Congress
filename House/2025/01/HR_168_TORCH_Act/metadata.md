# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/168?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/168
- Title: TORCH Act
- Congress: 119
- Bill type: HR
- Bill number: 168
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-04-21T01:15:56Z
- Update date including text: 2026-04-21T01:15:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-04 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-04 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/168",
    "number": "168",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000578",
        "district": "1",
        "firstName": "Doug",
        "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
        "lastName": "LaMalfa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "TORCH Act",
    "type": "HR",
    "updateDate": "2026-04-21T01:15:56Z",
    "updateDateIncludingText": "2026-04-21T01:15:56Z"
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
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:27:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T13:10:57Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:27:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr168ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 168\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. LaMalfa introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo improve the ability of the Secretary of Agriculture and the Secretary of the Interior to carry out forest management activities that reduce the risk of catastrophic wildfires, and for other purposes.\n#### 1. Short title\n##### (a) Short title\nThis Act may be cited as the Targeted Operations to Remove Catastrophic Hazards Act or the TORCH Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nTitle I\u2014HAZARDOUS FUEL REDUCTION ACTIVITIES\nSec. 101. Categorical exclusion for high priority hazard tree activities.\nSec. 102. Utilizing timber sales on National Forest System land for extreme risk reduction.\nSec. 103. Utilizing grazing for wildfire risk reduction.\nSec. 104. Amendments to the Healthy Forest Restoration Act of 2003 to improve wildfire mitigation.\nSec. 105. Amendment to fuel breaks in forests and other wildland vegetation.\nTitle II\u2014GOOD NEIGHBOR AUTHORITY\nSec. 201. Modification of the treatment of certain revenue and payments under good neighbor agreements.\nTitle III\u2014ELECTRICAL UTILITY LINES RIGHTS-OF-WAYS AND RELATED VEGETATION MANAGEMENT\nSec. 301. Vegetation management, facility inspection, and operation and maintenance relating to electric transmission and distribution facility rights-of-way.\nSec. 302. Categorical exclusion for electric utility lines rights-of-way.\nSec. 303. Permits and agreements with electrical utilities.\nTitle IV\u2014REFORM OF CERTAIN ADMINISTRATIVE REQUIREMENTS\nSec. 401. Nonapplicability of certain additional consultation requirements of the Endangered Species Act of 1973.\nSec. 402. Amendment to categorical exclusion for collaborative restoration projects.\nI\nHAZARDOUS FUEL REDUCTION ACTIVITIES\n#### 101. Categorical exclusion for high priority hazard tree activities\n##### (a) Categorical exclusion\n**(1) In general**\nNot later than 1 year after the date of enactment of this section, the Secretary of Agriculture shall develop a categorical exclusion (as defined in section 1508.4 of title 40, Code of Federal Regulations (or a successor regulation)) for high priority hazard tree activities.\n**(2) Administration**\nIn developing and administering the categorical exclusion under paragraph (1), the Secretary shall\u2014\n**(A)**\ncomply with the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ); and\n**(B)**\napply the extraordinary circumstances procedures under section 220.6 of title 36, Code of Federal Regulations (or successor regulations), in determining whether to use the categorical exclusion.\n##### (b) Project size limitations\nA project to carry out high priority hazard tree activities to which a categorical exclusion under subsection (a) is applied may not exceed 3,000 acres.\n##### (c) Definitions\nIn this section:\n**(1) High-priority hazard tree**\nThe term high-priority hazard tree means a standing tree that\u2014\n**(A)**\npresents a visible hazard to people or Federal property due to conditions such as deterioration of or damage to the root system, trunk, stem, or limbs of the tree, or the direction or lean of the tree, as determined by the Secretary;\n**(B)**\nis determined by the Secretary to be highly likely to fail and, if it failed, would be highly likely to cause injury to people or damage to Federal property; and\n**(C)**\nis within 300 feet of a National Forest System road with a maintenance level of 3, 4, or 5, a National Forest System trail, or a developed recreation site on National Forest System lands that is operated and maintained by the Secretary.\n**(2) High-priority hazard tree activities**\nThe term high priority hazard tree activities \u2014\n**(A)**\nmeans forest management activities that mitigate the risks associated with high-priority hazard trees, including pruning, felling, and disposal of those trees; and\n**(B)**\ndoes not include any activity\u2014\n**(i)**\nconducted in a wilderness area or wilderness study area;\n**(ii)**\nfor the construction of a permanent road or permanent trail;\n**(iii)**\nconducted on Federal land on which, by Act of Congress or Presidential proclamation, the removal of vegetation is restricted or prohibited;\n**(iv)**\nthat would be inconsistent with the applicable land and resource management plan; or\n**(v)**\nconducted in an inventoried roadless area.\n#### 102. Utilizing timber sales on National Forest System land for extreme risk reduction\nSection 14 of the National Forest Management Act of 1976 ( 16 U.S.C. 472a ) is amended\u2014\n**(1)**\nin subsection (d) by striking $10,000 and inserting $50,000 ; and\n**(2)**\nby adding at the end the following new subsection:\n(j) In the event of extreme risks to a unit of National Forest System land, including catastrophic wildfire, insect and disease outbreak, wind, hurricane, flood, drought, or to avoid impacts from such extreme events, the Secretary may, without an appraisal and under such rules and regulations prescribed by the Secretary, dispose of by sale or otherwise, portions of trees, or forest products located on such unit of National Forest System lands. .\n#### 103. Utilizing grazing for wildfire risk reduction\nThe Secretary of Agriculture, acting through the Chief of the U.S. Forest Service, in coordination with holders of permits to graze livestock on Federal land, shall develop a strategy to increase opportunities to utilize livestock grazing as wildfire risk reduction strategy, including\u2014\n**(1)**\ncompletion of reviews (as required under the National Environmental Policy Act of 1969 (U.S.C. 4321 et seq.)) to allow permitted grazing on vacant grazing allotments during instances of drought, wildfire or other natural disasters that disrupt grazing on allotments already permitted;\n**(2)**\nuse of targeted grazing;\n**(3)**\nincrease use of temporary permits to promote targeted fuels reduction and reduction of invasive annual grasses;\n**(4)**\nincreased use of grazing as a postfire recovery and restoration strategy, where appropriate; and\n**(5)**\nuse all applicable authorities under the law.\n#### 104. Amendments to the Healthy Forest Restoration Act of 2003 to improve wildfire mitigation\n##### (a) Promoting cross-Boundary wildfire mitigation\nSection 103(e)(5) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6513(e)(5) ) is amended by striking 2023 and inserting 2030 .\n##### (b) Wildfire resilience project size\nSection 605(c)(1) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591d(c)(1) ) is amended by striking 3000 acres and inserting 10,000 acres .\n#### 105. Amendment to fuel breaks in forests and other wildland vegetation\nSection 40806(d)(1) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592b(d)(1) ) is amended by striking 3,000 acres and inserting 10,000 acres .\nII\nGOOD NEIGHBOR AUTHORITY\n#### 201. Modification of the treatment of certain revenue and payments under good neighbor agreements\n##### (a) Good neighbor authority\nSection 8206 of the Agricultural Act of 2014 ( 16 U.S.C. 2113a ) is amended\u2014\n**(1)**\nin subsection (a)(6), by striking or Indian tribe ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(A), by inserting , Indian tribe, after Governor ;\n**(B)**\nin paragraph (2)(C), by striking clause (i) and inserting the following:\n(i) In general Funds received from the sale of timber by a Governor, an Indian tribe, or a county under a good neighbor agreement shall be retained and used by the Governor, Indian tribe, or county, as applicable\u2014 (I) to carry out authorized restoration services under the good neighbor agreement; and (II) if there are funds remaining after carrying out subclause (I), to carry out authorized restoration services under other good neighbor agreements. ; and\n**(C)**\nin paragraph (3), by inserting , Indian tribe, after Governor ; and\n**(D)**\nby striking paragraph (4).\n##### (b) Conforming amendments\nSection 8206(a) of the Agricultural Act of 2014 ( 16 U.S.C. 2113a(a) ) is amended\u2014\n**(1)**\nin paragraph (1)(B), by inserting , Indian tribe, after Governor ; and\n**(2)**\nin paragraph (5), by inserting , Indian tribe, after Governor .\n##### (c) Effective date\nThe amendments made by this Act apply to any project initiated pursuant to a good neighbor agreement (as defined in section 8206(a) of the Agricultural Act of 2014 ( 16 U.S.C. 2113a(a) ))\u2014\n**(1)**\nbefore the date of enactment of this Act, if the project was initiated after the date of enactment of the Agriculture Improvement Act of 2018 ( Public Law 115\u2013334 ; 132 Stat. 4490); or\n**(2)**\non or after the date of enactment of this Act.\nIII\nELECTRICAL UTILITY LINES RIGHTS-OF-WAYS AND RELATED VEGETATION MANAGEMENT\n#### 301. Vegetation management, facility inspection, and operation and maintenance relating to electric transmission and distribution facility rights-of-way\n##### (a) Hazard trees within 50 feet of electric power line\nSection 512(a)(1)(B)(ii) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1772(a)(1)(B)(ii) ) is amended by striking 10 and inserting 50 .\n##### (b) Consultation with private landowners\nSection 512(c)(3)(E) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1772(c)(3)(E) ) is amended\u2014\n**(1)**\nin clause (i), by striking and at the end;\n**(2)**\nin clause (ii), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(iii) consulting with private landowners with respect to any hazard trees identified for removal from land owned by such private landowners. .\n##### (c) Review and approval process\nClause (iv) of section 512(c)(4)(A) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1772(c)(4)(A) ) is amended to read as follows:\n(iv) ensures that\u2014 (I) a plan submitted without a modification under clause (iii) shall be automatically approved 60 days after review; and (II) a plan submitted with a modification under clause (iii) shall be automatically approved 67 days after review. .\n#### 302. Categorical exclusion for electric utility lines rights-of-way\n##### (a) Categorical exclusion established\nForest management activities described in subsection (c) are a category of activities designated as being categorically excluded from the preparation of an environmental assessment or an environmental impact statement under section 102 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332 ).\n##### (b) Forest management activities designated for categorical exclusion\nThe forest management activities designated as being categorically excluded under subsection (b) are\u2014\n**(1)**\nthe development and approval of a vegetation management, facility inspection, and operation and maintenance plan submitted under section 512(c)(1) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1772(c)(1) ) by the Secretary concerned; and\n**(2)**\nthe implementation of routine activities conducted under the plan referred to in paragraph (1).\n##### (c) Availability of categorical exclusion\nOn and after the date of the enactment of this Act, the Secretary concerned may use the categorical exclusion established under subsection (b) in accordance with this section.\n##### (d) Extraordinary circumstances\nUse of the categorical exclusion established under subsection (b) shall not be subject to the extraordinary circumstances procedures in section 220.6, title 36, Code of Federal Regulations, or section 1508.4, title 40, Code of Federal Regulations.\n##### (e) Exclusion of certain areas\nThe categorical exclusion established under subsection (b) shall not apply to any forest management activity conducted\u2014\n**(1)**\nin a component of the National Wilderness Preservation System; or\n**(2)**\non National Forest System lands on which, by Act of Congress, the removal of vegetation is restricted or prohibited.\n##### (f) Permanent roads\n**(1) Prohibition on establishment**\nA forest management activity designated under subsection (c) shall not include the establishment of a permanent road.\n**(2) Existing roads**\nThe Secretary concerned may carry out necessary maintenance and repair on an existing permanent road for the purposes of conducting a forest management activity designated under subsection (c).\n**(3) Temporary roads**\nThe Secretary concerned shall decommission any temporary road constructed for a forest management activity designated under subsection (c) not later than 3 years after the date on which the action is completed.\n##### (g) Applicable laws\nA forest management activity designated under subsection (c) shall not be subject to section 7 of the Endangered Species Act of 1973 ( 16 U.S.C. 1536 ), section 106 of the National Historic Preservation Act, or any other applicable law.\n##### (h) Secretary concerned defined\nIn this section, the term Secretary concerned means\u2014\n**(1)**\nthe Secretary of Agriculture, with respect to National Forest System lands; and\n**(2)**\nthe Secretary of the Interior, with respect to public lands.\n#### 303. Permits and agreements with electrical utilities\n##### (a) In general\nIn any special use permit or easement on National Forest System lands provided to an electric utility company (as defined in section 1262 of the Energy Policy Act of 2005 ( 42 U.S.C. 16451 )) the Secretary of Agriculture may provide permission to cut and remove trees or other vegetation from within the vicinity of distribution lines or transmission lines, including hazardous vegetation that increases fire risk, without requiring a separate timber sale if that cutting and removal is consistent with the applicable land management plan.\n##### (b) Use of proceeds\nA special use permit or easement that includes permission for the cutting and removal of trees or other vegetation described in subsection (a), shall include a requirement that, if the applicable electrical utility sells any portion of the material removed under the permit or easement, the electrical utility shall provide to the Secretary, acting through the Chief of the Forest Service, any proceeds received from the sale, less any transportation costs incurred in the sale.\n##### (c) Rule of construction\nNothing in this section shall be construed to require the sale of any material removed under a special use permit or easement that includes permission for the cutting and removal of trees or other vegetation described in subsection (a).\nIV\nREFORM OF CERTAIN ADMINISTRATIVE REQUIREMENTS\n#### 401. Nonapplicability of certain additional consultation requirements of the Endangered Species Act of 1973\n##### (a) Forest Service plans\nSection 6(d)(2) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1604(d)(2) ) is amended to read as follows:\n(2) No additional consultation required under certain circumstances Notwithstanding any other provision of law, the Secretary shall not be required to reinitiate consultation under section 7(a)(2) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(a)(2) ) or section 402.16 of title 50, Code of Federal Regulations (or a successor regulation), on a land management plan approved, amended, or revised under this section when\u2014 (A) a new species is listed or critical habitat is designated under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ); or (B) new information reveals effects of the land management plan that may affect a species listed or critical habitat designated under that Act in a manner or to an extent not previously considered. .\n##### (b) Bureau of Land Management plans\nSection 202 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1712 ) is amended by adding at the end the following:\n(g) Notwithstanding any other provision of law, the Secretary shall not be required to reinitiate consultation under section 7(a)(2) of the Endangered Species Act of 1973 ( 16 U.S.C. 1536(a)(2) ) or section 402.16 of title 50, Code of Federal Regulations (or a successor regulation), on a land use plan approved, amended, or revised under this section when\u2014 (1) a new species is listed or critical habitat is designated under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ); or (2) new information reveals effects of the land use plan that may affect a species listed or critical habitat designated under that Act in a manner or to an extent not previously considered. .\n#### 402. Amendment to categorical exclusion for collaborative restoration projects\nSection 603(c)(1) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591b(c)(1) ) is amended by striking 3000 acres and inserting 10,000 acres .",
      "versionDate": "2025-01-03",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7578",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TORCH Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-08",
        "text": "Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-433, Part I."
      },
      "number": "1110",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Grazing for Wildfire Risk Reduction Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-28",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "598",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FIR Act",
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
            "name": "Electric power generation and transmission",
            "updateDate": "2026-02-06T19:43:37Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-02-06T19:43:02Z"
          },
          {
            "name": "Fires",
            "updateDate": "2026-02-06T19:43:17Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-02-06T19:42:57Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-06T19:43:23Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-02-06T19:43:06Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-02-06T19:43:32Z"
          },
          {
            "name": "Livestock",
            "updateDate": "2026-02-06T19:43:28Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-02-06T19:43:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T18:51:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr168",
          "measure-number": "168",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-06-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr168v00",
            "update-date": "2025-06-06"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Targeted Operations to Remove Catastrophic Hazards Act or the TORCH Act</strong></p><p>This bill establishes requirements concerning forest management on federal land, including provisions to expedite the approval of forest management activities.</p><p>Specifically, it expands exclusions from environmental review requirements under the National Environmental Policy Act of 1969 for certain forest management activities, including by directing the Forest Service to develop a categorical exclusion for forest management activities that mitigate the risks associated with high-priority hazard trees. A categorical exclusion is a class of actions that a federal agency has determined do not significantly affect the quality of the human environment and, thus, do not require an environmental assessment nor an environmental impact statement.</p><p>The bill also exempts the Forest Service and the Bureau of Land Management from the requirement to reinitiate consultation with the Fish and Wildlife Service under the Endangered Species Act of 1973 on an approved, amended, or revised land management plan when (1) a new species is listed or critical habitat is designated, or (2) new information reveals that the land management plan may affect a listed species or critical habitat in a manner or to an extent not previously considered.</p><p>It also creates and modifies requirements related to vegetation management practices and forest management activities, such as activities to reduce wildfire risks. For example, the bill modifies the treatment of certain revenue under good neighbor agreements, which allow federal agencies to partner with state and local governments to carry out certain restoration services.</p>"
        },
        "title": "TORCH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr168.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Targeted Operations to Remove Catastrophic Hazards Act or the TORCH Act</strong></p><p>This bill establishes requirements concerning forest management on federal land, including provisions to expedite the approval of forest management activities.</p><p>Specifically, it expands exclusions from environmental review requirements under the National Environmental Policy Act of 1969 for certain forest management activities, including by directing the Forest Service to develop a categorical exclusion for forest management activities that mitigate the risks associated with high-priority hazard trees. A categorical exclusion is a class of actions that a federal agency has determined do not significantly affect the quality of the human environment and, thus, do not require an environmental assessment nor an environmental impact statement.</p><p>The bill also exempts the Forest Service and the Bureau of Land Management from the requirement to reinitiate consultation with the Fish and Wildlife Service under the Endangered Species Act of 1973 on an approved, amended, or revised land management plan when (1) a new species is listed or critical habitat is designated, or (2) new information reveals that the land management plan may affect a listed species or critical habitat in a manner or to an extent not previously considered.</p><p>It also creates and modifies requirements related to vegetation management practices and forest management activities, such as activities to reduce wildfire risks. For example, the bill modifies the treatment of certain revenue under good neighbor agreements, which allow federal agencies to partner with state and local governments to carry out certain restoration services.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119hr168"
    },
    "title": "TORCH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Targeted Operations to Remove Catastrophic Hazards Act or the TORCH Act</strong></p><p>This bill establishes requirements concerning forest management on federal land, including provisions to expedite the approval of forest management activities.</p><p>Specifically, it expands exclusions from environmental review requirements under the National Environmental Policy Act of 1969 for certain forest management activities, including by directing the Forest Service to develop a categorical exclusion for forest management activities that mitigate the risks associated with high-priority hazard trees. A categorical exclusion is a class of actions that a federal agency has determined do not significantly affect the quality of the human environment and, thus, do not require an environmental assessment nor an environmental impact statement.</p><p>The bill also exempts the Forest Service and the Bureau of Land Management from the requirement to reinitiate consultation with the Fish and Wildlife Service under the Endangered Species Act of 1973 on an approved, amended, or revised land management plan when (1) a new species is listed or critical habitat is designated, or (2) new information reveals that the land management plan may affect a listed species or critical habitat in a manner or to an extent not previously considered.</p><p>It also creates and modifies requirements related to vegetation management practices and forest management activities, such as activities to reduce wildfire risks. For example, the bill modifies the treatment of certain revenue under good neighbor agreements, which allow federal agencies to partner with state and local governments to carry out certain restoration services.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119hr168"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr168ih.xml"
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
      "title": "TORCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TORCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Targeted Operations to Remove Catastrophic Hazards Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve the ability of the Secretary of Agriculture and the Secretary of the Interior to carry out forest management actives that reduce the risk of catastrophic wildfires, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:52Z"
    }
  ]
}
```
