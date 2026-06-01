# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3738?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3738
- Title: MORE WATER Act
- Congress: 119
- Bill type: S
- Bill number: 3738
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-04-02T18:23:55Z
- Update date including text: 2026-04-02T18:23:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S380-381)
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S380-381)
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3738",
    "number": "3738",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "MORE WATER Act",
    "type": "S",
    "updateDate": "2026-04-02T18:23:55Z",
    "updateDateIncludingText": "2026-04-02T18:23:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S380-381)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T19:27:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:30Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3738is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3738\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Padilla introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to reauthorize the large-scale water recycling and reuse program, to establish a Water Conveyance Improvement Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making Our communities Resilient through Enhancing Water for Agriculture, Technology, the Environment, and Residences Act or the MORE WATER Act .\n#### 2. Reauthorization of large-scale water recycling and reuse program\nSection 40905 of the Infrastructure Investment and Jobs Act ( 43 U.S.C. 3205 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (1) through (4) as paragraphs (2) through (5), respectively; and\n**(B)**\nby inserting before paragraph (2) (as so redesignated) the following:\n(1) Construction The term construction has the meaning given the term in subsection (f) of section 4011 of the Water Infrastructure Improvements for the Nation Act ( Public Law 114\u2013322 ; 130 Stat. 1881), except that any reference in paragraph (2) of that subsection to storage shall be deemed to be a reference to infrastructure . ;\n**(2)**\nby striking subsection (b) and inserting the following:\n(b) Establishment The Secretary shall establish a program to provide grants to eligible entities on a competitive basis for the development of feasibility studies, planning, design, and construction of large-scale water recycling and reuse projects that provide substantial water supply and other benefits to the Reclamation States in accordance with this section. ;\n**(3)**\nin subsection (d)(4), by striking 30 and inserting 60 ;\n**(4)**\nin subsection (k)\u2014\n**(A)**\nby striking The authority and inserting the following:\n(1) In general Except as provided in paragraph (2), the authority ;\n**(B)**\nin paragraph (1) (as so designated), by striking 5 and inserting 10 ; and\n**(C)**\nby adding at the end the following:\n(2) Exception Paragraph (1) shall not apply to an eligible project that is under construction as of the termination date described in that paragraph. ; and\n**(5)**\nby adding at the end the following:\n(l) Authorization of appropriations There is authorized to be appropriated to the Secretary to provide grants for eligible projects and otherwise carry out this section $450,000,000 for the period of fiscal years 2028 through 2032. .\n#### 3. Water Conveyance Improvement Program\n##### (a) Definitions\nIn this section:\n**(1) Conveyance project**\nThe term conveyance project means a project for the undertaking of a new or improved water conveyance facility, or the restoration of the capacity of an existing water conveyance facility, that is located in a Reclamation State.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State, Indian Tribe, municipality, irrigation district, water district, wastewater district, or any State or regional organization with statutory water or power delivery authority;\n**(B)**\na State, regional, or local authority, the members of which include 1 or more organizations that\u2014\n**(i)**\nhave water or power delivery authority; or\n**(ii)**\nare responsible for operating conveyance facilities as a transferred works under the reclamation laws and Bureau of Reclamation policy;\n**(C)**\nan agency established under State law for the joint exercise of powers; and\n**(D)**\nany combination of entities described in subparagraphs (A) through (C).\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term Indian tribe in section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 ).\n**(4) Low-income community**\nThe term low-income community has the meaning given the term in section 45D(e) of the Internal Code of 1986 (including any regulations issued under that section), including Tribal communities.\n**(5) Multi-benefit project**\nThe term multi-benefit project means a conveyance project that provides in the region of the conveyance project benefits that include not fewer than 1 of the following quantified, significant benefits:\n**(A)**\nSafe drinking water benefits for low-income communities.\n**(B)**\nEnvironmental benefits.\n**(6) Program**\nThe term Program means the Water Conveyance Improvement Program established under subsection (b).\n**(7) Project proponent**\nThe term project proponent means an eligible entity that\u2014\n**(A)**\nplans and develops a non-Federal conveyance project; or\n**(B)**\noperates an existing Reclamation project that is a transferred works.\n**(8) Project sponsor**\nThe term project sponsor means an eligible entity that contributes to the non-Federal share of a conveyance project.\n**(9) Reclamation project**\nThe term Reclamation project means a Bureau of Reclamation project that is owned by the United States.\n**(10) Reclamation State**\nThe term Reclamation State means a State or territory described in the first section of the Act of June 17, 1902 ( 43 U.S.C. 391 ; 32 Stat. 388, chapter 1093).\n**(11) Safe drinking water**\nThe term safe drinking water means water that meets all applicable Federal and State primary and secondary drinking water standards.\n**(12) Secretary**\nThe term Secretary means the Secretary of the Interior (acting through the Commissioner of Reclamation).\n**(13) Stakeholder**\nThe term stakeholder means\u2014\n**(A)**\nwith respect to safe drinking water benefits for low-income communities\u2014\n**(i)**\n**(I)**\nan elected executive official with applicable authority or legislative body representing a low-income community (or a delegate); and\n**(II)**\nany agency exercising primary enforcement responsibility for public water systems in the State in which the applicable project is located;\n**(ii)**\nan Indian Tribe receiving safe drinking water benefits; or\n**(iii)**\na nonprofit organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of that Code with\u2014\n**(I)**\na demonstrated track record of supporting improved access to safe drinking water for low-income communities in the region of the applicable project; and\n**(II)**\nno financial conflict of interest with the project proponent or any project sponsor, except that other instances of partnership on similar projects shall not be considered a financial conflict of interest for purposes of this subclause; and\n**(B)**\nwith respect to environmental benefits\u2014\n**(i)**\na nonprofit organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of that Code with\u2014\n**(I)**\na demonstrated track record of supporting environmental restoration in the region of the applicable project, including species or species habitat; and\n**(II)**\nno financial conflict of interest with the project proponent or any project sponsor, except that other instances of partnership on similar projects shall not be considered a financial conflict of interest for purposes of this subclause; or\n**(ii)**\nan Indian Tribe, if the project is within the current or former reservation or aboriginal territory of the Indian Tribe.\n**(14) Water supply benefit**\nThe term water supply benefit means\u2014\n**(A)**\nan irrigation benefit;\n**(B)**\na general drinking water benefit; and\n**(C)**\noperational flexibility that allows the Bureau of Reclamation to provide multiple benefits, including any of the benefits described in subparagraphs (A) and (B).\n##### (b) Establishment of program\nThe Secretary shall establish within the Bureau of Reclamation a Water Conveyance Improvement Program to provide authority to participate in, and provide grants to, conveyance projects.\n##### (c) Reclamation-Led conveyance projects\n**(1) In general**\nOn the request of any State, department, agency, or subdivision of a State, or any public agency organized pursuant to State law, the Secretary may provide a grant to, and enter into an agreement on behalf of the United States for the design, study, and construction of, a conveyance project as part of a new Reclamation project, a new division of a Reclamation project, a new supplemental works on a Reclamation project, or the restoration or improvement of the capacity of an existing Reclamation project, in accordance with this subsection.\n**(2) Project commencement**\nThe construction of a conveyance project that is the subject of an agreement under this subsection shall not commence until the date on which the Secretary\u2014\n**(A)**\ndetermines that the conveyance project is feasible in accordance with the reclamation laws; and\n**(B)**\nsecures an agreement providing the funding necessary to pay the non-Federal share of the costs of the conveyance project in accordance with subsection (e).\n**(3) Feasibility determination**\nIn determining feasibility under paragraph (2)(A), the Secretary shall review and approve a feasibility analysis provided by a project sponsor if the Secretary determines that the analysis meets Bureau of Reclamation policy relating to the preparation of a feasibility study.\n##### (d) Non-Federal conveyance projects\n**(1) Proposal**\n**(A) In general**\nA project proponent may submit to the Secretary a proposal for the design, study, and construction of a conveyance project to be provided a grant under this section.\n**(B) Form**\nThe project proponent may submit a proposal under subparagraph (A) in the form of a completed feasibility study or any other means that provide information to support a determination that the conveyance project is eligible for a grant in accordance with paragraph (2).\n**(2) Requirements**\nThe Secretary may provide to the project proponent a grant for a conveyance project and enter into an agreement on behalf of the United States with the project proponent for the administration of the grant if\u2014\n**(A)**\nthe project proponent determines, and the Secretary concurs, through the preparation of a feasibility study that is streamlined to the maximum extent practicable, that the conveyance project\u2014\n**(i)**\nis technically and financially feasible; and\n**(ii)**\nis consistent with applicable Federal and State law;\n**(B)**\nthe project proponent has sufficient non-Federal funding available to complete the conveyance project, as determined by the Secretary;\n**(C)**\nthe project proponent is financially solvent, as determined by the Secretary; and\n**(D)**\nnot later than 60 days after the date on which the Secretary concurs with the determination under subparagraph (A) with respect to the conveyance project, the Secretary submits to Congress written notice of the determination.\n##### (e) Cost-Sharing requirement\n**(1) In general**\nThe Federal share of a conveyance project funded under this section shall not exceed 50 percent of the total cost of studies, planning, design, and construction of the conveyance project.\n**(2) Projects that are not multi-benefit**\nThe Federal share of a conveyance project other than a multi-benefit project funded under this section may be used\u2014\n**(A)**\nsolely for water supply benefits; or\n**(B)**\non the approval by the Secretary and, in the case of a non-Federal conveyance project or an existing Reclamation project that is a transferred works, at the request of the project proponent, for a combination of\u2014\n**(i)**\nwater supply benefits;\n**(ii)**\nsafe drinking water benefits for low-income communities;\n**(iii)**\nenvironmental benefits; or\n**(iv)**\nother benefits in accordance with the reclamation laws.\n**(3) Multi-benefit projects**\nIn the case of a multi-benefit project funded under this section\u2014\n**(A)**\nthe Federal share of not more than 30 percent of the costs of studies, planning, design, and construction of the multi-benefit project may be used for any of the benefits described in paragraph (2); and\n**(B)**\nan additional Federal share of not more than 20 percent of the costs of studies, planning, design, and construction of the multi-benefit project may be used for\u2014\n**(i)**\nquantified, significant safe drinking water benefits for low-income communities in accordance with subsection (f)(2)(A);\n**(ii)**\nquantified, significant environmental benefits described in subsection (f)(3); or\n**(iii)**\na combination of the benefits described in clauses (i) and (ii).\n**(4) Agreement**\nThe project proponent or the Secretary, in the case of any Reclamation-led conveyance project that is a new project or involves a reserved works, shall enter into an agreement with 1 or more applicable stakeholders representing multi-benefit interests that describes the benefits authorized under paragraph (3)(B) proposed for the conveyance project.\n**(5) Form of non-Federal share**\nThe non-Federal share of the cost of a conveyance project funded under this section may be in the form of\u2014\n**(A)**\ncash;\n**(B)**\nin-kind contributions;\n**(C)**\nreimbursable funding allocated pursuant to any statutory authority, if the eligible entity has entered into a repayment contract for the funding;\n**(D)**\na loan under the Water Infrastructure Finance and Innovation Act of 2014 ( 33 U.S.C. 3901 et seq. ) or any other Federal loan program;\n**(E)**\namounts made available from a State revolving fund pursuant to the rules of the applicable State; or\n**(F)**\nother non-Federal sources of funding, including State funding.\n##### (f) Special provisions applicable to multi-Benefit projects\n**(1) Requirement**\n**(A) In general**\nA conveyance project with a total cost of not less than $800,000,000 that is funded under this section shall be a multi-benefit project.\n**(B) Less than $800,000,000**\nThe Secretary shall ensure that not less than 50 percent of conveyance projects with a total cost of less than $800,000,000 that are funded under this section shall be multi-benefit projects.\n**(2) Description of safe drinking water benefits for low-income communities**\n**(A) In general**\nThe Federal funding for quantified, significant safe drinking water benefits for low-income communities referred to in subsection (e)(3)(B)(i) may be provided\u2014\n**(i)**\ndirectly, by paying for a sufficient proportion of the capacity of the conveyance project (or, in the case of a conveyance project restoring the original capacity of a conveyance facility, paying for sufficient water from the conveyance project) and any additional infrastructure necessary to deliver safe drinking water to a low-income community or other resource or facility accessible to the community;\n**(ii)**\nindirectly, by\u2014\n**(I)**\nsupporting a low-income ratepayer assistance program for a project sponsor, a member agency of a project sponsor, or a drinking water district in the region of the conveyance project; or\n**(II)**\ncontributing to a Federal or State program that assists in delivering safe drinking water to low-income communities;\n**(iii)**\nindirectly, by paying for a sufficient proportion of the project capacity during high-flow periods to provide a specific quantity of water (or, in the case of a conveyance project restoring the original capacity of a conveyance facility, paying for sufficient water from the conveyance project), with 1 of the project sponsors in return delivering the same quantity of water to the community through an exchange, banking water in a groundwater basin during times of excess for subsequent delivery to the low-income community;\n**(iv)**\nindirectly, by paying for enhancement, repair, or upgrades to a Bureau of Indian Affairs conveyance facility in the region of the project;\n**(v)**\nby any other direct or indirect means to provide safe drinking water to a low-income community; or\n**(vi)**\nthrough a combination of the methods authorized under clauses (i) through (v).\n**(B) Delivery of water for drinking**\nDelivery of water for drinking purposes shall be considered to be safe drinking water benefits for low-income communities for purposes of this section if\u2014\n**(i)**\nfacilities exist to treat the water that is to become safe drinking water; or\n**(ii)**\nthe stakeholders representing the applicable low-income communities agree that there are viable plans and funding sources (including Federal or State funding) to treat the delivered water or exchanged water that is to become safe drinking water.\n**(C) Inclusion**\nAny benefits described in subparagraph (A) that are safe drinking water benefits for low-income ratepayers shall be considered to meet the requirements for safe drinking water benefits for low-income communities under this section.\n**(D) Effect**\nNothing in this section requires a project proponent or project sponsor to pay for treatment of water delivered to low-income communities, other than low-income communities with which the project proponent or the project sponsor has an existing contractual relationship to deliver treated water.\n**(3) Description of environmental benefits**\nThe quantified, significant environmental benefits referred to in subsection (e)(3)(B)(ii) include\u2014\n**(A)**\nbenefits to a species listed as threatened or endangered under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) or other species of concern affected by operation of Reclamation projects or State or local water projects;\n**(B)**\nadditional flows to an inland water body, including the Great Salt Lake, either directly or indirectly through an exchange;\n**(C)**\nbenefits that improve aquatic or terrestrial habitats in the region of the proposed conveyance project;\n**(D)**\ncontributions to a Federal or State program that provides environmental benefits in the region of the project;\n**(E)**\ndelivery of additional water to wildlife refuges, either directly or indirectly through an exchange; or\n**(F)**\nstrategically designed actions that simultaneously achieve environmental and other benefits, such as habitat restoration or efforts to recover species that\u2014\n**(i)**\nimprove the operation of the conveyance project; or\n**(ii)**\nhave water supply or flood protection benefits.\n**(4) Types of projects**\nOf the multi-benefit projects funded under this section, the Secretary shall ensure that, to the maximum extent practicable\u2014\n**(A)**\n50 percent provide at least some environmental benefits (or a combination of environmental benefits and safe drinking water benefits for low-income communities); and\n**(B)**\n50 percent provide at least some safe drinking water benefits for low-income communities (or a combination of safe drinking water benefits for low-income communities and environmental benefits).\n**(5) Phased funding of multi-benefit projects**\n**(A) In general**\nDuring the first 2 years in which a multi-benefit project is being constructed, the applicable project sponsor may apply for and receive Federal funds for construction costs authorized under subsection (e)(3)(A), subject to subparagraph (C).\n**(B) Design**\nSubject to the provisions of this paragraph, to the maximum extent practicable, the project proponent shall seek to integrate environmental benefits and safe drinking water benefits for low-income communities into the design of the applicable multi-benefit project.\n**(C) Requirement**\nTo be eligible for Federal funds under subparagraph (A), the applicable project proponent shall\u2014\n**(i)**\ncommit to include safe drinking water benefits for low-income communities or environmental benefits in the multi-benefit project on the date on which Federal funds are provided under that subparagraph;\n**(ii)**\ndemonstrate that the project sponsor is in negotiations to add multi-benefit project elements with stakeholders representing the environment or safe drinking water for low-income communities; and\n**(iii)**\nnot later than 2 years after the date on which the project sponsor first receives construction funding for the project under subsection (e)(3)(A), submit a proposal for additional funding under subsection (e)(3)(B) that is consistent with the applicable agreement entered into under subsection (e)(4).\n**(D) Required ratio**\n**(i) In general**\nSubject to clauses (ii) and (iii), on submission of a proposal for additional funding under subparagraph (C)(iii), for any subsequent 5-year period for which Federal funds are made available for the applicable multi-benefit project under this section\u2014\n**(I)**\n60 percent shall be made available for costs relating to the benefits referred to in subsection (e)(3)(A); and\n**(II)**\n40 percent shall be made available for costs relating to environmental benefits or safe drinking water benefits for low-income communities in accordance with this subsection.\n**(ii) Modification**\nNotwithstanding clause (i), the project proponent or the Secretary, in the case of any Reclamation-led conveyance project that is a new project or involves a reserved works, and any stakeholders representing multi-benefit interests subject to an agreement referred to in subsection (e)(4) may by mutual agreement modify the ratio of funding for different components of the conveyance project established under clause (i) for funding over the specified 5-year period.\n**(iii) Allocation of total funding**\nThe Secretary shall ensure that the total allocation of funding for a multi-benefit project shall reflect the ratio of funding established under clause (i).\n##### (g) Criteria for selecting conveyance projects\nIn determining whether to select a conveyance project for a grant under this section, the Secretary shall consider\u2014\n**(1)**\nthe Federal benefits of the conveyance project;\n**(2)**\nwhether the conveyance project, in the judgment of the Secretary, is well-designed to achieve the benefits of the conveyance project at a reasonable cost;\n**(3)**\nwhether the conveyance project meets a critical need at the national, State, regional, or local level;\n**(4)**\nwhether the conveyance project assists the Federal Government in honoring contracts of the Federal Government;\n**(5)**\ndiversity in the geography and size of conveyance projects; and\n**(6)**\nsuch other factors as the Secretary determines appropriate.\n##### (h) Total dollar cap\nThe Secretary shall not impose a total dollar cap on Federal funds under this section for any individual conveyance project funded under the Program.\n##### (i) New conveyance facility\nNo Federal funds are authorized under this section for any new conveyance facility that costs more than $5,000,000,000.\n##### (j) Reimbursability of funds\nAny Federal funds provided by the Secretary under the Program shall be nonreimbursable to the United States, including\u2014\n**(1)**\nfunding of Reclamation-led conveyance projects under subsection (c); and\n**(2)**\ngrants to eligible entities for non-Federal conveyance projects under subsection (d).\n##### (k) Funding eligibility\nA conveyance project shall not be considered ineligible for funding under the Program on the basis of the conveyance project receiving assistance under any other Federal funding program or Federal joint use agreement.\n##### (l) Applicable law\nA conveyance project funded under the Program shall be consistent with applicable Federal, State, and Tribal law.\n##### (m) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $500,000,000 for the period of fiscal years 2028 through 2032.\n#### 4. Reauthorization of recycling program and environmental restoration program\n##### (a) Authorization of new water recycling and reuse projects\nSection 1602(g) of the Reclamation Wastewater and Groundwater Study and Facilities Act ( 43 U.S.C. 390h(g) ) is amended by striking paragraph (1) and inserting the following:\n(1) There is authorized to be appropriated to the Secretary of the Interior to carry out this section $550,000,000 for the period of fiscal years 2028 through 2032. .\n##### (b) Ceiling on Federal share\nSection 1631(d)(1) of the Reclamation Wastewater and Groundwater Study and Facilities Act ( 43 U.S.C. 390h\u201313(d)(1) ) is amended by striking $20,000,000 (October 1996 prices) and inserting $50,000,000 (in December 2025 prices, as automatically adjusted each January based on the percentage increase in the consumer price index for all urban consumers (United States city average) over the previous year, as published by the Bureau of Labor Statistics) .\n##### (c) Actions for benefit of endangered species, important habitat, and water bodies\nSection 4010(b) of the Water Infrastructure Improvements for the Nation Act ( Public Law 114\u2013322 ; 130 Stat. 1872) is amended by striking paragraph (2) and inserting the following:\n(2) Actions for benefit of endangered species, important habitat, and water bodies There is authorized to be appropriated to the Secretary of the Interior (acting through the Commissioner of Reclamation) $250,000,000 for the period of fiscal years 2028 through 2032\u2014 (A) for the restoration of habitat or improvement of conditions at the Great Salt Lake and other saline inland lakes affected by the operation of the Central Utah Project or Bureau of Reclamation water projects or deliveries; (B) for\u2014 (i) gravel and rearing area additions, fish passage improvements, barrier removal, and habitat restoration to the Sacramento River, its tributaries, or other rivers or river basins affected by the operation of Bureau of Reclamation facilities to benefit species listed as threatened or endangered under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), including Chinook salmon and steelhead trout; (ii) scientifically improved and increased real-time monitoring to inform real-time operations of Bureau of Reclamation facilities, and alternative methods, models, and equipment to improve temperature modeling, science, and monitoring to support flow benefits for fish species, and related forecasted information for purposes of predicting impacts to salmon, salmon habitat, species listed as threatened or endangered under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), or other species of concern as a result of water management at Bureau of Reclamation facilities; (iii) aquatic habitat restoration activities, including floodplain reconnection and reactivation projects (such as off-channel and managed floodplain inundation projects that enhance biological productivity and food web support for fish) that enhance the ability of the Bureau of Reclamation to meet contractual obligations for water deliveries; (iv) fish hatchery modernization and construction projects; and (v) structural or operational improvements, including temperature control and associated facilities, necessary to implement activities described in clauses (i) through (iv); and (C) for planning, design, scientific studies, resource and biological monitoring, environmental reviews, permitting, construction, implementation, and adaptive management associated with any of the activities described in subparagraphs (A) and (B). .\n#### 5. Offset from extension of certain provisions\nSection 4013 of the Water Infrastructure Improvements for the Nation Act ( 43 U.S.C. 390b note; Public Law 114\u2013322 ) is amended\u2014\n**(1)**\nin paragraph (1), by striking and at the end;\n**(2)**\nin paragraph (2), by striking in and inserting under ;\n**(3)**\nby redesignating paragraph (2) as paragraph (3); and\n**(4)**\nby inserting after paragraph (1) the following:\n(2) section 4009(c), section 4010(b)(2), and subsections (a), (b), (c), (d), and (f) of section 4011, which shall expire 15 years after that date of enactment; and .\n#### 6. Deauthorization of inactive projects offset\n##### (a) Purposes\nThe purposes of this section are\u2014\n**(1)**\nto establish an efficient and transparent process for deauthorizing Reclamation projects that have failed to receive a minimum level of investment to ensure active Reclamation projects can move forward while reducing the backlog of authorized Reclamation projects; and\n**(2)**\nto allow for exceptions for the deauthorization of Reclamation projects under paragraph (1) based on\u2014\n**(A)**\naction by Congress;\n**(B)**\nfunding to completion by the non-Federal project sponsor; or\n**(C)**\na finding by the Secretary that certain Reclamation projects should continue to be authorized to meet vitally important needs of a State or the United States.\n##### (b) Definitions\nIn this section:\n**(1) Reclamation project**\nThe term Reclamation project means a project that is\u2014\n**(A)**\nowned by the United States; and\n**(B)**\nconstructed and operated under the direction of the Bureau of Reclamation.\n**(2) Secretary**\nThe term Secretary means the Secretary of the Interior (acting through the Commissioner of Reclamation).\n##### (c) Interim deauthorization list\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives and make available on a publicly accessible internet website in a manner that is downloadable, searchable, and sortable\u2014\n**(1)**\nan interim deauthorization list of Reclamation projects\u2014\n**(A)**\nthat are authorized; and\n**(B)**\nfor which funding was not obligated during the fiscal year in which this Act is enacted or any of the preceding 7 fiscal years; and\n**(2)**\nfor each Reclamation project listed under paragraph (1)\u2014\n**(A)**\nthe date of authorization of the Reclamation project, including any subsequent modifications to the original authorization;\n**(B)**\na brief description of the Reclamation project;\n**(C)**\nthe estimated cost of completion of the Reclamation project; and\n**(D)**\nany remaining amounts authorized, but not appropriated, for the Reclamation project.\n##### (d) Final deauthorization list\n**(1) In general**\nNot later than 1 year after the date on which the interim deauthorization list is submitted under subsection (c), the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives and make available on a publicly accessible internet website in a manner that is downloadable, searchable, and sortable, a final deauthorization list of all Reclamation projects identified in the interim deauthorization list, other than any Reclamation project\u2014\n**(A)**\nfor which funding has been provided by an Act of Congress after the date of submission of the interim deauthorization list; or\n**(B)**\nthat the Secretary excludes under paragraph (2).\n**(2) Exclusions**\nThe Secretary may exclude from the final deauthorization list under paragraph (1) a Reclamation project that the Secretary determines is vitally important for the interests of the United States or a particular State, based on consideration of the effects of the Reclamation project on\u2014\n**(A)**\npublic health and safety;\n**(B)**\nthe economy; or\n**(C)**\nthe environment.\n##### (e) Deauthorization; congressional review\nEffective beginning on the date that is 1 year after the date of submission of the final deauthorization list under subsection (d), a Reclamation project included on the final deauthorization list under that subsection is deauthorized, unless, prior to that date\u2014\n**(1)**\na joint resolution disapproving the final deauthorization report is enacted into law;\n**(2)**\nfunding for the Reclamation project has been provided by an Act of Congress; or\n**(3)**\nthe non-Federal sponsor of the Reclamation project provides sufficient funds to complete the Reclamation project.",
      "versionDate": "2026-01-29",
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
            "name": "California",
            "updateDate": "2026-04-02T18:23:29Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-02T18:23:49Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2026-04-02T18:23:12Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-04-02T18:22:59Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2026-04-02T18:23:35Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-02T18:23:55Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2026-04-02T18:23:24Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-04-02T18:23:05Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-04-02T18:23:18Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2026-04-02T18:22:53Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-04-02T18:22:38Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-04-02T18:22:45Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-04-02T18:23:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-02-23T21:58:01Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3738is.xml"
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
      "title": "MORE WATER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MORE WATER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Making Our communities Resilient through Enhancing Water for Agriculture, Technology, the Environment, and Residences Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Infrastructure Investment and Jobs Act to reauthorize the large-scale water recycling and reuse program, to establish a Water Conveyance Improvement Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:34Z"
    }
  ]
}
```
