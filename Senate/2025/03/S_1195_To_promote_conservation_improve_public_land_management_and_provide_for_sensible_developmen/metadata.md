# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1195?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1195
- Title: Pershing County Economic Development and Conservation Act
- Congress: 119
- Bill type: S
- Bill number: 1195
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1195",
    "number": "1195",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Pershing County Economic Development and Conservation Act",
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
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T19:41:03Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:22Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1195is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1195\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Ms. Rosen introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo promote conservation, improve public land management, and provide for sensible development in Pershing County, Nevada, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Pershing County Economic Development and Conservation Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Checkerboard Land Resolution\nSec. 101. Findings.\nSec. 102. Sale or exchange of eligible land.\nSec. 103. Sale of encumbered land.\nSec. 104. Disposition of proceeds.\nTITLE II\u2014Wilderness Areas\nSec. 201. Additions to the National Wilderness Preservation System.\nSec. 202. Administration.\nSec. 203. Wildlife management.\nSec. 204. Release of wilderness study areas.\nSec. 205. Native American cultural and religious uses.\nTITLE III\u2014Tribal Trust Land\nSec. 301. Transfer of land to be held in trust for the Lovelock Paiute Tribe.\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) County**\nThe term County means Pershing County, Nevada.\n**(3) Eligible land**\nThe term eligible land means any land administered by the Director of the Bureau of Land Management\u2014\n**(A)**\nthat is within the area identified on the Map as Checkerboard Lands Resolution Area that is designated for disposal by the Secretary through\u2014\n**(i)**\nthe Winnemucca Consolidated Resource Management Plan; or\n**(ii)**\nany subsequent amendment or revision to the management plan that is undertaken with full public involvement;\n**(B)**\nthat is identified on the Map as Additional Lands Eligible for Disposal ; and\n**(C)**\nthat is not encumbered land.\n**(4) Encumbered land**\nThe term encumbered land means any land administered by the Director of the Bureau of Land Management within the area identified on the Map as Checkerboard Lands Resolution Area that is encumbered by mining claims, millsites, or tunnel sites.\n**(5) Map**\nThe term Map means the map entitled Pershing County Checkerboard Lands Resolution and dated July 8, 2024.\n**(6) Qualified entity**\nThe term qualified entity means, with respect to a portion of encumbered land\u2014\n**(A)**\nthe owner of a mining claim, millsite, or tunnel site located on a portion of the encumbered land on the date of enactment of this Act; and\n**(B)**\na successor in interest of an owner described in subparagraph (A).\n**(7) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(8) State**\nThe term State means the State of Nevada.\n**(9) Wilderness area**\nThe term wilderness area means a wilderness area designated by section 201(a).\nI\nCheckerboard Land Resolution\n#### 101. Findings\nCongress finds that\u2014\n**(1)**\nsince the passage of the Act of July 1, 1862 (12 Stat. 489, chapter 120) (commonly known as the Pacific Railway Act of 1862 ), under which railroad land grants along the Union Pacific Railroad right-of-way created a checkerboard land pattern of alternating public land and privately owned land, management of the land in the checkerboard area has been a constant source of frustration for the County government, private landholders in the County, and the Federal Government;\n**(2)**\nmanagement of Federal land in the checkerboard area has been costly and difficult for the Federal land management agencies, creating a disincentive to manage the land effectively;\n**(3)**\nparcels of land within the checkerboard area in the County will not vary significantly in appraised value by acre due to the similarity of highest and best use in the County; and\n**(4)**\nconsolidation of appropriate land within the checkerboard area through sales and exchanges for development and Federal management will\u2014\n**(A)**\nhelp improve the tax base of the County; and\n**(B)**\nsimplify management for the Federal Government.\n#### 102. Sale or exchange of eligible land\n##### (a) Authorization of conveyance\nNotwithstanding sections 202, 203 (other than subsection (b) of that section), 206 (other than subsections (d) and (f) of that section), and 209 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1712 , 1713, 1716, 1719), as soon as practicable after the date of enactment of this Act, the Secretary, in accordance with this Act and any other applicable law and subject to valid existing rights, shall conduct sales or exchanges of the eligible land as depicted on the Map.\n##### (b) Joint selection required\nAfter providing public notice, the Secretary and the County shall jointly select parcels of eligible land to be offered for sale or exchange under subsection (a).\n##### (c) Method of sale\nA sale of eligible land under subsection (a) shall be\u2014\n**(1)**\nconsistent with subsections (d) and (f) of section 203 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1713 );\n**(2)**\nconducted through a competitive bidding process, under which adjoining landowners are offered the first option, unless the Secretary determines there are suitable and qualified buyers that are not adjoining landowners; and\n**(3)**\nfor not less than fair market value, based on an appraisal in accordance with the Uniform Standards of Professional Appraisal Practice and this Act.\n##### (d) Land exchanges\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act and subject to the joint selection requirements under subsection (b), the Secretary shall offer to exchange all eligible land under this section for private land.\n**(2) Equal value exchange**\n**(A) In general**\nThe value of the eligible land and private land to be exchanged under paragraph (1)\u2014\n**(i)**\nshall be equal; or\n**(ii)**\nshall be made equal in accordance with subparagraph (B).\n**(B) Equalization**\n**(i) Surplus of eligible land**\nWith respect to the eligible land and private land to be exchanged under paragraph (1), if the value of the eligible land exceeds the value of the private land, the value of the eligible land and the private land shall be equalized by\u2014\n**(I)**\nthe owner of the private land making a cash equalization payment to the Secretary;\n**(II)**\nadding private land to the exchange; or\n**(III)**\nremoving eligible land from the exchange.\n**(ii) Surplus of private land**\nWith respect to the eligible land and private land to be exchanged under paragraph (1), if the value of the private land exceeds the value of the eligible land, the value of the private land and the eligible land shall be equalized by\u2014\n**(I)**\nthe Secretary making a cash equalization payment to the owner of the private land, in accordance with section 206(b) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1716(b) );\n**(II)**\nadding eligible land to the exchange; or\n**(III)**\nremoving private land from the exchange.\n**(3) Adjacent land**\nTo the extent practicable, the Secretary shall seek to enter into agreements with one or more owners of private land adjacent to the eligible land for the exchange of the private land for the eligible land, if the Secretary determines that the exchange would consolidate Federal land ownership and facilitate improved Federal land management.\n**(4) Priority land exchanges**\nIn acquiring private land under this subsection, the Secretary shall give priority to the acquisition of private land in higher-value natural resource areas in the County.\n##### (e) Mass appraisals\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, and every 5 years thereafter, the Secretary shall\u2014\n**(A)**\nconduct a mass appraisal of eligible land to be sold or exchanged under this section;\n**(B)**\nprepare an evaluation analysis for each land transaction under this section; and\n**(C)**\nmake available to the public the results of the mass appraisals conducted under subparagraph (A).\n**(2) Use**\nThe Secretary may use mass appraisals and evaluation analyses conducted under paragraph (1) to facilitate exchanges of eligible land for private land.\n**(3) Applicable law**\nAn appraisal under paragraph (1) shall be conducted in accordance with nationally recognized appraisal standards, including, as appropriate\u2014\n**(A)**\nthe Uniform Appraisal Standards for Federal Land Acquisitions; and\n**(B)**\nthe Uniform Standards of Professional Appraisal Practice.\n**(4) Duration**\nAn appraisal conducted under paragraph (1) shall remain valid for 5 years after the date on which the appraisal is approved by the Secretary.\n##### (f) Deadline for sale or exchange; exclusions\n**(1) Deadline**\nNot later than 90 days after the date on which the eligible land is jointly selected under subsection (b), the Secretary shall offer for sale or exchange the parcels of eligible land jointly selected under that subsection.\n**(2) Postponement or exclusion**\nThe Secretary or the County may postpone, or exclude from, a sale or exchange of all or a portion of the eligible land jointly selected under subsection (b) for emergency ecological or safety reasons.\n##### (g) Withdrawal\n**(1) In general**\nSubject to valid existing rights and mining claims, millsites, and tunnel sites, effective on the date on which a parcel of eligible land is jointly selected under subsection (b) for sale or exchange, that parcel is withdrawn from\u2014\n**(A)**\nall forms of entry and appropriation under the public land laws, including the mining laws;\n**(B)**\nlocation, entry, and patent under the mining laws; and\n**(C)**\noperation of the mineral leasing and geothermal leasing laws.\n**(2) Termination**\nThe withdrawal of a parcel of eligible land under paragraph (1) shall terminate\u2014\n**(A)**\non the date of sale or, in the case of exchange, the conveyance of title of the parcel of eligible land under this section; or\n**(B)**\nwith respect to any parcel of eligible land selected for sale or exchange under subsection (b) that is not sold or exchanged, not later than 2 years after the date on which the parcel was offered for sale or exchange under this section.\n##### (h) Maps and legal descriptions\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall finalize maps and legal descriptions of the parcels of eligible land to be sold or exchanged under this section.\n**(2) Availability**\nThe maps and legal descriptions finalized under paragraph (1) shall be on file and available for public inspection in appropriate offices of the Bureau of Land Management.\n**(3) Corrections**\nThe Secretary and the County may, by mutual agreement\u2014\n**(A)**\nmake minor boundary adjustments to the eligible land to be sold or exchanged under this section; and\n**(B)**\ncorrect any minor errors, including clerical and typographical errors, on the Map or any maps, acreage estimates, or legal descriptions finalized under this subsection.\n#### 103. Sale of encumbered land\n##### (a) Authorization of conveyance\nNotwithstanding sections 202, 203, 206, and 209 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1712 , 1713, 1716, 1719), not later than 90 days after the date of enactment of this Act and subject to valid existing rights held by third parties, the Secretary shall offer to convey to qualified entities, for fair market value, the remaining right, title, and interest of the United States, in and to the encumbered land as depicted on the Map.\n##### (b) Costs of sales to qualified entities\nAs a condition of each conveyance of encumbered land under this section, the qualified entity shall pay all costs related to the conveyance of the encumbered land, including the costs of surveys and other administrative costs associated with the conveyance.\n##### (c) Offer To convey\n**(1) In general**\nNot later than 180 days after the date on which the Secretary receives a fair market offer from a qualified entity for the conveyance of encumbered land, the Secretary shall accept the fair market value offer.\n**(2) Appraisal**\nFair market value of the interest of the United States in and to encumbered land shall be determined by an appraisal conducted in accordance with the Uniform Standards of Professional Appraisal Practice.\n##### (d) Conveyance\nNot later than 180 days after the date of acceptance by the Secretary of an offer from a qualified entity under subsection (c)(1) and completion of a sale for all or part of the applicable portion of encumbered land to the qualified entity, the Secretary, by delivery of an appropriate deed, patent, or other valid instrument of conveyance, shall convey to the qualified entity all remaining right, title, and interest of the United States in and to the applicable portion of the encumbered land.\n##### (e) Merger\nSubject to valid existing rights held by third parties, on delivery of the instrument of conveyance to the qualified entity under subsection (d), the prior interests in the locatable minerals and the right to use the surface for mineral purposes held by the qualified entity under a mining claim, millsite, tunnel site, or any other Federal land use authorization applicable to the encumbered land included in the instrument of conveyance, shall merge with all right, title, and interest conveyed to the qualified entity by the United States under this section to ensure that the qualified entity receives fee simple title to the purchased encumbered land.\n#### 104. Disposition of proceeds\n##### (a) Disposition of proceeds\nOf the proceeds from the sale of land under this title\u2014\n**(1)**\n5 percent shall be disbursed to the State for use in the general education program of the State;\n**(2)**\n10 percent shall be disbursed to the County for use as determined through normal County budgeting procedures; and\n**(3)**\nthe remainder shall be deposited in a special account in the Treasury of the United States, to be known as the Pershing County Special Account , which shall be available to the Secretary, in consultation with the County, for\u2014\n**(A)**\nthe acquisition of land from willing sellers (including interests in land) in the County\u2014\n**(i)**\nwithin a wilderness area;\n**(ii)**\nthat protects other environmentally significant land;\n**(iii)**\nthat secures public access to Federal land for hunting, fishing, and other recreational purposes; or\n**(iv)**\nthat improves management of Federal land within the area identified as Checkerboard Lands Resolution Area on the Map; and\n**(B)**\nthe reimbursement of costs incurred by the Secretary in preparing for the sale or exchange of land under this title.\n##### (b) Investment of special account\nAny amounts deposited in the special account established under subsection (a)(3)\u2014\n**(1)**\nshall earn interest in an amount determined by the Secretary of the Treasury, based on the current average market yield on outstanding marketable obligations of the United States of comparable maturities; and\n**(2)**\nmay be expended by the Secretary in accordance with this section.\n##### (c) Reports\n**(1) In general**\nNot later than September 30 of the fifth fiscal year after the date of enactment of this Act, and every 5 fiscal years thereafter, the Secretary shall submit to the State, the County, and the appropriate congressional committees a report on the operation of the special account established under subsection (a)(3) for the preceding 5 fiscal years.\n**(2) Contents**\nEach report submitted under paragraph (1) shall include, for the fiscal year covered by the report\u2014\n**(A)**\na statement of the amounts deposited into the special account;\n**(B)**\na description of the expenditures made from the special account for the fiscal year, including the purpose of the expenditures;\n**(C)**\nrecommendations for additional authorities to fulfill the purpose of the special account; and\n**(D)**\na statement of the balance remaining in the special account at the end of the fiscal year.\nII\nWilderness Areas\n#### 201. Additions to the National Wilderness Preservation System\n##### (a) Additions\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following parcels of Federal land in the State are designated as wilderness and as components of the National Wilderness Preservation System:\n**(1) Cain Mountain Wilderness addition**\nCertain Federal land managed by the Bureau of Land Management, comprising approximately 12,339 acres, as generally depicted on the map entitled Proposed Cain Mountain Wilderness and dated July 8, 2024, which is incorporated in, and considered to be a part of, the Cain Mountain Wilderness designated by sections 2905(b)(1)(C) and 2932(a)(1) of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ; 136 Stat. 3040; 136 Stat. 3048).\n**(2) Bluewing Wilderness**\nCertain Federal land managed by the Bureau of Land Management, comprising approximately 24,900 acres, as generally depicted on the map entitled Proposed Bluewing Wilderness and dated July 8, 2024, which shall be known as the Bluewing Wilderness .\n**(3) Selenite Peak Wilderness**\nCertain Federal land managed by the Bureau of Land Management, comprising approximately 22,822 acres, as generally depicted on the map entitled Proposed Selenite Peak Wilderness and dated July 8, 2024, which shall be known as the Selenite Peak Wilderness .\n**(4) Mount Limbo Wilderness**\nCertain Federal land managed by the Bureau of Land Management, comprising approximately 11,855 acres, as generally depicted on the map entitled Proposed Mt. Limbo Wilderness and dated July 8, 2024, which shall be known as the Mount Limbo Wilderness .\n**(5) North Sahwave Wilderness**\nCertain Federal land managed by the Bureau of Land Management, comprising approximately 13,875 acres, as generally depicted on the map entitled Proposed North Sahwave Wilderness and dated July 8, 2024, which shall be known as the North Sahwave Wilderness .\n**(6) Grandfathers Wilderness**\nCertain Federal land managed by the Bureau of Land Management, comprising approximately 35,339 acres, as generally depicted on the map entitled Proposed Grandfathers Wilderness and dated July 8, 2024, which shall be known as the Grandfathers Wilderness .\n**(7) Fencemaker Wilderness**\nCertain Federal land managed by the Bureau of Land Management, comprising approximately 14,942 acres, as generally depicted on the map entitled Proposed Fencemaker Wilderness and dated July 8, 2024, which shall be known as the Fencemaker Wilderness .\n##### (b) Boundary\nThe boundary of any portion of a wilderness area that is bordered by a road shall be 100 feet from the centerline of the road.\n##### (c) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and legal description of each wilderness area.\n**(2) Effect**\nEach map and legal description prepared under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the map or legal description.\n**(3) Availability**\nEach map and legal description prepared under paragraph (1) shall be on file and available for public inspection in the appropriate offices of the Bureau of Land Management.\n**(4) Withdrawal**\nSubject to valid existing rights, the wilderness areas designated by subsection (a) are withdrawn from\u2014\n**(A)**\nall forms of entry, appropriation, and disposal under the public land laws;\n**(B)**\nlocation, entry, and patent under the mining laws; and\n**(C)**\ndisposition under all laws relating to mineral and geothermal leasing or mineral materials.\n#### 202. Administration\n##### (a) Management\nSubject to valid existing rights, the wilderness areas shall be administered by the Secretary in accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), except that with respect to the wilderness areas\u2014\n**(1)**\nany reference in that Act to the effective date shall be considered to be a reference to the date of enactment of this Act; and\n**(2)**\nany reference in that Act to the Secretary of Agriculture shall be considered to be a reference to the Secretary.\n##### (b) Livestock\nThe grazing of livestock in the wilderness areas, if established before the date of enactment of this Act, shall be allowed to continue, subject to such reasonable regulations, policies, and practices as the Secretary considers to be necessary in accordance with\u2014\n**(1)**\nsection 4(d)(4) of the Wilderness Act ( 16 U.S.C. 1133(d)(4) ); and\n**(2)**\nthe guidelines set forth in Appendix A of the report of the Committee on Interior and Insular Affairs of the House of Representatives accompanying H.R. 2570 of the 101st Congress (House Report 101\u2013405).\n##### (c) Incorporation of acquired land and interests\nAny land or interest in land within the boundary of a wilderness area that is acquired by the United States after the date of enactment of this Act shall be added to and administered as part of the wilderness area.\n##### (d) Adjacent management\n**(1) In general**\nCongress does not intend for the designation of the wilderness areas to create protective perimeters or buffer zones around the wilderness areas.\n**(2) Nonwilderness activities**\nThe fact that nonwilderness activities or uses can be seen or heard from areas within a wilderness area shall not preclude the conduct of those activities or uses outside the boundary of the wilderness area.\n##### (e) Military overflights\nNothing in this title restricts or precludes\u2014\n**(1)**\nlow-level overflights of military aircraft over the wilderness areas, including military overflights that can be seen or heard within the wilderness areas;\n**(2)**\nflight testing and evaluation; or\n**(3)**\nthe designation or creation of new units of special use airspace, or the establishment of military flight training routes, over the wilderness areas.\n##### (f) Wildfire, insect, and disease management\nIn accordance with section 4(d)(1) of the Wilderness Act ( 16 U.S.C. 1133(d)(1) ), the Secretary may take such measures in the wilderness areas as are necessary for the control of fire, insects, and diseases (including, as the Secretary determines to be appropriate, the coordination of the activities with a State or local agency).\n##### (g) Climatological data collection\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ) and subject to such terms and conditions as the Secretary may prescribe, the Secretary may authorize the installation and maintenance of hydrologic, meteorologic, or climatological data collection devices in the wilderness areas if the Secretary determines that the facilities and access to the facilities are essential to flood warning, flood control, or water reservoir operation activities.\n##### (h) Water rights\n**(1) Findings**\nCongress finds that\u2014\n**(A)**\nthe wilderness areas are located\u2014\n**(i)**\nin the semiarid region of the Great Basin; and\n**(ii)**\nat the headwaters of the streams and rivers on land with respect to which there are few, if any\u2014\n**(I)**\nactual or proposed water resource facilities located upstream; and\n**(II)**\nopportunities for diversion, storage, or other uses of water occurring outside the land that would adversely affect the wilderness values of the land;\n**(B)**\nthe wilderness areas are generally not suitable for use or development of new water resource facilities; and\n**(C)**\nbecause of the unique nature of the wilderness areas, it is possible to provide for proper management and protection of the wilderness and other values of land in ways different from those used in other laws.\n**(2) Purpose**\nThe purpose of this section is to protect the wilderness values of the wilderness areas by means other than a federally reserved water right.\n**(3) Statutory construction**\nNothing in this title\u2014\n**(A)**\nconstitutes an express or implied reservation by the United States of any water or water rights with respect to the wilderness areas;\n**(B)**\naffects any water rights in the State (including any water rights held by the United States) in existence on the date of enactment of this Act;\n**(C)**\nestablishes a precedent with regard to any future wilderness designations;\n**(D)**\naffects the interpretation of, or any designation made under, any other Act; or\n**(E)**\nlimits, alters, modifies, or amends any interstate compact or equitable apportionment decree that apportions water among and between the State and other States.\n**(4) Nevada water law**\nThe Secretary shall follow the procedural and substantive requirements of State law in order to obtain and hold any water rights not in existence on the date of enactment of this Act with respect to the wilderness areas.\n**(5) New projects**\n**(A) Definition of water resource facility**\n**(i) In general**\nIn this paragraph, the term water resource facility means irrigation and pumping facilities, reservoirs, water conservation works, aqueducts, canals, ditches, pipelines, wells, hydropower projects, transmission and other ancillary facilities, and other water diversion, storage, and carriage structures.\n**(ii) Exclusion**\nIn this paragraph, the term water resource facility does not include wildlife guzzlers.\n**(B) Restriction on new water resource facilities**\nExcept as otherwise provided in this Act, on and after the date of enactment of this Act, neither the President nor any other officer, employee, or agent of the United States shall fund, assist, authorize, or issue a license or permit for the development of any new water resource facility within the wilderness areas.\n##### (i) Temporary telecommunications device\n**(1) In general**\nNothing in this title prevents the placement of a temporary telecommunications device for law enforcement or agency administrative purposes in the Selenite Peak Wilderness in accordance with paragraph (2).\n**(2) Additional requirements**\nAny temporary telecommunications device authorized by the Secretary under paragraph (1) shall\u2014\n**(A)**\nbe carried out in accordance with\u2014\n**(i)**\nthe Wilderness Act ( 16 U.S.C. 1131 et seq. ); and\n**(ii)**\nall other applicable laws (including regulations);\n**(B)**\nto the maximum practicable, be located in such a manner as to minimize impacts on the recreational and other wilderness values of the area; and\n**(C)**\nbe for a period of not longer than 7 years.\n#### 203. Wildlife management\n##### (a) In general\nIn accordance with section 4(d)(7) of the Wilderness Act ( 16 U.S.C. 1133(d)(7) ), nothing in this title affects or diminishes the jurisdiction of the State with respect to fish and wildlife management, including the regulation of hunting, fishing, and trapping, in the wilderness areas.\n##### (b) Management activities\nIn furtherance of the purposes and principles of the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the Secretary may conduct any management activities in the wilderness areas that are necessary to maintain or restore fish and wildlife populations and the habitats to support the populations, if the activities are carried out\u2014\n**(1)**\nconsistent with relevant wilderness management plans; and\n**(2)**\nin accordance with\u2014\n**(A)**\nthe Wilderness Act ( 16 U.S.C. 1131 et seq. ); and\n**(B)**\nappropriate policies, such as those set forth in Appendix B of the report of the Committee on Interior and Insular Affairs of the House of Representatives accompanying H.R. 2570 of the 101st Congress (House Report 101\u2013405), including noxious weed treatment and the occasional and temporary use of motorized vehicles if the use, as determined by the Secretary, would promote healthy, viable, and more naturally distributed wildlife populations that would enhance wilderness values with the minimal impact necessary to reasonably accomplish those tasks.\n##### (c) Existing activities\nIn accordance with section 4(d)(1) of the Wilderness Act ( 16 U.S.C. 1133(d)(1) ) and in accordance with appropriate policies such as those set forth in Appendix B of the Committee on Interior and Insular Affairs of the House of Representatives accompanying H.R. 2570 of the 101st Congress (House Report 101\u2013405), the State may continue to use aircraft, including helicopters, to survey, capture, transplant, monitor, and provide water for wildlife populations.\n##### (d) Wildlife water development projects\nSubject to subsection (f), the Secretary shall authorize structures and facilities, including existing structures and facilities, for wildlife water development projects, including guzzlers, in the wilderness areas if\u2014\n**(1)**\nthe structures and facilities will, as determined by the Secretary, enhance wilderness values by promoting healthy, viable, and more naturally distributed wildlife populations; and\n**(2)**\nthe visual impacts of the structures and facilities on the wilderness areas can reasonably be minimized.\n##### (e) Hunting, fishing, and trapping\n**(1) In general**\nThe Secretary may designate areas in which, and establish periods during which, for reasons of public safety, administration, or compliance with applicable laws, no hunting, fishing, or trapping will be permitted in the wilderness areas.\n**(2) Consultation**\nExcept in emergencies, the Secretary shall consult with the appropriate State agency and notify the public before taking any action under paragraph (1).\n##### (f) Cooperative agreement\nThe State, including a designee of the State, may conduct wildlife management activities in the wilderness areas\u2014\n**(1)**\nin accordance with the terms and conditions specified in the cooperative agreement between the Secretary and the State entitled Wildlife Management in Nevada BLM Wilderness Areas and signed September 2024, including any amendments to the cooperative agreement agreed to by the Secretary and the State; and\n**(2)**\nsubject to all applicable laws (including regulations).\n#### 204. Release of wilderness study areas\n##### (a) Finding\nCongress finds that, for the purposes of section 603(c) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1782(c) ), the approximately 48,600 acres of public land in the portions of the China Mountain, Mt. Limbo, Selenite Mountains, and Tobin Range wilderness study areas that have not been designated as wilderness by subsection (a) of section 201 and the portion of the Augusta Mountains wilderness study area within the County that has not been designated as wilderness by that subsection have been adequately studied for wilderness designation.\n##### (b) Release\nThe public land described in subsection (a)\u2014\n**(1)**\nis no longer subject to section 603(c) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1782(c) ); and\n**(2)**\nshall be managed in accordance with the applicable land use plans adopted under section 202 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1712 ).\n#### 205. Native American cultural and religious uses\n##### (a) In general\nNothing in this title alters or diminishes the treaty rights of any Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )).\n##### (b) Cultural uses\nNothing in this title precludes the traditional collection of pine nuts in a wilderness area for personal, noncommercial use consistent with the Wilderness Act ( 16 U.S.C. 1131 et seq. ).\nIII\nTribal Trust Land\n#### 301. Transfer of land to be held in trust for the Lovelock Paiute Tribe\n##### (a) In general\nSubject to valid existing rights, all right, title, and interest of the United States in and to the land described in subsection (b) shall be\u2014\n**(1)**\nheld in trust by the United States for the benefit of the Lovelock Paiute Tribe; and\n**(2)**\npart of the reservation of the Lovelock Paiute Tribe.\n##### (b) Description of land\nThe land referred to in subsection (a) is the approximately 10 acres of land administered by the Bureau of Land Management in the State, as depicted on the map prepared under subsection (d).\n##### (c) Survey\nNot later than 180 days after the date of enactment of this Act, the Secretary shall complete a survey to establish the boundaries of the land taken into trust under subsection (a).\n##### (d) Map\nAs soon as practicable after the date on which the Secretary completes the survey under subsection (c), the Secretary shall prepare a map that depicts the boundaries of the land established under that subsection.\n##### (e) Gaming prohibited\nThe land taken into trust under subsection (a) shall not be eligible, or considered to have been taken into trust, for class II gaming or class III gaming (as those terms are defined in section 4 of the Indian Gaming Regulatory Act ( 25 U.S.C. 2703 )).",
      "versionDate": "2025-03-27",
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
            "name": "Cemeteries and funerals",
            "updateDate": "2025-12-04T19:52:16Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-04T19:52:16Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2025-12-04T19:52:16Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-12-04T19:52:16Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-12-04T19:52:16Z"
          },
          {
            "name": "Nevada",
            "updateDate": "2025-12-04T19:52:16Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-12-04T19:52:16Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-12-04T19:52:16Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-12-04T19:52:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T21:10:30Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1195is.xml"
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
      "title": "Pershing County Economic Development and Conservation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pershing County Economic Development and Conservation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote conservation, improve public land management, and provide for sensible development in Pershing County, Nevada, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:22Z"
    }
  ]
}
```
