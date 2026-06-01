# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/717?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/717
- Title: Wildlife Movement Through Partnerships Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 717
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-04-03T08:05:45Z
- Update date including text: 2026-04-03T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/717",
    "number": "717",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "Z000018",
        "district": "1",
        "firstName": "Ryan",
        "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
        "lastName": "Zinke",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Wildlife Movement Through Partnerships Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:45Z",
    "updateDateIncludingText": "2026-04-03T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:07:50Z",
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "VA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NM"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "VA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "OR"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr717ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 717\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Zinke (for himself and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish the Wildlife Movement and Movement Area Grant Program and the State and Tribal Migration Research Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildlife Movement Through Partnerships Act of 2025 .\n#### 2. Purpose\nThe purpose of this Act is to provide financial and technical assistance for the purposes of promoting connectivity by improving habitat quality in movement areas by migratory big game and other wildlife\u2014\n**(1)**\nto identify and conserve movement areas by methods of science and management expertise employed by State and Tribal wildlife agencies and other wildlife professionals; and\n**(2)**\nto coordinate and advance the purposes of\u2014\n**(A)**\nSecretarial Order 3362, entitled Improving Habitat Quality in Western Big-Game Winter Range and Migration Corridors and issued by the Secretary on February 9, 2018;\n**(B)**\nthe wildlife crossings pilot program established under section 171(b) of title 23, United States Code; and\n**(C)**\nthe Migratory Big Game Initiative of the Department of Agriculture.\n#### 3. Definitions\nIn this Act:\n**(1) Big game**\nThe term big game means native species of large mammals, including deer, elk, pronghorn, wild sheep, and moose, for which State and Tribal wildlife agencies have established regulated means and methods of take.\n**(2) Connectivity**\nThe term connectivity means the degree to which a species of wildlife moves within and among areas of its habitat.\n**(3) Eligible recipient**\nThe term eligible recipient means\u2014\n**(A)**\na State fish and wildlife agency or other State agency responsible for managing natural resources or wildlife;\n**(B)**\na State department of transportation;\n**(C)**\nan Indian Tribe;\n**(D)**\na nonprofit organization described in section 501(c) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code, or a coalition of those organizations, including an organization that represents private landowners;\n**(E)**\nan institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ));\n**(F)**\na national or regional association representing a State or Tribal fish and wildlife agency;\n**(G)**\na Federal agency that may carry out projects that would support the purpose of this Act; and\n**(H)**\na county government.\n**(4) Federal land**\nThe term Federal land means land or water managed by the relevant agencies.\n**(5) Foundation**\nThe term Foundation means the National Fish and Wildlife Foundation established by section 2(a) of the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701(a) ).\n**(6) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(7) Movement area**\nThe term movement area means\u2014\n**(A)**\nan area wildlife frequently use, or could frequently use, to move, including for travel within, or colonization, of additional habitat by wildlife that occurs seasonally or more frequently in and around corridors; or\n**(B)**\nseasonal habitat where migration or other natural movement of big game and other wildlife has been observed and documented by\u2014\n**(i)**\na State or Tribal wildlife agency; or\n**(ii)**\n**(I)**\na scientific report published in a peer-reviewed professional publication; or\n**(II)**\nany other professional scientific publication recognized by a State or Tribal wildlife agency.\n**(8) Relevant agencies**\nThe term relevant agencies means\u2014\n**(A)**\nthe Department of the Interior, including the United States Fish and Wildlife Service, the Bureau of Indian Affairs, the Bureau of Land Management, the National Park Service, and the United States Geological Survey;\n**(B)**\nthe Department of Agriculture, including the Forest Service, the Natural Resources Conservation Service, and the Farm Service Agency; and\n**(C)**\nthe Department of Transportation.\n**(9) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(10) Wildlife**\nThe term wildlife means native terrestrial vertebrate species.\n#### 4. Wildlife Movement and Movement Area Grant Program\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a nonregulatory program, to be known as the Wildlife Movement and Movement Area Grant Program (referred to in this section as the grant program ).\n##### (b) Purpose\nThe purpose of the grant program is to fund projects that improve or conserve habitat quality in movement areas, including projects that\u2014\n**(1)**\nsecure habitat leases, fence modification, non-Federal land acquisition, conservation easements, improved hydrology, human-wildlife vehicle collision reduction, and road and infrastructure modification;\n**(2)**\narrange voluntary collaboration with landowners; and\n**(3)**\ncoordinate efforts among State and Tribal governments, including departments of transportation and other relevant agencies.\n##### (c) Cooperative agreement\nNot later than 1 year after the date of enactment of this Act, the Secretary shall enter into a cooperative agreement with the Foundation to administer the grant program for purposes of providing competitive matching grants in varying amounts to eligible recipients.\n##### (d) Grants\n**(1) Proposals**\n**(A) In general**\nNot later than 180 days after the date on which amounts are made available to carry out the grant program, and not less frequently than annually thereafter, the Foundation, in consultation with the Secretary, shall issue a request for proposals for projects to fund under the grant program.\n**(B) Requirements**\nA proposal submitted to the Foundation by an eligible recipient for funding under the grant program shall identify 1 or more movement areas where habitat improvement will be achieved, subject to the condition that the proposal shall include written acknowledgment of support from a State or Tribal fish and wildlife agency with jurisdiction over the movement area in which the proposal will be carried out.\n**(2) Cost sharing**\n**(A) Federal share**\nExcept as provided in subparagraph (C), the Federal share of the cost of a project funded under the grant program shall not exceed 90 percent of the total cost of the project.\n**(B) Non-Federal share**\nThe non-Federal share of the cost of a project funded under the grant program\u2014\n**(i)**\nexcept as provided in subparagraph (C), shall be not less than 10 percent of the total cost of the project; and\n**(ii)**\nmay be provided in cash or in-kind, as determined by the Foundation.\n**(C) Waiver**\nThe Foundation may waive the requirements under subparagraphs (A) and (B) for projects that would benefit Indian Tribes, historically disadvantaged communities, or areas of persistent poverty, as determined by the Foundation.\n##### (e) Requirement\nAfter the date on which the Secretary enters into a cooperative agreement with the Foundation under subsection (c), any amounts received by the Foundation under this section shall be subject to the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701 et seq. ), excluding section 10(a) of that Act ( 16 U.S.C. 3709(a) ).\n##### (f) Priority\nIn funding projects under the grant program, the Foundation may give priority to proposals that are\u2014\n**(1)**\nsubmitted by an eligible recipient described in section 3(3)(F); or\n**(2)**\njointly submitted by multiple eligible recipients.\n##### (g) Funding\nAfter the date on which the Secretary enters into a cooperative agreement with the Foundation under subsection (c), the Foundation shall\u2014\n**(1)**\n**(A)**\nfor each fiscal year, receive amounts made available to carry out the grant program in an advance payment of the entire amount on October 1, or as soon as practicable thereafter, of that fiscal year, to remain available until expended; and\n**(B)**\ninvest and reinvest those amounts for the benefit of the grant program; and\n**(2)**\notherwise administer the grant program to support partnerships between the public and private sectors in accordance with this section.\n##### (h) Report\nNot less frequently than once every 2 years, the Foundation shall submit to the Secretary, the Secretary of Agriculture, the Secretary of Transportation, and Congress a report on projects funded under the grant program and the contribution of those projects to conservation successes.\n##### (i) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to the Secretary to carry out the grant program such sums as are necessary for each of fiscal years 2026 through 2031.\n**(2) Big game**\nOf the amounts made available to carry out the grant program for each fiscal year, not less than 50 percent shall be used for projects that directly conserve, restore, or enhance big game movement areas.\n#### 5. State and Tribal Migration Research Program\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a program, to be known as the State and Tribal Migration Research Program (referred to in this section as the program ), to provide funds directly to State fish and wildlife agencies and Indian Tribes through an agreed on process between States, Indian Tribes, and the relevant agencies, to collect and analyze data on the identification, characteristics, or management of movement areas .\n##### (b) Administration\nFunds provided under this section shall be administered by the Science Applications program of the United States Fish and Wildlife Service.\n##### (c) Authorization of appropriations\nThere are authorized to be appropriated to the Secretary to carry out the program such sums as are necessary for each of fiscal years 2026 through 2031.\n#### 6. Partners for Fish and Wildlife Program\n##### (a) In general\nSection 4 of the Partners for Fish and Wildlife Act ( 16 U.S.C. 3773 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking The Secretary shall carry out the Partners for Fish and Wildlife Program and inserting the following:\n(a) In general The Secretary shall carry out the Partners for Fish and Wildlife Program (referred to in this section as the Program ) ; and\n**(2)**\nby adding at the end the following:\n(b) Use of funds Where prudent and necessary, funds under the Program may be used to provide technical assistance to other Federal agencies to implement voluntary programs with a focus on migration corridor or seasonal habitat conservation efforts on private and Tribal land. .\n##### (b) Reauthorization\nSection 5 of the Partners for Fish and Wildlife Act ( 16 U.S.C. 3774 ) is amended by striking 2019 through 2023 and inserting 2026 through 2031 .\n#### 7. USGS Wildlife Corridor Mapping\nThe Secretary, acting through the Director of the United States Geological Survey, shall support the continuation of a Corridor Mapping Team to provide technical assistance, as prioritized and required by States and Indian Tribes, to Federal agencies, States, and Indian Tribes working\u2014\n**(1)**\nto map movement areas using existing Global Positioning System data or other sources of credible scientific information; and\n**(2)**\nto assess or research movement areas.\n#### 8. USGS existing efforts\n##### (a) USGS existing efforts\n**(1) In general**\nThe Director of the United States Geological Survey shall work with Federal and State agencies and Indian Tribes to build on existing efforts to map movement areas.\n**(2) Protection of information**\nIn carrying out this subsection, the Director of the United States Geological Survey, in cooperation with Federal and State agencies and Indian Tribes, and consistent with rights afforded to sovereign nations and applicable State law, shall carry out necessary measures\u2014\n**(A)**\nto protect sensitive information with respect to the protection of private property rights and the precise locations of individuals; and\n**(B)**\nto prevent the poaching, illegal taking, and unfair chase of wildlife.\n**(3) Reports; published migration maps**\n**(A) In general**\nAnnually, the Director of the United States Geological Survey shall publish a report on completed analyses of mapped migration corridors, seasonal habitats, and connectivity areas.\n**(B) Requirement**\nTo the extent practicable, all efforts shall be made to incorporate data with existing State programs and use existing published maps described in subparagraph (A).\n**(4) Reports**\nNot less frequently than once every 2 years, the Secretary shall submit to Congress a report on projects funded under this subsection, including a description of the conservation value of each project.\n##### (b) Authorization of appropriations\nSection 2 of the Act of September 2, 1960 ( 16 U.S.C. 753b ), is amended to read as follows:\n2. Authorization of appropriations (a) In general There are authorized to be appropriated to carry out this Act such sums as are necessary for each of fiscal years 2026 through 2031. (b) Set-Aside Of the amounts made available to carry out this Act for each fiscal year, not less than 50 percent shall be used for projects that promote connectivity by improving habitat quality in movement areas of big game and other wildlife. .\n#### 9. Coordination\n##### (a) In general\nThe Secretary shall appoint a Senior Executive Service employee, who has experience with big game movement, to serve in the Office of the Secretary as coordinator of activities and necessary staff to carry out this Act and the amendments made by this Act.\n##### (b) Authority and responsibilities\nThe Senior Executive Service employee appointed under subsection (a) shall\u2014\n**(1)**\nadvise and assist\u2014\n**(A)**\nState and Tribal agencies and other eligible recipients;\n**(B)**\nrelevant Federal agencies and programs; and\n**(C)**\nthe Foundation; and\n**(2)**\nmaintain an informative summary of activities, and the results of those activities, carried out under this Act.\n##### (c) Interagency coordination\nThe Secretaries, or their authorized representatives, of the relevant agencies shall regularly convene\u2014\n**(1)**\nto coordinate actions and funding across Federal agencies for programs under this Act and the amendments made by this Act; and\n**(2)**\nto streamline coordination with States, Indian Tribes, and non-governmental partners with respect to those actions and that funding.\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section such sums as are necessary for each of fiscal years 2026 through 2031.\n#### 10. Requirement; savings provision\n##### (a) Requirement\nNo funds obligated under this Act or an amendment made by this Act shall be applied in a manner that requires non-voluntary changes in agricultural or domestic livestock production, permitted forestry practices, or access to valid existing rights, such as for energy development and mining, or water rights, consistent with Federal organic Acts and associated regulations.\n##### (b) Savings provision\nNothing in this Act or an amendment made by this Act\u2014\n**(1)**\nenlarges or diminishes the authority, jurisdiction, or responsibility of a State to manage, control, or regulate fish and wildlife under the law and regulations of the State on land and waters within the State, including on Federal land;\n**(2)**\nmodifies or abrogates a treaty with any Indian Tribe or enlarges or diminishes the authority, jurisdiction, or responsibility of an Indian Tribe to manage, control, or regulate wildlife on Tribal land;\n**(3)**\nimpacts the private property or privacy rights of landowners;\n**(4)**\nrestricts or reduces public access for hunting, angling, recreational shooting, or other compatible types of outdoor recreation;\n**(5)**\naffects military readiness for training occurring on land of the Department of the Interior reserved by the Department of the Defense;\n**(6)**\nconstitutes a Federal land designation or federally designated migration route, an alteration or removal of such a designation, or a directive to impact pre-existing administrative or management authority in any manner; or\n**(7)**\namends or otherwise affects any other Federal law (including regulations) relating to the conservation of native species.",
      "versionDate": "2025-01-23",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-03-19T18:17:34Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-03-19T18:17:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-27T21:12:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr717",
          "measure-number": "717",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2026-01-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr717v00",
            "update-date": "2026-01-13"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Wildlife Movement Through Partnerships Act of 2025</strong></p><p>This bill establishes additional support for wildlife movement areas. It also reauthorizes and modifies (1) the Partners for Fish and Wildlife Program, and (2) wildlife-related cooperative research and training programs.</p><p>Specifically, the bill establishes within the Department of the Interior a grant program for projects that improve or conserve habitat quality in movement areas of terrestrial vertebrate species. At least 50% of the amounts made available to carry out the grant program must be used for projects that directly conserve, restore, or enhance big game movement areas.</p><p>Interior must also establish a research program that provides funds to state fish and wildlife agencies and Indian tribes to collect and analyze data on the identification, characteristics, or management of movement areas.</p><p>The bill reauthorizes through FY2031 and expands the Partners for Fish and Wildlife Program to allow Interior to use program funds to provide technical assistance to other federal agencies to implement voluntary programs with a focus on migration corridor or seasonal habitat conservation efforts on private and tribal land.</p><p>The bill also reauthorizes through FY2031 cooperative research and training programs for fish and wildlife resources. At least 50% of the funding\u00a0must be used for projects that improve habitat quality in movement areas of big game and other wildlife.</p><p>Additionally, the bill directs the U.S. Geological Survey to work with, and provide technical assistance to, federal agencies, states, and Indian tribes to build on existing efforts to map movement areas.</p>"
        },
        "title": "Wildlife Movement Through Partnerships Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr717.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildlife Movement Through Partnerships Act of 2025</strong></p><p>This bill establishes additional support for wildlife movement areas. It also reauthorizes and modifies (1) the Partners for Fish and Wildlife Program, and (2) wildlife-related cooperative research and training programs.</p><p>Specifically, the bill establishes within the Department of the Interior a grant program for projects that improve or conserve habitat quality in movement areas of terrestrial vertebrate species. At least 50% of the amounts made available to carry out the grant program must be used for projects that directly conserve, restore, or enhance big game movement areas.</p><p>Interior must also establish a research program that provides funds to state fish and wildlife agencies and Indian tribes to collect and analyze data on the identification, characteristics, or management of movement areas.</p><p>The bill reauthorizes through FY2031 and expands the Partners for Fish and Wildlife Program to allow Interior to use program funds to provide technical assistance to other federal agencies to implement voluntary programs with a focus on migration corridor or seasonal habitat conservation efforts on private and tribal land.</p><p>The bill also reauthorizes through FY2031 cooperative research and training programs for fish and wildlife resources. At least 50% of the funding\u00a0must be used for projects that improve habitat quality in movement areas of big game and other wildlife.</p><p>Additionally, the bill directs the U.S. Geological Survey to work with, and provide technical assistance to, federal agencies, states, and Indian tribes to build on existing efforts to map movement areas.</p>",
      "updateDate": "2026-01-13",
      "versionCode": "id119hr717"
    },
    "title": "Wildlife Movement Through Partnerships Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildlife Movement Through Partnerships Act of 2025</strong></p><p>This bill establishes additional support for wildlife movement areas. It also reauthorizes and modifies (1) the Partners for Fish and Wildlife Program, and (2) wildlife-related cooperative research and training programs.</p><p>Specifically, the bill establishes within the Department of the Interior a grant program for projects that improve or conserve habitat quality in movement areas of terrestrial vertebrate species. At least 50% of the amounts made available to carry out the grant program must be used for projects that directly conserve, restore, or enhance big game movement areas.</p><p>Interior must also establish a research program that provides funds to state fish and wildlife agencies and Indian tribes to collect and analyze data on the identification, characteristics, or management of movement areas.</p><p>The bill reauthorizes through FY2031 and expands the Partners for Fish and Wildlife Program to allow Interior to use program funds to provide technical assistance to other federal agencies to implement voluntary programs with a focus on migration corridor or seasonal habitat conservation efforts on private and tribal land.</p><p>The bill also reauthorizes through FY2031 cooperative research and training programs for fish and wildlife resources. At least 50% of the funding\u00a0must be used for projects that improve habitat quality in movement areas of big game and other wildlife.</p><p>Additionally, the bill directs the U.S. Geological Survey to work with, and provide technical assistance to, federal agencies, states, and Indian tribes to build on existing efforts to map movement areas.</p>",
      "updateDate": "2026-01-13",
      "versionCode": "id119hr717"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr717ih.xml"
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
      "title": "Wildlife Movement Through Partnerships Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:51Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildlife Movement Through Partnerships Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Wildlife Movement and Movement Area Grant Program and the State and Tribal Migration Research Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:48Z"
    }
  ]
}
```
