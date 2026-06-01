# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/891?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/891
- Title: Pro-Housing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 891
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-04-07T14:44:16Z
- Update date including text: 2025-04-07T14:44:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/891",
    "number": "891",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000579",
        "district": "18",
        "firstName": "Patrick",
        "fullName": "Rep. Ryan, Patrick [D-NY-18]",
        "lastName": "Ryan",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Pro-Housing Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-07T14:44:16Z",
    "updateDateIncludingText": "2025-04-07T14:44:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-01",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-01T15:45:19Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-31T15:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr891ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 891\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Ryan introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Housing and Urban Development and the Administrator of the General Services Administration to establish programs for the development of affordable housing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pro-Housing Act of 2025 .\n#### 2. Local housing policy grant and loan pilot program\n##### (a) Planning grants\nBeginning not later than 120 days after the date of the enactment of this section, the Secretary shall award grants on a competitive basis to eligible entities for the purpose of developing and evaluating housing policy plans.\n##### (b) Implementation grants\nBeginning not later than 120 days after the date of the enactment of this section, the Secretary shall award grants on a competitive basis to eligible entities for the purpose of implementing housing policy plans.\n##### (c) Direct loans\n**(1) In general**\nBeginning not later than 120 days after the date of the enactment of this section, the Secretary shall provide direct loans to eligible entities for the purpose of implementing housing policy plans.\n**(2) Terms and limitations**\n**(A) In general**\nA direct loan provided under this section shall be subject to such terms and conditions as the Secretary determines appropriate.\n**(B) Interest rate**\nThe interest rate on a direct loan provided under this section shall be less than the yield on United States Treasury obligations of a similar maturity to the maturity of the direct loan on the date of execution of the loan agreement, at a rate determined by the Secretary, for the purpose of providing low-cost credit to eligible entities.\n##### (d) Rural and exurban area minimum\nThe Secretary shall provide not less than 20 percent of the amounts awarded or loaned under this section to eligible entities that plan to use them to assist an area that is rural or exurban, as determined by the Secretary in consultation the Director of the United States Census Bureau.\n##### (e) Applications\n**(1) In general**\nAn eligible entity seeking a planning grant, implementation grant, or direct loan provided under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Priority**\nIn awarding a planning grant, implementation grant, or direct loan provided under this section, the Secretary shall give priority to eligible entities that\u2014\n**(A)**\nhave developed or are likely to develop a housing policy plan that will\u2014\n**(i)**\nimprove housing supply, affordability, and accessibility for all individuals of every race and income level;\n**(ii)**\nreduce barriers to affordable housing development; and\n**(iii)**\navoid the displacement of residents by new housing developments in the area under the jurisdiction of the eligible entity;\n**(B)**\nin developing or implementing a housing policy plan, intend to leverage and efficiently use amounts from\u2014\n**(i)**\nanother Federal, State, or local assistance program relating to housing; or\n**(ii)**\na private funding source;\n**(C)**\nintend to\u2014\n**(i)**\nincrease the supply and affordability of housing that is located\u2014\n**(I)**\nnear local transit options; and\n**(II)**\nin areas in which a significant or expanding supply of jobs or demand for employment is concentrated;\n**(ii)**\ncoordinate with local transportation and workforce agencies in accomplishing the increase described in clause (i);\n**(iii)**\nleverage existing infrastructure by rehabilitating or converting existing properties when developing or implementing a housing policy plan; and\n**(iv)**\nwhere appropriate, coordinate policy development for, and analysis and implementation of, the housing policy plan of the eligible entity at a regional scale to achieve a more equitable distribution of affordable housing across jurisdictional boundaries; or\n**(D)**\nare a coalition of States or political subdivisions of States.\n**(3) Scoring**\nThe Secretary shall base the degree of priority given to an eligible entity that satisfies 1 or more subparagraphs under paragraph (2) on a scoring system established by the Secretary.\n##### (f) Matching requirement for grants\n**(1) In general**\nAn eligible entity that receives a planning grant or implementation grant shall contribute non-Federal amounts for developing or implementing a housing policy plan financed using amounts provided in such grant in the following amounts:\n**(A)**\nIf the area under the jurisdiction of an eligible entity has a population of 15,000 or fewer, the eligible entity shall provide non-Federal contributions in an amount equal to 15 percent of the amount of the grant.\n**(B)**\nIf the area under the jurisdiction of an eligible entity has a population between 15,001 and 30,000, the eligible entity shall provide non-Federal contributions in an amount equal to 25 percent of the amount of the grant.\n**(C)**\nIf the area under the jurisdiction of an eligible entity has a population between 30,001 and 40,000, the eligible entity shall provide non-Federal contributions in an amount equal to 35 percent of the amount of the grant.\n**(D)**\nIf the area under the jurisdiction of an eligible entity has a population between 40,001 and 70,000, the eligible entity shall provide non-Federal contributions in an amount equal to 45 percent of the amount of the grant.\n**(E)**\nIf the area under the jurisdiction of an eligible entity has a population of 70,001 or more, the eligible entity shall provide non-Federal contributions in an amount equal to 45 percent of the amount of the grant.\n**(2) Eligible matching amounts**\nIf an eligible entity uses amounts provided by the Federal Government not under this section to develop or implement a housing policy plan for which the eligible entity also receives a grant under this section, any non-Federal contribution made by the eligible entity as part of that Federal assistance program shall be counted towards the requirements under paragraph (1).\n**(3) Reduced matching requirement**\nBased on the available resources of an eligible entity, the Secretary may, at the discretion of the Secretary, reduce the amount of non-Federal contributions required to be provided by the eligible entity under paragraphs (1) and (2).\n##### (g) Use of funds\n**(1) In general**\nAn eligible entity that receives a planning grant, implementation grant, or direct loan provided under this section shall use a portion of the amounts from such grant or loan to submit the report required under subsection (j)(1).\n**(2) Planning grants**\nAn eligible entity that receives a planning grant shall use amounts from such grant to finance activities to develop and evaluate a housing policy plan for the area under the jurisdiction of the eligible entity, including\u2014\n**(A)**\nquantifying existing and projected housing needs for households of every income level, including extremely low-income families, as defined in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) );\n**(B)**\ndocumenting the characteristics of\u2014\n**(i)**\nthe housing in the area;\n**(ii)**\nthe households of the area, including cost-burdened households; and\n**(iii)**\nhousing underproduction in the area;\n**(C)**\ndeveloping strategies to increase the housing supply and the variety of housing types in the area to satisfy the housing needs of the population of the area;\n**(D)**\nanalyzing population and employment trends in the area and documenting projections of those trends;\n**(E)**\nconsidering strategies to minimize displacement of low-income families, as defined in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ), as a result of redevelopment in the area;\n**(F)**\nproviding for participation and input from community members, community groups, local builders, local realtors, nonprofit housing advocates, and local religious groups; and\n**(G)**\ncreating a schedule of programs and actions to implement the recommendations of the housing policy plan, including a plan for adopting actions through a local implementing ordinance or another regulatory process, such as a land use plan or a comprehensive plan.\n##### (h) Housing policy plan guidance\n**(1) In general**\nNot later than 90 days after the date of the enactment of this section, the Secretary shall issue guidance that includes recommended policies, strategies, and reforms for eligible entities to adopt in housing policy plans to\u2014\n**(A)**\nimprove the elasticity of housing supply;\n**(B)**\nexpand the supply and affordability of housing;\n**(C)**\nreduce barriers to housing development; and\n**(D)**\nmeaningfully reduce housing segregation by income and race.\n**(2) Policies**\nThe guidance issued under paragraph (1) shall include recommendations for policies, strategies, and reforms to\u2014\n**(A)**\nencourage and support the repurposing of land or structures for housing development;\n**(B)**\nallow for a greater variety of housing types;\n**(C)**\nrevise land use policies to allow for the development of more housing;\n**(D)**\nstreamline approval processes for housing development;\n**(E)**\nprovide financial incentives to support affordable housing development; and\n**(F)**\nsupport inclusive engagement with community members relating to reforms to expand housing supply.\n**(3) Areas**\nThe guidance issued under paragraph (1) shall include recommendations for policies, strategies, and reforms for urban, suburban, exurban, and rural areas.\n##### (i) Learning network\n**(1) In general**\nNot later than 1 year after the date on which the Secretary awards the first planning grant, implementation grant, or direct loan provided under this section, the Secretary shall establish a learning network to\u2014\n**(A)**\nfacilitate problem solving relating to the development and implementation of housing policy plans; and\n**(B)**\ndisseminate best practices and effective strategies and policies to improve local housing supply and affordability.\n**(2) Accessibility**\nThe learning network established under paragraph (1) shall be accessible to\u2014\n**(A)**\neligible entities that receive a grant or loan under this section; and\n**(B)**\neligible entities that submit an application under subsection (e).\n##### (j) Reports and study\n**(1) Grant and loan recipient reports**\nNot later than 180 days after the date on which an eligible entity receives a planning grant, implementation grant, or direct loan provided under this section, and not less frequently than quarterly thereafter for a 3-year period, the eligible entity shall submit to the Secretary a report that includes\u2014\n**(A)**\na description of the expenditures the eligible entity has made with amounts from such grant or loan;\n**(B)**\nfor an eligible entity receiving a planning grant, a summary of the progress of the eligibility entity towards finalizing a housing policy plan; and\n**(C)**\nfor an eligible entity receiving an implementation grant, data relating to the success of the implementation of the housing policy plan of the eligible entity.\n**(2) Secretary study and report**\n**(A) In general**\nNot later than 5 years after the date of the enactment of this section, the Secretary shall conduct a study with respect to\u2014\n**(i)**\nthe impact of implementation grants, planning grants, and direct loans provided under this section on the areas under the jurisdiction of eligible entities receiving those grants or loans; and\n**(ii)**\nsuccessful strategies from housing policy plans that were impactful in\u2014\n**(I)**\nexpanding the housing supply; and\n**(II)**\nincreasing the quantity of quality and affordable housing while avoiding the displacement of the residents of an area.\n**(B) Report**\nNot later than 1 year after the date on which the Secretary completes the study required under subparagraph (A), the Secretary shall submit to the appropriate committees of the Congress a report on the study.\n##### (k) Appropriations\n**(1) In general**\nThere are authorized to be appropriated to the Secretary $200,000,000 for each of fiscal years 2026 through 2031 to carry out this section.\n**(2) Costs of direct loans**\nThe Secretary may use any amounts made available under paragraph (1) to pay the costs of providing direct loans under this section.\n##### (l) Definitions\nIn this section:\n**(1) Cost-burdened household**\nThe term cost-burdened household means a household that spends not less than 30 percent of the income of the household on housing.\n**(2) Department**\nThe term Department means the Department of Housing and Urban Development.\n**(3) Direct loan**\nThe term direct loan has the meaning given the term in section 502 of the Federal Credit Reform Act ( 2 U.S.C. 661a ).\n**(4) Eligible entity**\nThe term eligible entity means a State, a political subdivision of a State, a coalition of States or political subdivisions of States, an Indian Tribe, or a Native Hawaiian organization that\u2014\n**(A)**\ndemonstrates, with respect to the area under the jurisdiction of the State, political subdivision, coalition, Indian Tribe, or organization\u2014\n**(i)**\nrising housing costs or a reasonable expectation that housing costs will rise in the area; and\n**(ii)**\na housing supply shortage;\n**(B)**\nif applying for a planning grant\u2014\n**(i)**\nintends to develop, or is in the process of developing, a housing policy plan; and\n**(ii)**\ndemonstrates an intent to use a portion of the planning grant to engage with community stakeholders and housing practitioners in developing a housing policy plan; and\n**(C)**\nif applying for an implementation grant or direct loan under this section\u2014\n**(i)**\nhas adopted and plans to implement, or is in the process of implementing, a housing policy plan; and\n**(ii)**\ndemonstrates the engagement of community stakeholders and housing practitioners in developing the housing policy plan.\n**(5) Housing policy plan**\nThe term housing policy plan means a comprehensive plan of an eligible entity to, with respect to the area under the jurisdiction of the eligible entity\u2014\n**(A)**\nincrease the housing supply in the area, while avoiding the displacement of the residents of the area;\n**(B)**\nincrease the affordability of housing in the area; and\n**(C)**\nreduce barriers to housing development in the area.\n**(6) Implementation grant**\nThe term implementation grant means a grant awarded under subsection (b).\n**(7) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(8) Native Hawaiian organization**\nThe term Native Hawaiian organization has the meaning given the term in section 2 of the Native American Graves Protection and Repatriation Act ( 25 U.S.C. 3001 ).\n**(9) Planning grant**\nThe term planning grant means a grant awarded under subsection (a).\n**(10) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development, acting through the Assistant Secretary for Community Planning and Development, in coordination with\u2014\n**(A)**\nthe Office of Economic Resilience of the Office of Community Planning and Development of the Department;\n**(B)**\nthe Office of Policy Development and Research of the Department;\n**(C)**\nthe Office of Fair Housing and Equal Opportunity of the Department;\n**(D)**\nthe Office of Housing of the Department; and\n**(E)**\nthe Office of Public and Indian Housing of the Department.\n**(11) State**\nThe term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, and any possession of the United States.\n#### 3. Transfer of unused Federal real property to State and local authorities for development\n##### (a) In general\nNot later than 120 days after the date of the enactment of this section, the Administrator of General Services shall establish a pilot program under which unused Federal real property is transferred in accordance with subsection (b)(2) to eligible entities for the development of mixed-use neighborhoods or affordable housing.\n##### (b) Transfer of property\n**(1) In general**\nAny unused Federal real property shall be transferred by the head of the agency concerned to the Administrator.\n**(2) Transfer to eligible entity**\nThe Administrator shall transfer to eligible entities any unused Federal real property transferred to the Administrator under paragraph (1).\n##### (c) Sunset\nAny transfers of property described in subsection (b) shall terminate on the date that is 5 years after the date of the enactment of this section.\n##### (d) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the General Services.\n**(2) Affordable housing**\nThe term affordable housing means housing that qualifies as affordable housing under section 215 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12745 ).\n**(3) Agency**\nThe term agency has the meaning given the term Executive agency in section 105 of title 5, United States Code.\n**(4) Eligible entity**\nThe term eligible entity means an entity established under State or local law as responsible for housing and urban development planning.\n**(5) Unused Federal real property**\nThe term unused Federal real property means land or a building\u2014\n**(A)**\nowned by the Federal Government; and\n**(B)**\ndeclared unused by the head of an agency.",
      "versionDate": "2025-01-31",
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
            "name": "Community life and organization",
            "updateDate": "2025-04-07T14:43:57Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-04-07T14:43:22Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-07T14:44:05Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-04-07T14:43:11Z"
          },
          {
            "name": "Housing supply and affordability",
            "updateDate": "2025-04-07T14:43:16Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-04-07T14:44:10Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-04-07T14:44:16Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-04-07T14:43:51Z"
          },
          {
            "name": "Residential rehabilitation and home repair",
            "updateDate": "2025-04-07T14:43:43Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-04-07T14:43:27Z"
          },
          {
            "name": "Urban and suburban affairs and development",
            "updateDate": "2025-04-07T14:43:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-04T17:21:56Z"
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
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr891ih.xml"
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
      "title": "Pro-Housing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pro-Housing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Housing and Urban Development and the Administrator of the General Services Administration to establish programs for the development of affordable housing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:27Z"
    }
  ]
}
```
