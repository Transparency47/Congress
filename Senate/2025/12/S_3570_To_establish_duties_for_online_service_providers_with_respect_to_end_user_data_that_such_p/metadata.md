# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3570?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3570
- Title: Data Care Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3570
- Origin chamber: Senate
- Introduced date: 2025-12-18
- Update date: 2026-03-21T11:03:25Z
- Update date including text: 2026-03-21T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in Senate
- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-18: Introduced in Senate

## Actions

- 2025-12-18 - IntroReferral: Introduced in Senate
- 2025-12-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3570",
    "number": "3570",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001194",
        "district": "",
        "firstName": "Brian",
        "fullName": "Sen. Schatz, Brian [D-HI]",
        "lastName": "Schatz",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Data Care Act of 2025",
    "type": "S",
    "updateDate": "2026-03-21T11:03:25Z",
    "updateDateIncludingText": "2026-03-21T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
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
            "date": "2025-12-18T18:23:28Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-18T18:23:28Z",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "WI"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-12-18",
      "state": "ME"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-18",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MN"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MN"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-20",
      "state": "CO"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-20",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3570is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3570\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Mr. Schatz (for himself, Mr. Merkley , Mr. Murphy , Ms. Baldwin , Mr. King , Mr. Sanders , Mr. Booker , Ms. Duckworth , Ms. Smith , Mr. Durbin , Mr. Welch , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish duties for online service providers with respect to end user data that such providers collect and use.\n#### 1. Short title\nThis Act may be cited as the Data Care Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) End user**\nThe term end user means an individual who engages with an online service provider or logs into or uses services provided by the online service provider over the internet or any other digital network.\n**(3) Individual identifying data**\nThe term individual identifying data means any data that is\u2014\n**(A)**\ncollected over the internet or any other digital network; and\n**(B)**\nlinked, or reasonably linkable, to\u2014\n**(i)**\na specific end user; or\n**(ii)**\na computing device that is associated with or routinely used by an end user.\n**(4) Online service provider**\nThe term online service provider means an entity that\u2014\n**(A)**\nis engaged in interstate commerce over the internet or any other digital network; and\n**(B)**\nin the course of business, collects individual identifying data about end users, including in a manner that is incidental to the business conducted.\n**(5) Sensitive data**\nThe term sensitive data means any data that includes\u2014\n**(A)**\na social security number;\n**(B)**\npersonal information (as defined in section 1302 of the Children's Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 )) collected from a child (as defined in such section 1302);\n**(C)**\na driver\u2019s license number, passport number, military identification number, or any other similar number issued on a government document used to verify identity;\n**(D)**\na financial account number, credit or debit card number, or any required security code, access code, or password that is necessary to permit access to a financial account of an individual;\n**(E)**\nunique biometric data such as a finger print, voice print, a retina or iris image, or any other unique physical representation;\n**(F)**\ninformation sufficient to access an account of an individual, such as user name and password or email address and password;\n**(G)**\nthe first and last name of an individual, or first initial and last name, or other unique identifier in combination with\u2014\n**(i)**\nthe month, day, and year of birth of the individual;\n**(ii)**\nthe maiden name of the mother of the individual; or\n**(iii)**\nthe past or present precise geolocation of the individual;\n**(H)**\ninformation that relates to\u2014\n**(i)**\nthe past, present, or future physical or mental health or condition of an individual; or\n**(ii)**\nthe provision of health care to an individual; and\n**(I)**\nthe nonpublic communications or other nonpublic user-created content of an individual.\n#### 3. Provider duties\n##### (a) In general\nAn online service provider shall fulfill the duties of care, loyalty, and confidentiality under paragraphs (1), (2), and (3), respectively, of subsection (b).\n##### (b) Duties\n**(1) Duty of care**\nAn online service provider shall\u2014\n**(A)**\nreasonably secure individual identifying data from unauthorized access; and\n**(B)**\nsubject to subsection (d), promptly inform an end user of any breach of the duty described in subparagraph (A) of this paragraph with respect to sensitive data of that end user.\n**(2) Duty of loyalty**\nAn online service provider may not use individual identifying data, or data derived from individual identifying data, in any way that\u2014\n**(A)**\nwill benefit the online service provider to the detriment of an end user; and\n**(B)**\n**(i)**\nwill result in reasonably foreseeable and material physical or financial harm to an end user; or\n**(ii)**\nwould be unexpected and highly offensive to a reasonable end user.\n**(3) Duty of confidentiality**\nAn online service provider\u2014\n**(A)**\nmay not disclose or sell individual identifying data to, or share individual identifying data with, any other person except as consistent with the duties of care and loyalty under paragraphs (1) and (2), respectively;\n**(B)**\nmay not disclose or sell individual identifying data to, or share individual identifying data with, any other person unless that person enters into a contract with the online service provider that imposes on the person the same duties of care, loyalty, and confidentiality toward the applicable end user as are imposed on the online service provider under this subsection; and\n**(C)**\nshall take reasonable steps to ensure that the practices of any person to whom the online service provider discloses or sells, or with whom the online service provider shares, individual identifying data fulfill the duties of care, loyalty, and confidentiality assumed by the person under the contract described in subparagraph (B), including by auditing, on a regular basis, the data security and data information practices of any such person.\n##### (c) Application of duties to third parties\nIf an online service provider transfers or otherwise provides access to individual identifying data to another person, the requirements of paragraphs (1), (2), and (3) of subsection (b) shall apply to such person with respect to such data in the same manner that such requirements apply to the online service provider.\n##### (d) Expansion of duty To inform regarding breaches\nThe Commission may promulgate regulations under section 553 of title 5, United States Code, to apply the breach notification requirement under subsection (b)(1)(B) with respect to specific categories of individual identifying data other than sensitive data, as the Commission determines necessary.\n##### (e) Exceptions\n**(1) Regulations**\nThe Commission may promulgate regulations under section 553 of title 5, United States Code, to exempt categories of online service providers or persons described in subsection (c) from the requirement under subsection (a) or subsection (c) (as applicable).\n**(2) Considerations**\nIn promulgating regulations under paragraph (1), the Commission shall consider, among other factors\u2014\n**(A)**\nthe privacy risks posed by the use of individual identifying data by an online service provider or person described in subsection (c) based on\u2014\n**(i)**\nthe size of the provider or person;\n**(ii)**\nthe complexity of the offerings of the provider;\n**(iii)**\nthe nature and scope of the activities of the provider or person; and\n**(iv)**\nthe sensitivity of the consumer information handled by the provider or person; and\n**(B)**\nthe costs and benefits of applying the requirement under subsection (a) or subsection (c) (as applicable) to online service providers or persons with particular combinations of characteristics considered under subparagraph (A) of this paragraph.\n#### 4. Enforcement\n##### (a) Enforcement by Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of section 3 by an online service provider or a person described in section 3(c) shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of Commission**\n**(A) In general**\nExcept as provided in subparagraph (C), the Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nExcept as provided in subparagraph (C), any person who violates section 3 shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Nonprofit organizations and common carriers**\nNotwithstanding section 4 or 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 44 , 45(a)(2)) or any jurisdictional limitation of the Commission, the Commission shall also enforce this Act, in the same manner provided in subparagraphs (A) and (B) of this paragraph, with respect to\u2014\n**(i)**\norganizations not organized to carry on business for their own profit or that of their members; and\n**(ii)**\ncommon carriers subject to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ).\n**(3) Rulemaking authority**\nThe Commission shall promulgate regulations under this Act in accordance with section 553 of title 5, United States Code.\n##### (b) Enforcement by States\n**(1) Authorization**\nSubject to paragraph (3), in any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of an online service provider or a person described in section 3(c) in a practice that violates section 3, the attorney general of the State may, as parens patriae, bring a civil action against the online service provider or person on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief, including civil penalties in the amount determined under paragraph (2).\n**(2) Civil penalties**\nAn online service provider or person described in section 3(c) that is found, in an action brought under paragraph (1), to have knowingly or repeatedly violated section 3 shall, in addition to any other penalty otherwise applicable to a violation of section 3, be liable for a civil penalty equal to the amount calculated by multiplying\u2014\n**(A)**\nthe greater of\u2014\n**(i)**\nthe number of days during which the online service provider or person was not in compliance with that section; or\n**(ii)**\nthe number of end users who were harmed as a result of the violation, by\n**(B)**\nan amount not to exceed the maximum civil penalty for which a person, partnership, or corporation may be liable under section 5(m)(1)(A) of the Federal Trade Commission Act ( 15 U.S.C. 45(m)(1)(A) ) (including any adjustments for inflation).\n**(3) Rights of Federal Trade Commission**\n**(A) Notice to Federal Trade Commission**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring a civil action under paragraph (1) before initiating the civil action.\n**(ii) Contents**\nThe notification required under clause (i) with respect to a civil action shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required under clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by Federal Trade Commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(4) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to\u2014\n**(A)**\nconduct investigations;\n**(B)**\nadminister oaths or affirmations; or\n**(C)**\ncompel the attendance of witnesses or the production of documentary or other evidence.\n**(5) Preemptive action by Federal Trade Commission**\nIf the Commission institutes a civil action or an administrative action with respect to a violation of section 3, the attorney general of a State may not, during the pendency of the action, bring a civil action under paragraph (1) against any defendant named in the complaint of the Commission based on the same set of facts giving rise to the alleged violation with respect to which the Commission instituted the action.\n**(6) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n**(7) Actions by other State officials**\n**(A) In general**\nIn addition to civil actions brought by attorneys general under paragraph (1), any other consumer protection officer of a State who is authorized by the State to do so may bring a civil action under paragraph (1), subject to the same requirements and limitations that apply under this subsection to civil actions brought by attorneys general.\n**(B) Savings provision**\nNothing in this subsection may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n#### 5. Nonenforceability of certain provisions waiving rights and remedies\nThe rights and remedies provided under this Act may not be waived or limited by contract or otherwise.\n#### 6. Relation to other privacy and security laws\nNothing in this Act may be construed to\u2014\n**(1)**\nmodify, limit, or supersede the operation of any privacy or security provision in any other Federal or State statute or regulation; or\n**(2)**\nlimit the authority of the Commission under any other provision of law.\n#### 7. Effective date\n##### (a) In general\nThis Act shall take effect on the date of enactment of this Act.\n##### (b) Applicability\nSection 3 shall apply with respect to an online service provider or person described in section 3(c) on and after the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-12-18",
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
        "updateDate": "2026-01-20T16:38:14Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3570is.xml"
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
      "title": "Data Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Data Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish duties for online service providers with respect to end user data that such providers collect and use.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:33:31Z"
    }
  ]
}
```
