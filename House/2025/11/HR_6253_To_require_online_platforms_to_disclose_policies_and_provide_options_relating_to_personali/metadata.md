# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6253?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6253
- Title: Algorithmic Transparency and Choice Act
- Congress: 119
- Bill type: HR
- Bill number: 6253
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-01-07T22:27:15Z
- Update date including text: 2026-01-07T22:27:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-21 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-21 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6253",
    "number": "6253",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001039",
        "district": "3",
        "firstName": "Kat",
        "fullName": "Rep. Cammack, Kat [R-FL-3]",
        "lastName": "Cammack",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Algorithmic Transparency and Choice Act",
    "type": "HR",
    "updateDate": "2026-01-07T22:27:15Z",
    "updateDateIncludingText": "2026-01-07T22:27:15Z"
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
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
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
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:02:50Z",
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
                "date": "2025-12-11T21:39:04Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:38:48Z",
                "name": "Markup by"
              },
              {
                "date": "2025-11-21T21:38:38Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6253ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6253\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mrs. Cammack introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require online platforms to disclose policies and provide options relating to personalized recommendations systems to minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Algorithmic Transparency and Choice Act .\n#### 2. Notice and algorithm preference requirements for covered online platforms to provide to minors\n##### (a) Requirements\nBeginning on the date that is 1 year after the date of the enactment of this Act, the provider of a covered online platform shall do the following:\n**(1)**\nProvide covered users of the platform with the following:\n**(A)**\nA notice that the platform uses a personalized recommendation system to select the content the covered user sees, presented in a clear and conspicuous manner on the platform whenever the covered user interacts with a personalized recommendation system for the first time.\n**(B)**\nA notice, included in the terms and conditions of the platform, in a clear, accessible, and easily comprehensible manner that is updated whenever the platform makes a material change, that includes the following:\n**(i)**\nA description of any feature, input, and parameter essential to the operation of the personalized recommendation system.\n**(ii)**\nHow any user-specific data used by the personalized recommendation system is collected or inferred about a covered user of the platform and each category of such data.\n**(iii)**\nAny option that the platform makes available for a covered user of the platform to opt out or exercise an option under subparagraph (C) or (D), modify the profile of the covered user, or to influence any feature, input, or parameter used by the personalized recommendation system.\n**(iv)**\nAny quantity (such as time spent using a product or specific measure of engagement or social interaction) that the personalized recommendation system is designed to optimize, as well as a general description of the relative importance of each quantity for such ranking.\n**(C)**\nAn option to easily switch between the personalized recommendation system and an input-transparent algorithm in their use of the platform.\n**(D)**\nAn option to limit the type or category of recommendations from a personalized recommendation system.\n**(2)**\nProvide an input-transparent algorithm as the default setting for a covered user of the platform.\n##### (b) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of Commission**\n**(A) In general**\nThe Federal Trade Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n##### (c) Rules of construction\n**(1) Disclosure of proprietary and privileged information prohibited**\nNothing in this section may be construed to require a covered online platform to disclose any information, including data or any personalized recommendation system\u2014\n**(A)**\nrelating to a trade secret or other protected intellectual property;\n**(B)**\nthat is confidential business information; or\n**(C)**\nthat is privileged.\n**(2) Rule of construction**\nNothing in this section may be construed to limit or prohibit the ability of a covered online platform to, at the direction of a covered user or group of covered users, restrict another covered user from searching for, finding, accessing, or interacting with the account, content, data, or online community of such covered user or group.\n##### (d) Definitions\nIn this section:\n**(1) Approximate geolocation information**\nThe term approximate geolocation information means information that identifies the location of an individual, but with a precision of less than 5 miles.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Connected device**\nThe term connected device means an electronic device that\u2014\n**(A)**\nis capable of connecting to the internet, either directly or indirectly through a network, to communicate information at the direction of an individual;\n**(B)**\nhas computer processing capabilities for collecting, sending, receiving, or analyzing data; and\n**(C)**\nis primarily designed for or marketed to consumers.\n**(4) Covered online platform**\nThe term covered online platform means an online platform that uses a personalized recommendation system.\n**(5) Covered user**\nThe term covered user means, with respect to an online platform, a minor who registers an account or creates a profile on the covered platform.\n**(6) Fully automated system**\nThe term fully automated system means an operation or set of operations performed on data with minimal or no direction, instruction, prompting, oversight, involvement, or intervention by a natural person.\n**(7) Input-transparent algorithm**\n**(A) In general**\nThe term input-transparent algorithm means a fully automated system that does not use the user-specific data of a covered user to determine the selection, order, relative prioritization, or relative prominence of information that is furnished to such covered user on an online platform, unless the user-specific data is expressly provided to the platform by the covered user for such purpose.\n**(B) Data expressly provided to the platform**\nFor purposes of subparagraph (A), user-specific data that is provided by a covered user for the express purpose of determining the selection, order, relative prioritization, or relative prominence of information that is furnished to such user on an online platform\u2014\n**(i)**\nincludes any search term, filter, and speech pattern supplied by the covered user (if provided for the purpose of enabling the platform to accept spoken input or selecting the language in which the covered user interacts with the platform), saved preference, the resumption of a previous search, and the current precise geolocation information that is supplied by the covered user;\n**(ii)**\nincludes the current approximate geolocation information of the covered user;\n**(iii)**\nincludes data affirmatively submitted to the platform by the covered user that expresses the clear desire of the covered user to receive particular information;\n**(iv)**\ndoes not include the history of the connected device of the covered user, including the history of web searches and browsing, previous geographical locations, physical activity, device interaction, and financial transactions of the covered user; and\n**(v)**\ndoes not include inferences about the covered user or the connected device of the covered user, without regard to whether such inferences are based on data described in clauses (i) or (iii).\n**(8) Minor**\nThe term minor means an individual under the age of 18.\n**(9) Online platform**\nThe term online platform \u2014\n**(A)**\nmeans a public-facing website, internet application, or mobile internet application, including a social network, or video sharing service\u2014\n**(i)**\nthat serves the public; and\n**(ii)**\nthat primarily provides a forum for user-generated content, including messages, videos, images, games, and audio files; and\n**(B)**\ndoes not include\u2014\n**(i)**\na provider of broadband internet access service (as described in section 8.1(b) of title 47, Code of Federal Regulations, or successor regulation); or\n**(ii)**\nelectronic mail.\n**(10) Personalized recommendation system**\nThe term personalized recommendation system \u2014\n**(A)**\nmeans a fully automated system that determines the selection, order, relative prioritization, or relative prominence of information that is furnished to a covered user on an online platform based, in whole or part, on user-specific data that was not expressly provided by the covered user to the platform for such purpose; and\n**(B)**\ndoes not include a fully automated system used by an online platform if\u2014\n**(i)**\nthe only user-specific data, including any inference about the covered user, that the system uses is\u2014\n**(I)**\ninformation relating to the age of the covered user; and\n**(II)**\nsuch information is only used to fulfill a request to restrict the access of a covered user to content on the basis that the content is not age-appropriate for the covered user; or\n**(ii)**\nsuch system is designed to block or filter spam, prevent or detect fraud or other illegal activity, or preserve the security of any system, product, or service.\n**(11) Precise geolocation information**\nThe term precise geolocation information means geolocation information that identifies the location of an individual to within a range of 5 miles or less.\n**(12) User-specific data**\nThe term user-specific data means information relating to a covered user or a specific connected device that would not necessarily be true of every individual or device.\n##### (e) Relationship to State laws\nNo State or political subdivision of a State may prescribe, maintain, or enforce any law, rule, regulation, requirement, standard, or other provision having the force and effect of law, if such law rule, regulation, requirement, standard, or other provision covers the requirements of subsection (a).",
      "versionDate": "2025-11-21",
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
            "name": "Child safety and welfare",
            "updateDate": "2026-01-07T20:51:46Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-01-07T20:51:07Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-01-07T21:14:07Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-01-07T20:53:22Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2026-01-07T22:27:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-10T21:35:00Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6253ih.xml"
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
      "title": "Algorithmic Transparency and Choice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Algorithmic Transparency and Choice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require online platforms to disclose policies and provide options relating to personalized recommendations systems to minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:19Z"
    }
  ]
}
```
