# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1783?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1783
- Title: American Apprenticeship Act
- Congress: 119
- Bill type: HR
- Bill number: 1783
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-04-21T08:05:47Z
- Update date including text: 2026-04-21T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1783",
    "number": "1783",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "American Apprenticeship Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:05:47Z",
    "updateDateIncludingText": "2026-04-21T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:07:30Z",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "MA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MN"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "OH"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "IL"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1783ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1783\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Ms. DeLauro introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo assist States in, and pay for the Federal share of the cost of, defraying the cost of pre-apprenticeships or related instruction associated with qualified apprenticeship programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Apprenticeship Act .\n#### 2. Pre-apprenticeship and qualified apprenticeship programs\n##### (a) Definitions\nIn this Act:\n**(1) Qualified apprenticeship**\nThe term qualified apprenticeship , used with respect to a program, means an apprenticeship program that is\u2014\n**(A)**\nregistered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ); and\n**(B)**\nconcentrated in an industry sector or occupation that represents less than 10 percent of apprenticeable occupations or of the programs under the national apprenticeship system.\n**(2) Postsecondary educational institution**\nThe term postsecondary educational institution means an institution of higher education, as defined in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n**(3) Pre-apprenticeship**\nThe term pre-apprenticeship , used with respect to a program, means an initiative or set of strategies that\u2014\n**(A)**\nis designed to prepare individuals to enter and succeed in a qualified apprenticeship program;\n**(B)**\nis carried out by a sponsor described in paragraph (6)(B) that has a documented partnership with one or more sponsors of qualified apprenticeship programs; and\n**(C)**\nincludes each of the following:\n**(i)**\nTraining (including a curriculum for the training), aligned with industry standards related to apprenticeships in a qualified apprenticeship program, and reviewed and approved annually by sponsors of such apprenticeships within the documented partnership, that will prepare individuals by teaching the skills and competencies needed to enter one or more qualified apprenticeship programs.\n**(ii)**\nProvision of hands-on training and theoretical education to individuals that\u2014\n**(I)**\nis carried out in a manner that includes proper observation of supervision and safety protocols; and\n**(II)**\nis carried out in a manner that does not displace a paid employee.\n**(iii)**\nA formal agreement with a sponsor of a qualified apprenticeship program that would enable participants who successfully complete the pre-apprenticeship program to enter directly into the qualified apprenticeship program (if a place in the program is available and if the participant meets the qualifications of the qualified apprenticeship program), and includes agreements concerning earning credit recognized by a postsecondary educational institution for skills and competencies acquired during the pre-apprenticeship program.\n**(4) Related instruction**\nThe term related instruction means an organized and systematic form of classroom or web-based instruction designed to provide an apprentice with the knowledge of the theoretical and technical subjects related to the occupation of the apprentice or the instruction needed to prepare an individual to enter and succeed in an qualified apprenticeship program.\n**(5) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(6) Sponsor**\nThe term sponsor means\u2014\n**(A)**\nwith respect to a qualified apprenticeship program, an employer, joint labor-management partnership, trade association, professional association, labor organization, or other entity, that administers the qualified apprenticeship program; and\n**(B)**\nwith respect to a pre-apprenticeship program, a local educational agency, a secondary school, an area career and technical education school, a State board, a local board, a joint labor-management committee, a labor organization, or a community-based organization, with responsibility for the pre-apprenticeship program.\n**(7) Workforce Innovation and Opportunity Act definitions**\nThe terms area career and technical education school , community-based organization , individual with a barrier to employment , local board , local educational agency , secondary school , and State board have the meanings given the terms in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n##### (b) Grants for tuition assistance\n**(1) In general**\nThe Secretary may make grants to States on a competitive basis to assist the States in, and pay for the Federal share of the cost of, defraying the cost of a pre-apprenticeship, or the cost of related instruction, associated with a qualified apprenticeship program.\n**(2) Application**\nTo be eligible to receive a grant under this subsection, a State shall submit an application to the Secretary for such a project at such time, in such manner, and containing a strategic plan that contains such information as the Secretary may require, including\u2014\n**(A)**\ninformation identifying the State agency (referred to in this Act as the State entity ) that will administer the grant as determined by the Governor of the State;\n**(B)**\na description of strategies that the State entity will use to collaborate with key industry representatives, State agencies, postsecondary educational institutions, labor-management entities, and other relevant partners to launch or expand pre-apprenticeships for and apprenticeships in qualified apprenticeship programs;\n**(C)**\na description of how the State entity will\u2014\n**(i)**\ncoordinate activities carried out under this subsection with activities carried out under the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ) and the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ) to support pre-apprenticeships for and apprenticeships in qualified apprenticeship programs;\n**(ii)**\nleverage funds provided under the Acts specified in clause (i) to support pre-apprenticeships for and apprenticeships in qualified apprenticeship programs; and\n**(iii)**\nutilize, and encourage individual participants in programs supported under this subsection to utilize, available Federal and State financial assistance, including assistance available under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ), education assistance benefits available to veterans, and Federal Pell Grants available under section 401 of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ), prior to using assistance made available under this Act;\n**(D)**\na description of strategies to elevate apprenticeships in qualified apprenticeship programs as a workforce solution in nontraditional industries, such as information technology, health care, advanced manufacturing, transportation, and other industries determined to be high-demand by the State board for the State;\n**(E)**\na description of activities that the State entity will carry out to build awareness about the economic potential of apprenticeships in qualified apprenticeship programs;\n**(F)**\na description that outlines how the State entity will increase opportunities for pre-apprenticeships for and apprenticeships in qualified apprenticeship programs, among members of minority groups, youth, individuals with disabilities, veterans, and individuals with barriers to employment;\n**(G)**\na description of\u2014\n**(i)**\nhow the State entity will ensure that the qualified apprenticeship program meets certain performance measures and quality standards, including that the qualified apprenticeship program has been in existence for not fewer than 6 months prior to the application date;\n**(ii)**\nthe targeted outreach strategies that the State entity will use for populations previously underserved through apprenticeships; and\n**(iii)**\nany State performance measures that the State will use, at the election of the State, to measure the effectiveness of the project; and\n**(H)**\nin the case of a State that has already received a grant under this subsection for a project, information indicating that the State met the performance measures with respect to the project.\n**(3) Application review process**\nA joint team of employees from the Department of Labor and the Department of Education shall\u2014\n**(A)**\nreview such an application; and\n**(B)**\nmake recommendations to the Secretary regarding approval of the application.\n**(4) Use of funds**\nA State that receives a grant under this subsection shall use the funds made available through the grant to defray any of the following costs of related instruction:\n**(A)**\nTuition and fees.\n**(B)**\nCost of textbooks, equipment, curriculum development, and other required educational materials.\n**(C)**\nCosts of any other item or service determined by the State to be necessary.\n**(5) Administrative costs**\nThe State may use not more than 10 percent of the grant funds for administrative costs relating to carrying out the project described in paragraph (1).\n**(6) Performance and evaluation**\nThe Secretary, after consultation with the Secretary of Education, shall\u2014\n**(A)**\nestablish performance measures based on indicators set by the Administrator of the Office of Apprenticeship of the Department of Labor; and\n**(B)**\nestablish an evaluation system aligned with the performance measures, and reporting requirements for the program carried out under this subsection.\n##### (c) Federal share\n**(1) In general**\nThe Federal share of the cost described in subsection (b)(1) shall be not less than 20 percent and not more than 50 percent.\n**(2) Non-Federal share**\nThe State may make the non-Federal share available\u2014\n**(A)**\nin cash or in kind, fairly evaluated, including plant, equipment, or services; and\n**(B)**\ndirectly or through donations from public or private entities.\n##### (d) Report\nThe Secretary shall prepare and submit to Congress, not later than September 30, 2030, a report\u2014\n**(1)**\ndetailing the results of the evaluation described in subsection (b)(6)(B); and\n**(2)**\nanalyzing the extent to which States have used grant funds effectively under this section.\n##### (e) Policy of the United States\nIt is the policy of the United States that funds made available under this section should be used to supplement and not supplant other funds available under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ) and other Federal and State funds available to the State to support workforce development programs.\n#### 3. Identifying in-demand occupations\nThe Secretary shall\u2014\n**(1)**\nidentify in-demand occupations nationally and regionally that lack the use of apprenticeships in qualified apprenticeship programs;\n**(2)**\nanalyze the use of the qualified apprenticeship program model in those identified in-demand occupations; and\n**(3)**\nprepare and submit to States and Congress a report that contains the analysis described in paragraph (2).\n#### 4. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $15,000,000 for each of fiscal years 2026 through 2031.",
      "versionDate": "2025-03-03",
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
        "actionDate": "2025-02-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "531",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Apprenticeship Act",
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
            "updateDate": "2025-04-23T17:41:30Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-23T17:41:30Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-04-23T17:41:30Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-23T17:41:30Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-23T17:41:30Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-04-23T17:41:30Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-04-23T17:41:30Z"
          },
          {
            "name": "Vocational and technical education",
            "updateDate": "2025-04-23T17:41:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-21T15:49:51Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1783ih.xml"
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
      "title": "American Apprenticeship Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Apprenticeship Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To assist States in, and pay for the Federal share of the cost of, defraying the cost of pre-apprenticeships or related instruction associated with qualified apprenticeship programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T10:18:36Z"
    }
  ]
}
```
