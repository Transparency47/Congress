# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/812?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/812
- Title: MAKERS Act
- Congress: 119
- Bill type: HR
- Bill number: 812
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-03-20T08:06:55Z
- Update date including text: 2026-03-20T08:06:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/812",
    "number": "812",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001157",
        "district": "13",
        "firstName": "David",
        "fullName": "Rep. Scott, David [D-GA-13]",
        "lastName": "Scott",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "MAKERS Act",
    "type": "HR",
    "updateDate": "2026-03-20T08:06:55Z",
    "updateDateIncludingText": "2026-03-20T08:06:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:05:50Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "PA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "GA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "IN"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "IL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NC"
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
      "sponsorshipDate": "2026-03-19",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr812ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 812\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. David Scott of Georgia (for himself, Mr. Fitzpatrick , Mr. Takano , Mr. Johnson of Georgia , Mr. Jackson of Illinois , Mr. Carson , Mr. Foster , Ms. Vel\u00e1zquez , and Mrs. Foushee ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo direct the Director of the National Science Foundation to award grants for, and support research on, the development of makerspaces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making Advances Kinetic Education, Research, and Skills Act or the MAKERS Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMaker communities can be found in both rural and urban communities throughout the Nation.\n**(2)**\nMaking has been shown to engage and motivate children and adults in STEM disciplines.\n**(3)**\nInformal education and makerspaces promote skills that employers desire, such as technical skills, problem-solving skills, teamwork, and analytical skills.\n**(4)**\nStudies have shown that underrepresented populations often have better successes in informal and out-of-school STEM than in formal STEM programs.\n**(5)**\nSome studies have shown that makerspaces help to build not only technical hard skills but also collaboration and other soft skills that employers desire.\n#### 3. Purpose\nThe purpose of this Act is to encourage the formation and study of makerspaces to\u2014\n**(1)**\nengage populations within community colleges and community environments in STEM programs;\n**(2)**\ndevelop desirable STEM technical and other skills, including collaboration; and\n**(3)**\nbuild a STEM-capable workforce.\n#### 4. Definitions\nIn this Act, the following definitions apply:\n**(1) Historically Black college or university**\nThe term \u201chistorically Black college or university\u201d has the meaning given the term \u201cpart B institution\u201d under section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 ).\n**(2) Makerspace**\nThe term makerspace means a community space that\u2014\n**(A)**\nprovides access to tools, technology, and knowledge for learners and entrepreneurs;\n**(B)**\nresults in the prototyping or creation of physical goods, interdisciplinary learning, and educational innovation; and\n**(C)**\nsupports the development of educational opportunities for personal growth, workforce training, and early stage business ventures.\n**(3) Minority-serving institution**\nThe term \u201cminority-serving institution\u201d means an institution listed in section 371(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1067q(a) ).\n**(4) Rural community**\nThe term rural community has the meaning given the term rural area in section 520 of the Housing Act of 1949 ( 42 U.S.C. 1490 ).\n**(5) STEM**\nThe term STEM means the subjects of science, technology, engineering, and mathematics.\n**(6) Workforce development component**\nThe term workforce development component means\u2014\n**(A)**\nan economic development board or corporation, including a State board or local workforce board;\n**(B)**\nan internship program;\n**(C)**\na certificate program;\n**(D)**\nemployers or an employer or industry partnership representing multiple employers;\n**(E)**\na community-based organization; or\n**(F)**\nany other program considered acceptable by the Director of the National Science Foundation.\n#### 5. Grant program for research and capacity building of makerspaces\n##### (a) Establishment\nThe Director of the National Science Foundation shall award grants on a competitive basis to institutions of higher education, or consortia of such institutions, to support the research and development of makerspaces to assist in the formation of a STEM-capable workforce.\n##### (b) Use of funds\nA grant awarded under this section may be used for\u2014\n**(1)**\nresearch on the effectiveness of makerspaces in engaging students and the community in STEM skills and in teaching and learning, and the development, compilation, and dissemination of best practices on the use of makerspaces for STEM learning and workforce preparedness;\n**(2)**\nequipment to achieve the purpose under paragraph (1); and\n**(3)**\nany other activities the Director considers appropriate.\n##### (c) Priority\nIn selecting grant recipients under this section, the Director shall give priority to applicants that\u2014\n**(1)**\napply in partnership with one or more entities that are\u2014\n**(A)**\na workforce development component;\n**(B)**\na high-need local education agency as described in section 9(b)(3) of the National Science Foundation Authorization Act of 2002 ( 42 U.S.C. 1862n(b)(3) ); or\n**(C)**\nan independent nonprofit or academic makerspace;\n**(2)**\nconsist of one or more entities that are\u2014\n**(A)**\na community college; or\n**(B)**\na historically Black college or university or other minority-serving institution of higher education; or\n**(3)**\napply in partnership with or consist of an entity that is\u2014\n**(A)**\ndescribed in paragraph (1) or (2); and\n**(B)**\noperates within a rural community.\n##### (d) Limitation\nFunds provided through a grant under this section may not be used for the construction of a physical building or facility to hold a makerspace unless the Director determines that such construction is necessary for reasons of safety or the use of relevant equipment.\n##### (e) Technical assistance\nThe Director may provide technical assistance to entities receiving a grant or entities seeking such a grant under this section.",
      "versionDate": "2025-01-28",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-03T17:00:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr812",
          "measure-number": "812",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr812v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Making Advances Kinetic Education, Research, and Skills Act or the MAKERS Act</strong></p><p>This bill requires the National Science Foundation (NSF) to award competitive grants to institutions of higher education to support research and development related to makerspaces. Under the bill, <em>makerspaces</em> are defined as community spaces that provide learners and entrepreneurs with tools, technology, and knowledge, and support educational opportunities for personal growth, workforce training, and early-stage business ventures.</p><p>Grant funds may be used to support research on the effectiveness of makerspaces in engaging students and communities in science, technology, engineering, and math (STEM), among other functions.</p><p>In awarding\u00a0grants, the NSF must prioritize certain applicants, including (1) community colleges and minority-serving institutions; and (2) institutions that apply in partnership with workforce development entities, high-need local educational agencies, or independent nonprofit or academic makerspaces.</p>"
        },
        "title": "MAKERS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr812.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Making Advances Kinetic Education, Research, and Skills Act or the MAKERS Act</strong></p><p>This bill requires the National Science Foundation (NSF) to award competitive grants to institutions of higher education to support research and development related to makerspaces. Under the bill, <em>makerspaces</em> are defined as community spaces that provide learners and entrepreneurs with tools, technology, and knowledge, and support educational opportunities for personal growth, workforce training, and early-stage business ventures.</p><p>Grant funds may be used to support research on the effectiveness of makerspaces in engaging students and communities in science, technology, engineering, and math (STEM), among other functions.</p><p>In awarding\u00a0grants, the NSF must prioritize certain applicants, including (1) community colleges and minority-serving institutions; and (2) institutions that apply in partnership with workforce development entities, high-need local educational agencies, or independent nonprofit or academic makerspaces.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr812"
    },
    "title": "MAKERS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Making Advances Kinetic Education, Research, and Skills Act or the MAKERS Act</strong></p><p>This bill requires the National Science Foundation (NSF) to award competitive grants to institutions of higher education to support research and development related to makerspaces. Under the bill, <em>makerspaces</em> are defined as community spaces that provide learners and entrepreneurs with tools, technology, and knowledge, and support educational opportunities for personal growth, workforce training, and early-stage business ventures.</p><p>Grant funds may be used to support research on the effectiveness of makerspaces in engaging students and communities in science, technology, engineering, and math (STEM), among other functions.</p><p>In awarding\u00a0grants, the NSF must prioritize certain applicants, including (1) community colleges and minority-serving institutions; and (2) institutions that apply in partnership with workforce development entities, high-need local educational agencies, or independent nonprofit or academic makerspaces.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr812"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr812ih.xml"
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
      "title": "MAKERS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MAKERS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Making Advances Kinetic Education, Research, and Skills Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the National Science Foundation to award grants for, and support research on, the development of makerspaces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:34Z"
    }
  ]
}
```
