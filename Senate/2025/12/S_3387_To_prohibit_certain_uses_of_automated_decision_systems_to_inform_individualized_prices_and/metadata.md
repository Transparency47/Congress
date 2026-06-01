# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3387?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3387
- Title: One Fair Price Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3387
- Origin chamber: Senate
- Introduced date: 2025-12-08
- Update date: 2026-03-20T11:03:19Z
- Update date including text: 2026-03-20T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-08: Introduced in Senate
- 2025-12-08 - IntroReferral: Introduced in Senate
- 2025-12-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-08: Introduced in Senate

## Actions

- 2025-12-08 - IntroReferral: Introduced in Senate
- 2025-12-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-08",
    "latestAction": {
      "actionDate": "2025-12-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3387",
    "number": "3387",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "One Fair Price Act of 2025",
    "type": "S",
    "updateDate": "2026-03-20T11:03:19Z",
    "updateDateIncludingText": "2026-03-20T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-08",
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
      "actionDate": "2025-12-08",
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
            "date": "2025-12-08T23:10:23Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-08T23:10:23Z",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3387is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3387\nIN THE SENATE OF THE UNITED STATES\nDecember 8 (legislative day, December 4), 2025 Mr. Gallego introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit certain uses of automated decision systems to inform individualized prices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Fair Price Act of 2025 .\n#### 2. Prohibition on surveillance-based price setting\n##### (a) Surveillance-Based price setting\n**(1) In general**\nSubject to paragraphs (2) and (3), it shall be unlawful for a person to offer or charge different prices to different consumers for the same, or a substantially similar, product or service using, informed by, or based on, in whole or in part, surveillance data.\n**(2) Safe harbor**\n**(A) In general**\nThe following shall not be considered surveillance-based price setting for purposes of paragraph (1) if the conditions of subparagraph (B) are met:\n**(i)**\nA difference in price that is based solely on reasonable costs associated with providing the product or service to different consumers.\n**(ii)**\nA bona fide discount that is offered to any member of a broadly defined group, including teachers, active duty personnel, veterans, senior citizens, or students.\n**(iii)**\nA bona fide discount that is offered to any consumer who affirmatively and knowingly enrolls in a loyalty program.\n**(B) Conditions for exception**\nThe conditions described in this subparagraph are the following:\n**(i)**\nAny basis for a difference in reasonable costs associated with providing a product or service to different consumers is disclosed to the consumer prior to purchase.\n**(ii)**\nAny eligibility condition or criteria for receiving or earning a bona fide discount is clearly and conspicuously disclosed.\n**(iii)**\nAny bona fide discount is offered uniformly to any consumer who meets the disclosed eligibility conditions or criteria.\n**(iv)**\nAny surveillance data used solely to offer or administer a bona fide discount is not used for any other purpose, including profiling, targeted advertising, or individualized price setting.\n**(v)**\nAny loyalty program that allows a user to accrue and exchange points, credits, or any similar nonmonetary system of value for a product or service does not charge a different price for those points, credits, or similar nonmonetary system of value to different consumers for the same or substantially similar product or service.\n**(3) Inapplicability to insurance or credit products**\nThe prohibition under paragraph (1) shall not apply to the business of insurance or any credit product.\n##### (b) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices; Unfair methods of competition**\nA violation of subsection (a) or a regulation promulgated under such subsection shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) and as a violation of section 5(a) of the Federal Trade Commission Act ( 15 U.S.C. 45(a) ) regarding unfair methods of competition.\n**(2) Powers of the Commission**\n**(A) In general**\nExcept as provided in subparagraph (C), the Commission shall enforce subsection (a) and any regulation promulgated under such subsection in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nExcept as provided in subparagraph (C), any person who violates such subsection or a regulation promulgated under such subsection shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(C) Common carriers, nonprofit organizations, and air carriers**\nNotwithstanding section 4, 5(a)(2), or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 , 45(a)(2), 46) or any jurisdictional limitation of the Commission, the Commission shall also enforce subsection (a) or a regulation promulgated under subsection (a), in the same manner provided in subparagraphs (A) and (B), with respect to\u2014\n**(i)**\ncommon carriers subject to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) and all Acts amendatory thereof and supplementary thereto;\n**(ii)**\norganizations not organized to carry on business for their own profit or that of their members; and\n**(iii)**\nair carriers and foreign air carriers subject to the Federal Aviation Act of 1958.\n**(D) Rulemaking**\n**(i) In general**\nThe Commission may promulgate in accordance with section 553 of title 5, United States Code, such rules as may be necessary to carry out this section, including guidance regarding how to comply with subsection (a).\n**(ii) Small business concerns**\nThe Commission shall consider rules necessary to carry out this Act as having a significant economic impact on a substantial number of small entities for purposes of chapter 6 of title 5, United States Code (commonly referred to as the Regulatory Flexibility Act ).\n**(E) Authority preserved**\nNothing in this Act may be construed to limit the authority of the Commission under any other provision of law.\n##### (c) Actions by States\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by the engagement of any person in an act or practice in violation of subsection (a) or a regulation promulgated under such subsection, the attorney general of the State, may as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with such subsection or such regulation;\n**(C)**\nobtain, for each violation, the greater of\u2014\n**(i)**\nthe actual monetary damages incurred from the violation; or\n**(ii)**\n$3,000; or\n**(D)**\nobtain, for each violation, any other restitution, penalties, and other legal or equitable relief as the court may deem appropriate.\n**(2) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this Act shall be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n##### (d) Private right of action\n**(1) In general**\nAn individual who has been injured by a person in violation of subsection (a) or a regulation promulgated under such subsection may bring a civil action against such person in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin the violation;\n**(B)**\nobtain, for each violation, the greater of\u2014\n**(i)**\nthe actual monetary damages incurred from the violation; or\n**(ii)**\n$3,000; or\n**(C)**\nobtain, for each violation, any other restitution, penalties, and other legal or equitable relief as the court may deem appropriate.\n**(2) Willful violations**\nIf the court finds that the defendant acted willfully in committing a violation described in paragraph (1), the court may, in its discretion, increase the amount of the award to an amount equal to not more than 3 times the amount available under paragraph (1)(B).\n**(3) Prima facie case; rebuttal**\n**(A) Prima facie case**\nIn any proceeding commenced pursuant to paragraph (1), the defendant shall be presumed to be in violation of subsection (a) if the plaintiff can demonstrate that\u2014\n**(i)**\ntwo or more individuals were offered different prices by the defendant for the same, or a substantially similar, product or service during the same, or a substantially similar, period of time; or\n**(ii)**\none individual was offered different prices by the defendant for the same, or a substantially similar, product or service during the same, or a substantially similar, period of time while using different means of viewing the price.\n**(B) Burden of rebutting prima facie case**\nThe defendant may rebut the presumption described in subparagraph (A) by demonstrating that the alleged difference in price was\u2014\n**(i)**\nnot informed, in whole or in part, by surveillance data; or\n**(ii)**\nfully explained by the safe harbors described in subsection (a)(2).\n**(4) Costs and attorney\u2019s fees**\nThe court shall award to a prevailing plaintiff in an action under this subsection the litigation costs of such action and reasonable attorney\u2019s fees, as determined by the court.\n**(5) Limitation**\nAn action may be commenced under this subsection not later than 5 years after the date on which the individual first discovered or had a reasonable opportunity to discover the violation.\n**(6) Nonexclusive remedy**\nBringing a civil action under this subsection shall be in addition to any other remedy available to the individual bringing such civil action.\n**(7) Invalidity of pre-dispute arbitration and joint action waivers**\nNotwithstanding chapter 1 of title 9, United States Code (commonly known as the Federal Arbitration Act ), or any other provision of law, a pre-dispute arbitration agreement or pre-dispute joint action waiver between a person in violation of subsection (a) and an individual is not valid or enforceable for purposes of the individual bringing a civil action against such person under this subsection.\n##### (e) Joint study and report\n**(1) Study**\nNot later than 1 year after the date of enactment of this section, the Office of Advocacy of the Small Business Administration (in this subsection referred to as the Office of Advocacy ), in consultation with the Commission, shall conduct a joint study to evaluate the impact of this Act on\u2014\n**(A)**\nsmall business concerns; and\n**(B)**\npromoting competition between large and small business enterprises.\n**(2) Report**\nNot later than 180 days after the Office of Advocacy completes the study under paragraph (1), the Commission and the Office of Advocacy shall submit to Congress a report on such study, including any relevant findings and recommendations resulting from such study.\n##### (f) Definitions\nIn this section:\n**(1) Bona fide discount**\nThe term bona fide discount means an offered price that is lower than the genuine price at which a product or service is widely offered to the public on a regular basis for a reasonably substantial period of time and not for the purpose of establishing a fictitious price to enable the subsequent offer of a reduction.\n**(2) Business of insurance; credit**\nThe terms business of insurance and credit have the meaning given such terms in section 1002 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 ).\n**(3) Commission**\nThe term Commission means the Federal Trade Commission.\n**(4) Genetic information**\nThe term genetic information has the meaning given such term in section 2791(d) of the Public Health Service Act ( 42 U.S.C. 300gg\u201391(d) ).\n**(5) Personal information**\nThe term personal information means any quality, feature, attribute, or trait of an individual, including any immutable characteristic (such as race and eye color), mutable characteristic (such as address, weight, citizenship, family, or parenthood status), genetic information, and any other information that could reasonably be linked, directly or indirectly, with a particular individual or household.\n**(6) Pre-dispute arbitration agreement**\nThe term pre-dispute arbitration agreement means any agreement to arbitrate a dispute that has not arisen at the time of making the agreement.\n**(7) Pre-dispute joint action waiver**\nThe term pre-dispute joint action waiver means an agreement, including as part of a pre-dispute arbitration agreement, that would prohibit, or waive the right of, one of the parties to the agreement to participate in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not arisen at the time of making the agreement.\n**(8) Price**\nThe term price means the amount charged or offered to a consumer in relation to a transaction, including any related cost and fee and any other material term of the transaction that has direct bearing on the amount paid by the consumer or the value of the product or service offered or provided to the consumer.\n**(9) Small business concern**\nThe term small business concern \u2014\n**(A)**\nhas the meaning given such term in section 3 of the Small Business Act ( 15 U.S.C. 632 ); and\n**(B)**\nshall not include a small business concern involved in developing, training, or selling a product or service for the primary purpose of aiding a business to determine a price.\n**(10) Surveillance data**\nThe term surveillance data \u2014\n**(A)**\nmeans data that is related to the personal information, behavior, or biometrics of an individual; and\n**(B)**\nincludes data gathered, purchased, or otherwise acquired.\n#### 3. Application of prohibition on surveillance-based price setting to air carriers and ticket agents\n##### (a) In general\nSection 41712 of title 49, United States Code, is amended by adding at the end the following:\n(d) Prohibition on surveillance-Based price setting It shall be an unfair or deceptive practice under subsection (a) for an air carrier, foreign air carrier, or ticket agent to engage in surveillance-based price setting, as described in section 2(a) of the One Fair Price Act of 2025 . .\n##### (b) No preemption of consumer protection claims\nSection 41713(b)(4) of title 49, United States Code, is amended by adding at the end the following:\n(D) No preemption of surveillance-based price setting claims Nothing in subparagraphs (A) through (C) may be construed\u2014 (i) to preempt, displace, or supplant any action for civil damages or injunctive relief based on a violation of section 2(a) of the One Fair Price Act of 2025 ; or (ii) to restrict the authority of any government entity, including an attorney general of a State, from bringing a legal claim on behalf of the citizens of the State with respect to any such violation. .",
      "versionDate": "2025-12-08",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-01-07T17:32:03Z"
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
      "date": "2025-12-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3387is.xml"
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
      "title": "One Fair Price Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "One Fair Price Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit certain uses of automated decision systems to inform individualized prices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:15Z"
    }
  ]
}
```
