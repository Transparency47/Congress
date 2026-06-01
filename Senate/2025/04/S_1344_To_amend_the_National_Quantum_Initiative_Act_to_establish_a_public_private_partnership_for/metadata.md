# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1344?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1344
- Title: Quantum Sandbox for Near-Term Applications Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1344
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-12-05T22:49:20Z
- Update date including text: 2025-12-05T22:49:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1344",
    "number": "1344",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
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
    "title": "Quantum Sandbox for Near-Term Applications Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:49:20Z",
    "updateDateIncludingText": "2025-12-05T22:49:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T20:04:49Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1344is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1344\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mrs. Blackburn (for herself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the National Quantum Initiative Act to establish a public-private partnership for near-term quantum application development and acceleration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quantum Sandbox for Near-Term Applications Act of 2025 .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nThe National Quantum Initiative and its ongoing activities explore and promote Quantum Information Science.\n**(2)**\nContinual innovation by the quantum industry of the United States is critically important.\n**(3)**\nQuantum and quantum-hybrid applications have the ability to provide innovative solutions for near-term use cases across a variety of public and private sector challenges.\n**(4)**\nMany quantum computers are available via the cloud and through a dedicated near-term quantum application acceleration program that is inclusive of the wide variety of quantum computing technologies will break down barriers to access quantum computing hardware systems.\n**(5)**\nBusiness and consumers of the United States will be able to see benefits of the innovation through a program focusing on near-term use of the technology.\n**(6)**\nQuantum information science is a foundational technology that is transforming the economy of the 21st century.\n**(7)**\nRobust leadership in quantum research and near-term development will have a great impact on the economic security of the United States.\n**(8)**\nUnrivaled excellence in workforce development is key in developing next generation leaders in quantum applications.\n#### 3. Public-private partnership for quantum application development acceleration\n##### (a) In general\nTitle IV of the National Quantum Initiative Act ( 15 U.S.C. 8851 et seq. ) is amended by adding at the end the following:\n405. Public-private partnership for quantum application development acceleration (a) Definitions In this section: (1) Quantum applications The term quantum applications means algorithms and applications which use quantum mechanics through quantum processing units. These applications include quantum computing, quantum communication, quantum sensing, and quantum-hybrid applications which are applications that use both quantum computing and classical computing hardware systems. (2) Quantum sandbox The term quantum sandbox means a program\u2014 (A) for innovation and development of applications using quantum information sciences with a focus on near-term use cases; and (B) that can be used to develop and test demonstrations, proofs of concepts, and pilot applications. (3) Near-term use case The term near-term use case means an application that can be developed and deployed in less than 24 months. (b) Establishment of quantum sandbox required The Secretary of Commerce shall, in coordination with the Director of the National Institute of Standards and Technology, establish a quantum sandbox through the establishment of a public-private partnership focused on quantum application development acceleration for quantum application near-term use cases. (c) Engagement As part of the Program and in carrying out subsection (b), the Secretary shall, acting through the Director of the National Institute of Standards and Technology, engage with the Quantum Economic Development Consortium, the National Laboratories (as defined in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 )), federally funded research and development centers, and other members of the United States quantum computing and quantum information ecosystem. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of such Act is amended by adding after the item relating to section 404 the following new item:\nSec. 405. Public-private partnership for quantum application development acceleration. .",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-05-06",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "3220",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Quantum Sandbox for Near-Term Applications Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-19T16:00:38Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1344is.xml"
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
      "title": "Quantum Sandbox for Near-Term Applications Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T02:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Quantum Sandbox for Near-Term Applications Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T02:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Quantum Initiative Act to establish a public-private partnership for near-term quantum application development and acceleration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T02:33:20Z"
    }
  ]
}
```
