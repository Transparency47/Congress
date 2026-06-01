# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8250?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8250
- Title: Parents Decide Act
- Congress: 119
- Bill type: HR
- Bill number: 8250
- Origin chamber: House
- Introduced date: 2026-04-13
- Update date: 2026-04-23T18:49:47Z
- Update date including text: 2026-04-23T18:49:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-13: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-13: Introduced in House

## Actions

- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-13",
    "latestAction": {
      "actionDate": "2026-04-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8250",
    "number": "8250",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Parents Decide Act",
    "type": "HR",
    "updateDate": "2026-04-23T18:49:47Z",
    "updateDateIncludingText": "2026-04-23T18:49:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-13",
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
      "actionDate": "2026-04-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-13",
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
          "date": "2026-04-13T18:31:20Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8250ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8250\nIN THE HOUSE OF REPRESENTATIVES\nApril 13, 2026 Mr. Gottheimer (for himself and Ms. Stefanik ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require operating system providers to verify the age of any user of an operating system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Parents Decide Act .\n#### 2. Required age verification for users of operating systems\n##### (a) Requirements\nAn operating system provider, with respect to any operating system of such provider, shall carry out the following:\n**(1)**\nRequire any user of the operating system to provide the date of birth of the user in order to\u2014\n**(A)**\nset up an account on the operating system; and\n**(B)**\nuse the operating system.\n**(2)**\nIf the relevant user of the operating system is under 18 years of age, require a parent or legal guardian of the user to verify the date of birth of the user.\n**(3)**\nDevelop a system to allow an app developer to access any information as is necessary, collected by the operating system to carry out this section and any regulation promulgated under this section, to verify the date of birth of a user of an app of the app developer.\n##### (b) Safe harbor\nAn operating system provider may not be held liable for a violation of a provision of this Act or a regulation promulgated under this Act if the provider follows the requirements described in such provision or regulation.\n##### (c) Enforcement by Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section or a regulation promulgated under this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Commission shall enforce this section and any regulation promulgated under this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act. Any person who violates this section or a regulation promulgated under this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (d) Regulations\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Commission shall promulgate, under section 553 of title 5, United States Code, regulations to carry out this section, including regulations relating to the following:\n**(A)**\nHow an operating system provider can\u2014\n**(i)**\nverify the date of birth of a parent or legal guardian described in subsection (a)(2); and\n**(ii)**\ncarry out the requirements described in subsection (a) with respect to an operating system of such provider that may be shared by individuals of varying ages.\n**(B)**\nData protection standards related to how an operating system provider shall ensure a date of birth collected by the operating system provider from a user, or the parent or legal guardian of the user, to carry out this section and any regulation promulgated under this section\u2014\n**(i)**\nis collected in a secure manner to maintain the privacy of the user or the parent or legal guardian of the user; and\n**(ii)**\nis not stolen or breached.\n**(C)**\nHow an operating system provider shall\u2014\n**(i)**\nensure an app developer can access information collected by the operating system provider to carry out this section and any regulation promulgated under this section, subject to the data protection standards under subparagraph (B), to verify the date of birth of a user of an app of the app developer; and\n**(ii)**\nensure the parent or legal guardian of a user of an operating system who is under 18 years of age is allowed to control what such user is allowed to access on a device.\n**(2) Briefing to Congress**\nNot later than 180 days after the date of the enactment of this Act, the Commission shall brief Congress on the following information:\n**(A)**\nThe rulemaking process of the Commission with respect to such regulations.\n**(B)**\nAny considerations of the Commission with respect to implementing such regulations.\n##### (e) Report\nNot later than 18 months after the date of the enactment of this Act, the Commission shall submit to Congress a report on\u2014\n**(1)**\nhow operating system providers carry out the requirements described in subsection (a); and\n**(2)**\nany recommendation for legislative action related to updating such requirements.\n##### (f) Effective date\nThis section, and any regulation promulgated pursuant to subsection (d)(1), shall take effect on the date that is 1 year after the date of the enactment of this Act.\n##### (g) Definitions\nIn this section:\n**(1) App**\nThe term app means a software application or electronic service that may be run or directed by a user on a computer, mobile device, or any other general purpose computing device.\n**(2) App developer**\nThe term app developer means a person that owns or controls an app that is available for use in the United States.\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Operating system**\nThe term operating system means software that supports the basic functions of a computer, mobile device, or any other general purpose computing device.\n**(5) Operating system provider**\nThe term operating system provider means a person that develops, licenses, or controls the operating system on a computer, mobile device, or any other general purpose computing device.",
      "versionDate": "2026-04-13",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-04-20T22:20:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-13",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr8250",
          "measure-number": "8250",
          "measure-type": "hr",
          "orig-publish-date": "2026-04-13",
          "originChamber": "HOUSE",
          "update-date": "2026-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8250v00",
            "update-date": "2026-04-23"
          },
          "action-date": "2026-04-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Parents Decide Act</strong></p><p>This bill establishes age-verification requirements for providers of operating systems, which includes software that supports the basic functions of a computer, mobile device, or other general purpose computing device.</p><p>First, operating system providers must require users to provide their date of birth to set up an account on, and use, the operating system. If the user is under 18 years old, the operating\u00a0system must require a parent or legal guardian to verify the user's date of birth.</p><p>Additionally, operating system providers must develop a system to allow app developers to access information necessary to verify the date of birth of a user of the developer's app.</p><p>The bill provides for enforcement\u00a0of these requirements by the Federal Trade Commission (FTC).</p><p>The FTC also must issue regulations on how operating system providers\u00a0can (1)\u00a0verify the date of birth of a parent or legal guardian and carry out requirements for verifying the ages of users, (2) secure data\u00a0collected through the verification process, and (3) ensure parents\u00a0or legal guardians have control over what\u00a0users who are under 18 years old are able to access on a device.</p><p>The FTC must brief Congress on the rulemaking process and report on how operating system providers carry out the requirements of the bill.</p>"
        },
        "title": "Parents Decide Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8250.xml",
    "summary": {
      "actionDate": "2026-04-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Parents Decide Act</strong></p><p>This bill establishes age-verification requirements for providers of operating systems, which includes software that supports the basic functions of a computer, mobile device, or other general purpose computing device.</p><p>First, operating system providers must require users to provide their date of birth to set up an account on, and use, the operating system. If the user is under 18 years old, the operating\u00a0system must require a parent or legal guardian to verify the user's date of birth.</p><p>Additionally, operating system providers must develop a system to allow app developers to access information necessary to verify the date of birth of a user of the developer's app.</p><p>The bill provides for enforcement\u00a0of these requirements by the Federal Trade Commission (FTC).</p><p>The FTC also must issue regulations on how operating system providers\u00a0can (1)\u00a0verify the date of birth of a parent or legal guardian and carry out requirements for verifying the ages of users, (2) secure data\u00a0collected through the verification process, and (3) ensure parents\u00a0or legal guardians have control over what\u00a0users who are under 18 years old are able to access on a device.</p><p>The FTC must brief Congress on the rulemaking process and report on how operating system providers carry out the requirements of the bill.</p>",
      "updateDate": "2026-04-23",
      "versionCode": "id119hr8250"
    },
    "title": "Parents Decide Act"
  },
  "summaries": [
    {
      "actionDate": "2026-04-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Parents Decide Act</strong></p><p>This bill establishes age-verification requirements for providers of operating systems, which includes software that supports the basic functions of a computer, mobile device, or other general purpose computing device.</p><p>First, operating system providers must require users to provide their date of birth to set up an account on, and use, the operating system. If the user is under 18 years old, the operating\u00a0system must require a parent or legal guardian to verify the user's date of birth.</p><p>Additionally, operating system providers must develop a system to allow app developers to access information necessary to verify the date of birth of a user of the developer's app.</p><p>The bill provides for enforcement\u00a0of these requirements by the Federal Trade Commission (FTC).</p><p>The FTC also must issue regulations on how operating system providers\u00a0can (1)\u00a0verify the date of birth of a parent or legal guardian and carry out requirements for verifying the ages of users, (2) secure data\u00a0collected through the verification process, and (3) ensure parents\u00a0or legal guardians have control over what\u00a0users who are under 18 years old are able to access on a device.</p><p>The FTC must brief Congress on the rulemaking process and report on how operating system providers carry out the requirements of the bill.</p>",
      "updateDate": "2026-04-23",
      "versionCode": "id119hr8250"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8250ih.xml"
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
      "title": "Parents Decide Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parents Decide Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require operating system providers to verify the age of any user of an operating system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T04:48:33Z"
    }
  ]
}
```
