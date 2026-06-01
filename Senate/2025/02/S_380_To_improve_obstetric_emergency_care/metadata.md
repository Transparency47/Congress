# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/380
- Title: Rural Obstetrics Readiness Act
- Congress: 119
- Bill type: S
- Bill number: 380
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-03-20T11:03:17Z
- Update date including text: 2026-03-20T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/380",
    "number": "380",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Rural Obstetrics Readiness Act",
    "type": "S",
    "updateDate": "2026-03-20T11:03:17Z",
    "updateDateIncludingText": "2026-03-20T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2026-03-19T14:00:02Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-04T17:49:03Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WV"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "DE"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s380is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 380\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Ms. Hassan (for herself, Ms. Collins , Mrs. Britt , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo improve obstetric emergency care.\n#### 1. Short title\nThis Act may be cited as the Rural Obstetrics Readiness Act .\n#### 2. Obstetric emergency training program\nSection 330O of the Public Health Service Act ( 42 U.S.C. 254c\u201321 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (4), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(5) developing, and facilitating access to, an evidence-based program to train practitioners in rural health care facilities without dedicated obstetric units to provide emergency obstetric services during pregnancy, labor, delivery, or the postpartum period, including training on how to prepare for, identify, stabilize, and safely transfer, as appropriate and within the scope of practice of an individual practitioner, a woman experiencing labor, delivery, obstetric hemorrhage, severe hypertension, cardiac conditions, perinatal mental health conditions, substance use, sepsis, or other conditions, as appropriate. ;\n**(2)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively;\n**(3)**\nby inserting after subsection (b) the following:\n(c) Training program for eligible practitioners in rural health care facilities A training program described in subsection (a)(5) shall include an assessment of obstetric training needs for rural health care facilities without dedicated obstetric units. In developing the training program, a recipient of a grant under such subsection shall\u2014 (1) work in consultation with at least one representative from a national medical society that has experience or expertise in rural health care delivery in each of the fields of gynecology and obstetrics, emergency medicine, family medicine, and anesthesiology; and (2) facilitate access to obstetric readiness training via regional training partnerships and technical assistance to rural health care facilities. ; and\n**(4)**\nin subsection (e), as so redesignated, by adding at the end the following: In addition to amounts appropriated under the previous sentence, for grants for the purpose described in subsection (a)(5), there are authorized to be appropriated $5,000,000 for the period of fiscal years 2026 through 2028 .\n#### 3. Grant funding for equipment and supplies\nPart D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ) is amended by inserting after section 330A\u20132 the following:\n330A\u20133. Program of support for obstetric services (a) In general The Secretary shall award grants, contracts, or cooperative agreements to eligible entities to integrate obstetric readiness training curriculum into rural health care settings, build workforce capacity, and purchase equipment necessary to manage obstetric emergencies. (b) Use of funds A recipient of funds under this section shall use such funds for the purpose described in subsection (a), which may include any of the following: (1) Purchasing or providing equipment and technical assistance to train practitioners who are not specialized in obstetrics in preparing for, identifying, stabilizing, and transferring, as appropriate and within the scope of practice of the practitioner, individuals experiencing obstetric emergencies. (2) Purchasing or providing equipment necessary to prepare for, identify, stabilize, or transfer, as appropriate, individuals experiencing obstetric emergencies. (3) Developing and carrying out protocols for transfer of patients to other facilities and network engagement with other facilities. (4) Hiring additional personnel or paying the salaries of personnel. (5) Establishing training opportunities to enable non-obstetric health professionals to gain exposure to, and expertise in, the delivery of obstetric services, including through clinical rotations, fellowships, or cross-training clinicians in other specialties. (6) Enabling clinical educators to coordinate, develop, and implement comprehensive interdisciplinary trainings, including team-based simulation training for providers who may need to respond to an obstetric emergency. (c) Eligible entities To be eligible to receive a grant under this section, an entity shall\u2014 (1) be\u2014 (A) a rural hospital, critical access hospital (as determined under section 1820(c)(2) of the Social Security Act), or a rural emergency hospital (as defined in section 1861(kkk)(2) of the Social Security Act) that is located in a maternity care health professional target area or a rural area (as defined by the Secretary); or (B) a consortium of 3 entities that includes at least 2 entities described in subparagraph (A); and (2) agree to carry out the program described in subsection (a), in coordination with other federally funded maternal and child health programs, to the extent practicable, and in consultation with other maternal and child health programs in the same geographic area. (d) Definitions In this section\u2014 (1) the term maternity care health professional target area means a primary care health professional shortage area that is experiencing a shortage of maternity health care professionals, as identified under section 332(k); and (2) the term rural area has the meaning given such term by the Federal Office of Rural Health Policy. (e) Authorization of appropriations To carry out this section, there is authorized to be appropriated $15,000,000 for the period of fiscal years 2026 through 2029. .\n#### 4. Pilot program for teleconsultation\nPart D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ), is amended by inserting after section 330A\u20133, as added by section 3, the following:\n330A\u20134. Pilot program for teleconsultation (a) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration and in consultation with the Administrator of the Centers for Medicare & Medicaid Services, shall award grants or cooperative agreements to States, political subdivisions of States, and Indian Tribes and Tribal organizations (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act) to support the provision of urgent maternal health care in rural facilities without a dedicated obstetric unit, including by\u2014 (1) supporting the development of statewide or regional maternal health care telehealth access programs; and (2) supporting the improvement of existing statewide or regional maternal health care telehealth access programs described in subsection (b). (b) Statewide or regional maternal health care telehealth access programs A maternal health care telehealth access program described in this section, with respect to which an award under subsection (a) may be used, shall\u2014 (1) be a statewide or regional network of maternal health care teams that provide urgent support to rural non-obstetric settings of care; (2) support and further develop organized State or regional networks of maternal health care teams to provide urgent consultative support to rural non-obstetric settings of care; (3) conduct an assessment of urgent maternal health consultation needs among providers in rural non-obstetric settings of care; (4) provide assurances that the physicians responsive to the tele-consultation line are credentialed within their employing facility and can provide consultation where the patient is receiving care consistent with State requirements to provide care to individuals experiencing labor, delivery, obstetric hemorrhage, severe hypertension in pregnancy and postpartum, cardiac conditions related to or exacerbated by pregnancy, perinatal mental health conditions, substance use during pregnancy or the postpartum period, sepsis during pregnancy or after pregnancy end, or other conditions, as appropriate; (5) provide rapid statewide or regional clinical telephone or telehealth consultations when requested between the maternal care teams and providers in rural emergency non-obstetric settings; and (6) provide information to health care providers about available maternal health services for people in the community and assist with referrals to specialty care and community or behavioral health resources. (c) Reporting An entity receiving an award under this section shall submit a report to the Secretary, in such manner and containing such information as the Secretary may require, not later than 18 months after initial receipt of the grant. (d) Authorization of appropriations To carry out this section, there is authorized to be appropriated $5,000,000 for the period of fiscal years 2026 through 2029. .\n#### 5. Study on obstetric units in rural areas\nThe Secretary of Health and Human Services shall\u2014\n**(1)**\nconduct a study that maps maternity ward closures and regional patterns of patient transport and examines models for regional partnerships for rural obstetric care; and\n**(2)**\nnot later than 3 years after the date of enactment of this Act, submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce and the Committee on Education and Workforce of the House of Representatives, a report on the results of the study conducted under paragraph (1).",
      "versionDate": "2025-02-04",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-12",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1254",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rural Obstetrics Readiness Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-11T18:22:18Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-04-11T18:21:14Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-11T18:21:51Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-11T18:22:07Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-04-11T18:21:29Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-04-11T18:21:39Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-04-11T18:21:09Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-04-11T18:20:55Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-04-11T18:21:22Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-04-11T18:20:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-07T15:08:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "Senate",
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
          "measure-id": "id119s380",
          "measure-number": "380",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s380v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Obstetrics Readiness Act</strong></p><p>This bill creates and expands federal grant programs within the Health Resources and Services Administration (HRSA) to increase capacity to provide emergency obstetric health services in rural areas or areas without practitioners or facilities specializing in obstetric services.\u00a0</p><p>Specifically,\u00a0HRSA must establish a program for providing grants to certain hospitals or\u00a0consortiums that include hospitals in rural areas or areas with maternal health care professional shortages for training, developing a workforce, and purchasing equipment relating to obstetric emergencies. In addition, the bill requires\u00a0HRSA\u2019s Alliance for Innovation on Maternal Health Capacity program to provide grants for training on emergency obstetric services for practitioners in rural health care facilities without dedicated obstetric units. HRSA must also establish a pilot program to provide grants to government entities for developing or improving telehealth access programs to support urgent maternal health care in rural facilities without a dedicated obstetric unit.\u00a0</p>"
        },
        "title": "Rural Obstetrics Readiness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s380.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Obstetrics Readiness Act</strong></p><p>This bill creates and expands federal grant programs within the Health Resources and Services Administration (HRSA) to increase capacity to provide emergency obstetric health services in rural areas or areas without practitioners or facilities specializing in obstetric services.\u00a0</p><p>Specifically,\u00a0HRSA must establish a program for providing grants to certain hospitals or\u00a0consortiums that include hospitals in rural areas or areas with maternal health care professional shortages for training, developing a workforce, and purchasing equipment relating to obstetric emergencies. In addition, the bill requires\u00a0HRSA\u2019s Alliance for Innovation on Maternal Health Capacity program to provide grants for training on emergency obstetric services for practitioners in rural health care facilities without dedicated obstetric units. HRSA must also establish a pilot program to provide grants to government entities for developing or improving telehealth access programs to support urgent maternal health care in rural facilities without a dedicated obstetric unit.\u00a0</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s380"
    },
    "title": "Rural Obstetrics Readiness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Obstetrics Readiness Act</strong></p><p>This bill creates and expands federal grant programs within the Health Resources and Services Administration (HRSA) to increase capacity to provide emergency obstetric health services in rural areas or areas without practitioners or facilities specializing in obstetric services.\u00a0</p><p>Specifically,\u00a0HRSA must establish a program for providing grants to certain hospitals or\u00a0consortiums that include hospitals in rural areas or areas with maternal health care professional shortages for training, developing a workforce, and purchasing equipment relating to obstetric emergencies. In addition, the bill requires\u00a0HRSA\u2019s Alliance for Innovation on Maternal Health Capacity program to provide grants for training on emergency obstetric services for practitioners in rural health care facilities without dedicated obstetric units. HRSA must also establish a pilot program to provide grants to government entities for developing or improving telehealth access programs to support urgent maternal health care in rural facilities without a dedicated obstetric unit.\u00a0</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s380"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s380is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Rural Obstetrics Readiness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Obstetrics Readiness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve obstetric emergency care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:51Z"
    }
  ]
}
```
