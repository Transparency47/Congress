# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6257
- Title: SMK Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6257
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-02-23T16:53:52Z
- Update date including text: 2026-02-23T16:53:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6257",
    "number": "6257",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "SMK Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-23T16:53:52Z",
    "updateDateIncludingText": "2026-02-23T16:53:52Z"
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
          "date": "2025-11-21T14:02:35Z",
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
                "date": "2025-12-11T21:43:06Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:42:50Z",
                "name": "Markup by"
              },
              {
                "date": "2025-11-21T21:42:33Z",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6257ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6257\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Dunn of Florida introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo protect minors from harms associated with ephemeral messaging features and unsolicited direct contact on social media platforms by prohibiting certain ephemeral messaging features for minors and mandating the provision of parental direct messaging controls, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Messaging for Kids Act of 2025 or the SMK Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) App**\nThe term app means a software application or an electronic service that may be run or directed by a user on a computer, gaming device, mobile device, or any other general purpose computing device.\n**(2) App store**\nThe term app store means a publicly available website, software application, or other electronic service that distributes and facilitates the download onto a mobile device of an app from a third-party developer by a user of a computer, gaming device, mobile device, or any other general purpose computing device.\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Covered user**\nThe term covered user means a user of a social media platform if the provider of such social media platform\u2014\n**(A)**\nhas actual knowledge that the user is a minor; or\n**(B)**\nwould know that the user is a minor if not for willful disregard by the provider.\n**(5) Direct messaging feature**\n**(A) In general**\nThe term direct messaging feature means a function of a social media platform that enables a user to send a message, image, video, audio, or other communication directly to another user or a group of users of the social media platform.\n**(B) Exclusion**\nThe term direct messaging feature does not include a function of a social media platform that enables a user to post content on the social media platform to\u2014\n**(i)**\na public or semi-public profile; or\n**(ii)**\na feed accessible to a broader group of users.\n**(6) Ephemeral messaging feature**\n**(A) In general**\nThe term ephemeral messaging feature means a function of a social media platform that permanently deletes or renders inaccessible a message, image, video, audio, or other communication sent between users of the social media platform (such that neither the sender nor any recipient of such communication may readily retrieve or review the communication in the original form through the social media platform)\u2014\n**(i)**\nafter a predetermined period;\n**(ii)**\nonce viewed by such a recipient; or\n**(iii)**\nupon exiting the specific chat or messaging interface.\n**(B) Exceptions**\nThe term ephemeral messaging feature does not include\u2014\n**(i)**\na function of a social media platform that allows a user of the social media platform to manually delete a message, image, video, audio, or other communication sent by such user after the transmission of the communication (if such deletion does not automatically occur for each recipient of the communication or by the default design of such function); or\n**(ii)**\nstandard data volatility in transit or temporary caching not designed to make such a communication permanently inaccessible after viewing or a short, predetermined time.\n**(7) Minor**\nThe term minor means an individual under the age of 17 years.\n**(8) Parent**\nThe term parent means an individual who is an adult with the legal right to make a decision on behalf of a minor, including any of the following:\n**(A)**\nA natural parent.\n**(B)**\nAn adoptive parent.\n**(C)**\nA legal guardian.\n**(D)**\nAnother individual with legal custody of the minor.\n**(9) Parental direct messaging controls**\nThe term parental direct messaging controls means a set of tools or settings that a provider of a social media platform provides to a parent of a covered user of the social media platform that allows the parent to manage the use of a direct messaging feature by such covered user.\n**(10) Social media platform**\nThe term social media platform means a website or an app that enables a user of the website or app to do any of the following:\n**(A)**\nCreate and maintain a public or semi-public profile that serves as a central representation of the identity and activity of such user.\n**(B)**\nConnect with other users to form a network or community based on personal relationships, shared interests, or direct reciprocal interactions.\n**(C)**\nShare and consume user-generated content primarily within the context of such network or community, where the direct social interaction between the users in the network or community is a core and defining aspect of the dissemination of and engagement with such user-generated content.\n**(D)**\nEngage in persistent and private or semi-public interpersonal communication and interaction that is integral to the experience of such user on such website or app (rather than incidental to the consumption of content or the retrieval of information).\n**(11) Unapproved contact**\nThe term unapproved contact , with respect to a covered user for whom parental direct messaging controls have been activated, means a user of a social media platform with respect to whom the covered user may not use a direct messaging feature unless a parent of such covered user has provided verifiable parental consent under this Act.\n**(12) Verifiable parental consent**\nThe term verifiable parental consent \u2014\n**(A)**\nhas the meaning given that term in section 1302 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 ); and\n**(B)**\nincludes ongoing mechanisms for parents to activate and manage parental direct messaging controls provided under this Act.\n#### 3. Prohibition on ephemeral messaging features for minors\nA provider of a social media platform may not offer, provide, or enable any ephemeral messaging feature of such social media platform to any covered user of the social media platform.\n#### 4. Parental controls for direct messaging of minors\n##### (a) Requirement\nA provider of a social media platform that offers, provides, or enables any direct messaging feature of such social media platform to any covered user of the social media platform shall provide easily accessible and usable parental direct messaging controls to a parent of the covered user that the parent may activate and manage by providing verifiable parental consent.\n##### (b) Accessibility; usability; awareness\nThe parental direct messaging controls described in subsection (a) shall meet the following requirements:\n**(1)**\nBe clearly and conspicuously accessible to a parent of a covered user through\u2014\n**(A)**\nthe settings of a profile of the covered user; and\n**(B)**\nany parental portal or interface offered by the social media platform.\n**(2)**\nBe designed to be user-friendly with clear explanations of the manner in which the parental direct messaging controls operate.\n**(3)**\nBe prominently displayed by the social media platform to\u2014\n**(A)**\na user who indicates that the user is a parent; and\n**(B)**\na user who creates a profile for an individual who is likely to be a covered user.\n##### (c) Functionality of controls\nAs a default setting on a social media platform, the parental direct messaging controls described in subsection (a) shall allow a parent of a covered user of the social media platform to do any of the following (unless the parent adjusts the default setting with respect to any of the following by providing verifiable parental consent):\n**(1)**\nReceive a timely notification that\u2014\n**(A)**\nalerts the parent about a request from an unapproved contact who seeks to engage in direct messaging with the covered user; and\n**(B)**\nallows the parent to approve or deny the request before the unapproved contact and the covered user engage in any direct messaging.\n**(2)**\nView and manage a list of any contacts approved for engaging in direct messaging with the covered user.\n**(3)**\nBe informed if the covered user changes the age listed on a profile of the covered user (if any such change affects the applicability of such parental direct messaging controls).\n**(4)**\nDisable any direct messaging feature of a profile of the covered user.\n##### (d) Default settings for covered users under 13\n**(1) Requirement**\nA provider of a social media platform, as a default setting, shall disable any direct messaging feature of a profile of a covered user under the age of 13.\n**(2) Verifiable parental consent**\nA parent may provide to a provider of a social media platform verifiable parental consent to enable any direct messaging feature of a profile of a covered user described in paragraph (1).\n##### (e) No degradation of other features or services\nA provider of a social media platform may not degrade the functionality or availability of any other feature or service of the social media platform for a covered user of the social media platform based on the activation or management of parental direct messaging controls by a parent of the covered user under this section (except as necessary to implement the parental direct messaging controls).\n##### (f) No circumvention\nA provider of a social media platform shall take reasonable measures to prevent a covered user of the social media platform from easily circumventing parental direct messaging controls activated and managed by a parent of the covered user under this section.\n#### 5. App store warning for apps with direct messaging features\nA provider of an app store shall provide a clear and conspicuous warning to a parent of a covered user when the covered user attempts to download or purchase an app with respect to a social media platform that includes a direct messaging feature if the parent has required the provision of verifiable parental consent from the parent through a setting provided by such app store for any such download or purchase by the covered user.\n#### 6. Enforcement\n##### (a) Enforcement by Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a regulation under 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act, and any person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (b) Actions by States\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of this Act, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with this Act;\n**(C)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(D)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(2) Notice**\nBefore filing an action under this subsection, the attorney general, official, or agency of the State involved shall provide to the Commission a written notice of such action and a copy of the complaint for such action. If the attorney general, official, or agency determines that it is not feasible to provide the notice described in this paragraph before the filing of the action, the attorney general, official, or agency shall provide written notice of the action and a copy of the complaint to the Commission immediately upon the filing of the action.\n**(3) Authority of Commission**\n**(A) In general**\nOn receiving notice under paragraph (2) of an action under this subsection, the Commission shall have the right\u2014\n**(i)**\nto intervene in the action;\n**(ii)**\nupon so intervening, to be heard on all matters arising therein; and\n**(iii)**\nto file petitions for appeal.\n**(B) Limitation on State action while Federal action is pending**\nIf the Commission or the Attorney General of the United States has instituted a civil action for violation of this Act (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under this subsection during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of this Act alleged in such complaint.\n**(4) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this Act shall be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n#### 7. Rules of construction on encryption\n##### (a) No requirement To weaken or impair encryption\nNothing in this Act may be construed to require a provider of a social media platform or of any other interactive computer service or electronic communication service to\u2014\n**(1)**\ndecrypt or ensure an ability to decrypt an encrypted communication of a user;\n**(2)**\npreclude the use of any form of encryption, including end-to-end encryption, for any communication of a user; or\n**(3)**\ndesign, build, or implement any feature, function, software, hardware, or other capability for the purpose of weakening, undermining, circumventing, or overcoming any security control, including encryption, that is used to protect the privacy or security of any communication or data of a user.\n##### (b) Preservation of privacy and security\nThis Act shall be implemented in a manner that\u2014\n**(1)**\nrespects and protects the privacy of a user and the security of any communication of a user; and\n**(2)**\ndoes not require or encourage the systemic surveillance or monitoring of any encrypted communication of a user or the creation of any capability that would allow for such systemic surveillance or monitoring.\n##### (c) Implementation of Act\nNo requirement under this Act to restrict any feature for a covered user or to provide parental direct messaging controls for a direct messaging feature of a social media platform may be construed to override any protection for an encrypted communication described in this section and a provider of a social media platform shall adhere to any such requirement, to the maximum extent technically feasible, through means that do not compromise the integrity of strong encryption offered to any user of the social media platform.\n#### 8. Preemption\nNo State, or political subdivision of a State, may maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law that relates to the provisions of this Act.\n#### 9. Severability\nIf any provision of this Act or the application of this Act to any person or circumstance is held to be unconstitutional, the remaining provisions of this Act and the application of this Act to other persons or circumstances shall not be affected.\n#### 10. Effective date\n##### (a) In general\nExcept as provided in subsection (b), this Act shall take effect on the date that is 180 days after the date of the enactment of this Act.\n##### (b) Compliance deadlines\nNotwithstanding subsection (a)\u2014\n**(1)**\na provider of a social media platform shall have 1 year after the date of the enactment of this Act to comply with the provisions of section 4; and\n**(2)**\na provider of a social media platform shall have 18 months after the date of the enactment of this Act to comply with the provisions of section 5.",
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
            "updateDate": "2026-02-23T16:51:24Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-23T16:51:36Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-23T16:51:42Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-02-23T16:52:35Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2026-02-23T16:51:51Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-02-23T16:53:51Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-23T16:53:36Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-02-23T16:52:01Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-02-23T16:53:10Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-02-23T16:52:13Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-23T16:53:28Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-02-23T16:51:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-10T21:34:34Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6257ih.xml"
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
      "title": "SMK Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SMK Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Messaging for Kids Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect minors from harms associated with ephemeral messaging features and unsolicited direct contact on social media platforms by prohibiting certain ephemeral messaging features for minors and mandating the provision of parental direct messaging controls, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:16Z"
    }
  ]
}
```
