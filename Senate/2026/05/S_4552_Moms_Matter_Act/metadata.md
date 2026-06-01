# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4552?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4552
- Title: Moms Matter Act
- Congress: 119
- Bill type: S
- Bill number: 4552
- Origin chamber: Senate
- Introduced date: 2026-05-18
- Update date: 2026-05-29T07:38:44Z
- Update date including text: 2026-05-29T07:38:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-18: Introduced in Senate
- 2026-05-18 - IntroReferral: Introduced in Senate
- 2026-05-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-05-18: Introduced in Senate

## Actions

- 2026-05-18 - IntroReferral: Introduced in Senate
- 2026-05-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-18",
    "latestAction": {
      "actionDate": "2026-05-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4552",
    "number": "4552",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Moms Matter Act",
    "type": "S",
    "updateDate": "2026-05-29T07:38:44Z",
    "updateDateIncludingText": "2026-05-29T07:38:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-18",
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
      "actionDate": "2026-05-18",
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
          "date": "2026-05-18T20:09:18Z",
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4552is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4552\nIN THE SENATE OF THE UNITED STATES\nMay 18, 2026 Mrs. Gillibrand (for herself, Ms. Blunt Rochester , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo address maternal mental health conditions and substance use disorders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Moms Matter Act .\n#### 2. Maternal mental health equity grant program\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use, shall establish a program to award grants to eligible entities to address maternal mental health conditions and substance use disorders, with a focus on demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n##### (b) Application\nTo be eligible to receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Priority\nIn awarding grants under this section, the Secretary shall give priority to an eligible entity that\u2014\n**(1)**\nis, or will partner with, a community-based organization to address maternal mental health conditions and substance use disorders described in subsection (a);\n**(2)**\nis operating in an area with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes; and\n**(3)**\nis operating in a health professional shortage area designated under section 332 of the Public Health Service Act ( 42 U.S.C. 254e ).\n##### (d) Use of funds\nAn eligible entity that receives a grant under this section shall use the grant for the following:\n**(1)**\nEstablishing or expanding maternity care programs to improve the integration of maternal mental health and behavioral health care services into primary care settings where pregnant individuals regularly receive health care services.\n**(2)**\nEstablishing or expanding group prenatal care programs or postpartum care programs.\n**(3)**\nExpanding existing programs that improve maternal mental and behavioral health during the prenatal and postpartum periods, with a focus on individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n**(4)**\nProviding services and support for pregnant and postpartum individuals with maternal mental health conditions and substance use disorders, including referrals to addiction treatment centers that offer evidence-based treatment options.\n**(5)**\nAddressing stigma associated with maternal mental health conditions and substance use disorders, with a focus on individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n**(6)**\nRaising awareness of warning signs of maternal mental health conditions and substance use disorders, with a focus on pregnant and postpartum individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n**(7)**\nEstablishing or expanding programs to prevent suicide or self-harm among pregnant and postpartum individuals.\n**(8)**\nOffering evidence-aligned programs at freestanding birth centers that provide maternal mental and behavioral health care education, treatments, and services, and other services for individuals throughout the prenatal and postpartum period.\n**(9)**\nEstablishing or expanding programs to provide education and training to maternity care providers with respect to\u2014\n**(A)**\nidentifying potential warning signs for maternal mental health conditions or substance use disorders in pregnant and postpartum individuals, with a focus on individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes; and\n**(B)**\nin the case where such providers identify such warning signs, offering referrals to mental and behavioral health care professionals.\n**(10)**\nDeveloping a website, or other source, that includes information on health care providers who treat maternal mental health conditions and substance use disorders.\n**(11)**\nEstablishing or expanding programs in communities to improve coordination between maternity care providers and mental and behavioral health care providers who treat maternal mental health conditions and substance use disorders, including through the use of toll-free hotlines.\n**(12)**\nCarrying out other programs aligned with evidence-based practices for addressing maternal mental health conditions and substance use disorders for pregnant and postpartum individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n##### (e) Reporting\n**(1) Eligible entities**\nAn eligible entity that receives a grant under subsection (a) shall submit annually to the Secretary, and make publicly available, a report on the activities conducted using funds received through a grant under this section. Such reports shall include quantitative and qualitative evaluations of such activities, including the experience of individuals who received health care through such grant.\n**(2) Secretary**\nNot later than the end of fiscal year 2030, the Secretary shall submit to Congress a report that includes\u2014\n**(A)**\na summary of the reports received under paragraph (1);\n**(B)**\nan evaluation of the effectiveness of grants awarded under this section;\n**(C)**\nrecommendations with respect to expanding coverage of evidence-based screenings and treatments for maternal mental health conditions and substance use disorders; and\n**(D)**\nrecommendations with respect to ensuring activities described under subsection (d) continue after the end of a grant period.\n##### (f) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na community-based organization serving pregnant and postpartum individuals, including such organizations serving individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes;\n**(B)**\na nonprofit or patient advocacy organization with expertise in maternal mental and behavioral health;\n**(C)**\na maternity care provider;\n**(D)**\na mental or behavioral health care provider who treats maternal mental health conditions or substance use disorders;\n**(E)**\na State or local governmental entity, including a State or local public health department;\n**(F)**\nan Indian Tribe or Tribal organization (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); and\n**(G)**\nan Urban Indian organization (as such term is defined in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 )).\n**(2) Freestanding birth center**\nThe term freestanding birth center has the meaning given that term under section 1905(l) of the Social Security Act ( 42 U.S.C. 1396d(1) ).\n**(3) Maternal mortality**\nThe term maternal mortality means a death occurring during or within a 1-year period after pregnancy, caused by pregnancy-related or childbirth complications, including a suicide, overdose, or other death resulting from a mental health or substance use disorder attributed to or aggravated by pregnancy-related or childbirth complications.\n**(4) Maternity care provider**\nThe term maternity care provider means a health care provider who\u2014\n**(A)**\nis a physician, a physician assistant, a midwife who meets, at a minimum, the international definition of a midwife and global standards for midwifery education as established by the International Confederation of Midwives, an advanced practice registered nurse, a doula accredited by a State to receive reimbursement for doula services under a State plan (or a waiver of such plan) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), or a lactation consultant certified by the International Board of Lactation Consultant Examiners; and\n**(B)**\nhas a focus on maternal or perinatal health.\n**(5) Postpartum and postpartum period**\nThe terms postpartum and postpartum period refer to the 1-year period beginning on the last day of the pregnancy of an individual.\n**(6) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(7) Severe maternal morbidity**\nThe term severe maternal morbidity means a health condition, including a mental health condition or substance use disorder, attributed to or aggravated by pregnancy or childbirth that results in significant short-term or long-term consequences to the health of the individual who was pregnant.\n##### (g) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $25,000,000 for each of fiscal years 2027 through 2031.\n#### 3. Grants to grow and diversify the maternal mental and behavioral health care workforce\nTitle VII of the Public Health Service Act is amended by inserting after section 757 of such Act ( 42 U.S.C. 294f ) the following new section:\n758. Maternal mental and behavioral health care workforce grants (a) In general The Secretary may award grants to entities to establish or expand programs described in subsection (b) to grow and diversify the maternal mental and behavioral health care workforce. (b) Use of funds Recipients of grants under this section shall use the grants to grow and diversify the maternal mental and behavioral health care workforce by\u2014 (1) establishing schools or programs that provide education and training to individuals seeking appropriate licensing or certification as mental or behavioral health care providers who will specialize in maternal mental health conditions or substance use disorders; or (2) expanding the capacity of existing schools or programs described in paragraph (1), for the purposes of increasing the number of students enrolled in such schools or programs, including by awarding scholarships for students. (c) Prioritization In awarding grants under this section, the Secretary shall give priority to any entity that\u2014 (1) has demonstrated a commitment to recruiting and retaining students and faculty from racial and ethnic minority groups; (2) has developed a strategy to recruit and retain a diverse pool of students into the maternal mental or behavioral health care workforce program or school supported by funds received through the grant, particularly from racial and ethnic minority groups and other underserved populations; (3) has developed a strategy to recruit and retain students who plan to practice in a health professional shortage area designated under section 332; (4) has developed a strategy to recruit and retain students who plan to practice in an area with significant maternal health disparities, to the extent practicable; and (5) includes in the standard curriculum for all students within the maternal mental or behavioral health care workforce program or school a bias, racism, or discrimination training program that includes training on implicit bias and racism. (d) Reporting As a condition on receipt of a grant under this section for a maternal mental or behavioral health care workforce program or school, an entity shall agree to submit to the Secretary an annual report on the activities conducted through the grant, including\u2014 (1) the number and demographics of students participating in the program or school; (2) the extent to which students in the program or school are entering careers in\u2014 (A) health professional shortage areas designated under section 332; and (B) areas with significant maternal health disparities, to the extent such data are available; and (3) whether the program or school has included in the standard curriculum for all students a bias, racism, or discrimination training program that includes training on implicit bias and racism, and if so the effectiveness of such training program. (e) Period of grants The period of a grant under this section shall be up to 5 years. (f) Application To seek a grant under this section, an entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including any information necessary for prioritization under subsection (c). (g) Technical assistance The Secretary shall provide, directly or by contract, technical assistance to entities seeking or receiving a grant under this section on the development, use, evaluation, and postgrant period sustainability of the maternal mental or behavioral health care workforce programs or schools proposed to be, or being, established or expanded through the grant. (h) Report by the Secretary Not later than 4 years after the date of enactment of this section, the Secretary shall prepare and submit to Congress, and post on the website of the Department of Health and Human Services, a report on the effectiveness of the grant program under this section at\u2014 (1) recruiting students from racial and ethnic minority groups and other underserved populations; (2) increasing the number of mental or behavioral health care providers specializing in maternal mental health conditions or substance use disorders from racial and ethnic minority groups and other underserved populations; (3) increasing the number of mental or behavioral health care providers specializing in maternal mental health conditions or substance use disorders working in health professional shortage areas designated under section 332; and (4) increasing the number of mental or behavioral health care providers specializing in maternal mental health conditions or substance use disorders working in areas with significant maternal health disparities, to the extent such data are available. (i) Definitions In this section: (1) Racial and ethnic minority group The term racial and ethnic minority group has the meaning given such term in section 1707(g)(1). (2) Mental or behavioral health care provider The term mental or behavioral health care provider means a health care provider in the field of mental and behavioral health, including substance use disorders, acting in accordance with State law. (j) Authorization of appropriations To carry out this section, there is authorized to be appropriated $15,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2026-05-18",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4552is.xml"
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
      "title": "Moms Matter Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:38:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Moms Matter Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:38:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address maternal mental health conditions and substance use disorders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:33:49Z"
    }
  ]
}
```
