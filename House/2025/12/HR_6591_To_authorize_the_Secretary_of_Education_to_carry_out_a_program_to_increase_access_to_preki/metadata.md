# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6591?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6591
- Title: Computer Science for All Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6591
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-31T09:05:41Z
- Update date including text: 2026-01-31T09:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6591",
    "number": "6591",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "R000620",
        "district": "29",
        "firstName": "Luz",
        "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
        "lastName": "Rivas",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Computer Science for All Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-31T09:05:41Z",
    "updateDateIncludingText": "2026-01-31T09:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:05:10Z",
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "RI"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "OH"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
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
      "sponsorshipDate": "2025-12-10",
      "state": "IN"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "WA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-10",
      "state": "DC"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MD"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NJ"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "IL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NV"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "WA"
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
      "sponsorshipDate": "2026-01-12",
      "state": "NC"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "IL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NY"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6591ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6591\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. Rivas (for herself, Mr. Amo , Mrs. Beatty , Ms. Budzinski , Mr. Carson , Ms. DelBene , Mr. Goldman of New York , Ms. Norton , Mr. Ivey , Ms. Kelly of Illinois , Mr. Lieu , Mrs. McIver , Mr. Quigley , and Ms. Titus ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo authorize the Secretary of Education to carry out a program to increase access to prekindergarten through grade 12 computer science education.\n#### 1. Short title\nThis Act may be cited as the Computer Science for All Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nComputer science is transforming industry, creating new fields of commerce, driving innovation, and bolstering productivity. By 2034, computer science and information jobs are expected to grow by 20 percent, faster than the average of any other occupation.\n**(2)**\nKnowledge of computer science and use of technology is increasingly essential for all individuals, not just those working or planning to work in the technology sector.\n**(3)**\nProviding students with computer science education in elementary school and secondary school is critical for student success, and strengthening the workforce of a 21st century economy.\n**(4)**\nWhile an estimated 90 percent of parents want computer science taught in their children\u2019s schools, just 60 percent of public high schools offer a foundational computer science course.\n**(5)**\nBlack and Hispanic workers in the science and engineering workforce continue to be underrepresented. Black employees represent 11 percent of the United States workforce, but only 9 percent of the STEAM workforce. Hispanic employees represent 17 percent of the United States workforce, but only 8 percent of the STEAM workforce.\n**(6)**\nWhile underrepresented minority students overall face an opportunity gap in STEAM education, women of color particularly face an achievement gap in science and engineering education. In 2022, while women were conferred nearly a third of all science and engineering degrees, women of color received only 15 percent (Black: 3 percent; Hispanic: 4.5 percent; Native American or Alaskan Native: 1 percent; Asian or Pacific Islander: 5 percent; and multiracial: 1 percent).\n**(7)**\nIn 2022, of all engineering technologies and engineering-related bachelor level-related studies, only 4 percent of nationwide enrollment was represented by Black students, while just 13 percent were represented by Hispanic students.\n**(8)**\nWomen overall face challenges in accessing computer science education. Only 18 percent of all bachelor\u2019s degrees conferred in computer science went to women in 2015, and women of color received only 9 percent of degrees (Black: 3 percent; Hispanic: 2 percent; Native American or Alaska Native: 0.8 percent; and Asian or Pacific islander: 3 percent).\n**(9)**\nLack of universal computer science education is evident in the lack of a widespread tech industry, which is overwhelmingly concentrated in a few cities nationwide. Tech industry entrepreneurship is concentrated in just a few States and computer science education is limited to affluent schools and students, placing low-income, minority, and rural communities at risk of being left behind.\n#### 3. Definitions\nIn this Act:\n**(1) Computational thinking**\nThe term computational thinking \u2014\n**(A)**\nmeans the wide range of creative processes that go into formulating problems and their solutions in such a way that the solutions can be carried out by a computer; and\n**(B)**\nmay involve some understanding of software and hardware design, logic and the use of abstraction and representation, algorithm design, algorithm expression, problem decomposition, modularity, programming paradigms and languages, issues of information security and privacy, the application of computation across a wide range of disciplines, and the societal impact of computing. Programming is a hands-on, inquiry-based way in which computational thinking may be learned.\n**(2) Computer science education**\nThe term computer science education includes any of the following:\n**(A)**\nComputational thinking.\n**(B)**\nSoftware design.\n**(C)**\nHardware architecture and organization.\n**(D)**\nTheoretical foundations.\n**(E)**\nUse of abstraction and representation in problem solving.\n**(F)**\nLogic.\n**(G)**\nAlgorithm design and implementation.\n**(H)**\nThe limits of computation.\n**(I)**\nProgramming paradigms and languages.\n**(J)**\nParallel and distributed computing.\n**(K)**\nInformation security and privacy.\n**(L)**\nComputing systems and networks.\n**(M)**\nGraphics and visualization.\n**(N)**\nDatabases and information retrieval.\n**(O)**\nThe relationship between computing and mathematics.\n**(P)**\nArtificial intelligence.\n**(Q)**\nApplications of computing across a broad range of disciplines and problems.\n**(R)**\nCloud computing.\n**(S)**\nThe social impacts and professional practices of computing.\n**(3) Eligible entity**\nThe term eligible entity means a State, local educational agency, or eligible Tribal school that demonstrates an ability to carry out an ambitious computer science education expansion effort for all students served by the State, agency, or school, respectively, including traditionally underrepresented students.\n**(4) Eligible tribal school**\nThe term eligible Tribal school means\u2014\n**(A)**\na school operated by the Bureau of Indian Education;\n**(B)**\na school operated pursuant to the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 450 et seq. ); or\n**(C)**\na tribally controlled school (as defined in section 5212 of the Tribally Controlled Schools Act of 1988 ( 25 U.S.C. 2511 )).\n**(5) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n**(6) Local educational agency**\nThe term local educational agency means a local educational agency that meets the requirements of section 1003(f) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6303(f) ).\n**(7) Poverty line**\nThe term poverty line has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 8101 ).\n**(8) Secretary**\nThe term Secretary means the Secretary of Education.\n**(9) State**\nThe term State has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ), in which at least one local educational agency is located.\n**(10) STEAM**\nThe term STEAM means the subjects of science, technology, engineering, arts, and mathematics, including computer science.\n#### 4. Grants to states, local educational agencies, and eligible tribal schools\n##### (a) Grants to states, local educational agencies, and eligible tribal schools\n**(1) In general**\nThe Secretary shall award grants to eligible entities to serve as models for national replication of computer science education expansion efforts.\n**(2) Consortia and partnerships**\nAn eligible entity may apply for a grant under this section as part of a consortium or in partnership with a State educational agency or other partner.\n**(3) Duration**\nGrants awarded under this section shall be for a period of not more than 5 years.\n##### (b) Application requirements\nAn eligible entity that desires a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including, at a minimum, plans for the following:\n**(1)**\nEvery high school student served by eligible entity to have access to computer science education not later than 5 years after receipt of grant funds.\n**(2)**\nAll students served by the eligible entity to have access to a progression of computer science education from prekindergarten through middle school that prepares students for high school computer science education.\n**(3)**\nExpansion of overall access to rigorous STEAM classes, utilizing computer science as a catalyst for increased interest in STEAM more broadly, and reducing the enrollment and academic achievement gap for underrepresented groups such as minorities, girls, and youth from families living at, or below, the poverty line.\n**(4)**\nContinuous monitoring and evaluation of project activities.\n**(5)**\nEffectively sustaining project activities after the grant period ends, and the length of time which the applicant plans to sustain the project activities.\n**(6)**\nPreparing the students for application of computer science knowledge in rapidly evolving technologies, such as artificial intelligence.\n##### (c) Use of grant funds\n**(1) Required activities**\nAn eligible entity that receives a grant under this section shall use the grant funds for each of the following activities:\n**(A)**\nTraining teachers of elementary school and secondary school to teach computer science.\n**(B)**\nExpanding access to high-quality learning materials and online learning options.\n**(C)**\nCreating plans for expanding overall access to rigorous STEAM classes, utilizing computer science as a catalyst for increased interest in STEAM more broadly, and reducing course equity gaps for all students, including underrepresented groups such as minorities, girls, and youth from low-income families.\n**(D)**\nEnsuring additional support and resources, which may include mentoring for students traditionally underrepresented in STEAM fields.\n**(2) Permissible activities**\nAn eligible entity that receives a grant under this section may use the grant funds for the following activities:\n**(A)**\nBuilding effective regional collaborations with industry, nonprofit organizations, 2-year and 4-year degree granting institutions of higher education (including community colleges, Historically Black Colleges and Universities, Hispanic-serving institutions, Asian American and Native American Pacific Islander-serving institutions, American Indian Tribally controlled colleges and universities, Alaska Native and Native Hawaiian-serving institutions, Predominantly Black Institutions, Native American-serving, Nontribal institutions, and other minority-serving institutions), and out-of-school providers.\n**(B)**\nRecruiting and hiring instructional personnel as needed, including curriculum specialists.\n**(C)**\nPreparations for effectively sustaining project activities after the grant period ends.\n**(D)**\nDisseminating information about effective practices.\n**(E)**\nIncluding the use of artificial intelligence in the classroom to expand students\u2019 access to a rapidly evolving technology.\n**(3) Limitation**\nNot more than 15 percent of a grant awarded under this Act may be used to purchase equipment.\n##### (d) National activities\nOf the amount appropriated under subsection (e) for a fiscal year, the Secretary may reserve not more than 2.5 percent of funds available for grants under this section for national activities, including technical assistance, evaluation, and dissemination.\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section a total of $250,000,000 for fiscal year 2026 and the succeeding 4 fiscal years.\n#### 5. Reporting requirements\n##### (a) Grantee reports\nEach eligible entity that receives a grant under this Act shall submit to the Secretary a report, not less than twice a year during the grant period, on the use of grant funds that shall include data on the numbers of students served through activities funded under this Act, disaggregated by race (for Asian and Native Hawaiian or Pacific Islander students using the same race response categories as the decennial census of the population), ethnicity, gender, and eligibility to receive a free or reduced price lunch under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ).\n##### (b) Report by the secretary\nNot later than 5 years after the first grant is awarded under this Act, the Secretary shall submit to Congress a report based on the analysis of reports received under subsection (a) with a recommendation on how to expand the program under this Act.\n#### 6. Amendments to other laws\n##### (a) Department of Education Organization Act\nSection 203(c)(1) of the Department of Education Organization Act ( 20 U.S.C. 3413(c)(1) ) is amended by inserting before the semicolon the following: , which shall include information with respect to the existence of computer science education (as defined in section 3 of the Computer Science for All Act of 2025 ), disaggregated by the type of computer science education and by State, local educational agency, and eligible tribal school (as such terms are defined in such section 3) .\n##### (b) The Education Sciences Reform Act of 2002\nSection 153(a)(1) of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9543(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (N), by striking and at the end;\n**(2)**\nin subparagraph (O), by adding and at the end; and\n**(3)**\nby adding at the end the following:\n(P) the existence of computer science education (as defined in section 3 of the Computer Science for All Act of 2025 ) in elementary schools and secondary schools, and the degree of competency in computer science fields among such students. .",
      "versionDate": "2025-12-10",
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
        "updateDate": "2025-12-12T16:31:14Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6591ih.xml"
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
      "title": "Computer Science for All Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T14:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Computer Science for All Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T14:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Education to carry out a program to increase access to prekindergarten through grade 12 computer science education.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T14:05:40Z"
    }
  ]
}
```
