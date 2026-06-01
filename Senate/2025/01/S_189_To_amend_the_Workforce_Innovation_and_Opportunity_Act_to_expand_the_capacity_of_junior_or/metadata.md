# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/189?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/189
- Title: CONSTRUCTS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 189
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-12-05T22:02:22Z
- Update date including text: 2025-12-05T22:02:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/189",
    "number": "189",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacklyn",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "CONSTRUCTS Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:02:22Z",
    "updateDateIncludingText": "2025-12-05T22:02:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T19:29:46Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s189is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 189\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Ms. Rosen (for herself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to expand the capacity of junior or community colleges and area career and technical education schools to conduct training services, education, and outreach activities for careers in the residential construction industry.\n#### 1. Short title\nThis Act may be cited as the Creating Opportunities for New Skills Training at Rural or Underserved Colleges and Trade Schools Act of 2025 and CONSTRUCTS Act of 2025 .\n#### 2. Education and training for careers in residential construction\n##### (a) In general\nSubtitle D of title I of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3221 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 172 as section 173; and\n**(2)**\nby inserting after section 171 the following:\n172. Education and training for careers in residential construction (a) Definitions In this section: (1) Incumbent worker The term incumbent worker has the meaning given the term in section 680.780 of title 20, Code of Federal Regulations, or a successor regulation. (2) Junior or community college The term junior or community college has the meaning given the term in section 312 of the Higher Education Act of 1965 ( 20 U.S.C. 1058 ). (3) Rural area The term rural area means any\u2014 (A) nonmetropolitan area; or (B) rural area, as defined under section 520 of the Housing Act of 1949 ( 42 U.S.C. 1490 ). (4) Underserved population The term underserved population means a group of individuals with a common demographic trait (such as individuals from the same gender, race, or ethnicity), the members of which\u2014 (A) based on the most recent satisfactory demographic and employment data from the Bureau of the Census, comprise a percentage of individuals employed in the construction sector that is lower than the percentage of the total population of the United States comprised by such members; (B) are low-income individuals; (C) are individuals with barriers to employment; or (D) are veterans. (b) Establishment of program (1) In general The Secretary of Labor, in consultation with the Secretary of Education, shall establish a program, through which the Secretary of Labor shall award, on a competitive basis, grants to eligible entities to expand their capacity to provide training services, education, and outreach activities for careers in the residential construction industry. (2) Grant period A grant awarded under this section shall be for a period of not more than 4 years. (c) Eligible entities To be eligible to receive a grant under this section, an entity shall be\u2014 (1) a junior or community college; (2) an area career and technical education school; or (3) a provider of training services, as described in section 122(a)(2). (d) Applications An eligible entity that desires to receive a grant under this section shall submit an application to the Secretary of Labor at such time, in such manner, and containing such information as the Secretary may require, including the following information: (1) A description of the new or expanded training services, education, or outreach activities supported by the grant, including a description of how the new training services, education, or outreach activities will align with existing programming related to careers in the residential construction industry at the eligible entity, and the relevant faculty or technical instructors employed by the eligible entity on the date of the submission of the application or who may be employed by the eligible entity to carry out the training services, education, or outreach activities supported by the grant. (2) A description of the populations that will be served through the training services, education, or outreach activities supported by the grant, including whether the participants in such training services, education, or outreach activities are\u2014 (A) incumbent workers; (B) individuals in rural areas; (C) in-school youth; (D) opportunity youth; or (E) part of an underserved population. (3) A description of the partnerships the eligible entity will facilitate through the grant, including the process by which the eligible entity will ensure that a partner provides fair wages and benefits that are commensurate with local pay and benefit packages, and a plan for sustaining activities and partnerships supported by the grant after the completion of the grant period. (4) A description of the anticipated outcomes of the training services, education, or outreach activities supported by the grant, including, at a minimum, the recognized postsecondary credential, postsecondary credit, or degree to be earned by participants, and a timetable showing how the eligible entity will meet the primary indicators of performance described in section 116(b)(2)(A). (5) A description of the intended impact of the training services, education, or outreach activities on the local housing market, including a description of how the new training services, education, or outreach activities will increase the supply of affordable housing. (6) Such other information as the Secretary may require. (e) Priority In awarding grants under this section, the Secretary of Labor shall give priority to eligible entities that serve rural areas or underserved populations. (f) Use of funds (1) Required uses An eligible entity that receives a grant under this section shall use the grant funds\u2014 (A) to create or expand an evidence-based education or training program to provide skills needed in the residential construction industry, including skills related to\u2014 (i) carpentry; (ii) framing; (iii) masonry; (iv) welding; (v) plumbing; (vi) electrical work; (vii) construction management; (viii) architecture; (ix) HVAC; (x) land surveying and geomatics; (xi) construction mathematics; (xii) heavy equipment operation; and (xiii) such other trades as identified by the Department of Labor; (B) to create or expand an education or training program focused on increasing the skills of incumbent workers who are residential construction workers; (C) to create a partnership with a local residential construction business or developer, either alone or in conjunction with a nonprofit organization, labor organization, entity in the State or local workforce development system, sponsor of a pre-apprenticeship or apprenticeship program, YouthBuild program, or another community partner, with a focus on engaging with organizations that recruit employees or program participants from underserved populations; and (D) to facilitate outreach to secondary school and elementary school students about the residential construction industry and education and training programs available under this section, which may include developing dual or concurrent enrollment programs (as defined under section 8101 of the Elementary and Secondary Education Act of 1965) for secondary students to participate in such education and training programs or integrating such programs in a relevant career and technical education program administered by an elementary school or secondary school. (2) Permissive uses An eligible entity that receives a grant under this section may use the grant funds\u2014 (A) to hire technical instructors or other faculty with demonstrated experience and expertise in residential construction to lead education or training programs related to skills and recognized postsecondary credentials needed for a career in the residential construction industry; (B) to operate an education and training clinic in a rural area or area not otherwise served by an entity described in subsection (c), to the extent necessary and practicable; (C) to develop promotion materials for the purpose of increasing awareness of the training services, education, or outreach activities; or (D) to provide supportive services through merit-based and needs-based scholarships, to promote retention in, and completion of\u2014 (i) an education or training program supported under this section; or (ii) tests or coursework related to certification. (g) Assistance; flexible schedules An eligible entity that receives a grant under this section shall\u2014 (1) use flexible schedules in carrying out the education or training program, including night classes, part-time schedules, and online curricula, to accommodate individuals who work during the day or live in rural areas; and (2) provide an individual, upon completion of the education or training program, supportive services for job search and placement to ensure the success of such individuals in achieving the education and career goals. (h) Compliance with applicable laws (1) In general Each recipient of funds under this section, and any entity that enters into a partnership with such recipient for the purpose of this Act, shall attest to the Secretary of Labor that the recipient or entity\u2014 (A) is in compliance with each Federal, State, and local labor law; (B) will remain in compliance with each Federal, State, and local labor law; and (C) is not subject to a pending action or case relating to a violation of any law enforced by the Department of Labor, Federal Labor Relations Authority, Equal Employment Opportunity Commission, or National Labor Relations Board. (2) Federal, state, and local labor law In this subsection, the term Federal, State, and local labor law means any Federal, State, or local labor law that would be applicable to the recipient or entity described in paragraph (1), as determined by the Secretary of Labor. (i) Performance accountability (1) In general An eligible entity that receives a grant under this section shall, not later than 18 months after receiving such grant and annually thereafter for the duration of the grant period, submit to the Secretary of Labor a report containing the eligible entity\u2019s outcomes with respect to the primary indicators of performance described in section 116(b)(2)(A). (2) Report to Congress Not later than 6 months after receiving initial reports from each eligible entity receiving a grant under this section, the Secretary shall prepare and submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Education and Workforce of the House of Representatives a report containing, at a minimum, the information described in paragraph (1) for each such eligible entity. (j) Authorization of appropriations There are authorized to be appropriated $20,000,000 to carry out this section for each of fiscal years 2025 through 2029. .\n##### (b) Table of contents\nThe table of contents in section 1(b) of the Workforce Innovation and Opportunity Act is amended\u2014\n**(1)**\nby striking the item relating to section 172; and\n**(2)**\nby inserting after the item relating to section 171 the following:\nSec. 172. Education and training for careers in residential construction. Sec. 173. Authorization of appropriations. .",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1055",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CONSTRUCTS Act of 2025",
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
            "name": "Building construction",
            "updateDate": "2025-03-25T17:06:29Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-25T17:06:50Z"
          },
          {
            "name": "Education of the disadvantaged",
            "updateDate": "2025-03-25T17:05:38Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-25T17:06:10Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-25T17:06:36Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-03-25T17:05:55Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-25T17:05:44Z"
          },
          {
            "name": "Housing supply and affordability",
            "updateDate": "2025-03-25T17:06:16Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-25T17:06:43Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-03-25T17:06:23Z"
          },
          {
            "name": "Vocational and technical education",
            "updateDate": "2025-03-25T17:05:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-02-24T21:15:45Z"
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
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s189is.xml"
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
      "title": "CONSTRUCTS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CONSTRUCTS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Creating Opportunities for New Skills Training at Rural or Underserved Colleges and Trade Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Workforce Innovation and Opportunity Act to expand the capacity of junior or community colleges and area career and technical education schools to conduct training services, education, and outreach activities for careers in the residential construction industry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:33:46Z"
    }
  ]
}
```
