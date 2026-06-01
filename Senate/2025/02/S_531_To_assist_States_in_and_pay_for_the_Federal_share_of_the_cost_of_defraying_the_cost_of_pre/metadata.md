# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/531?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/531
- Title: American Apprenticeship Act
- Congress: 119
- Bill type: S
- Bill number: 531
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-03-03T21:02:27Z
- Update date including text: 2026-03-03T21:02:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/531",
    "number": "531",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "American Apprenticeship Act",
    "type": "S",
    "updateDate": "2026-03-03T21:02:27Z",
    "updateDateIncludingText": "2026-03-03T21:02:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T23:04:48Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s531is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 531\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Ms. Klobuchar (for herself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo assist States in, and pay for the Federal share of the cost of, defraying the cost of pre-apprenticeships or related instruction associated with qualified apprenticeship programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Apprenticeship Act .\n#### 2. Pre-apprenticeship and qualified apprenticeship programs\n##### (a) Definitions\nIn this Act:\n**(1) Qualified apprenticeship**\nThe term qualified apprenticeship , used with respect to a program, means an apprenticeship program that is\u2014\n**(A)**\nregistered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ); and\n**(B)**\nconcentrated in an industry sector or occupation that represents less than 10 percent of apprenticeable occupations or of the programs under the national apprenticeship system.\n**(2) Postsecondary educational institution**\nThe term postsecondary educational institution means an institution of higher education, as defined in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n**(3) Pre-apprenticeship**\nThe term pre-apprenticeship , used with respect to a program, means an initiative or set of strategies that\u2014\n**(A)**\nis designed to prepare individuals to enter and succeed in a qualified apprenticeship program;\n**(B)**\nis carried out by a sponsor described in paragraph (6)(B) that has a documented partnership with one or more sponsors of qualified apprenticeship programs; and\n**(C)**\nincludes each of the following:\n**(i)**\nTraining (including a curriculum for the training), aligned with industry standards related to apprenticeships in a qualified apprenticeship program, and reviewed and approved annually by sponsors of such apprenticeships within the documented partnership, that will prepare individuals by teaching the skills and competencies needed to enter one or more qualified apprenticeship programs.\n**(ii)**\nProvision of hands-on training and theoretical education to individuals that\u2014\n**(I)**\nis carried out in a manner that includes proper observation of supervision and safety protocols; and\n**(II)**\nis carried out in a manner that does not displace a paid employee.\n**(iii)**\nA formal agreement with a sponsor of a qualified apprenticeship program that would enable participants who successfully complete the pre-apprenticeship program to enter directly into the qualified apprenticeship program (if a place in the program is available and if the participant meets the qualifications of the qualified apprenticeship program), and includes agreements concerning earning credit recognized by a postsecondary educational institution for skills and competencies acquired during the pre-apprenticeship program.\n**(4) Related instruction**\nThe term related instruction means an organized and systematic form of classroom or web-based instruction designed to provide an apprentice with the knowledge of the theoretical and technical subjects related to the occupation of the apprentice or the instruction needed to prepare an individual to enter and succeed in an qualified apprenticeship program.\n**(5) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(6) Sponsor**\nThe term sponsor means\u2014\n**(A)**\nwith respect to a qualified apprenticeship program, an employer, joint labor-management partnership, trade association, professional association, labor organization, or other entity, that administers the qualified apprenticeship program; and\n**(B)**\nwith respect to a pre-apprenticeship program, a local educational agency, a secondary school, an area career and technical education school, a State board, a local board, a joint labor-management committee, a labor organization, or a community-based organization, with responsibility for the pre-apprenticeship program.\n**(7) Workforce Innovation and Opportunity Act definitions**\nThe terms area career and technical education school , community-based organization , individual with a barrier to employment , local board , local educational agency , secondary school , and State board have the meanings given the terms in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n##### (b) Grants for tuition assistance\n**(1) In general**\nThe Secretary may make grants to States on a competitive basis to assist the States in, and pay for the Federal share of the cost of, defraying the cost of a pre-apprenticeship, or the cost of related instruction, associated with a qualified apprenticeship program.\n**(2) Application**\nTo be eligible to receive a grant under this subsection, a State shall submit an application to the Secretary for such a project at such time, in such manner, and containing a strategic plan that contains such information as the Secretary may require, including\u2014\n**(A)**\ninformation identifying the State agency (referred to in this Act as the State entity ) that will administer the grant as determined by the Governor of the State;\n**(B)**\na description of strategies that the State entity will use to collaborate with key industry representatives, State agencies, postsecondary educational institutions, labor-management entities, and other relevant partners to launch or expand pre-apprenticeships for and apprenticeships in qualified apprenticeship programs;\n**(C)**\na description of how the State entity will\u2014\n**(i)**\ncoordinate activities carried out under this subsection with activities carried out under the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ) and the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ) to support pre-apprenticeships for and apprenticeships in qualified apprenticeship programs;\n**(ii)**\nleverage funds provided under the Acts specified in clause (i) to support pre-apprenticeships for and apprenticeships in qualified apprenticeship programs; and\n**(iii)**\nutilize, and encourage individual participants in programs supported under this subsection to utilize, available Federal and State financial assistance, including assistance available under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ), education assistance benefits available to veterans, and Federal Pell Grants available under section 401 of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ), prior to using assistance made available under this Act;\n**(D)**\na description of strategies to elevate apprenticeships in qualified apprenticeship programs as a workforce solution in nontraditional industries, such as information technology, health care, advanced manufacturing, transportation, and other industries determined to be high-demand by the State board for the State;\n**(E)**\na description of activities that the State entity will carry out to build awareness about the economic potential of apprenticeships in qualified apprenticeship programs;\n**(F)**\na description that outlines how the State entity will increase opportunities for pre-apprenticeships for and apprenticeships in qualified apprenticeship programs, among members of minority groups, youth, individuals with disabilities, veterans, and individuals with barriers to employment;\n**(G)**\na description of\u2014\n**(i)**\nhow the State entity will ensure that the qualified apprenticeship program meets certain performance measures and quality standards, including that the qualified apprenticeship program has been in existence for not fewer than 6 months prior to the application date;\n**(ii)**\nthe targeted outreach strategies that the State entity will use for populations previously underserved through apprenticeships; and\n**(iii)**\nany State performance measures that the State will use, at the election of the State, to measure the effectiveness of the project; and\n**(H)**\nin the case of a State that has already received a grant under this subsection for a project, information indicating that the State met the performance measures with respect to the project.\n**(3) Application review process**\nA joint team of employees from the Department of Labor and the Department of Education shall\u2014\n**(A)**\nreview such an application; and\n**(B)**\nmake recommendations to the Secretary regarding approval of the application.\n**(4) Use of funds**\nA State that receives a grant under this subsection shall use the funds made available through the grant to defray any of the following costs of related instruction:\n**(A)**\nTuition and fees.\n**(B)**\nCost of textbooks, equipment, curriculum development, and other required educational materials.\n**(C)**\nCosts of any other item or service determined by the State to be necessary.\n**(5) Administrative costs**\nThe State may use not more than 10 percent of the grant funds for administrative costs relating to carrying out the project described in paragraph (1).\n**(6) Performance and evaluation**\nThe Secretary, after consultation with the Secretary of Education, shall\u2014\n**(A)**\nestablish performance measures based on indicators set by the Administrator of the Office of Apprenticeship of the Department of Labor; and\n**(B)**\nestablish an evaluation system aligned with the performance measures, and reporting requirements for the program carried out under this subsection.\n##### (c) Federal share\n**(1) In general**\nThe Federal share of the cost described in subsection (b)(1) shall be not less than 20 percent and not more than 50 percent.\n**(2) Non-Federal share**\nThe State may make the non-Federal share available\u2014\n**(A)**\nin cash or in kind, fairly evaluated, including plant, equipment, or services; and\n**(B)**\ndirectly or through donations from public or private entities.\n##### (d) Report\nThe Secretary shall prepare and submit to Congress, not later than September 30, 2030, a report\u2014\n**(1)**\ndetailing the results of the evaluation described in subsection (b)(6)(B); and\n**(2)**\nanalyzing the extent to which States have used grant funds effectively under this section.\n##### (e) Policy of the United States\nIt is the policy of the United States that funds made available under this section should be used to supplement and not supplant other funds available under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ) and other Federal and State funds available to the State to support workforce development programs.\n#### 3. Identifying in-demand occupations\nThe Secretary shall\u2014\n**(1)**\nidentify in-demand occupations nationally and regionally that lack the use of apprenticeships in qualified apprenticeship programs;\n**(2)**\nanalyze the use of the qualified apprenticeship program model in those identified in-demand occupations; and\n**(3)**\nprepare and submit to States and Congress a report that contains the analysis described in paragraph (2).\n#### 4. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $15,000,000 for each of fiscal years 2026 through 2031.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-03-03",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1783",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Apprenticeship Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-04-23T17:41:06Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-23T17:41:06Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-04-23T17:41:06Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-23T17:41:06Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-23T17:41:06Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-04-23T17:41:06Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-04-23T17:41:06Z"
          },
          {
            "name": "Vocational and technical education",
            "updateDate": "2025-04-23T17:41:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-12T16:24:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119s531",
          "measure-number": "531",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2026-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s531v00",
            "update-date": "2026-03-03"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>American Apprenticeship Act</strong></p> <p>This bill authorizes the Department of Labor to make grants to assist states in carrying out projects that defray the cost of pre-apprenticeship or related instruction for qualified apprenticeship programs.</p> <p>Labor shall (1) establish performance measures and an evaluation system for such grant program; and (2) identify in-demand occupations that lack the use of apprenticeships, analyze the use of the qualified apprenticeship program model in those occupations, and report on such analysis to states and Congress.</p>"
        },
        "title": "American Apprenticeship Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s531.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Apprenticeship Act</strong></p> <p>This bill authorizes the Department of Labor to make grants to assist states in carrying out projects that defray the cost of pre-apprenticeship or related instruction for qualified apprenticeship programs.</p> <p>Labor shall (1) establish performance measures and an evaluation system for such grant program; and (2) identify in-demand occupations that lack the use of apprenticeships, analyze the use of the qualified apprenticeship program model in those occupations, and report on such analysis to states and Congress.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119s531"
    },
    "title": "American Apprenticeship Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Apprenticeship Act</strong></p> <p>This bill authorizes the Department of Labor to make grants to assist states in carrying out projects that defray the cost of pre-apprenticeship or related instruction for qualified apprenticeship programs.</p> <p>Labor shall (1) establish performance measures and an evaluation system for such grant program; and (2) identify in-demand occupations that lack the use of apprenticeships, analyze the use of the qualified apprenticeship program model in those occupations, and report on such analysis to states and Congress.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119s531"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s531is.xml"
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
      "title": "American Apprenticeship Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Apprenticeship Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to assist States in, and pay for the Federal share of the cost of, defraying the cost of pre-apprenticeships or related instruction associated with qualified apprenticeship programs, and for other programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:03Z"
    }
  ]
}
```
