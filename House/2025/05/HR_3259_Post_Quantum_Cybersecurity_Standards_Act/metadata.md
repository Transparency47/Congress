# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3259?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3259
- Title: Post Quantum Cybersecurity Standards Act
- Congress: 119
- Bill type: HR
- Bill number: 3259
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2026-05-19T17:20:33Z
- Update date including text: 2026-05-19T17:20:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-06-11 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-11 - Committee: Ordered to be Reported by the Yeas and Nays: 35 - 0.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-06-11 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-11 - Committee: Ordered to be Reported by the Yeas and Nays: 35 - 0.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3259",
    "number": "3259",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Post Quantum Cybersecurity Standards Act",
    "type": "HR",
    "updateDate": "2026-05-19T17:20:33Z",
    "updateDateIncludingText": "2026-05-19T17:20:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 35 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
        "item": [
          {
            "date": "2025-06-11T14:08:39Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-07T14:00:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3259ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3259\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Ms. Stevens (for herself and Ms. Tenney ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the National Quantum Initiative Act and the Cyber Security Research and Development Act to advance the rapid deployment of post quantum cybersecurity standards across the United States economy, support United States cryptography research, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Post Quantum Cybersecurity Standards Act .\n#### 2. NIST cryptography programs and NSF cryptography research\n##### (a) National Institute of Standards and Technology cryptography programs\nThe National Quantum Initiative Act is amended\u2014\n**(1)**\nin section 2 ( 15 U.S.C. 8801 )\u2014\n**(A)**\nby redesignating paragraphs (4), (5), (6), (7), the first paragraph (8) (relating to the definition of Subcommittee on Economic and Security Implications ), and the second paragraph (8) (relating to the definition of Subcommittee on Quantum Information Science ) as paragraphs (5), (7), (8), (9), (11), and (12), respectively;\n**(B)**\nby inserting after paragraph (3) the following new paragraph:\n(4) Critical infrastructure The term critical infrastructure has the meaning given such term in section 1016(e) of Public Law 107\u201356 ( 42 U.S.C. 5195c(e) ) ;\n**(C)**\nby inserting after paragraph (5), as so redesignated, the following new paragraph:\n(6) Post-quantum cryptography The term post-quantum cryptography means those cryptographic algorithms or methods that are assessed not to be specifically vulnerable to attack by either a quantum computer or classical computer. ; and\n**(D)**\nby inserting after paragraph (9), as so redesignated, the following new paragraph:\n(10) Sector risk management agency The term sector risk management agency has the meaning given such term in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 ). ; and\n**(2)**\nin section 201 ( 15 U.S.C. 8831 ), by\u2014\n**(A)**\nredesignating subsection (c) as subsection (d); and\n**(B)**\ninserting after subsection (b) the following new subsection:\n(c) Post quantum cryptography deployment (1) In general The Director of the National Institute of Standards and Technology, in consultation with the Secretary of Homeland Security and the heads of sector risk management agencies, as appropriate, shall promote the voluntary adoption and deployment of post-quantum cryptography standards, including by\u2014 (A) disseminating and making publicly available guidance and resources to help organizations adopt and deploy post-quantum cryptography standards; (B) providing technical assistance, as practicable, to entities that are high risk of quantum cryptoanalytic attacks, such as entities determined to be critical infrastructure or digital infrastructure providers; and (C) conducting such other activities as determined necessary by the Director to promote the adoption and deployment of post-quantum cryptography standards across the United States. (2) Grant program (A) In general Subject to the availability of appropriations and after the date on which the Director of National Institute of Standards and Technology has issued post-quantum cryptography standards under paragraph (1), the Director may establish a program to identify and provide technical assistance through the award of grants to entities that are at high risk of quantum cryptoanalytic attacks, including by granting funds, in adopting such post-quantum cryptographic standards and remediating quantum-related vulnerabilities. (B) Use of funds Grants awarded to entities under this subsection may be used to cover reasonable costs, up to a specified amount established by the Director of the National Institute of Standards and Technology, of activities to adopt post-quantum cryptographic standards and remediate quantum-related vulnerabilities. (C) Guidance The Director of the National Institute of Standards and Technology may develop, and periodically update, guidance, including eligibility, application disclosure requirements, grant amount and duration, and any additional requirements regarding the award of grants under this paragraph. (D) Consultation If the program described in this paragraph is established, the Director of the National Institute of Standards and Technology shall consult with the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security, the heads of other Sector Specific Agencies and risk management agencies, and appropriate representatives of private sector entities, including nonprofit organizations, to share information regarding the program and guidance developed under subparagraph (C). .\n##### (b) National Science Foundation cryptography research\nSubsection (a)(1)(A) of section 4 of the Cyber Security Research and Development Act ( 15 U.S.C. 7403 ) is amended by inserting , including post-quantum cryptography before the semicolon.",
      "versionDate": "2025-05-07",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-06-16T17:52:58Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-06-16T17:52:44Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-16T17:52:51Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-06-16T17:55:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-22T16:18:25Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3259ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Quantum Initiative Act and the Cyber Security Research and Development Act to advance the rapid deployment of post quantum cybersecurity standards across the United States economy, support United States cryptography research, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:36Z"
    },
    {
      "title": "Post Quantum Cybersecurity Standards Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Post Quantum Cybersecurity Standards Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:25Z"
    }
  ]
}
```
