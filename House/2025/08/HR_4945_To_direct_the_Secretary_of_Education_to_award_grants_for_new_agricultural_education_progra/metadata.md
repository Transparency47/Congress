# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4945?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4945
- Title: GO Ag Act
- Congress: 119
- Bill type: HR
- Bill number: 4945
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-12-19T09:08:07Z
- Update date including text: 2025-12-19T09:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4945",
    "number": "4945",
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
    "title": "GO Ag Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:08:07Z",
    "updateDateIncludingText": "2025-12-19T09:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:30:25Z",
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
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "MO"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "TX"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-15",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NJ"
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
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "IL"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4945ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4945\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Thompson of Pennsylvania (for himself, Mr. Alford , Mr. Cuellar , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Education to award grants for new agricultural education programs in secondary schools.\n#### 1. Short title\nThis Act may be cited as the Growing Opportunities in Agriculture Act or the GO Ag Act .\n#### 2. Grant program for new agricultural education programs\n##### (a) Grant program authorized\n**(1) In general**\nThe Secretary shall award, on a competitive basis, grants to eligible entities to support the creation of new agricultural education programs in secondary schools.\n**(2) Grant duration**\nA grant awarded under this section may not exceed a 5-year grant period.\n##### (b) Application\n**(1) In general**\nTo receive a grant under this section, an eligible entity shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including\u2014\n**(A)**\nan identification and the role with respect to each program to be funded under the grant of any eligible partners of the eligible entity, including an assurance the grant under this section will not be used to prepare students for employment with solely one or more of such eligible partners;\n**(B)**\nan assurance that each program that will receive assistance under the grant is not yet in operation and such grant will be used to start such program;\n**(C)**\na description of the grant budget, how each program will fund necessary expenses for the program not covered by the grant (such as any funds to be provided by State, local, or private entities), and how the eligible entity will continue each such program after the grant is exhausted;\n**(D)**\na description of how grant will directly benefit students, including special populations, served by the eligible entity;\n**(E)**\na description of how each such program will be coordinated with the activities carried out under section 124 or 135 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2344 ; 2355);\n**(F)**\na description of how each such program reflects the needs of regional, State, or local employers, as demonstrated by the comprehensive needs assessment under section 134(c) of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2354(c) ) carried out by the eligible entity; and\n**(G)**\nan assurance that the eligible entity will\u2014\n**(i)**\nprovide information to the Secretary, as requested, for the evaluation under subsection (d) and any evaluations that the Secretary may carry out; and\n**(ii)**\nmake data available to third parties for validation, in accordance with applicable data privacy laws, including section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g , commonly known as the Family Educational Rights and Privacy Act of 1974 ).\n**(2) Process**\nThe Secretary shall create a process for evaluating applications submitted under paragraph (1) and determining the amount of each grant for successful applications, except that in no case may an eligible entity receive a grant exceeding $100,000.\n##### (c) Uses of funds\nEach eligible entity receiving a grant under this section shall use such grant for the creation of new agricultural education programs in secondary schools, which may include\u2014\n**(1)**\ncurriculum development and delivery, including classroom or laboratory instruction, work-based learning, and leadership education delivered through career and technical student organizations;\n**(2)**\nthe purchase of equipment, technology, and course materials; and\n**(3)**\nother costs the Secretary may determine to be eligible.\n##### (d) Evaluation and annual report\nEach eligible entity receiving a grant under this section shall provide for an independent evaluation of the activities carried out using such grant and submit to the Secretary an annual report that includes\u2014\n**(1)**\na description of how the grant was used;\n**(2)**\nthe performance of each program assistance with such grant with respect to, at a minimum, the performance indicators described under section 113 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2323 ), as applicable, and disaggregated\u2014\n**(A)**\nby subgroups of students described in section 1111(c)(2)(B) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(c)(2)(B) ); and\n**(B)**\nby each special population; and\n**(3)**\na quantitative analysis of the effectiveness of each such program.\n##### (e) Definitions\nIn this section:\n**(1) Agricultural education**\nThe term agricultural education means career and technical education that is focused on agriculture, including classroom or laboratory instruction, work-based learning, and leadership education delivered through career and technical student organizations.\n**(2) Eligible entity**\nThe term eligible entity has the meaning given the term eligible recipient in section 3(21)(A) of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302(21)(A) ).\n**(3) Eligible partner**\nThe term eligible partner means\u2014\n**(A)**\nan institution of higher education or a consortium of such institutions; or\n**(B)**\na community stakeholder relevant to a program to be funded under this section, including a labor organization, a local or regional business or industry, or a local workforce development board.\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $5,000,000, to remain available through fiscal year 2028.",
      "versionDate": "2025-08-08",
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
        "updateDate": "2025-09-18T20:18:45Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4945ih.xml"
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
      "title": "GO Ag Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GO Ag Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Growing Opportunities in Agriculture Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Education to award grants for new agricultural education programs in secondary schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T04:18:25Z"
    }
  ]
}
```
