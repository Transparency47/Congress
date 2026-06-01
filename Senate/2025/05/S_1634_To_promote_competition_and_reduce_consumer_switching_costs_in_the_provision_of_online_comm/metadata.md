# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1634?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1634
- Title: ACCESS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1634
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-06-09T14:43:18Z
- Update date including text: 2025-06-09T14:43:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1634",
    "number": "1634",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "ACCESS Act of 2025",
    "type": "S",
    "updateDate": "2025-06-09T14:43:18Z",
    "updateDateIncludingText": "2025-06-09T14:43:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T18:54:50Z",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "MO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1634is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1634\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Warner (for himself, Mr. Hawley , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo promote competition and reduce consumer switching costs in the provision of online communications services.\n#### 1. Short title\nThis Act may be cited as the Augmenting Compatibility and Competition by Enabling Service Switching Act of 2025 or the ACCESS Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Communications provider**\nThe term communications provider means a consumer-facing communications and information services provider.\n**(3) Competing communications provider**\nThe term competing communications provider , with respect to a large communications platform provider, means another communications provider offering, or planning to offer, similar products or services to consumers.\n**(4) Competing communications service**\nThe term competing communications service , with respect to a large communications platform, means a similar product or service provided by a competing communications provider.\n**(5) Custodial third-party agent**\nThe term custodial third-party agent means an entity that is duly authorized by a user to interact with a large communications platform provider on that user\u2019s behalf to manage the user\u2019s online interactions, content, and account settings.\n**(6) Interoperability interface**\nThe term interoperability interface means an electronic interface maintained by a large communications platform for purposes of achieving interoperability.\n**(7) Large communications platform**\nThe term large communications platform means a product or service provided by a communications provider that\u2014\n**(A)**\ngenerates income, directly or indirectly, from the collection, processing, sale, or sharing of user data; and\n**(B)**\nhas more than 100,000,000 monthly active users in the United States.\n**(8) Large communications platform provider**\nThe term large communications platform provider means a communications provider that provides, manages, or controls a large communications platform.\n**(9) User data**\n**(A) In general**\nThe term user data means information that is\u2014\n**(i)**\ncollected directly by a communications provider; and\n**(ii)**\nlinked, or reasonably linkable, to a specific person.\n**(B) Exclusion**\nThe term user data does not include information that is rendered unusable, unreadable, de-identified, or anonymized.\n#### 3. Portability\n##### (a) General duty of large communications platform providers\nA large communications platform provider shall, for each large communications platform it operates, maintain a set of transparent, third-party-accessible interfaces (including application programming interfaces) to initiate the secure transfer of user data to a user, or to a competing communications provider acting at the direction of a user, in a structured, commonly used, and machine-readable format.\n##### (b) General duty of competing communications providers\nA competing communications provider that receives ported user data from a large communications platform provider shall reasonably secure any user data it acquires.\n##### (c) Exemption for certain services\nThe obligations under this section shall not apply to a product or service by which a large communications platform provider does not generate any income or other compensation, directly or indirectly, from collecting, using, or sharing user data.\n#### 4. Interoperability\n##### (a) General duty of large communications platform providers\nA large communications platform provider shall, for each large communications platform it operates, maintain a set of transparent, third-party-accessible interfaces (including application programming interfaces) to facilitate and maintain technically compatible, interoperable communications with a user of a competing communications provider.\n##### (b) General duty of competing communications providers\nA competing communications provider that accesses an interoperability interface of a large communications platform provider shall reasonably secure any user data it acquires, processes, or transmits.\n##### (c) Interoperability obligations for large communications platform providers\n**(1) In general**\nIn order to achieve interoperability under subsection (a), a large communications platform provider shall fulfill the duties under paragraphs (2) through (6) of this subsection.\n**(2) Non-discrimination**\n**(A) In general**\nA large communications platform provider shall facilitate and maintain interoperability with competing communications services for each of its large communications platforms through an interoperability interface, based on fair, reasonable, and nondiscriminatory terms.\n**(B) Reasonable thresholds, access standards, and fees**\n**(i) In general**\nA large communications platform provider may establish reasonable thresholds related to the frequency, nature, and volume of requests by a competing communications provider to access resources maintained by the large communications platform provider, beyond which the large communications platform provider may assess a reasonable fee for such access.\n**(ii) Usage expectations**\nA large communications platform provider may establish fair, reasonable, and nondiscriminatory usage expectations to govern access by competing communications providers, including fees or penalties for providers that exceed those usage expectations.\n**(iii) Limitation on fees and usage expectations**\nAny fees, penalties, or usage expectations assessed under clauses (i) and (ii) shall be reasonably proportional to the cost, complexity, and risk to the large communications platform provider of providing such access.\n**(iv) Notice**\nA large communications platform provider shall provide public notice of any fees, penalties, or usage expectations that may be established under clauses (i) and (ii), including reasonable advance notice of any changes.\n**(v) Security and privacy standards**\nA large communications platform provider shall, consistent with industry best practices, set privacy and security standards for access by competing communications services to the extent reasonably necessary to address a threat to the large communications platform or user data, and shall report any suspected violations of those standards to the Commission.\n**(C) Prohibited changes to interfaces**\nA change to an interoperability interface or terms of use made with the purpose, or substantial effect, of unreasonably denying access or undermining interoperability for competing communications services shall be considered a violation of the duty under subparagraph (A) to facilitate and maintain interoperability based on fair, reasonable, and nondiscriminatory terms.\n**(3) Functional equivalence**\nA large communications platform provider that maintains interoperability between its own large communications platform and other products, services, or affiliated offerings of such provider shall offer a functionally equivalent version of that interface to competing communications services.\n**(4) Interface information**\n**(A) In general**\nNot later than 120 days after the date of enactment of this Act, a large communications platform provider shall disclose to competing communications providers complete and accurate documentation describing access to the interoperability interface required under this section.\n**(B) Contents**\nThe documentation required under subparagraph (A)\u2014\n**(i)**\nis limited to interface documentation necessary to achieve development and operation of interoperable products and services; and\n**(ii)**\ndoes not require the disclosure of the source code of a large communications platform.\n**(5) Notice of changes**\nA large communications platform provider shall provide reasonable advance notice to a competing communications provider, which may be provided through public notice, of any change to an interoperability interface maintained by the large communications platform provider that will affect the interoperability of a competing communications service.\n**(6) Non-commercialization by a large communications platform provider**\nA large communications platform provider may not collect, use, or share user data obtained from a competing communications service through the interoperability interface except for the purposes of safeguarding the privacy and security of such information or maintaining interoperability of services.\n##### (d) Non-Commercialization by a competing communications provider\nA competing communications provider that accesses an interoperability interface may not collect, use, or share user data obtained from a large communications platform provider through the interoperability interface except for the purposes of safeguarding the privacy and security of such information or maintaining interoperability of services.\n##### (e) Exemption for certain services\nThe obligations under this section shall not apply to a product or service by which a large communications platform provider does not generate any income or other compensation, directly or indirectly, from collecting, using, or sharing user data.\n#### 5. Delegatability\n##### (a) General duty of large communications platform providers\nA large communications platform provider shall maintain a set of transparent third-party-accessible interfaces by which a user may delegate a custodial third-party agent to manage the user\u2019s online interactions, content, and account settings on a large communications platform on the same terms as a user.\n##### (b) Authentication\nNot later than 180 days after the date of enactment of this Act, the Commission shall establish rules and procedures to facilitate a custodial third-party agent\u2019s ability to obtain access pursuant to subsection (a) in a way that ensures that a request for access on behalf of a user is a verifiable request.\n##### (c) Registration with the Commission\nA custodial third-party agent shall register with the Commission as a condition of, and prior to, accessing an interface described in subsection (a).\n##### (d) Deregistration by the Commission\nThe Commission shall establish rules and procedures to deregister a custodial third-party agent that the Commission determines has violated the duties established in this section.\n##### (e) Revocation of access rights\nA large communications platform provider may revoke or deny access for any custodial third-party agent that\u2014\n**(1)**\nfails to register with the Commission; or\n**(2)**\nrepeatedly facilitates fraudulent or malicious activity.\n##### (f) Duties of a custodial third-Party agent\nA custodial third-party agent\u2014\n**(1)**\nshall reasonably safeguard the privacy and security of user data provided to it by a user, or accessed on a user\u2019s behalf;\n**(2)**\nshall not access or manage a user\u2019s online interactions, content, or account settings in any way that\u2014\n**(A)**\nwill benefit the custodial third-party agent to the detriment of the user;\n**(B)**\nwill result in any reasonably foreseeable harm to the user; or\n**(C)**\nis inconsistent with the directions or reasonable expectations of the user; and\n**(3)**\nshall not collect, use, or share any user data provided to it by a user, or accessed on a user\u2019s behalf, for the commercial benefit of the custodial third-party agent.\n##### (g) Fees\nA custodial third-party agent may charge users a fee for the provision of the products or services described in subsection (a).\n##### (h) Extent of access rights\nNothing in this section shall be construed to confer greater rights of access for a custodial third-party agent to a large communications platform than are accessible to a user.\n#### 6. Implementation and enforcement\n##### (a) Regulations\nNot later than 1 year after the date of enactment of this Act, the Commission shall promulgate regulations to implement section 4(c)(2)(B)(v) and subsections (b), (c), and (d) of section 5.\n##### (b) Authentication\nNot later than 180 days after the date of enactment of this Act, the Commission, in consultation with relevant industry stakeholders, shall establish rules and procedures to facilitate the verification of the validity of requests from users and competing communications providers to obtain user data under sections 3(a) and 4(a).\n##### (c) Technical standards\nNot later than 180 days after the date of enactment of this Act, the Director of the National Institute of Standards and Technology shall develop and publish model technical standards by which to make interoperable popular classes of communications or information services, including\u2014\n**(1)**\nonline messaging;\n**(2)**\nmultimedia sharing; and\n**(3)**\nsocial networking.\n##### (d) Compliance assessment\nThe Commission shall regularly assess compliance by large communications platform providers with the provisions of this Act.\n##### (e) Complaints\nThe Commission shall establish procedures under which a user, a large communications platform provider, a competing communications provider, and a custodial third-party agent may file a complaint alleging that a large communications platform provider, a competing communication provider, or a custodial third-party agent has violated this Act.\n##### (f) Enforcement\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act, or regulations enacted pursuant to this Act, shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of commission**\n**(A) In general**\nExcept as provided in subparagraph (C), the Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nExcept as provided in subparagraph (C), any person who violates section 3 shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Nonprofit organizations and common carriers**\nNotwithstanding section 4 or 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 44 , 45(a)(2)) or any jurisdictional limitation of the Commission, the Commission shall also enforce this Act, in the same manner provided in subparagraphs (A) and (B) of this paragraph, with respect to common carriers subject to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ).\n**(D) Fines**\nIn assessing any fine for a violation of this Act, the Commission shall consider each individual user affected by a violation of this Act as an individual violation.\n##### (g) Reliance on open standards\nAny large communications platform provider that establishes and maintains interoperability through an open standard established under subsection (c) shall be entitled to a rebuttable presumption of providing access on fair, reasonable, and nondiscriminatory terms.\n##### (h) Preemption\nThe provisions of this Act shall preempt any State law only to the extent that such State law is inconsistent with the provisions of this Act.\n##### (i) Effective date\nThis Act shall take effect on the date on which the Commission promulgates regulations under subsection (a).\n#### 7. Relation to other laws\nNothing in this Act shall be construed to modify, limit, or supersede the operation of any privacy or security provision in\u2014\n**(1)**\nsection 552a of title 5, United States Code (commonly known as the Privacy Act of 1974 );\n**(2)**\nthe Right to Financial Privacy Act of 1978 ( 12 U.S.C. 3401 et seq. );\n**(3)**\nthe Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. );\n**(4)**\nthe Fair Debt Collection Practices Act ( 15 U.S.C. 1692 et seq. );\n**(5)**\nthe Children's Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 et seq. );\n**(6)**\ntitle V of the Gramm-Leach-Bliley Act ( 15 U.S.C. 6801 et seq. );\n**(7)**\nchapters 119, 123, and 206 of title 18, United States Code;\n**(8)**\nsection 444 of the General Education Provisions Act ( 20 U.S.C. 1232g ) (commonly referred to as the Family Educational Rights and Privacy Act of 1974 );\n**(9)**\nsection 445 of the General Education Provisions Act ( 20 U.S.C. 1232h );\n**(10)**\nthe Privacy Protection Act of 1980 ( 42 U.S.C. 2000aa et seq. );\n**(11)**\nthe regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1320d\u20132 note), as those regulations relate to\u2014\n**(A)**\na person described in section 1172(a) of the Social Security Act ( 42 U.S.C. 1320d\u20131(a) ); or\n**(B)**\ntransactions referred to in section 1173(a)(1) of the Social Security Act ( 42 U.S.C. 1320d\u20132(a)(1) );\n**(12)**\nthe Communications Assistance for Law Enforcement Act ( 47 U.S.C. 1001 et seq. );\n**(13)**\nsections 222 and 227 of the Communications Act of 1934 ( 47 U.S.C. 222 , 227); or\n**(14)**\nany other privacy or security provision of Federal law.",
      "versionDate": "2025-05-07",
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
        "updateDate": "2025-06-09T14:43:18Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1634is.xml"
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
      "title": "ACCESS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ACCESS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Augmenting Compatibility and Competition by Enabling Service Switching Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote competition and reduce consumer switching costs in the provision of online communications services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:18:17Z"
    }
  ]
}
```
