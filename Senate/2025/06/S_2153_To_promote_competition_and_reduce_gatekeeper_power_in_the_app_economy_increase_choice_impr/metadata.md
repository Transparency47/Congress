# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2153
- Title: Open App Markets Act
- Congress: 119
- Bill type: S
- Bill number: 2153
- Origin chamber: Senate
- Introduced date: 2025-06-24
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in Senate
- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-24: Introduced in Senate

## Actions

- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2153",
    "number": "2153",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Open App Markets Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T20:30:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "UT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
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
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2153is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2153\nIN THE SENATE OF THE UNITED STATES\nJune 24, 2025 Mrs. Blackburn (for herself, Mr. Blumenthal , Mr. Lee , Ms. Klobuchar , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo promote competition and reduce gatekeeper power in the app economy, increase choice, improve quality, and reduce costs for consumers.\n#### 1. Short title\nThis Act may be cited as the Open App Markets Act .\n#### 2. Definitions\nIn this Act:\n**(1) App**\nThe term app means a software application or electronic service that may be run or directed by a user on a computer, a mobile device, or any other general purpose consumer computing device.\n**(2) App store**\nThe term app store means a publicly available website, software application, or other electronic service that distributes apps from third-party developers to users of a computer, a mobile device, or any other general purpose consumer computing device.\n**(3) Covered company**\nThe term covered company means any person that owns or controls\u2014\n**(A)**\nan app store for which users in the United States exceed 50,000,000 on a monthly basis (inclusive of support functions associated with the app store such as updates to apps); and\n**(B)**\nthe operating system or operating system configuration on which the app store described in subparagraph (A) operates.\n**(4) Developer**\nThe term developer means a person that owns or controls an app or an app store.\n**(5) In-app payment system**\nThe term in-app payment system means an application, service, or user interface to manage billing or process the payments from users of an app.\n**(6) Nonpublic business information**\nThe term nonpublic business information means nonpublic data that is\u2014\n**(A)**\nderived from a developer or an app or app store owned or controlled by a developer, including interactions between users and the app or app store of the developer; and\n**(B)**\ncollected by a covered company in the course of operating an app store or providing an operating system.\n#### 3. Protecting a competitive app market\n##### (a) Exclusivity and tying\nA covered company shall not\u2014\n**(1)**\nrequire developers to use or enable an in-app payment system owned or controlled by the covered company or any of its business partners as a condition of the distribution of an app on an app store or being accessible on an operating system;\n**(2)**\nrequire as a term of distribution on an app store that pricing terms or conditions of sale be equal to or more favorable on its app store than the terms or conditions under another app store; or\n**(3)**\ntake punitive action or otherwise impose less favorable terms and conditions against a developer\u2014\n**(A)**\nfor using or offering different pricing terms or conditions of sale through another in-app payment system or on another app store; or\n**(B)**\non the basis that an app provides access to other third-party apps or games through remote electronic services rather than through download from an app store.\n##### (b) Interference with legitimate business communications\nA covered company shall not impose restrictions on communications of developers with the users of an app of the developer through the app or direct outreach to a user concerning legitimate business offers, such as pricing terms and product or service offerings. Nothing in this subsection shall prohibit a covered company from requiring that an app acquire user consent prior to the collection and sharing of the data of the user by an app.\n##### (c) Nonpublic business information\nA covered company shall not use nonpublic business information derived from a third-party app for the purpose of competing with that app.\n##### (d) Interoperability\nA covered company that controls the operating system or operating system configuration on which its app store operates shall allow and provide readily accessible means for users of that operating system to\u2014\n**(1)**\nchoose third-party apps or app stores as defaults;\n**(2)**\ninstall third-party apps or app stores through means other than its app store; and\n**(3)**\nhide or delete apps or app stores provided or preinstalled by the covered company or any of its business partners.\n##### (e) Self-Preferencing in search\n**(1) In general**\nA covered company shall not provide unequal treatment of apps in an app store through ranking schemes, user interface features, or algorithms that unreasonably preference or rank the apps of the covered company or any of its business partners over those of other apps in organic search results.\n**(2) Considerations**\nUnreasonably preferencing does not include clearly disclosed advertising.\n##### (f) Open app development\n**(1) Access**\nA covered company shall provide access to operating system interfaces and hardware and software features to developers that are generally available to the public.\n**(2) Documentation**\nA covered company shall provide documentation and development information sufficient to access such interfaces and features.\n**(3) Timely and equivalent basis**\nA covered company shall provide the access and documentation under this subsection on a reasonably timely basis and on terms that are equivalent to the terms for access by the covered company or to its business partners.\n#### 4. Protecting the security and privacy of users\n##### (a) In general\n**(1) No violation**\nSubject to section (b), a covered company shall not be in violation of section 3 for an action that is\u2014\n**(A)**\nnecessary to achieve user privacy or security;\n**(B)**\ntaken to prevent spam or fraud;\n**(C)**\nnecessary to prevent unlawful infringement of preexisting intellectual property; or\n**(D)**\ntaken to prevent a violation of, or comply with, Federal or State law.\n**(2) Privacy and security protections**\nIn paragraph (1), the term necessary to achieve user privacy or security includes\u2014\n**(A)**\nallowing an end user to opt in, and providing information regarding the reasonable risks, prior to enabling installation of the third-party apps or app stores;\n**(B)**\nremoving malicious or fraudulent apps or app stores from an end user device;\n**(C)**\nproviding an end user with the means to verify the authenticity and origin of third-party apps or app stores; and\n**(D)**\nproviding an end user with the option to limit access to the user's device or device features, or limit the collection and sharing of the data of the user with third-party apps or app stores.\n##### (b) Requirements\n**(1) In general**\nSubsection (a) shall only apply if the covered company establishes by a preponderance of the evidence that the action described in that subsection is\u2014\n**(A)**\napplied on a demonstrably consistent basis to\u2014\n**(i)**\napps of the covered company or its business partners; and\n**(ii)**\nother apps; and\n**(B)**\nnarrowly tailored and could not be achieved through a less discriminatory and technically possible means.\n**(2) Certification**\nThe principal executive officer or officers of the covered company, or persons performing similar functions shall submit to the court a certification made under penalty of perjury in accordance with section 1746 of title 28, United States Code, that the action described in subsection (a) is not used as a pretext to exclude, or impose unnecessary or discriminatory terms on, third-party apps, in-app payment systems, or alternative app stores.\n#### 5. Enforcement\n##### (a) Enforcement\n**(1) In general**\nThe Federal Trade Commission, the Attorney General, and any attorney general of a State subject to the requirements in paragraph (3) shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ), the Sherman Act ( 15 U.S.C. 1 et seq. ), the Clayton Act ( 15 U.S.C. 12 et seq. ), and the Antitrust Civil Process Act ( 15 U.S.C. 1311 et seq. ), as appropriate, were incorporated into and made a part of this Act.\n**(2) Federal trade commission independent litigation authority**\nIf the Federal Trade Commission has reason to believe that a covered company violated this Act, the Federal Trade Commission may commence a civil action, in its own name by any of its attorneys designated by it for such purpose, to recover a civil penalty and seek other appropriate relief in a district court of the United States against the covered company.\n**(3) Parens patriae**\nAny attorney general of a State may bring a civil action in the name of such State for a violation of this Act as parens patriae on behalf of natural persons residing in such State, in any district court of the United States having jurisdiction of the defendant, and may secure any form of relief provided for in this section.\n##### (b) Suits by developers injured\n**(1) In general**\nExcept as provided in paragraph (3), any developer injured by reason of anything forbidden in this Act may sue therefor in any district court of the United States in the district in which the defendant resides or is found or has an agent, without respect to the amount in controversy, and shall recover threefold the damages by the developer sustained and the cost of suit, including a reasonable attorney\u2019s fee. The court may award under this paragraph, pursuant to a motion by such developer promptly made, simple interest on actual damages for the period beginning on the date of service of the pleading of the developer setting forth a claim under this Act and ending on the date of judgment, or for any shorter period therein, if the court finds that the award of such interest for such period is just in the circumstances. In determining whether an award of interest under this paragraph for any period is just in the circumstances, the court shall consider only\u2014\n**(A)**\nwhether the developer or the opposing party, or either party\u2019s representative, made motions or asserted claims or defenses so lacking in merit as to show that such party or representative acted intentionally for delay or otherwise acted in bad faith;\n**(B)**\nwhether, in the course of the action involved, the developer or the opposing party, or either party\u2019s representative, violated any applicable rule, statute, or court order providing for sanctions for dilatory behavior or otherwise providing for expeditious proceedings; and\n**(C)**\nwhether the developer or the opposing party, or either party\u2019s representative, engaged in conduct primarily for the purpose of delaying the litigation or increasing the cost thereof.\n**(2) Injunctive relief**\nExcept as provided in paragraph (3), any developer shall be entitled to sue for and have injunctive relief, in any court of the United States having jurisdiction over the parties, against threatened loss or damage by a violation of this Act, when and under the same conditions and principles as injunctive relief against threatened conduct that will cause loss or damage is granted by courts of equity, under the rules governing such proceedings, and upon the execution of proper bond against damages for an injunction improvidently granted and a showing that the danger of irreparable loss or damage is immediate, a preliminary injunction may issue. In any action under this paragraph in which the plaintiff substantially prevails, the court shall award the cost of suit, including a reasonable attorney\u2019s fee, to such plaintiff.\n**(3) Foreign state-owned enterprises**\nA developer of an app that is owned by, or under the control of, a foreign state may not bring an action under this subsection.\n#### 6. Reporting\nNot later than 3 years after the date of enactment of this Act, the Federal Trade Commission, the Comptroller General of the United States, and the Antitrust Division of the Department of Justice shall each separately review and provide an in-depth analysis of the impact of this Act on competition, innovation, barriers to entry, and concentrations of market power or market share after the date of enactment of this Act.\n#### 7. Rule of construction\nNothing in this Act may be construed\u2014\n**(1)**\nto limit\u2014\n**(A)**\nany authority of the Attorney General or the Federal Trade Commission under the antitrust laws (as defined in the first section of the Clayton Act ( 15 U.S.C. 12 )), the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ), or any other provision of law; or\n**(B)**\nthe application of any law;\n**(2)**\nto require\u2014\n**(A)**\na covered company to provide service under a hardware or software warranty for damage caused by third-party apps or app stores installed through means other than the app store of the covered company; or\n**(B)**\ncustomer service for the installation or operation of third-party apps or app stores described in subparagraph (A);\n**(3)**\nto prevent an action taken by a covered company that is reasonably tailored to protect the rights of third parties under section 106, 1101, 1201, or 1401 of title 17, United States Code, or rights actionable under sections 32 or 43 of the Act entitled An Act to provide for the registration and protection of trademarks used in commerce, to carry out the provisions of certain international conventions, and for other purposes , approved July 5, 1946 (commonly known as the Lanham Act or the Trademark Act of 1946 ) ( 15 U.S.C. 1114 , 1125), or corollary State law;\n**(4)**\nto require a covered company to license any intellectual property, including any trade secrets, owned by or licensed to the covered company;\n**(5)**\nto prevent a covered company from asserting preexisting rights of the covered company under intellectual property law to prevent the unlawful use of any intellectual property owned by or duly licensed to the covered company; or\n**(6)**\nto require a covered company to interoperate or share data with any person or business user that\u2014\n**(A)**\nis on any list maintained by the Federal Government by which entities are identified as limited or prohibited from engaging in economic transactions as part of United States sanctions or export control regimes;\n**(B)**\nis a foreign entity that has been identified by the Federal Government as a national security, intelligence, or law enforcement risk, including the Government of the People\u2019s Republic of China or the government of a foreign adversary (as defined in section 8(c) of the Secure and Trusted Communications Networks Act of 2019 ( 473 U.S.C. 1607(c) )); or\n**(C)**\nis engaged in illegal or fraudulent activity.\n#### 8. Severability\nIf any provision of this Act, or the application of such a provision to any person or circumstance, is held to be unconstitutional, the remaining provisions of this Act, and the application of such provisions to any person or circumstance shall not be affected thereby.\n#### 9. Effective date\nThis Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-06-24",
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
        "updateDate": "2025-07-15T10:35:58Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2153is.xml"
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
      "title": "Open App Markets Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Open App Markets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote competition and reduce gatekeeper power in the app economy, increase choice, improve quality, and reduce costs for consumers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:17Z"
    }
  ]
}
```
