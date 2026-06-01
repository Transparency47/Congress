# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5828?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5828
- Title: Dads Matter Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5828
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-01-29T22:41:13Z
- Update date including text: 2026-01-29T22:41:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5828",
    "number": "5828",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Dads Matter Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-29T22:41:13Z",
    "updateDateIncludingText": "2026-01-29T22:41:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
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
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:04:45Z",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "AZ"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5828ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5828\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mr. Vindman (for himself and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Health and Human Services to carry out a public awareness campaign to increase awareness of the importance of father inclusion and engagement in improving overall health outcomes during pregnancy, childbirth, and postpartum, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dads Matter Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nFather engagement can play an important role in improving maternal health care, addressing maternal mortality and morbidity, and bettering the development and long-term growth of the child.\n**(2)**\nThe participation of fathers during prenatal care appointments provides the mother with additional support to recognize potential pregnancy-related complications that could lead to maternal mortality and morbidity.\n**(3)**\nWhen fathers are involved during pregnancy appointments and milestones, mothers are 1.5 times more likely to receive prenatal care in the first trimester, which improves health outcomes for both the mother and baby.\n**(4)**\nFather support during pregnancy can help promote behavioral health of the mother.\n**(5)**\nFather engagement reduces the risks of postpartum mood and anxiety disorders and contributes to a lower likelihood of preterm birth and a healthier birthweight.\n**(6)**\nIncluding fathers in conversations about safe sleep guidelines and sharing guidance about infant crying and the risks of shaken baby syndrome can help reduce infant deaths.\n**(7)**\nActive support of the father during breastfeeding greatly increases the chances of successful breastfeeding, which improves the physical and mental health of the baby and the mother.\n**(8)**\nPhysical contact between the father and the baby just after birth and in the months following birth has been shown to improve the health and development of the baby, improve the mental health of the father, and foster father-child bonding in the short-term and long-term.\n#### 3. Increasing awareness of the importance of father inclusion and engagement in the pregnancy, birth, and postpartum process\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services shall carry out a public awareness campaign to increase understanding of the importance of father inclusion and engagement in improving overall health outcomes during pregnancy, childbirth, and postpartum, for both the mother and baby.\n##### (b) Requirements\nThe campaign under subsection (a) shall include\u2014\n**(1)**\nmessaging intended to provide information to the public about the importance of a father\u2019s role in pregnancy and parenting;\n**(2)**\nresources and information to counter popular narratives that minimize the importance of engaged and involved fathers in pregnancy and parenting; and\n**(3)**\nresources and information that promote awareness about the impact of father inclusion on maternal and infant outcomes, including\u2014\n**(A)**\nthe importance of father-to-infant, skin-to-skin contact in improving the health and development of a newborn and fostering father-child bonding in the short- and long-term;\n**(B)**\nthe role of fathers in promoting the behavioral health of the mother;\n**(C)**\nthe role of fathers in increasing the number of prenatal and postpartum appointments a mother attends;\n**(D)**\nthe effects of father attendance during prenatal and postnatal appointments;\n**(E)**\nthe effects of paternal postpartum depression;\n**(F)**\nthe role of father support in improving rates of successful breastfeeding; and\n**(G)**\nthe role of father involvement in providing the mother with additional support to recognize potential pregnancy-related complications, which could include\u2014\n**(i)**\npreeclampsia;\n**(ii)**\nperipartum cardiomyopathy;\n**(iii)**\npreterm labor;\n**(iv)**\nperinatal mood and anxiety disorders;\n**(v)**\npregnancy loss or miscarriage;\n**(vi)**\nstillbirth;\n**(vii)**\nhigh blood pressure;\n**(viii)**\ncervical infections;\n**(ix)**\ngestational diabetes;\n**(x)**\nplacental abruption;\n**(xi)**\nectopic pregnancy; and\n**(xii)**\nuterine rupture.\n#### 4. Guidance to States on encouraging father inclusion and engagement in the pregnancy, birth, and postpartum process\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services shall issue guidance to States that addresses how States can encourage and incentivize providers of maternity care, including hospitals, health care systems, midwifery practices, freestanding birth centers, community health centers, and other maternity care providers, and providers of health care coverage, including managed care entities, to provide training and education to health care practitioners, such as pediatricians, obstetricians, and gynecologists, about the benefits of including and engaging fathers in the pregnancy, birth, and postpartum process.\n##### (b) Requirements\nThe guidance under subsection (a) shall\u2014\n**(1)**\ninclude information on how health care practitioners can\u2014\n**(A)**\noffer peer-to-peer, father-to-father encouragement, support, and education in communities that traditionally are not inclusive of fathers;\n**(B)**\nprovide fathers with information on\u2014\n**(i)**\nwhat to expect before, during, and after the birth process;\n**(ii)**\nhow to better\u2014\n**(I)**\nunderstand and support their partner throughout such process; and\n**(II)**\nserve as an advocate in her care; and\n**(iii)**\nrecommendations and protocol relating to pregnancy, postpartum, and child care, including\u2014\n**(I)**\nmaternal, infant, and routine childhood vaccines;\n**(II)**\nmaternal warning signs;\n**(III)**\nthe importance of fetal movement counting;\n**(IV)**\nmaternal mental health and postpartum recovery;\n**(V)**\nbreastfeeding practices;\n**(VI)**\nhealth care appointments;\n**(VII)**\nsafe sleep practices;\n**(VIII)**\nskin-to-skin contact;\n**(IX)**\nbaby care, including safe soothing of a crying baby;\n**(X)**\nchild bonding; and\n**(XI)**\nearly childhood development; and\n**(C)**\nscreen fathers for depression and provide referrals for treatment that may positively impact child development and reduce the risk of adverse childhood experiences;\n**(2)**\naddress cultural beliefs about fatherhood, a man\u2019s role in maternal health, and families; and\n**(3)**\nreaffirm a father\u2019s ability to play a positive and valuable role during pregnancy, birth, and early childhood development, regardless of race or ethnicity.\n#### 5. GAO study and report\nNot later than 6 years after the date of enactment of this Act, the Comptroller General of the United States shall conduct, and submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, a report describing the results of, a study on the effectiveness of this Act.",
      "versionDate": "2025-10-24",
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
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2131",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Dads Matter Act of 2025",
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
        "updateDate": "2025-12-03T15:08:16Z"
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
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5828ih.xml"
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
      "title": "Dads Matter Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dads Matter Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Health and Human Services to carry out a public awareness campaign to increase awareness of the importance of father inclusion and engagement in improving overall health outcomes during pregnancy, childbirth, and postpartum, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T05:18:16Z"
    }
  ]
}
```
