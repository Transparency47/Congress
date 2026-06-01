# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4349?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4349
- Title: Parents Over Platforms Act
- Congress: 119
- Bill type: S
- Bill number: 4349
- Origin chamber: Senate
- Introduced date: 2026-04-20
- Update date: 2026-05-04T20:36:51Z
- Update date including text: 2026-05-04T20:36:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in Senate
- 2026-04-20 - IntroReferral: Introduced in Senate
- 2026-04-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-04-20: Introduced in Senate

## Actions

- 2026-04-20 - IntroReferral: Introduced in Senate
- 2026-04-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4349",
    "number": "4349",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Parents Over Platforms Act",
    "type": "S",
    "updateDate": "2026-05-04T20:36:51Z",
    "updateDateIncludingText": "2026-05-04T20:36:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-04-20T22:26:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4349is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4349\nIN THE SENATE OF THE UNITED STATES\nApril 20, 2026 Mr. Moran (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo ensure responsible age assurance practices within the mobile ecosystem, particularly concerning the protection of minors, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Parents Over Platforms Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014APPLICATION DISTRIBUTION PROVIDER AND DEVELOPER RESPONSIBILITIES\nSec. 101. Age assurance.\nSec. 102. Application distributor and developer obligations.\nTITLE II\u2014LIABILITY AND ENFORCEMENT\nSec. 201. Limitations on liability.\nSec. 202. Enforcement.\nSec. 203. Preemption.\nSec. 204. Severability.\nSec. 205. Effective date.\n#### 2. Definitions\nIn this Act:\n**(1) Adult**\nThe term adult means an account holder who is or is estimated to be 18 years of age or older.\n**(2) Age category**\nThe term age category means categorization of an individual based on age or estimated age, including a description of the user as a minor, an adult, or as being within a given age range.\n**(3) Age signal**\nThe term age signal means a signal that indicates an account holder\u2019s age category, which the account holder or the account holder\u2019s parent has agreed to share.\n**(4) Application**\n**(A) In general**\nThe term application means a software program that is\u2014\n**(i)**\ndesigned to be run on a connected device, and to perform, or to help the user perform, a specific task on the connected device; and\n**(ii)**\ndistributed through an application distribution provider.\n**(B) Exclusions**\nThe term application does not include\u2014\n**(i)**\nwebsites or internet browser extensions; or\n**(ii)**\nsoftware with a primary purpose of extending the functionality of an internet browser.\n**(5) Application distributor**\nThe term application distributor \u2014\n**(A)**\nmeans a software application that distributes applications from developers to users of a connected device; and\n**(B)**\ndoes not include an internet browser.\n**(6) Application distribution provider**\nThe term application distribution provider means an entity, company, or organization that owns, operates, or controls an application distributor.\n**(7) Commission**\nThe term Commission means the Federal Trade Commission.\n**(8) Connected device**\nThe term connected device means a smartphone, tablet, gaming console, or virtual reality device that enables users to connect to the internet and download applications.\n**(9) Covered application**\n**(A) In general**\nThe term covered application \u2014\n**(i)**\nmeans an application\u2014\n**(I)**\nthat is not an application distributor; and\n**(II)**\nfor which a developer provides, whether legally required or not\u2014\n**(aa)**\na different experience for adults than for minors; or\n**(bb)**\nan experience that is intended only for adults; and\n**(ii)**\nincludes an application for which a developer provides different account types, content, or features, or engages in different advertising or data practices, depending on a user\u2019s age.\n**(B) Exclusion**\nThe term covered application does not include an internet browser or online search engine.\n**(10) Covered website**\n**(A) In general**\nThe term covered website means a website that provides a URL-accessible or web version of a covered application.\n**(B) Exclusion**\nThe term covered website does not include an internet browser or online search engine.\n**(11) Developer**\nThe term developer means any person, entity, company, or organization that creates, owns, or controls an application.\n**(12) Minor**\nThe term minor means an account holder who is or is estimated to be under the age of 18.\n**(13) Personalized advertising**\n**(A) In general**\nThe term personalized advertising means the displaying of an advertisement to an account holder that is selected based on personal data obtained from the account holder\u2019s activities over time and across non-affiliated websites or online applications to predict such account holder\u2019s preferences or interests.\n**(B) Exclusion**\nThe term personalized advertising does not include\u2014\n**(i)**\nadvertising based on an account holder\u2019s activities within a developer\u2019s own application or applications;\n**(ii)**\nadvertising based on the context of an account holder\u2019s current interaction with an application;\n**(iii)**\nadvertising directed to an account holder in response to the account holder\u2019s direct request for information or feedback; or\n**(iv)**\nthe processing of personal data solely for measuring or reporting advertising performance, reach, or frequency.\nI\nAPPLICATION DISTRIBUTION PROVIDER AND DEVELOPER RESPONSIBILITIES\n#### 101. Age assurance\n##### (a) Responsibilities of application distribution providers\nAn application distribution provider\u2014\n**(1)**\nshall ask account holders to declare their age when creating an account with the application distribution provider;\n**(2)**\nmay use commercially reasonable efforts to obtain the age category of an account holder with a reasonable level of certainty;\n**(3)**\nmay provide account holders with a mechanism to obtain their age category and the ability to request an update if they believe their age category is incorrect; and\n**(4)**\nshall provide developers of covered applications the technical ability to access an age signal where the account holder or the account holder\u2019s parent has agreed to share such age signal.\n##### (b) Rules of construction\nNothing in this section shall be construed to\u2014\n**(1)**\npreclude an application distribution provider from using multiple commercially reasonable methods to obtain, estimate, or provide the age category of an account holder; or\n**(2)**\nrestrict an application distribution provider\u2019s ability to satisfy the requirements of this section by obtaining a minor account holder\u2019s age from the minor\u2019s parent.\n#### 102. Application distributor and developer obligations\n##### (a) Application distribution providers\n**(1) Obligations**\nAn application distribution provider shall do the following:\n**(A)**\nProvide a minor account holder\u2019s parent with the ability to prevent the minor from acquiring or using a developer\u2019s covered application from the application distributor.\n**(B)**\nProvide developers with the ability to provide information regarding their relevant parental controls for a covered application through a centralized product page or user interface, hosted by the application distribution provider, that provides relevant information about a covered application.\n**(C)**\nComply with the obligations described in subsection (b) with respect to any covered applications for which the application distribution provider is also the developer.\n**(D)**\nNot use data collected from third-party covered applications in the course of compliance with this section to give the application distribution provider's own applications preference relative to those of third parties, or to otherwise use such data in an anti-competitive manner.\n**(2) Rule of construction**\nNothing in this section shall be construed to prevent an application distribution provider from creating a user interface or centralized page for minor account holders' parents to block categories by age rating of covered applications based on the content and features of the covered application.\n##### (b) Developers of covered applications\n**(1) In general**\nA developer of a covered application shall do the following:\n**(A)**\nReport to the application distribution provider whether the application of the developer provides a different experience for adult users than for minor users or is intended only for adults.\n**(B)**\nWith respect to any covered application that is authorized to be used by a minor, provide information regarding privacy and online safety settings to help parents support minors using such application.\n**(C)**\nUse commercially reasonable efforts to determine whether a user is an adult or a minor with a reasonable level of certainty in accordance with paragraph (2).\n**(D)**\nMake a reasonable effort to ensure that users who are minors cannot engage in any activity that has been restricted by the developer for adults only.\n**(E)**\nObtain consent prior to permitting minor account holders from accessing a covered application or portion thereof that the developer has designated as unsuitable for use by minors without parental guidance or supervision, or from accessing content that is age-gated by law.\n**(F)**\nNot deliver personalized advertising to minors.\n**(G)**\nWith respect to an age signal requested by a developer from an application distribution provider regarding use of a covered application, the developer\u2014\n**(i)**\nshall request the minimum amount of information needed for purposes of compliance with this Act;\n**(ii)**\nmay not willfully disregard any information regarding an individual\u2019s age or age category that is otherwise available to the developer;\n**(iii)**\nmay not share the information obtained from the age signal with third parties, except for a service provider, but only if necessary for such service provider to implement safety measures or privacy protections for minors or otherwise required to do so by law; and\n**(iv)**\nmay not use the age signal for any purpose beyond that intended by this Act, including using the age signal to obtain or attempt to obtain a user\u2019s date of birth.\n**(H)**\nIn the event that a developer uses a method other than an age signal provided by an application distribution provider to satisfy the requirements of this section, the developer\u2014\n**(i)**\nshall request the minimum amount of information needed for purposes of compliance with this Act;\n**(ii)**\nmay not willfully disregard any information regarding an individual\u2019s age or age category that is available to the developer;\n**(iii)**\nmay not share the information obtained in the course of complying with this section with third parties, except for a service provider, but only if necessary for such service provider to implement safety measures or privacy protections for minors or otherwise required to do so by law; and\n**(iv)**\nmay not use age data for any purpose beyond that intended by this Act, including using age data to obtain or attempt to obtain a user\u2019s date of birth.\n**(2) Commercially reasonable effort**\n**(A) In general**\nSubject to subparagraph (B), for the purposes paragraph (1)(C), an age signal provided to a developer by an application distribution provider shall be considered a commercially reasonable effort.\n**(B) Exception**\nWith respect to an application that is intended only for adults and is required by law to restrict access to adults, an age signal provided to a developer by an application distribution provider that indicates a user is\u2014\n**(i)**\na minor shall be a sufficient basis to block access to such application; or\n**(ii)**\nan adult shall not, by itself, satisfy the requirement to determine whether a user is an adult with a reasonable level of certainty, including for purposes of other laws that require access restrictions based on age.\n##### (c) Special rules\n**(1) Common control**\nIf a developer and an application distribution provider are controlled by the same entity, the developer may rely on age determinations made by that entity.\n**(2) Applicability to covered websites**\nA developer of a covered website shall have the same requirements as a developer of a covered application under this Act and may carry over or repurpose an age signal received from an application distribution provider under section 101(a)(4) to fulfill such requirements with respect to the developer's covered website.\nII\nLIABILITY AND ENFORCEMENT\n#### 201. Limitations on liability\n##### (a) Application distribution providers\nAn application distribution provider that makes a good faith effort to comply with the obligations of this Act (as determined by the Commission or a court taking into consideration available technology) shall not be liable under any provision of this Act, or otherwise liable for its actions taken in attempt to comply with this Act, including, but not limited to, the following with regard to facilitation of the provision of an age signal:\n**(1)**\nAny erroneous age signal.\n**(2)**\nAny conduct by a developer of a covered application that receives any age signal.\n**(3)**\nFailing to provide an age signal due to any reasonable technical limitations or outages that prevent the provision of the age signal upon request.\n**(4)**\nNot providing the age signal to developers that do not adhere to reasonable safety standards and application distribution provider policies.\n##### (b) Developers\n**(1) Sole liability for determining whether an application is a covered application**\nA developer shall be solely responsible for correctly identifying whether an application of the developer is a covered application under this Act. No application distribution provider is required to proactively identify a covered application, and an application distribution provider shall not be held liable in cases where a developer provides inaccurate information about its applications.\n**(2) Erroneous age signal**\nA developer of a covered application shall not be liable for an erroneous age signal provided by an application distribution provider if the developer makes a reasonable effort, taking into consideration available technology, to properly use the age signal and carry out commercially reasonable methods to obtain or estimate the age of an account holder.\n#### 202. Enforcement\n##### (a) Unfair or deceptive acts or practices\nA violation of this Act or a regulation promulgated thereunder shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the Commission\n**(1) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person who violates this Act or a regulation promulgated thereunder shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n#### 203. Preemption\nNo State or political subdivision of a State may maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of any State, or political subdivision of a State, related to the provisions of this Act.\n#### 204. Severability\nIf any provision of this Act or the application of any provision to any person or circumstance is held invalid by a final decision of a court of competent jurisdiction, the remainder of this Act shall be given effect without the invalid provision or application.\n#### 205. Effective date\nThis Act shall take effect on the date that is 2 years after the date of its enactment.",
      "versionDate": "2026-04-20",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-11",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "6333",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Parents Over Platforms Act",
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
        "updateDate": "2026-05-04T20:36:50Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4349is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2026-04-29T04:53:36Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Parents Over Platforms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure responsible age assurance practices within the mobile ecosystem, particularly concerning the protection of minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:49Z"
    }
  ]
}
```
