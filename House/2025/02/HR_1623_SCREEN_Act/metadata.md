# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1623?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1623
- Title: SCREEN Act
- Congress: 119
- Bill type: HR
- Bill number: 1623
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-04-07T17:53:48Z
- Update date including text: 2026-04-07T17:53:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-26 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee in the Nature of a Substitute (Amended) by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-26 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee in the Nature of a Substitute (Amended) by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1623",
    "number": "1623",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "SCREEN Act",
    "type": "HR",
    "updateDate": "2026-04-07T17:53:48Z",
    "updateDateIncludingText": "2026-04-07T17:53:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee in the Nature of a Substitute (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-11T21:40:59Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:40:46Z",
                "name": "Markup by"
              },
              {
                "date": "2025-02-26T21:40:34Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "OK"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "UT"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "AZ"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "AL"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TN"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TN"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "TN"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NC"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "IN"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "SC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "AL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "SC"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "FL"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "UT"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "WV"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "OK"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "UT"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1623ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1623\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mrs. Miller of Illinois (for herself, Mr. Van Drew , Mr. Brecheen , Mr. LaMalfa , Mr. Austin Scott of Georgia , Mr. Kennedy of Utah , Mr. Crane , Mr. Aderholt , Mr. Babin , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require certain interactive computer services to adopt and operate technology verification measures to ensure that users of the platform are not minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shielding Children's Retinas from Egregious Exposure on the Net Act or the SCREEN Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nOver the 3 decades preceding the date of enactment of this Act, Congress has passed several bills to protect minors from access to online pornographic content, including title V of the Telecommunications Act of 1996 ( Public Law 104\u2013104 ) (commonly known as the Communications Decency Act ), section 231 of the Communications Act of 1934 ( 47 U.S.C. 231 ) (commonly known as the Child Online Protection Act ), and the Children\u2019s Internet Protection Act (title XVII of division B of Public Law 106\u2013554 ).\n**(2)**\nWith the exception of the Children's Internet Protection Act (title XVII of division B of Public Law 106\u2013554 ), the Supreme Court of the United States has struck down the previous efforts of Congress to shield children from pornographic content, finding that such legislation constituted a compelling government interest but that it was not the least restrictive means to achieve such interest. In Ashcroft v. ACLU, 542 U.S. 656 (2004), the Court even suggested at the time that blocking and filtering software could conceivably be a primary alternative to the requirements passed by Congress.\n**(3)**\nIn the nearly 2 decades since the Supreme Court of the United States suggested the use of blocking and filtering software , such technology has proven to be ineffective in protecting minors from accessing online pornographic content. The Kaiser Family Foundation has found that filters do not work on 1 in 10 pornography sites accessed intentionally and 1 in 3 pornography sites that are accessed unintentionally. Further, it has been proven that children are able to bypass blocking and filtering software by employing strategic searches or measures to bypass the software completely.\n**(4)**\nAdditionally, Pew Research has revealed studies showing that only 39 percent of parents use blocking or filtering software for their minor\u2019s online activities, meaning that 61 percent of children only have restrictions on their internet access when they are at school or at a library.\n**(5)**\n17 States have now recognized pornography as a public health hazard that leads to a broad range of individual harms, societal harms, and public health impacts.\n**(6)**\nIt is estimated that 80 percent of minors between the ages of 12 to 17 have been exposed to pornography, with 54 percent of teenagers seeking it out. The internet is the most common source for minors to access pornography with pornographic websites receiving more web traffic in the United States than Twitter, Netflix, Pinterest, and LinkedIn combined.\n**(7)**\nExposure to online pornography has created unique psychological effects for minors, including anxiety, addiction, low self-esteem, body image disorders, an increase in problematic sexual activity at younger ages, and an increased desire among minors to engage in risky sexual behavior.\n**(8)**\nThe Supreme Court of the United States has recognized on multiple occasions that Congress has a compelling government interest to protect the physical and psychological well-being of minors, which includes shielding them from indecent content that may not necessarily be considered obscene by adult standards.\n**(9)**\nBecause blocking and filtering software has not produced the results envisioned nearly 2 decades ago, it is necessary for Congress to pursue alternative policies to enable the protection of the physical and psychological well-being of minors.\n**(10)**\nThe evolution of our technology has now enabled the use of age verification technology that is cost efficient, not unduly burdensome, and can be operated narrowly in a manner that ensures only adults have access to a website\u2019s online pornographic content.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nshielding minors from access to online pornographic content is a compelling government interest that protects the physical and psychological well-being of minors; and\n**(2)**\nrequiring interactive computer services that are in the business of creating, hosting, or making available pornographic content to enact technological measures that shield minors from accessing pornographic content on their platforms is the least restrictive means for Congress to achieve its compelling government interest.\n#### 3. Definitions\nIn this Act:\n**(1) Child pornography; minor**\nThe terms child pornography and minor have the meanings given those terms in section 2256 of title 18, United States Code.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered platform**\nThe term covered platform \u2014\n**(A)**\nmeans an entity\u2014\n**(i)**\nthat is an interactive computer service;\n**(ii)**\nthat\u2014\n**(I)**\nis engaged in interstate or foreign commerce; or\n**(II)**\npurposefully avails itself of the United States market or a portion thereof; and\n**(iii)**\nfor which it is in the regular course of the trade or business of the entity to create, host, or make available content that meets the definition of harmful to minors under paragraph (4) and that is provided by the entity, a user, or other information content provider, with the objective of earning a profit; and\n**(B)**\nincludes an entity described in subparagraph (A) regardless of whether\u2014\n**(i)**\nthe entity earns a profit on the activities described in subparagraph (A)(iii); or\n**(ii)**\ncreating, hosting, or making available content that meets the definition of harmful to minors under paragraph (4) is the sole source of income or principal business of the entity.\n**(4) Harmful to minors**\nThe term harmful to minors , with respect to a picture, image, graphic image file, film, videotape, or other visual depiction, means that the picture, image, graphic image file, film, videotape, or other depiction\u2014\n**(A)**\n**(i)**\ntaken as a whole and with respect to minors, appeals to the prurient interest in nudity, sex, or excretion;\n**(ii)**\ndepicts, describes, or represents, in a patently offensive way with respect to what is suitable for minors, an actual or simulated sexual act or sexual contact, actual or simulated normal or perverted sexual acts, or lewd exhibition of the genitals; and\n**(iii)**\ntaken as a whole, lacks serious, literary, artistic, political, or scientific value as to minors;\n**(B)**\nis obscene; or\n**(C)**\nis child pornography.\n**(5) Information content provider; interactive computer service**\nThe terms information content provider and interactive computer service have the meanings given those terms in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ).\n**(6) Sexual act; sexual contact**\nThe terms sexual act and sexual contact have the meanings given those terms in section 2246 of title 18, United States Code.\n**(7) Technology verification measure**\nThe term technology verification measure means technology that\u2014\n**(A)**\nemploys a system or process to determine whether it is more likely than not that a user of a covered platform is a minor; and\n**(B)**\nprevents access by minors to any content on a covered platform.\n**(8) Technology verification measure data**\nThe term technology verification measure data means information that\u2014\n**(A)**\nidentifies, is linked to, or is reasonably linkable to an individual or a device that identifies, is linked to, or is reasonably linkable to an individual;\n**(B)**\nis collected or processed for the purpose of fulfilling a request by an individual to access any content on a covered platform; and\n**(C)**\nis collected and processed solely for the purpose of utilizing a technology verification measure and meeting the obligations imposed under this Act.\n#### 4. Technology verification measures\n##### (a) Covered platform requirements\nBeginning on the date that is 1 year after the date of enactment of this Act, a covered platform shall adopt and utilize technology verification measures on the platform to ensure that\u2014\n**(1)**\nusers of the covered platform are not minors; and\n**(2)**\nminors are prevented from accessing any content on the covered platform that is harmful to minors.\n##### (b) Requirements for age verification measures\nIn order to comply with the requirement of subsection (a), the technology verification measures adopted and utilized by a covered platform shall do the following:\n**(1)**\nUse a technology verification measure in order to verify a user's age.\n**(2)**\nProvide that requiring a user to confirm that the user is not a minor shall not be sufficient to satisfy the requirement of subsection (a).\n**(3)**\nMake publicly available the verification process that the covered platform is employing to comply with the requirements under this Act.\n**(4)**\nSubject the Internet Protocol (IP) addresses, including known virtual proxy network IP addresses, of all users of a covered platform to the technology verification measure described in paragraph (1) unless the covered platform determines based on available technology that a user is not located within the United States.\n##### (c) Choice of verification measures\nA covered platform may choose the specific technology verification measures to employ for purposes of complying with subsection (a), provided that the technology verification measure employed by the covered platform meets the requirements of subsection (b) and prohibits a minor from accessing the platform or any information on the platform that is obscene, child pornography, or harmful to minors.\n##### (d) Use of third parties\nA covered platform may contract with a third party to employ technology verification measures for purposes of complying with subsection (a) but the use of such a third party shall not relieve the covered platform of its obligations under this Act or from liability under this Act.\n##### (e) Rule of construction\nNothing in this section shall be construed to require a covered platform to submit to the Commission any information that identifies, is linked to, or is reasonably linkable to a user of the covered platform or a device that identifies, is linked to, or is reasonably linkable to a user of the covered platform.\n##### (f) Technology verification measure data security\nA covered platform shall\u2014\n**(1)**\nestablish, implement, and maintain reasonable data security to\u2014\n**(A)**\nprotect the confidentiality, integrity, and accessibility of technology verification measure data collected by the covered platform or a third party employed by the covered platform; and\n**(B)**\nprotect such technology verification measure data against unauthorized access; and\n**(2)**\nretain the technology verification measure data for no longer than is reasonably necessary to utilize a technology verification measure or what is minimally necessary to demonstrate compliance with the obligations under this Act.\n#### 5. Consultation requirements\nIn enforcing the requirements under section 4, the Commission shall consult with the following individuals, including with respect to the applicable standards and metrics for making a determination on whether a user of a covered platform is not a minor:\n**(1)**\nIndividuals with experience in computer science and software engineering.\n**(2)**\nIndividuals with experience in\u2014\n**(A)**\nadvocating for online child safety; or\n**(B)**\nproviding services to minors who have been victimized by online child exploitation.\n**(3)**\nIndividuals with experience in consumer protection and online privacy.\n**(4)**\nIndividuals who supply technology verification measure products or have expertise in technology verification measure solutions.\n**(5)**\nIndividuals with experience in data security and cryptography.\n#### 6. Commission requirements\n##### (a) In general\nThe Commission shall\u2014\n**(1)**\nconduct regular audits of covered platforms to ensure compliance with the requirements of section 4;\n**(2)**\nmake public the terms and processes for the audits conducted under paragraph (1), including the processes for any third party conducting an audit on behalf of the Commission;\n**(3)**\nestablish a process for each covered platform to submit only such documents or other materials as are necessary for the Commission to ensure full compliance with the requirements of section 4 when conducting audits under this section; and\n**(4)**\nprescribe the appropriate documents, materials, or other measures required to demonstrate full compliance with the requirements of section 4.\n##### (b) Guidance\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Commission shall issue guidance to assist covered platforms in complying with the requirements of section 4.\n**(2) Limitations on guidance**\nNo guidance issued by the Commission with respect to this Act shall confer any rights on any person, State, or locality, nor shall operate to bind the Commission or any person to the approach recommended in such guidance. In any enforcement action brought pursuant to this Act, the Commission shall allege a specific violation of a provision of this Act. The Commission may not base an enforcement action on, or execute a consent order based on, practices that are alleged to be inconsistent with any such guidelines, unless the practices allegedly violate a provision of this Act.\n#### 7. Enforcement\n##### (a) Unfair or deceptive act or practice\nA violation of section 4 shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of the Commission\n**(1) In general**\nThe Commission shall enforce section 4 in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this title.\n**(2) Privileges and immunities**\nAny person who violates section 4 shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n#### 8. GAO report\nNot later than 2 years after the date on which covered platforms are required to comply with the requirement of section 4(a), the Comptroller General of the United States shall submit to Congress a report that includes\u2014\n**(1)**\nan analysis of the effectiveness of the technology verification measures required under such section;\n**(2)**\nan analysis of rates of compliance with such section among covered platforms;\n**(3)**\nan analysis of the data security measures used by covered platforms in the age verification process;\n**(4)**\nan analysis of the behavioral, economic, psychological, and societal effects of implementing technology verification measures;\n**(5)**\nrecommendations to the Commission on improving enforcement of section 4(a), if any; and\n**(6)**\nrecommendations to Congress on potential legislative improvements to this Act, if any.\n#### 9. Severability clause\nIf any provision of this Act, or the application of such a provision to any person or circumstance, is held to be unconstitutional, the remaining provisions of this Act, and the application of such provisions to any other person or circumstance, shall not be affected thereby.",
      "versionDate": "2025-02-26",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-26",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "737",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SCREEN Act",
      "type": "S"
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
            "updateDate": "2026-01-13T19:12:39Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-01-13T19:12:52Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-01-13T19:12:39Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-01-13T19:12:39Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-07T17:53:48Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-01-13T19:12:39Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-01-13T19:12:39Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2026-01-13T19:12:45Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2026-01-13T19:12:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-13T20:24:29Z"
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
          "measure-id": "id119hr1623",
          "measure-number": "1623",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-09-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1623v00",
            "update-date": "2025-09-11"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Shielding Children's Retinas from Egregious Exposure on the Net Act or the SCREEN Act</strong><br/><br/>This bill establishes age-verification requirements for commercial interactive computer services (e.g., websites) that make available content that is harmful to minors (e.g., content that appeals to the prurient interest in nudity or sex, is obscene, or is child pornography).<br/><br/>Specifically, the bill requires such services to adopt and utilize technology verification measures to ensure that (1) users of the service are not minors, and (2) minors are prevented from accessing any content on the service that is harmful to minors.<br/><br/>Additionally, such services must (1) use the technology to verify a user's age; (2) publish the verification process that the service uses; and (3) subject users'\u00a0Internet Protocol (IP) addresses, including known virtual proxy network (VPN) IP addresses, to the technology verification measures, unless the service determines a user is not located within the United States.<br/><br/>Covered services also must implement data security measures to protect information about individuals collected through the verification process.<br/><br/>The Federal Trade Commission must conduct regular audits of such services, issue guidance, and otherwise enforce the requirements of this bill.</p>"
        },
        "title": "SCREEN Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1623.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Shielding Children's Retinas from Egregious Exposure on the Net Act or the SCREEN Act</strong><br/><br/>This bill establishes age-verification requirements for commercial interactive computer services (e.g., websites) that make available content that is harmful to minors (e.g., content that appeals to the prurient interest in nudity or sex, is obscene, or is child pornography).<br/><br/>Specifically, the bill requires such services to adopt and utilize technology verification measures to ensure that (1) users of the service are not minors, and (2) minors are prevented from accessing any content on the service that is harmful to minors.<br/><br/>Additionally, such services must (1) use the technology to verify a user's age; (2) publish the verification process that the service uses; and (3) subject users'\u00a0Internet Protocol (IP) addresses, including known virtual proxy network (VPN) IP addresses, to the technology verification measures, unless the service determines a user is not located within the United States.<br/><br/>Covered services also must implement data security measures to protect information about individuals collected through the verification process.<br/><br/>The Federal Trade Commission must conduct regular audits of such services, issue guidance, and otherwise enforce the requirements of this bill.</p>",
      "updateDate": "2025-09-11",
      "versionCode": "id119hr1623"
    },
    "title": "SCREEN Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Shielding Children's Retinas from Egregious Exposure on the Net Act or the SCREEN Act</strong><br/><br/>This bill establishes age-verification requirements for commercial interactive computer services (e.g., websites) that make available content that is harmful to minors (e.g., content that appeals to the prurient interest in nudity or sex, is obscene, or is child pornography).<br/><br/>Specifically, the bill requires such services to adopt and utilize technology verification measures to ensure that (1) users of the service are not minors, and (2) minors are prevented from accessing any content on the service that is harmful to minors.<br/><br/>Additionally, such services must (1) use the technology to verify a user's age; (2) publish the verification process that the service uses; and (3) subject users'\u00a0Internet Protocol (IP) addresses, including known virtual proxy network (VPN) IP addresses, to the technology verification measures, unless the service determines a user is not located within the United States.<br/><br/>Covered services also must implement data security measures to protect information about individuals collected through the verification process.<br/><br/>The Federal Trade Commission must conduct regular audits of such services, issue guidance, and otherwise enforce the requirements of this bill.</p>",
      "updateDate": "2025-09-11",
      "versionCode": "id119hr1623"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1623ih.xml"
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
      "title": "SCREEN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCREEN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shielding Children's Retinas from Egregious Exposure on the Net Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require certain interactive computer services to adopt and operate technology verification measures to ensure that users of the platform are not minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:26Z"
    }
  ]
}
```
