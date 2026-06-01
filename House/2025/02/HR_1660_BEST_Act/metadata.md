# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1660?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1660
- Title: BEST Act
- Congress: 119
- Bill type: HR
- Bill number: 1660
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-12-10T09:05:43Z
- Update date including text: 2025-12-10T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1660",
    "number": "1660",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "BEST Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:05:43Z",
    "updateDateIncludingText": "2025-12-10T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:10:50Z",
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NM"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DC"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MI"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WI"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
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
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-18",
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
      "sponsorshipDate": "2025-04-01",
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
      "sponsorshipDate": "2025-05-09",
      "state": "RI"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1660ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1660\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Brownley (for herself, Ms. Schakowsky , Mr. Mullin , Ms. Chu , Ms. Stansbury , Ms. Norton , Mr. Panetta , Ms. Ross , Mr. Vargas , Mr. Thanedar , Ms. Moore of Wisconsin , Mr. Larson of Connecticut , Mr. Johnson of Georgia , Ms. S\u00e1nchez , Ms. Barrag\u00e1n , and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo award grants to States to establish or improve, and carry out, Seal of Biliteracy programs to recognize high-level student proficiency in speaking, reading, and writing in both English and a second language, and early language programs.\n#### 1. Short title\nThis Act may be cited as the Biliteracy Education Seal and Teaching Act or the BEST Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe people of the United States celebrate cultural and linguistic diversity and seek to prepare students with skills to succeed in the 21st century.\n**(2)**\nIt is fitting to commend the dedication of students who have achieved proficiency in multiple languages and to encourage their peers to follow in their footsteps.\n**(3)**\nThe congressionally requested Commission on Language Learning, in its 2017 report America's Languages: Investing in Language Education for the 21st Century , notes the pressing national need for more people of the United States who are proficient in 2 or more languages for national security, economic growth, and the fulfillment of the potential of all people of the United States.\n**(4)**\nThe Commission on Language Learning also notes the extensive cognitive, educational, and employment benefits deriving from biliteracy.\n**(5)**\nBiliteracy in general correlates with higher graduation rates, higher grade point averages, higher rates of matriculation into higher education, and higher earnings for all students, regardless of background.\n**(6)**\nThe study of America\u2019s languages in elementary and secondary schools should be encouraged because it contributes to a student\u2019s cognitive development and to the national economy and security.\n**(7)**\nRecognition of student achievement in language proficiency will enable institutions of higher education and employers to readily recognize and acknowledge the valuable expertise of bilingual students in academia and the workplace.\n**(8)**\nStates such as Utah, Arizona, Washington, and New Mexico have developed innovative testing methods for languages, including Native American languages, where no formal proficiency test currently exists.\n**(9)**\nThe use of proficiency in a government-recognized official Native American language as the base language for a Seal of Biliteracy, with proficiency in any additional partner language demonstrated through tested proficiency, has been successfully demonstrated in Hawaii.\n**(10)**\nStudents in every State and every school should be able to benefit from a Seal of Biliteracy program.\n#### 3. Definitions\nIn this Act:\n**(1) ESEA definitions**\nThe terms elementary school , English learner , local educational agency , middle grades , secondary school , and State have the meanings given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Classical language**\nThe term classical language \u2014\n**(A)**\nmeans\u2014\n**(i)**\na language that is no longer spoken; or\n**(ii)**\na language\u2014\n**(I)**\nthe spoken varieties of which diverge further away from the classical language over time; and\n**(II)**\nthat possesses an independent literary tradition and a large body of ancient written literature; and\n**(B)**\nincludes Greek, Latin, Chinese, Arabic, and Sanskrit.\n**(3) Native American language**\nThe term Native American language has the meaning given the term in section 103 of the Native American Languages Act ( 25 U.S.C. 2902 ).\n**(4) Seal of Biliteracy program**\nThe term Seal of Biliteracy program means any program described in section 4(a) that is established or improved, and carried out, with funds received under this Act.\n**(5) Second language**\nThe term second language \u2014\n**(A)**\nmeans any language other than\u2014\n**(i)**\nEnglish; or\n**(ii)**\nin a case where the provisions of paragraph (2) of section 4(a) apply, the Native American language of proficiency described in such paragraph; and\n**(B)**\nincludes Braille, American Sign Language, or a classical language.\n**(6) Secretary**\nThe term Secretary means the Secretary of Education.\n#### 4. Grants for State Seal of Biliteracy programs\n##### (a) Establishment of program\n**(1) In general**\nFrom amounts made available under subsection (f), the Secretary shall award grants, on a competitive basis, to States to enable the States to establish or improve, and carry out, Seal of Biliteracy programs and early language programs that lead to a Seal of Biliteracy to recognize student proficiency in both English and a second language, which\u2014\n**(A)**\nshall be demonstrated through proficiency in speaking and writing in both languages; and\n**(B)**\nmay also be demonstrated through reading and listening in both languages.\n**(2) Inclusion of Native American languages**\nNotwithstanding paragraph (1), each Seal of Biliteracy program shall contain provisions allowing the use of Native American languages, including allowing speakers of any Native American language recognized as official by any American government, including any Tribal government, to use equivalent proficiency in speaking, reading, and writing in the Native American language in lieu of proficiency in speaking, reading, and writing in English.\n**(3) Duration**\nA grant awarded under this section shall be for a period of 2 years, and may be renewed at the discretion of the Secretary.\n**(4) Renewal**\nAt the end of a grant term, a State that receives a grant under this section may reapply for a grant under this section.\n**(5) Limitations**\nA State shall not receive more than 1 grant under this section at any time.\n**(6) Return of unspent grant funds**\nEach State that receives a grant under this section shall return any unspent grant funds not later than 6 months after the date on which the term for the grant ends.\n##### (b) Grant program\nA State that desires a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information and assurances as the Secretary may require, including\u2014\n**(1)**\na description of the criteria a student must meet to demonstrate proficiency for the State Seal of Biliteracy in both languages, which\u2014\n**(A)**\nshall include proficiency criteria for the 2 productive skills of speaking and writing; and\n**(B)**\nmay include proficiency criteria for the skills of reading and listening;\n**(2)**\na detailed description of the State\u2019s plan\u2014\n**(A)**\nto ensure that English learners and former English learners are included in the State Seal of Biliteracy program;\n**(B)**\nto ensure equitable access to the State Seal of Biliteracy program for students with identified disabilities, including vision and hearing impairments and cognitive or learning disabilities, that preclude demonstration of language proficiency in one of the skills identified in paragraph (1);\n**(C)**\nto ensure that\u2014\n**(i)**\nall languages, including Native American languages and American Sign Language, can be tested for the State Seal of Biliteracy program; and\n**(ii)**\nNative American language speakers and learners are included in the State Seal of Biliteracy program, including students at tribally controlled schools and at schools funded by the Bureau of Indian Education; and\n**(D)**\nto reach elementary school and middle grades students (including eligible students described in subsection (c)(2), heritage language learners, and English learners), their parents, and schools with information regarding the State Seal of Biliteracy program;\n**(3)**\nan assurance that a student who meets the requirements under paragraph (1) and subsection (c) receives\u2014\n**(A)**\na permanent seal or other marker on the student's secondary school diploma or its equivalent; or\n**(B)**\ndocumentation of proficiency on the student's official academic transcript; and\n**(4)**\nan assurance that a student is not charged a fee for providing information under subsection (c)(1).\n##### (c) Student participation in a Seal of Biliteracy program\n**(1) In general**\nTo participate in a Seal of Biliteracy program, a student shall provide information to the State that serves the student at such time, in such manner, and including such information and assurances as the State may require, including an assurance that the student has met the criteria established by the State under subsection (b)(1).\n**(2) Student eligibility for participation**\nA student who gained proficiency in a second language outside of school may apply to the State of the student's residence under paragraph (1) to participate in a Seal of Biliteracy program.\n##### (d) Use of funds\nGrant funds made available under this section shall be used for\u2014\n**(1)**\nthe administrative costs of establishing or improving, and carrying out, a Seal of Biliteracy program that meets the requirements of subsection (b);\n**(2)**\npublic outreach and education about the Seal of Biliteracy program; and\n**(3)**\nsubgrants to local educational agencies for language educator professional development, public outreach, and subsidizing baseline and final Seal of Biliteracy testing for low-income students.\n##### (e) Report\nNot later than 18 months after receiving a grant under this section, a State shall issue a report to the Secretary describing the implementation of the Seal of Biliteracy program for which the State received the grant.\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2025 through 2029.",
      "versionDate": "2025-02-27",
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
        "name": "Education",
        "updateDate": "2025-03-18T16:18:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1660",
          "measure-number": "1660",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1660v00",
            "update-date": "2025-05-08"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Biliteracy Education Seal and Teaching Act or the BEST Act</strong></p><p>This bill directs the Department of Education to award renewable two-year grants to states to establish or improve, and carry out, Seal of Biliteracy programs and early language programs\u00a0to recognize student proficiency in both English and a second language. Student proficiency shall be demonstrated through proficiency in speaking and writing in both languages and may also be demonstrated through reading and listening in both languages.\u00a0 \u00a0</p><p>Further, these programs must allow speakers of any official Native American language to use equivalent proficiency in speaking, reading, and writing in such language in lieu of proficiency in English.</p>"
        },
        "title": "BEST Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1660.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Biliteracy Education Seal and Teaching Act or the BEST Act</strong></p><p>This bill directs the Department of Education to award renewable two-year grants to states to establish or improve, and carry out, Seal of Biliteracy programs and early language programs\u00a0to recognize student proficiency in both English and a second language. Student proficiency shall be demonstrated through proficiency in speaking and writing in both languages and may also be demonstrated through reading and listening in both languages.\u00a0 \u00a0</p><p>Further, these programs must allow speakers of any official Native American language to use equivalent proficiency in speaking, reading, and writing in such language in lieu of proficiency in English.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119hr1660"
    },
    "title": "BEST Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Biliteracy Education Seal and Teaching Act or the BEST Act</strong></p><p>This bill directs the Department of Education to award renewable two-year grants to states to establish or improve, and carry out, Seal of Biliteracy programs and early language programs\u00a0to recognize student proficiency in both English and a second language. Student proficiency shall be demonstrated through proficiency in speaking and writing in both languages and may also be demonstrated through reading and listening in both languages.\u00a0 \u00a0</p><p>Further, these programs must allow speakers of any official Native American language to use equivalent proficiency in speaking, reading, and writing in such language in lieu of proficiency in English.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119hr1660"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1660ih.xml"
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
      "title": "BEST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:57:58Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BEST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Biliteracy Education Seal and Teaching Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To award grants to States to establish or improve, and carry out, Seal of Biliteracy programs to recognize high-level student proficiency in speaking, reading, and writing in both English and a second language, and early language programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:33Z"
    }
  ]
}
```
