# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5151?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5151
- Title: Quiet Communities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5151
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2025-10-01T08:06:16Z
- Update date including text: 2025-10-01T08:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5151",
    "number": "5151",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Quiet Communities Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-01T08:06:16Z",
    "updateDateIncludingText": "2025-10-01T08:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-04T13:01:00Z",
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
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MI"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NY"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "VA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-04",
      "state": "DC"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CO"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "IL"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NY"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NY"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "TN"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "HI"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "NY"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "VA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5151ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5151\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Ms. Meng (for herself, Mr. Lynch , Mr. Min , Mr. Thanedar , Ms. Brownley , Mr. Fitzpatrick , Mr. Nadler , Mr. Beyer , Mr. Sherman , Ms. Norton , Mr. Peters , Mr. Goldman of New York , Mr. Levin , Mr. Neguse , Mr. Casten , Mr. Suozzi , Ms. Chu , and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reestablish the Office of Noise Abatement and Control in the Environmental Protection Agency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quiet Communities Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\napproximately 28,000,000 individuals in the United States are afflicted with some hearing impairment, and it has been estimated that 10,000,000 of those impairments are at least partially attributable to damage from exposure to noise;\n**(2)**\nfor millions of individuals in the United States, noise from aircraft, vehicular traffic, and a variety of other sources is a constant source of torment;\n**(3)**\nmillions of individuals in the United States are exposed to noise levels that can lead to sleep loss, psychological and physiological damage, and work disruption;\n**(4)**\nchronic exposure to noise has been linked to increased risk of cardiovascular disorders, learning deficits in children, stress, and diminished quality of life;\n**(5)**\nexcessive noise leading to sleep deprivation and task interruptions can result in untold costs to society as a result of diminished worker productivity;\n**(6)**\npursuant to the Clean Air Act ( 42 U.S.C. 7401 et seq. ), the Noise Control Act of 1972 ( 42 U.S.C. 4901 et seq. ), and the Quiet Communities Act of 1978 ( 42 U.S.C. 4901 note; Public Law 95\u2013609 ; 92 Stat. 3079), the Environmental Protection Agency established and maintained an Office of Noise Abatement and Control, which has not received funding since 1982;\n**(7)**\nresponsibilities of the Office of Noise Abatement and Control included promulgating noise emission standards, requiring product labeling, facilitating the development of low-noise-emission products, coordinating Federal noise reduction programs, assisting State and local noise abatement efforts, and promoting noise education and research;\n**(8)**\nbecause the Environmental Protection Agency remains legally responsible for enforcing regulations issued under the Noise Control Act of 1972 ( 42 U.S.C. 4901 et seq. ), even though funding for the activities of the Office of Noise Abatement and Control described in paragraph (7) was terminated, and because that Act prohibits State and local governments from regulating noise sources in many situations, noise abatement programs across the United States lie dormant; and\n**(9)**\nas population growth and air and vehicular traffic continue to increase, noise pollution is likely to become an even greater problem in the future, and the health and welfare of individuals in the United States demands that the Environmental Protection Agency, the lead Federal agency for the protection of public health and welfare, once again assume a role in combating noise pollution.\n#### 3. Reestablishment of Office of Noise Abatement and Control\n##### (a) Reestablishment\nThe Administrator of the Environmental Protection Agency (referred to in this section as the Administrator ) shall reestablish within the Environmental Protection Agency an Office of Noise Abatement and Control (referred to in this section as the Office ).\n##### (b) Duties\nThe responsibilities of the Office shall include\u2014\n**(1)**\npromoting the development of effective State and local noise control programs by providing States with technical assistance and grants to develop those programs, including the purchasing of equipment for local communities;\n**(2)**\ncarrying out a national noise control research program to assess the impacts of noise from varied noise sources on mental and physical health;\n**(3)**\ncarrying out a national noise environmental assessment program\u2014\n**(A)**\nto identify trends in noise exposure and response, ambient levels, and compliance data; and\n**(B)**\nto determine the effectiveness of noise abatement actions, including actions for areas around major transportation facilities (such as highways, railroad facilities, and airports);\n**(4)**\ndeveloping and disseminating to the public information and educational materials relating to the mental and physical effects of noise and the most effective means for noise control through the use of materials for school curricula, volunteer organizations, radio and television programs, publications, and other means;\n**(5)**\ndeveloping educational and training materials and programs, including national and regional workshops, to support State and local noise abatement and control programs;\n**(6)**\nestablishing regional technical assistance centers to use the capabilities of institutions of higher education and private organizations to assist State and local noise control programs; and\n**(7)**\nundertaking an assessment of the effectiveness of the Noise Control Act of 1972 ( 42 U.S.C. 4901 et seq. ).\n##### (c) Preferred Approaches\nIn carrying out the duties of the Office under subsection (b), the Office shall emphasize noise abatement approaches that rely on local and State activities, market incentives, and coordination with other public and private agencies.\n##### (d) Study\n**(1) In general**\nThe Administrator shall carry out a study of aircraft noise and the effects of that noise on surrounding communities.\n**(2) Contracts and other agreements**\nThe Administrator shall enter into contracts or other agreements with independent scientists with expertise in noise measurements, noise effects, and noise abatement techniques to conduct the study under paragraph (1).\n**(3) Contents**\nThe study under paragraph (1) shall examine\u2014\n**(A)**\nthe selection of noise measurement methodologies by the Federal Aviation Administration;\n**(B)**\nthe threshold of aircraft noise at which health impacts are felt; and\n**(C)**\nthe effectiveness of aircraft noise abatement programs at airports around the United States.\n**(4) Report**\n**(A) In general**\nNot later than 2 years after the date of enactment of this Act, the Administrator shall submit to Congress a report on the results of the study conducted under paragraph (1).\n**(B) Requirements**\nThe report submitted under subparagraph (A) shall include specific recommendations on new measures that can be implemented to mitigate the impact of aircraft noise on surrounding communities.\n##### (e) Conforming amendment\nThe Noise Pollution and Abatement Act of 1970 ( Public Law 91\u2013604 ; 84 Stat. 1709) is repealed.\n#### 4. Grants under Quiet Communities Program\nSection 14 of the Noise Control Act of 1972 ( 42 U.S.C. 4913 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin the matter preceding paragraph (1) by striking but not limited to ;\n**(B)**\nin paragraph (2) by striking sections 6, 7, and 8 of this Act and inserting section 6 or 8 of this Act, or section 44715 of title 49, United States Code ; and\n**(C)**\nby redesignating paragraphs (1) through (5) as subparagraphs (A) through (E), respectively, and indenting appropriately;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin the matter preceding paragraph (1) by striking but not be limited to and inserting in accordance with the Federal authority pursuant to this Act to regulate sources of noise in interstate commerce ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (C) by striking and, at the end;\n**(ii)**\nby redesignating subparagraphs (A) through (D) as clauses (i) through (iv), respectively, and indenting appropriately; and\n**(iii)**\nby adding at the end the following:\n(v) establishing and implementing training programs on use of noise abatement equipment; and (vi) implementing noise abatement plans; ;\n**(C)**\nby striking the undesignated matter following paragraph (5); and\n**(D)**\nby redesignating paragraphs (1) through (5) as subparagraphs (A) through (E), respectively, and indenting appropriately; and\n**(3)**\nby redesignating subsections (a) through (g) as paragraphs (1) through (7), respectively, and indenting appropriately.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated for the Office of Noise Abatement and Control reestablished under section 3(a) $25,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-09-04",
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
        "name": "Environmental Protection",
        "updateDate": "2025-09-23T17:01:33Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5151ih.xml"
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
      "title": "Quiet Communities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Quiet Communities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reestablish the Office of Noise Abatement and Control in the Environmental Protection Agency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:22Z"
    }
  ]
}
```
