# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/299
- Title: Mentoring to Succeed Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 299
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-12-05T22:58:00Z
- Update date including text: 2025-12-05T22:58:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S482-484)
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S482-484)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/299",
    "number": "299",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
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
    "title": "Mentoring to Succeed Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:58:00Z",
    "updateDateIncludingText": "2025-12-05T22:58:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S482-484)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T17:56:42Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NJ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s299is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 299\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Durbin (for himself, Ms. Duckworth , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish a competitive grant program to support the establishment, expansion, or enhancement of youth mentoring programs for eligible youth, and to provide for social and emotional learning, employability skill development, career exploration, work-based learning, and other youth workforce opportunities.\n#### 1. Short title\nThis Act may be cited as the Mentoring to Succeed Act of 2025 .\n#### 2. Youth mentoring programs\n##### (a) In general\nSubtitle D of title I of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3221 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 172 as section 173; and\n**(2)**\nby inserting after section 171 the following:\n172. Youth mentoring programs (a) Purpose The purpose of this section is to make assistance available for mentoring programs for eligible youth, in order to\u2014 (1) establish, expand, or support mentoring programs; (2) assist eligible youth enrolled in secondary schools in developing cognitive and social-emotional skills; and (3) prepare eligible youth for success in high school, postsecondary education, and the workforce. (b) Definitions In this section: (1) Community-based organization The term community-based organization means a youth-serving private nonprofit organization (which may include a faith-based organization or may be an affiliate of a national organization) that\u2014 (A) is representative of a community or a significant segment of a community; (B) has demonstrated expertise and effectiveness in workforce development; and (C) has demonstrated expertise\u2014 (i) in the planning and delivery of education, training, and related activities that are included in a career pathway; (ii) in forging coordination and cooperation between educators and other members of the community; and (iii) in development and implementation of data systems that measure the progress of students and outcomes of career pathways. (2) Covered institution of higher education The term covered institution of higher education means\u2014 (A) an institution of higher education, as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ); or (B) a postsecondary vocational institution, as defined in section 102(c) of such Act ( 20 U.S.C. 1002(c) ). (3) Covered partnership The term covered partnership means a partnership between\u2014 (A) a community-based organization; and (B) (i) an industry or sector partnership; (ii) a local educational agency; or (iii) another public entity or private employer, as appropriate. (4) Covered recognized postsecondary credential The term covered recognized postsecondary credential means a recognized postsecondary credential issued by a covered institution of higher education. (5) Disability The term disability has the meaning given the term for purposes of section 602(3) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401(3) ). (6) Eligible entity The term eligible entity means a community-based organization or covered partnership that\u2014 (A) provides mentoring services; and (B) provides youth workforce readiness programming and career exploration. (7) Eligible youth The term eligible youth means\u2014 (A) an in-school youth; (B) a youth who meets all requirements to be an in-school youth, except that\u2014 (i) in lieu of meeting the requirements of section 129(a)(1)(C)(ii), the youth is in secondary school; or (ii) in lieu of meeting the requirements of section 129(a)(1)(C)(iv), the youth\u2014 (I) is failing academically or at risk of dropping out of school, is chronically absent, is enrolled in fewer classes or for fewer credit hours than a typical full-time student, has changed schools 3 or more times in the past 180 days, or has a history of multiple suspensions; or (II) (aa) is a gang member or resides in a community with high rates of, and prevalence of risk factors associated with, violence-related injuries and deaths, and with other relevant health and safety risks (including high rates of poverty, suicide, or substance use disorder (including opioid use disorder)) or has a parent or guardian who is struggling with substance use disorder; (bb) has 1 or both parents incarcerated; or (cc) has experienced 1 or more adverse childhood experiences, traumatic events, or toxic stressors, as assessed through an evidence-based screening; (C) an out-of-school youth; or (D) a youth who meets all requirements to be an out-of-school youth, except that\u2014 (i) in lieu of meeting the requirements of section 129(a)(1)(B)(ii), the youth would be placed in secondary school if the youth were attending school; or (ii) in lieu of meeting the requirements of section 129(a)(1)(B)(iii), the youth is described in subparagraph (B)(ii)(II). (8) Mentoring The term mentoring means a structured, managed activity\u2014 (A) in which eligible youth are appropriately matched with screened and trained adult or peer volunteer mentors for consistent relationships; (B) that provides direct one-on-one, group, or peer mentoring services that focus on\u2014 (i) providing enrichment; (ii) promoting educational or workforce success; (iii) minimizing risk behaviors; (iv) promoting social skills and healthy relationships; or (v) any combination of objectives described in clauses (i) through (iv); (C) that involves meetings, events, and activities on a regular basis, for a period of not less than 1 year; and (D) that is intended to meet, in part, the social and emotional development needs of an eligible youth, the need of the eligible youth for involvement with a caring and supportive adult, and the need of the eligible youth for positive role models, connections, and stability. (9) High school The term high school has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ). (10) Youth workforce readiness programming The term youth workforce readiness programming means job training, or a workforce development program providing an employment and training activity, such as mentoring, an activity to promote communication and problem-solving skills, career exploration, a job readiness activity and certification, a summer job, or a year-round job opportunity or apprenticeship, provided to eligible youth. (c) Program authorized (1) In general From amounts made available for this section, the Secretary shall award grants, on a competitive basis, to eligible entities to establish, expand, or support mentoring programs in accordance with subsection (d). (2) Duration A grant awarded under this section shall be for a period not to exceed 3 years. (d) Authorized activities (1) In general An eligible entity receiving a grant under this section shall use grant funds to establish, expand, or support not less than 1 mentoring program that\u2014 (A) is designed to assist eligible youth in developing cognitive and social-emotional skills to prepare the eligible youth for success in high school, postsecondary education, and the workforce by linking the eligible youth with mentors who\u2014 (i) have received mentor training, including training on trauma-informed practices, youth engagement, cultural competency, and social-emotional learning; and (ii) have been screened using appropriate reference checks and criminal background checks, in accordance with the requirements of subsection (e)(2)(F)(ii); (B) serves a population that includes eligible youth living in or from underserved communities or communities with employment disparities; (C) provides coaching and technical assistance to mentors participating in the mentoring program; (D) seeks to\u2014 (i) reduce juvenile justice involvement of eligible youth; (ii) foster positive relationships between eligible youth and their peers, other adults, and family members; (iii) develop the workforce readiness skills of eligible youth by exploring paths to employment, including encouraging students with disabilities to explore transition services; and (iv) increase the participation of eligible youth in community service activities; (E) encourages eligible youth to set goals and plan for their futures, including making plans and identifying goals for postsecondary education and participation in the workforce; (F) develops and carries out regular training for mentors, including training on\u2014 (i) the impact of adverse childhood experiences; (ii) trauma-informed practices and interventions; (iii) cultural competency; (iv) social and emotional learning; (v) positive youth development and engagement practices; and (vi) disability inclusion practices to ensure access and participation by students with disabilities; (G) works in coordination with a private employer and a local educational agency with not less than 1 high-need school (as defined in section 2211(b) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6631(b) ); (H) recruits, screens, matches, trains, and, as necessary, compensates mentors; (I) hires staff, as necessary, to perform or support the objectives of the program; and (J) provides inclusive and accessible youth engagement activities, such as\u2014 (i) career awareness activities, including job site visits, informational interviews, resume writing, interview preparation, and networking; (ii) academic or postsecondary education preparation activities, including trade or vocational school visits, visits to institutions of higher education, and assistance in applying to institutions of higher education; (iii) support for the use of career pathways; (iv) paid and unpaid work experiences that have as a component academic and occupational education, which may include\u2014 (I) paid employment opportunities; (II) pre-apprenticeship programs and apprenticeship programs; (III) paid internships; (IV) job shadowing; and (V) on-the-job training opportunities; (v) work-based learning (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 )) that provides opportunities for the application of employability skills and hands-on work experiences through partnerships among eligible entities; (vi) occupational skill training, which shall include priority consideration for training programs that lead to covered recognized postsecondary credentials that are aligned with in-demand industry sectors or occupations in the local area involved, if the local board determines that the programs meet the quality criteria described in section 123(a); (vii) activities that help youth prepare for and transition to postsecondary education and training; and (viii) services to help prepare eligible youth for the workforce, such as\u2014 (I) leadership development opportunities; (II) workforce or workforce readiness opportunities; (III) financial literacy education; (IV) entrepreneurial skills training; (V) services that provide labor market and employment information about in-demand industry sectors or occupations available in the local area; (VI) activities to develop fundamental workforce readiness skills or to develop employability skills (such as communication, creativity, collaboration, and critical thinking) that support social-emotional development through every developmental stage; and (VII) career exposure offered by local industry or sector partnerships to provide career assessments, education, and career planning. (2) Additional activities An eligible entity receiving a grant under this section may use grant funds to\u2014 (A) provide professional development (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 )) for training educators and other providers of educational services who participate in the mentoring program; (B) develop assets and resources that assist an employer or groups of employers or sectors in working with eligible youth; (C) in the case of an eligible entity that seeks to implement the program through a partnership with another eligible entity, establish the partnership; and (D) conduct program evaluation, including acquiring and analyzing the data described in subsection (g). (3) Subgrants An eligible entity receiving a grant under this section may, with the approval of the Secretary, use grant funds to award subgrants to eligible organizations to carry out activities described in paragraphs (1) and (2). (e) Application An eligible entity desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and accompanied by such information as the Secretary may require, including\u2014 (1) a needs assessment that includes baseline data on the measures described in subsection (g)(1)(B); and (2) a plan to establish, expand, or support a mentoring program that meets the requirements of subsection (d)(1), including\u2014 (A) the targeted outcomes, mentor type, and meeting frequency for the program; (B) a description of and data regarding the eligible youth who will participate as mentees in the program, including\u2014 (i) any age ranges to be served or any other eligibility criteria; and (ii) how the eligible entity will ensure that the program serves eligible youth living in or from underserved communities or communities with employment disparities, in accordance with subsection (d)(1)(B); (C) the number of mentor-mentee matches proposed to be established and maintained annually under the program; (D) the capacity and expertise of the program to serve eligible youth in a way that is responsive to children and youth of color, expectant and parenting youth, indigenous youth, youth who are lesbian, gay, bisexual, transgender, or queer, and youth with disabilities; (E) actions taken to ensure that the design of the program reflects input from eligible youth; (F) an assurance that mentors supported under the program are appropriately screened and have demonstrated a willingness to comply with aspects of the mentoring program, including\u2014 (i) a written screening plan that includes all of the policies and procedures used to screen and select mentors, including eligibility requirements and preferences for such applicants; (ii) a description of the methods to be used to conduct criminal background checks on all prospective mentors and the methods in place to exclude mentors with convictions directly related to child safety that occur during the mentor\u2019s participation in the program or in the 7-year period preceding the mentor\u2019s participation; and (iii) a description of the methods to be used to ensure that the mentors are willing and able to serve as a mentor on a long-term, consistent basis as defined in the application; (G) a description of\u2014 (i) the community-based organizations or the covered partnerships through which the eligible entity will implement the program; and (ii) if a covered partnership will assist in implementing the program, the collaboration and coordination that the community-based organization in the partnership has carried out or will carry out with other entities in the partnership, related to that implementation; (H) in the case of a program that includes an opportunity to earn a covered recognized postsecondary credential, a description of the activities leading to the covered recognized postsecondary credential; and (I) a budget detailing program activities and administrative costs. (f) Priority In awarding grants under this section, the Secretary shall give priority to eligible entities that\u2014 (1) prior to receiving a grant, serve eligible youth with the greatest need who reside in\u2014 (A) a high-poverty community; (B) a rural area; or (C) a community with high rates of, and prevalence of risk factors associated with, violence-related injuries and deaths, and with other relevant health and safety risks (including high rates of poverty, suicide, or substance use disorder (including opioid use disorder)); (2) provide eligible youth participating in the mentoring program supported under this section with opportunities for postsecondary education preparation and career development, including\u2014 (A) job training, professional development, work shadowing, internships, networking, resume writing and review, interview preparation, transition or vocational rehabilitation services for students with disabilities, application assistance and visits to institutions of higher education, and leadership development through community service, and relevant program elements described in section 129(c)(2)); and (B) partnerships with the private sector and local businesses to provide internship and career exploration activities and resources; and (3) consult and engage eligible youth in the development, design, and implementation of the mentoring program, including by demonstrating such consultation and engagement in the application submitted under subsection (e) and agreeing to continue such consultation after receiving the grant. (g) Reporting requirements (1) In general Not later than 180 days after the end of each year of the grant period, an eligible entity receiving a grant under this section shall submit to the Secretary a report that\u2014 (A) includes\u2014 (i) the number of eligible youth and mentors, and the demographics of eligible youth and mentors, who participated in the mentoring program that was supported with grant funds; (ii) data on the academic achievement, dropout rates, truancy, absenteeism, outcomes of arrests for violent crime, full-time employment, part-time employment, and postsecondary education enrollment of eligible youth participating in the program; and (iii) data on social-emotional development of eligible youth participating in the program, as assessed with a validated social-emotional assessment tool; (B) may include indicators such as achievement of career competencies, or successful completion of internships, apprenticeships, or work-based learning opportunities, or high school graduation; and (C) includes any other information that the Secretary may require to evaluate the success of the mentoring program. (2) Student privacy An eligible entity shall ensure that the report submitted under paragraph (1) is prepared in a manner that protects the privacy rights of each eligible youth in the same manner as is required for students under section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g ; commonly known as the Family Educational Rights and Privacy Act of 1974 ). (h) Mentoring program resources and technical assistance The Secretary shall work with the Administrator of the Office of Juvenile Justice and Delinquency Prevention and the Secretary of Education to\u2014 (1) refer eligible entities receiving grants under this section to the National Mentoring Resource Center to obtain resources on best practices and research related to mentoring programs and to request no-cost training and technical assistance; and (2) provide such eligible entities with information regarding transitional services for eligible youth returning from correctional facilities and transition services for students with disabilities. (i) Authorization of appropriations There are authorized to be appropriated to carry out this section such sums as may be necessary for each of fiscal years 2026 through 2030. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Workforce Innovation and Opportunity Act is amended by striking the item relating to section 172 and inserting the following:\nSec. 172. Youth mentoring programs. Sec. 173. Authorization of appropriations. .\n#### 3. Study on mentoring programs\n##### (a) In general\nThe Secretary of Labor, acting through the Chief Evaluation Officer of the Department of Labor, shall conduct a study to\u2014\n**(1)**\nidentify successful mentoring programs and evidence-based strategies for administering and monitoring such programs;\n**(2)**\nevaluate the role of mentors in promoting cognitive development and social-emotional learning to enhance academic achievement and to improve workforce readiness; and\n**(3)**\nevaluate the effectiveness of the grant program under section 172 of the Workforce Innovation and Opportunity Act, as added by section 2, on student academic outcomes and youth career development.\n##### (b) Timing\nNot later than 3 years after the date of enactment of this Act, the Secretary of Labor, acting through the Chief Evaluation Officer, shall submit the results of the study to the appropriate congressional committees.",
      "versionDate": "2025-01-29",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "811",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Mentoring to Succeed Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Community life and organization",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Education of the disadvantaged",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Educational guidance",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-25T17:51:19Z"
          },
          {
            "name": "Youth employment and child labor",
            "updateDate": "2025-03-25T17:51:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-07T16:01:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
    "originChamber": "Senate",
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
          "measure-id": "id119s299",
          "measure-number": "299",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s299v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Mentoring to Succeed Act of 2025</strong></p><p>This bill establishes grants to support mentoring programs for eligible youth (e.g., in-school youth, out-of-school youth, or youth who are failing academically or who meet specified criteria).\u00a0</p><p>Specifically, the bill directs the Department of Labor to award competitive grants for certain community-based organizations or partnerships involving community-based organizations to (1) establish, expand, or support mentoring programs; (2) assist eligible youth enrolled in secondary schools in developing cognitive and social-emotional skills; and (3) prepare eligible youth for success in high school, postsecondary education, and the workforce.</p><p>Additionally, Labor must work with the Department of Justice's Office of Juvenile Justice and Delinquency Prevention and the Department of Education to (1) refer grant recipients to the National Mentoring Resource Center to obtain mentoring resources, and (2) provide grant recipients with information regarding transitional services for eligible youth returning from correctional facilities and transition services for students with disabilities.</p><p>The bill also requires Labor's Chief Evaluation Office to study and report on mentoring programs.</p>"
        },
        "title": "Mentoring to Succeed Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s299.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Mentoring to Succeed Act of 2025</strong></p><p>This bill establishes grants to support mentoring programs for eligible youth (e.g., in-school youth, out-of-school youth, or youth who are failing academically or who meet specified criteria).\u00a0</p><p>Specifically, the bill directs the Department of Labor to award competitive grants for certain community-based organizations or partnerships involving community-based organizations to (1) establish, expand, or support mentoring programs; (2) assist eligible youth enrolled in secondary schools in developing cognitive and social-emotional skills; and (3) prepare eligible youth for success in high school, postsecondary education, and the workforce.</p><p>Additionally, Labor must work with the Department of Justice's Office of Juvenile Justice and Delinquency Prevention and the Department of Education to (1) refer grant recipients to the National Mentoring Resource Center to obtain mentoring resources, and (2) provide grant recipients with information regarding transitional services for eligible youth returning from correctional facilities and transition services for students with disabilities.</p><p>The bill also requires Labor's Chief Evaluation Office to study and report on mentoring programs.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s299"
    },
    "title": "Mentoring to Succeed Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Mentoring to Succeed Act of 2025</strong></p><p>This bill establishes grants to support mentoring programs for eligible youth (e.g., in-school youth, out-of-school youth, or youth who are failing academically or who meet specified criteria).\u00a0</p><p>Specifically, the bill directs the Department of Labor to award competitive grants for certain community-based organizations or partnerships involving community-based organizations to (1) establish, expand, or support mentoring programs; (2) assist eligible youth enrolled in secondary schools in developing cognitive and social-emotional skills; and (3) prepare eligible youth for success in high school, postsecondary education, and the workforce.</p><p>Additionally, Labor must work with the Department of Justice's Office of Juvenile Justice and Delinquency Prevention and the Department of Education to (1) refer grant recipients to the National Mentoring Resource Center to obtain mentoring resources, and (2) provide grant recipients with information regarding transitional services for eligible youth returning from correctional facilities and transition services for students with disabilities.</p><p>The bill also requires Labor's Chief Evaluation Office to study and report on mentoring programs.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119s299"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s299is.xml"
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
      "title": "Mentoring to Succeed Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mentoring to Succeed Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a competitive grant program to support the establishment, expansion, or enhancement of youth mentoring programs for eligible youth, and to provide for social and emotional learning, employability skill development, career exploration, work-based learning, and other youth workforce opportunities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:30Z"
    }
  ]
}
```
