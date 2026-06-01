# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6440?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6440
- Title: Right to Read Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6440
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-12T08:06:17Z
- Update date including text: 2026-05-12T08:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6440",
    "number": "6440",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "G000606",
        "district": "7",
        "firstName": "Adelita",
        "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
        "lastName": "Grijalva",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Right to Read Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-12T08:06:17Z",
    "updateDateIncludingText": "2026-05-12T08:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:05:15Z",
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
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OH"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OR"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WA"
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
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-16",
      "state": "WA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "HI"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CT"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "IL"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MN"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MA"
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
      "sponsorshipDate": "2026-01-13",
      "state": "DC"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "MI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "RI"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MD"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "PR"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "WA"
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "ME"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "VA"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "OR"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6440ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6440\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mrs. Grijalva (for herself, Mrs. Beatty , Ms. Bonamici , and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo ensure that students in schools have a right to read, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Right to Read Act of 2025 .\n#### 2. Definitions\nSection 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (19) through (28), paragraphs (29) through (43), paragraphs (44) through (49), and paragraphs (50) through (52) as paragraphs (20) through (29), paragraphs (31) through (45), paragraphs (47) through (52), and paragraphs (54) through (56), respectively;\n**(2)**\nby inserting after paragraph (18) the following:\n(19) Effective school library The term effective school library means a library that\u2014 (A) is staffed by supporting staff and at least one full-time State-certified school librarian who\u2014 (i) is an instructional leader, information specialist, and teacher; (ii) supports the digital learning environment and the development of participatory learning, inquiry learning, digital literacy, and information literacy; and (iii) supports, supplements, and elevates the literacy experience through guidance in reading for learning and motivational reading initiatives in order to enhance student achievement and foster lifelong reading and learning; (B) is otherwise adequately staffed to be open to students before, during, and after the school day; (C) has a sufficient collection of professionally curated up-to-date digital and print materials and technology, including openly licensed educational resources; (D) provides appropriate facilities for maintaining and providing equitable access to materials, technology, connectivity, and library and literacy instruction; (E) provides regular skills development or training for classroom teachers, school librarians, library paraprofessional staff, and other educators; (F) provides opportunities for collaboration between classroom teachers and school librarians; and (G) implements nationally recognized professional standards of practice. ;\n**(3)**\nby inserting after paragraph (29), as redesignated by paragraph (1), the following:\n(30) Information literacy The term information literacy means the set of skills needed to find, retrieve, understand, evaluate, analyze, and effectively use information (which encompasses spoken and broadcast words and videos, printed materials, and digital content, data, and images). ;\n**(4)**\nby inserting after paragraph (45), as redesignated by paragraph (1), the following:\n(46) Right to read The term right to read means all students have access to\u2014 (A) linguistically and developmentally appropriate, evidence-based reading instruction; (B) effective school libraries; (C) family literacy support; (D) culturally diverse and inclusive materials; (E) reading materials in the home; and (F) the freedom to choose reading materials. ; and\n**(5)**\nby inserting after paragraph (52), as redesignated by paragraph (1), the following:\n(53) Teacher The term teacher includes a school librarian. .\n#### 3. Amendments to title I\n##### (a) State plans\nSection 1111 of that Act ( 20 U.S.C. 6311 ) is amended\u2014\n**(1)**\nin subsection (a)(4)(A)(ii)(I)(aa), by inserting (including school librarians) after teachers ; and\n**(2)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby redesignating subparagraph (G) as subparagraph (H);\n**(ii)**\nin subparagraph (F), by striking and after the semicolon;\n**(iii)**\nby inserting after subparagraph (F) the following:\n(G) how the State will work to ensure that low-income students, minority students, students with disabilities, and English learners are not disproportionally enrolled in schools that lack an effective school library, and the measures the State educational agency will use to evaluate and publicly report the progress of the State educational agency with respect to ensuring such access to an effective school library; and ; and\n**(iv)**\nin subparagraph (H), as redesignated by clause (i), by inserting , including the development of digital literacy and information literacy skills after academic standards ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (J), by inserting (including school librarians) after teachers ;\n**(ii)**\nin subparagraph (M), by striking and after the semicolon;\n**(iii)**\nin subparagraph (N), by striking the period at the end and inserting ; and ; and\n**(iv)**\nby adding at the end the following:\n(O) the State educational agency has a policy regarding the right to read and will notify local educational agencies, Indian tribes and tribal organizations, schools, teachers, school librarians, principals, other school leaders, specialized support personnel, parents, and the public of such policy. .\n##### (b) Local educational agency plans\nSection 1112 of that Act ( 20 U.S.C. 6312 ) is amended\u2014\n**(1)**\nin subsection (a)(1)(A), by inserting (including school librarians) after teachers ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (12)(B), by striking and after the semicolon;\n**(B)**\nby striking paragraph (13); and\n**(C)**\nby adding at the end the following:\n(13) how the local educational agency will\u2014 (A) support and improve effective school libraries by supporting the work of State-certified school librarians to ensure that students have equitable access to such libraries; and (B) assist schools in developing effective school libraries to provide students an opportunity to develop digital literacy and information literacy skills and improve academic achievement; (14) the policies the local educational agency has in place to protect the right to read; and (15) any other information on how the local educational agency proposes to use funds to meet the purposes of this part, and that the local educational agency determines appropriate to provide, which may include a description of how the local educational agency will assist schools in identifying and serving gifted and talented students. .\n#### 4. Amendments to title II\n##### (a) Authorization of appropriations\nSection 2003 of that Act ( 20 U.S.C. 6603 ) is amended\u2014\n**(1)**\nin subsection (b), by inserting except for subpart 2, after part B, ; and\n**(2)**\nby adding at the end the following:\n(c) Literacy education for all, results for the nation There are authorized to be appropriated\u2014 (1) for grants authorized under section 2222, $500,000,000 for fiscal year 2026 and each of the succeeding 4 fiscal years; and (2) for grants authorized under section 2226, $100,000,000 for fiscal year 2026 and each of the succeeding 4 fiscal years. .\n##### (b) Formula grants to states\nSection 2101 of that Act ( 20 U.S.C. 6611 ) is amended\u2014\n**(1)**\nin subsection (c)(4)(B)\u2014\n**(A)**\nby redesignating clauses (xiv) through (xxi) as clauses (xvii) through (xxiv), respectively;\n**(B)**\nby striking clause (xiii) and inserting the following:\n(xiii) Supporting and improving effective school libraries that involve collaboration with State-certified school librarians. ; and\n**(C)**\nby inserting after clause (xiii) the following:\n(xiv) Developing, improving, and implementing mechanisms to assist local educational agencies and schools in effectively recruiting, hiring, and retaining State-certified school librarians. (xv) Providing training to school librarians, teachers, and school leaders on how to leverage effective school libraries for academic achievement, digital literacy, information literacy, and student and family engagement. (xvi) Providing training to library paraprofessional and other library staff to improve the effectiveness of school library programs. ; and\n**(2)**\nin subsection (d)(3)(A), by inserting (including school librarians) after teachers .\n##### (c) Local uses of funds\nSection 2103(b)(3) of that Act ( 20 U.S.C. 6613(b)(3) ) is amended by striking subparagraph (K) and inserting the following:\n(K) programs and activities to support and improve effective school libraries that involve collaboration with State-certified school librarians, such as efforts to promote and support digital literacy, information literacy, extended student inquiry, and capstone projects; .\n##### (d) Reservations\nSection 2201 of that Act ( 20 U.S.C. 6621 ) is amended\u2014\n**(1)**\nby striking paragraph (2); and\n**(2)**\nby redesignating paragraphs (3) and (4) as paragraphs (2) and (3), respectively.\n##### (e) Learn purposes and definitions\nSection 2221(b) of that Act ( 20 U.S.C. 6641(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (K), by striking and after the semicolon;\n**(B)**\nin subparagraph (L), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(M) provides opportunities for students to develop digital literacy and information literacy skills. ; and\n**(2)**\nin paragraph (2)(C), by inserting public libraries, or pediatric literacy programs after which may include early childhood education programs .\n##### (f) Comprehensive literacy state development grants\nSection 2222 of that Act ( 20 U.S.C. 6642 ) is amended\u2014\n**(1)**\nin subsection (a), by striking From the amounts reserved by the Secretary under section 2201(2) and not reserved under subsection (b), and inserting From amounts appropriated to carry out this section ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking reserved to carry out this subpart and inserting appropriated to carry out this section ; and\n**(B)**\nin paragraphs (2) and (3), by striking subpart and inserting section each place the term appears;\n**(3)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by striking and the State agency responsible for administering child care programs and inserting the State agency responsible for administering child care programs in the State, and the State library administrative agency ; and\n**(B)**\nin paragraph (2)(A), by inserting , diverse high quality print materials, and effective school libraries, after teachers of literacy ; and\n**(4)**\nin subsection (f)(2)\u2014\n**(A)**\nby redesignating subparagraphs (B) through (E) as subparagraphs (C) through (F), respectively; and\n**(B)**\nby inserting after subparagraph (A) the following:\n(B) Providing technical assistance to eligible entities in the development of effective school libraries, which may include establishing a statewide office to coordinate technical assistance for such libraries. .\n##### (g) Subgrants to eligible entities in support of birth through kindergarten entry literacy\nSection 2223(a)(1) of that Act ( 20 U.S.C. 6643(a)(1) ) is amended by inserting the State library administrative agency, before and, if applicable, .\n##### (h) Innovative approaches to literacy\nSection 2226(a) of that Act ( 20 U.S.C. 6646(a) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking From amounts reserved under section 2201(2) and inserting From amounts appropriated to carry out this section ;\n**(2)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively; and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) increasing the number of State-certified school librarians supporting students in high need schools; .\n##### (i) Technical amendments\n**(1)**\nSection 2231(a) of that Act ( 20 U.S.C. 6661(a) ) is amended, in the matter preceding paragraph (1) by striking section 2201(3) and inserting section 2201(2) .\n**(2)**\nSection 2241 of that Act ( 20 U.S.C. 6671 ) is amended, in the matter preceding paragraph (1), by striking section 2201(4) and inserting section 2201(3) .\n#### 5. Amendments to title iv\n##### (a) State use of funds\nSection 4104(b)(3)(A)(i) of that Act ( 20 U.S.C. 7114(b)(3)(A)(i) ) is amended\u2014\n**(1)**\nby redesignating subclauses (VI) and (VII) as subclauses (VII) and (VIII), respectively; and\n**(2)**\nby inserting after subclause (V) the following:\n(VI) digital literacy and information literacy activities and programs, including those provided through effective school libraries; .\n##### (b) Activities To support well-Rounded educational opportunities\nSection 4107(a)(3) of that Act ( 20 U.S.C. 7117(a)(3) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (I) and (J) as subparagraphs (J) and (K), respectively; and\n**(2)**\nby inserting after subparagraph (H) the following:\n(I) programs and activities the promote the development of digital literacy and information literacy skills, including those provided through an effective school library; .\n#### 6. Data collection and reporting on school libraries\n##### (a) Data collection\nThe Secretary of Education shall direct the National Center for Education Statistics to biennially collect data on elementary school and secondary school libraries.\n##### (b) Elements\nThe data collected biennially under subsection (a) shall include\u2014\n**(1)**\nthe number and percentage of elementary schools and secondary schools in each State that have dedicated school library facilities located on the grounds of the school and the square footage of each such library facility;\n**(2)**\nthe number and percentage of schools counted under paragraph (1) that employ at least one full-time State-certified school librarian; and\n**(3)**\nwith respect to each elementary and secondary school library\u2014\n**(A)**\nthe number of State-certified school librarians;\n**(B)**\nthe number of additional school library staff;\n**(C)**\nthe number and types of physical collections or assets;\n**(D)**\nthe number and types of virtual collections or databases the school library has access to;\n**(E)**\nthe number and types of student use devices managed by school library staff;\n**(F)**\nthe amount of time State-certified school librarians spend planning with teachers and instructing students;\n**(G)**\nthe amount of time State-certified school librarians spend planning with and providing professional development for teachers; and\n**(H)**\nother pertinent information that the Secretary of Education determines is important in order to support effective school libraries.\n##### (c) Report to congress\nNot later than one year after the date of enactment of this Act and every two years thereafter, the Secretary of Education shall submit to Congress a report that includes the data collected under this section.\n##### (d) ESEA terms\nIn this section, the terms elementary school and secondary school have the meanings given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section such sums as may be necessary for each fiscal year.\n#### 7. Liability protections related to the right to read\n##### (a) In general\nSection 8556 of that Act ( 20 U.S.C. 7946 ) is amended\u2014\n**(1)**\nby redesignating subsections (b) through (e) as subsections (c) through (f), respectively;\n**(2)**\nby inserting after subsection (a) the following:\n(b) Liability protections related to the right To read No teacher, school librarian, school leader, paraprofessional, or other staff shall be liable for harm caused by an act or omission of such person if the actions were carried out in conformity with State or local policies regarding the right to read. ;\n**(3)**\nin subsection (a), in the matter preceding paragraph (1), by striking subsection (b) and inserting subsection (c) ;\n**(4)**\nin subsection (c)(3), as redesignated by paragraph (1), by striking A State law that and inserting Except with respect to subsection (b), a State law that ; and\n**(5)**\nin subsection (f), as redesignated by paragraph (1)\u2014\n**(A)**\nin paragraph (1), by striking Nothing in this section and inserting Except with respect to subsection (b), nothing in this section ; and\n**(B)**\nin paragraph (2), by striking Nothing in this subpart and inserting Except with respect to subsection (b), nothing in this subpart .\n##### (b) Preemption and election of state nonapplicability\nSection 8555(b) of that Act ( 20 U.S.C. 7945(b) ) is amended by striking This subpart shall not apply and inserting Except for section 8556(b), this subpart shall not apply .\n#### 8. Protecting constitutional rights in school libraries\nSubpart 2 of part F of title VIII of that Act ( 20 U.S.C. 7901 et seq. ) is amended by adding at the end the following:\n8549D. Protecting constitutional rights in school libraries The Secretary shall require an assurance from each State and local educational agency receiving funds under this Act confirming that the State or local educational agency\u2014 (1) will protect the First Amendment rights of students in school libraries and will affirmatively further the right to receive information by\u2014 (A) providing access to a variety of reading materials; (B) recognizing that public schools prepare individuals for participation as citizens; (C) recognizing that school boards have important and discretionary functions; (D) acknowledging that among a school board\u2019s functions is a role to play in determining the holdings of a school library; (E) understanding the importance of First Amendment protections in school libraries as centers for voluntary inquiry and the dissemination of information and ideas; (F) understanding that school boards must exercise their discretionary authority in a manner that comports with First Amendment protections and imperatives; and (G) understanding that the exercise of a school board\u2019s role in determining the holdings of a school library may not be done in a manner that is partisan, political, or otherwise aimed at prescribing particular schools of thought or opinion; and (2) will provide equal protection in the conduct of school libraries in compliance with the requirements of the Fourteenth Amendment and nondiscrimination laws. .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S8513-8514)"
      },
      "number": "3365",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Right to Read Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-01-06T15:36:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-04",
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
          "measure-id": "id119hr6440",
          "measure-number": "6440",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-04",
          "originChamber": "HOUSE",
          "update-date": "2026-03-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6440v00",
            "update-date": "2026-03-05"
          },
          "action-date": "2025-12-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Right to Read Act of 2025</strong></p><p>This bill expands access to school libraries and literacy skills support for elementary and secondary school students. It also outlines certain constitutional rights and liability protections related to school libraries.</p><p>Specifically, the bill reauthorizes through FY2030 (1) the Comprehensive Literacy State Development Program, which provides grants to ensure high-quality instruction and effective strategies in reading and writing for children through 12th grade; and (2) the Innovative Approaches to Literacy Program, which provides grants to support the development of literacy skills in low-income communities.</p><p>Additionally, the bill allows Supporting Effective Instruction State Grants to be used to assist local educational agencies (LEAs) and schools in recruiting, hiring, and retaining state-certified school librarians.</p><p>Further, the bill authorizes states and LEAs to use Student Support and Academic Enrichment grants for programs and activities that promote the development of digital literacy and information literacy skills.</p><p>The Department of Education (ED) must direct the National Center for Education Statistics to biennially collect data on school libraries.</p><p>ED must require an assurance from each state and LEA receiving certain funds confirming that it will (1) protect the First Amendment rights of students in school libraries, and (2) provide equal protection in the conduct of school libraries in compliance with the requirements of the Fourteenth Amendment and nondiscrimination laws.</p><p>The bill also provides liability protection to teachers, school librarians, school leaders, paraprofessionals, and other staff for actions that conform with state or local policies regarding the right to read.</p>"
        },
        "title": "Right to Read Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6440.xml",
    "summary": {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Right to Read Act of 2025</strong></p><p>This bill expands access to school libraries and literacy skills support for elementary and secondary school students. It also outlines certain constitutional rights and liability protections related to school libraries.</p><p>Specifically, the bill reauthorizes through FY2030 (1) the Comprehensive Literacy State Development Program, which provides grants to ensure high-quality instruction and effective strategies in reading and writing for children through 12th grade; and (2) the Innovative Approaches to Literacy Program, which provides grants to support the development of literacy skills in low-income communities.</p><p>Additionally, the bill allows Supporting Effective Instruction State Grants to be used to assist local educational agencies (LEAs) and schools in recruiting, hiring, and retaining state-certified school librarians.</p><p>Further, the bill authorizes states and LEAs to use Student Support and Academic Enrichment grants for programs and activities that promote the development of digital literacy and information literacy skills.</p><p>The Department of Education (ED) must direct the National Center for Education Statistics to biennially collect data on school libraries.</p><p>ED must require an assurance from each state and LEA receiving certain funds confirming that it will (1) protect the First Amendment rights of students in school libraries, and (2) provide equal protection in the conduct of school libraries in compliance with the requirements of the Fourteenth Amendment and nondiscrimination laws.</p><p>The bill also provides liability protection to teachers, school librarians, school leaders, paraprofessionals, and other staff for actions that conform with state or local policies regarding the right to read.</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119hr6440"
    },
    "title": "Right to Read Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Right to Read Act of 2025</strong></p><p>This bill expands access to school libraries and literacy skills support for elementary and secondary school students. It also outlines certain constitutional rights and liability protections related to school libraries.</p><p>Specifically, the bill reauthorizes through FY2030 (1) the Comprehensive Literacy State Development Program, which provides grants to ensure high-quality instruction and effective strategies in reading and writing for children through 12th grade; and (2) the Innovative Approaches to Literacy Program, which provides grants to support the development of literacy skills in low-income communities.</p><p>Additionally, the bill allows Supporting Effective Instruction State Grants to be used to assist local educational agencies (LEAs) and schools in recruiting, hiring, and retaining state-certified school librarians.</p><p>Further, the bill authorizes states and LEAs to use Student Support and Academic Enrichment grants for programs and activities that promote the development of digital literacy and information literacy skills.</p><p>The Department of Education (ED) must direct the National Center for Education Statistics to biennially collect data on school libraries.</p><p>ED must require an assurance from each state and LEA receiving certain funds confirming that it will (1) protect the First Amendment rights of students in school libraries, and (2) provide equal protection in the conduct of school libraries in compliance with the requirements of the Fourteenth Amendment and nondiscrimination laws.</p><p>The bill also provides liability protection to teachers, school librarians, school leaders, paraprofessionals, and other staff for actions that conform with state or local policies regarding the right to read.</p>",
      "updateDate": "2026-03-05",
      "versionCode": "id119hr6440"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6440ih.xml"
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
      "title": "Right to Read Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T11:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Right to Read Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that students in schools have a right to read, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T11:18:27Z"
    }
  ]
}
```
