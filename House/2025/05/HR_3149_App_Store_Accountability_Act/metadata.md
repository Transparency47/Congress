# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3149?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3149
- Title: App Store Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 3149
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-04-07T17:43:48Z
- Update date including text: 2026-04-07T17:43:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-01 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-01 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3149",
    "number": "3149",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "J000307",
        "district": "10",
        "firstName": "John",
        "fullName": "Rep. James, John [R-MI-10]",
        "lastName": "James",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "App Store Accountability Act",
    "type": "HR",
    "updateDate": "2026-04-07T17:43:48Z",
    "updateDateIncludingText": "2026-04-07T17:43:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-11T21:44:10Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:43:58Z",
                "name": "Markup by"
              },
              {
                "date": "2025-05-01T20:43:43Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "FL"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3149ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3149\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. James (for himself and Mr. Bilirakis ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo safeguard children by providing parents with clear and accurate information about the apps downloaded and used by their children and to ensure proper parental consent is achieved, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the App Store Accountability Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nSec. 3. App store obligations.\nSec. 4. App developer obligations.\nSec. 5. Compliance.\nSec. 6. Enforcement by the Federal Trade Commission.\nSec. 7. Enforcement by States.\nSec. 8. Safe harbor.\nSec. 9. Preemption.\nSec. 10. Severability.\nSec. 11. Effective date.\n#### 2. Definitions\nIn this Act:\n**(1) Age category**\nThe term age category means the category of an individual based on their age, including the following categories:\n**(A) Adult**\nAn adult is such an individual who has attained 18 years of age.\n**(B) Teenager**\nA teenager is such an individual who has attained 16 years of age but has not attained 18 years of age.\n**(C) Child**\nA child is such an individual who has attained 13 years of age but has not attained 16 years of age.\n**(D) Young child**\nA young child is such an individual who has not attained 13 years of age.\n**(2) Age category data**\nThe term age category data means information that identifies the age category of a user and is collected by a covered app store provider and shared with an app developer.\n**(3) Age rating**\nThe term age rating means a publicly displayed assessment of an app\u2019s appropriateness for different age categories.\n**(4) App**\nThe term app means a software application or electronic service that may be run or directed by a user on a computer, mobile device, or any other general purpose computing device.\n**(5) App developer**\nThe term app developer means any person that owns or controls an app on the app store of a covered app store provider and is available in the United States.\n**(6) App store**\nThe term app store means a publicly available website, software application, or other electronic service that distributes and facilitates the download onto a mobile device of an app from a third-party developer by a user of a computer, mobile device, or any other general purpose computing device.\n**(7) Commission**\nThe term Commission means the Federal Trade Commission.\n**(8) Covered app store provider**\nThe term covered app store provider means any person that owns or controls an app store available in the United States and for which users in the United States exceed 5,000,000.\n**(9) Know**\nThe term know means to have actual knowledge or willful disregard.\n**(10) Minor**\nThe term minor means an individual who has not attained 18 years of age.\n**(11) Mobile device**\nThe term mobile device means a phone or general purpose tablet that provides cellular or wireless connectivity, is capable of connecting to the Internet, runs a mobile operating system, and is capable of running apps through the mobile operating system.\n**(12) Mobile operating system**\nThe term mobile operating system means a set of software that manages mobile device hardware resources, provides common services for mobile device programs, controls memory allocation, and provides interfaces for applications to access device functionality.\n**(13) Parent**\nThe term parent , with respect to a minor, means an adult with the legal right to make decisions on behalf of the minor, including\u2014\n**(A)**\na natural parent;\n**(B)**\nan adoptive parent;\n**(C)**\na legal guardian; or\n**(D)**\nan individual with legal custody over the minor.\n**(14) Parental account**\nThe term parental account means an account with a covered app store provider that is\u2014\n**(A)**\nverified to be established by an individual who the app store provider has determined is at least 18 years of age through the covered app store provider\u2019s age verification method or process; and\n**(B)**\naffiliated with one or more account of a user or prospective user who is a minor.\n**(15) Parental consent disclosure**\nThe term parental consent disclosure means the following information that is provided to a parent before obtaining parental consent\u2014\n**(A)**\na description of\u2014\n**(i)**\nthe personal data collected by the app from a user; and\n**(ii)**\nthe personal data shared by the app with a third party;\n**(B)**\na description of the measures taken by the app developer to protect the confidentiality of the user\u2019s personal data;\n**(C)**\nif there is an age rating for the app or an in-app purchase, the app\u2019s or in-app purchase\u2019s age rating; and\n**(D)**\nif there is a content description for the app or in-app purchase, the app\u2019s or in-app purchase\u2019s content description.\n**(16) Personal data**\nThe term personal data has the same meaning as the term personal information as defined in section 1302 of the Children\u2019s Online Privacy Protection Act ( 15 U.S.C. 6501 ).\n**(17) Signal**\nThe term signal means age bracketed data sent by a real-time secure application programming interface or operating system that is likely to be accessed by minors.\n**(18) Significant change**\nThe term significant change means a material modification of an app\u2019s terms of service or privacy policy that\u2014\n**(A)**\nchanges the category of data collected or stored;\n**(B)**\nchanges the category of data shared with an unaffiliated third party that is not a service provider or processor;\n**(C)**\nalters the app\u2019s age rating or content description;\n**(D)**\nadds new monetization features, including in-app purchases or advertisements; or\n**(E)**\nchanges the app\u2019s user experience or functionality in a manner that a reasonable individual would view as material.\n**(19) Verifiable parental consent**\nThe term verifiable parental consent means authorization that is provided\u2014\n**(A)**\nby a parental account;\n**(B)**\nin response to a clear and conspicuous parental content disclosure; and\n**(C)**\nsignifies a parent\u2019s freely given, specific, informed, and unambiguous agreement.\n#### 3. App store obligations\n##### (a) In general\nEach covered app store provider shall\u2014\n**(1)**\nat the time an individual creates an account with the covered app store provider\u2014\n**(A)**\nrequest age information from the individual; and\n**(B)**\nverify the individual\u2019s age category using a commercially available method or process that is reasonably designed to ensure accuracy;\n**(2)**\nif the age verification method or process determines the individual is a minor\u2014\n**(A)**\nrequire the account to be affiliated with a parental account; and\n**(B)**\nobtain verifiable parental consent from the holder of the affiliated parental account before allowing the minor to download or purchase an app or make an in-app purchase;\n**(3)**\nafter receiving notice of a significant change from an app developer\u2014\n**(A)**\nnotify the user of a significant change; and\n**(B)**\nfor a minor account, notify the holder of the affiliated parental account and obtain a new verifiable parental consent;\n**(4)**\nprovide to an app developer the user\u2019s age category and the status of verified parental consent if the user is a minor;\n**(5)**\nnotify an app developer when a parent revokes verifiable parental consent;\n**(6)**\nprotect the confidentiality of personal data related to age verification by\u2014\n**(A)**\nlimiting its collection, processing, and storage to what is strictly necessary to verify a user\u2019s age, obtain verifiable parental consent, or maintain compliance records; and\n**(B)**\nsafeguarding personal data related to age verification by adopting reasonable administrative, technical, and physical safeguards to secure the collection, processing, storage, and transmission of this data, including through industry-standard encryption;\n**(7)**\nif a covered app store provider displays an age rating or description of an app\u2019s content, the age rating and description must be clearly and prominently displayed and be in plain and concise language; and\n**(8)**\nprovide to an app developer the ability to determine, in real time, the age category of any user and, with respect to any user that is a minor, whether the covered app store provider has obtained verifiable parental consent.\n##### (b) Rules of construction\nNothing in this section shall be construed\u2014\n**(1)**\nto prevent a covered app store provider from taking reasonable measures to block, detect, or prevent the distribution of unlawful or obscene material to minors, to block or filter spam, to prevent criminal activity, or to protect the security of an app store or app;\n**(2)**\nto require a covered app store provider to disclose to an app developer information other than such user\u2019s age category and, with respect to any user that is a minor, whether the covered app store provider has obtained verifiable parental consent in accordance with this section;\n**(3)**\nto allow a covered app store provider to use any measures required by this section in a way that is arbitrary, capricious, anti-competitive, or unlawful; or\n**(4)**\nto affect or restrict the expression of political, religious, or other viewpoints.\n#### 4. App developer obligations\n##### (a) In general\nAn app developer shall\u2014\n**(1)**\nverify through a covered app store\u2019s method or process the age category of the app developer\u2019s users or potential users and, for a minor account, whether verifiable parental consent has been obtained;\n**(2)**\nnotify a covered app store provider of a significant change to the app; and\n**(3)**\nrequest age category data or verifiable parental consent\u2014\n**(A)**\nat the time a potential app user downloads or purchases an app;\n**(B)**\nwhen the app developer implements a significant change to the app; or\n**(C)**\nto comply with an applicable law or regulation.\n##### (b) App developer requests\nAn app developer may request age category data or verifiable parental consent\u2014\n**(1)**\nno more than once during each 12-month period to verify the accuracy of user age verification data or continued account use within the verified age category;\n**(2)**\nwhen there is reasonable suspicion of account transfer or misuse outside the verified age category; or\n**(3)**\nat the time a user creates a new account with the app developer.\n##### (c) Permissible uses\nAn app developer may use age category data to\u2014\n**(1)**\nenforce any app developer-created age-related restrictions;\n**(2)**\nensure compliance with applicable laws and regulations; and\n**(3)**\nimplement any app developer-created features or defaults.\n##### (d) Restrictions\nAn app developer may not\u2014\n**(1)**\nenforce a contract or terms of service against a minor unless the app developer has verified through the covered app store provider that verifiable parental consent has been obtained;\n**(2)**\nknowingly misrepresent any material information in the parental consent disclosure; or\n**(3)**\nshare age category data with an unaffiliated third party that is not a service provider or processor.\n##### (e) App age rating\nIf an app developer provides an age rating or description of an app\u2019s content to a covered app store or user, the age rating or description must be in plain and concise language.\n##### (f) Covered app store provider signal\n**(1) In general**\nEach app developer shall use a covered app store provider\u2019s signal to determine the age category of a user.\n**(2) Rule of construction**\nReceipt of a covered app store provider\u2019s signal serves as actual knowledge of a user\u2019s age category.\n#### 5. Compliance\n##### (a) Guidance\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Commission shall issue guidance to assist covered app store providers and app developers in complying with the requirements of this Act.\n**(2) Limitations**\n**(A) No conferring of rights or binding effect**\nAny guidance issued by the Commission with respect to this Act shall not confer any rights on any person, State, or locality, nor shall such guidance operate to bind the Commission or any person to the approach recommended in such guidance.\n**(B) Basis of enforcement actions**\nIn any enforcement action brought pursuant to this Act, the Commission shall allege a specific violation of a provision of this Act. The Commission may not base an enforcement action on, or execute a consent order based on, practices that are alleged to be inconsistent with any such guidelines, unless the practices allegedly violate sections 3 or 4.\n##### (b) Mechanism To certify compliance\n**(1) In general**\nThe Commission shall\u2014\n**(A)**\nestablish a mechanism, in such form and manner as the Commission determines is appropriate, for any covered app store provider to submit a request for the Commission to review their policies relevant to the requirements under section 3; and\n**(B)**\nnot later than 30 days after receiving such a request\u2014\n**(i)**\nreview such policies to determine whether the covered app store provider that submitted such request is compliant with such requirements; and\n**(ii)**\nif the Commission determines that such provider is compliant with such requirements and does not permit or is able to quickly remedy any method of circumventing such requirements, submit to Congress and make publicly available on the website of the Commission a notice certifying that such provider is compliant with such requirements.\n**(2) Notification of significant changes**\nIf a covered app store provider that the Commission certifies is compliant with the requirements of section 3 makes a significant change to any policy of such provider that is relevant to such requirements, such provider shall notify the Commission of such change to ensure that the change does not impact the certification of compliance under paragraph (1).\n**(3) Period of eligibility**\nA certification of compliance under paragraph (1) shall be valid for 1 year after the date of the issuance of such certification.\n##### (c) Complaints\n**(1) In general**\nThe Commission shall establish a mechanism to receive complaints regarding the compliance of any covered app store provider with the requirements described in section 3.\n**(2) Review**\nThe Commission shall regularly review any complaints received through the mechanism described in paragraph (1) and, if necessary, evaluate the covered app store provider's certification of compliance under subsection (b)(1).\n#### 6. Enforcement by the Federal Trade Commission\n##### (a) Unfair or deceptive acts or practices\nA violation of this Act or a regulation promulgated thereunder shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the Commission\n**(1) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person who violates this Act or a regulation promulgated thereunder shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n#### 7. Enforcement by States\n##### (a) In general\n**(1) Civil actions**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of that State has been or is threatened or adversely affected by the engagement of any person in a practice that violates this Act, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in a district court of the United States of appropriate jurisdiction to\u2014\n**(A)**\nenjoin that practice;\n**(B)**\nenforce compliance with the regulation;\n**(C)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(D)**\nobtain such other relief as the court may consider to be appropriate.\n**(2) Notice**\n**(A) In general**\nBefore filing an action under paragraph (1), the attorney general of the State involved shall provide to the Commission\u2014\n**(i)**\na written notice of that action; and\n**(ii)**\na copy of the complaint for that action.\n**(B) Exemption**\n**(i) In general**\nSubparagraph (A) shall not apply with respect to the filing of an action by an attorney general of a State under this subsection, if the attorney general determines that it is not feasible to provide the notice described in that subparagraph before the filing of the action.\n**(ii) Notification**\nIn an action described in clause (i), the attorney general of a State shall provide notice and a copy of the complaint to the Commission at the same time as the attorney general files the action.\n##### (b) Intervention\n**(1) In general**\nOn receiving notice under subsection (a)(2), the Commission shall have the right to intervene in the action that is the subject of the notice.\n**(2) Effect of intervention**\nIf the Commission intervenes in an action under subsection (a), it shall have the right\u2014\n**(A)**\nto be heard with respect to any matter that arises in that action; and\n**(B)**\nto file a petition for appeal.\n##### (c) Construction\nFor purposes of bringing any civil action under subsection (a), nothing in this chapter shall be construed to prevent an attorney general of a State from exercising the powers conferred on the attorney general by the laws of that State to\u2014\n**(1)**\nconduct investigations;\n**(2)**\nadminister oaths or affirmations; or\n**(3)**\ncompel the attendance of witnesses or the production of documentary and other evidence.\n##### (d) Actions by the Commission\nIn any case in which an action is instituted by or on behalf of the Commission for a violation of this Act, no State may, during the pendency of that action, institute an action under subsection (a) against any defendant named in the complaint in that action for such violation.\n##### (e) Venue; service of process\n**(1) Venue**\nAny action brought under subsection (a) may be brought in the district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code.\n**(2) Service of process**\nIn an action brought under subsection (a), process may be served in any district in which the defendant\u2014\n**(A)**\nis an inhabitant; or\n**(B)**\nmay be found.\n#### 8. Safe harbor\n##### (a) In general\nAn app developer is deemed not liable for a violation of this Act if the app developer demonstrates it has\u2014\n**(1)**\nrelied in good faith on age verification data provided by a covered app store provider or it obtained a signal from a covered app store provider that indicates the user is a minor;\n**(2)**\ncomplied with the requirements of section 4; and\n**(3)**\nreasonably conforms to widely accepted industry standards or best practices, or to standards or best practices identified by the Commission, for age ratings and app content descriptions and applies those standards or best practices consistently and in good faith.\n##### (b) Limitations\nThe safe harbor described in this section applies only to actions brought under this Act and does not limit the liability of an app developer under any other applicable law.\n#### 9. Preemption\n##### (a) In general\nNo State or political subdivision of a State may maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of any State, or political subdivision of a State, related to the provisions of this Act.\n##### (b) Rule of construction\nNothing in this subsection shall be construed as preempting, displacing, or supplanting contract or tort law.\n#### 10. Severability\nIf any provision of this Act, or the application thereof to any person or circumstance, is held invalid, the remainder of this Act, and the application of such provision to other persons not similarly situated or to other circumstances, shall not be affected by the invalidation.\n#### 11. Effective date\nExcept as otherwise provided in this Act, this Act shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-05-01",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1586",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "App Store Accountability Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-02-24T19:03:53Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2026-02-24T18:40:58Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-24T18:49:21Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-24T18:49:15Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-02-24T18:49:49Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-07T17:43:47Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-02-24T19:08:50Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2026-02-24T18:42:22Z"
          },
          {
            "name": "Federal Trade Commission (FTC)",
            "updateDate": "2026-02-24T19:04:20Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-02-24T19:05:21Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-02-24T18:42:54Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-02-24T19:01:29Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-02-24T18:49:57Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-02-24T18:44:59Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-24T19:04:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-06-04T15:43:04Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3149ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To safeguard children by providing parents with clear and accurate information about the apps downloaded and used by their children and to ensure proper parental consent is achieved, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T07:49:01Z"
    },
    {
      "title": "App Store Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T07:24:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "App Store Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T07:23:20Z"
    }
  ]
}
```
