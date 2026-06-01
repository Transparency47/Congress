# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1347?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1347
- Title: Making Education Affordable and Accessible Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1347
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-05-19T12:54:42Z
- Update date including text: 2025-05-19T12:54:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1347",
    "number": "1347",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Making Education Affordable and Accessible Act of 2025",
    "type": "S",
    "updateDate": "2025-05-19T12:54:42Z",
    "updateDateIncludingText": "2025-05-19T12:54:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T21:27:34Z",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "AR"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1347is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1347\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Peters (for himself and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to make college affordable and accessible by expanding access to dual or concurrent enrollment programs and early college high school programs.\n#### 1. Short title\nThis Act may be cited as the Making Education Affordable and Accessible Act of 2025 .\n#### 2. Dual or concurrent enrollment programs and early college high school\nPart B of title VII of the Higher Education Act of 1965 ( 20 U.S.C. 1138 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 745 as section 746;\n**(2)**\nin section 746, as redesignated by paragraph (1), by striking fiscal year 2009 and inserting fiscal year 2025 ; and\n**(3)**\nby inserting after section 744 the following:\n745. Dual or concurrent enrollment programs and early college high school (a) Purpose The purpose of this section is to expand access for high school students to the opportunities offered in dual or concurrent enrollment programs and early college high school programs established through partnerships between local educational agencies and institutions of higher education that enable such students to earn postsecondary credits while enrolled in a public high school. (b) Definitions In this section: (1) ESEA definitions The terms dual or concurrent enrollment program , early college high school , high school , and parent have the meanings given to those terms in section 8101 of the Elementary and Secondary Education Act of 1965. (2) Eligible institution The term eligible institution means an institution of higher education that carries out or plans to carry out a dual or concurrent enrollment program or an early college high school program. (3) First-generation college student The term first-generation college student has the meaning given the term in section 402A(h). (4) Rural school The term rural school means a school designated with a locale code of 41, 42, or 43, as determined by the Secretary. (c) Grants authorized (1) In general The Secretary may award grants to eligible institutions to carry out dual or concurrent enrollment programs or early college high school programs. (2) Duration A grant awarded under this subsection shall be for a period of not more than 5 years. (3) Renewal The Secretary may renew a grant awarded to an eligible institution under this subsection if the Secretary determines that the eligible institution demonstrated sufficient positive outcomes under the program carried out under the grant, based on the reports submitted under subsection (h). (d) Application An eligible institution that desires to receive a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. Such application shall include a description of\u2014 (1) the partnership between the eligible institution and each local educational agency involved in carrying out the dual or concurrent enrollment program or early college high school program; and (2) how the eligible institution will expand student access to a dual or concurrent enrollment program or an early college high school program, especially for students described in subsection (e). (e) Priority In awarding grants under this section, the Secretary shall give priority to eligible institutions that will use grant funds for dual or concurrent enrollment programs or early college high school programs that serve students from low-income families, students who attend rural schools, or first-generation college students. (f) Use of funds An eligible institution that receives a grant under this section shall use the grant funds to carry out a dual or concurrent enrollment program or an early college high school program for students enrolled in a public high school, which may include activities such as\u2014 (1) providing educators, principals, counselors, and other school leaders with professional development activities, trainings, and certifications that enhance or enable the provision of postsecondary coursework through a dual or concurrent enrollment program or an early college high school program; (2) designing the sequence of courses for a dual or concurrent enrollment program or an early college high school program\u2014 (A) to match the academic standards and rigor of a corresponding postsecondary course; and (B) in collaboration with educators from the local educational agency and faculty from the eligible institution; (3) establishing a course articulation process for defining and approving courses for high school and postsecondary credit or credentials for both 2-year and 4-year institutions of higher education in the State; (4) establishing outreach programs to provide elementary school and secondary school students, especially those students in middle grades, and their parents, educators, school counselors, and principals with general information about a dual or concurrent enrollment program or an early college high school program, including the eligibility requirements and academic preparation needed for the program; (5) helping students meet eligibility criteria for postsecondary courses and ensuring that students understand how credits earned will transfer to institutions of higher education in the State; or (6) coordinating high school transition with academic calendars. (g) Flexibility of funds (1) In general Subject to paragraph (2), an eligible institution that receives a grant under this section may use grant funds for any of the costs associated with carrying out a dual or concurrent enrollment program or an early college high school program, including the costs of\u2014 (A) tuition and fees, books, and required instructional materials for the program so that students will not be required to pay tuition or fees for postsecondary courses; and (B) transportation to and from the program. (2) Limitation An eligible institution may use not more than 20 percent of grant funds received under this section for transportation costs described in paragraph (1)(B). (h) Evaluation and reports (1) In general Each eligible institution receiving a grant under this section shall\u2014 (A) conduct an independent evaluation regarding the effectiveness and rigor of the activities as carried out by such eligible institution under this section, which shall include\u2014 (i) data on course-specific student enrollment; and (ii) the number of resulting postsecondary credits earned by students through dual or concurrent enrollment programs or early college high school programs supported under the grant that are transferred to institutions of higher education; and (B) prepare and submit to the Secretary a report containing the results of the evaluation described in subparagraph (A). (2) Requirements The Secretary may establish additional requirements for the program evaluations required under paragraph (1). (3) Report Not later than 3 years after the date of enactment of the Making Education Affordable and Accessible Act of 2025 , and every 2 years thereafter, the Secretary shall submit to Congress a summarized report that describes the findings of the evaluations conducted under paragraph (1)(A). .",
      "versionDate": "2025-04-08",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-19T12:54:42Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1347is.xml"
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
      "title": "Making Education Affordable and Accessible Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Making Education Affordable and Accessible Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to make college affordable and accessible by expanding access to dual or concurrent enrollment programs and early college high school programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:25Z"
    }
  ]
}
```
