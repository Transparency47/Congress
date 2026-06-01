# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3220?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3220
- Title: Quantum Sandbox for Near-Term Applications Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3220
- Origin chamber: House
- Introduced date: 2025-05-06
- Update date: 2026-01-09T09:06:48Z
- Update date including text: 2026-01-09T09:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-05-06: Introduced in House

## Actions

- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3220",
    "number": "3220",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Quantum Sandbox for Near-Term Applications Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:48Z",
    "updateDateIncludingText": "2026-01-09T09:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T14:00:10Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MI"
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
      "sponsorshipDate": "2025-05-06",
      "state": "TX"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "NC"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "TN"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "OH"
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
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NJ"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3220ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3220\nIN THE HOUSE OF REPRESENTATIVES\nMay 6, 2025 Mr. Obernolte (for himself, Ms. Stevens , Mr. Weber of Texas , and Mr. Hudson ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the National Quantum Initiative Act to establish a public-private partnership for near-term quantum application development and acceleration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quantum Sandbox for Near-Term Applications Act of 2025 .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nThe National Quantum Initiative and its ongoing activities explore and promote Quantum Information Science.\n**(2)**\nContinual innovation by the quantum industry of the United States is critically important.\n**(3)**\nQuantum and quantum-hybrid applications have the ability to provide innovative solutions for near-term use cases across a variety of public and private sector challenges.\n**(4)**\nMany quantum computers are available via the cloud and through a dedicated near-term quantum application acceleration program that is inclusive of the wide variety of quantum computing technologies that will break down barriers to access quantum computing hardware systems.\n**(5)**\nBusiness and consumers of the United States will be able to see benefits of the innovation through a program focusing on near-term use of the technology.\n**(6)**\nQuantum information science is a foundational technology that is transforming the economy of the 21st century.\n**(7)**\nRobust leadership in quantum research and near-term development will have a great impact on the economic security of the United States.\n**(8)**\nUnrivaled excellence in workforce development is key in developing next generation leaders in quantum applications.\n#### 3. Public-private partnership for quantum application development acceleration\n##### (a) In general\nTitle IV of the National Quantum Initiative Act ( 15 U.S.C. 8851 et seq. ) is amended by adding at the end the following:\n405. Public-private partnership for quantum application development acceleration (a) Definitions In this section: (1) Quantum applications The term quantum applications means algorithms and applications which use quantum mechanics through quantum processing units. These applications include quantum computing, quantum communication, quantum sensing, and quantum-hybrid applications which are applications that use both quantum computing and classical computing hardware systems. (2) Quantum sandbox The term quantum sandbox means a program\u2014 (A) for innovation and development of applications using quantum information sciences with a focus on near-term use cases; and (B) that can be used to develop and test demonstrations, proofs of concepts, and pilot applications. (3) Near-term use case The term near-term use case means an application that can be developed and deployed in less than 24 months. (b) Establishment of quantum sandbox required The Secretary of Commerce, in coordination with the Director of the National Institute of Standards and Technology, shall establish a quantum sandbox through the establishment of a public-private partnership focused on quantum computing application development acceleration for quantum, quantum communication, quantum sensing, and quantum-hybrid computing near-term use cases. (c) Engagement As part of the Program and in carrying out subsection (b), the Secretary shall, acting through the Director of the National Institute of Standards and Technology, engage with the Quantum Economic Development Consortium, the National Laboratories (as defined in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 )), federally funded research and development centers, and other members of the United States quantum computing and quantum information ecosystem. .\n##### (b) Clerical amendment\nThe table of contents of the National Quantum Initiative Act ( 15 U.S.C. 8801 et seq. ) is amended by adding after the item relating to section 404 the following new item:\nSec. 405. Public-private partnership for quantum application development acceleration. .",
      "versionDate": "2025-05-06",
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
        "actionDate": "2025-04-08",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1344",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Quantum Sandbox for Near-Term Applications Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-22T15:27:23Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3220ih.xml"
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
      "title": "Quantum Sandbox for Near-Term Applications Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T13:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Quantum Sandbox for Near-Term Applications Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T13:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Quantum Initiative Act to establish a public-private partnership for near-term quantum application development and acceleration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T13:48:19Z"
    }
  ]
}
```
