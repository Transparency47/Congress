# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8229
- Title: Lower Grocery Prices Act
- Congress: 119
- Bill type: HR
- Bill number: 8229
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-05-01T13:37:42Z
- Update date including text: 2026-05-01T13:37:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8229",
    "number": "8229",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Lower Grocery Prices Act",
    "type": "HR",
    "updateDate": "2026-05-01T13:37:42Z",
    "updateDateIncludingText": "2026-05-01T13:37:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
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
          "date": "2026-04-09T15:30:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-09T15:30:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8229ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8229\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Pappas introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit certain uses of algorithmic decision systems to inform individualized prices for food, groceries, and agricultural commodities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lower Grocery Prices Act .\n#### 2. Prohibition on surveillance-based price setting for food, groceries, and agricultural commodities\n##### (a) Surveillance-Based price setting\n**(1) General prohibition**\nA person may not engage in surveillance-based price setting for food, groceries, or agricultural commodities. If each condition in paragraph (2) is met, any of the following is not surveillance-based price setting:\n**(A)**\nA difference in price is based solely on reasonable costs associated with providing the good or service to different consumers.\n**(B)**\nA discounted price is offered to members of a broadly defined group, including teachers, veterans, senior citizens, or students, based on publicly disclosed eligibility criteria.\n**(C)**\nA discounted price is offered through a loyalty, membership, or rewards program that consumers affirmatively enrolled in, including signing up for a mailing list, registering for promotional communication, or participating in a promotional event.\n**(2) Additional conditions for exception**\nThe conditions in this paragraph are the following:\n**(A)**\nAny eligibility criteria or condition for receiving or earning the discount or reward is clearly and conspicuously disclosed.\n**(B)**\nAny discount or reward is offered uniformly to all consumers who meet the disclosed eligibility criteria.\n**(C)**\nAny surveillance data is used solely to offer or administer the discount or reward and is not used for any other purpose, including profiling, targeted advertising, or individualized price setting.\n**(3) Requirement to publish procedures**\nNot later than 180 days before the date on which a person intends to engage in any of the actions described in subparagraphs (A) through (C) of paragraph (1), that person shall make publicly available, in a conspicuous and accessible format, reasonable procedures that include the following:\n**(A)**\nA process for ensuring the accuracy of all data considered by the automated decision system.\n**(B)**\nA procedure that allows a consumer to correct or challenge the accuracy of data considered by the automated decision system.\n**(C)**\nDisclosure to consumers what data is considered and how automated decision-making considers the data when setting particular prices.\n##### (b) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices; Unfair methods of competition**\nA violation of subsection (a) or a regulation promulgated under such subsection shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices and as a violation of the Federal Trade Commission Act ( 15 U.S.C. 45(a) ) regarding unfair methods of competition.\n**(2) Powers of Commission**\nThe Federal Trade Commission shall enforce subsection (a) and any regulation promulgated under such subsection in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act. Any person who violates such subsection or a regulation promulgated under such subsection shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(3) Common carriers and nonprofit organizations**\nNotwithstanding section 4, 5(a)(2), or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 ; 45(a)(2); 46) or any jurisdictional limitation of the Federal Trade Commission, the Federal Trade Commission shall also enforce subsection (a) or a regulation promulgated under subsection (a), in the same manner provided in paragraphs (1) and (2), with respect to\u2014\n**(A)**\ncommon carriers subject to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) and all Acts amendatory thereof and supplementary thereto; and\n**(B)**\norganizations not organized to carry on business for their own profit or that of their members.\n**(4) Authority preserved**\nNothing in this section may be construed to limit the authority of the Commission under any other provision of law.\n##### (c) Actions by States\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of subsection (a) or a regulation promulgated under such subsection, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with such subsection or such regulation;\n**(C)**\nobtain, per violation, the greater of\u2014\n**(i)**\nthe actual monetary damages incurred from the violation; or\n**(ii)**\n$3,000; or\n**(D)**\nobtain any restitution, penalties, and any other legal or equitable relief on behalf of residents as the court may deem just and proper.\n**(2) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this section may be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n##### (d) Private right of action\n**(1) In general**\nA person injured by an act or practice in violation of subsection (a) or a regulation promulgated under such subsection may bring in an appropriate State court or an appropriate district court of the United States\u2014\n**(A)**\nto enjoin the violation;\n**(B)**\nto obtain, for each violation, the greater of\u2014\n**(i)**\nthe actual monetary damages incurred from the violation; or\n**(ii)**\n$3,000; or\n**(C)**\nto obtain, for each violation, any other restitution, penalties, and other legal or equitable relief as the court may deem just and proper.\n**(2) Willful violations**\nIf the court finds that the defendant acted willfully in committing a violation described in paragraph (1), the court may, in its discretion, increase the amount of the award to an amount equal to not more than 3 times the amount available under paragraph (1)(B).\n**(3) Costs and attorney\u2019s fees**\nThe court shall award to a prevailing plaintiff in an action under this subsection the costs of such action and reasonable attorney\u2019s fees, as determined by the court.\n**(4) Limitation**\nAn action may be commenced under this subsection not later than 5 years after the date on which the person first discovered or had a reasonable opportunity to discover the violation.\n**(5) Nonexclusive remedy**\nThe remedy provided by this subsection shall be in addition to any other remedies available to the person.\n**(6) Invalidity of pre-dispute arbitration and joint action waivers**\nNotwithstanding chapter 1 of title 9, United States Code (commonly known as the Federal Arbitration Act ), or any other provision of law, a pre-dispute arbitration agreement or pre-dispute joint action waiver between a person engaged in the commerce of food, grocery, or agricultural commodities and a consumer is not valid or enforceable for purposes of this section.\n##### (e) Definitions\nIn this section:\n**(1) Automated decision system**\nThe term automated decision system \u2014\n**(A)**\nmeans a system, software, or process that uses computation, the result for which is used to assist or approximate human decision-making; and\n**(B)**\nincludes a system, software, or process derived from machine learning, statistics, or other data processing or artificial intelligence techniques.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Genetic information**\nThe term genetic information \u2014\n**(A)**\nmeans, with respect to an individual, information about\u2014\n**(i)**\nany genetic test;\n**(ii)**\nthe genetic tests of any family member; and\n**(iii)**\nthe manifestation of a disease or disorder in any family member;\n**(B)**\nincludes, with respect to an individual, any request for, or receipt of, genetic services, or participation in clinical research which includes genetic services, by the individual or any family member of the individual; and\n**(C)**\ndoes not include information about the sex or age of the individual.\n**(4) Personal information**\nThe term personal information means any quality, feature, attribute, or trait of an individual, including any immutable characteristic (such as race and eye color), mutable characteristic (such as address, weight, citizenship, family, or parenthood status), and any other information that could reasonably be linked, directly or indirectly, with a particular person or household.\n**(5) Pre-dispute arbitration agreement**\nThe term pre-dispute arbitration agreement means any agreement to arbitrate a dispute that has not arisen at the time of making the agreement.\n**(6) Pre-dispute joint action waiver**\nThe term pre-dispute joint action waiver means an agreement, including as part of a pre-dispute arbitration agreement, that would prohibit, or waive the right of, one of the parties to the agreement to participate in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not arisen at the time of making the agreement.\n**(7) Price**\nThe term price means the amount charged or offered to a consumer in relation to a transaction, including any related cost and fee and any other material term of the transaction that has direct bearing on the amount paid by the consumer or the value of the good or service offered or provided to the consumer.\n**(8) Surveillance-based price setting**\nThe term surveillance-based price setting means using an automated decision system to offer or inform a customized price for a good or service for a specific person or consumer, or group of people or consumers, based, in whole or in part, on surveillance data.\n**(9) Surveillance data**\nThe term surveillance data \u2014\n**(A)**\nmeans data obtained through observation, inference, or surveillance of an individual that is related to personal information, genetic information, behavior, or biometrics of the individual or a group, band, class, or tier in which the individual belongs; and\n**(B)**\nincludes information gathered, purchased, or otherwise acquired.\n##### (f) Preemption of directly conflicting State laws\n**(1) In general**\nNothing in this section may be construed to preempt, displace, or supplant any State law, except to the extent that a provision of State law conflicts with a provision of this section.\n**(2) Greater protection under State law**\nFor the purposes of this section, a provision of State law does not conflict with a provision of this section if such State law provides additional protections with respect to individuals protected under this section with respect to surveillance-based wage setting or the collection of surveillance data.",
      "versionDate": "2026-04-09",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4640",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop AI Price Gouging and Wage Fixing Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2026-04-17T19:09:29Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8229ih.xml"
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
      "title": "Lower Grocery Prices Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T09:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lower Grocery Prices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T09:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit certain uses of algorithmic decision systems to inform individualized prices for food, groceries, and agricultural commodities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T09:18:54Z"
    }
  ]
}
```
