# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3589?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3589
- Title: RESTORE Act
- Congress: 119
- Bill type: HR
- Bill number: 3589
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-12-05T21:30:41Z
- Update date including text: 2025-12-05T21:30:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3589",
    "number": "3589",
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
    "title": "RESTORE Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:30:41Z",
    "updateDateIncludingText": "2025-12-05T21:30:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:01:25Z",
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
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "WV"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "MD"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3589ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3589\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mrs. Harshbarger (for herself and Mr. Moore of West Virginia ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo expand and promote research and data collection on reproductive health conditions, to provide training opportunities for medical professionals to learn how to diagnose and treat reproductive health conditions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reproductive Empowerment and Support Through Optimal Restoration Act or the RESTORE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAll women and men are worthy of the highest standard of medical care, including the opportunity to assess, understand, and improve their reproductive health. Unfortunately, many couples do not receive adequate information about their reproductive health and do not have access to restorative reproductive medicine.\n**(2)**\nThere is a growing interest among women to proactively assess their overall health and understand how factors such as age and medical history contribute to reproductive health and fertility.\n**(3)**\nReproductive health conditions are the leading causes of infertility, which affects 15 to 16 percent of couples in the United States. Such conditions include the following:\n**(A)**\nEndometriosis, a disease where tissue resembling endometrial lining tissue grows outside of the uterus. The tissue often adheres to different organs, disfiguring them and, through scar tissue or adhesions, can make the organs stick to one another or to the pelvic walls. It has been found in the abdominal organs, the bowel, the diaphragm, the lungs, the brain, and the eye. It is a progressive disease and has been compared to growing like cancer. Endometriosis is often diagnosed in stages, with Stage I as the mildest form and Stage IV as the most severe and widespread form. The average diagnosis delay for endometriosis is 6 to 12 years. Endometriosis frequently goes undiagnosed, and women may suffer for years with painful periods, pelvic pain, or infertility. The cause of endometriosis is unknown.\n**(B)**\nAdenomyosis, a disease that occurs when endometrial tissue (tissue that would normally line the inside of the uterus) grows into the muscle layer of the uterus. Adenomyosis is different from, but can exist concurrently with, endometriosis. Adenomyosis may increase the risk of miscarriage and preterm labor and may contribute to infertility. The cause of adenomyosis is unknown.\n**(C)**\nPolycystic ovary syndrome, a reproductive hormonal disorder that causes cysts to grow on the ovaries, usually as a result of hormonal imbalances. Polycystic ovary syndrome affects approximately 15 percent of women overall but is more common among women with infertility. It is more prevalent among women with obesity and insulin resistance. Women with polycystic ovary syndrome who are trying to achieve pregnancy are commonly prescribed oral ovulation medication and hormonal injections that stimulate ovulation. Effective diagnosis and treatment exist, and should be made available for all women. Accurate and timely diagnosis and treatment can correct underlying hormonal imbalances, critical for both long-term health improvements as well as for fertility outcomes.\n**(D)**\nUterine fibroids, which are muscular tumors that grow in the wall of the uterus. While not all women will experience symptoms associated with fibroids, if the tumors are large enough or embedded far enough in the uterine lining, they can lead to pain and heavy bleeding. Treatment for fibroids may include assessment of underlying hormonal imbalances, hysteroscopic myomectomy, abdominal myomectomy, uterine fibroid embolization, and uterine artery embolization. Uterine fibroids can increase risks of preterm labor, pregnancy complications leading to a cesarean section, and placental abruption, among other risks. The cause of uterine fibroids is unknown.\n**(E)**\nBlocked fallopian tubes, a condition where the fallopian tubes are blocked by tubal spasm, scarring from inflammatory conditions, debris, tubal polyps, tubal ligation, prior ectopic pregnancy, pelvic adhesions, endometriosis, prior pelvic infection (pelvic inflammatory disease or PID ). Approximately 1 in 4 women with infertility have a tubal blockage. This condition makes achieving pregnancy difficult, if not impossible. Treatments for a blockage include fallopian tube recanalization, tubo-tubal anastomosis (tubal ligation reversal), or neosalpingostomy/fimbrioplasty.\n**(4)**\nResearch shows 4 or more conditions or factors are the cause of most male and female infertility.\n**(5)**\nThere is a gap in research and care for male and female reproductive health conditions, which affect many Americans struggling with unexplained infertility.\n**(6)**\nRestorative reproductive medicine aims to diagnose and treat underlying hormonal and other imbalances, restore health where possible, and improve women\u2019s health functioning and long-term outcomes.\n**(7)**\nRestorative reproductive medicine can eliminate barriers to successful conception, pregnancy, and birth. It can also address some causes of recurrent miscarriages.\n**(8)**\nRestorative reproductive medicine often alleviates other difficult symptoms associated with reproductive health conditions, including hormonal acne, hormonal weight gain, hormonal mood and depression, painful periods, painful flare-ups, bloating, inflammation, heavy periods, irregular periods, nerve pain, bowel symptoms, pain during sexual intercourse, and back pain.\n#### 3. Definitions\nIn this Act:\n**(1) Assisted reproductive technology**\nThe term assisted reproductive technology means any treatments or procedures that involve the handling of a human egg, sperm, and embryo outside of the body with the intent of facilitating a pregnancy, including artificial insemination, intrauterine insemination, in vitro fertilization, gamete intrafallopian fertilization, zygote intrafallopian fertilization, egg, embryo, and sperm cryopreservation, and egg or embryo donation.\n**(2) Fertility awareness-based methods**\nThe term fertility awareness-based methods means modern, evidence-based methods of tracking the menstrual cycle through observable biological signs in a woman, such as body temperature, cervical fluid, and hormone production in the reproductive system, including luteinizing hormone (LH) and estrogen. Such methods include Fertility Education and Medical Management, the sympto thermal method, the Marquette method, the Creighton method, and the Billings ovulation method.\n**(3) Fertility education and medical management**\nThe term fertility education and medical management means the program developed in collaboration with the Reproductive Health Research Institute for medical research, protocols, and medical training for health care professionals in order to enable the clinical application of important research advances in reproductive endocrinology, by providing education for women about their bodies and hormonal health and medical support, as appropriate.\n**(4) Infertility**\nThe term infertility means a symptom of an underlying disease or condition within a person\u2019s body that makes it difficult or impossible to successfully conceive and carry a child to term, which is diagnosed after 12 months of intercourse without the use of a chemical, barrier, or other contraceptive method for women under 35 or after 6 months of targeted intercourse without the use of a chemical, barrier, or other contraceptive method for women 35 and older, where conception should otherwise be possible.\n**(5) Natural procreative technology; NaProTECHNOLOGY**\nThe term Natural Procreative Technology or NaProTECHNOLOGY means an approach to health care that monitors and maintains a woman\u2019s reproductive and gynecological health, including laparoscopic gynecologic surgery to reconstruct the uterus, fallopian tubes, ovaries, and other organ structures to eliminate endometriosis and other reproductive health conditions.\n**(6) Reproductive health conditions**\nThe term reproductive health conditions includes endometriosis, adenomyosis, polycystic ovary syndrome, uterine fibroids, blocked fallopian tubes, hormone imbalances, hyperprolactinemia, thyroid conditions, ovulation dysfunctions, and other health conditions that make it difficult or impossible to successfully conceive a child where conception should otherwise be possible.\n**(7) Restorative reproductive health**\nThe term restorative reproductive health includes empowering women and men to know and understand their bodies and appreciate the importance of natural reproductive health to overall health and well-being, including through the use of body literacy programs that incorporate science-based charting methods, teacher-lead reproductive health education, restorative reproductive medicine, Natural Procreative Technology, fertility awareness-based methods, and fertility education and medical management.\n**(8) Restorative reproductive medicine**\nThe term restorative reproductive medicine \u2014\n**(A)**\nmeans any scientific approach to reproductive medicine that seeks to cooperate with, or restore the normal physiology and anatomy of, the human reproductive system, without the use of methods that are inherently suppressive, circumventive, or destructive to natural human functions; and\n**(B)**\nmay include ultrasounds, blood tests, hormone panels, laparoscopic and exploratory surgeries, examining the man's or woman\u2019s overall health and lifestyle, eliminating environmental endocrine disruptors, and assessing the health and fertility of the individual's partner, Natural Procreative Technology, fertility awareness-based methods, and fertility education and medical management.\n#### 4. Prohibiting discrimination against health care providers who do not participate in assisted reproductive technology\nNotwithstanding any other law, the Federal Government, and any person or entity that receives Federal financial assistance, including any State or local government, may not penalize, retaliate against, or otherwise discriminate against a health care provider on the basis that the provider does not or declines to\u2014\n**(1)**\nassist in, receive training in, provide, perform, refer for, pay for, or otherwise participate in assisted reproductive technology; or\n**(2)**\nfacilitate or make arrangements for any of the activities specified in paragraph (1) in a manner that violates the provider's sincerely held religious beliefs or moral convictions.\n#### 5. Implementing literature reviews on the standard of care for the diagnosis of infertility\n##### (a) In general\nThe Assistant Secretary for Health of the Department of Health and Human Services (referred to in this section as the Assistant Secretary ) shall collect data on the topics described in subsection (b) and, not later than 2 years after the date of enactment of this Act and every 3 years thereafter, issue a report on the standard of care for women who have been diagnosed with infertility.\n##### (b) Topics\nIn carrying out subsection (a), the Assistant Secretary shall\u2014\n**(1)**\nassess peer-reviewed studies on referrals to restorative reproductive medicine that are given prior to referrals for or use of assisted reproductive technology;\n**(2)**\nassess peer-reviewed studies related to access to patient and health care provider information and training for fertility awareness-based methods; and\n**(3)**\nassess the extent to which the treatments, tests, and training described in paragraphs (1) and (2) are covered under public and private health plans.\n##### (c) Privacy requirements\nIn carrying out subsection (a), the Assistant Secretary shall ensure that the privacy and confidentiality of individual patients are protected in a manner consistent with relevant privacy and confidentiality law.\n#### 6. Implementing literature reviews on the standard of care for individuals seeking a reproductive health condition diagnosis\n##### (a) In general\nThe Assistant Secretary for Health of the Department of Health and Human Services (referred to in this section as the Assistant Secretary ) shall collect data on the topics described in subsection (b) and, not later than 2 years after the date of enactment of this Act and every 3 years thereafter, issue a report on the standard of care for women and men seeking reproductive health condition diagnoses.\n##### (b) Topics\nIn carrying out paragraph (1), the Assistant Secretary shall\u2014\n**(1)**\nassess peer-reviewed studies related to access to restorative reproductive medicine and restorative reproductive health, including access to medical professionals trained in NaProTechnology and fertility education and medical management;\n**(2)**\nassess peer-reviewed studies related to access to information and training on fertility awareness-based methods; and\n**(3)**\nassess the extent to which the treatments, tests, and training described in paragraphs (1) and (2) are covered under public and private health plans.\n##### (c) Privacy requirements\nIn carrying out subsection (a), the Assistant Secretary shall ensure that the privacy and confidentiality of individual patients are protected in a manner consistent with relevant privacy and confidentiality law.\n#### 7. Expanding the national survey of family growth to include reproductive health conditions, restorative reproductive medicine, and fertility awareness-based methods\n##### (a) In general\nThe Director of the Centers for Disease Control and Prevention (referred to in this section as the Director ) shall evaluate the National Survey of Family Growth conducted by the National Center for Health Statistics of the Centers for Disease Control and Prevention and consider making modifications to the survey questions used for such purposes.\n##### (b) Topics\nThe evaluation by the Director pursuant to subsection shall include consideration of adding questions related to\u2014\n**(1)**\nrestorative reproductive health;\n**(2)**\nreproductive health conditions and infertility;\n**(3)**\nrestorative reproductive medicine availability and utilization; and\n**(4)**\navailability of, and training on, fertility awareness-based methods.\n##### (c) Report\nThe Director shall submit to Congress a report on the evaluation under subsection (a) not later than 3 years after the date of enactment of this Act and every 3 years thereafter.\n#### 8. Including access to title x award funds for restorative reproductive medicine grantees\nSection 1006 of the Public Health Service Act ( 42 U.S.C. 300a\u20134 ) is amended by adding at the end the following:\n(e) (1) Notwithstanding any other requirements relating to the experience required for an applicant to qualify for a grant or contract under this title, an entity shall be deemed eligible for a grant or contract under this title on the basis of being primarily engaged in providing restorative reproductive medicine, or providing training and education for medical students and professionals in restorative reproductive medicine, provided that such entity is otherwise eligible for the grant or contract. (2) In this subsection, the term restorative reproductive medicine has the meaning given such term in section 3 of the RESTORE Act . .\n#### 9. Advancing education on reproductive health conditions and women\u2019s natural cycle\n##### (a) Expanding grant access and application\nThe Deputy Assistant Secretary for Population Affairs of the Department of Health and Human Services (referred to in this section as the Deputy Assistant Secretary ) shall develop, within the existing Teen Pregnancy Prevention program, access to, and advertisement for, applicants for grants under such program that specialize in restorative reproductive medicine, restorative reproductive health, and fertility awareness-based methods. To be eligible to receive an award under this subsection, an entity shall be primarily engaged in services or education relating to restorative reproductive medicine, restorative reproductive health, or fertility awareness-based methods.\n##### (b) Report\nNot later than 18 months after the date of enactment of this Act, the Deputy Assistant Secretary shall submit to Congress and make publicly available on the website of the Office of Population Affairs a report on recipients of grants under the Teen Pregnancy Prevention program and the services, education, and training provided by such recipients.\n#### 10. Advancing restorative reproductive medicine and fertility awareness-based methods training under the Reproductive Health National Training Center\n##### (a) In general\nThe Assistant Secretary for Health of the Department of Health and Human Services (referred to in this section as the Assistant Secretary ) shall coordinate with the Office of Population Affairs and the Office on Women\u2019s Health to review, revise, and instruct the staff of the Reproductive Health National Training Center on reproductive health conditions, restorative reproductive medicine, restorative reproductive health, and fertility awareness-based methods.\n##### (b) Training\nBeginning not later than 2 years after the date of enactment of this Act, as a condition for receipt of a grant or contract under title X of the Public Health Service Act ( 42 U.S.C. 300 et seq. ), the staff of the Reproductive Health National Training Center shall provide training to staff working in other entities receiving grants or contracts under title X of the Public Health Service Act ( 42 U.S.C. 300 et seq. ) about reproductive health conditions, restorative reproductive medicine, restorative reproductive health, and fertility awareness-based methods, which may include providing toolkits and other information, including online, about peer learning opportunities, NaProTechnology educational fellowships, fertility education and medical management, short videos on reproductive health conditions and restorative reproductive medicine, and contract medical professional seminars and training.\n#### 11. Advancing lifestyle medicine prescriptions as a method for treating male infertility\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in collaboration with the Assistant Secretary for Health and the Deputy Assistant Secretary for Population Affairs, shall evaluate, and develop within relevant health programs of the Department of Health and Human Services, education for awareness of and treatment for, through lifestyle and metabolic modifications, male factor infertility.\n##### (b) Topics\nThe development of treatment for male factor infertility in health programs by the Secretary pursuant to subsection (a) shall include consideration for\u2014\n**(1)**\nsperm count;\n**(2)**\nsperm motility;\n**(3)**\nsperm morphology;\n**(4)**\nerectile dysfunction;\n**(5)**\nhormonal imbalance;\n**(6)**\nsexually transmitted infections;\n**(7)**\nendocrine-disrupting chemicals;\n**(8)**\ntesticular torsion;\n**(9)**\nvaricoceles;\n**(10)**\nobesity;\n**(11)**\ninsulin resistance; and\n**(12)**\nsubstance use.\n##### (c) Report\nNot later than 18 months after the date of enactment of this Act, the Secretary shall submit to Congress, and make publicly available, plans to develop education on treatment for male factor infertility in health programs of the Department of Health and Human Services.\n#### 12. Modernizing medical coding to accurately classify and reimburse providers of restorative treatments\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in collaboration with the Administrator of the Centers for Medicare & Medicaid Services, the Director of the National Center for Health Statistics of the Centers for Disease Control and Prevention, and the CPT Editorial Panel of the American Medical Association, shall take all necessary actions to update, not later than 1 year after the date of enactment of this Act, diagnostic and procedural codes related to infertility treatments to reflect the latest knowledge and practices related to the practice of restorative reproductive medicine.\n##### (b) Requirements\nIn carrying out subsection (a), the Secretary shall\u2014\n**(1)**\nconduct a thorough review and revision of ICD\u201310\u2013CM codes for conditions such as endometriosis, polycystic ovary syndrome, uterine fibroids, adenomyosis, blocked fallopian tubes, and male mechanisms of infertility to ensure accurate classification of severe, chronic reproductive health conditions requiring medical or surgical intervention;\n**(2)**\ndevelop and implement new ICD\u201310\u2013PCS codes for laparoscopic excision, hysteroscopic procedures, and other minimally invasive surgeries aimed at addressing such conditions, including the excision of fibroids, ovarian cysts, and adenomyosis-related tissue removal;\n**(3)**\nrevise diagnostic and procedural codes under the International Classification of Diseases to more accurately reflect severe and chronic reproductive conditions;\n**(4)**\ndevelop new Current Procedural Terminology codes for minimally invasive surgeries and other interventions that target infertility-related conditions, specifically including laparoscopic excision, differentiation between laparoscopic ablation and laparoscopic excision of endometriosis, appendectomy related to endometriosis, bowel resection related to endometriosis, hysteroscopic myomectomy, abdominal myomectomy, cystectomy, other minimally invasive procedures that directly treat underlying reproductive health conditions, and for family planning services, specifically including female cycle charting instruction;\n**(5)**\nestablish new Healthcare Common Procedure Coding System codes to ensure appropriate reimbursement under the Medicare and Medicaid programs for reproductive health-related surgical procedures, postoperative care, and family planning services, specifically including female cycle charting instruction;\n**(6)**\nconduct an actuarial analysis to determine appropriate reimbursement rates and assign relative value units to reflect the complexity and time required for these procedures, including physician visits, surgical interventions, education, and care coordination, ensuring that providers are incentivized to offer thorough diagnostic and restorative care; and\n**(7)**\nimplement a restorative reproductive medicine bundled payment model accurately reimbursing health care providers for the time and resources needed to identify, diagnose, and treat the underlying cause of infertility or reproductive health condition in order to provide restorative fertility care, including\u2014\n**(A)**\nbundles that include diagnostics, medical management, surgical intervention, education, care coordination, and extended physician time; and\n**(B)**\nestablishing a corresponding set of Current Procedural Terminology codes for the bundle type variations and conduct an actuarial analysis to determine appropriate reimbursement rates and assign relative value units reflecting the complexity of restorative care.\n#### 13. Expanding research on reproductive health conditions, fertility awareness-based methods, and infertility\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ), in coordination with the Assistant Secretary for Health, the Director of the Agency for Healthcare Research and Quality, the Director of the Advanced Research Projects Agency for Health, the Director of the Centers for Disease Control and Prevention, the Director of the National Institutes of Reproductive Empowerment and Support Through Optimal Restoration Act Health, and the heads of other agencies and offices of the Department of Health and Human Services that are conducting research on reproductive health conditions, infertility, and maternal health, shall expand and coordinate programs to conduct and support research on reproductive health conditions.\n##### (b) Topics\nThe research directed by the Secretary pursuant to subsection (a) may include research on\u2014\n**(1)**\nthe causes of reproductive health conditions, especially endometriosis, adenomyosis, uterine fibroids, and polycystic ovary syndrome;\n**(2)**\nways to diagnose reproductive health conditions;\n**(3)**\nrestorative reproductive medicine and new treatment options for reproductive health conditions;\n**(4)**\nendocrine disrupting chemicals in endometriosis, the relationship of endometriosis and cancer, prenatal and epigenetic influences on the risk for endometriosis;\n**(5)**\npremenstrual syndrome, hormone dysfunction, ovulation defects, abnormal uterine bleeding, adhesion prevention, tubal corrective surgery, and preconception and pregnancy health;\n**(6)**\nthe growth and progression of reproductive health conditions and recurrence post-surgical procedures;\n**(7)**\nthe increasing prevalence of sexually transmitted infections and related effects on fertility in men and women;\n**(8)**\nthe impact of exposure to microplastics on male and female reproductive organs and the specific impact of such exposure on sperm quality;\n**(9)**\nmale mechanisms of infertility, including low sperm count, low sperm motility, erectile dysfunction, low testosterone, varicocele, testicular torsion, substance use, and obesity; and\n**(10)**\nthe effectiveness of restorative reproductive medicine to achieve pregnancy and live birth.\n##### (c) Report\nNot later than 2 years after the date of enactment of this Act, the Secretary shall make an ongoing report on the research publicly available on the website of the Department of Health and Human Services.\n#### 14. Severability\nIf any provision of this Act, or the application of such provision to any person, entity, government, or circumstance, is held to be unconstitutional, the remainder of this Act, or the application of such provision to all other persons, entities, governments, or circumstances, shall not be affected thereby.",
      "versionDate": "2025-05-23",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1882",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RESTORE Act",
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
        "updateDate": "2025-07-14T15:19:54Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3589ih.xml"
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
      "title": "RESTORE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-03T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESTORE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reproductive Empowerment and Support Through Optimal Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand and promote research and data collection on reproductive health conditions, to provide training opportunities for medical professionals to learn how to diagnose and treat reproductive health conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-03T04:18:25Z"
    }
  ]
}
```
