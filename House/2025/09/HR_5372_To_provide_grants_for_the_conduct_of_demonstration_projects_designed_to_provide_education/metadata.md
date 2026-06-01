# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5372?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5372
- Title: DEMO Act
- Congress: 119
- Bill type: HR
- Bill number: 5372
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-09-25T14:21:09Z
- Update date including text: 2025-09-25T14:21:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5372",
    "number": "5372",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000096",
        "district": "7",
        "firstName": "Danny",
        "fullName": "Rep. Davis, Danny K. [D-IL-7]",
        "lastName": "Davis",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "DEMO Act",
    "type": "HR",
    "updateDate": "2025-09-25T14:21:09Z",
    "updateDateIncludingText": "2025-09-25T14:21:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5372ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5372\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Davis of Illinois introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide grants for the conduct of demonstration projects designed to provide education and training for eligible individuals with an arrest or conviction record to enter and follow a career pathway in the health professions through occupations that are expected to experience a labor shortage or be in high demand, under the health profession opportunity grant program under section 2008 of the Social Security Act.\n#### 1. Short title\nThis Act may be cited as the Demonstrating that Empowerment Makes Opportunities Act or the DEMO Act .\n#### 2. Grants for demonstration projects to provide career pathways in the health professions for certain individuals with an arrest or conviction record\nSection 2008 of the Social Security Act ( 42 U.S.C. 1397g ) is amended by redesignating subsection (d) as subsection (e) and inserting after subsection (c) the following:\n(d) Demonstration projects To provide career pathways in the health professions for certain individuals with an arrest or conviction record (1) Grant authority The Secretary, in consultation with the Secretary of Labor, the Secretary of Education, and the Attorney General, shall award grants in accordance with this subsection to eligible entities to conduct demonstration projects for the purpose of providing education and training for eligible individuals with arrest or conviction records to enter and follow a career pathway in the health professions through occupations that pay well and are expected to experience a labor shortage or be in high demand. (2) Duration A demonstration project shall be conducted under this subsection for not less than 3 years. (3) Application requirements An applicant seeking a grant under this subsection for a demonstration project shall submit to the Secretary an application for the grant, that includes the following: (A) A demonstration that the State in which the project is to be conducted has in effect policies or laws that permit certain allied health and behavioral health care credentials to be awarded to people with certain arrest or conviction records (which policies or laws shall include appeals processes and other opportunities to demonstrate rehabilitation to obtain credentials, licensure, and approval to work in the proposed health careers), and a plan described in the application which will use a career pathway to assist participants with such a record in acquiring credentials, licensing, and employment in the specified careers. (B) A discussion of how the project or future strategic hiring decisions will demonstrate the experience and expertise of the project in working with job seekers who have arrest or conviction records or employers with experience working with people with arrest or conviction records. (C) A demonstration that the applicant has experience working with low-income populations, or a description of the plan of the applicant to work with a partner organization that has the experience. (D) An identification of promising innovations or best practices that can be used to provide the training. (E) A proof of concept or demonstration that the applicant has done sufficient research on workforce shortage or in-demand jobs for which people with certain types of arrest or conviction records can be hired. (F) A plan for recruiting students who are eligible individuals into the project. (G) A plan for providing post-employment support and ongoing training as part of a career pathway under the project. (4) Preferences in considering applications In considering applications for a grant under this subsection, the Secretary shall give preference to\u2014 (A) applications submitted by applicants who have completed a demonstration project funded under this section, if an evaluation of the project, which was funded by the Secretary, found the project to have positive outcomes in the categories of\u2014 (i) graduation and credential attainment; (ii) job placement and retention; and (iii) evidence of addressing the worker shortage or in-demand jobs described in the original application for funding for the completed demonstration project; and (B) applications which have an emergency cash fund to assist project participants financially in emergency situations. (5) Support to be provided (A) Required support A project for which a grant is made under this subsection shall include access to legal assistance for project participants for the purpose of addressing arrest or conviction records and associated workforce barriers. (B) Allowed support The goods and services provided under a project for which a grant is made under this subsection may include the following: (i) A reserve fund for financial assistance to project participants in emergency situations. (ii) Assistance with programs and activities, including legal assistance, deemed necessary to address arrest or conviction records as an employment barrier. (6) Technical assistance The Secretary shall provide technical assistance\u2014 (A) to assist eligible entities in applying for grants under this subsection; (B) that is tailored to meet the needs of grantees at each stage of the administration of projects for which grants are made under this subsection; and (C) that is tailored to meet the specific needs of eligible entities in carrying out the projects. (7) Evaluations (A) In general The Secretary shall, by grant, contract, or interagency agreement, conduct rigorous and well-designed evaluations of the demonstration projects for which a grant is made under this subsection, which shall include identification of successful activities for creating opportunities for developing and sustaining, particularly with respect to low-income individuals with arrest or conviction records, a health professions workforce that has accessible entry points, that meets high standards for education, training, certification, and professional development, and that provides increased wages and affordable benefits, including health care coverage, that are responsive to the needs of the workforce. (B) Rule of interpretation Evaluations conducted pursuant to this paragraph may include a randomized controlled trial, but this paragraph shall not be interpreted to require an evaluation to include such a trial. (8) Definitions In this subsection: (A) Eligible entity The term eligible entity means any of the following entities that demonstrates in an application submitted under this subsection that the entity has the capacity to fully develop and administer the demonstration project described in the application: (i) A local workforce development board established under section 107 of the Workforce Innovation and Opportunity Act. (ii) A State or territory, a political subdivision of a State or territory, or an agency of a State, territory, or such a political subdivision. (iii) An Indian tribe, a tribal organization, or a tribal college or university. (iv) An institution of higher education (as defined in the Higher Education Act of 1965). (v) A hospital (as defined in section 1861(e)). (vi) A skilled nursing facility (as defined in section 1819(h)(1)(A)). (vii) A Federally qualified health center (as defined in section 1861(aa)(4)). (viii) A nonprofit organization described in section 501(c)(3) of the Internal Revenue Code of 1986, a labor organization, or an entity with shared labor-management oversight, that has a demonstrated history of providing health profession training to eligible individuals. (ix) An opioid treatment program (as defined in section 1861(iii)(2)). (B) Eligible individual The term eligible individual means an individual whose income does not exceed 138 percent of the Federal poverty level. (9) Appropriation Out of any funds in the Treasury of the United States not otherwise appropriated, there are appropriated to the Secretary to carry out this subsection $10,000,000 for fiscal year 2026. .\n#### 3. Effective date\nThe amendment made by this Act shall take effect on October 1, 2025.",
      "versionDate": "2025-09-16",
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
        "name": "Health",
        "updateDate": "2025-09-25T14:21:09Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5372ih.xml"
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
      "title": "DEMO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DEMO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Demonstrating that Empowerment Makes Opportunities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide grants for the conduct of demonstration projects designed to provide education and training for eligible individuals with an arrest or conviction record to enter and follow a career pathway in the health professions through occupations that are expected to experience a labor shortage or be in high demand, under the health profession opportunity grant program under section 2008 of the Social Security Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:28Z"
    }
  ]
}
```
