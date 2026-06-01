# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8183?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8183
- Title: MATCH Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8183
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-05-14T08:08:27Z
- Update date including text: 2026-05-14T08:08:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8183",
    "number": "8183",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "O000086",
        "district": "4",
        "firstName": "Burgess",
        "fullName": "Rep. Owens, Burgess [R-UT-4]",
        "lastName": "Owens",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "MATCH Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:27Z",
    "updateDateIncludingText": "2026-05-14T08:08:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:33:10Z",
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
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8183ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8183\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Mr. Owens introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to provide for the establishment of talent marketplaces.\n#### 1. Short title\nThis Act may be cited as the Modernizing Access to Talents, Credentials, and Hiring Act of 2026 or MATCH Act of 2026 .\n#### 2. Talent marketplace\n##### (a) Definitions\nSection 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ) is amended by adding at the end the following:\n(72) Talent marketplace (A) Talent marketplace The term talent marketplace means an array of publicly- and privately-owned platforms supported by interconnected and, where relevant, interoperable and based on open standards, technologies (which may include artificial intelligence) that\u2014 (i) is made available to the public; (ii) is used to match individuals with employment and learning opportunities in a State (or a consortium of States) using information provided by users, including\u2014 (I) education and training providers; (II) employers; (III) jobseekers; (IV) students; and (V) any other individual; and (iii) incorporates and allows users access to\u2014 (I) the learning and employment records of users of such marketplace; (II) a credential registry; and (III) a skills profile generator. (B) Credential registry The term credential registry means a process through which a digital portal or repository may be used by education and training providers to make publicly available, and, where relevant, interoperable and based on open standards, a description, using standardized terminology, of the skills, competencies and learning outcomes associated with credentials, including recognized postsecondary credentials. (C) Learning and employment record The term learning and employment record means a digital, machine-readable record of an individual\u2019s educational and employment history that\u2014 (i) contains information that may be self attested and is verified by the employers, persons for whom the individual performed services, and education and training providers of such individual; (ii) allows the individual to control such information and use any such information for the purpose of matching such individual with employment and learning opportunities as described in subparagraph (A)(ii) ; and (iii) uses standardized terminology. (D) Skills profile generator The term skills profile generator means a digital tool that can be used to create a skill profile that, using standardized terminology, describes skills gained through, or necessary for\u2014 (i) employment; (ii) hiring; or (iii) education. (E) Standardized terminology The term standardized terminology means, in relation to a learning employment record, credential registry, or skills profile generator made available through a talent marketplace, a limited set of terms that is provided through a publicly available, and, where relevant, interoperable and based on open standards, skills framework and used to describe skills, competencies, or learning outcomes in a manner that\u2014 (i) provides a definition of such skill, competency, or outcome, and identifies the skills framework used for such definition; (ii) ensures that identical terms are used to describe substantially similar skills, competencies, or outcomes across such records, registries, and generators in such marketplace; and (iii) permits such terms to be effectively used for the purpose of matching individuals with employment and learning opportunities as described in subparagraph (A)(ii) . .\n##### (b) Workforce data quality initiative\n**(1) In general**\nSection 169 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3224 ) is further amended by adding at the end the following:\n(d) Workforce data quality initiative (1) Grant program Of the amount made available pursuant to section 132(a)(2)(A) for any program year, the Secretary shall use not less than 5 percent and not more than 10 percent of such amount, and may also use funds authorized for purposes of carrying out this section, to award grants to eligible entities to create workforce longitudinal data systems, talent marketplaces, and associated resources for the purposes of assisting States to\u2014 (A) improve program quality; (B) produce evidence for decision making; (C) meet performance reporting requirements; (D) protect the privacy of users; and (E) improve transparency in relation to labor market trends and changes in job skills needed to obtain employment. (2) Application To be eligible to receive a grant under this subsection, an eligible entity shall submit an application to the Secretary, at such time and in such manner as the Secretary may require, which shall include\u2014 (A) a description of the activities the eligible entity is proposing, including a description of the need for such activities and a detailed budget; (B) a description of the expected outcomes and outputs (such as systems or products) that will result from the proposed activities and the proposed uses of such outputs; (C) a description of how the proposed activities will support the reporting of performance data for the performance accountability requirements under section 116, including outcomes for eligible training providers; (D) a description of the methods and procedures the eligible entity will use to ensure the security and privacy of the collection, storage, and use of all data involved in the systems and resources supported through the grant, including compliance with State and Federal privacy and confidentiality law; (E) a plan for how the eligible entity will continue the activities or sustain the use of the outputs created with the grant funds after the grant period ends; and (F) a description of how the eligible entity will ensure interoperability and portability between the talent marketplace maintained by the eligible entity and other talent marketplaces through the use of open standards. (3) Priority In awarding grants under the subsection, the Secretary shall give priority to eligible entities that\u2014 (A) are\u2014 (i) State agencies of States that have not previously received a grant from the Secretary for the purposes of this subsection and demonstrate a substantial need to improve its data infrastructure, including for the development of a talent marketplace; or (ii) consortia of State agencies that are comprised of State agencies from multiple States and include at least one State agency described in clause (i) and have the capacity to make significant contributions toward building interoperable and portable interstate data infrastructure; and (B) will use grant funds to\u2014 (i) expand the adoption and use of linked, publicly available, and interoperable data on knowledge, skills, and abilities represented through credentials, occupational job descriptions, and learning assertions, including through the development of a talent marketplace or other tools and services designed to help learners and workers make informed decisions; (ii) participate in and contribute data to a multistate data collaborative, including data that provides participating States the ability to better understand\u2014 (I) earnings and employment outcomes of individuals who work out-of-State; and (II) interstate earnings and employment trends; (iii) enhance collaboration with private sector workforce and labor market data entities and the end-users of workforce and labor market data, including individuals, employers, economic development agencies, and workforce development providers; or (iv) leverage the use of non-Federal contributions to improve workforce data infrastructure, including staff capacity building. (4) Use of funds In addition to the activities described in paragraph (3)(B) , an eligible entity awarded a grant under this subsection may use funds to carry out any of the following activities: (A) Developing or enhancing a State\u2019s workforce longitudinal data system, including by participating and contributing data to the State\u2019s data system, if applicable, that links with elementary and secondary school and postsecondary data. (B) Accelerating the replication and adoption of data systems, projects, products, or practices already in use in one or more States to other States. (C) Research and labor market data improvement activities to improve the timeliness, relevance, and accessibility of such data through pilot projects that are developed locally but designed to scale to other regions or States. (D) Establishing or enhancing a talent marketplace. (E) Developing policies, guidelines, and security measures for data collection, storing, and sharing to ensure compliance with relevant Federal and State privacy laws and regulations. (F) Increasing local board access to and integration with the State\u2019s workforce longitudinal data system in a secure manner. (G) Creating or participating in a data exchange for collecting and using standards-based jobs and employment data including, at a minimum, job titles or occupation codes. (H) Improving State and local staff capacity to understand, use, and analyze data to improve decision-making and improve participant outcomes. (5) Administration (A) Duration A grant awarded under this subsection may be for a period of up to 3 years. (B) Supplement, not supplant Funds made available under this subsection shall be used to supplement, and not supplant, other Federal, State, or local funds used for development of State data systems. (C) Report Each eligible entity that receives a grant under this subsection shall submit a report to the Secretary not later than 180 days after the conclusion of the grant period on the activities supported through the grant and improvements in the use of workforce and labor market information that have resulted from such activities. (6) Definition In this subsection\u2014 (A) Eligible entity The term \u2018eligible entity\u2019 means a State agency, including a State workforce agency or a consortium of State agencies, including a multistate data collaborative, that is or includes the State agency responsible for\u2014 (i) State employer wage records used by the State\u2019s unemployment insurance programs in labor market information reporting and analysis and for fulfilling the reporting requirements under section 116(d); (ii) the production of labor market information; and (iii) the direct administration of one or more of the core programs. (B) Multistate data collaborative The term multistate data collaborative means a partnership among two or more States to coordinate the governance and standards for workforce related data maintained by such States in order to facilitate interoperability and the secure exchange of such data between such States. .\n**(2) Conforming amendment**\nSection 132(a)(2)(A) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3172(a)(2)(A) ) is amended by inserting after projects), the following: 169(d) (relating to workforce data quality initiatives), .\n##### (c) List and information To assist participants in choosing providers\nSection 122(d) of the Workforce Innovation and Opportunity Act (29 U.S.C. 12 3152(d)) is amended\u2014\n**(1)**\nby redesignating paragraphs (2), (3), and (4) as paragraphs (3), (4), and (6), respectively;\n**(2)**\nby inserting after paragraph (1) the following:\n(2) Talent marketplace The Governor may establish (or develop in partnership with other States) a talent marketplace. ;\n**(3)**\nby amending paragraph (4) (as so redesignated) to read as follows:\n(4) Availability The list (including the talent marketplace if one has been established by the State), and the accompanying information shall be made available to such participants and to members of the public through the one-stop delivery system in the State\u2014 (A) on a publicly accessible website that\u2014 (i) is consumer-tested; and (ii) is searchable, easily understandable, and navigable, and allows for the comparison of eligible programs through the use of common, linked, open-data descriptive language, including interoperable skills and competency data; and (B) in a manner that does not reveal personally identifiable information about an individual participant. ; and\n**(4)**\nby inserting before paragraph (6) (as so redesignated), the following:\n(5) Website technical assistance The Secretary shall\u2014 (A) upon request, provide technical assistance to a State on establishing a website that meets the requirements of paragraph (4); and (B) disseminate to each State effective practices or resources from States and private sector entities related to establishing a website that is consumer-tested to ensure that the website is easily understood, searchable, and navigable. .\n##### (d) Assistance in developing talent marketplaces\nSection 7(a)(3) of the Wagner-Peyser Act ( 29 U.S.C. 49f(a)(3) ) is amended\u2014\n**(1)**\nin subparagraph (F), by striking the and at the end;\n**(2)**\nby moving subparagraph (G) four ems to the right;\n**(3)**\nin subparagraph (G), by striking the period at the end and inserting ; and ; and\n**(4)**\nby adding at the end the following:\n(H) establishing a talent marketplace (as defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 )). .",
      "versionDate": "2026-04-02",
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
        "actionDate": "2026-04-21",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 14."
      },
      "number": "8210",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A Stronger Workforce for America Act of 2026",
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
        "updateDate": "2026-04-17T19:00:55Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8183ih.xml"
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
      "title": "MATCH Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T09:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MATCH Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T09:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modernizing Access to Talents, Credentials, and Hiring Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T09:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Workforce Innovation and Opportunity Act to provide for the establishment of talent marketplaces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T09:18:55Z"
    }
  ]
}
```
