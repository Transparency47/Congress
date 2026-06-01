# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6265
- Title: Safer GAMING Act
- Congress: 119
- Bill type: HR
- Bill number: 6265
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-02-23T17:22:58Z
- Update date including text: 2026-02-23T17:22:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6265",
    "number": "6265",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Safer GAMING Act",
    "type": "HR",
    "updateDate": "2026-02-23T17:22:58Z",
    "updateDateIncludingText": "2026-02-23T17:22:58Z"
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
          "date": "2025-11-21T14:00:30Z",
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
                "date": "2025-12-11T21:36:34Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:36:11Z",
                "name": "Markup by"
              },
              {
                "date": "2025-11-21T21:35:54Z",
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
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "NJ"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6265ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6265\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Kean introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require online video game providers to provide certain safeguards for minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safer Guarding of Adolescents from Malicious Interactions on Network Games Act or the Safer GAMING Act .\n#### 2. Safeguard requirements for online video game providers\n##### (a) Definitions\nIn this section:\n**(1) Adult user**\nThe term adult user means a user of an interactive online video game if the provider of such game knows that such user is not a minor.\n**(2) Covered user**\nThe term covered user means a user of an interactive online video game if the provider of such game knows that such user is a minor.\n**(3) Interactive online video game**\nThe term interactive online video game means a video game that\u2014\n**(A)**\nconnects to the internet; and\n**(B)**\nallows a user of such video game to communicate with other users of such video game.\n**(4) Know; knows**\nThe term know or knows means to have actual knowledge or to have acted in willful disregard.\n**(5) Minor**\nThe term minor means an individual under the age of 18 years.\n**(6) Online video game provider**\nThe term online video game provider means a person that provides an interactive online video game directly to a consumer for the use of the consumer, including through a website, mobile application, or other online means.\n**(7) Parent**\nThe term parent means the legal guardian of a minor.\n**(8) Video game**\nThe term video game means a device or software program that\u2014\n**(A)**\nreceives and stores data or instructions generated by the user of such object, device, or software program; and\n**(B)**\nprocesses such data or instructions to create an interactive game for such user to play or view on a computer, gaming system, console, mobile device, or other technological means.\n##### (b) Safeguards required\n**(1) In general**\nAn online video game provider shall provide safeguards to the parent of a covered user of an interactive online video game of such provider that allow the parent to limit communication between such covered user and any other user (including any adult user) of such online video game.\n**(2) Features**\nAn online video game provider required to provide safeguards under paragraph (1) shall ensure the following:\n**(A)**\nThe safeguards\u2014\n**(i)**\nare accessible and easy-to use;\n**(ii)**\nare enabled by default on the account of a covered user of the interactive online video game of such provider; and\n**(iii)**\ncan be disabled only by the parent of the covered user.\n**(B)**\nThe most protective level of control offered to a user with respect to privacy and safety settings\u2014\n**(i)**\nincludes such safeguards by default; and\n**(ii)**\nwith respect to a covered user, can be disabled only by the parent of the covered user.\n**(3) Rule of construction**\nNothing in this section may be construed to prohibit an online video game provider from providing the parent of a covered user of an interactive online video game of such provider with the ability to limit or allow communication between the covered user and multiple other users.\n**(4) Effective date**\nThis subsection shall take effect on the date that is 1 year after the date of the enactment of this Act.\n##### (c) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (b) shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Federal Trade Commission shall enforce subsection (b) in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section. Any person who violates subsection (b) shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(3) Authority preserved**\nNothing in this section may be construed to limit the authority of the Federal Trade Commission under any other provision of law.\n##### (d) Actions by States\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of subsection (b), the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with such subsection;\n**(C)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(D)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(2) Notice**\nBefore filing an action under this subsection, the attorney general, official, or agency of the State involved shall provide to the Federal Trade Commission a written notice of such action and a copy of the complaint for such action. If the attorney general, official, or agency determines that it is not feasible to provide the notice described in this paragraph before the filing of the action, the attorney general, official, or agency shall provide written notice of the action and a copy of the complaint to the Federal Trade Commission immediately upon the filing of the action.\n**(3) Authority of Federal Trade Commission**\n**(A) In general**\nOn receiving notice under paragraph (2) of an action under this subsection, the Federal Trade Commission shall have the right\u2014\n**(i)**\nto intervene in the action; and\n**(ii)**\nupon so intervening\u2014\n**(I)**\nto be heard on all matters arising therein; and\n**(II)**\nto file petitions for appeal.\n**(B) Limitation on State action while Federal action is pending**\nIf the Federal Trade Commission or the Attorney General of the United States has instituted a civil action for violation of subsection (b) (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under this subsection during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of such subsection alleged in such complaint.\n**(4) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this Act shall be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n##### (e) Preemption\nNo State or political subdivision of a State may prescribe, maintain, or enforce any law, rule, regulation, requirement, standard, or other provision having the force and effect of law, if such law, rule, regulation, requirement, standard, or other provision relates to the provisions of this Act.",
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
            "updateDate": "2026-02-23T17:21:56Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-23T17:15:50Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-02-23T17:16:22Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-02-23T17:16:02Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-02-23T17:22:44Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-02-23T17:22:58Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-02-23T17:15:34Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-02-23T17:22:16Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-02-23T17:22:05Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-23T17:22:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-10T21:35:18Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6265ih.xml"
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
      "title": "Safer GAMING Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safer GAMING Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safer Guarding of Adolescents from Malicious Interactions on Network Games Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require online video game providers to provide certain safeguards for minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:17Z"
    }
  ]
}
```
