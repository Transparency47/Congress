# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3287?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3287
- Title: Pregnancy.Gov Act
- Congress: 119
- Bill type: HR
- Bill number: 3287
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-04-17T08:06:59Z
- Update date including text: 2026-04-17T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3287",
    "number": "3287",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Pregnancy.Gov Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:06:59Z",
    "updateDateIncludingText": "2026-04-17T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "TX"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "GA"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "SC"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WI"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "TN"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-05-09",
      "state": "CA"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "MN"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "SC"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "VA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "NY"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3287ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3287\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mrs. Harshbarger (for herself, Mr. Babin , Mr. Crenshaw , Mr. McCormick , Mrs. Biggs of South Carolina , Mr. Fitzgerald , Mr. Bilirakis , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Health and Human Services to establish a clearinghouse of ZIP-Code based information to expecting mothers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pregnancy.Gov Act .\n#### 2. Pregnancy.gov\nThe Public Health Service Act is amended by adding at the end the following:\nXXXIV Pregnancy.gov 3401. Website (a) Website Not later than 1 year after the date of enactment of this section, the Secretary shall publish a public website entitled pregnancy.gov . The Secretary may not delegate implementation or administration of such website below the level of the Office of the Secretary. Such website shall include the following: (1) A clearinghouse of relevant resources available for pregnant women. (2) A series of questions through which a user is able to generate a list of relevant resources of interest within the user\u2019s ZIP Code. (3) A means to direct the user to identify whether to list the relevant resources of interest that are available online or within 1, 5, 10, 50, and 100 miles of the user. (4) A mechanism to provide for the submission of feedback on how user-friendly and helpful the website was in providing the tailored information the user was seeking. (5) A mechanism for users to take an assessment through the portal and provide consent to use the user\u2019s contact information which the Secretary may use to conduct outreach via phone or email to follow up with users on additional resources that would be helpful for the users to review. (b) Resource list aggregation (1) In general The Secretary shall invite States to provide recommendations of relevant resources referred to in subsection (a)(3). (2) Criteria for making recommendations The Secretary shall develop criteria to provide to the States to determine whether resources recommended as described in paragraph (1) should appear on the website. Such criteria shall include the requirement that the relevant resource is not a prohibited entity and the requirement that the relevant resource has been engaged in providing services for a minimum of 3 consecutive years. (3) Grant program (A) In general The Secretary shall provide grants to States to establish or support a system that\u2014 (i) aggregates relevant resources referred to in subsection (a)(3), in accordance with the criteria developed under paragraph (2); and (ii) may be coordinated, to the extent determined appropriate by the State, by a statewide, regionally based, or community-based public or private entity. (B) Applications To be eligible to receive a grant under subparagraph (A), a State shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including a plan for outreach and awareness activities, and a list of relevant resources that would be included in the State system supported by the grant. (c) Prohibition regarding certain entities Relevant resources listed on the website established under this section, and any additional resources promoted by the Secretary, may not include any resource offered by a prohibited entity. No prohibited entity may receive a grant provided under subsection (b)(3). (d) Services in different languages The Secretary shall ensure that the website under this section provides the widest possible access to services for families who speak languages other than English. (e) Reporting requirements (1) In general Not later than 180 days after the date on which the website is established under this section, the Secretary shall submit to Congress a report on\u2014 (A) the traffic of the website; (B) user feedback on the accessibility and helpfulness of the website in tailoring to the user\u2019s needs; (C) insights on gaps in relevant resources with respect to services for pregnant and postpartum women, or women parenting young children; (D) suggestions on how to improve user experience and accessibility based on user feedback and missing resources that would be helpful to include in future updates; and (E) certification that no prohibited entities are listed as a relevant resource or are in receipt of a grant under subsection (b)(3). (2) Confidentiality The report under paragraph (1) shall not include any personal identifying information regarding individuals who have used the website. (f) Funding (1) Website Except as provided in paragraph (2), this section shall be carried out using amounts available under the heading General Departmental Management\u2014Office of the Secretary\u2014Department of Health and Human Services under the Departments of Labor, Health and Human Services, and Education, and Related Agencies Appropriations Act. (2) Grant program (A) In general Subsection (b)(3) shall be carried out using amounts available for\u2014 (i) the State Personal Responsibility Education Program under section 513 of the Social Security Act; (ii) title X of the Public Health Service Act; or (iii) the provisions of law specified in clauses (i) and (ii). (B) Authorized amount Of the amounts specified in subparagraph (A), the Secretary may use not more than $50,000,000 for the period of fiscal years 2026 through 2030. (3) Rule of construction Nothing in this section may be construed as prohibiting the appropriation of funds to carry out this Act. (g) Definitions In this section: (1) Abortion The term abortion means the use or prescription of any instrument, medicine, drug, or any other substance or device to intentionally\u2014 (A) kill the unborn child of a woman known to be pregnant; or (B) terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) after viability, to produce a live birth and preserve the life and health of the child born alive; (ii) to remove a dead unborn child; or (iii) to treat an ectopic pregnancy. (2) Born alive The term born alive has the meaning given such term in section 8(b) of title 1, United States Code. (3) Prohibited entity The term prohibited entity means an entity, including its affiliates, subsidiaries, successors, and clinics that performs, induces, refers for, or counsels in favor of abortions, or provides financial support to any other organization that conducts such activities. (4) Relevant resources The term relevant resources means the Federal, State, local governmental, and private resources that serve pregnant and postpartum women, or women parenting young children, in the categories of the following topics: (A) Mentorship opportunities, including pregnancy and parenting help and case management resources. (B) Health and well-being services, including women\u2019s medical services such as obstetrical and gynecological support services for women, abortion pill reversal, breastfeeding, general health services, primary care, and dental care. (C) Financial assistance, work opportunities, nutrition assistance, childcare, and education opportunities for parents. (D) Material or legal support, including transportation, food, nutrition, clothing, household goods, baby supplies, housing, shelters, maternity homes, tax preparation, legal support for child support, family leave, breastfeeding protections, and custody issues. (E) Recovery and mental health services, including services with respect to addiction or suicide intervention, intimate partner violence, sexual assault, rape, sex trafficking, and counseling for women and families surrounding the unexpected loss of a child. (F) Prenatal diagnostic services, including disability support organizations, medical interventions for a baby, perinatal hospice resources, pregnancy and infant loss support, and literature on pregnancy wellness. (G) Healing and support services for abortion survivors and their families. (H) Services providing childcare, adoption, foster care, and short-term childcare services and resources. (I) Comprehensive information on alternatives to abortion. (J) Information about abortion risks, including complications and failures. (K) Links to information on child development from moment of conception. (5) Unborn child The term unborn child has the meaning given such term in section 1841(d) of title 18, United States Code. (6) Website The term website means the public website entitled pregnancy.gov required to be established under subsection (a). .",
      "versionDate": "2025-05-08",
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
        "updateDate": "2025-05-28T12:29:12Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3287ih.xml"
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
      "title": "Pregnancy.Gov Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pregnancy.Gov Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Health and Human Services to establish a clearinghouse of ZIP-Code based information to expecting mothers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:48:26Z"
    }
  ]
}
```
