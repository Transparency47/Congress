# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1787?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1787
- Title: Dolores River National Conservation Area and Special Management Area Act
- Congress: 119
- Bill type: S
- Bill number: 1787
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2026-05-18T20:50:31Z
- Update date including text: 2026-05-18T20:50:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1787",
    "number": "1787",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Dolores River National Conservation Area and Special Management Area Act",
    "type": "S",
    "updateDate": "2026-05-18T20:50:31Z",
    "updateDateIncludingText": "2026-05-18T20:50:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
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
        "item": [
          {
            "date": "2025-12-17T14:30:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-15T18:47:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1787is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1787\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Bennet (for himself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo establish the Dolores River National Conservation Area and the Dolores River Special Management Area in the State of Colorado, to protect private water rights in the State, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Dolores River National Conservation Area and Special Management Area Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Dolores River National Conservation Area\nSec. 101. Establishment of Dolores River National Conservation Area.\nSec. 102. Management of Conservation Area.\nSec. 103. Dolores River National Conservation Area Advisory Council.\nTITLE II\u2014Dolores River Special Management Area\nSec. 201. Designation of Dolores River Special Management Area.\nSec. 202. Management of Special Management Area.\nTITLE III\u2014Technical modifications to potential additions to National Wild and Scenic Rivers System\nSec. 301. Purpose.\nSec. 302. Release of designated segments from Dolores River congressional study area.\nSec. 303. Applicability of continuing consideration provision.\nTITLE IV\u2014General provisions\nSec. 401. Management of covered land.\nSec. 402. Protection of water rights and other interests.\nSec. 403. Effect on private property and regulatory authority.\nSec. 404. Tribal rights and traditional uses.\n#### 2. Definitions\nIn this Act:\n**(1) Conservation Area**\nThe term Conservation Area means the Dolores River National Conservation Area established by section 101(a).\n**(2) Council**\nThe term Council means the Dolores River National Conservation Area Advisory Council established under section 103(a).\n**(3) Covered land**\nThe term covered land means\u2014\n**(A)**\nthe Conservation Area; and\n**(B)**\nthe Special Management Area.\n**(4) Dolores Project**\nThe term Dolores Project has the meaning given the term in section 3 of the Colorado Ute Indian Water Rights Settlement Act of 1988 ( Public Law 100\u2013585 ; 102 Stat. 2974).\n**(5) Map**\nThe term Map means the map prepared by the Bureau of Land Management entitled Proposed Dolores River National Conservation Area and Special Management Area and dated December 13, 2024.\n**(6) Secretary**\nThe term Secretary means\u2014\n**(A)**\nin title I, the Secretary of the Interior;\n**(B)**\nin title II, the Secretary of Agriculture; and\n**(C)**\nin title IV\u2014\n**(i)**\nthe Secretary of the Interior, with respect to land under the jurisdiction of the Secretary of the Interior; and\n**(ii)**\nthe Secretary of Agriculture, with respect to land under the jurisdiction of the Secretary of Agriculture.\n**(7) Special Management Area**\nThe term Special Management Area means the Dolores River Special Management Area established by section 201(a).\n**(8) State**\nThe term State means the State of Colorado.\n**(9) Unreasonably diminish**\nThe term unreasonably diminish has the same meaning as used in section 7(a) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1278(a) ).\n**(10) Water resource project**\nThe term water resource project means any dam, irrigation and pumping facility, reservoir, water conservation work, aqueduct, canal, ditch, pipeline, well, hydropower project, and transmission and other ancillary facility, and other water diversion, storage, and carriage structure.\nI\nDolores River National Conservation Area\n#### 101. Establishment of Dolores River National Conservation Area\n##### (a) Establishment\n**(1) In general**\nSubject to valid existing rights, there is established the Dolores River National Conservation Area in the State.\n**(2) Land included**\nThe Conservation Area shall consist of approximately 52,872 acres of Bureau of Land Management land in the State, as generally depicted as Proposed Lower Dolores River National Conservation Area on the Map.\n##### (b) Purpose\nThe purpose of the Conservation Area is to conserve, protect, and enhance the native fish, whitewater boating, recreational, hunting, fishing, scenic, cultural, archaeological, natural, geological, historical, ecological, watershed, wildlife, educational, and scientific resources of the Conservation Area.\n##### (c) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall prepare a map and legal description of the Conservation Area.\n**(2) Effect**\nThe map and legal description prepared under paragraph (1) shall have the same force and effect as if included in this title, except that the Secretary may correct minor errors in the map or legal description.\n**(3) Public availability**\nA copy of the map and legal description shall be on file and available for public inspection in the appropriate offices of the Bureau of Land Management.\n#### 102. Management of Conservation Area\n##### (a) In general\nThe Secretary shall manage the Conservation Area in accordance with\u2014\n**(1)**\nthis Act;\n**(2)**\nthe Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); and\n**(3)**\nother applicable laws.\n##### (b) Uses\nSubject to the provisions of this Act, the Secretary shall allow only such uses of the Conservation Area as are consistent with the purpose described in section 101(b).\n##### (c) Management plan\n**(1) Plan required**\n**(A) In general**\nNot later than 3 years after the date of enactment of this Act, the Secretary shall develop a management plan for the long-term protection, management, and monitoring of the Conservation Area.\n**(B) Review and revision**\nThe management plan under subparagraph (A) shall, from time to time, be subject to review and revision, in accordance with\u2014\n**(i)**\nthis Act;\n**(ii)**\nthe Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); and\n**(iii)**\nother applicable laws.\n**(2) Consultation and coordination**\nThe Secretary shall prepare and revise the management plan under paragraph (1)\u2014\n**(A)**\nin consultation with\u2014\n**(i)**\nthe State;\n**(ii)**\nunits of local government;\n**(iii)**\nthe public;\n**(iv)**\nthe Council; and\n**(v)**\nthe Native Fish Monitoring and Recommendation Team, as described in section 402(b)(1); and\n**(B)**\nin coordination with the Secretary of Agriculture, with respect to the development of the separate management plan for the Special Management Area, as described in section 202(c).\n**(3) Recommendations**\nIn preparing and revising the management plan under paragraph (1), the Secretary shall take into consideration any recommendations from the Council.\n**(4) Treaty rights**\nIn preparing and revising the management plan under paragraph (1), taking into consideration the rights and obligations described in section 402, the Secretary shall ensure that the management plan does not alter or diminish\u2014\n**(A)**\nthe treaty rights of any Indian Tribe;\n**(B)**\nany rights described in the Colorado Ute Indian Water Rights Settlement Act of 1988 ( Public Law 100\u2013585 ; 102 Stat. 2973); or\n**(C)**\nthe operation or purposes of the Dolores Project.\n##### (d) Incorporation of acquired land and interests\nAny land or interest in land located within the boundary of the Conservation Area that is acquired by the United States in accordance with section 401(c) after the date of enactment of this Act shall\u2014\n**(1)**\nbecome part of the Conservation Area; and\n**(2)**\nbe managed as provided in this section.\n##### (e) Department of Energy leases\n**(1) In general**\nNothing in this title affects valid leases or lease tracts existing on the date of enactment of this Act issued under the uranium leasing program of the Department of Energy.\n**(2) Management**\n**(A) In general**\nSubject to subparagraph (B), land designated for the program described in paragraph (1) shall be\u2014\n**(i)**\nexempt from section 401(b); and\n**(ii)**\nmanaged in a manner that allow the leases to fulfill the purposes of the program, consistent with the other provisions of this title and title IV.\n**(B) Designation**\nLand subject to a lease described in paragraph (1) shall be considered part of the Conservation Area and managed in accordance with other provisions of this title on a finding by the Secretary that\u2014\n**(i)**\n**(I)**\nthe lease has expired; and\n**(II)**\nthe applicable lease tract has been removed from the leasing program by the Secretary of Energy; and\n**(ii)**\nthe land that was subject to the lease is suitable for inclusion in the Conservation Area.\n**(C) Effect**\nNothing in subparagraph (B) prevents the Secretary of Energy from extending any lease described in paragraph (1).\n#### 103. Dolores River National Conservation Area Advisory Council\n##### (a) Establishment\nNot later than 1 year after the date of enactment of this Act, the Secretary shall establish an advisory council, to be known as the Dolores River National Conservation Area Advisory Council .\n##### (b) Duties\nThe Council shall advise\u2014\n**(1)**\nthe Secretary with respect to the preparation, implementation, and monitoring of the management plan prepared under section 102(c); and\n**(2)**\nthe Secretary of Agriculture with respect to the preparation, implementation, and monitoring of the management plan prepared under section 202(c).\n##### (c) Applicable law\nThe Council shall be subject to\u2014\n**(1)**\nchapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act );\n**(2)**\nthe Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); and\n**(3)**\nthis Act.\n##### (d) Membership\n**(1) In general**\nThe Council shall include 14 members to be appointed by the Secretary, of whom, to the extent practicable\u2014\n**(A)**\n2 members shall represent agricultural water user interests in the Conservation Area or the Dolores River watershed, of whom 1 shall represent the Dolores Water Conservancy District;\n**(B)**\n2 members shall represent conservation interests in the Conservation Area;\n**(C)**\n2 members shall represent recreation interests in the Conservation Area, 1 of whom shall represent whitewater boating interests;\n**(D)**\n1 member shall be a representative of Dolores County, Colorado;\n**(E)**\n1 member shall be a representative of San Miguel County, Colorado;\n**(F)**\n1 member shall be a representative of Montezuma County, Colorado;\n**(G)**\n1 member shall be a private landowner that owns land in immediate proximity to the Conservation Area;\n**(H)**\n1 member shall be a representative of Colorado Parks and Wildlife;\n**(I)**\n1 member shall be a holder of a grazing-allotment permit in the Conservation Area; and\n**(J)**\n2 members shall be representatives of Indian Tribes, 1 of whom shall be a representative of the Ute Mountain Ute Tribe.\n**(2) Representation**\n**(A) In general**\nThe Secretary shall ensure that the membership of the Council is fairly balanced in terms of the points of view represented and the functions to be performed by the Council.\n**(B) Requirements**\n**(i) In general**\nThe members of the Council described in subparagraphs (B) and (C) of paragraph (1) shall be residents that live within reasonable proximity to the Conservation Area.\n**(ii) County representatives**\nThe members of the Council described in subparagraphs (D) and (E) of paragraph (1) shall be\u2014\n**(I)**\nresidents of the respective counties referred to in those subparagraphs; and\n**(II)**\ncapable of representing the interests of the applicable board of county commissioners.\n##### (e) Terms of office\n**(1) In general**\nThe term of office of a member of the Council shall be 5 years.\n**(2) Reappointment**\nA member may be reappointed to the Council on completion of the term of office of the member.\n##### (f) Compensation\nA member of the Council\u2014\n**(1)**\nshall serve without compensation for service on the Council; but\n**(2)**\nmay be reimbursed for qualified expenses of the member.\n##### (g) Chairperson\nThe Council shall elect a chairperson from among the members of the Council.\n##### (h) Meetings\n**(1) In general**\nThe Council shall meet at the call of the chairperson\u2014\n**(A)**\nnot less frequently than quarterly until the management plan under section 102(c) is developed; and\n**(B)**\nthereafter, at the call of the Secretary.\n**(2) Public meetings**\nEach meeting of the Council shall be open to the public.\n**(3) Notice**\nA notice of each meeting of the Council shall be published in advance of the meeting.\n##### (i) Technical assistance\nThe Secretary shall provide, to the maximum extent practicable in accordance with applicable law, any information and technical services requested by the Council to assist in carrying out the duties of the Council.\n##### (j) Renewal\nThe Secretary shall ensure that the Council charter is renewed as required under applicable law.\n##### (k) Duration\nThe Council\u2014\n**(1)**\nshall continue to function for the duration of existence of the Conservation Area; but\n**(2)**\non completion of the management plan, shall only meet\u2014\n**(A)**\nat the call of the Secretary; or\n**(B)**\nin the case of a review or proposed revision to the management plan.\nII\nDolores River Special Management Area\n#### 201. Designation of Dolores River Special Management Area\n##### (a) Establishment\n**(1) In general**\nSubject to valid existing rights, there is established the Dolores River Special Management Area in the State.\n**(2) Land included**\nThe Special Management Area shall consist of approximately 15,452 acres of Federal land in the San Juan National Forest in the State, including National Forest System land in the Dolores River segment that extends from the Dolores Project boundary downstream to the boundary of the San Juan National Forest, as of the date of enactment of this Act, as generally depicted as Proposed Dolores River Special Management Area on the Map.\n##### (b) Purpose\nThe purpose of the Special Management Area is to conserve, protect, and enhance the native fish, whitewater boating, recreational, hunting, fishing, scenic, cultural, archaeological, natural, geological, historical, ecological, watershed, wildlife, educational, and scientific resources of the Special Management Area.\n##### (c) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and legal description of the Special Management Area with the Committee on Natural Resources of the House of Representatives and the Committee on Energy and Natural Resources of the Senate.\n**(2) Effect**\nThe map and legal description prepared under paragraph (1) shall have the same force and effect as if included in this title, except that the Secretary may correct minor errors in the map or legal description.\n**(3) Public availability**\nA copy of the map and legal description shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n#### 202. Management of Special Management Area\n##### (a) In general\nThe Secretary shall manage the Special Management Area in accordance with\u2014\n**(1)**\nthis Act;\n**(2)**\nthe National Forest Management Act of 1976 ( 16 U.S.C. 1600 et seq. ); and\n**(3)**\nother applicable laws.\n##### (b) Uses\nThe Secretary shall allow only such uses of the Special Management Area as the Secretary determines would further the purpose of the Special Management Area, as described in section 201(b).\n##### (c) Management plan\n**(1) Plan required**\n**(A) In general**\nNot later than 3 years after the date of enactment of this Act, the Secretary shall develop a management plan for the long-term protection, management, and monitoring of the Special Management Area.\n**(B) Review and revision**\nThe management plan under subparagraph (A) shall, from time to time, be subject to review and revision in accordance with\u2014\n**(i)**\nthis Act;\n**(ii)**\nthe National Forest Management Act of 1976 ( 16 U.S.C. 1600 et seq. ); and\n**(iii)**\nother applicable laws.\n**(2) Consultation and coordination**\nThe Secretary shall prepare and revise the management plan under paragraph (1)\u2014\n**(A)**\nin consultation with\u2014\n**(i)**\nthe State;\n**(ii)**\nunits of local government;\n**(iii)**\nthe public;\n**(iv)**\nthe Council; and\n**(v)**\nthe Native Fish Monitoring and Recommendation Team, as described in section 402(b)(1); and\n**(B)**\nin coordination with the Secretary of the Interior, with respect to the development of the separate management plan for the Conservation Area, as described in section 102(c).\n**(3) Recommendations**\nIn preparing and revising the management plan under paragraph (1), the Secretary shall take into consideration any recommendations from the Council.\n**(4) Treaty rights**\nIn preparing and revising the management plan under paragraph (1), taking into consideration the rights and obligations described in section 402, the Secretary shall ensure that the management plan does not alter or diminish\u2014\n**(A)**\nthe treaty rights of any Indian Tribe;\n**(B)**\nany rights described in the Colorado Ute Indian Water Rights Settlement Act of 1988 ( Public Law 100\u2013585 ; 102 Stat. 2973); or\n**(C)**\nthe operation or purposes of the Dolores Project.\n##### (d) Incorporation of acquired land and interests\nAny land or interest in land located within the boundary of the Special Management Area that is acquired by the United States in accordance with section 401(c) after the date of enactment of this Act shall\u2014\n**(1)**\nbecome part of the Special Management Area; and\n**(2)**\nbe managed as provided in this section.\nIII\nTechnical modifications to potential additions to National Wild and Scenic Rivers System\n#### 301. Purpose\nThe purpose of this title is to release portions of the Dolores River and certain tributaries from designation for potential addition under the Wild and Scenic Rivers Act ( 16 U.S.C. 1271 et seq. ) or from further study under that Act.\n#### 302. Release of designated segments from Dolores River congressional study area\nSection 5(a)(56) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1276(a)(56) ) is amended by inserting and the segments of the Dolores River located in the Dolores River National Conservation Area designated by the Dolores River National Conservation Area and Special Management Area Act before the period at the end.\n#### 303. Applicability of continuing consideration provision\nSection 5(d)(1) of the Wild and Scenic Rivers Act ( 16 U.S.C. 1276(d)(1) ) shall not apply to\u2014\n**(1)**\nthe Conservation Area; or\n**(2)**\nthe Special Management Area.\nIV\nGeneral provisions\n#### 401. Management of covered land\n##### (a) Motorized vehicles\n**(1) In general**\nExcept in cases in which motorized vehicles are needed for administrative purposes or to respond to an emergency, the use of motorized vehicles in the covered land shall be permitted only on designated routes.\n**(2) Road construction**\nExcept as necessary for administrative purposes, protection of public health and safety, or providing reasonable access to private property, the Secretary shall not construct any permanent or temporary road within the covered land after the date of enactment of this Act.\n##### (b) Withdrawals\nSubject to valid existing rights, all covered land, including any land or interest in land that is acquired by the United States within the covered land after the date of enactment of this Act, is withdrawn from\u2014\n**(1)**\nentry, appropriation or disposal under the public land laws;\n**(2)**\nlocation, entry, and patent under the mining laws; and\n**(3)**\noperation of the mineral leasing, mineral materials, and geothermal leasing laws, except as provided in section 102(e).\n##### (c) Willing sellers\nAny acquisition of land or interests in land under this Act shall be only by purchase from willing sellers, donation, or exchange.\n##### (d) Grazing\nThe Secretary shall issue and administer any grazing leases or permits and trailing permits and administer allotments in the covered land in accordance with the laws (including regulations) applicable to the issuance and administration of leases and permits on other land under the jurisdiction of the Bureau of Land Management or Forest Service, as applicable.\n##### (e) Access to private land\nTo ensure reasonable use and enjoyment of private property (whether in existence on the date of enactment of this Act or in an improved state), the Secretary shall grant reasonable and feasible access through the covered land to any private property that is located within or adjacent to the covered land, if other routes to the private property are blocked by physical barriers, such as the Dolores River or the cliffs of the Dolores River.\n##### (f) Easements\nThe Secretary may lease or acquire easements on private land from willing lessors, donors, or sellers for recreation, access, conservation, or other permitted uses, to the extent necessary to fulfill the purposes of the Conservation Area or Special Management Area, as applicable.\n##### (g) Wildfire, insect, and disease management\nThe Secretary may take any measures that the Secretary determines to be necessary to control fire, insects, and diseases in the covered land, (including, as the Secretary determines to be appropriate, the coordination of the measures with the State or a local agency).\n##### (h) Management of Ponderosa Gorge\n**(1) In general**\nThe Secretary shall manage the areas of the Conservation Area and Special Management Area identified on the Map as Ponderosa Gorge in a manner that maintains the wilderness character of those areas as of the date of enactment of this Act.\n**(2) Prohibited activities**\nSubject to paragraphs (3) and (4), in the areas described in paragraph (1), the following activities shall be prohibited:\n**(A)**\nNew permanent or temporary road construction or the renovation of nonsystem roads in existence on the date of enactment of this Act.\n**(B)**\nThe use of motor vehicles, motorized equipment, or mechanical transport, except as necessary to meet the minimum requirements for the administration of the Federal land, to protect public health and safety, or to conduct ecological restoration activities to improve the aquatic habitat of the Dolores River channel.\n**(C)**\nProjects undertaken for the purpose of harvesting commercial timber.\n**(3) Utility corridor**\nNothing in this subsection affects the operation, maintenance, or location of the utility right-of-way within the corridor, as depicted on the Map.\n**(4) Effect on certain vegetation management projects**\nNothing in this subsection\u2014\n**(A)**\naffects the implementation of the Lone Pine Vegetation Management Project authorized by the Forest Service in a decision notice dated January 23, 2020; or\n**(B)**\nprohibits activities relating to the harvest of merchantable products that are byproducts of activities conducted\u2014\n**(i)**\nfor ecological restoration; or\n**(ii)**\nto further the purposes of this Act.\n##### (i) Effect\nNothing in this Act prohibits the Secretary from issuing a new permit and right-of-way within the covered land for a width of not more than 150 feet for a right-of-way that serves a transmission line in existence on the date of enactment of this Act, on the condition that the Secretary shall relocate the right-of-way in a manner that furthers the purposes of this Act.\n##### (j) Climatological data collection\nSubject to such terms and conditions as the Secretary may require, nothing in this Act precludes the installation and maintenance of hydrologic, meteorological, or climatological collection devices in the covered land if the facilities and access to the facilities are essential to public safety, flood warning, flood control, water reservoir operation activities, or the collection of hydrologic data for water resource management purposes.\n#### 402. Protection of water rights and other interests\n##### (a) Dolores Project\n**(1) Operation**\nThe Dolores Project and the operation of McPhee Reservoir shall continue to be the responsibility of, and be operated by, the Secretary, in cooperation with the Dolores Water Conservancy District, in accordance with applicable laws and obligations.\n**(2) Effect**\nNothing in this Act affects the Dolores Project or the current or future operation of McPhee Reservoir in accordance with\u2014\n**(A)**\nthe reclamation laws;\n**(B)**\nany applicable\u2014\n**(i)**\nDolores Project water contract, storage contract, or carriage contract; or\n**(ii)**\nallocation of Dolores Project water;\n**(C)**\nthe environmental assessment and finding of no significant impact prepared by the Bureau of Reclamation Upper Colorado Region and approved August 2, 1996;\n**(D)**\nthe operating agreement entitled Operating Agreement, McPhee Dam and Reservoir, Contract No. 99-WC-40-R6100, Dolores Project, Colorado and dated April 25, 2000 (or any subsequent renewal or revision of that agreement);\n**(E)**\nmitigation measures for whitewater boating, including any such measure described in\u2014\n**(i)**\nthe document entitled Dolores Project Colorado Definite Plan Report and dated April 1977;\n**(ii)**\nthe Dolores Project final environmental statement dated May 9, 1977; or\n**(iii)**\na document referred to in subparagraph (C) or (D);\n**(F)**\napplicable Federal or State laws relating to the protection of the environment, including\u2014\n**(i)**\nthe Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. );\n**(ii)**\nthe National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ); and\n**(iii)**\nthe Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ); and\n**(G)**\nthe Colorado Ute Indian Water Rights Settlement Act of 1988 ( Public Law 100\u2013585 ; 102 Stat. 2973).\n##### (b) Management of flows\n**(1) In general**\nIn managing available flows below McPhee Dam to conserve, protect, and enhance the resources described in sections 101(b) and 201(b) of the Dolores River within the covered land, including native fish and whitewater boating resources, the Secretary shall seek to provide regular and meaningful consultation and collaboration with interested stakeholders, including the Native Fish Monitoring and Recommendation Team, which includes water management entities, affected counties, conservation interests, whitewater boating interests, Colorado Parks and Wildlife, and the Ute Mountain Ute Tribe, during the process of decision making.\n**(2) Annual report**\nBeginning on the date that is 1 year after the date of enactment of this Act and annually thereafter, the Commissioner of Reclamation shall prepare and make publically available a report that describes any progress with respect to the conservation, protection, and enhancement of native fish in the Dolores River.\n##### (c) Water resource projects\n**(1) In general**\nSubject to valid existing rights and paragraph (2), after the date of enactment of this Act, the Secretary or any other officer, employee, or agent of the United States may not assist by loan, grant, license, or otherwise in the construction or modification of any water resource project\u2014\n**(A)**\nlocated on the covered land that would\u2014\n**(i)**\naffect the free-flowing character of any stream within the covered land; or\n**(ii)**\nunreasonably diminish the resource values described in sections 101(b) and 201(b) of the Dolores River within the covered land; or\n**(B)**\nlocated outside the covered land that would unreasonably diminish the resource values described in sections 101(b) and 201(b) of the Dolores River within the covered land.\n**(2) Limitations**\nSubject to the requirements of this section, nothing in paragraph (1)\u2014\n**(A)**\nprevents, outside the covered land\u2014\n**(i)**\nthe construction of small diversion dams or stock ponds;\n**(ii)**\nnew minor water developments in accordance with existing decreed water rights; or\n**(iii)**\nminor modifications to structures; or\n**(B)**\naffects access to, or operation, maintenance, relicensing, repair, or replacement of, existing water resource projects.\n##### (d) Effect\nNothing in this Act\u2014\n**(1)**\naffects\u2014\n**(A)**\nany water right that is\u2014\n**(i)**\ndecreed under the laws of the State; and\n**(ii)**\nin existence on the date of enactment of this Act;\n**(B)**\nthe use, allocation, ownership, or control, in existence on the date of enactment of this Act, of any water or water right;\n**(C)**\nany vested absolute or decreed conditional water right in existence on the date of enactment of this Act, including any water right held by the United States;\n**(D)**\nany interstate water compact in existence on the date of enactment of this Act; or\n**(E)**\nState jurisdiction over any water law, water right, or adjudication or administration relating to any water resource;\n**(2)**\nimposes\u2014\n**(A)**\nany mandatory streamflow requirement within the covered land; or\n**(B)**\nany Federal water quality standard within, or upstream of, the covered land that is more restrictive than would be applicable if the covered land had not been designated as the Conservation Area or Special Management Area under this Act; or\n**(3)**\nconstitutes an express or implied reservation by the United States of any reserved or appropriative water right within the covered land.\n#### 403. Effect on private property and regulatory authority\n##### (a) Effect\nNothing in this Act\u2014\n**(1)**\naffects valid existing rights;\n**(2)**\nrequires any owner of private property to bear any costs associated with the implementation of the management plan under this Act;\n**(3)**\naffects the jurisdiction or responsibility of the State with respect to fish and wildlife in the State;\n**(4)**\nrequires a change in or affects local zoning laws of the State or a political subdivision of the State; or\n**(5)**\naffects\u2014\n**(A)**\nthe jurisdiction over, use, or maintenance of county roads in the covered land; or\n**(B)**\nthe administration of the portion of the road that is not a county road and that is commonly known as the Dolores River Road within the Conservation Area, subject to the condition that the Secretary shall not improve the road beyond the existing primitive condition of the road.\n##### (b) Adjacent management\n**(1) No buffer zones**\nThe designation of the Conservation Area and the Special Management Area by this Act shall not create any protective perimeter or buffer zone around the Conservation Area or Special Management Area, as applicable.\n**(2) Private land**\nNothing in this Act requires the prohibition of any activity on private land outside the boundaries of the Conservation Area or the Special Management Area that can be seen or heard from within such a boundary.\n#### 404. Tribal rights and traditional uses\n##### (a) Treaty rights\nNothing in this Act affects the treaty rights of any Indian Tribe, including rights under the Agreement of September 13, 1873, ratified by the Act of April 29, 1874 (18 Stat. 36, chapter 136).\n##### (b) Traditional tribal uses\nSubject to any terms and conditions as the Secretary determines to be necessary and in accordance with applicable law, the Secretary shall allow for the continued use of the covered land by members of Indian Tribes\u2014\n**(1)**\nfor traditional ceremonies; and\n**(2)**\nas a source of traditional plants and other materials.",
      "versionDate": "2025-05-15",
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
            "name": "Advisory bodies",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Colorado",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Dams and canals",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Livestock",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Watersheds",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2026-01-07T19:44:30Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-01-07T19:44:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-18T15:14:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
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
          "measure-id": "id119s1787",
          "measure-number": "1787",
          "measure-type": "s",
          "orig-publish-date": "2025-05-15",
          "originChamber": "SENATE",
          "update-date": "2026-02-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1787v00",
            "update-date": "2026-02-11"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Dolores River National Conservation Area and Special Management Area Act</strong></p><p>This bill establishes the Dolores River National Conservation Area and the Dolores River Special Management Area in Colorado to protect certain natural, recreational, scenic, cultural, historical, and other values of the areas.</p><p>The conservation area must\u00a0consist of approximately 52,872 acres of Bureau of Land Management land. The special management area must consist of\u00a0approximately 15,452 acres of federal land in the San Juan National Forest.</p><p>A management plan must be developed for each area. The\u00a0bill directs the Department of the Interior to allow for the continued use of the areas by members of Indian tribes for traditional ceremonies and as a source of traditional plants and other materials.</p><p>Additionally, Interior must manage the\u00a0portions of the\u00a0areas identified as Ponderosa Gorge in a manner that maintains its wilderness character, including by prohibiting (1) road construction; (2) the use of motor vehicles, motorized equipment, or mechanical transport; and (3) projects undertaken for the purpose of harvesting commercial timber.</p><p>Interior must also establish the Dolores River National Conservation Area Advisory Council.</p><p>Finally, the bill releases segments of the Dolores River inside the areas from further study for potential addition to the Wild and Scenic Rivers System.</p>"
        },
        "title": "Dolores River National Conservation Area and Special Management Area Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1787.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dolores River National Conservation Area and Special Management Area Act</strong></p><p>This bill establishes the Dolores River National Conservation Area and the Dolores River Special Management Area in Colorado to protect certain natural, recreational, scenic, cultural, historical, and other values of the areas.</p><p>The conservation area must\u00a0consist of approximately 52,872 acres of Bureau of Land Management land. The special management area must consist of\u00a0approximately 15,452 acres of federal land in the San Juan National Forest.</p><p>A management plan must be developed for each area. The\u00a0bill directs the Department of the Interior to allow for the continued use of the areas by members of Indian tribes for traditional ceremonies and as a source of traditional plants and other materials.</p><p>Additionally, Interior must manage the\u00a0portions of the\u00a0areas identified as Ponderosa Gorge in a manner that maintains its wilderness character, including by prohibiting (1) road construction; (2) the use of motor vehicles, motorized equipment, or mechanical transport; and (3) projects undertaken for the purpose of harvesting commercial timber.</p><p>Interior must also establish the Dolores River National Conservation Area Advisory Council.</p><p>Finally, the bill releases segments of the Dolores River inside the areas from further study for potential addition to the Wild and Scenic Rivers System.</p>",
      "updateDate": "2026-02-11",
      "versionCode": "id119s1787"
    },
    "title": "Dolores River National Conservation Area and Special Management Area Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Dolores River National Conservation Area and Special Management Area Act</strong></p><p>This bill establishes the Dolores River National Conservation Area and the Dolores River Special Management Area in Colorado to protect certain natural, recreational, scenic, cultural, historical, and other values of the areas.</p><p>The conservation area must\u00a0consist of approximately 52,872 acres of Bureau of Land Management land. The special management area must consist of\u00a0approximately 15,452 acres of federal land in the San Juan National Forest.</p><p>A management plan must be developed for each area. The\u00a0bill directs the Department of the Interior to allow for the continued use of the areas by members of Indian tribes for traditional ceremonies and as a source of traditional plants and other materials.</p><p>Additionally, Interior must manage the\u00a0portions of the\u00a0areas identified as Ponderosa Gorge in a manner that maintains its wilderness character, including by prohibiting (1) road construction; (2) the use of motor vehicles, motorized equipment, or mechanical transport; and (3) projects undertaken for the purpose of harvesting commercial timber.</p><p>Interior must also establish the Dolores River National Conservation Area Advisory Council.</p><p>Finally, the bill releases segments of the Dolores River inside the areas from further study for potential addition to the Wild and Scenic Rivers System.</p>",
      "updateDate": "2026-02-11",
      "versionCode": "id119s1787"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1787is.xml"
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
      "title": "Dolores River National Conservation Area and Special Management Area Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dolores River National Conservation Area and Special Management Area Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Dolores River National Conservation Area and the Dolores River Special Management Area in the State of Colorado, to protect private water rights in the State, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:25Z"
    }
  ]
}
```
