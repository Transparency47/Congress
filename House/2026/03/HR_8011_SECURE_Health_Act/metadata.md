# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8011?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8011
- Title: SECURE Health Act
- Congress: 119
- Bill type: HR
- Bill number: 8011
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-05-20T08:08:31Z
- Update date including text: 2026-05-20T08:08:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8011",
    "number": "8011",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "SECURE Health Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:31Z",
    "updateDateIncludingText": "2026-05-20T08:08:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Intelligence (Permanent Select) Committee",
          "systemCode": "hlig00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Intelligence (Permanent Select) Committee",
      "systemCode": "hlig00",
      "type": "Select"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-19T13:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-19T13:00:20Z",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8011ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8011\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mrs. Kiggans of Virginia (for herself and Mr. Bera ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committees on Armed Services , and Intelligence (Permanent Select) , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo increase global health security, create more stable societies, and save lives, especially children\u2019s lives, by clarifying and focusing United States support for frontline health workers across global health and humanitarian investments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening and Expanding Capacity for Unified Response and Excellence in Health Act or the SECURE Health Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nStrengthening the global health workforce is critical for improving health outcomes worldwide, preventing the international spread of infectious diseases, enhancing global health security, reinforcing supply chains, and ultimately protecting the health and economic well-being of the American people.\n**(2)**\nAccess to healthcare and a skilled health workforce is essential for maintaining a healthy overall global workforce and ensuring a stable supply of goods vital to the United States economy.\n**(3)**\nRecognizing the growing demand for mental health services, efforts to strengthen the global health workforce can help expand access to qualified providers, evidence-based practices, and innovation to improve the quality of mental health care globally and in the United States.\n**(4)**\nOne in five active physicians and one in six nurses in the United States are foreign-educated, and legal immigrants comprise 18 percent of the entire healthcare workforce, with the number of hospitals hiring foreign-educated nurses nearly doubling between 2010 and 2022.\n**(5)**\nUnited States leadership and investments in global health have driven remarkable progress, including a 60 percent reduction in child mortality and a 38 percent reduction in maternal mortality from 1990 to 2020, a 31 percent decline in new HIV infections from 2010 to 2020, and a 38 percent decrease in malaria-related deaths from 2000 to 2019\u2014contributing to enhanced productivity and economic growth.\n**(6)**\nNations with healthier populations are more likely to be productive, prosperous, and peaceful, whereas countries with poorer health conditions are more prone to instability and conflict, which compromises United States national security.\n**(7)**\nA well-trained, well-equipped, and well-supported frontline health workforce is critical to the effectiveness, sustainability, and resilience of United States global health programs, as well as to strengthening national security and global economic prosperity.\n**(8)**\nDespite the critical role of frontline health workers in improving health, advancing security, and spurring economic growth both in the United States and abroad, nearly half of the world\u2019s population\u2014approximately 4.5 billion people\u2014lacks access to critical health services.\n**(9)**\nRecognizing that frontline health workers are critical to preventing malnutrition, particularly during pregnancy and among children, it is necessary to invest in health workers to enable these workers to deliver nutrition interventions integrated with other health services and, as a result, build community resilience, reduce preventable deaths, and contribute to long-term economic stability.\n**(10)**\nEvery day, more than 15,000 children die worldwide, primarily from preventable causes, and 810 women lose their lives due to pregnancy or childbirth-related complications.\n**(11)**\nMillions of people succumb annually to HIV/AIDS, tuberculosis, malaria, and other treatable and often preventable conditions.\n**(12)**\nIn 2024, an estimated 300 million people across 72 countries required humanitarian assistance and protection due to conflicts, disease outbreaks, and other crises.\n**(13)**\nFrontline health workers frequently perform life-saving services under hazardous conditions, often at great personal risk, with limited access to essential medicines, medical equipment, and safe water and sanitation.\n**(14)**\nSince 2020, more than 14,000 attacks on healthcare facilities, transport, and personnel have been reported, resulting in almost 2,800 health workers killed in conflict zones and significantly hindering access to critical health services for millions.\n**(15)**\nFrontline health workers serve as the first\u2014and often the only\u2014link to healthcare for millions of people in low- and middle-income countries.\n**(16)**\nWhen enabled with modern training, supervision, and digital tools, community health workers can efficiently extend the reach of the healthcare system and help ensure medical innovations.\n**(17)**\nBy 2030, the world is projected to face a shortfall of at least 11 million health workers without immediate and concerted action, particularly in low- and middle-income countries.\n**(18)**\nThe Commission on Health Employment and Economic Growth demonstrated that investments in health yield a ninefold economic return, identifying health employment as a force multiplier for economic growth.\n**(19)**\nFrontline health workers play a vital role in strengthening national resilience, saving lives, fostering economic growth, developing robust primary healthcare systems, and preventing and responding to humanitarian crises and global health security threats from infectious diseases.\n#### 3. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto pursue the expansion, training, payment, support, equipping, and protection of the frontline global health workforce;\n**(2)**\nto support integrated investments in health workers that resemble their true responsibilities and move away from siloed, single-disease investments in health workers;\n**(3)**\nto use global health investments to catalyze the expansion and most efficient utilization of frontline health workers and address severe global health workforce shortages; and\n**(4)**\nto require host organization contributions as part of any investments of the United States in salary support and plans for transitioning those salaries to domestic financing to better ensure the sustainability of remuneration for health workers.\n#### 4. Global health workforce strategy\n##### (a) Establishment; updating\n**(1) In general**\nThe President shall establish and regularly update a 5-year strategy to be known as the Global Health Workforce Strategy .\n**(2) Contents**\nThe strategy shall\u2014\n**(A)**\nidentify spending by the United States Government to support the global health workforce from global health and humanitarian assistance funds; and\n**(B)**\ninclude measurable goals and implementation plans for global health workforce investments by the United States.\n##### (b) Strategies of Federal departments and agencies\nThe head of each Federal department and agency that uses resources for international health and humanitarian assistance shall\u2014\n**(1)**\nestablish policies for the use of such resources that align with the strategy established under subsection (a); and\n**(2)**\nregularly update such policies.\n#### 5. Global Health Workforce Coordinator\n##### (a) Appointment\nThe President shall appoint an individual to serve, within the Department of State, with the concurrent title and responsibility as the Global Health Workforce Coordinator.\n##### (b) Duties\nThe Global Health Workforce Coordinator shall\u2014\n**(1)**\ncoordinate and oversee the implementation of this Act; and\n**(2)**\napprove strategy and resource allocations across foreign assistance programs supporting the global health workforce.\n#### 6. Interagency task force\n##### (a) Establishment\nThe President shall establish, within the National Security Council, an interagency task force to be co-chaired by\u2014\n**(1)**\nthe Global Health Workforce Coordinator appointed under section 5(a); and\n**(2)**\nan appropriate senior director of the National Security Council selected by the President.\n##### (b) Duties\nThe interagency task force shall\u2014\n**(1)**\ncoordinate and oversee the implementation of this Act; and\n**(2)**\nensure the alignment of global health investments across Federal departments and agencies.\n#### 7. Annual reporting requirements\n##### (a) In general\nThe President, acting in coordination with the heads of relevant Federal departments and agencies, shall publish an annual report detailing efforts of Federal departments and agencies to train and support frontline health workers across all funding streams.\n##### (b) Contents\nThe report shall include, at a minimum, the following:\n**(1) Funding for health workers**\nA breakdown of funding across all cadres of health workers that is\u2014\n**(A)**\ncategorized as direct or indirect support; and\n**(B)**\ndifferentiated between\u2014\n**(i)**\nsingle United States Government source funding for a specific disease or condition; and\n**(ii)**\nintegrated funding approaches that use more than one United States Government source of funding to cover multiple diseases or conditions.\n**(2) Support for training**\nA breakdown of funding that supports the training of health workers, including\u2014\n**(A)**\npre-service training to address workforce shortages;\n**(B)**\nin-service training for skill development;\n**(C)**\ninstitutional capacity building and retention measures; and\n**(D)**\ndigital capacity and access for health workers.\n**(3) Support for salaries and sustained employment**\nA breakdown of funding that supports the salaries and employment of health workers, including\u2014\n**(A)**\nfunds allocated to workforce expansion;\n**(B)**\nsalary support with details on plans to transition to domestic funding sources; and\n**(C)**\nprotection measures for health workers, including safe work conditions, labor standards, and protections during conflicts, pandemics, or crises.\n#### 8. Global reporting\n##### (a) In general\nThe United States shall seek to establish and support a biennial, independent global report on the status of the global health workforce, produced outside the donor and United Nations system.\n##### (b) Contents\nThe report shall assess the status of the global health workforce, including international and domestic funding, the policy environment, and other avenues for global health workforce support, for the purpose of tracking and encouraging greater progress, increased international and domestic funding, and the success of global engagement in support of the global health workforce.",
      "versionDate": "2026-03-19",
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
        "updateDate": "2026-04-17T19:34:46Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8011ih.xml"
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
      "title": "SECURE Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SECURE Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening and Expanding Capacity for Unified Response and Excellence in Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase global health security, create more stable societies, and save lives, especially children's lives, by clarifying and focusing United States support for frontline health workers across global health and humanitarian investments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T05:18:50Z"
    }
  ]
}
```
