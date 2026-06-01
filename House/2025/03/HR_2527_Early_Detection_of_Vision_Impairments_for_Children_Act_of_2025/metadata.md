# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2527
- Title: Early Detection of Vision Impairments for Children Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2527
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-04-29T08:06:50Z
- Update date including text: 2026-04-29T08:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2527",
    "number": "2527",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "V000131",
        "district": "33",
        "firstName": "Marc",
        "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
        "lastName": "Veasey",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Early Detection of Vision Impairments for Children Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-29T08:06:50Z",
    "updateDateIncludingText": "2026-04-29T08:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:00:35Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "OR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "DC"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NM"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "MN"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "IN"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "MS"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "OH"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-17",
      "state": "NC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MI"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "VA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "VA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "KS"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2527ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2527\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Veasey (for himself and Mr. Bilirakis ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to improve children\u2019s vision and eye health through grants to States, territories, and Tribal organizations, and the provision of technical assistance to support those efforts.\n#### 1. Short title\nThis Act may be cited as the Early Detection of Vision Impairments for Children Act of 2025 .\n#### 2. Statewide early vision detection and intervention programs and systems related to children\u2019s vision and eye health\nPart Q of title III of the Public Health Service Act ( 42 U.S.C. 280h et seq. ) is amended by adding at the end the following:\n399Z\u20133. Statewide early vision detection and intervention programs and systems related to children\u2019s vision and eye health (a) Grants or cooperative agreements (1) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration, shall make awards of grants or cooperative agreements to eligible entities to develop and implement statewide early detection and intervention programs and systems related to children\u2019s vision and eye health. (2) Eligibility To be eligible to receive a grant or cooperative agreement under paragraph (1), an entity shall\u2014 (A) be a State, territory, Indian Tribe or Tribal organization, or Urban Indian organization, including a State or community department of children and families, health, or public health, or a State educational agency; and (B) submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (3) Use of awards Amounts provided under a grant or cooperative agreement under paragraph (1) shall be used for three or more of the following activities: (A) Implementing early detection practices (such as vision screening) and intervention initiatives for the purpose of identifying vision concerns in children as they engage in the medical, home, public educational, or early learning setting, promoting referrals to eye care, and promoting the use of evidence-based and age-appropriate standards guided by nationally recognized and uniform guidelines. (B) Developing an integrated approach to State-level data collection and management to advance State-based performance improvement systems and uniform children\u2019s vision and eye health guidelines across relevant and appropriate State-level jurisdictions. (C) Identifying strategies to improve eye health outcomes, expand access to care, and reduce health disparities for the detection, diagnosis, and treatment of ocular disease and eye conditions in children who experience barriers to eye care from rural and underserved populations. (D) Raising awareness by providing the public, including families, guardians (permanent, legal, or temporary), family or community caregivers, and early learning settings with children\u2019s vision and eye health information that is accurate, accessible, culturally and linguistically competent, comprehensive, up-to-date, and evidence-based or evidence-informed. (E) Establishing a coordinated public health system for vision care and eye health, including early detection, referral to eye care, diagnosis and intervention, and follow-up for children. (F) Providing referrals to wrap-around vision services, as necessary, for a future of independent living. (4) Collaboration with necessary community and State partners In carrying out activities under this subsection, the recipient of a grant or cooperative agreement shall consult with necessary community and State partners, including State agencies responsible for the administration of title V of Social Security Act (the Maternal and Child Health Block Grant Program), title XIX of such Act (the Medicaid Early Periodic Screening, Diagnosis, and Treatment Program), title XXI of such Act (the State Children\u2019s Health Insurance Program), and parts B and C of the Individuals with Disabilities Education Act, the Indian Health Service, and consumer groups for the purposes of program and policy development, collaboration, and improvement. (5) Evaluation and report (A) In general An entity that receives a grant or cooperative agreement under this subsection shall annually submit to the Secretary a report that describes the activities carried out under the grant or agreement, including a description of the period of performance covered under the report, the scope of activities carried out during such period, the outcomes of such activities, and a demonstration of whether funding recipients have met project goals for the designated time period outlined in the initial application under paragraph (2). (B) Availability of reports The Secretary shall make available to the general public the annual reports under subparagraph (A). (b) Technical assistance (1) In general The Secretary shall provide eligible entities under subsection (a) with technical support in the development, implementation, and enhancement of activities described in such subsection. (2) Grants The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall award grants or cooperative agreements to provide technical assistance to eligible entities to\u2014 (A) develop, maintain, and improve data collection systems related to children\u2019s vision screening, evaluation, diagnosis, and intervention services; (B) disseminate information for stakeholders, including States and local governments, Indian Tribes, Tribal organizations, Urban Indian organizations, public health departments, and nonprofit organizations, to launch effective strategies and interventions in preventing and treating childhood vision disorders; (C) conduct applied research related to early vision screening and intervention programs and outcomes; (D) ensure quality monitoring of vision screening, evaluation, and intervention programs and systems; and (E) assist eligible entities in coordinating on best practices and maintaining national goals related to vision and eye health. (3) Evaluation (A) In general Not later than 4 years after the date of enactment of this section, the recipient of a grant or cooperative agreement under this subsection shall evaluate the activities conducted with funds received under this section and submit a report to the Secretary on the outcomes, costs, and program effectiveness of such activities. (B) Contents A report under subparagraph (A) shall be in such form and contain such information as the Secretary determines appropriate. (C) Submission Upon determination by the Secretary that a report under subparagraph (A) meets the requirements of this paragraph, the recipient shall submit the report to Congress. (4) Eligibility To be eligible to receive a grant or cooperative agreement under this subsection, an entity shall be a public or nonprofit private organization or institution, with expertise, or demonstrated proficiency, in developing systems-based approaches to children\u2019s vision and eye health for the purpose of providing technical assistance in relation to one or more of the activities described in subsection (a). (c) Coordination and consultation The Secretary shall coordinate and consult with the Health Resources and Services Administration, the Centers for Disease Control and Prevention, the Centers for Medicare & Medicaid Services, the Administration for Communities and Families, the Indian Health Service, and the Department of Education on recommendations for policy development at the Federal, State, and Tribal levels with the private sector, including consumer, medical, and other health and education child serving not-for-profit organizations with respect to early detection and intervention programs and systems. (d) Definitions In this section: (1) Indian Tribe The term Indian Tribe has the meaning given to the term Indian tribe in section 102 of the Federally Recognized Indian Tribe List Act of 1994. (2) State educational agency The term State educational agency has the meaning given such term in section 8101 of the Elementary and Secondary Education Act of 1965. (3) Tribal organization The term Tribal organization has the meaning given such term in section 4 of the Indian Self-Determination and Education Assistance Act. (4) Urban Indian organization The term Urban Indian organization has the meaning given such term in section 4 of the Indian Health Care Improvement Act. (e) Authorization of appropriations There are authorized to be appropriated\u2014 (1) to carry out this section, other than subsection (a)(5), $5,000,000 for each of fiscal years 2026 through 2030; and (2) to carry out subsection (a)(5), $5,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-03-31",
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
        "updateDate": "2025-04-08T12:51:28Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2527ih.xml"
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
      "title": "Early Detection of Vision Impairments for Children Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Early Detection of Vision Impairments for Children Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to improve children's vision and eye health through grants to States, territories, and Tribal organizations, and the provision of technical assistance to support those efforts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T04:18:29Z"
    }
  ]
}
```
