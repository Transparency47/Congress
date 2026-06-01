# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7885?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7885
- Title: Cybersecurity Skills Integration Act
- Congress: 119
- Bill type: HR
- Bill number: 7885
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-03T19:46:13Z
- Update date including text: 2026-04-03T19:46:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7885",
    "number": "7885",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Cybersecurity Skills Integration Act",
    "type": "HR",
    "updateDate": "2026-04-03T19:46:13Z",
    "updateDateIncludingText": "2026-04-03T19:46:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:00:50Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7885ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7885\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Thompson of Pennsylvania (for himself and Ms. Bonamici ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Education to establish a pilot program to award competitive grants for the integration of cybersecurity education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cybersecurity Skills Integration Act .\n#### 2. Purpose\nThe purpose of this Act is to improve the cybersecurity competencies of the critical infrastructure workforce, particularly operators of critical infrastructure technology, by developing postsecondary career and technical education programs that integrate cybersecurity education.\n#### 3. Cybersecurity education grants\n##### (a) In general\nFrom the amounts made available to carry out this Act, the Secretary of Education shall, not later than 1 year after the date of enactment of this Act, establish a pilot program under which the Secretary shall award grants, on a competitive basis, to eligible partnerships for\u2014\n**(1)**\nthe development and implementation of postsecondary career and technical education programs that incorporate cybersecurity education and prepare individuals to meet workforce needs in critical infrastructure sectors; and\n**(2)**\nthe integration of cybersecurity education into existing postsecondary career and technical education programs that prepare individuals to meet workforce needs in critical infrastructure sectors.\n##### (b) Consultation and coordination\nIn awarding grants under this Act, the Secretary shall consult with the Secretary of Labor, the Director of the National Institute of Standards and Technology, and the Secretary of Homeland Security, to determine the greatest workforce needs in critical infrastructure sectors.\n##### (c) Grant amount\nThe amount of any grant made under this Act shall not exceed $500,000 in any fiscal year.\n##### (d) Applications\nTo be eligible to receive a grant under this Act, an eligible partnership shall submit an application to the Secretary at such time, in such manner, containing such information as the Secretary may reasonably require, and including a description of\u2014\n**(1)**\nthe roles and responsibilities of each partner in the eligible partnership, and each partner\u2019s capacity to support the postsecondary career and technical education program to be developed and implemented with funds awarded under this Act, or the postsecondary career and technical education program into which cybersecurity education will be integrated with funds awarded under this Act;\n**(2)**\nthe critical infrastructure sector or sectors that such postsecondary career and technical education program prepares individuals to enter;\n**(3)**\nthe in-demand occupation within such sector or sectors that such postsecondary career and technical education program prepares individuals to enter;\n**(4)**\nthe workforce needs of such critical infrastructure sector or sectors, including cybersecurity workforce needs, and how the postsecondary career and technical education program will meet such workforce needs;\n**(5)**\nhow the eligible partnership will incorporate cybersecurity education aligned to the National Initiative for Cybersecurity Education (NICE) Cybersecurity Workforce Framework developed by the National Institute of Standards and Technology of the Department of Commerce, or successor framework, into such postsecondary career and technical education program;\n**(6)**\nthe assessment, capstone project, or other means of demonstrating knowledge and cybersecurity skills specific to the critical infrastructure sector or sectors that such postsecondary career and technical education program prepares individuals to enter, and an assurance that such assessment, project, or other demonstration of knowledge and skills will be a requirement for program completion;\n**(7)**\nthe work-based learning opportunities the eligible partnership will offer;\n**(8)**\nhow such postsecondary career and technical education program will lead to a recognized postsecondary credential and employment in the critical infrastructure sector or sectors targeted by the postsecondary career and technical education program;\n**(9)**\nthe process through which the cybersecurity education curriculum and educational materials developed or integrated using such grant will be updated annually to include the most recent information on cybersecurity threats specific to such critical infrastructure sector or sectors;\n**(10)**\nhow such postsecondary career and technical education program will be sustained following the grant period;\n**(11)**\nhow such postsecondary career and technical education program will promote diversity within the cybersecurity workforce in critical infrastructure sectors; and\n**(12)**\nany other purpose for which the eligible partnership intends to use funds awarded under this Act.\n##### (e) Regional diversity\nWhen awarding grants under this Act, the Secretary shall ensure that grants are awarded to eligible partnerships in different regions.\n##### (f) Reporting Requirements\nAn eligible partnership that receives a grant under this Act shall annually submit a report to the Secretary that includes\u2014\n**(1)**\na description of how any funds awarded to the eligible partnership under this Act have been used during the period covered by the report;\n**(2)**\nthe number of students who have received a recognized postsecondary credential during such period from the postsecondary career and technical education program into which cybersecurity education was incorporated using such funds, disaggregated by the subgroups of students described in section 1111(c)(2)(B) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(c)(2)(B) ) and by each special population;\n**(3)**\na description of any updates made during the preceding year to the cybersecurity education curriculum and educational materials of such postsecondary career and technical education program in accordance with the requirements of subsection (d)(9); and\n**(4)**\nthe percentage of participants in unsubsidized employment in an in-demand occupation in a critical infrastructure sector targeted by the postsecondary career and technical education program after exiting the postsecondary career and technical education program.\n##### (g) Authorization of Appropriations\nThere are authorized to be appropriated to the Secretary to carry out this Act $10,000,000.\n##### (h) Definitions\nIn this Act:\n**(1) Critical Infrastructure**\nThe term critical infrastructure has the meaning given the term in section 1016(e) of the USA PATRIOT Act ( 42 U.S.C. 5195c(e) ).\n**(2) Cybersecurity education**\nThe term cybersecurity education shall mean education on critical infrastructure cyber defense, including\u2014\n**(A)**\nensuring the confidentiality, integrity, and availability of information systems used in critical infrastructure, including control systems and operational technology;\n**(B)**\ndeveloping engineering skills applicable to industrial control systems and operational technologies used in critical infrastructure systems; and\n**(C)**\ntraining to ensure the continuous physical and environmental safety of the operations of critical infrastructure systems.\n**(3) Eligible partnership**\n**(A) Required partners**\nThe term eligible partnership means a partnership that includes\u2014\n**(i)**\na postsecondary educational institution; and\n**(ii)**\n2 or more public or private employers, in a critical infrastructure sector, with demonstrated cybersecurity workforce needs, that is located in the region where the postsecondary career and technical education program will be developed and implemented with a grant awarded under this Act.\n**(B) Optional partners**\nThe partnership may also include one or more\u2014\n**(i)**\ncommunity stakeholders (such as local governments, nonprofit institutions, economic development organizations, planning agencies, labor organizations, or industry associations);\n**(ii)**\nlocal educational agencies (as the term is defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )); and\n**(iii)**\neligible agencies that are located in the region where the postsecondary career and technical education program will be developed and implemented with funds awarded under this Act.\n**(4) Eligible agency**\nThe term eligible agency means a State board designated or created consistent with State law as the sole State agency responsible for the administration of career and technical education in the State or for the supervision of the administration of career and technical education in the State.\n**(5) In-demand industry sector or occupation**\nThe term in-demand industry sector or occupation has the meaning given the term in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n**(6) Postsecondary educational institution**\nThe term postsecondary educational institution means\u2014\n**(A)**\nan institution of higher education (defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )) that provides not less than a 2-year program of instruction that is acceptable for credit toward an associate\u2019s or bachelor's degree;\n**(B)**\na tribally controlled college or university (defined in section 2(a)(4) of the Tribally Controlled Colleges and Universities Assistance Act of 1978 ( 25 U.S.C. 1801(a)(4) )); or\n**(C)**\na nonprofit educational institution offering certificate or other skilled training programs at the postsecondary level.\n**(7) Postsecondary career and technical education program**\nThe term postsecondary career and technical education program means a coordinated, nonduplicative sequence of academic and technical content at the postsecondary level that\u2014\n**(A)**\naddresses both academic and technical knowledge and skills, including employability skills;\n**(B)**\nis aligned with the needs of industries in the economy of the State, region, Tribal community, or local area;\n**(C)**\nprogresses in specificity (beginning with all aspects of an industry or career cluster and leading to more occupation-specific instruction);\n**(D)**\nhas multiple entry and exit points that incorporate credentialing; and\n**(E)**\nculminates in the attainment of a recognized postsecondary credential.\n**(8) Secretary**\nThe term Secretary means the Secretary of Education.\n**(9) Work based learning**\nThe term work based learning means sustained interactions with industry or community professionals in real workplace settings, to the extent practicable, or simulated environments at an educational institution that foster in-depth, firsthand engagement with the tasks required in a given career field, that are aligned to curriculum and instruction.\n**(10) Recognized Postsecondary Credential**\nThe term recognized postsecondary credential has the meaning given the term in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n**(11) Special Populations**\nThe term special populations means\u2014\n**(A)**\nindividuals with disabilities;\n**(B)**\nindividuals from economically disadvantaged families, including low-income youth and adults;\n**(C)**\nindividuals preparing for non-traditional fields;\n**(D)**\nsingle parents, including single pregnant women;\n**(E)**\nout-of-workforce individuals;\n**(F)**\nEnglish learners;\n**(G)**\nhomeless individuals described in section 11434a of title 42, United States Code;\n**(H)**\nyouth who are in, or have aged out of, the foster care system; and\n**(I)**\nyouth with a parent who\u2014\n**(i)**\nis a member of the Armed Forces (as such term is defined in section 101(a)(4) of title 10, United States Code); and\n**(ii)**\nis on active duty (as such term is defined in section 101(d)(1) of such title).",
      "versionDate": "2026-03-09",
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
        "name": "Education",
        "updateDate": "2026-04-01T20:35:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-09",
    "originChamber": "House",
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
          "measure-id": "id119hr7885",
          "measure-number": "7885",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-09",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7885v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-03-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Cybersecurity Skills Integration Act</strong></p><p>This bill requires the Department of Education to establish a pilot program in order to award grants to partnerships between postsecondary educational institutions and employers in critical infrastructure sectors for cybersecurity education programs.</p>"
        },
        "title": "Cybersecurity Skills Integration Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7885.xml",
    "summary": {
      "actionDate": "2026-03-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cybersecurity Skills Integration Act</strong></p><p>This bill requires the Department of Education to establish a pilot program in order to award grants to partnerships between postsecondary educational institutions and employers in critical infrastructure sectors for cybersecurity education programs.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr7885"
    },
    "title": "Cybersecurity Skills Integration Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cybersecurity Skills Integration Act</strong></p><p>This bill requires the Department of Education to establish a pilot program in order to award grants to partnerships between postsecondary educational institutions and employers in critical infrastructure sectors for cybersecurity education programs.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr7885"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7885ih.xml"
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
      "title": "Cybersecurity Skills Integration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T04:58:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cybersecurity Skills Integration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T04:58:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Education to establish a pilot program to award competitive grants for the integration of cybersecurity education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T04:48:30Z"
    }
  ]
}
```
