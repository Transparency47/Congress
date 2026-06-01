# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5308
- Title: Service Starts At Home Act
- Congress: 119
- Bill type: HR
- Bill number: 5308
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-12-10T07:11:05Z
- Update date including text: 2025-12-10T07:11:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5308",
    "number": "5308",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001136",
        "district": "3",
        "firstName": "Herbert",
        "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
        "lastName": "Conaway",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Service Starts At Home Act",
    "type": "HR",
    "updateDate": "2025-12-10T07:11:05Z",
    "updateDateIncludingText": "2025-12-10T07:11:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:01:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5308ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5308\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Conaway introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Education to carry out grant programs to encourage student participation in local government and volunteer service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Service Starts At Home Act .\n#### 2. Grants to support internships in local government\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary shall carry out a program under which the Secretary makes grants, on a competitive basis, to eligible entities to support paid internships within units of local government for secondary school students and students who are qualified undergraduates at institutions of higher education in the State in which the entity is located.\n##### (b) Application\nTo be considered for a grant under subsection (a), an eligible entity shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Local government internship program\nEach eligible entity that receives a grant under subsection (a) shall use such grant to carry out a program under which the entity\u2014\n**(1)**\nidentifies appropriate paid internship opportunities within units of local government for secondary school students and students who are undergraduates at institutions of higher education in the State in which the entity is located;\n**(2)**\nestablishes a process for the selection of students to fill such internships;\n**(3)**\ndetermines hourly rates of pay and other terms and conditions applicable to such internships; and\n**(4)**\npays the costs incurred in providing such internships.\n##### (d) Accommodations and educational standards\nIn carrying out the internship program under subsection (c), an eligible entity shall\u2014\n**(1)**\nwork with institutions of higher education to ensure that the work performed by interns has educational value and meets applicable educational standards; and\n**(2)**\nseek to provide reasonable employment-related accommodations to interns who have childcare needs, transportation difficulties, or other such challenges, which may include accommodations such as flexible work schedules for interns and allowing interns to telework to the extent determined practicable by the eligibility entity concerned.\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $50,000,000 for each of fiscal years 2026 through 2030.\n#### 3. Scholarship for volunteer service programs\n##### (a) Funding\n**(1) State programs**\n**(A) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall carry out a program under which the Secretary makes allocations to States, in accordance with subparagraph (B), to carry out the scholarship program under subsection (b).\n**(B) Allocations to States**\nFrom the amount appropriated to carry out this section for each fiscal year and not reserved under paragraph (2), each State that has an application approved by the Secretary under subparagraph (C) shall be allocated an amount in proportion to number of students enrolled in the public elementary schools and secondary schools in the State for the previous school year relative to the total number of students enrolled in the public elementary schools and secondary schools for such school year in every State that has an application approved by the Secretary under such subparagraph.\n**(C) State application**\nTo be eligible to receive an allocation under subparagraph (B), a State shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Federal program**\nFrom the amount appropriated to carry out this section for each fiscal, the Secretary may reserve not more than 20 percent to carry out the Federal supplemental scholarship program under subsection (c).\n##### (b) State administered scholarship program\n**(1) In general**\nEach State that receives an allocation under subsection (a)(2) shall use such allocation to carry out a program under which the State awards scholarships, on a competitive basis, to eligible students who demonstrate a commitment to volunteer service work.\n**(2) Application**\nA student who seeks a scholarship under this subsection shall submit an application to the State at such time, in such manner, and containing such information as the State may require.\n**(3) Student eligibility**\nTo be eligible to receive a scholarship under this subsection a student shall meet the following criteria:\n**(A) First-time applicant**\nIn the case of a first-time applicant for a scholarship under this subsection, the student shall\u2014\n**(i)**\nbe enrolled\u2014\n**(I)**\nin a secondary school and be in the final year of a program of study leading to a regular high school diploma; or\n**(II)**\nin an institution of higher education; and\n**(ii)**\nhave completed at least 100 hours of volunteer service work in the preceding school year (or another one-year period determined by the Secretary).\n**(B) Renewal applicant**\nIn the case of a student who received a scholarship under this subsection for an academic year and is seeking a scholarship for a subsequent academic year, the student shall\u2014\n**(i)**\nbe enrolled in an institution of higher education;\n**(ii)**\nbe in good academic standing (as determined by the institution); and\n**(iii)**\nhave completed at least 100 hours of volunteer service work in the preceding school year (or another one-year period determined by the Secretary).\n**(4) Renewal process**\nSubject to the availability of funds for such purpose, a State that receives an allocation under subsection (a) shall\u2014\n**(A)**\naward a scholarship to each renewal applicant who meets the requirements described in paragraph (3)(B); and\n**(B)**\nestablish a streamlined process under which renewal applicants can apply for such scholarships with minimal documentation required.\n**(5) Priority**\nIn awarding scholarships under this subsection, a State shall\u2014\n**(A)**\nin accordance with paragraph (4), first award scholarships to renewal applicants described in paragraph (3)(B); and\n**(B)**\nfrom any funds remaining after awarding such scholarships, award scholarships to first-time applicants described in paragraph (3)(A).\n**(6) Use of funds**\nA scholarship received by a student under this subsection may be used by such student only to pay the student\u2019s costs of attendance at an institution of higher education.\n**(7) Duration**\nEach scholarship under this subsection shall be awarded for a period of one academic year. A student may receive a scholarship under this subsection for a total period of not more than 4 academic years.\n**(8) Amount**\nThe amount of each scholarship under this subsection shall be\u2014\n**(A)**\n$1,000, for a student who completed at least 100 hours, but less than 138 hours, of volunteer service work in the preceding school year (or another one-year period determined by the Secretary);\n**(B)**\n$1,500, for a student who completed at least 138 hours, but less than 175 hours, of volunteer service work in the preceding school year (or another one-year period determined by the Secretary);\n**(C)**\n$2,000, for a student who completed at least 175 hours, but less than 213 hours, of volunteer service work in such period;\n**(D)**\n$2,500, for a student who completed at least 213 hours, but less than 250 hours, of volunteer service work in such period; and\n**(E)**\n$3,000, for a student who completed at least 250 hours of volunteer service work in such period.\n##### (c) Federal supplemental scholarship program\n**(1) In general**\nFrom amounts reserved under subsection (a)(2), the Secretary may carry out a program under which the Secretary awards supplementary funds, on a competitive basis, directly to eligible students for volunteer service work.\n**(2) Amount**\nThe amount of supplementary funds awarded to each student under paragraph (1) shall be determined by the Secretary.\n**(3) Priority**\nIn awarding scholarships under this subsection, the Secretary shall prioritize the award of funds to students who have not received a scholarship under subsection (b).\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $100,000,000 for each of fiscal years 2026 through 2030.\n#### 4. Recognition of achievement in community service\nThe Secretary shall carry out a program to recognize elementary schools, secondary schools, local educational agencies, and institutions of higher education based on their overall volunteer achievement and contributions to community service.\n#### 5. Definitions\nIn this Act:\n**(1) ESEA definitions**\nThe terms elementary school , local educational agency , regular high school diploma , secondary school , Secretary , and State have the meanings given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Cost of attendance**\nThe term cost of attendance has the meaning given that term in section 472 of the Higher Education Act of 1965 ( 20 U.S.C. 1087ll ).\n**(3) Eligible entity**\nThe term eligible entity means a State or a unit of local government.\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given that term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(5) Unit of local government**\nThe term unit of local government means\u2014\n**(A)**\na county, municipality, town, township, village, parish, borough, or other unit of general government below the State level; or\n**(B)**\na governing body of an Indian Tribe or Tribal organization.\n**(6) Volunteer service work**\nThe term volunteer service work \u2014\n**(A)**\nmeans unpaid acts of volunteer service conducted for or on behalf of a government or other nonprofit organization, which may include a community-based organization, faith-based organization, school, national service program, civic or fraternal service organization, local government agency, or other such organization; and\n**(B)**\ndoes not include acts of proselytizing, conducting worship services, religious instruction, political lobbying, court ordered service, or service conducted primarily for the benefit of the family of a student eligible for a scholarship under section 3.",
      "versionDate": "2025-09-11",
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
        "actionDate": "2025-09-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2782",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Service Starts At Home Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-09-24T15:00:20Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5308ih.xml"
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
      "title": "Service Starts At Home Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T07:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Service Starts At Home Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Education to carry out grant programs to encourage student participation in local government and volunteer service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T07:18:27Z"
    }
  ]
}
```
