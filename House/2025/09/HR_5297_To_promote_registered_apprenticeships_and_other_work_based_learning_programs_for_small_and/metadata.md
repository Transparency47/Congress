# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5297
- Title: PARTNERS Act
- Congress: 119
- Bill type: HR
- Bill number: 5297
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2026-04-17T13:28:28Z
- Update date including text: 2026-04-17T13:28:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5297",
    "number": "5297",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "PARTNERS Act",
    "type": "HR",
    "updateDate": "2026-04-17T13:28:28Z",
    "updateDateIncludingText": "2026-04-17T13:28:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-11T13:03:25Z",
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
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "KY"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MI"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "IA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5297ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5297\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Ms. Bonamici (for herself, Mr. Guthrie , Ms. Stevens , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo promote registered apprenticeships and other work-based learning programs for small and medium-sized businesses within in-demand industry sectors, through the establishment and support of industry or sector partnerships.\n#### 1. Short title\nThis Act may be cited as the Promoting Apprenticeships through Regional Training Networks for Employers Required Skills Act of 2025 or the PARTNERS Act .\n#### 2. Purpose\nThe purpose of this Act is to promote registered apprenticeships and other work-based learning programs for small and medium-sized businesses within in-demand industry sectors, through the establishment and support of industry or sector partnerships.\n#### 3. Definitions\nIn this Act:\n**(1) Eligible partnership**\nThe term eligible partnership means an industry or sector partnership as defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ) that submits and obtains approval of an application consistent with section 5(c).\n**(2) In-demand industry sector**\nThe term in-demand industry sector means a sector described in subparagraphs (A)(i) and (B) of section 3(23) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102(23) ).\n**(3) Local or regional**\nThe term local or regional , used with respect to an entity, means that the entity provides services in, respectively, a local area or region.\n**(4) Registered apprenticeship**\nThe term registered apprenticeship means an apprenticeship registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ).\n**(A) In general**\nThe term work-based learning program means a program that provides workers with paid work experience and corresponding classroom instruction, delivered in an employment relationship that both the business and worker intend to lead to continuing employment after the program ends.\n**(B) Work experience**\nIn subparagraph (A), the term paid work experience includes training by an employer that is provided to a paid employee while engaged in productive work in a job that provides knowledge or skills essential to the full and adequate performance of the job.\n**(5) Workforce terms**\nThe terms Governor , individual with a barrier to employment , industry or sector partnership , local area , local board , State board , outlying area , recognized postsecondary credential , region , State , and supportive services , used with respect to activities supported under this Act, have the meanings given the terms in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n**(6) Secretary**\nThe term Secretary means the Secretary of Labor.\n#### 4. Availability of funds\nFrom funds paid into the general fund of the Treasury and available under section 286(s)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1356(s)(2) ), the Secretary shall carry out this Act.\n#### 5. Allotments to states\n##### (a) Reservation\nOf the amounts available for this Act under section 4, the Secretary may reserve\u2014\n**(1)**\nnot more than 5 percent of those amounts for the costs of technical assistance and Federal administration of this Act;\n**(2)**\nnot more than 2 percent of those amounts for the costs of evaluations conducted under section 8(b); and\n**(3)**\nnot more than 1/4 of 1 percent of such amounts to provide assistance to the outlying areas.\n##### (b) Allotments\n**(1) In general**\nOf the amounts available for this Act under section 4 that remain after the Secretary makes the reservations under subsection (a), the Secretary shall, for the purpose of supporting (which may include assistance in establishing expanded) local or regional eligible partnerships to support work-based learning programs under this Act, make allotments to eligible States in accordance with clauses (ii) through (v) of section 132(b)(1)(B) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3172(b)(1)(B) ), subject to paragraph (2).\n**(2) Application**\nFor purposes of applying the clauses described in paragraph (1), under paragraph (1), the Secretary\u2014\n**(A)**\nshall not apply subclauses (I) and (III) of clause (iv) with respect to the first fiscal year after the date of enactment of this Act;\n**(B)**\nshall apply clause (iv)(II) by substituting 0.5 percent of the remaining amounts described in paragraph (1) for the total described in that clause;\n**(C)**\nshall not apply clause (iv)(IV);\n**(D)**\nshall apply clause (v)(II) by substituting the term allotment percentage , used with respect to the second full fiscal year after the date of enactment of this Act, or a subsequent fiscal year, means a percentage of the remaining amounts described in paragraph (1) that is received through an allotment made under this subsection for the fiscal year for the two sentences in that clause; and\n**(E)**\nshall apply clause (v)(III) by substituting a work-based learning program carried out under this Act for a program of workforce investment activities carried out under this subtitle .\n**(3) Use of unallotted funds**\nIf a State fails to meet the requirements for an allotment under this subsection, the Secretary may allot funds that are not allotted under paragraphs (1) and (2) to eligible States under a formula based on the formula specified in section 132(c) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3173(c) ).\n**(4) Definition**\nIn this subsection, the term eligible State means a State that meets the requirements of section 102 or 103 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3112 , 3113) and subsection (c).\n##### (c) State eligibility\nTo be eligible to receive an allotment under subsection (b), a State, in consultation with State boards and local boards, shall submit an application to the Secretary, at such time, in such manner, and containing a description of the activities to be carried out with the grant funds. At a minimum, the application shall include information on\u2014\n**(1)**\nthe local or regional industry or sector partnerships that will be supported, including the lead partners for the partnerships, and how the partnerships will work to engage small and medium-sized businesses, as applicable, in the activities of the partnerships;\n**(2)**\nthe in-demand industry sectors that will be served, including how such industry sectors were identified, and how the activities of the partnerships will align with State, regional, and local plans as required under title I of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3111 et seq. );\n**(3)**\nthe registered apprenticeship programs or other work-based learning programs to be supported though the partnerships;\n**(4)**\nthe populations that will receive services, including individuals with barriers to employment and populations that were historically underrepresented in the industry sectors to be served through the partnerships;\n**(5)**\nthe services, including business engagement, classroom instruction, and support services (including at least 6 months of post-employment support services), that will be supported through the grant funds;\n**(6)**\nthe recognized postsecondary credentials that workers will obtain through participation in the program and the quality of the program that leads to the credentials;\n**(7)**\nlevels of performance to be achieved on the performance indicators described in section 8, to measure progress towards expanding work-based learning programs;\n**(8)**\nhow local or regional partnerships will leverage additional resources, including funding provided under title I of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3111 et seq. ) and non-Federal resources, to support the activities carried out under this Act; and\n**(9)**\nsuch other subjects as the Secretary may require.\n##### (d) Review of applications\nThe Secretary shall review applications submitted under subsection (c) in consultation with the Secretary of Education and the Secretary of Health and Human Services.\n#### 6. Grants to partnerships\n##### (a) Grants\n**(1) In general**\nThe Governor of a State that receives an allotment under section 5 shall use the funds made available through the allotment and not reserved under subsection (d) to award grants to eligible partnerships. The Governor shall award the grants for the purpose of assisting (which may include establishing or expanding) local or regional industry or sector partnerships that are identified in the application submitted under section 5(c), to carry out activities described in section 7.\n**(2) Period and amount of grant**\nA State may make a grant under this section for a period of 3 years, and in an amount of not more than $500,000.\n**(3) Availability of funds**\nThe Governor of a State that receives an allotment under section 5 for a fiscal year may use the funds made available through the allotment during that year or the 2 subsequent fiscal years.\n##### (b) Eligibility\nTo be eligible to receive a grant under this section, an industry or sector partnership described in subsection (a)(1) shall\u2014\n**(1)**\nsubmit an application to the State at such time, in such manner, and containing such information as the State may require; and\n**(2)**\ndesignate a partner in the industry or sector partnership, to serve as the fiscal agent for purposes of the grant.\n##### (c) Awards of grants\n**(1) Participation in multiple eligible partnerships**\nSubject to paragraph (2), a State may award grants under this section in a way that results in an entity being represented in more than one partnership that receives such a grant.\n**(2) Geographic diversity**\nIn making the grants, a State shall ensure that there is geographic diversity in the areas in which activities will be carried out under the grants.\n##### (d) Administration\nThe State may reserve not more than 5 percent of the amount of an allotment under section 5 for the administration of the grants awarded under this section.\n#### 7. Use of funds\n##### (a) In general\nAn eligible partnership that receives a grant under section 6 shall use the grant funds to support a registered apprenticeship or other work-based learning program. The eligible partnership shall use the grant funds to support the activities described in subsections (b) and (c) and such other strategies as may be necessary to support the development and implementation of work-based learning programs, and participant retention in and completion of those programs. The partnership may use the grant funds to establish or expand eligible partnerships.\n##### (b) Business engagement\nThe eligible partnership shall use grant funds to provide services to engage businesses in work-based learning programs, which may include assisting a small or medium-sized business with\u2014\n**(1)**\nthe navigation of the registration process for a sponsor of a registered apprenticeship program;\n**(2)**\nthe connection of the business with an education provider to develop classroom instruction to complement on-the-job learning;\n**(3)**\nthe development of a curriculum for a work-based learning program;\n**(4)**\nthe employment of workers in a work-based learning program for a transitional period before the business hires an individual for continuing employment;\n**(5)**\nthe provision of training to managers and front-line workers to serve as trainers or mentors to workers in the work-based learning program;\n**(6)**\nthe provision of career awareness activities; and\n**(7)**\nthe recruitment of individuals to participate in a work-based learning program from individuals receiving additional workforce and human services, including\u2014\n**(A)**\nworkers in programs under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. );\n**(B)**\nrecipients of assistance through the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ); and\n**(C)**\nrecipients of assistance through the program of block grants to States for temporary assistance for needy families established under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ).\n##### (c) Support services for workers\n**(1) In general**\nThe eligible partnership shall use grant funds to provide support services for workers to assure their success in work-based learning programs, which may include\u2014\n**(A)**\nconnection of individuals with adult basic education during pre-work-based learning or training, and during the period of employment;\n**(B)**\nconnection of individuals with pre-work-based learning or training, including through a pre-apprenticeship program;\n**(C)**\nprovision of additional mentorship and retention supports for individuals pre-work-based learning or training, and during the period of employment;\n**(D)**\nprovision of tools, work attire, and other required items necessary to start employment pre-work-based learning or training, and during the period of employment; and\n**(E)**\nprovision of transportation, child care services, or other support services pre-work-based learning or training, and during the period of employment, except that not more than 5 percent of grant funds received by an eligible partnership may be used for the provision of such services.\n**(2) Length of services**\nEach eligible partnership shall provide support services for workers for not less than 12 months after the date of placement of an individual in a work-based learning program. That 12-month period shall include a period of pre-work-based learning or training, a transitional period of employment as described in subsection (b)(4), and a period of continuing employment.\n#### 8. Performance and accountability\n##### (a) Local reports\nNot later than 1 year after receiving a grant under section 6, and annually thereafter, each eligible partnership in a State shall conduct an evaluation and submit to the State a local report containing information on\u2014\n**(1)**\nlevels of performance achieved by the eligible partnership with respect to the performance indicators under section 116(b)(2)(A) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3141(b)(2)(A) )\u2014\n**(A)**\nfor all workers in the work-based learning program involved; and\n**(B)**\nfor all such workers, disaggregated by each population specified in section 3(24) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102(24) ) and by race, ethnicity, sex, and age; and\n**(2)**\nlevels of performance achieved by the eligible partnership with respect to the performance indicators under that section 116(b)(2)(A)\u2014\n**(A)**\nfor individuals with barriers to employment in the work-based learning program involved; and\n**(B)**\nfor all such individuals, disaggregated by each population specified in section 3(24) of the Workforce Innovation and Opportunity Act and by race, ethnicity, sex, and age.\n##### (b) State reports\nNot later than 24 months after receiving initial local reports under subsection (a) (but in no case less than 18 months after the corresponding grants are awarded) and annually thereafter, the State shall conduct an evaluation and submit a report to the Secretary containing\u2014\n**(1)**\nthe information provided by the eligible partnerships through the local reports; and\n**(2)**\nthe State level of performance, aggregated across all eligible partnerships, with respect to the performance indicators described in subsection (a).\n#### 9. Conforming amendments\n##### (a) American competitiveness and workforce improvement act of 1998\nSection 414(c) of the American Competitiveness and Workforce Improvement Act of 1998 ( 29 U.S.C. 3224a(c) ) is repealed.\n##### (b) Immigration and nationality act\nSection 286(s)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1356(s)(2) ) is amended to read as follows:\n(2) Use of fees for work-based learning programs 50 percent of amounts deposited into the H\u20131B Nonimmigrant Petitioner Account shall remain available to the Secretary of Labor until expended to carry out the PARTNERS Act. .",
      "versionDate": "2025-09-11",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-15",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Homeland Security, Ways and Means, Transportation and Infrastructure, Education and Workforce, Oversight and Government Reform, and Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4393",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DIGNIDAD (Dignity) Act of 2025",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-24T14:41:48Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5297ih.xml"
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
      "title": "PARTNERS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T02:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PARTNERS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Apprenticeships through Regional Training Networks for Employers Required Skills Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote registered apprenticeships and other work-based learning programs for small and medium-sized businesses within in-demand industry sectors, through the establishment and support of industry or sector partnerships.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:20Z"
    }
  ]
}
```
