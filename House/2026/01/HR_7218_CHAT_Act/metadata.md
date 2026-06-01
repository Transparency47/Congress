# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7218?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7218
- Title: CHAT Act
- Congress: 119
- Bill type: HR
- Bill number: 7218
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-02-13T16:35:34Z
- Update date including text: 2026-02-13T16:35:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7218",
    "number": "7218",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "CHAT Act",
    "type": "HR",
    "updateDate": "2026-02-13T16:35:34Z",
    "updateDateIncludingText": "2026-02-13T16:35:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:04:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7218ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7218\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mr. Lawler introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require artificial intelligence chatbots to implement age verification measures and establish certain protections for minor users, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Children Harmed by AI Technology Act or the CHAT Act .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Companion AI chatbot**\nThe term companion AI chatbot \u2014\n**(A)**\nmeans any software-based artificial intelligence system or program that exists for the primary purpose of simulating emotional interaction, friendship, companionship, or therapeutic communication with a user; and\n**(B)**\ndoes not include the following:\n**(i)**\nA bot that is used only for customer service, a business operational purpose, productivity and analysis related to source information, internal research, or technical assistance.\n**(ii)**\nA bot that is a feature of a video game and is limited to replies related to the video game that cannot discuss topics related to mental health, self-harm, sexually explicit conduct, or maintain a dialogue on other topics unrelated to the video game.\n**(iii)**\nA stand-alone consumer electronic device that functions as a speaker and voice command interface, acts as a voice-activated virtual assistant, and does not sustain a relationship across multiple interactions or generate outputs that are likely to elicit emotional responses in the user.\n**(3) Covered entity**\nThe term covered entity means any person that owns, operates, or otherwise makes available a companion AI chatbot to individuals in the United States.\n**(4) Minor**\nThe term minor means any individual that has not attained 18 years of age.\n**(5) Popup**\nThe term popup means a visible notification on the screen of a user that can be resolved if interacted with by the user.\n**(6) Sexually explicit communication**\nThe term sexually explicit communication includes any content, conversation, or material that describes, depicts, or encourages sexually explicit conduct, as defined in paragraph (2)(B) of section 2256 of title 18, United States Code.\n**(7) Suicidal ideation**\nThe term suicidal ideation means, with respect to an interaction between a minor and a companion AI chatbot, any dialogue in which such minor expresses thoughts of self-harm or suicide.\n#### 3. Covered entity obligations\n##### (a) Creation of user accounts\nA covered entity shall require each individual accessing a companion AI chatbot to make a user account in order to use or otherwise interact with such chatbot.\n##### (b) Age verification\n**(1) Age verification of existing accounts**\nWith respect to each user account of a companion AI chatbot that exists as of the date described in section 7, a covered entity shall\u2014\n**(A)**\non such date, freeze any such account;\n**(B)**\nin order to restore the functionality of such account, require that the user provide age information that is verifiable using a commercially available method or process that is reasonably designed to ensure accuracy; and\n**(C)**\nusing such age information, classify each user as a minor or an adult.\n**(2) Age verification of new accounts**\nAt the time an individual creates a new user account to use or interact with a companion AI chatbot, a covered entity shall\u2014\n**(A)**\nrequest age information from the individual; and\n**(B)**\nverify the individual\u2019s age using a commercially available method or process that is reasonably designed to ensure accuracy.\n##### (c) Minor account protections\nIf the age verification process described in subsection (b) determines that a user is a minor, a covered entity shall\u2014\n**(1)**\nrequire the account of such user to be affiliated with a parental account, which such covered entity has verified using a commercially available method or process that is reasonably designed to ensure accuracy;\n**(2)**\nobtain verifiable parental consent from the holder of the account before allowing a minor to access and use the companion AI chatbot;\n**(3)**\nimmediately inform the holder of the parental account of any interaction involving suicidal ideation; and\n**(4)**\nblock the minor's access to any companion AI chatbot that engages in sexually explicit communication.\n##### (d) Confidentiality of age verification data\nA covered entity shall protect the confidentiality of age information provided by a user for age verification by limiting the collection, processing, use, and storage of such information to what is strictly necessary to verify a user\u2019s age, obtain verifiable parental consent, or maintain compliance records.\n##### (e) Monitoring for suicidal ideation\nA covered entity shall monitor companion AI chatbot interactions for suicidal ideation and, in response to any such interaction, provide to the user and the parental account affiliated with such user appropriate resources by presenting contact information for the National Suicide Prevention Lifeline.\n##### (f) Notification of artificial chatbot\nAt the beginning of any interaction between a user and a companion AI chatbot, and not less frequently than every 60 minutes during such interaction thereafter, a covered entity shall display to such user a clear popup that notifies the user that they are not engaging in dialogue with a human counterpart.\n#### 4. Compliance\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Commission shall issue guidance to assist covered entities in complying with the requirements of this Act.\n##### (b) Limitation\nIn any enforcement action brought pursuant to this Act, the Commission shall allege a specific violation of a provision of this Act. The Commission may not base an enforcement action on, or execute a consent order based on, practices that are alleged to be inconsistent with any guidance issued by the Commission with respect to this Act, unless the practices are alleged to violate a provision of this Act. A person may use such guidance as evidence of compliance with this Act.\n#### 5. Enforcement\n##### (a) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act or a regulation promulgated under this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates this Act or a regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Enforcement by States\n**(1) In general**\n**(A) Civil actions**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of that State has been or is threatened or adversely affected by the engagement of any person in a practice that violates this Act, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in a district court of the United States of appropriate jurisdiction to\u2014\n**(i)**\nenjoin that practice;\n**(ii)**\nenforce compliance with the requirements of this Act;\n**(iii)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(iv)**\nobtain such other relief as the court may consider to be appropriate.\n**(B) Notice**\n**(i) In general**\nBefore filing an action under subparagraph (A), the attorney general of the State involved shall provide to the Commission\u2014\n**(I)**\na written notice of that action; and\n**(II)**\na copy of the complaint for that action.\n**(ii) Exemption**\n**(I) In general**\nClause (i) shall not apply with respect to the filing of an action by an attorney general of a State under this subsection if the attorney general determines that it is not feasible to provide the notice described in that clause before the filing of the action.\n**(II) Notification**\nIn an action described in subclause (I), the attorney general of a State shall provide notice and a copy of the complaint to the Commission at the same time as the attorney general files the action.\n**(2) Intervention**\n**(A) In general**\nOn receiving notice under paragraph (1)(B), the Commission shall have the right to intervene in the action that is the subject of the notice.\n**(B) Effect of intervention**\nIf the Commission intervenes in an action under paragraph (1), it shall have the right\u2014\n**(i)**\nto remove the action to the appropriate district court of the United States;\n**(ii)**\nto be heard with respect to any matter that arises in that action; and\n**(iii)**\nto file a petition for appeal.\n**(3) Construction**\nFor purposes of bringing any civil action under paragraph (1), nothing in this Act shall be construed to prevent an attorney general of a State from exercising the powers conferred on the attorney general by the laws of that State to\u2014\n**(A)**\nconduct investigations;\n**(B)**\nadminister oaths or affirmations; or\n**(C)**\ncompel the attendance of witnesses or the production of documentary and other evidence.\n**(4) Actions by the Commission**\nIn any case in which an action is instituted by or on behalf of the Commission for a violation of this Act, no State may, during the pendency of that action, institute an action under paragraph (1) against any defendant named in the complaint in that action for such violation.\n**(5) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\na State court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n#### 6. Safe Harbor\nA covered entity is deemed not liable for a violation of this Act if the covered entity demonstrates it has\u2014\n**(1)**\nrelied in good faith on age information provided by a user of the companion AI chatbot for purposes of verifying the age of such user;\n**(2)**\ncomplied with the guidance described in section 4; and\n**(3)**\nreasonably conformed to widely accepted industry standards or best practices, or to standards or best practices identified by the Commission, for age verification and applied those standards or best practices consistently and in good faith.\n#### 7. Effective Date\nThis Act shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2026-01-22",
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
        "actionDate": "2025-09-04",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2714",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CHAT Act",
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
        "name": "Commerce",
        "updateDate": "2026-02-13T16:35:34Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7218ih.xml"
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
      "title": "CHAT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHAT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Children Harmed by AI Technology Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require artificial intelligence chatbots to implement age verification measures and establish certain protections for minor users, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:39Z"
    }
  ]
}
```
