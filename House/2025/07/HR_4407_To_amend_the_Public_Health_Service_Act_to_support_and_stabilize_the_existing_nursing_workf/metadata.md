# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4407?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4407
- Title: National Nursing Workforce Center Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4407
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-04-09T16:05:35Z
- Update date including text: 2026-04-09T16:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4407",
    "number": "4407",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "National Nursing Workforce Center Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-09T16:05:35Z",
    "updateDateIncludingText": "2026-04-09T16:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "WA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "NE"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "DE"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NJ"
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
      "sponsorshipDate": "2025-08-12",
      "state": "NC"
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
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
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
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4407ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4407\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mrs. Kim (for herself, Ms. Strickland , Mr. Bacon , Ms. McBride , and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to support and stabilize the existing nursing workforce, establish programs to increase the number of nurses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Nursing Workforce Center Act of 2025 .\n#### 2. State nursing workforce centers\nTitle VII of the Public Health Service Act ( 42 U.S.C. 292 et seq. ) is amended\u2014\n**(1)**\nby redesignating part G ( 42 U.S.C. 295j et seq. ) as part H; and\n**(2)**\nby inserting after part F the following new part:\nG Nursing workforce centers 785. State and regional nursing workforce center data collection pilot program (a) In general The Secretary may carry out a 2-year pilot program to establish new or enhance existing State-based nursing workforce centers, evaluate the impact of State-based nursing workforce centers on outcomes, and assess the feasibility of nursing workforce public-private partnerships. The Secretary shall begin implementation of such pilot program not later than 1 year after the date of enactment of the National Nursing Workforce Center Act of 2025 . (b) Grant terms (1) Term The term of a grant awarded under the pilot program under subsection (a) shall be 2 years. (2) Matching requirement As a condition on receipt of a grant under the pilot program under subsection (a), the Secretary shall require the applicant to agree, with respect to costs to be incurred by the applicant in carrying out the activities funded through the grant, to make available non-Federal contributions (in cash or in kind) toward such costs in an amount that is equal to not less than $1 for each $4 of Federal funds provided through the grant. Such contributions may be made directly or through donations from public or private entities. (c) Eligibility To be eligible to receive a grant under this section, an entity shall be\u2014 (1) a State agency; (2) a State board of nursing; (3) an organization that is exempt from taxation under section 501(c)(3) of the Internal Revenue Code of 1986; (4) a community-based organization; (5) a school of nursing (as defined in section 801); or (6) another type of school or program determined by the Secretary to be an eligible entity for purposes of this section. (d) Equitable distribution In awarding grants under this section, the Secretary shall ensure, to the greatest extent possible, that such grants are equitably distributed among the geographical regions of the United States. (e) Priority In selecting the eligible entity to be awarded a grant under this section for a nursing workforce center in a particular State, the Secretary shall give priority to eligible entities that\u2014 (1) propose to provide statewide services; (2) have expertise in the State\u2019s nursing workforce issues; (3) have a history of convening entities to address nursing workforce issues; and (4) have partnerships with entities that traditionally educate and employ the State\u2019s nurses. (f) Use of funds A nursing workforce center supported under this section may use funds provided under this section for the following statewide activities: (1) Conducting comprehensive analysis of and research on\u2014 (A) existing State nursing workforce data and gaps in such data; (B) 2- and 4-year nursing education programs, including with respect to\u2014 (i) faculty capacity and pay; (ii) enrollment, retention, and graduation; (iii) services for nursing students and the outcomes of such services; (iv) facility needs; and (v) clinical placement capacity; (C) State-specific scholarships, grants, and financial aid; and (D) factors contributing to retention and recruitment challenges and to nurses leaving the workplace or profession. (2) Conducting strategic nursing workforce planning with employers across all work settings and nursing education. (3) Conducting focused research on trends in nursing shortages, including the fiscal and clinical outcomes of contract nursing. (4) Establishing and implementing programs to\u2014 (A) support and retain faculty to increase enrollment in schools of nursing; (B) recruit and retain nurses in all settings where nurses practice; (C) support leadership development; (D) prepare the nursing workforce to address social determinants of health and health inequities; (E) prepare nurses for public health crisis and pandemic response; and (F) assist individuals in obtaining education and training required to enter the nursing profession, and advance within such profession, such as by providing career counseling and mentoring. (g) Reports Not later than one year after the date on which the first grant is awarded under the pilot program under subsection (a), and annually thereafter, the Secretary shall submit to Congress a report on the grants awarded under such pilot program during the year covered by the report. Each such report shall include\u2014 (1) a description of initiatives to study the unique characteristics of State nursing workforces, and efforts to increase the number of new nurses, recruit nurses to the nursing profession, and retain nurses in the workplace; (2) impact data on nurses served by nursing workforce centers, including demographic information of the individuals served, the number of such individuals, and the types of services provided; (3) the effectiveness of establishing formal public-private relationships for purposes of understanding the national nursing workforce through improved data collection and standardization; (4) data on continuous evaluation and quality improvement, and other relevant data as determined by the Secretary; and (5) the Secretary\u2019s recommendations and best practices for\u2014 (A) reducing shortages among different nursing specialties; (B) reducing shortages in rural and underserved areas; (C) improving geographical distribution of the nursing workforce; and (D) reducing shortages among different types of nursing employers. (h) Funding From the amounts appropriated to the Health Resources and Services Administration for workforce initiatives, the Secretary may use up to $1,500,000 for each of fiscal years 2026 and 2027 for purposes of carrying out this section. .\n#### 3. State and regional centers for health workforce analysis\n##### (a) Expansion of covered programs\nSection 761(c)(1)(A) of the Public Health Service Act ( 42 U.S.C. 294n(c)(1)(A) ) is amended by striking under this title and inserting under this Act .\n##### (b) Analysis and technical assistance\nSection 761(c) of the Public Health Service Act ( 42 U.S.C. 294n(c) ) is amended by adding at the end the following:\n(3) Minimum requirement At least one grant or contract awarded under this subsection may be awarded to an eligible entity that demonstrates\u2014 (A) a mission to advance and support the nursing workforce; (B) experience and expertise in guiding State-level nursing workforce centers; (C) experience in working with nursing workforce data; (D) expertise in analytical methods and tools appropriate for nursing workforce research; and (E) awareness of emerging topics, issues, and trends related to the nursing workforce. (4) Analysis and reporting Analysis and reporting carried out pursuant to a grant or contract under this subsection may include\u2014 (A) collaborating with nursing workforce centers to produce or deliver, with respect to the supply of nurses, the demand for nurses, and the capacity to educate and train the nursing workforce\u2014 (i) regional and national reports; (ii) articles in peer-reviewed journals; (iii) presentations at national and international conferences and meetings; and (iv) policy briefs, fact sheets, articles, blogs, and other publications available in the public domain; (B) evaluating the programs and activities of the nursing workforce centers overall; (C) developing evidence-based or evidence-informed strategies and best practices to alleviate nursing workforce shortages across States and regions; and (D) conducting rapid data analysis and short-term, issue-specific research. (5) Technical Assistance Technical assistance provided pursuant to this subsection may include\u2014 (A) providing technical assistance to nursing workforce centers on the collection, analysis, and reporting of standardized supply, demand, and education and training data to inform analysis conducted pursuant to this subsection; (B) collaborating with nursing workforce centers to identify and deliver evidence-based or evidence-informed strategies to alleviate nursing shortages and the maldistribution of nurses; (C) providing online and in-person training opportunities for nurses and other staff at nursing workforce centers; and (D) developing and maintaining a website that\u2014 (i) is accessible to grant and contract recipients under section 785 and this section; (ii) supports resources for the provision of technical assistance under this section, such as\u2014 (I) evidence-based or evidence-informed educational materials, tools, recent findings of interest, and links to relevant resources; and (II) logistical and administrative information, such as online trainings, webinars, and publications; and (iii) includes a publicly accessible repository of webinars, tools, and resources. (6) Definition In this subsection, the term nursing workforce center means a nursing workforce center funded under section 785. .",
      "versionDate": "2025-07-15",
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
        "actionDate": "2026-03-19",
        "text": "Committee on Health, Education, Labor, and Pensions. Hearings held."
      },
      "number": "1482",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "National Nursing Workforce Center Act of 2025",
      "type": "S"
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
            "name": "Congressional oversight",
            "updateDate": "2026-04-06T19:35:29Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-09T16:05:35Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2026-04-06T19:35:29Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-04-06T19:35:29Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-04-06T19:35:29Z"
          },
          {
            "name": "Labor market",
            "updateDate": "2026-04-06T19:35:29Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2026-04-06T19:35:29Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2026-04-06T19:35:29Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-04-06T19:35:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-07-31T12:15:54Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4407ih.xml"
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
      "title": "National Nursing Workforce Center Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Nursing Workforce Center Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to support and stabilize the existing nursing workforce, establish programs to increase the number of nurses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:31Z"
    }
  ]
}
```
