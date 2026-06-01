# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/935?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/935
- Title: Health Care Workforce Innovation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 935
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-05-13T08:06:10Z
- Update date including text: 2026-05-13T08:06:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/935",
    "number": "935",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Health Care Workforce Innovation Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:10Z",
    "updateDateIncludingText": "2026-05-13T08:06:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:02:25Z",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "WA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "DC"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "WA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "MA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "NY"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "OR"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "WA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr935ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 935\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Garbarino (for himself, Ms. Schrier , Mr. Valadao , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to provide for a health care workforce innovation program.\n#### 1. Short title\nThis Act may be cited as the Health Care Workforce Innovation Act of 2025 .\n#### 2. Health care workforce innovation program\nSection 755(b) of the Public Health Service Act ( 42 U.S.C. 294e(b) ) is amended by adding at the end the following:\n(5) (A) Supporting and developing new innovative, community-driven approaches for the education and training of allied health professionals, including those described in subparagraph (F)(i), with an emphasis on expanding the supply of such professionals located in, and meeting the needs of, underserved communities and rural areas. Grants or contracts under this paragraph shall be awarded through a new program (referred to as the Health Care Workforce Innovation Program or in this paragraph as the Program ). (B) To be eligible to receive a grant or contract under the Program an entity shall\u2014 (i) be a Federally qualified health center (as defined in section 1905(l)(2)(B) of the Social Security Act), a State-level association or other consortium that represents and is comprised of Federally qualified health centers, a certified rural health clinic that meets the requirements of section 334, or an accredited, nonprofit post-secondary vocational program that trains allied health professionals to work in primary care settings; and (ii) submit to the Secretary an application that, at a minimum, contains\u2014 (I) a description of how all trainees will be trained in accredited training programs either directly or through partnerships with public or nonprofit private entities, such as schools of allied health; (II) a description of the community-driven health care workforce innovation model to be carried out under the grant or contract, including the specific allied health professions to be funded; (III) the geographic service area that will be served, including quantitative data, if available, showing that such particular area faces a shortage of allied health professionals and lacks access to health care; (IV) a description of the benefits provided to each health care professional trained under the proposed model during the education and training phase; (V) a description of the experience that the applicant has in the recruitment, retention, and promotion of the well-being of workers and volunteers; (VI) a description of how the funding awarded under the Program will supplement rather than supplant existing funding; (VII) a description of the scalability and replicability of the community-driven approach to be funded under the Program; (VIII) a description of the infrastructure, outreach and communication plan, and other program support costs required to operationalize the proposed model; and (IX) any other information, as the Secretary determines appropriate. (C) (i) An entity shall use amounts received under a grant or contract awarded under the Program to carry out the innovative, community-driven model described in the application under subparagraph (B). Such amounts may be used for launching new or expanding existing innovative health care professional partnerships, including the following specific uses: (I) Establishing or expanding a partnership between such entity and 1 or more high schools, accredited public or nonprofit private vocational-technical schools, accredited public or nonprofit private 2-year colleges, area health education centers, and entities with clinical settings for the provision of education and training opportunities not available at the grantee\u2019s facilities. (II) Providing education and training programs to improve allied health professionals\u2019 readiness in settings that serve underserved communities and rural areas; encouraging students from underserved and disadvantaged backgrounds and former patients to consider careers in health care, and better reflecting and meeting community needs; providing education and training programs for individuals to work in patient-centered, team-based, community-driven health care models that include integration with other clinical practitioners and training in cultural and linguistic competence; providing pre-apprenticeship and apprenticeship programs for health care technical, support, and entry-level occupations, particularly for those enrolled in dual or concurrent enrollment programs; building a preceptorship training-to-practice model for medical, behavioral health, oral health, and public health disciplines in an integrated, community-driven setting; providing and expanding internships, career ladders, and development opportunities for health care professionals, including new and existing staff; or investing in training equipment, supplies, and limited renovations or retrofitting of training space needed for grantees to carry out their particular model. (ii) Amounts received under a grant or contract awarded under the Program shall not be used to support construction costs or to supplant funding from existing programs that support the applicant\u2019s health workforce. (iii) Models funded under the Program shall be for a duration of at least 3 years. (D) In awarding grants or contracts under the Program, the Secretary shall give priority to applicants that will use grant or contract funds to support workforce innovation models that increase the number of individuals from underserved and disadvantaged backgrounds working in such health care professions, improve access to health care (including medical, behavioral health and oral health) in underserved communities, or demonstrate that the model can be replicated in other underserved communities in a cost-efficient and effective manner to achieve the purposes of the Program. (E) An entity that receives a grant or contract under the Program shall provide periodic reports to the Secretary detailing the findings and outcomes of the innovative, community-driven model carried out under the grant. Such reports shall contain information in a manner and at such times as determined appropriate by the Secretary. (F) In this paragraph: (i) The term allied health professional includes individuals who provide clinical support services, including medical assistants, dental assistants, dental hygienists, dental therapists, pharmacy technicians, physical therapists, physical therapist assistants, and health care interpreters; individuals providing non-clinical support, such as billing and coding professionals and health information technology professionals; dieticians; medical technologists; emergency medical technicians; community health workers; health education specialists; health care paraprofessionals; and peer support specialists. (ii) The term rural area has the meaning given such term by the Administrator of the Health Resources and Services Administration. (iii) The term underserved communities means areas, population groups, and facilities designated as health professional shortage areas under section 332, medically underserved areas as defined under section 330I(a), or medically underserved populations as defined under section 330(b)(3). (G) (i) There are authorized to be appropriated such sums as may be necessary for each of fiscal years 2026 through 2028, to carry out this paragraph, to remain available until expended. (ii) A grant or contract provided under the Program shall not exceed $2,500,000 for a grant period. .",
      "versionDate": "2025-02-04",
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
        "actionDate": "2026-03-26",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4254",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Health Workforce Innovation Act",
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
            "name": "Community life and organization",
            "updateDate": "2025-04-11T15:03:25Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-04-11T15:03:19Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-11T15:03:34Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-04-11T15:03:12Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-04-11T15:03:46Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-04-11T15:00:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-07T15:54:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr935",
          "measure-number": "935",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr935v00",
            "update-date": "2025-04-28"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Health Care Workforce Innovation Act of 2025</strong></p><p>This bill establishes the Health Care Workforce Innovation Program within the Health Resources and Services Administration to provide grants to federally qualified health centers, rural health clinics, and post-secondary vocational programs for developing education and training for allied health professionals (e.g., professionals providing clinical or\u00a0non-clinical support services, community health workers, and health education specialists).</p><p>Specifically, grant recipients must use the funds to carry out innovative, community-based programs to train allied health professionals, with a focus on supporting rural and underserved areas. Grant recipients may use the funds to launch or expand health care professional partnerships\u00a0(e.g., between a grant recipient and a school), establish apprenticeship or other career programs, or invest in training equipment, among other activities. </p>"
        },
        "title": "Health Care Workforce Innovation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr935.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Health Care Workforce Innovation Act of 2025</strong></p><p>This bill establishes the Health Care Workforce Innovation Program within the Health Resources and Services Administration to provide grants to federally qualified health centers, rural health clinics, and post-secondary vocational programs for developing education and training for allied health professionals (e.g., professionals providing clinical or\u00a0non-clinical support services, community health workers, and health education specialists).</p><p>Specifically, grant recipients must use the funds to carry out innovative, community-based programs to train allied health professionals, with a focus on supporting rural and underserved areas. Grant recipients may use the funds to launch or expand health care professional partnerships\u00a0(e.g., between a grant recipient and a school), establish apprenticeship or other career programs, or invest in training equipment, among other activities. </p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr935"
    },
    "title": "Health Care Workforce Innovation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Health Care Workforce Innovation Act of 2025</strong></p><p>This bill establishes the Health Care Workforce Innovation Program within the Health Resources and Services Administration to provide grants to federally qualified health centers, rural health clinics, and post-secondary vocational programs for developing education and training for allied health professionals (e.g., professionals providing clinical or\u00a0non-clinical support services, community health workers, and health education specialists).</p><p>Specifically, grant recipients must use the funds to carry out innovative, community-based programs to train allied health professionals, with a focus on supporting rural and underserved areas. Grant recipients may use the funds to launch or expand health care professional partnerships\u00a0(e.g., between a grant recipient and a school), establish apprenticeship or other career programs, or invest in training equipment, among other activities. </p>",
      "updateDate": "2025-04-28",
      "versionCode": "id119hr935"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr935ih.xml"
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
      "title": "Health Care Workforce Innovation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Care Workforce Innovation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to provide for a health care workforce innovation program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:24Z"
    }
  ]
}
```
