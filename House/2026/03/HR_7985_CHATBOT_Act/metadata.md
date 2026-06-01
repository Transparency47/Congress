# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7985?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7985
- Title: CHATBOT Act
- Congress: 119
- Bill type: HR
- Bill number: 7985
- Origin chamber: House
- Introduced date: 2026-03-18
- Update date: 2026-04-02T22:06:14Z
- Update date including text: 2026-04-02T22:06:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-18: Introduced in House

## Actions

- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7985",
    "number": "7985",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CHATBOT Act",
    "type": "HR",
    "updateDate": "2026-04-02T22:06:14Z",
    "updateDateIncludingText": "2026-04-02T22:06:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
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
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T14:00:10Z",
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
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "VA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7985ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7985\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2026 Mr. Mullin (for himself, Ms. Matsui , Mrs. Dingell , Mr. Soto , Ms. Tlaib , Ms. McClellan , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the marketing, advertising, or provision of professional services without the appropriate licenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Curbing Harmful AI Tools By Offering Transparency Act or the CHATBOT Act .\n#### 2. AI Chatbot Transparency\n##### (a) Prohibition; requirement\n**(1) In general**\nA covered entity may not provide the generation of output from an AI chatbot, or disseminate marketing or advertising materials, that, from the perspective of a reasonable user\u2014\n**(A)**\nindicate or imply possession of an appropriate license to practice a covered profession without, at that time, the possession of such license; and\n**(B)**\nfalsely indicate or imply that the output is provided or verified by a human in possession of an appropriate license to practice a covered profession.\n**(2) Imply defined**\nFor purposes of paragraph (1)(A), the term imply \u2014\n**(A)**\nmeans a representation that a reasonable user would understand as claiming possession of a professional license, including a statement about credentials, qualifications, fictitious professional experience, or authoritative and conclusive recommendations, advice, or guidance that a reasonable user would understand is typically only provided by a practitioner of a covered profession; and\n**(B)**\ndoes not include providing general information, procedural guidance not specific to the circumstance of the user, or informative content that does not represent or suggest licensure.\n##### (b) Guidance\nNot later than 12 months after the date of the enactment of this section, the Commission, in consultation with relevant agencies and stakeholders, including consumer advocacy organizations and technology experts, shall provide guidance on complying with the requirements of this section.\n##### (c) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (a) or a regulation promulgated under such subsection shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of commission**\nThe Federal Trade Commission shall enforce subsection (a) and a regulation promulgated under such subsection in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section. Any person who violates subsection (a) or a regulation promulgated under such subsection shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act. Nothing in this Act may be construed to limit the authority of the Commission under any other provision of law.\n##### (d) Actions by states\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of subsection (a) or a regulation promulgated under such subsection, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with this subsection (a) or a regulation promulgated under such subsection;\n**(C)**\nobtain damages for actual monetary loss from the violation or up to $5,000 in damages for each such violation, whichever is greater, on behalf of residents State; or\n**(D)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(2) Notice**\nBefore filing an action under this subsection, the attorney general, official, or agency of the State involved shall provide to the Federal Trade Commission a written notice of such action and a copy of the complaint for such action. If the attorney general, official, or agency determines it is not feasible to provide the notice described in this paragraph before the filing of the action, the attorney general, official, or agency shall provide written notice of the action and a copy of the complaint to the Federal Trade Commission immediately upon the filing of the action.\n**(3) Authority of the Federal Trade Commission**\n**(A) In general**\nOn receiving notice under paragraph (2) of an action under this subsection, the Federal Trade Commission shall have the right\u2014\n**(i)**\nto intervene in the action;\n**(ii)**\nupon so intervening, to be heard on all matters arising therein; and\n**(iii)**\nto file petitions for appeal.\n**(B) Limitation on state action while Federal action is pending**\nIf the Federal Trade Commission or the Attorney General of the United States has instituted a civil action for violation of this subsection (a) or a regulation promulgated under such subsection (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under this subsection during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of such regulation alleged in such complaint.\n**(C) Rules of construction**\n**(i) State authority**\nFor purposes of bringing a civil action under this subsection, nothing in this Act may be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n**(ii) Preservation of State authority**\nNothing in this Act may be construed to preempt, limit, or otherwise affect or restrict the application of any State law, rule, regulation, requirement, or standard that provides a user with greater or additional rights, remedies, or protections than the rights, remedies, and protections provided under this Act, including any State law, rule, requirement, or standard governing the licensing, regulation, or discipline of a covered profession regulated under State law, including enforcement actions for the unlicensed practice of such profession.\n##### (e) Private right of action\n**(1) In general**\nA person injured by an act or practice in violation of subsection (a) or a regulation promulgated under such subsection may bring in an appropriate district court of the United States\u2014\n**(A)**\nan action to enjoin the violation;\n**(B)**\nan action to recover damages for actual monetary loss from the violation, or to receive up to $5,000 in damages for each such violation, whichever is greater; or\n**(C)**\nboth such actions.\n**(2) Willful or knowing violations**\nIf the court finds that the defendant acted willfully or knowingly in committing a violation described in paragraph (1), the court may, in its discretion, increase the amount of the award to an amount equal to not more than 3 times the amount available under paragraph (1)(B).\n**(3) Costs and attorney\u2019s fees**\nThe court shall award to a prevailing plaintiff in an action under this subsection the costs of such action and reasonable attorney\u2019s fees, as determined by the court.\n**(4) Limitation**\nAn action may be commenced under this subsection not later than 5 years after the date on which the person first discovered or had a reasonable opportunity to discover the violation.\n**(5) Nonexclusive remedy**\nThe remedy provided by this subsection shall be in addition to any other remedies available to the person.\n##### (f) Adjustment for inflation for civil penalties and damages\nBeginning on the date that the Consumer Price Index is first published by the Bureau of Labor Statistics that is at least 1 year after the date of the enactment of this Act, and each year thereafter, the amount specified in subsections (d)(1)(C) and (e)(1)(B) shall be increased by the percentage increase, if any, in the Consumer Price Index published on such date from the Consumer Price Index published the previous year.\n##### (g) Definitions\nIn this section:\n**(1) Appropriate license**\nThe term appropriate license means a permit or authorization required to practice a covered profession, as determined by the State in which the covered entity provides the service.\n**(2) AI chatbot**\nThe term AI chatbot means a system that uses artificial intelligence to engage in interactive conversations with a user similar to the communications that an individual would have with a human.\n**(3) Artificial intelligence; AI**\nThe term artificial intelligence or AI has the meaning given that term in section 9401 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(4) Commission**\nThe term Commission means the Federal Trade Commission.\n**(5) Covered entity**\nThe term covered entity means an individual or company that deploys an AI chatbot.\n**(6) Covered profession**\nThe term covered profession means a profession that does any of the following:\n**(A)**\nOperates in the finance and insurance sector (as defined in NAICS Code 52).\n**(B)**\nOperates in the health care and social assistance sector (as defined in NAICS Code 62).\n**(C)**\nProvides legal services (as defined in NAICS code 5411).\n**(D)**\nProvides accounting, tax preparation, bookkeeping, and payroll services (as defined in NAICS code 5412).\n**(7) State**\nThe term State means each of the several States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.",
      "versionDate": "2026-03-18",
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
        "updateDate": "2026-04-02T22:06:13Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7985ih.xml"
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
      "title": "CHATBOT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-31T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHATBOT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Curbing Harmful AI Tools By Offering Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the marketing, advertising, or provision of professional services without the appropriate licenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T04:48:22Z"
    }
  ]
}
```
