# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2122?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2122
- Title: IMPACT Act 2.0
- Congress: 119
- Bill type: HR
- Bill number: 2122
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-05-16T14:26:59Z
- Update date including text: 2026-05-16T14:26:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-14 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-14 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2122",
    "number": "2122",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "IMPACT Act 2.0",
    "type": "HR",
    "updateDate": "2026-05-16T14:26:59Z",
    "updateDateIncludingText": "2026-05-16T14:26:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T22:08:21Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "OH"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "NY"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2122ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2122\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mrs. Foushee (for herself and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo strengthen and enhance the competitiveness of cement, concrete, asphalt binder, and asphalt mixture production in the United States through the research, development, demonstration, and commercial application of technologies to reduce emissions from cement, concrete, asphalt binder, and asphalt mixture production, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the IMPACT Act 2.0 .\n#### 2. Federal highway administration\n##### (a) Performance-Based low-Emissions transportation materials grants\n**(1) Purpose**\nThe purpose of this subsection is to encourage States to improve State-level cement, concrete, asphalt binder, and asphalt mixture specifications and standards to facilitate the purchase of low-emissions cement, concrete, asphalt binder, or asphalt mixtures.\n**(2) Establishment**\nThe Administrator of the Federal Highway Administration (referred to in this section as the Administrator ) shall provide to States\u2014\n**(A)**\nreimbursement for the additional cost of using low-emissions cement, concrete, asphalt binder, and asphalt mixtures used in highway projects of the State;\n**(B)**\nincentives for the acquisition of low-emissions cement, concrete, asphalt binder, and asphalt mixtures for use in highway projects of the State;\n**(C)**\ntechnical assistance to update the specifications and standards of the State to be performance-based specifications and standards; and\n**(D)**\ntechnical assistance to benchmark and quantify embodied greenhouse gas emissions.\n**(3) Reimbursement and incentive amounts**\n**(A) Reimbursement amount**\nThe amount of reimbursement under paragraph (2)(A) shall be equal to the incrementally higher cost of using such materials relative to the cost of using traditional materials, as determined by the State and verified by the Administrator.\n**(B) Incentive amount**\nThe amount of an incentive under paragraph (2)(B) shall be equal to 2 percent of the cost of using low-emissions cement, concrete, asphalt binder, and asphalt mixtures on a highway project of the State.\n**(C) Limitation**\nAmounts provided for reimbursement and incentives under this subsection may not exceed the amount authorized to be appropriated under paragraph (6).\n**(4) Eligibility**\nTo be eligible to receive reimbursement or incentives under this subsection, a State shall have in effect, as appropriate, special provisions, specifications, or standards, such as engineering performance standards, or a collection of embodied greenhouse gas emissions reporting tools, such as environmental product declarations, that facilitate the purchase of low-emissions cement, concrete, asphalt binder, and asphalt mixtures.\n**(5) Coordination**\nIn carrying out this subsection, the Administrator shall leverage the Every Day Counts Initiative of the Department of Transportation to promote the commercialization of low-emissions cement, concrete, asphalt binder, and asphalt mixtures.\n**(6) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary to carry out this subsection $15,000,000 for the period of fiscal years 2025 through 2027.\n##### (b) Directory of low-Emission cement, concrete, asphalt binder, or asphalt mixtures\n**(1) In general**\nThe Administrator shall establish and maintain a publicly available directory of low-emissions cement, concrete, asphalt binder, or asphalt mixtures submitted by States that the Administrator determines to be eligible for reimbursement or incentives under subsection (a).\n**(2) Submission and approval**\n**(A) In general**\nNot later than 180 days after the date of enactment of this Act, the Administrator shall establish a procedure under which States may submit new low-emissions cement, concrete, asphalt binder, or asphalt mixtures to be included in the directory under paragraph (1).\n**(B) Submission**\nTo be considered for inclusion in the directory under paragraph (1), a State shall submit an application relating to the low-emissions cement, concrete, asphalt binder, or asphalt mixture to the Administrator at such time, in such manner, and containing such information as the Administrator determines to be necessary.\n**(C) Decision deadline**\nNot later than 180 days after the date on which the Administrator receives an application under subparagraph (B), the Administrator shall\u2014\n**(i)**\napprove the application and include the low-emissions cement, concrete, asphalt binder, or asphalt mixture in the directory under paragraph (1); or\n**(ii)**\ndeny the application.\n**(D) Written reasons for denial**\nIf the Administrator denies an application under paragraph (C)(ii), the Administrator shall provide the State a written explanation for the denial.\n**(3) Project selection**\nLow-emissions cement, concrete, asphalt binder, or asphalt mixtures approved under paragraph (2)(C)(i) and included in the directory under paragraph (1) may be used in any highway project.\n#### 3. Advance purchase commitment program\n##### (a) Purpose\nThe purposes of this section are\u2014\n**(1)**\nto allow States to purchase or contractually guarantee the direct purchase of conforming low-emissions cement, concrete, asphalt binder, or asphalt mixtures; and\n**(2)**\nto encourage continuous innovation and long-term emissions reductions in the production of concrete, cement, asphalt binder, and asphalt mixtures.\n##### (b) Eligible projects\nSection 133 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (b) by adding at the end the following:\n(25) A project that includes the use of innovative, domestically produced cement, concrete, asphalt mixture, or asphalt binder manufactured using a process described in subsection (l). (26) Subject to subsection (m), a project that is carried out through an advance multiyear contract with a producer for a specified quantity and specified price of innovative, domestically produced cement, concrete, asphalt mixture, or asphalt binder manufactured using a process described in subsection (l). ; and\n**(2)**\nby adding at the end the following:\n(l) Requirements for certain projects The process referred to in paragraphs (25) and (26) of subsection (b) is a manufacturing process that\u2014 (1) produces materials with\u2014 (A) superior durability to conventional materials; and (B) superior performance with respect to\u2014 (i) compressive strength; (ii) tensile strength; or (iii) workability; or (2) produces materials that meet the engineering specifications of the State and achieve superior performance with respect to\u2014 (A) environmental performance; or (B) energy efficiency. .\n##### (c) State flexibility\nSection 133(h)(6) of title 23, United States Code, is amended by adding at the end the following:\n(D) Procurement for innovative building materials (i) In general A State may use the funds set aside under this subsection to enter into an advance multi-year contract described in subsection (m) for a specified quantity and specified price of innovative, domestically produced cement, concrete, asphalt mixture, or asphalt binder. (ii) Use of funds States may not provide payments to the producer as part of the advance procurement under clause (i) unless materials have been delivered according to contract terms and conditions. .\n##### (d) Limitation\nSection 133 of title 23, United States Code, is further amended by adding at the end the following:\n(m) Advance multi-Year contracts Except as otherwise provided in this section, none of the funds made available under this section may be used for a multi-year contract unless\u2014 (1) cancellation provisions in the contract do not include consideration of recurring manufacturing costs of the producer associated with the production of unfunded units to be delivered under the contract; (2) the contract provides that payments to the producer under the contract shall not be made in advance of incurred costs on funded units; (3) the contract does not provide for a price adjustment based on a failure to award a follow-on contract; (4) the producer submits a statement describing the quantity and cost of the cement, concrete, asphalt mixture, and asphalt binder; (5) the producer demonstrates material steps towards commercial production and operational capacity of cement, concrete, asphalt mixture, or asphalt binder production with respect to logistics, planned material storage, handling capacities, and delivery mechanisms, of which failure to demonstrate material progress towards commercial production and operational capacity may result in termination of a portion or all of the advance procurement at the sole discretion of the State; and (6) the contract fulfills, to the maximum extent possible, preference criteria set by the State. .\n##### (e) Low-Emissions cement, concrete, and asphalt defined\nIn this Act, the term low-emissions cement, concrete, and asphalt means cement, concrete, asphalt binder, or asphalt mixture that reduces, to the maximum extent practicable, greenhouse gas or directly related pollutant emissions to levels below commercially available cement, concrete, or asphalt.",
      "versionDate": "2025-03-14",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-04-01T11:25:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2122",
          "measure-number": "2122",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2026-05-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2122v00",
            "update-date": "2026-05-16"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>IMPACT Act 2.0</strong></p><p>This bill expands and modifies Federal Highway Administration (FHWA) programs, including the Surface Transportation Block Grant (STBG) program, to provide states reimbursement, incentives, and technical assistance to purchase low-emissions cement, concrete, asphalt binder, or asphalt mixtures. Under the bill, these are products that reduce, to the maximum extent practicable, greenhouse gas or directly related pollutant emissions to levels below the commercially available products.</p><p>Specifically, the FHWA\u00a0must provide to states</p><ul><li>reimbursement for the additional cost of using low-emissions cement, concrete, asphalt binder, and asphalt mixtures used in state highway projects;</li><li>incentives for the acquisition of these products for use in state highway projects;</li><li>technical assistance to update the state's specifications and standards to be performance-based specifications and standards; and</li><li>technical assistance to benchmark and quantify embodied greenhouse gas emissions (i.e., emissions associated with the production and transportation of goods).</li></ul><p>The FHWA must leverage the Every Day Counts Initiative to promote the commercialization of low-emissions cement, concrete, asphalt binder, and asphalt mixtures.</p><p>The FHWA must establish and maintain a publicly available directory of state-submitted low-emissions products that the\u00a0FHWA determines to be eligible for reimbursement or incentives.</p><p>Further, the bill modifies the STBG program to allow states to issue advance purchase commitments for cement, concrete, asphalt binder, or asphalt mixtures (1) with superior durability and performance to conventional materials, or (2) that achieve superior performance with respect to environmental performance or energy efficiency. The bill allows for multi-year contracts, under specific conditions.</p>"
        },
        "title": "IMPACT Act 2.0"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2122.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>IMPACT Act 2.0</strong></p><p>This bill expands and modifies Federal Highway Administration (FHWA) programs, including the Surface Transportation Block Grant (STBG) program, to provide states reimbursement, incentives, and technical assistance to purchase low-emissions cement, concrete, asphalt binder, or asphalt mixtures. Under the bill, these are products that reduce, to the maximum extent practicable, greenhouse gas or directly related pollutant emissions to levels below the commercially available products.</p><p>Specifically, the FHWA\u00a0must provide to states</p><ul><li>reimbursement for the additional cost of using low-emissions cement, concrete, asphalt binder, and asphalt mixtures used in state highway projects;</li><li>incentives for the acquisition of these products for use in state highway projects;</li><li>technical assistance to update the state's specifications and standards to be performance-based specifications and standards; and</li><li>technical assistance to benchmark and quantify embodied greenhouse gas emissions (i.e., emissions associated with the production and transportation of goods).</li></ul><p>The FHWA must leverage the Every Day Counts Initiative to promote the commercialization of low-emissions cement, concrete, asphalt binder, and asphalt mixtures.</p><p>The FHWA must establish and maintain a publicly available directory of state-submitted low-emissions products that the\u00a0FHWA determines to be eligible for reimbursement or incentives.</p><p>Further, the bill modifies the STBG program to allow states to issue advance purchase commitments for cement, concrete, asphalt binder, or asphalt mixtures (1) with superior durability and performance to conventional materials, or (2) that achieve superior performance with respect to environmental performance or energy efficiency. The bill allows for multi-year contracts, under specific conditions.</p>",
      "updateDate": "2026-05-16",
      "versionCode": "id119hr2122"
    },
    "title": "IMPACT Act 2.0"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>IMPACT Act 2.0</strong></p><p>This bill expands and modifies Federal Highway Administration (FHWA) programs, including the Surface Transportation Block Grant (STBG) program, to provide states reimbursement, incentives, and technical assistance to purchase low-emissions cement, concrete, asphalt binder, or asphalt mixtures. Under the bill, these are products that reduce, to the maximum extent practicable, greenhouse gas or directly related pollutant emissions to levels below the commercially available products.</p><p>Specifically, the FHWA\u00a0must provide to states</p><ul><li>reimbursement for the additional cost of using low-emissions cement, concrete, asphalt binder, and asphalt mixtures used in state highway projects;</li><li>incentives for the acquisition of these products for use in state highway projects;</li><li>technical assistance to update the state's specifications and standards to be performance-based specifications and standards; and</li><li>technical assistance to benchmark and quantify embodied greenhouse gas emissions (i.e., emissions associated with the production and transportation of goods).</li></ul><p>The FHWA must leverage the Every Day Counts Initiative to promote the commercialization of low-emissions cement, concrete, asphalt binder, and asphalt mixtures.</p><p>The FHWA must establish and maintain a publicly available directory of state-submitted low-emissions products that the\u00a0FHWA determines to be eligible for reimbursement or incentives.</p><p>Further, the bill modifies the STBG program to allow states to issue advance purchase commitments for cement, concrete, asphalt binder, or asphalt mixtures (1) with superior durability and performance to conventional materials, or (2) that achieve superior performance with respect to environmental performance or energy efficiency. The bill allows for multi-year contracts, under specific conditions.</p>",
      "updateDate": "2026-05-16",
      "versionCode": "id119hr2122"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2122ih.xml"
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
      "title": "IMPACT Act 2.0",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "IMPACT Act 2.0",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To strengthen and enhance the competitiveness of cement, concrete, asphalt binder, and asphalt mixture production in the United States through the research, development, demonstration, and commercial application of technologies to reduce emissions from cement, concrete, asphalt binder, and asphalt mixture production, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T06:33:29Z"
    }
  ]
}
```
