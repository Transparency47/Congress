# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2496?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2496
- Title: Dairy Nutrition Incentive Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2496
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-04-10T08:05:42Z
- Update date including text: 2026-04-10T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2496",
    "number": "2496",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Dairy Nutrition Incentive Program Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:42Z",
    "updateDateIncludingText": "2026-04-10T08:05:42Z"
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
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:13:00Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "ME"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "WA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "WI"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "OH"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "AL"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "OR"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "WI"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "CO"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "SD"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NY"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "WI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "OR"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MN"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "UT"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "KS"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "IN"
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
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2496ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2496\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Costa (for himself, Mr. Langworthy , Ms. Pingree , Mr. Newhouse , Mr. Panetta , Mr. Rouzer , Mr. Van Orden , Mr. Miller of Ohio , Mr. Rogers of Alabama , Ms. Bonamici , Mr. Grothman , Mr. Riley of New York , and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to establish a dairy nutrition incentive program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dairy Nutrition Incentive Program Act of 2025 .\n#### 2. Dairy nutrition incentive program\n##### (a) In general\nThe Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) is amended by adding at the end the following:\n31. Dairy nutrition incentive program (a) Definitions In this section: (1) Dairy product The term dairy product means a product for which cow\u2019s milk is listed as\u2014 (A) the first ingredient on the labeled ingredients list of the product; or (B) the second ingredient on the labeled ingredients list of the product, if the first listed ingredient is water. (2) Eligible entity The term eligible entity means\u2014 (A) a State or local governmental entity; and (B) a nonprofit organization. (3) Fluid milk The term fluid milk means any variety of pasteurized cow\u2019s milk that\u2014 (A) is packaged in liquid form; and (B) contains vitamins A and D at levels consistent with the Food and Drug Administration standards, and applicable State and local standards, for fluid milk. (4) Naturally nutrient-rich dairy The term naturally nutrient-rich dairy means\u2014 (A) fluid milk; (B) yogurt and other cultured cow\u2019s milk dairy products; and (C) cheese (including nonstandardized cheese) made from cow\u2019s milk. (5) Program The term program means the dairy nutrition incentive program established under subsection (b). (b) Establishment Not later than 180 days after the date of enactment of this section, the Secretary shall establish a dairy nutrition incentive program under which the Secretary shall develop and test methods to increase the purchase and consumption of naturally nutrient-rich dairy by members of households that receive benefits under the supplemental nutrition assistance program by providing an incentive for the purchase of naturally nutrient-rich dairy at the point of purchase to members of households purchasing food using those benefits. (c) Grants or cooperative agreements (1) In general To carry out the program, the Secretary shall enter into cooperative agreements with, or provide grants to, eligible entities, on a competitive basis, for projects that meet the purpose of the program described in subsection (b). (2) Application An eligible entity seeking to enter into a cooperative agreement or receive a grant under the program shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (3) Selection criteria The Secretary shall develop and make public criteria for evaluating proposed projects in applications submitted under paragraph (2), which shall incorporate a scientifically based strategy designed to improve diet quality and nutritional outcomes through the increased purchase of naturally nutrient-rich dairy. (4) Priority In entering into cooperative agreements and awarding grants under the program, the Secretary shall give priority to projects that\u2014 (A) maximize the percentage of funds used for direct incentives for participants in the supplemental nutrition assistance program; (B) include a project design\u2014 (i) that provides incentives when naturally nutrient-rich dairy is purchased using benefits under the supplemental nutrition assistance program; and (ii) in which the incentives earned may be used only to purchase naturally nutrient-rich dairy; (C) include project sites that serve members of households that participate in the supplemental nutrition assistance program; and (D) incorporate the use of point-of-sale systems that can electronically issue incentives earned under the program. (5) Additional financial assistance An eligible entity may request funds from the Secretary, pursuant to section 16, to offset initial costs to enable electronic benefits transfer technology for electronic point-of-sale systems described in paragraph (4)(D) for projects sites selected under the program. (d) Evaluation (1) In general The Secretary shall provide for an independent evaluation of each project carried out under the program that measures, to the maximum extent practicable, the effect of incentives on purchases of naturally nutrient-rich dairy by members of households that receive benefits under the supplemental nutrition assistance program. (2) Methodology requirement The independent evaluation under paragraph (1) shall use rigorous methodologies, such as random assignment or other methods that are capable of producing scientifically valid information regarding activities that are effective. (3) Discontinuance (A) In general Except as provided in subparagraph (B), subject to availability of funds, nothing in this section shall limit the continuation of a project carried out under the program. (B) Noncompliance The Secretary may discontinue a project or close a project site under the program if the project\u2014 (i) does not comply with the requirements under this section; (ii) does not comply with the requirements of the grant awarded or cooperative agreement entered into under the program, as applicable; or (iii) if the Secretary determines that the results of the independent evaluation of the project under paragraph (1) are not satisfactory. (4) Public dissemination The Secretary shall make publicly available the results of each independent evaluation carried out under paragraph (1). (e) Report Not later than December 31 of the first full calendar year following the date of establishment of the program, and biennially thereafter, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report that includes a description of\u2014 (1) the status of each project carried out under the program; and (2) the results of each completed evaluation under paragraph (1) during the period covered by the report. (f) Funding (1) Mandatory funding There is appropriated to the Secretary, out of any funds in the Treasury not otherwise appropriated, $10,000,000 for each fiscal year to carry out this section. (2) Authorization of appropriations (A) In general In addition to the funds made available under paragraph (1), there is authorized to be appropriated to the Secretary to carry out this section $10,000,000 for fiscal year 2026 and each fiscal year thereafter. (B) Appropriations in advance With respect to any funds made available under subparagraph (A), only funds appropriated in advance specifically to carry out this section shall be available to carry out this section. (3) Evaluation costs Of the funds made available to carry out this section for a fiscal year, the Secretary shall use not more than 7 percent to carry out subsection (d). (4) Limitation on use Funds made available to carry out this section shall not be used for any project that limits the use of benefits under the supplemental nutrition assistance program. .\n##### (b) Transition from healthy fluid milk incentives projects\n**(1) In general**\nThe Secretary of Agriculture (referred to in this subsection as the Secretary ) shall transition projects carried out under section 4208 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2026a ) to be carried out as part of the dairy nutrition incentive program established under section 31 of the Food and Nutrition Act of 2008.\n**(2) No interruption**\nIn carrying out paragraph (1), the Secretary shall ensure that\u2014\n**(A)**\nthere is no interruption in projects being carried out under section 4208 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2026a ) during the transition described in that paragraph; and\n**(B)**\nany additional authorities or flexibilities under the dairy nutrition incentive program established under section 31 of the Food and Nutrition Act of 2008 shall be applied to the projects described in subparagraph (A).\n**(3) Repeal**\nEffective 1 year after the date on which the Secretary certifies that the Secretary has completed carrying out paragraph (1), section 4208 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2026a ) is repealed.",
      "versionDate": "2025-03-31",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1021",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Dairy Nutrition Incentive Program Act of 2025",
      "type": "S"
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
        "updateDate": "2025-05-06T21:08:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119hr2496",
          "measure-number": "2496",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2025-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2496v00",
            "update-date": "2025-05-12"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dairy Nutrition Incentive Program Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a dairy nutrition incentive program to develop and test methods to increase the purchase and consumption of dairy under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the program must provide an incentive to SNAP benefit recipients for the purchase of naturally nutrient-rich dairy, which the bill defines to include fluid milk, yogurt, and cheese made from cow's milk. To carry out the program, USDA must enter into cooperative agreements with, or provide competitive grants to, state or local governments and nonprofit organizations for projects. The bill provides funding for the program for each fiscal year.</p><p>USDA must provide for an independent evaluation of each project that measures, to the maximum extent practicable, the effect of incentives on purchases of naturally nutrient-rich dairy by SNAP recipients.</p><p>Projects currently carried out by the USDA Healthy Fluid Milk Incentives (HFMI) program must be transitioned to the new dairy nutrition incentive program; the bill repeals the HFMI program one year after USDA certifies that the transition is complete.</p>"
        },
        "title": "Dairy Nutrition Incentive Program Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2496.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dairy Nutrition Incentive Program Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a dairy nutrition incentive program to develop and test methods to increase the purchase and consumption of dairy under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the program must provide an incentive to SNAP benefit recipients for the purchase of naturally nutrient-rich dairy, which the bill defines to include fluid milk, yogurt, and cheese made from cow's milk. To carry out the program, USDA must enter into cooperative agreements with, or provide competitive grants to, state or local governments and nonprofit organizations for projects. The bill provides funding for the program for each fiscal year.</p><p>USDA must provide for an independent evaluation of each project that measures, to the maximum extent practicable, the effect of incentives on purchases of naturally nutrient-rich dairy by SNAP recipients.</p><p>Projects currently carried out by the USDA Healthy Fluid Milk Incentives (HFMI) program must be transitioned to the new dairy nutrition incentive program; the bill repeals the HFMI program one year after USDA certifies that the transition is complete.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119hr2496"
    },
    "title": "Dairy Nutrition Incentive Program Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dairy Nutrition Incentive Program Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a dairy nutrition incentive program to develop and test methods to increase the purchase and consumption of dairy under the Supplemental Nutrition Assistance Program (SNAP).</p><p>Specifically, the program must provide an incentive to SNAP benefit recipients for the purchase of naturally nutrient-rich dairy, which the bill defines to include fluid milk, yogurt, and cheese made from cow's milk. To carry out the program, USDA must enter into cooperative agreements with, or provide competitive grants to, state or local governments and nonprofit organizations for projects. The bill provides funding for the program for each fiscal year.</p><p>USDA must provide for an independent evaluation of each project that measures, to the maximum extent practicable, the effect of incentives on purchases of naturally nutrient-rich dairy by SNAP recipients.</p><p>Projects currently carried out by the USDA Healthy Fluid Milk Incentives (HFMI) program must be transitioned to the new dairy nutrition incentive program; the bill repeals the HFMI program one year after USDA certifies that the transition is complete.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119hr2496"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2496ih.xml"
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
      "title": "Dairy Nutrition Incentive Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dairy Nutrition Incentive Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to establish a dairy nutrition incentive program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:32Z"
    }
  ]
}
```
