# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5202?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5202
- Title: BABIES Act
- Congress: 119
- Bill type: HR
- Bill number: 5202
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2025-12-06T06:53:29Z
- Update date including text: 2025-12-06T06:53:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5202",
    "number": "5202",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001234",
        "district": "3",
        "firstName": "Kelly",
        "fullName": "Rep. Morrison, Kelly [D-MN-3]",
        "lastName": "Morrison",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "BABIES Act",
    "type": "HR",
    "updateDate": "2025-12-06T06:53:29Z",
    "updateDateIncludingText": "2025-12-06T06:53:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
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
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
          "date": "2025-09-08T16:05:05Z",
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
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5202ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5202\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Ms. Morrison (for herself and Mrs. Hinson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo address maternity care shortages and promote optimal maternity outcomes by expanding access to birth centers and exploring more effective payment models for birth center care, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Better Availability of Birth Centers Improves Outcomes and Expands Savings Act or the BABIES Act .\n#### 2. Grants to improve access to freestanding birth center services\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. Strong start birth center grants to assist birth centers with start-up or expansion costs to expand access to birth center services in underserved areas (a) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration, may award grants to eligible birth centers that are accredited, or intend to seek accreditation, as birth centers by a nationally recognized accrediting body such as the Commission for the Accreditation of Birth Centers, or that have the intention of seeking such accreditation, for the purposes described in subsection (b). (b) Use of funds A birth center receiving a grant under this section may use such grant funds for any of the following purposes: (1) Renovation, expansion, or construction of a birth center facility. (2) Purchasing or updating equipment for a birth center. (3) Accreditation and State licensure activities. (c) Grants; grant amounts For each of fiscal years 2026 through 2030, the Secretary shall award grants under this section to up to 15 birth centers, each in an amount of not less than $300,000 and not more than $500,000. (d) Special considerations In awarding grants under this section, the Secretary shall give special consideration to an eligible birth center that\u2014 (1) is located in, or offers services to, a geographic area that\u2014 (A) has been designated under section 332 as a health professional shortage area with respect to maternity care; or (B) has maternity care outcomes that are below a threshold established by the Secretary; and (2) has not previously received a grant under this section. (e) Authorization of appropriations There is authorized to be appropriated to carry out this section $5,000,000 for the period of fiscal years 2026 through 2030. .\n#### 3. Medicaid demonstration program to improve freestanding birth center services\nSection 1903 of the Social Security Act ( 42 U.S.C. 1396b ) is amended by adding at the end the following new subsection:\n(cc) Demonstration program To improve freestanding birth center services (1) Authority The Secretary shall conduct a demonstration program for the purpose of exploring more effective payment models for birth center care in order to improve access to, and the quality and scope of, freestanding birth center services for women with a low-risk pregnancy who are eligible for medical assistance under the State plan under this title or under a waiver of such plan. (2) Deadlines for participation criteria, prospective payment system; planning grants (A) Participation and prospective payment system deadline Not later than 1 year after the date of the enactment of this subsection, the Secretary shall do the following: (i) Publication of participation criteria for freestanding birth centers (I) In general The Secretary shall publish criteria for a freestanding birth center to be certified by a State for purposes of participating in a State demonstration program conducted under this subsection. (II) Requirements The criteria required to be published under subclause (I) shall include the following: (aa) Accreditation At the time of certification for purposes of participating in the demonstration program conducted under this subsection, a freestanding birth center shall be accredited or have completed the initial phase of accreditation from an approved, nationally recognized birth center accreditation body, as determined by the Secretary. (bb) Licensure and other requirements A freestanding birth center shall\u2014 (AA) be licensed, or otherwise approved, by the State to provide prenatal, labor and delivery, postpartum, newborn care, and other ambulatory services for which medical assistance is available under the State plan or waiver under this title; and (BB) comply with such other requirements relating to the health and safety of individuals who receive services furnished by the facility as the State shall establish. (cc) Care coordination A freestanding birth center shall be able to meet care coordination requirements established by the Secretary, including requirements to coordinate care across settings and providers to ensure seamless transitions for patients across the full spectrum of health services, and shall be able to engage in consultation for higher level maternity care services, non-maternity care services, and behavioral health needs, which may include plans for consultation, collaboration and referral, and arrangements with the following: (AA) Federally qualified health centers (and as applicable, rural health clinics) to provide Federally qualified health center services (and as applicable, rural health clinic services) to the extent such services are not provided directly through the birth center. (BB) Other outpatient clinics, including licensed midwifery and physician practices. (CC) Inpatient acute care facilities with obstetrical care units. (dd) Scope of services As determined by the Secretary, a freestanding birth center shall be able to provide peripartum care for women with a low-risk pregnancy and for newborns, consistent with evidence-based guidelines. (ee) Capabilities A freestanding birth center shall have the following capabilities: (AA) In addition to the requirements specified under section 431.53 of title 42, Code of Federal Regulations, and any successor regulation (relating to assurance of transportation), the capability and equipment to provide prenatal, labor and delivery, postpartum, and newborn care for women with a low-risk pregnancy, readiness at all times to initiate emergency procedures to meet unexpected needs of such women and of newborns within the center, including at least 2 qualified staff on-site at every birth, and the ability to facilitate transport to an acute care hospital with an obstetrical care unit when necessary. (BB) An established transfer plan with a receiving hospital with an obstetrical care unit with policies and procedures for timely transport. (CC) Medical consultation available from a licensed board-certified physician with admitting privileges in obstetrics at a nearby hospital, as defined by State law or regulation. (DD) Data collection, storage, and retrieval, including data on intrapartum and postpartum maternal and newborn transfer rates and hospital admissions. (EE) The ability to initiate and document quality improvement programs as required by accreditation that include efforts to maximize patient safety, such as safety checklists, validated training and competency of staff, and emergency preparedness and drills. (ff) Health care providers A freestanding birth center shall employ, or have care delivery arrangements with, both of the following: (AA) A physician licensed to practice within the State or jurisdiction of the birth center. (BB) A midwife that meets or exceeds the education and training standards of the International Confederation of Midwives and who is licensed to practice within the jurisdiction of the birth center. (gg) Non-duplication In carrying out this subsection, the Secretary shall, with respect to a State participating in the demonstration program, establish procedures to prevent, to the greatest extent practicable, the provision of, or payment for, services under the demonstration program for which medical assistance is available under the State plan under this title or waiver of such plan. (ii) Guidance on development of prospective payment system for testing under State demonstration programs (I) In general The Secretary shall issue guidance for States participating in a demonstration program conducted under this subsection to establish a prospective payment system that shall only apply to freestanding birth center services that\u2014 (aa) meet the criteria established under clause (i); and (bb) are furnished by a freestanding birth center participating in such a demonstration program. (II) Requirements The guidance issued by the Secretary under subclause (I) shall, to the greatest extent practicable, provide for\u2014 (aa) a partial facility payment based on units in the case that a pregnant woman is admitted in labor and then needs to be transferred to the hospital in labor before the birth of the baby; (bb) a facility payment for therapeutic rest or for observation short stays to rule out labor; (cc) ensuring payment for the newborn and mother as 2 separate facility payment components; (dd) ensuring payment for nitrous oxide and hydrotherapy supplies costs for pain relief; (ee) ensuring payment for all professional services of health professionals involved in the delivery of care in a birth center, which may include\u2014 (AA) 3 or more prenatal office visits; (BB) observation and triage; (CC) newborn exam and care; and (DD) multiple postpartum, mother, and newborn visits, as needed; (ff) ensuring payment for partial prenatal and postpartum care episodes or for prenatal care only with planned delivery in the hospital and returning for postpartum care in the birth center; and (gg) payment for services provided within\u2014 (AA) in the case of a pregnant woman, the period that commences upon the confirmation of pregnancy when the woman is accepted into care at the freestanding birth center, continues through prenatal care, labor, and delivery, and ends at the completion of the postpartum period (as defined by State law or regulation) with documentation of a plan for continued well woman care, inclusive of at least 2 postpartum care visits; and (BB) in the case of a newborn, a period that continues through the first 28 days of life with documentation of continued infant care. (iii) Publication of an RFP for States to apply for the demonstration program (I) In general The Secretary shall publish a request for proposal (in this clause referred to as an RFP ) for States to establish and test a prospective payment system for freestanding birth center services that\u2014 (aa) meets the criteria established under clause (i); and (bb) are furnished by a freestanding birth center participating in a demonstration program under this subsection. (II) Requirements The RFP published by the Secretary under subclause (I) shall, to the greatest extent practicable, include the following parameters: (aa) States shall have a minimum number of established or developing birth centers. (bb) States shall have a mechanism to recognize or license birth centers. (cc) States shall have at least 1 area that has been designated a maternity care desert. (dd) States shall have areas with maternity care outcomes that are below a certain threshold, as determined by the Secretary. (ee) States shall represent a diverse selection of geographic areas, including rural and underserved areas. (ff) Preference shall be given to States that demonstrate the potential to expand the availability of and access to maternity care services in a demonstration area and increase the quality of services provided by freestanding birth centers without increasing net Federal spending, as determined by the Secretary. (III) Required information A State application to conduct a demonstration program under this subsection shall include the following: (aa) A description of the target population of individuals who are eligible for medical assistance under the State plan under this title or under a waiver of such plan and are to be served under the demonstration program. (bb) A list of the participating freestanding birth centers in the State. (cc) Verification that each participating freestanding birth center meets the participation criteria established in paragraph (2)(A)(i). (dd) A description of the scope of the freestanding birth center services available under the State plan under this title or waiver of such plan for women with a low-risk pregnancy that will be paid for under the prospective payment system tested in the demonstration program. (ee) Verification that the State has agreed to pay for such services at the rate established under the prospective payment system. (ff) An assurance that the State will require freestanding birth centers to submit to the State, and that the State will submit to the Secretary, such information and data as the State or Secretary may require relating to the demonstration program or an episode of care for such a pregnant woman or newborn. (gg) Such other information as the Secretary may require relating to the demonstration program, including with respect to determining the soundness of the proposed prospective payment system. (IV) Deadlines for submission of RFP applications The deadline for a State to submit an application to participate in the demonstration program conducted under this subsection shall be the date that is 90 days after the date on which the Secretary publishes the RFP under subclause (I). (B) Planning grants (i) In general Not later than 18 months after the date of the enactment of this subsection, the Secretary shall award a planning grant to up to 6 States for the purpose of developing a detailed proposal to conduct a demonstration program described in paragraph (3). (ii) Use of funds A State awarded a planning grant under this subparagraph shall use the funds awarded under such grant to\u2014 (I) solicit input with respect to the development of the demonstration program from patients, providers (including certified nurse-midwives, other midwives licensed within the State, and physicians), and other stakeholders; (II) secure participation of freestanding birth centers that meet the criteria established under subparagraph (A)(i), including by providing support for such centers to meet that criteria (including accreditation) in order to maximize the number of freestanding birth centers participating in the demonstration program; and (III) in accordance with the guidance issued under subparagraph (A)(ii), establish a prospective payment system which the State shall use for making payments to freestanding birth centers participating in the demonstration program. (3) State demonstration programs (A) In general Not later than 2 years after the date of the enactment of this subsection, the States selected by the Secretary under paragraph (2)(B)(i) shall begin conducting the demonstration program under this paragraph. (B) Length of demonstration programs A State conducting a demonstration program in accordance with this paragraph shall conduct the program for a 4-year period. (C) Payment for services provided by freestanding birth centers (i) In general For each quarter during the 4-year period during which a State participates in a demonstration program under this subsection, the Secretary shall pay such State an amount equal to the Federal medical assistance percentage (as defined in section 1905(b)) of the total amount expended by such State during such quarter under the prospective payment system established by such State pursuant to paragraph (2)(B)(III) to freestanding birth centers for services that are\u2014 (I) furnished pursuant to the criteria established under paragraph (2)(A)(i) to individuals enrolled in the State plan (or waiver of such plan) of such State under this title; and (II) described in the demonstration program application submitted by such State and approved by the Secretary. (ii) Administrative expenses Amounts expended by a State to conduct a demonstration program in accordance with this paragraph shall be considered, for purposes of subsection (a)(7), to be necessary for the proper and efficient administration of the State plan. (D) Waiver of Statewideness requirement The Secretary shall waive the requirements of section 1902(a)(1) (relating to Statewideness), section 1902(a)(10)(B) (relating to comparability), and any other provision of this title which would be directly contrary to the authority under this subsection as may be necessary for a State to conduct a demonstration program in accordance with this paragraph. (E) Annual reports (i) In general Not later than 2 years after the date on which the first State is selected to conduct a demonstration program under this subsection, and annually thereafter, based on information and data submitted by States in accordance with the assurance provided under paragraph (2)(A)(iii)(III)(ff), the Secretary shall submit to Congress an annual report on all State demonstration programs conducted under this subsection. Each such report shall include, with respect to each such State demonstration program\u2014 (I) an assessment of clinical outcomes for maternity services provided by freestanding birth centers participating in the demonstration program for individuals who are eligible for medical assistance under a State plan under this title or under a waiver of such plan and are women with a low-risk pregnancy with outcomes in comparable demographic and geographic areas, including with respect to\u2014 (aa) the number of births and data on intrapartum and postpartum maternal and newborn transfer rates and hospital admissions; and (bb) the rate of primary and repeat cesarean sections, preterm births, and neonatal intensive care unit admissions; and (II) an assessment of the impact of all the State demonstration programs conducted under this subsection on the Federal and State costs relating to providing freestanding birth center services for individuals who are eligible for medical assistance under a State plan under this title or under a waiver of such plan and are women with a low-risk pregnancy (including with respect to the provision of inpatient, emergency, and ambulatory services) and newborn care, compared to the Federal and State costs related to the provision of\u2014 (aa) freestanding birth center services to such individuals by freestanding birth centers outside of such demonstration programs; and (bb) traditional maternity services as provided in non-birth center clinics and hospital programs. (ii) Recommendations Not later than 6 months before the the last day of the 4-year period for which demonstration programs are conducted under this subsection, the Secretary shall submit to Congress recommendations concerning whether such demonstration programs shall be continued, expanded, modified, or terminated. (4) Funding (A) In general Out of any funds in the Treasury not otherwise appropriated, there is appropriated to the Secretary\u2014 (i) for fiscal year 2027, $3,000,000 for purposes of carrying out paragraph (2)(B); and (ii) for each of fiscal years 2028 through 2031, $6,000,000 for purposes of carrying out the demonstration programs described in paragraph (3). (B) Availability Funds appropriated under subparagraph (A) shall remain available until expended. (5) Definitions In this subsection: (A) Freestanding birth center services The term freestanding birth center services has the meaning given such term in section 1905(l)(3)(A) and includes such other services as the Secretary shall determine for purposes of conducting the demonstration programs described in paragraph (3). (B) Low-risk pregnancy The term low-risk pregnancy means an uncomplicated singleton term pregnancy with a vertex presentation and an expected uncomplicated birth. .",
      "versionDate": "2025-09-08",
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
        "actionDate": "2025-05-05",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1598",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "BABIES Act",
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
        "name": "Health",
        "updateDate": "2025-09-23T17:38:06Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5202ih.xml"
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
      "title": "BABIES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BABIES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Better Availability of Birth Centers Improves Outcomes and Expands Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address maternity care shortages and promote optimal maternity outcomes by expanding access to birth centers and exploring more effective payment models for birth center care, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:25Z"
    }
  ]
}
```
