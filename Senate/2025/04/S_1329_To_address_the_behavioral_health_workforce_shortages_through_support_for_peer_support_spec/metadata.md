# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1329?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1329
- Title: PEER Support Act
- Congress: 119
- Bill type: S
- Bill number: 1329
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-12-19T12:03:16Z
- Update date including text: 2025-12-19T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1329",
    "number": "1329",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "PEER Support Act",
    "type": "S",
    "updateDate": "2025-12-19T12:03:16Z",
    "updateDateIncludingText": "2025-12-19T12:03:16Z"
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
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
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
          "date": "2025-04-08T16:32:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "IN"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "WI"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "AK"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "OR"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1329is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1329\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Kaine (for himself, Mr. Banks , Ms. Baldwin , Ms. Murkowski , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo address the behavioral health workforce shortages through support for peer support specialists, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Empathetic and Effective Recovery Support Act or the PEER Support Act .\n#### 2. Definition of peer support specialist\n##### (a) In general\nIn this Act, the term peer support specialist means an individual\u2014\n**(1)**\n**(A)**\nwho has lived experience of recovery from a mental health condition or substance use disorder and who specializes in supporting individuals with mental health conditions or substance use disorders; or\n**(B)**\nwho has lived experience as a parent or caregiver of an individual with a mental health condition or substance use disorder and who specializes in supporting families navigating mental health or substance use service systems; and\n**(2)**\nwho is certified as qualified to furnish peer support services, as described in subsection (b), under a process that is determined by the State in which such individual furnishes such services or determined appropriate by the Secretary of Health and Human Services.\n##### (b) Peer support services\nThe services described in this subsection shall be consistent with the National Practice Guidelines for Peer Supporters issued by the National Association of Peer Supporters (or a successor publication) and inclusive of the Core Competencies for Peer Workers in Behavioral Health Services of the Substance Abuse and Mental Health Services Administration.\n#### 3. Recognizing the peer support specialist profession\nNot later than January 1, 2026, the Director of the Office of Management and Budget shall revise the Standard Occupational Classification system to include an occupational category for peer support specialists.\n#### 4. Establishing the Office of Recovery\nPart A of title V of the Public Health Service Act ( 42 U.S.C. 290aa et seq. ) is amended by inserting after section 501C ( 42 U.S.C. 290aa\u20130b ) the following:\n501D. Office of Recovery (a) In general There is established, in the Substance Abuse and Mental Health Services Administration, an Office of Recovery (referred to in this section as the Office ). (b) Director The Office shall be headed by a Director who has demonstrated experience in, and lived experience with, mental health or substance use disorder recovery. (c) Responsibilities Through the Office of Recovery, the responsibilities of the Director shall include\u2014 (1) providing leadership in the identification of new and emerging issues related to recovery support services; (2) supporting technical assistance, data analysis, and evaluation functions in order to assist States, localities, territories, Indian Tribes, and Tribal organizations in developing recovery support services and identifying best practices with the objective of expanding the capacity of, and access to, recovery support services; (3) providing support for the training, education, integration, and professionalization of the peer support specialist workforce; (4) disseminating best practice recommendations with respect to peer support specialist training, certification, supervision, and practice to States and other entities that employ peer support specialists; (5) supporting peer support specialists with ongoing professional development and retention activities; and (6) developing recommendations on creating career pathways for peer support specialists. (d) Functions Beginning on the date of enactment of this section, the functions of the Office shall include the responsibilities described in subsection (c) and the functions of the Office of Recovery of the Substance Abuse and Mental Health Services Administration on the day before such date of enactment, including all of its personnel, assets, authorities, obligations, and liabilities, except as otherwise specified in this section. (e) Definition of peer support specialist In this section, the term peer support specialist has the meaning given such term in section 2 of the Providing Empathetic and Effective Recovery Support Act . .\n#### 5. Research and recommendations on criminal background check process for peer support specialists\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in coordination with the Attorney General, shall develop a report on research and recommendations with respect to criminal background check processes for individuals becoming peer support specialists.\n##### (b) Contents\nThe report under subsection (a) shall include\u2014\n**(1)**\na summary of evidence-informed literature on the effectiveness of peer support specialists in improving the mental health and the substance use disorder recovery of other individuals;\n**(2)**\na survey of each State's laws (including regulations) that contain criminal background check requirements for serving as a peer support specialist, including\u2014\n**(A)**\nan analysis of criminal offenses that are included in State laws (including regulations) that prevent individuals from earning a peer support specialist certification or from practicing as a peer support specialist;\n**(B)**\nan analysis of requirements (if any) under the State plan under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) or under a waiver of such plan relating to background checks for providers participating under such plan or waiver and the extent to which any such requirements differ from similar requirements imposed under State law (including regulations);\n**(C)**\nan analysis of requirements (if any) of any State receiving a grant under part B of title XIX of the Public Health Service Act ( 42 U.S.C. 300x et seq. ) relating to background checks for providers participating in a program under, or otherwise providing services supported by, such grant;\n**(D)**\na review of State laws (including regulations) that provide exemptions from prohibitions regarding certification or practice of peer support specialists; and\n**(E)**\nan indication of each State that has gone through the process of amending or otherwise changing criminal background check laws (including regulations) for the certification and practice of peer support specialists; and\n**(3)**\nrecommendations to States on criminal background check processes that would reduce barriers to becoming certified as peer support specialists.\n##### (c) Availability\nNot later than 1 year after the date of enactment of this Act, the Secretary shall\u2014\n**(1)**\npost the report required under subsection (a) on the publicly accessible internet website of the Substance Abuse and Mental Health Services Administration; and\n**(2)**\ndistribute such report to\u2014\n**(A)**\nState agencies responsible for certification of peer support specialists;\n**(B)**\nthe Centers for Medicare & Medicaid Services;\n**(C)**\nState agencies responsible for carrying out a State plan under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) or under a waiver of such plan; and\n**(D)**\nState agencies responsible for carrying out a grant under part B of title XIX of the Public Health Service Act ( 42 U.S.C. 300x et seq. ).",
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
        "actionDate": "2025-04-08",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2741",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PEER Support Act",
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
        "name": "Health",
        "updateDate": "2025-05-15T17:31:39Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1329is.xml"
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
      "title": "PEER Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PEER Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-22T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Empathetic and Effective Recovery Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-22T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address the behavioral health workforce shortages through support for peer support specialists, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-22T03:48:40Z"
    }
  ]
}
```
