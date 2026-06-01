# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/737?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/737
- Title: SCREEN Act
- Congress: 119
- Bill type: S
- Bill number: 737
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2026-04-07T17:54:44Z
- Update date including text: 2026-04-07T17:54:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/737",
    "number": "737",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "SCREEN Act",
    "type": "S",
    "updateDate": "2026-04-07T17:54:44Z",
    "updateDateIncludingText": "2026-04-07T17:54:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T16:43:57Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "UT"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "IN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s737is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 737\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Lee (for himself, Mr. Curtis , and Mr. Banks ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require certain interactive computer services to adopt and operate technology verification measures to ensure that users of the platform are not minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shielding Children's Retinas from Egregious Exposure on the Net Act or the SCREEN Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nOver the 3 decades preceding the date of enactment of this Act, Congress has passed several bills to protect minors from access to online pornographic content, including title V of the Telecommunications Act of 1996 ( Public Law 104\u2013104 ) (commonly known as the Communications Decency Act ), section 231 of the Communications Act of 1934 ( 47 U.S.C. 231 ) (commonly known as the Child Online Protection Act ), and the Children\u2019s Internet Protection Act (title XVII of division B of Public Law 106\u2013554 ).\n**(2)**\nWith the exception of the Children's Internet Protection Act (title XVII of division B of Public Law 106\u2013554 ), the Supreme Court of the United States has struck down the previous efforts of Congress to shield children from pornographic content, finding that such legislation constituted a compelling government interest but that it was not the least restrictive means to achieve such interest. In Ashcroft v. ACLU, 542 U.S. 656 (2004), the Court even suggested at the time that blocking and filtering software could conceivably be a primary alternative to the requirements passed by Congress.\n**(3)**\nIn the nearly 2 decades since the Supreme Court of the United States suggested the use of blocking and filtering software , such technology has proven to be ineffective in protecting minors from accessing online pornographic content. The Kaiser Family Foundation has found that filters do not work on 1 in 10 pornography sites accessed intentionally and 1 in 3 pornography sites that are accessed unintentionally. Further, it has been proven that children are able to bypass blocking and filtering software by employing strategic searches or measures to bypass the software completely.\n**(4)**\nAdditionally, Pew Research has revealed studies showing that only 39 percent of parents use blocking or filtering software for their minor\u2019s online activities, meaning that 61 percent of children only have restrictions on their internet access when they are at school or at a library.\n**(5)**\n17 States have now recognized pornography as a public health hazard that leads to a broad range of individual harms, societal harms, and public health impacts.\n**(6)**\nIt is estimated that 80 percent of minors between the ages of 12 to 17 have been exposed to pornography, with 54 percent of teenagers seeking it out. The internet is the most common source for minors to access pornography with pornographic websites receiving more web traffic in the United States than Twitter, Netflix, Pinterest, and LinkedIn combined.\n**(7)**\nExposure to online pornography has created unique psychological effects for minors, including anxiety, addiction, low self-esteem, body image disorders, an increase in problematic sexual activity at younger ages, and an increased desire among minors to engage in risky sexual behavior.\n**(8)**\nThe Supreme Court of the United States has recognized on multiple occasions that Congress has a compelling government interest to protect the physical and psychological well-being of minors, which includes shielding them from indecent content that may not necessarily be considered obscene by adult standards.\n**(9)**\nBecause blocking and filtering software has not produced the results envisioned nearly 2 decades ago, it is necessary for Congress to pursue alternative policies to enable the protection of the physical and psychological well-being of minors.\n**(10)**\nThe evolution of our technology has now enabled the use of age verification technology that is cost efficient, not unduly burdensome, and can be operated narrowly in a manner that ensures only adults have access to a website\u2019s online pornographic content.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nshielding minors from access to online pornographic content is a compelling government interest that protects the physical and psychological well-being of minors; and\n**(2)**\nrequiring interactive computer services that are in the business of creating, hosting, or making available pornographic content to enact technological measures that shield minors from accessing pornographic content on their platforms is the least restrictive means for Congress to achieve its compelling government interest.\n#### 3. Definitions\nIn this Act:\n**(1) Child pornography; minor**\nThe terms child pornography and minor have the meanings given those terms in section 2256 of title 18, United States Code.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered platform**\nThe term covered platform \u2014\n**(A)**\nmeans an entity\u2014\n**(i)**\nthat is an interactive computer service;\n**(ii)**\nthat\u2014\n**(I)**\nis engaged in interstate or foreign commerce; or\n**(II)**\npurposefully avails itself of the United States market or a portion thereof; and\n**(iii)**\nfor which it is in the regular course of the trade or business of the entity to create, host, or make available content that meets the definition of harmful to minors under paragraph (4) and that is provided by the entity, a user, or other information content provider, with the objective of earning a profit; and\n**(B)**\nincludes an entity described in subparagraph (A) regardless of whether\u2014\n**(i)**\nthe entity earns a profit on the activities described in subparagraph (A)(iii); or\n**(ii)**\ncreating, hosting, or making available content that meets the definition of harmful to minors under paragraph (4) is the sole source of income or principal business of the entity.\n**(4) Harmful to minors**\nThe term harmful to minors , with respect to a picture, image, graphic image file, film, videotape, or other visual depiction, means that the picture, image, graphic image file, film, videotape, or other depiction\u2014\n**(A)**\n**(i)**\ntaken as a whole and with respect to minors, appeals to the prurient interest in nudity, sex, or excretion;\n**(ii)**\ndepicts, describes, or represents, in a patently offensive way with respect to what is suitable for minors, an actual or simulated sexual act or sexual contact, actual or simulated normal or perverted sexual acts, or lewd exhibition of the genitals; and\n**(iii)**\ntaken as a whole, lacks serious, literary, artistic, political, or scientific value as to minors;\n**(B)**\nis obscene; or\n**(C)**\nis child pornography.\n**(5) Information content provider; interactive computer service**\nThe terms information content provider and interactive computer service have the meanings given those terms in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ).\n**(6) Sexual act; sexual contact**\nThe terms sexual act and sexual contact have the meanings given those terms in section 2246 of title 18, United States Code.\n**(7) Technology verification measure**\nThe term technology verification measure means technology that\u2014\n**(A)**\nemploys a system or process to determine whether it is more likely than not that a user of a covered platform is a minor; and\n**(B)**\nprevents access by minors to any content on a covered platform.\n**(8) Technology verification measure data**\nThe term technology verification measure data means information that\u2014\n**(A)**\nidentifies, is linked to, or is reasonably linkable to an individual or a device that identifies, is linked to, or is reasonably linkable to an individual;\n**(B)**\nis collected or processed for the purpose of fulfilling a request by an individual to access any content on a covered platform; and\n**(C)**\nis collected and processed solely for the purpose of utilizing a technology verification measure and meeting the obligations imposed under this Act.\n#### 4. Technology verification measures\n##### (a) Covered platform requirements\nBeginning on the date that is 1 year after the date of enactment of this Act, a covered platform shall adopt and utilize technology verification measures on the platform to ensure that\u2014\n**(1)**\nusers of the covered platform are not minors; and\n**(2)**\nminors are prevented from accessing any content on the covered platform that is harmful to minors.\n##### (b) Requirements for age verification measures\nIn order to comply with the requirement of subsection (a), the technology verification measures adopted and utilized by a covered platform shall do the following:\n**(1)**\nUse a technology verification measure in order to verify a user's age.\n**(2)**\nProvide that requiring a user to confirm that the user is not a minor shall not be sufficient to satisfy the requirement of subsection (a).\n**(3)**\nMake publicly available the verification process that the covered platform is employing to comply with the requirements under this Act.\n**(4)**\nSubject the Internet Protocol (IP) addresses, including known virtual proxy network IP addresses, of all users of a covered platform to the technology verification measure described in paragraph (1) unless the covered platform determines based on available technology that a user is not located within the United States.\n##### (c) Choice of verification measures\nA covered platform may choose the specific technology verification measures to employ for purposes of complying with subsection (a), provided that the technology verification measure employed by the covered platform meets the requirements of subsection (b) and prohibits a minor from accessing the platform or any information on the platform that is obscene, child pornography, or harmful to minors.\n##### (d) Use of third parties\nA covered platform may contract with a third party to employ technology verification measures for purposes of complying with subsection (a), but the use of such a third party shall not relieve the covered platform of its obligations under this Act or from liability under this Act.\n##### (e) Rule of construction\nNothing in this section shall be construed to require a covered platform to submit to the Commission any information that identifies, is linked to, or is reasonably linkable to a user of the covered platform or a device that identifies, is linked to, or is reasonably linkable to a user of the covered platform.\n##### (f) Technology verification measure data security\nA covered platform shall\u2014\n**(1)**\nestablish, implement, and maintain reasonable data security to\u2014\n**(A)**\nprotect the confidentiality, integrity, and accessibility of technology verification measure data collected by the covered platform or a third party employed by the covered platform; and\n**(B)**\nprotect such technology verification measure data against unauthorized access; and\n**(2)**\nretain the technology verification measure data for no longer than is reasonably necessary to utilize a technology verification measure or what is minimally necessary to demonstrate compliance with the obligations under this Act.\n#### 5. Consultation requirements\nIn enforcing the requirements under section 4, the Commission shall consult with the following individuals, including with respect to the applicable standards and metrics for making a determination on whether a user of a covered platform is not a minor:\n**(1)**\nIndividuals with experience in computer science and software engineering.\n**(2)**\nIndividuals with experience in\u2014\n**(A)**\nadvocating for online child safety; or\n**(B)**\nproviding services to minors who have been victimized by online child exploitation.\n**(3)**\nIndividuals with experience in consumer protection and online privacy.\n**(4)**\nIndividuals who supply technology verification measure products or have expertise in technology verification measure solutions.\n**(5)**\nIndividuals with experience in data security and cryptography.\n#### 6. Commission requirements\n##### (a) In general\nThe Commission shall\u2014\n**(1)**\nconduct regular audits of covered platforms to ensure compliance with the requirements of section 4;\n**(2)**\nmake public the terms and processes for the audits conducted under paragraph (1), including the processes for any third party conducting an audit on behalf of the Commission;\n**(3)**\nestablish a process for each covered platform to submit only such documents or other materials as are necessary for the Commission to ensure full compliance with the requirements of section 4 when conducting audits under this section; and\n**(4)**\nprescribe the appropriate documents, materials, or other measures required to demonstrate full compliance with the requirements of section 4.\n##### (b) Guidance\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Commission shall issue guidance to assist covered platforms in complying with the requirements of section 4.\n**(2) Limitations on guidance**\n**(A) In general**\nNo guidance issued by the Commission with respect to this Act shall confer any rights on any person, State, or locality, nor shall operate to bind the Commission or any person to the approach recommended in such guidance.\n**(B) Specificity in enforcement**\nIn any enforcement action brought pursuant to this Act, the Commission shall allege a specific violation of a provision of this Act.\n**(C) Enforcement actions**\nThe Commission may not base an enforcement action on, or execute a consent order based on, practices that are alleged to be inconsistent with any such guidelines, unless the practices allegedly violate a provision of this Act.\n#### 7. Enforcement\n##### (a) Unfair or deceptive act or practice\nA violation of section 4 shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the Commission\n**(1) In general**\nThe Commission shall enforce section 4 in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this title.\n**(2) Privileges and immunities**\nAny person who violates section 4 shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n#### 8. GAO report\nNot later than 2 years after the date on which covered platforms are required to comply with the requirement of section 4(a), the Comptroller General of the United States shall submit to Congress a report that includes\u2014\n**(1)**\nan analysis of the effectiveness of the technology verification measures required under such section;\n**(2)**\nan analysis of rates of compliance with such section among covered platforms;\n**(3)**\nan analysis of the data security measures used by covered platforms in the age verification process;\n**(4)**\nan analysis of the behavioral, economic, psychological, and societal effects of implementing technology verification measures;\n**(5)**\nrecommendations to the Commission on improving enforcement of section 4(a), if any; and\n**(6)**\nrecommendations to Congress on potential legislative improvements to this Act, if any.\n#### 9. Severability clause\nIf any provision of this Act, or the application of such a provision to any person or circumstance, is held to be unconstitutional, the remaining provisions of this Act, and the application of such provisions to any other person or circumstance, shall not be affected thereby.",
      "versionDate": "2025-02-26",
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
        "text": "Forwarded by Subcommittee to Full Committee in the Nature of a Substitute (Amended) by Voice Vote."
      },
      "number": "1623",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SCREEN Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child safety and welfare",
            "updateDate": "2026-01-13T19:13:48Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-01-13T19:13:48Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-01-13T19:13:48Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-01-13T19:13:48Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-07T17:54:44Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-01-13T19:13:48Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-01-13T19:13:48Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2026-01-13T19:13:48Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2026-01-13T19:13:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-13T20:40:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
    "originChamber": "Senate",
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
          "measure-id": "id119s737",
          "measure-number": "737",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-08-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s737v00",
            "update-date": "2025-08-12"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Shielding Children's Retinas from Egregious Exposure on the Net Act or the SCREEN Act</strong><br/><br/>This bill establishes age-verification requirements for commercial interactive computer services (e.g., websites) that make available content that is harmful to minors (e.g., content that appeals to the prurient interest in nudity or sex, is obscene, or is child pornography).<br/><br/>Specifically, the bill requires such services to adopt and utilize technology verification measures to ensure that (1) users of the service are not minors, and (2) minors are prevented from accessing any content on the service that is harmful to minors.<br/><br/>Additionally, such services must (1) use the technology to verify a user's age; (2) publish the verification process that the service uses; and (3) subject users'\u00a0Internet Protocol (IP) addresses, including known virtual proxy network (VPN) IP addresses, to the technology verification measures, unless the service determines a user is not located within the United States.<br/><br/>Covered services also must implement data security measures to protect information about individuals collected through the verification process.<br/><br/>The Federal Trade Commission must conduct regular audits of such services, issue guidance, and otherwise enforce the requirements of this bill.</p>"
        },
        "title": "SCREEN Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s737.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Shielding Children's Retinas from Egregious Exposure on the Net Act or the SCREEN Act</strong><br/><br/>This bill establishes age-verification requirements for commercial interactive computer services (e.g., websites) that make available content that is harmful to minors (e.g., content that appeals to the prurient interest in nudity or sex, is obscene, or is child pornography).<br/><br/>Specifically, the bill requires such services to adopt and utilize technology verification measures to ensure that (1) users of the service are not minors, and (2) minors are prevented from accessing any content on the service that is harmful to minors.<br/><br/>Additionally, such services must (1) use the technology to verify a user's age; (2) publish the verification process that the service uses; and (3) subject users'\u00a0Internet Protocol (IP) addresses, including known virtual proxy network (VPN) IP addresses, to the technology verification measures, unless the service determines a user is not located within the United States.<br/><br/>Covered services also must implement data security measures to protect information about individuals collected through the verification process.<br/><br/>The Federal Trade Commission must conduct regular audits of such services, issue guidance, and otherwise enforce the requirements of this bill.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119s737"
    },
    "title": "SCREEN Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Shielding Children's Retinas from Egregious Exposure on the Net Act or the SCREEN Act</strong><br/><br/>This bill establishes age-verification requirements for commercial interactive computer services (e.g., websites) that make available content that is harmful to minors (e.g., content that appeals to the prurient interest in nudity or sex, is obscene, or is child pornography).<br/><br/>Specifically, the bill requires such services to adopt and utilize technology verification measures to ensure that (1) users of the service are not minors, and (2) minors are prevented from accessing any content on the service that is harmful to minors.<br/><br/>Additionally, such services must (1) use the technology to verify a user's age; (2) publish the verification process that the service uses; and (3) subject users'\u00a0Internet Protocol (IP) addresses, including known virtual proxy network (VPN) IP addresses, to the technology verification measures, unless the service determines a user is not located within the United States.<br/><br/>Covered services also must implement data security measures to protect information about individuals collected through the verification process.<br/><br/>The Federal Trade Commission must conduct regular audits of such services, issue guidance, and otherwise enforce the requirements of this bill.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119s737"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s737is.xml"
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
      "title": "SCREEN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SCREEN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Shielding Children's Retinas from Egregious Exposure on the Net Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require certain interactive computer services to adopt and operate technology verification measures to ensure that users of the platform are not minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:27Z"
    }
  ]
}
```
