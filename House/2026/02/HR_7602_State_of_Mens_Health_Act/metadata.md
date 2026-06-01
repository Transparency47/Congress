# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7602
- Title: State of Men’s Health Act
- Congress: 119
- Bill type: HR
- Bill number: 7602
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-05-21T08:08:56Z
- Update date including text: 2026-05-21T08:08:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7602",
    "number": "7602",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001125",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Carter, Troy A. [D-LA-2]",
        "lastName": "Carter",
        "party": "D",
        "state": "LA"
      }
    ],
    "title": "State of Men\u2019s Health Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:56Z",
    "updateDateIncludingText": "2026-05-21T08:08:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:34:35Z",
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
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NC"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "MO"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "VA"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NC"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "TN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "DC"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NJ"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "AL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7602ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7602\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Carter of Louisiana (for himself and Mr. Murphy ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to study and report on the state of men\u2019s health in the United States and to establish an Office of Men\u2019s Health within the Department of Health and Human Services.\n#### 1. Short title\nThis Act may be cited as the State of Men\u2019s Health Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nRisks to the health and well-being of the Nation\u2019s men (and their families) are on the rise due to a lack of education on, awareness of, and pursuit of preventive screening and care. These risks include\u2014\n**(A)**\nmen are more at risk for premature death from 9 out of the top 10 causes of death;\n**(B)**\nafter a steady decline from 1979 to 2016, the lifespan gender gap has expanded since 2016 from 4.4 years to a crisis level of 5.9 years with the current average age of death for men being 73.2 years versus 79.1 years for women; and\n**(C)**\nin the United States, men die at an overall rate 1.4 times higher than women on an age-adjusted basis.\n**(2)**\nWhile this health crisis is of particular concern to men, it is also a concern for women who prematurely lose their fathers, husbands, sons, and brothers.\n**(3)**\nMen\u2019s health is a concern to the Federal Government and State governments, which absorb the enormous costs of premature death and disability among men, including the costs of caring for dependents who are left behind.\n**(4)**\nAccording to the Social Security Administration, 16.8 percent of widows 65 years of age or older are impoverished, compared to 4.9 percent of married women 65 years of age or older.\n**(5)**\nEducating men, their families, and health care providers about the importance of early detection of health issues that can impact men, such as cardiovascular disease, mental health, HIV/AIDS, osteoporosis, cancer (lung, prostate, skin, colorectal, testicular, and more), and other pertinent health issues, can result in reducing rates of mortality of diseases impacting males, as well as improve the health of the Nation\u2019s males and the Nation\u2019s overall economic well-being.\n**(6)**\nOf concern are the physical, mental, and emotional well-being of our military men (and women) returning from war zones and our veterans, particularly with respect to mental health and suicide prevention.\n**(7)**\nRecent scientific studies have shown that regular medical exams, preventive screenings, regular exercise, and healthy eating habits can save lives.\n**(8)**\nMen die of suicide at four times the rate of women. According to the Centers for Disease Control and Prevention, men make up 50 percent of the population but nearly 80 percent of suicides.\n**(9)**\nAccording to the National Cancer Institute, cancer mortality is higher among men than women (171.5 per 100,000 men and 126.3 per 100,000 women).\n**(10)**\nProstate cancer is the most frequently diagnosed cancer in the United States among men. One in 9 men will be diagnosed with prostate cancer in their lifetime. In 2026, over 333,830 men will be newly diagnosed with prostate cancer and 36,320 men with prostate cancer will die. The incidence of prostate cancer is 50 percent higher in African-American men, who are twice as likely to die from such cancer. There are over 3,100,000 men in the United States living with prostate cancer.\n**(11)**\nIt is estimated that, in 2026, approximately 110,910 men in the United States will be diagnosed with lung cancer, and an estimated 63,040 men will die from lung cancer.\n**(12)**\nIt is estimated that, in 2026, approximately 55,410 men in the United States will be diagnosed with colon cancer and 28,750 men will be diagnosed with rectal cancer. In the United States, colorectal cancer is the third-leading cause of cancer-related deaths in men.\n**(13)**\nMen make up over half the diabetes patients aged 18 and over in the United States (18.9 million men total), and over one-third of them don\u2019t know it. Approximately 37.3 million people in the United States are living with diabetes, and men are more likely to die from the disease. In the United States, 96 million people aged 18 and older have prediabetes. People with diagnosed diabetes have medical expenditures that are 2.3 times higher than patients without diabetes.\n**(14)**\nA research study found that premature death and morbidity in men costs Federal, State, and local governments in excess of $142 billion annually. It also costs United States employers, and society as a whole, in excess of $156 billion annually and an additional $181 billion annually in decreased quality of life.\n**(15)**\nAbout 9,810 men will be diagnosed in 2026 with testicular cancer, and many of these men will die from this disease or suffer serious adverse outcomes due to lack of early diagnosis and treatment. A common reason for delay in treatment of this disease is a delay in seeking medical attention after discovering a testicular mass.\n**(16)**\nMen over the past decade have shown poorer health outcomes than women across all racial and ethnic groups as well as across socioeconomic status conditions.\n**(17)**\nHealthy fathers can be role models for their children, leading by example, and encouraging them to lead healthy lifestyles. The premature death and disability of fathers is an issue of central importance to children.\n**(18)**\nEstablishing an Office of Men\u2019s Health is needed to investigate these findings and take further action to promote awareness of men\u2019s health needs.\n#### 3. GAO study and report on the state of men\u2019s health\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\ncomplete a study on the state of men\u2019s health in the United States, including the territories of the United States; and\n**(2)**\nsubmit a report to the Congress on the results of such study.\n##### (b) Report contents\nThe report required by subsection (a) shall\u2014\n**(1)**\nidentify health disparities in men\u2019s health;\n**(2)**\ndescribe the programs and activities of the Federal Government that are currently authorized and can be optimized to improve men\u2019s health to eliminate or reduce such health disparities;\n**(3)**\nrecommend any additional programs or activities that should be undertaken by the Federal Government to eliminate or reduce such health disparities;\n**(4)**\nidentify and describe efforts to coordinate and support men\u2019s health throughout the Federal Government and identify ways in which such coordination and support can be improved;\n**(5)**\nidentify the number of offices within the Federal Government focusing on health services and recommend offices that\u2014\n**(A)**\ncould be combined or transitioned into an office on men\u2019s health; or\n**(B)**\ncould assume a leadership role on men\u2019s health;\n**(6)**\nreview and assess programs and activities to improve male engagement in the health care system;\n**(7)**\nassess the Federal research landscape to identify opportunities for additional investments that could catalyze significant progress in addressing men\u2019s health needs; and\n**(8)**\nidentify ways to increase public awareness of the need for greater investment in and attention to men\u2019s health research, as well as men\u2019s health outcomes.\n##### (c) Funding\nNo additional funds are authorized to be appropriated to carry out this section. Any funds used to carry out this section shall be derived from amounts authorized to be appropriated by other provisions of law.\n#### 4. Office of Men\u2019s Health\nPart A of title II of the Public Health Service Act ( 42 U.S.C. 202 et seq. ) is amended by adding at the end the following:\n229A. Health and Human Services Office of Men\u2019s Health (a) Establishment Not later than 18 months after the date of enactment of this section, the Secretary shall establish within the Department of Health and Human Services an Office of Men\u2019s Health. (b) Considerations In establishing such Office, the Secretary shall take into consideration the results of the study under section 3 of the State of Men\u2019s Health Act . (c) Activities The activities of the Office of Men\u2019s Health shall include\u2014 (1) conducting, supporting, coordinating, and promoting programs and activities to improve the state of men\u2019s health in the United States; (2) assisting in the coordination of programs and activities of the Department of Health and Human Services relating to men\u2019s health, including coordination of public awareness, education, and screening programs and activities related to men\u2019s health, with an emphasis on colorectal cancer, prostate cancer, diabetes, high cholesterol, and mental health screening programs for men identified as being at increased risk of developing such diseases and conditions; and (3) establishing and maintaining a database of best practices, clinical guidelines, clinical research, and funding opportunities relating to men\u2019s health. (d) Report Not later than two years after the establishment of the Office of Men\u2019s Health, the Secretary shall submit to Congress a report describing the activities of such Office, including\u2014 (1) findings regarding men\u2019s health; and (2) recommendations to improve men\u2019s health outcomes as a result of the findings. (e) Funding No additional funds are authorized to be appropriated to carry out this section. Any funds used to carry out this section shall be derived from amounts authorized to be appropriated by other provisions of law, excluding any amounts authorized to be appropriated to the Office on Women\u2019s Health under section 229 or any other office of women\u2019s health in the Department of Health and Human Services. .",
      "versionDate": "2026-02-20",
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
        "updateDate": "2026-02-27T17:02:37Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7602ih.xml"
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
      "title": "State of Men\u2019s Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State of Men\u2019s Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to study and report on the state of men's health in the United States and to establish an Office of Men's Health within the Department of Health and Human Services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T05:18:21Z"
    }
  ]
}
```
