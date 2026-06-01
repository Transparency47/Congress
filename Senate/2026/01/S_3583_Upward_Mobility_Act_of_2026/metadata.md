# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3583?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3583
- Title: Upward Mobility Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3583
- Origin chamber: Senate
- Introduced date: 2026-01-06
- Update date: 2026-04-21T19:18:12Z
- Update date including text: 2026-04-21T19:18:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-06: Introduced in Senate
- 2026-01-06 - IntroReferral: Introduced in Senate
- 2026-01-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-06: Introduced in Senate

## Actions

- 2026-01-06 - IntroReferral: Introduced in Senate
- 2026-01-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-06",
    "latestAction": {
      "actionDate": "2026-01-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3583",
    "number": "3583",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Upward Mobility Act of 2026",
    "type": "S",
    "updateDate": "2026-04-21T19:18:12Z",
    "updateDateIncludingText": "2026-04-21T19:18:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-06",
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
          "date": "2026-01-06T22:21:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "MT"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3583is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. 3583\nIN THE SENATE OF THE UNITED STATES\nJanuary 6, 2026 Mr. Husted introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo establish a pilot program in which States may use consolidated funds, through Upward Mobility Grants, for antipoverty programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Upward Mobility Act of 2026 .\n#### 2. Consolidation of antipoverty programs\n##### (a) Definitions\nIn this section:\n**(1) Antipoverty objectives**\nThe term antipoverty objectives means the objectives described in subsection (b)(2).\n**(2) Antipoverty program**\nThe term antipoverty program means the set of activities for which a covered amount may be used.\n**(3) Covered amount**\n**(A) In general**\nSubject to subparagraph (B), the term covered amount means\u2014\n**(i)**\nan amount that a State is eligible to receive in Federal funds, through a grant, contract, or other payment\u2014\n**(I)**\nunder subsection (a) or (h) of section 16 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025 ) (relating to the supplemental nutrition assistance program);\n**(II)**\nfor benefits (as defined in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 )) for participants of the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) pursuant to section 4(a)(1) of that Act ( 7 U.S.C. 2013(a)(1) );\n**(III)**\nunder paragraph (1) or (2) of section 403(a) of the Social Security Act ( 42 U.S.C. 603(a) ) (relating to the temporary assistance for needy families program State family assistance grant);\n**(IV)**\nunder section 658O(b) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858m(b) ), from amounts appropriated under that Act or under section 418(a)(3)(A) of the Social Security Act ( 42 U.S.C. 618(a)(3)(A) ) (relating to a program of child care services);\n**(V)**\nunder section 2604 (other than subsection (e)), 2607A, 2607B, or 2609A of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8623 , 8626a, 8626b, or 8628a) (relating to programs of home energy assistance);\n**(VI)**\nunder section 132(b)(2)(B) or section 170 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3171(b)(2)(B) , 3225) (relating to assistance for dislocated workers); and\n**(VII)**\nunder subsection (b) or (d) of section 106 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5306 ) (relating to community development);\n**(ii)**\nthe amount that public housing agencies, as defined in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ), located in a State are eligible to receive through allocations\u2014\n**(I)**\nunder section 8(o) of such Act ( 42 U.S.C. 1437f(o) ) for tenant-based assistance; and\n**(II)**\nunder section 9 of such Act ( 42 U.S.C. 1437g ) for public housing from the Capital Fund and Operating Fund; and\n**(iii)**\nthe amount that persons and families located in a State (other than members of an Indian tribe) are eligible to receive in Federal assistance under section 521 of the Housing Act of 1949 ( 42 U.S.C. 1490a ).\n**(B) Rule**\nThe term covered amount \u2014\n**(i)**\nincludes an amount described in subparagraph (A) whether or not the State or public housing agency involved is directed to use the amount to provide funding for localities or other entities under Federal law, subject to clause (ii); and\n**(ii)**\ndoes not include any amount described in subparagraph (A) that a State or public housing agency is so directed to use to provide funding for an Indian tribe.\n**(4) Direct assistance benefits**\nThe term direct assistance benefits means\u2014\n**(A)**\nnutrition (including food) benefits;\n**(B)**\ncash benefits for low-income families and individuals;\n**(C)**\nchild care subsidies;\n**(D)**\nhome energy (including utility) assistance;\n**(E)**\nemployment and training services provided directly to a dislocated worker; and\n**(F)**\nhousing (including rent) subsidies.\n**(5) Indian tribe**\nThe term Indian tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Act ( 25 U.S.C. 5304 ).\n**(6) Marginal Effective Tax Rate**\nThe term Marginal Effective Tax Rate , used with respect to an individual, means the percentage of an increase in earned income attributable to the individual's employment, as determined for a State under subsection (j)(2), that is offset by\u2014\n**(A)**\nthe combined reduction or loss in value of per-capita direct assistance for the individual; and\n**(B)**\nthe combined increase in Federal, State, and local income and payroll taxes for the individual.\n**(7) Per-capita direct assistance**\nThe term per-capita direct assistance , used with respect to a State, means\u2014\n**(A)**\nthe total amount of Federal funding used in a pilot project in any year for direct assistance benefits from the funding sources listed in paragraph (3); divided by\n**(B)**\nthe population of the State.\n**(8) Secretary**\nThe term Secretary means the Secretary of Health and Human Services, acting through the Assistant Secretary for Children and Families.\n**(9) State**\nThe term State means each of the several States of the United States, and the District of Columbia.\n##### (b) Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto achieve the goals of\u2014\n**(A)**\nstreamlining service delivery and reducing inconsistent eligibility requirements and benefit cliffs through pilot projects promoting antipoverty objectives;\n**(B)**\npromoting upward mobility through improved employment outcomes described in subsection (j)(2)(B), including increased employment and earnings, among participants in a pilot project; and\n**(C)**\nproviding incentives to States to reduce dependence on per-capita direct assistance through the pilot projects by enabling individuals to achieve the improved employment outcomes; and\n**(2)**\nto accomplish those goals by authorizing States to apply to receive Upward Mobility Grants for the purpose of carrying out a pilot project to promote antipoverty objectives, consisting of\u2014\n**(A)**\nreduced benefit cliffs through benefit structures that limit Marginal Effective Tax Rates; and\n**(B)**\nincreased levels of employment and earnings among participants in programs covered by the pilot project, skills acquisition, housing (including rental housing) affordability, access to nutrition, reduced home energy costs, affordable child care, and temporary assistance to low-income families.\n##### (c) Establishment\n**(1) In general**\nThere is established a pilot program through which the Secretary may\u2014\n**(A)**\npermit not more than 5 States to carry out pilot projects; and\n**(B)**\nconsolidate funding from antipoverty programs into Upward Mobility Grants made under subsection (d)(1), and make those grants to the States to carry out the projects.\n**(2) Limited scope pilot projects**\nA State may elect to seek such permission and consolidated funding to carry out a limited scope pilot project described in the State\u2019s application under subsection (f).\n**(3) Duration**\nThe Secretary shall provide the permission and grants described in this subsection for a pilot project for a single period of 5 years.\n##### (d) Upward Mobility Grants\n**(1) Pilot project grant amounts**\nNotwithstanding any other provision of Federal law applicable to an antipoverty program, except as otherwise provided in this section, for each fiscal year of the pilot project period applicable to a pilot project approved for a State pursuant to subsection (g), the Secretary shall make an Upward Mobility Grant to the State, as calculated under paragraph (2), for purposes of carrying out the project for that fiscal year.\n**(2) Calculation**\n**(A) First year**\nFor the first fiscal year of the pilot project, the Secretary shall make an Upward Mobility Grant to the State, in a sum calculated as the total of the covered amounts received by the State, for the preceding fiscal year, adjusted by the percentage change in the Personal Consumption Expenditures Price Index of the Bureau of Economic Analysis of the Department of Commerce for such preceding fiscal year.\n**(B) Subsequent years**\nFor each fiscal year of the pilot project (referred to in this subparagraph as a target fiscal year ) after the first fiscal year described in subparagraph (A), the Secretary shall make an Upward Mobility Grant to the State, in an updated sum equal to the sum calculated for the State under this paragraph for the preceding fiscal year, adjusted\u2014\n**(i)**\nby the percentage change in that Personal Consumption Expenditures Price Index between the first day of the preceding fiscal year and the first day of the target fiscal year; and\n**(ii)**\nin a manner consistent with the per-capita direct assistance adjustment prohibition described in subsection (k).\n**(C) Adjustment for appropriations lapse**\n**(i) First year**\nFor the purposes of determining, under subparagraph (A), a total of covered amounts for a preceding fiscal year in which there was a lapse in appropriations, the total of the covered amounts shall be determined as if the corresponding funding was appropriated for the entire fiscal year.\n**(ii) Subsequent years**\nFor the purposes of determining, under subparagraph (B), a sum calculated for a State for a preceding fiscal year in which there was a lapse in appropriations, the sum shall be determined as if the corresponding funding was appropriated for the entire fiscal year.\n**(D) Limited scope pilot projects**\nNotwithstanding subparagraphs (A) and (B), if a State has obtained approval to carry out a limited scope pilot project under this section, the Upward Mobility Grant for the State shall be a percentage, between 10 and 100 percent, as indicated by the State in the application submitted under subsection (f) of the amount the State would otherwise receive under subparagraph (A) or (B).\n**(3) Payments**\nFor each fiscal year quarter during the pilot project, the Secretary shall make a payment to the State under the Upward Mobility Grant, equal to 25 percent of the amount of the grant.\n##### (e) Impact of participation\n**(1) Waiver**\nNotwithstanding any other provision of Federal law applicable to an antipoverty program, except as otherwise provided in this section, if a State elects to carry out a pilot project and obtains approval of an application under subsection (g), the Secretary shall, subject to paragraph (2) and consistent with the goals of the antipoverty programs included in the pilot project, grant the State, for purposes of the pilot project, such waivers to statutory or regulatory requirements, as the State requests in its application\u2014\n**(A)**\nrelating to consolidating, replacing, or altering eligibility requirements;\n**(B)**\nrelating to the design, operation, or delivery of an antipoverty program; and\n**(C)**\nrelating to the use, allocation, or distribution of funding.\n**(2) Provisions excluded from waiver authority**\nA waiver shall not be granted under paragraph (1) with respect to any provision of law relating to\u2014\n**(A)**\nthe goals of any antipoverty program;\n**(B)**\ncivil rights or the prohibition of discrimination;\n**(C)**\nhealth or safety;\n**(D)**\nlabor standards under the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. );\n**(E)**\nenvironmental protection;\n**(F)**\nany restriction on providing benefits to individuals who are not citizens of or are unlawfully present in the United States;\n**(G)**\nthe protection of religious freedom for providers and beneficiaries of assistance;\n**(H)**\nany funding restriction or limitation provided in an appropriations Act;\n**(I)**\na maintenance of effort requirement; or\n**(J)**\nany requirement that a State distribute to a sub-State entity part or all of an amount paid to the State.\n**(3) Housing programs**\nFunds made available under a pilot project for the goals of an antipoverty program related to a covered amount described in clause (i)(VII), (ii), or (iii) of subsection (a)(3)(A) shall continue to be provided to the same eligible local entities or recipients as under applicable law in effect as of the date of enactment of this Act.\n**(4) Impact on funding**\n**(A) In general**\nDuring the period of the pilot project\u2014\n**(i)**\nthe State shall not be eligible to receive Federal funding for the antipoverty programs, outside the pilot project; and\n**(ii)**\nindividuals receiving per-capita direct assistance through the pilot project shall not be eligible for additional benefits under the antipoverty programs, outside the pilot project.\n**(B) Exceptions**\nNotwithstanding subparagraph (A), in the case of a State carrying out a limited scope pilot project described in subsection (c)(2), the State may continue to receive Federal funding for the antipoverty programs, outside the pilot project.\n**(C) SNAP contingency fund**\n**(i) In general**\nNotwithstanding subparagraph (A), on the request of a State carrying out a pilot project, the Secretary of Agriculture may use contingency reserve funding made available under the provisions described in clause (ii) to provide benefits to individuals receiving per-capita direct assistance through the pilot project under the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) during a period of economic downturn, a natural disaster, a public health emergency, or another unanticipated event that increases the demand for those benefits, as determined by the Secretary of Agriculture.\n**(ii) Provisions described**\nThe provisions referred to in clause (i) are the following:\n**(I)**\nThe matter under the heading Supplemental nutrition assistance program under the heading Food and Nutrition Service under the heading Domestic Food Programs in title IV of division B of the Continuing Appropriations, Agriculture, Legislative Branch, Military Construction and Veterans Affairs, and Extensions Act, 2026 ( Public Law 119\u201337 ).\n**(II)**\nThe matter under the heading Supplemental nutrition assistance program under the heading Food and Nutrition Service under the heading Domestic Food Programs in title IV of division B of the Consolidated Appropriations Act, 2024 ( Public Law 118\u201342 ; 138 Stat. 93).\n**(III)**\nSection 1109 of the Full-Year Continuing Appropriations and Extensions Act, 2025 ( Public Law 119\u20134 ; 139 Stat. 13).\n**(D) Temporary Assistance for Needy Families (TANF) Contingency Fund**\nNotwithstanding subparagraph (A), on the request of a State carrying out a pilot project, the Secretary may use funds available under section 403(b) of the Social Security Act ( 42 U.S.C. 603(b) ) to provide benefits to individuals receiving per-capita direct assistance under the temporary assistance for needy families program established under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ) through the pilot project during a period of economic downturn, a natural disaster, a public health emergency, or another unanticipated event that increases the demand for those benefits, as determined by the Secretary. Nothing in the preceding sentence shall be construed as requiring the State carrying out the pilot project to submit a request under section 403(b) of the Social Security Act ( 42 U.S.C. 603(b) ) during an eligible month (as defined in paragraph (4) of such section) for payment of funds under such section or for the Secretary to determine that the State is an eligible State for purposes of such section.\n**(E) Low-Income Home Energy Assistance Program (LIHEAP) Emergency Fund**\nNotwithstanding subparagraph (A), on the request of a State carrying out a pilot project, the Secretary may use funds available under section 2602(e) of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8621(e) ) (in addition to meeting the objectives described in that section) to provide benefits to households that include individuals receiving per-capita direct assistance through the pilot project under the Low-Income Home Energy Assistance Program established under that Act during a period of economic downturn, a natural disaster, a public health emergency, or another unanticipated event that increases the demand for those benefits, as determined by the Secretary.\n**(F) Emergency funding**\n**(i) In general**\nNotwithstanding subparagraph (A), nothing shall prohibit a State carrying out a pilot project from receiving an appropriation described in clause (ii), and using that appropriation to provide benefits to individuals receiving per-capita direct assistance through the pilot project.\n**(ii) Appropriation**\nAn appropriation described in this clause is an appropriation\u2014\n**(I)**\nfor an antipoverty program related to a covered amount described in subsection (a)(3)(A); and\n**(II)**\nmade in an Act other than an regular appropriations Act.\n**(5) Clarification**\nA waiver granted to a State under paragraph (1) includes a waiver for agencies, persons, and families in the State described in clauses (ii) and (iii) of subsection (a)(3)(A).\n##### (f) Applications\nTo be eligible to receive an Upward Mobility Grant to carry out a pilot project under this section, a State shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including\u2014\n**(1)**\ninformation stating\u2014\n**(A)**\nhow the State will utilize the Upward Mobility Grant to achieve the antipoverty objectives described in subsection (b)(2)(B);\n**(B)**\nhow the State will achieve the goals of the antipoverty programs included in the pilot project involved, including (as applicable to the programs included) skills acquisition, housing (including rental housing) affordability, access to nutrition, reduced home energy costs, affordable child care, and temporary assistance to low-income families; and\n**(C)**\nhow the State will ensure that funds made available under the pilot project for the goals of an antipoverty program related to a covered amount described in clause (i)(VII), (ii), or (iii) of subsection (a)(3)(A) shall continue to be provided to the same eligible local entities or recipients as under applicable law in effect as of the date of enactment of this Act, and information demonstrating demonstrable, substantive, and robust engagement with those local entities and recipients on the waiver provisions described in subsection (e)(1).\n**(2)**\n**(A)**\ninformation stating which statutory and regulatory requirements applicable to an antipoverty program the State requests to be waived, as described in subparagraphs (A), (B), and (C) of subsection (e)(1);\n**(B)**\na description of how the State will utilize the Upward Mobility Grant funds to design and use a benefit structure for benefits and services provided through the pilot project that promotes upward mobility through improvements on the upward mobility measures outlined in subsection (j)(2); and\n**(C)**\nbenchmark goals for improvements on those measures;\n**(3)**\ninformation describing\u2014\n**(A)**\nthe eligibility criteria established by the State for pilot project participants;\n**(B)**\nhow the State, in carrying out the pilot project, will\u2014\n**(i)**\nprotect beneficiary data and privacy;\n**(ii)**\nprevent fraudulent use of funds; and\n**(iii)**\nmaintain clear, auditable records for all funds and services; and\n**(C)**\nthe program integrity measures established by the State to ensure that the State provides direct assistance benefits to eligible pilot project participants in compliance with the criteria established under subparagraph (A) and requirements established under clauses (i), (ii), and (iii) of subparagraph (B);\n**(4)**\n**(A)**\ninformation describing how the State will apply the work requirement for direct assistance benefit recipients specified in subsection (h); and\n**(B)**\ninformation describing the program integrity measures established by the State to ensure compliance with that work requirement;\n**(5)**\ninformation demonstrating how the State will engage nonprofit organizations, faith-based organizations, private service providers, local governments, and other local entities to deliver holistic, customized case management and a portion of the services for the pilot project;\n**(6)**\ninformation describing how the State will evaluate the project by contracting under subsection (j) with an independent, third-party evaluator, and will ensure the most rigorous results from the evaluation and the strongest possible measurement through the evaluation of the causal link between the State\u2019s proposed benefit structure and the upward mobility measures listed in subsection (j)(2), including\u2014\n**(A)**\nthe methodology that will be used to evaluate the pilot project;\n**(B)**\nthe data the State will collect and provide to the evaluator;\n**(C)**\nthe process by which the State will collect the data to provide to the evaluator; and\n**(D)**\ninformation on the evaluator's qualifications, including\u2014\n**(i)**\nconfirmation that the evaluator is independent from the State and from any nonprofit organizations, faith-based organizations, private service providers, local governments, and other local entities participating in the pilot project; and\n**(ii)**\ninformation stating whether the evaluator has demonstrated substantial experience in conducting rigorous evaluations, utilizing the methodology described under subparagraph (A);\n**(7)**\ninformation\u2014\n**(A)**\ndescribing how the State will utilize fiscal savings resulting from improvements on upward mobility measures under subsection (j)(2) to improve program operations and infrastructure of programs covered by the pilot project, including\u2014\n**(i)**\nestablishing a State reserve fund to provide temporary per-capita direct assistance benefits to eligible individuals and households during a period of economic downturn, a natural disaster, a public health emergency, or another unanticipated event that increases the demand for those benefits, as determined by the corresponding Secretary;\n**(ii)**\nusing the savings to improve program management, eligibility verification, benefits distribution, compliance monitoring, and enforcement of the work requirement required under subsection (h);\n**(iii)**\nusing the savings for renovation, expansion, or maintenance of community facilities to promote antipoverty objectives described in subsection (b)(2)(B);\n**(iv)**\nusing the savings for resources for capacity-building to increase collaboration with and involvement of nonprofit organizations, faith-based organizations, private service providers, local governments, and other local entities to deliver services funded under the pilot project;\n**(v)**\nusing the savings to integrate program operations, improve case management, streamline client intake, or reduce administrative duplication; and\n**(vi)**\nproviding work supports for individuals who are employed and working hours consistent with section 261.32 of title 45, Code of Federal Regulations (or a successor regulation), who are not receiving assistance through the Upward Mobility Grant; and\n**(B)**\ndemonstrating how the supports described in subparagraph (A)(vi) will be designed to\u2014\n**(i)**\nincrease the level of hours worked for those receiving such a support; and\n**(ii)**\nincrease the level of earnings for those receiving such a support;\n**(8)**\nat the election of the State, a proposal\u2014\n**(A)**\nthat describes how the State will reduce regulatory barriers for the purpose of increasing market access to, or lowering the costs of, nutrition, child care, home energy (including utilities), employment and training services for dislocated workers, or housing (including rental housing) (referred to in this paragraph as covered basics ); and\n**(B)**\nthat includes\u2014\n**(i)**\nidentification of existing (as of the date of submission) State regulatory barriers that limit market entry to, or production or supply of, any of the covered basics; and\n**(ii)**\nactions the State will take to reduce, streamline, or eliminate regulations establishing such barriers; and\n**(9)**\nin the case of a State seeking to carry out a limited scope pilot project\u2014\n**(A)**\na detailed description of the more limited scope of the pilot project, including whether the project will involve a limited percentage of the individuals eligible to participate in the pilot project, a limited geographic area, a limited number of antipoverty programs, or some other limitation on the project; and\n**(B)**\ninformation indicating the percentage described in subsection (d)(2)(D) that the State seeks to receive through the pilot program.\n##### (g) Evaluating and approving applications\n**(1) In general**\nIn order for a State to receive an Upward Mobility Grant to carry out a pilot project under this section, the State shall obtain approval from the Secretary of the application for the pilot project submitted under subsection (f).\n**(2) Comment period**\nOn receiving the application, the Secretary shall\u2014\n**(A)**\nnot later than 5 days after the date of that receipt, provide notice on the website of the Department of Health and Human Services of receipt of the application; and\n**(B)**\ngive interested persons, including stakeholders in the State, an opportunity to submit comments on the application for a 30-day period beginning on the date on which the Secretary provides notice under subparagraph (A).\n**(3) Evaluation of applications**\nIn evaluating an application to carry out a project, the Secretary shall\u2014\n**(A)**\nevaluate the application based on the extent to which the project\u2014\n**(i)**\nwill achieve the antipoverty objectives described in subsection (b)(2)(B);\n**(ii)**\nwill achieve the goals described in subsection (f)(1)(B); and\n**(iii)**\nwill meet the requirements described in subsection (f)(1)(C) relating to provision of funds and to engagement;\n**(B)**\nevaluate the application based on the extent to which the project will make improvements on the upward mobility measures described in subsection (j)(2); and\n**(C)**\nconsider the extent to which the methodology of the project evaluation under subsection (j) and data collection under subsection (f) will\u2014\n**(i)**\nproduce rigorous results, using experimental designs that use\u2014\n**(I)**\nrandom assignment; or\n**(II)**\nif random assignment is not feasible, another reliable, evidence-based research methodology that allows for the strongest practicable causal inferences; and\n**(ii)**\nprovide sufficient contextual information on the characteristics of the population served by the project, including demographic and geographic information, to assess the applicability of the project in other settings.\n**(4) Priority**\nIn determining which applications to approve under this subsection, the Secretary shall give priority to\u2014\n**(A)**\napplications for a pilot project with a program design that limits\u2014\n**(i)**\nthe average Marginal Effective Tax Rate of an increase in earned income attributable to employment through the pilot project to not more than 50 percent; and\n**(ii)**\nthe average Marginal Effective Tax Rate of an increase in such earned income to not more than 50 percent, among participants for whom such increase results in lack of eligibility for any per-capita direct assistance;\n**(B)**\napplications the Secretary projects will most make improvements on the upward mobility measures described in subsection (j)(2);\n**(C)**\napplications for a pilot project for which the methodology described in paragraph (3)(C) will use an experimental design that uses\u2014\n**(i)**\nrandom assignment; or\n**(ii)**\nif random assignment is not feasible\u2014\n**(I)**\na natural experiment design;\n**(II)**\na synthetic control method;\n**(III)**\na differences-in-differences technique;\n**(IV)**\na regression discontinuity method;\n**(V)**\nan instrumental variable method;\n**(VI)**\na panel data with mixed effects method;\n**(VII)**\na propensity score matching method; or\n**(VIII)**\na cross-sectional regression method;\n**(D)**\napplications that describe program integrity measures that will maximize compliance with\u2014\n**(i)**\nthe work requirement described in subsection (h); and\n**(ii)**\nthe requirements established under clauses (i), (ii), (iii) of subsection (f)(3)(B).\n**(5) Approval or disapproval**\n**(A) Grounds for disapproval**\nIn reviewing an application, the Secretary determines that the project will not achieve the antipoverty objectives described in subsection (b)(2)(B), achieve the goals described in subsection (f)(1)(B), or meet the requirements described in subsection (f)(1)(C) relating to the provision of funds and to engagement, the Secretary shall disapprove the application. Nothing in this subparagraph shall be construed to prevent the Secretary from disapproving an application for another reason specified in this section.\n**(B) Timeline**\nThe Secretary shall decide whether or not to approve the application not later than 90 days after the date of receipt of the application.\n**(6) Process after disapproval**\nIf the Secretary decides to disapprove the application of a State\u2014\n**(A)**\nthe Secretary shall provide the State with a detailed explanation of the decision;\n**(B)**\nthe State may submit a modified application to the Secretary for approval; and\n**(C)**\nif a modified application is submitted, the Secretary shall make a decision on approval of the application, after evaluating and giving priority as described in paragraphs (3) and (4), not later than 30 days after the date of receipt of the modified application.\n##### (h) Work requirement and program integrity\n**(1) SNAP requirements**\nThe requirements under subsections (d) and (o) of section 6 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015 ) shall apply to recipients of direct assistance benefits under a pilot project carried out under this section, subject to such changes to those requirements as the Secretary determines necessary.\n**(2) Regulations; audit**\nThe Secretary shall\u2014\n**(A)**\nprescribe such regulations as the Secretary determines necessary and appropriate to ensure compliance with and State enforcement of the requirements described in paragraph (1); and\n**(B)**\naudit the program integrity measures described in paragraphs (3)(C) and (4)(B) of subsection (f) established by States.\n##### (i) Data sharing\nThe Secretary shall facilitate data sharing, concerning data and other information relating to antipoverty programs, with Federal agencies and offices (other than the Administration for Children and Families of the Department of Health and Human Services) as necessary to administer the pilot program carried out under this Act. The Secretary shall cooperate with each State participating in the pilot program to coordinate access by Federal agencies and offices to data and other information relating to antipoverty programs included in the State\u2019s pilot project.\n##### (j) Evaluations\n**(1) In general**\n**(A) Determinations**\nEach State that carries out a pilot project under this Act shall enter into a contract for an annual independent, third-party evaluation of the pilot project, for purposes of determining, for purposes of this section\u2014\n**(i)**\nper-capita direct assistance, and per-capita direct assistance described in paragraph (2)(C); and\n**(ii)**\nimprovement on the upward mobility measures described in paragraph (2), as described in paragraph (3).\n**(B) Qualifications**\nThe evaluator shall demonstrate the independence described in clause (i), and the substantial experience described in clause (ii), of subsection (f)(6)(D).\n**(2) Upward mobility measures**\nThe State shall require the evaluator to conduct annual evaluations of the pilot project on upward mobility measures, which measure\u2014\n**(A)**\nthe Marginal Effective Tax Rates, for pilot project participants, of increases in earned income attributable to employment through the pilot project;\n**(B)**\nparticipant employment outcomes, consisting of achievement of (relative to the full fiscal year that precedes the date on which the Secretary approves the application for the pilot project under subsection (g) (referred to in this paragraph as the pre-implementation year ))\u2014\n**(i)**\nhigher earnings of participants;\n**(ii)**\na higher percentage of participants with employment;\n**(iii)**\na higher percentage of participants with full-time employment; and\n**(iv)**\na higher percentage of participants who have retained employment;\n**(C)**\nreduction (relative to the pre-implementation year) in per-capita direct assistance by reducing the dependence of participants on per-capita direct assistance through improvement in employment outcomes described in subparagraph (B);\n**(D)**\nelimination or reduction in (relative to the pre-implementation year) marriage penalties for participants; and\n**(E)**\nreduction (relative to the pre-implementation year) in poverty among participants.\n**(3) Improvement**\nThe State shall require the evaluator, as part of each annual evaluation, to measure\u2014\n**(A)**\nimprovement (relative to the pre-implementation year) on the upward mobility measures described in paragraph (2); and\n**(B)**\nimprovement on the upward mobility measures, relative to the benchmark goals described under subsection (f)(2)(C).\n**(4) Use of evaluations**\nThe evaluator shall prepare and submit to the Secretary a report containing the results of each annual evaluation.\n**(5) Comparison**\nThe evaluator shall make comparisons on the upward mobility measures by comparing the outcomes of the entire population enrolled in the antipoverty programs related to a covered amount described in subsection (a)(3)(A)(i) for the preceding fiscal year described in subsection (d)(2)(A), to the outcomes for that entire population enrolled in those antipoverty programs (included in the pilot project or not so included) for the year covered by the evaluation.\n##### (k) Funding adjustment\nNo State shall receive an adjustment to an Upward Mobility Grant because the State increased the amount of the per-capita direct assistance provided, through an Upward Mobility Grant.\n#### 3. Transfers and savings provision\n##### (a) Definitions\nFor purposes of this section, unless otherwise provided or indicated by the context\u2014\n**(1)**\nthe term Administration means the Administration for Children and Families;\n**(2)**\nthe term covered Federal agency means an agency, as defined in section 551(1) of title 5, United States Code, that carries out an antipoverty program;\n**(3)**\nthe term function means any duty, obligation, power, authority, responsibility, right, privilege, activity, or program;\n**(4)**\nthe term Secretary means the Secretary of Health and Human Services, acting through the Assistant Secretary for Children and Families; and\n**(5)**\nthe term transferred function means a function (including a part of a function) transferred under this section.\n##### (b) Administrative funding\n**(1) Amounts to States for administrative costs**\n**(A) In general**\nNotwithstanding any other provision of this section, for each State carrying out a pilot project under this Act, each head of a covered Federal agency shall transfer to the State, for a fiscal year, an amount that bears the same relationship to the total amount of funding for administrative costs of the antipoverty program involved for that fiscal year for all States as the amount of funding the State received for the nonadministrative costs of the program for the prior fiscal year bears to the total amount of funding that all States received for those costs for the prior fiscal year.\n**(B) Determination**\nFor the purposes of determining, under subparagraph (A), the funding a State received for nonadministrative costs for a prior fiscal year in which there was a lapse in appropriations, the funding shall be determined as if the corresponding money was appropriated for the entire fiscal year.\n**(2) Limited scope pilot projects**\nFor a State carrying out a limited scope pilot project under section 2(c)(2), the head of the Federal agency shall adjust the amount to be transferred under paragraph (1) to account for the limited scope.\n##### (c) Transfer of functions\n**(1) In general**\nThere are transferred to the Administration a portion, determined by the Office of Management and Budget, of the functions that the heads of covered Federal agencies exercised before the date of the enactment of this Act (including related functions of any officer or employee of a covered Federal agency). The portion shall consist of those functions (or parts of functions) that the Office determines are appropriate for the Administration to exercise in carrying out this Act.\n**(2) Delegation and assignment**\nExcept where otherwise expressly prohibited by law or otherwise provided by this Act, the Secretary may delegate any of the transferred functions to such officers and employees of the Administration as the Secretary may designate, and may authorize successive redelegations of such functions as may be necessary or appropriate. No delegation of transferred functions by the Secretary under this section shall relieve such Secretary of responsibility for the administration of such functions.\n**(3) Reorganization**\nThe Secretary is authorized to allocate or reallocate any transferred function among the officers of the Administration, and to establish, consolidate, alter, or discontinue such organizational entities in the Administration as may be necessary or appropriate.\n**(4) Transfer and allocations of appropriations and personnel**\nExcept as otherwise provided in this Act, the personnel employed in connection with, and the assets, liabilities, contracts, property, records, and unexpended balances of appropriations, authorizations, allocations, and other funds employed, used, held, arising from, available to, or to be made available in connection with the transferred functions, subject to section 1531 of title 31, United States Code, shall be transferred to the Administration. Unexpended funds transferred pursuant to this section shall be used only for the purposes for which the funds were originally authorized and appropriated. The Director of the Office of Management and Budget shall provide for such further measures and dispositions as may be necessary to effectuate the purposes of this Act.\n**(5) Rules**\nThe Secretary is authorized to prescribe, in accordance with the provisions of chapters 5 and 6 of title 5, United States Code, such rules and regulations as the Secretary determines necessary or appropriate to administer and manage the functions of the Administration to carry out section 2.\n**(6) Transition**\nThe Secretary is authorized to utilize\u2014\n**(A)**\nthe services of officers, employees, and other personnel of a covered Federal agency with respect to transferred functions; and\n**(B)**\nfunds appropriated to such functions for such period of time as may reasonably be needed to facilitate the orderly implementation of this Act.\n##### (d) Savings provisions\n**(1) Continuing effect of legal documents**\nAll orders, determinations, rules, regulations, permits, agreements, grants, contracts, certificates, licenses, registrations, privileges, and other administrative actions\u2014\n**(A)**\nwhich have been issued, made, granted, or allowed to become effective by the President, any covered Federal agency or official thereof, or by a court of competent jurisdiction, in the performance of transferred functions; and\n**(B)**\nwhich are in effect on the date of enactment of this Act, or were final before that date and are to become effective on or after that date,\nshall continue in effect according to their terms until modified, terminated, superseded, set aside, or revoked in accordance with law by the President, the Secretary or other authorized official, a court of competent jurisdiction, or by operation of law.\n**(2) Proceedings not affected**\nThe provisions of this Act shall not affect any proceedings, including notices of proposed rulemaking, or any application for any license, permit, certificate, or financial assistance pending before any covered Federal agency on the date of enactment of this Act, with respect to transferred functions but such proceedings and applications shall be continued. Orders shall be issued in such proceedings, appeals shall be taken therefrom, and payments shall be made pursuant to such orders, as if this Act had not been enacted, and orders issued in any such proceedings shall continue in effect until modified, terminated, superseded, or revoked by a duly authorized official, by a court of competent jurisdiction, or by operation of law. Nothing in this paragraph shall be deemed to prohibit the discontinuance or modification of any such proceeding under the same terms and conditions and to the same extent that such proceeding could have been discontinued or modified if this Act had not been enacted.\n**(3) Suits not affected**\nThe provisions of this Act shall not affect suits commenced before the date of enactment of this Act, and in all such suits, proceedings shall be had, appeals taken, and judgments rendered in the same manner and with the same effect as if this Act had not been enacted.\n**(4) Nonabatement of actions**\nNo suit, action, or other proceeding commenced by or against a covered Federal agency, or by or against any individual in the official capacity of such individual as an officer of a covered Federal agency, shall abate by reason of the enactment of this Act.\n**(5) Administrative actions relating to promulgation of regulations**\nAny administrative action relating to the preparation or promulgation of a regulation by a covered Federal agency relating to a transferred function may be continued by the Administration with the same effect as if this Act had not been enacted.\n**(6) References**\nReference in any other Federal law, Executive order, rule, regulation, or delegation of authority, or any document of or relating to\u2014\n**(A)**\nthe head of a covered Federal agency with regard to a transferred function, shall be deemed to refer to the Secretary; and\n**(B)**\na covered Federal agency with regard to a transferred function, shall be deemed to refer to the Administration.",
      "versionDate": "2026-01-06",
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
        "actionDate": "2026-01-06",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Financial Services, Agriculture, Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6949",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Upward Mobility Act of 2026",
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
        "name": "Social Welfare",
        "updateDate": "2026-04-21T19:18:12Z"
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
      "date": "2026-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3583is.xml"
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
      "title": "Upward Mobility Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-30T04:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Upward Mobility Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-30T04:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a pilot program in which States may use consolidated funds, through Upward Mobility Grants, for antipoverty programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-30T04:03:29Z"
    }
  ]
}
```
