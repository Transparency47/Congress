# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3994?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3994
- Title: Understanding Student Parent Outcomes Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3994
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3994",
    "number": "3994",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "R000305",
        "district": "2",
        "firstName": "Deborah",
        "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
        "lastName": "Ross",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Understanding Student Parent Outcomes Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:00:05Z",
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
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "GA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3994ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3994\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Ross (for herself, Mrs. McBath , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo improve data collection related to student parents pursuing higher education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Understanding Student Parent Outcomes Act of 2025 .\n#### 2. Data on student parents pursuing higher education\n##### (a) IPEDS data elements\nThe Commissioner of Education Statistics shall carry out the following:\n**(1)**\n**(A)**\nTo ensure consistency of the data collected pursuant to paragraph (B), establish a common definition of the term parenting student that covers any student who identifies as a parent or caregiver of a dependent child, in consultation with groups that include\u2014\n**(i)**\nstudents who are parents or caregivers of dependent children;\n**(ii)**\nexperts in data collection related to such students;\n**(iii)**\nsupport staff at institutions of higher education for such students;\n**(iv)**\nfinancial aid administrators at institutions of higher education; and\n**(v)**\nresearch staff at institutions of higher education.\n**(B)**\n**(i)**\nNot later than 2 years after the date of the enactment of this Act, develop data elements related to parenting students (as such term is defined pursuant to subparagraph (A)) attending institutions of higher education for the surveys conducted as a part of the Integrated Postsecondary Education Data System (IPEDS) or any other Federal postsecondary institution data collection effort, to collect data related to such parenting students that shall be disaggregated in accordance with clause (ii), and which includes data elements on\u2014\n**(I)**\nthe number of parenting students;\n**(II)**\nthe enrollment, retention, and completion rates of parenting students;\n**(III)**\nthe average individual net price charged to parenting students by institutions of higher education (as determined based on the calculation of the individual net price of an institution of higher education for a student under section 132(h)(2) of the Higher Education Act of 1965 ( 20 U.S.C. 1015a(h)(2) ));\n**(IV)**\nthe marital status of such students (reported in aggregate by marital status categories);\n**(V)**\nthe number of such students who are employed for all or part of the academic year while enrolled;\n**(VI)**\nthe median income of such students, and the number of such students in each income category (determined in accordance with section 132(i)(6) of the Higher Education Act of 1965 ( 20 U.S.C. 1015a(i)(6) ));\n**(VII)**\nthe number of such students who are enrolled in an associate, baccalaureate, or graduate degree program, or a certificate program;\n**(VIII)**\nthe number of such students who are enrolled full-time, part-time, or less than part-time;\n**(IX)**\nthe number of such students who are Federal Pell grant recipients;\n**(X)**\nthe number of such students who use campus-based childcare services;\n**(XI)**\nthe number and age of dependent children of such students;\n**(XII)**\nthe disability status of dependent children of such students; and\n**(XIII)**\nthe transfer status of such students (without regard to whether such students were admitted as a transfer student or not).\n**(ii)**\nAny data collected using the data elements developed pursuant to clause (i) shall be disaggregated\u2014\n**(I)**\nby students who identify as a parent of a dependent child; and\n**(II)**\nby students who identify as a caregiver of a dependent child.\n**(2)**\nNot later than 2 years after the date of enactment of this Act, include the experts described in paragraph (1)(A)(ii) in the technical and scientific peer-review groups and scientific program advisory committees authorized under section 114(g) of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9514(g) ) to advise, on a continuous basis, the Commissioner on best practices related to data collection on parenting students (as such term is defined pursuant to paragraph (1)(A)).\n**(3)**\nBeginning with academic year 2026\u20132027 and annually thereafter\u2014\n**(A)**\ncollect information on the data elements described in paragraph (1)(B) with respect to, at a minimum, the institutions of higher education required to complete, pursuant to section 487(a)(17) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a)(17) ), the surveys described in paragraph (1)(B); and\n**(B)**\ndisaggregate the information collected\u2014\n**(i)**\nby race and ethnicity; and\n**(ii)**\nby gender.\n##### (b) Technical assistance\nThe Secretary of Education, in consultation with the Commissioner of Education Statistics, shall provide technical assistance to States and institutions of higher education related to developing and carrying out State and institutional data collection mechanisms for data on the parental status of students collected in accordance with subsection (a) , including\u2014\n**(1)**\nhow to leverage existing systems, surveys, and other data collection mechanisms to collect and report such data, and examples and best practices related to data collection and privacy;\n**(2)**\nintegration and reporting of such data with State information systems, including statewide longitudinal data systems;\n**(3)**\nhow to account for data elements that change over time; and\n**(4)**\nrecommendations of best practices to institutions of higher education related to communicating with students about data use and privacy, including how data will be used to help students who are parents or caregivers of dependent children.\n#### 3. Study on improving student parent outcomes\n##### (a) Study\nThe Secretary of Education shall conduct a study of a demographically and geographically representative sample of institutions of higher education (as determined by the Secretary) on best practices of institutions of higher education that improve outcomes for students attending institutions of higher education who are parents or caregivers of dependent children. Such study shall include qualitative and quantitative research on\u2014\n**(1)**\nthe enrollment, persistence, and retention of students attending institutions of higher education who are parents or caregivers of dependent children, disaggregated by race, ethnicity, gender, income, and the type of program in which such students are enrolled (such as an associate, baccalaureate, or graduate degree program, or a certificate program);\n**(2)**\nthe effects of the availability of campus-based childcare services on such outcomes of students who are parents or caregivers of dependent children, including a comparison of students whose children are served by the campus-based childcare services with students whose children are not served by campus-based childcare services;\n**(3)**\nenrollment trends of students who are parents or caregivers of dependent children to attend certain institutions or types of institutions, and whether such trends and preferences are based on the availability of institutional support services for such students, such as campus-based childcare, student parent centers, and grants under the Child Care Access Means Parents in School Program under subpart 7 of part A of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070e );\n**(4)**\nthe percentage of children served by campus-based childcare services who are the children of students, compared to the percentage of such children who are children of faculty, staff, and other community members, disaggregated by\u2014\n**(A)**\nrace, ethnicity, gender, employment or student status (including faculty, staff, community member, and student status), and family income of the parent of such children; and\n**(B)**\nonly with respect to students who are parents of such children, the type of program in which the student is enrolled (such as an associate, baccalaureate, or graduate degree program, or a certificate program); and\n**(5)**\nthe strategies used by institutions of higher education for integration of on-campus services for students who are parents or caregivers of dependent children with other State and institution-provided services, such as the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ), the program of block grants for States for temporary assistance for needy families established under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ), the special supplemental nutrition program for women, infants, and children under the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ), workforce programs including adult education and literacy activities (as defined in section 203 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3272 )), and Head Start and Early Head Start programs carried out under the Head Start Act ( 42 U.S.C. 9831 et seq. ).\n##### (b) Report and dissemination of findings\nNot later than 2 years after the date of the enactment of this Act, the Secretary of Education shall report the findings of the study conducted under subsection (a) to Congress, and make such findings publicly available. Such findings shall include information on the best practices identified by the Secretary to be most effective at improving outcomes for students attending institutions of higher education who are parents or caregivers of dependent children.\n#### 4. Definitions\nIn this Act:\n**(1) Institution of higher education**\nThe term institution of higher education has the meaning given the term section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n**(2) State**\nThe term State has the meaning given the term in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 ).",
      "versionDate": "2025-06-12",
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
        "updateDate": "2025-07-03T14:03:14Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3994ih.xml"
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
      "title": "Understanding Student Parent Outcomes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Understanding Student Parent Outcomes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-24T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve data collection related to student parents pursuing higher education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-24T04:18:24Z"
    }
  ]
}
```
