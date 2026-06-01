# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2485?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2485
- Title: Arts Education for All Act
- Congress: 119
- Bill type: HR
- Bill number: 2485
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-05-21T08:08:07Z
- Update date including text: 2026-05-21T08:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2485",
    "number": "2485",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Arts Education for All Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:07Z",
    "updateDateIncludingText": "2026-05-21T08:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:07:50Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NE"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "ME"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "DC"
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
      "sponsorshipDate": "2025-03-31",
      "state": "GA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-31",
      "state": "NM"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "OR"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
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
      "sponsorshipDate": "2025-06-03",
      "state": "NC"
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
      "sponsorshipDate": "2025-06-04",
      "state": "NC"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NC"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NV"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "IL"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "GA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NY"
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
      "sponsorshipDate": "2025-06-12",
      "state": "WA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CT"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "OR"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MN"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "OH"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NY"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "AZ"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "AZ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NJ"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "OR"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CT"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "IL"
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
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2485ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2485\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Ms. Bonamici (for herself, Mr. Bacon , Ms. Pingree , Ms. Leger Fernandez , Ms. Norton , Mr. Johnson of Georgia , Ms. Randall , Ms. Stansbury , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo expand arts education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Arts Education for All Act .\nI\nEarly Childhood Education Programs\n#### 101. Early childhood education programs\nThe Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ) is amended\u2014\n**(1)**\nin section 658G(b)(1), by striking subparagraph (A) and inserting the following:\n(A) offering training, coaching, or professional development opportunities for child care providers that relate to the use of evidence-based, developmentally appropriate and age-appropriate strategies to promote the social, emotional, physical, adaptive, communication, and cognitive development of children, including key programmatic strategies, and offering specialized training for child care providers caring for those populations prioritized in section 658E(c)(2)(Q), and children with disabilities; ; and\n**(2)**\nin section 658P, by adding at the end the following:\n(16) Key programmatic strategies The term key programmatic strategies means strategies related to\u2014 (A) nutrition and physical activity; (B) recommended practices for age-appropriate exposure to screen media; and (C) the integration and utilization of instructional methods to assist learning across disciplines, including methods that use the arts, language, literacy, mathematics, science, and social studies. .\nII\nAmendments to the Elementary and Secondary Education Act of 1965\n#### 201. References\nExcept as otherwise expressly provided, whenever in this title an amendment or repeal is expressed in terms of an amendment to, or repeal of, a section or other provision, the reference shall be considered to be made to a section or other provision of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6301 et seq. ).\n#### 202. State and local plans\n##### (a)\nSection 1111(g) ( 20 U.S.C. 6311(g) ) is amended by adding at the end the following:\n(5) Use of arts education to improve student achievement Each State\u2019s plan shall describe how the State educational agency will\u2014 (A) support and encourage the offering of a variety of arts education experiences to students as part of the State educational agency\u2019s overall strategy to improve student achievement in the subjects described in section 8101(52); (B) integrate arts education instruction into the curriculum; (C) increase the number of arts educators, including arts education specialists, in schools; (D) utilize partnerships with specialized teaching artists to train teachers to augment creative thinking techniques into the instruction provided in math, reading, English language arts, science, and other subjects described in section 8101(52); (E) ensure that arts instruction provided in the State is standards-based, as applicable, and sequential with arts courses offered in the grades 6 through 12 building upon such courses offered in earlier grades; (F) increase the number of classes taught by arts educators, including arts education specialists, with a particular focus on classes with high percentages of students who are low-income, students with disabilities, English learners, or students of color; and (G) support partnerships that increase the amount of arts education and creative youth development available in afterschool and summer learning programs. .\n##### (b)\nSection 1112(b) ( 20 U.S.C. 6312(b) ) is amended\u2014\n**(1)**\nin paragraph (12), by striking and at the end;\n**(2)**\nby redesignating paragraph (13) as paragraph (14); and\n**(3)**\nby inserting after paragraph (12) the following:\n(13) how the local educational agency will support learning in the arts and encourage the use of the arts education to improve student achievement consistent with section 1111(g)(5); and .\n#### 203. Report cards\nSection 1111(h)(1)(C) ( 20 U.S.C. 6311(h)(1)(C) ) is amended\u2014\n**(1)**\nby redesignating clause (xiv) as (xv); and\n**(2)**\nby inserting after clause (xiii) the following:\n(xiv) Information on arts courses, including\u2014 (I) the number of, range, and sequence of course offerings; (II) the average pupil-to-teacher ratio in such courses; (III) the average amount of instructional time in such courses; and (IV) for each semester, the percentage (in the aggregate and dis\u00adag\u00adgre\u00adgated by high-poverty compared to low-poverty schools, which for the purpose of this subclause, means schools in the top quartile of poverty and the bottom quartile of poverty in the State) of\u2014 (aa) schools offering arts courses; (bb) students taking arts courses; and (cc) arts courses taught by arts teachers with full State certification or licensure. .\n#### 204. School improvement\nSection 1111(d)(2)(B) ( 20 U.S.C. 6311(d)(2)(B) ) is amended\u2014\n**(1)**\nin clause (iv), by striking ; and and inserting a semicolon;\n**(2)**\nby redesignating clause (v) as clause (vi); and\n**(3)**\nby inserting after clause (iv) the following:\n(v) (I) provides for an evaluation of the arts courses offered at such school during the school day and the certification, training and skills of staff that are teaching such courses including teaching artists; and (II) based on such evaluation, incorporate the offering of arts courses into the offerings of such school; and .\n#### 205. Arts for neglected and delinquent children and youth\nSection 1415(a)(2)(B)(ii) ( 20 U.S.C. 6435(a)(2)(B)(ii) ) is amended by inserting access to the arts and arts education and after improving .\n#### 206. Subgrants to local educational agencies\n##### (a) Local uses of funds\nSection 2103(b)(3) ( 20 U.S.C. 6613(b)(3) ) is amended\u2014\n**(1)**\nin subparagraph (O), by striking ; and and inserting a semicolon;\n**(2)**\nby redesignating subparagraph (P) as subparagraph (Q); and\n**(3)**\nby inserting after subparagraph (O) the following:\n(P) carrying out activities to increase pathways to obtain rigorous, high-quality teacher certification or licensure for individuals seeking to become teachers of the arts; and .\n##### (b) Professional development for arts teachers\nSection 2103 ( 20 U.S.C. 6613 ) is further amended by inserting at the end the following:\n(c) Professional development for arts teachers In carrying out the programs and activities described under subsection (a), a local educational agency shall provide professional development for teachers of the arts, as appropriate, to fulfill the needs of such agency and the schools of such agency. (d) Professional development for integration of the arts In carrying out the programs and activities described under subsection (a), a local educational agency shall provide professional development for teachers to integrate the arts into their instruction in math, reading, English language arts, science, and other subjects described in section 8101(52). .\n#### 207. 21st century community learning centers\n##### (a) Arts organizations\nSection 4205(a) ( 20 U.S.C. 7175(a) ) is amended\u2014\n**(1)**\nin paragraph (13), by striking ; and ;\n**(2)**\nin paragraph (14), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(15) partnering with, integrating the services of, and utilizing the services and offerings provided by arts services organizations or other community-focused arts nonprofits and organizations that further creative youth development. .\n##### (b) Professional development\nSection 4203(a)(6) ( 20 U.S.C. 7173(a)(6) ) is amended by inserting , including arts education after areas .\nIII\nAmendments to the Juvenile Justice and Delinquency Prevention Act of 1974 and to the Omnibus Crime Control and Safe Streets Act of 1968\n#### 301. Amendments to the Juvenile Justice and Delinquency Prevention Act of 1974\nSection 223(a) of the Juvenile Justice and Delinquency Prevention Act of 1974 ( 42 U.S.C. 5633(a) ) is amended\u2014\n**(1)**\nin paragraph (32) by striking and at the end,\n**(2)**\nin paragraph (33) by striking the period at the end and inserting ; and , and\n**(3)**\nby adding at the end the following:\n(34) describe how the State will coordinate services, activities for juvenile justice and delinquency prevention with State and local agencies and organizations, including State and local arts agencies, arts organizations, and organizations that further creative youth development. .\n#### 302. Amendments to adult and juvenile offender demonstration projects and the State, tribal and local reentry courts programs\nThe Omnibus Crime Control and Safe Streets Act of 1968 is amended in section 2976(b)(4)\u2014\n**(1)**\nby striking ; and in subparagraph (A);\n**(2)**\nafter subparagraph (A), by inserting the following:\n(B) use arts education programs and services to better facilitate reentry and reduce recidivism and connect offenders to educational opportunities and employment after reentry into the community; and ; and\n**(3)**\nby redesignating subparagraph (B) as subparagraph (C).\nIV\nAmendments to the Education Sciences Reform Act of 2002 and the National Assessment of Educational Progress Authorization Act\n#### 401. Arts research\nSection 133 of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9533 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking ; and at the end of subparagraph (10)(D);\n**(B)**\nby redesignating subparagraph (11) as subparagraph (12); and\n**(C)**\nby inserting after paragraph (10) the following:\n(11) carry out research on the use of the arts and arts education that is rigorous, peer reviewed and large scale to determine which methods and uses of the arts and arts education are most effective, cost efficient and able to be applied, duplicated, and scaled up for the use in elementary and secondary classrooms, including in low-performing schools; and ; and\n**(2)**\nin subsection (c)(2), by adding at the end the following:\n(L) Use of the arts and arts education in improving elementary and secondary education. .\n#### 402. Arts statistical data\nSection 153(a)(1) of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9543(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (N), by striking ; and and inserting a semicolon;\n**(2)**\nby redesignating subparagraph (O) as subparagraph (P); and\n**(3)**\nby inserting after subparagraph (N), the following:\n(O) access to, the integration of and the inclusion of arts education; and .\n#### 403. National assessment of educational progress\nSection 303(b) of the National Assessment of Educational Progress Authorization Act ( 20 U.S.C. 9622(b) ) is amended by adding at the end the following:\n(7) Arts assessment The Assessment Board shall select the arts as a subject to be assessed under this subsection, at the same frequency and in the same grades (at a minimum) as such assessment was scheduled prior to July 24, 2021. .",
      "versionDate": "2025-03-31",
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
            "name": "Art, artists, authorship",
            "updateDate": "2026-03-20T14:42:47Z"
          },
          {
            "name": "Child care and development",
            "updateDate": "2026-03-20T14:42:39Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2026-03-20T14:43:02Z"
          },
          {
            "name": "Education of the disadvantaged",
            "updateDate": "2026-03-20T14:42:57Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2026-03-20T14:42:52Z"
          },
          {
            "name": "Educational guidance",
            "updateDate": "2026-03-20T14:43:06Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-03-20T14:42:32Z"
          },
          {
            "name": "Juvenile crime and gang violence",
            "updateDate": "2026-03-20T14:43:11Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-03-20T14:42:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-04-07T13:20:19Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2485ih.xml"
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
      "title": "Arts Education for All Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Arts Education for All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand arts education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:50Z"
    }
  ]
}
```
