# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6333
- Title: Parents Over Platforms Act
- Congress: 119
- Bill type: HR
- Bill number: 6333
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2026-05-04T20:36:43Z
- Update date including text: 2026-05-04T20:36:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-01 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-01 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6333",
    "number": "6333",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "A000148",
        "district": "4",
        "firstName": "Jake",
        "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
        "lastName": "Auchincloss",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Parents Over Platforms Act",
    "type": "HR",
    "updateDate": "2026-05-04T20:36:43Z",
    "updateDateIncludingText": "2026-05-04T20:36:43Z"
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
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T17:01:25Z",
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
                "date": "2025-12-11T21:45:30Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:45:21Z",
                "name": "Markup by"
              },
              {
                "date": "2025-12-01T21:45:10Z",
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
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6333ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6333\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mr. Auchincloss (for himself and Mrs. Houchin ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo ensure responsible age assurance practices within the mobile ecosystem, particularly concerning the protection of minors, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Parents Over Platforms Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Definitions.\nTitle I\u2014APPLICATION DISTRIBUTOR AND DEVELOPER RESPONSIBILITIES\nSec.\u2002101.\u2002Age assurance.\nSec.\u2002102.\u2002Application distributor and developer obligations.\nTitle II\u2014LIABILITY AND ENFORCEMENT\nSec.\u2002201.\u2002Limitations on liability.\nSec.\u2002202.\u2002Enforcement.\nSec.\u2002203.\u2002Preemption.\nSec.\u2002204.\u2002Severability.\nSec.\u2002205.\u2002Effective date.\n#### 2. Definitions\nIn this Act:\n**(1) Adult**\nThe term Adult means an account holder who is or is estimated to be 18 years of age or older.\n**(2) Age category**\nThe term Age Category means categorization of an individual based on age or estimated age, including a description of the user as a Minor, Adult, or being within a given age range.\n**(3) Age signal**\nThe term Age Signal means a signal that indicates an account holder\u2019s Age Category, which the account holder or the account holder\u2019s parent has agreed to share.\n**(4) Application**\nThe term Application means a software program that is\u2014\n**(A)**\ndesigned to be run on a Connected Device, and to perform, or to help the user perform a specific task on the Connected Device; and\n**(B)**\ndistributed through an Application Distribution Provider.\nThe term does not include websites or internet Browser extensions, or software with a primary purpose of extending the functionality of an internet Browser.\n**(5) Application distributor**\nThe term Application Distributor means a software application that distributes Applications from Developers to users of a Connected Device. The term does not include internet Browsers.\n**(6) Application distribution provider**\nThe term Application Distribution Provider means an entity, company, or organization that owns, operates, or controls an Application Distributor.\n**(7) Connected device**\nThe term Connected Device means a smartphone, tablet, gaming console, or virtual reality device that enables users to connect to the internet and download software applications.\n**(8) Covered application**\nThe term Covered Application means an Application that is not an Application Distributor and that a Developer provides, whether legally required or not, a different experience for Adults than for Minors or an experience that is intended only for Adults. This includes, but is not limited to, Developers that provide different account types, content, or features or engage in different advertising or data practices depending on a user\u2019s age. The term does not include internet Browsers or Online Search Engines.\n**(9) Developer**\nThe term Developer means any person, entity, company, or organization that creates, owns, or controls an Application.\n**(10) Minor**\nThe term Minor means an account holder who is or is estimated to be under the age of 18.\n**(11) Covered website**\nThe term Covered Website means a website that provides a URL-accessible or web version of a Covered Application. The term does not include internet Browsers or Online Search Engines.\n**(12) Personalized advertising**\nPersonalized Advertising means displaying advertisements to an account holder where the advertisement is selected based on personal data obtained from that account holder\u2019s activities over time and across non-affiliated websites or online applications to predict such account holder\u2019s preferences or interests.\nPersonalized Advertising\n**(1)**\nAdvertising based on an account holder\u2019s activities within a Developer\u2019s own Application or Applications;\n**(2)**\nAdvertising based on the context of an account holder\u2019s current interaction with an Application;\n**(3)**\nAdvertising directed to an account holder in response to the account holder\u2019s direct request for information or feedback; or\n**(4)**\nThe processing of personal data solely for measuring or reporting advertising performance, reach, or frequency.\nI\nAPPLICATION DISTRIBUTOR AND DEVELOPER RESPONSIBILITIES\n#### 101. Age assurance\n##### (a) Responsibilities of application distribution providers\nAn Application Distribution Provider\u2014\n**(1)**\nshall ask account holders to declare their age when creating an account with the Application Distribution Provider;\n**(2)**\nmay use commercially reasonable efforts to obtain the Age Category of an account holder with a reasonable level of certainty;\n**(3)**\nmay provide account holders with a mechanism to obtain their Age Category and the ability to request an update if they believe their Age Category is incorrect; and\n**(4)**\nshall provide Developers of Covered Applications the technical ability to call an Age Signal where the account holder or the account holder\u2019s parent has agreed to such sharing.\n##### (b) Rule of construction\n**(1)**\nNothing in this section shall be construed to preclude an Application Distribution Provider from using multiple commercially reasonable methods to obtain, estimate, or provide the Age Category of an account holder.\n**(2)**\nNothing in this section shall be construed to restrict an Application Distribution Provider\u2019s ability to satisfy this section by obtaining a Minor account holder\u2019s age from the Minor\u2019s parent.\n#### 102. Application distributor and developer obligations\n##### (a) Application distribution providers\nAn Application Distribution Provider\u2014\n**(1)**\nshall provide the account holder\u2019s parent with the ability to prevent account holders who are not Adults from acquiring or using the Developer\u2019s Covered Application from the Application Distributor;\n**(2)**\nshall provide the Developer of a Covered Application with the ability to prevent account holders who are not Adults from acquiring or using the Developer\u2019s Covered Application from the Application Distributor.\n**(A)**\nNothing in this section shall prevent Application Distribution Providers from creating a user interface or centralized page for account holder\u2019s parents to block categories by age rating of Covered Applications based on the content and features of the Covered Application.\n**(2)**\nshall provide the capability to Developers to provide information regarding their relevant parental controls for a Covered Application through a centralized product page or user interface, hosted by the Application Distribution Provider, that provides relevant information about a Covered Application;\n**(3)**\nshall comply with the obligations set out in subsection (b) for its own Covered Applications for which the Application Distribution Provider is also the Developer; and\n**(4)**\nshall not use data collected from third-party Covered Applications in the course of compliance with this section to give the Application Distribution Provider preference relative to those of third parties, or to otherwise use such data in an anticompetitive manner.\n##### (b) Developers of covered applications\nA Developer of a Covered Application\u2014\n**(1)**\nshall report to the Application Distribution Provider whether their Applications provide a different experience for Adults than for users who are not Adults or is intended only for Adults;\n**(2)**\nshall provide information regarding privacy and online safety settings to help parents support Minors using their Covered Applications, unless their Application is intended only for Adults and blocks Minors;\n**(3)**\nshall use commercially reasonable efforts to determine whether a user is an Adult or a Minor with a reasonable level of certainty;\n**(A)**\nFor the purposes of this section, an Age Signal provided by an Application Distribution Provider shall be considered a commercially reasonable effort, unless a Developer\u2019s Application is intended only for Adults and blocks Minors and is required by law to restrict access to Adults, in which case\u2014\n**(i)**\nan Age Signal provided by an Application Distribution Provider indicating a user is a Minor shall be sufficient basis to block access; and\n**(ii)**\nan Age Signal provided by an Application Distribution Provider indicating a user is an Adult shall not, by itself, satisfy the requirement to determine whether a user is an Adult with a reasonable level of certainty, including for purposes of other laws that require access restrictions based on age.\n**(4)**\nshall make a reasonable effort to ensure that users who are Minors cannot engage in any activity that has been restricted by the developer for Adults only;\n**(5)**\nshall obtain consent prior to permitting Minor account holders from accessing a Covered Application or portion thereof that the Developer has designated as unsuitable for use by Minors without parental guidance or supervision, or from accessing content that is age-gated by law;\n**(6)**\nshall not deliver personalized advertising to Minors; and\n**(7)**\nif the Developer determines that it is a Covered Application, and chooses to call an Age Signal facilitated by an Application Distribution Provider to satisfy the requirements of this section, the Developer\u2014\n**(A)**\nshall request the minimum amount of information needed for purposes of compliance with this Act;\n**(B)**\nmay not willfully disregard any information regarding an individual\u2019s age or Age Category that is otherwise available to the Developer;\n**(C)**\nmay not share the information obtained from the Age Signal with third parties, except for a service provider, but only if necessary for such service provider to implement safety measures or privacy protections for minors or otherwise required to do so by law; and\n**(D)**\nmay not use the Age Signal for any purpose beyond that intended by this Act, including but not limited to using the Age Signal to back into or attempt to back into a user\u2019s date of birth.\n**(8)**\nif the Developer uses a method other than an Age Signal provided by an Application Distribution Provider to satisfy the requirements of this section, the Developer\u2014\n**(A)**\nshall request the minimum amount of information needed for purposes of compliance with this Act;\n**(B)**\nmay not willfully disregard any information regarding an individual\u2019s age or Age Category that is available to the Developer;\n**(C)**\nmay not share the information obtained in the course of complying with this section with third parties, except for a service provider, but only if necessary for such service provider to implement safety measures or privacy protections for minors or otherwise required to do so by law; and\n**(D)**\nmay not use age data for any purpose beyond that intended by this Act, including but not limited to using age data to back into or attempt to back into a user\u2019s date of birth.\n##### (c) Rule of construction\nIf the Developer and an Application Distribution Provider are controlled by the same entity, the Developer may rely on age determinations made by that entity.\n##### (d) Rule of Construction\nDevelopers of Covered websites shall have the same requirements as Developers of Covered Applications in this Act and may carry over to Covered websites an Age Signal received from an Application Distribution Provider to fulfill such requirements.\nII\nLIABILITY AND ENFORCEMENT\n#### 201. Limitations on liability\n##### (a) Application distribution providers and operating system providers\nAn Application Distribution Provider or Operating System Provider that makes a good faith effort to comply with the obligations of this Act, taking into consideration available technology, shall not be liable under any provision of this Act, or otherwise liable for its actions taken in attempt to comply with this Act, including but not limited to the following with regard to facilitation of the provision of an Age Signal:\n**(1)**\nAny erroneous Age Signal.\n**(2)**\nAny conduct by a Developer of a Covered Application that receives any Age Signal.\n**(3)**\nFailing to provide an Age Signal due to any reasonable technical limitations or outages that prevent the provision of the Age Signal upon request.\n**(4)**\nNot providing the Age Signal to Developers that do not adhere to reasonable safety standards and Application Distributor policies.\n##### (b) Developers\nA Developer of a Covered Application\u2014\n**(1)**\nas between the Developer of a Covered Application and the Application Distribution Provider, is solely liable for correctly identifying whether their Applications are Covered Applications under this Act. No Application Distributor is required to proactively identify Covered Applications, and an Application Distributor will not be held liable in cases where a Developer provides inaccurate information about its Applications; and\n**(2)**\nshall not be liable for an erroneous Age Signal provided by an Application Distribution Provider, if the Developer makes a reasonable effort, taking into consideration available technology, to properly use the Age Signal and carry out commercially reasonable methods to obtain or estimate the age of an account holder.\n#### 202. Enforcement\n##### (a) Unfair or deceptive acts or practices\nA violation of this Act or a regulation promulgated thereunder shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the commission\n**(1) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person who violates this Act or a regulation promulgated thereunder shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n#### 203. Preemption\nNo State or political subdivision of a State may maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of any State, or political subdivision of a State, related to the provisions of this Act.\n#### 204. Severability\nIf any provision of this Act or the application of any provision to any person or circumstance is held invalid by a final decision of a court of competent jurisdiction, the remainder of this Act shall be given effect without the invalid provision or application.\n#### 205. Effective date\nThis Act shall take effect not later than 24 months after the date of its enactment.",
      "versionDate": "2025-12-01",
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
        "actionDate": "2026-04-20",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "4349",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Parents Over Platforms Act",
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
            "name": "Child safety and welfare",
            "updateDate": "2026-02-23T17:07:45Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-02-23T17:07:45Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-02-23T17:07:45Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2026-02-23T17:08:04Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-02-23T17:07:53Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-23T17:07:45Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-02-23T17:07:45Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-02-23T17:08:28Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-23T17:07:45Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-02-23T17:08:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-09T22:21:52Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6333ih.xml"
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
      "title": "Parents Over Platforms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parents Over Platforms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure responsible age assurance practices within the mobile ecosystem, particularly concerning the protection of minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:18Z"
    }
  ]
}
```
