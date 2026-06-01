# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3681?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3681
- Title: Leveraging Educational Opportunity Networks Act
- Congress: 119
- Bill type: HR
- Bill number: 3681
- Origin chamber: House
- Introduced date: 2025-06-03
- Update date: 2025-11-21T12:04:06Z
- Update date including text: 2025-11-21T12:04:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-03: Introduced in House

## Actions

- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3681",
    "number": "3681",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "E000296",
        "district": "3",
        "firstName": "Dwight",
        "fullName": "Rep. Evans, Dwight [D-PA-3]",
        "lastName": "Evans",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Leveraging Educational Opportunity Networks Act",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:06Z",
    "updateDateIncludingText": "2025-11-21T12:04:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
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
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T16:04:00Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NC"
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
      "sponsorshipDate": "2025-08-19",
      "state": "NC"
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
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3681ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3681\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. Evans of Pennsylvania (for himself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Labor to award grants to certain entities to establish workforce training programs.\n#### 1. Short title\nThis Act may be cited as the Leveraging Educational Opportunity Networks Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAbout 60 percent of workers in the United States do not hold a 4-year college degree. These almost 70,000,000 workers in the United States without a bachelor\u2019s degree have gained marketable skills through on-the-job training, boot camps, micro-credentialing programs, community colleges, and many other types of job training programs. Short-term workforce training programs have been growing in demand. Polling data finds that people in the United States are increasingly seeking education programs that are relevant for work and suited to their personal needs. Over the past 2 years, even as community college enrollment has dropped, boot camps, and online training programs are growing in size and market share.\n**(2)**\nFederal job training policy should focus on making more funding available to support high-quality sectoral training programs, including wraparound supports. Policymakers should prioritize options that boosts Federal funding for cohort-based sectoral training programs, including through the Workforce Innovation and Opportunity Act. Complementary models could include grant competitions that encourage cross-sector partnerships and support training investments for high priority roles (e.g. the Department of Commerce\u2019s Good Jobs Challenge).\n**(3)**\nFurther, the working poor are a pool of invisible talent and the source for a revitalized workforce to fill high-demand jobs in manufacturing, energy, health, technology, and science sectors of the economy. More than 32 percent of the United States labor force, or 51.9 million workers, currently make less than $15 an hour and 1.1 million workers earn wages at the prevailing Federal minimum wage ($7.25 an hour, or $14,137 a year).\n**(4)**\nUsing United States Census Bureau data, the Bureau of Labor Statistics determined that 6,300,000 workers were living at or below the official poverty level in 2020, which represented 4.1 percent of the total workforce (U.S. Department of Labor, September 2022) and 25 percent of working families can be considered working poor.\n**(5)**\nThe United States is experiencing a long-term labor shortage, The Demographic Drought . As the size of the United States working age population shrinks, the country is experiencing record-low rates of labor participation, and it has the lowest birth rates in history.\n**(6)**\nEconomic growth is dependent on a reliable supply of skilled and ready to work employees. The economy is expected to add 12,000,000 jobs between 2020 and 2030. Science, technology, engineering, and mathematics ( STEM ) occupations will experience the highest growth rates. Occupations in the STEM field are expected to grow 8 percent by 2029, compared with 3.7 percent for all other occupations.\n**(7)**\nAs of April 2023, there were 10,100,000 job openings and only 5,700,000 people looking for work (U.S. Department of Labor April 2023 Employment Report).\n**(8)**\nAbout 60 percent of workers do not have a bachelor\u2019s degree, and about 45 percent of workers have a bachelor\u2019s degree.\n**(9)**\nMore than 39 million people in the United States have attended some college but earned no degree.\n**(10)**\nA 2015 evaluation by the Aspen Institute\u2019s Economic Opportunities Program documented that poor, unemployed, and under employed students who earned an industry-recognized credential landed high skill entry level positions and earned 18 percent more in income than a similar group of people who did not receive this type of training.\n**(11)**\nAfrican American men face a range of challenges in the labor market which hinder their employment opportunities. African American men comprise about 13 percent of the male population, but 35 percent of those incarcerated. One in 3 African American men born today can expect to be incarcerated in his lifetime, compared to 1 in 6 Latino men and 1 in 17 White men. African American women are similarly affected where 1 in 18 African American women born in 2001 are likely to be incarcerated sometime in her life, compared to 1 in 111 white women. The effect of these realities is devastating and enduring, formerly incarcerated people are unemployed at a rate of over 27 percent which is higher than the total United States unemployment rate during any historical period, including the Great Depression.\n**(12)**\nMore must be done to break the cycle of generational poverty and reduce racial, economic, and social disparities in the United States.\n#### 3. Establishment of grant program\n##### (a) Grants authorized\n**(1) In general**\nThe Secretary of Labor shall award grants, on a competitive basis, to eligible entities to develop and implement workforce training programs.\n**(2) Geographic diversity**\nTo the maximum extent practicable, the Secretary shall ensure geographical diversity in selecting eligible entities to receive grants under subsection (a).\n##### (b) Eligible entity\nAn eligible entity is a consortium of the following:\n**(1)**\nAn organization described in section 501(c)(3) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(c)(3) );\n**(2)**\nA national training organization with dues paying affiliated members in at least 10 States;\n**(3)**\nAn accredited institution, not including an institution of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 101 )); or\n**(4)**\nAn institution that operates a post-secondary, career and technical network of accredited, dues paying institutions.\n##### (c) Uses of funds\n**(1) In general**\nAn eligible entity that receives a grant under this Act shall use such grant to\u2014\n**(A)**\ndevelop and implement a career and technical education program as described in subsection (d);\n**(B)**\noffer a program to enrollees prior to the participation of such enrollees in a workforce training program that supports the enrollees in transitioning to a learning environment, which shall include\u2014\n**(i)**\nopportunities to foster camaraderie among enrollees;\n**(ii)**\nprepare enrollees for training success;\n**(iii)**\ntutoring and employment readiness coaching; and\n**(iv)**\ncognitive behavioral techniques to support a change in the perception and thinking of enrollees;\n**(C)**\nprovide\u2014\n**(i)**\nneed-based stipends to enrollees in a workforce training program to assist enrollees in completing training programs;\n**(ii)**\nconflict resolution services and regular check-ins on a monthly basis to an employer that employs an enrollee who has completed a workforce training program offered by the eligible entity; and\n**(iii)**\nsupportive services to enrollees;\n**(D)**\npartner with an employer that\u2014\n**(i)**\npays a living wage;\n**(ii)**\nprovides avenues for career growth and professional development to enrollees who complete a program of an eligible entity that the employer partnered with; and\n**(iii)**\nengages in the career training process, including\u2014\n**(I)**\nserving on an industry advisory group;\n**(II)**\nassisting the eligible entity with establishing a career and technical education program as described in subsection (d);\n**(III)**\nsponsoring internships; and\n**(IV)**\nparticipating in mock interview hiring sessions and hiring fairs;\n**(E)**\ndetermine the qualifications and credentials required for employment by the employers identified in paragraph (4);\n**(F)**\nassess and understand the demand of employers for employees in the local areas in which;\n**(G)**\nidentify employers that pay a living wage in the local areas in which an eligible entity operates a career and technical education program;\n**(H)**\nidentify employers and industry sectors in which job growth is expected to occur;\n**(I)**\nproduce\u2014\n**(i)**\nan analysis of existing and emerging in-demand industry sectors and occupations and the employment needs of employers in such industry sectors; and\n**(ii)**\nan analysis of the knowledge and skills needed to meet the employment needs of the employers in the States in which the entity operates a career and technical education program; and\n**(J)**\nimplement strategies to recruit individuals into the workforce training program and assess prospective enrollees.\n**(2) Required allocation of funds**\nAn eligible entity that receives a grant under this Act shall use at least 70 percent of such grant for the uses of funds described in subparagraphs (A) and (C)(i).\n##### (d) Career and technical education program\nA career and technical education program developed and implemented under this Act shall\u2014\n**(1)**\nbe developed to meet the in-demand needs of employers in the local area in which such program is being implemented;\n**(2)**\npay enrollees a living wage;\n**(3)**\nbe at least 12 weeks in duration;\n**(4)**\nupon an enrollee completing such a program, result in the enrollee earning a recognized post-secondary credential;\n**(5)**\noperate in at least 10 States;\n**(6)**\nprioritize enrollees who read at no higher than the 6th grade reading level; and\n**(7)**\nensure that at least 50 percent of the individuals enrolled the program are\u2014\n**(A)**\noffenders (as defined in section 3(38) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102(3)(38) ));\n**(B)**\nlow-income and economically isolated individuals (including individuals who are from rural, urban, and historically disadvantaged communities); and\n**(C)**\nfrom populations that have been underserved or adversely affected by persistent poverty or inequality.\n##### (e) Application\n**(1) In general**\nTo be eligible to receive a grant under this Act, an eligible entity shall submit an application at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Priority**\nThe Secretary shall prioritize eligible entities that propose to carry out a workforce training program in the following industries:\n**(A)**\nConstruction.\n**(B)**\nDisaster relief and recovery services.\n**(C)**\nIndustrial manufacturing.\n**(D)**\nFood manufacturing.\n**(E)**\nSupply chain management and services.\n**(F)**\nInformation technology.\n**(G)**\nFinancial services.\n**(H)**\nShip building and other defense-related industries.\n**(I)**\nHealth care.\n##### (f) Report\nNot later than 1 year after and eligible entity receives a grant under this Act, and on an annual basis thereafter, each eligible entity shall submit to the Secretary of Labor a report on the following:\n**(1)**\nThe earnings of each enrollee\u2014\n**(A)**\nprior to entering into a career and technical education program operated by such eligible entity; and\n**(B)**\n6 months after completing such program.\n**(2)**\nThe percentage of program participants who are in unsubsidized employment\u2014\n**(A)**\nafter 30 days and prior to 90 days after exit from such program; and\n**(B)**\nafter 280 days and prior to 365 days after exit from such program;\n**(3)**\nThe starting wages of the program participants described in paragraph (2)(A); and\n**(4)**\nThe percentage of program participants who obtain a recognized postsecondary credential during participation in, or within 1 year after exit from, the program.\n##### (g) Definitions\nIn this Act:\n**(1) Career and technical education**\nThe term career and technical education has the meaning given the term in section 3(5) of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ).\n**(2) Living wage**\nThe term living wage means a wage that one full-time worker earns that covers the cost of the minimum basic needs of the worker and the family of the worker for the area in which such worker lives.\n**(3) Supportive services**\nThe term supportive services means services such as transportation, child care, dependent care, housing, and needs-related payments, that are necessary to enable an individual to participate in a career and technical education program carried out under this Act.\n**(4) WIOA terms**\nThe terms local area and recognized postsecondary credential have the meanings given the terms in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n#### 4. Authorization of appropriations\nTo carry out this Act, there is authorized to be appropriated $30,000,000 for each of the fiscal years 2026 through 2029.",
      "versionDate": "2025-06-03",
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
        "updateDate": "2025-06-23T14:04:52Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3681ih.xml"
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
      "title": "Leveraging Educational Opportunity Networks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Leveraging Educational Opportunity Networks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Labor to award grants to certain entities to establish workforce training programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-09T13:18:22Z"
    }
  ]
}
```
