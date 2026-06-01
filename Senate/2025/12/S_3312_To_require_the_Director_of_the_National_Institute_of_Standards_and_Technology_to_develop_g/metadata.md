# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3312?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3312
- Title: Quantum Readiness and Innovation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3312
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2026-01-06T18:57:35Z
- Update date including text: 2026-01-06T18:57:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3312",
    "number": "3312",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Quantum Readiness and Innovation Act of 2025",
    "type": "S",
    "updateDate": "2026-01-06T18:57:35Z",
    "updateDateIncludingText": "2026-01-06T18:57:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T21:55:43Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3312is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3312\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mr. Peters (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Director of the National Institute of Standards and Technology to develop guidance for upgrading information systems to post-quantum cryptography, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quantum Readiness and Innovation Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Classical computer; quantum computer**\nThe terms classical computer and quantum computer have the meanings given such terms in section 3 of the Quantum Computing Cybersecurity Preparedness Act ( Public Law 117\u2013260 ; 6 U.S.C. 1526 note).\n**(3) Critical infrastructure sectors**\nThe term critical infrastructure sectors means the critical infrastructure sectors defined in the National Security Memorandum on Critical Infrastructure Security and Resilience (NSM\u201322), dated April 30, 2024.\n**(4) High-impact system**\nThe term high-impact system means a Federal information system that holds sensitive information, the loss of which would be categorized as high impact under Federal Information Processing Standards Publication 199 (relating to standards for security categorization of Federal information and information systems), as in effect on the day before the date of the enactment of this Act.\n**(5) Post-quantum cryptography**\nThe term post-quantum cryptography \u2014\n**(A)**\nmeans those cryptographic algorithms or methods that are assessed not to be specifically vulnerable to attack by either a quantum computer or classical computer; and\n**(B)**\nincludes\u2014\n**(i)**\nthe lattice-based digital signature algorithm specified in National Institute of Standards and Technology Federal Information Processing Standards Publication 204 (dated August 13, 2024; relating to Module-Lattice-Based Digital Signature Standard), or any successor standard;\n**(ii)**\nthe module-lattice-based key encapsulation mechanism specified in National Institute of Standards and Technology Federal Information Processing Standards Publication 203 (dated August 13, 2024; relating to Module-Lattice-Based Key-Encapsulation Mechanism Standard), or any successor standard; and\n**(iii)**\nany cryptographic algorithm or method implemented in accordance with National Institute of Standards and Technology Federal Information Processing Standard Publication 140\u20133 (dated March 22, 2019; relating to Security Requirements for Cryptographic Modules), or any successor standard, operating within a zero trust architecture as described in National Institute of Standards and Technology Special Publication 800\u2013207 (dated August 2020; relating to Zero Trust Architecture), or any successor standard.\n**(6) Sector risk management agency**\nThe term sector risk management agency has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ).\n#### 3. Guidance on upgrading to post-quantum cryptography\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Director of the National Institute of Standards and Technology, in consultation with the Director of the Office of Science and Technology Policy, shall establish guidance for upgrading information systems to post-quantum cryptography, including guidance that is specifically tailored for critical infrastructure sectors.\n##### (b) Requirement\nThe guidance established pursuant to subsection (a) shall include standards and selection criteria to guide the procurement and deployment of commercial solutions for an entity seeking to upgrade to post-quantum cryptography.\n##### (c) Dissemination of guidance\n**(1) In general**\nThe Director of the National Institute of Standards and Technology shall make available to entities in the private sector the guidance established under subsection (a).\n**(2) Special Publications**\nThe Director may satisfy the requirement under paragraph (1) through the publication of Special Publications.\n##### (d) Coordination and assistance for industry-Led assessments of adoption of guidance\n**(1) In general**\nIf an industry sector representative, who is part of the Quantum Economic Development Consortium, decides to carry out an assessment of the adoption by the industry sector of the guidance established under subsection (a), the Director of the National Institute of Standards and Technology shall offer to collaborate on such assessment with such representative.\n**(2) Technical Assistance and Interoperability Frameworks**\nIf requested by the representative described in paragraph (1), the Director of the National Institute of Standards and Technology shall support the assessment by providing\u2014\n**(A)**\ntechnical and administrative support;\n**(B)**\ntest beds to support the assessment; and\n**(C)**\ninteroperability frameworks.\n**(3) Coordination Assistance**\nThe Director of the National Institute of Standards and Technology may support an assessment described in paragraph (1) by coordinating between stakeholders as the Director considers necessary.\n#### 4. Strategy for Federal agency upgrade to post-quantum cryptography\n##### (a) National Quantum Cybersecurity Upgrade Strategy\nNot later than 360 days after the date of the enactment of this Act, the Director of the Office of Science and Technology Policy, in coordination with the Director of the National Institute of Standards and Technology and in consultation with the Quantum Economic Development Consortium, shall develop a National Quantum Cybersecurity Upgrade Strategy that includes the following:\n**(1)**\nA definition of a cryptographically relevant quantum computer.\n**(2)**\nRecommended standards to apply to determine whether a quantum computer meets such definition, including\u2014\n**(A)**\nthe characteristics of such computers; and\n**(B)**\nthe particular point at which such computers are capable of attacking real world systems that classical computers are unable to attack.\n**(3)**\nGuidelines for assessing the urgency of upgrading to post-quantum cryptography for each Federal agency relative to\u2014\n**(A)**\nthe critical functions of each agency; and\n**(B)**\nthe risk each agency faces should a cryptographically relevant quantum computer attack a system operated by the agency.\n**(4)**\nRecommended performance measures for upgrading to post-quantum cryptography for the following tasks:\n**(A)**\nPreparation for upgrading to post-quantum cryptography, including\u2014\n**(i)**\nthe adoption of hardware integrating quantum-resistant cryptographic algorithms; and\n**(ii)**\nthe deployment of software-only post-quantum cryptography overlays that meet or exceed security standards set forth in the Federal Information Processing Standards issued by the National Institute of Standards and Technology.\n**(B)**\nEstablishment of a baseline understanding of the data inventory, including through the use of automated tools to identify assets.\n**(C)**\nPlanning and execution of post-quantum cryptographic solutions, including ensuring that data at rest and in motion is subject to appropriate protections.\n**(D)**\nMonitoring and evaluating the success of the upgrade and assessing the security of the system.\n**(5)**\nA plan for implementing the above performance measures, including evaluating and monitoring entities that are at high risk of quantum attacks, including sector risk management agencies.\n##### (b) Post-Quantum voluntary pilot program\n**(1) In general**\nNot later than 360 days after the date of the enactment of this Act, the Director of the Office of Science and Technology Policy shall establish a pilot program to provide planning, technical, and any other support the Director considers appropriate to any covered entity that elects to participate in the program for the purpose of upgrading the systems of such covered entity to post-quantum cryptography.\n**(2) High risk entities**\nThe Director shall encourage any covered entity that is at high risk of quantum attack to participate in the pilot program established under paragraph (1).\n**(3) Requirements**\nUnder the pilot program established under paragraph (1)\u2014\n**(A)**\nnot later than 18 months after the date of the establishment of the program, not fewer than 1 high-impact system of any covered entity participating in the program shall be upgraded to post-quantum cryptography in accordance with the recommended performance measures described in subsection (a)(4); and\n**(B)**\nupon completion of the initial upgrade under subparagraph (A), the head of the covered entity may upgrade\u2014\n**(i)**\n1 additional system in accordance with such performance measures; or\n**(ii)**\n2 or more systems in accordance with such performance measures if the head notifies the Director before initiating such upgrade.\n**(4) Pilot program reports**\n**(A) In general**\nFor each covered entity participating in the program established under paragraph (1), the Director, in coordination with the head of such entity, shall submit to the appropriate congressional committees\u2014\n**(i)**\nan initial report not later than 180 days after the date on which the initial upgrade is completed under paragraph (3)(A); and\n**(ii)**\nan updated report annually until such date as the Director considers appropriate.\n**(B) Elements**\nEach report submitted under subparagraph (A) shall describe\u2014\n**(i)**\nthe actions of the head of the covered entity in carrying out the program; and\n**(ii)**\nany planning, technical, or other support that the Director provided to the head of the covered entity through the program.\n**(5) Covered entity defined**\nIn this subsection, the term covered entity means\u2014\n**(A)**\na sector risk management agency;\n**(B)**\na Federal agency; or\n**(C)**\na mission partner of a Federal agency.\n##### (c) Report to Congress\nNot later than 360 days after the date of the enactment of this Act, the Director of the Office of Science and Technology Policy shall submit to the appropriate congressional committees a report that includes the National Quantum Cybersecurity Upgrade Strategy developed under subsection (a) and a description of the pilot program established pursuant to subsection (b)(1).",
      "versionDate": "2025-12-02",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-06T18:57:34Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3312is.xml"
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
      "title": "Quantum Readiness and Innovation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-20T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Quantum Readiness and Innovation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the National Institute of Standards and Technology to develop guidance for upgrading information systems to post-quantum cryptography, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T05:48:17Z"
    }
  ]
}
```
