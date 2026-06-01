# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2892?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2892
- Title: Jumpstart on College Act
- Congress: 119
- Bill type: S
- Bill number: 2892
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-12-05T21:43:49Z
- Update date including text: 2025-12-05T21:43:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2892",
    "number": "2892",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Jumpstart on College Act",
    "type": "S",
    "updateDate": "2025-12-05T21:43:49Z",
    "updateDateIncludingText": "2025-12-05T21:43:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T20:32:45Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2892is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2892\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Markey (for himself and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo direct the Secretary of Education to make grants to support early college high schools and dual or concurrent enrollment programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Jumpstart on College Act .\n#### 2. Purpose\nThe purpose of this Act is to increase the percentage of students who complete a recognized postsecondary credential within 100 percent of the normal time for the completion of such credential, including low-income students and students from other populations that are underrepresented in higher education.\n#### 3. Definitions\nIn this Act:\n**(1) ESEA terms**\nThe terms dual or concurrent enrollment program , early college high school , educational service agency , four-year adjusted cohort graduation rate , local educational agency , secondary school , and State have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Eligible entity**\nThe term eligible entity means an institution of higher education in partnership with one or more local educational agencies (which may be an educational service agency). Such partnership may also include other entities, such as nonprofit organizations or businesses and schools in juvenile detention centers.\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(4) Low-income student**\nThe term low-income student means a student counted under section 1124(c) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6333(c) ).\n**(5) Recognized postsecondary credential**\nThe term recognized postsecondary credential has the meaning given the term in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n**(6) Secretary**\nThe term Secretary means the Secretary of Education.\n#### 4. Authorization of appropriations; reservations\n##### (a) In general\nTo carry out this Act, there are authorized to be appropriated $250,000,000 for fiscal year 2026 and each of the 5 succeeding fiscal years.\n##### (b) Reservations\nFrom the funds appropriated under subsection (a) for each fiscal year, the Secretary shall reserve\u2014\n**(1)**\nnot less than 40 percent for grants to eligible entities under section 5;\n**(2)**\nnot less than 55 percent for grants to States under section 6; and\n**(3)**\nnot less than 5 percent for national activities under section 8.\n#### 5. Grants to eligible entities\n##### (a) In general\nThe Secretary shall award grants to eligible entities, on a competitive basis, to assist such entities in establishing or supporting an early college high school or dual or concurrent enrollment program in accordance with this section.\n##### (b) Duration\nEach grant under this section shall be awarded for a period of 6 years.\n##### (c) Grant amount\nThe Secretary shall ensure that the amount of each grant under this section is sufficient to enable each grantee to carry out the activities described in subsection (h), except that a grant under this section may not exceed $2,000,000, of which not more than 15 percent of the overall grant total may be used to improve data systems for the purpose of facilitating the execution of the reporting requirement in section 7(a).\n##### (d) Matching requirement\n**(1) In general**\nFor each year that an eligible entity receives a grant under this section, the entity shall contribute matching funds, in the amounts described in paragraph (2), for the activities supported by the grant.\n**(2) Amounts described**\nThe amounts described in this paragraph are\u2014\n**(A)**\nfor each of the first and second years of the grant period, 20 percent of the grant amount;\n**(B)**\nfor each of the third and fourth years of the grant period, 30 percent of the grant amount;\n**(C)**\nfor the fifth year of the grant period, 40 percent of the grant amount; and\n**(D)**\nfor the sixth year of the grant period, 50 percent of the grant amount.\n**(3) Determination of amount contributed**\n**(A) In-kind contributions**\nThe Secretary shall allow an eligible entity to meet the requirements of this subsection through in-kind contributions.\n**(B) Non-Federal sources**\nNot less than half of each amount described in paragraph (2) shall be provided by the eligible entity from non-Federal sources.\n##### (e) Supplement, not supplant\nAn eligible entity shall use a grant received under this section only to supplement funds that would, in the absence of such a grant, be made available from other Federal, State, or local sources for activities supported by the grant, and not to supplant such funds.\n##### (f) Priority\nIn awarding grants under this section, the Secretary shall give priority to eligible entities that\u2014\n**(1)**\npropose to establish or support an early college high school or dual or concurrent enrollment program that will serve a student population of which not less than 51 percent are low-income students;\n**(2)**\ninclude a local educational agency that serves a high school that is\u2014\n**(A)**\nidentified for comprehensive support and improvement under section 1111(c)(4)(D)(i) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(c)(4)(D)(i) ); or\n**(B)**\nimplementing a targeted support and improvement plan as described in section 1111(d)(2) of such Act ( 20 U.S.C. 6311(d)(2) );\n**(3)**\nare from States that provide assistance to early college high schools or dual or concurrent enrollment programs, such as assistance to defray the costs of higher education (including costs of tuition, fees, and textbooks); and\n**(4)**\npropose to establish or support an early college high school or dual or concurrent enrollment program that meets quality standards established by\u2014\n**(A)**\na nationally recognized accrediting agency or association that offers accreditation specifically for such programs; or\n**(B)**\na State process specifically for the review and approval of such programs.\n##### (g) Equitable distribution\nThe Secretary shall ensure, to the extent practicable, that eligible entities receiving grants under this section\u2014\n**(1)**\nare from a representative cross-section of\u2014\n**(A)**\nurban, suburban, and rural areas; and\n**(B)**\nregions of the United States; and\n**(2)**\ninclude both 2-year and 4-year institutions of higher education.\n##### (h) Uses of funds\n**(1) Mandatory activities**\n**(A) In general**\nAn eligible entity shall use grant funds received under this section\u2014\n**(i)**\nto support the activities described in its application under subsection (i);\n**(ii)**\nto create and maintain a coherent system of supports for students, teachers, principals, and faculty under the program, including\u2014\n**(I)**\ncollege and career readiness, academic, and social support services for students; and\n**(II)**\nprofessional development for secondary school teachers, faculty, and principals, and faculty from the institution of higher education, including\u2014\n**(aa)**\njoint professional development activities; and\n**(bb)**\nactivities to assist such teachers, faculty, and principals in using effective parent and community engagement strategies and to help ensure the success of students academically at risk of not enrolling in or completing postsecondary education, first-generation college students, and each category of students described in section 1111(b)(2)(B)(xi) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(b)(2)(B)(xi) );\n**(iii)**\nto carry out liaison activities among the partners that comprise the eligible entity pursuant to an agreement or memorandum of understanding documenting commitments, resources, roles, and responsibilities of the partners consistent with the design of the program;\n**(iv)**\nfor outreach programs to ensure that secondary school students and their families, including students academically at risk of not enrolling in or completing postsecondary education, first-generation college students, and each category of students described in section 1111(b)(2)(B)(xi) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(b)(2)(B)(xi) ), are\u2014\n**(I)**\naware of, and recruited into, the early college high school or dual or concurrent enrollment program; and\n**(II)**\nassisted with the process of enrolling and succeeding in the early college high school or dual or concurrent enrollment program, which may include providing academic support;\n**(v)**\nto collect, share, and use data (in compliance with section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g )) for program improvement and program evaluation; and\n**(vi)**\nto review and strengthen its program to maximize the potential that students participating in the program will eventually complete a recognized postsecondary credential, including by optimizing\u2014\n**(I)**\nthe curriculum of the program;\n**(II)**\nthe use of high-quality assessments of student learning, such as performance-based, project-based, or portfolio assessments that measure higher-order thinking skills;\n**(III)**\nthe sequence of courses offered by the program; and\n**(IV)**\nthe alignment of academic calendars between the secondary schools and the institution of higher education participating in the program.\n**(B) New programs**\nIn the case of an eligible entity that uses a grant under this section to establish an early college high school or dual or concurrent enrollment program, the entity shall use such funds during the first year of the grant period\u2014\n**(i)**\nto design the curriculum and sequence of courses in collaboration with, at a minimum\u2014\n**(I)**\nfaculty from the institution of higher education;\n**(II)**\nteachers and faculty from the local educational agency; and\n**(III)**\nin the case of a career and technical education program, employers or workforce development entities to ensure that the program is aligned with labor market demand;\n**(ii)**\nto develop and implement an articulation agreement between the institution of higher education and the local educational agency that governs how secondary and postsecondary credits will be awarded under the program; and\n**(iii)**\nto carry out the activities described in subparagraph (A).\n**(2) Allowable activities**\nAn eligible entity may use grant funds received under this section to support the activities described in its application under subsection (i), including by\u2014\n**(A)**\npurchasing textbooks and equipment that support the program\u2019s curriculum;\n**(B)**\npursuant to the assurance provided by the eligible entity under subsection (i)(3)(A), paying tuition and fees for postsecondary courses taken by students under the program;\n**(C)**\nincorporating work-based learning opportunities (other than by paying wages of students) into the program (which may include partnering with entities that provide such opportunities), including\u2014\n**(i)**\ninternships;\n**(ii)**\ncareer-based capstone projects;\n**(iii)**\npre-apprenticeships and registered apprenticeships provided by eligible providers of apprenticeship programs described in section 122(a)(2)(B) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3152(a)(2)(B) ); and\n**(iv)**\nwork-based learning opportunities provided under chapters 1 and 2 of subpart 2 of part A of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070a\u201311 et seq. );\n**(D)**\nproviding students with transportation to and from the program;\n**(E)**\npaying costs for\u2014\n**(i)**\nhigh school teachers to obtain the skills, credentials, or industry certifications necessary to teach for the institution of higher education participating in the program; or\n**(ii)**\npostsecondary faculty to become certified to teach high school; or\n**(F)**\nproviding time during which secondary school teachers and faculty and faculty from an institution of higher education can collaborate, which may include\u2014\n**(i)**\nprofessional development;\n**(ii)**\nthe planning of team activities for such teachers and faculty; and\n**(iii)**\ncurricular design and student assessment.\n##### (i) Application\n**(1) In general**\nTo be eligible to receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Contents of application**\nThe application under paragraph (1) shall include, at minimum, a description of\u2014\n**(A)**\nthe partnership that comprises the eligible entity, including documentation of partner commitments, resources and budget, roles, and responsibilities;\n**(B)**\nhow the partners that comprise the eligible entity will coordinate to carry out the mandatory activities described in subsection (h)(1);\n**(C)**\nthe number of students intended to be served by the program and demographic information relating to such students;\n**(D)**\nhow the eligible entity\u2019s curriculum and sequence of courses form a program of study leading to a recognized postsecondary credential;\n**(E)**\nhow postsecondary credits earned will be transferable to institutions of higher education within the State, including any applicable statewide transfer agreements and any provisions of such agreements that are specific to dual or concurrent enrollment programs;\n**(F)**\nhow the eligible entity will conduct outreach to students;\n**(G)**\nhow the eligible entity will determine the eligibility of students for postsecondary courses, including an explanation of the multiple factors the entity will take into account to assess the readiness of students for such courses; and\n**(H)**\nthe sustainability plan for the early college high school or dual or concurrent enrollment program.\n**(3) Assurances**\nThe application under paragraph (1) shall include assurances from the eligible entity that\u2014\n**(A)**\nstudents participating in a program funded with a grant under this section will not be required to pay tuition or fees for postsecondary courses taken under the program;\n**(B)**\npostsecondary credits earned by students under the program will be transcribed upon completion of the required course work; and\n**(C)**\ninstructors of postsecondary courses under the program will meet the same standards applicable to other faculty at the institution of higher education that is participating in the program.\n#### 6. Grants to States\n##### (a) In general\nThe Secretary shall award grants to States, on a competitive basis, to assist States in supporting or establishing early college high schools or dual or concurrent enrollment programs.\n##### (b) Duration\nEach grant under this section shall be awarded for a period of 6 years.\n##### (c) Grant amount\nThe Secretary shall ensure that the amount of each grant under this section is sufficient to enable each grantee to carry out the activities described in subsection (f), of which not more than 15 percent of the overall grant total may be used to improve data systems for the purpose of facilitating the execution of the reporting requirement in section 7(a).\n##### (d) Matching requirement\nFor each year that a State receives a grant under this section, the State shall provide, from non-Federal sources, an amount equal to 50 percent of the amount of the grant received by the State for such year to carry out the activities supported by the grant.\n##### (e) Supplement, not supplant\nA State shall use a grant received under this section only to supplement funds that would, in the absence of such grant, be made available from other Federal, State, or local sources for activities supported by the grant, and not to supplant such funds.\n##### (f) Uses of funds\n**(1) Mandatory activities**\nA State shall use grant funds received under this section to\u2014\n**(A)**\nsupport the activities described in its application under subsection (g);\n**(B)**\nplan and implement a statewide strategy for expanding access to early college high schools and dual or concurrent enrollment programs for students who are underrepresented in higher education to raise statewide rates of secondary school graduation, readiness for postsecondary education, and completion of recognized postsecondary credentials, with a focus on students academically at risk of not enrolling in or completing postsecondary education;\n**(C)**\nidentify any obstacles to such a strategy under State law or policy;\n**(D)**\nprovide technical assistance (either directly or through a knowledgeable intermediary) to early college high schools and dual or concurrent enrollment programs, which may include\u2014\n**(i)**\nbrokering relationships and agreements that forge a strong partnership between elementary and secondary and postsecondary partners; and\n**(ii)**\noffering statewide training, professional development, and peer learning opportunities for school leaders, instructors, and counselors or advisors;\n**(E)**\nidentify and implement policies that will improve the effectiveness and ensure the quality of early college high schools and dual or concurrent enrollment programs, such as eligibility and access, funding, data and quality assurance, governance, accountability, and alignment policies;\n**(F)**\nupdate the State\u2019s requirements for a student to receive a regular high school diploma to align with the challenging State academic standards and entrance requirements for credit-bearing coursework as described in subparagraphs (A) and (D) of section 1111(b)(1) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(b)(1) );\n**(G)**\nincorporate indicators regarding student access to and completion of early college high schools and dual or concurrent enrollment programs into the school quality and student success indicators included in the State system of annual meaningful differentiation as described under section 1111(c)(4)(B)(v)(I) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(c)(4)(B)(v)(I) );\n**(H)**\ndisseminate best practices for early college high schools and dual or concurrent enrollment programs, which may include best practices from programs in the State or other States;\n**(I)**\nfacilitate statewide secondary and postsecondary data collection, research and evaluation, and reporting to policymakers and other stakeholders, disaggregated for each category of students described in section 1111(b)(2)(B)(xi) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(b)(2)(B)(xi) ); and\n**(J)**\nconduct outreach programs to ensure that secondary school students, their families, and community members are made aware of early college high schools and dual or concurrent enrollment programs in the State through a new or existing State online website that complies with the web accessibility requirements under Federal and State laws that protect individuals with disabilities.\n**(2) Allowable activities**\nA State may use grant funds received under this section to\u2014\n**(A)**\nestablish a mechanism to offset the costs of tuition, fees, standardized testing, performance assessments, and support services for low-income students and students from underrepresented populations enrolled in early college high schools or dual or concurrent enrollment programs;\n**(B)**\nestablish formal transfer systems within and across State higher education systems, including 2-year and 4-year public and private institutions to maximize the transferability of postsecondary courses;\n**(C)**\nprovide incentives to local educational agencies that\u2014\n**(i)**\nassist high school teachers in getting the credentials needed to participate in early college high school and dual or concurrent enrollment programs;\n**(ii)**\nencourage the use of instructors at institutions of higher education to teach higher education courses in high schools; and\n**(iii)**\nparticipate in an annual assessment of current availability and shortages of high school instructors who are credentialed to teach a dual or concurrent enrollment course, and shortages of these instructors in specific curricular areas; and\n**(D)**\nsupport initiatives to improve the quality of early college high school and dual or concurrent enrollment programs at participating institutions, including by assisting such institutions in aligning programs with the quality standards described in section 5(f)(4).\n##### (g) State applications\n**(1) Application**\nTo be eligible to receive a grant under this section, a State shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Contents of application**\nThe application under paragraph (1) shall include, at minimum, a description of\u2014\n**(A)**\nhow the State will carry out the mandatory State activities described in subsection (f)(1);\n**(B)**\nhow the State will ensure that any programs funded with a grant under this section are coordinated with programs under\u2014\n**(i)**\nthe Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. );\n**(ii)**\nthe Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. );\n**(iii)**\nthe Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6301 et seq. ); and\n**(iv)**\nthe Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. );\n**(C)**\nhow the State intends to use grant funds to address achievement gaps for each category of students described in section 1111(b)(2)(B)(xi) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(b)(2)(B)(xi) );\n**(D)**\nhow the State will access and leverage additional resources necessary to sustain early college high schools and dual or concurrent enrollment programs;\n**(E)**\nhow the State will identify and eliminate barriers to implementing effective early college high schools and dual or concurrent enrollment programs after the grant expires, including by engaging businesses and nonprofit organizations; and\n**(F)**\nsuch other information as the Secretary determines to be appropriate.\n#### 7. Reporting and oversight\n##### (a) In general\nNot less frequently than once annually, each State and eligible entity that receives a grant under this Act shall submit to the Secretary a report on the progress of the State or eligible entity in carrying out the programs supported by such grant.\n##### (b) Form of report\nThe report under subsection (a) shall be submitted to the Secretary at such time, in such manner, and containing such information as the Secretary may require. The Secretary shall issue uniform guidelines describing the information that shall be reported by grantees under such subsection.\n##### (c) Contents of report\n**(1) In general**\nThe report under subsection (a) shall include, at minimum, the following:\n**(A)**\nThe number of students enrolled in the early college high school or dual or concurrent enrollment program.\n**(B)**\nThe number and percentage of students enrolled in the early college high school or dual or concurrent enrollment program who earn a recognized postsecondary credential concurrently with a high school diploma.\n**(C)**\nThe number of postsecondary credits earned by students while enrolled in the early college high school or dual or concurrent enrollment program that may be applied toward a recognized postsecondary credential.\n**(D)**\nThe number and percentage of students enrolled in the early college high school or dual or concurrent enrollment program who earn a high school diploma.\n**(E)**\nThe number and percentage of individuals who complete the early college high school or dual or concurrent enrollment program and who enroll in postsecondary education.\n**(2) Categories of students**\nThe information described in each of subparagraphs (A) through (E) of paragraph (1) shall be disaggregated for each category of students described in section 1111(b)(2)(B)(xi) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(b)(2)(B)(xi) ).\n#### 8. National activities\n##### (a) Reporting by Secretary\nNot less frequently than once annually, the Secretary shall submit to Congress a report that includes\u2014\n**(1)**\nan analysis of the information received from States and eligible entities under section 7;\n**(2)**\nan identification of best practices for carrying out programs supported by grants under this Act; and\n**(3)**\nthe results of the evaluation under subsection (b).\n##### (b) National evaluation\nNot later than 6 months after the date of enactment of this Act, the Secretary shall seek to enter into a contract with an independent entity to perform an evaluation of the grants awarded under this Act. Such evaluation shall apply rigorous procedures to obtain valid and reliable data concerning student outcomes by social and academic characteristics and monitor the progress of students from secondary school to and through postsecondary education.\n##### (c) Technical assistance\nThe Secretary shall provide technical assistance to States and eligible entities concerning best practices and quality improvement programs in early college high schools and dual or concurrent enrollment programs and shall disseminate such best practices among eligible entities, States, and local educational agencies.\n##### (d) Administrative costs\nFrom amounts reserved to carry out this section under section 4(b)(3), the Secretary may reserve such sums as may be necessary for the direct administrative costs of carrying out the Secretary\u2019s responsibilities under this Act.\n#### 9. Rules of construction\n##### (a) Employees\nNothing in this Act shall be construed to alter or otherwise affect the rights, remedies, and procedures afforded to the employees of local educational agencies (including schools) or institutions of higher education under Federal, State, or local laws (including applicable regulations or court orders) or under the terms of collective bargaining agreements, memoranda of understanding, or other agreements between such employees and their employers.\n##### (b) Graduation rate\nFor purposes of this Act and any other Federal law, a student who graduates from an early college high school supported by a grant under section 5 within 100 percent of the normal time for completion described in the eligible entity\u2019s application under such section shall be counted in the four-year adjusted cohort graduation rate for such high school.",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-11-19",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "6133",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Jumpstart on College Act",
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
        "name": "Education",
        "updateDate": "2025-12-02T15:27:33Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2892is.xml"
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
      "title": "Jumpstart on College Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Jumpstart on College Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Education to make grants to support early college high schools and dual or concurrent enrollment programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T06:03:21Z"
    }
  ]
}
```
