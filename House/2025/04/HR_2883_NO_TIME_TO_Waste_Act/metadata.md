# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2883?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2883
- Title: NO TIME TO Waste Act
- Congress: 119
- Bill type: HR
- Bill number: 2883
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-03-26T08:06:33Z
- Update date including text: 2026-03-26T08:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2883",
    "number": "2883",
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
    "title": "NO TIME TO Waste Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:33Z",
    "updateDateIncludingText": "2026-03-26T08:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-10T13:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "sponsorshipDate": "2025-04-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2883ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2883\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Ms. Pingree (for herself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the Secretary of Agriculture to carry out activities to reduce food loss and waste, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the New Opportunities for Technological Innovation, Mitigation, and Education To Overcome Waste Act, or the NO TIME TO Waste Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Commissioner**\nThe term Commissioner means the Commissioner of Food and Drugs.\n**(3) Food**\nThe term food means any raw, cooked, processed, or prepared substance, ice, beverage, or ingredient used or intended for use in whole or in part for human consumption.\n**(4) Food loss**\nThe term food loss means, with respect to food, that the food does not reach a consumer as a result of an issue in the production, storage, processing, or distribution phase.\n**(5) Food recovery**\nThe term food recovery means the collection of wholesome food that would otherwise go to waste and the redistribution of that food to feed people.\n**(6) Food spoilage**\nThe term food spoilage means a process or change that renders a food product undesirable or unacceptable for human consumption.\n**(7) Food waste**\nThe term food waste means, with respect to food, that the food is intended for human consumption but is unconsumed by humans for any reason at the retail or consumption phase.\n**(8) Liaison**\nThe term Liaison means the Food Loss and Waste Reduction Liaison established under section 224 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6924 ).\n**(9) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(10) Upcycled food product**\nThe term upcycled food product means a product that\u2014\n**(A)**\nis created from surplus food, unmarketable food, or edible or inedible food byproducts; and\n**(B)**\nis made with ingredients that\u2014\n**(i)**\notherwise would not have gone to human consumption;\n**(ii)**\nare sourced and produced using supply chains for which upstream data can be verified and validated for accuracy; and\n**(iii)**\nhave a positive impact on the environment.\n#### 3. Office of Food Loss and Waste\n##### (a) Establishment\nThe Secretary shall establish in the Department of Agriculture an Office of Food Loss and Waste (referred to in this section as the Office ).\n##### (b) Responsibilities\nThe Office shall be responsible for\u2014\n**(1)**\nsupporting the role and responsibilities of the Liaison;\n**(2)**\ncomprehensive research on methods to quantify on-farm food loss and supply chain food loss;\n**(3)**\nresearch on new technologies to reduce food loss and food waste;\n**(4)**\nquantifying the impact of food waste reduction policies on greenhouse gas emissions reductions;\n**(5)**\nsubmitting to Congress and making publicly available reports describing the progress of the United States in advancing toward or achieving the goal of reducing food loss and food waste by 50 percent, compared to 2016 levels, by 2030;\n**(6)**\npublishing reports to Congress and to the public for the purpose of engaging with educational campaigns relating to food loss and food waste;\n**(7)**\ncarrying out the grant program under subsection (d);\n**(8)**\ncontributing to an assessment relating to how food loss and food waste affects climate change, food and nutrition security, and public health;\n**(9)**\ncreating and distributing tools, resources, and publications\u2014\n**(A)**\nto support efforts and measures to reduce and prevent food loss and food waste; and\n**(B)**\nto contribute to increased education relating to food loss and food waste for private entities, nonprofit and community-based organizations, and individuals;\n**(10)**\ntracking and assessing programs across Federal agencies to advance research relating to food loss and food waste;\n**(11)**\nanalyzing food loss and food waste policy data and establishing and disseminating model policies for municipal, local, State, territorial, and Tribal governments that are proven to reduce food loss or food waste;\n**(12)**\nrecommending new regulations, investments, or policies to the Liaison and the Secretary to address new identified gaps on preventing and reducing food loss and food waste; and\n**(13)**\ncarrying out such other activities as the Secretary or the Liaison determine to be appropriate.\n##### (c) Partnerships\nIn carrying out the responsibilities described in subsection (b), the Secretary, in consultation with other Federal agencies, the Liaison, and the Office, shall establish partnerships with regional partner institutions to plan, conduct, and arrange for public research, data, education, and recommendations relating to food loss and food waste prevention and reduction and food recovery issues locally, regionally, and nationally.\n##### (d) Grant program\n**(1) In general**\nThe Office shall establish a grant program to support collecting data on existing State and local food loss and food waste policies.\n**(2) Eligibility**\nAn entity eligible to receive a grant under paragraph (1) is\u2014\n**(A)**\na municipal, local, State, or Tribal government;\n**(B)**\na partnership of 1 or more governments described in subparagraph (A) and 1 or more nonprofit organizations; or\n**(C)**\na partnership of 2 or more\u2014\n**(i)**\ngovernments described in subparagraph (A); or\n**(ii)**\nnonprofit organizations.\n**(3) Collaboration**\nAn entity that receives a grant under paragraph (1) may collaborate with 1 or more nonprofit, private, or other organizations in carrying out activities using the grant funds.\n**(4) Project requirements**\nA data collection project carried out using a grant under paragraph (1) shall\u2014\n**(A)**\nbe carried out for not longer than 3 years; and\n**(B)**\ninclude the provision of data collected under the project to the Office.\n**(5) Data requirements**\nData collected under a project carried out using a grant under paragraph (1) shall provide rigorous evidence of the impact of food loss and food waste policies, which may include\u2014\n**(A)**\nestimates of the quantity of the reduction of food loss and food waste after the implementation of a policy;\n**(B)**\nwhere relevant, estimates of the quantity of food loss and food waste in a similar community that is not subject to the policy; and\n**(C)**\nthe economic benefits and impacts realized from food that is recovered, upcycled, reused, or recycled.\n**(6) Matching requirement**\nAn entity that receives a grant under paragraph (1) shall provide funds, in-kind contributions, or a combination of both from sources other than funds provided through the grant in an amount equal to not less than 10 percent of the amount of the grant, which may include private funding or other sources of revenue, as determined by the Secretary.\n**(7) Model policies**\nAfter the Office receives the data collected under the grant program under this paragraph, the Office shall analyze the data and establish model policies for municipal, local, State, and Tribal governments that are proven to reduce food waste.\n##### (e) Authorizations of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Office $1,500,000 for each of fiscal years 2026 through 2030.\n**(2) Grant program**\n**(A) In general**\nThere is authorized to be appropriated to carry out the grant program under subsection (d) $2,000,000 for each of fiscal years 2026 through 2030.\n**(B) Administrative costs**\nOf the amount appropriated under subparagraph (A), the Secretary may retain not more than 4 percent to pay administrative costs incurred by the Secretary in carrying out subsection (d).\n#### 4. Improving coordination to prevent and reduce food loss and waste\n##### (a) Regional coordinators\n**(1) In general**\nThe Secretary shall establish in the Department of Agriculture regional coordinators.\n**(2) Responsibilities**\nThe regional coordinators established under paragraph (1) shall be responsible for\u2014\n**(A)**\npartnering with food producers, food processors, distributors, and food recovery organizations and acting as regional points of contact to facilitate real-time food recovery;\n**(B)**\nunderstanding and developing the capacity needed for ongoing food recovery;\n**(C)**\nproviding technical support to food recovery organizations to improve the ability of the food recovery organizations to pick up surplus food, process that food, and deliver that food to populations or communities; and\n**(D)**\nengaging with Department of Agriculture regional food business centers to identify opportunities for synergy and alignment with those centers.\n**(3) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary to carry out this subsection $1,000,000.\n##### (b) Food recovery and distribution infrastructure support and coordination block grants\n**(1) In general**\nThe Secretary, in coordination with the Office of Food Loss and Waste established under section 3, shall establish as part of the program under section 203D(d) of the Emergency Food Assistance Act of 1983 ( 7 U.S.C. 7507(d) ) a program to award annual block grants to States and Indian Tribes to carry out projects to develop and support food recovery infrastructure and innovative food distribution models.\n**(2) Distribution**\nA State shall distribute a block grant received under paragraph (1) to applicable food recovery organizations and local governments to address any gaps in food recovery infrastructure, including\u2014\n**(A)**\nstorage and capacity of processing infrastructure equipment and facilities;\n**(B)**\ntemperature-controlled food distribution infrastructure;\n**(C)**\ntechnological solutions supporting food recovery, such as real-time updates to connect organizations that have surplus food with organizations that distribute surplus food; and\n**(D)**\nsupport of salaries, wages, and benefits for food recovery organizations.\n**(3) Coordination**\nIn establishing the program under paragraph (1), the Secretary shall coordinate with other Department of Agriculture agencies and programs, including\u2014\n**(A)**\nthe Agricultural Marketing Service;\n**(B)**\nthe Emergency Food Assistance Program Reach and Resiliency Grants; and\n**(C)**\nsuch other agencies and programs as the Secretary determines to be appropriate.\n**(4) Authorization of appropriations**\nThere is authorized to be appropriated to carry out this subsection $2,000,000 for each of fiscal years 2026 through 2030.\n#### 5. Strengthening government approach to food loss and waste\n##### (a) Interagency collaboration on food loss and waste\n**(1) In general**\nThe Secretary, in collaboration with the Administrator and the Commissioner, shall collaborate to carry out the agreement relative to cooperation and coordination on food loss and waste signed by those officials on December 17, 2020.\n**(2) Reports**\nEvery year, the Secretary, acting through the Liaison and the Office of Food Loss and Waste established under section 3, in consultation with the Administrator and the Commissioner, shall submit to Congress and make publicly available a report describing the progress of the Secretary in carrying out the agreement described in paragraph (1).\n**(3) Interagency engagement**\nPursuant to paragraph (1), the Secretary, the Administrator, and the Commissioner shall engage with the heads of other Federal departments and agencies, including the Secretary of Defense, the Secretary of Education, the Secretary of Transportation, the Secretary of Homeland Security, the Administrator of General Services, and such other Federal departments and agencies as the Secretary, the Administrator, and the Commissioner determine to be appropriate, to expand work on food loss and food waste.\n**(4) Consultation**\n**(A) In general**\nThe Secretary shall consult with, and receive advice from, representatives described in subparagraph (B) relating to\u2014\n**(i)**\nprogramming and policy issues relating to understanding existing and future challenges relating to food loss and food waste;\n**(ii)**\nacquiring the latest data relating to food loss and food waste;\n**(iii)**\nthe latest innovative solutions relating to food loss and food waste from leading experts; and\n**(iv)**\nsharing and developing procurement best practices that will assist the heads of Federal departments and agencies described in paragraph (3) in\u2014\n**(I)**\npreventing food loss and waste;\n**(II)**\nreducing food loss and food waste;\n**(III)**\nleading by example in addressing issues relating to food loss and food waste; and\n**(IV)**\nengaging contractors in reducing food loss and food waste in the operations of the contractors.\n**(B) Representatives**\nThe representatives referred to in subparagraph (A) are representatives of\u2014\n**(i)**\nthe private sector;\n**(ii)**\nagricultural producers;\n**(iii)**\nfood industry members, such as food safety trainers, food aggregators and processors, food safety professionals, retailers, and food service entities;\n**(iv)**\nnonprofit organizations;\n**(v)**\nfood recovery organizations of varying sizes; and\n**(vi)**\nany other sector, as determined by the Secretary.\n**(C) Representation of smaller producers and food insecure communities**\nIn consulting and receiving advice under subparagraph (A), the Secretary shall ensure participation by smaller producers and organizations from communities most impacted by food and nutrition insecurity and food loss and food waste issues.\n**(D) Forms of consultation**\nThe Secretary may consult and receive advice under subparagraph (A) through\u2014\n**(i)**\na meeting through which input is sought, such as a workshop, town hall meeting, or listening session;\n**(ii)**\na meeting described in clause (i) with an existing group formed by representatives described in subparagraph (B); and\n**(iii)**\nsuch other means as the Secretary determines to be appropriate.\n**(E) Interagency meetings**\nThe Secretary shall host quarterly meetings with the Administrator, the Commissioner, and the heads of other Federal agencies for the purpose of sharing communications relating to consultation and advice received under subparagraph (A) with those officials regularly.\n**(F) FACA exemption**\nChapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ), shall not apply to any group formed for purposes of consultation or providing advice under this paragraph.\n**(5) Continuation of effect**\nNothing in the subsection shall be affected by the expiration of the agreement described in paragraph (1).\n**(6) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary to carry out this subsection $1,000,000 for each of fiscal years 2026 through 2030.\n##### (b) Federal contractors\nSection 4 of the Federal Food Donation Act of 2008 ( 42 U.S.C. 1792 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking 180 days and all that follows through the Federal and inserting 180 days after the date of enactment of the New Opportunities for Technological Innovation, Mitigation, and Education To Overcome Waste Act, the Federal ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking encourages and inserting requires ; and\n**(ii)**\nby striking and after the semicolon;\n**(C)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(3) requires the contractor to submit to the applicable executive agency a report describing\u2014 (A) efforts and actions to prevent and reduce food loss and food waste (as those terms are defined in section 2 of the New Opportunities for Technological Innovation, Mitigation, and Education To Overcome Waste Act); (B) food waste (as so defined) through activities carried out under the contract; and (C) food donated as described in paragraph (1). ; and\n**(2)**\nby adding at the end the following:\n(c) Reports to Congress Every 2 years, each executive agency shall submit to Congress reports describing the matters reported to the executive agency under subsection (a)(3). .\n##### (c) Strengthening food loss and waste research at the Department of Agriculture\n**(1) Critical agriculture research and extension**\nIn awarding grants under the critical agriculture research and extension crosscutting program area priority established by the Secretary under subsection (b) of the Competitive, Special, and Facilities Research Grant Act ( 7 U.S.C. 3157(b) ), the Secretary shall give priority to grants to address food loss and food waste.\n**(2) Inter-disciplinary engagement in animal systems**\nIn awarding grants under the inter-disciplinary engagement in animal systems crosscutting program area priority established by the Secretary under subsection (b) of the Competitive, Special, and Facilities Research Grant Act ( 7 U.S.C. 3157(b) ), the Secretary shall give priority to grants to address food loss and food waste.\n**(3) Animal nutrition, growth, and lactation**\nIn awarding grants under the animal nutrition, growth, and lactation emphasis area program established by the Secretary under subsection (b) of the Competitive, Special, and Facilities Research Grant Act ( 7 U.S.C. 3157(b) ), the Secretary shall give priority to grants\u2014\n**(A)**\nto reduce losses due to production inefficiencies, including on-farm milk loss; and\n**(B)**\nto use wholesome uneaten food and food processing byproducts from the human food system as feed ingredients.\n#### 6. Composting and food waste reduction program\nSection 222(d)(2) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6923(d)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking local or municipal governments and inserting State, local, municipal, or Tribal governments ;\n**(2)**\nin subparagraph (C), by adding at the end the following:\n(iv) Guidance The Secretary shall publish guidance for applying for pilot projects under this paragraph for applicants that lack resources to obtain technical assistance in preparing an application to assist those applicants in preparing an application, particularly to carry out a pilot project for the reduction of food loss and food waste (as those terms are defined in section 2 of the New Opportunities for Technological Innovation, Mitigation, and Education To Overcome Waste Act) through means other than composting. (v) Period for submission of applications The Secretary shall accept submissions of applications for pilot projects under this paragraph for a duration sufficient to ensure that smaller and rural communities are able to submit applications, as determined by the Secretary. ; and\n**(3)**\nin subparagraph (D), by inserting (which may include private funding or other sources of revenue, as determined by the Secretary) after funds provided through the grant .\n#### 7. Promoting the formation of public-private partnerships on food loss and waste\n##### (a) In general\nThe Secretary, acting through the Office of Food Loss and Waste established under section 3, in collaboration with the Administrator, shall establish a program to award grants to eligible governments described in subsection (b) to incentivize the establishment of public-private partnerships that commit to reducing food loss and food waste in accordance with the goal of the Secretary and the Administrator to reduce food loss and food waste by 50 percent by 2030.\n##### (b) Eligible governments\nA entity eligible to receive a grant under subsection (a) is a State, municipal, local, or Tribal government.\n##### (c) Partnerships\nAn eligible government described in subsection (b) that receives a grant under subsection (a) shall use the grant to establish a partnership with the following entities:\n**(1)**\n1 or more nonprofit organizations.\n**(2)**\n1 or more private entities from any of the following sectors:\n**(A)**\nGrocery and specialty food.\n**(B)**\nHospitality.\n**(C)**\nRestaurants.\n**(D)**\nSupercenters.\n**(E)**\nHospitals.\n**(F)**\nNursing homes.\n**(G)**\nAdult care facilities.\n**(H)**\nAny other sector that the Secretary determines to be appropriate.\n##### (d) Requirements\nA partnership established under subsection (c) shall\u2014\n**(1)**\ncommit to reducing food loss and food waste in accordance with the goal described in subsection (a);\n**(2)**\nprovide\u2014\n**(A)**\na framework for cooperative action relating to food loss and food waste;\n**(B)**\na forum for leadership and the sharing of information on best practices relating to food loss and food waste; and\n**(C)**\na list of the highest priorities on issues relating to food loss and food waste;\n**(3)**\nestablish a methodology for measurement of reductions in food loss and food waste, with the support of a technical team of individuals from 1 or more organizations in the partnership;\n**(4)**\ncollect data and prepare reports for the purposes of\u2014\n**(A)**\nestablishing a baseline of food loss and food waste appropriate for the scope of the collaboration for which the grant was awarded;\n**(B)**\nmonitoring progress in reducing food loss and food waste;\n**(C)**\nidentifying particular areas relating to food loss and food waste that need attention; and\n**(D)**\nhighlighting successes in reducing food loss and food waste that can be replicated;\n**(5)**\nestablish 1 or more working groups to facilitate dialogue and dissemination of insights and best practices relating to food loss and food waste; and\n**(6)**\nmake publicly available an annual report describing the activities of the partnership.\n##### (e) Matching requirement\nAn eligible government described in subsection (b) that receives a grant under subsection (a) shall provide funds, in-kind contributions, or a combination of both from sources other than funds provided through the grant in an amount equal to not less than 50 percent of the amount of the grant, which may include private funding or other sources of revenue, as determined by the Secretary.\n##### (f) Coordination\nA partnership established under subsection (c) shall coordinate with regional coordinators established under section 4(a), as the partnership determines to be appropriate.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $2,000,000 for each of fiscal years 2026 through 2030.\n#### 8. Food loss and waste education and awareness campaign\n##### (a) In general\nThe Secretary, in consultation with the Administrator, shall initiate a national food waste education and public awareness campaign (referred to in this section as the campaign ) through\u2014\n**(1)**\nthe Liaison; and\n**(2)**\nthe Office of Food Loss and Waste established under section 3.\n##### (b) Requirements\nThe campaign shall, at a minimum\u2014\n**(1)**\nillustrate how much food goes to waste in the United States and households across the United States;\n**(2)**\nhighlight methods for preserving and storing foods;\n**(3)**\nprovide consumers tips to identify whether food is still safe and edible, regardless of any BEST If Used By or the USE By date on the label or food packaging indicating quality and freshness;\n**(4)**\nteach consumers the differences between food freshness and food safety;\n**(5)**\nteach consumers how to compost food scraps;\n**(6)**\ndevelop educational materials usable by several different channels, including for specific industry sectors (including retail, food service, and consumer packaged goods), local governments, schools, community and faith-based organizations, and other appropriate channels;\n**(7)**\neducate consumers on food products made with food waste, including upcycled food products, or that use innovative technology to prevent food loss and food waste;\n**(8)**\ninclude interactive elements; and\n**(9)**\ninform about intersectional issues of food loss and food waste, including public health, food insecurity, and climate change.\n##### (c) Priorities\nIn carrying out the campaign, the Secretary shall prioritize\u2014\n**(1)**\ninitial research to determine a means to segment populations to target;\n**(2)**\nidentify, using the means determined under paragraph (1), population segments to target;\n**(3)**\nunderstanding how to best target those identified population segments; and\n**(4)**\ndetermining which strategies are most effective in changing consumer behaviors.\n##### (d) Dual framework campaign\n**(1) In general**\nThe Secretary shall carry out the campaign through\u2014\n**(A)**\ncommunity engagement, which allows information to be delivered through locally trusted sources, with locally tailored solutions and partners (such as for donation or compost options); and\n**(B)**\nnational messaging appropriate for raising awareness of\u2014\n**(i)**\nnationally applicable issues (such as the meaning of best by date labels, tips for meal planning, or businesses that manufacture products using ingredients that would otherwise go to waste, including upcycled food products); and\n**(ii)**\nsuch other issues as the Secretary determines to be appropriate.\n**(2) Pilot projects**\n**(A) In general**\nThe Secretary shall\u2014\n**(i)**\nfor the purpose of testing methods and materials for carrying out the campaign through community engagement under paragraph (1)(A), carry out pilot projects in communities selected by the Secretary; and\n**(ii)**\nassess the results of those pilot projects, including through waste audits or other quantitative measurements.\n**(B) Requirements**\nIn carrying out pilot projects under subparagraph (A), the Secretary shall\u2014\n**(i)**\nensure equity and diversity of representation;\n**(ii)**\nincorporate elements of behavioral science to inform which aspects of the campaign will be effective; and\n**(iii)**\nin coordination with State, local, or municipal governments, inform consumers in a community of solutions, food products, or initiatives that are available to help prevent or reduce food waste.\n##### (e) Waste audits\nThe Secretary shall conduct audits to gather data relating to the impact of the campaign in communities targeted by the campaign for the purpose of informing future efforts under the campaign, including by comparing outcomes in communities targeted by the campaign to outcomes in communities not targeted by the campaign.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $2,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1395",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "NO TIME TO Waste Act);",
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
        "updateDate": "2025-05-22T12:31:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2883",
          "measure-number": "2883",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2883v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>New Opportunities for Technological Innovation, Mitigation, and Education To Overcome Waste Act or the NO TIME TO Waste Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to reduce U.S. food loss and waste (FLW) through federal coordination,\u00a0grants, and education.</p><p>Under the bill, <em>food loss </em>means the food that does not reach a consumer as a result of an issue in the production, storage, processing, or distribution phase. <em>Food waste</em> means that food intended for human consumption is unconsumed for any reason at the retail or consumption phase.</p><p>The bill requires USDA to collaborate with the Food and Drug Administration and the Environmental Protection Agency to carry out\u00a0a December, 17, 2020, agreement to coordinate federal efforts to cut FLW.</p><p>Further,\u00a0USDA must establish an Office of Food Loss and Waste to support the existing role of the Food Loss and Waste Liaison. The office must also, among other things, establish</p><ul><li>a grant program to support collecting data on existing state and local FLW policies (and the office must use the data to establish model policies for state and local governments);</li><li>a block grant program for states and Indian tribes to develop and support food recovery infrastructure and innovative food distribution models; and</li><li>a grant program to incentivize state, municipal, local, and tribal governments to establish public-private partnerships that commit to reducing FLW by 50% by 2030.</li></ul><p>The Office of Food Loss and Waste must also initiate a national FLW education and public awareness campaign.</p>"
        },
        "title": "NO TIME TO Waste Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2883.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>New Opportunities for Technological Innovation, Mitigation, and Education To Overcome Waste Act or the NO TIME TO Waste Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to reduce U.S. food loss and waste (FLW) through federal coordination,\u00a0grants, and education.</p><p>Under the bill, <em>food loss </em>means the food that does not reach a consumer as a result of an issue in the production, storage, processing, or distribution phase. <em>Food waste</em> means that food intended for human consumption is unconsumed for any reason at the retail or consumption phase.</p><p>The bill requires USDA to collaborate with the Food and Drug Administration and the Environmental Protection Agency to carry out\u00a0a December, 17, 2020, agreement to coordinate federal efforts to cut FLW.</p><p>Further,\u00a0USDA must establish an Office of Food Loss and Waste to support the existing role of the Food Loss and Waste Liaison. The office must also, among other things, establish</p><ul><li>a grant program to support collecting data on existing state and local FLW policies (and the office must use the data to establish model policies for state and local governments);</li><li>a block grant program for states and Indian tribes to develop and support food recovery infrastructure and innovative food distribution models; and</li><li>a grant program to incentivize state, municipal, local, and tribal governments to establish public-private partnerships that commit to reducing FLW by 50% by 2030.</li></ul><p>The Office of Food Loss and Waste must also initiate a national FLW education and public awareness campaign.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr2883"
    },
    "title": "NO TIME TO Waste Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>New Opportunities for Technological Innovation, Mitigation, and Education To Overcome Waste Act or the NO TIME TO Waste Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to reduce U.S. food loss and waste (FLW) through federal coordination,\u00a0grants, and education.</p><p>Under the bill, <em>food loss </em>means the food that does not reach a consumer as a result of an issue in the production, storage, processing, or distribution phase. <em>Food waste</em> means that food intended for human consumption is unconsumed for any reason at the retail or consumption phase.</p><p>The bill requires USDA to collaborate with the Food and Drug Administration and the Environmental Protection Agency to carry out\u00a0a December, 17, 2020, agreement to coordinate federal efforts to cut FLW.</p><p>Further,\u00a0USDA must establish an Office of Food Loss and Waste to support the existing role of the Food Loss and Waste Liaison. The office must also, among other things, establish</p><ul><li>a grant program to support collecting data on existing state and local FLW policies (and the office must use the data to establish model policies for state and local governments);</li><li>a block grant program for states and Indian tribes to develop and support food recovery infrastructure and innovative food distribution models; and</li><li>a grant program to incentivize state, municipal, local, and tribal governments to establish public-private partnerships that commit to reducing FLW by 50% by 2030.</li></ul><p>The Office of Food Loss and Waste must also initiate a national FLW education and public awareness campaign.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr2883"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2883ih.xml"
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
      "title": "NO TIME TO Waste Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NO TIME TO Waste Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "New Opportunities for Technological Innovation, Mitigation, and Education To Overcome Waste Act,",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Agriculture to carry out activities to reduce food loss and waste, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:25Z"
    }
  ]
}
```
