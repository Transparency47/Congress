# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2301?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2301
- Title: To promote the development of renewable energy on public land, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 2301
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2025-04-24T08:05:15Z
- Update date including text: 2025-04-24T08:05:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-24 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-24 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-18 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2301",
    "number": "2301",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To promote the development of renewable energy on public land, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-04-24T08:05:15Z",
    "updateDateIncludingText": "2025-04-24T08:05:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:08:00Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-24T16:02:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2301ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2301\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Levin introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo promote the development of renewable energy on public land, and for other purposes.\n#### 1. Definitions\nIn this Act:\n**(1) Covered land**\nThe term covered land means land that is\u2014\n**(A)**\nFederal land;\n**(B)**\nnot excluded from the development of geothermal, solar, or wind energy under\u2014\n**(i)**\na land use plan; or\n**(ii)**\nother Federal law; and\n**(C)**\nnot included in an area\u2014\n**(i)**\nthat is subject to the Desert Renewable Energy Conservation Plan developed by the California Energy Commission, the California Department of Fish and Wildlife, the Bureau of Land Management, and the United States Fish and Wildlife Service; or\n**(ii)**\nfor which the Secretary determines existing wind and solar energy land use planning meets or exceeds the standards established under section 3.\n**(2) Energy storage project**\nThe term energy storage project means equipment that\u2014\n**(A)**\nreceives, stores, and delivers energy using batteries, compressed air, pumped hydropower, hydrogen storage (including hydrolysis), thermal energy storage, regenerative fuel cells, flywheels, capacitors, superconducting magnets, or other technologies identified by the Secretary of Energy; and\n**(B)**\nhas a storage capacity of not less than 5 kilowatt hours.\n**(3) Exclusion area**\nThe term exclusion area means covered land that is identified by the Bureau of Land Management as not suitable for development of renewable energy projects.\n**(4) Federal land**\nThe term Federal land means\u2014\n**(A)**\npublic land; and\n**(B)**\nNational Forest System lands administered by the Department of Agriculture through the Forest Service where the Secretary has authority to issue leases for the development and utilization of geothermal resources under section 3 and section 15 of the Geothermal Steam Act of 1970 ( 30 U.S.C. 1002 , 1014).\n**(5) Fund**\nThe term Fund means the Renewable Energy Resource Conservation Fund established by section 6(c)(1).\n**(6) Land use plan**\nThe term land use plan means\u2014\n**(A)**\nwith respect to public land, a land use plan established under the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); and\n**(B)**\nwith respect to National Forest System land, a land management plan approved, amended, or revised under section 6 of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1604 ).\n**(7) National Forest System**\nThe term National Forest System has the meaning given the term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609(a) ).\n**(8) Priority area**\nThe term priority area means covered land identified by the land use planning process of the Bureau of Land Management as being a preferred location for a renewable energy project, including an area that is identified as a designated leasing area under the rule of the Bureau of Land Management entitled Competitive Processes, Terms, and Conditions for Leasing Public Lands for Solar and Wind Energy Development and Technical Changes and Corrections (81 Fed. Reg. 92122 (December 19, 2016)) (or a successor regulation).\n**(9) Public land**\nThe term public land has the meaning given the term public lands in section 103 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1702 ).\n**(10) Renewable energy project**\nThe term renewable energy project \u2014\n**(A)**\nmeans a project carried out on covered land that\u2014\n**(i)**\nuses wind, solar, or geothermal energy to generate energy; or\n**(ii)**\ntransmits electricity to support wind, solar, or geothermal energy generation; and\n**(B)**\nmay include an associated energy storage project.\n**(11) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 2. Updating national goals for renewable energy production on Federal land\nSection 3104 of the Energy Act of 2020 ( 43 U.S.C. 3004 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby striking 25 and inserting 60 ; and\n**(B)**\nby striking 2025 and inserting December 31, 2030 ; and\n**(2)**\nby adding at the end the following:\n(c) Update Not later than 18 months after the date of enactment of this subsection, the Secretary, in consultation with the Secretary of Agriculture and the heads of other relevant Federal agencies, shall update the national goals for renewable energy production on Federal land established under subsection (a). .\n#### 3. Land use planning and updates to programmatic environmental impact statements\n##### (a) Priority areas\n**(1) Establishment of priority areas; designation of areas eligible for the submission of renewable energy project applications**\n**(A) In general**\nFor purposes of renewable energy planning, the Secretary, consistent with the requirements described in subparagraph (B), shall\u2014\n**(i)**\ndesignate areas on covered land eligible for the submission of renewable energy project applications; and\n**(ii)**\nconsider establishing priority areas on covered land for renewable energy projects.\n**(B) Requirements**\nIn carrying out activities under clauses (i) and (ii) of subparagraph (A), the Secretary shall comply with\u2014\n**(i)**\nthe principles of multiple use (as defined in section 103 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1702 )); and\n**(ii)**\nthe national goals for renewable energy production established under section 3104 of the Energy Act of 2020 ( 43 U.S.C. 3004 ), including the minimum production goal described in subsection (b) of that section.\n**(2) Priority for certain applications**\nIn considering applications for renewable energy projects on covered land, with respect to an application for a proposed renewable energy project on covered land that is to be carried out in a priority area, the Secretary shall\u2014\n**(A)**\nprioritize the application to be carried out in any identified priority area; and\n**(B)**\non approval of the application, provide to the applicant who submitted the application the opportunity to participate in any regional mitigation plan developed for the applicable priority area.\n**(3) Programmatic planning**\n**(A) Solar energy**\nAs soon as practicable, but not later than 18 months after the Record of Decision titled Approved Record of Decision and Amendments/Record of Decision for Utility-Scale Solar Energy Development dated December 2024 was issued, the Secretary shall consider establishing priority areas on covered land for Solar energy projects in the planning area (as defined in the Record of Decision).\n**(B) Wind energy**\nAs soon as practicable, but not later than 1 year after the date of enactment of this Act, the Secretary shall initiate a review of the final programmatic Environment Impact Statement referenced in the notice of availability entitled Notice of Availability of the Final Programmatic Environmental Impact Statement on Wind Energy Development on BLM\u2013Administered Lands in the Western United States, Including Proposed Amendments to Selected Land Use Plans (70 Fed. Reg. 36651 (June 24, 2005)), that considers establishment of wind application and priority areas on covered lands, and complete that review within 3 years of issuing a notice of intent.\n##### (b) Review and modification\n**(1) In general**\nSubject to paragraph (2), not less frequently than once every 10 years, the Secretary shall\u2014\n**(A)**\nafter an opportunity for public comment, review the adequacy of all land allocations for renewable energy projects for the purposes of\u2014\n**(i)**\nencouraging and facilitating new renewable energy projects; and\n**(ii)**\nconsistent with a mitigation sequence of avoiding, minimizing, and compensating for adverse impacts to other public uses and values of covered land, including\u2014\n**(I)**\nwildlife habitat;\n**(II)**\nspecies listed as threatened or endangered under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. );\n**(III)**\nwater resources;\n**(IV)**\ncultural resources;\n**(V)**\nrecreational uses;\n**(VI)**\nland with wilderness characteristics;\n**(VII)**\nland with special management designations; and\n**(VIII)**\nareas of Tribal importance; and\n**(B)**\nbased on the review carried out under subparagraph (A), add, modify, or eliminate priority areas, exclusion areas, and areas on covered land open or closed to solar or wind energy right-of-way applications or to geothermal leasing.\n**(2) Limitation**\nParagraph (1) shall not apply to any covered land that the Secretary determines, after seeking public input, is subject to an existing land use plan that meets the purposes described in paragraph (1)(A).\n**(3) Report**\nIf the Secretary determines, in an annual report required under subsection (g) of section 3102 of the Energy Act of 2020 ( 43 U.S.C. 3002 ) (as redesignated by section 4(a)(1)), that the national goal for renewable energy production established under subsection (a) of section 3104 of that Act ( 43 U.S.C. 3004 ), including the minimum production goal established under subsection (b) of that section, may not be met, the Secretary shall act more frequently than otherwise required by this section to designate areas eligible for the submission of renewable energy project applications and establish additional priority areas for renewable energy projects.\n##### (c) Compliance with the national environmental policy act of 1969\nFor purposes of this section, compliance with the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) shall be accomplished\u2014\n**(1)**\nfor geothermal energy\u2014\n**(A)**\nby updating the document entitled Final Programmatic Environmental Impact Statement for Geothermal Leasing in the Western United States and dated October 2008; and\n**(B)**\nby incorporating into the updated document under subparagraph (A) any additional regional analyses completed by Federal agencies after the date on which the document described in that subparagraph was finalized;\n**(2)**\nfor solar energy\u2014\n**(A)**\nby updating the document entitled Final Programmatic Environmental Impact Statement (PEIS) for Solar Energy Development in Six Southwestern States and dated July 2012; and\n**(B)**\nby incorporating into the updated document under subparagraph (A) any additional regional analyses completed by Federal agencies after the date on which the document described in that subparagraph was finalized; and\n**(3)**\nfor wind energy\u2014\n**(A)**\nby updating the document entitled Final Programmatic Environmental Impact Statement on Wind Energy Development on BLM\u2013Administered Lands in the Western United States and dated June 2005; and\n**(B)**\nby incorporating into the updated document under subparagraph (A) any additional regional analyses completed by Federal agencies after the date on which the document described in that subparagraph was finalized.\n##### (d) No effect on processing site-Specific applications\nNothing in this section modifies any requirement to conduct site-specific environmental reviews or process permits for proposed renewable energy projects during preparation of an updated programmatic environmental impact statement, land use plan, or amendment to a land use plan.\n##### (e) Coordination\nIn developing any update required under this section, the Secretary shall coordinate, on an ongoing basis, with appropriate State, Tribal, and local governments, transmission infrastructure owners, operators, and developers, renewable energy developers, and other appropriate entities to ensure that priority areas established by the Secretary under this section take into account\u2014\n**(1)**\neconomic viability (including having access to existing or planned transmission lines);\n**(2)**\nconsistency with a mitigation sequence to avoid, minimize, and compensate for impacts to\u2014\n**(A)**\nfish, wildlife, or plants;\n**(B)**\nfish, wildlife, or plant habitat;\n**(C)**\nrecreational uses;\n**(D)**\nland with wilderness characteristics;\n**(E)**\nland with special management designations;\n**(F)**\ncultural resources;\n**(G)**\nareas of Tribal importance; and\n**(H)**\nother uses of covered land;\n**(3)**\nfeasibility of siting on previously disturbed land, including commercial and industrial land, mine land, and previously contaminated sites; and\n**(4)**\nconsistency with section 202 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1712 ), including subsection (c)(9) of that section ( 43 U.S.C. 1712(c)(9) ).\n##### (f) Transmission\nIn carrying out this section, the Secretary shall\u2014\n**(1)**\ndetermine whether adequate transmission exists for renewable energy projects on covered land; and\n**(2)**\nif a determination is made in the negative under paragraph (1), in coordination with the heads of other relevant Federal agencies, review existing land use plans to determine if amendments to those land use plans would be appropriate to support adequate transmission capability.\n##### (g) Incentives for renewable energy development in priority areas\nThe Secretary may establish, by regulation, incentives to be provided to individuals carrying out renewable energy projects in priority areas established under this section.\n#### 4. Improving wind and solar energy project permitting\n##### (a) Role of Renewable Energy Coordination Offices\nSection 3102 of the Energy Act of 2020 ( 43 U.S.C. 3002 ) is amended\u2014\n**(1)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively; and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Processing of Wind and Solar energy applications (1) Delegation to State Renewable Energy Coordination Offices (A) In general Notwithstanding any other provision of law, the Secretary may delegate to a State Renewable Energy Coordination Office the authority to process applications for eligible projects proposed to be carried out on land managed by the Bureau of Land Management in the applicable State. (B) Roles and responsibilities of managers For purposes of processing applications described in subparagraph (A), the manager of the applicable State Renewable Energy Coordination Office\u2014 (i) shall have the authority to issue grants or leases for eligible projects; (ii) with the approval of the State Director of the applicable Bureau of Land Management State Office, may use other employees in field and district offices of the applicable Bureau of Land Management State Office, or hire additional experts, to assist with timely processing of applications, with the costs of hiring additional experts to be charged to applicants; and (iii) shall report to the State Director of the applicable Bureau of Land Management State Office. (2) Prohibition of delegation to employees of field or district offices Except as provided in paragraph (1)(B)(ii), the Secretary may not delegate to employees of field or district offices of the Bureau of Land Management the authority to process applications for eligible projects proposed to be carried out on land managed by the Bureau of Land Management. .\n##### (b) Cost recovery agreements\n**(1) In general**\nNot later than 30 days after the date on which an applicant submits a complete application for a right-of-way for a wind or solar energy project, including submission of the filing fee required under section 2804.12 of title 43, Code of Federal Regulations (or a successor regulation), the Secretary shall provide a cost recovery agreement with respect to the application.\n**(2) Effect**\nIssuance of a cost recovery agreement under paragraph (1) and payment of cost recovery fees shall preclude any new claims to the use of the applicable covered land during any period in which the application is active.\n**(3) Conflicts; studies**\n**(A) Conflicts**\nTo be considered complete under paragraph (1), an application described in that paragraph shall address any known conflicts with respect to the use of the applicable covered land, as identified in scientific literature or other studies.\n**(B) Additional studies**\nAdditional studies shall not be required for purposes of considering an application to be complete under paragraph (1).\n##### (c) Environmental requirements\n**(1) Notice of intent**\n**(A) In general**\nNot later than 180 days after the date on which the agency notifies the applicant that the application to establish a right-of-way is complete, or a later date to be established by the Secretary under subparagraph (B), if an environmental impact statement is determined to be necessary, the Secretary shall issue a notice of intent to prepare an environmental impact statement with respect to the application.\n**(B) Extension**\nThe Secretary shall establish a later date by which the notice under subparagraph (A) shall be issued, if the Secretary determines that the 180-day period under that paragraph should be extended due to\u2014\n**(i)**\nthe application being considered a low priority under section 2804.35 of title 43, Code of Federal Regulations (or a successor regulation);\n**(ii)**\nproject-specific circumstances, including the need for further studies, making the 180-day deadline insufficient; or\n**(iii)**\nthe application not meeting the requirements for approval.\n**(2) Categorical exclusion**\nAs the Secretary determines to be appropriate, the Secretary may promulgate regulations providing that preliminary geotechnical work and meteorological monitoring relating to renewable energy projects shall be categorically excluded from the requirements for an environmental assessment or environmental impact statement under section 1501.4 of title 40, Code of Federal Regulations (or a successor regulation).\n##### (d) Processing priority\nIn processing applications described in subsection (b)(1), the Secretary shall\u2014\n**(1)**\ngive priority to applications for renewable energy projects in priority areas; and\n**(2)**\nprocess applications for renewable energy projects in areas that are not priority areas in the order in which the applications are received.\n##### (e) Use of competitive process\n**(1) In general**\nSubject to paragraph (2), the Secretary shall not use a competitive process for the review of an application described in subsection (b)(1), except\u2014\n**(A)**\nin a case in which 2 or more applicants file an application for the same site (or portions of the same site) not more than 15 days apart; or\n**(B)**\nas otherwise established by the Secretary through a subsequent rulemaking process delineating the instances in which the Secretary will use the competitive process.\n**(2) Limitation**\nParagraph (1) shall not apply to applications for competitive right-of-way leases in priority areas.\n#### 5. Increasing economic certainty\n##### (a) Rents and fees\n**(1) In general**\nIn determining rental rates and other fees for renewable energy project leases or right-of-way grants, the Secretary shall ensure that the total rental rates and other fees charged do not exceed the average amount charged for similar activities on private land in the State or county in which the rental rates and other fees are charged.\n**(2) Individual appraisals not required**\nFor purposes of determining rental rates for renewable energy projects, the Secretary\u2014\n**(A)**\nshall not be required to conduct individual appraisals; and\n**(B)**\nmay use average cash rents included in the Pastureland Rents Survey prepared by the National Agricultural Statistics Service, as determined for the 5-year period ending on the date on which the rental rate is determined.\n**(3) Increases in base rental rates**\nAfter a base rental rate is established for a lease or right-of-way grant authorization for a renewable energy project, any increase in the base rental rate shall be limited to the Implicit Price Deflator-Gross Product Index published by the Bureau of Economic Analysis of the Department of Commerce on the date of issuance of the lease or right-of way grant authorization.\n**(4) Capacity fees**\nThe Secretary may consider charging a capacity fee for a renewable energy project only if the Secretary determines that capacity fees are charged within the region or State in which the renewable energy project is carried out, as part of leaseholds on State or private land.\n##### (b) Bonds\nThe Secretary shall adopt a process for establishing bond requirements for decommissioning renewable energy projects that\u2014\n**(1)**\ndo not establish a minimum per acre amount; and\n**(2)**\nare based on the difference between\u2014\n**(A)**\nthe estimated, site-specific net costs of reclamation of the covered land; and\n**(B)**\nthe salvage value of materials available after decommissioning the renewable energy project.\n#### 6. Disposition of revenues; Renewable Energy Resource Conservation Fund\n##### (a) Disposition of revenues\n**(1) Availability**\nExcept as provided in paragraph (3), without further appropriation or fiscal year limitation, of amounts collected from wind and solar energy projects as bonus bids, rentals, fees, or other payments under a right-of-way, permit, lease, or other authorization\u2014\n**(A)**\nfor the period beginning on January 1, 2026, and ending on December 31, 2045\u2014\n**(i)**\n25 percent shall be paid by the Secretary of the Treasury to the State within the boundaries of which the revenue is derived;\n**(ii)**\n25 percent shall be paid by the Secretary of the Treasury to the 1 or more counties within the boundaries of which the revenue is derived, to be allocated among the counties based on the percentage of land from which the revenue is derived;\n**(iii)**\n15 percent shall be deposited in the Treasury and credited to the Bureau of Land Management\u2019s Renewable Energy Management account to be made available to the Secretary to carry out sections 3 and 4 (including amendments made by those sections), including the transfer of the funds by the Bureau of Land Management to other Federal agencies and State agencies to facilitate the processing of permits for renewable energy projects, with priority given to using the amounts, to the maximum extent practicable, without detrimental impacts to emerging markets, expediting the issuance of permits required for the development of wind and solar energy projects in the States from which the revenues are derived; and\n**(iv)**\n35 percent shall be deposited in the Fund; and\n**(B)**\nbeginning on January 1, 2046\u2014\n**(i)**\n25 percent shall be paid by the Secretary of the Treasury to the State within the boundaries of which the revenue is derived;\n**(ii)**\n25 percent shall be paid by the Secretary of the Treasury to the 1 or more counties within the boundaries of which the revenue is derived, to be allocated among the counties based on the percentage of land from which the revenue is derived;\n**(iii)**\n10 percent shall be deposited in the Treasury and be made available to the Secretary to carry out sections 3 and 4 (including amendments made by those sections), including the transfer of the funds by the Bureau of Land Management to other Federal agencies and State agencies to facilitate the processing of permits for wind and solar energy projects, with priority given to using the amounts, to the maximum extent practicable, without detrimental impacts to emerging markets, expediting the issuance of permits required for the development of renewable energy projects in the States from which the revenues are derived; and\n**(iv)**\n40 percent shall be deposited in the Fund.\n**(2) Rule for projects located in multiple states**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall issue a proposed rule establishing a formula for the disposition of revenues under subparagraphs (A)(i) and (B)(i) of paragraph (1) in a case in which a wind and solar energy project is located in more than 1 State.\n**(3) Filing fees**\nWith respect to wind and solar energy projects\u2014\n**(A)**\nparagraph (1) does not apply to amounts collected from application filing fees authorized under section 304 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1734 ); and\n**(B)**\nsuch application filing fees may be retained by the applicable agency to recover costs associated with issuing the right-of-way, permit, or other authorization associated with the application.\n##### (b) Payments to states and counties\n**(1) In general**\nAmounts paid to States and counties under subsection (a)(1) shall be used consistent with section 35 of the Mineral Leasing Act ( 30 U.S.C. 191 ).\n**(2) Payments in lieu of taxes**\nA payment to a county under subparagraph (A)(ii) or (B)(ii) of subsection (a)(1) shall be in addition to a payment in lieu of taxes received by the county under chapter 69 of title 31, United States Code.\n##### (c) Renewable energy resource conservation fund\n**(1) In general**\nThere is established in the Treasury a fund, to be known as the Renewable Energy Resource Conservation Fund , which shall be administered by the Secretary.\n**(2) Use of funds**\n**(A) In general**\nThe Secretary may make amounts in the Fund available to Federal, State, local, and Tribal agencies for distribution in regions in which renewable energy projects are located on Federal land, for the purposes described in subparagraph (B).\n**(B) Purposes**\nThe purposes referred to in subparagraph (A) are\u2014\n**(i)**\nrestoring and protecting\u2014\n**(I)**\nfish and wildlife habitat for species affected by renewable energy projects;\n**(II)**\nfish and wildlife corridors for species affected by renewable energy projects; and\n**(III)**\nwetlands, streams, rivers, and other natural water bodies in areas affected by renewable energy projects; and\n**(ii)**\npreserving and improving recreational access to Federal land and water in the applicable region through an easement, right-of-way, or other instrument from willing landowners for the purpose of enhancing public access to existing Federal land and water that is inaccessible or restricted due to renewable energy projects.\n**(3) Cooperative agreements**\nThe Secretary may enter into cooperative agreements with State and Tribal agencies, nonprofit organizations, and other appropriate entities to carry out the activities described in paragraph (2).\n**(4) Investment of fund**\n**(A) In general**\nAny amounts deposited in the Fund shall earn interest in an amount determined by the Secretary of the Treasury on the basis of the current average market yield on outstanding marketable obligations of the United States of comparable maturities.\n**(B) Use**\nAny interest earned under subparagraph (A) may be deposited into the Fund and used without further appropriation.\n**(5) Report to congress**\nAt the end of each fiscal year, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives a report identifying\u2014\n**(A)**\nthe amounts described in subsection (a) that were collected during that fiscal year, organized by source;\n**(B)**\nthe amount and purpose of payments made to each Federal, State, local, and Tribal agency under paragraph (2) during that fiscal year; and\n**(C)**\nthe amount remaining in the Fund at the end of the fiscal year.\n**(6) Intent of congress**\nIt is the intent of Congress that the revenues deposited and expended from the Fund shall supplement (and not supplant) annual appropriations for activities described in paragraph (2).\n#### 7. Savings clause\nNotwithstanding any other provision of this Act, the Secretary and the Secretary of Agriculture shall continue to manage public land under the principles of multiple use and sustained yield in accordance with title I of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ) or the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1600 et seq. ), as applicable, for the purposes of land use planning, permit processing, and conducting environmental reviews.",
      "versionDate": "2025-03-24",
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
        "name": "Energy",
        "updateDate": "2025-04-08T11:46:00Z"
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
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2301ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote the development of renewable energy on public land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T02:48:18Z"
    },
    {
      "title": "To promote the development of renewable energy on public land, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T08:06:04Z"
    }
  ]
}
```
