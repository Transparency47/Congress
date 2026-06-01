# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7524?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7524
- Title: Older Workers’ Bureau Act
- Congress: 119
- Bill type: HR
- Bill number: 7524
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-04-03T08:05:49Z
- Update date including text: 2026-04-03T08:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7524",
    "number": "7524",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Older Workers\u2019 Bureau Act",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:49Z",
    "updateDateIncludingText": "2026-04-03T08:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:00:30Z",
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
      "sponsorshipDate": "2026-02-12",
      "state": "OR"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7524ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7524\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Beyer (for himself, Ms. Bonamici , and Ms. Garcia of Texas ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish in the Department of Labor an Older Workers\u2019 Bureau, to establish a data hub and a technical assistance center at the Department of Labor related to employment of older workers and the effect of older employment on retirement security, to establish grant programs related to the employment of older workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Older Workers\u2019 Bureau Act .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nOf the 5,350,000 workers expected to be added to the United States Workforce over the next 10 years, 2,070,000 will be older than 55, according to the Bureau of Labor Statistics.\n**(2)**\nFrom 2004 to 2024, the share of older workers in the labor force grew from 16 percent to over 23 percent.\n**(3)**\nUnder the Supplemental Poverty Measure (SPM) the older adult poverty rate went up to 15 percent in 2024 from 9.5 percent during the COVID\u201319 pandemic.\n**(4)**\nOlder adults in the bottom 20 percent of wealth died on average 9 years earlier than those in the top 20 percent.\n**(5)**\nPhysically and psychologically difficult working conditions are widespread and damaging for older workers.\n**(6)**\nOlder workers are more likely to be involuntary part time, gig, or temporary workers than prime age workers.\n**(7)**\nMore than 1/3 or 35.1 percent of women ages 55 and older earned low wages, defined as $17.37 per hour or less.\n**(8)**\nConcern about age discrimination amongst older workers reached a record high during the COVID\u201319 pandemic and remains consistently and persistently high at 64 percent.\n**(9)**\nMore than 1,000,000 older workers were pushed out or voluntarily left the labor force during the COVID\u201319 pandemic.\n**(10)**\nWhile some older workers have returned to the labor force since the beginning of the COVID\u201319 pandemic, many have struggled to obtain work and others fear returning to unsafe working conditions.\n**(11)**\nSignificant numbers of women between the age of 55 and 64 have unexpected workforce exits due to health and care giving responsibilities.\n**(12)**\nOlder workers need specific policy consideration and assistance that could be met by establishing an Older Workers\u2019 Bureau within the Department of Labor.\n##### (b) Purpose\nIt is the purpose of this Act to promote productive, inclusive, and welfare-enhancing employment opportunities and workplaces for older workers through research, policy development, outreach, and grant programs.\n#### 3. Definitions\nFor the purposes of this Act:\n**(1) Bureau**\nThe term Bureau means the Older Workers\u2019 Bureau established under section 4(a).\n**(2) Director**\nThe term Director means the Director of the Older Workers\u2019 Bureau.\n**(3) Older worker**\nThe term older worker means an individual who\u2014\n**(A)**\nis not younger than 55 years of age; and\n**(B)**\n**(i)**\nis employed;\n**(ii)**\nis seeking employment; or\n**(iii)**\nwants employment, is available for employment, and has sought employment within the preceding 12 months.\n**(4) Secretary**\nThe term Secretary means the Secretary of Labor.\n#### 4. Older Worker\u2019s Bureau\n##### (a) Establishment\nThere is established in the Department of Labor a bureau to be known as the Older Workers\u2019 Bureau , which shall be under the direction of the Director of the Older Workers\u2019 Bureau.\n##### (b) Personnel\n**(1) Director**\n**(A) Appointment**\nNot later than 1 year after the date of enactment of this Act, the President shall appoint a Director to lead the Bureau.\n**(B) Inclusion in Executive Schedule**\nSection 5315 of title 5, United States Code, is amended by adding at the end the following:\nDirector of the Older Workers\u2019 Bureau, Department of Labor. .\n**(2) Staff**\nThe Secretary, acting through the Director, shall employ such staff as the Secretary determines necessary to carry out the functions of the Bureau, at such rates of pay as the Secretary may provide, subject to the provisions of chapter 51 and subchapter III of chapter 53 of such title, relating to classification and General Schedule pay rates. The Secretary may not reduce staffing levels of the Bureau below that necessary to carry out such functions efficiently.\n##### (c) Functions\nThe Director shall promote the welfare and improve the working conditions of older workers, increase the efficiency, capacity, and coordination of programs serving older workers, and advance the employment opportunities of older workers, including by carrying out, with respect to older workers, the following:\n**(1)**\nResearch relating to\u2014\n**(A)**\npublic benefits that support\u2014\n**(i)**\nthe economic and financial security of such workers; and\n**(ii)**\naccess and retention of safety net supports for such workers who earn an annual income that is not more than 200 percent of the Federal poverty guidelines;\n**(B)**\naccess for such workers to\u2014\n**(i)**\nleave under the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2601 et seq. ); and\n**(ii)**\nworkplace flexibility opportunities to support the needs of such workers with respect to managing personal health and caregiving responsibilities;\n**(C)**\ntailored, person-centered approaches to job training and adult education (including on soft skills, financial literacy education, and digital literacy) for such workers;\n**(D)**\naccess to savings and tax-advantaged opportunities for such workers to provide a path toward a financially secure retirement;\n**(E)**\nage discrimination in the workplace, including how such discrimination is, and could be, addressed and how such discrimination impacts such workers;\n**(F)**\nwages paid to such workers, including whether such wages are commensurate with experience;\n**(G)**\njob security for such workers, including\u2014\n**(i)**\nthe probability of job loss; and\n**(ii)**\nresources available to such workers in the event of job separation;\n**(H)**\nretirement readiness for such workers, including the impact of Federal policies on retirement readiness for such workers; and\n**(I)**\nthe impact of Federal policies on the equitable treatment (including with respect to race, sex, sexual orientation, gender identity, education, ability, and residence) of such workers and their retirement.\n**(2)**\nPolicy development.\n**(3)**\nOutreach and education.\n**(4)**\nGrant program administration.\n**(5)**\nCoordinating Federal research relating to such workers.\n**(6)**\nImproving access to data on the economic situation of such workers.\n##### (d) Office quarters\nThe Secretary shall furnish sufficient quarters, office furniture, and equipment as the Secretary determines necessary to carry out the functions of the Bureau.\n##### (e) Report\nThe Director\u2014\n**(1)**\nshall annually submit to the Secretary a report\u2014\n**(A)**\non the activities of the Bureau with respect to older workers, including with respect to the functions described in subsection (c);\n**(B)**\nthat catalogs Federal programs that support the employment, economic success, and well-being of such workers;\n**(C)**\nthat identifies issues with respect to such workers that may be improved with Federal support; and\n**(D)**\nthat makes recommendations to promote the welfare and economic and financial security, improve the working conditions, increase the efficiency, capacity, and coordination of programs serving older workers, and advance the employment opportunities of such workers; and\n**(2)**\nmay publish such report, as directed by the Secretary.\n##### (f) Consultation\nIn carrying out the functions of the Bureau, the Secretary, acting through the Director, may consult with\u2014\n**(1)**\nFederal agencies that have jurisdiction over matters involving older adults, including\u2014\n**(A)**\nthe Social Security Administration, including the Office of Retirement and Disability Policy;\n**(B)**\nthe Department of Health and Human Services, including the Administration for Community Living, the Centers for Medicare and Medicaid Services, the National Institute for Occupational Safety and Health, and the National Institute on Aging;\n**(C)**\nthe Equal Employment Opportunity Commission;\n**(D)**\nthe Department of Veterans Affairs;\n**(E)**\nthe Department of the Treasury, including the Internal Revenue Service; and\n**(F)**\nthe Department of Housing and Urban Development; and\n**(2)**\nany other Federal agency that the Secretary determines has relevant expertise.\n##### (g) Applicability\nThe Secretary shall take such actions as are necessary to ensure the Bureau is operational not later than 1 year after the date of enactment of this Act.\n#### 5. Research grants\nNot later than 180 days after the date on which the Bureau is operational, the Secretary, acting through the Director, shall carry out a program to award, on a competitive basis, grants to facilitate, with respect to older workers, research\u2014\n**(1)**\ndesigned to identify areas that could benefit from additional research for the purposes of\u2014\n**(A)**\nidentifying and eliminating barriers to securing employment, job retention, and reemployment for such workers; and\n**(B)**\nidentifying policies that the Federal Government may implement to assist such workers; and\n**(2)**\nas determined appropriate by the Secretary, into the areas identified under paragraph (1).\n#### 6. Grants to combat structural ageism\n##### (a) In general\nNot later than 180 days after the date on which the Bureau is operational, the Secretary, acting through the Director, shall carry out a program to award, on a competitive basis, grants to covered institutions to\u2014\n**(1)**\nfacilitate activities, services, and programs to improve the welfare of older workers;\n**(2)**\ncombat structural ageism;\n**(3)**\nimprove employment opportunities for older workers; and\n**(4)**\ncreate a more diverse and inclusive workplace.\n##### (b) Priority\nIn making grants under subsection (a), the Secretary shall give priority to a covered institution that is located in an area that has no training programs specifically targeted to disadvantaged older workers.\n##### (c) Covered institutions defined\nFor the purposes of this section, the term covered institution means any of the following:\n**(1)**\nAn employer.\n**(2)**\nAn employer association.\n**(3)**\nA labor organization.\n**(4)**\nA nonprofit with expertise in older workers.\n**(5)**\nA worker organization.\n**(6)**\nAnother institution determined appropriate by the Secretary.\n#### 7. Authorization of appropriations\nTo carry out sections 5 and 6, there is authorized to be appropriated $10,000,000 for each fiscal year after fiscal year 2027.",
      "versionDate": "2026-02-12",
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
        "updateDate": "2026-02-26T18:27:50Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7524ih.xml"
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
      "title": "Older Workers\u2019 Bureau Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Older Workers\u2019 Bureau Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish in the Department of Labor an Older Workers' Bureau, to establish a data hub and a technical assistance center at the Department of Labor related to employment of older workers and the effect of older employment on retirement security, to establish grant programs related to the employment of older workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:27Z"
    }
  ]
}
```
