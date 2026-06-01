# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3654?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3654
- Title: TERRA Act
- Congress: 119
- Bill type: HR
- Bill number: 3654
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-05-12T08:06:11Z
- Update date including text: 2026-05-12T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-09-04 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-09-09 - Committee: Subcommittee Hearings Held
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-09-04 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-09-09 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3654",
    "number": "3654",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "R000621",
        "district": "6",
        "firstName": "Emily",
        "fullName": "Rep. Randall, Emily [D-WA-6]",
        "lastName": "Randall",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "TERRA Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:06:11Z",
    "updateDateIncludingText": "2026-05-12T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-09-09T19:07:51Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-09-04T21:42:10Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "WA"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "ID"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "KS"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "PA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "WA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "MI"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CO"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MI"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "OK"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3654ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3654\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Ms. Randall (for herself, Ms. Perez , Mr. Simpson , Ms. Davids of Kansas , Mr. Huffman , Mr. Mullin , Mr. Fitzpatrick , Ms. Strickland , and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize the integration and administrative streamlining of Federal funding for Indian Tribes that have reservations, other Tribal lands, or ways of life at risk due to environmental impacts and natural disasters, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Tribal Emergency Response Resources Act or the TERRA Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Statement of purpose.\nSec.\u20023.\u2002Definitions.\nSec.\u20024.\u2002Lead agency.\nTitle I\u2014Program Components; Plan Development and Approval\nSec.\u2002101.\u2002Integration of Federal programs authorized.\nSec.\u2002102.\u2002Eligible Federal programs.\nSec.\u2002103.\u2002Activities authorized under a Plan.\nSec.\u2002104.\u2002Plan requirements.\nSec.\u2002105.\u2002Technical assistance.\nSec.\u2002106.\u2002Plan submission and review.\nSec.\u2002107.\u2002Waiver authority.\nSec.\u2002108.\u2002Plan approval or denial.\nTitle II\u2014Plan Implementation; Funding Administration; Interdepartmental Memorandum of Agreement; Report\nSec.\u2002201.\u2002Reduced reporting requirements.\nSec.\u2002202.\u2002Streamlined permitting and review implementation.\nSec.\u2002203.\u2002Expedited fee-to-trust process for Plan implementation.\nSec.\u2002204.\u2002Streamlined funding framework implementation.\nSec.\u2002205.\u2002Transfer and distribution of funds.\nSec.\u2002206.\u2002Administration of funds.\nSec.\u2002207.\u2002No reduction in amounts.\nSec.\u2002208.\u2002Interdepartmental memorandum of agreement.\nSec.\u2002209.\u2002Report required.\n#### 2. Statement of purpose\nThe purpose of this Act is to empower Indian Tribes that have reservations, other Tribal lands, or ways of life at risk due to environmental impacts and natural disasters, including but not limited to flooding, erosion, sea level rise, permafrost degradation, ocean acidification, extended drought, extreme temperatures, tsunamis, storm surges, and more frequent and severe wildfires, hurricanes, and tornadoes, to integrate funding from multiple eligible Federal programs into comprehensive Plans designed to meet the needs of those Indian Tribes and their communities with respect to preventing or addressing those environmental impacts or natural disasters, including by community-driven relocation, if applicable, while\u2014\n**(1)**\nreducing administrative, reporting, and accounting costs; and\n**(2)**\nserving Tribally determined goals consistent with the policy of self-determination, the unique Government-to-Government relationship between the Government of the United States and the Governments of Indian Tribes, and the unique Federal trust responsibility to Indian Tribes and Indian people assumed by the United States, including all Federal agencies.\n#### 3. Definitions\nFor the purposes of this Act:\n**(1) Affected agency**\nThe term affected agency means a Federal agency that administers a program that has been integrated, or is being proposed for integration, into a Plan.\n**(2) Community-driven relocation**\nThe term community-driven relocation means any voluntary, Tribally led climate adaptation strategy that may involve moving all or part of a Tribal community from an area prone to environmental hazards to a safer area, such as plans and projects for protect-in-place, managed retreat, and full-scale relocation efforts, which may include, but are not limited to, demolition and construction of new housing, utilities, and infrastructure.\n**(3) Coordinated project schedule**\nThe term coordinated project schedule means the coordinated project schedule required under section 202(c)(1).\n**(4) Department**\nThe term Department means the Department of the Interior.\n**(5) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code.\n**(6) Federal partner**\nThe term Federal partner means each of\u2014\n**(A)**\nthe Department;\n**(B)**\nthe Department of Agriculture;\n**(C)**\nthe Department of Commerce;\n**(D)**\nthe Department of Defense;\n**(E)**\nthe Department of Energy;\n**(F)**\nthe Department of Health and Human Services;\n**(G)**\nthe Department of Homeland Security;\n**(H)**\nthe Department of Housing and Urban Development;\n**(I)**\nthe Department of Justice;\n**(J)**\nthe Department of Transportation;\n**(K)**\nthe Department of the Treasury;\n**(L)**\nthe Environmental Protection Agency;\n**(M)**\nthe Federal Communications Commission;\n**(N)**\nthe Federal Energy Regulatory Commission;\n**(O)**\nthe Advisory Council on Historic Preservation; and\n**(P)**\nany other Federal agency that operates a program that is proposed by an Indian Tribe and determined eligible by the Secretary for integration into a Plan under this Act.\n**(7) Federal program**\nThe term Federal program means any Federal program or Federal funding source that an Indian Tribe integrates or seeks to integrate into the Plan of the Indian Tribe.\n**(8) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(9) NEPA**\nThe term NEPA means the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n**(10) Participating agency**\nThe term participating agency means a Federal agency that, regardless of whether the Federal agency is a Federal partner or an affected agency\u2014\n**(A)**\nhas review, permitting, or other authorization responsibility with respect to the services or activities to be carried out under a Plan, including but not limited to responsibilities that require review under NEPA, section 306108 of title 54, United States Code (commonly known as the National Historic Preservation Act ), or other applicable Federal law;\n**(B)**\nis designated by the Secretary as a participating agency for that Plan; and\n**(C)**\nparticipates in the streamlined permitting and review procedures for implementing that Plan, in accordance with section 202.\n**(11) Plan**\nThe term Plan means a Plan authorized under this Act.\n**(12) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(13) Traditional Ecological Knowledge**\nThe term Traditional Ecological Knowledge means a body of observations, oral and written knowledge, innovations, practices, and beliefs developed by Indian Tribes through long-term interaction and experience with the environment passed from generation to generation, that continues to evolve and may only be obtained with an Indian Tribe\u2019s free, prior, and informed consent.\n#### 4. Lead agency\nNotwithstanding any other provision of law\u2014\n**(1)**\nthe lead Federal agency responsible for implementation of this Act is the Department; and\n**(2)**\nunless otherwise provided in this Act, the Secretary possesses sole and exclusive decisionmaking authority for all Federal actions under this Act, including but not limited to the sole and exclusive authority to determine whether a Federal program is eligible for integration into a Plan.\nI\nProgram Components; Plan Development and Approval\n#### 101. Integration of Federal programs authorized\nThe Secretary shall, on approving a proposed Plan submitted by an Indian Tribe under this Act, authorize the Indian Tribe, in accordance with the Plan, to\u2014\n**(1)**\nintegrate funding from eligible Federal programs (referred to in this section as the integrated Federal programs ), including but not limited to implementing any waivers of statutory, regulatory, and administrative requirements, regulations, policies, and procedures granted under section 107;\n**(2)**\ncarry out the core services and activities that would otherwise be provided through the integrated Federal programs in accordance with the designated purposes of the Plan;\n**(3)**\nreallocate, reprogram, consolidate, or rebudget funds from the integrated Federal programs, as needed, among the various services and activities to be carried out under the Plan in accordance with the designated purposes of the Plan, without the need for any waiver to be granted under section 107;\n**(4)**\nif appropriate, and in accordance with the designated purposes of the Plan, reallocate, reprogram, consolidate, or rebudget some or all of the funds from the integrated Federal programs to costs associated with community-driven relocation; and\n**(5)**\nprovide a single report each year, based on the model report developed under section 201(b)\u2014\n**(A)**\nin lieu of reporting, recordkeeping, auditing, or similar requirements or procedures associated with the integrated Federal programs; and\n**(B)**\nwithout the need for a waiver to be granted under section 107.\n#### 102. Eligible Federal programs\nFor a Federal program to be eligible for integration into a Plan, the following criteria must be met with respect to the purpose and nature of funding:\n**(1) Purpose**\nAn Indian Tribe plans to implement the Federal program for a purpose that helps to address environmental resiliency, which may include, but is not limited to, advancing such purpose through\u2014\n**(A)**\nclimate resilience, mitigation, or community-driven relocation;\n**(B)**\ndisaster relief, preparedness, or prevention;\n**(C)**\nenvironmental remediation;\n**(D)**\nhousing;\n**(E)**\ninfrastructure maintenance or development;\n**(F)**\neconomic development;\n**(G)**\nland management (including but not limited to purchasing, leasing, and fee-to-trust);\n**(H)**\ncapacity building;\n**(I)**\nreal estate services;\n**(J)**\nnatural resources management or development;\n**(K)**\nenergy or utility services;\n**(L)**\npublic health or welfare; and\n**(M)**\nany purpose relating to, or otherwise supporting or facilitating, a purpose described in subparagraphs (A) through (L).\n**(2) Nature of funding**\nThe funding of the Federal program is provided to an Indian Tribe based on at least one of the following:\n**(A)**\nThe eligibility of an Indian Tribe or members of an Indian Tribe to receive funds\u2014\n**(i)**\nunder a statutory or administrative formula making funds available to the Indian Tribe or members of the Indian Tribe; or\n**(ii)**\nbased solely or in part on the status of the Indian Tribe or members of the Indian Tribe as Indians under Federal law.\n**(B)**\nThe fact that an Indian Tribe or members of an Indian Tribe have secured funds as a result of a noncompetitive process or a specific designation.\n**(C)**\nA competitive process under which Indian Tribes are designated eligible recipients, regardless of whether the competitive funding is for the benefit of the Indian Tribe because of the status of the Indian Tribe or the status of the beneficiaries the funding serves.\n**(D)**\nBlock grant funds provided to an Indian Tribe, regardless of whether the block grant is for the benefit of the Indian Tribe because of the status of the Indian Tribe or the status of the beneficiaries the grant serves.\n#### 103. Activities authorized under a Plan\nFederal funding integrated into a Plan shall be expended (including but not limited to reallocating, reprogramming, consolidating, or rebudgeting the funds) for purposes\u2014\n**(1)**\nconsistent with the core services or activities that otherwise would have been provided or carried out under the Federal programs integrated into the Plan; or\n**(2)**\nrelating to community-driven relocation.\n#### 104. Plan requirements\n##### (a) In general\nA Plan submitted by an Indian Tribe to the Secretary for approval shall\u2014\n**(1)**\nidentify the Federal programs to be integrated into the Plan;\n**(2)**\nbe consistent with the purpose of this Act;\n**(3)**\ndescribe, at the option of the Indian Tribe\u2014\n**(A)**\nthe nature and severity of the environment-related threats to the existing reservation, other Tribal lands, or ways of life of the Indian Tribe; and\n**(B)**\nif applicable, a strategy for community-driven relocation to be addressed by the Plan, that identifies\u2014\n**(i)**\nthe general location of the proposed relocation efforts; and\n**(ii)**\na summary of geospatial information, if available, illustrating\u2014\n**(I)**\nthe proposed relocation area; and\n**(II)**\nif applicable, the locations of environmental, cultural, and historic resources;\n**(4)**\ndescribe the way in which Federal program funds and services are to be integrated, consolidated, and delivered to provide services and carry out activities under the designated purposes of the Plan, including but not limited to provisions that detail how funding sources are anticipated to be coordinated, consistent with section 204(b);\n**(5)**\nidentify any need for taking land into trust for the benefit of the Indian Tribe for environment-related purposes, pursuant to section 203;\n**(6)**\nidentify the projected expenditures under the Plan in a single budget covering all consolidated funds;\n**(7)**\nidentify any Federal environmental or historic preservation reviews, permits, or other authorizations anticipated to be required to be completed or obtained to implement the Plan, including but not limited to any reviews that may be required under NEPA or section 306108 of title 54, United States Code (commonly known as the National Historic Preservation Act );\n**(8)**\nidentify any statutory, regulatory, or administrative requirements, regulations, policies, or procedures that the Indian Tribe believes need to be waived to efficiently and effectively implement the Plan; and\n**(9)**\nbe approved by the governing body of the Indian Tribe, by resolution or other applicable means.\n##### (b) Confidentiality\nTraditional Ecological Knowledge, including but not limited to information relating to natural, cultural, and historical resources, submitted in a Plan shall be\u2014\n**(1)**\nkept confidential; and\n**(2)**\nexempt from the disclosure requirements under\u2014\n**(A)**\nsection 552(b)(3) of title 5, United States Code (commonly known as the Freedom of Information Act );\n**(B)**\nchapter 10 of part I of title 5, United States Code (commonly known as the Federal Advisory Committee Act );\n**(C)**\nthe Open, Public, Electronic, and Necessary Government Data Act (title II of Public Law 115\u2013435 );\n**(D)**\nNEPA; and\n**(E)**\nsimilar disclosure statutes and requirements, as applicable.\n#### 105. Technical assistance\n##### (a) In general\nOn request of an Indian Tribe, the Secretary shall provide technical assistance to the Indian Tribe with respect to any phase or aspect of a Plan, including but not limited to\u2014\n**(1)**\nproject planning and design to develop a proposed Plan for submission; and\n**(2)**\nreview by the Secretary of a draft proposed Plan, in accordance with subsection (b).\n##### (b) Review by secretary\nIf an Indian Tribe requests review of a draft proposed Plan under subsection (a)(2), the Secretary shall\u2014\n**(1)**\nidentify any issues or missing information that may prevent the approval of the draft proposed Plan; and\n**(2)**\nprovide followup technical assistance to resolve any issues identified in paragraph (1), as applicable.\n##### (c) Review not a decision\nA review of a draft proposed Plan under subsection (b) shall not constitute an official Federal agency determination or decision.\n##### (d) Agency consultation\n**(1) In general**\nIn providing technical assistance under subsection (a), on request of the Indian Tribe receiving technical assistance, or as the Secretary determines appropriate, the Secretary shall consult with any Federal agencies anticipated to be affected agencies or participating agencies with respect to the applicable Plan.\n**(2) Scope**\nFederal agencies with which the Secretary consults under paragraph (1) shall provide technical assistance with respect to any requested phase or aspect of a Plan, including but not limited to\u2014\n**(A)**\nwaiver requests under section 107;\n**(B)**\nstreamlined funding frameworks under section 204; and\n**(C)**\ncoordinated project scheduling under section 202(c).\n#### 106. Plan submission and review\n##### (a) Letter of intent\nAn Indian Tribe shall notify the Secretary, in writing, of the intent of the Indian Tribe to prepare a proposed Plan.\n##### (b) Plan consultation\nOn receipt of notice from an Indian Tribe under subsection (a), the Secretary shall consult with the Indian Tribe\u2014\n**(1)**\nto identify potential Federal programs that may be integrated into the proposed Plan; and\n**(2)**\nto identify any waivers of applicable statutory, regulatory, or administrative requirements, regulations, policies, or procedures necessary to enable the Indian Tribe to efficiently and effectively implement the proposed Plan.\n##### (c) Plan submission\nA proposed Plan submitted by an Indian Tribe to the Secretary shall satisfy the requirements of this Act.\n#### 107. Waiver authority\n##### (a) Tribal waiver request\nIn consultation with the Secretary, an Indian Tribe submitting a proposed Plan may include in the proposed Plan a request that the head of an affected agency waive any statutory, regulatory, or administrative requirement, regulation, policy, or procedure that the Indian Tribe considers necessary to enable the Indian Tribe to efficiently and effectively implement the proposed Plan.\n##### (b) Waiver authority\n**(1) In general**\nNotwithstanding any other provision of law, but subject to paragraph (2), the head of an affected agency shall waive any applicable statutory, regulatory, or administrative requirement, regulation, policy, or procedure for which an Indian Tribe has requested a waiver under subsection (a), including but not limited to\u2014\n**(A)**\nmatching requirements;\n**(B)**\ncompetition procedures and other competitive funding requirements;\n**(C)**\nformula funding limitations;\n**(D)**\nrepayment obligations;\n**(E)**\nrequirements to partner with a State or local government or agency, or community organization;\n**(F)**\ndeadlines; and\n**(G)**\nany statutory requirements that may be interpreted to prevent\u2014\n**(i)**\nthe Indian Tribe from receiving funds from multiple, or overlapping, sources of Federal funding; or\n**(ii)**\nthe creation by the head of the affected agency of a funding set-aside for Indian Tribes.\n**(2) Limitation**\nA waiver requested by an Indian Tribe under paragraph (1) shall not be granted if the head of the affected agency determines granting the waiver will be inconsistent with\u2014\n**(A)**\nthe purpose of this Act; or\n**(B)**\nthe provision of law from which the Federal program included in the Plan derives its authority that is specifically applicable to Indians.\n##### (c) Waiver submission and review\n**(1) Determination on waiver request**\nNot later than 45 days after the date on which an Indian Tribe submits a waiver request under subsection (a), the head of the affected agency shall\u2014\n**(A)**\nmake a determination on whether to grant or deny the request; and\n**(B)**\nprovide written notice of the determination and the reasons for the determination to the requesting Indian Tribe and the Secretary.\n**(2) Deemed approval**\nIf the head of an affected agency does not provide written notice to the Indian Tribe of a determination on a waiver request within the 45-day period described in paragraph (1), the waiver request shall be deemed to be granted.\n**(3) Interagency dispute resolution**\n**(A) In general**\nOn request of an Indian Tribe that submitted a waiver request under subsection (a), the Secretary shall initiate an interagency dispute resolution process involving\u2014\n**(i)**\nthe Secretary;\n**(ii)**\nthe Indian Tribe; and\n**(iii)**\nthe head of the affected agency.\n**(B) Timeline**\nA dispute initiated under subparagraph (A) shall be resolved not later than 30 days after the date on which the process is initiated under that subparagraph.\n**(C) Final authority**\nIf the dispute resolution process fails to resolve the dispute between the Indian Tribe and the affected agency, the head of the affected agency shall have the final authority to resolve the dispute.\n**(D) Notice to Indian Tribe**\nNot later than 10 days after the date on which the dispute is resolved under this paragraph, the Secretary shall provide the Indian Tribe with\u2014\n**(i)**\nthe final determination on the waiver request; and\n**(ii)**\nnotice of the right to file a civil action in accordance with section 108(f).\n#### 108. Plan approval or denial\n##### (a) In general\nThe Secretary shall have the sole and exclusive authority to approve or disapprove\u2014\n**(1)**\na Plan submitted by an Indian Tribe; and\n**(2)**\nthe integration of individual Federal programs into the Plan.\n##### (b) Presumption of approval\nBecause Plans promote the policy of self-determination, the Secretary shall review Plans with the presumption of approval.\n##### (c) Approval or denial process\n**(1) In general**\nExcept as provided in subsection (d), not later than 90 days after the date on which the Secretary receives a proposed Plan submitted by an Indian Tribe, the Secretary shall\u2014\n**(A)**\napprove or deny the Plan; and\n**(B)**\nprovide written notice of that decision to the Indian Tribe.\n**(2) Approval**\nIf the Secretary approves a Plan, the Secretary shall authorize the transfer and distribution of funds associated with the Federal programs integrated into the Plan.\n**(3) Denial**\nIf the Secretary denies a Plan, the Secretary shall provide to the Indian Tribe written notification of disapproval that\u2014\n**(A)**\ncontains a specific finding that clearly demonstrates, or that is supported by controlling legal authority, that the Plan does not meet the requirements of this Act; and\n**(B)**\nclearly states any objections contributing to the denial.\n**(4) Partial approval**\nIf the Secretary determines a Plan cannot be approved in its entirety, the Secretary shall approve, with the consent of the applicable Indian Tribe, any portion of the Plan that can be approved and deny any portion of the proposed Plan that cannot be approved, pursuant to the processes described in paragraph (5).\n**(5) Denial pending waiver approval**\n**(A) Partial approval**\nIf a Plan is denied under paragraph (3) solely on the basis that a waiver request that is part of the Plan has not been approved or is subject to dispute resolution under section 107, on request of the applicable Indian Tribe, the Secretary shall grant partial approval for those portions of the Plan not affected by the waiver request.\n**(B) Approval after resolution**\nWith respect to a Plan described in subparagraph (A), upon approval or resolution of the waiver request under section 107 and on request of the applicable Indian Tribe, the Secretary shall approve the Plan or amended Plan not later than 45 days after the date on which the Secretary receives the request.\n**(6) Deemed approval**\nIf the Secretary does not provide written notice to an Indian Tribe of a decision on a Plan within the 90-day period described in paragraph (1), the Plan shall be deemed approved.\n##### (d) Extension of time\n**(1) In general**\nSubject to paragraph (2), the Secretary may extend or otherwise alter the 90-day period described in subsection (c)(1) if, before expiration of the original 90-day period, the Secretary obtains the express written consent of the Indian Tribe that submitted the applicable Plan.\n**(2) Extension restrictions**\nAn extension or alteration of the 90-day period under paragraph (1) may only be\u2014\n**(A)**\nprovided once; and\n**(B)**\nfor a period of not more than 90 days.\n##### (e) Review of denial\nIn addition to the requirements of subsection (c)(3), if the Secretary denies or partially denies a proposed Plan the Secretary shall\u2014\n**(1)**\nprovide technical assistance to the applicable Indian Tribe with respect to the denied proposed Plan, or the denied portion of the proposed Plan, to overcome any stated objections and ensure the proposed Plan meets the requirements of this Act, to the maximum extent possible; and\n**(2)**\nnotwithstanding the right to bring a civil action under subsection (f), on request of the Indian Tribe, provide the Indian Tribe with a hearing on the record with the right to engage in full discovery relevant to any issue raised in the matter and the opportunity for appeal on the objections raised by the Secretary under subsection (c)(3), under such rules and regulations as the Secretary may issue.\n##### (f) Civil actions\n**(1) In general**\nAn Indian Tribe may bring a civil action in a district court of the United States against\u2014\n**(A)**\nthe Secretary for a Plan denial under this section;\n**(B)**\nthe head of an affected agency whose recommendation contributed to a Plan denial under this section;\n**(C)**\nthe head of an affected agency for a waiver denial under section 107; and\n**(D)**\nthe Secretary or head of an affected agency or participating agency for failure to comply with any applicable obligations or responsibilities under this Act.\n**(2) Administrative exhaustion not required**\nAn Indian Tribe may bring a civil action under paragraph (1) without regard to whether the Indian Tribe had an administrative hearing for a Plan denial under subsection (e)(2), engaged in the dispute resolution process for a waiver denial under section 107(c)(3), or sought other available administrative remedies.\n**(3) Relief**\nIn a civil action brought by an Indian Tribe under paragraph (1), a district court of the United States may order appropriate relief (including injunctive relief to reverse a denial of a Plan or a waiver to compel an officer or employee of the United States, or any agency thereof, to perform a duty provided under this Act or regulations promulgated under this Act) against any action by an officer or employee of the United States or any Federal agency contrary to this Act or regulations promulgated under this Act.\n**(4) Attorney fees**\nIf an Indian Tribe substantially prevails in a civil action brought by the Indian Tribe under this subsection or secures a court order under section 202(f), a district court of the United States may award attorneys\u2019 fees, expert witness fees, and other costs of participating in such action, as the court deems reasonable.\n##### (g) Final agency action\nNotwithstanding any other provision of law, a decision by an official of the Department that constitutes final agency action and that relates to an appeal within the Department that is conducted under this section shall be made by an official who holds a position at a higher organizational level within the Department than the level of the departmental agency at which the decision that is the subject of the appeal was made.\nII\nPlan Implementation; Funding Administration; Interdepartmental Memorandum of Agreement; Report\n#### 201. Reduced reporting requirements\n##### (a) Certain Federal program requirements superseded\nAn Indian Tribe with a Plan approved by the Secretary under section 108\u2014\n**(1)**\nshall be required to submit a single report each year based on the model report developed by the Secretary under subsection (b)(1) in accordance with the Plan of the Indian Tribe; and\n**(2)**\nshall not be required to comply with reporting, recordkeeping, auditing, or similar requirements or procedures required by affected agencies and individual Federal programs integrated into the Plan of the Indian Tribe.\n##### (b) Duties of secretary\nThe Secretary shall\u2014\n**(1)**\ndevelop a model report, to be made available to the Indian Tribes, that describes all services or activities undertaken and expenditures made under a Plan;\n**(2)**\ndevelop and use a single monitoring and oversight system for Plans, which shall record all information relevant to the administration of Plans, including but not limited to, with respect to each Plan\u2014\n**(A)**\nannual reports submitted by Indian Tribes under this section;\n**(B)**\nstreamlined funding frameworks, as updated by the Secretary pursuant to section 204(b)(2)(B); and\n**(C)**\ncoordinated project schedules, including any environmental review timetables included in those coordinated project schedules, as updated by the Secretary pursuant to section 202(c)(2)(B); and\n**(3)**\nmaintain and make available to Indian Tribes a list of all\u2014\n**(A)**\nFederal programs approved and denied for integration into Plans; and\n**(B)**\nwaiver requests granted and denied under section 107.\n##### (c) Model report format\n**(1) Requirements**\nThe model report developed under subsection (b)(1) shall contain information sufficient to\u2014\n**(A)**\ndetermine whether the Indian Tribe has complied with the requirements of the Plan of the Indian Tribe; and\n**(B)**\nenable the head of each affected agency to determine whether the Indian Tribe has complied with all directly applicable statutory and regulatory requirements of the integrated Federal programs of each affected agency that are not\u2014\n**(i)**\nsuperseded on integration into a Plan; or\n**(ii)**\nwaived under section 107.\n**(2) Limitation**\nThe model report developed under subsection (b)(1) shall not require an Indian Tribe to report on the expenditure of funds expressed by fund source or single agency code transferred to the Indian Tribe under a Plan.\n#### 202. Streamlined permitting and review implementation\n##### (a) Identification of Federal agencies\n**(1) In general**\nOn approval of a Plan by the Secretary under section 108, the Secretary, in consultation with the Indian Tribe, shall identify and invite all Federal agencies that have permitting, review, approval, or other authorization responsibilities with respect to the services or activities to be carried out under the Plan, including but not limited to responsibilities that require review under NEPA, section 306108 of title 54, United States Code (commonly known as the National Historic Preservation Act ), and other applicable Federal law, to participate in the streamlined permitting and review process described in this section.\n**(2) Lead agency**\nThe Department shall be the lead Federal agency responsible for implementation of this Act.\n##### (b) Participating agencies\n**(1) In general**\nA Federal agency invited under subsection (a) shall be designated as a participating agency for a Plan, unless the Federal agency informs the Secretary in writing not later than 14 days after the date on which the Federal agency receives the invitation from the Secretary under that subsection that the Federal agency\u2014\n**(A)**\nhas no jurisdiction or review, permitting, or other authorization responsibility with respect to the services or activities to be carried out under the Plan; or\n**(B)**\ndoes not intend to exercise review, permitting, or other authorization responsibility relating to, or submit comments on, implementation of the Plan.\n**(2) Changed circumstances**\nOn request of a Federal agency based on a showing of changed circumstances, the Secretary may designate a Federal agency that has opted out under paragraph (1) to be a participating agency.\n**(3) Effect**\nDesignation as a participating agency under paragraph (1) shall not grant the participating agency authority or jurisdiction over\u2014\n**(A)**\nthe Plan; or\n**(B)**\nthe services and activities to be carried out under the Plan beyond the existing statutory authority of the participating agency, if any, to approve particular services or activities under the Plan.\n##### (c) Coordinated project schedule\n**(1) In general**\nNot later than 60 days after the date on which a Plan submitted to the Secretary is approved by the Secretary under section 108, the Secretary, in consultation with the applicable Indian Tribe and each participating agency designated under subsection (b)(1), shall develop a coordinated project schedule for completing any review and obtaining any permit or other authorization required to carry out the services and activities under the Plan, except those requirements waived under section 107.\n**(2) Required information**\n**(A) In general**\nA coordinated project schedule shall include, but is not limited to, the following information collected by the Secretary:\n**(i)**\nA list of, and roles and responsibilities for, all participating agencies with review, permitting, or other authorization responsibility for services or activities under the Plan.\n**(ii)**\nA discussion of potential avoidance, minimization, and mitigation strategies, if known and required by applicable Federal law.\n**(iii)**\nA plan and schedule for public and Tribal outreach and coordination, to the extent required by applicable Federal law.\n**(iv)**\nIf applicable, an environmental review timetable, as described in subsection (d).\n**(B) Updates**\nThe information described in subparagraph (A) shall be updated by the Secretary not less frequently than every 6 months.\n##### (d) Environmental review timetable\n**(1) Establishment**\nAs part of a coordinated project schedule, the Secretary, in consultation with the applicable Indian Tribe, each participating agency, and, if appropriate, any State in which the relevant services or activities in the Plan are located, shall establish an environmental review timetable that includes but is not limited to intermediate and final completion dates for all required environmental reviews necessary for each permit or other authorization required by a participating agency to support completion of the services or activities in the Plan that have not otherwise been waived under section 107, including but not limited to any review required pursuant to NEPA.\n**(2) Term**\nTo the maximum extent practicable, and consistent with applicable Federal law, an environmental review timetable established under paragraph (1) shall not exceed an overall term of 1 year after a Plan is approved.\n**(3) Determinations**\nIf a participating agency is required to issue a determination with respect to an environmental review, permit, or other authorization as part of the coordinated project schedule described in paragraph (1), the participating agency shall issue the determination not later than 90 days after all the required information for the environmental review, permit, or other authorization is in possession of the participating agency.\n**(4) Delay**\nIf the Secretary determines that an environmental review, permit, or other authorization will not be completed or issued in accordance with this subsection and the applicable environmental review timetable, the Secretary shall\u2014\n**(A)**\nnotify the participating agency responsible for completing the environmental review or issuing the permit or other authorization of the discrepancy; and\n**(B)**\nrequest that the participating agency take such measures as the Secretary, in consultation with the participating agency, determines appropriate to comply with that environmental review timetable.\n##### (e) Coordination of required reviews and authorizations\n**(1) Concurrent reviews**\nTo efficiently integrate the exercise of review, permitting, and other authorization responsibilities, each participating agency shall, to the maximum extent practicable\u2014\n**(A)**\ncarry out the responsibilities of the participating agency with respect to a Plan concurrently, and in conjunction with, the responsibilities of other participating agencies, including reviews required under NEPA and section 306108 of title 54, United States Code (commonly known as the National Historic Preservation Act ), unless the participating agency determines that doing so would impair the ability of the participating agency to carry out the other statutory obligations of the participating agency;\n**(B)**\nformulate and implement administrative, policy, and procedural mechanisms to enable the participating agency to ensure completion of the process for reviews and issuance of permits and other authorizations in a timely, coordinated, and responsible manner; and\n**(C)**\nwhere an environmental impact statement is required for services or activities in a Plan pursuant to section 102(2)(C) of NEPA ( 42 U.S.C. 4332(2)(C) ), prepare a single, interagency environmental impact statement for the services or activities unless the Secretary provides justification in the coordinated project schedule that multiple environmental impact statements are more efficient.\n**(2) Adoption, incorporation by reference, and use of documents**\n**(A) In general**\nOn request of an Indian Tribe, the Secretary shall consider and, as appropriate, adopt or incorporate by reference, the analysis and documentation prepared for a Plan under the laws and procedures of the Indian Tribe as the documentation, or part of the documentation, required to complete a review or issue a permit or other authorization for the Plan.\n**(B) NEPA compliance**\nA document adopted under subparagraph (A) or a document that includes documentation incorporated under that subparagraph may serve as the documentation required for an environmental review or a supplemental environmental review required to be prepared by a lead agency pursuant to NEPA.\n**(3) Presumption of negative impacts of taking no action**\nFor all environmental reviews required pursuant to NEPA that require consideration of a no action alternative, there shall be a presumption that, given the ongoing threats addressed by this Act, the effects of taking no action will be negative for the Indian Tribe.\n##### (f) Petition to court\n**(1) Right to petition**\nAn Indian Tribe may obtain a review of an alleged failure by a participating agency to act in accordance with an applicable deadline described in a coordinated project schedule by filing a written petition with a district court of the United States or other court of competent jurisdiction seeking an order under paragraph (2).\n**(2) Court order**\nIf a district court of the United States or other court of competent jurisdiction finds that a participating agency has failed to act in accordance with an applicable deadline described in paragraph (1), the court shall set a schedule and deadline for the participating agency to act as soon as practicable, which shall not exceed 90 days from the date on which the order of the court is issued, unless the court determines a longer time is necessary to comply with applicable law.\n#### 203. Expedited fee-to-trust process for Plan implementation\n##### (a) Mandatory trust acquisitions\nOn request of an Indian Tribe, the Secretary shall take land into trust for the benefit of the Indian Tribe if the Indian Tribe\u2014\n**(1)**\nacquired the land using funds distributed in accordance with a Plan; or\n**(2)**\nafter the Indian Tribe acquires the land, the Secretary determines the Indian Tribe faces imminent environmental risk if not able to use that land for community-driven relocation.\n##### (b) Discretionary trust acquisitions\nOn request of an Indian Tribe, the Secretary may take into trust for the benefit of the Indian Tribe any land owned by the Indian Tribe and intended for use pursuant to a Plan, regardless of when the land was acquired, in accordance with this section and the procedures described in part 151 of title 25, Code of Federal Regulations (as in effect on the date of the enactment of this Act), except that\u2014\n**(1)**\nthe Indian Tribe shall\u2014\n**(A)**\nnot be subject to the documentation requirements described in that part; but\n**(B)**\nensure, in consultation with the Secretary, that sufficient information for the trust acquisition request is included in the Plan (or in subsequent materials); and\n**(2)**\nthe Secretary shall\u2014\n**(A)**\nregardless of the actual location of the land, evaluate the trust acquisition request using the procedures for evaluating\u2014\n**(i)**\nan on-reservation acquisition pursuant to section 151.9(c) of title 25, Code of Federal Regulations (as in effect on the date of the enactment of this Act); or\n**(ii)**\nas applicable, an initial Indian acquisition pursuant to section 151.12(c) of title 25, Code of Federal Regulations (as in effect on the date of the enactment of this Act);\n**(B)**\nas applicable, evaluate the request using the environmental review process described in section 202; and\n**(C)**\nact on the request of an Indian Tribe in accordance with the timeframe for approving or denying a Plan under section 108.\n#### 204. Streamlined funding framework implementation\n##### (a) In general\nThe Secretary, in consultation with the applicable Indian Tribe, shall function as the lead Federal agency in developing and implementing the streamlined funding frameworks described in this section.\n##### (b) Streamlined funding framework\n**(1) In general**\nIn consultation with the applicable Indian Tribe, the Secretary shall develop a streamlined funding framework for each Plan that details how funding sources for the Federal programs integrated into the Plan will be transferred in an efficient manner to the Department for distribution to the Indian Tribe, consistent with the requirements of this Act.\n**(2) Required information**\n**(A) In general**\nEach streamlined funding framework developed under paragraph (1) shall include, but is not limited to, the following information:\n**(i)**\nA list of, and roles and responsibilities for, all affected agencies with Federal programs integrated into a Plan.\n**(ii)**\nA funding timetable establishing a comprehensive schedule of dates by which\u2014\n**(I)**\nall funds are expected to be apportioned to the affected agencies; and\n**(II)**\nthose funds shall be transferred to the Secretary and disbursed to the Indian Tribe, in accordance with the requirements of section 205.\n**(B) Updates**\nThe information described in subparagraph (A) shall be updated by the Secretary not less frequently than once per year.\n**(3) Affected agencies**\nTo efficiently and effectively integrate funding from Federal programs according to a Plan, each affected agency shall, to the maximum extent practicable\u2014\n**(A)**\nprioritize the ease of use of Plan funds by Indian Tribes;\n**(B)**\nformulate and implement administrative, policy, and procedural mechanisms to enable the affected agency to coordinate funding with the funding sources of other affected agencies; and\n**(C)**\ncarry out the obligations of the affected agency with respect to a Plan under any other applicable Federal law concurrently, and in conjunction with, other affected agencies, unless the affected agency determines that doing so would impair the ability of the affected agency to carry out other statutory obligations of the affected agency.\n#### 205. Transfer and distribution of funds\n##### (a) Responsibility\nThe Secretary shall be responsible for\u2014\n**(1)**\nthe receipt of all funds covered by a Plan approved by the Secretary; and\n**(2)**\nthe distribution of those funds to the applicable Indian Tribe by not later than 45 days after the date on which the Secretary receives those funds from the affected agency.\n##### (b) Set-Asides\nNotwithstanding any other provision of law\u2014\n**(1)**\nan affected agency may establish and implement, for the purposes of carrying out this Act, a set-aside of funding for Indian Tribes from any Federal program the affected agency administers; and\n**(2)**\nthe amount for a set-aside described in paragraph (1) shall be not less than 10 percent of the total appropriations made available for the applicable Federal program.\n##### (c) Transfer of funds\nNotwithstanding any other provision of law, not later than 30 days after the date on which funds are apportioned to an affected agency to carry out a Federal program integrated into a Plan, the head of the affected agency that administers the Federal program integrated into the Plan shall transfer those funds, through a nonexpenditure transfer, to the Secretary for distribution to an Indian Tribe.\n##### (d) Distribution of funds\nNotwithstanding any other provision of law, on request of an Indian Tribe, all funds distributed to the Indian Tribe in accordance with a Plan shall be distributed to the Indian Tribe pursuant to an existing contract, compact, or funding agreement entered into under the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. ).\n##### (e) Emergency distribution of funds\nNotwithstanding any other provision of law, the Secretary may, on request of an Indian Tribe, distribute limited funding on an interim basis before the date on which the Secretary approves a Plan under section 108.\n#### 206. Administration of funds\n##### (a) Requirements\n**(1) In general**\n**(A) Consolidation and reallocation of funds**\nNotwithstanding any other provision of law, an Indian Tribe may reallocate, reprogram, consolidate, or rebudget any funds transferred to the Indian Tribe pursuant to a Plan to further any purpose covered by the Plan and to best meet the needs of the Indian Tribe, without the need for additional Federal approval or a waiver under section 107.\n**(B) Authorized use of funds**\nFunds used to carry out a Plan shall be administered in such a manner as the Secretary determines to be appropriate to ensure the funds are spent on services and activities carrying out the purposes authorized under the Plan.\n**(C) Effect**\nNothing in this section interferes with the ability of the Secretary to use accounting procedures that conform to generally accepted accounting principles, auditing procedures, and safeguarding of funds that conform to chapter 75 of title 31, United States Code (commonly known as the Single Audit Act of 1984 ).\n**(2) Separate records and audits not required**\nNotwithstanding any other provision of law (including but not limited to regulations and circulars of any agency (including but not limited to Office of Management and Budget Circular A\u2013133)), an Indian Tribe that has in place a Plan approved under section 108 shall not be required to\u2014\n**(A)**\nmaintain separate records that trace any service or activity conducted under the Plan to the Federal program for which the funds were initially authorized or transferred;\n**(B)**\nallocate expenditures among those Federal programs;\n**(C)**\naudit expenditures by the original source of the Federal program; or\n**(D)**\nreport on or in accordance with any requirements associated with the underlying Federal program, where instead only 1 annual report on the Plan is required pursuant to the model report developed by the Secretary under section 201(b)(1).\n##### (b) Carryover\n**(1) In general**\nAny funds transferred to an Indian Tribe under section 205(c) that are not obligated or expended prior to the beginning of the fiscal year after the fiscal year for which the funds were appropriated shall remain available for obligation or expenditure, without fiscal year limitation, subject to the condition that the funds shall be obligated or expended in accordance with the Plan of the Indian Tribe.\n**(2) No additional documentation**\nAn Indian Tribe shall not be required to provide any additional justification or documentation of the purposes of a Plan as a condition of receiving or expending carryover funds described in paragraph (1).\n##### (c) Indirect costs\nNotwithstanding any other provision of law, an Indian Tribe shall be entitled to recover 100 percent of any indirect costs incurred by the Indian Tribe as a result of the transfer of funds to the Indian Tribe under section 205(c).\n##### (d) Matching funds\nNotwithstanding any other provision of law, any funds transferred to an Indian Tribe under section 205(c) shall be treated as non-Federal funds for purposes of meeting matching requirements under any other Federal law.\n##### (e) Interest or other income\nAn Indian Tribe shall be entitled to retain interest earned on any funds transferred to the Indian Tribe under section 205(c) and that interest shall not diminish the amount of funds the Indian Tribe is authorized to receive under the Plan in the year the interest is earned (or in any subsequent fiscal year).\n#### 207. No reduction in amounts\n##### (a) In general\nIn no case shall the amount of Federal funds available to an Indian Tribe that seeks to propose a Plan under section 106 be reduced as a result of the\u2014\n**(1)**\nenactment of this Act; or\n**(2)**\napproval or implementation of a Plan of the Indian Tribe.\n##### (b) Interaction with other laws\nThe integration of a Federal program into a Plan shall not\u2014\n**(1)**\nmodify, limit, or otherwise affect the eligibility of the Federal program for contracting under the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. ); or\n**(2)**\neliminate the applicability of any provision of that Act, as the provision relates to a specific Federal program eligible for contracting under that Act.\n#### 208. Interdepartmental memorandum of agreement\n##### (a) Memorandum of agreement required\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Office of the Assistant Secretary for Indian Affairs shall lead the Federal partners in negotiating and entering into an interdepartmental memorandum of agreement providing for the implementation of this Act.\n**(2) Tribal consultation**\nIn negotiating and entering to an interdepartmental memorandum of agreement under paragraph (1), the Department and the Federal partners shall consult with representatives of Indian Tribes.\n##### (b) Requirements and restrictions\nThe interdepartmental memorandum of agreement required under subsection (a)(1)\u2014\n**(1)**\nshall include, but is not limited to, provisions relating to\u2014\n**(A)**\ninteragency cooperation with respect to the procedures for approval of Plans by the Secretary under section 108 and the granting of waivers by affected agencies under section 107;\n**(B)**\nestablishing a Tribal working group to advise the Federal partners on overall program management and implementation; and\n**(C)**\nensuring an annual meeting between the Federal partners and the Tribal working group described in subparagraph (B); but\n**(2)**\nshall not\u2014\n**(A)**\nintroduce additional criteria for Federal program eligibility;\n**(B)**\nlimit the role of the Department as the lead Federal agency responsible for implementation of this Act; or\n**(C)**\nrestrict the role of the Secretary and the sole and exclusive decisionmaking authority of the Secretary for all Federal actions under this Act, unless otherwise provided in this Act, including but not limited to the sole and exclusive authority to determine whether a Federal program is eligible for integration into a Plan.\n##### (c) Applicability\nChapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act ), shall not apply to the Tribal working group described in subsection (b)(1)(B) or any Federal agency coordinating with that Tribal working group.\n##### (d) Detail of Federal employees\nAn employee of the Federal Government may be detailed to the Department for the purposes of carrying out this Act without reimbursement and without interruption or loss of civil service status or privilege.\n#### 209. Report required\nNot later than 2 years after the date of enactment of this Act, the Secretary, in consultation with affected agencies and representatives of Indian Tribes, shall submit to the Committee on Indian Affairs of the Senate and the Committee on Natural Resources of the House of Representatives a report on the status of the implementation of this Act.",
      "versionDate": "2025-05-29",
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
            "updateDate": "2025-09-19T19:50:28Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-09-19T19:50:07Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-19T19:50:34Z"
          },
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-09-19T19:49:57Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-19T19:50:18Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-09-19T19:49:50Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-09-19T19:49:33Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2025-09-19T19:49:44Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-09-19T19:50:02Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-09-19T19:50:23Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-19T19:50:13Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2025-09-19T19:49:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-06-23T17:59:43Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3654ih.xml"
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
      "title": "TERRA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T08:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TERRA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T08:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tribal Emergency Response Resources Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T08:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the integration and administrative streamlining of Federal funding for Indian Tribes that have reservations, other Tribal lands, or ways of life at risk due to environmental impacts and natural disasters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T08:48:21Z"
    }
  ]
}
```
