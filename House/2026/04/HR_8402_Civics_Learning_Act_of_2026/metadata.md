# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8402?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8402
- Title: Civics Learning Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8402
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-05-04T15:57:55Z
- Update date including text: 2026-05-04T15:57:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8402",
    "number": "8402",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Civics Learning Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-04T15:57:55Z",
    "updateDateIncludingText": "2026-05-04T15:57:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "AL"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
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
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "FL"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "HI"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "IN"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "MA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "MA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "MN"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NV"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NJ"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NC"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "WI"
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
      "sponsorshipDate": "2026-04-21",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8402ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8402\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Mr. Cleaver (for himself, Ms. Sewell , Mr. DeSaulnier , Mr. Mullin , Ms. S\u00e1nchez , Ms. Wilson of Florida , Ms. Tokuda , Ms. Kelly of Illinois , Mr. Casten , Ms. Schakowsky , Mr. Carson , Mr. Lynch , Mr. Keating , Ms. McCollum , Ms. Titus , Mr. Gottheimer , Ms. Vel\u00e1zquez , Mr. Nadler , Ms. Ross , Mr. Evans of Pennsylvania , Ms. Scanlon , Ms. Moore of Wisconsin , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to increase civics education programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Civics Learning Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe dearth of civics lessons available to students across the United States has helped to foster a political climate that is deeply partisan and divided.\n**(2)**\nPolarization in the United States has fractured public morale in our democratic institutions and has created an environment in which people are less likely to be well-informed on the processes of our constitutional republic, the current state of affairs, and the importance of participating in the political process.\n**(3)**\nIt is impossible to tell the true, full history of this Nation and recognize the power of our representative democracy without discussing the painful and powerful history of the civil rights movement. It is incumbent on Congress to ensure the full history of our great Nation is being taught to the next generation of leaders.\n**(4)**\nAccording to the Annenberg Constitution Day Civics Survey conducted by the Annenberg Public Policy Center of the University of Pennsylvania, in 2022\u2014\n**(A)**\nonly 47 percent of people in the United States surveyed were capable of naming all 3 branches of government, while 25 percent of Americans were not able to name any of the branches of government;\n**(B)**\nless than half of Americans (46 percent) correctly stated that the Supreme Court has the final responsibility for determining the constitutionality of laws if the President and Supreme Court disagree; and\n**(C)**\n26 percent could not name any of the rights guaranteed under the First Amendment.\n**(5)**\nIn 2022, only 22 percent of eighth graders were found to have performed at or above the proficient level on the National Assessment of Educational Progress civics exam conducted by the National Center of Education Studies.\n**(6)**\nA lack of knowledge regarding the structural basics of our constitutional republic and the history of our struggle for suffrage and civil rights creates an increasingly ill-equipped electorate which over time, can, and will continue to, contribute to a weakened democracy.\n#### 3. Amendments to the Elementary and Secondary Education Act of 1965\nSection 2233 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6663 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby inserting and prioritize innovative civics learning and teaching, including by encouraging after to encourage ; and\n**(B)**\nby inserting (including students and teachers at high-need schools (as defined in section 2221)) before the period;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby inserting and appropriated under subsection (h) of this section after 2231(b)(2) ; and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) may include\u2014 (A) hands-on civic engagement activities for teachers and students; (B) activities about the history and principle of the Constitution of the United States, including the Bill of Rights, women\u2019s suffrage, and the civil rights movement; (C) before-school, during-school, after-school, and extracurricular activities; (D) activities that include service learning and community service projects that are linked to school curriculum; (E) activities that encourage and support student participation in school governance; and (F) online and video game based learning. ;\n**(3)**\nin subsection (c), by striking paragraph (3) and inserting the following:\n(3) Diversity of projects (A) Diversity of grants In awarding grants under this section, the Secretary shall ensure that, to the extent practicable, grants are distributed among eligible entities that will serve geographically diverse areas, including urban, suburban, and rural areas, and public elementary schools. (B) Allocation of grant funding To the extent practicable based on the applications received under subsection (d), the Secretary shall ensure that\u2014 (i) not less than 30 percent of the grant funds under this section are awarded to eligible entities that serve elementary school students and teachers; (ii) not less than 30 percent of the grant funds under this section are awarded to eligible entities that serve middle school students and teachers; and (iii) not more than 40 percent of the grant funds under this section are awarded to eligible entities that serve high school students and teachers. ;\n**(4)**\nin subsection (d), by inserting , and containing such information, after manner ; and\n**(5)**\nby adding at the end the following:\n(f) Grant award preference In awarding grants under this section, the Secretary shall give preference to applications for programs that carry out the activities listed in subsection (b)(2) for the purpose of strengthening civics education and learning. (g) Annual report Not later than 90 days after the end of each fiscal year, the Secretary shall submit to the Committee on Education and Workforce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report containing\u2014 (1) a description of each eligible entity awarded a grant under this section during the preceding fiscal year; (2) a description of whether each such eligible entity was able to meet each of the purposes under subsection (a), and if so, how such eligible entity was able to meet such purposes; and (3) any recommendations for continuation of the grant program under this section. (h) Authorization of appropriations In addition to the amounts reserved under section 2231(b)(2), there are authorized to be appropriated $70,000,000 to carry out this section for fiscal year 2027. .",
      "versionDate": "2026-04-21",
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
        "name": "Education",
        "updateDate": "2026-05-04T15:57:55Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8402ih.xml"
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
      "title": "Civics Learning Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-27T11:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Civics Learning Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-27T11:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 to increase civics education programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-27T11:48:25Z"
    }
  ]
}
```
