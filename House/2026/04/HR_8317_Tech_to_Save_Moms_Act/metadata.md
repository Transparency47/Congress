# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8317?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8317
- Title: Tech to Save Moms Act
- Congress: 119
- Bill type: HR
- Bill number: 8317
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-04-28T08:06:42Z
- Update date including text: 2026-04-28T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8317",
    "number": "8317",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Tech to Save Moms Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:42Z",
    "updateDateIncludingText": "2026-04-28T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:01:35Z",
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
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "IA"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "OH"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NC"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "TX"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "TN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DC"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CT"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "AL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "AL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "PA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "WI"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NJ"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "TX"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MI"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "KY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8317ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8317\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Ms. Williams of Georgia (for herself, Ms. Underwood , Mrs. Hinson , Mr. Joyce of Ohio , Ms. Adams , Mr. Krishnamoorthi , Ms. Johnson of Texas , Ms. Clarke of New York , Mr. Moulton , Mr. Cohen , Ms. Norton , Mrs. Hayes , Mr. Figures , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize grants to evaluate, develop, and expand the use of technology-enabled collaborative learning and capacity building models to improve maternal health outcomes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tech to Save Moms Act .\n#### 2. Integrated telehealth models in maternity care services\n##### (a) In general\nSection 1115A(b)(2)(B) of the Social Security Act ( 42 U.S.C. 1315a(b)(2)(B) ) is amended by adding at the end the following:\n(xxviii) Focusing on title XIX, providing for the adoption of and use of telehealth tools that allow for screening, monitoring, and management of common health complications with respect to an individual receiving medical assistance during such individual\u2019s pregnancy and for not more than a 1-year period beginning on the last day of the pregnancy. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect 1 year after the date of the enactment of this Act.\n#### 3. Grants to expand the use of technology-enabled collaborative learning and capacity models for pregnant and postpartum individuals\nTitle III of the Public Health Service Act is amended by inserting after section 330P ( 42 U.S.C. 254c\u201322 ) the following:\n330Q. Expanding capacity for maternal health outcomes (a) Establishment Beginning not later than 1 year after the date of enactment of this Act, the Secretary shall award grants to eligible entities to evaluate, develop, and expand the use of technology-enabled collaborative learning and capacity building models and improve maternal health outcomes\u2014 (1) in health professional shortage areas; (2) in areas with high rates of maternal mortality and severe maternal morbidity; (3) in rural and underserved areas; (4) in areas with significant maternal health disparities; and (5) for medically underserved populations and American Indians and Alaska Natives, including Indian Tribes, Tribal organizations, and Urban Indian organizations. (b) Use of Funds (1) Required uses Recipients of grants under this section shall use the grants to\u2014 (A) train maternal health care providers, students, and other similar professionals through models that include\u2014 (i) methods to increase safety and health care quality; (ii) implicit bias, racism, and discrimination; (iii) best practices in screening for and, as needed, evaluating and treating maternal mental health conditions and substance use disorders; (iv) training on best practices in maternity care for pregnant and postpartum individuals during public health emergencies; (v) methods to screen for social determinants of maternal health risks in the prenatal and postpartum; and (vi) the use of remote patient monitoring tools for pregnancy-related complications described in section 1115A(b)(2)(B)(xxviii); (B) evaluate and collect information on the effect of such models on\u2014 (i) access to and quality of care; (ii) outcomes with respect to the health of an individual; and (iii) the experience of individuals who receive pregnancy-related health care; (C) develop qualitative and quantitative measures to identify best practices for the expansion and use of such models; (D) study the effect of such models on patient outcomes and maternity care providers; and (E) conduct any other activity determined by the Secretary. (2) Permissible uses Recipients of grants under this section may use grants to support\u2014 (A) the use and expansion of technology-enabled collaborative learning and capacity building models, including hardware and software that\u2014 (i) enables distance learning and technical support; and (ii) supports the secure exchange of electronic health information; and (B) maternity care providers, students, and other similar professionals in the provision of maternity care through such models. (c) Application (1) In general An eligible entity seeking a grant under subsection (a) shall submit to the Secretary an application, at such time, in such manner, and containing such information as the Secretary may require. (2) Assurance An application under paragraph (1) shall include an assurance that such entity shall collect information on and assess the effect of the use of technology-enabled collaborative learning and capacity building models, including with respect to\u2014 (A) maternal health outcomes; (B) access to maternal health care services; (C) quality of maternal health care; and (D) retention of maternity care providers serving areas and populations described in subsection (a). (d) Limitations (1) Number The Secretary may not award more than 1 grant under this section. (2) Duration A grant awarded under this section shall be for a 5-year period. (e) Access to broadband In administering grants under this section, the Secretary may coordinate with other agencies to ensure that funding opportunities are available to support access to reliable, high-speed internet for grantees. (f) Technical assistance The Secretary shall provide (either directly or by contract) technical assistance to eligible entities, including recipients of grants under subsection (a), on the development, use, and sustainability of technology-enabled collaborative learning and capacity building models to expand access to maternal health care services provided by such entities, including\u2014 (1) in health professional shortage areas; (2) in areas with high rates of maternal mortality and severe maternal morbidity or significant maternal health disparities; (3) in rural and underserved areas; and (4) for medically underserved populations or American Indians and Alaska Natives. (g) Research and evaluation The Secretary, in consultation with experts, shall develop a strategic plan to research and evaluate the evidence for technology-enabled collaborative learning and capacity building models. (h) Reporting (1) Eligible entities An eligible entity that receives a grant under subsection (a) shall submit to the Secretary a report, at such time, in such manner, and containing such information as the Secretary may require. (2) Secretary Not later than 4 years after the date of enactment of this section, the Secretary shall submit to the Congress, and make available on the website of the Department of Health and Human Services, a report that includes\u2014 (A) a description of grants awarded under subsection (a) and the purpose and amounts of such grants; (B) a summary of\u2014 (i) the evaluations conducted under subsection (b)(1)(B); (ii) any technical assistance provided under subsection (f); and (iii) the activities conducted under subsection (a); and (C) a description of any significant findings with respect to\u2014 (i) patient outcomes; and (ii) best practices for expanding, using, or evaluating technology-enabled collaborative learning and capacity building models. (i) Authorization of appropriations There is authorized to be appropriated to carry out this section, $6,000,000 for each of fiscal years 2027 through 2031. (j) Definitions In this section: (1) Eligible entity (A) In general The term eligible entity means an entity that provides, or supports the provision of, maternal health care services or other evidence-based services for pregnant and postpartum individuals\u2014 (i) in health professional shortage areas; (ii) in rural or underserved areas; (iii) in areas with high rates of adverse maternal health outcomes or significant racial and ethnic disparities in maternal health outcomes; and (iv) who are\u2014 (I) members of medically underserved populations; or (II) American Indians and Alaska Natives, including Indian Tribes, Tribal organizations, and Urban Indian organizations. (B) Inclusions An eligible entity may include entities that lead, or are capable of leading a technology-enabled collaborative learning and capacity building model. (2) Health professional shortage area The term health professional shortage area means a health professional shortage area designated under section 332. (3) Indian Tribe The term Indian Tribe has the meaning given such term in section 4 of the Indian Self-Determination and Education Assistance Act. (4) Maternal mortality The term maternal mortality means a death occurring during or within the 1-year period after pregnancy caused by pregnancy-related or childbirth complications, including a suicide, overdose, or other death resulting from a mental health or substance use disorder attributed to or aggravated by pregnancy or childbirth complications. (5) Medically underserved population The term medically underserved population has the meaning given such term in section 330(b)(3). (6) Postpartum The term postpartum means the 1-year period beginning on the last date of an individual\u2019s pregnancy. (7) Severe maternal morbidity The term severe maternal morbidity means a health condition, including a mental health or substance use disorder, attributed to or aggravated by pregnancy or childbirth that results in significant short-term or long-term consequences to the health of the individual who was pregnant. (8) Technology-enabled collaborative learning and capacity building model The term technology-enabled collaborative learning and capacity building model means a distance health education model that connects health care professionals, and other specialists, through simultaneous interactive video conferencing for the purpose of facilitating case-based learning, disseminating best practices, and evaluating outcomes in the context of maternal health care. (9) Tribal organization The term Tribal organization has the meaning given such term in section 4 of the Indian Self-Determination and Education Assistance Act. (10) Urban Indian organization The term Urban Indian organization has the meaning given such term in section 4 of the Indian Health Care Improvement Act. .\n#### 4. Grants to promote equity in maternal health outcomes through digital tools\n##### (a) In general\nBeginning not later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services (in this section referred to as the Secretary ) shall make grants to eligible entities to reduce maternal health disparities by increasing access to digital tools related to maternal health care, including provider-facing technologies, such as early warning systems and clinical decision support mechanisms.\n##### (b) Applications\nTo be eligible to receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Prioritization\nIn awarding grants under this section, the Secretary shall prioritize an eligible entity\u2014\n**(1)**\nin an area with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes;\n**(2)**\nin a health professional shortage area designated under section 332 of the Public Health Service Act ( 42 U.S.C. 254e ) or a rural or underserved area; and\n**(3)**\nthat promotes technology that addresses maternal health disparities.\n##### (d) Limitations\n**(1) Number**\nThe Secretary may award not more than 1 grant under this section.\n**(2) Duration**\nA grant awarded under this section shall be for a 5-year period.\n##### (e) Technical assistance\nThe Secretary shall provide technical assistance to an eligible entity on the development, use, evaluation, and postgrant sustainability of digital tools for purposes of promoting equity in maternal health outcomes.\n##### (f) Reporting\n**(1) Eligible entities**\nAn eligible entity that receives a grant under subsection (a) shall submit to the Secretary a report, at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Secretary**\nNot later than 4 years after the date of the enactment of this Act, the Secretary shall submit to Congress a report that includes\u2014\n**(A)**\nan evaluation on the effectiveness of grants awarded under this section to improve maternal health outcomes, particularly for pregnant and postpartum individuals from racial and ethnic minority groups;\n**(B)**\nrecommendations on new grant programs that promote the use of technology to improve such maternal health outcomes; and\n**(C)**\nrecommendations with respect to\u2014\n**(i)**\ntechnology-based privacy and security safeguards in maternal health care;\n**(ii)**\nreimbursement rates for maternal telehealth services;\n**(iii)**\nthe use of digital tools to analyze large data sets to identify potential pregnancy-related complications;\n**(iv)**\nbarriers that prevent maternity care providers from providing telehealth services across States;\n**(v)**\nthe use of consumer digital tools such as mobile phone applications, patient portals, and wearable technologies to improve maternal health outcomes;\n**(vi)**\nbarriers that prevent access to telehealth services, including a lack of access to reliable, high-speed internet or electronic devices;\n**(vii)**\nbarriers to data sharing between the Special Supplemental Nutrition Program for Women, Infants, and Children program and maternity care providers, and recommendations for addressing such barriers; and\n**(viii)**\nlessons learned from expanded access to telehealth related to maternity care during the COVID\u201319 public health emergency.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $6,000,000 for each of fiscal years 2027 through 2031.\n#### 5. Report on the use of technology in maternity care\n##### (a) In general\nNot later than 60 days after the date of enactment of this Act, the Secretary of Health and Human Services shall seek to enter an agreement with the National Academies of Sciences, Engineering, and Medicine (referred to in this Act as the National Academies ) under which the National Academies shall conduct a study on the use of technology and patient monitoring devices in maternity care.\n##### (b) Content\nThe agreement entered into pursuant to subsection (a) shall provide for the study of the following:\n**(1)**\nThe use of innovative technology (including artificial intelligence) in maternal health care, including the extent to which such technology has affected racial or ethnic biases in maternal health care.\n**(2)**\nThe use of patient monitoring devices (including pulse oximeter devices) in maternal health care, including the extent to which such devices have affected racial or ethnic biases in maternal health care.\n**(3)**\nBest practices for reducing and preventing racial or ethnic biases in the use of innovative technology and patient monitoring devices in maternity care.\n**(4)**\nBest practices in the use of innovative technology and patient monitoring devices for pregnant and postpartum individuals from racial and ethnic minority groups.\n**(5)**\nBest practices with respect to privacy and security safeguards in such use.\n##### (c) Report\nThe agreement under subsection (a) shall direct the National Academies to complete the study under this section, and transmit to Congress a report on the results of the study, not later than 24 months after the date of enactment of this Act.\n#### 6. Definitions\nIn this Act:\n**(1) Maternal mortality**\nThe term maternal mortality means a death occurring during or within a 1-year period after pregnancy, caused by pregnancy-related or childbirth complications, including a suicide, overdose, or other death resulting from a mental health or substance use disorder attributed to or aggravated by pregnancy-related or childbirth complications.\n**(2) Maternity care provider**\nThe term maternity care provider means a health care provider who\u2014\n**(A)**\nis a physician, a physician assistant, a midwife who meets, at a minimum, the international definition of a midwife and global standards for midwifery education as established by the International Confederation of Midwives, an advanced practice registered nurse, a doula accredited by a State to receive reimbursement for doula services under a State plan (or a waiver of such plan) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), or a lactation consultant certified by the International Board of Lactation Consultant Examiners; and\n**(B)**\nhas a focus on maternal or perinatal health.\n**(3) Postpartum**\nThe term postpartum refers to the 1-year period beginning on the last day of the pregnancy of an individual.\n**(4) Racial and ethnic minority group**\nThe term racial and ethnic minority group has the meaning given such term in section 1707(g)(1) of the Public Health Service Act ( 42 U.S.C. 300u\u20136(g)(1) ).\n**(5) Severe maternal morbidity**\nThe term severe maternal morbidity means a health condition, including mental health conditions and substance use disorders, attributed to or aggravated by pregnancy or childbirth that results in significant short-term or long-term consequences to the health of the individual who was pregnant.",
      "versionDate": "2026-04-15",
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
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "958",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tech to Save Moms Act",
      "type": "S"
    },
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
        "updateDate": "2026-04-22T13:59:44Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8317ih.xml"
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
      "title": "Tech to Save Moms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tech to Save Moms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize grants to evaluate, develop, and expand the use of technology-enabled collaborative learning and capacity building models to improve maternal health outcomes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T05:48:32Z"
    }
  ]
}
```
