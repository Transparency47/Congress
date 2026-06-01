# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6765?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6765
- Title: Safe Passages Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6765
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-01-14T16:06:50Z
- Update date including text: 2026-01-14T16:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6765",
    "number": "6765",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Safe Passages Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T16:06:50Z",
    "updateDateIncludingText": "2026-01-14T16:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6765ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6765\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Smith of New Jersey (for himself and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prioritize and fund life-affirming maternal and child health initiatives globally by equipping local health providers and community health workers to reduce the leading causes of maternal and child mortality, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Passages Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAround the world, over 287,000 women die each year from pregnancy-related complications\u2014most of which are preventable.\n**(2)**\nIn sub-Saharan Africa, the maternal mortality rate in 2023 was 442 per 100,000 live births, compared to 14 per 100,000 in developed countries.\n**(3)**\nSub-Saharan Africa accounts for approximately 70 percent of all global maternal deaths.\n**(4)**\nThese deaths are nearly all caused by treatable conditions including postpartum hemorrhage, severe preeclampsia, infection, and obstructed labor, reflecting a lack of access to skilled birth attendants with the training, tools, and infrastructure needed to provide life-affirming obstetrical care.\n**(5)**\nShort of death and in the absence of skilled pregnancy care and birth attendance, women may also suffer severe complications during and after childbirth including stillbirths, obstetric fistula, severe anemia, infection, and cardiovascular damage, all of which can cause lifelong complications.\n**(6)**\nMaternal death, which is also associated with a decline in the standard of living for children in the bereaved family, is one of the leading causes of fetal and newborn death.\n**(7)**\nInfants whose mothers die during childbirth face dramatically elevated risk with a least 20-fold times risk of mortality in the first month of life.\n**(8)**\nEven beyond the neonatal period, maternal death is associated with 4\u20136 times greater mortality risk for young children.\n**(9)**\nThese statistics reflect not merely public health trends but the personal tragedies of women, children, and families whose futures are forever altered.\n**(10)**\nThe first 1,000 days of life\u2014from conception to age 2\u2014represent a critical window in which appropriate maternal and infant health care can dramatically reduce risk of child malnutrition, stunting, developmental delays, and early childhood illness and help prevent and treat complications of pregnancy that can have short- and long-term impacts on the health of mothers.\n**(11)**\nStrengthening maternal and child health preserves both mother and child, strengthens family units, enhances a myriad of human development goals, and upholds the dignity and worth of every human life.\n**(12)**\nThe engagement and support of fathers through financial, material, relational and emotional support of the mother and child, is key to strengthening maternal and child health and promoting a safe passage, and has been correlated with increased prenatal care, enhanced skilled birth attendance, improved maternal mental health and higher neonatal survival.\n**(13)**\nPrograms such as Maternal Life International\u2019s Safe Passages model have proven successful in training frontline providers, reducing mortality, and delivering sustainable, culturally respectful, life-affirming care in low-resource settings.\n#### 3. Purpose\nThe purpose of this Act is to advance and fund life-affirming maternal and child health interventions that\u2014\n**(1)**\nequip local providers, including midwives, physicians, physician assistants, nurse practitioners, and community health workers, with life-affirming training in how to prevent, recognize, and manage the leading causes of maternal and perinatal death and their complications;\n**(2)**\nprovide medical resources, training, and emergency obstetric equipment to carry out the above skilled life-affirming management of obstetrical and perinatal complications;\n**(3)**\nprovide education and support for health care and nutrition during the first 1,000 days of life;\n**(4)**\nprovide education and support for fathers in their support and responsibility for the well-being of the mother and child;\n**(5)**\nsupport a continuum of life-affirming care for women and men inclusive of pre-conception health, fertility health, fertility awareness, healthy child spacing, natural family planning, safe birth and postpartum mental health; and\n**(6)**\noperate in full alignment with respect for life at all stages from conception to natural death and strengthening the family.\n#### 4. Safe passages maternal and child health program\n##### (a) Establishment\nThere is established a global initiative to be known as the Safe Passages Maternal and Child Health Program to help reduce maternal and child mortality in low- and lower-middle-income countries with high maternal and child mortality rates through fiscal year 2030, through faith-based health partnerships, community-based care, collaboration with national health systems, and life-affirming health interventions.\n##### (b) Elements\nInterventions supported by the program established by subsection (a) are for life-affirming training and resource assistance for the following:\n**(1)**\nPrevention, recognition, diagnosis and treatment of obstetrical hemorrhage, and its complications, including postpartum anemia.\n**(2)**\nPrevention, recognition, diagnosis and management of preeclampsia and other hypertensive, metabolic and cardiovascular disorders of pregnancy, and their complications, up to 1-year postpartum.\n**(3)**\nPrevention, recognition, diagnosis and treatment of infections and their complications associated with ectopic pregnancy, miscarriage, stillbirth, normal pregnancy, childbirth and the postpartum period.\n**(4)**\nPrevention, recognition, diagnosis and management of obstructed labor and its complications, including uterine rupture, obstetric fistulas, and additional related complications.\n**(5)**\nReduction of fetal, perinatal, neonatal and infant mortality, including stillbirth, by preventing, recognizing, diagnosing and treating fetal distress, newborn asphyxia, birth trauma, intrauterine growth restriction, premature birth, small size for gestational age, and neonatal infections and sepsis.\n**(6)**\nNutritional and health education for the mother and provision of nutritional resources for the mother and child during the first 1,000 days of life, from conception to 2 years of age provided through coordination with the office leading on global food security.\n**(7)**\nTraining and dissemination of natural fertility awareness based methods in accordance with evidence-based non-abortive practices.\n**(8)**\nPromote increasing fathers\u2019 support and involvement for mothers and children.\n##### (c) Implementation\nThe Secretary of State shall prioritize the implementation of the program established by subsection (a) in collaboration with new and existing global health partnerships deemed to be efficient and reliable in the expenditure of taxpayer dollars, prioritizing local faith-based providers and faith-based organizations with strong local partnerships and which have experience and expertise in maternal and child health delivery in resource-limited settings.\n#### 5. Amendment to existing law and availability of funds\n##### (a) Amendment\nSection 104(c) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151b(c) ) is amended to read as follows:\n(c) Maternal and child health and nutrition Assistance under this section shall prioritize maternal and child health interventions consistent with the Safe Passages Maternal and Child Health Program established by section 4 of the Safe Passages Act of 2025, including prevention and treatment of obstetric complications, such as hemorrhage, hypertensive disorders, sepsis, obstructed labor, and neonatal resuscitation; support for maternal nutrition; health care for the child throughout the first 1,000 days of life from conception to approximately 2 years of age; and support for fathers to care for mothers and their children. Such assistance shall promote natural methods of fertility awareness and shall not be used for abortion or abortion-related services. .\n##### (b) Availability\nNotwithstanding any other provision of law, the President, acting through the Secretary of State, shall, from funds made available under the Global Health Programs account, make available not less than $400,000,000 annually to carry out section 4 of this Act and subsection (c) of section 104 of the Foreign Assistance Act of 1961, as amended by subsection (a), including for life-affirming maternal and child health programs that\u2014\n**(1)**\nfocus on the prevention of maternal, fetal, and neonatal deaths;\n**(2)**\npromote natural methods of fertility awareness and couple-centered care;\n**(3)**\nprovide training and emergency response to the 5 leading causes of maternal mortality: hemorrhage, hypertensive disorders, sepsis and infections, obstructed labor and uterine rupture, and miscarriage, to include surgical management of obstetrical emergencies and pregnancy complications (not to include elective abortions);\n**(4)**\nprovide training and response for the leading causes of maternal late postpartum complications: severe anemia, neurological and cardiovascular injury following hypertensive disorders, fistula, hemorrhage, infections, and postpartum mental health conditions;\n**(5)**\nprovide training and emergency response to the leading causes of infant mortality: premature birth, birth complications (birth asphyxia/trauma), intrauterine growth restriction, and neonatal sepsis and infections;\n**(6)**\nuphold life-affirming care for both mother and child; and\n**(7)**\nengage fathers in these life-affirming maternal and child health programs as well as in the care of the mothers and their children.\n#### 6. Reporting and oversight\nNot later than 2 years after the date of the enactment of this Act, and biennially thereafter, the Secretary of State shall submit to Congress a report detailing\u2014\n**(1)**\nthe number of trainings offered, providers and cadres trained, including midwives, physicians, community health workers, nurses, physician assistants, nurse practitioners, pharmacists, laboratory technicians, and other birth attendants, and the content of the training curricula;\n**(2)**\nthe effectiveness of such trainings, measured rigorously and objectively, to determine improvements in knowledge and skills through pre- and post-training assessments;\n**(3)**\ninitial and annual co-investments made by private industry and foreign governments;\n**(4)**\nsustainability plans and timelines for organizations and governments receiving assistance;\n**(5)**\nthe number of facilities receiving support for facility upgrades (such as basic lab tests, blood transfusion services, second-line uterotonics for postpartum hemorrhage, broad spectrum antibiotics, referral and transport systems for rural health-care facilities, and ultrasound services for recognition and management of high-risk pregnancies), and the nature of the upgrades;\n**(6)**\nany support provided for establishment of revolving capital funds;\n**(7)**\ncommunity- and hospital-level data on maternal, fetal, neonatal and infant morbidity and mortality, presented as a comparison between areas served and not served;\n**(8)**\nregions and facilities served;\n**(9)**\nestimated maternal and child lives saved; and\n**(10)**\ncompliance with United States foreign assistance restrictions and goals of this Act.",
      "versionDate": "2025-12-16",
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
        "name": "International Affairs",
        "updateDate": "2026-01-14T16:06:50Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6765ih.xml"
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
      "title": "Safe Passages Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Passages Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prioritize and fund life-affirming maternal and child health initiatives globally by equipping local health providers and community health workers to reduce the leading causes of maternal and child mortality, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T12:18:26Z"
    }
  ]
}
```
