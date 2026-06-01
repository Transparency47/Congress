# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3406?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3406
- Title: PATHS to Tutor Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3406
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-02-04T05:06:24Z
- Update date including text: 2026-02-04T05:06:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3406",
    "number": "3406",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "PATHS to Tutor Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T05:06:24Z",
    "updateDateIncludingText": "2026-02-04T05:06:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T21:50:01Z",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3406is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3406\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Booker (for himself, Mr. Cornyn , and Mr. Murphy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish a grant program for innovative partnerships among teacher preparation programs, local educational agencies, and community-based organizations to expand access to high-quality tutoring in hard-to-staff schools and high-need schools, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Partnering Aspiring Teachers with High-need Schools to Tutor Act of 2025 or the PATHS to Tutor Act of 2025 .\n#### 2. Grant program for high-quality tutoring\n##### (a) Definitions\nIn this section:\n**(1) Educational service agency**\nThe term educational service agency has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Educator preparation program**\nThe term educator preparation program means a State-accredited program at a public or nonprofit institution of higher education or other nonprofit provider that prepares individuals to serve as educators.\n**(3) Hard-to-staff school**\nThe term hard-to-staff school means a high-need school that has a high rate of teacher turnover or a large concentration of teachers in their first or second year of teaching.\n**(4) High-need school**\nThe term high-need school has the meaning given the term in section 2211 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6631 ).\n**(5) High-quality tutoring**\nThe term high-quality tutoring means tutoring\u2014\n**(A)**\nthat is provided by a tutor;\n**(B)**\nthat is one-on-one or in a small group not to exceed a ratio of 1 tutor to 4 students, or a small group ratio based on evidence determined sufficient by the State educational agency in the State in which the tutoring takes place;\n**(C)**\nthat includes plans and time for tutors to collaborate;\n**(D)**\nthat\u2014\n**(i)**\nincludes multiple sessions each week that are of sufficient length, such as the length of a regularly scheduled class or period; and\n**(ii)**\nis\u2014\n**(I)**\nembedded in the school schedule, preferably during the regular school day or tightly integrated to the regular school day and provided before or after school; or\n**(II)**\nduring school vacations;\n**(E)**\nin which content and grade-specific tutors are matched with students;\n**(F)**\nthat is aligned to local standards and curriculum;\n**(G)**\nthat includes high-quality pre-service training and ongoing professional support;\n**(H)**\nthat a local consortium facilitates by\u2014\n**(i)**\nthe local educational agency and schools in the local consortium supporting tutors through direct supervision and feedback; and\n**(ii)**\nthe faculty or staff of the educator preparation program in the local consortium providing additional capacity; and\n**(I)**\nwhere tutors are adequately compensated for their work.\n**(6) Local consortium**\nThe term local consortium means a consortium consisting of community partners as follows:\n**(A)**\nThe consortium shall include the following entities, one or both of which shall serve as the lead entity of the consortium:\n**(i)**\nA local educational agency, an individual school, or an educational service agency.\n**(ii)**\nAn educator preparation program.\n**(B)**\nThe consortium may include a community partner, such as\u2014\n**(i)**\na community-based organization;\n**(ii)**\na child- and youth-serving organization or agency;\n**(iii)**\nan institution of higher education, as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) );\n**(iv)**\na foundation;\n**(v)**\nan educator organization;\n**(vi)**\nan organization representing education professionals;\n**(vii)**\na local government, including a government agency serving children and youth, such as a child welfare and juvenile justice agency;\n**(viii)**\nan organization representing students; or\n**(ix)**\nan organization representing parents.\n**(7) Local educational agency**\nThe term local educational agency has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(8) Mentor**\nThe term mentor means an experienced educator, including a teacher-educator at an educator preparation program, dedicated to advising a tutor or administering the tutoring program.\n**(9) Secretary**\nThe term Secretary means the Secretary of Education.\n**(10) Tutor**\nThe term tutor means\u2014\n**(A)**\na postsecondary student, including one who is enrolled in an educator preparation program;\n**(B)**\na recent graduate of an educator preparation program;\n**(C)**\nan individual serving as an education paraprofessional or teaching aide; or\n**(D)**\na fully certified and licensed educator (such as a recently retired educator, an educator experiencing a gap in employment due to COVID-induced budget cuts, or an educator providing tutoring before or after school or during the summer).\n##### (b) Demonstration competitive grant program\nThe Secretary shall award grants, on a competitive basis, to local consortia to enable the local consortia to carry out high-quality tutoring, especially at hard-to-staff schools or high-need schools.\n##### (c) Application\nA local consortium that desires to receive a grant under this section shall submit an application to the Secretary at such time, in such manner, and accompanied by such information as the Secretary may require, including the following:\n**(1)**\nA description of the local consortium, including which public or nonprofit entity participating in the local consortium shall serve as the fiscal agent for the local consortium.\n**(2)**\nA description of the strategy for recruitment, careful selection, and matching of tutors with hard-to-staff schools and high-need schools.\n**(3)**\nA description of the pre-service training and ongoing professional support for tutors.\n**(4)**\nA list of hard-to-staff schools and high-need schools, and the grades that will be supported in each school, identified by the local consortium to receive a comprehensive, coordinated continuum of services and support.\n**(5)**\nA description of how the high-quality tutoring program plans to accelerate student learning.\n**(6)**\nA description of how the local consortium will ensure that the high-quality tutoring provided under such program does not result in the tracking or negative labeling of students, or remediation.\n**(7)**\nA description of the duration of the high-quality tutoring, including the duration of sessions, the number of days a week tutoring will occur, and the length in weeks the tutoring will occur.\n**(8)**\nAn assurance that the local consortium will align high-quality tutoring to the local curriculum and standards of the local educational agency and school and will be designed to support student success in the classroom.\n**(9)**\nA description of materials and supports and how they are aligned with the local curriculum and standards of the local educational agency and school.\n**(10)**\nA description of how the high-quality tutoring program will build school capacity in the schools in which the tutors will serve.\n**(11)**\nAn assurance that the local consortium will leverage tutors to supplement, not supplant, existing staff.\n**(12)**\nA description of how tutors will be adequately compensated.\n**(13)**\nAn assurance that the local consortium will use funds to supplement and not supplant funds otherwise available to carry out high-quality tutoring and will not use any funds to replace teaching positions with tutoring positions.\n**(14)**\nA description of how the tutoring program will incorporate research-based social-emotional learning practices, trauma-informed learning practices, and culturally and linguistically responsive practices.\n##### (d) Priority\nIn awarding grants under this section, the Secretary shall give priority to local consortia that plan to support high-need schools in building student learning capacity by using tutors who\u2014\n**(1)**\nare postsecondary students who are enrolled in educator preparation programs; or\n**(2)**\nare enrolled in a historically Black college or university (defined as a part B institution under section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 )) or another minority-serving institution (defined as an eligible institution under section 371(a) of such Act ( 20 U.S.C. 1067q(a) )).\n##### (e) Use of funds\nA local consortium that receives a grant under this section may use the grant funds for the following:\n**(1)**\nMatching, training, and placing tutors with schools to deliver high-quality tutoring.\n**(2)**\nSupporting tutors to work with small groups of students attending high-need schools wherein tutors are providing supervision and instruction, and providing the tutors with time for collaboration with mentors.\n**(3)**\nMatching tutors in the high-quality tutoring program with mentors.\n**(4)**\nProviding stipends to such tutors and mentors.\n**(5)**\nPurchasing instructional materials and connectivity resources, including internet access and accessible devices.\n**(6)**\nProviding transportation for students attending the high-quality tutoring program.\n**(7)**\nProviding meals and snacks for students attending the high-quality tutoring program.\n**(8)**\nProviding facilities for conducting the high-quality tutoring program.\n##### (f) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to carry out this section $500,000,000.\n**(2) Allocation**\nFrom the amounts appropriated to carry out this section\u2014\n**(A)**\nnot less than 85 percent shall be used for directly supporting students, including providing stipends to tutors and mentors in the high-quality tutoring program, providing transportation, meals, and snacks, and purchasing instructional materials and connectivity resources for students; and\n**(B)**\nnot more than 15 percent shall be used for other uses in carrying out this section.\n#### 3. Coordination with the Corporation for National and Community Service\n##### (a) Interagency agreement\nThe Secretary of Education shall enter into an interagency agreement with the Corporation for National and Community Service under section 121(b) of the National and Community Service Act of 1990 ( 42 U.S.C. 12571(b) ) under which the Corporation shall approve tutor positions under a program funded under section 2, as approved national service positions (as defined in section 101 of the National and Community Service Act of 1990 ( 42 U.S.C. 12511 )). Such interagency agreement shall specify how a degree or certificate of completion for a term of service as a provider of high-quality tutoring will be submitted to the Corporation.\n##### (b) Special rule\nNotwithstanding section 148 of the National and Community Service Act of 1990 ( 42 U.S.C. 12604 ), the Secretary and the Chief Executive Officer of the Corporation for National and Community Service shall develop a program under which national service educational awards may be disbursed to tutors upon completion of service under a program funded under section 2.",
      "versionDate": "2025-12-09",
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
        "actionDate": "2025-12-09",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "6532",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PATHS to Tutor Act of 2025",
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
        "updateDate": "2026-01-08T19:41:01Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3406is.xml"
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
      "title": "PATHS to Tutor Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PATHS to Tutor Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Partnering Aspiring Teachers with High-need Schools to Tutor Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a grant program for innovative partnerships among teacher preparation programs, local educational agencies, and community-based organizations to expand access to high-quality tutoring in hard-to-staff schools and high-need schools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:32Z"
    }
  ]
}
```
