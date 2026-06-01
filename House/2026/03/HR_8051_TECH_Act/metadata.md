# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8051?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8051
- Title: TECH Act
- Congress: 119
- Bill type: HR
- Bill number: 8051
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-05-27T08:06:01Z
- Update date including text: 2026-05-27T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8051",
    "number": "8051",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "TECH Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:01Z",
    "updateDateIncludingText": "2026-05-27T08:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:02:20Z",
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
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "UT"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8051ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8051\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Mr. Kennedy of Utah (for himself and Mr. Owens ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo ensure that qualified technical schools offering certain career pathway and job training programs have the same access to Federal grants as 2-year and 4-year institutions of higher education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transforming Education through College and Hands-On Training Act or the TECH Act .\n#### 2. Modification to eligibility for certain Federal grant programs\n##### (a) In general\nNotwithstanding any other provision of law, a qualified technical school shall be eligible to participate in any covered Federal grant program to the same extent, and on the same basis, as any 2-year or 4-year institution of higher education.\n##### (b) Agency action\nNot later than 180 days after the date of enactment of this Act, each Secretary concerned shall\u2014\n**(1)**\nmodify the eligibility criteria and application procedures for the covered Federal grant programs under the jurisdiction of such Secretary, as necessary, to ensure that qualified technical schools are eligible to participate in the program to the same extent, and on the same basis, as 2-year and 4-year institutions of higher education, as required under subsection (a); and\n**(2)**\nissue guidance that specifies how grants under such program should be dispersed among qualified technical schools and 2-year and 4-year institutions of higher education to ensure that the sectors and occupations described in subsection (c)(4)(A)(ii) have an adequate workforce pipeline to replace the aging and retiring current employees.\n##### (c) Definitions\nIn this section:\n**(1) 2-year or 4-year institution of higher education**\nThe term 2-year or 4-year institution of higher education means in institution described in section 101(a) of the Higher Education Act of 1965 (20 U.S.C 1001(a)).\n**(2) Covered Federal grant program**\nThe term covered Federal grant program means the following:\n**(A)**\nGrants made by the Department of Education under\u2014\n**(i)**\nthe Strengthening Institutions Program authorized under part A of title III of the Higher Education Act of 1965 ( 20 U.S.C. 1057 et seq. );\n**(ii)**\nthe Federal TRIO Program authorized under chapter 1 of subpart 2 of part A of title IV of the Higher Education Act of 1965 (20 U.S.C. 20 U.S.C. 1070a\u201311 et seq. ); and\n**(iii)**\nthe Child Care Access Means Parents in School Program (commonly known as the CCAMPIS Program ) authorized under section 419N of the Higher Education Act of 1965 ( 20 U.S.C. 1070e ).\n**(B)**\nGrants made by the Department of Labor under the Strengthening Community Colleges Training Grants Program authorized under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ).\n**(3) Eligible career pathway program**\nThe term eligible career pathway program means a program that\u2014\n**(A)**\nmeets the requirements of section 484(d)(2) of the Higher Education Act of 1965 ( 20 U.S.C. 1091(d)(2) );\n**(B)**\nis listed on the provider list under section 122(d) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3152(d) );\n**(C)**\nis part of a career pathway, as defined in section 3 of that Act ( 29 U.S.C. 3102 ); and\n**(D)**\nis aligned to a program of study as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ).\n**(4) Eligible job training program**\n**(A) In General**\nThe term eligible job training program means a career and technical education program at qualified technical school that\u2014\n**(i)**\nis a program of at least 150 clock hours of instruction, but less than 600 clock hours of instruction, or an equivalent number of credit hours, offered by a qualified technical school during a minimum of 8 weeks, but less than 15 weeks;\n**(ii)**\nprovides training that is\u2014\n**(I)**\nin a sector or occupation determined by the Secretary concerned to be essential for national security, public safety, supply chain security, transportation, critical manufacturing or infrastructure, healthcare, or public health; and\n**(II)**\naligned with the requirements of high-skill, high-wage, or in-demand industry sectors or occupations in the State or local area, as determined by an industry or sector partnership;\n**(iii)**\nis a program of training services, and provided through an eligible training provider, as described under section 122(d) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3152(d) );\n**(iv)**\nprovides a student, upon completion of the program, with a recognized postsecondary credential that is recognized by employers in the relevant industry, including credentials recognized by industry or sector partnerships in the relevant industry in the State or local area where the industry is located and the job training program is provided;\n**(v)**\nhas been determined by the school (after validation of that determination by an industry or sector partnership) to provide academic content, an amount of instructional time, and a recognized postsecondary credential that are sufficient to\u2014\n**(I)**\nmeet the hiring requirements of potential employers; and\n**(II)**\nsatisfy any applicable educational prerequisite requirement for professional licensure or certification, so that the student who completes the program and seeks employment qualifies to take any licensure or certification examination needed to practice or find employment in an occupation that the program prepares students to enter;\n**(vi)**\nmay include integrated education and training;\n**(vii)**\nmay be offered as part of an eligible career pathway program; and\n**(viii)**\ndoes not exceed by more than 50 percent the minimum number of clock hours required for training if the State has established such a requirement.\n**(B) Approval by the Secretary**\nIn the case of a program that is seeking to establish eligibility as an eligible job training program under this paragraph, the Secretary of Education shall make a determination about whether the program meets the requirements of this paragraph not more than 60 days after the date on which such program is submitted for consideration as an eligible job training program.\n**(C) Additional assurance**\nThe Secretary of Education shall not determine that a program is an eligible job training program in accordance with subparagraph (B) unless the Secretary receives a certification from the appropriate State board containing an assurance that the program meets the requirements of subparagraph (A).\n**(5) Qualified technical school**\nThe term qualified technical school means a postsecondary vocational institution (as defined in section 102(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(c) ) that\u2014\n**(A)**\noffers an eligible career pathway program or an eligible job training program; and\n**(B)**\nis located in the United States.\n**(6) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Education, with respect to covered Federal grant programs administered by the Department of Education; and\n**(B)**\nthe Secretary of Labor, with respect to a covered Federal grant programs administered by the Department of Labor.\n**(7) WIOA terms**\nThe terms industry or sector partnership , in-demand industry sector or occupation , recognized postsecondary credential , and State board have the meanings given such terms in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).",
      "versionDate": "2026-03-24",
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
        "actionDate": "2026-04-22",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4371",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TECH Act",
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
        "updateDate": "2026-04-01T20:32:06Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8051ih.xml"
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
      "title": "TECH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T17:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transforming Education through College and Hands-On Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T17:23:31Z"
    },
    {
      "title": "TECH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T17:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that qualified technical schools offering certain career pathway and job training programs have the same access to Federal grants as 2-year and 4-year institutions of higher education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T17:18:24Z"
    }
  ]
}
```
