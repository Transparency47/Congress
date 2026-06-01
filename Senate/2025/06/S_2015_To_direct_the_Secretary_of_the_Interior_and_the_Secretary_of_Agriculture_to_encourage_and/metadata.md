# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2015?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2015
- Title: National Prescribed Fire Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2015
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2015",
    "number": "2015",
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
    "title": "National Prescribed Fire Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
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
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-10",
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
      "actionDate": "2025-06-10",
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
            "date": "2025-06-10T18:52:12Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "NC"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "UT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "FL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2015is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2015\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mr. Wyden (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of the Interior and the Secretary of Agriculture to encourage and expand the use of prescribed fire on land managed by the Department of the Interior or the Forest Service, with an emphasis on units of the National Forest System in the western and southeastern United States, to acknowledge and support the long-standing use of cultural burning by Indian Tribes and Indigenous practitioners, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the National Prescribed Fire Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Use of funds\nSec. 101. Definition of prescribed fire.\nSec. 102. Prescribed fire funding.\nSec. 103. Policies and practices.\nSec. 104. Collaborative Prescribed Fire Program.\nTITLE II\u2014Facilitating implementation and outreach\nSec. 201. Cooperative agreements and contracts.\nSec. 202. Human resources.\nSec. 203. Liability of prescribed fire managers.\nSec. 204. Environmental review.\nSec. 205. Prescribed fire education program.\nTITLE III\u2014Reporting\nSec. 301. Annual reports to National Fire Planning and Operations Database.\nSec. 302. Annual implementation report.\n#### 2. Definitions\nIn this Act:\n**(1) Congressional committees**\nThe term congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources, the Committee on Agriculture, Nutrition, and Forestry, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Natural Resources, the Committee on Agriculture, and the Committee on Appropriations of the House of Representatives.\n**(2) Federal land**\nThe term Federal land means\u2014\n**(A)**\nland under the jurisdiction of the Secretary; and\n**(B)**\nNational Forest System land.\n**(3) Landscape-scale prescribed fire plan**\nThe term landscape-scale prescribed fire plan means a decision document prepared pursuant to the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) that\u2014\n**(A)**\ncovers a unit of the National Forest System, a Bureau of Land Management district, or a subunit of such a unit or district;\n**(B)**\nanalyzes the site-specific environmental consequences of prescribed fire on land described in subparagraph (A); and\n**(C)**\nobviates the need for subsequent decisions pursuant to the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) with respect to the unit, district, or subunit described in subparagraph (A).\n**(4) National Forest System**\n**(A) In general**\nThe term National Forest System has the meaning given the term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609(a) ).\n**(B) Exclusions**\nThe term National Forest System does not include the national grasslands or land utilization projects administered under title III of the Bankhead-Jones Farm Tenant Act ( 7 U.S.C. 1010 et seq. ).\n**(5) Prescribed fire**\nThe term prescribed fire means a fire deliberately ignited to burn wildland fuels in a natural or modified state\u2014\n**(A)**\nunder specified environmental conditions that are intended to allow the fire to be confined to a predetermined area and produce the fireline intensity and rate of spread required to attain planned resource management objectives; and\n**(B)**\nin accordance with applicable law (including regulations).\n**(6) Secretaries**\nThe term Secretaries means\u2014\n**(A)**\nthe Secretary; and\n**(B)**\nthe Secretary of Agriculture.\n**(7) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(8) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary, in the case of land under the jurisdiction of the Secretary; and\n**(B)**\nthe Secretary of Agriculture, in the case of land under the jurisdiction of the Secretary of Agriculture.\nI\nUse of funds\n#### 101. Definition of prescribed fire\n##### (a) In general\nIn this title, the term prescribed fire has the meaning given the term in section 2.\n##### (b) Exclusion\nIn this title, the term prescribed fire does not include a fire that is ignited for the primary purpose of pile burning.\n#### 102. Prescribed fire funding\n##### (a) Funding flexibility\n**(1) Department of Agriculture**\nThe Secretary of Agriculture may use not more than 15 percent of funds appropriated for each fiscal year for hazardous fuels management in the National Forest System for activities described in subsection (b).\n**(2) Department of the Interior**\nThe Secretary may use not more than 15 percent of funds appropriated for each fiscal year for hazardous fuels management and post-fire activities in the account for wildland fire management of the Department of the Interior for activities described in subsection (b).\n##### (b) Description of activities\nThe activities referred to in subsection (a) are\u2014\n**(1)**\nwith respect to prescribed fires on Federal land, or on non-Federal land if the Secretary concerned determines that such activities would benefit resources on Federal land\u2014\n**(A)**\nentering into procurement contracts or cooperative agreements for prescribed fire activities;\n**(B)**\nissuing grants to a State, Tribal government, local government, prescribed fire council, prescribed burn association, or nonprofit organization for the implementation of prescribed fires, including\u2014\n**(i)**\ncarrying out necessary environmental reviews;\n**(ii)**\ncarrying out any site preparation necessary for implementing prescribed fires; and\n**(iii)**\nconducting any required pre-ignition cultural or environmental surveys; and\n**(C)**\nconducting outreach to the public, Indian Tribes and beneficiaries, and adjacent landowners;\n**(2)**\nimplementing prescribed fires on non-Federal land, if the Secretary concerned determines that the prescribed fire would benefit Federal land, including\u2014\n**(A)**\ncarrying out necessary environmental reviews;\n**(B)**\ncarrying out any site preparation necessary for implementing prescribed fires; and\n**(C)**\nconducting any required pre-ignition cultural and environmental surveys;\n**(3)**\nproviding to Federal employees and cooperators training for prescribed fire and basic smoke management practices;\n**(4)**\nconducting post-prescribed fire activities, such as monitoring for hazard trees or reignitions and invasive species management;\n**(5)**\nproviding technical or financial assistance to a State, Tribal government, local government, prescribed fire council, prescribed burn association, or nonprofit organization for the purpose of providing training for prescribed fire or basic smoke management practices, consistent with any standards developed by the National Wildfire Coordinating Group or State prescribed fire standards; and\n**(6)**\nproviding funding for the applicable Collaborative Prescribed Fire Program established under section 104.\n##### (c) Prioritization\n**(1) In general**\nSubject to paragraph (2), the Secretary concerned shall coordinate with the other Secretary concerned, State and local government agencies, Indian Tribes, and applicable nongovernmental organizations to establish prioritization criteria for expending amounts pursuant to subsection (a) for activities described in paragraphs (2), (5), and (6) of subsection (b).\n**(2) Requirement**\nIn establishing criteria under paragraph (1), the Secretary concerned shall give priority to a project that is\u2014\n**(A)**\nimplemented across a large contiguous area;\n**(B)**\ncross-boundary in nature;\n**(C)**\nin an area that is\u2014\n**(i)**\nwithin or adjacent to the wildland-urban interface and identified as a priority area in a statewide forest action plan or Community Wildfire Protection Plan; or\n**(ii)**\nidentified as important to the protection of a Tribal trust resource or the reserved or treaty rights of an Indian Tribe;\n**(D)**\non land that is at high or very high risk of experiencing a wildfire that would be difficult to suppress;\n**(E)**\nin an area that is designated as critical habitat and in need of ecological restoration or enhancement that can be achieved with the aid of prescribed fire; or\n**(F)**\nsupportive of potential operational delineations or strategic response zones.\n#### 103. Policies and practices\n##### (a) Increasing prescribed fire\nBeginning with the first fiscal year that begins after the date of enactment of this Act, and for each of the 9 fiscal years thereafter, the Secretaries shall conduct prescribed fires on Federal land such that the total acreage of Federal land on which prescribed fires are conducted is 10 percent greater than the total acreage of all Federal land on which prescribed fires were conducted during the preceding fiscal year.\n##### (b) Operational strategy\nThe Secretary concerned shall develop, in coordination with State, local, and Tribal governments, a prescribed fire operational strategy for each region of the National Forest System or the Department of the Interior, as applicable, that describes\u2014\n**(1)**\nthe fire deficit by region; and\n**(2)**\nstaffing and funding needs to address the fire deficit under paragraph (1).\n#### 104. Collaborative Prescribed Fire Program\n##### (a) In general\nThe Secretary concerned, in coordination with the other Secretary concerned, shall establish a Collaborative Prescribed Fire Program (referred to in this section as the program ) to select and fund prescribed fire projects (each of which is referred to in this section as a project ) in accordance with\u2014\n**(1)**\nthe prioritization criteria established under section 102(c);\n**(2)**\nthe Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. );\n**(3)**\nthe National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. );\n**(4)**\nthe applicable land use or land management plan; and\n**(5)**\nany other applicable law.\n##### (b) Eligibility criteria\nTo be eligible for nomination under subsection (c), a proposal for a project shall\u2014\n**(1)**\nbe consistent with a landscape restoration strategy\u2014\n**(A)**\nthat is complete or substantially complete;\n**(B)**\nthat identifies and prioritizes prescribed fire treatments for a 10-year period within a landscape that is\u2014\n**(i)**\nnot less than 50,000 acres;\n**(ii)**\ncomposed primarily of forested Federal land under the jurisdiction of the Secretary concerned, but may also include other Federal, State, Tribal, or private land, if a treatment on that land would benefit the applicable Federal land; and\n**(iii)**\nin need of\u2014\n**(I)**\nactive ecosystem restoration; or\n**(II)**\nmaintenance activities to retain previously treated land in a wildfire-resilient state;\n**(C)**\nthat incorporates the best available science and scientific application tools to identify project areas;\n**(D)**\nthat fully maintains, or contributes toward the restoration of, the structure and composition of old growth stands according to the pre-fire suppression old growth conditions characteristic of the forest type\u2014\n**(i)**\ntaking into account the contribution of the stand to landscape fire adaptation and watershed health; and\n**(ii)**\nretaining the large trees contributing to old growth structure;\n**(E)**\nunder which would be carried out any forest restoration treatments that reduce hazardous fuels through the use of fire for ecological restoration and maintenance and reestablishing natural fire regimes, where appropriate, which\u2014\n**(i)**\nmay include site preparation, if necessary to prepare the landscape for reestablishment of a natural fire regime; and\n**(ii)**\nshall maximize the retention of large trees, as appropriate for the forest type, to the extent that the trees promote fire-resilient stands; and\n**(F)**\nunder which\u2014\n**(i)**\nno permanent roads would be established; and\n**(ii)**\nfunding would be committed to decommission all temporary roads constructed to carry out the strategy;\n**(2)**\nbe developed and implemented through a collaborative process that\u2014\n**(A)**\nincludes multiple interested persons representing diverse interests; and\n**(B)**\nis transparent and nonexclusive;\n**(3)**\ndescribe plans, as applicable\u2014\n**(A)**\nto reduce the risk of uncharacteristic wildfire;\n**(B)**\nto improve fish and wildlife habitat, including for endangered, threatened, and sensitive species;\n**(C)**\nto maintain or improve water quality and watershed function;\n**(D)**\nto prevent, remediate, or control invasions of exotic species;\n**(E)**\nto maintain, decommission, and rehabilitate roads and trails;\n**(F)**\nto report annually on performance, including setting accomplishment targets for each year;\n**(G)**\nto take into account any applicable community wildfire protection plan; and\n**(H)**\nto mitigate smoke impacts on nearby communities;\n**(4)**\ninclude an analysis of any anticipated cost savings, including savings resulting from\u2014\n**(A)**\na reduced risk of wildfire damages, especially to high-value resources; and\n**(B)**\na decrease in the unit costs of implementing ecological restoration treatments over time;\n**(5)**\ninclude estimates of\u2014\n**(A)**\nthe amount of annual Federal funding necessary to implement the proposed project; and\n**(B)**\nthe amount of new non-Federal investment for carrying out the proposed project that would be leveraged;\n**(6)**\ndescribe the collaborative process described in paragraph (2) through which the proposal was developed, including a description of\u2014\n**(A)**\nparticipation by, or consultation with, State, local, and Tribal governments; and\n**(B)**\nany established record of successful collaborative planning and implementation of prescribed fire projects on National Forest System land and other land included in the proposal by the collaborators;\n**(7)**\npropose to benefit local economies by providing local employment or training opportunities through contracts, grants, or agreements for planning, design, implementation, or monitoring with\u2014\n**(A)**\nlocal private, nonprofit, or cooperative entities;\n**(B)**\nYouth Conservation Corps crews or related partnerships with State, local, and nonprofit youth groups;\n**(C)**\nexisting or proposed small or micro businesses, clusters, or incubators; or\n**(D)**\nother entities that will hire or train local individuals to complete those contracts, grants, or agreements; and\n**(8)**\nbe subject to any other requirements that the Secretary concerned determines to be necessary for the efficient and effective administration of the program.\n##### (c) Nomination process\n**(1) Submission**\nA proposal for a project shall be submitted to the appropriate Regional Forester, State Director, or other similar official.\n**(2) Nomination**\n**(A) In general**\nAn official described in paragraph (1) may nominate for selection by the Secretary concerned any proposals received by the official under that paragraph that meet the eligibility criteria described in subsection (b).\n**(B) Concurrence**\nIn the case of a proposal for a project that involves activities on the land of both Secretaries concerned, a nomination under subparagraph (A) shall include the concurrence of the appropriate official for the applicable land that is not under the jurisdiction of the official nominating the proposal.\n**(3) Other land**\nIn the case of a proposal for a project that involves activities on land that is not under the jurisdiction of either Secretary concerned, a nomination under subparagraph (A) shall include evidence that the landowner intends to participate in, and provide appropriate funding to carry out, the activities.\n##### (d) Selection process\n**(1) In general**\nThe Secretary concerned, in consultation with the other Secretary concerned, shall select for implementation proposals for projects\u2014\n**(A)**\nthat have been nominated under subsection (c)(2);\n**(B)**\nthat meet the eligibility criteria described in subsection (b); and\n**(C)**\nin accordance with the prioritization criteria established under section 102(c).\n**(2) Criteria**\nIn selecting proposals under paragraph (1), the Secretary concerned shall give special consideration to\u2014\n**(A)**\nthe strength of the proposal, including the landscape restoration strategy described in subsection (b)(1) of the proposal;\n**(B)**\nthe strength of the ecological case of the proposal and the proposed ecological restoration strategies under the proposal;\n**(C)**\nthe strength of the collaborative process described in subsection (b)(2) through which the proposal was developed and the likelihood of successful collaboration throughout implementation;\n**(D)**\nthe extent to which the proposal is likely to achieve reductions in long-term wildfire risk and increased protection of high-value resources;\n**(E)**\nthe extent to which an appropriate level of non-Federal investment would be leveraged in carrying out the proposed project; and\n**(F)**\nensuring geographic diversity of projects implemented under this section.\n**(3) Limitation**\nThe Secretary concerned may select not more than\u2014\n**(A)**\n20 proposals under paragraph (1) to be funded during any fiscal year; and\n**(B)**\nthe number of proposals under paragraph (1) that the Secretary concerned determines are likely to receive adequate funding.\n##### (e) Reporting\n**(1) Project reporting**\nA recipient of financial assistance to carry out a project under the program shall annually submit to the Secretary concerned a report summarizing, at a minimum, with respect to the year covered by the report\u2014\n**(A)**\nthe number of acres of land treated with prescribed fire by the recipient under the program; and\n**(B)**\nthe amount of Federal and non-Federal funds used by the recipient under the program.\n**(2) Program report**\nNot later than 5 years after the first fiscal year in which funding is made available to carry out projects under the program, and every 5 years thereafter, the Secretary concerned shall submit to the congressional committees a report describing the program, including an assessment of whether, and to what extent, the program is fulfilling the purposes of this section.\n##### (f) Limitations\n**(1) Total funding**\nThe Secretary concerned shall not provide more than $20,000,000 in total funding for projects under the program in any fiscal year.\n**(2) Project size limitation**\nThe Secretary concerned shall not provide more than $1,000,000 for any 1 project under the program in any fiscal year.\n**(3) Project sunset**\nThe Secretary concerned shall not provide funding for a project under the program for a period of more than 10 fiscal years.\n**(4) Project cancellation**\nThe Secretary concerned shall cease funding any project under the program that, for 3 consecutive years, fails to meet the annual accomplishment targets set under subsection (b)(3)(F).\n##### (g) Funding\nOf the amounts made available under section 102(a), the Secretary concerned may use to carry out this section not more than $10,000,000 for each of fiscal years 2025 through 2034.\nII\nFacilitating implementation and outreach\n#### 201. Cooperative agreements and contracts\n##### (a) Definition of eligible entity\nIn this section, the term eligible entity means\u2014\n**(1)**\na State;\n**(2)**\nan Indian Tribe;\n**(3)**\na county or municipal government;\n**(4)**\na fire district;\n**(5)**\na nongovernmental organization; and\n**(6)**\na private entity.\n##### (b) Authorization\nThe Secretary concerned may enter into a cooperative agreement or contract with an eligible entity to authorize the eligible entity to coordinate, plan, or conduct a prescribed fire on Federal land in accordance with other applicable laws, regulations, and land management plans.\n##### (c) Subcontracts\nThe Secretary concerned may authorize a State, an Indian Tribe, or a county that enters into a cooperative agreement or contract under subsection (b) to enter into a subcontract to conduct a prescribed fire on Federal land pursuant to that cooperative agreement or contract, subject to any other terms and conditions that the Secretary concerned determines to be appropriate.\n##### (d) Long-Term contracts\nA cooperative agreement or contract with an eligible entity under subsection (b) may authorize the eligible entity to conduct a series of prescribed fires on Federal land for a period of not longer than 10 years.\n#### 202. Human resources\n##### (a) Prescribed fire workforce\n**(1) Increasing workforce retention**\n**(A) Hazard pay**\n**(i) In general**\nEach Federal employee in any classification series, as identified by the Secretaries, shall be entitled to be paid the appropriate differential under subsection (d) of section 5545 of title 5, United States Code, as if such employee was covered by such subsection, when such employee carries out work directly related to the ignition, management, and control of a prescribed fire.\n**(ii) Regulations**\nThe Director of the Office of Personnel Management shall prescribe regulations to carry out this subparagraph.\n**(B) Incentive payments for fuels assignments**\nThe Secretaries shall submit to the congressional committees a joint report describing mechanisms to attract and retain a skilled fuels workforce, including pay incentives that would account for and offset the more competitive pay options offered through wildfire suppression assignments.\n**(2) Dedicated prescribed fire task forces**\n**(A) In general**\nThe Secretaries shall\u2014\n**(i)**\nnot later than 180 days after the date of enactment of this Act, establish at least 1 multiparty task force of Federal employees and non-Federal entities within each Geographic Area Coordination Center to plan, lead, and support prescribed fire across ownership boundaries that are priorities at the landscape, region, State, or Federal level; and\n**(ii)**\nsupport each task force established under clause (i) by assigning a dedicated Federal employee\u2014\n**(I)**\nto aid necessary administrative functions relating to partnership agreements; and\n**(II)**\nto coordinate prescribed fire across ownership boundaries.\n**(B) Cooperative agreements**\nThe Secretaries may enter into 1 or more cooperative agreements to carry out this paragraph.\n**(3) Conversion of seasonal firefighters to permanent employees**\nThe Secretaries may noncompetitively convert a Federal seasonal employee to a Federal permanent employee if\u2014\n**(A)**\nthe listed job duties of the employee include wildland firefighting;\n**(B)**\nthe employee received a rating of at least Fully Successful in each of the performance appraisals of the employee for the 3 most recent seasons of Federal employment of the employee; and\n**(C)**\nthe job duties and performance standards of the position into which the permanent employee converts emphasize implementing prescribed fires.\n**(4) Employment of formerly incarcerated individuals**\n**(A) In general**\nThe Secretaries, in consultation with the Attorney General and State departments of corrections, shall seek to provide career pathways, training, and wraparound support services, including through partnerships with the Corps Network, to individuals described in subparagraph (B) to work as prescribed fire practitioners.\n**(B) Individuals described**\nAn individual referred to in subparagraph (A) is an individual that\u2014\n**(i)**\nhas been convicted in any court of a criminal offense, other than arson or a violent crime (as defined by the Secretaries, in consultation with the Attorney General and State departments of corrections), and was sentenced to a term of imprisonment for that offense; and\n**(ii)**\nduring the term of imprisonment described in clause (i), served on a wildland firefighting crew or received other comparable training.\n**(5) Underutilized employees**\nThe Secretaries shall support the recruitment, development, and participation of underutilized employees, as determined by the Secretaries, in the wildland fire workforce, including by fostering leadership opportunities, mentorship networks, and training.\n**(6) Veterans crews**\n**(A) In general**\nThe Secretaries, in consultation with the Secretary of Veterans Affairs, shall seek\u2014\n**(i)**\nto provide a career pathway to individuals described in subparagraph (B) to work as prescribed fire practitioners; and\n**(ii)**\nto establish crews composed predominantly of veterans to conduct prescribed fires.\n**(B) Individuals described**\nAn individual referred to in subparagraph (A) is an individual who\u2014\n**(i)**\nserved in the active military, naval, or air service; and\n**(ii)**\nwas discharged or released under conditions other than dishonorable.\n##### (b) Additional training centers\nSubject to the availability of appropriations, not later than 2 years after the date of enactment of this Act, the Secretary, in cooperation with the Secretary of Agriculture (and the Secretary of Defense in the case of a center located on a military installation), shall\u2014\n**(1)**\nestablish, operate, and facilitate a prescribed fire training program or center that offers training in prescribed fire within each Geographic Area Coordination Center region where such a program or center does not exist on the date of enactment of this Act; and\n**(2)**\nsupport the establishment of an Indigenous-led prescribed fire and cultural burning training center operated by an Indian Tribe or partnership of Indian Tribes.\n##### (c) Competencies for firefighters\nThe Secretaries, in coordination with the Fire Executive Council, shall task the National Wildfire Coordinating Group with the duty to adjust training requirements to obtain a certification to serve in a supervisory role for a prescribed fire and any other positions determined to be necessary by the Secretaries\u2014\n**(1)**\nin order to reduce the time required to obtain such a certification; and\n**(2)**\nsuch that significant experience, gained exclusively during a prescribed fire, is required to obtain such a certification.\n##### (d) Enhancing interoperability between Federal and non-Federal practitioners\n**(1) Qualification databases and dispatch systems**\nThe Secretaries shall establish a collaborative process to create mechanisms for non-Federal-agency fire practitioners to be included in prescribed fire and wildfire resource ordering and reimbursement processes.\n**(2) Partnership agreements**\nThe Secretaries shall\u2014\n**(A)**\ndevelop partnership agreements for prescribed fire with all relevant State, Federal, Tribal, university, and nongovernmental entities that choose to be included in resource ordering and reimbursement processes under paragraph (1);\n**(B)**\ncreate agreements and structures necessary to include non-Federal-agency and other nontraditional partners in direct work with Federal agencies to address prescribed fires; and\n**(C)**\ntreat any prescribed fire practitioner meeting applicable National Wildfire Coordinating Group standards as eligible to be included in statewide participating agreements.\n#### 203. Liability of prescribed fire managers\n##### (a) Definitions\nIn this section:\n**(1) Covered activity**\nThe term covered activity means an activity carried out on Federal land directly related to a wildland fire, prescribed fire, or prescribed fire with cultural objectives in the course of executing a Federal action.\n**(2) Covered entity**\nThe term covered entity means a non-Federal entity engaged in a covered activity, if that non-Federal entity is acting\u2014\n**(A)**\nunder the direct supervision of a Federal employee; and\n**(B)**\nwithin the scope of a contract or agreement in carrying out that covered activity.\n##### (b) Indemnity of Federal and Tribal employees\nThe Secretaries, in coordination with the Attorney General, shall develop, for employees involved in covered activities, a voluntary training course describing\u2014\n**(1)**\nliability protections afforded to those employees when acting within the scope of their employment;\n**(2)**\nthe limits on any liability protections under paragraph (1); and\n**(3)**\nreimbursements available for qualified employees for professional liability insurance under section 636 of division A of Public Law 104\u2013208 (5 U.S.C. prec. 5941 note).\n##### (c) Indemnity of other cooperators\n**(1) In general**\nBeginning on the date of enactment of this Act, a covered entity shall be considered to be an employee of the Federal Government for purposes of chapter 171 of title 28, United States Code (commonly known as the Federal Tort Claims Act ), while that covered entity is engaged in covered activities.\n**(2) Guidance**\nNot later than 1 year after the date of enactment of this Act, the Secretaries, in consultation with the Attorney General, shall issue guidance on the necessary provisions and implementation requirements for contracts or agreements that would extend liability protections to covered entities under paragraph (1).\n**(3) Reimbursement**\nBeginning in the first fiscal year that begins after the date of enactment of this Act, the Secretaries shall request, through annual appropriations, funds sufficient to reimburse the Treasury for any claims paid during the prior fiscal year pursuant to paragraph (1).\n##### (d) Effect\nNothing in this section limits or otherwise affects\u2014\n**(1)**\nthe application of any statutory or judicial immunity to Federal employees;\n**(2)**\nthe application of chapter 171 of title 28, United States Code (commonly known as the Federal Tort Claims Act ), to Federal employees; or\n**(3)**\nthe application of section 314 of Public Law 101\u2013512 ( 25 U.S.C. 5321 note).\n#### 204. Environmental review\n##### (a) Smoke management agencies\n**(1) Policy**\nThe Secretaries shall ensure that policies, training, and programs of the Secretaries are consistent with this subsection\u2014\n**(A)**\nto facilitate greater use of prescribed fire; and\n**(B)**\nto address public health and safety, including impacts from smoke from wildfires and prescribed fires.\n**(2) Coordination among Federal, Tribal, and State air quality agencies and Federal, Tribal, and State land management agencies**\nTo facilitate the use of prescribed fire on Federal, State, Tribal, and private land, the Administrator of the Environmental Protection Agency, in cooperation with Federal and State land management agencies, shall coordinate with State, Tribal, and local air quality agencies that regulate smoke under the Clean Air Act ( 42 U.S.C. 7401 et seq. )\u2014\n**(A)**\nto the maximum extent practicable, to provide State, Tribal, and local air quality agencies with guidance, data, imagery, or modeling to support the development of exceptional event demonstrations in accordance with sections 50.14 and 51.930 of title 40, Code of Federal Regulations (or successor regulations);\n**(B)**\nto develop archives and automated tools to provide State, Tribal, and local air quality agencies with the data, imagery, and modeling under subparagraph (A);\n**(C)**\nto develop decision support tools for State, Tribal, and local air quality agencies to assist in determining whether an exceptional event demonstration, if the Administrator of the Environmental Protection Agency concurs with such demonstration, would have regulatory significance;\n**(D)**\nto provide technical assistance, best practices, or templates to States, Indian Tribes, and local governments for use in approving the use of prescribed fire under a State, Tribal, or local government smoke management program;\n**(E)**\n**(i)**\nto promote basic smoke management practices and other best practices to protect the public from wildland fire smoke;\n**(ii)**\nto disseminate information about basic smoke management practices;\n**(iii)**\nto educate landowners that use prescribed fire about the importance of\u2014\n**(I)**\nusing basic smoke management practices; and\n**(II)**\nincluding basic smoke management practices as a component of a prescribed fire plan; and\n**(iv)**\nto share with the public, in coordination with other public health agencies, information about measures that individuals can take to protect themselves from wildland fire smoke; and\n**(F)**\nto develop guidance and tools to streamline the demonstration of a clear causal relationship between prescribed fire smoke and a related exceedance of a national ambient air quality standard.\n**(3) Exceptional event demonstrations**\n**(A) In general**\nThe appropriate State or Tribal air quality agency (including any local air quality agency delegated authority by a State) may develop and submit to the Administrator of the Environmental Protection Agency an exceptional event demonstration in accordance with sections 50.14 and 51.930 of title 40, Code of Federal Regulations (or successor regulations), for a prescribed fire.\n**(B) Approval**\nThe Administrator of the Environmental Protection Agency shall concur with an exceptional event demonstration submitted under subparagraph (A) in accordance with the requirements of sections 50.14 and 51.930 of title 40, Code of Federal Regulations (or successor regulations), including that the applicable prescribed fire was not reasonably controllable or preventable and that the applicable prescribed fire was a human activity unlikely to recur, if the State or Tribal air quality agency demonstrates in that exceptional event demonstration that, at a minimum, the applicable prescribed fire was\u2014\n**(i)**\nconducted in accordance with a State or Tribal smoke management program or basic smoke management practices; and\n**(ii)**\nconsistent with a land or resource management plan with a stated objective to establish, restore, or maintain a sustainable and resilient ecosystem.\n**(C) Demonstration assistance for Federal land**\nFor any prescribed fire conducted on Federal land, the Secretary concerned\u2014\n**(i)**\nshall assist with the development of an exceptional event demonstration under subparagraph (A) on request of a State or Tribal air quality agency; and\n**(ii)**\nmay develop and submit an exceptional event demonstration under subparagraph (A) with the concurrence of the applicable State or Tribal air quality agency.\n**(4) Programs and research**\nTo address the public health and safety risk of the expanded use of prescribed fire under this Act, the Secretaries, in coordination with the Administrator of the Environmental Protection Agency and the Director of the Centers for Disease Control and Prevention, shall conduct research to improve or develop\u2014\n**(A)**\nwildland fire smoke prediction models;\n**(B)**\nsmoke impact display tools for the public and decisionmakers;\n**(C)**\nappropriate, cost-effective, and consistent strategies to mitigate the impacts of smoke from prescribed fire on nearby communities;\n**(D)**\nconsistent nationally and scientifically supported messages regarding personal protection equipment for the public; and\n**(E)**\nprescribed fire activity tracking and emission inventory systems for planning and post-treatment accountability.\n##### (b) Development of landscape-Scale Federal prescribed fire plans\n**(1) Inclusion of landscape-scale prescribed fire plans**\nThe Secretary concerned shall, with respect to units of the National Forest System or Bureau of Land Management districts with existing prescribed fire programs\u2014\n**(A)**\nnot later than 1 year after the date of enactment of this Act, determine which of those units or districts have landscape-scale prescribed fire plans; and\n**(B)**\nnot later than 2 years after the date of enactment of this Act\u2014\n**(i)**\ndetermine whether each plan described in subparagraph (A) requires revision;\n**(ii)**\nestablish a schedule for the revision of each plan described in subparagraph (A) that requires revision; and\n**(iii)**\ndevelop landscape-scale prescribed fire plans for any units or districts that do not have landscape-scale prescribed fire plans.\n**(2) Environmental compliance**\nIn carrying out paragraph (1), the Secretary concerned shall\u2014\n**(A)**\ncomply with\u2014\n**(i)**\nthe National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. );\n**(ii)**\nthe Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. );\n**(iii)**\ndivision A of subtitle III of title 54, United States Code; and\n**(iv)**\nany other applicable laws; and\n**(B)**\nconsider the site-specific environmental consequences of the landscape-scale prescribed fire decisions under this subsection.\n**(3) Collaborative development**\nIn carrying out paragraph (1), the Secretary concerned shall collaborate with diverse actors from academia, Forest Service and Bureau of Land Management research and development programs, nongovernmental organizations, cultural fire practitioners, and other entities, as determined appropriate by the Secretary concerned.\n**(4) Consultation with Indian Tribes**\nThe Secretary concerned shall engage in government-to-government consultation with Indian Tribes in complying with this subsection.\n**(5) Reports**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary concerned shall submit to Congress a report describing the progress of the Secretary concerned with respect to carrying out this subsection.\n#### 205. Prescribed fire education program\n##### (a) In general\nThe Secretaries shall carry out a national prescribed fire education program focused on fire ecology and prescribed fire planning and implementation.\n##### (b) Program elements\nA prescribed fire education program under subsection (a) may include\u2014\n**(1)**\npublic service advertisements;\n**(2)**\nthe use of social media;\n**(3)**\ncampaign and educational activities and materials;\n**(4)**\ncommercial licensing;\n**(5)**\ncharacter images and appearances; and\n**(6)**\nawards and recognition.\nIII\nReporting\n#### 301. Annual reports to National Fire Planning and Operations Database\n##### (a) Purpose\nThe purpose of this section is to ensure an accurate reporting of annual prescribed fire accomplishments in the United States.\n##### (b) Cost-Share\nSubject to the availability of appropriations, the Secretary may provide financial assistance to States to pay a portion of the costs associated with annually reporting to the National Fire Planning and Operations Database (or a successor database) the prescribed fire accomplishments of the State.\n##### (c) Eligibility for funds\nIf, by December 31 of a calendar year, a State has not submitted to the National Fire Planning and Operations Database (or a successor database) a report describing, at a minimum, the number of acres on which uncharacteristic wildfire risk is effectively mitigated using prescribed fire in the State, the State shall not be eligible to receive any amounts made available under this Act for the previous fiscal year.\n#### 302. Annual implementation report\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretaries shall each submit to the congressional committees a report describing the activities carried out under this Act.",
      "versionDate": "2025-06-10",
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
        "actionDate": "2025-06-10",
        "text": "Referred to the Committee on Natural Resources, and in addition to the Committees on Agriculture, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3889",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "National Prescribed Fire Act of 2025",
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
            "name": "Air quality",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Fires",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Minority employment",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Temporary and part-time employment",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2026-01-07T19:50:30Z"
          },
          {
            "name": "Women's employment",
            "updateDate": "2026-01-07T19:50:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-14T17:37:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-10",
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
          "measure-id": "id119s2015",
          "measure-number": "2015",
          "measure-type": "s",
          "orig-publish-date": "2025-06-10",
          "originChamber": "SENATE",
          "update-date": "2026-02-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2015v00",
            "update-date": "2026-02-11"
          },
          "action-date": "2025-06-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>National Prescribed Fire Act of 2025</strong></p><ul></ul><p>This bill directs the Department of Agriculture (USDA) and the Department of the Interior to increase the number and size of prescribed fires conducted on federal lands.</p><p>For 10 years, Interior and USDA must annually conduct prescribed fires on federal land so that the total acreage where prescribed fires are conducted is 10% greater than the previous fiscal year.\u00a0</p><p>Interior and USDA must establish a collaborative prescribed fire program to provide financial assistance to eligible entities to conduct prescribed fires in priority landscapes.</p><p>Interior and USDA may enter into cooperative agreements or contracts with states, Indian tribes, counties, municipal governments, fire districts, nongovernmental organizations, or private entities to coordinate prescribed fires on federal land.</p><p>Interior and USDA must expand employment opportunities for prescribed fire practitioners, including by expanding hazard pay, supporting underrepresented groups, and establishing additional training centers.\u00a0</p><p>To address the public health and safety risk of the expanded use of prescribed fire, the Environmental Protection Agency must coordinate with state, tribal, and local air quality agencies to support the environmental review of wildland fires.</p>"
        },
        "title": "National Prescribed Fire Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2015.xml",
    "summary": {
      "actionDate": "2025-06-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>National Prescribed Fire Act of 2025</strong></p><ul></ul><p>This bill directs the Department of Agriculture (USDA) and the Department of the Interior to increase the number and size of prescribed fires conducted on federal lands.</p><p>For 10 years, Interior and USDA must annually conduct prescribed fires on federal land so that the total acreage where prescribed fires are conducted is 10% greater than the previous fiscal year.\u00a0</p><p>Interior and USDA must establish a collaborative prescribed fire program to provide financial assistance to eligible entities to conduct prescribed fires in priority landscapes.</p><p>Interior and USDA may enter into cooperative agreements or contracts with states, Indian tribes, counties, municipal governments, fire districts, nongovernmental organizations, or private entities to coordinate prescribed fires on federal land.</p><p>Interior and USDA must expand employment opportunities for prescribed fire practitioners, including by expanding hazard pay, supporting underrepresented groups, and establishing additional training centers.\u00a0</p><p>To address the public health and safety risk of the expanded use of prescribed fire, the Environmental Protection Agency must coordinate with state, tribal, and local air quality agencies to support the environmental review of wildland fires.</p>",
      "updateDate": "2026-02-11",
      "versionCode": "id119s2015"
    },
    "title": "National Prescribed Fire Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>National Prescribed Fire Act of 2025</strong></p><ul></ul><p>This bill directs the Department of Agriculture (USDA) and the Department of the Interior to increase the number and size of prescribed fires conducted on federal lands.</p><p>For 10 years, Interior and USDA must annually conduct prescribed fires on federal land so that the total acreage where prescribed fires are conducted is 10% greater than the previous fiscal year.\u00a0</p><p>Interior and USDA must establish a collaborative prescribed fire program to provide financial assistance to eligible entities to conduct prescribed fires in priority landscapes.</p><p>Interior and USDA may enter into cooperative agreements or contracts with states, Indian tribes, counties, municipal governments, fire districts, nongovernmental organizations, or private entities to coordinate prescribed fires on federal land.</p><p>Interior and USDA must expand employment opportunities for prescribed fire practitioners, including by expanding hazard pay, supporting underrepresented groups, and establishing additional training centers.\u00a0</p><p>To address the public health and safety risk of the expanded use of prescribed fire, the Environmental Protection Agency must coordinate with state, tribal, and local air quality agencies to support the environmental review of wildland fires.</p>",
      "updateDate": "2026-02-11",
      "versionCode": "id119s2015"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2015is.xml"
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
      "title": "National Prescribed Fire Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "National Prescribed Fire Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of the Interior and the Secretary of Agriculture to encourage and expand the use of prescribed fire on land managed by the Department of the Interior or the Forest Service, with an emphasis on units of the National Forest System in the western and southeastern United States, to acknowledge and support the long-standing use of cultural burning by Indian Tribes and Indigenous practitioners, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:18Z"
    }
  ]
}
```
