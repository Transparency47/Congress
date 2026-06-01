# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3262
- Title: NURSE Act
- Congress: 119
- Bill type: HR
- Bill number: 3262
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-12-19T09:07:57Z
- Update date including text: 2025-12-19T09:07:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-07 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-07 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3262",
    "number": "3262",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "NURSE Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:57Z",
    "updateDateIncludingText": "2025-12-19T09:07:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-07T14:00:30Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
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
      "sponsorshipDate": "2025-05-19",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "NE"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3262ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3262\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Ms. Titus (for herself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo make demonstration grants to eligible local educational agencies or consortia of eligible local educational agencies for the purpose of increasing the numbers of school nurses in public elementary schools and secondary schools.\n#### 1. Short title\nThis Act may be cited as the Nurses for Under-Resourced Schools Everywhere Act or the NURSE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe National Association of School Nurses identifies schools as primary locations to address student health issues. Since a school nurse is the health care provider that many students see on the most regular basis, it is the position of National Association of School Nurses that a professional registered school nurse be present in every school all day, every day.\n**(2)**\nThe American Academy of Pediatrics has recognized the crucial role that school nurses play in children\u2019s health and has called for having a full-time school nurse every day and in every school building.\n**(3)**\nThe school nurse functions as the leader and coordinator of the school health services team, including by carrying out chronic disease management and health promotion as well as facilitating access to a medical home for each child and supporting academic achievement.\n**(4)**\nWith over 25 percent of students managing chronic conditions such as asthma, diabetes, and epilepsy, the presence of a school nurse ensures these children can thrive in a safe and supportive environment.\n**(5)**\nA 2024 Morning Consult public-opinion poll conducted to understand the public perception of school nursing found that 87 percent of adults in the United States have a favorable view of school nurses.\n**(6)**\nAccording to data from the National Association of School Nurses, one-third of schools do not have a school nurse.\n**(7)**\nThe American Federation of Teachers has called for a nurse in every school, as nurses are frontline workers that address an array of health needs and their presence in a school can help to improve student learning.\n**(8)**\nSchool nurses promote wellness and disease prevention to improve health outcomes for our Nation\u2019s children. In addition, school nurses perform early intervention services such as periodic assessments for vision, hearing, and dental problems, in an effort to remove barriers to learning.\n**(9)**\nThe National Association of School Nurses has reported that medication administration to students is one of the most common health-related activities performed in school. As more chronically ill and medically unstable children enter the school system each year, the medical factors that promote and support their academic success increase, including the need for medications that enhance overall health or stabilize chronic conditions.\n**(10)**\nAccording to the American Academy of Pediatrics, students today face increased social and emotional issues, which enhance the need for preventive services and interventions for acute and chronic health issues. School nurses are actively engaged members of school-based mental health teams and spend nearly 32 percent of their time providing mental health services, including universal and targeted interventions, screenings to identify early warning signs and provide referrals to medical providers, and crisis planning.\n**(11)**\nCommunicable and infectious diseases account for millions of school days lost each year. Data illustrates that when students have access to a registered nurse in school, immunization rates increase.\n#### 3. Increasing the number of school nurses\n##### (a) Definitions\nIn this section:\n**(1) ESEA terms**\nThe terms elementary school , local educational agency , secondary school , and State educational agency have the meanings given to the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Acuity**\nThe term acuity , when used with respect to a level, means the level of a patient\u2019s sickness, such as a chronic condition, which influences the need for nursing care.\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na local educational agency in which not less than 20 percent of the children are eligible to participate in the school lunch program established under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. );\n**(B)**\na consortium of local educational agencies described in subparagraph (A); or\n**(C)**\na State educational agency in consortium with local educational agencies described in subparagraph (A).\n**(4) High-need local educational agency**\nThe term high-need local educational agency means a local educational agency described in paragraph (3)(A)\u2014\n**(A)**\nthat serves not fewer than 15,000 children who are eligible to participate in the program described in such paragraph; or\n**(B)**\nfor which not less than 40 percent of the children served by the agency are eligible to participate in the program described in such paragraph.\n**(5) Nurse**\nThe term nurse means a registered nurse, as defined under State law.\n**(6) Secretary**\nThe term Secretary means the Secretary of Education.\n**(7) Workload**\nThe term workload , when used with respect to a nurse, means the amount of time the nurse takes to provide care and complete the other tasks for which the nurse is responsible.\n##### (b) Demonstration grant program authorized\n**(1) In general**\nFrom amounts appropriated to carry out this section, the Secretary of Education shall award demonstration grants, on a competitive basis, to eligible entities to pay the Federal share of the costs of increasing the number of school nurses in the public elementary schools and secondary schools served by the eligible entity, which may include hiring a school nurse to serve schools in multiple school districts.\n**(2) S EA s**\nIn the case of an eligible entity described in subsection (a)(3)(C) that receives a grant under paragraph (1), such entity shall use amounts received under the grant to award subgrants to the local educational agencies that are members of the entity, and reserve not more than 10 percent of such grant funds to support statewide activities to meet a variety of health needs, which may include hiring a nurse to provide training and technical assistance to schools statewide that meet the criteria established in subsection (d)(2)(A).\n##### (c) Applications\n**(1) In general**\nAn eligible entity desiring a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Contents**\nEach application submitted under paragraph (1) shall include information with respect to the current (as of the date of application) number of school nurses, student health acuity levels, and workload of school nurses in each of the public elementary schools and secondary schools served by the eligible entity.\n##### (d) Priority\nIn awarding grants under this section, the Secretary shall give priority to each application submitted by an eligible entity that\u2014\n**(1)**\nis a high-need local educational agency, a consortium composed of high-need local education agencies, or a State educational agency in consortium with high-need local education agencies; and\n**(2)**\ndemonstrates\u2014\n**(A)**\nthe greatest need for new or additional nursing services among students in the public elementary schools and secondary schools served by the agency or consortium; or\n**(B)**\nthat the eligible entity does not have a school nurse in any of the public elementary schools and secondary schools served by the local educational agency or the consortium-member local educational agencies.\n##### (e) Federal share; non-Federal share\n**(1) Federal share**\nThe Federal share of a grant under this section\u2014\n**(A)**\nshall not exceed 75 percent for each year of the grant; and\n**(B)**\nin the case of a multiyear grant, shall decrease for each succeeding year of the grant, in order to ensure the continuity of the increased hiring level of school nurses using State or local sources of funding following the conclusion of the grant.\n**(2) Non-Federal share**\nThe non-Federal share of a grant under this section may be in cash or in-kind, and may be provided from State resources, local resources, contributions from private organizations, or a combination thereof.\n**(3) Waiver**\nThe Secretary may waive or reduce the non-Federal share of an eligible entity receiving a grant under this section if the eligible entity demonstrates an economic hardship.\n##### (f) Report\nNot later than 2 years after the date on which a grant is first made to a local educational agency under this section, the Secretary shall submit to Congress a report on the results of the demonstration grant program carried out under this section, including an evaluation of\u2014\n**(1)**\nthe effectiveness of the program in increasing the number of school nurses; and\n**(2)**\nthe impact of any resulting enhanced health of students on learning, such as academic achievement, attendance, and classroom time.\n##### (g) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section such sums as may be necessary for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-05-07",
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
        "updateDate": "2025-05-22T17:16:51Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3262ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make demonstration grants to eligible local educational agencies or consortia of eligible local educational agencies for the purpose of increasing the numbers of school nurses in public elementary schools and secondary schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T06:12:48Z"
    },
    {
      "title": "NURSE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T06:09:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NURSE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nurses for Under-Resourced Schools Everywhere Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T06:08:15Z"
    }
  ]
}
```
