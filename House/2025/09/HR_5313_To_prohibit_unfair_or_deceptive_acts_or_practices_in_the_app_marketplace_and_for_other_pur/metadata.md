# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5313?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5313
- Title: App Store Freedom Act
- Congress: 119
- Bill type: HR
- Bill number: 5313
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-12-05T22:52:26Z
- Update date including text: 2025-12-05T22:52:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5313",
    "number": "5313",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "F000478",
        "district": "7",
        "firstName": "Russell",
        "fullName": "Rep. Fry, Russell [R-SC-7]",
        "lastName": "Fry",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "App Store Freedom Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:52:26Z",
    "updateDateIncludingText": "2025-12-05T22:52:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:05:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5313ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5313\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Fry introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit unfair or deceptive acts or practices in the app marketplace, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the App Store Freedom Act .\n#### 2. Protecting a competitive app market\n##### (a) Requirements\n**(1) Interoperability**\nA covered company that owns or controls the operating system on which an app store owned or controlled by the covered company operates shall allow and provide readily accessible means for a user of such operating system to\u2014\n**(A)**\nchoose a third-party app or app store as a default;\n**(B)**\ninstall a third-party app or app store through means other than the app store owned or controlled by the covered company; and\n**(C)**\nhide or delete an app or app store provided or pre-installed by the covered company (or any business partner of the covered company).\n**(2) Open app development**\nA covered company, in a timely manner, without cost, and on terms that are equivalent to the terms of access by the covered company or any business partner of the covered company, shall provide to a developer of an app accessible on an operating system, or distributed through an app store, owned or controlled by the covered company\u2014\n**(A)**\naccess to any interface and hardware and software feature of the operating system that are generally available to the covered company and any business partner of the covered company; and\n**(B)**\ndocumentation and development information sufficient to access any such interface and feature.\n**(3) Compliance**\nA covered company shall be in compliance with the requirements described under paragraph (2) if that company\u2014\n**(A)**\nlicenses any intellectual property that the developer of an app needs to access any interface or hardware or software feature of such operating system; or\n**(B)**\nlimits the interfaces and hardware and software features of the operating system generally available to the covered company and any businesses partner of the company to interfaces and hardware and software features that do not implicate such intellectual property rights.\n##### (b) Prohibitions\n**(1) Exclusivity and tying**\nA covered company may not\u2014\n**(A)**\nrequire, as a condition for an app to be accessible on an operating system or distributed through an app store that is owned or controlled by the covered company, that\u2014\n**(i)**\na developer of the app use or enable an in-app payment system owned or controlled by the covered company or any business partner of the covered company; or\n**(ii)**\npricing or other terms of sale be equal to or more favorable on such operating system or app store than on another operating system or app store; or\n**(B)**\ntake punitive action or otherwise impose less favorable terms and conditions against a developer of an app distributed outside of an app store that is owned or controlled by the covered company\u2014\n**(i)**\nfor using or offering different pricing or other terms of sale on an app store or through an in-app payment system that is not owned or controlled by the covered company; or\n**(ii)**\non the basis that such app provides access to a third-party app that is not owned or controlled by the covered company through remote electronic services rather than through download from an operating system or an app store that is owned or controlled by the covered company.\n**(2) Interference with legitimate business communications**\n**(A) In general**\nA covered company may not impose any restriction or fee on the communication of a developer of an app accessible on an operating system or distributed through an app store that is owned or controlled by the covered company with a user of the app, whether through such app or direct outreach to such user, concerning legitimate business offers, including pricing or other terms of sale and product or service offerings.\n**(B) Rule of construction**\nNothing in this paragraph may be construed to prohibit a covered company from requiring that consent of a user be obtained prior to collecting and sharing data of the user through an app accessible on an operating system or distributed through an app store that is owned or controlled by the covered company if the apps and services of the company are subject to the same consent.\n**(3) Nonpublic business information**\nA covered company may not use nonpublic business information derived from an app accessible on an operating system or distributed through an app store that is owned or controlled by the covered company for the purpose of competing with such app.\n#### 3. Enforcement\n##### (a) Enforcement by Federal trade commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of commission**\nExcept as provided in paragraph (3)\u2014\n**(A)**\nthe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act; and\n**(B)**\nany covered company who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(3) Penalties**\n**(A) Additional civil penalty**\nIn addition to any penalty applicable under the Federal Trade Commission Act, any covered company who violates this Act shall be liable for a civil penalty of not more than $1,000,000 for each violation.\n**(B) Method**\nAny civil penalty described in subparagraph (A) shall be obtained in the same manner as a civil penalty for a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(4) Authority preserved**\nNothing in this section may be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Enforcement by states\n**(1) In general**\nIf the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by an act or practice that violates this Act, the State may bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(2) Rights of commission**\n**(A) Notice to commission**\n**(i) In general**\nExcept as provided in clause (iii), an attorney general, official, or agency of a State, before filing a civil action under paragraph (1), shall provide written notification to the Commission that the attorney general, official, or agency intends to bring such civil action.\n**(ii) Contents**\nThe notification required under clause (i) shall include a copy of the complaint for the civil action.\n**(iii) Exception**\nIf it is not feasible for an attorney general, official, or agency of a State to provide the notification required under clause (i) before filing a civil action under paragraph (1), the attorney general, official, or agency shall provide the notification to the Commission immediately upon the filing of the civil action.\n**(B) Intervention by commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action filed by an attorney general, official, or agency of a State under paragraph (1); and\n**(ii)**\nupon so intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nappeal a decision in the civil action.\n**(C) Limitation on state action while Federal action is pending**\nIf the Commission or the Attorney General of the United States has instituted a civil action for violation of this Act (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under paragraph (1) during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of such Act alleged in such complaint.\n**(3) Rule of construction**\nFor purposes of bringing a civil action under paragraph (1), nothing in this Act may be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of the State to conduct investigations, administer oaths or affirmations, or compel the attendance of witnesses or the production of documentary or other evidence.\n#### 4. Effect on State law\n##### (a) In general\nA State, or political subdivision of a State, may not maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of the State, or political subdivision of the State, that\u2014\n**(1)**\nprohibits a covered company from engaging in any conduct prohibited by section 2; or\n**(2)**\nrequires a covered company to take any action required by section 2.\n##### (b) Rule of construction\nThis section may not be construed to\u2014\n**(1)**\npreempt any law of a State or political subdivision of a State relating to contracts, torts, or unfair competition; or\n**(2)**\npreempt any law of a State or political subdivision of a State to the extent that such law relates to an act of fraud, unauthorized access to personal information, or notification of unauthorized access to personal information.\n#### 5. Rules of construction\nNothing in this Act may be construed\u2014\n**(1)**\nto limit\u2014\n**(A)**\nany authority of the Federal Trade Commission under the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ), or any other provision of law; or\n**(B)**\nthe application of any Federal law;\n**(2)**\nto require a covered company\u2014\n**(A)**\nto provide service under a hardware or software warranty for damage caused by a third-party app or app store installed through means other than an app store owned or controlled by the covered company; or\n**(B)**\nto provide customer service for the installation or operation of such a third-party app or app store;\n**(3)**\nto prevent an action taken by a covered company that is reasonably tailored to protect the rights of a person under section 106, 1101, 1201, or 1401 of title 17, United States Code, or rights actionable under sections 32 or 43 of the Act entitled An Act to provide for the registration and protection of trademarks used in commerce, to carry out the provisions of certain international conventions, and for other purposes , approved July 5, 1946 (commonly known as the Lanham Act or the Trademark Act of 1946 ) ( 15 U.S.C. 1114 , 1125), or corollary State law;\n**(4)**\nto require a covered company to license any intellectual property, including any trade secrets, owned by or licensed to the covered company;\n**(5)**\nto prevent a covered company from asserting rights of the covered company under intellectual property law to prevent the unlawful use of any intellectual property owned by or duly licensed to the covered company;\n**(6)**\nto require a covered company to work with or share data with any person who\u2014\n**(A)**\nis on any list maintained by the Federal Government by which entities are identified as limited or prohibited from engaging in economic transactions as part of United States sanctions or export control regimes;\n**(B)**\nis a foreign entity that has been identified by the Federal Government as a national security, intelligence, or law enforcement risk, including the Government of the People\u2019s Republic of China or the government of a foreign adversary (as defined in section 8(c)(2) of the Secure and Trusted Communications Networks Act of 2019 ( 473 U.S.C. 1607(c)(2) )); or\n**(C)**\nis a foreign adversary controlled application (as defined in section 2(g)(3) of the Protecting Americans from Foreign Adversary Controlled Applications Act ( Public Law 118\u201350 ; 15 U.S.C. 9901 note)); or\n**(7)**\nto limit any Federal or State law relating to antitrust.\n#### 6. Definitions\nIn this Act:\n**(1) App**\nThe term app means a software application or electronic service that may be run or directed by a user on a computer, a mobile device, or any other general purpose consumer computing device.\n**(2) App store**\nThe term app store means a publicly available website, software application, or other electronic service that may distribute apps from third-party developers to users of a computer, a mobile device, or any other general purpose consumer computing device.\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Covered company**\nThe term covered company means any person who owns or controls\u2014\n**(A)**\nan app store for which the number of users in the United States exceeds 100,000,000; and\n**(B)**\nthe operating system on which such app store operates.\n**(5) Developer**\nThe term developer means a person who owns or controls an app or an app store.\n**(6) In-app payment system**\nThe term in-app payment system means an application, service, or user interface to manage billing or process a payment from a user of an app.\n**(7) Nonpublic business information**\nThe term nonpublic business information means nonpublic data that is\u2014\n**(A)**\nderived from a developer or an app or app store owned or controlled by a developer, including an interaction between a user and the app or app store of the developer; and\n**(B)**\ncollected by a covered company in the course of operating an app store or providing an operating system.\n**(8) Operating system**\nThe term operating system includes an operating system configuration.\n#### 7. Guidance; effective date\n##### (a) FTC guidance\nNot later than 180 days after the date of the enactment of this Act, the Commission shall issue guidance to assist covered companies in complying with this Act.\n##### (b) Effective date\nThis Act shall take effect on the date on which the Commission issues guidance under subsection (a).",
      "versionDate": "2025-09-11",
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
        "actionDate": "2025-05-06",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3209",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "App Store Freedom Act",
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
        "updateDate": "2025-09-24T15:25:15Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5313ih.xml"
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
      "title": "App Store Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T07:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "App Store Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit unfair or deceptive acts or practices in the app marketplace, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T07:18:29Z"
    }
  ]
}
```
