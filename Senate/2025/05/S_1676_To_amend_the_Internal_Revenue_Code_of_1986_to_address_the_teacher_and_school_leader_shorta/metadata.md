# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1676?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1676
- Title: RETAIN Act
- Congress: 119
- Bill type: S
- Bill number: 1676
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-12-05T21:53:30Z
- Update date including text: 2025-12-05T21:53:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S2839-2841)
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S2839-2841)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1676",
    "number": "1676",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "RETAIN Act",
    "type": "S",
    "updateDate": "2025-12-05T21:53:30Z",
    "updateDateIncludingText": "2025-12-05T21:53:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S2839-2841)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T16:53:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1676is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1676\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Durbin (for himself and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to address the teacher and school leader shortage in early childhood, elementary, and secondary education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Retaining Educators Takes Added Investment Now Act or the RETAIN Act .\n#### 2. Purpose\nThe purpose of this Act is to create a refundable tax credit for early childhood educators, teachers, early childhood education program directors, school leaders, and school-based mental health services providers in early childhood, elementary, and secondary education settings that rewards retention based on the time spent serving high-need students.\n#### 3. Findings\nCongress finds the following:\n**(1)**\nThe shortage of experienced, qualified early childhood educators and elementary school and secondary school teachers is a national problem that compromises the academic outcomes and long-term success of students.\n**(2)**\nThe shortage is the result of many factors including low pay, frequent turnover in school leadership, poor teaching conditions, and inadequate teacher supports.\n**(3)**\nThe shortage is worse in high-poverty areas where the factors contributing to the shortage are particularly acute and have an increased negative impact on teachers of color remaining in the field.\n**(4)**\nA child\u2019s access to high-quality early childhood education is critical to supporting positive outcomes, and early childhood educators\u2014\n**(A)**\nplay an important role in setting the foundation for future learning, and\n**(B)**\npromote the development of vital skills, habits, and mindsets that children need to be successful in school and in life.\n**(5)**\nIn 2024, the national median pay of early childhood educators was a mere $37,120, with many early childhood educators relying on government assistance programs such as Medicaid, the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ), or the temporary assistance for needy families program established under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ), and struggling to provide for their own families.\n**(6)**\nStudies have demonstrated that well-qualified, experienced teachers are the single most important school-based element contributing to a child\u2019s academic achievement and success.\n**(7)**\nIn the 2023\u20132024 academic year, the average teacher salary in public elementary schools and secondary schools was only $72,030. When adjusted for inflation, the average teacher salary has declined by 5 percent over the past decade.\n**(8)**\nOn average, public elementary school and secondary school teachers were paid 23.5 percent less than other college graduates working in non-teaching fields, and many teachers struggle with large amounts of student loan debt.\n**(9)**\nIn the 2023\u20132024 academic year, the average teacher salary for a first-year teacher in a public elementary school or secondary school was $46,526.\n**(10)**\nAn experienced, well-qualified education workforce must also be reflective of the diversity of the student body across race, ethnicity, and disability.\n**(11)**\nHigher pay for teachers can result in a more diverse teacher workforce, and minority students often perform better on standardized tests, have improved attendance, and are suspended less frequently when they have at least one same-race teacher.\n**(12)**\nExperienced, well-qualified school leaders and school-based mental health service providers are essential for providing strong educational opportunities and services for students and promoting teacher retention through improved professional supports and teaching conditions.\n**(13)**\nIn 2024, the teaching profession experienced the lowest levels of employment in 50 years.\n#### 4. Refundable tax credit for teacher and school leader retention\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Teacher and school leader retention credit (a) Allowance of credit (1) In general In the case of an individual who is employed in a position described in paragraph (2) during a school year ending with or within the taxable year, there shall be allowed as a credit against the tax imposed by this subtitle for the taxable year an amount equal to the applicable amount (as determined under subsection (b)). (2) Eligible positions The positions described in this paragraph shall consist of the following: (A) An eligible early childhood educator. (B) An eligible early childhood education program director. (C) An eligible early childhood education provider. (D) An eligible teacher. (E) An eligible paraprofessional. (F) An eligible school-based mental health services provider. (G) An eligible school leader. (b) Applicable amount (1) In general For purposes of this section, the applicable amount shall be an amount determined based on the number of school years for which the individual has been continuously employed in any position described in subsection (a)(2), as follows: (A) Subject to paragraph (2), for the first year of employment, $5,800. (B) For the second continuous year of employment, $5,800. (C) For the third and fourth continuous year of employment, $7,000. (D) For the fifth, sixth, seventh, eighth, and ninth continuous year of employment, $8,700. (E) For the tenth continuous year of employment, $11,600. (F) For the eleventh, twelfth, thirteenth, fourteenth, and fifteenth continuous year of employment, $8,700. (G) For the sixteenth continuous year of employment, $7,000. (H) For the seventeenth, eighteenth, nineteenth, and twentieth continuous year of employment, $5,800. (2) First year For purposes of the first year of employment ending with or within a taxable year, an individual must have been so employed for a period of not less than 4 months before the first day of such taxable year. (3) Limitation based on total number of school years In the case of any individual who has been employed in any position described in subsection (a)(2) for a total of more than 20 school years, the applicable amount shall be reduced to zero. (c) Inflation adjustment (1) In general In the case of any taxable year beginning after 2026, each of the dollar amounts in subsection (b)(1) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for such calendar year by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding If any increase determined under paragraph (1) is not a multiple of $100, such increase shall be rounded to the nearest multiple of $100. (d) Supplementing, not supplanting, State and local education funds (1) In general A State educational agency or local educational agency shall not reduce or adjust any compensation, or any assistance provided through a loan forgiveness program, to an employee of the State educational agency or local educational agency who serves in any position described in subsection (a)(2) due to the individual\u2019s eligibility for the credit under this section. (2) Methodology Upon request by the Secretary of Education, a State educational agency or local educational agency shall reasonably demonstrate that the methodology used to allocate amounts for compensation and for loan forgiveness to the employees described in paragraph (1) at qualifying schools or qualifying early childhood education programs ensures that employees at each qualifying school or qualifying early childhood education program in the State or served by the local educational agency, respectively, receive the same amount of State or local funds for compensation and loan forgiveness that the qualifying school or qualifying early childhood education program would receive if the credit under this section had not been enacted. (e) Information sharing The Secretary of Education and the Secretary of Health and Human Services shall provide the Secretary with such information as is necessary for purposes of determining whether an early childhood education program or an elementary school or secondary school satisfies the requirements for a qualifying early childhood education program or a qualifying school, respectively. (f) Definitions For purposes of this section\u2014 (1) ESEA definitions The terms elementary school , local educational agency , secondary school , State educational agency , and educational service agency have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ). (2) Eligible early childhood education program director The term eligible early childhood education program director means an employee or officer of a qualifying early childhood education program who is responsible for the daily instructional leadership and managerial operations of such program. (3) Eligible early childhood education provider The term eligible early childhood education provider means an individual\u2014 (A) who\u2014 (i) has an associate\u2019s degree or higher degree in early childhood education or a related field, or (ii) is enrolled during the taxable year in a program leading to such an associate\u2019s or higher degree and is making satisfactory progress toward such degree, and (B) who is responsible for the daily instructional leadership and managerial operations of a qualifying early childhood education program in a home-based setting. (4) Eligible early childhood educator The term eligible early childhood educator means an individual\u2014 (A) who\u2014 (i) has an associate\u2019s degree or higher degree in early childhood education or a related field, or (ii) is enrolled during the taxable year in a program leading to such an associate\u2019s or higher degree and is making satisfactory progress toward such degree, (B) who has credentials or a license under State law for early childhood education, as applicable, and (C) whose primary responsibility is for the learning and development of children in a qualifying early childhood education program during the taxable year. (5) Eligible paraprofessional The term eligible paraprofessional means an individual\u2014 (A) who is a paraprofessional, as defined in section 3201 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7011 ), (B) who meets the applicable State professional standards and qualifications pursuant to section 1111(g)(2)(M) of such Act ( 20 U.S.C. 6311(g)(2)(M) ), (C) whose primary responsibilities involve working or assisting in a classroom setting, and (D) who is employed in a qualifying school or a qualifying early childhood education program. (6) Eligible school-based mental health services provider The term eligible school-based mental health services provider means an individual\u2014 (A) described in section 4102(6) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7112(6) ), and (B) who is employed in a qualifying school or a qualifying early childhood education program. (7) Eligible school leader The term eligible school leader means a principal, assistant principal, or other individual who is\u2014 (A) an employee or officer of a qualifying school, and (B) responsible for the daily instructional leadership and managerial operations in the qualifying school. (8) Eligible teacher The term eligible teacher means an individual who\u2014 (A) is an elementary school or secondary school teacher who, as determined by the State or local educational agency, is a teacher of record who provides direct classroom teaching (or classroom-type teaching in a nonclassroom setting) to students in a qualifying school, and (B) (i) meets applicable State certification and licensure requirements, including any requirements for certification obtained through alternative routes to certification, in the State in which such school is located and in the subject area in which the individual is the teacher of record, or (ii) is enrolled during the taxable year in a program leading to State certification and licensure as described in clause (i) and is making satisfactory progress toward such certification and licensure requirements. (9) Qualifying early childhood education program (A) In general The term qualifying early childhood education program means an early childhood education program, as defined in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 ), that, regardless of setting\u2014 (i) serves children who receive services for which financial assistance is provided in accordance with the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ), the Head Start Act ( 42 U.S.C. 9831 et seq. ), or the child and adult care food program established under section 17 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766 ), and (ii) participates in a State tiered and transparent system for measuring program quality. (B) Special rule Notwithstanding subparagraph (A), an early childhood education program that does not satisfy the requirements of subparagraph (A)(ii) shall be deemed to be a qualifying early childhood education program until September 30, 2025, if the program\u2014 (i) satisfies all requirements of subparagraph (A) except for clause (ii) of such subparagraph, and (ii) (I) meets the Head Start program performance standards described in section 641A(a) of the Head Start Act ( 42 U.S.C. 9836a(a) ), if applicable, or (II) is accredited by a national accreditor of early learning programs as of the date of enactment of the Retaining Educators Takes Added Investment Now Act . (10) Qualifying school The term qualifying school means\u2014 (A) a public elementary school or secondary school that\u2014 (i) is in the school district of a local educational agency that is eligible for assistance under part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ), or (ii) is served or operated by an educational service agency that is eligible for such assistance, or (B) an elementary school or secondary school that is funded by the Bureau of Indian Education and that is in the school district of a local educational agency that is eligible for such assistance. .\n##### (b) W\u20132 reporting of continuous employment for certain positions at qualifying early childhood education programs or qualifying schools\nSection 6051(a) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (16), by striking the period at the end of paragraph (17) and inserting , and , and by inserting after paragraph (17) the following new paragraph:\n(18) in the case of an employee who is employed in a position described in subsection (a)(2) of section 36C, the number of school years for which such employee has been continuously employed in any such position. .\n##### (c) Conforming amendments\n**(1)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following:\nSec. 36C. Teacher and school\n                                leader retention credit.\n**(2)**\nSection 6211(b)(4)(A) of such Code is amended by inserting 36C, after 36B, .\n**(3)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 5. Developing interagency data series\nThe Secretary of Labor, in coordination with the Secretary of Treasury, the Secretary of Education, and the Secretary of Health and Human Services, shall\u2014\n**(1)**\ndevelop and publish on the internet website of the Bureau of Labor Statistics a data series that captures\u2014\n**(A)**\nthe average base salary of teachers in elementary schools and secondary schools, disaggregated by\u2014\n**(i)**\nemployment in public elementary schools and secondary schools that receive assistance under part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ),\n**(ii)**\nemployment in public elementary schools and secondary schools that do not receive such assistance, and\n**(iii)**\ngeographic region, and\n**(B)**\nthe average base salary of early childhood educators, disaggregated by highest level of degree attained, and\n**(2)**\nupdate the data series under paragraph (1) on an annual basis.",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-05-08",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3308",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RETAIN Act",
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
        "name": "Taxation",
        "updateDate": "2025-06-06T18:24:38Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1676is.xml"
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
      "title": "RETAIN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RETAIN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Retaining Educators Takes Added Investment Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to address the teacher and school leader shortage in early childhood, elementary, and secondary education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:18:21Z"
    }
  ]
}
```
