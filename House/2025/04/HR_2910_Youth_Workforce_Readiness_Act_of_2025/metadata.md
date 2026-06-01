# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2910?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2910
- Title: Youth Workforce Readiness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2910
- Origin chamber: House
- Introduced date: 2025-04-14
- Update date: 2026-04-15T08:05:52Z
- Update date including text: 2026-04-15T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-14: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-14: Introduced in House

## Actions

- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-14",
    "latestAction": {
      "actionDate": "2025-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2910",
    "number": "2910",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Youth Workforce Readiness Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:52Z",
    "updateDateIncludingText": "2026-04-15T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-14",
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
      "actionDate": "2025-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-14",
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
          "date": "2025-04-14T13:02:20Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "NE"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "GA"
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
      "sponsorshipDate": "2025-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NV"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "PA"
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
      "sponsorshipDate": "2025-06-03",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "KS"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MO"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "IL"
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "IL"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
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
      "sponsorshipDate": "2025-06-05",
      "state": "IL"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "RI"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
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
      "sponsorshipDate": "2025-10-24",
      "state": "WA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NH"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "MA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2910ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2910\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2025 Mr. Harder of California (for himself, Mr. Fitzpatrick , Mr. Bacon , and Mrs. McBath ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish a competitive grant program to support out-of-school-time youth workforce readiness programs, providing employability skills development, career exploration, employment readiness training, mentoring, work-based learning, and workforce opportunities for eligible youth.\n#### 1. Short title\nThis Act may be cited as the Youth Workforce Readiness Act of 2025 .\n#### 2. Purpose\nThe purpose of this Act is to establish or expand activities to\u2014\n**(1)**\nincrease access and opportunities for youth to obtain the education and training that youth need to succeed in the labor market;\n**(2)**\nsupport engagement in and the integration of programs and activities offered during out-of-school-time hours through the workforce investment, education, and economic development systems;\n**(3)**\nimprove the quality of the workforce and meet the skill requirements of employers;\n**(4)**\nengage employers in addressing the training, skill, and employment needs of youth and youth jobseekers, and fostering opportunities for connection and economic mobility; and\n**(5)**\ninclude younger youth in the education and workforce investment activities in an age and developmentally appropriate manner.\n#### 3. Definitions\nIn this Act:\n**(1) Community-based organization**\nThe term community-based organization means a youth-serving private nonprofit organization (which may include a faith-based organization) that\u2014\n**(A)**\nis representative of a community or a significant segment of a community;\n**(B)**\nhas demonstrated expertise and effectiveness in workforce development; and\n**(C)**\nhas demonstrated expertise\u2014\n**(i)**\nin the planning and delivery of education, training, and related activities that are included in a career pathway;\n**(ii)**\nin forging coordination and cooperation between educators and other members of the community; and\n**(iii)**\nin development and implementation of data systems that measure the progress of students and outcomes of career pathways.\n**(2) Covered partnership**\nThe term covered partnership means a partnership between\u2014\n**(A)**\na community-based organization; and\n**(B)**\nan industry or sector partnership, a local educational agency, and another public entity or private employer, as appropriate.\n**(3) Eligible youth**\nThe term eligible youth has the meaning given the term in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ), except that the individual involved shall be\u2014\n**(A)**\nnot younger than age 6; and\n**(B)**\nnot older than age 18 (or age 19 if enrolled in secondary school).\n**(4) Industry or sector partnership**\nThe term industry or sector partnership means\u2014\n**(A)**\nan industry or sector partnership, as defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ); and\n**(B)**\na collaborative that meets the requirements of paragraph (26) of that section 3 but also includes\u2014\n**(i)**\nan Indian tribe or tribal organization (as such terms are defined in section 166(b) of that Act ( 29 U.S.C. 3221(b) )), as appropriate; or\n**(ii)**\na community-based organization.\n**(5) Out-of-school-time**\nThe term out-of-school-time , used with respect to a program described in section 7, means a supervised program regularly attended by eligible youth, that fosters learning and development during out-of-school-time hours, which includes hours before school, after school, during summer vacation or another school holiday, or on a Saturday or Sunday.\n**(6) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(7) WIOA definitions**\nThe terms career pathway , customized training , in-demand industry sector or occupation , local area , local board , local educational agency , and recognized postsecondary credential have the meanings given the terms in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n**(8) Workforce readiness program**\nThe term workforce readiness program means an out-of-school-time program that\u2014\n**(A)**\nmeets the requirements of section 7;\n**(B)**\nis offered by a community-based organization of an eligible entity or a related covered partnership; and\n**(C)**\nis intended to help prepare eligible youth for the workforce.\n#### 4. Grant program establishment\n##### (a) Grants\nUsing the amounts made available under section 9, the Secretary shall award grants, on a competitive basis, to eligible entities.\n##### (b) General use of funds\nThe Secretary shall award the grants, on a competitive basis, to assist eligible entities in planning, developing, and implementing nationwide, comprehensive workforce readiness programs, that are\u2014\n**(1)**\nin out-of-school-time programs;\n**(2)**\ncarried out by community-based organizations of the eligible entity or related covered partnerships; and\n**(3)**\nfor eligible youth.\n##### (c) Periods of grants\nThe Secretary shall award the grants for periods of not less than 3 years and not more than 5 years.\n#### 5. Eligible entities\nTo be eligible to receive a grant under section 4, an entity shall\u2014\n**(1)**\n**(A)**\nbe a national youth-serving organization with active chapters, affiliates, or subgrant recipients, that are community-based organizations (including such organizations that are facility-based organizations) in not fewer than 35 States; and\n**(B)**\nprovide programming focused on youth workforce readiness in an out-of-school-time program; and\n**(2)**\nobtain approval of an application under section 6.\n#### 6. Application\nTo be eligible to receive a grant under section 4, an entity shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including\u2014\n**(1)**\na description of how the entity will implement a youth workforce readiness program in a manner that ensures an equitable geographic distribution of program activities, including an equitable distribution between urban and rural communities;\n**(2)**\na description of the proposed program activities to be funded and their locations;\n**(3)**\na description of populations of eligible youth to be served, including populations living in or from underserved communities or communities with employment disparities;\n**(4)**\na description of the effective strategies, best practices, or evidence-based practices the workforce readiness program will use;\n**(5)**\nan assurance that the program will take place in safe and easily accessible facilities;\n**(6)**\na demonstration of how, in implementing the proposed program activities, the entity will coordinate activities with Federal, State, and local programs and make the most effective use of public resources;\n**(7)**\na description of\u2014\n**(A)**\nthe community-based organizations or the covered partnerships through which the entity will implement the program; and\n**(B)**\nif a covered partnership will assist in implementing the program, the collaboration and coordination activities that the community-based organization in the partnership has carried out or will carry out with other entities in the partnership, related to that implementation;\n**(8)**\nif the program includes an opportunity to earn a recognized postsecondary credential, a description of the activities leading to the credential;\n**(9)**\nan assurance that funds provided under this Act will be used to supplement and not supplant other Federal, State, or local funds expended to provide youth programs or workforce readiness programs; and\n**(10)**\na budget detailing program activities and administrative costs.\n#### 7. Program activities\n##### (a) In general\nAn eligible entity that receives a grant under section 4 shall use the grant funds\u2014\n**(1)**\nif the entity seeks to implement the workforce readiness program through a covered partnership, to establish the partnership; and\n**(2)**\nto carry out the development and implementation of a youth workforce readiness program\u2014\n**(A)**\nthat includes services to help prepare eligible youth who are not younger than age 15 for the workforce, which services shall include\u2014\n**(i)**\nsupport for the use of career pathways;\n**(ii)**\npaid and unpaid work experiences that have as a component academic and occupational education, which may include\u2014\n**(I)**\nsummer employment opportunities and other employment opportunities available throughout the school year;\n**(II)**\npre-apprenticeship and apprenticeship programs registered under the National Apprenticeship Act;\n**(III)**\ninternships and job shadowing; and\n**(IV)**\non-the-job training opportunities;\n**(iii)**\nwork-based learning (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 )) that provides opportunities for the application of employability skills, and hands-on work experiences through covered partnerships;\n**(iv)**\noccupational skill training, which shall include priority consideration for training programs that lead to recognized postsecondary credentials that are aligned with in-demand industry sectors or occupations in the local area involved, if the local board determines that the programs meet the quality criteria described in section 123 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3153 );\n**(v)**\nthe provision of customized training;\n**(vi)**\neducation offered concurrently with and in the same context as workforce readiness activities and training for a specific occupation or occupational cluster; and\n**(vii)**\nactivities that help youth prepare for and transition to postsecondary education and training;\n**(B)**\nthat includes services to help prepare eligible youth for the workforce, which services shall include\u2014\n**(i)**\nleadership development opportunities, which may include community service and peer-centered activities encouraging responsibility and other positive social and civic behaviors, as appropriate;\n**(ii)**\nworkforce or workforce readiness opportunities;\n**(iii)**\nsupportive services;\n**(iv)**\nadult mentoring for the period of participation and a subsequent period, for a total of not less than 12 months;\n**(v)**\ncomprehensive guidance and counseling, which may include drug and alcohol abuse, prevention services, counseling and referral, as appropriate;\n**(vi)**\nfinancial literacy education;\n**(vii)**\nentrepreneurial skills training;\n**(viii)**\nservices that provide labor market and employment information about in-demand industry sectors or occupations available in the local area, such as career awareness, career counseling, and career exploration services;\n**(ix)**\nactivities to develop fundamental workforce readiness skills, or to develop employability skills (such as communication, creativity, collaboration, and critical thinking) that support social-emotional development through every developmental stage, in both formal and informal learning experiences;\n**(x)**\nacademic counseling to support workforce readiness; and\n**(xi)**\ncareer exposure, through mentoring and targeted programming, offered by local industry or sector partnerships, to provide career assessments and education and career planning; and\n**(C)**\nthat may include\u2014\n**(i)**\nthe provision of professional development (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 )) for training educators and other providers of educational services who participate in the workforce readiness program; and\n**(ii)**\ndeveloping assets and resources that assist an employer or groups of employers or sectors in working with eligible youth.\n##### (b) Subgrants\nThe eligible entity may use the grant funds, with the approval of the Secretary, to award subgrants to eligible organizations to carry out activities through a youth workforce readiness program.\n#### 8. Evaluation and reporting\n##### (a) Measures of effectiveness\n**(1) In general**\nAn eligible entity that implements a youth workforce readiness program under this Act shall\u2014\n**(A)**\nensure that the program is\u2014\n**(i)**\nbased upon an assessment of objective data regarding the need for such a program in the communities served; and\n**(ii)**\nevaluated on an established set of performance measures aimed at ensuring the availability of high-quality opportunities by measuring eligible youth success; and\n**(B)**\ncollect the data necessary for the measures of eligible youth success described in subparagraph (A)(ii).\n**(2) Measures**\nThe performance measures (including indicators) that will be used to evaluate the youth workforce readiness programs\u2014\n**(A)**\nshall be aligned with the regular academic program of the school of and the academic needs of participating eligible youth;\n**(B)**\nshall include performance measures that\u2014\n**(i)**\nare able to track the success (such as improvement over time) of eligible youth; and\n**(ii)**\ninclude assessment results and other indicators of eligible youth success, such as improved attendance during the school day, better classroom grades, regular (or consistent) program attendance, and on-time advancement to the next grade level; and\n**(C)**\nfor high school students, may include indicators such as achievement of career competencies, or successful completion of internships, apprenticeships, or work-based learning opportunities, or high school graduation.\n##### (b) Periodic evaluation\n**(1) In general**\nThe Secretary shall conduct a periodic evaluation of the eligible entity, to assess the progress of the entity's youth workforce readiness program toward ensuring high-quality opportunities by measuring eligible youth success.\n**(2) Use of results**\nThe results of evaluations under paragraph (1) shall be\u2014\n**(A)**\nused to refine, improve, and strengthen the program, and to refine the performance measures; and\n**(B)**\nused by the Secretary to determine whether a grant for a program is eligible to be renewed under section 4.\n##### (c) Reporting\nThe Secretary shall submit a report containing the results of the evaluation to the appropriate committees of Congress, and make the report available to the public.\n#### 9. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $100,000,000 for each of fiscal years 2026 through 2030.\n#### 10. Reestablishment of youth councils\n##### (a) Establishment\nSection 107 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3122 ) is amended by adding at the end the following:\n(j) Youth council (1) Establishment There shall be established, as a subgroup within each local board, a youth council appointed by the local board, in cooperation with the chief elected official for the local area. (2) Membership The membership of each youth council shall include representatives with special interest or professional expertise with youth workforce development programs, activities related to youth workforce readiness, youth workforce investment activities, local labor or joint labor-management organizations, and education related representatives\u2014 (A) membership may include\u2014 (i) members of the local board with special interest or expertise in youth workforce readiness or youth workforce development; (ii) local labor or joint labor-management organizations with a special interest or expertise in youth workforce readiness or youth workforce development; representatives of the workforce, in the local area, with a special interest or expertise in youth workforce readiness or youth workforce development; (iii) representatives of entities administering education and training activities, including career and technical education activities, in the local area, with special interest or expertise in youth workforce readiness or youth workforce development; (iv) representatives of youth service agencies, including juvenile justice, local law enforcement agencies, and representatives of local public housing authorities; (v) parents of eligible youth, and current or former youth program participants; (vi) representatives of vulnerable populations (including foster youth, minority youth, and youth with disabilities); (vii) community representatives, employers of eligible youth, and workplace learning advisors, with experience relating to youth workforce activities; and (viii) representatives of the Job Corps; and (B) may include such other individuals as the chairperson of the local board, in cooperation with the chief elected official, determines to be appropriate. (3) Relationship to local board Members of the youth council who are not otherwise members of the local board shall be voting members of the youth council and nonvoting members of the board. (4) Duties The duties of the youth council shall include\u2014 (A) representing the interests of youth before the local board; (B) collaborating with the local board to ensure programs address youth workforce development and youth workforce readiness; and (C) advising the local board on the inclusion and incorporation of the local youth workforce in decisions, as appropriate. .\n##### (b) State plans\nSection 102(b)(2)(C) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3112(b)(2)(C) ) is amended\u2014\n**(1)**\nin clause (vii), by striking and at the end;\n**(2)**\nby redesignating clause (viii) as clause (ix); and\n**(3)**\nby inserting after clause (vii) the following:\n(viii) how the local boards in the State are incorporating the recommendations of the youth councils within the local boards; and .\n##### (c) Local plans\nSection 108(b) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3123(b) ) is amended\u2014\n**(1)**\nin paragraph (21), by striking and at the end;\n**(2)**\nby redesignating paragraph (22) as paragraph (23); and\n**(3)**\nby inserting after paragraph (21) the following:\n(22) how the local board is incorporating the recommendations of the youth council within the local board; and .\n##### (d) Annual reports\nSection 116(d) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3141(d) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (K), by striking and at the end;\n**(B)**\nby redesignating subparagraph (L) as subparagraph (M); and\n**(C)**\nby inserting after subparagraph (K) the following:\n(L) information on the activities carried out in the State on the recommendation of youth councils in the State; and ; and\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A), by striking (L) and inserting (M) ;\n**(B)**\nin subparagraph (B), by striking and at the end;\n**(C)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(D)**\nby inserting after subparagraph (B) the following:\n(C) information on the activities carried out in the local area on the recommendation of the youth council within the local board; and .",
      "versionDate": "2025-04-14",
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
        "name": "Labor and Employment",
        "updateDate": "2025-05-22T21:10:55Z"
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
      "date": "2025-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2910ih.xml"
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
      "title": "Youth Workforce Readiness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Youth Workforce Readiness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a competitive grant program to support out-of-school-time youth workforce readiness programs, providing employability skills development, career exploration, employment readiness training, mentoring, work-based learning, and workforce opportunities for eligible youth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T06:48:22Z"
    }
  ]
}
```
