# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1553?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1553
- Title: Empowering and Enforcing Environmental Justice Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1553
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2025-12-05T22:08:43Z
- Update date including text: 2025-12-05T22:08:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1553",
    "number": "1553",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001300",
        "district": "44",
        "firstName": "Nanette",
        "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
        "lastName": "Barrag\u00e1n",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Empowering and Enforcing Environmental Justice Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:08:43Z",
    "updateDateIncludingText": "2025-12-05T22:08:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "OR"
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
      "sponsorshipDate": "2025-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "TX"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NV"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CO"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "AZ"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "WA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NM"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "OH"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1553ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1553\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Ms. Barrag\u00e1n (for herself, Mrs. McIver , Ms. Tlaib , Ms. Bonamici , Ms. Norton , Mr. Krishnamoorthi , Ms. Crockett , Mr. Kennedy of New York , Ms. Titus , Ms. Matsui , Ms. DeGette , and Ms. Ansari ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish an Office of Environmental Justice within the Department of Justice, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Empowering and Enforcing Environmental Justice Act of 2025 .\n#### 2. Office of Environmental Justice\n##### (a) In general\nChapter 31 of title 28, United States Code, is amended by adding at the end the following:\n530E. Environmental Justice (a) Definitions In this section: (1) Council The term Council means the Senior Advisory Council established under subsection (c). (2) Department The term Department means the Department of Justice. (3) Environmental justice The term environmental justice means the just treatment and meaningful involvement of all people, regardless of income, race, color, national origin, Tribal affiliation, or disability in agency decision-making and other Federal activities that affect human health and the environment so that individuals\u2014 (A) are fully protected from disproportionate and adverse human health and environmental effects (including risks) and hazards, including those related to climate change, the cumulative impacts of environmental and other burdens, and the legacy of racism or other structural or systemic barriers; and (B) have equitable access to a healthy, sustainable, and resilient environment in which to live, play, work, learn, grow, worship, and engage in cultural and subsistence practices. (4) Environmental justice matter The term environmental justice matter includes any civil or criminal matter in which the conduct or action at issue may involve a disproportionate and adverse environmental or human health effect on\u2014 (A) an identifiable low-income, Tribal, or Indigenous population or community in the United States; or (B) a community in the United States with environmental justice concerns. (5) Indigenous population or community The term Indigenous population or community includes populations or communities of American Indians, Alaska Natives, and Native Hawaiians. (6) Low-income community The term low-income community means any census block group in which 30 percent or more of the population are individuals with an annual household income equal to, or less than, the greater of\u2014 (A) an amount equal to 80 percent of the median income of the area in which the household is located, as reported by the Department of Housing and Urban Development; and (B) 200 percent of the Federal poverty line. (7) Office The term Office means the Office of Environmental Justice established under subsection (b)(1). (8) State The term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands. (b) Office of Environmental Justice (1) Establishment There is established the Office of Environmental Justice within the Environment and Natural Resources Division of the Department. (2) Personnel and funding The Attorney General shall provide to the Office such personnel and funds as are necessary to establish the Office under paragraph (1) and to carry out the duties of the Office under paragraph (4). (3) Leadership The Office shall be headed by a Director, who shall be appointed by the Attorney General. (4) Duties The Director shall: (A) Develop, and update every 5 years thereafter, the environmental justice strategy for the Department relating to Federal actions to address environmental justice. (B) Coordinate environmental justice matters that arise at the Department and United States Attorneys' offices, including building outreach and engagement capacity and competency among the Department\u2019s personnel. (C) Administer the grant program established under section 3 of the Empowering and Enforcing Environmental Justice Act of 2025 . (D) Promote and protect the right of the public to participate meaningfully in the decision-making process on environmental justice matters and design communications efforts with the goal of maximizing community understanding of how to participate in environmental justice matters, including how to file administrative complaints with Federal agencies. (E) Counsel and assist State, local, and Tribal governments on how to coordinate their actions with the Federal Government with respect to environmental justice matters and counsel and assist State, local, and Tribal governments and Indigenous populations or communities in providing equal environmental protection for all individuals. (F) Provide support for State and local environmental enforcement training in communities with environmental justice concerns. (G) Work with the Community Relations Service to facilitate a working relationship between parties involved in environmental justice matters, including regulated industry, State, local, and Tribal decision-makers, nonprofits, low-income communities, and Indigenous populations or communities. (H) Organize, at minimum, bimonthly calls or meetings with environmental justice organizations and communities with environmental justice concerns. (I) Manage the Council. (J) Make recommendations to Federal agencies on community participation in the development of administrative settlement agreements relating to environmental justice matters. (K) Develop\u2014 (i) instructional videos and other materials for Department personnel to provide an overview of the scope of environmental justice matters and procedures for identifying and reporting such matters; (ii) education programs for environmental attorneys about criminal, civil, and civil rights laws; (iii) education programs for civil, criminal, and civil rights attorneys about environmental laws for the purpose of identifying and effectively addressing environmental justice matters; (iv) an email address that Department attorneys and other Department personnel may contact that enables Department attorneys and other Department personnel to seek information and guidance on environmental justice matters; (v) joint education and training activities, where appropriate, with Federal agencies and State, local, and Tribal legal offices; (vi) a continuing legal education course on environmental justice matters, developed in coordination with the Office of Legal Education and the Environmental Protection Agency; and (vii) training programs with respect to environmental justice for individuals participating in the Attorney General's Honors Program. (L) Coordinate with all relevant components within the Department to develop and maintain an appropriate system for tracking and assessing cases that raise environmental justice matters. (c) Senior Advisory Council (1) Establishment There is established a Senior Advisory Council to advise the Assistant Attorney General of the Environment and Natural Resources Division on matters of environmental justice and recommend policy and initiatives with respect to environmental justice matters. (2) Co-chair The Co-chairs of the Council shall be the Assistant Attorney General of the Environment and Natural Resources Division and the Director of the Office. (3) Members The Council shall be composed of: (A) The Assistant Attorney General of the Environment and Natural Resources Division. (B) The Director of the Office. (C) One representative of the Office of the Deputy Attorney General. (D) One representative of the Office of the Associate Attorney General. (E) One representative from the Environmental Enforcement Section of the Environmental and Natural Resources Division. (F) One representative from the Environmental Defense Section of the Environment and Natural Resources Division. (G) One representative of the Civil Rights Division. (H) One representative of the Civil Division. (I) One representative of the Federal Bureau of Investigation. (J) One representative of the Bureau of Prisons. (K) One representative of the Community Relations Service. (L) One representative of the Office for Access to Justice. (M) One representative of the Office of Legal Policy. (N) One representative of the Office of Legislative Affairs. (O) One representative of the Office of Tribal Justice. (P) Two representatives from the Executive Office for United States Attorneys. (Q) The Section Chief of the Environmental Justice Section. (R) Not fewer than 2 representatives from United States Attorneys' offices. (4) Reporting requirement (A) In general Not later than 180 days after the date of enactment of the Empowering and Enforcing Environmental Justice Act of 2025 , and annually thereafter, each member of the Council shall submit to the Director a report on the implementation of the progress of the component of which the member is a representative in implementing the environmental justice strategy of the Department and any proposed revisions to the environmental justice strategy of that component. (B) Other reports and briefings In addition to the reports required under subparagraph (A), the Director may also request a report or briefing from the head of any component not a member of the Council explaining how the component may facilitate the efforts of the Department in meeting the obligations of the Department under the environmental justice strategy. (5) Administration The Director shall coordinate and support the work of the Council. The Director shall convene the Council not later than 90 days after the date of enactment of the Empowering and Enforcing Environmental Justice Act of 2025 and shall convene the Council not less than 4 times annually thereafter. (6) Guidance for Department (A) In general Not later than 180 days after the date of enactment of the Empowering and Enforcing Environmental Justice Act of 2025 , the Council shall develop guidance with respect to environmental justice and provide such guidance to Department personnel, including provisions for identifying, tracking, and addressing environmental justice matters. (B) Review and update Not later than 3 years after the development of the guidance under subparagraph (A), and every 3 years thereafter, the Department shall review and update such guidance. .\n##### (b) Technical amendment\nThe table of sections for chapter 31 of title 28, United States Code, is amended by adding at the end the following:\n530E. Environmental justice. .\n#### 3. Environmental Justice Matters Enforcement Grants\n##### (a) Definitions\nIn this section:\n**(1) Certain congressional committees**\nThe term certain congressional committees means\u2014\n**(A)**\nthe Committees on Environment and Public Works and the Judiciary of the Senate; and\n**(B)**\nthe Committees on Energy and Commerce and the Judiciary of the House of Representatives.\n**(2) Environmental justice**\nThe term environmental justice means the just treatment and meaningful involvement of all people, regardless of income, race, color, national origin, Tribal affiliation, or disability in agency decision-making and other Federal activities that affect human health and the environment so that individuals\u2014\n**(A)**\nare fully protected from disproportionate and adverse human health and environmental effects (including risks) and hazards, including those related to climate change, the cumulative impacts of environmental and other burdens, and the legacy of racism or other structural or systemic barriers; and\n**(B)**\nhave equitable access to a healthy, sustainable, and resilient environment in which to live, play, work, learn, grow, worship, and engage in cultural and subsistence practices.\n**(3) Environmental justice matter**\nThe term environmental justice matter includes any civil or criminal matter where the conduct or action at issue may involve a disproportionate and adverse environmental or human health effect on an identifiable low-income, minority, Tribal, or Indigenous population or community in the United States.\n**(4) Indigenous population or community**\nThe term Indigenous population or community includes populations or communities of American Indians, Alaska Natives, and Native Hawaiians.\n**(5) Low-income community**\nThe term low-income community means any census block group in which 30 percent or more of the population are individuals with an annual household income equal to, or less than, the greater of\u2014\n**(A)**\nan amount equal to 80 percent of the median income of the area in which the household is located, as reported by the Department of Housing and Urban Development; and\n**(B)**\n200 percent of the Federal poverty line.\n**(6) State**\nThe term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n##### (b) In general\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall establish a grant program (in this section referred to as the Program ) within the Office of Environmental Justice to improve the capacity of State, local, and Tribal governments to enforce environmental laws involving environmental justice matters.\n##### (c) Grant authority\nIn carrying out the Program, the Assistant Attorney General may award grants on a competitive basis to eligible recipients, except that no eligible recipient may be awarded more than 1 grant.\n##### (d) Eligible recipients\nThe Assistant Attorney General may award a grant under the Program to a State, local, or Tribal government determined by the Assistant Attorney General to be capable of carrying out a project pursuant to subsection (e).\n##### (e) Grant funds\nGrant funds awarded under the Program, shall only be used to\u2014\n**(1)**\ntrain State, local, and Tribal agencies responsible for prosecuting and enforcing laws involving environmental justice matters;\n**(2)**\nhire staff to assist in the investigation, prosecution, and enforcement of laws involving environmental justice matters; or\n**(3)**\nestablish collaborative programs to provide technical and legal assistance, outreach, and engagement to help communities with environmental justice concerns participate in decisions impacting the environment, health, and safety of those communities with environmental justice concerns.\n##### (f) Applications\nTo be eligible for a grant under the Program, an eligible recipient shall submit to the Assistant Attorney General an application in such form, at such time, and containing such information as the Assistant Attorney General determines to be appropriate.\n##### (g) Limitations on grant amounts\nSubject to the availability of appropriations under subsection (j), each grant made under this section shall be for an amount not less than $50,000 and not greater than $1,000,000.\n##### (h) Federal share\nThe Federal share of a project under the Program shall not exceed 80 percent, unless the Attorney General waives, wholly or in part, this requirement.\n##### (i) Report\nNot later than 18 months after the date of enactment of this Act, and every 2 years thereafter, the Attorney General shall submit a report to certain congressional committees on the grant program established under this section, including a description of the grantees and activities for which grantees used grants awarded under this section.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $50,000,000 for each of the fiscal years 2026 through 2035.",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S1350)"
      },
      "number": "720",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Empowering and Enforcing Environmental Justice Act of 2025",
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
            "name": "Advisory bodies",
            "updateDate": "2025-07-17T20:30:37Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T20:31:11Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2025-07-17T20:30:14Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2025-07-17T20:30:28Z"
          },
          {
            "name": "Environmental regulatory procedures",
            "updateDate": "2025-07-17T20:30:33Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-17T20:30:19Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-17T20:30:42Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-07-17T20:31:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-04-29T14:53:06Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1553ih.xml"
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
      "title": "Empowering and Enforcing Environmental Justice Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Empowering and Enforcing Environmental Justice Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish an Office of Environmental Justice within the Department of Justice, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:36Z"
    }
  ]
}
```
