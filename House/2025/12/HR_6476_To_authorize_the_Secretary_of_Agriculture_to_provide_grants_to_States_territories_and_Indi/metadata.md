# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6476?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6476
- Title: Relief for Farmers Hit with PFAS Act
- Congress: 119
- Bill type: HR
- Bill number: 6476
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-16T08:08:05Z
- Update date including text: 2026-05-16T08:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6476",
    "number": "6476",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "Relief for Farmers Hit with PFAS Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:05Z",
    "updateDateIncludingText": "2026-05-16T08:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:04:11Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-04",
      "state": "ME"
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
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6476ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6476\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Ms. Pingree (for herself, Mr. Lawler , and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo authorize the Secretary of Agriculture to provide grants to States, territories, and Indian Tribes to address contamination by perfluoroalkyl and polyfluoroalkyl substances on farms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Relief for Farmers Hit with PFAS Act .\n#### 2. Definitions\nIn this Act:\n**(1) Agricultural land**\n**(A) In general**\nThe term agricultural land means any land that is used, or capable of use without substantial modification, for production of farm products.\n**(B) Inclusions**\nThe term agricultural land includes irrigation water, livestock water, surface water, groundwater, and agricultural inputs on or associated with land described in subparagraph (A).\n**(2) Commercial farm**\nThe term commercial farm means a farm on which a person produces any farm product with the intent that the farm product be sold or otherwise disposed of to generate income.\n**(3) Eligible government**\nThe term eligible government means\u2014\n**(A)**\na State;\n**(B)**\nthe District of Columbia;\n**(C)**\na territory of the United States; and\n**(D)**\nan Indian Tribe.\n**(4) Farm product**\n**(A) In general**\nThe term farm product means any plant or animal that is useful to humans.\n**(B) Inclusions**\nThe term farm product includes\u2014\n**(i)**\nforages;\n**(ii)**\nsod crops;\n**(iii)**\ngrains;\n**(iv)**\nfood crops;\n**(v)**\ndairy products;\n**(vi)**\npoultry and poultry products;\n**(vii)**\nbees;\n**(viii)**\nlivestock and livestock products;\n**(ix)**\nproducts of aquaculture;\n**(x)**\nfruits;\n**(xi)**\nberries;\n**(xii)**\nvegetables;\n**(xiii)**\nflowers;\n**(xiv)**\nseeds;\n**(xv)**\ngrasses;\n**(xvi)**\nChristmas trees; and\n**(xvii)**\nother similar products, as determined by the Secretary.\n**(5) Perfluoroalkyl or polyfluoroalkyl substance; PFAS**\nThe term perfluoroalkyl or polyfluoroalkyl substance or PFAS means a chemical that\u2014\n**(A)**\ncontains at least one of\u2014\n**(i)**\nR\u2013(CF2)\u2013CF(R\u2032)R\u2032\u2032, where both the CF2 and CF moieties are saturated carbons, and none of the R groups can be hydrogen;\n**(ii)**\nR\u2013CF2OCF2\u2013R\u2032, where both the CF2 moieties are saturated carbons, and none of the R groups can be hydrogen; or\n**(iii)**\nCF3C(CF3)RR\u2032, where all the carbons are saturated, and none of the R groups can be hydrogen; or\n**(B)**\nis covered by the most recent working definition of PFAS issued by the Administrator of the Environmental Protection Agency.\n**(6) Program**\nThe term program means the program established under section 3(a).\n**(7) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(8) Septage**\nThe term septage means waste, refuse, effluent, sludge, and any other materials from septic tanks, cesspools, or any other similar facilities.\n**(9) Sludge**\nThe term sludge means\u2014\n**(A)**\nsolid, semisolid, or liquid waste generated from a municipal, commercial, or industrial\u2014\n**(i)**\nwastewater treatment plant;\n**(ii)**\nwater supply treatment plant; or\n**(iii)**\nwet process air pollution control facility; and\n**(B)**\nany other waste having similar characteristics and effect.\n#### 3. Establishment\n##### (a) In general\nThe Secretary shall establish a program under which the Secretary shall provide grants to eligible governments for the purposes described in section 4(a).\n##### (b) Eligibility\n**(1) In general**\nTo be eligible to receive a grant under the program, the territory of an eligible government shall contain\u2014\n**(A)**\nagricultural land that contains any soil with levels of PFAS that the Secretary, in coordination with the Administrator of the Environmental Protection Agency, determines to be unsafe; or\n**(B)**\nwater used for the production of farm products with levels of PFAS that the Administrator of the Environmental Protection Agency, in coordination with the Secretary, determines to be unsafe.\n**(2) Consideration**\nIn determining the eligibility of an eligible government for a grant under the program, the Secretary, in consultation with the Administrator of the Environmental Protection Agency, shall consider State standards and limitations relating to soil and water.\n##### (c) Applications\n**(1) In general**\nTo receive a grant under the program, the Department of Agriculture or similar agency of an eligible government shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Spend plan**\nAn application submitted under paragraph (1) shall contain a plan describing how the eligible government will administer the funding received under the program, including funding priorities and oversight.\n##### (d) Set-Aside\nEach year, the Secretary shall provide not less than 30 percent of the total funding provided under the program to 1 or more eligible governments with a population of less than 3,000,000.\n#### 4. Purposes\n##### (a) In general\nAn eligible government may use a grant received under the program to provide funding for any of the following purposes:\n**(1)**\nMonitoring (including through blood serum testing) the PFAS-related health complications of a person, and members of the household of that person, if agricultural land the person lives or works on is found to be contaminated by PFAS.\n**(2)**\nBuying, selling, or providing compensation for agricultural land or farm products found, through test results provided to the eligible government, to be contaminated by PFAS, including costs associated with the depopulation or disposal of farm products, premortem or postmortem.\n**(3)**\nInvesting in agricultural equipment, facilities, and infrastructure to ensure that agricultural land that, or a commercial farm any agricultural land of which, is found to be contaminated by PFAS maintains profitability while the producers on the agricultural land, in response to the PFAS contamination\u2014\n**(A)**\ntransition to an alternative production system; or\n**(B)**\nimplement remediation strategies (including disposal), technological adaptations, or other modifications to the operations of the agricultural land or commercial farm.\n**(4)**\nAssisting the producers on agricultural land that, or a commercial farm any agricultural land of which, is found to be contaminated by PFAS in developing an enterprise budget for\u2014\n**(A)**\nalternative production systems;\n**(B)**\nremediation strategies;\n**(C)**\ntechnological adaptations;\n**(D)**\ntransitioning to an alternative revenue stream; or\n**(E)**\nrelocating a farming operation to new agricultural land.\n**(5)**\nProviding financial assistance to a person the commercial farm of which is found to be contaminated by PFAS, including income replacement.\n**(6)**\nEvaluating and expanding the capacity of PFAS testing and data management in the territory of the eligible government.\n**(7)**\nConducting research that\u2014\n**(A)**\nsupports short-term farm management decisions with respect to agricultural land that has been contaminated by PFAS; and\n**(B)**\nassesses future options for viable uses of agricultural land and water used for agricultural production that has been contaminated by PFAS.\n**(8)**\nConducting research that quantifies the impact of PFAS on commercial farms and agricultural communities in the territory of the eligible government.\n**(9)**\nConducting research on\u2014\n**(A)**\nsoil and water remediation systems;\n**(B)**\nthe viability of those systems for PFAS-contaminated commercial farms;\n**(C)**\nthe composting or disposal of PFAS-contaminated crops or livestock;\n**(D)**\nimplementing alternative production systems in response to PFAS contamination;\n**(E)**\nthe PFAS uptake of various farm products; and\n**(F)**\nfood safety relating to PFAS contamination.\n**(10)**\nDeveloping and implementing educational programs for owners of agricultural land, including determining best practices for\u2014\n**(A)**\ninforming residents about the potential of being near or on a site on which sludge or septage application was licensed or permitted by the eligible government or the Federal Government; and\n**(B)**\nproviding information and guidance on buying or selling agricultural land on which sludge or septage was applied.\n**(11)**\nLong-term monitoring of agricultural land contaminated by PFAS and establishing a corresponding centralized data repository.\n**(12)**\nAssisting owners and operators of commercial farms not directly affected by PFAS contamination with marketing efforts whose branding and marketing may be affected by the public perception of PFAS contamination in the territory of the eligible government.\n**(13)**\nVoluntary testing of farm products, agricultural land, or other locations that are suspected to be contaminated with PFAS.\n##### (b) Priority\n**(1) In general**\nIn using funding received under the program, an eligible government shall prioritize purposes that directly assist producers who are experiencing financial losses due to agricultural PFAS contamination.\n**(2) Department of Agriculture priority**\nIn providing grants under the program, the Secretary shall prioritize the provision of grants to eligible governments that will use the grant funds for the purposes described in paragraphs (3) through (5) of subsection (a).\n#### 5. Reports\nEach year of the period of a grant received under the program, the department of agriculture or similar agency of an eligible government shall submit to the Secretary and Congress a report describing\u2014\n**(1)**\nthe uses of the grant during the previous year, including\u2014\n**(A)**\nthe purposes described in section 4(a) for which the grant was used;\n**(B)**\nthe amount of the grant allocated to each purpose described in section 4(a); and\n**(C)**\nthe extent to which the funding received under the program, including funding priorities and oversight, was administered in accordance with the plan described in section 3(c)(2);\n**(2)**\nany additional needs identified by agricultural producers in the territory of the eligible government; and\n**(3)**\nany additional information the Secretary determines to be appropriate.\n#### 6. Task force\nThe Secretary shall establish a task force composed of officers or employees of the Department of Agriculture\u2014\n**(1)**\nto provide advice to the Secretary relating to whether addressing PFAS contamination should be added as an eligible activity under each program of the Department of Agriculture;\n**(2)**\nto evaluate necessary actions for farms already enrolled in a Department of Agriculture program where PFAS is detected; and\n**(3)**\nto provide technical assistance to eligible governments in addressing PFAS contamination.\n#### 7. Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this Act $500,000,000 for the period of fiscal years 2026 through 2029.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S8513)"
      },
      "number": "3353",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Relief for Farmers Hit with PFAS Act",
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
        "updateDate": "2026-01-07T16:03:07Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6476ih.xml"
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
      "title": "Relief for Farmers Hit with PFAS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Relief for Farmers Hit with PFAS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Agriculture to provide grants to States, territories, and Indian Tribes to address contamination by perfluoroalkyl and polyfluoroalkyl substances on farms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:19Z"
    }
  ]
}
```
