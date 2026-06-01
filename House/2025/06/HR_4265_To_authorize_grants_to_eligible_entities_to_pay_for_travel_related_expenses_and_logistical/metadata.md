# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4265
- Title: Reproductive Health Travel Fund Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4265
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2026-05-21T08:07:49Z
- Update date including text: 2026-05-21T08:07:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-30: Introduced in House

## Actions

- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4265",
    "number": "4265",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001159",
        "district": "10",
        "firstName": "Marilyn",
        "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
        "lastName": "Strickland",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Reproductive Health Travel Fund Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:49Z",
    "updateDateIncludingText": "2026-05-21T08:07:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
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
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T18:00:35Z",
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
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "TX"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "WA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "WI"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "MO"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "NV"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "TX"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "CA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "CA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "IL"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "VA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "WA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "IL"
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
      "sponsorshipDate": "2025-08-29",
      "state": "DC"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MI"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "TN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
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
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "OR"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4265ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4265\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Ms. Strickland (for herself, Mrs. Fletcher , Mr. Smith of Washington , Mr. Pocan , Mr. Cleaver , Ms. Titus , Ms. Crockett , Mr. Panetta , Ms. Kamlager-Dove , Ms. S\u00e1nchez , Mr. Casten , Ms. McClellan , Ms. DelBene , and Mrs. Ramirez ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize grants to eligible entities to pay for travel-related expenses and logistical support for individuals with respect to accessing abortion services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reproductive Health Travel Fund Act of 2025 .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nOn June 24, 2022, in its decision in Dobbs v. Jackson Women\u2019s Health Organization (142 S. Ct. 2228 (2022)) (referred to in this section as the Dobbs decision ), the Supreme Court overturned Roe v. Wade (410 U.S. 113 (1973)), eliminating the constitutional right to abortion and reversing decades of precedent recognizing the constitutional right to an abortion.\n**(2)**\nWhile abortion has never been accessible to all even under the framework of Roe v. Wade, the Dobbs decision has decimated access for millions of people in the United States.\n**(3)**\nAs expected, the impacts of the Dobbs decision have fallen the hardest on people who already face barriers to health care access due to systemic barriers and discrimination, particularly Black people, Indigenous people, and other people of color, people with disabilities, people in rural areas, young people, people with documentation barriers, LGBTQ+ people, people who are parenting, people with complex medical needs who require hospital-based care, and people having difficulty making ends meet.\n**(4)**\nAbortion bans prevent many people from accessing the care they want and need.\n**(5)**\nPeople have always had abortions and always will, even in the face of legal, financial, and logistical barriers, or criminalization. However, since the Dobbs decision, many are being forced to travel hundreds of miles away from their homes and communities, taking extra time off of work, forgoing days of pay, piecing together extended childcare, and finding ways to cover significant travel expenses. Others are being forced to carry their pregnancies to term.\n**(6)**\nJust months after the Dobbs decision, one-third of women of reproductive age in the United States faced excessive travel times for abortion. For residents of States that had banned abortion, travel times increased by more than 4 hours on average. Black women faced the greatest impact, with 40 percent needing to drive at least 1 hour for abortion care after the decision, versus 15 percent before the decision.\n**(7)**\nAbortion funds and practical support funds (referred to in this section as abortion funds or funds ) are community-based organizations that support people in overcoming financial and logistical barriers to abortion care. In 2024, abortion funds provided over $50,000,000 for abortion funding and over $13,000,000 for logistical support.\n**(8)**\nFunds work together to remove financial and logistical barriers to abortion access and have been doing this work for decades. Funds help cover transportation, food, lodging, childcare, translation support, doula services, and other supports abortion seekers and their families need.\n**(9)**\nMany funds are led by people who have had abortions themselves, including a growing base of Black and Brown leaders who have themselves faced abortion obstacles and understand the complex circumstances individuals may face.\n**(10)**\nAbortion funds have a history of being under-resourced and rely mostly on volunteer time and energy to support communities.\n**(11)**\nAbortion and practical support funds hold some of the closest ties to people who are having abortions and have the first hand experience, up-to-date and on-the-ground knowledge, and the regional and national connections needed to support abortion seekers financially, emotionally, or logistically.\n**(12)**\nMore and more States are seeking to ban abortion or enact extreme restrictions, significantly limiting the circumstances in which abortions are available. Furthermore, people have been prevented from seeking care because of the confusion created by new and changing abortion restrictions, misinformation, disinformation, and muddled judicial decisions, all of which have contributed to a chilling effect for people seeking legal care out of State. People seeking abortions often do not have a full understanding shifting legal landscape, including abortion laws, in their State. People calling abortion funds for support often ask if they are doing something illegal by traveling to get care of the abortion laws in their State and people calling abortion funds for support often ask if they are doing something illegal by traveling to get care. Abortion funds serve to mitigate this confusion and directly connect people to accurate information.\n**(13)**\nFollowing the Dobbs decision, the demand for abortions has surged, with requests increasing by 56 percent from 2023 to 2024. During the same period, the number of abortion seekers supported by abortion funds grew by 33 percent. Despite immense efforts from abortion funds from 2022 to 2024, the number of callers who received support decreased from 70 percent to 54 percent. This is due to escalating costs of abortion care and practical support, as well as inadequate funding to meet the post-Dobbs demand.\n**(14)**\nClinics in States where abortion is legal and more accessible continue to receive an influx of people seeking abortions.\n**(15)**\nWhen people are not able to access an abortion when they need it, they may be forced to seek an abortion later into their pregnancy. This increases costs exponentially. Barriers to abortion care after the Dobbs decision have led to an increasing complexity in the cases that abortion funds are managing. People who are forced to cross State lines for abortion care may need increased financial support for coordinating and paying for higher logistical barriers (such as transportation, lodging, meals, childcare, medication) to access the abortion care they want, need, and deserve. For many, the increased financial burden will push abortion care completely out of reach without financial and logistical assistance for appointment costs and travel.\n#### 3. Grants to pay for travel expenses and logistical support for individuals accessing abortion services\n##### (a) In general\nThe Secretary of the Treasury (referred to in this section as the Secretary ) may award grants to eligible entities to pay for travel-related expenses and logistical support for individuals with respect to accessing abortion services.\n##### (b) Timing\nBeginning not later than 30 days after the date of enactment of this Act, the Secretary shall solicit applications for grants under this section.\n##### (c) Use of funds\n**(1) Permissible uses**\nAn eligible entity receiving a grant under this section shall use the grant for travel-related expenses and logistical support for individuals with respect to accessing abortion services, which may include any of the following expenses and support:\n**(A)**\nRound trip travel to the location where the abortion services are provided.\n**(B)**\nLodging.\n**(C)**\nMeals.\n**(D)**\nChildcare.\n**(E)**\nTranslation services.\n**(F)**\nDoula care.\n**(G)**\nPatient education and information services.\n**(H)**\nLost wages.\n**(2) Organizational costs**\nAn eligible entity receiving a grant under this section may use up to, but not more than, 15 percent of the grant funds to cover organizational costs such as\u2014\n**(A)**\ncommunity outreach efforts;\n**(B)**\nphysical infrastructure construction and maintenance;\n**(C)**\nwebsite development and maintenance; and\n**(D)**\nincreasing staff capacity and training.\n**(3) Impermissible uses**\nAn eligible entity receiving a grant under this section shall not use the grant for costs of an abortion procedure.\n##### (d) Applications\nTo seek a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary determines appropriate.\n##### (e) Priority\nIn selecting the recipients of grants under this section, the Secretary shall give priority to eligible entities that\u2014\n**(1)**\nserve individuals who live in a jurisdiction that has banned or severely restricted access to abortion;\n**(2)**\nserve individuals who travel to a jurisdiction other than the one where they live to be provided abortion services; or\n**(3)**\nhave a program in operation, or submit as part of the application required under subsection (d) a plan to establish and operate a program, to help individuals access abortion services.\n##### (f) Annual reports to Congress\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to Congress a report on the program under this section.\n**(2) Confidentiality**\nThe reports under paragraph (1) shall not include any individually identifiable information.\n##### (g) Preemption\n**(1) In general**\nThe provisions of this section shall supersede any provision of State, Tribal, territorial, or local law that would have the effect of prohibiting any use of funds provided for under this section.\n**(2) Prohibition on Federal cooperation in antiabortion proceedings**\nNo Federal agency or official engaged in carrying out the program under this section may cooperate with any State, Tribal, territorial, or local antiabortion proceeding, including any antiabortion investigation, prosecution, or civil lawsuit, relating to the activities carried out under such program or any individual or entity receiving or providing services under such program.\n##### (h) Definitions\nIn this section:\n**(1)**\nThe term eligible entity \u2014\n**(A)**\nmeans a nonprofit organization, or a community-based organization, that assists individuals seeking an abortion through programs, services, or activities that are unbiased and medically and factually accurate; and\n**(B)**\nexcludes any entity that discourages individuals from seeking an abortion.\n**(2)**\nThe term nonprofit organization means an organization that\u2014\n**(A)**\nis described in subsection (c)(3) of section 501 of the Internal Revenue Code of 1986; and\n**(B)**\nis, under subsection (a) of such section, exempt from taxation.\n##### (i) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $350,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-06-30",
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
        "updateDate": "2025-09-09T14:08:24Z"
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
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4265ih.xml"
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
      "title": "Reproductive Health Travel Fund Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T07:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reproductive Health Travel Fund Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize grants to eligible entities to pay for travel-related expenses and logistical support for individuals with respect to accessing abortion services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T07:48:20Z"
    }
  ]
}
```
