# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6489?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6489
- Title: SAFE BOTs Act
- Congress: 119
- Bill type: HR
- Bill number: 6489
- Origin chamber: House
- Introduced date: 2025-12-05
- Update date: 2026-02-24T16:53:51Z
- Update date including text: 2026-02-24T16:53:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-05: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-05 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-12-05: Introduced in House

## Actions

- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-05 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-05",
    "latestAction": {
      "actionDate": "2025-12-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6489",
    "number": "6489",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "SAFE BOTs Act",
    "type": "HR",
    "updateDate": "2026-02-24T16:53:51Z",
    "updateDateIncludingText": "2026-02-24T16:53:51Z"
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
      "actionDate": "2025-12-05",
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
      "actionDate": "2025-12-05",
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
      "actionDate": "2025-12-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-05",
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
          "date": "2025-12-05T16:00:35Z",
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
                "date": "2025-12-11T21:39:58Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:39:48Z",
                "name": "Markup by"
              },
              {
                "date": "2025-12-05T21:39:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6489ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6489\nIN THE HOUSE OF REPRESENTATIVES\nDecember 5, 2025 Mrs. Houchin introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo ensure that providers of chatbots clearly and conspicuously disclose to users who are minors that chatbots are artificial intelligence systems, not natural person, and do not provide advice from licensed professionals, and for other proposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Adolescents From Exploitative BOTs Act or the SAFE BOTs Act .\n#### 2. Requirements for chatbots used by minors\n##### (a) Certain statements prohibited\nA chatbot provider may not provide to a covered user a chatbot that states to the covered user that the chatbot is a licensed professional (unless such statement is true).\n##### (b) Disclosure required\n**(1) In general**\nA chatbot provider shall clearly and conspicuously disclose, in accordance with paragraphs (2) and (3), to each covered user of a chatbot of such provider notice of the following:\n**(A)**\nThe chatbot is an artificial intelligence system and not a natural person.\n**(B)**\nResources for contacting a suicide and crisis intervention hotline.\n**(2) Timing**\n**(A) AI system disclosure**\nA disclosure under paragraph (1)(A) shall be made\u2014\n**(i)**\nat the initiation of the first interaction of a covered user with a chatbot; and\n**(ii)**\nat any point at which, during an interaction of a covered user with a chatbot, the covered user prompts the chatbot about whether the chatbot is an artificial intelligence system.\n**(B) Crisis resources disclosure**\nA disclosure under paragraph (1)(B) shall be made at any point at which, during an interaction of a covered user with a chatbot, the covered user prompts the chatbot about suicide or suicidal ideation.\n**(3) Use of plain language**\nA disclosure under paragraph (1) shall be made in a clear, age-appropriate, and plain language manner that is reasonably understandable by a minor.\n##### (c) Policies required\nA chatbot provider shall establish, implement, and maintain reasonable policies, practices, and procedures\u2014\n**(1)**\nto ensure that a chatbot of the provider advises a covered user to take a break from the chatbot at the point at which a continuous and uninterrupted interaction of the covered user with the chatbot has lasted for 3 hours; and\n**(2)**\nto address, with respect to covered users\u2014\n**(A)**\nsexual material harmful to minors;\n**(B)**\ngambling; and\n**(C)**\nthe distribution, sale, or use of illegal drugs, tobacco products, or alcohol.\n##### (d) Effective date\nSubsections (a), (b), and (c) shall take effect on the date that is 1 year after the date of the enactment of this Act.\n##### (e) Enforcement by federal trade commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (a), (b), or (c) shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of commission**\nThe Federal Trade Commission shall enforce subsections (a), (b), and (c) in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section. Any person who violates subsection (a), (b), or (c) shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(3) Authority preserved**\nNothing in this subsection may be construed to limit the authority of the Federal Trade Commission under any other provision of law.\n##### (f) Actions by states\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of subsection (a), (b), or (c), the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with such subsection;\n**(C)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(D)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(2) Notice**\nBefore filing an action under this subsection, the attorney general, official, or agency of the State involved shall provide to the Federal Trade Commission a written notice of such action and a copy of the complaint for such action. If the attorney general, official, or agency determines that it is not feasible to provide the notice described in this paragraph before the filing of the action, the attorney general, official, or agency shall provide written notice of the action and a copy of the complaint to the Federal Trade Commission immediately upon the filing of the action.\n**(3) Authority of federal trade commission**\n**(A) In general**\nOn receiving notice under paragraph (2) of an action under this subsection, the Federal Trade Commission shall have the right\u2014\n**(i)**\nto intervene in the action; and\n**(ii)**\nupon so intervening\u2014\n**(I)**\nto be heard on all matters arising therein; and\n**(II)**\nto file petitions for appeal.\n**(B) Limitation on state action while federal action is pending**\nIf the Federal Trade Commission or the Attorney General of the United States has instituted a civil action for violation of subsection (a), (b), or (c) (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under this subsection during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of such subsection alleged in such complaint.\n**(4) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this Act shall be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n##### (g) Study on chatbots and mental health of minors\n**(1) In general**\nThe Secretary of Health and Human Services, acting through the Director of the National Institutes of Health, shall conduct a 4-year longitudinal study to evaluate the risks and benefits of chatbots with respect to the mental health of minors, including with respect to loneliness, anxiety, social skill building, social isolation, depression, self-harm, and suicidal ideation.\n**(2) Consultation**\nIn carrying out the study under paragraph (1), the Secretary shall consult with\u2014\n**(A)**\nthe Director of the National Institute of Mental Health;\n**(B)**\npediatric mental health experts;\n**(C)**\ntechnologists;\n**(D)**\nethicists; and\n**(E)**\neducators.\n**(3) Report**\nNot later than 4 years after the date of the enactment of this Act, the Secretary, acting through the Director, shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committees on Commerce, Science, and Transportation and Health, Education, Labor, and Pensions of the Senate a report on the results of the study conducted under paragraph (1) and any related recommendations.\n##### (h) Relationship to state laws\nNo State or political subdivision of a State may prescribe, maintain, or enforce any law, rule, regulation, requirement, standard, or other provision having the force and effect of law, if such law, rule, regulation, requirement, standard, or other provision covers a matter described in subsection (a), (b), or (c).\n##### (i) Rule of construction\nNothing in this Act may be construed to require the affirmative collection by a chatbot provider of any personal information with respect to the age of a user that a chatbot provider is not already collecting in the normal course of business.\n##### (j) Severability\nIf any provision of this Act or the application of this Act to any person or circumstance is held invalid, the remaining provisions of this Act and the application of this Act to other persons or circumstances shall not be affected.\n##### (k) Definitions\nIn this Act:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Chatbot**\nThe term chatbot means an artificial intelligence system, marketed to and available for use by consumers, that engages in interactive, natural-language communication with a user and generates or selects content in response to user inputs (including text, voice, or other inputs) using a conversational context.\n**(3) Chatbot provider**\n**(A) In general**\nThe term chatbot provider means a person that provides a chatbot directly to a consumer for the use of the consumer, including through a website, mobile application, or other online means.\n**(B) Limitation**\nA person that provides a website, mobile application, or other online service that includes a chat function incidental to the predominant purpose of such website, application, or service shall not be treated as a chatbot provider solely on the basis of such incidental chat function.\n**(4) Covered user**\nThe term covered user means a user of a chatbot if the provider of such chatbot\u2014\n**(A)**\nhas actual knowledge that such user is a minor; or\n**(B)**\nwould know that such user is a minor if not for willful disregard.\n**(5) Minor**\nThe term minor means an individual under the age of 17 years.\n**(6) Sexual material harmful to minors**\nThe term sexual material harmful to minors means a picture, image, graphic image file, film, videotape, or other visual depiction that\u2014\n**(A)**\n**(i)**\ntaken as a whole and with respect to minors, appeals to the prurient interest in nudity, sex, or excretion;\n**(ii)**\ndepicts, describes, or represents, in a patently offensive way with respect to what is suitable for minors, an actual or simulated sexual act or sexual contact, actual or simulated normal or perverted sexual acts, or lewd exhibition of the genitals; and\n**(iii)**\ntaken as a whole, lacks serious literary, artistic, political, or scientific value as to minors; or\n**(B)**\nis child pornography.",
      "versionDate": "2025-12-05",
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
            "updateDate": "2026-02-24T16:46:38Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-24T16:46:20Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-24T16:46:14Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2026-02-24T16:53:38Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-02-24T16:53:02Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-02-24T16:52:37Z"
          },
          {
            "name": "Gambling",
            "updateDate": "2026-02-24T16:53:51Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-02-24T16:46:27Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2026-02-24T16:53:44Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-02-24T16:52:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-10T21:36:20Z"
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
      "date": "2025-12-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6489ih.xml"
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
      "title": "SAFE BOTs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE BOTs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Adolescents From Exploitative BOTs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that providers of chatbots clearly and conspicuously disclose to users who are minors that chatbots are artificial intelligence systems, not natural person, and do not provide advice from licensed professionals, and for other proposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:15Z"
    }
  ]
}
```
