# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3365?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3365
- Title: HEALTH for MOM Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3365
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2025-09-18T08:07:18Z
- Update date including text: 2025-09-18T08:07:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3365",
    "number": "3365",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "HEALTH for MOM Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-18T08:07:18Z",
    "updateDateIncludingText": "2025-09-18T08:07:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:05:45Z",
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
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "MA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3365ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3365\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Nunn of Iowa (for himself, Ms. Pressley , and Ms. Underwood ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to provide States with the option to provide coordinated care through a pregnancy medical home for high-risk pregnant women, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Harnessing Effective and Appropriate Long-Term Health for Moms On Medicaid Act of 2025 or the HEALTH for MOM Act of 2025 .\n#### 2. State option to provide coordinated care through a health home for pregnant and postpartum women\nTitle XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) is amended by inserting after section 1945A the following new section:\n1945B. State option to provide coordinated care through a health home for pregnant and postpartum women (a) State option (1) In general Notwithstanding section 1902(a)(1) (relating to statewideness) and section 1902(a)(10)(B) (relating to comparability), beginning 2 years after the date of the enactment of this section, a State, at its option as a State plan amendment and after consultation with health care providers and individuals enrolled under such plan who are or have been pregnant, may provide for medical assistance under this title to an eligible woman who chooses to\u2014 (A) enroll in a maternity health home under this section by selecting a designated provider, a team of health care professionals operating with such a provider, or a health team as the woman\u2019s maternity health home for purposes of providing the woman with pregnancy and postpartum coordinated care services; or (B) receive such services from a designated provider, a team of health care professionals operating with such a provider, or a health team that has voluntarily opted to participate in a maternity health home for eligible women under this section. (2) Eligible woman defined (A) In general In this section, the term eligible woman means an individual who\u2014 (i) is eligible for medical assistance under the State plan (or under a waiver of such plan) for all items and services covered under the State plan (or waiver) that are not less in amount, duration, or scope, or are determined by the Secretary to be substantially equivalent, to the medical assistance available for an individual described in subsection (a)(10)(A)(i); and (ii) is pregnant. (B) Continuation of eligibility An individual described in subparagraph (A) shall be deemed to be described in such subparagraph through the earlier of\u2014 (i) the end of the month in which the individual\u2019s eligibility for medical assistance under the State plan (or waiver) ends; and (ii) the last day of the 1-year period that begins on the last day of the individual\u2019s pregnancy. (C) Exclusion of individuals eligible for a limited pregnancy-related only benefit package Such term does not include an individual who had a pregnancy end within the last 365 days and whose eligibility under such plan (or waiver) is limited to coverage for a limited type of benefits and services. (b) Qualification standards The Secretary shall establish standards for qualification as a maternity health home or as a designated provider, team of health care professionals operating with such a provider, or a health team eligible for participation in a maternity health home for purposes of this section. Such standards shall include requiring designated providers, teams of health care professionals operating with such providers, and health teams (designated as a maternity health home) to demonstrate to the State the ability to do the following: (1) Coordinate prompt care and access to maternity and postpartum care services, including services provided by specialists, and programs for an eligible woman during pregnancy and during the period for which she remains eligible as described in subsection (a)(2)(B). (2) Develop an individualized, comprehensive, patient-centered care plan for each eligible woman that accommodates patient preferences and, if applicable, reflects adjustments to the payment methodology described in subsection (c)(2)(B). (3) Develop and incorporate into each eligible woman\u2019s care plan, in a culturally and linguistically appropriate manner consistent with the needs of the eligible woman, ongoing home care, community-based primary care, inpatient care, social support services, behavioral health services, local hospital emergency care, oral health care, and to the extent, applicable, care management and planning related to a change in an eligible woman\u2019s eligibility for medical assistance or a change in health insurance coverage. (4) Coordinate with pediatric care providers, community-based providers, behavioral health providers, social service providers, local hospital and emergency care providers, oral health providers, specialists, and providers of early intervention services to ensure full implementation of the client\u2019s care plan, as appropriate. (5) Collect and report information under subsection (f)(1). (c) Payments (1) In general A State shall provide a designated provider, a team of health care professionals operating with such a provider, or a health team with payments for the provision of pregnancy and postpartum coordinated care services, to each eligible woman that selects such provider, team of health care professionals, or health team as the woman\u2019s maternity health home or care provider. Payments made to a maternity health home or care provider for such services shall be treated as medical assistance for purposes of section 1903(a), except that, during the first 4 fiscal year quarters that the State plan amendment is in effect, the Federal medical assistance percentage applicable to such payments shall be increased by 15 percentage points, but in no case may exceed 90 percent. (2) Methodology The State shall specify in the State plan amendment the methodology the State will use for determining payment for the provision of pregnancy and postpartum coordinated care services or treatment to an eligible woman. Such methodology for determining payment\u2014 (A) may be based on\u2014 (i) a per-member per-month basis for each eligible woman enrolled in the maternity health home; (ii) a prospective payment model, in the case of payments to Federally qualified health centers or a rural health clinics; or (iii) an alternate model of payment (which may include a model developed under a waiver under section 1115) proposed by the State and approved by the Secretary; (B) may be adjusted to reflect, with respect to each eligible woman\u2014 (i) the severity of the risks associated with the woman\u2019s pregnancy; (ii) the severity of the risks associated with the woman\u2019s postpartum health care needs; and (iii) the level or amount of time of care coordination required with respect to the woman; and (C) shall be established consistent with section 1902(a)(30)(A). (d) Coordinating care (1) Hospital notification A State with a State plan amendment approved under this section shall require each hospital that is a participating provider under the State plan (or under a waiver of such plan) to establish procedures in the case of an eligible woman who seeks treatment in the emergency department of such hospital for\u2014 (A) providing the woman with culturally and linguistically appropriate information on the respective treatment models and opportunities for the woman to access a maternity health home and its associated benefits; and (B) notifying the maternity health home in which the woman is enrolled, or the designated provider, team of health care professionals operating with such a provider, or health team treating the woman, of the woman\u2019s treatment in the emergency department and of the protocols for the maternity health home, designated provider, or team to be involved in the woman\u2019s emergency care or post-discharge care. (2) Education with respect to availability of a maternity health home (A) In general In order for a State plan amendment to be approved under this section, a State shall include in the State plan amendment a description of the State\u2019s process for\u2014 (i) educating providers participating in the State plan (or a waiver of such plan) on the availability of maternity health homes for eligible women, including the process by which such providers can participate in or refer eligible women to an approved maternity health home or a designated provider, team of health care professionals operating with such a provider, or health team; and (ii) educating eligible women, in a culturally and linguistically appropriate manner, on the availability of maternity health homes. (B) Outreach The process established by the State under subparagraph (A) shall include the participation of relevant stakeholders or other public or private organizations or entities that provide outreach and information on the availability of health care items and services to families of individuals eligible to receive medical assistance under the State plan (or a waiver of such plan). (3) Mental health coordination A State with a State plan amendment approved under this section shall consult and coordinate, as appropriate, with the Secretary in addressing issues regarding the prevention, identification, and treatment of mental health conditions and substance use disorders among eligible women. (4) Coordination of social and support services A State with a State plan amendment approved under this section shall consult and coordinate, as appropriate, with the Secretary in establishing means to connect eligible women receiving pregnancy and postpartum care coordinated under this section with social and support services, including services made available under maternal, infant, and early childhood home visiting programs established under section 511, and services made available under section 330H or title X of the Public Health Service Act, the Special Supplemental Nutrition Program for Women, Infants, and Children, or under title V. (e) Monitoring A State shall include in the State plan amendment\u2014 (1) a methodology for tracking reductions in inpatient days and reductions in the total cost of care resulting from improved care coordination and management under this section; (2) a proposal for use of health information technology in providing an eligible woman with pregnancy and postpartum coordinated care services as specified under this section and improving service delivery and coordination across the care continuum; and (3) a methodology for tracking prompt and timely access to medically necessary care for eligible women from out-of-State providers. (f) Data collection (1) Provider reporting requirements In order to receive payments from a State under subsection (c), a maternity health home, or a designated provider, a team of health care professionals operating with such a provider, or a health team, shall report to the State, at such time and in such form and manner as may be required by the State, including through a health information exchange or other public health data sharing entity, the following information: (A) With respect to each such designated provider, team of health care professionals operating with such a provider, and health team (designated as a maternity health home), the name, National Provider Identification number, address, and specific health care services offered to be provided to eligible women who have selected such provider, team of health care professionals, or health team as the womens maternity health home. (B) Information on all applicable measures for determining the quality of services provided by such provider, team of health care professionals, or health team, including, to the extent applicable, maternal, perinatal, and child health quality measures under section 1139B. (C) Such other information as the Secretary shall specify in guidance. (2) State reporting requirements (A) Comprehensive report A State with a State plan amendment approved under this section shall report to the Secretary (and, upon request, to the Medicaid and CHIP Payment and Access Commission), at such time, but at a minimum frequency of every 12 months, and in such form and manner determined by the Secretary to be reasonable and minimally burdensome, including through a health information exchange or other public health data sharing entity, the following information: (i) Information described in paragraph (1). (ii) The number and, to the extent available and while maintaining all relevant protecting privacy and confidentially protections, disaggregated demographic information of eligible women who have enrolled in a maternity health home pursuant to this section. (iii) The number of maternity health homes in the State. (iv) The medical and behavioral health conditions or factors that contribute to severe maternal morbidity among eligible women enrolled in maternity health homes in the State. (v) The extent to which such women receive health care items and services under the State plan before, during, and after the women\u2019s enrollment in such a maternity health home. (vi) Where applicable, mortality data and data for the associated causes of death for eligible women enrolled in a maternity health home under this section, in accordance with subsection (g). For deaths occurring postpartum, such data shall distinguish between deaths occurring up to 42 days postpartum and deaths occurring between 43 days to up to 1 year postpartum. Where applicable, data reported under this clause shall be reported alongside comparable data from a State\u2019s maternal mortality review committee, as established in accordance with section 317K(d) of the Public Health Service Act, for purposes of further identifying and comparing statewide trends in maternal mortality among populations participating in the maternity health home under this section. (vii) The type of delivery systems and payment models used to provide health home services to eligible individuals enrolled in a maternal health home under such amendment. (viii) Information on hospitalizations, morbidity, and mortality of eligible individuals and their infants enrolled in a maternal health home in such State alongside comparable data from a State\u2019s maternal mortality review committee. (B) Implementation report Not later than 18 months after a State has a State plan amendment approved under this section, the State shall submit to the Secretary, and make publicly available on the appropriate State website, a report on how the State is implementing the option established under this section, including through any best practices adopted by the State. (g) Confidentiality A State with a State plan amendment under this section shall establish confidentiality protections for the purposes of subsection (f)(2)(A) to ensure, at a minimum, that there is no disclosure by the State of any identifying information about any specific eligible woman enrolled in a maternity health home or any maternal mortality case, and that all relevant confidentiality and privacy protections, including the requirements under 1902(a)(7)(A), are maintained. (h) Rule of construction Nothing in this section shall be construed to require\u2014 (1) an eligible woman to enroll in a maternity health home under this section; or (2) a designated provider or health team to act as a maternity health home and provide services in accordance with this section if the provider or health team does not voluntarily agree to act as a maternity health home. (i) Planning grants (1) In general Beginning October 1, 2025, from the amount appropriated under paragraph (2), the Secretary shall award planning grants to States for purposes of developing and submitting a State plan amendment under this section. The Secretary shall award a grant to each State that applies for a grant under this subsection, but the Secretary may determine the amount of the grant based on the merits of the application and the goal of the State to prioritize health outcomes for eligible women. A planning grant awarded to a State under this subsection shall remain available until expended. (2) Appropriation There are authorized to be appropriated to the Secretary $50,000,000 for the 2-year period beginning on the date of the enactment of this section, for the purposes of making grants under this subsection, to remain available until expended. (3) Limitation The total amount of payments made to States under this subsection shall not exceed $50,000,000. (j) Additional definitions In this section: (1) Designated provider The term designated provider means a physician (including an obstetrician-gynecologist), hospital, clinical practice or clinical group practice, rural clinic, community health center, community mental health center, or any other entity or provider that is determined by the State and approved by the Secretary to be qualified to be a maternity health home on the basis of documentation evidencing that the entity has the systems, expertise, and infrastructure in place to provide pregnancy and postpartum coordinated care services. Such term may include providers who are employed by, or affiliated with, a hospital. (2) Maternity health home The term maternity health home means a designated provider (including a provider that operates in coordination with a team of health care professionals) or a health team is selected by an eligible woman to provide pregnancy and postpartum coordinated care services. (3) Health team The term health team has the meaning given such term for purposes of section 3502 of Public Law 111\u2013148 . (4) Pregnancy and postpartum coordinated care services (A) In general The term pregnancy and postpartum coordinated care services means items and services related to the coordination of care for comprehensive and timely high-quality, culturally and linguistically appropriate, services described in subparagraph (B) that are provided to an eligible woman by a designated provider, a team of health care professionals operating with such a provider, or a health team (designated as a maternity health home). (B) Services described (i) In general The services described in this subparagraph shall include with respect to a State electing the State plan amendment option under this section, any medical assistance for items and services for which payment is available under the State plan or under a waiver of such plan. (ii) Other items and services In addition to medical assistance described in clause (i), the services described in this subparagraph shall include the following: (I) Comprehensive care management. (II) Care coordination (including with pediatricians, specialists, and providers of early intervention services, as appropriate), health promotion, and providing access to the full range of maternal, obstetric, and gynecologic services, including services from out-of-State providers. (III) Comprehensive transitional care, including appropriate follow-up, from inpatient to other settings. (IV) Patient and family support (including authorized representatives). (V) Referrals to community and social support services, if relevant. (VI) Use of health information technology to link services, as feasible and appropriate. (5) Team of health care professionals The term team of health care professionals means a team of health care professionals (as described in the State plan amendment under this section) that may\u2014 (A) include\u2014 (i) physicians, including gynecologist-obstetricians, pediatricians, and other professionals such as physicians assistants, advance practice nurses, including certified midwives, nurses, nurse care coordinators, dietitians, nutritionists, social workers, behavioral health professionals, physical counselors, physical therapists, occupational therapists, or any professionals that assist in prenatal care, delivery, or postpartum care for which medical assistance is available under the State plan or a waiver of such plan and determined to be appropriate by the State and approved by the Secretary; (ii) an entity or individual who is designated to coordinate such care delivered by the team; and (iii) when appropriate and if otherwise eligible to furnish items and services that are reimbursable as medical assistance under the State plan or under a waiver of such plan, doulas, community health workers, translators and interpreters, and other individuals with culturally appropriate and trauma-informed expertise; and (B) provide care at a facility that is freestanding, virtual, or based at a hospital, community health center, community mental health center, rural clinic, clinical practice or clinical group practice, academic health center, or any entity determined to be appropriate by the State and approved by the Secretary, or provide care at the home of an individual with respect to a home birth. .",
      "versionDate": "2025-05-13",
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
        "updateDate": "2025-07-30T14:05:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-13",
    "originChamber": "House",
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
          "measure-id": "id119hr3365",
          "measure-number": "3365",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-13",
          "originChamber": "HOUSE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3365v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-05-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Harnessing Effective and Appropriate Long-Term Health for Moms On Medicaid Act of 2025 or the HEALTH for MOM Act of\u00a0</strong><strong>2025</strong></p><p>This bill allows state Medicaid programs to cover services that are provided by maternity health homes (designated providers or health teams that provide pregnancy and postpartum coordinated care services).</p><p>Participating maternity health homes must meet standards set by the Centers for Medicare & Medicaid Services (CMS), including the ability to coordinate prompt access to services, develop individualized care plans, provide supportive services, and coordinate with pediatric care providers. States must conduct outreach to providers, pregnant women, and other relevant stakeholders on the availability of such health homes and must report specified information relating to the implementation and outcomes of such services.</p><p>The CMS must award grants to states to develop plans for implementation. The bill also temporarily increases the Federal Medical Assistance Percentage (i.e., federal matching rate) for maternity health home services.</p>"
        },
        "title": "HEALTH for MOM Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3365.xml",
    "summary": {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Harnessing Effective and Appropriate Long-Term Health for Moms On Medicaid Act of 2025 or the HEALTH for MOM Act of\u00a0</strong><strong>2025</strong></p><p>This bill allows state Medicaid programs to cover services that are provided by maternity health homes (designated providers or health teams that provide pregnancy and postpartum coordinated care services).</p><p>Participating maternity health homes must meet standards set by the Centers for Medicare & Medicaid Services (CMS), including the ability to coordinate prompt access to services, develop individualized care plans, provide supportive services, and coordinate with pediatric care providers. States must conduct outreach to providers, pregnant women, and other relevant stakeholders on the availability of such health homes and must report specified information relating to the implementation and outcomes of such services.</p><p>The CMS must award grants to states to develop plans for implementation. The bill also temporarily increases the Federal Medical Assistance Percentage (i.e., federal matching rate) for maternity health home services.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr3365"
    },
    "title": "HEALTH for MOM Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Harnessing Effective and Appropriate Long-Term Health for Moms On Medicaid Act of 2025 or the HEALTH for MOM Act of\u00a0</strong><strong>2025</strong></p><p>This bill allows state Medicaid programs to cover services that are provided by maternity health homes (designated providers or health teams that provide pregnancy and postpartum coordinated care services).</p><p>Participating maternity health homes must meet standards set by the Centers for Medicare & Medicaid Services (CMS), including the ability to coordinate prompt access to services, develop individualized care plans, provide supportive services, and coordinate with pediatric care providers. States must conduct outreach to providers, pregnant women, and other relevant stakeholders on the availability of such health homes and must report specified information relating to the implementation and outcomes of such services.</p><p>The CMS must award grants to states to develop plans for implementation. The bill also temporarily increases the Federal Medical Assistance Percentage (i.e., federal matching rate) for maternity health home services.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr3365"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3365ih.xml"
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
      "title": "HEALTH for MOM Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T03:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEALTH for MOM Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Harnessing Effective and Appropriate Long-Term Health for Moms On Medicaid Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to provide States with the option to provide coordinated care through a pregnancy medical home for high-risk pregnant women, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T03:33:32Z"
    }
  ]
}
```
