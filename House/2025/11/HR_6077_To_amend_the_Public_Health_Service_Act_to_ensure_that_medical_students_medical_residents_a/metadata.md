# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6077?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6077
- Title: HEAL-AI Act
- Congress: 119
- Bill type: HR
- Bill number: 6077
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2025-12-02T15:33:24Z
- Update date including text: 2025-12-02T15:33:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6077",
    "number": "6077",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001300",
        "district": "44",
        "firstName": "Nanette",
        "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
        "lastName": "Barrag\u00e1n",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "HEAL-AI Act",
    "type": "HR",
    "updateDate": "2025-12-02T15:33:24Z",
    "updateDateIncludingText": "2025-12-02T15:33:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:05:35Z",
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
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6077ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6077\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Ms. Barrag\u00e1n (for herself, Mr. Lieu , and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to ensure that medical students, medical residents, and medical faculty receive education and training in the deployment of artificial intelligence in the medical profession, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthcare Education in AI Literacy Act or the HEAL-AI Act .\n#### 2. Artificial intelligence medical education\nPart C of title VII of the Public Health Service Act ( 42 U.S.C. 293k et seq. ) is amended by adding at the end the following:\nIII Artificial intelligence medical education 749C. Purpose The purpose of this subpart is to create a program of grants to be administered by the Health Resources and Services Administration for the education and training of medical students, medical residents, and medical faculty in the deployment of artificial intelligence in the medical profession. 749D. Definitions In this subpart: (1) Artificial intelligence or AI The term artificial intelligence or AI means, with respect to the medical profession, a machine-based system\u2014 (A) capable of generating predictions, recommendations, or decisions that influence real medical profession environments, as aligned with a set of objectives defined by humans; and (B) that employs inputs derived from both machine and human sources to perceive and process data from real or virtual environments to provide information or facilitate actions. (2) Education and training The term education and training \u2014 (A) means, with respect to the medical profession, competency-based medical education and training for skill-building and decisionmaking to improve health outcomes and patient care; and (B) includes\u2014 (i) the use of data and data analysis; (ii) training such as virtual simulation and case studies; and (iii) student assessment to provide\u2014 (I) feedback and personalize learning; and (II) the latest updates to health care. (3) Medical resident The term medical resident means a graduate from an accredited medical school who is participating in a postgraduate medical residency training program at a residency sponsoring institution. (4) Medical student The term medical student means a student who attends a qualified medical school. (5) Qualified medical school The term qualified medical school means an accredited school of medicine or accredited school of osteopathic medicine. (6) Residency sponsoring institution The term residency sponsoring institution means an institution that sponsors a postgraduate medical residency training program accredited by the Accreditation Council for Graduate Medical Education. (7) Secretary The term Secretary means the Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration. 749E. Grant program to support artificial intelligence literacy for medical students, residents, and faculty (a) Grant program The Secretary shall establish and carry out a program under which the Secretary makes grants, on a competitive basis, to qualified medical schools or residency sponsoring institutions for the education and training of medical students, medical residents, and medical faculty of such schools or institutions in the deployment of artificial intelligence in the medical profession. (b) Applications (1) Eligibility To be eligible to receive a grant under this section, a qualified medical school or residency sponsoring institution shall include in the application submitted under section 796, in addition to any information required by such section\u2014 (A) the desired grant amount, not to exceed $100,000; and (B) the assurances described in paragraph (2). (2) Required assurances The assurances described in this paragraph are the following: (A) An assurance that the school or institution will comply with the reporting requirements under section 749F. (B) An assurance that the school or institution will provide a description of the need for medical students, medical residents, or medical faculty of such school or institution, as appropriate, to become literate in artificial intelligence and to indicate how the grant would facilitate\u2014 (i) bringing interdisciplinary expertise to the development and provision of the AI curriculum; (ii) completing formal program evaluation regarding effectiveness of the local implementation of AI; and (iii) sharing tools and learning with the broader education community to support relationship building and continued education within the medical education community. (c) Use of funds (1) In general A grant under this section may only be used for the education and training of medical students, medical residents, and medical faculty in the deployment of artificial intelligence to understand the immediate effectiveness of training in competencies of the technology, including\u2014 (A) utilizing AI for medical diagnostics, treatment recommendations, and predictive analytics; (B) integrating AI tools into clinical support and decision-making processes; (C) understanding the ethical implications of AI in health care, such as bias, patient data privacy, and algorithm transparency; (D) studying the impact of artificial intelligence in medical ethics use cases; and (E) conducting practical educational demonstrations or laboratories to exhibit the variety of use cases artificial intelligence may be deployed in a health profession field. (2) Limitation on use for administrative costs Not more than 10 percent of the amount of a grant under this section may be used for administrative costs, including the preparation of the annual reports required under section 749F. (3) Prohibition on publishing in predatory journals A grant under this section may not be used to support the publication of any piece in a predatory journal. (d) Renewal A qualified medical school or residency sponsoring institution that receives a grant under this section may apply for renewal of such grant for one or more additional grant periods. (e) Access; Priority In making grants under this section, the Secretary shall\u2014 (1) promote access to emerging technologies; and (2) give priority to schools or institutions that provide care to medically underserved communities. (f) Collaborating with outside entities In carrying out the activities described in subsection (c)(1), a qualified medical school or residency sponsoring institution may\u2014 (1) collaborate with academic, nonprofit, and government entities, including other educational departments within the university or college of the qualified medical school, such as departments of computer science, computer engineering, software engineering, data science, computer programming, scientific computing, or any other related field as the Secretary determines appropriate; and (2) consult with\u2014 (A) any of the academic, nonprofit, or government entities described in paragraph (1); or (B) a for-profit entity. (g) Geographic diversity In awarding grants under this section, the Secretary shall ensure that, to the extent practicable, grants are distributed among qualified medical schools and residency sponsoring institutions that serve geographically diverse areas, including urban, suburban, and rural areas across the United States. The Secretary may award grants under this section to not more than two qualified medical schools or residency sponsoring institutions located within the same 2020 United States Census Division. (h) Yearly funding limit A qualified medical school or residency sponsoring institution may not receive more than $100,000 in funding under this section in any fiscal year. 749F. Reporting requirements (a) Annual reports Not later than 180 days after receiving a grant under section 749E, and annually thereafter for the duration of the grant period, a qualified medical school or residency sponsoring institution that receives such grant shall submit to the Secretary a report that includes\u2014 (1) a summary of the educational program goals and objectives and related evidence to support academic progress or advancements made under such grant; (2) the amount of grant funds expended by such school or institution for artificial intelligence education and training; (3) a description of how education and training was integrated into existing curricula, or used to create new curricula including the strategy, approach, and methods to begin development of the resources or curricula; (4) the number of learners that enrolled in and successfully completed at least one course funded by such grant, to become knowledgeable in artificial intelligence literacy; and (5) a list of any entity with which the school or institution collaborated or consulted under section 749E(f). (b) Requirement To make educational material publicly available Not later than 30 days after submitting a report under subsection (a), the qualified medical school or residency sponsoring institution submitting such report shall make publicly available any educational materials funded by the grant with respect to which such report was submitted\u2014 (1) on the website of the school or institution; or (2) on an online academic research portal. 749G. Authorization of appropriations There is authorized to be appropriated to carry out this subpart $1,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-11-18",
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
        "updateDate": "2025-12-02T15:33:24Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6077ih.xml"
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
      "title": "HEAL-AI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEAL-AI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthcare Education in AI Literacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to ensure that medical students, medical residents, and medical faculty receive education and training in the deployment of artificial intelligence in the medical profession, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T01:48:20Z"
    }
  ]
}
```
