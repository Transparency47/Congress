# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1212?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1212
- Title: Countering Online Radicalization and Terrorism Act
- Congress: 119
- Bill type: HR
- Bill number: 1212
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-12-10T09:06:02Z
- Update date including text: 2025-12-10T09:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-11 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-11 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1212",
    "number": "1212",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Countering Online Radicalization and Terrorism Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:06:02Z",
    "updateDateIncludingText": "2025-12-10T09:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-11T18:17:14Z",
              "name": "Referred to"
            }
          },
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "CA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "CO"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "IA"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1212ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1212\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Pfluger (for himself, Mr. Panetta , Mr. Weber of Texas , and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo require the Secretary of Homeland Security to conduct annual assessments on terrorism threats to the United States posed by terrorist organizations utilizing foreign cloud-based mobile or desktop messaging applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Countering Online Radicalization and Terrorism Act .\n#### 2. Sense of Congress regarding the use of foreign cloud-based mobile and desktop messaging applications for terrorist activity\nIt is the sense of Congress that\u2014\n**(1)**\nthe heightened terrorism threat landscape and the increasing utilization of foreign cloud-based mobile and desktop messaging applications by terrorist organizations represent a national security threat, and the challenges posed by such threat are not well understood; and\n**(2)**\nthe Department of Homeland Security, in consultation with the Office of the Director of National Intelligence, must take steps to recognize, assess, and address such threat, thereby reducing risks to the people of the United States.\n#### 3. Annual assessments on terrorism threats to the United States posed by terrorist organizations utilizing foreign cloud-based mobile and desktop messaging applications\n##### (a) Assessments\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act and annually thereafter for five years, the Secretary of Homeland Security, in consultation with the Director of National Intelligence, shall submit to the appropriate congressional committees an assessment of terrorism threats to the United States posed by terrorist organizations utilizing foreign cloud-based mobile or desktop messaging applications.\n**(2) Contents**\nThe terrorism threat assessments under paragraph (1) shall address the following:\n**(A)**\nIn the first such assessment, an analysis of incidents in which terrorist organizations have utilized foreign cloud-based mobile and desktop messaging applications to facilitate the ability to radicalize and recruit individuals.\n**(B)**\nInformation related to online payment features of foreign cloud-based mobile and desktop messaging applications, and how such features provide monetary support to terrorist organizations.\n**(C)**\nRecommendations on appropriate measures to address terrorism threats to the United States posed by terrorist organizations utilizing foreign cloud-based mobile or desktop messaging applications.\n**(3) Coordination**\nEach terrorism threat assessment under paragraph (1)\u2014\n**(A)**\nshall be coordinated with the Office of the General Counsel, the Privacy Office, and the Office of for Civil Rights and Civil Liberties of the Department of Homeland Security prior to release outside the Department to ensure each such assessment complies with applicable law and protects individuals\u2019 privacy, civil rights, and civil liberties, and\n**(B)**\nmay be informed by existing products, as appropriate.\n**(4) Form**\nEach terrorism threat assessment under paragraph (1) shall be submitted in unclassified form, but may include a classified annex only for the protection of intelligence sources and methods relating to the matters contained in such assessment. The Secretary of Homeland Security shall post on a publicly available website of the Department of Homeland Security the unclassified portion of each such assessment.\n**(5) Briefing**\nNot later than 30 days after the submission of each terrorism threat assessment under paragraph (1), the Secretary of Homeland Security shall brief the appropriate congressional committees regarding each such assessment. The head of any other relevant Federal department or agency shall join the Secretary for any such briefing if any such committee, in consultation with the Secretary, determines such is appropriate.\n**(6) Appropriate congressional committees**\nIn this subsection, the term appropriate congressional committees means the Committee on Homeland Security and the Permanent Select Committee on Intelligence of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Select Committee on Intelligence of the Senate.\n##### (b) Information sharing\nThe Secretary of Homeland Security shall review information relating to terrorism threats to the United States posed by terrorist organizations utilizing foreign cloud-based mobile or desktop messaging applications that is gathered by State and local fusion centers and the National Network of Fusion Centers, and incorporate such information, as appropriate, into the Department of Homeland Security\u2019s own information relating to such. The Secretary shall ensure the dissemination to State and local fusion centers and the National Network of Fusion Centers of such information.\n##### (c) Definitions\nIn this section:\n**(1) Foreign cloud-based mobile or desktop messaging applications**\n**(A) In general**\nThe term foreign cloud-based mobile or desktop messaging applications includes any application specified in subparagraph (B) that has a connection, relationship, or other association with or to any of the following:\n**(i)**\nA foreign adversary (as such term is defined in section 7.2 of subpart A of part 7 of subtitle A of title 15, Code of Federal Regulations).\n**(ii)**\nA person owned by, controlled by, or subject to the jurisdiction or direction of a foreign adversary.\n**(iii)**\nA terrorist organization.\n**(B) Applications specified**\nAn application specified in this subparagraph includes the following:\n**(i)**\nAn application owned or operated, in whole or in part, by ByteDance.\n**(ii)**\nTamtam.\n**(iii)**\nTelegram.\n**(iv)**\nVkontakte.\n**(v)**\nWeChat.\n**(vi)**\nWeibo.\n**(vii)**\nRedNote.\n**(viii)**\nAny other application the Secretary of Homeland Security, in consultation with the Director of National Intelligence, determines appropriate.\n**(2) Fusion center**\nThe term fusion center has the meaning given such term in subsection (k) of section 210A of the Homeland Security Act of 2002 ( 6 U.S.C. 124h ).\n**(3) National Network of Fusion Centers**\nThe term National Network of Fusion Centers means a decentralized arrangement of fusion centers intended to enhance the ability of individual State and local fusion centers to leverage the capabilities and expertise of all such fusion centers for the purpose of enhancing analysis and homeland security information sharing nationally.\n**(4) Terrorist organization**\nThe term terrorist organization means\u2014\n**(A)**\nany entity designated as a foreign terrorist organization pursuant to section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ); or\n**(B)**\nany entity engaged in terrorism, as such term is defined in section 2(18) of the Homeland Security Act of 2002 ( 6 U.S.C. 101(18) ).",
      "versionDate": "2025-02-11",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2025-07-03T13:33:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-03T13:33:47Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-07-03T13:33:36Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-07-03T13:33:51Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-07-03T13:33:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-15T13:40:24Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1212ih.xml"
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
      "title": "Countering Online Radicalization and Terrorism Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T12:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Countering Online Radicalization and Terrorism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Homeland Security to conduct annual assessments on terrorism threats to the United States posed by terrorist organizations utilizing foreign cloud-based mobile or desktop messaging applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T12:48:39Z"
    }
  ]
}
```
