# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2577?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2577
- Title: PLAN for School Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2577
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-03-30T18:09:47Z
- Update date including text: 2026-03-30T18:09:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2577",
    "number": "2577",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "R000609",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. Rutherford, John H. [R-FL-5]",
        "lastName": "Rutherford",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PLAN for School Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-30T18:09:47Z",
    "updateDateIncludingText": "2026-03-30T18:09:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:07:05Z",
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CO"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "PA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CT"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
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
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "IA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "HI"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "MI"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CO"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "NE"
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
      "sponsorshipDate": "2025-08-29",
      "state": "VA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "VT"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "AZ"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CT"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "NY"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "CT"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "CO"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2577ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2577\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Rutherford (for himself, Mr. Neguse , Mr. Tony Gonzales of Texas , Mr. Correa , Mr. Fitzpatrick , and Mrs. Hayes ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Homeland Security Act of 2002 to establish Regional School Safety Development Centers to provide consultation for schools to develop or improve a school safety plan based on evidence-based best practices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preparing Leaders to Assess Needs for School Safety Act of 2025 or the PLAN for School Safety Act of 2025 .\n#### 2. School safety development center program\n##### (a) In general\nSubtitle A of title XXII of the Homeland Security Act of 2002 ( 6 U.S.C. 651 et seq. ) is amended by adding at the end the following new section:\n2220F. School Safety Development Center Program (a) In general The Director shall make awards, including grants or cooperative agreements, to eligible entities to establish, improve, or maintain statewide or intrastate Regional School Safety Development Centers ( School Safety Development Centers ) for the purposes of providing customized consulting services to schools to develop, improve, or implement the school\u2019s individualized school safety plan. (b) Awards (1) Application To seek an award under this section, an eligible entity shall submit an application to the Director at such time, in such manner, and containing such information as the Director may require. At minimum, any such application shall include evidence of the applicant\u2019s expertise in comprehensive school safety and school climate, including evidence-based violence prevention for students and educators, suicide prevention, student mental health, and school security. (2) Preference In making awards under this section, the Director shall, as appropriate, give preference to eligible entities that have existing relationships with local schools, particularly those in rural, Tribal, or low-resourced communities, as applicable by the proposed geographical area, or minority-serving institutions described in sections 371(a) and 326(e)(1) of the Higher Education Act of 1965 ( 20 U.S.C. 1067q(a) and 1063b(e)(1)). (3) Use of funds An eligible entity shall use an award received under this section to establish, improve, or maintain a School Safety Development Center, which shall include each of the following: (A) Developing communications materials for and disseminating to schools, educators, parents, legal guardians, and youth, and increasing State-wide or intrastate regional public awareness of evidence-based research and best practices for school safety and student mental health. (B) Conducting individualized consultations with schools to research and analyze a school\u2019s existing school safety and student mental health policies, or developing or improving, in coordination with a school, a customized school safety and student mental health plan to fit the individualized, age- and developmentally-appropriate needs of such school community based on evidence-based best practices. (C) Assisting schools in the implementation of their customized school safety and mental health plan, including the following: (i) Identification of Federal or State government funding for implementation of the plan, in whole or in part. (ii) Provide training, resources, or technical assistance to assist schools in applying for such Federal or State government funding. (iii) Providing training, resources, and technical assistance to educate school staff and families regarding the policies and procedures of the plan. (4) Matching requirement The Federal share of the cost of activities for which a grant or cooperative agreement is made to an eligible entity under this section may not exceed 95 percent of the total cost of such activities. (c) Award administration (1) Training and technical assistance The Director, in consultation with the Secretary of Education and the Youth Advisory Council (established pursuant to paragraph (2)(C)), shall provide eligible entities receiving awards under this section, training and technical assistance on the following: (A) Best practices for individualized consulting with schools based on their unique needs for implementation in accordance with subsection (b)(3). (B) Evidence-based practices and recommendations established under section 2220D that are presented in a clear and concise manner for schools and the public. (2) Subject matter experts (A) Personnel The Director shall hire additional personnel and contractors with expertise in school mental health and school administration to provide additional subject matter expertise in implementing evidence-based programming within schools to carry out paragraph (1). (B) Detailee (i) In general The Secretary of Education shall detail, on a reimbursable basis, to the Agency an employee of the Department of Education to assist in the provision of the training and technical assistance described in paragraph (1). (ii) Reimbursement The Director shall reimburse the Secretary of Education for any costs associated with the detailee under clause (i). (C) Youth Advisory Council (i) Establishment Not later than one year after the date of the enactment of this section, the Director shall establish and convene a Youth Advisory Council for the purpose of providing joint advice on the implementation of this section. (ii) Participation The Youth Advisory Council shall include participation from the following: (I) Parents, academic experts, mental health professionals, and members of civil society with respect to the prevention of violence in schools. (II) Youth representation, including youth who have experienced school violence. (d) Report to Congress Not later than two years after the date of the enactment of this section and annually thereafter, the Director shall submit to the Committee on Homeland Security, the Committee on the Judiciary, the Committee on Education and Workforce, and the Committee on Appropriations of the House of Representatives and the Committee on Homeland Security and Governmental Affairs, the Committee on Health, Education, Labor, and Pensions, and the Committee on Appropriations of the Senate a report on actions taken by the Director to implement this section, including information relating to the following: (1) The name, location, and number of eligible entities in each State receiving awards under this section. (2) A comparative analysis of actions recommended in school safety plans by such eligible entities through the School Safety Development Centers assisted through such awards. (3) An assessment of the effectiveness of such School Safety Development Centers in assisting schools to develop and implement school safety plans, as a means to avert violence, including self-harm, if applicable, and policy recommendations for improved effectiveness. (e) Rule of construction (1) Waiver of requirements Nothing in this section may be construed to establish, satisfy, or waive any requirement under any of the following: (A) Title II of the Americans With Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. ). (B) The Rehabilitation Act of 1973 ( 29 U.S.C. 701 et seq. ). (C) Title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ). (D) Title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ). (E) The Age Discrimination Act of 1975 ( 42 U.S.C. 6101 et seq. ). (F) The Family Educational Rights and Privacy Act of 1973 ( 20 U.S.C. 1232g ). (2) No effect on other laws Nothing in this section may be construed to preclude or contradict any other provision of law authorizing training in the use of firearms. (f) Authorization of appropriations (1) In general To carry out this section, there are authorized to be appropriated $25,000,000 annually from fiscal years 2026 through 2030. (2) Restriction on use of funds Amounts made available to carry out this section may not be used to\u2014 (A) consult or train any school or person in the use of firearms; or (B) hire school personnel or school-based contractors for the schools the School Safety Development Centers are advising under subsection (b)(3). (g) Definitions In this section: (1) Eligible entities The term eligible entities means any of the following: (A) A State. (B) A State educational agency (as such term is defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ). (C) A Tribal educational agency (as such term is defined in section 6132 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7452 )). (D) An institution of higher education eligible for assistance under title III of the Higher Education Act of 1965 ( 20 U.S.C. 1051 et seq. ). (E) A Tribal College or University (as such term is defined in section 313 of the Higher Education Act of 1965 ( 20 U.S.C. 1059c )). (2) Evidence-based The term evidence-based has the meaning given such term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ). (3) School The term school has the meaning given such term in section 2704 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10554 ). (4) School safety plan The term school safety plan means a set of common actions schools can take to address the foundational elements of school safety, including designated staff, school climate and mental health, reporting systems, threat assessment, emergency planning, educator training, student prevention training, exercises and drills, site assessments, and recovery plans. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 is amended by inserting after the item relating to section 2220E the following new item:\nSec. 2220F. School Safety Development Center program. .",
      "versionDate": "2025-04-01",
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
            "name": "Advisory bodies",
            "updateDate": "2026-03-30T18:09:23Z"
          },
          {
            "name": "Child health",
            "updateDate": "2026-03-30T18:09:39Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2026-03-30T18:09:34Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-30T18:09:29Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2026-03-30T18:09:06Z"
          },
          {
            "name": "Educational facilities and institutions",
            "updateDate": "2026-03-30T18:09:14Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-03-30T18:08:54Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2026-03-30T18:09:47Z"
          },
          {
            "name": "School administration",
            "updateDate": "2026-03-30T18:08:58Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-03-30T18:09:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-04-08T16:26:59Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2577ih.xml"
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
      "title": "PLAN for School Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PLAN for School Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preparing Leaders to Assess Needs for School Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to establish Regional School Safety Development Centers to provide consultation for schools to develop or improve a school safety plan based on evidence-based best practices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T06:48:32Z"
    }
  ]
}
```
