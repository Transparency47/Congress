# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4332
- Title: YALI Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4332
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-05-28T16:05:37Z
- Update date including text: 2026-05-28T16:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 39 - 6.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 39 - 6.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4332",
    "number": "4332",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "YALI Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-28T16:05:37Z",
    "updateDateIncludingText": "2026-05-28T16:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 39 - 6.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
        "item": [
          {
            "date": "2026-05-13T15:47:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-10T15:03:00Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NV"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
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
      "sponsorshipDate": "2025-07-10",
      "state": "AL"
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
      "sponsorshipDate": "2025-07-10",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
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
      "sponsorshipDate": "2025-07-10",
      "state": "DC"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "GA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "WI"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "OH"
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
      "sponsorshipDate": "2025-07-10",
      "state": "MA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MN"
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
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "RI"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4332ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4332\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Ms. Kamlager-Dove (for herself, Mrs. Kim , Ms. Jacobs , Mr. McCaul , Mrs. Cherfilus-McCormick , Ms. Titus , Mrs. Foushee , Ms. Sewell , Ms. Schakowsky , Mr. Cohen , Ms. Norton , Ms. Williams of Georgia , Ms. Moore of Wisconsin , Mrs. Beatty , Mr. Keating , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo establish a comprehensive United States Government initiative to build the capacity of young leaders and entrepreneurs in Africa, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Young African Leaders Initiative Act of 2025 or the YALI Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Young African Leaders Initiative, launched in 2010, is a signature effort to invest in the next generation of African leaders;\n**(2)**\nAfrica is a continent of strategic importance and it is vital for the United States to support strong and enduring partnerships with the next generation of African leaders;\n**(3)**\nthe United States Government should prioritize investments to build the capacity of emerging young African leaders in sub-Saharan Africa, including through efforts to\u2014\n**(A)**\nenhance leadership skills;\n**(B)**\nencourage entrepreneurship;\n**(C)**\nstrengthen public administration and the role of civil society;\n**(D)**\nenhance peace and security in their respective countries of origin and across Africa; and\n**(E)**\nconnect young African leaders continentally and globally across the private, civic, and public sectors;\n**(4)**\nyouth in Africa have a positive impact on efforts to foster economic growth, improve public sector transparency and governance, and counter extremism, and should be an area of focus for United States outreach on the African continent; and\n**(5)**\nthe Secretary of State should\u2014\n**(A)**\nincrease the number of fellows from Africa participating in the Mandela Washington Fellowship above the estimated 700 fellows who participated during fiscal year 2021; and\n**(B)**\nidentify additional ways to connect YALI alumni to United States public and private resources and institutions.\n#### 3. Young African Leaders Initiative program\n##### (a) In general\nThere is established the Young African Leaders Initiative (referred to in this section as YALI ), which shall be carried out by the Secretary of State.\n##### (b) Purpose\nYALI shall seek to build the capacity of young African leaders in sub-Saharan Africa in the areas of business, civic engagement, or public administration, including through efforts\u2014\n**(1)**\nto support young African leaders by offering professional development, training, and networking opportunities, particularly in the areas of leadership, innovation, civic engagement, elections, human rights, entrepreneurship, good governance, peace and security, and public administration; and\n**(2)**\nto provide increased economic and technical assistance to young African leaders to promote economic growth, strengthen ties between United States and African businesses, build resilience to predatory lending practices, and improve capacity in key economic areas such as tendering, bidding, and contract negotiations, budget management and oversight, anti-corruption, and establishment of clear policy and regulatory practices.\n##### (c) Fellowships\n**(1) In general**\nYALI shall support the participation in the United States in the Mandela Washington Fellowship for Young African Leaders of fellows from Africa who\u2014\n**(A)**\nare between 25 and 35 years of age;\n**(B)**\nhave demonstrated strong capabilities in entrepreneurship, innovation, public service, and leadership; and\n**(C)**\nhave had a positive impact in their communities, organizations, or institutions.\n**(2) Oversight**\nThe fellowships described in paragraph (1) shall be overseen by the Secretary of State through the Bureau of Educational and Cultural Affairs.\n**(3) Eligibility**\nThe Secretary of State shall establish and publish\u2014\n**(A)**\neligibility criteria for participation as a fellow under paragraph (1); and\n**(B)**\ncriteria for determining which eligible applicants will be selected.\n##### (d) Reciprocal exchanges\nSubject to the approval of the Secretary of State, United States citizens may\u2014\n**(1)**\nengage in reciprocal exchanges in connection with alumni of the fellowship described in subsection (c); and\n**(2)**\ncollaborate on projects with such fellowship alumni.\n##### (e) Regional leadership centers and networks\nThe Administrator of the United States Agency for International Development shall establish\u2014\n**(1)**\nnot fewer than 4 regional leadership centers in sub-Saharan Africa to offer in-person and online training throughout the year on business and entrepreneurship, civic leadership, and public management to young African leaders who are between 18 and 35 years of age, have demonstrated strong capabilities in entrepreneurship, innovation, public service and leadership, and peace-building and conflict resolution, and have had a positive impact in their communities, organizations, or institutions; and\n**(2)**\nan online network that provides information and courses on, and connections with leaders in, the private and public sectors of Africa.\n##### (f) Activities\n**(1) United States-based activities**\nThe Secretary of State, in coordination with the heads of relevant Federal departments and agencies, shall oversee all United States-based activities carried out under YALI, including\u2014\n**(A)**\nthe participation of Mandela Washington Fellows in a 6-week Leadership Institute at a United States educational institution in business, civic engagement, or public management, including academic sessions, site visits, professional networking opportunities, leadership training, community service, and organized cultural activities; and\n**(B)**\nthe participation by Mandela Washington fellows in an annual Mandela Washington Fellowship Summit, to provide such Fellows the opportunity to meet with United States leaders from the private, public, and nonprofit sectors.\n**(2) Africa-based activities**\nThe Secretary of State, in coordination with the Administrator for the United States Agency for International Development and the heads of other relevant Federal departments and agencies, should continue to support YALI activities in sub-Saharan Africa, including\u2014\n**(A)**\ncontinued leadership training and other professional development opportunities for Mandela Washington Fellowship for Young African Leaders alumni upon their return to their home countries, including online courses, technical assistance, and access to funding;\n**(B)**\ntraining for young African leaders at regional leadership centers established pursuant to subsection (e), and through online and in-person courses offered by such centers; and\n**(C)**\nopportunities for networking and engagement with\u2014\n**(i)**\nalumni of the Mandela Washington Fellowship for Young African Leaders;\n**(ii)**\nalumni of programs at regional leadership centers established pursuant to subsection (e);\n**(iii)**\nUnited States and like-minded diplomatic missions, business leaders, and others as appropriate; and\n**(iv)**\nwhere practicable and appropriate, other United States-funded regional leadership programs, including the Young Southeast Asian Leaders Initiative (YSEALI), the Young Leaders of the Americas Initiative (YLAI), the Young Pacific Leaders (YPL), and the Young Transatlantic Innovation Leaders Initiative (YTILI), and through Department of State programs such as the Community Engagement Exchange Program and other initiatives.\n**(3) Implementation**\nTo carry out this subsection, the Secretary of State, in coordination with the Administrator of the United States Agency for International Development and the heads of other relevant Federal departments and agencies, shall seek to partner with the private sector to pursue public-private partnerships, leverage private sector expertise, expand networking opportunities, and identify funding opportunities and fellowship and employment opportunities for YALI.\n##### (g) Implementation plan\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Administrator of the United States Agency for International Development and the heads of other relevant Federal departments and agencies, shall submit a plan to the appropriate congressional committees for implementing YALI, including\u2014\n**(1)**\na description of clearly defined program goals, targets, and planned outcomes for each year and for the duration of implementation of the program;\n**(2)**\na strategy to monitor and evaluate the program and progress made toward achieving such goals, targets, and planned outcomes; and\n**(3)**\na strategy to ensure the program is promoting United States foreign policy goals in Africa, including ensuring that the program is clearly branded, paired with robust public diplomacy efforts, and incorporates diversity among participants as practicable, including countries and communities in Africa facing economic distress, civil conflict, marginalization, and other challenges.\n##### (h) Report\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter for the following 4 years, the Secretary of State, in coordination with the Administrator of the United States Agency for International Development, shall submit to the appropriate congressional committees and publish in a publicly accessible, internet-based form, a report that includes\u2014\n**(1)**\na description of the progress made toward achieving the goals, targets, and planned outcomes described in subsection (g)(1), including an overview of the program implemented in the previous year and an estimated number of beneficiaries;\n**(2)**\nan assessment of how YALI is contributing to and promoting United States-Africa relations, particularly in areas of increased private sector investment, trade promotion, support to civil society, improved public administration, promoting peace and security, and fostering entrepreneurship and youth empowerment;\n**(3)**\nrecommendations for improvements or changes to YALI and the implementation plan, if any, that would improve their effectiveness during subsequent years of YALI\u2019s implementation; and\n**(4)**\nfor the first report submitted under this subsection, an assessment of the feasibility of expanding YALI to Morocco, Algeria, Tunisia, Libya, and Egypt.\n##### (i) Defined term\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations of the Senate;\n**(2)**\nthe Committee on Appropriations of the Senate;\n**(3)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(4)**\nthe Committee on Appropriations of the House of Representatives.\n##### (j) Sunset\nThis section shall cease to have effect on the date that is 5 years after the date of the enactment of this Act.",
      "versionDate": "2025-07-10",
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
        "actionDate": "2026-02-10",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 324."
      },
      "number": "2236",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "YALI Act of 2026",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Africa",
            "updateDate": "2026-04-01T20:17:16Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2026-04-01T20:17:16Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-01T20:17:16Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-04-01T20:17:16Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-04-01T20:17:16Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2026-04-01T20:17:16Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-01T20:17:16Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-04-01T20:17:16Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-04-01T20:17:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-29T22:29:02Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4332ih.xml"
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
      "title": "YALI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "YALI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Young African Leaders Initiative Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a comprehensive United States Government initiative to build the capacity of young leaders and entrepreneurs in Africa, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T05:18:29Z"
    }
  ]
}
```
