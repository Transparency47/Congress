# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8520?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8520
- Title: HELP Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8520
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-20T13:25:45Z
- Update date including text: 2026-05-20T13:25:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8520",
    "number": "8520",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001220",
        "district": "3",
        "firstName": "Morgan",
        "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
        "lastName": "McGarvey",
        "party": "D",
        "state": "KY"
      }
    ],
    "title": "HELP Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T13:25:45Z",
    "updateDateIncludingText": "2026-05-20T13:25:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "PA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "OH"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8520ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8520\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Mr. McGarvey (for himself, Mr. Fitzpatrick , Mr. Correa , Mr. Garcia of California , Mr. Tonko , Mrs. Sykes , Mr. Frost , and Mr. Morelle ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo facilitate nationwide accessibility and coordination of 211 services in order to provide information and referral to all individuals in the United States for health and human services needs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Human-Services Emergency Logistics Program Act of 2026 or the HELP Act of 2026 .\n#### 2. Strengthening nationwide accessibility and coordination of 211 services for information and referral for health and human services\n##### (a) In general\nThe Secretary of Health and Human Services (in this Act referred to as the Secretary ) shall establish a program for the following purposes:\n**(1)**\nTo increase the capacity of 211 services in the States, to ensure 211 services are directly accessible to all individuals in each State.\n**(2)**\nTo increase coordination between 211, 988, and 911 service providers.\n**(3)**\nTo increase awareness and use of 211 services by the public.\n##### (b) Administration\nIn carrying out the program under subsection (a), the Secretary shall select one administering agency to assist the Secretary in implementing such program.\n##### (c) Allotments\n**(1) In general**\nFor the purpose specified in subsection (a)(1), the Secretary shall, using funds made available under section 6 and in consultation with the administering agency, determine the amount to be made available for grants to qualified 211 service entities in each State.\n**(2) Formula**\nThe Secretary shall develop a formula for determining the total amount to be allotted for each State for the grants referred to in paragraph (1). Such formula shall be based on population, population density, poverty rate, and other evidence-based predictive data related to the needs in the State for, and access to, health and human services.\n#### 3. Administering agency\n##### (a) Eligibility\nAn entity is eligible to be selected as the administering agency under this section if such entity is an organization that\u2014\n**(1)**\nis described in section 501(c) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code;\n**(2)**\nhas experience working with, and providing technical assistance to, 211 service providers;\n**(3)**\nhas established relationships with local, community-based organizations in each State; and\n**(4)**\nhas experience in disaster response and Federal grants management (and the infrastructure required to manage such grants).\n##### (b) Duties of administering agency\nThe duties of the administering agency shall be\u2014\n**(1)**\nwith respect to the purpose specified in section 2(a)(1)\u2014\n**(A)**\nto advise the Secretary on, and make recommendations to, the Secretary with respect to State allotments from amounts made available under section 6, including the amount of each State allotment;\n**(B)**\nto determine the amount of funding, on a State-by-State basis, using the amount of each such State allotment, to be made available to each of the qualified 211 service entities in such State; and\n**(C)**\nto award grants to such qualified 211 service entities in each State under section 4;\n**(2)**\nbeginning with calendar year 2026 and not less frequently than once every 5 calendar years thereafter, to submit to the Secretary an evaluation of the network of 211 service providers throughout the United States that is conducted in accordance with subsection (d);\n**(3)**\nbeginning with calendar year 2026 and each calendar year thereafter, to submit to the Secretary the report under subsection (d);\n**(4)**\nwith respect to the purpose specified in section 2(a)(2), to increase coordination among 211 service providers, 911 service providers, 988 service providers, and other entities providing similar services; and\n**(5)**\nwith respect to the purpose specified in section 2(a)(3), to develop and implement a public awareness campaign that\u2014\n**(A)**\neducates the public with respect to the purpose, function, and use of 211 services; and\n**(B)**\nensures consistent messaging and branding across 211 service providers.\n##### (c) Shared data platforms\nThe administering agency may use funds reserved under section 6 to support shared data platforms, including with respect to the integration or sharing of 211 resource and service-level data.\n##### (d) Application\nAn eligible entity seeking to be selected as the administering agency under this section shall submit to the Secretary an application not less frequently than once every 10 years, at such time, in such manner, and containing such information as the Secretary may require, including the following:\n**(1)**\nHow the eligible entity intends to\u2014\n**(A)**\nmeet the goal of ensuring that every individual in the United States with phone or internet service can connect to 211 services at no charge; and\n**(B)**\nmeet the goal of ensuring availability, throughout each State, of 211 information and referral services with respect to health and human services.\n**(2)**\nInformation about the manner in which the entity will\u2014\n**(A)**\nselect qualified 211 service entities to receive a grant (or subgrant) under this Act;\n**(B)**\ndevelop, sustain, and evaluate the 211 services provided in the United States and work to ensure sufficient 211 service provider capacity for answering and responding to calls to 211;\n**(C)**\nprovide for increased coordination between 211, 911, and 988 systems and other entities providing similar services to divert calls to mental health and human services responders who can assist individuals and link individuals with voluntary, community-based services, as appropriate; and\n**(D)**\nuse annual 211 operational data to inform the eligible entity\u2019s approach to assessing the program and establishing oversight metrics.\n**(3)**\nA certification that the entity will take all steps necessary to ensure that all activities and information provided by the qualified 211 service entities receiving grants (or eligible 211 service provider receiving a subgrant) pursuant to this Act will be directly accessible for purposes of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ), section 508 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794d ), and part 1194 of title 36, Code of Federal Regulations (or any successor regulations).\n##### (e) Evaluation and reports\n**(1) Evaluation**\n**(A) In general**\nThe administering agency shall award a contract to an independent entity to conduct the evaluation specified in subsection (b)(2).\n**(B) Content**\nThe evaluation under subsection (b)(2) shall address\u2014\n**(i)**\nbarriers to access to 211 services;\n**(ii)**\neffectiveness of 211 services at connecting individuals to needed health and human services;\n**(iii)**\nthe effectiveness of collaborations among 211, 988, and 911 systems, and other entities providing similar services;\n**(iv)**\nthe comprehensiveness of the information in the 211 databases;\n**(v)**\npublic awareness of 211 services; and\n**(vi)**\nuser satisfaction with 211 services.\n**(2) Report**\nThe administering agency shall submit to the Secretary a report on the program carried out under this section, with information disaggregated by State and by each eligible 211 service provider, which shall\u2014\n**(A)**\ndescribe the activities or services funded through a grant by each qualified 211 service entity receiving such a grant (or each eligible 211 service provider receiving a subgrant);\n**(B)**\nassess the effectiveness of such activities and services in making available, to all residents of the State, 211 services for information and referrals with respect to health and human services;\n**(C)**\nassess the effectiveness of collaboration with resource and referral entities and service providers; and\n**(D)**\ndescribe the services to which individuals were referred by eligible 211 service providers receiving funding under this Act and any efforts to track the effectiveness of such referrals.\n#### 4. Grants to 211 service entities to increase capacity\n##### (a) In general\nThe administering agency shall make grants to qualified 211 service entities in a State to expand the availability and accessibility of 211 services in the State.\n##### (b) Use of funds\nThe administering agency shall, as a condition on the receipt of funding under this Act, ensure that any qualified 211 service entity selected by the administering agency to receive a grant using such funds, only use such grant for\u2014\n**(1)**\nthe provision of 211 services via voice, short message service, or other messaging, internet, or other communication methods, including\u2014\n**(A)**\nthe operation and maintenance of 211 contact centers;\n**(B)**\nincreasing public awareness of 211 services in the State in collaboration with 911 and 988 services and other entities providing similar services;\n**(C)**\ncoordination of the State\u2019s 211 services, including the collection, accessibility, and display of information through information and referral databases;\n**(D)**\nthe conduct of statewide and regional planning for the provision of 211 services; and\n**(E)**\nany activities necessary to ensure that 211 services are directly accessible, consistent with the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ), section 508 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794d ), and part 1194 of title 36, Code of Federal Regulations (or any successor regulations);\n**(2)**\nthe start-up costs of extending 211 services to unserved areas, including costs of software and hardware upgrades and telecommunications and internet costs;\n**(3)**\nadministrative costs, such as staffing, training, and activities related to accreditation;\n**(4)**\ninfrastructure costs, including internet hosting and site development and maintenance for an information and referral database and the development and maintenance of cloud-based data and messaging capacity;\n**(5)**\nthe evaluation of 211 service provider activities and capacity;\n**(6)**\nincreasing coordination and collaboration\u2014\n**(A)**\namong 211 services within the State;\n**(B)**\nwith local 911 and 988 service providers; and\n**(C)**\nwith shared data platforms, including with respect to the integration or sharing of resource and service-level data;\n**(7)**\nthe preparation and submission of reports under State reporting requirements and to the administering agency for purposes of section 3(b)(4);\n**(8)**\ninnovations that support service delivery; and\n**(9)**\ncarrying out such other activities determined to be appropriate by the administering agency.\n##### (c) Selection\n**(1) In general**\n**(A) State 211 networks**\nExcept as provided in subparagraph (B), the administering agency shall award the State allocation determined under section 3(b)(1) to the eligible State 211 network in each State.\n**(B) Exception**\nIf the administering agency determines there is no eligible State 211 network in a State, the administering agency shall award grants from the State allotment determined under section 3(b)(1) directly to all eligible 211 service providers in such State.\n**(2) Considerations**\nIn awarding grants to all eligible 211 service providers in a State under paragraph (1)(B), the administering agency shall consider\u2014\n**(A)**\nthe ability of the 211 service provider seeking the grant to carry out activities in furtherance of the provision of 211 services;\n**(B)**\nthe extent to which the award of the grant will facilitate equitable geographic distribution of grants to ensure that rural communities have access to 211 services; and\n**(C)**\nthe extent to which the award of the grant will further the goals of\u2014\n**(i)**\nmaking available 211 services to all individuals in a State via voice, short message service, or other messaging, internet, or other communication methods; and\n**(ii)**\nincreasing the provision of community information and referral with respect to health and human services, among individuals, families, agencies seeking such services and the providers of such services.\n**(3) Conditions**\nThe administering agency shall ensure that each qualified 211 service entity submits an application and agrees, as a condition on the receipt of funds under this section\u2014\n**(A)**\nin making 211 services available, to the maximum extent practicable, to\u2014\n**(i)**\nabide by the most recently issued version of the Inform USA Standards and Quality Indicators for Professional Information and Referral or a comparable set of standards;\n**(ii)**\ncollaborate with public and private organizations that provide health and human services and existing national, regional, and local information and referral systems to provide an exhaustive and comprehensive database of services that is maintained and updated on a consistent basis from which to provide information or referrals to individuals using 211 services; and\n**(iii)**\nensure State-level coordination across all 211 service providers in such State; and\n**(B)**\nto provide matching funds, in the form of cash or in-kind contributions, from non-Federal sources in an amount equal to not less than 25 percent of the amount of funds received by the entity under this section.\n##### (d) Administrative costs for certain states\nIn the case of a State described in subsection (c)(1)(B), the administering agency may use, of the amount of the allocation determined for such State under section 2(c), an amount determined by the administering agency necessary to cover additional administrative expenses incurred by the administering agency resulting from the lack of an eligible State 211 network in such State.\n#### 5. Definitions\nIn this Act:\n**(1) 211 service**\nThe term 211 service means providing individuals with information and referrals, via voice telephone, text telephone, short message service, text, internet phone, or other communication methods, with respect to health and human services and referrals to agencies providing health and human services.\n**(2) Eligible 211 service provider**\nThe term eligible 211 service provider means a provider of 211 services that\u2014\n**(A)**\nis a nonprofit or governmental entity;\n**(B)**\nhas the capability (directly or through contract with another entity) to provide such services via phone at no charge to the consumer; and\n**(C)**\nhas access to the applicable State or local 211 dialing code.\n**(3) Qualified 211 service entity**\nThe term qualified 211 service entity means\u2014\n**(A)**\nan eligible State 211 network; and\n**(B)**\nin the case of a State described in section 4(c)(1)(B), an eligible 211 service provider.\n**(4) Eligible state 211 network**\nThe term eligible State 211 network means a nonprofit entity that\u2014\n**(A)**\nrepresents all eligible 211 service providers in a State; and\n**(B)**\nprovides coordination or infrastructure for providers of 211 services, including\u2014\n**(i)**\nacting as a fiscal agent for State 211 funding; or\n**(ii)**\nsupporting information and referral databases, phone systems, dashboards, web access, or text and website chat tools.\n**(5) Health and human services**\nThe term health and human services means services provided with respect to homelessness and housing supports, veterans resources, food assistance, disaster response and recovery resources, workforce development, community health resources, mental health resources, caregiving resources, domestic violence resources, and other health and human service needs, that\u2014\n**(A)**\nassist individuals in becoming more self-sufficient, in preventing dependency, and in strengthening family relationships;\n**(B)**\naddress social determinants of health;\n**(C)**\nsupport personal and social development; or\n**(D)**\nhelp ensure the health and well-being of individuals, families, and communities.\n**(6) Indian Tribe; Tribal organization**\nThe terms Indian Tribe and Tribal organization have the meanings given such terms in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(7) State**\nThe term State means the several States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands, or an Indian Tribe or Tribal organization.\n#### 6. Funding\n##### (a) Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act $250,000,000 for each of fiscal years 2026 through 2032, to remain available until expended.\n##### (b) Reservation\nOf the amount made available under paragraph (1) to carry out this Act for a fiscal year, the Secretary may reserve not more than 10 percent for administrative and coordinating activities by the administering agency (including the expenditures referred to in section 4(d)).",
      "versionDate": "2026-04-27",
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
        "name": "Health",
        "updateDate": "2026-05-20T13:25:45Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8520ih.xml"
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
      "title": "HELP Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HELP Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Human-Services Emergency Logistics Program Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To facilitate nationwide accessibility and coordination of 211 services in order to provide information and referral to all individuals in the United States for health and human services needs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:29Z"
    }
  ]
}
```
