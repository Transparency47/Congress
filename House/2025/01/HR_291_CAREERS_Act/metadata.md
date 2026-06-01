# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/291?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/291
- Title: CAREERS Act
- Congress: 119
- Bill type: HR
- Bill number: 291
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-02-27T09:07:02Z
- Update date including text: 2026-02-27T09:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/291",
    "number": "291",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "CAREERS Act",
    "type": "HR",
    "updateDate": "2026-02-27T09:07:02Z",
    "updateDateIncludingText": "2026-02-27T09:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:31:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T18:01:38Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "HI"
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
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "OR"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr291ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 291\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Langworthy (for himself and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Rural Innovation Stronger Economy Grant Program of the Department of Agriculture.\n#### 1. Short title\nThis Act may be cited as the Creating Access to Rural Employment and Education for Resilience and Success Act or the CAREERS Act .\n#### 2. Workforce training programs\n##### (a) In general\nSection 379I of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008w ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)(A)\u2014\n**(i)**\nin clause (iii)\u2014\n**(I)**\nby striking subclause (I) and inserting the following:\n(I) an institution of higher education (as defined in section 101, and subparagraphs (A) and (B) of section 102(a)(1), of the Higher Education Act of 1965 ( 20 U.S.C. 1001 , 1002(a)(1))); ;\n**(II)**\nby redesignating subclauses (II) and (III) as subclauses (III) and (IV), respectively, and inserting after subclause (I) the following:\n(II) an area career and technical education school (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ); ; and\n**(III)**\nin subclause (IV) (as so redesignated by subclause (II) of this clause), by striking and ;\n**(ii)**\nin clause (iv)\u2014\n**(I)**\nby striking subclause (IV) and inserting the following:\n(IV) an institution of higher education (as defined in section 101, and subparagraphs (A) and (B) of section 102(a)(1), of the Higher Education Act of 1965 ( 20 U.S.C. 1001 , 1002(a)(1))); ; and\n**(II)**\nby redesignating subclause (V) as subclause (VI) and inserting after subclause (IV) the following:\n(V) an area career and technical education school (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ); or ; and\n**(iii)**\nby adding at the end the following:\n(v) in the case of a career pathway program, includes 1 or more member of the local workforce development board established under section 107 of the Workforce Innovation and Opportunity Act and serving the region to ensure such program is integrated with the activities carried out by the local workforce development board; and ; and\n**(B)**\nby adding at the end the following:\n(6) Career pathway The term career pathway has the meaning given the term in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ). (7) Industry or sector partnership The term industry or sector partnership has the meaning given the term in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ). ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting carry out career pathway programs or industry or sector partnerships aligned with industry sectors in rural communities before the 3rd comma;\n**(ii)**\nin subparagraph (A), by striking and at the end;\n**(iii)**\nin subparagraph (B), by striking the period and inserting a semicolon; and\n**(iv)**\nby adding at the end the following:\n(C) address workforce challenges faced by specific industry sectors in rural communities; and (D) promote targeted skills development initiatives to stimulate innovation and enhance economic development in rural regions. ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i), by inserting career pathway program, or industry or sector partnerships before the semicolon; and\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nby inserting career pathway program, or industry or sector partnerships before to provide ; and\n**(bb)**\nby inserting leadership development, before customized ;\n**(ii)**\nin subparagraph (E), by striking and at the end;\n**(iii)**\nin subparagraph (F), by striking the period and inserting ; and ; and\n**(iv)**\nby adding at the end the following:\n(G) the ability of the eligible entity to carry out activities to address the issues of worker displacement, an aging workforce, and youth migration. ; and\n**(C)**\nby striking paragraph (5) and inserting the following;\n(5) Geographic distribution The Secretary shall ensure regional diversity of recipients of grants or participants in providing grants under paragraph (1) for jobs accelerators, career pathway programs, industry or sector partnerships, and related programming. ;\n**(3)**\nin subsection (d)(1)\u2014\n**(A)**\nin subparagraph (B), by striking the period and inserting ; or ; and\n**(B)**\nby adding at the end the following:\n(C) to support career pathway programs or industry or sector partnerships to be carried out in industries in rural communities, including\u2014 (i) telecommunications or broadband services; (ii) water, waste water, and disposal services; (iii) electric supply services; (iv) conservation practices and management; (v) health care; (vi) child care; (vii) manufacturing; (viii) agribusiness related to production, processing, and distribution; and (ix) any other sectors that are identified by the local workforce development board serving the region to be an in-demand industry sector or occupation, as defined in section 3 of the Workforce Innovation and Opportunity Act. ;\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1), by striking and at the end;\n**(B)**\nin paragraph (2)(B)\u2014\n**(i)**\nin clause (xvii), by striking or at the end; and\n**(ii)**\nby redesignating clause (xviii) as clause (xix) and inserting after clause (xvii) the following:\n(xviii) the number of individuals who have completed skills development, recognized postsecondary credentials, or gained specialized education through career pathways programs or industry or sector partnership; or ; and\n**(iii)**\nin clause (xix) (as so redesignated by clause (ii) of this subparagraph), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(3) in the case of a career pathway program or industry or sector partnership, report to the Secretary the employment and earnings outcomes for individuals who participate in the program on the indicators described in subclauses (I) through (III) of section 116(b)(2)(A)(i) of the Workforce Innovation and Opportunity Act. ; and\n**(5)**\nin subsection (f), by striking 2019 through 2023 and inserting 2025 through 2030 .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on such date as the Secretary of Agriculture shall determine, which shall be not later than 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-19T15:28:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr291",
          "measure-number": "291",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr291v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Creating Access to Rural Employment and Education for Resilience and Success Act or the CAREERS Act</strong></p><p>This bill reauthorizes the Rural Innovation Stronger Economy (RISE) Grant Program and expands the program to include support for career pathway programs or industry or sector partnerships in industries in rural communities.</p><p>As background, this Department of Agriculture (USDA) program offers grant assistance to create and augment high-wage jobs, accelerate the formation of new businesses, support industry clusters, and maximize the use of local productive assets in eligible low-income rural areas.</p><p>Under the bill, RISE grant program funds may be used to support career pathway programs (i.e., a combination of rigorous and high-quality education, training, and other services) or industry or sector partnerships in industries in rural communities. These industries may include\u00a0public utilities (i.e., telecommunications, broadband, water, wastewater, disposal, and electric supply services), conservation practices and management, health care, child care, manufacturing, and agribusiness.</p><p>The bill removes the current requirement that the program provide grants (to the maximum extent practicable) for job accelerators in at least 25 states. Instead, USDA must ensure the regional diversity of grant recipients or participants in providing for job accelerators, career pathway programs, and industry or sector partnerships.</p><p>The bill also includes additional reporting requirements for career pathway programs and industry or sector partnership grant recipients.</p>"
        },
        "title": "CAREERS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr291.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating Access to Rural Employment and Education for Resilience and Success Act or the CAREERS Act</strong></p><p>This bill reauthorizes the Rural Innovation Stronger Economy (RISE) Grant Program and expands the program to include support for career pathway programs or industry or sector partnerships in industries in rural communities.</p><p>As background, this Department of Agriculture (USDA) program offers grant assistance to create and augment high-wage jobs, accelerate the formation of new businesses, support industry clusters, and maximize the use of local productive assets in eligible low-income rural areas.</p><p>Under the bill, RISE grant program funds may be used to support career pathway programs (i.e., a combination of rigorous and high-quality education, training, and other services) or industry or sector partnerships in industries in rural communities. These industries may include\u00a0public utilities (i.e., telecommunications, broadband, water, wastewater, disposal, and electric supply services), conservation practices and management, health care, child care, manufacturing, and agribusiness.</p><p>The bill removes the current requirement that the program provide grants (to the maximum extent practicable) for job accelerators in at least 25 states. Instead, USDA must ensure the regional diversity of grant recipients or participants in providing for job accelerators, career pathway programs, and industry or sector partnerships.</p><p>The bill also includes additional reporting requirements for career pathway programs and industry or sector partnership grant recipients.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hr291"
    },
    "title": "CAREERS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating Access to Rural Employment and Education for Resilience and Success Act or the CAREERS Act</strong></p><p>This bill reauthorizes the Rural Innovation Stronger Economy (RISE) Grant Program and expands the program to include support for career pathway programs or industry or sector partnerships in industries in rural communities.</p><p>As background, this Department of Agriculture (USDA) program offers grant assistance to create and augment high-wage jobs, accelerate the formation of new businesses, support industry clusters, and maximize the use of local productive assets in eligible low-income rural areas.</p><p>Under the bill, RISE grant program funds may be used to support career pathway programs (i.e., a combination of rigorous and high-quality education, training, and other services) or industry or sector partnerships in industries in rural communities. These industries may include\u00a0public utilities (i.e., telecommunications, broadband, water, wastewater, disposal, and electric supply services), conservation practices and management, health care, child care, manufacturing, and agribusiness.</p><p>The bill removes the current requirement that the program provide grants (to the maximum extent practicable) for job accelerators in at least 25 states. Instead, USDA must ensure the regional diversity of grant recipients or participants in providing for job accelerators, career pathway programs, and industry or sector partnerships.</p><p>The bill also includes additional reporting requirements for career pathway programs and industry or sector partnership grant recipients.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hr291"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr291ih.xml"
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
      "title": "CAREERS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CAREERS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Creating Access to Rural Employment and Education for Resilience and Success Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Rural Innovation Stronger Economy Grant Program of the Department of Agriculture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:35Z"
    }
  ]
}
```
