# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1885?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1885
- Title: Stop the Scroll Act
- Congress: 119
- Bill type: S
- Bill number: 1885
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-04-16T12:48:13Z
- Update date including text: 2026-04-16T12:48:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1885",
    "number": "1885",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Stop the Scroll Act",
    "type": "S",
    "updateDate": "2026-04-16T12:48:13Z",
    "updateDateIncludingText": "2026-04-16T12:48:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
        "item": [
          {
            "date": "2026-04-14T14:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-22T17:41:23Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-22T17:41:23Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "PA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "OH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MI"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1885is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1885\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mrs. Britt (for herself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Federal Trade Commission, with the concurrence of the Secretary of Health and Human Services acting through the Surgeon General, to implement a mental health warning label on covered platforms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop the Scroll Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSocial media platform use is associated with risks to the physical and mental health of users, including exposure to bullying, online harassment and abuse, discrimination, and child sexual exploitation.\n**(2)**\nProduct warning labels can increase awareness of risks and influence behavior.\n**(3)**\nExtended use of social media, which addictive algorithms encourage, can contribute to negative health impacts associated with covered platforms.\n**(4)**\nThe Federal Government has a compelling interest in ensuring that users of a covered platform can make informed decisions about the amount of time the user spends on the covered platform, which requires an understanding of the mental health risks involved with using a covered platform.\n**(5)**\nIn May 2023, the Surgeon General issued an advisory warning that social media use is associated with a broad range of harms to mental health, and then called for warning labels on covered platforms to raise awareness of these risks and promote healthier online engagement.\n**(6)**\nGiven the substantial body of evidence documenting the adverse health effects of unregulated digital engagement, it is both appropriate and necessary to require clear, factual risk disclosures to ensure users are adequately informed before engaging with such platforms.\n**(7)**\nThis approach aligns with well-established public health standards that have long governed disclosure practices in industries affecting consumer well-being.\n**(8)**\nConspicuousness of labels is important, as evidenced by studies on tobacco and alcohol warning labels.\n#### 3. Definitions\nIn this Act:\n**(1) Anonymous content sharing platform**\nThe term anonymous content sharing platform means any website or mobile application that does not require registration and is used to share content, including digital images, recorded videos, text conversations, or live video conversations.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered platform**\nThe term covered platform means\u2014\n**(A)**\na social media platform as such term is defined in section 124 of the Trafficking Victims Prevention and Protection Reauthorization Act of 2022 ( 42 U.S.C. 1862w ); or\n**(B)**\nan anonymous content sharing platform.\n**(4) Covered platform provider**\nThe term covered platform provider means any person who, for commercial purposes in or affecting commerce, provides, manages, operates, or controls a covered platform.\n**(5) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(6) User**\nThe term user means, with respect to a covered platform, a person who registers an account with, creates a profile on, or otherwise accesses the covered platform.\n#### 4. Warning label\n##### (a) In general\nA covered platform provider shall\u2014\n**(1)**\neach time a user accesses the covered platform of the provider while physically located in the United States, clearly and conspicuously display a mental health warning label (referred to in this section as a covered label ) that complies with the requirements under this section, including the regulations promulgated under subsection (d);\n**(2)**\ncause the covered label to disappear only if the user\u2014\n**(A)**\nexits the covered platform; or\n**(B)**\nacknowledges the potential for harm and chooses to proceed to the covered platform despite the risk; and\n**(3)**\nif a user acknowledges the potential for harm and chooses to proceed to the covered platform in accordance with paragraph (2)(B), redisplay such covered label after each hour of continuous use by such user.\n##### (b) Content of covered label\nA covered label shall\u2014\n**(1)**\nwarn the user of potential negative mental health impacts of accessing the covered platform; and\n**(2)**\nprovide the user access to Federal resources to address the potential negative mental health impacts described in paragraph (1), including the 988 Suicide and Crisis Lifeline.\n##### (c) Restrictions on form\nA covered platform provider may not\u2014\n**(1)**\ninclude a covered label exclusively through a hyperlink or in the terms and conditions of the covered platform;\n**(2)**\ninclude extraneous information in a covered label that obscures the visibility or prominence of the covered label; or\n**(3)**\nallow a user to disable a covered label, except as provided in subsection (a).\n##### (d) Implementation\nNot later than 180 days after the date of enactment of this Act, the Commission, with the concurrence of the Secretary acting through the Surgeon General, shall promulgate regulations containing appropriate requirements for a covered label.\n##### (e) Review\nNot later than 5 years after the date on which the Commission promulgates the regulations required by subsection (d), and not less frequently than once every 5 years thereafter, the Commission, with the concurrence of the Secretary acting through the Surgeon General, shall review and revise such regulations to address changes in technology, market conditions, and medical science.\n#### 5. Enforcement\n##### (a) Enforcement by the commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act or a regulation promulgated under this Act by a covered platform provider shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the commission**\n**(A) In general**\nExcept as provided in subparagraph (C), the Commission shall enforce this Act and any regulation promulgated under this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nExcept as provided in subparagraph (C), any person who violates this Act or any regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Nonprofit organizations and common carriers**\nNotwithstanding section 4 or 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 44 , 45(a)(2)) or any jurisdictional limitation of the Commission, the Commission shall also enforce this Act and any regulation promulgated under this Act, in the same manner provided in subparagraphs (A) and (B), with respect to\u2014\n**(i)**\norganizations not organized to carry on business for their own profit or that of their members; and\n**(ii)**\ncommon carriers subject to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) and all Acts amendatory thereof and supplementary thereto.\n**(D) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n**(E) Rulemaking**\nThe Commission, with the concurrence of the Secretary acting through the Surgeon General, shall promulgate in accordance with section 553 of title 5, United States Code, such rules as may be necessary to carry out this Act.\n##### (b) Enforcement by States\n**(1) Authorization**\nSubject to paragraph (3), in any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of a covered platform provider in a practice that violates this Act, the attorney general of the State may, as parens patriae, bring a civil action against the covered platform provider on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief, including civil penalties in the amount determined under paragraph (2).\n**(2) Civil penalties**\nA covered platform provider that is found, in an action brought under paragraph (1), to have knowingly or repeatedly violated this Act shall, in addition to any other penalty otherwise applicable to a violation of this Act, be liable for a civil penalty equal to the amount calculated by multiplying\u2014\n**(A)**\nthe greater of\u2014\n**(i)**\nthe number of days during which the covered platform provider was not in compliance with this Act; or\n**(ii)**\nthe number of end users for whom the covered label was not displayed as a result of the violation; by\n**(B)**\nan amount not to exceed the maximum civil penalty for which a person, partnership, or corporation may be liable under section 5(m)(1)(A) of the Federal Trade Commission Act ( 15 U.S.C. 45(m)(1)(A) ) (including any adjustments for inflation).\n**(3) Rights of the commission**\n**(A) Notice to the commission**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring a civil action under paragraph (1) before initiating the civil action.\n**(ii) Contents**\nThe notification required under clause (i) with respect to a civil action shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required under clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by the commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal in the civil action.\n**(4) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to\u2014\n**(A)**\nconduct investigations;\n**(B)**\nadminister oaths or affirmations; or\n**(C)**\ncompel the attendance of witnesses or the production of documentary or other evidence.\n**(5) Preemptive action by the commission**\nIf the Commission institutes a civil action or an administrative action with respect to a violation of this Act, the attorney general of a State may not, during the pendency of such action, bring a civil action under paragraph (1) against any defendant named in the complaint of the Commission based on the same set of facts giving rise to the alleged violation with respect to which the Commission instituted the action.\n**(6) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n**(7) Actions by other State officials**\nIn addition to a civil action brought by an attorney general under paragraph (1), any other consumer protection officer of a State who is authorized by the State to do so may bring a civil action under paragraph (1), subject to the same requirements and limitations that apply under this subsection to a civil action brought by an attorney general.\n**(8) Savings provision**\nNothing in this subsection may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n##### (c) Extraterritorial jurisdiction\nThere is extraterritorial jurisdiction over any violation of this Act if such violation involves an individual in the United States or if any act in furtherance of the violation was committed in the United States.\n#### 6. Effective date\nThis Act shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-05-22",
      "versionType": "Introduced in Senate"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-16T12:47:47Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2026-04-16T12:47:24Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-04-16T12:48:07Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-04-16T12:46:12Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-04-16T12:46:04Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-04-16T12:47:13Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-04-16T12:45:57Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-04-16T12:46:45Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-04-16T12:48:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-06-23T18:01:16Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1885is.xml"
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
      "title": "Stop the Scroll Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop the Scroll Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal Trade Commission, with the concurrence of the Secretary of Health and Human Services acting through the Surgeon General, to implement a mental health warning label on covered platforms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:25Z"
    }
  ]
}
```
