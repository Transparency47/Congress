# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1572?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1572
- Title: World LEAP Act
- Congress: 119
- Bill type: HR
- Bill number: 1572
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-04-16T08:07:01Z
- Update date including text: 2026-04-16T08:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1572",
    "number": "1572",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "World LEAP Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:07:01Z",
    "updateDateIncludingText": "2026-04-16T08:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NM"
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
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "DE"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "RI"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-26",
      "state": "VA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "AL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1572ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1572\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mrs. Kiggans of Virginia (for herself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Education to award grants to local educational agencies to establish or improve world language or dual language programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the World Language Education Assistance Program Act or the World LEAP Act .\n#### 2. Purpose\nThe purpose of this Act is to establish and make assistance available to the World Language Education Assistance Program in order to\u2014\n**(1)**\nestablish or improve and carry out World Language Education Assistance Program grant programs;\n**(2)**\nsupport and uplift dual language and world language programs; and\n**(3)**\nprovide students with the language skills necessary for an interconnected and global world.\n#### 3. Findings\nCongress finds the following:\n**(1)**\nRecent academic studies demonstrate that America\u2019s language capacity has reached a crisis point, with only one fifth of United States residents speaking a language other than English at home, 90 percent of United States-based employers reporting a reliance on employees with language skills other than English, and one third of foreign language-dependent employers reporting a language skills gap. This language crisis has real world implications for business, government, the military, and diplomatic and intelligence services.\n**(2)**\nThe Department of Education does not have an innovative world languages program for elementary and secondary students.\n**(3)**\nThe Nation\u2019s education system is suffering from severe shortages of world language, English learner, and bilingual and dual language immersion educators.\n**(4)**\nThe lack of a Federal elementary and secondary school world language and dual language program, coupled with the continuing shortage of world language and bilingual teachers, creates significant obstacles to providing equitable opportunities for all students to develop multilingualism. English learners, a population which has grown by 2,100,000 between 2000 and 2019, have been disproportionately impacted.\n**(5)**\nThe Federal Government has a strong interest in better preparing American students to compete in the global economy.\n#### 4. Definitions\nIn this Act:\n**(1) Community-based heritage language school**\nThe term community-based heritage language school means a nonprofit, community-based school that offers classes for students in pre-kindergarten through grade 12, for the purpose of maintaining and teaching the language and culture of non-English speaking communities.\n**(2) Dual language program**\nThe term dual language program means\u2014\n**(A)**\nwith respect to pre-kindergarten and elementary school, a bilingual education program in which students receive instruction in English and a language other than English for at least half of the instructional school day for each year of pre-kindergarten and elementary school, with the goal of achieving proficiency in both languages; and\n**(B)**\nwith respect to grades 6 through 8, a bilingual education program in which students who participated in a program described in subparagraph (A) continue to receive instruction in English and a language other than English for at least half of the instructional school day for each year of such grades 6 through 8.\n**(3) ESEA definitions**\nThe terms English learner , secondary school , local educational agency , professional development , Secretary , and State have the meanings given those terms in section 8101 of the Elementary and Secondary Act of 1965 ( 20 U.S.C. 7801 ).\n**(4) Heritage learner**\nThe term heritage learner means an individual\u2014\n**(A)**\nwith proficiency in, or a cultural connection to (through family, community, or country of origin), a language other than English; and\n**(B)**\nwho is studying such language in pre-kindergarten, elementary school, or secondary school.\n**(5) World language program**\nThe term world language program means a program that educates and prepares pre-kindergarten, elementary, or secondary school students to communicate, in a proficient and culturally competent manner, with individuals who speak a language other than English.\n#### 5. World language education assistance program\n##### (a) Establishment\n**(1) In general**\nThe Secretary shall award, on a competitive basis, grants to local educational agencies to establish and carry out new, or improve existing world language or dual language programs.\n**(2) Duration**\nA grant awarded under this section shall be for a period of 3 years and may be renewed at the discretion of the Secretary.\n##### (b) Application\nA local educational agency desiring a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information and assurances as the Secretary may require.\n##### (c) Criteria for selection\n**(1) In general**\nIn awarding a grant to a local educational agency under this section, the Secretary shall select applications describing programs that\u2014\n**(A)**\nprovide approaches to instruction that lead to demonstrated growth in language proficiency from kindergarten through grade 12;\n**(B)**\ncan be disseminated and duplicated in other local educational agencies;\n**(C)**\nhave a plan for how the program will continue after the conclusion of the grant period; and\n**(D)**\ninclude a professional development component.\n**(2) Priority**\nIn awarding grants under this section, the Secretary shall give priority to applications describing programs that\u2014\n**(A)**\ninclude intensive summer professional development for world language program and dual language program teachers;\n**(B)**\nenter into partnerships with community-based heritage language schools and communities;\n**(C)**\nprovide world language and dual language immersion programs, including with respect to English learners and heritage learners;\n**(D)**\nare carried out through a consortium that shall include the agency receiving the grant and an elementary school or secondary school served by such agency, with a preference for consortia that include an institution of higher education;\n**(E)**\ncollaborate with the appropriate State licensure office to broaden pathways for language or dual language teacher certification; or\n**(F)**\nconduct outreach and recruit secondary and post-secondary students, including former English learners and heritage learners, into programs that prepare such students to become dual language or world language program teachers.\n##### (d) Use of funds\nA local educational agency that receives a grant under this section shall\u2014\n**(1)**\nreserve not less than 20 percent of such grant funds to provide\u2014\n**(A)**\naccessible pathways for paraprofessionals to gain certification and licensure as world language or dual language teachers; and\n**(B)**\nprofessional development for certified and licensed world language or dual language teachers;\n**(2)**\nreserve not more than 5 percent of such grant funds to evaluate the efficacy of programs carried out with funds awarded under this section; and\n**(3)**\nafter making the reservations required under paragraphs (1) and (2), use the remainder of such grant funds to establish and carry out new, and improve existing, world language or dual language programs (including any associated administrative expenses).\n##### (e) Reporting requirements\n**(1) In general**\nNot later than 18 months after receiving a grant under this section, each local educational agency shall submit to the Secretary a report that\u2014\n**(A)**\ndescribes the implementation of the program for which the local educational agency received the grant; and\n**(B)**\nincludes data that identifies\u2014\n**(i)**\nthe number of students enrolled in language education at the elementary and secondary schools served by the local educational agency prior to receiving a grant under this section;\n**(ii)**\nthe number of students enrolled in such language instruction as of the date of submission of the report;\n**(iii)**\nthe number of certified bilingual educators working for the local educational agency prior to receiving a grant under this section;\n**(iv)**\nthe number of certified bilingual educators working for the local educational agency as of the date of submission of the report; and\n**(v)**\nlevels of community support for language education\u2014\n**(I)**\nprior to receiving a grant under this section; and\n**(II)**\nas of the date of submission of the report.\n**(2) Student privacy**\nA local educational agency shall prepare the report required under paragraph (1) in a manner that protects the privacy rights of each student in accordance with section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g ; commonly known as the Family Educational Rights and Privacy Act of 1974 ).\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $15,000,000 for fiscal year 2026 and for each subsequent fiscal year.",
      "versionDate": "2025-02-25",
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
            "name": "Congressional oversight",
            "updateDate": "2026-04-13T15:02:47Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2026-04-13T15:02:17Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-04-13T15:02:26Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-04-13T15:02:36Z"
          },
          {
            "name": "Foreign language and bilingual programs",
            "updateDate": "2026-04-13T15:02:22Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-04-13T15:02:52Z"
          },
          {
            "name": "Student records",
            "updateDate": "2026-04-13T15:02:58Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-04-13T15:02:41Z"
          },
          {
            "name": "Vocational and technical education",
            "updateDate": "2026-04-13T15:02:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-21T14:45:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119hr1572",
          "measure-number": "1572",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1572v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>World Language Education Assistance Program Act or the World LEAP Act</b></p> <p>This bill requires the Department of Education to award competitive grants to local educational agencies to establish and carry out new, or improve existing, world language or dual language programs.</p>"
        },
        "title": "World LEAP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1572.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><b>World Language Education Assistance Program Act or the World LEAP Act</b></p> <p>This bill requires the Department of Education to award competitive grants to local educational agencies to establish and carry out new, or improve existing, world language or dual language programs.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1572"
    },
    "title": "World LEAP Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><b>World Language Education Assistance Program Act or the World LEAP Act</b></p> <p>This bill requires the Department of Education to award competitive grants to local educational agencies to establish and carry out new, or improve existing, world language or dual language programs.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1572"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1572ih.xml"
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
      "title": "World LEAP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "World LEAP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "World Language Education Assistance Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Education to award grants to local educational agencies to establish or improve world language or dual language programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:22Z"
    }
  ]
}
```
