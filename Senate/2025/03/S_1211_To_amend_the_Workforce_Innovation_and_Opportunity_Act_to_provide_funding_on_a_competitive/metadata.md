# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1211?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1211
- Title: AID Youth Employment Act
- Congress: 119
- Bill type: S
- Bill number: 1211
- Origin chamber: Senate
- Introduced date: 2025-03-31
- Update date: 2026-04-13T14:38:32Z
- Update date including text: 2026-04-13T14:38:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in Senate
- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1926-1930)
- Latest action: 2025-03-31: Introduced in Senate

## Actions

- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1926-1930)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1211",
    "number": "1211",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
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
    "title": "AID Youth Employment Act",
    "type": "S",
    "updateDate": "2026-04-13T14:38:32Z",
    "updateDateIncludingText": "2026-04-13T14:38:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1926-1930)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T21:52:19Z",
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
      "sponsorshipDate": "2025-03-31",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1211is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1211\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Mr. Durbin (for himself and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to provide funding, on a competitive basis, for summer and year-round employment opportunities for youth ages 14 through 24.\n#### 1. Short title\nThis Act may be cited as the Assisting In Developing Youth Employment Act or the AID Youth Employment Act .\n#### 2. Youth employment opportunities\nTitle I of the Workforce Innovation and Opportunity Act is amended\u2014\n**(1)**\nby redesignating subtitle E ( 29 U.S.C. 3241 et seq. ) as subtitle F; and\n**(2)**\nby inserting after subtitle D ( 29 U.S.C. 3221 et seq. ) the following:\nE Youth Employment Opportunities 176. Definitions In this subtitle: (1) Eligible youth The term eligible youth means an individual who\u2014 (A) is not younger than age 14 or older than age 24; and (B) is\u2014 (i) an in-school youth; (ii) an out-of-school youth; or (iii) an unemployed individual. (2) Indian tribe; tribal organization The terms Indian tribe and tribal organization have the meanings given the terms in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (3) In-school youth; out-of-school youth The terms in-school youth and out-of-school youth have the meanings given the terms in section 129(a)(1). (4) Institution of higher education The term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ). (5) Marginalized The term marginalized , used with respect to an individual, includes individuals who are homeless, in foster care, involved in the juvenile or criminal justice system, or are not enrolled in or are at risk of dropping out of an educational institution and who live in an underserved community that has faced trauma through acute or long-term exposure to substantial discrimination, historical or cultural oppression, intergenerational poverty, civil unrest, a high rate of violence, or a high rate of drug overdose mortality. (6) Subsidized employment The term subsidized employment means employment for which the employer receives a total or partial subsidy to offset costs of employing an eligible youth under this subtitle. (7) Tribal area The term tribal area means\u2014 (A) an area on or adjacent to an Indian reservation; (B) land held in trust by the United States for Indians; (C) a public domain Indian allotment; (D) a former Indian reservation in Oklahoma; and (E) land held by an incorporated Native group, Regional Corporation, or Village Corporation under the provisions of the Alaska Native Claims Settlement Act ( 43 U.S.C. 1601 et seq. ). (8) Tribal college or university The term tribal college or university has the meaning given the term Tribal College or University in section 316(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059c(b) ). (9) Tribally designated housing entity The term tribally designated housing entity , used with respect to an Indian tribe (as defined in this section), has the meaning given in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ). 176A. Allocation of funds (a) Allocation Of the funds appropriated under section 176E that remain available after any reservation under subsection (b), the Secretary may make available\u2014 (1) not more than $1,800,000,000 in accordance with section 176B to provide eligible youth with subsidized summer employment opportunities; and (2) not more than $2,400,000,000 in accordance with section 176C to provide eligible youth with subsidized year-round employment opportunities. (b) Reservation The Secretary may reserve not more than 10 percent of the funds appropriated under section 176E to provide technical assistance and oversight, in order to assist eligible entities in applying for and administering grants awarded under this subtitle. 176B. Summer employment competitive grant program (a) In general (1) Grants Using the amounts made available under 176A(a)(1), the Secretary shall award, on a competitive basis, planning and implementation grants. (2) General use of funds The Secretary shall award the grants to assist eligible entities by paying for the program share of the cost of\u2014 (A) in the case of a planning grant, planning a summer youth employment program to provide subsidized summer employment opportunities; and (B) in the case of an implementation grant, implementation of such a program, to provide such opportunities. (b) Periods and amounts of grants (1) Planning grants The Secretary may award a planning grant under this section for a 1-year period, in an amount of not more than $250,000. (2) Implementation grants The Secretary may award an implementation grant under this section for a 3-year period, in an amount of not more than $6,000,000. (c) Eligible entities (1) In general To be eligible to receive a planning or implementation grant under this section, an entity shall\u2014 (A) be a\u2014 (i) State, local government, or Indian tribe or tribal organization, that meets the requirements of paragraph (2); or (ii) community-based organization that meets the requirements of paragraph (3); and (B) meet the requirements for a planning or implementation grant, respectively, specified in paragraph (4). (2) Government partnerships An entity that is a State, local government, or Indian tribe or tribal organization referred to in paragraph (1)(A)(i) shall demonstrate that the entity has entered into a partnership with State, local, or tribal entities\u2014 (A) that shall include\u2014 (i) a local educational agency or tribal educational agency (as defined in section 6132 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7452 )); (ii) a local board or tribal workforce development agency; (iii) a State, local, or tribal agency serving youth under the jurisdiction of the juvenile justice system or criminal justice system; (iv) a State, local, or tribal child welfare agency; (v) a State, local, or tribal agency or community-based organization, with\u2014 (I) expertise in providing counseling services and trauma-informed and gender-responsive trauma prevention, identification, referral, and support (including treatment) services; and (II) a proven track record of serving low-income, vulnerable youth and out-of-school youth; (vi) if the State, local government, or Indian tribe or tribal organization is seeking an implementation grant and has not established a summer youth employment program, an entity that is carrying out a State, local, or tribal summer youth employment program; and (vii) an employer or employer association; and (B) that may include\u2014 (i) an institution of higher education or tribal college or university; (ii) a representative of a labor or labor-management organization; (iii) an entity that carries out a program that receives funding under the Juvenile Justice and Delinquency Prevention Act of 1974 ( 34 U.S.C. 11101 et seq. ); (iv) a collaborative applicant as defined in section 401 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 ) or a private nonprofit organization that serves homeless individuals and households (including such an applicant or organization that serves individuals or households that are at risk of homelessness in tribal areas) or serves foster youth; (v) an entity that carries out a program funded under the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ), including Native American programs funded under section 116 of that Act ( 20 U.S.C. 2326 ) and tribally controlled postsecondary career and technical institution programs funded under section 117 of that Act ( 20 U.S.C. 2327 ); (vi) a local or tribal youth committee; (vii) a State or local public housing agency or a tribally designated housing entity; and (viii) another appropriate State, local, or tribal agency. (3) Community-based organization partnerships A community-based organization referred to in paragraph (1)(A)(ii) shall demonstrate that the organization has entered into a partnership with State, local, or tribal entities\u2014 (A) that shall include\u2014 (i) a unit of general local government or tribal government; (ii) an agency described in paragraph (2)(A)(i); (iii) a local board or tribal workforce development agency; (iv) a State, local, or tribal agency serving youth under the jurisdiction of the juvenile justice system or criminal justice system; (v) a State, local, or tribal child welfare agency; (vi) if the organization is seeking an implementation grant and has not established a summer youth employment program, an entity that is carrying out a State, local, or tribal summer youth employment program; and (vii) an employer or employer association; and (B) that may include one or more entities described in paragraph (2)(B). (4) Entities eligible for particular grants (A) Entities eligible for planning grants The Secretary may award a planning grant under this section to an eligible entity that\u2014 (i) is preparing to establish or expand a summer youth employment program that meets the minimum requirements specified in subsection (d)(1)(B)(iv); and (ii) has not received a grant under this section. (B) Entities eligible for implementation grants (i) In general The Secretary may award an implementation grant under this section to an eligible entity that\u2014 (I) has received a planning grant under this section; or (II) has established a summer youth employment program and demonstrates a minimum level of capacity to enhance or expand the summer youth employment program described in the application submitted under subsection (d). (ii) Capacity In determining whether an entity has the level of capacity referred to in clause (i)(II), the Secretary may include as capacity\u2014 (I) the entity's staff capacity and staff training to deliver youth employment services; and (II) the entity's existing youth employment services (as of the date of submission of the application submitted under subsection (d)) that are consistent with the application. (d) Application (1) In general Except as provided in paragraph (2), an eligible entity desiring to receive a grant under this section for a summer youth employment program shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including, at a minimum, each of the following: (A) With respect to an application for a planning or implementation grant\u2014 (i) a description of the eligible youth for whom summer employment services will be provided; (ii) a description of the eligible entity, and a description of the expected participation and responsibilities of each of the partners in the partnership described in subsection (c); (iii) information demonstrating sufficient need for the grant in the State, local, or tribal population, which may include information showing\u2014 (I) a high level of unemployment among youth (including young adults) ages 14 through 24; (II) a high rate of out-of-school youth; (III) a high rate of homelessness; (IV) a high rate of poverty; (V) a high rate of adult unemployment; (VI) a high rate of community or neighborhood crime; (VII) a high rate of violence; or (VIII) a high level or rate on another indicator of need; (iv) a description of the strategic objectives the eligible entity seeks to achieve through the program to provide eligible youth with core work readiness skills, which may include\u2014 (I) financial literacy skills, including providing the support described in section 129(b)(2)(D); (II) sector-based technical skills aligned with employer needs; (III) skills that\u2014 (aa) are soft employment skills, early work skills, or work readiness skills; and (bb) include social skills, communications skills, higher-order thinking skills, self-control, and positive self-concept; and (IV) (for the marginalized eligible youth) basic skills like communication, math, and problem solving in the context of training for advancement to better jobs and postsecondary training; and (v) information demonstrating that the eligible entity has obtained commitments to provide the non-program share described in paragraph (2) of subsection (h). (B) With respect to an application for a planning grant\u2014 (i) a description of the intermediate and long-term goals for planning activities for the duration of the planning grant; (ii) a description of how grant funds will be used to develop a plan to provide summer employment services for eligible youth; (iii) a description of how the eligible entity will carry out an analysis of best practices for identifying, recruiting, and engaging program participants, in particular the marginalized eligible youth; (iv) a description of how the eligible entity will carry out an analysis of best practices for placing youth participants\u2014 (I) in opportunities that\u2014 (aa) are appropriate, subsidized employment opportunities with employers based on factors including age, skill, experience, career aspirations, work-based readiness, and barriers to employment; and (bb) may include additional services for participants, including core work readiness skill development and mentorship services; (II) in summer employment that\u2014 (aa) is not less than 6 weeks; (bb) follows a schedule of not more than 20 hours per week; (cc) pays wages at rates not less than the applicable Federal, State, or local minimum wage rate; and (dd) for employment involving construction, pays wages at rates not less than those previously on similar construction in the locality as determined by the Secretary in accordance with subchapter IV of chapter 31 of title 40, United States Code (commonly known as the Davis-Bacon Act ); and (v) a description of how the eligible entity plans to develop a mentorship program or connect youth with positive, supportive mentorships, consistent with paragraph (3). (C) With respect to an application for an implementation grant\u2014 (i) a description of how the eligible entity plans to identify, recruit, and engage program participants, in particular the marginalized eligible youth; (ii) a description of the manner in which the eligible entity plans to place eligible youth participants in subsidized employment opportunities, and in summer employment, described in subparagraph (B)(iv); (iii) (for a program serving the marginalized eligible youth) a description of workplaces for the subsidized employment involved, which may include workplaces in the public, private, and nonprofit sectors; (iv) a description of how the eligible entity plans to provide or connect eligible youth participants with positive, supportive mentorships, consistent with paragraph (3); (v) a description of services that will be available to employers participating in the youth employment program, to provide supervisors involved in the program with coaching and mentoring on\u2014 (I) how to support youth development; (II) how to structure learning and reflection; and (III) how to deal with youth challenges in the workplace; (vi) a description of how the eligible entity plans to offer structured pathways back into employment and a youth employment program under this section for eligible youth who have been terminated from employment or removed from the program; (vii) a description of how the eligible entity plans to engage eligible youth beyond the duration of the summer employment opportunity, which may include\u2014 (I) developing or partnering with a year-round youth employment program; (II) referring eligible youth to other year-round programs, which may include\u2014 (aa) programs funded under section 176C or the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ); (bb) after school programs; (cc) secondary or postsecondary education programs; (dd) training programs; (ee) cognitive behavior therapy programs; (ff) apprenticeship programs; and (gg) national service programs; (III) employing a full-time, permanent staff person who is responsible for youth outreach, followup, and recruitment; or (IV) connecting eligible youth with job development services, including career counseling, resume and job application assistance, interview preparation, and connections to job leads; (viii) evidence of the eligible entity's capacity to provide the services described in this subsection; and (ix) a description of the quality of the summer youth employment program, including a program that leads to a recognized postsecondary credential. (2) Indian tribe; tribal organizations An eligible entity that is an Indian tribe or tribal organization and desires to receive a grant under this section for a summer youth employment program may, in lieu of submitting the application described in paragraph (1), submit an application to the Secretary that meets such requirements as the Secretary develops after consultation with the tribe or organization. (3) Mentor For purposes of subparagraphs (B)(iv), (B)(v), and (C)(iv) of paragraph (1), a mentor\u2014 (A) shall be an individual who has been matched with an eligible youth based on the youth's needs; (B) shall make contact with the eligible youth at least once each week; (C) shall be a trusted member of the local community; and (D) may include\u2014 (i) a mentor trained in trauma-informed care (including provision of trauma-informed trauma prevention, identification, referral, or support services to youth that have experienced or are at risk of experiencing trauma), conflict resolution, and positive youth development; (ii) a job coach trained to provide youth with guidance on how to navigate the workplace and troubleshoot problems; (iii) a supervisor trained to provide at least two performance assessments and serve as a reference; or (iv) a peer mentor who is a former or current participant in the youth employment program involved. (e) Awards for populations and areas (1) Populations The Secretary shall reserve, from the amounts made available under section 176A(a)(1)\u2014 (A) 50 percent to award grants under this section for planning or provision of subsidized summer employment opportunities for eligible youth who are in-school youth; and (B) 50 percent to award such grants to plan for planning or provision of such opportunities for eligible youth who are out-of-school youth or unemployed individuals. (2) Areas (A) In general In awarding the grants, the Secretary shall consider the regional diversity of the areas to be served, to ensure that urban, suburban, rural, and tribal areas are receiving grant funds. (B) Rural and tribal area inclusion (i) Rural areas Not less than 20 percent of the amounts made available under section 176A(a)(1) for each fiscal year shall be made available for activities to be carried out in rural areas. (ii) Tribal areas Not less than 5 percent of the amounts made available under section 176A(a)(1) for each fiscal year shall be made available for activities to be carried out in tribal areas. (f) Program priorities In allocating funds under this section, the Secretary shall give priority to eligible entities\u2014 (1) who propose to coordinate their activities\u2014 (A) with local or tribal employers; and (B) with agencies described in subsection (c)(2)(A)(i) to ensure the summer youth employment programs provide clear linkages to remedial, academic, and occupational programs carried out by the agencies; (2) who propose a plan to increase private sector engagement in, and job placement through, summer youth employment; and (3) who have, in their counties, States, or tribal areas (as compared to other counties in their State, other States, or other tribal areas, respectively), a high level or rate described in subsection (d)(1)(A)(iii). (g) Use of funds (1) In general An eligible entity that receives a grant under this section may use the grant funds for services described in subsection (d). (2) Discretionary uses The eligible entity may also use the funds\u2014 (A) to provide wages to eligible youth in subsidized summer employment programs; (B) to provide eligible youth with support services, including case management, child care assistance, child support services, and transportation assistance; and (C) to develop data management systems to assist with programming, evaluation, and records management. (3) Administration An eligible entity may reserve not more than 10 percent of the grant funds for the administration of activities under this section. (4) Carry-over authority Any amounts provided to an eligible entity under this section for a fiscal year may, at the discretion of the Secretary, remain available to that entity for expenditure during the succeeding fiscal year to carry out programs under this section. (h) Program share (1) Planning grants The program share for a planning grant awarded under this section shall be 100 percent of the cost described in subsection (a)(2)(A). (2) Implementation grants (A) In general The program share for an implementation grant awarded under this section shall be 50 percent of the cost described in subsection (a)(2)(B). (B) Exception Notwithstanding subparagraph (A), the Secretary\u2014 (i) may increase the program share for an eligible entity; and (ii) shall increase the program share for an Indian tribe or tribal organization to not less than 95 percent of the cost described in subsection (a)(2)(B). (C) Non-program share The eligible entity may provide the non-program share of the cost\u2014 (i) in cash or in kind, fairly evaluated, including plant, equipment, or services; and (ii) from State, local, tribal or private (including philanthropic) sources and, in the case of an Indian tribe or tribal organization, from Federal sources. 176C. Year-round employment competitive grant program (a) In general (1) Grants Using the amounts made available under 176A(a)(2), the Secretary shall award, on a competitive basis, planning and implementation grants. (2) General use of funds The Secretary shall award the grants to assist eligible entities by paying for the program share of the cost of\u2014 (A) in the case of a planning grant, planning a year-round youth employment program to provide subsidized year-round employment opportunities; and (B) in the case of an implementation grant, implementation of such a program to provide such opportunities. (b) Periods and amounts of grants The planning grants shall have the periods and amounts described in section 176B(b)(1). The implementation grants shall have the periods and grants described in section 176B(b)(2). (c) Eligible entities (1) In general To be eligible to receive a planning or implementation grant under this section, an entity shall, except as provided in paragraph (2)\u2014 (A) be a\u2014 (i) State, local government, or Indian tribe or tribal organization, that meets the requirements of section 176B(c)(2); or (ii) community-based organization that meets the requirements of section 176B(c)(3); and (B) meet the requirements for a planning or implementation grant, respectively, specified in section 176B(c)(4). (2) Year-round youth employment programs For purposes of paragraph (1), any reference in section 176B(c)\u2014 (A) to a summer youth employment program shall be considered to refer to a year-round youth employment program; and (B) to a provision of section 176B shall be considered to refer to the corresponding provision of this section. (d) Application (1) In general Except as provided in paragraph (2), an eligible entity desiring to receive a grant under this section for a year-round youth employment program shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including, at a minimum, each of the following: (A) With respect to an application for a planning or implementation grant, the information and descriptions specified in section 176B(d)(1)(A). (B) With respect to an application for a planning grant, the descriptions specified in section 176B(d)(1)(B), except that the description of an analysis for placing youth in employment described in clause (iv)(II)(bb) of that section shall cover employment that follows a schedule\u2014 (i) that consists of\u2014 (I) not more than 15 hours per week for in-school youth; and (II) not less than 20 and not more than 40 hours per week for out-of-school youth; and (ii) that depends on the needs and work-readiness level of the population being served. (C) With respect to an application for an implementation grant, the descriptions and evidence specified in section 176B(d)(1)(C)\u2014 (i) except that the reference in section 176B(d)(1)(C)(ii) to employment described in section 176B(d)(1)(B) shall cover employment that follows the schedule described in subparagraph (B); and (ii) except that the reference to programs in clause (vii)(II)(aa) of that section shall be considered to refer only to programs funded under the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ). (D) With respect to an application for an implementation grant\u2014 (i) a description of how the eligible entity plans to provide mental health services, as needed, to eligible youth participants; and (ii) a description of how the eligible entity plans to address barriers to participation among eligible youth, including provding transportation and child care. (2) Indian tribe; tribal organizations An eligible entity that is an Indian tribe or tribal organization and desires to receive a grant under this section for a year-round youth employment program may, in lieu of submitting the application described in paragraph (1), submit an application to the Secretary that meets such requirements as the Secretary develops after consultation with the tribe or organization. (3) Mentor For purposes of paragraph (1), any reference in subparagraphs (B)(iv), (B)(v), and (C)(iv) of section 176B(d)(1) to a mentor shall be considered to refer to a mentor who\u2014 (A) shall be an individual described in subparagraphs (A) and (C) of section 176B(d)(3); (B) shall make contact with the eligible youth at least twice each week; and (C) may be an individual described in section 176B(d)(3)(D). (4) Year-round employment For purposes of this subsection, any reference in section 176B(d)\u2014 (A) to summer employment shall be considered to refer to year-round employment; and (B) to a provision of section 176B shall be considered to refer to the corresponding provision of this section. (e) Awards for populations and areas; Priorities (1) Populations The Secretary shall reserve, from the amounts made available under section 176A(a)(2)\u2014 (A) 50 percent to award grants under this section for planning or provision of subsidized year-round employment opportunities for eligible youth who are in-school youth; and (B) 50 percent to award such grants to plan for planning or provision of such opportunities for eligible youth who are out-of-school youth or unemployed individuals. (2) Areas; priorities In awarding the grants, the Secretary shall\u2014 (A) carry out section 176B(e)(2); and (B) give priority to eligible entities\u2014 (i) who\u2014 (I) propose the coordination and plan described paragraphs (1) and (2) of section 176B(f), with respect to year-round youth employment; and (II) meet the requirements of section 176B(f)(3); or (ii) who\u2014 (I) propose a plan to coordinate activities with entities carrying out State, local, or tribal summer youth employment programs, to provide pathways to year-round employment for eligible youth who are ending summer employment; and (II) meet the requirements of section 176B(f)(3). (f) Use of funds An eligible entity that receives a grant under this section may use the grant funds\u2014 (1) for services described in subsection (d); (2) as described in section 176B(g)(2), with respect to year-round employment programs; (3) as described in section 176B(g)(3), with respect to activities under this section; and (4) at the discretion of the Secretary, as described in section 176B(g)(4), with respect to activities under this section. (g) Program share (1) Planning grants The provisions of section 176B(h)(1) shall apply to planning grants awarded under this section, with respect to the cost described in subsection (a)(2)(A). (2) Implementation grants The provisions of section 176B(h)(2) shall apply to implementation grants awarded under this section, with respect to the cost described in subsection (a)(2)(B). 176D. Evaluation and administration (a) Performance measures (1) Establishment The Secretary shall establish performance measures for purposes of carrying out annual reviews under subsection (b) and of developing and implementing a system of continuous quality improvement under subsection (c). (2) Components The performance measures for the eligible entities shall consist of\u2014 (A) the indicators of performance described in paragraph (3); and (B) an adjusted level of performance for each indicator described in subparagraph (A). (3) Indicators of performance (A) In general The indicators of performance shall consist of\u2014 (i) the percentage of youth employment program participants who are in education or training activities, or in employment, during the second quarter after exit from the program; (ii) the percentage of youth employment program participants who are in education or training activities, or in employment, during the fourth quarter after exit from the program; (iii) the percentage of youth employment program participants who obtain a recognized postsecondary credential, or a secondary school diploma or its recognized equivalent (subject to subparagraph (B)), during participation in or within 1 year after exit from the program; and (iv) the percentage of youth employment program participants who, during a program year, are in a youth employment program that includes an education or training program that leads to an outcome specified by the Secretary, which may include\u2014 (I) obtaining a recognized postsecondary credential or employment; or (II) achieving measurable skill gains toward such a credential or employment. (B) Indicator relating to credential For purposes of subparagraph (A)(iii), youth employment program participants who obtain a secondary school diploma or its recognized equivalent shall be included in the percentage counted as meeting the criterion under such subparagraph only if such participants, in addition to obtaining such diploma or its recognized equivalent, have obtained or retained employment or are in a youth employment program that includes an education or training program leading to a recognized postsecondary credential within 1 year after exit from the program. (4) Levels of performance (A) In general For each eligible entity, there shall be established, in accordance with this paragraph, levels of performance for each of the corresponding indicators of performance described in paragraph (3). (B) Identification in application Each eligible entity shall identify, in the application submitted under subsection (d) of section 176B or 176C, expected levels of performance for each of those indicators of performance for each program year covered by the application. (C) Agreement on adjusted levels of performance The eligible entity shall reach agreement with the Secretary on levels of performance for each of those indicators of performance for each such program year. The levels agreed to shall be considered to be the adjusted levels of performance for the eligible entity for such program years and shall be incorporated into the application prior to the approval of such application. (b) Annual review The Secretary shall carry out an annual review of each eligible entity receiving a grant under this subtitle. In conducting the review, the Secretary shall review the performance of the entity on the performance measures under this section and determine if the entity has used any practices that shall be considered best practices for purposes of this subtitle. (c) Continuous quality improvement (1) In general The Secretary shall, in addition to conducting the annual review, develop and implement a system of continuous quality improvement designed to improve the quality of activities carried out under this subtitle. (2) Activities In implementing the system, the Secretary shall carry out activities including\u2014 (A) using the performance measures established under this section, to assess the quality of employment programs funded under sections 176B and 176C and providing the eligible entities carrying out those programs with continuing feedback on their performance on those measures; (B) creating improvement plans to address quality issues concerning the employment programs; (C) providing targeted support (including technical assistance and training) to staff of the eligible entities on improving the quality of the employment programs in areas where the system demonstrates that improvements are needed; and (D) publishing and disseminating information on the quality of the employment programs. (d) Report to Congress (1) Preparation The Secretary shall prepare a report on the grant programs established by this subtitle, which report shall include a description of\u2014 (A) the eligible entities receiving funding under this subtitle; (B) the activities carried out by the eligible entities; (C) how the eligible entities were selected to receive funding under this subtitle; (D) an assessment of the results achieved by the grant programs including findings from the annual reviews conducted under subsection (b); and (E) a description of the development and implementation of, and outcomes from, the system of continuous quality improvement described in subsection (c). (2) Submission Not later than 3 years after the date of enactment of the AID Youth Employment Act , and annually thereafter, the Secretary shall submit a report described in paragraph (1) to the appropriate committees of Congress. (e) Application to Indian tribes and tribal organizations The Secretary may issue regulations that clarify the application of all the provisions of this subtitle to Indian tribes and tribal organizations. 176E. Authorization of appropriations There are authorized to be appropriated\u2014 (1) to carry out section 176B, $375,000,000 for each of fiscal years 2026 through 2030; and (2) to carry out section 176C, $500,000,000 for each of fiscal years 2026 through 2030. .\n#### 3. Conforming amendments\n##### (a) References\n**(1)**\nSection 121(b)(1)(C)(ii)(II) of the Workforce Investment and Opportunity Act ( 29 U.S.C. 3152(b)(1)(C)(ii)(II) ) is amended by striking subtitles C through E and inserting subtitles C through F .\n**(2)**\nSection 503(b) of such Act ( 29 U.S.C. 3343(b) ) is amended by inserting before the period the following: (as such subtitles were in effect on the day before the date of enactment of this Act) .\n##### (b) Table of contents\nThe table of contents in section 1(b) of such Act is amended by striking the item relating to the subtitle heading for subtitle E of title I and inserting the following:\nSubtitle E\u2014Youth Employment Opportunities Sec. 176. Definitions. Sec. 176A. Allocation of funds. Sec. 176B. Summer employment competitive grant program. Sec. 176C. Year-round employment competitive grant program. Sec. 176D. Evaluation and administration. Sec. 176E. Authorization of appropriations. Subtitle F\u2014Administration .",
      "versionDate": "2025-03-31",
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
        "actionDate": "2025-03-31",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2506",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "AID Youth Employment Act",
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
            "name": "Adoption and foster care",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Education of the disadvantaged",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Homelessness and emergency shelter",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Juvenile crime and gang violence",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Minority employment",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Temporary and part-time employment",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Unemployment",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-03-09T18:56:14Z"
          },
          {
            "name": "Youth employment and child labor",
            "updateDate": "2026-03-09T18:56:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-04-10T13:00:40Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1211is.xml"
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
      "title": "AID Youth Employment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T01:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AID Youth Employment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Assisting In Developing Youth Employment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Workforce Innovation and Opportunity Act to provide funding, on a competitive basis, for summer and year-round employment opportunities for youth ages 14 through 24.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:31Z"
    }
  ]
}
```
