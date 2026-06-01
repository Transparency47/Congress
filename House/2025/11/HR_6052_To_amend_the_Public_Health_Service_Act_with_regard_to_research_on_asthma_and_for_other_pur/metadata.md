# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6052?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6052
- Title: Elijah E. Cummings Family Asthma Act
- Congress: 119
- Bill type: HR
- Bill number: 6052
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-02-24T09:05:29Z
- Update date including text: 2026-02-24T09:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6052",
    "number": "6052",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Elijah E. Cummings Family Asthma Act",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:29Z",
    "updateDateIncludingText": "2026-02-24T09:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
          "date": "2025-11-17T17:02:20Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "PA"
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
      "sponsorshipDate": "2025-11-17",
      "state": "NY"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6052ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6052\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mrs. Dingell (for herself, Mr. Fitzpatrick , Ms. Clarke of New York , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act with regard to research on asthma, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Elijah E. Cummings Family Asthma Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to the Centers for Disease Control and Prevention, in 2023, more than 27,800,000 people in the United States had asthma, including an estimated 4,800,000 children.\n**(2)**\nAccording to the Centers for Disease Control and Prevention, asthma is more common among Black Americans, Native individuals (American Indians/Alaska Natives), Puerto Ricans, and people of multiple races compared to non-Hispanic, White individuals.\n**(3)**\nAccording to the Centers for Disease Control and Prevention, among children, males have higher rates of asthma than females, and in adults, women have higher rates of asthma than men. Individuals living below the poverty threshold also had significantly higher rates of asthma in 2023 than individuals living above the poverty threshold.\n**(4)**\nAccording to the Centers for Disease Control and Prevention, in 2023 more than 3,600 people in the United States died from asthma. The rate of mortality from asthma is higher among Black Americans and women.\n**(5)**\nThe Agency for Healthcare and Quality reports that asthma accounted for approximately 131,000 hospitalizations and 1,100,000 visits to hospital emergency departments in 2022.\n**(6)**\nAccording to the Centers for Disease Control and Prevention, the annual cost of asthma to the United States is approximately $81,900,000,000, including $3,000,000,000 in indirect costs from missed days of school and work.\n**(7)**\nAccording to the Centers for Disease Control and Prevention, more than 7,900,000 school days and 10,900,000 workdays are missed annually as a result of asthma.\n**(8)**\nAsthma episodes can be triggered by both outdoor air pollution and indoor air pollution, including pollutants such as cigarette smoke and combustion by-products. Asthma episodes can also be triggered by indoor allergens, such as animal dander, mold, cockroaches, and rodents, and outdoor allergens such as pollen.\n**(9)**\nPublic health interventions and medical care in accordance with existing guidelines have been proven effective in the treatment and management of asthma. Better asthma management could reduce the numbers of emergency department visits and hospitalizations due to asthma. Studies published in medical journals, including the Journal of Asthma and The Journal of Pediatrics, have shown that better asthma management results in improved asthma outcomes at a lower cost. However, research published in Preventing Chronic Disease has shown gaps in consistent and comprehensive coverage of guidelines-based asthma care across State Medicaid programs.\n**(10)**\nThe high health and financial burden caused by asthma underscores the importance of adherence to the National Asthma Education and Prevention Program Guidelines of the National Heart, Lung, and Blood Institute. Increasing adherence to guidelines-based care and resulting patient management practices will enhance the quality of life for patients with asthma and decrease asthma-related morbidity and mortality.\n**(11)**\nIn 2016, the Centers for Disease Control and Prevention reported that less than half of people with asthma reported receiving self-management training for their asthma. More education about triggers, proper treatment, and asthma management methods is needed.\n**(12)**\n21 States do not receive funding through the National Asthma Control Program of the Centers for Disease Control and Prevention. Without this funding, State health departments have a limited capacity to improve the reach, quality, effectiveness, and sustainability of asthma control services, conduct comprehensive adult and pediatric surveillance, and reduce asthma morbidity, mortality, and disparities.\n**(13)**\nFor every $1 spent by the National Asthma Control Program of the Centers for Disease Control and Prevention, there is a $71 return on investment from reduced healthcare and economic costs related to asthma.\n**(14)**\nThe alarming rise in the prevalence of asthma, its adverse effect on school attendance and productivity, and its cost for hospitalizations and emergency room visits highlight the importance of public health interventions, including increasing awareness of asthma as a chronic illness, its symptoms, the role of both indoor and outdoor environmental factors that exacerbate the disease, and other factors that affect its exacerbations and severity. The goals of the Federal Government and its partners in the nonprofit and private sectors should include reducing the number and severity of asthma attacks, asthma\u2019s financial burden, and the health disparities associated with asthma.\n#### 3. Asthma-related activities of the Centers for Disease Control and Prevention\nSection 317I of the Public Health Service Act ( 42 U.S.C. 247b\u201310 ) is amended to read as follows:\n317I. Asthma-related activities of the Centers for Disease Control and Prevention (a) Program for providing information and education to the public The Secretary, acting through the Director of the Centers for Disease Control and Prevention and the Director of the National Center for Environmental Health, shall collaborate with State and local health departments to conduct activities regarding asthma, including the provision of information and education to the public regarding asthma, including\u2014 (1) deterring the harmful consequences of uncontrolled asthma; and (2) disseminating health education and information regarding prevention of asthma episodes and strategies for managing asthma. (b) Development of State strategic plans for asthma control Not later than 1 year after the date of enactment of the Elijah E. Cummings Family Asthma Act , the Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall collaborate with State and local health departments to develop State strategic plans for asthma control incorporating public health responses to reduce the burden of asthma, particularly regarding disproportionately affected populations. (c) Compilation of data (1) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, in collaboration with State and local health departments, shall\u2014 (A) conduct asthma surveillance activities to collect data on the prevalence and severity of asthma, the effectiveness of public health asthma interventions, and the quality of asthma management, including\u2014 (i) collection of data on or among people with asthma to monitor the impact on health and quality of life; (ii) surveillance of health care facilities; and (iii) collection of data from electronic health records or other electronic communications; (B) compile and annually publish data regarding\u2014 (i) the prevalence of childhood asthma; (ii) the child mortality rate of asthma; (iii) the number of hospital admissions and emergency department visits by children associated with asthma nationally, disaggregated by State, age, sex, race, and ethnicity; (iv) the prevalence of adult asthma; (v) the adult mortality rate of asthma; and (vi) the number of hospital admissions and emergency department visits by adults associated with asthma nationally, disaggregated by State, age, sex, race, and ethnicity; and (C) modernize asthma surveillance systems to\u2014 (i) enable real-time exchange of data from healthcare, schools, and public health entities; and (ii) support timely publication of national and State trend reports, disaggregated by age, sex, race, ethnicity, payer, and geography. (2) Data privacy None of the data collected, compiled, or published under paragraph (1) may contain individually identifiable information. (3) Ensuring comparability The Secretary, acting through the Director of the Centers for Disease Control and Prevention, in collaboration with State and local health departments, shall ensure that the data described in paragraph (1) are collected and compiled using a consistent methodology so as to maximize the comparability of results. (d) Collaboration with nonprofits The Director of the Centers for Disease Control and Prevention may collaborate with national, State, and local nonprofit organizations to provide information and education about asthma. (e) Reports to Congress (1) In general Not later than 3 years after the date of enactment of the Elijah E. Cummings Family Asthma Act , and 2 years thereafter, the Secretary shall, in collaboration with patient groups, nonprofit organizations, medical societies, and other relevant governmental and nongovernmental entities, submit to Congress a report that\u2014 (A) catalogs, with respect to asthma prevention, management, and surveillance\u2014 (i) the activities of the Federal Government, including an assessment of the progress of the Federal Government and States, with respect to achieving the goals of the Healthy People 2030 initiative; and (ii) the activities of other entities that participate in the program under this section, including nonprofit organizations, patient advocacy groups, and medical societies; and (B) makes recommendations for the future direction of asthma-related activities, in consultation with researchers from the National Institutes of Health, including\u2014 (i) a description of how the Federal Government may improve its response to asthma, including identifying any barriers that may exist; (ii) a description of how the Federal Government may continue, expand, and improve its private-public partnerships with respect to asthma, including identifying any barriers that may exist; (iii) the identification of steps that may be taken to reduce the\u2014 (I) morbidity, mortality, and overall prevalence of asthma; (II) financial burden of asthma on society; (III) burden of asthma on disproportionately affected areas, particularly those in medically underserved populations (as defined in section 330(b)(3)); and (IV) burden of asthma as a chronic disease that can be worsened by environmental exposures; (iv) the identification of programs and policies that have achieved the steps described in clause (iii); (v) the identification of steps that may be taken to expand such programs and policies to benefit larger populations; and (vi) recommendations for future research and interventions. (2) Coordination for recommendations In making recommendations under paragraph (1)(B), the Secretary shall coordinate with\u2014 (A) the Secretary of Health and Human Services, including the Director of the Centers for Disease Control and Prevention and the Administrator of the Centers for Medicare & Medicaid Services; (B) the Administrator of the Environmental Protection Agency; (C) the Secretary of Housing and Urban Development; (D) the Secretary of Education; (E) the Secretary of Veterans Affairs; and (F) the Secretary of Defense. (f) Authorization of appropriations To carry out this section, there is authorized to be appropriated $70,000,000 for the period of fiscal years 2025 through 2029. .",
      "versionDate": "2025-11-17",
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
        "updateDate": "2025-11-24T17:37:24Z"
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
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6052ih.xml"
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
      "title": "Elijah E. Cummings Family Asthma Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T13:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Elijah E. Cummings Family Asthma Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-21T13:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act with regard to research on asthma, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-21T13:33:27Z"
    }
  ]
}
```
