# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8196?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8196
- Title: Workforce Data Quality Initiative Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8196
- Origin chamber: House
- Introduced date: 2026-04-06
- Update date: 2026-04-17T19:35:54Z
- Update date including text: 2026-04-17T19:35:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-06: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-06: Introduced in House

## Actions

- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Introduced in House
- 2026-04-06 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-06",
    "latestAction": {
      "actionDate": "2026-04-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8196",
    "number": "8196",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001322",
        "district": "5",
        "firstName": "Michael",
        "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
        "lastName": "Baumgartner",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Workforce Data Quality Initiative Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-17T19:35:54Z",
    "updateDateIncludingText": "2026-04-17T19:35:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-06",
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
      "actionDate": "2026-04-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-06",
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
          "date": "2026-04-06T14:01:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8196ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8196\nIN THE HOUSE OF REPRESENTATIVES\nApril 6, 2026 Mr. Baumgartner introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to add the Workforce data quality initiative.\n#### 1. Short title\nThis Act may be cited as the Workforce Data Quality Initiative Act of 2026 .\n#### 2. Workforce data quality initiative\n##### (a) Reservations of funds for workforce data quality initiative\nSection 132(a)(2)(A) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3172(a)(2)(A) ) is amended by\u2014\n**(1)**\nstriking , 169(c) (relating to dislocated worker projects), ; and\n**(2)**\nby inserting , and under subsections (c) (relating to dislocated worker projects) and (d) (relating to workforce data quality initiatives) of section 169 before ; and .\n##### (b) Workforce data quality initiative\nSection 169 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3224 ) is amended by adding at the end the following:\n(d) Workforce data quality initiative (1) Grant program Of amount made available pursuant to section 132(a)(2)(A) for any program year, the Secretary shall use not less than 5 percent and not more than 10 percent of such amount, and may also use funds appropriated under section 172(d) for purposes of carrying out this section, to award grants to eligible entities to create workforce longitudinal data systems and associated resources for the purposes of strengthening program quality, building State capacity to produce evidence for decision-making, meeting performance reporting requirements, protecting privacy, and improving transparency. (2) Application To be eligible to receive a grant under this subsection, an eligible entity shall submit an application to the Secretary at such time and in such manner as the Secretary may require, which shall include\u2014 (A) a description of the proposed activities that will be conducted by the eligible entity, including a description of the need for such activities and a detailed budget for such activities; (B) a description of the expected outcomes and outputs (such as systems or products) that will result from the proposed activities and the proposed uses of such outputs; (C) a description of how the proposed activities will\u2014 (i) support the reporting of performance data, including employment and earnings outcomes, for the performance accountability requirements under section 116, including outcomes for eligible providers of training services; (ii) improve workforce data standardization across programs in the State; and (iii) improve the collection, accuracy, timeliness, and usability of real-time, economy-wide data on new and emerging skills and in-demand occupational roles; (D) a description of the methods and procedures the eligible entity will use to ensure the security and privacy of the collection, storage, and use of all data involved in the systems and resources supported through the grant, including compliance with State and Federal privacy and confidentiality statutes and regulations; and (E) a plan for how the eligible entity will continue the activities or sustain the use of the outputs created with the grant funds after the grant period ends. (3) Priority In awarding grants under the subsection, the Secretary shall give priority to\u2014 (A) eligible entities that are\u2014 (i) a State agency of a State that has not previously received a grant from the Secretary for the purposes of this subsection and demonstrates a substantial need to improve its data infrastructure; or (ii) a consortium of State agencies that is comprised of State agencies from multiple States and includes at least one State agency described in clause (i) and has the capacity to make significant contributions toward building interoperable, cross-State data infrastructure; and (B) eligible entities that will use grant funds to\u2014 (i) expand the adoption and use of linked, open, and interoperable data on credentials, including through the development of a credential registry or other tools and services designed to help learners and workers make informed decisions, such as a credential navigation feature that allows participants and the public to search a list of recognized post-secondary credentials offered by eligible providers of training services under section 122; (ii) participate in and contribute data to a multistate data collaborative, including data that provide participating States the ability to better understand\u2014 (I) earnings and employment outcomes of individuals who work out-of-State; and (II) cross-State earnings and employment trends; (iii) enhance collaboration with private sector workforce and labor market data entities and the end-users of workforce and labor market data, including individuals, employers, economic development agencies, and workforce development providers; (iv) leverage the use of non-Federal contributions to improve workforce data infrastructure, including staff capacity building; or (v) expand existing statewide integrated longitudinal data systems, including such systems receiving assistance under section 208 of the Educational Technical Assistance Act of 2002 ( 20 U.S.C. 9607 ). (4) Use of funds In addition to the activities described in paragraph (3)(B), an eligible entity awarded a grant under this subsection may use funds to carry out any of the following activities: (A) Developing or enhancing a State\u2019s workforce longitudinal data system, including by participating and contributing data to the State\u2019s data system, if applicable, that links with elementary and secondary school and post-secondary data. (B) Accelerating the replication and adoption of data systems, projects, products, or practices already in use in one or more States to other States. (C) Research and labor market data improvement activities to improve the timeliness, relevance, and accessibility of such data through pilot projects that are developed locally but designed to scale to other regions or States. (D) Establishing, enhancing, or connecting to a system of interoperable learning and employment records that provides individuals who choose to participate in such system ownership of a verified and secure record of their skills and achievements and the ability to share such record with employers and education providers. (E) Developing policies, guidelines, and security measures for data collection, storing, and sharing to ensure compliance with relevant Federal and State privacy laws and regulations. (F) Increasing local board access to and integration with the State\u2019s workforce longitudinal data system in a secure manner. (G) Creating or participating in a data exchange for collecting and using standards-based jobs and employment data including, at a minimum, job titles or occupation codes. (H) Improving State and local staff capacity to understand, use, and analyze data to improve decision-making and improve participant outcomes. (5) Administration (A) Duration A grant awarded under this subsection may be for a period of up to 3 years. (B) Supplement, not supplant Funds made available under this subsection shall be used to supplement, and not supplant, other Federal, State, or local funds used for development of State data systems. (C) Report Each eligible entity that receives a grant under this subsection shall submit a report to the Secretary not later than 180 days after the conclusion of the grant period on the activities supported through the grant and improvements in the use of workforce and labor market information that have resulted from such activities. (6) Eligible entity defined In this subsection, the term eligible entity means a State agency or consortium of State agencies, including a multistate data collaborative, that is or includes the State agencies responsible for\u2014 (A) State employer wage records used by the State\u2019s unemployment insurance programs in labor market information reporting and analysis and for fulfilling the reporting requirements of this Act; (B) the production of labor market information; and (C) the direct administration of one or more of the core programs. .",
      "versionDate": "2026-04-06",
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
        "updateDate": "2026-04-17T19:35:54Z"
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
      "date": "2026-04-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8196ih.xml"
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
      "title": "Workforce Data Quality Initiative Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Workforce Data Quality Initiative Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Workforce Innovation and Opportunity Act to add the Workforce data quality initiative.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T05:18:49Z"
    }
  ]
}
```
