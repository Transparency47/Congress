# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6273?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6273
- Title: SPY Kids Act
- Congress: 119
- Bill type: HR
- Bill number: 6273
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-01-12T18:08:53Z
- Update date including text: 2026-01-12T18:08:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-21 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee in the Nature of a Substitute (Amended) by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-21 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee in the Nature of a Substitute (Amended) by Voice Vote.
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6273",
    "number": "6273",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "SPY Kids Act",
    "type": "HR",
    "updateDate": "2026-01-12T18:08:53Z",
    "updateDateIncludingText": "2026-01-12T18:08:53Z"
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
      "text": "Forwarded by Subcommittee to Full Committee in the Nature of a Substitute (Amended) by Voice Vote.",
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
          "date": "2025-11-21T14:00:20Z",
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
                "date": "2025-12-11T21:37:47Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:37:36Z",
                "name": "Markup by"
              },
              {
                "date": "2025-11-21T21:37:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6273ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6273\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mrs. Miller-Meeks introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit market or product-focused research on children and minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Profiling Youth and Kids Act or the SPY Kids Act .\n#### 2. Definitions\nIn this Act:\n**(1) Child**\nThe term child means an individual who is under the age of 13.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered platform**\nThe term covered platform means a platform that is a website, software, application, or electronic service connected to the internet that\u2014\n**(A)**\nis publicly available for use by consumers;\n**(B)**\nenables the creation of a username or user identifier\u2014\n**(i)**\nthat is searchable on the platform; and\n**(ii)**\nthat can be followed by or is otherwise accessible to other users of the platform;\n**(C)**\nas the predominant purpose of the platform, facilitates the creation and access to user-generated content through text, images, video, audio, or any other interactive medium;\n**(D)**\nuses a design feature to promote user engagement on the platform; and\n**(E)**\nuses the personal information of the user to advertise, market, or make content recommendations.\n**(4) Design feature**\nThe term design feature \u2014\n**(A)**\nmeans any feature or component of a covered platform that encourages or increases the frequency, time spent, or activity of a minor on the covered platform; and\n**(B)**\nincludes any of the following:\n**(i)**\nInfinite scrolling or auto play.\n**(ii)**\nRewards or incentives based on the frequency, time spent, or activity of a minor on the covered platform.\n**(iii)**\nNotifications and push alerts.\n**(iv)**\nBadges or other visual award symbols based on the frequency, time spent, or activity of a minor on the covered platform.\n**(v)**\nAppearance altering filters.\n**(5) Know; knows**\nThe term know or knows means to have actual knowledge or to have acted in willful disregard.\n**(6) Parent**\nThe term parent means the legal guardian of a minor.\n**(7) Personal information**\nThe term personal information has the meaning given that term in section 1302 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 ).\n**(8) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n**(9) Teen**\nThe term teen means an individual who is over the age of 13 and under the age of 17.\n**(10) User**\nThe term user means, with respect to a covered platform, an individual who registers an account or creates a profile on the covered platform.\n**(11) Verifiable parental consent**\nThe term verifiable parental consent has the meaning given that term in section 1302 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 )).\n#### 3. Market research\n##### (a) Prohibition of research on children\nA covered platform may not, in the case of a user or visitor that the covered platform knows is a child, conduct market or product-focused research on such child.\n##### (b) Limitation on research on teens\nA covered platform may not, in the case of a user or visitor that the online platform knows is a teen, conduct market or product-focused research on such teen, unless the covered platform obtains verifiable parental consent before conducting such research on such teen.\n##### (c) Rule of construction\nNothing in this Act may be construed to limit the processing of personal information solely for measuring or reporting advertising or content performance, reach, or frequency, including through an independent measurement.\n#### 4. Enforcement\n##### (a) Enforcement by Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act. Any person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (b) Actions by States\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of this Act, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with this Act;\n**(C)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(D)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(2) Notice**\nBefore filing an action under this subsection, the attorney general, official, or agency of the State involved shall provide to the Commission a written notice of such action and a copy of the complaint for such action. If the attorney general, official, or agency determines that it is not feasible to provide the notice described in this paragraph before the filing of the action, the attorney general, official, or agency shall provide written notice of the action and a copy of the complaint to the Commission immediately upon the filing of the action.\n**(3) Authority of Commission**\n**(A) In general**\nOn receiving notice under paragraph (2) of an action under this subsection, the Commission shall have the right\u2014\n**(i)**\nto intervene in the action;\n**(ii)**\nupon so intervening, to be heard on all matters arising therein; and\n**(iii)**\nto file petitions for appeal.\n**(B) Limitation on State action while Federal action is pending**\nIf the Commission or the Attorney General of the United States has instituted a civil action for violation of this Act (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under this subsection during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of this Act alleged in such complaint.\n**(4) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this Act shall be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n#### 5. Rules of construction\nNothing in this Act may be construed to\u2014\n**(1)**\nlimit or impair the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 et seq. ) or any rule or regulation promulgated under such Act; or\n**(2)**\nauthorize any action in conflict with section 18(h) of the Federal Trade Commission Act ( 15 U.S.C. 57a(h) ).\n#### 6. Relationship to State laws\nNo State or political subdivision of a State may prescribe, maintain, or enforce any law, rule, regulation, requirement, standard, or other provision having the force and effect of law, if such law, rule, regulation, requirement, standard, or other provision relates to the provisions of this Act.\n#### 7. Effective date\nExcept as otherwise provided in this Act, this Act shall take effect on the date that is 90 days after the date of the enactment of this Act.",
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
            "updateDate": "2026-01-12T18:05:04Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-01-12T18:08:53Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-01-12T18:04:51Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-01-12T18:08:00Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-01-12T18:06:03Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-01-12T18:05:13Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2026-01-12T18:08:19Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-01-12T18:05:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-09T22:18:38Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6273ih.xml"
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
      "title": "SPY Kids Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-22T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SPY Kids Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-22T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Profiling Youth and Kids Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-22T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit market or product-focused research on children and minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-22T09:18:27Z"
    }
  ]
}
```
