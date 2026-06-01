# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4186?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4186
- Title: Perinatal Workforce Act
- Congress: 119
- Bill type: S
- Bill number: 4186
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-13T19:09:00Z
- Update date including text: 2026-04-13T19:09:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4186",
    "number": "4186",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Perinatal Workforce Act",
    "type": "S",
    "updateDate": "2026-04-13T19:09:00Z",
    "updateDateIncludingText": "2026-04-13T19:09:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
        "item": {
          "date": "2026-03-25T16:21:38Z",
          "name": "Referred To"
        }
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4186is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4186\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Ms. Baldwin (for herself, Mr. Merkley , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to grow and diversify the perinatal workforce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Perinatal Workforce Act .\n#### 2. HHS agency directives\n##### (a) Guidance to States\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services shall issue and disseminate guidance to States to educate providers, managed care entities, and other insurers about the value and process of delivering respectful maternal health care through diverse and multidisciplinary care provider models.\n**(2) Contents**\nThe guidance required by paragraph (1) shall address how States can encourage and incentivize hospitals, health systems, midwifery practices, freestanding birth centers, other maternity care provider groups, managed care entities, and other insurers\u2014\n**(A)**\nto recruit and retain maternity care providers, mental and behavioral health care providers acting in accordance with State law, and registered dietitians or nutrition professionals (as such term is defined in section 1861(vv)(2) of the Social Security Act ( 42 U.S.C. 1395x(vv)(2) ))\u2014\n**(i)**\nfrom racially, ethnically, and linguistically diverse backgrounds;\n**(ii)**\nwith experience practicing in racially and ethnically diverse communities; and\n**(iii)**\nwho have undergone training on implicit bias and racism;\n**(B)**\nto incorporate into maternity care teams\u2014\n**(i)**\nmidwives who meet, at a minimum, the international definition of a midwife and global standards for midwifery education as established by the International Confederation of Midwives;\n**(ii)**\nperinatal health workers;\n**(iii)**\nphysician assistants;\n**(iv)**\nadvanced practice registered nurses; and\n**(v)**\nlactation consultants certified by the International Board of Lactation Consultant Examiners;\n**(C)**\nto provide collaborative, culturally and linguistically congruent care; and\n**(D)**\nto provide opportunities for individuals enrolled in accredited midwifery education programs to participate in job shadowing with maternity care teams in hospitals, health systems, midwifery practices, and freestanding birth centers.\n##### (b) Study on respectful and culturally and linguistically congruent maternity care\n**(1) Study**\nThe Secretary of Health and Human Services acting through the Director of the National Institutes of Health (in this subsection referred to as the Secretary ) shall conduct a study on best practices in respectful and culturally and linguistically congruent maternity care.\n**(2) Report**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall\u2014\n**(A)**\ncomplete the study required by paragraph (1);\n**(B)**\nsubmit to the Congress and make publicly available a report on the results of such study; and\n**(C)**\ninclude in such report\u2014\n**(i)**\na compendium of examples of hospitals, health systems, midwifery practices, freestanding birth centers, other maternity care provider groups, managed care entities, and other insurers that are delivering respectful and culturally and linguistically congruent maternal health care;\n**(ii)**\na compendium of examples of hospitals, health systems, midwifery practices, freestanding birth centers, other maternity care provider groups, managed care entities, and other insurers that have made progress in reducing disparities in maternal health outcomes and improving birthing experiences for pregnant and postpartum individuals from racial and ethnic minority groups; and\n**(iii)**\nrecommendations to hospitals, health systems, midwifery practices, freestanding birth centers, other maternity care provider groups, managed care entities, and other insurers, for best practices in respectful and culturally and linguistically congruent maternity care.\n#### 3. Grants to grow and diversify the perinatal workforce\nTitle VII of the Public Health Service Act is amended by inserting after section 757 ( 42 U.S.C. 294f ) the following:\n758. Perinatal workforce grants (a) In general The Secretary shall award grants to entities to establish or expand programs described in subsection (b) to grow and diversify the perinatal workforce. (b) Use of funds Recipients of grants under this section shall use the grants to grow and diversify the perinatal workforce by\u2014 (1) establishing accredited schools or programs that provide education and training to individuals seeking appropriate licensing and certification as\u2014 (A) physician assistants who will complete clinical training in the field of maternal and perinatal health; (B) perinatal health workers; or (C) midwives who meet, at a minimum, the international definition of a midwife and global standards for midwifery education as established by the International Confederation of Midwives; and (2) expanding the capacity of existing accredited schools or programs described in paragraph (1), for the purposes of increasing the number of students enrolled in such accredited schools or programs, such as by awarding scholarships for students (including students from racially, ethnically, and linguistically diverse backgrounds). (c) Prioritization In awarding grants under this section, the Secretary shall give priority to a school or program described in subsection (b) that\u2014 (1) has demonstrated a commitment to recruiting and retaining students and faculty from racial and ethnic minority groups; (2) has developed a strategy to recruit and retain a diverse pool of students into the school or program described in subsection (b) that is supported by funds received through the grant, particularly from racial and ethnic minority groups and other underserved populations; (3) has developed a strategy to recruit and retain students who plan to practice in a health professional shortage area designated under section 332; (4) has developed a strategy to recruit and retain students who plan to practice in an area with significant racial and ethnic disparities in maternal health outcomes, to the extent practicable; and (5) includes in the standard curriculum for all students within the school or program described in subsection (b) a bias, racism, or discrimination training program that includes training on implicit bias and racism. (d) Reporting As a condition on receipt of a grant under this section for a school or program described in subsection (b), an entity shall agree to submit to the Secretary an annual report on the activities conducted through the grant, including\u2014 (1) the number and demographics of students participating in the school or program; (2) the extent to which students in the school or program are entering careers in\u2014 (A) health professional shortage areas designated under section 332; and (B) areas with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes, to the extent such data are available; and (3) whether the school or program has included in the standard curriculum for all students a bias, racism, or discrimination training program that includes explicit and implicit bias, and if so the effectiveness of such training program. (e) Period of grants The period of a grant under this section shall be up to 5 years. (f) Application To seek a grant under this section, an entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including any information necessary for prioritization under subsection (c). (g) Technical assistance The Secretary shall provide, directly or by contract, technical assistance to entities seeking or receiving a grant under this section on the development, use, evaluation, and postgrant period sustainability of the school or program described in subsection (b) that is proposed to be, or is being, established or expanded through the grant. (h) Report by the Secretary Not later than 4 years after the date of enactment of this section, the Secretary shall prepare and submit to the Congress, and post on the internet website of the Department of Health and Human Services, a report on the effectiveness of the grant program under this section at\u2014 (1) recruiting students from racial and ethnic minority groups; (2) increasing the number of health professionals described in subparagraphs (A), (B), and (C) of subsection (b)(1) from racial and ethnic minority groups and other underserved populations; (3) increasing the number of such health professionals working in health professional shortage areas designated under section 332; and (4) increasing the number of such health professionals working in areas with significant racial and ethnic disparities in maternal health outcomes, to the extent such data are available. (i) Definition In this section, the term racial and ethnic minority group has the meaning given such term in section 1707(g)(1). (j) Authorization of appropriations To carry out this section, there is authorized to be appropriated $15,000,000 for each of fiscal years 2027 through 2031. .\n#### 4. Grants to grow and diversify the nursing workforce in maternal and perinatal health\nTitle VIII of the Public Health Service Act is amended by inserting after section 811 ( 42 U.S.C. 296j ) the following:\n812. Perinatal nursing workforce grants (a) In general The Secretary shall award grants to schools of nursing to grow and diversify the perinatal nursing workforce. (b) Use of funds Recipients of grants under this section shall use the grants to grow and diversify the perinatal nursing workforce by providing scholarships to students seeking to become\u2014 (1) nurse practitioners whose education includes a focus on maternal and perinatal health; (2) certified nurse-midwives; or (3) clinical nurse specialists whose education includes a focus on maternal and perinatal health. (c) Prioritization In awarding grants under this section, the Secretary shall give priority to any school of nursing that\u2014 (1) has developed a strategy to recruit and retain a diverse pool of students seeking to enter careers focused on maternal and perinatal health, particularly students from racial and ethnic minority groups and other underserved populations; (2) has developed a partnership with a practice setting in a health professional shortage area designated under section 332 for the clinical placements of the school\u2019s students; (3) has developed a strategy to recruit and retain students who plan to practice in an area with significant racial and ethnic disparities in maternal health outcomes, to the extent practicable; and (4) includes in the standard curriculum for all students seeking to enter careers focused on maternal and perinatal health a bias, racism, or discrimination training program that includes education on implicit bias and racism. (d) Reporting As a condition on receipt of a grant under this section, a school of nursing shall agree to submit to the Secretary an annual report on the activities conducted through the grant, including, to the extent practicable\u2014 (1) the number and demographics of students in the school of nursing seeking to enter careers focused on maternal and perinatal health; (2) the extent to which such students are preparing to enter careers in\u2014 (A) health professional shortage areas designated under section 332; and (B) areas with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes, to the extent such data are available; and (3) whether the standard curriculum for all students seeking to enter careers focused on maternal and perinatal health includes a bias, racism, or discrimination training program that includes education on implicit bias and racism. (e) Period of grants The period of a grant under this section shall be up to 5 years. (f) Application To seek a grant under this section, an entity shall submit to the Secretary an application, at such time, in such manner, and containing such information as the Secretary may require, including any information necessary for prioritization under subsection (c). (g) Technical assistance The Secretary shall provide, directly or by contract, technical assistance to schools of nursing seeking or receiving a grant under this section on the processes of awarding and evaluating scholarships through the grant. (h) Report by the Secretary Not later than 4 years after the date of enactment of this section, the Secretary shall prepare and submit to the Congress, and post on the internet website of the Department of Health and Human Services, a report on the effectiveness of the grant program under this section at\u2014 (1) recruiting students from racial and ethnic minority groups and other underserved populations; (2) increasing the number of advanced practice registered nurses entering careers focused on maternal and perinatal health from racial and ethnic minority groups and other underserved populations; (3) increasing the number of advanced practice registered nurses entering careers focused on maternal and perinatal health working in health professional shortage areas designated under section 332; and (4) increasing the number of advanced practice registered nurses entering careers focused on maternal and perinatal health working in areas with significant racial and ethnic disparities in maternal health outcomes, to the extent such data are available. (i) Authorization of appropriations To carry out this section, there is authorized to be appropriated $15,000,000 for each of fiscal years 2027 through 2031. .\n#### 5. GAO report\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act and every 5 years thereafter, the Comptroller General of the United States shall submit to Congress a report on barriers to maternal health education and access to care in the United States. Such report shall include the information and recommendations described in subsection (b).\n##### (b) Content of report\nThe report under subsection (a) shall include\u2014\n**(1)**\nan assessment of current barriers to entering and successfully completing accredited midwifery education programs, and recommendations for addressing such barriers, particularly for low-income women and women from racial and ethnic minority groups;\n**(2)**\nan assessment of current barriers to entering and successfully completing accredited education programs for other health professional careers related to maternity care, including maternity care providers, mental and behavioral health care providers acting in accordance with State law, and registered dietitians or nutrition professionals (as such term is defined in section 1861(vv)(2) of the Social Security Act ( 42 U.S.C. 1395x(vv)(2) )), particularly for low-income women and women from racial and ethnic minority groups;\n**(3)**\nan assessment of current barriers that prevent midwives from meeting the international definition of a midwife and global standards for midwifery education as established by the International Confederation of Midwives, and recommendations for addressing such barriers, particularly for low-income women and women from racial and ethnic minority groups;\n**(4)**\nan assessment of disparities in access to maternity care providers, mental or behavioral health care providers acting in accordance with State law, and registered dietitians or nutrition professionals (as such term is defined in section 1861(vv)(2) of the Social Security Act ( 42 U.S.C. 1395x(vv)(2) )), and perinatal health workers, stratified by race, ethnicity, gender identity, primary language, geographic location, and insurance type and recommendations to promote greater access equity; and\n**(5)**\nrecommendations to promote greater equity in compensation for perinatal health workers under public and private insurers, particularly for such individuals from racially and ethnically diverse backgrounds.\n#### 6. Definitions\nIn this Act:\n**(1) Culturally and linguistically congruent**\nThe term culturally and linguistically congruent , with respect to care or maternity care, means care that is in agreement with the preferred cultural values, beliefs, worldview, language, and practices of the health care consumer and other stakeholders.\n**(2) Maternity care provider**\nThe term maternity care provider means a health care provider who\u2014\n**(A)**\nis a physician, a physician assistant, a midwife who meets at a minimum the international definition of a midwife and global standards for midwifery education as established by the International Confederation of Midwives, an advanced practice registered nurse, a doula accredited by a State to receive reimbursement for doula services under a State plan (or a waiver of such plan) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), or a lactation consultant certified by the International Board of Lactation Consultant Examiners; and\n**(B)**\nhas a focus on maternal or perinatal health.\n**(3) Perinatal health worker**\nThe term perinatal health worker means a nonclinical health worker focused on maternal or perinatal health, such as a doula, community health worker, peer supporter, lactation educator or counselor, nutritionist or dietitian, childbirth educator, social worker, home visitor, patient navigator or coordinator, or language interpreter.\n**(4) Postpartum**\nThe term postpartum refers to the 1-year period beginning on the last day of the pregnancy of an individual.\n**(5) Racial and ethnic minority group**\nThe term racial and ethnic minority group has the meaning given such term in section 1707(g)(1) of the Public Health Service Act ( 42 U.S.C. 300u\u20136(g)(1) ).",
      "versionDate": "2026-03-25",
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
        "actionDate": "2026-03-18",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, Veterans' Affairs, Natural Resources, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7973",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Momnibus Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-25",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8089",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Perinatal Workforce Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-04-09T14:08:31Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4186is.xml"
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
      "title": "Perinatal Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Perinatal Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to grow and diversify the perinatal workforce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:27Z"
    }
  ]
}
```
