# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1237?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1237
- Title: New Producer Economic Security Act
- Congress: 119
- Bill type: S
- Bill number: 1237
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-02-25T12:03:22Z
- Update date including text: 2026-02-25T12:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1237",
    "number": "1237",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "New Producer Economic Security Act",
    "type": "S",
    "updateDate": "2026-02-25T12:03:22Z",
    "updateDateIncludingText": "2026-02-25T12:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
            "date": "2025-04-01T20:19:01Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-01T20:19:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1237is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1237\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Ms. Smith introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo establish the New Producer Economic Security Program within the Farm Service Agency Office of Outreach and Education.\n#### 1. Short title\nThis Act may be cited as the New Producer Economic Security Act .\n#### 2. New Producer Economic Security Program\n##### (a) Definitions\nIn this section:\n**(1) Authorized legal entity**\nThe term authorized legal entity means any corporation, business trust, estate, trust, partnership, limited liability company, association, joint venture, public corporation, cooperative, pension or investment fund, or any other legal or commercial entity organized or created under the laws of any State that meets each of the following requirements:\n**(A)**\nThe entity is not a subsidiary of, or owned in any part by, a multilayered subsidiary entity.\n**(B)**\nThe shareholders, partners, members, or beneficial owners of the entity do not exceed 25 individuals.\n**(C)**\nThe shareholders, partners, members, or beneficial owners of the entity are all natural persons who\u2014\n**(i)**\nregularly and frequently make, or take an important part in making, management decisions substantially contributing to or affecting the operation of a farm or forest; or\n**(ii)**\nperform physical work that significantly contributes to cultivation, stewardship, crop or livestock production, or food production.\n**(2) Covered project**\nThe term covered project means a project described in subsection (e).\n**(3) Eligible entity**\n**(A) In general**\nThe term eligible entity means an entity that\u2014\n**(i)**\nhas demonstrated experience in serving qualified beneficiaries; and\n**(ii)**\nis\u2014\n**(I)**\na State, local, or territorial government;\n**(II)**\nan Indian Tribe or Tribal organization (as those terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ));\n**(III)**\na Native community development financial institution certified by the Secretary of the Treasury;\n**(IV)**\na community development financial institution (as defined in section 103 of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4702 )) certified by the Secretary of the Treasury, acting through the Director of the Community Development Financial Institutions Fund established under section 104(a) of that Act ( 12 U.S.C. 4703(a) );\n**(V)**\nan organization described in paragraph (2) or (3) of section 501(c) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code;\n**(VI)**\na foundation;\n**(VII)**\na cooperative entity;\n**(VIII)**\nan institution of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ));\n**(IX)**\na financial institution described in section 1.7(b)(1)(B) of the Farm Credit Act of 1971 ( 12 U.S.C. 2015(b)(1)(B) ); and\n**(X)**\nany other appropriate partner, as determined by the Secretary.\n**(B) Exclusion**\nThe term eligible entity does not include a corporation that is foreign-based or foreign-owned.\n**(4) Eligible land**\n**(A) In general**\nThe term eligible land means\u2014\n**(i)**\nagricultural land;\n**(ii)**\nprivate land;\n**(iii)**\nurban land;\n**(iv)**\npublic land, including Federal, State, and municipally owned or managed land;\n**(v)**\nlands held in common that are controlled and managed by groups of individuals;\n**(vi)**\nlands held in trust;\n**(vii)**\nmultiple parcels of land described in any of clauses (i) through (vi) that are noncontiguous; and\n**(viii)**\npublic or private shoreline or intertidal zone areas, which may be wholly or partially underwater.\n**(B) Exclusion**\nThe term eligible land does not include a natural area (as defined in section 650.23(a) of title 7, Code of Federal Regulations (or successor regulations)).\n**(5) Program**\nThe term program means the New Producer Economic Security Program established under subsection (b).\n**(6) Qualified beneficiary**\n**(A) In general**\nThe term qualified beneficiary means a farmer, a rancher, or a forest owner who\u2014\n**(i)**\nis a natural person;\n**(ii)**\nis\u2014\n**(I)**\na shareholder in an authorized legal entity;\n**(II)**\nan officer, director, or employee of an authorized legal entity;\n**(III)**\na member or manager of an authorized legal entity;\n**(IV)**\na partner in an authorized legal entity;\n**(V)**\na beneficiary or trustee of an authorized legal entity; or\n**(VI)**\nany other individual who\u2014\n**(aa)**\nregularly and frequently makes, or takes an important part in making, management decisions substantially contributing to or affecting the operation of a farm or forest; or\n**(bb)**\nperforms physical work that significantly contributes to cultivation, stewardship, crop or livestock production, or food production; and\n**(iii)**\n**(I)**\nhas never operated, or has not operated for more than 10 consecutive years, a farm or a ranch;\n**(II)**\noperates only on rented or leased land;\n**(III)**\nhas an income that is at or below 200 percent of the national poverty level or half of the median household income of the county in which the natural person is located; or\n**(IV)**\nis economically disadvantaged, as determined by the Secretary.\n**(B) Exclusion**\nThe term qualified beneficiary does not include a natural person who solely provides capital to an authorized legal entity that is not a qualified beneficiary described in subparagraph (A).\n**(7) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) Establishment\nThe Secretary shall establish within the Farm Service Agency a competitive program, to be known as the New Producer Economic Security Program , to make grants to, enter into cooperative agreements with, or provide other capital support to eligible entities to carry out covered projects in accordance with subsection (e).\n##### (c) Purpose\nThe purposes of the program are\u2014\n**(1)**\nto strengthen the food systems security of the United States by efficiently investing in community-led solutions to increasing access to land, capital, and markets for qualified beneficiaries; and\n**(2)**\nto support projects that\u2014\n**(A)**\nsupport farm establishment and long-term farm business viability;\n**(B)**\nsupport the financial viability of qualified beneficiaries;\n**(C)**\nsupport the physical and mental health of qualified beneficiaries;\n**(D)**\nincrease land access;\n**(E)**\nprevent land loss;\n**(F)**\nestablish innovative ways to make land accessible to qualified beneficiaries;\n**(G)**\ntransition farmland from existing landowners to qualified beneficiaries; and\n**(H)**\nprovide appropriate technical assistance related to permissible activities described in subsection (e)(2).\n##### (d) Selection\n**(1) Application requirements**\nTo be eligible to receive assistance under the program, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including\u2014\n**(A)**\ninformation demonstrating that the covered project the eligible entity seeks to carry out is designed\u2014\n**(i)**\nto serve qualified beneficiaries; and\n**(ii)**\nto meet the purposes of the program described in subsection (c);\n**(B)**\na description of how project activities will support the long-term financial viability of qualified beneficiaries;\n**(C)**\na plan for notification and consultation with local Tribal governments for the future sale of land, if applicable;\n**(D)**\nan analysis of anticipated benefits to the community and the agricultural economy within the project area; and\n**(E)**\na plan for evaluation, data management, communication, and reporting of project findings and results.\n**(2) Evaluation and selection of applications**\n**(A) Evaluation process**\nThe Secretary shall develop a process for evaluating and selecting applications submitted under paragraph (1) in collaboration with the stakeholder committee established under subparagraph (B).\n**(B) Stakeholder committee**\n**(i) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish and convene a stakeholder committee to provide input on the distribution of funds and the evaluation and selection of applications submitted under paragraph (1).\n**(ii) Consideration**\nThe Secretary shall ensure that the stakeholder committee established under clause (i) includes perspectives reflecting\u2014\n**(I)**\nthe complexity of the rural and urban agricultural landscapes of the United States; and\n**(II)**\nthe wide variety of agricultural production models employed by qualified beneficiaries.\n**(C) Priority**\nIn selecting applications submitted under paragraph (1), the Secretary shall give priority to applications for covered projects that\u2014\n**(i)**\nprovide direct financial assistance to qualified beneficiaries;\n**(ii)**\ninvolve a substantial and effective collaborative network or partnership of public or private entities;\n**(iii)**\ninclude a right of first refusal for Tribal citizens or governments when land becomes available on or near Tribal communities;\n**(iv)**\ninvolve mechanisms, such as a deed restriction or conservation easement, that restrict the resale value of eligible land to protect the land for agricultural use;\n**(v)**\nsupport the voluntary transition of agricultural land from existing producers to qualified beneficiaries;\n**(vi)**\nprovide technical assistance, including translation and interpretation services;\n**(vii)**\ninclude activities under subsection (e) designed to support farmworkers; or\n**(viii)**\nsupport long-term adoption of conservation practices that are consistent with conservation practice standards of the Natural Resources Conservation Service and designed to achieve conservation outcomes.\n##### (e) Covered projects\n**(1) Required use of funds**\nAn eligible entity that receives assistance under the program shall provide direct assistance to qualified beneficiaries in order to facilitate access to land, capital, and markets, which may include payments\u2014\n**(A)**\nto acquire real property (including air rights, water rights, and other interests therein), including closing costs;\n**(B)**\nto subsidize interest rates and mortgage principal amounts for qualified beneficiaries;\n**(C)**\nto provide down payment assistance to decrease farm mortgages;\n**(D)**\nto secure clear title on heirs\u2019 property;\n**(E)**\nto conduct surveys and assessments of eligible land;\n**(F)**\nto improve or remediate land, water, and soil;\n**(G)**\nto construct or repair infrastructure;\n**(H)**\nto support land use planning;\n**(I)**\nto acquire succession planning assistance;\n**(J)**\nto carry out Tribal consultation;\n**(K)**\nto support acquisition of a Department of Agriculture farm number; and\n**(L)**\nfor any other activities, as determined by the Secretary.\n**(2) Permissible activities**\nAn eligible entity that receives assistance under the program may use the funds\u2014\n**(A)**\nfor activities associated with strengthening the economic security of qualified beneficiaries by increasing access to markets and capital;\n**(B)**\nto provide direct assistance to qualified beneficiaries in assessing, purchasing, acquiring, or retaining eligible land;\n**(C)**\nfor activities designed to support farm establishment and long-term viability;\n**(D)**\nto establish a revolving loan fund or other innovative financial mechanism designed for the purpose of investing in covered projects beyond the initial project timeline; and\n**(E)**\nto provide technical assistance that meets the specific needs of, and is accessible to qualified beneficiaries, including\u2014\n**(i)**\nproviding translation and interpretation services;\n**(ii)**\ndeveloping and carrying out strategies to identify unique needs and gaps in access, knowledge, and services; and\n**(iii)**\nspecialized consultation, training, coaching, capacity building, and mentoring focused on\u2014\n**(I)**\naccessing, purchasing, acquiring, or retaining eligible land;\n**(II)**\ncomprehension of, preparation to apply for, and complying with Department of Agriculture programs;\n**(III)**\nsuccession planning;\n**(IV)**\nmarket planning and risk analysis;\n**(V)**\ncooperative development;\n**(VI)**\nlegal and tax issues;\n**(VII)**\ndeveloping business plans and feasibility studies;\n**(VIII)**\nfinancial planning and recordkeeping;\n**(IX)**\nenterprise, business, and labor management; and\n**(X)**\nany other activities as determined by the Secretary.\n**(3) Subcontract**\nAn eligible entity may subcontract with an organization to carry out a use or activity under paragraph (1) or (2) if the services of the subcontractor are necessary.\n**(4) Funding mechanism**\n**(A) Eligible entities**\nThe Secretary shall make funding available under the program to eligible entities in the form of\u2014\n**(i)**\ngrants;\n**(ii)**\ncooperative agreements;\n**(iii)**\ncapitalization loans, in the case of an activity described in paragraph (2)(D); or\n**(iv)**\nother means, as determined by the Secretary.\n**(B) Qualified beneficiaries**\nIn carrying out covered projects under the program, an eligible entity shall provide direct assistance to qualified beneficiaries in the form of\u2014\n**(i)**\ngrants;\n**(ii)**\nloans (both long-term and interim); or\n**(iii)**\nother direct payments or assistance, as determined by the Secretary.\n**(5) Repayment of funds in case of noncompliance**\nAn eligible entity that violates the terms or conditions of assistance provided under the program shall reimburse the Secretary for that assistance.\n##### (f) Funding\n**(1) Authorization of appropriations**\nThere are authorized to be appropriated to the Secretary such sums as are necessary to carry out this section.\n**(2) Agency contribution account**\nIn addition to amounts otherwise made available under paragraph (1), the Secretary may use funds available through 1 or more contribution accounts established under section 1241(f)(1) of the Food Security Act of 1985 ( 16 U.S.C. 3841(f)(1) ).\n**(3) Administration**\nOf the amounts made available to carry out the program, the Secretary may use an appropriate amount for the costs of implementing and administering the program.\n**(4) Distribution of funds**\n**(A) Limitation**\nAn eligible entity that receives assistance under the program shall obligate the amounts for a covered project by not later than 5 years after the date on which the funds are made available to the eligible entity, unless the Secretary determines otherwise.\n**(B) Exclusion**\nIn the case of a covered project to support qualified beneficiaries in assessing, purchasing, acquiring, or retaining eligible land for a period longer than the 5-year period described in subparagraph (A), section 200.311 of title 2, Code of Federal Regulations (or a successor regulation) shall not apply.",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-18",
        "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit."
      },
      "number": "2536",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "New Producer Economic Security Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:44:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119s1237",
          "measure-number": "1237",
          "measure-type": "s",
          "orig-publish-date": "2025-04-01",
          "originChamber": "SENATE",
          "update-date": "2026-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1237v00",
            "update-date": "2026-02-18"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>New Producer Economic Security Act</strong></p><p>This bill\u00a0establishes the\u00a0New Producer Economic Security Program within the Farm Service Agency (FSA)\u00a0to provide funding and grants to help\u00a0new farmers, ranchers, and forest owners.</p><p>Specifically, the FSA must make competitive grants to, enter into cooperative agreements with, or provide other capital support to eligible entities (e.g., state or local governments, Indian tribes, nonprofit organizations, and institutions of higher education). These entities must provide direct assistance to qualified farmers, ranchers, and forest owners (e.g., those who have not operated a farm or ranch\u00a0for more than 10 consecutive years or are economically disadvantaged).\u00a0The bill specifically excludes from assistance any foreign-based or foreign-owned corporation.</p><p>The direct assistance may include payments to qualified beneficiaries to acquire real property (including air rights and water rights), secure clear title on heirs' property, and improve or remediate land, water, and soil. Eligible entities may also use grants (1) to provide direct assistance to qualified\u00a0beneficiaries in assessing, purchasing, acquiring, or retaining eligible land; (2) for activities designed to support farm establishment and long-term viability; and (3) to provide technical assistance.</p><p>The FSA must establish a stakeholder committee, and in collaboration with the committee, develop a process for evaluating and selecting applications submitted by eligible entities. The\u00a0stakeholder committee must include perspectives reflecting the complexity of the rural and urban U.S. agricultural landscapes and the wide variety of agricultural production models.</p>"
        },
        "title": "New Producer Economic Security Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1237.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>New Producer Economic Security Act</strong></p><p>This bill\u00a0establishes the\u00a0New Producer Economic Security Program within the Farm Service Agency (FSA)\u00a0to provide funding and grants to help\u00a0new farmers, ranchers, and forest owners.</p><p>Specifically, the FSA must make competitive grants to, enter into cooperative agreements with, or provide other capital support to eligible entities (e.g., state or local governments, Indian tribes, nonprofit organizations, and institutions of higher education). These entities must provide direct assistance to qualified farmers, ranchers, and forest owners (e.g., those who have not operated a farm or ranch\u00a0for more than 10 consecutive years or are economically disadvantaged).\u00a0The bill specifically excludes from assistance any foreign-based or foreign-owned corporation.</p><p>The direct assistance may include payments to qualified beneficiaries to acquire real property (including air rights and water rights), secure clear title on heirs' property, and improve or remediate land, water, and soil. Eligible entities may also use grants (1) to provide direct assistance to qualified\u00a0beneficiaries in assessing, purchasing, acquiring, or retaining eligible land; (2) for activities designed to support farm establishment and long-term viability; and (3) to provide technical assistance.</p><p>The FSA must establish a stakeholder committee, and in collaboration with the committee, develop a process for evaluating and selecting applications submitted by eligible entities. The\u00a0stakeholder committee must include perspectives reflecting the complexity of the rural and urban U.S. agricultural landscapes and the wide variety of agricultural production models.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119s1237"
    },
    "title": "New Producer Economic Security Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>New Producer Economic Security Act</strong></p><p>This bill\u00a0establishes the\u00a0New Producer Economic Security Program within the Farm Service Agency (FSA)\u00a0to provide funding and grants to help\u00a0new farmers, ranchers, and forest owners.</p><p>Specifically, the FSA must make competitive grants to, enter into cooperative agreements with, or provide other capital support to eligible entities (e.g., state or local governments, Indian tribes, nonprofit organizations, and institutions of higher education). These entities must provide direct assistance to qualified farmers, ranchers, and forest owners (e.g., those who have not operated a farm or ranch\u00a0for more than 10 consecutive years or are economically disadvantaged).\u00a0The bill specifically excludes from assistance any foreign-based or foreign-owned corporation.</p><p>The direct assistance may include payments to qualified beneficiaries to acquire real property (including air rights and water rights), secure clear title on heirs' property, and improve or remediate land, water, and soil. Eligible entities may also use grants (1) to provide direct assistance to qualified\u00a0beneficiaries in assessing, purchasing, acquiring, or retaining eligible land; (2) for activities designed to support farm establishment and long-term viability; and (3) to provide technical assistance.</p><p>The FSA must establish a stakeholder committee, and in collaboration with the committee, develop a process for evaluating and selecting applications submitted by eligible entities. The\u00a0stakeholder committee must include perspectives reflecting the complexity of the rural and urban U.S. agricultural landscapes and the wide variety of agricultural production models.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119s1237"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1237is.xml"
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
      "title": "New Producer Economic Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "New Producer Economic Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the New Producer Economic Security Program within the Farm Service Agency Office of Outreach and Education.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:34Z"
    }
  ]
}
```
