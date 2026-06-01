# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1633
- Title: TEST AI Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1633
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2025-06-10T14:38:07Z
- Update date including text: 2025-06-10T14:38:07Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1633",
    "number": "1633",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Lujan, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "TEST AI Act of 2025",
    "type": "S",
    "updateDate": "2025-06-10T14:38:07Z",
    "updateDateIncludingText": "2025-06-10T14:38:07Z"
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
          "date": "2025-05-07T18:42:34Z",
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
      "sponsorshipDate": "2025-05-07",
      "state": "TN"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "IL"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "ID"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1633is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1633\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Luj\u00e1n (for himself, Mrs. Blackburn , Mr. Durbin , Mr. Risch , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Director of the National Institute of Standards and Technology to establish a pilot program that uses testbeds to develop measurement standards for the evaluation of artificial intelligence systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Testing and Evaluation Systems for Trusted Artificial Intelligence Act of 2025 or the TEST AI Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Artificial intelligence system**\nThe term artificial intelligence system has the meaning given the term artificial intelligence in section 5002 of the National Artificial Intelligence Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Covered foreign country**\nThe term covered foreign country means\u2014\n**(A)**\nthe People\u2019s Republic of China;\n**(B)**\nthe Russian Federation;\n**(C)**\nthe Democratic People\u2019s Republic of Korea; and\n**(D)**\nthe Islamic Republic of Iran.\n**(3) Director**\nThe term Director means the Director of the National Institute of Standards and Technology.\n**(4) Institute**\nThe term Institute means the National Institute of Standards and Technology.\n**(5) Testbed**\nThe term testbed means a facility or mechanism equipped for conducting rigorous, transparent, and replicable testing of tools or technologies to evaluate the functionality, performance, and security of those tools or technologies.\n**(6) Working group**\nThe term Working Group means the working group established under section 3(c)(1).\n#### 3. Pilot program on testbeds for development of measurement standards for evaluation of artificial intelligence systems\n##### (a) Pilot program required\n**(1) In general**\nThe Director shall, in coordination with the Secretary of Energy and after consultation with the Working Group, carry out a pilot program of testbeds to assess the feasibility and advisability of developing measurement standards for the evaluation of artificial intelligence systems used by Federal agencies through the use of testbeds.\n**(2) Process**\nThe Director shall carry out the pilot program required by paragraph (1) by building and demonstrating an iterative process whereby measurement science is advanced and standards are developed using testbeds in accordance with subsection (d), and the results of the tests are reviewed by stakeholders from government, the private sector, and academia.\n##### (b) Memorandum of Understanding\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Commerce and the Secretary of Energy shall enter into a memorandum of understanding to implement the coordination between the Secretary of Energy and the Director required by paragraph (2).\n**(2) Requirements**\nThe memorandum shall be sufficient to ensure the Institute and other Federal agencies have access, as may be necessary and as determined by the Secretary of Energy, to the resources, personnel, and facilities at the Department of Energy, including the cross-cutting research and development programs to support the activities of the pilot program require by subsection (a)(1).\n**(3) Renegotiations**\nNot later than 2 years after the establishment of the pilot program required by subsection (a)(1), and every 2 years thereafter, Secretary of Commerce and the Secretary of Energy shall reassess the memorandum of understanding to ensure that it meets the needs of the agencies and adequately supports the activities of the pilot program.\n##### (c) Artificial Intelligence Testing Working Group\n**(1) Establishment**\n**(A) In general**\nNot later than 90 days after the memorandum of understanding required by subsection (b)(1) is signed, the Secretary of Commerce shall establish a working group to provide advice to the Secretary of Commerce and the Secretary of Energy on the development of measurement standards for the evaluation of artificial intelligence systems under the pilot program required by subsection (a).\n**(B) Designation**\nThe working group established under subparagraph (A) shall be known as the Artificial Intelligence Testing Working Group .\n**(2) Membership**\n**(A) In general**\nThe Working Group shall be comprised of not more than 10 members that include the following:\n**(i)**\nThe Secretary of Commerce or a designee of the Secretary of Commerce from the Department of Commerce.\n**(ii)**\nThe Secretary of Energy or a designee of the Secretary of Energy from the Department of Energy.\n**(iii)**\nThe Director or a designee of the Director from the Institute.\n**(iv)**\nRepresentatives from the private sector, as the members described in clauses (i) through (iii) consider appropriate.\n**(v)**\nRepresentatives from academic institutions, as the members described in clauses (i) through (iii) consider appropriate.\n**(B) Prohibition**\nNo citizen of a covered foreign country may serve as a member of the Working Group.\n**(3) Strategy for measurement standards**\n**(A) In general**\nNot later than 1 year after the date on which the Working Group is established under paragraph (1), the Working Group shall develop a strategy for the development of measurement standards for the evaluation of artificial intelligence systems.\n**(B) Elements**\nThe strategy required by subparagraph (A) shall\u2014\n**(i)**\nidentify measurement standards that the members of the Working Group consider necessary, including standards with respect to an artificial intelligence system for\u2014\n**(I)**\nreliability;\n**(II)**\nperformance;\n**(III)**\ncapability;\n**(IV)**\ninterpretability;\n**(V)**\nsecurity, including the propensity of the system for leaking data;\n**(VI)**\nprivacy;\n**(VII)**\ndata bias; and\n**(VIII)**\nbounds for applicability and use cases;\n**(ii)**\ninclude a proposed blueprint for developing the measurement standards;\n**(iii)**\nidentify the applications or artificial intelligence systems to which the standards should initially apply; and\n**(iv)**\nidentify metrics for the assessment of the pilot program.\n**(C) Publication**\nThe Secretary of Commerce shall publish on a publicly accessible website of the Department of Commerce the strategy for measurement standards required by subparagraph (A) to provide the information contained in the strategy to stakeholders, including code and model developers, researchers, and industrial users of artificial intelligence systems.\n##### (d) Development of Testbeds for measurement standards\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Director shall, in collaboration with the Secretary of Energy and in coordination with the Working Group, develop, in accordance with the strategy developed under subsection (c)(3)(A), testbeds on which to demonstrate the development of measurement standards for the evaluation of artificial intelligence systems to be used by Federal agencies.\n**(2) Experts**\nIn carrying out paragraph (1), the Director may hire any expert the Director considers necessary, including experts from academia, industry, and standards development organizations.\n##### (e) Report\nNot later than 180 days after the date on which the Director completes the first testbed demonstration and development of measurement standards under subsection (d)(1), the Director shall submit to Congress a report that\u2014\n**(1)**\nreviews the findings of the Director with respect to the initial demonstration carried out under this section;\n**(2)**\nrecommends revisions to the pilot program plan, including by identifying any resources, funding, or personnel that is needed to improve and continue the development of testbeds and measurement standards for the evaluation of artificial intelligence systems for multiple applications; and\n**(3)**\nmakes recommendations for legislative or administrative action to advance the development of measurement standards for the evaluation of artificial intelligence systems.",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-06-10T14:38:07Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1633is.xml"
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
      "title": "TEST AI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TEST AI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Testing and Evaluation Systems for Trusted Artificial Intelligence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the National Institute of Standards and Technology to establish a pilot program that uses testbeds to develop measurement standards for the evaluation of artificial intelligence systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:29Z"
    }
  ]
}
```
