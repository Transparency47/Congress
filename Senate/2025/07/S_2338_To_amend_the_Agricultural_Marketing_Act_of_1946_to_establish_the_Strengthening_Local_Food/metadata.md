# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2338?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2338
- Title: Strengthening Local Food Security Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2338
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-03-25T11:03:19Z
- Update date including text: 2026-03-25T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S4458)
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S4458)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2338",
    "number": "2338",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Strengthening Local Food Security Act of 2025",
    "type": "S",
    "updateDate": "2026-03-25T11:03:19Z",
    "updateDateIncludingText": "2026-03-25T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S4458)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
            "date": "2025-07-17T18:06:53Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-17T18:06:53Z",
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
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WV"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "CO"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "RI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2338is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2338\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Reed (for himself and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Marketing Act of 1946 to establish the Strengthening Local Food Security Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Local Food Security Act of 2025 .\n#### 2. Strengthening Local Food Security Program\nSubtitle A of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1621 et seq. ) is amended by adding at the end the following:\n210B. Strengthening Local Food Security Program (a) Definitions In this section: (1) Collaborator The term collaborator , with respect to a project carried out under the Program, means an individual or entity (including a private entity, a for-profit entity, and a nonprofit entity) that\u2014 (A) is unaffiliated with the eligible unit of government carrying out the project; (B) cooperates with respect to\u2014 (i) the application relating to the project under subsection (e); and (ii) the conduct of the project; and (C) is not immediately connected to the management of the project. (2) Covered producer The term covered producer means, as determined by the Secretary\u2014 (A) a small or mid-sized fisher, farmer, or rancher; (B) a beginning fisher, farmer, or rancher; (C) a veteran fisher, farmer, or rancher; and (D) an underserved fisher, farmer, or rancher. (3) Eligible unit of government The term eligible unit of government means\u2014 (A) a State agency, commission, or department that is responsible for agriculture, procurement, food distribution, emergency response, or other similar activities within the State; (B) the District of Columbia; (C) the Commonwealth of Puerto Rico; (D) the United States Virgin Islands; (E) Guam; and (F) a Tribal government. (4) Partnership The term partnership means a relationship involving close cooperation between or among individuals and entities (including private, for-profit, and nonprofit entities) with specified, joint rights and responsibilities in the management of a project carried out under the Program. (5) Program The term Program means the Strengthening Local Food Security Program established under subsection (b). (6) Secretary The term Secretary means the Secretary of Agriculture. (7) Underserved community The term underserved community means a community (including an urban or rural community and a Tribal community) that, as determined by the Secretary\u2014 (A) has limited access to affordable, healthy foods, including fresh fruits and vegetables, in grocery retail stores or farmer-to-consumer direct markets; and (B) has\u2014 (i) a high rate of hunger or food insecurity; or (ii) a high poverty rate. (b) Establishment The Secretary shall establish a program, to be known as the Strengthening Local Food Security Program , under which the Secretary shall enter into cooperative agreements with eligible units of government for the purposes of\u2014 (1) purchasing food, including seafood, produce, meat, eggs, dairy, and poultry, from local and regional covered producers; and (2) distributing that food within the geographic boundaries of the eligible unit of government, including to hunger relief organizations and schools participating in school meal programs under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ) and the Child Nutrition Act of 1966 ( 42 U.S.C. 1771 et seq. ). (c) Purposes The purposes of the Program are\u2014 (1) to maintain and improve food and agricultural supply chain resiliency and expand economic opportunities for covered producers; (2) to promote food security; and (3) to strengthen the food system for food banks, schools, and childcare institutions. (d) Noncompetitive allocation (1) In general The Secretary shall\u2014 (A) enter into cooperative agreements with, and provide funding to, eligible units of government under the Program on a noncompetitive basis; (B) of the amounts appropriated to carry out the Program for each fiscal year\u2014 (i) allocate 10 percent to Tribal governments, to be allocated using a funding formula determined by the Secretary; (ii) of the amounts remaining after making the allocation under clause (i), allocate 1 percent to each State; and (iii) after making the allocations under clauses (i) and (ii), allocate the remaining amounts to each eligible unit of government (excluding Tribal governments) by applying the formula described in section 214 of Public Law 98\u20138 ( 7 U.S.C. 7515 ); and (C) in the case of an eligible unit of government that has not submitted to the Secretary, by the date that is 1 year after the date on which amounts are allocated to the eligible unit of government under subparagraph (B), an application under subsection (e) for spending those amounts, redistribute those amounts to 1 or more other eligible units of government with the capacity to spend those amounts. (2) Eligible units of government in same State For purposes of allocating funding under paragraph (1), 1 or more eligible units of government described in subsection (a)(3)(A) in the same State shall be treated as 1 eligible unit of government. (e) Applications (1) In general To be eligible to receive funding under this section, an eligible unit of government shall submit to the Secretary an application, at such time, in such manner, and containing such information as the Secretary shall require, by regulation, including\u2014 (A) a plan that\u2014 (i) identifies\u2014 (I) the lead agency responsible for carrying out the plan; and (II) community partners that will contribute to the implementation of the plan; (ii) describes the means by which the funds will be used\u2014 (I) to grow a local food system; and (II) (aa) to promote food security; (bb) to increase the prevalence of local, nutritious food in schools; or (cc) to carry out both items (aa) and (bb); and (iii) meets the requirements of subsection (f); and (B) an assurance that\u2014 (i) the eligible unit of government will comply with the requirements of the plan; and (ii) the funds will supplement, not supplant, funds provided by the eligible unit of government in support of local food, school meals, or hunger relief systems. (2) Review The Secretary\u2014 (A) shall review each application submitted under paragraph (1) to ensure that the plan included in the application will carry out the purposes of the Program described in subsection (c); and (B) may accept or reject each application, as the Secretary determines to be appropriate. (f) Requirements (1) In general Under a cooperative agreement entered into under the Program, an eligible unit of government shall\u2014 (A) only purchase food\u2014 (i) from fishermen, farmers, producers, and processors that are\u2014 (I) within the geographic boundaries of the eligible unit of government in which the food will be delivered; or (II) not more than 400 miles from the delivery destination of the food; or (ii) through a subawardee described in subsection (g)(1) that purchases food to fulfill the subaward only from fishermen, farmers, producers, and processors that are\u2014 (I) within the geographic boundaries of the eligible unit of government in which the food will be delivered; or (II) not more than 400 miles from the delivery destination of the food; (B) ensure that not less than 51 percent of the total annual value of products purchased by the eligible unit of government and any subawardees comprises purchases from covered producers; (C) give priority to distributing food to underserved communities; (D) expend funding not later than 3 years after the date on which the funding is provided to the eligible unit of government; and (E) subject to paragraph (2), use not more than 25 percent of the amount allocated to the eligible unit of government for Program administration and technical assistance, which may include support for\u2014 (i) participating producers; (ii) efforts to grow the local agricultural value chain; and (iii) covered producers in obtaining food safety training and certifications. (2) Administration and technical assistance Of the amount used for Program administration and technical assistance under paragraph (1)(E), an eligible unit of government shall allocate not less than 35 percent for technical assistance. (g) Subcontracts and subawards To effectuate the purposes of the Program described in subsection (c), an eligible unit of government\u2014 (1) may enter into subcontracts (including with other units of that government) and provide subawards to support partnerships and collaborators, subject to subsection (f)(1)(E); and (2) on entering into a subcontract or subaward pursuant to paragraph (1), shall\u2014 (A) structure the subcontract or subaward to be inclusive of all costs associated with implementing the Program purposes, including the costs of\u2014 (i) food products; (ii) aggregation and distribution; (iii) equipment or infrastructure upgrades to support food safety compliance; and (iv) personnel; and (B) require members of a partnership and collaborators to demonstrate evidence of existing community or industry engagement. (h) Availability of funds To effectuate the purposes of the Program described in subsection (c) and ensure that the producers described in subsection (f)(1)(B) can meaningfully participate in the Program, the Secretary shall provide\u2014 (1) not less than 50 percent of the funding awarded to an eligible unit of government in advance of the distribution of food under the agreement entered into under the Program; and (2) the remaining funding awarded to the eligible unit of government not later than the midpoint of the period of performance established in that agreement. (i) Food safety training and certification (1) In general The Secretary may require food purchased under a cooperative agreement entered into under the Program to be purchased from a farm that has undergone food safety training, or received a relevant food safety certification, with respect to production, packaging, handling, and storage to minimize risks of food safety hazards. (2) Training, plans, and certifications If the Secretary imposes the requirement described in paragraph (1)\u2014 (A) (i) compliance with the requirement may be demonstrated by\u2014 (I) a receipt of food safety training, including Good Agricultural Practices training, or an equivalent food safety curriculum; or (II) a relevant food safety certification; but (ii) the Secretary shall not require such compliance to be demonstrated by a Federal certification; and (B) each eligible unit of government shall provide technical assistance in obtaining the required food safety training or certification, in accordance with subsection (f)(1)(E). (j) Reports An eligible unit of government that enters into a cooperative agreement under the Program shall submit to the Secretary, at such times as the Secretary determines to be appropriate, reports that shall include data relating to the procurement and distribution of food under the cooperative agreement. (k) Funding (1) Mandatory funding Of the funds of the Commodity Credit Corporation, the Secretary shall use to carry out this section $200,000,000 for fiscal year 2025 and each fiscal year thereafter. (2) Authorization of appropriations In addition to other funds and authorities available to the Secretary, in order to carry out activities under this section, there is authorized to be appropriated $200,000,000 for each of fiscal years 2025 through 2029, to remain available until expended by the Secretary. .",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-08-07T16:44:22Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2338is.xml"
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
      "title": "Strengthening Local Food Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Local Food Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Marketing Act of 1946 to establish the Strengthening Local Food Security Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:24Z"
    }
  ]
}
```
