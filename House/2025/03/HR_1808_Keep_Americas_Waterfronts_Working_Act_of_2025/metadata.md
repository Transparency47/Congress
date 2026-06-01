# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1808?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1808
- Title: Keep America’s Waterfronts Working Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1808
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-04-21T08:05:40Z
- Update date including text: 2026-04-21T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1808",
    "number": "1808",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "P000597",
        "district": "1",
        "firstName": "Chellie",
        "fullName": "Rep. Pingree, Chellie [D-ME-1]",
        "lastName": "Pingree",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "Keep America\u2019s Waterfronts Working Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-21T08:05:40Z",
    "updateDateIncludingText": "2026-04-21T08:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:00:40Z",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "VA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "ME"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "RI"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "HI"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "LA"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "RI"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "OR"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NJ"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "GU"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1808ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1808\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Ms. Pingree (for herself, Mr. Wittman , Mr. Golden of Maine , Mr. Peters , Mr. Tonko , Mr. Carbajal , Mr. Magaziner , Ms. Tokuda , Ms. Brown , Mr. Carter of Louisiana , and Mr. Amo ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Coastal Zone Management Act of 1972 to establish a working waterfronts Task Force and working waterfronts grant and loan programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keep America\u2019s Waterfronts Working Act of 2025 .\n#### 2. Working waterfronts\nThe Coastal Zone Management Act of 1972 ( 16 U.S.C. 1451 et seq. ) is amended by inserting after section 306A ( 16 U.S.C. 1455a ) the following:\n306B. Working waterfronts (a) Task Force (1) In general The Secretary shall establish a task force to work directly with covered entities, users of working waterfronts, and coastal stakeholders to identify and address critical needs with respect to working waterfronts. (2) Membership The Secretary shall appoint members of the Task Force, and shall include\u2014 (A) experts in the unique economic, social, cultural, ecological, geographic, and resource concerns of working waterfronts; and (B) representatives from\u2014 (i) the Office of Coastal Management of the National Oceanic and Atmospheric Administration; (ii) the United States Fish and Wildlife Service; (iii) the Department of Agriculture; (iv) the Environmental Protection Agency; (v) the United States Geological Survey; (vi) the Department of the Navy; (vii) the National Marine Fisheries Service; (viii) the Economic Development Administration; (ix) such other Federal agencies as the Secretary determines appropriate; (x) Indian Tribes; and (xi) Native Hawaiian organizations. (3) Functions The Task Force shall\u2014 (A) identify and prioritize critical needs with respect to working waterfronts in coastal states that have a management program approved under section 306, in the areas of\u2014 (i) economic and cultural importance of such working waterfronts to communities; (ii) changing circumstances and threats such working waterfronts face from trade barriers and environmental changes, including sea level rise, extreme weather events, ocean acidification, and harmful algal blooms; and (iii) identifying such working waterfronts and highlighting them within communities; (B) outline options, in consultation with coastal states and coastal stakeholders, to address each critical need identified under subparagraph (A), including adaptation and mitigation options where applicable; (C) identify which Federal agency is responsible for addressing each critical need identified under subparagraph (A); and (D) recommend which Federal agency is best suited to address each critical need identified under subparagraph (A) for which no responsible Federal agency is identified under subparagraph (C). (4) Report Not later than 18 months after the date of the enactment of this section, the Task Force shall submit to Congress a report regarding the findings of the Task Force under this subsection. (5) Implementation Not later than 30 months after the date of the enactment of this section, the head of each Federal agency identified under paragraph (3)(C) shall, to the extent practicable and subject to the availability of appropriations, implement the options outlined under paragraph (3)(B). (b) Working waterfronts plan (1) In general A covered entity may submit to the Secretary a working waterfronts plan for approval under this subsection, which, as applicable and with respect to the covered entity\u2014 (A) shall\u2014 (i) provide for the preservation and expansion of access to coastal waters by coastal users; (ii) be complementary to and incorporate the policies, objectives, and regulations of regional and local working waterfronts plans or strategies in effect before the date of the enactment of this section; (iii) be developed through a process that\u2014 (I) ensures the involvement of coastal stakeholders; and (II) is consistent with other coastal management programs, regulations, and activities of the covered entity; (iv) designate each qualified holder of the covered entity, if any; (v) if the covered entity designates a qualified holder under clause (iv)\u2014 (I) ensure that such qualified holder complies with the duty of a qualified holder to enforce each working waterfront covenant to which the qualified holder is a party; and (II) certify that the covered entity retains the responsibility to ensure that each affected working waterfront is managed in a manner that is consistent with the working waterfronts plan of the covered entity; and (vi) include\u2014 (I) an assessment of the economic, social, cultural, and historical value of working waterfronts; (II) a description of any relevant non-Federal laws and regulations that affect working waterfronts in the geographic areas identified under subclauses (III) and (IV); (III) an identification of geographic areas where working waterfronts are, as of the date of the enactment of this subsection, under threat of conversion to uses incompatible with commercial and recreational fishing, recreational fishing and boating businesses, aquaculture, boatbuilding, or other water-dependent, coastal-related business, and the level of that threat; (IV) an identification of geographic areas with a historical connection to working waterfronts where working waterfronts are not, as of the date of the enactment of this section, available, and, where appropriate, an assessment of the environmental impacts of any expansion or new development of working waterfronts on the coastal ecosystems of such geographic areas; (V) an identification of additional working waterfronts needs, including improvements to existing working waterfronts; (VI) a strategic and prioritized plan for the preservation, expansion, and improvement of each relevant working waterfront; (VII) for geographic areas identified under subclauses (III) and (IV), an identification of the current availability and potential for expansion of public access to coastal waters in such geographic areas; (VIII) a description of the degree of community support for the plan included under subclause (VI); and (IX) a contingency plan for any property that reverts to the covered entity pursuant to a determination made by the covered entity under subsection (c)(11)(B); and (B) may\u2014 (i) be developed using existing information contained in relevant surveys, plans, or other documents to fulfill the information requirements under this paragraph; (ii) include a vulnerability assessment, hazards resilience plan, or identification of waterfront properties exposed to sea level rise or inundation; and (iii) be part of a management program approved under section 306. (2) Duration of approval (A) In general A working waterfronts plan approved by the Secretary under this subsection shall be effective during the 5-year period beginning on the date of such approval. (B) Maintenance of approval An eligible covered entity that participates in the grant program on the basis of an approved working waterfronts plan of that eligible covered entity shall resubmit such working waterfronts plan for approval by the Secretary before the end of each 5-year period described in subparagraph (A). (c) Working Waterfronts Grant Program (1) In general The Secretary shall, in consultation with covered entities, Federal agencies the Secretary determines appropriate, and interested coastal stakeholders with expertise in working waterfronts planning, establish a regionally equitable and competitive grant program, to be known as the Working Waterfronts Grant Program . (2) Uses The Secretary may award grants under this subsection to eligible covered entities\u2014 (A) to implement or revise an approved working waterfronts plan of such eligible covered entity, including\u2014 (i) acquiring a working waterfront or an interest in a working waterfront; (ii) making improvements to a working waterfront, including constructing or repairing wharfs, boat ramps, or related facilities; or (iii) carrying out necessary climate adaptation mitigation activities for a working waterfront; or (B) to develop a working waterfronts plan of such eligible covered entity under subsection (b). (3) Application (A) In general To be eligible for a grant under this subsection, an eligible covered entity shall submit an application to the Secretary\u2014 (i) that, if applicable, is consistent with the management program of the eligible covered entity approved under section 306; and (ii) in such form, at such time, and containing such information as the Secretary determines appropriate. (B) Deadline Not later than 60 days after the date on which the Secretary receives an application for a grant under this paragraph, the Secretary shall approve or reject such application. (4) Guidelines The Secretary shall, in consultation with the entities described in paragraph (1), issue guidelines regarding the implementation of the grant program. (5) Criteria In awarding a grant to an eligible covered entity, the Secretary shall take into account the following criteria: (A) The economic, cultural, and historical significance of working waterfronts to the eligible covered entity. (B) The demonstrated working waterfronts needs of the eligible covered entity, as described in the approved working waterfronts plan of the eligible covered entity, if any. (C) The ability of the eligible covered entity to meet the matching requirement under paragraph (10). (D) The potential for rapid turnover in the ownership of relevant working waterfronts, and, if applicable, the need for the eligible covered entity to respond quickly when property in an existing or potential working waterfront area or public access area, as identified in the approved working waterfronts plan of the eligible covered entity, if any, comes under threat of conversion to incompatible uses or becomes available for purchase. (E) As applicable, the impact of the approved working waterfronts plan of the eligible covered entity, if any, on the coastal ecosystem and working waterfronts of the eligible covered entity and the users of the coastal ecosystem of the eligible covered entity. (6) Other technical and financial assistance (A) In general Upon the request of an eligible covered entity that is awarded a grant under this subsection, the Secretary shall provide to such eligible covered entity technical assistance\u2014 (i) to identify and obtain sources of Federal technical or financial assistance other than that provided under this subsection to develop a working waterfronts plan for approval under subsection (b) or to implement or revise an approved working waterfronts plan; (ii) to develop a working waterfronts plan for approval under subsection (b); (iii) to implement or revise an approved working waterfronts plan; (iv) to integrate resilience planning into working waterfronts preservation efforts of such eligible covered entity; (v) to develop additional tools to protect working waterfronts; (vi) regarding guidance for best storm water management practices with regard to working waterfronts; or (vii) to collect and disseminate best practices regarding working waterfronts and resilience planning. (B) Limitation The Secretary may use not more than 5 percent of the amounts made available under this subsection in each fiscal year to provide technical assistance under this paragraph. (7) Public access requirement A project carried out with a grant awarded under this subsection, other than a project that involves commercial fishing or other industrial access points to which the eligible covered entity determines public access would be unsafe, shall provide for the expansion, improvement, or preservation of reasonable and appropriate public access to coastal waters at or in the vicinity of working waterfronts. (8) Limitation on acquisition An eligible covered entity that is awarded a grant under this subsection, or any entity to which such eligible covered entity allocates a portion of such grant under paragraph (9), may use such grant award to acquire title to or an interest in a working waterfront, including an easement, only\u2014 (A) for fair market value from a willing seller; or (B) for less than fair market value from a seller that certifies to the Secretary that the seller is willing and is not subject to coercion. (9) Allocation (A) In general An eligible covered entity that is awarded a grant under this subsection may allocate a portion of such grant award to a unit of State or local government, a nonprofit organization, a fishing cooperative, or any other appropriate entity for the purpose of carrying out this subsection if such eligible covered entity ensures that any such allocated grant award is used consistently with this subsection. (B) Identified working waterfronts The Secretary shall encourage each eligible covered entity that is awarded a grant under this subsection to equitably allocate such grant award among working waterfronts identified in the approved working waterfronts plan of each such eligible covered entity, if any. (10) Matching requirement (A) In general Except as provided in subparagraph (B), the Federal share of a project carried out with a grant awarded under this subsection may not exceed 75 percent. (B) Waiver of matching requirement The Secretary may waive the application of subparagraph (A)\u2014 (i) with respect to an eligible covered entity that is awarded a grant under this subsection that has designated a qualified holder that is located within\u2014 (I) a disadvantaged community; or (II) a community that has an inability to draw on other sources of funding because of the small population or low income of the community; or (ii) for any other reason the Secretary determines appropriate. (C) Non-Federal share An eligible covered entity that is awarded a grant under this subsection may satisfy the non-Federal share of a project carried out with a grant awarded under this subsection through in-kind contributions and other noncash support, including the following: (i) The value, as determined by an appraisal performed at such time before the award of the grant as the Secretary determines appropriate, of a working waterfront or an interest in a working waterfront, including conservation and other easements, that is held in perpetuity by a qualified holder, if the working waterfront or interest in a working waterfront\u2014 (I) is identified in the grant application; and (II) is acquired by the qualified holder not later than 3 years after\u2014 (aa) the grant award date; or (bb) the date of the submission of such application and before the end of the initial 5-year period for which the approved working waterfronts plan associated with the grant application, if any, is effective. (ii) The costs, including cash or in-kind contributions, associated with the acquisition, restoration, or enhancement of or making other improvements to a working waterfront or an interest in a working waterfront, if\u2014 (I) such costs are identified in the grant application; and (II) the costs are incurred\u2014 (aa) before the end of the initial 5-year period for which the approved working waterfronts plan associated with the grant application, if any, is effective; or (bb) for working waterfronts described in clause (i), within the time limits described in that clause. (11) Working waterfront covenants (A) In general An eligible covered entity that is awarded a grant under this subsection may use such grant award with respect to a working waterfront only for which each person other than the eligible covered entity that holds title to or an interest in such working waterfront enters into a working waterfront covenant. (B) Violation (i) In general An eligible covered entity may determine, on the record after an opportunity for a hearing, that a working waterfront covenant of the eligible covered entity has been violated. (ii) Reversion; conveyance; right of immediate entry If an eligible covered entity makes a determination under clause (i) that a violation described under that clause has occurred\u2014 (I) all right, title, and interest in and to the working waterfront covered by the violated working waterfront covenant shall revert to the eligible covered entity; (II) the eligible covered entity may convey the working waterfront or interest in the working waterfront to a qualified holder; and (III) the eligible covered entity shall have the right of immediate entry onto the working waterfront covered by the violated working waterfront covenant. (12) Terms and conditions The Secretary shall subject each grant awarded under this subsection to such terms and conditions as the Secretary determines appropriate to ensure that each such grant is used for purposes consistent with this section. (13) Report (A) In general The Secretary shall biennially submit to Congress a report regarding the implementation of this subsection, which shall include\u2014 (i) an evaluation, based on performance measures developed by the Secretary, of the effectiveness of the grant program in accomplishing the purposes of this subsection; (ii) an account of all expenditures under this subsection; and (iii) descriptions of each project carried out using a grant awarded under this section. (B) Alternative manner of submission The Secretary may submit each report required under subparagraph (A) by including the information required under that subparagraph in each report required under section 316. (14) Administrative expenses The Secretary may use not more than 5 percent of the amounts made available under this subsection in each fiscal year to pay the administrative expenses necessary to carry out this subsection. (15) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this subsection $50,000,000 for each of fiscal years 2025 through 2029. (d) Definitions In this section: (1) Approved working waterfronts plan The term approved working waterfronts plan means a working waterfronts plan that is approved by the Secretary under subsection (b). (2) Coastal Indian Tribe The term coastal Indian Tribe means an Indian Tribe with respect to which land owned by the Indian Tribe, held in trust by the United States for the Indian Tribe, or held by the Indian Tribe and subject to restrictions on alienation imposed by the United States or the reservation of the Indian Tribe is located within a coastal state. (3) Coastal users The term coastal users means\u2014 (A) persons that engage in commercial or recreational fishing; (B) recreational fishing and boating businesses; and (C) boatbuilding, aquaculture, and other water-dependent, coastal-related businesses. (4) Covered entity The term covered entity means\u2014 (A) a coastal state; (B) a coastal Indian Tribe; or (C) a Native Hawaiian organization. (5) Eligible covered entity The term eligible covered entity means a covered entity that\u2014 (A) has an approved working waterfronts plan; (B) is in the process of developing a working waterfronts plan for approval under subsection (b); or (C) has a coastal land use plan that the Secretary determines is sufficient for the purposes of this section. (6) Grant program The term grant program means the grant program established under subsection (c). (7) Indian Tribe The term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (8) Native Hawaiian organization The term Native Hawaiian organization means a nonprofit organization\u2014 (A) that serves the interests of Native Hawaiians; (B) in which Native Hawaiians serve in substantive and policymaking positions; (C) that is recognized for having expertise in Native Hawaiian culture and heritage, including tourism; and (D) is located within a coastal state. (9) Qualified holder The term qualified holder means\u2014 (A) a unit of local government of a covered entity, if the covered entity is a coastal state; or (B) a nonprofit organization; that is designated by a covered entity in the approved working waterfronts plan of the covered entity to carry out some or all of the functions of the covered entity under the grant program if the covered entity applies for and is awarded a grant under the grant program, including holding title to or an interest in a working waterfront acquired with a grant awarded under the grant program. (10) Task Force The term Task Force means the task force established under subsection (a)(1). (11) Disadvantaged community The term disadvantaged community means a community the Secretary determines, based on appropriate data, indices, and screening tools, is economically, socially, or environmentally disadvantaged. (12) Working waterfront The term working waterfront means real property (including support structures over water and other facilities) that\u2014 (A) provides access to coastal waters by coastal users; and (B) is used for, or supports, commercial and recreational fishing, recreational fishing and boating businesses, and boatbuilding, aquaculture, and other water-dependent, coastal-related business. (13) Working waterfront covenant The term working waterfront covenant means an agreement in recordable form entered into between a person that holds title to or an interest in a working waterfront and a covered entity that is awarded a grant under the grant program or a qualified holder of such covered entity that provides such assurances as the Secretary determines necessary to ensure the following: (A) Except as provided in subparagraph (C), the title to or interest in the working waterfront will be held by an entity that is subject to such agreement in perpetuity. (B) The working waterfront will be managed in a manner that is consistent with the purposes of this section, and the working waterfront will not be converted to any use that is inconsistent with this section. (C) If the title to or interest in the working waterfront is subsequently sold or otherwise exchanged\u2014 (i) each party involved in such sale or exchange shall accede to such agreement; and (ii) funds equal to the fair market value of the title to or interest in the working waterfront shall be paid to the Secretary by the parties to the sale or exchange, and such funds shall be, at the discretion of the Secretary, paid to the relevant covered entity or a qualified holder of such covered entity for use in the implementation of the approved working waterfronts plan of the covered entity. (D) Such agreement shall be subject to enforcement and oversight by the covered entity or by another person as the Secretary determines appropriate. 306C. Working Waterfronts Preservation Loan Fund (a) General authority (1) Grants to eligible coastal states to establish working waterfronts preservation loan funds (A) In general The Secretary may enter into an agreement with an eligible coastal state to issue a capitalization grant, including a letter of credit, to such eligible coastal state to implement the approved working waterfronts plan of such eligible coastal state. (B) Establishment of working waterfronts preservation loan funds (i) In general To be eligible to receive a capitalization grant under this subsection, an eligible coastal state shall establish a working waterfronts preservation loan fund. (ii) Deposit Each capitalization grant made to an eligible coastal state under this paragraph shall be deposited in the working waterfronts preservation loan fund of such eligible coastal state. (C) Extended period A capitalization grant made to an eligible coastal state under this section shall be available to the eligible coastal state for obligation for a period of 2 fiscal years. (2) Use of funds (A) In general An eligible coastal state shall use amounts deposited in the working waterfronts preservation loan fund of such eligible coastal state, including loan repayments and interest earned on such amounts, to provide financial assistance described in subsection (f) to a covered entity to implement the approved working waterfronts plan of such eligible coastal state through preservation, improvement, restoration, rehabilitation, and acquisition of working waterfronts pursuant to criteria established by the Secretary. (B) Sale of bonds A covered entity may use amounts received under this section as a source of revenue (restricted solely to interest earnings of the applicable working waterfronts preservation loan fund) or security for payment of the principal and interest on a revenue or general obligation bond issued by the eligible coastal state to provide matching funds under subsection (e) if the proceeds of the sale of the bond will be deposited in the working waterfronts preservation loan fund of such eligible coastal state. (C) No increased bonding authority Amounts deposited in the working waterfronts preservation loan fund of an eligible coastal state may not be used as a source of payment of, or security for (directly or indirectly), in whole or in part, any obligation the interest on which is exempt from the tax imposed under chapter 1 of the Internal Revenue Code of 1986. (3) Limitation An eligible coastal state may not provide financial assistance described in subsection (f) to a covered entity that does not have the technical, managerial, and financial capability to ensure compliance with the requirements of this section. (4) Prevailing wages The Secretary shall ensure compliance with the provisions of the Act of March 3, 1931 ( 40 U.S.C. 3141 et seq. ; commonly known as the Davis-Bacon Act ) with respect to any construction project carried out in whole or in part with financial assistance made available from a working waterfronts preservation loan fund. (5) Reservation Each eligible coastal state that enters into a capitalization agreement under paragraph (1) shall, each fiscal year, reserve 0.2 percent of the amount in the working waterfronts preservation loan fund of the eligible coastal state to provide financial assistance described in subsection (f) to an Indian Tribe or a Native Hawaiian organization. (b) Intended use plans (1) In general Each eligible coastal state that enters into a capitalization agreement under subsection (a)(1) shall annually prepare an intended use plan, subject to notice and an opportunity for public comment, that identifies the intended uses of the amounts available to the working waterfronts preservation loan fund of the eligible coastal state. (2) Contents Each intended use plan prepared by an eligible coastal state under paragraph (1) shall include, with respect to the eligible coastal state\u2014 (A) a list of each project to be assisted with amounts from the working waterfronts preservation loan fund in the first fiscal year that begins after the date such intended use plan is finalized, including, with respect to each such project\u2014 (i) a description of the project; (ii) the expected terms of financial assistance; and (iii) the size of the community served; (B) the criteria and methods established to distribute amounts from the working waterfronts preservation loan fund; and (C) a description of the financial status of the working waterfronts preservation loan fund and the short- and long-term goals of such working waterfronts preservation loan fund. (c) Working waterfronts preservation loan fund management (1) In general Each working waterfronts preservation loan fund under this section shall be established, maintained, and credited with repayments and interest and the fund corpus shall be available in perpetuity to provide financial assistance described in subsection (f) to covered entities under this section. (2) Extra amounts To the extent amounts in a working waterfronts preservation loan fund are not required for obligation or expenditure, such amounts shall be invested in interest-bearing obligations. (d) Assistance for disadvantaged communities (1) Loan subsidy (A) In general Notwithstanding any other provision of this section, if an eligible coastal state makes a loan to a disadvantaged community pursuant to subsection (a)(2), the eligible coastal state may provide additional subsidization to such disadvantaged community, including\u2014 (i) forgiveness of principal; (ii) grants; (iii) negative interest loans; (iv) other loan forgiveness; and (v) through buying, refinancing, or restructuring debt. (B) Exclusion A loan from a working waterfronts preservation loan fund with an interest rate equal to or greater than 0 percent shall not be considered additional subsidization for the purposes of this subsection. (2) Total amount of subsidies Of the amount of a capitalization grant received by an eligible coastal state for any fiscal year, the total amount of loan subsidies made by such eligible coastal state pursuant to paragraph (1)\u2014 (A) may not exceed 35 percent; and (B) to the extent that there are, as determined by the Secretary, sufficient applications from disadvantaged communities for loans, may not be less than 12 percent. (e) Eligible coastal state contribution Each capitalization agreement entered into under subsection (a)(1) shall require that the eligible coastal state subject to such agreement deposit in the working waterfronts preservation loan fund of the eligible coastal state an amount equal to not less than 20 percent of the total amount of the capitalization grant to be made to the eligible coastal state on or before the date on which the capitalization grant payment is made to the eligible coastal state. (f) Types of assistance The amounts deposited into a working waterfronts preservation loan fund of an eligible coastal state under this section may be used by the eligible coastal state\u2014 (1) to make a loan to a covered entity, on the condition that\u2014 (A) the interest rate for the loan does not exceed the market rate; (B) principal and interest payments on the loan will commence not later than 18 months after completion of the project for which the loan was made; (C) the loan will be fully amortized not later than 30 years after the completion of the project, except that in the case of a disadvantaged community an eligible coastal state may provide an extended term for the loan, if the extended term\u2014 (i) terminates not later than the date that is 40 years after the completion of the project; and (ii) does not exceed the expected design life of the project; (D) the recipient of the loan will establish a dedicated source of revenue (or, in the case of a privately owned working waterfront property, demonstrate that there is adequate security) for the repayment of the loan; and (E) the working waterfronts preservation loan fund of the eligible coastal state will be credited with all payments of principal and interest on the loan; (2) to buy or refinance the debt obligation of a municipality or an intermunicipal or interstate agency within the eligible coastal state at an interest rate that is less than or equal to the market interest rate; (3) to guarantee, or purchase insurance for, a local obligation (all of the proceeds of which finance a project eligible for financial assistance under this section) if the guarantee or purchase would improve credit market access or reduce the interest rate applicable to the obligation; (4) as a source of revenue or security for the payment of principal and interest on a revenue or general obligation bond issued by the eligible coastal state if the proceeds of the sale of the bond will be deposited into the working waterfronts preservation loan fund of the eligible coastal state; or (5) to earn interest on the amounts deposited into the working waterfronts preservation loan fund of the eligible coastal state. (g) Administration of working waterfronts preservation loan funds (1) Combined financial administration Notwithstanding subsection (c), an eligible coastal state may combine the financial administration of a working waterfronts preservation loan fund of the eligible coastal state with the financial administration of any other revolving fund established by the eligible coastal state if the Secretary determines that the capitalization grants made under this section, together with loan repayments and interest, will be separately accounted for and used solely for the purposes specified in subsection (a). (2) Cost of administering working waterfronts preservation loan fund (A) In general For each fiscal year, an eligible coastal state may use the amount described in subparagraph (B)\u2014 (i) to cover the reasonable costs of administration of the programs under this section, including the recovery of reasonable costs expended to establish a working waterfronts preservation loan fund that are incurred after the date of the enactment of this section; and (ii) to provide technical assistance to working waterfronts projects carried out within the eligible coastal state. (B) Description of amount The amount referred to in subparagraph (A) is an amount equal to the sum of\u2014 (i) the amount of any fees collected by the eligible coastal state for use in accordance with subparagraph (A)(i), regardless of the source; and (ii) the greater of\u2014 (I) $400,000; (II) 0.2 percent of the current valuation of the working waterfronts preservation loan fund of the eligible coastal state; or (III) an amount equal to 4 percent of all grant awards made to the working waterfronts preservation loan fund of the eligible coastal state under this section for the fiscal year. (h) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $50,000,000 for each of fiscal years 2025 through 2029. (i) Definitions In this section: (1) Approved working waterfronts plan The term approved working waterfronts plan has the meaning given the term in section 306B. (2) Covered entity The term covered entity means\u2014 (A) a State agency; (B) an Indian Tribe; (C) a Native Hawaiian organization; (D) a local government; or (E) a nonprofit organization. (3) Disadvantaged community The term disadvantaged community has the meaning given the term in section 306B. (4) Eligible coastal state The term eligible coastal state means a coastal state that has an approved working waterfronts plan. (5) Working waterfront The term working waterfront has the meaning given the term in section 306B. (6) Working waterfronts preservation loan fund The term working waterfronts preservation loan fund means a revolving loan fund established under this section for the preservation of working waterfronts. .",
      "versionDate": "2025-03-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2026-02-11T15:11:56Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-11T15:12:01Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-02-11T15:12:06Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-02-11T15:11:52Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2026-02-11T15:12:16Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-02-11T15:12:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-19T15:24:03Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1808ih.xml"
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
      "title": "Keep America\u2019s Waterfronts Working Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep America\u2019s Waterfronts Working Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Coastal Zone Management Act of 1972 to establish a working waterfronts Task Force and working waterfronts grant and loan programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T02:48:24Z"
    }
  ]
}
```
