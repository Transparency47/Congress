# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8616?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8616
- Title: Caja del Rio Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 8616
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-19T05:08:48Z
- Update date including text: 2026-05-19T05:08:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8616",
    "number": "8616",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Caja del Rio Protection Act",
    "type": "HR",
    "updateDate": "2026-05-19T05:08:48Z",
    "updateDateIncludingText": "2026-05-19T05:08:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:07:45Z",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NM"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8616ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8616\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Ms. Leger Fernandez introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish the Caja del Rio Special Management Area and Caja del Rio National Conservation Area in the State of New Mexico, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Caja del Rio Protection Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Caja del Rio Special Management Area\nSec. 101. Establishment of the Caja del Rio Special Management Area.\nSec. 102. Management of the Special Management Area.\nTITLE II\u2014Caja del Rio National Conservation Area\nSec. 201. Establishment of the Caja del Rio National Conservation Area.\nSec. 202. Management of the Conservation Area.\nSec. 203. Land exchanges.\nTITLE III\u2014General Provisions\nSec. 301. Management of Covered Areas.\nSec. 302. Tribal contracting and protected rights.\nSec. 303. Effect.\n#### 2. Definitions\nIn this Act:\n**(1) Conservation Area**\nThe term Conservation Area means the Caja del Rio National Conservation Area established by section 201(a)(1).\n**(2) Covered area**\nThe term covered area means each of\u2014\n**(A)**\nthe Conservation Area; and\n**(B)**\nthe Special Management Area.\n**(3) Decommission**\nThe term decommission, with respect to a road, means\u2014\n**(A)**\nreestablishing native vegetation on the road;\n**(B)**\neffectively blocking the road to vehicular traffic, where feasible; and\n**(C)**\ndeveloping and implementing an effective monitoring and response plan for invasive species and vehicular traffic incursions.\n**(4) Ecological restoration**\nThe term ecological restoration has the meaning given the term restoration in section 4 of the Southwest Forest Health and Wildfire Prevention Act of 2004 ( 16 U.S.C. 6703 ).\n**(5) Indian land**\nThe term Indian land has the meaning given the term Indian lands in section 4 of the Indian Gaming Regulatory Act ( 25 U.S.C. 2703 ).\n**(6) Indian Tribe**\nThe term Indian Tribe means the governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation individually identified (including parenthetically) in the list published most recently as of the date of enactment of this Act pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ).\n**(7) Indigenous knowledge**\nThe term Indigenous knowledge has the meaning given the term in section 219.19 of title 36, Code of Federal Regulations (or a successor regulation).\n**(8) Interested indian tribe**\nThe term interested Indian Tribe , with respect to the covered area, means an Indian Tribe with\u2014\n**(A)**\nhistoric, precontact, cultural, or religious connections to the public land within the covered area;\n**(B)**\na former reservation located within the covered area; or\n**(C)**\ntreaty rights or other reserved rights associated with the covered area.\n**(9) Land grant-merced**\nThe term land grant-merced means a community land grant issued under the laws or customs of the Government of Spain or Mexico that\u2014\n**(A)**\nis recognized under New Mexico Statutes Chapter 49, Articles 1 and 4 (or a successor statute);\n**(B)**\nhas a record of traditional historic use in the covered area; or\n**(C)**\nhas a patented exterior boundary that is or was previously located on or adjacent to the covered area.\n**(10) Map**\nThe term Map means the map entitled The Caja del Rio Special management Area and National Conservation Area and dated April 20, 2026.\n**(11) Secretary**\nThe term Secretary means\u2014\n**(A)**\nin title I, the Secretary of Agriculture;\n**(B)**\nin title II, the Secretary of the Interior; and\n**(C)**\nin this section and title III\u2014\n**(i)**\nthe Secretary of the Interior, with respect to land under the jurisdiction of the Secretary of the Interior; and\n**(ii)**\nthe Secretary of Agriculture, with respect to land under the jurisdiction of the Secretary of Agriculture.\n**(12) Special management area**\nThe term Special Management Area means the Caja del Rio Special Management Area established by section 101(a)(1).\n**(13) State**\nThe term State means the State of New Mexico.\n**(14) Traditional historic community**\nThe term traditional historic community means a historic community that\u2014\n**(A)**\nmeets the definition of that term in New Mexico Statutes Section 3\u20137\u20131.1 (or a successor statute); and\n**(B)**\nhas a record of traditional historic use in the covered area.\n**(15) Traditional historic use**\nThe term traditional historic use means a habitual use conducted by a land grant-merced or traditional historic community within the covered area for noncommercial or personal benefit, including\u2014\n**(A)**\nhunting, fishing, grazing, wood gathering, pinon harvesting, or herb and plant gathering; or\n**(B)**\nany long-established and habitual and sustainable use by the land grant-merced or traditional historic community, as determined by the Secretary, in coordination with the land grant-merced or traditional historic community, that is agreed to in writing by the Secretary and the land grant-merced or traditional historic community.\n**(16) Tribal organization**\nThe term Tribal organization has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ), except that such organization shall be affiliated with an interested Indian Tribe.\n**(17) Withdrawal area**\nThe term withdrawal area means the area withdrawn by section 401.\nI\nCaja del Rio Special Management Area\n#### 101. Establishment of the Caja del Rio Special Management Area\n##### (a) Establishment\n**(1) In general**\nSubject to valid existing rights, there is established the Caja del Rio Special Management Area in the State.\n**(2) Land included**\nThe Special Management Area shall consist of approximately 67,163 acres of Federal land in the Santa Fe National Forest in the State as generally depicted as Caja del Rio Special Management Area on the Map.\n##### (b) Purposes\nThe purposes of the Special Management Area are\u2014\n**(1)**\nto conserve and permanently protect the cultural, spiritual, religious, scenic viewshed, ecological, wildlife habitat, natural, geological, historical, and traditional values of the Special Management Area; and\n**(2)**\nto enhance opportunities for interested Indian Tribes to engage in the preservation and management of the Special Management Area.\n#### 102. Management of the Special Management Area\n##### (a) In general\nThe Secretary shall manage the Special Management Area\u2014\n**(1)**\nsubject to valid existing rights;\n**(2)**\nin accordance with\u2014\n**(A)**\nthis Act;\n**(B)**\nthe Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1600 et seq. ); and\n**(C)**\nany other applicable laws; and\n**(3)**\nin a manner that conserves, protects, and enhances the resources of the Special Management Area.\n##### (b) Uses\nThe Secretary shall allow only uses of the Special Management Area that are consistent with\u2014\n**(1)**\nopportunities for cultural, spiritual, religious, medicinal, and traditional historic practices within the Special Management Area; and\n**(2)**\nthe purposes described in section 101(b).\n##### (c) Management plan\n**(1) Plan required**\nNot later than 3 years after the date of enactment of this Act, the Secretary shall develop a comprehensive management plan for the long-term management of the Special Management Area.\n**(2) Coordination and consultation**\nThe Secretary shall prepare and revise the management plan required under paragraph (1)\u2014\n**(A)**\nin coordination with\u2014\n**(i)**\nthe Secretary of the Interior, with respect to the development of a management plan for the Conservation Area and the withdrawal area, as described in section 202(c);\n**(ii)**\nthe Director of the National Park Service and the Director of the Bureau of Land Management, with respect to the administration, protection, and interpretation of the El Camino Real de Tierra Adentro National Historic Trail;\n**(iii)**\nthe State; and\n**(iv)**\napplicable units of local government, including any applicable land grant-mercedes or traditional historic communities; and\n**(B)**\nin consultation with interested Indian Tribes.\n**(3) Travel management**\n**(A) In general**\nThe Secretary shall include in the management plan required under paragraph (1) a travel management plan to decrease unauthorized road access and motorized use in the Special Management Area.\n**(B) Designation and maintenance of roads**\n**(i) In general**\nExcept as provided in clause (ii), only roads depicted on the Map shall be designated and maintained by the Secretary in the Special Management Area.\n**(ii) Additional roads**\nThe Secretary may designate roads in the Special Management Area in addition to the roads referred to in clause (i) if the Secretary determines the additional roads are necessary\u2014\n**(I)**\nto achieve the purposes described in section 101(b); or\n**(II)**\nnot more than 1 mile from the historic settlement area commonly known as Buckman , to accommodate critical water infrastructure or recreation access.\n**(4) Existing agreements**\nTo the maximum extent practicable, the Secretary shall incorporate into the management plan required under paragraph (1) stewardship agreements or contracts relating to the Federal land described in section 101(a)(2) that exist on the date of enactment of this Act.\n**(5) Cooperating agency**\nAt the request of an interested Indian Tribe, the Secretary shall include the interested Indian Tribe as a cooperating agency in the development and revision of the management plan required under paragraph (1).\n**(6) Indigenous knowledge**\nAt the request of an interested Indian Tribe, the Secretary shall ensure that Indigenous knowledge is incorporated into the development and revision of the management plan required under paragraph (1).\n##### (d) Maps and legal descriptions\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file maps and legal descriptions of the Special Management Area with\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) Force of law**\nThe maps and legal descriptions filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct errors in the maps and legal descriptions.\n**(3) Public availability**\nThe maps and legal descriptions filed under paragraph (1) shall be on file and available for public inspection in the appropriate offices of the Forest Service.\nII\nCaja del Rio National Conservation Area\n#### 201. Establishment of the Caja del Rio National Conservation Area\n##### (a) Establishment\n**(1) In general**\nSubject to valid existing rights, there is established the Caja del Rio National Conservation Area in the State.\n**(2) Land included**\nThe Conservation Area shall consist of approximately 17,837 acres of Bureau of Land Management land in the State as generally depicted as Caja del Rio-National Conservation Area on the Map.\n##### (b) Purposes\nThe purposes of the Conservation Area are\u2014\n**(1)**\nto conserve and permanently protect the cultural, spiritual, religious, scenic viewshed, ecological, wildlife habitat, natural, geological, historical, and traditional values of the Conservation Area; and\n**(2)**\nto enhance opportunities for interested Indian Tribes to engage in the preservation and management of the Conservation Area.\n#### 202. Management of the Conservation Area\n##### (a) In general\nThe Secretary shall manage the Conservation Area\u2014\n**(1)**\nsubject to valid and existing rights;\n**(2)**\nin accordance with\u2014\n**(A)**\nthis Act;\n**(B)**\nthe Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); and\n**(C)**\nany other applicable laws;\n**(3)**\nin a manner that conserves, protects, and enhances the resources of the Conservation Area; and\n**(4)**\nas a component of the National Landscape Conservation System.\n##### (b) Uses\nThe Secretary shall allow only uses of the Conservation Area that are consistent with\u2014\n**(1)**\nopportunities to undertake cultural, spiritual, religious, medicinal, or traditional historic use practices in the Conservation Area; and\n**(2)**\nthe purposes described in section 201(b).\n##### (c) Management plan\n**(1) Plan required**\nNot later than 3 years after the date of enactment of this Act, the Secretary shall develop a comprehensive management plan for the long-term management of the Conservation Area and the withdrawal area.\n**(2) Coordination and consultation**\nThe Secretary shall prepare and revise the management plan required under paragraph (1)\u2014\n**(A)**\nin coordination with\u2014\n**(i)**\nthe Secretary of Agriculture, with respect to the development of a management plan for the Special Management Area, as described in section 102(c);\n**(ii)**\nthe Director of the National Park Service and the Chief of the Forest Service, with respect to the administration, protection, and interpretation of the El Camino Real de Tierra Adentro National Historic Trail;\n**(iii)**\nthe State; and\n**(iv)**\napplicable units of local government, including any applicable land grant-mercedes or traditional historic communities; and\n**(B)**\nin consultation with interested Indian Tribes.\n**(3) Existing agreements**\nTo the maximum extent practicable, the Secretary shall incorporate into the management plan required under paragraph (1) stewardship agreements or contracts relating to the Federal land described in section 201(a)(2) that exist on the date of enactment of this Act.\n**(4) Cooperating agency**\nAt the request of an interested Indian Tribe, the Secretary shall include the interested Indian Tribe as a cooperating agency in the development and revision of the management plan required under paragraph (1).\n**(5) Indigenous knowledge**\nAt the request of an interested Indian Tribe, the Secretary shall ensure that Indigenous knowledge is incorporated into the development and revision of the management plan required under paragraph (1).\n##### (d) Travel management\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall prepare a travel management plan to decrease unauthorized road access and motorized use in the Conservation Area and the withdrawal area.\n**(2) Requirement**\nIn preparing the travel management plan under paragraph (1), the Secretary shall designate the use of motorized vehicles only on\u2014\n**(A)**\nthe road within the Conservation Area identified as CR 55C or Old Route 66 ; and\n**(B)**\nany roads in the Conservation Area and the withdrawal area that the Secretary determines to be necessary\u2014\n**(i)**\nto achieve the purposes described in section 201(b); and\n**(ii)**\nto allow for access to private property or critical infrastructure.\n##### (e) Maps and legal descriptions\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file maps and legal descriptions of the Conservation Area with\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) Force of law**\nThe maps and legal descriptions filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct errors in the maps and legal descriptions.\n**(3) Public availability**\nThe maps and legal descriptions filed under paragraph (1) shall be on file and available for public inspection in the appropriate offices of the Bureau of Land Management.\n#### 203. Land exchanges\n##### (a) In general\nSubject to subsections (c) through (f), the Secretary shall attempt to enter into an agreement to initiate an exchange under section 2201.1 of title 43, Code of Federal Regulations (or successor regulations), with the Commissioner of Public Lands of New Mexico, by the date that is 18 months after the date of enactment of this Act, to provide for a conveyance to the State of all right, title, and interest of the United States in and to the Bureau of Land Management land in the State identified under subsection (b) in exchange for the conveyance by the State to the Secretary of all right, title, and interest of the State in and to parcels of State trust land within the boundary of the Conservation Area described in section 201(a)(2) or the boundary of the withdrawal area described in section 401.\n##### (b) Identification of land for exchange\nThe Secretary and the Commissioner of Public Lands of New Mexico shall jointly identify the Bureau of Land Management land in the State and State trust land eligible for exchange under this section, the exact acreage and legal description of which shall be determined by surveys approved by the Secretary and the New Mexico State Land Office.\n##### (c) Applicable law\nA land exchange under subsection (a) shall be carried out in accordance with section 206 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1716 ).\n##### (d) Conditions\nA land exchange under subsection (a) shall be subject to\u2014\n**(1)**\nvalid existing rights; and\n**(2)**\nsuch terms as the Secretary and the State shall establish.\n##### (e) Valuation, appraisals, and equalization\n**(1) In general**\nThe value of the Bureau of Land Management land and the State trust land to be conveyed in a land exchange under this section\u2014\n**(A)**\nshall be equal, as determined by appraisals conducted in accordance with paragraph (2); or\n**(B)**\nif not equal, shall be equalized in accordance with paragraph (3).\n**(2) Appraisals**\n**(A) In general**\nThe Bureau of Land Management land and State trust land to be exchanged under this section shall be appraised by an independent, qualified appraiser that is agreed to by the Secretary and the State.\n**(B) Requirements**\nAn appraisal under subparagraph (A) shall be conducted in accordance with\u2014\n**(i)**\nthe Uniform Appraisal Standards for Federal Land Acquisitions; and\n**(ii)**\nthe Uniform Standards of Professional Appraisal Practice.\n**(3) Equalization**\n**(A) In general**\nIf the value of the Bureau of Land Management land and the State trust land to be conveyed in a land exchange under this section is not equal, the value may be equalized by\u2014\n**(i)**\nmaking a cash equalization payment to the Secretary or to the State, as appropriate, in accordance with section 206(b) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1716(b) ); or\n**(ii)**\nreducing the acreage of the Bureau of Land Management land or State trust land to be exchanged, as appropriate.\n**(B) Cash equalization payments**\nAny cash equalization payments received by the Secretary under subparagraph (A)(i) shall be\u2014\n**(i)**\ndeposited in the Federal Land Disposal Account established by section 206(a) of the Federal Land Transaction Facilitation Act ( 43 U.S.C. 2305(a) ); and\n**(ii)**\nused in accordance with that Act ( 43 U.S.C. 2301 et seq. ).\n##### (f) Limitation\nNo exchange of land shall be conducted under this section unless mutually agreed to by the Secretary and the State.\nIII\nGeneral Provisions\n#### 301. Management of Covered Areas\n##### (a) Road construction\n**(1) Permanent roads**\nNo new permanent road construction shall be permitted in a covered area unless otherwise designated under section 102(c)(3)(B) or 202(d)(2).\n**(2) Temporary roads**\nExcept as necessary for administrative purposes, the protection of health and safety, the control of fire, insects, or diseases, to facilitate cultural uses, or to provide reasonable access to private property, no temporary road construction shall be permitted in a covered area.\n**(3) Decommissioning of roads**\nNot later than 3 years after the date of enactment of this Act, the Secretary shall decommission any road in a covered area that has not been designated on the Map or in the applicable travel management plan for the covered area.\n##### (b) Motorized vehicles\n**(1) In general**\nExcept as provided in paragraph (2), the use of motorized vehicles in a covered area shall be permitted only on roads that are designated on the Map or in the applicable travel management plan for the covered area.\n**(2) Exceptions**\nThe use of motorized vehicles may be allowed in a covered area on roads not described in paragraph (1) if the use is necessary\u2014\n**(A)**\nfor administrative purposes;\n**(B)**\nto respond to an emergency;\n**(C)**\nfor Tribal religious or cultural practices; or\n**(D)**\nfor grazing in accordance with subsection (d).\n##### (c) Withdrawals\n**(1) In general**\nSubject to valid existing rights, all Federal land within a covered area, including any land or interest in land that is acquired by the United States within the covered area after the date of enactment of this Act, is withdrawn from\u2014\n**(A)**\nall forms of entry, appropriation, or disposal under public land laws, including the issuance of new rights-of-way on, under, or through the applicable Federal land;\n**(B)**\nlocation, entry, and patent under mining laws; and\n**(C)**\noperation of the mineral leasing, mineral materials, and geothermal leasing laws.\n**(2) Additional land**\nIf the Secretary acquires additional land within a covered area or the withdrawal area after the date of enactment of this Act, the acquired land is withdrawn from operation of the laws referred to in paragraph (1) on the date of acquisition of the land.\n##### (d) Grazing\nThe grazing of livestock in a covered area, as established before the date of enactment of this Act, shall be permitted to continue\u2014\n**(1)**\nsubject to such reasonable regulations, policies, and practices as the Secretary considers necessary;\n**(2)**\nin accordance with applicable law; and\n**(3)**\nin a manner consistent with the purposes of the applicable covered area described in section 101(b) or 201(b).\n##### (e) Wildfire, Insect, and Disease Management\nNothing in this Act prohibits the Secretary, in cooperation with other Federal, State, and local agencies, as appropriate, from conducting any measures necessary to control wildland fire, insects, and diseases in a covered area, consistent with the purposes of this Act.\n##### (f) Ecological restoration\n**(1) In general**\nEcological restoration in a covered area may be permitted\u2014\n**(A)**\nif necessary to protect, maintain, or enhance the applicable covered area (including the protection of traditional food or material gathering);\n**(B)**\nfor any purposes necessary to control wildland fire, insects, and diseases; and\n**(C)**\nto support the resilience of watersheds and wildlife habitat.\n**(2) Requirement**\nEcological restoration under paragraph (1) shall be carried out in a covered area\u2014\n**(A)**\nsubject to such reasonable regulations, policies, and practices as the Secretary considers necessary;\n**(B)**\nin a manner consistent with the purposes of the applicable covered area as described in section 101(b) or 201(b); and\n**(C)**\nin accordance with applicable law.\n##### (g) Acquisition of land\n**(1) In general**\nThe Secretary may acquire any land or interest in land within the boundary of a covered area or contiguous to a covered area, as depicted on the Map, by donation, purchase from a willing seller, or exchange.\n**(2) Incorporation of acquired land and interests in land**\nAny land or interest in land acquired under paragraph (1) shall\u2014\n**(A)**\nif the acquired land or interest in land is within the Santa Fe National Forest, become part of the Special Management Area; or\n**(B)**\nif the acquired land or interest in land is not located within the Santa Fe National Forest, become part of the Conservation Area.\n**(3) Withdrawal area**\nThe Secretary of the Interior may acquire any land or interest in land within the boundary of the withdrawal area, as depicted on the Map, by donation, purchase from a willing seller, or exchange.\n##### (h) Law enforcement\n**(1) In general**\nThe Secretary shall ensure adequate law enforcement presence in a covered area with respect to law enforcement matters under the jurisdiction of the Secretary to maintain the integrity of the covered area.\n**(2) No effect on jurisdiction**\nNothing in this Act limits or otherwise affects the civil or criminal regulatory jurisdiction, including law enforcement, for issues under the jurisdiction of an Indian Tribe.\n**(3) Penalties**\nIn developing a management plan for a covered area, the Secretary may consider provisions for increased penalties for unauthorized activities in the covered area, including littering, vandalism, damage to cultural sites, and unauthorized recreational shooting.\n##### (i) Notice of available routes and prohibited uses\nThe Secretary shall ensure that visitors to a covered area have access to adequate notice relating to designated routes, roads, and prohibited uses in the covered area through\u2014\n**(1)**\nthe placement of appropriate signage along designated routes, parking areas, trailheads, or any other highly visited area, including notice of penalties for prohibited uses; and\n**(2)**\nthe distribution of maps, safety education materials, and other information that the Secretary determines to be appropriate.\n#### 302. Tribal contracting and protected rights\n##### (a) Tribal contracting\n**(1) In general**\nThe Secretary may contract with 1 or more interested Indian Tribes or Tribal organizations to perform administrative or management functions within a covered area through\u2014\n**(A)**\ncontracts entered into under the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. );\n**(B)**\nagreements or contracts entered into under section 2 of the Tribal Forest Protection Act of 2004 ( 25 U.S.C. 3115a );\n**(C)**\nagreements or contracts for stewardship contracting projects entered into under section 604 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591c ); and\n**(D)**\nany other applicable authority.\n**(2) Tribal assistance**\nUsing any applicable authority, the Secretary may provide technical and financial assistance to an interested Indian Tribe to improve the capacity of the interested Indian Tribe to develop, enter into, and carry out activities under an agreement or contract entered into under paragraph (1).\n##### (b) Tribal cultural and religious uses\n**(1) In general**\nNothing in this Act diminishes any Tribal rights relating to access to a covered area for Tribal activities, including spiritual, cultural, medicinal, and traditional food gathering activities.\n**(2) Tribal uses and interests**\n**(A) Access and use**\nIn accordance with applicable law, the Secretary shall ensure access to a covered area by members of an interested Indian Tribe for traditional cultural and religious purposes.\n**(B) Temporary closure**\n**(i) In general**\nIn carrying out subparagraph (A), the Secretary, on request of an interested Indian Tribe, may temporarily close to the general public the use of 1 or more specific portions of a covered area to protect the privacy of cultural, religious, and food, medicinal, and materials gathering activities by members of the interested Indian Tribe.\n**(ii) Requirements**\n**(I) In general**\nAny closure under clause (i) shall be made so as to affect the smallest practicable area for the minimum period of time necessary.\n**(II) Access**\nAccess by members of an interested Indian Tribe to a portion of a covered area closed under clause (i) shall be consistent with the purpose and intent of Public Law 95\u2013341 (commonly known as the American Indian Religious Freedom Act ) ( 42 U.S.C. 1996 et seq. ) and other applicable law.\n##### (c) Federally secured rights\n**(1) Federally secured rights**\nNothing in this Act alters, modifies, enlarges, diminishes, or abrogates rights secured by treaty, statute, Executive order, or other Federal law of any interested Indian Tribe, including off-reservation reserved rights.\n**(2) Indian land**\nNothing in this Act affects any Indian land.\n**(3) Land claims**\nThe designation of a covered area does not affect any legitimate land claims to the covered area that were secured by treaty or an Act of Congress.\n##### (d) Plant and mineral gathering for cultural purposes\n**(1) In general**\nNotwithstanding section 2.6 of title 36, Code of Federal Regulations (or a successor regulation), the Secretary shall allow an enrolled member of any interested Indian Tribe that is culturally affiliated with the land located within the boundaries of a covered area or Bandelier National Monument to collect plants, including parts or products of plants, and mineral resources within the applicable covered area or Bandelier National Monument for noncommercial traditional and cultural uses.\n**(2) Application**\n**(A) In general**\nExcept as provided in subparagraph (B), a collection activity under paragraph (1) shall be\u2014\n**(i)**\nconsistent with applicable laws; and\n**(ii)**\nsubject to such conditions as the Secretary determines to be necessary to protect the resources and values of the applicable covered area or Bandelier National Monument.\n**(B) Quantity limitations**\n**(i) Existing regulations**\nNo quantity limitation contained in a regulation of the National Park Service, Forest Service, or Bureau of Land Management, as applicable, in effect on the date of enactment of this Act shall apply to a collection activity under paragraph (1).\n**(ii) Limitations imposed by the Secretary**\nThe Secretary may limit the quantity of plants, including parts or products of plants, and mineral resources collected under paragraph (1) if the Secretary determines that the limitation is necessary to protect the resources and values of the applicable covered area or Bandelier National Monument.\n#### 303. Effect\n##### (a) Treaty rights\nNothing in this Act affects the treaty rights of any Indian Tribe or land grant-merced.\n##### (b) Water rights\n**(1) In general**\nNothing in this Act\u2014\n**(A)**\nconstitutes an express or implied reservation by the United States of water or water rights for any purpose;\n**(B)**\nmodifies or otherwise affects any water rights existing on the date of enactment of this Act, including any water rights held by the United States;\n**(C)**\naffects an interstate water compact existing on the date of enactment of this Act; or\n**(D)**\nimposes any mandatory streamflow requirement or any Federal water quality standard within the covered land.\n**(2) State water law**\nThe Secretary shall follow the procedural and substantive requirements of applicable State law to obtain and hold any water rights not in existence on the date of enactment of this Act with respect to a covered area.\n##### (c) Drinking water infrastructure\n**(1) In general**\nNothing in this Act affects valid existing rights, including the existing rights-of-way of Santa Fe County, the city of Santa Fe, or the Buckman Direct Diversion Board in the State, to conduct necessary repair, operations, maintenance, replacement, or expansion of drinking water supply infrastructure.\n**(2) New permits or rights-of-way**\nThe Secretary may grant to Santa Fe County or the city of Santa Fe in the State new permits or rights-of-way to build water supply infrastructure not more than 1 mile from the historic settlement area commonly known as Buckman within the Special Management Area.\n**(3) Requirement**\nAny repair, operations, maintenance, replacement, expansion, or new construction of water supply infrastructure in a covered area shall be conducted in a manner that is consistent with the purposes of this Act.\n##### (d) Fish and wildlife\nNothing in this Act affects the jurisdiction of the State with respect to fish and wildlife located on public land in the State, except that the Secretary, after consultation with the New Mexico Department of Game and Fish, may designate zones where, and establish periods during which, hunting shall not be allowed within a covered area for reasons of public safety, administration, or public use and enjoyment.\n##### (e) Nondisclosure\n**(1) In general**\nThe Secretary shall not disclose to the public\u2014\n**(A)**\ninformation relating to the covered area that is derived from Indigenous knowledge that has not otherwise been released to the public as of the date of enactment of this Act; or\n**(B)**\ninformation relating to the nature or location of any sacred site in a covered area, if the Secretary determines, in consultation with the interested Indian Tribe, that such a disclosure may\u2014\n**(i)**\nrisk harm to the cultural resources of the sacred site;\n**(ii)**\ncause a significant invasion of privacy; or\n**(iii)**\nimpede the use of the sacred site for traditional cultural activities by an Indian Tribe or members of an Indian Tribe.\n**(2) Freedom of information act applicability**\n**(A) In general**\nInformation described in paragraph (1) shall be exempt from disclosure under section 552 of title 5, United States Code.\n**(B) Applicability**\nFor purposes of subparagraph (A), this subsection shall be considered a statute described in section 552(b)(3)(B) of title 5, United States Code.\nIV\nCaja del Rio Withdrawal Area\n#### 401. Withdrawal\nSubject to any valid existing rights, the Federal land and any interest in the Federal land depicted as Caja del Rio Withdrawal Area on the Map is withdrawn from\u2014\n**(1)**\nall forms of entry, appropriation, and disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\noperation of the mineral leasing, mineral materials, and geothermal leasing laws.",
      "versionDate": "2026-04-30",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8616ih.xml"
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
      "title": "Caja del Rio Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T05:08:48Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Caja del Rio Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T05:08:47Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Caja del Rio Special Management Area and Caja del Rio National Conservation Area in the State of New Mexico, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T05:03:27Z"
    }
  ]
}
```
