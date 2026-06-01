# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5351?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5351
- Title: NSF AI Education Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5351
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2026-05-23T08:07:24Z
- Update date including text: 2026-05-23T08:07:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-09-15: Introduced in House

## Actions

- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5351",
    "number": "5351",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000480",
        "district": "20",
        "firstName": "Vince",
        "fullName": "Rep. Fong, Vince [R-CA-20]",
        "lastName": "Fong",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "NSF AI Education Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:24Z",
    "updateDateIncludingText": "2026-05-23T08:07:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
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
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:01:20Z",
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
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "OR"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CO"
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
      "sponsorshipDate": "2025-09-26",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NJ"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "FL"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "UT"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "GA"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "AK"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NV"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NM"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NE"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OK"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "IN"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "WI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NC"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-22",
      "state": "MI"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5351ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5351\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Mr. Fong (for himself, Ms. Salinas , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo support National Science Foundation education and professional development relating to artificial intelligence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NSF AI Education Act of 2025 .\n#### 2. Scholarships and fellowships in artificial intelligence\nParagraph (2) of section 540l(e) of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9451(e) ; enacted as part of title LIV of division E of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 )) is amended\u2014\n**(1)**\nin the heading, by striking Faculty ; and\n**(2)**\nby adding at the end the following new subparagraphs:\n(D) Student scholarships and fellowships in artificial intelligence (i) In general The Director of the National Science Foundation may support scholarships and fellowships for undergraduate and graduate students by making awards through institutions of higher education, including community colleges, to students who are enrolled in programs of study leading to degrees or concentrations in or related to the design, research, assessment, development, deployment, integration, or application of artificial intelligence. (ii) Considerations In carrying out clause (i), the Director of the National Science Foundation may prioritize making awards to students who are enrolled in programs of study leading to degrees or concentrations in or related to any of the following: (I) The teaching of artificial intelligence at elementary schools, secondary schools, career and technical education schools, institutions of higher education, or through other higher education and professional education programs. (II) Artificial intelligence and advanced manufacturing, including the integration of artificial intelligence into advanced manufacturing operations. (III) Artificial intelligence and agriculture, including the integration of artificial intelligence into agricultural operations, prediction, and decision making. (iii) Awards Scholarships and fellowships awarded under this subparagraph may be in the form of awards that may cover the cost of tuition, education-related fees, a stipend, and professional development funds for a period of up to five years. Such scholarships and fellowships shall be paid directly to the institution of higher education in which the student is enrolled. (iv) Outreach The Director of the National Science Foundation shall conduct outreach and encourage applications from rural-located institutions of higher education, rural-serving institutions of higher education, emerging research institutions, Tribal Colleges or Universities, and institutions located in an Established Program to Stimulate Competitive Research (EPSCoR) jurisdiction. (v) Method The Director of the National Science Foundation may carry out this subparagraph by making awards through new or existing programs. (E) Artificial intelligence professional development fellowships (i) In general The Director of the National Science Foundation may support activities to promote the exchange of ideas and encourage collaborations between institutions of higher education and industry partners in the field of artificial intelligence, including through fellowships for students, teachers, faculty, and industry professionals. (ii) Supplementals for students and faculty The Director of the National Science Foundation may award fellowships for students and faculty to pursue professional development programs in STEM fields that are administered by or affiliated with institutions of higher education, including community colleges, in order to enable recipients to attain skills, training, or education in partnership with industry members on the design, research, assessment, development, deployment, integration, or application of artificial intelligence. (iii) Fellowships for industry professionals The Director of the National Science Foundation may award fellowships to industry professionals to enable recipients to seek short-term appointments to instruct and educate students on the design, research, assessment, development, deployment, integration, or application of artificial intelligence. (iv) Fellowships for school professionals The Director of the National Science Foundation may award fellowships to teachers, school counselors, and other school professionals for professional development programs in order to enable recipients to attain skills, training, or education in partnership with industry members on the teaching, use of, or application of artificial intelligence in K\u201312 settings. (v) Awards Awards made under this subparagraph may be in the form of an award that covers the cost of tuition, education-related fees, a stipend, and professional development funds for up to one year. Such awards shall be paid directly to the institution of higher education that administers, or is affiliated with, the program in which the fellowship recipient is participating. (F) National Science Foundation outreach campaign The Director of the National Science Foundation may carry out a nationwide outreach campaign to industry as well as students at elementary schools, secondary schools, career and technical education schools, and institutions of higher education, or through other higher education and professional education programs, to increase awareness regarding National Science Foundation-funded artificial intelligence education opportunities. (G) Eligibility To be eligible to receive a scholarship or fellowship under this paragraph, an individual shall satisfy all of the following: (i) Be a citizen, national, or lawful permanent resident of the United States. (ii) Demonstrate a commitment to a career in advancing the field of artificial intelligence. (iii) Accept the terms of a fellowship under this subparagraph. (H) Reports (i) In general Not later than seven years after the date of the enactment of this subparagraph, the Director of the National Science Foundation shall submit to Congress, and make widely available to the public, a report including any recommendations for legislative action that could optimize the effectiveness of the scholarships and fellowships under this paragraph. (ii) Requirements In preparing the reports under clause (i), the Director of the National Science Foundation may, as practicable\u2014 (I) include an assessment of the effectiveness of such scholarships and fellowships in expanding apprenticeships, internships, and other applied or experiential learning opportunities offered by employers in conjunction with community colleges or other institutions of higher education; (II) assess the number of students who received such scholarships and fellowship; (III) assess the percentage of such students who successfully complete their education programs and who intend to enter the workforce; (IV) assess the percentage of undergraduate, graduate, and postdoctoral students who enter the workforce in a field relating to such scholarship or fellowship; (V) assess the impact on the number of K\u201312 teachers, school counselors, and other school professionals who received such scholarships or fellowships; and (VI) include an assessment of the effects such scholarships and fellowships have on related fields. .\n#### 3. Community college and area career and technical educational school centers of artificial intelligence excellence\n##### (a) In general\nSubparagraph (B) of section 5401 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9451(e)(3) ; enacted as part of title LIV of division E of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 )) is amended to read as follows:\n(B) Centers of AI excellence (i) Definitions In this subparagraph: (I) Area career and technical education school The term area career and technical education school has the meaning given such term in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ). (II) Eligible applicant The term eligible applicant means a community college, or area career and technical education school, in partnership with one or more of the following: (aa) A Federal, State, local, Tribal, or territorial government entity. (bb) An institution of higher education. (cc) An entity in private industry. (dd) An economic development organization or venture development organization. (ee) A nonprofit organization. (III) Venture development organization The term venture development organization has the meaning given such term in section 27(a) of the Stevenson-Wydler Technology Innovation Act of ( 15 U.S.C. 3722(a) ). (ii) Establishment of centers of AI excellence The Director of the National Science Foundation, in coordination with the Regional Technology Hubs program of the Department of Commerce, subject to the availability of appropriations, shall establish up to eight regionally and geographically diverse eligible applicants to be designated as Community College and Area Career and Technical Education Centers of AI Excellence (referred to in this subparagraph as Centers of AI Excellence ). Such Centers of AI Excellence shall enhance educational outcomes and drive workforce development by integrating artificial intelligence into teaching, learning, and community engagement. (iii) Application An eligible applicant seeking to be designated as a Center of AI Excellence under this subparagraph shall submit to the Director of the National Science Foundation an application at such time, in such manner, and containing such information as the Director may require. Such application shall include the following: (I) A description of the focus area or areas for such proposed Center of AI Excellence and how such area or areas are aligned with regional investments made by industry and the Federal Government. (II) A description of the capacity of the applicant to carry out the purpose of such proposed Center of AI Excellence. (III) A description of demonstrate current and anticipated future workforce demands in occupations directly related to such proposed Center of AI Excellence. (IV) A description of how the eligible applicant will support the collection of information and data for purposes of evaluation of such proposed Center of AI Excellence. (V) An evaluation plan that includes the use of outcome-oriented measures to assess the impact and efficacy of such proposed Center for AI Excellence. (iv) Activities A designated Center of AI Excellence shall develop and disseminate information regarding best practices for matters such as the following: (I) Artificial intelligence research and education, and research on the effects of artificial intelligence in education, at community colleges and area career and technical education schools. (II) Methods to scale up successful programs that perform research or provide education on artificial intelligence at community colleges and area career and technical education schools. (III) Providing educators and teachers with actionable strategies and resources to effectively integrate artificial intelligence into curriculums in the classroom. (IV) Providing experiential learning opportunities, including research and industry experiences on artificial intelligence and learning opportunities for students that are enabled through artificial intelligence. (V) Identifying pathways for students to jobs that are enabled by artificial intelligence, such as previously nonexistent jobs with respect to which artificial intelligence use is an integral part, jobs working directly on artificial intelligence, and previously existing jobs with respect to which needed skills have been significantly changed due to working with artificial intelligence. (VI) Facilitating partnerships with employers, employer consortia, or other private sector organizations that offer apprenticeships, internships, cooperative education, or applied learning experiences in the field of artificial intelligence. (v) Partnerships The Director of the National Science Foundation shall encourage applicants to consider including or partnering with a nonprofit organization, civil society organizations, industry, or an institution of higher education (or a consortium thereof) that has extensive experience and expertise in artificial intelligence. (vi) Evaluations All applications for designation under clause (ii) shall include an evaluation plan that includes the use of outcome-oriented measures to assess the impact and efficacy of the proposed Center for AI Excellence. (vii) Accountability and dissemination (I) Evaluation required The Director of the National Science Foundation shall evaluate the activities under clause (iv). Such evaluation, to the extent practicable, shall integrate the findings of research resulting from such activity or activities as a result of a designation under clause (ii) with the findings of other research on artificial intelligence education. (II) Report on evaluations Not later than 180 days after the completion of the evaluation under subclause (I), the Director of the National Science Foundation shall submit to Congress and make widely available to the public a report that includes the following: (aa) The results of such evaluation. (bb) Any recommendations for administrative and legislative action that could optimize the effectiveness of the designations made under clause (ii). .\n#### 4. Awards for research on artificial intelligence in education\n##### (a) In general\nSection 5401 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9451 ; enacted as part of title LIV of division E of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 )) is amended\u2014\n**(1)**\nby redesignating subsection (g) as subsection (i); and\n**(2)**\nby inserting after subsection (f) the following new subsections:\n(g) Awards for research on artificial intelligence in education (1) Eligible entity defined In this subsection, the term eligible entity means any of the following: (A) An institution of higher education. (B) A nonprofit organization. (C) A consortium of one or more institutions of higher education or nonprofit organizations and one or more private sector entities. (2) Awards (A) In general The Director of the National Science Foundation may make awards, on a competitive, merit-reviewed basis, to eligible entities, to enable such eligible entities to promote research regarding teaching models, tools, and materials for artificial intelligence, its integration into the classroom, teaching, and learning for pre-kindergarten through grade 12 students, and its impacts on educational and learning outcomes. (B) Method The Director of the National Science Foundation may carry out subparagraph (A) by making awards through new or existing programs. (3) Application (A) In general An eligible entity that desires to receive an award under this subsection shall submit to the Director of the National Science Foundation an application at such time, in such manner, and containing such information as the Director may require. (B) Contents An application under subparagraph (A) may include the following: (i) A description of any regional partnerships the eligible entity plans to utilize to carry out the award. (ii) With respect to an application that concerns the use or integration of artificial intelligence, a description of potential ethical concerns and implications of teacher, faculty, and student interactions with artificial intelligence. (iii) A description of how proposed research on teaching models, tools, and materials were developed in consultation with other educators, academia, industry, government entities, or civil society organizations. (iv) Such other information as the Director may require. (4) Use of award funds Awards described in paragraph (2)(A) shall be used by the recipient to carry out the following: (A) Emphasize preparing incoming K\u201312 teachers to integrate artificial intelligence into their classrooms in beneficial and innovative ways. (B) Support research to develop, pilot, fully implement, or test topics, such as the following: (i) Instructional materials and high-quality learning opportunities for teaching artificial intelligence. (ii) Models for the preparation of new teachers who will teach artificial intelligence. (iii) Scalable models of professional development and ongoing support for teachers. (iv) Tools and models for teaching and learning aimed at supporting student success. (v) Evaluations of the effect of different approaches to teaching artificial intelligence on students\u2019 educational and learning outcomes. (5) Partnerships In making awards under this subsection, the Director of the National Science Foundation shall carry out the following: (A) Encourage applicants which, for the purpose of the proposed activity or activities funded through such award, include or partner with a nonprofit organization or an institution of higher education (or a consortium thereof) that has extensive experience and expertise in integrating artificial intelligence into K\u201312 classrooms. (B) Encourage applicants which, for the purpose of such proposed activity or activities funded through such award, include or partner with a consortium of schools, institutions of higher education, school districts, non-profit organizations, or other State and local government entities. (C) Encourage applicants which, for the purpose of such proposed activity or activities funded through such award, include commitments from school principals, other school leaders, or administrators to make a priority reforms and activities proposed by the applicant. (h) Artificial intelligence collaborative (1) In general The Director of the National Science Foundation may establish a pilot program of regional cohorts that will provide peer support, mentoring, and hands-on research experiences for educators, principals, and other school leaders of students in kindergarten through grade 12, in order to build a network allowing educators, principals, other school leaders to carry out the following: (A) Engage with one another on educational efforts related to teaching and using artificial intelligence and evaluating its effects on students\u2019 educational and learning outcomes. (B) Interact with researchers, academia, and local industry involved in artificial intelligence. (2) Method The Director of the National Science Foundation may carry out this subsection by making awards through new or existing programs, including the pilot program authorized under section 10511(a)(2)(B) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19172 ; enacted as part of title V of division B of Public Law 117\u2013167 ). .",
      "versionDate": "2025-09-15",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-09-29T14:13:07Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-09-29T14:13:07Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-09-29T14:13:07Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-09-29T14:13:07Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-09-29T14:13:07Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-09-29T14:13:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-29T13:26:03Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5351ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NSF AI Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:23:13Z"
    },
    {
      "title": "NSF AI Education Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To support National Science Foundation education and professional development relating to artificial intelligence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:18:16Z"
    }
  ]
}
```
