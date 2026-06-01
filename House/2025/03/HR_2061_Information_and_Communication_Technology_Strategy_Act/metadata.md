# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2061?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2061
- Title: Information and Communication Technology Strategy Act
- Congress: 119
- Bill type: HR
- Bill number: 2061
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-03-27T01:19:55Z
- Update date including text: 2026-03-27T01:19:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2061",
    "number": "2061",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "J000302",
        "district": "13",
        "firstName": "John",
        "fullName": "Rep. Joyce, John [R-PA-13]",
        "lastName": "Joyce",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Information and Communication Technology Strategy Act",
    "type": "HR",
    "updateDate": "2026-03-27T01:19:55Z",
    "updateDateIncludingText": "2026-03-27T01:19:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NV"
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
      "sponsorshipDate": "2025-09-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2061ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2061\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Joyce of Pennsylvania (for himself and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Commerce, acting through the Assistant Secretary of Commerce for Communications and Information, to report on and develop a whole-of-Government strategy with respect to the economic competitiveness of the information and communication technology supply chain, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Information and Communication Technology Strategy Act .\n#### 2. Economic competitiveness of information and communication technology supply chain\n##### (a) Report\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the information and communication technology supply chain that\u2014\n**(1)**\nidentifies\u2014\n**(A)**\ninformation and communication technology critical to the economic competitiveness of the United States; and\n**(B)**\nthe industrial capacity of\u2014\n**(i)**\nUnited States vendors that produce information and communication technology identified under subparagraph (A); and\n**(ii)**\ntrusted information and communication technology vendors that produce information and communication technology identified under subparagraph (A);\n**(2)**\nassesses the economic competitiveness of vendors described under paragraph (1)(B);\n**(3)**\nassesses whether, and to what extent, there is a dependence by providers of advanced telecommunications capability in the United States on information and communication technology identified under paragraph (1)(A) that is not trusted;\n**(4)**\nidentifies\u2014\n**(A)**\nwhat actions by the Federal Government are needed to support, and bolster the economic competitiveness of, trusted information and communication technology vendors; and\n**(B)**\nwhat Federal resources are needed to reduce dependence by providers of advanced telecommunications capability in the United States on companies that\u2014\n**(i)**\nproduce information and communication technology; and\n**(ii)**\nare not trusted; and\n**(5)**\ndefines lines of effort and assigns responsibilities for a whole-of-Government response to ensuring the competitiveness of the information and communication technology supply chain in the United States.\n##### (b) Whole-of-Government strategy\n**(1) In general**\nThe Secretary shall develop, on the basis of the report required by subsection (a), a whole-of-Government strategy to ensure the economic competitiveness of trusted information and communication technology vendors that includes\u2014\n**(A)**\nrecommendations on how\u2014\n**(i)**\nto strengthen the structure, resources, and authorities of the Federal Government to support the economic competitiveness of trusted information and communication technology vendors, including United States vendors that are trusted information and communication technology vendors; and\n**(ii)**\nthe Federal Government can address any barriers to a market-based solution for increasing the economic competitiveness of such information and communication technology vendors;\n**(B)**\ndefined lines of effort and responsibilities for Federal agencies to implement the strategy; and\n**(C)**\na description of\u2014\n**(i)**\nany change to a Federal program, Federal law, or structure of the Federal Government necessary to implement any recommendation under subparagraph (A); and\n**(ii)**\nany additional Federal resource necessary to implement any recommendation under subparagraph (A).\n**(2) Report**\nNot later than 180 days after the submission of the report required by subsection (a), the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report containing the strategy developed under paragraph (1).\n##### (c) Consultation required\nIn carrying out subsections (a) and (b), the Secretary shall consult with\u2014\n**(1)**\na cross-section of trusted information and communication technology vendors; and\n**(2)**\nthe Secretary of State, the Secretary of Homeland Security, the Attorney General, the Director of National Intelligence, the Chair of the Federal Communications Commission, and any other head of an agency the Secretary determines necessary.\n##### (d) Definitions\nIn this section:\n**(1) Advanced telecommunications capability**\nThe term advanced telecommunications capability has the meaning given that term in section 706 of the Telecommunications Act of 1996 ( 47 U.S.C. 1302 ).\n**(2) Information and communication technology**\nThe term information and communication technology means a technology (including software), component, or material that enables communications by radio or wire.\n**(3) Information and communication technology supply chain**\nThe term information and communication technology supply chain means all of the companies that produce information and communication technology.\n**(4) Not trusted**\nThe term not trusted means, with respect to a company or information and communication technology, that the company or information and communication technology is determined by the Secretary to pose an unacceptable risk to the national security of the United States or the security and safety of United States persons based solely on one or more determinations described under paragraphs (1) through (4) of section 2(c) of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1601(c) ).\n**(5) Secretary**\nThe term Secretary means the Secretary of Commerce, acting through the Assistant Secretary of Commerce for Communications and Information.\n**(6) Trusted**\nThe term trusted means, with respect to a company, that the Secretary has not determined that the company is not trusted.\n**(7) Trusted information and communication technology vendor**\nThe term trusted information and communication technology vendor means a company\u2014\n**(A)**\nthat produces information and communication technology; and\n**(B)**\nthat is trusted.",
      "versionDate": "2025-03-11",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-03-26T15:53:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2061",
          "measure-number": "2061",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2061v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Information and Communication Technology Strategy Act</b></p> <p>This bill requires the National Telecommunications and Information Administration to report on the information and communication technology supply chain and to develop a strategy to ensure the economic competitiveness of trusted information and communication technology vendors.</p> <p>The report must include (1) an identification of technology that is critical to U.S. economic competitiveness and the industrial capacity of U.S. vendors and other trusted vendors that produce such technology, (2) an assessment of whether and to what extent there is a dependence by providers of advanced telecommunications capability in the United States on technology that is not trusted, and (3) an identification of federal government actions and resources needed to support the economic competitiveness of trusted vendors and reduce dependence on companies that are not trusted.</p>"
        },
        "title": "Information and Communication Technology Strategy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2061.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Information and Communication Technology Strategy Act</b></p> <p>This bill requires the National Telecommunications and Information Administration to report on the information and communication technology supply chain and to develop a strategy to ensure the economic competitiveness of trusted information and communication technology vendors.</p> <p>The report must include (1) an identification of technology that is critical to U.S. economic competitiveness and the industrial capacity of U.S. vendors and other trusted vendors that produce such technology, (2) an assessment of whether and to what extent there is a dependence by providers of advanced telecommunications capability in the United States on technology that is not trusted, and (3) an identification of federal government actions and resources needed to support the economic competitiveness of trusted vendors and reduce dependence on companies that are not trusted.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hr2061"
    },
    "title": "Information and Communication Technology Strategy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Information and Communication Technology Strategy Act</b></p> <p>This bill requires the National Telecommunications and Information Administration to report on the information and communication technology supply chain and to develop a strategy to ensure the economic competitiveness of trusted information and communication technology vendors.</p> <p>The report must include (1) an identification of technology that is critical to U.S. economic competitiveness and the industrial capacity of U.S. vendors and other trusted vendors that produce such technology, (2) an assessment of whether and to what extent there is a dependence by providers of advanced telecommunications capability in the United States on technology that is not trusted, and (3) an identification of federal government actions and resources needed to support the economic competitiveness of trusted vendors and reduce dependence on companies that are not trusted.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hr2061"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2061ih.xml"
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
      "title": "Information and Communication Technology Strategy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Information and Communication Technology Strategy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Commerce, acting through the Assistant Secretary of Commerce for Communications and Information, to report on and develop a whole-of-Government strategy with respect to the economic competitiveness of the information and communication technology supply chain, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:54Z"
    }
  ]
}
```
