# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6565?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6565
- Title: Reuniting Families Act
- Congress: 119
- Bill type: HR
- Bill number: 6565
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-14T02:45:22Z
- Update date including text: 2026-01-14T02:45:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6565",
    "number": "6565",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001080",
        "district": "28",
        "firstName": "Judy",
        "fullName": "Rep. Chu, Judy [D-CA-28]",
        "lastName": "Chu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Reuniting Families Act",
    "type": "HR",
    "updateDate": "2026-01-14T02:45:22Z",
    "updateDateIncludingText": "2026-01-14T02:45:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:02:50Z",
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
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "AZ"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "VT"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "OR"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "IN"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-10",
      "state": "WA"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "FL"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "AZ"
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
      "sponsorshipDate": "2025-12-10",
      "state": "DC"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "WA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "GA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
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
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MN"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-10",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-10",
      "state": "IL"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "VA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "WA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NM"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
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
      "sponsorshipDate": "2025-12-10",
      "state": "MI"
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
      "sponsorshipDate": "2025-12-10",
      "state": "HI"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6565ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6565\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. Chu (for herself, Ms. Ansari , Ms. Balint , Ms. Barrag\u00e1n , Ms. Bonamici , Mr. Carson , Mr. Castro of Texas , Ms. Crockett , Ms. DelBene , Mr. Espaillat , Mr. Frost , Ms. Garcia of Texas , Mr. Garcia of California , Mr. Gomez , Mrs. Grijalva , Ms. Norton , Ms. Jayapal , Mr. Johnson of Georgia , Mr. Krishnamoorthi , Mr. Lieu , Ms. Matsui , Mr. McGovern , Ms. Meng , Mr. Nadler , Ms. Omar , Mr. Quigley , Mrs. Ramirez , Ms. S\u00e1nchez , Ms. Schakowsky , Mr. Scott of Virginia , Ms. Simon , Mr. Smith of Washington , Ms. Stansbury , Mr. Takano , Mr. Thanedar , Ms. Tokuda , Mr. Vargas , Ms. Vel\u00e1zquez , and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to promote family unity, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Reuniting Families Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTitle I\u2014Reducing family-based visa backlogs and promoting family reunification\nSec. 101. Recapture of immigrant visas lost to bureaucratic delay.\nSec. 102. Reclassification of spouses, permanent partners, and minor children of legal permanent residents as immediate relatives.\nSec. 103. Country limits.\nSec. 104. Promoting family unity.\nSec. 105. Relief for orphans, widows, and widowers.\nSec. 106. Exemption from immigrant visa limit for certain veterans who are natives of the Philippines.\nSec. 107. Fianc\u00e9e child status protection.\nSec. 108. Equal treatment for all stepchildren.\nSec. 109. Retention of priority dates.\nSec. 110. Relief for spouses and children on other visas.\nSec. 111. Extension of the application period for certain aliens present in the United States for adjustment of status.\nSec. 112. Expansion of cancellation of removal.\nSec. 113. Prohibition on removal of aliens with pending applications.\nTitle II\u2014Uniting American Families Act\nSec. 201. Definitions of permanent partner and permanent partnership.\nSec. 202. Definition of child.\nSec. 203. Numerical limitations on individual foreign states.\nSec. 204. Allocation of immigrant visas.\nSec. 205. Procedure for granting immigrant status.\nSec. 206. Annual admission of refugees and admission of emergency situation refugees.\nSec. 207. Asylum.\nSec. 208. Adjustment of status of refugees.\nSec. 209. Inadmissible aliens.\nSec. 210. Nonimmigrant status for permanent partners awaiting the availability of an immigrant visa.\nSec. 211. Derivative status for permanent partners of nonimmigrant visa holders.\nSec. 212. Conditional permanent resident status for certain alien spouses, permanent partners, and sons and daughters.\nSec. 213. Conditional permanent resident status for certain alien entrepreneurs, spouses, permanent partners, and children.\nSec. 214. Deportable aliens.\nSec. 215. Removal proceedings.\nSec. 216. Cancellation of removal; adjustment of status.\nSec. 217. Adjustment of status of nonimmigrant to that of person admitted for permanent residence.\nSec. 218. Application of criminal penalties for misrepresentation and concealment of facts regarding permanent partnerships.\nSec. 219. Requirements as to residence, good moral character, attachment to the principles of the Constitution.\nSec. 220. Naturalization for permanent partners of citizens.\nSec. 221. Application of family unity provisions to permanent partners of certain LIFE Act beneficiaries.\nSec. 222. Application to Cuban Adjustment Act.\nSec. 223. Nationality at birth.\nTitle III\u2014Promoting Diversity and Protecting Against Discrimination in our Immigration System\nSec. 301. Increasing diversity visas.\nSec. 302. Addressing the impact of the Muslim and African bans.\nTitle IV\u2014Addressing the Needs of Refugee Families\nSec. 401. Prioritization of family reunification in refugee resettlement process.\nSec. 402. Priority 3 family reunification cases.\nSec. 403. Admission of refugee families and timely adjudication.\nI\nReducing family-based visa backlogs and promoting family reunification\n#### 101. Recapture of immigrant visas lost to bureaucratic delay\n##### (a) Worldwide level of family-Sponsored immigrants\nSection 201(c) of the Immigration and Nationality Act ( 8 U.S.C. 1151(c) ) is amended to read as follows:\n(c) Worldwide level of family-Sponsored immigrants (1) In general The worldwide level of family-sponsored immigrants under this subsection for a fiscal year is equal to the sum of\u2014 (A) 480,000; (B) the number computed under paragraph (2); and (C) the number computed under paragraph (3). (2) Unused visa numbers from previous fiscal year The number computed under this paragraph for a fiscal year is the difference, if any, between\u2014 (A) the worldwide level of family-sponsored immigrant visas established for the previous fiscal year; and (B) the number of visas issued under section 203(a), subject to this subsection, during the previous fiscal year. (3) Unused visa numbers from fiscal years 1992 through 2025 The number computed under this paragraph is the difference, if any, between\u2014 (A) the difference, if any, between\u2014 (i) the sum of the worldwide levels of family-sponsored immigrant visas established for fiscal years 1992 through 2025; and (ii) the number of visas issued under section 203(a), subject to this subsection, during such fiscal years; and (B) the number of unused visas from fiscal years 1992 through 2025 that were issued after fiscal year 2025 under section 203(a), subject to this subsection. .\n##### (b) Worldwide level of employment-Based immigrants\nSection 201(d) of the Immigration and Nationality Act ( 8 U.S.C. 1151(d) ) is amended to read as follows:\n(d) Worldwide level of employment-Based immigrants (1) In general The worldwide level of employment-based immigrants under this subsection for a fiscal year is equal to the sum of\u2014 (A) 140,000; (B) the number computed under paragraph (2); and (C) the number computed under paragraph (3). (2) Unused visa numbers from previous fiscal year The number computed under this paragraph for a fiscal year is the difference, if any, between\u2014 (A) the worldwide level of employment-based immigrant visas established for the previous fiscal year; and (B) the number of visas issued under section 203(b), subject to this subsection, during the previous fiscal year. (3) Unused visa numbers from fiscal years 1992 through 2025 The number computed under this paragraph is the difference, if any, between\u2014 (A) the difference, if any, between\u2014 (i) the sum of the worldwide levels of employment-based immigrant visas established for each of fiscal years 1992 through 2025; and (ii) the number of visas issued under section 203(b), subject to this subsection, during such fiscal years; and (B) the number of unused visas from fiscal years 1992 through 2025 that were issued after fiscal year 2025 under section 203(b), subject to this subsection. .\n##### (c) Aliens not subject to direct numerical limitations\nSection 201(b) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b) ) is amended by adding at the end the following:\n(3) (A) Aliens who are beneficiaries (including derivative beneficiaries) of approved immigrant petitions bearing priority dates more than ten years prior to the alien's application for admission as an immigrant or adjustment of status. (B) Aliens described in section 203(d). .\n##### (d) Effective date\nThe amendments made by this section shall take effect on the date which is 60 days after the date of the enactment of this Act.\n#### 102. Reclassification of spouses, permanent partners, and minor children of legal permanent residents as immediate relatives\n##### (a) In general\nSection 201(b)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(2) ) is amended to read as follows:\n(2) Immediate relative (A) In general (i) Immediate relative defined In this subparagraph, the term immediate relative means a child, spouse, permanent partner, or parent of a citizen of the United States or a child, spouse, or permanent partner of a lawful permanent resident (and for each family member of a citizen or lawful permanent resident under this subparagraph, such individual\u2019s spouse, permanent partner, or child who is accompanying or following to join the individual), except that, in the case of parents, such citizens shall be at least 21 years of age. (ii) Previously issued visa Aliens admitted under section 211(a) on the basis of a prior issuance of a visa under section 203(a) to their accompanying parent who is an immediate relative. (iii) Parents and children An alien who was the child or parent of a citizen of the United States or a child of a lawful permanent resident at the time of the citizen\u2019s or resident\u2019s death if the alien files a petition under section 204(a)(1)(A)(ii) within 2 years after such date or prior to reaching 21 years of age. (iv) Spouse or permanent partner An alien who was the spouse or permanent partner of a citizen of the United States or lawful permanent resident for not less than 2 years at the time of the citizen\u2019s or resident\u2019s death or, if married for less than 2 years at the time of the citizen\u2019s or resident\u2019s death, proves by a preponderance of the evidence that the marriage or permanent partnership was entered into in good faith and not solely for the purpose of obtaining an immigration benefit and was not legally separated from the citizen or resident (or, in the case of a permanent partnership, whose permanent partnership was not terminated) at the time of the citizen\u2019s or resident\u2019s death, and each child of such alien, shall be considered, for purposes of this subsection, an immediate relative after the date of the citizen\u2019s or resident\u2019s death if the spouse or permanent partner files a petition under section 204(a)(1)(A)(ii) before the date on which the spouse or permanent partner remarries or enters a permanent partnership with another person. (v) Special rule For purposes of this subparagraph, an alien who has filed a petition under clause (iii) or (iv) of section 204(a)(1)(A) remains an immediate relative if the United States citizen or lawful permanent resident spouse, permanent partner, or parent loses United States citizenship or residence on account of the abuse. (B) Birth during temporary visit abroad Aliens born to an alien lawfully admitted for permanent residence during a temporary visit abroad. .\n##### (b) Allocation of immigrant visas\nSection 203(a) of the Immigration and Nationality Act ( 8 U.S.C. 1153(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking 23,400 and inserting 127,200 ;\n**(2)**\nby striking paragraph (2) and inserting the following:\n(2) Unmarried sons without permanent partners and unmarried daughters without permanent partners of permanent resident aliens Qualified immigrants who are the unmarried sons without permanent partners or unmarried daughters without permanent partners (but are not the children) of an alien lawfully admitted for permanent residence shall be allocated visas in a number not to exceed 80,640, plus any visas not required for the class specified in paragraph (1). ;\n**(3)**\nin paragraph (3), by striking 23,400 and inserting 80,640 ; and\n**(4)**\nin paragraph (4), by striking 65,000 and inserting 191,520 .\n##### (c) Technical and conforming amendments\n**(1) Rules for determining whether certain aliens are immediate relatives**\nSection 201(f) of the Immigration and Nationality Act ( 8 U.S.C. 1151(f) ) is amended\u2014\n**(A)**\nin paragraph (1), by striking paragraphs (2) and (3), and inserting paragraph (2), ;\n**(B)**\nby striking paragraph (2);\n**(C)**\nby redesignating paragraphs (3) and (4) as paragraphs (2) and (3), respectively; and\n**(D)**\nin paragraph (3), as redesignated by subparagraph (C), by striking through (3) and inserting and (2) .\n**(2) Allocation of immigration visas**\nSection 203(h) of the Immigration and Nationality Act ( 8 U.S.C. 1153(h) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking subsections (a)(2)(A) and (d) and inserting subsection (d) ;\n**(ii)**\nin subparagraph (A), by striking becomes available for such alien (or, in the case of subsection (d), the date on which an immigrant visa number became available for the alien\u2019s parent), and inserting became available for the alien\u2019s parent, ; and\n**(iii)**\nin subparagraph (B), by striking applicable ;\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) Petitions described The petition described in this paragraph is a petition filed under section 204 for classification of the alien\u2019s parent under subsection (a), (b), or (c). ; and\n**(C)**\nin paragraph (3), by striking subsections (a)(2)(A) and (d) and inserting subsection (d) .\n**(3) Procedure for granting immigrant status**\nSection 204 of the Immigration and Nationality Act ( 8 U.S.C. 1154 ) is amended\u2014\n**(A)**\nin subsection (a)(1)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i), by inserting or lawful permanent resident after citizen ;\n**(II)**\nin clause (ii), by striking described in the second sentence of section 201(b)(2)(A)(i) also and inserting , alien child, or alien parent described in section 201(b)(2)(A) ;\n**(III)**\nin clause (iii)\u2014\n**(aa)**\nin subclause (I)(aa), by inserting or legal permanent resident after citizen ; and\n**(bb)**\nin subclause (II)(aa)\u2014\n(AA)\nin subitems (AA) and (BB), by inserting or legal permanent resident; after citizen each place that term appears;\n(BB)\nin subitem (CC), by inserting or legal permanent resident after citizen each place that term appears; and\n(CC)\nin subitem (CC)(bbb), by inserting or legal permanent resident after citizenship ;\n**(IV)**\nin clause (iv), by inserting or legal permanent resident after citizen each place that term appears;\n**(V)**\nin clause (v)(I), by inserting or legal permanent resident after citizen ; and\n**(VI)**\nin clause (vi)\u2014\n**(aa)**\nby inserting or legal permanent resident status after renunciation of citizenship ; and\n**(bb)**\nby inserting or legal permanent resident after abuser\u2019s citizenship ;\n**(ii)**\nby striking subparagraph (B);\n**(iii)**\nin subparagraph (C), by striking subparagraph (A)(iii), (A)(iv), (B)(ii), or (B)(iii) and inserting clause (iii) or (iv) of subparagraph (A) ; and\n**(iv)**\nin subparagraph (J), by striking or clause (ii) or (iii) of subparagraph (B) ;\n**(B)**\nin subsection (a), by striking paragraph (2);\n**(C)**\nin subsection (c)(1), by striking or preference status ; and\n**(D)**\nin subsection (h), by striking or a petition filed under subsection (a)(1)(B)(ii) .\n#### 103. Country limits\nSection 202(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1152(a)(2) ) is amended by striking 7 percent (in the case of a single foreign state) or 2 percent and inserting 20 percent (in the case of a single foreign state) or 5 percent .\n#### 104. Promoting family unity\n##### (a) Repeal of three- and ten-Year and permanent bars\nSection 212(a)(9) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(9) ) is amended to read as follows:\n(9) Aliens previously removed (A) Arriving alien Any alien who has been ordered removed under section 235(b)(1) or at the end of proceedings under section 240 initiated upon the alien's arrival in the United States and who again seeks admission within 5 years of the date of such removal (or within 20 years in the case of a second or subsequent removal or at any time in the case of an alien convicted of an aggravated felony) is inadmissible. (B) Other aliens Any alien not described in subparagraph (A), and who seeks admission within 10 years of the date of such alien's departure or removal (or within 20 years of such date in the case of a second or subsequent removal or at any time in the case of an alien convicted of an aggravated felony), is inadmissible if the alien\u2014 (i) has been ordered removed under section 240 or any other provision of law; or (ii) departed the United States while an order of removal was outstanding. (C) Exception Subparagraphs (A) and (B) shall not apply to an alien seeking admission within a period if, prior to the date of the alien's reembarkation at a place outside the United States or attempt to be admitted from foreign contiguous territory, the Secretary of Homeland Security has consented to the alien's reapplying for admission. .\n##### (b) Misrepresentations\nThe Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended\u2014\n**(1)**\nby amending section 212(a)(6)(C)(ii) ( 8 U.S.C. 1182(a)(6)(C)(ii) ) to read as follows:\n(ii) Misrepresentation of citizenship (I) In general Any alien who willfully misrepresents, or has willfully misrepresented, himself or herself to be a citizen of the United States for any purpose or benefit under this Act (including section 274A) or any Federal or State law is inadmissible. (II) Exception In the case of an alien making a misrepresentation described in subclause (I), if the alien was under the age of 21 at the time of making such misrepresentation that he or she was a citizen, the alien shall not be considered to be inadmissible under any provision of this subsection based on such misrepresentation. ;\n**(2)**\nin section 212(a)(6)(C)(iii) ( 8 U.S.C. 1182(a)(6)(C)(iii) ), by striking of clause (i) ;\n**(3)**\nby amending subsection (i)(1) of section 212 ( 8 U.S.C. 1182(i)(1) ) to read as follows:\n(i) (1) The Attorney General or the Secretary of Homeland Security may, in the discretion of the Attorney General or the Secretary, waive the application of subsection (a)(6)(C) in the case of an immigrant who is the parent, spouse, permanent partner, son, or daughter of a United States citizen or of an alien lawfully admitted for permanent residence, or an alien granted classification under clause (iii) or (iv) of section 204(a)(1)(A), if it is established to the satisfaction of the Attorney General or the Secretary that the admission to the United States of such alien would not be contrary to the national welfare, safety, or security of the United States. ; and\n**(4)**\nby amending section 237(a)(3)(D) ( 8 U.S.C. 1227(a)(3)(D) ) to read as follows:\n(D) Misrepresentation of citizenship (i) In general Any alien who willfully misrepresents, or has willfully misrepresented, himself or herself to be a citizen of the United States for any purpose or benefit under this Act (including section 274A) or any Federal or State law is deportable. (ii) Exception In the case of an alien making a misrepresentation described in subclause (i), if the alien was under the age of 21 at the time of making such misrepresentation that he or she was a citizen, the alien shall not be considered to be deportable under any provision of this subsection based on such misrepresentation. .\n##### (c) Waivers of inadmissibility\nSection 212 of the Immigration and Nationality Act ( 8 U.S.C. 1182 ) is amended by inserting after subsection (b) the following:\n(c) Notwithstanding any other provision of law, the Secretary of Homeland Security or the Attorney General may waive the operation of any one or more grounds of inadmissibility set forth in this section for humanitarian purposes, to assure family unity, or when it is otherwise in the public interest. This waiver shall be available to individuals eligible for relief under subsection (h). .\n##### (d) Waivers of deportability\nSection 237 of the Immigration and Nationality Act ( 8 U.S.C. 1227 ) is amended by adding at the end the following:\n(e) Notwithstanding any other provision of law, the Secretary of Homeland Security or the Attorney General may waive the operation of any one or more grounds of removal set forth in this section for humanitarian purposes, to assure family unity, or when it is otherwise in the public interest. .\n#### 105. Relief for orphans, widows, and widowers\n##### (a) In general\n**(1) Special rule for orphans, spouses, and permanent partners**\nIn applying clauses (iii) and (iv) of section 201(b)(2)(A) of the Immigration and Nationality Act , as added by section 102(a) of this Act, to an alien whose citizen or lawful permanent resident relative died before the date of the enactment of this Act, the alien relative may file the classification petition under section 204(a)(1)(A)(ii) of such Act, as amended by section 102(c)(4)(A)(i)(II) of this Act, not later than 2 years after the date of the enactment of this Act.\n**(2) Eligibility for parole**\nIf an alien was excluded, deported, removed, or departed voluntarily before the date of the enactment of this Act based solely upon the alien\u2019s lack of classification as an immediate relative (as defined in section 201(b)(2)(A)(iv) of the Immigration and Nationality Act , as amended by section 102(a) of this Act) due to the death of such citizen or resident\u2014\n**(A)**\nsuch alien shall be eligible for parole into the United States pursuant to the Secretary of Homeland Security\u2019s discretionary authority under section 212(d)(5) of such Act ( 8 U.S.C. 1182(d)(5) ); and\n**(B)**\nsuch alien\u2019s application for adjustment of status shall be considered notwithstanding section 212(a)(9) of such Act ( 8 U.S.C. 1182(a)(9) ).\n**(3) Eligibility for parole**\nIf an alien described in section 204(l) of the Immigration and Nationality Act ( 8 U.S.C. 1154(l) ), was excluded, deported, removed, or departed voluntarily before the date of the enactment of this Act\u2014\n**(A)**\nsuch alien shall be eligible for parole into the United States pursuant to the Secretary of Homeland Security\u2019s discretionary authority under section 212(d)(5) of such Act ( 8 U.S.C. 1182(d)(5) ); and\n**(B)**\nsuch alien\u2019s application for adjustment of status shall be considered notwithstanding section 212(a)(9) of such Act ( 8 U.S.C. 1182(a)(9) ).\n##### (b) Processing of immigrant visas and derivative petitions\n**(1) In general**\nSection 204(b) of the Immigration and Nationality Act ( 8 U.S.C. 1154(b) ) is amended\u2014\n**(A)**\nby striking After an investigation and inserting the following:\n(1) In general After an investigation ; and\n**(B)**\nby adding at the end the following:\n(2) Death of qualifying relative (A) In general Any alien described in subparagraph (B) whose qualifying relative died before the completion of immigrant visa processing may have an immigrant visa application adjudicated as if such death had not occurred. An immigrant visa issued before the death of the qualifying relative shall remain valid after such death. (B) Alien described An alien described in this subparagraph is an alien who\u2014 (i) is an immediate relative (as described in section 201(b)(2)(A)); (ii) is a family-sponsored immigrant (as described in subsection (a) or (d) of section 203); (iii) is a derivative beneficiary of an employment-based immigrant under section 203(b) (as described in section 203(d)); or (iv) is the spouse, permanent partner, or child of a refugee (as described in section 207(c)(2)) or an asylee (as described in section 208(b)(3)). .\n**(2) Transition period**\n**(A) In general**\nNotwithstanding a denial or revocation of an application for an immigrant visa for an alien whose qualifying relative died before the date of the enactment of this Act, such application may be renewed by the alien through a motion to reopen, without fee.\n**(B) Inapplicability of bars to entry**\nNotwithstanding section 212(a)(9) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(9) ), an alien\u2019s application for an immigrant visa shall be considered if the alien was excluded, deported, removed, or departed voluntarily before the date of the enactment of this Act.\n##### (c) Naturalization\nSection 319(a) of the Immigration and Nationality Act ( 8 U.S.C. 1430(a) ) is amended\u2014\n**(1)**\nby inserting or permanent partner after spouse each place such term appears;\n**(2)**\nby inserting (or, if the spouse is deceased, the spouse was a citizen of the United States) after citizen of the United States ; and\n**(3)**\nby inserting or permanent partnership after marital union .\n##### (d) Waivers of inadmissibility\nSection 212 of the Immigration and Nationality Act ( 8 U.S.C. 1182 ) is amended\u2014\n**(1)**\nby redesignating the second subsection (t) as subsection (u); and\n**(2)**\nby adding at the end the following:\n(v) Continued waiver eligibility for widows, widowers, and orphans In the case of an alien who would have been statutorily eligible for any waiver of inadmissibility under this Act but for the death of a qualifying relative, the eligibility of such alien shall be preserved as if the death had not occurred and the death of the qualifying relative shall be the functional equivalent of hardship for purposes of any waiver of inadmissibility which requires a showing of hardship. .\n##### (e) Surviving relative consideration for certain petitions and applications\nSection 204(l)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1154(l)(1) ) is amended\u2014\n**(1)**\nby striking who resided in the United States at the time of the death of the qualifying relative and who continues to reside in the United States ; and\n**(2)**\nby striking any related applications, and inserting any related applications (including affidavits of support), .\n##### (f) Immediate relatives\nSection 201(b)(2)(A)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(2)(A)(i) ) is amended by striking within 2 years after such date .\n##### (g) Family-Sponsored immigrants\nSection 212(a)(4)(C)(i) is amended\u2014\n**(1)**\nin subclause (I), by striking , or and inserting a semicolon;\n**(2)**\nin subclause (II), by striking or at the end; and\n**(3)**\nby adding at the end the following:\n(IV) the status as a surviving relative under section 204(l); or .\n#### 106. Exemption from immigrant visa limit for certain veterans who are natives of the Philippines\n##### (a) Short title\nThis section may be cited as the Filipino Veterans Family Reunification Act .\n##### (b) Aliens not subject to direct numerical limitations\nSection 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) ) is amended by adding at the end the following:\n(F) Aliens who are eligible for an immigrant visa under paragraph (1) or (3) of section 203(a) and who have a parent who was naturalized pursuant to section 405 of the Immigration Act of 1990 ( 8 U.S.C. 1440 note). .\n#### 107. Fianc\u00e9e child status protection\n##### (a) Definition\nSection 101(a)(15)(K)(iii) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(K)(iii) ) is amended by inserting , if a determination of the age of such minor child is made using the age of the alien on the date on which the petition is filed with the Secretary of Homeland Security to classify the alien\u2019s parent as the fianc\u00e9e or fianc\u00e9 of a United States citizen (in the case of an alien parent described in clause (i)) or as the spouse or permanent partner of a United States citizen under section 201(b)(2)(A)(i) (in the case of an alien parent described in clause (ii)) before the semicolon at the end.\n##### (b) Adjustment of status authorized\nSection 214(d) of the Immigration and Nationality Act ( 8 U.S.C. 1184(d)(1) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively; and\n**(2)**\nin paragraph (1), by striking In the event and inserting the following:\n(2) (A) If an alien does not marry the petitioner under paragraph (1) within 3 months after the alien and the alien\u2019s minor children are admitted into the United States, such alien and children shall be required to depart from the United States. If such aliens fail to depart from the United States, they shall be removed in accordance with sections 240 and 241. (B) Subject to subparagraphs (C) and (D), if an alien marries the petitioner described in section 101(a)(15)(K)(i) within 3 months after the alien is admitted into the United States, the Secretary of Homeland Security or the Attorney General, subject to the provisions of section 245(d), may adjust the status of the alien, and any minor children accompanying or following to join the alien, to that of an alien lawfully admitted for permanent residence on a conditional basis under section 216 if the alien and any such minor children apply for such adjustment and are not determined to be inadmissible to the United States. (C) Paragraphs (5) and (7)(A) of section 212(a) shall not apply to an alien who is eligible to apply for adjustment of his or her status to an alien lawfully admitted for permanent residence under this section. (D) An alien eligible for a waiver of inadmissibility as otherwise authorized under this Act shall be permitted to apply for adjustment of his or her status to that of an alien lawfully admitted for permanent residence under this section. .\n##### (c) Age determination\nSection 245(d) of the Immigration and Nationality Act ( 8 U.S.C. 1155(d) ) is amended\u2014\n**(1)**\nby inserting (1) before The Attorney General ; and\n**(2)**\nby adding at the end the following:\n(2) A determination of the age of an alien admitted to the United States under section 101(a)(15)(K)(iii) shall be made, for purposes of adjustment to the status of an alien lawfully admitted for permanent residence on a conditional basis under section 216, using the age of the alien on the date on which the petition is filed with the Secretary of Homeland Security to classify the alien\u2019s parent as the fianc\u00e9e or fianc\u00e9 of a United States citizen (in the case of an alien parent admitted to the United States under section 101(a)(15)(K)(i)) or as the spouse or permanent partner of a United States citizen under section 201(b)(2)(A)(i) (in the case of an alien parent admitted to the United States under section 101(a)(15)(K)(ii)). .\n##### (d) Effective date\n**(1) In general**\nThe amendments made by this section shall be effective as if included in the Immigration Marriage Fraud Amendments of 1986 ( Public Law 99\u2013639 ).\n**(2) Applicability**\nThe amendments made by this section shall apply to all petitions or applications described in such amendments that\u2014\n**(A)**\nare pending as of the date of the enactment of this Act; or\n**(B)**\nhave been denied, but would have been approved if such amendments had been in effect at the time of adjudication of the petition or application.\n**(3) Motion to reopen or reconsider**\nA motion to reopen or reconsider a petition or application described in paragraph (2)(B) shall be granted if such motion is filed with the Secretary of Homeland Security or the Attorney General not later than 2 years after the date of the enactment of this Act.\n#### 108. Equal treatment for all stepchildren\nSection 101(b)(1)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1101(b)(1)(B) ) is amended by striking , provided the child had not reached the age of eighteen years at the time the marriage creating the status of stepchild occurred .\n#### 109. Retention of priority dates\nSection 203 of the Immigration and Nationality Act ( 8 U.S.C. 1153 ) is amended\u2014\n**(1)**\nby amending subsection (h)(3) to read as follows:\n(3) Retention of priority date If the age of an alien is determined under paragraph (1) to be 21 years of age or older for the purposes of subsections (a)(2)(A) and (d), and a parent of the alien files a family-based petition for such alien, the priority date for such petition shall be the original priority date issued upon receipt of the original family- or employment-based petition for which either parent was a beneficiary. ; and\n**(2)**\nby adding at the end the following:\n(i) Permanent priority dates The priority date for any family- or employment-based petition shall be the date of filing of the petition with the Secretary of Homeland Security (or the Secretary of State, if applicable), unless the filing of the petition was preceded by the filing of a labor certification with the Secretary of Labor, in which case that date shall constitute the priority date. The beneficiary of any petition shall retain his or her earliest priority date based on any petition filed on his or her behalf that was approvable when filed, regardless of the category of subsequent petitions. .\n#### 110. Relief for spouses and children on other visas\n##### (a) Work authorization for holders\nSection 214 of the Immigration and Nationality Act ( 8 U.S.C. 1184 ) is amended by adding at the end the following:\n(s) In the case of an alien spouse or child over the age of 16 admitted under subparagraphs (E), (H), (L), and (O) of section 101(a)(15)(H) who is accompanying or following to join a principle alien admitted under such section, the Secretary shall authorize such nonimmigrant to engage in employment in the United States and provide the nonimmigrant with an employment authorized endorsement or other appropriate work permit. .\n##### (b) Protecting H\u20134 children who age out of status\n**(1)**\nSection 214(g)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1184(g) ) is amended by inserting at the end\nThe following exceptions apply: (A) Any alien who\u2014 (i) is the beneficiary of a petition filed under section 204(a) of that Act for a preference status under paragraph (1), (2), or (3) of section 203(b) of that Act; and (ii) is eligible to be granted that status but for application of the per country limitations applicable to immigrants under those paragraphs, may apply for, and the Attorney General may grant, an extension of such nonimmigrant status until the alien\u2019s application for adjustment of status has been processed and a decision made thereon. (B) The children, accompanying or following to join, an alien described in (A) shall be eligible to apply for and receive an extension of their nonimmigrant status, regardless of their age, so long as\u2014 (i) the parent of a minor described in (A) maintains their nonimmigrant status; and (ii) the alien was under 18 years of age when they were first granted nonimmigrant status as an alien accompanying or following to join, the nonimmigrant parent. .\n**(2)**\nSection 203(h) of the Immigration and Nationality Act ( 8 U.S.C. 1153(h) ) is amended by inserting at the end of the paragraph:\n(5) Notwithstanding paragraph (1), a determination of whether an alien described under section 204(g)(4)(B) satisfies the age requirement for purposes of a derivative visa or adjustment of status application under paragraph (1), (2), or (3) of section 203(b) of the of the Immigration and Nationality Act shall be made using the age of the alien on the date the petitioner files a petition on behalf of the parent beneficiary with the Secretary of Homeland Security (or the Secretary of State, if applicable), unless the filing of the petition was preceded by the filing of a labor certification with the Secretary of Labor, in which case that date shall be used to identify the age. .\n#### 111. Extension of the application period for certain aliens present in the United States for adjustment of status\nSection 245(i) of the Immigration and Nationality Act ( 8 U.S.C. 1255(i) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), in the undesignated matter following clause (ii), by striking the semicolon and inserting ; and ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (i), by striking April 30, 2001 and inserting the date that is not later than 5 years after the date of the enactment of the Reuniting Families Act ; and\n**(ii)**\nin clause (ii), by striking ; and and inserting a period; and\n**(C)**\nby striking subparagraph (C); and\n**(2)**\nby amending paragraph (3)(B) to read as follows:\n(B) Any remaining portion of such fees remitted under such paragraphs shall be deposited into the Immigration Examinations Fee Account established under section 286(m). .\n#### 112. Expansion of cancellation of removal\n##### (a) In general\nSection 240A of the Immigration and Nationality Act ( 8 U.S.C. 1229b ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by striking 10 and inserting 7 ; and\n**(ii)**\nby amending subparagraph (D) to read as follows:\n(D) establishes that removal would result in extreme hardship to\u2014 (i) the alien; or (ii) the alien\u2019s spouse or permanent partner, parent, or child who is a citizen of the United States or an alien lawfully admitted for permanent residence. ; and\n**(B)**\nby adding at the end the following:\n(7) Affirmative Application process (A) In general The Secretary of Homeland Security may cancel the removal of, and adjust to the status of an alien lawfully admitted for permanent residence, an alien described in paragraph (1) or (2), who\u2014 (i) demonstrates that the alien is the spouse, permanent partner, parent, son or daughter, or legal guardian of a citizen of the United States; and (ii) submits to the Secretary of Homeland Security an application at such time, in such manner, and containing such information as the Secretary may reasonably require. (B) Numerical limitations Notwithstanding any other provision of law, an alien admitted to the United States under this section shall not be subject to any numerical limitation. ; and\n**(2)**\nby striking subsection (e).\n##### (b) Regulations\nThe Secretary of Homeland Security shall promulgate regulations setting forth procedures and requirements with respect to the processing and adjudication of affirmative applications for cancellation of removal under paragraph (7) of section 240A(b) of the Immigration and Nationality Act ( 8 U.S.C. 1229b(b) ), as added by subsection (a)(1)(B).\n#### 113. Prohibition on removal of aliens with pending applications\n##### (a) In general\nSection 235 of the Immigration and Nationality Act ( 8 U.S.C. 1225 ) is amended\u2014\n**(1)**\nin the section heading, by inserting ; prohibition on removal after hearing ; and\n**(2)**\nby adding at the end the following:\n(e) Prohibition on removal of aliens with certain pending petitions and applications (1) Beneficiaries of petitions for immigrant visas An alien who is the beneficiary (including a spouse or child of the principal alien, if eligible to receive a visa under section 203(d)) of a petition for classification under section 204 that was filed with the Secretary of Homeland Security and who is prima facie eligible for approval may not be removed while such petition or application is pending or a decision on such petition or application is on appeal. (2) Applicants for certain nonimmigrant and special immigrant classifications and cancellation of removal An applicant for classification as a nonimmigrant described in subparagraph (T), (U), or (V) of section 101(a)(15), an applicant for classification as a special immigrant under section 101(a)(27)(J), or an applicant for cancellation of removal under section 240A may not be removed while such application is pending or a decision on such application is on appeal. .\n##### (b) Conforming amendment\nThe table of contents at the beginning of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended by striking the item relating to section 235 and inserting the following:\nSec. 235. Inspection by immigration officers; expedited removal of inadmissible arriving aliens; referral for hearing; prohibition on removal. .\nII\nUniting American Families Act\n#### 201. Definitions of permanent partner and permanent partnership\nSection 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ) is amended\u2014\n**(1)**\nin paragraph (15)(K)(ii), by inserting or permanent partnership after marriage ; and\n**(2)**\nby adding at the end the following:\n(52) The term permanent partner means an individual 18 years of age or older who\u2014 (A) is in a committed, intimate relationship with another individual 18 years of age or older in which both parties intend a lifelong commitment; (B) is financially interdependent with that other individual, unless the Secretary of Homeland Security or the Secretary of State has determined, on a case-by-case basis, that the requirement under this subparagraph is unreasonable; (C) is not married to or in a permanent partnership with anyone other than that other individual; (D) is unable to contract with that other individual a marriage cognizable under this Act; and (E) is not a first-, second-, or third-degree blood relation of that other individual. (53) The term permanent partnership means the relationship that exists between two permanent partners. (54) The term alien permanent partner means the individual in a permanent partnership who is being sponsored for a visa .\n#### 202. Definition of child\n##### (a) Titles I and II\nSection 101(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1101(b)(1) ) is amended by adding at the end the following:\n(H) (i) a biological child of an alien permanent partner if the child was under the age of 18 at the time the permanent partnership was formed; or (ii) a child adopted by an alien permanent partner while under the age of 16 years if the child has been in the legal custody of, and has resided with, such adoptive parent for at least 2 years and if the child was under the age of 18 at the time the permanent partnership was formed. .\n##### (b) Title III\nSection 101(c) of the Immigration and Nationality Act ( 8 U.S.C. 1101(c) ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting or as described in subsection (b)(1)(H) after The term child means an unmarried person under twenty-one years of age ; and\n**(2)**\nin paragraph (2), by inserting or a deceased permanent partner of the deceased parent, father, or mother, after deceased parent, father, and mother .\n#### 203. Numerical limitations on individual foreign states\n##### (a) Per country levels\nSection 202(a)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1152(a)(4) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting , permanent partners, after spouses ;\n**(2)**\nin the heading of subparagraph (A), by inserting , permanent partners, after spouses ; and\n**(3)**\nin the heading of subparagraph (C), by striking and daughters and inserting without permanent partners and unmarried daughters without permanent partners .\n##### (b) Rules for chargeability\nSection 202(b)(2) of such Act ( 8 U.S.C. 1152(b)(2) ) is amended\u2014\n**(1)**\nby inserting or permanent partner after spouse each place it appears; and\n**(2)**\nby inserting or permanent partners after husband and wife .\n#### 204. Allocation of immigrant visas\n##### (a) Preference allocation for sons and daughters of citizens\nSection 203(a)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1153(a)(3) ) is amended\u2014\n**(1)**\nin the heading, by inserting and daughters and sons with permanent partners after daughters ; and\n**(2)**\nby inserting , or daughters or sons with permanent partners, after daughters .\n##### (b) Employment creation\nSection 203(b)(5)(A)(ii) of such Act ( 8 U.S.C. 1153(b)(5)(A)(ii) ) is amended by inserting permanent partner, after spouse, .\n##### (c) Treatment of family members\nSection 203(d) of such Act ( 8 U.S.C. 1153(d) ) is amended\u2014\n**(1)**\nby inserting , permanent partner, after spouse each place it appears; and\n**(2)**\nby striking or (E) and inserting (E), or (H) .\n#### 205. Procedure for granting immigrant status\n##### (a) Classification petitions\nSection 204(a)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1154(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by inserting or permanent partner after spouse ;\n**(2)**\nin subparagraph (A)(iii)\u2014\n**(A)**\nby inserting or permanent partner after spouse each place it appears; and\n**(B)**\nin subclause (I), by inserting or permanent partnership after marriage each place it appears;\n**(3)**\nin subparagraph (A)(v)(I), by inserting permanent partner, after is the spouse, ;\n**(4)**\nin subparagraph (A)(vi)\u2014\n**(A)**\nby inserting or termination of the permanent partnership after divorce ; and\n**(B)**\nby inserting , permanent partner, after spouse ; and\n**(5)**\nin subparagraph (B)\u2014\n**(A)**\nby inserting or permanent partner after spouse each place it appears;\n**(B)**\nby inserting or permanent partnership after marriage in clause (ii)(I)(aa) and the first place it appears in clause (ii)(I)(bb); and\n**(C)**\nin clause (ii)(II)(aa)(CC)(bbb), by inserting (or the termination of the permanent partnership) after termination of the marriage .\n##### (b) Immigration fraud prevention\nSection 204(c) of such Act ( 8 U.S.C. 1154(c) ) is amended\u2014\n**(1)**\nby inserting or permanent partner after spouse each place it appears; and\n**(2)**\nby inserting or permanent partnership after marriage each place it appears.\n##### (c) Restrictions on petitions based on marriages entered while in exclusion or deportation proceedings\nSection 204(g) of such Act ( 8 U.S.C. 1154(g) ) is amended by inserting or permanent partnership after marriage each place it appears.\n##### (d) Survival of rights To petition\nSection 204(h) of such Act ( 8 U.S.C. 1154(h) ) is amended\u2014\n**(1)**\nby inserting or permanent partnership after marriage each place it appears; and\n**(2)**\nby inserting or formation of a new permanent partnership after Remarriage .\n#### 206. Annual admission of refugees and admission of emergency situation refugees\nSection 207(c) of the Immigration and Nationality Act ( 8 U.S.C. 1157(c) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nby inserting or permanent partner after spouse each place it appears;\n**(B)**\nby inserting or permanent partner\u2019s after spouse\u2019s ; and\n**(C)**\nin subparagraph (A)\u2014\n**(i)**\nby striking or after (D), ; and\n**(ii)**\nby inserting , or (H) after (E) ; and\n**(2)**\nin paragraph (4), by inserting or permanent partner after spouse .\n#### 207. Asylum\nSection 208(b)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1158(b)(3) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting or permanent partner after spouse ; and\n**(2)**\nin subparagraph (A)\u2014\n**(A)**\nby inserting or permanent partner after spouse ;\n**(B)**\nby striking or after (D), ; and\n**(C)**\nby inserting , or (H) after (E) .\n#### 208. Adjustment of status of refugees\nSection 209(b)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1159(b)(3) ) is amended by inserting or permanent partner after spouse .\n#### 209. Inadmissible aliens\n##### (a) Classes of aliens ineligible for visas or admission\nSection 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) is amended\u2014\n**(1)**\nin paragraph (3)(D)(iv), by inserting permanent partner, after spouse, ;\n**(2)**\nin paragraph (4)(C)(i)(I), by inserting , permanent partner, after spouse ;\n**(3)**\nin paragraph (6)(E)(ii), by inserting permanent partner, after spouse, ; and\n**(4)**\nin paragraph (9)(B)(v), by inserting , permanent partner, after spouse .\n##### (b) Waivers\nSection 212(d) of such Act ( 8 U.S.C. 1182(d) ) is amended\u2014\n**(1)**\nin paragraph (11), by inserting permanent partner, after spouse, ; and\n**(2)**\nin paragraph (12), by inserting , permanent partner, after spouse .\n##### (c) Waivers of inadmissibility on health-Related grounds\nSection 212(g)(1)(A) of such Act ( 8 U.S.C. 1182(g)(1)(A) ) is amended by inserting or permanent partner after spouse .\n##### (d) Waivers of inadmissibility on criminal and related grounds\nSection 212(h)(1)(B) of such Act ( 8 U.S.C. 1182(h)(1)(B) ) is amended by inserting permanent partner, after spouse, .\n##### (e) Waiver of inadmissibility for misrepresentation\nSection 212(i)(1) of such Act ( 8 U.S.C. 1182(i)(1) ) is amended by inserting permanent partner, after spouse, .\n#### 210. Nonimmigrant status for permanent partners awaiting the availability of an immigrant visa\nSection 214 of the Immigration and Nationality Act ( 8 U.S.C. 1184 ) is amended\u2014\n**(1)**\nin subsection (e)(2), by inserting or permanent partner after spouse ; and\n**(2)**\nin subsection (r)\u2014\n**(A)**\nin paragraph (1), by inserting or permanent partner after spouse ; and\n**(B)**\nby inserting or permanent partnership after marriage each place it appears.\n#### 211. Derivative status for permanent partners of nonimmigrant visa holders\nSection 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by inserting , which shall include permanent partners after immediate family ;\n**(B)**\nin clause (ii), by inserting , which shall include permanent partners after immediate families ; and\n**(C)**\nin clause (iii), by inserting , which shall include permanent partners, after immediate families, ;\n**(2)**\nin subparagraph (E), by inserting or permanent partner after spouse ;\n**(3)**\nin subparagraph (F)(ii), by inserting or permanent partner after spouse ;\n**(4)**\nin subparagraph (G)(i), by inserting , which shall include his or her permanent partner after members of his or their immediate family ;\n**(5)**\nin subparagraph (G)(ii), by inserting , which shall include permanent partners, after the members of their immediate families ;\n**(6)**\nin subparagraph (G)(iii), by inserting , which shall include his permanent partner, after the members of his immediate family ;\n**(7)**\nin subparagraph (G)(iv), by inserting , which shall include permanent partners after the members of their immediate families ;\n**(8)**\nin subparagraph (G)(v), by inserting , which shall include permanent partners after the members of the immediate families ;\n**(9)**\nin subparagraph (H), by inserting or permanent partner after spouse ;\n**(10)**\nin subparagraph (I), by inserting or permanent partner after spouse ;\n**(11)**\nin subparagraph (J), by inserting or permanent partner after spouse ;\n**(12)**\nin subparagraph (L), by inserting or permanent partner after spouse ;\n**(13)**\nin subparagraph (M)(ii), by inserting or permanent partner after spouse ;\n**(14)**\nin subparagraph (O)(iii), by inserting or permanent partner after spouse ;\n**(15)**\nin subparagraph (P)(iv), by inserting or permanent partner after spouse ;\n**(16)**\nin subparagraph (Q)(ii)(II), by inserting or permanent partner after spouse ;\n**(17)**\nin subparagraph (R), by inserting or permanent partner after spouse ;\n**(18)**\nin subparagraph (S), by inserting or permanent partner after spouse ;\n**(19)**\nin subparagraph (T)(ii)(I), by inserting or permanent partner after spouse ;\n**(20)**\nin subparagraph (T)(ii)(II), by inserting or permanent partner after spouse ;\n**(21)**\nin subparagraph (U)(ii)(I), by inserting or permanent partner after spouse ;\n**(22)**\nin subparagraph (U)(ii)(II), by inserting or permanent partner after spouse ; and\n**(23)**\nin subparagraph (V), by inserting permanent partner or after beneficiary (including a .\n#### 212. Conditional permanent resident status for certain alien spouses, permanent partners, and sons and daughters\n##### (a) Section heading\n**(1) In general**\nThe heading for section 216 of the Immigration and Nationality Act ( 8 U.S.C. 1186a ) is amended by inserting and permanent partners after spouses .\n**(2) Clerical amendment**\nThe table of contents of such Act is amended by amending the item relating to section 216 to read as follows:\nSec. 216. Conditional permanent resident status for certain alien spouses and permanent partners and sons and daughters. .\n##### (b) In general\nSection 216(a) of such Act ( 8 U.S.C. 1186a(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting or permanent partner after spouse ;\n**(2)**\nin paragraph (2)(A), by inserting or permanent partner after spouse ;\n**(3)**\nin paragraph (2)(B), by inserting permanent partner, after spouse, ; and\n**(4)**\nin paragraph (2)(C), by inserting permanent partner, after spouse, .\n##### (c) Termination of status If finding that qualifying marriage improper\nSection 216(b) of such Act ( 8 U.S.C. 1186a(b) ) is amended\u2014\n**(1)**\nin the heading, by inserting or permanent partnership after marriage ;\n**(2)**\nin paragraph (1)(A), by inserting or permanent partnership after marriage ; and\n**(3)**\nin paragraph (1)(A)(ii)\u2014\n**(A)**\nby inserting or has ceased to satisfy the criteria for being considered a permanent partnership under this Act, after terminated, ; and\n**(B)**\nby inserting or permanent partner after spouse .\n##### (d) Requirements of timely petition and interview for removal of condition\nSection 216(c) of such Act ( 8 U.S.C. 1186a(c) ) is amended\u2014\n**(1)**\nin paragraphs (1), (2)(A)(ii), (3)(A)(ii), (3)(C), (4)(B), and (4)(C), by inserting or permanent partner after spouse each place it appears; and\n**(2)**\nin paragraph (3)(A), in the matter following clause (ii), and in paragraphs (3)(D), (4)(B), and (4)(C), by inserting or permanent partnership after marriage each place it appears.\n##### (e) Contents of petition\nSection 216(d)(1) of such Act ( 8 U.S.C. 1186a(d)(1) ) is amended\u2014\n**(1)**\nin the heading of subparagraph (A), by inserting or permanent partnership after marriage ;\n**(2)**\nin subparagraph (A)(i), by inserting or permanent partnership after marriage ;\n**(3)**\nin subparagraph (A)(i)(I), by inserting before the comma at the end , or is a permanent partnership recognized under this Act ;\n**(4)**\nin subparagraph (A)(i)(II)\u2014\n**(A)**\nby inserting or has not ceased to satisfy the criteria for being considered a permanent partnership under this Act, after terminated, ; and\n**(B)**\nby inserting or permanent partner after spouse ;\n**(5)**\nin subparagraph (A)(ii), by inserting or permanent partner after spouse ; and\n**(6)**\nin subparagraph (B)(i)\u2014\n**(A)**\nby inserting or permanent partnership after marriage ; and\n**(B)**\nby inserting or permanent partner after spouse .\n##### (f) Definitions\nSection 216(g) of such Act ( 8 U.S.C. 1186a(g) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby inserting or permanent partner after spouse each place it appears; and\n**(B)**\nby inserting or permanent partnership after marriage each place it appears;\n**(2)**\nin paragraph (2), by inserting or permanent partnership after marriage ;\n**(3)**\nin paragraph (3), by inserting or permanent partnership after marriage ; and\n**(4)**\nin paragraph (4)\u2014\n**(A)**\nby inserting or permanent partner after spouse each place it appears; and\n**(B)**\nby inserting or permanent partnership after marriage .\n#### 213. Conditional permanent resident status for certain alien entrepreneurs, spouses, permanent partners, and children\n##### (a) Section heading\n**(1) In general**\nThe heading for section 216A of the Immigration and Nationality Act ( 8 U.S.C. 1186b ) is amended by inserting or permanent partners after spouses .\n**(2) Clerical amendment**\nThe table of contents of such Act is amended by amending the item relating to section 216A to read as follows:\nSec. 216A. Conditional permanent resident status for certain alien entrepreneurs, spouses or permanent partners, and children. .\n##### (b) In general\nSection 216A(a) of such Act ( 8 U.S.C. 1186b(a) ) is amended, in paragraphs (1), (2)(A), (2)(B), and (2)(C), by inserting or permanent partner after spouse each place it appears.\n##### (c) Termination of status If finding that qualifying entrepreneurship improper\nSection 216A(b)(1) of such Act ( 8 U.S.C. 1186b(b)(1) ) is amended by inserting or permanent partner after spouse in the matter following subparagraph (C).\n##### (d) Requirements of timely petition and interview for removal of condition\nSection 216A(c) of such Act ( 8 U.S.C. 1186b(c) ) is amended, in paragraphs (1), (2)(A)(ii), and (3)(C), by inserting or permanent partner after spouse .\n##### (e) Definitions\nSection 216A(f)(2) of such Act ( 8 U.S.C. 1186b(f)(2) ) is amended by inserting or permanent partner after spouse each place it appears.\n#### 214. Deportable aliens\nSection 237(a) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a) ) is amended\u2014\n**(1)**\nin paragraph (1)(D)(i), by inserting or permanent partners after spouses each place it appears;\n**(2)**\nin paragraphs (1)(E)(ii), (1)(E)(iii), and (1)(H)(I)(I), by inserting or permanent partner after spouse ; and\n**(3)**\nin paragraphs (2)(E)(i) and (3)(C)(ii), by inserting or permanent partner after spouse each place it appears.\n#### 215. Removal proceedings\nSection 240 of the Immigration and Nationality Act ( 8 U.S.C. 1229a ) is amended\u2014\n**(1)**\nin the heading of subsection (c)(7)(C)(iv), by inserting permanent partners, after spouses, ; and\n**(2)**\nin subsection (e)(1), by inserting or permanent partner after spouse .\n#### 216. Cancellation of removal; adjustment of status\nSection 240A(b) of the Immigration and Nationality Act ( 8 U.S.C. 1229b(b) ) is amended\u2014\n**(1)**\nin the heading for paragraph (2), by inserting , permanent partner, after spouse ; and\n**(2)**\nin paragraph (2)(A), by inserting , permanent partner, after spouse each place it appears.\n#### 217. Adjustment of status of nonimmigrant to that of person admitted for permanent residence\n##### (a) Prohibition on adjustment of status\nSection 245(d) of the Immigration and Nationality Act ( 8 U.S.C. 1255(d) ) is amended by inserting or permanent partnership after marriage .\n##### (b) Avoiding immigration fraud\nSection 245(e) of such Act ( 8 U.S.C. 1255(e) ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting or permanent partnership after marriage ; and\n**(2)**\nby adding at the end the following new paragraph:\n(4) Paragraph (1) and section 204(g) shall not apply with respect to a permanent partnership if the alien establishes by clear and convincing evidence to the satisfaction of the Secretary of Homeland Security that the permanent partnership was entered into in good faith and in accordance with section 101(a)(52) and the permanent partnership was not entered into for the purpose of procuring the alien\u2019s admission as an immigrant and no fee or other consideration was given (other than a fee or other consideration to an attorney for assistance in preparation of a lawful petition) for the filing of a petition under section 204(a) or 214(d) with respect to the alien permanent partner. In accordance with regulations, there shall be only one level of administrative appellate review for each alien under the previous sentence. .\n##### (c) Adjustment of status for certain aliens paying fee\nSection 245(i)(1) of such Act ( 8 U.S.C. 1255(i)(1) ) is amended by inserting or permanent partner after spouse each place it appears.\n##### (d) Adjustment of status for certain alien informants\nSection 245(j) of such Act ( 8 U.S.C. 1255(j) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby inserting or permanent partner after spouse ; and\n**(B)**\nby inserting sons and daughters with and without permanent partners, after daughters, ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby inserting or permanent partner after spouse ; and\n**(B)**\nby inserting sons and daughters with and without permanent partners, after daughters, .\n##### (e) Trafficking\nSection 245(l)(1) of such Act is amended by inserting permanent partner, after spouse, .\n#### 218. Application of criminal penalties for misrepresentation and concealment of facts regarding permanent partnerships\nSection 275(c) of the Immigration and Nationality Act ( 8 U.S.C. 1325(c) ) is amended to read as follows:\n(c) Any individual who knowingly enters into a marriage or permanent partnership for the purpose of evading any provision of the immigration laws shall be imprisoned for not more than 5 years, or fined not more than $250,000, or both. .\n#### 219. Requirements as to residence, good moral character, attachment to the principles of the Constitution\nSection 316(b) of the Immigration and Nationality Act ( 8 U.S.C. 1427(b) ) is amended by inserting or permanent partner after spouse .\n#### 220. Naturalization for permanent partners of citizens\nSection 319 of the Immigration and Nationality Act ( 8 U.S.C. 1430 ) is amended\u2014\n**(1)**\nin subsection (b)(1), by inserting or permanent partner after spouse ;\n**(2)**\nin subsection (b)(3), by inserting or permanent partner after spouse ;\n**(3)**\nin subsection (d)\u2014\n**(A)**\nby inserting or permanent partner after spouse each place it appears; and\n**(B)**\nby inserting or permanent partnership after marital union ;\n**(4)**\nin subsection (e)(1)\u2014\n**(A)**\nby inserting or permanent partner after spouse ; and\n**(B)**\nby inserting or permanent partnership after marital union ; and\n**(5)**\nin subsection (e)(2), by inserting or permanent partner after spouse .\n#### 221. Application of family unity provisions to permanent partners of certain LIFE Act beneficiaries\nSection 1504 of the LIFE Act (division B of the Miscellaneous Appropriations Act, 2001, as enacted into law by section 1(a)(4) of Public Law 106\u2013554 ) is amended\u2014\n**(1)**\nin the heading, by inserting , permanent partners, after spouses ;\n**(2)**\nin subsection (a), by inserting , permanent partner, after spouse ; and\n**(3)**\nin each of subsections (b) and (c)\u2014\n**(A)**\nin the subsection headings, by inserting , permanent partners, after spouses ; and\n**(B)**\nby inserting , permanent partner, after spouse each place it appears.\n#### 222. Application to Cuban Adjustment Act\n##### (a) In general\nThe first section of Public Law 89\u2013732 (November 2, 1966; 8 U.S.C. 1255 note) is amended\u2014\n**(1)**\nin the next to last sentence, by inserting , permanent partner, after spouse the first two places it appears; and\n**(2)**\nin the last sentence, by inserting , permanent partners, after spouses .\n##### (b) Conforming amendments\n**(1) Immigration and Nationality Act**\nSection 101(a)(51)(D) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(51)(D) ) is amended by striking or spouse and inserting , spouse, or permanent partner .\n**(2) Violence Against Women Act**\nSection 1506(c)(2)(A)(I)(IV) of the Violence Against Women Act of 2000 ( 8 U.S.C. 1229a note; division B of Public Law 106\u2013386 ) is amended by striking or spouse and inserting , spouse, or permanent partner .\n#### 223. Nationality at birth\nSection 301 of the Immigration and Nationality Act ( 8 U.S.C. 1401 ) is amended by adding at the end the following:\n(i) Any reference to a person born of parents in this section shall include the following: (1) Any legally recognized parent-child relationship formed within the first year of a person\u2019s life regardless of any genetic or gestational relationship. (2) Either parent of a child born through Assisted Reproductive Technology who is legally recognized as a parent in the relevant jurisdiction regardless of any genetic or gestational relationship. (3) The spouse of a parent at the time of birth, where both of the following apply: (A) At least one parent is a legally recognized parent. (B) The marriage occurred before the child\u2019s birth and is recognized in the United States, regardless of where the parents reside. .\nIII\nPromoting Diversity and Protecting Against Discrimination in our Immigration System\n#### 301. Increasing diversity visas\nSection 201(e) of the Immigration and Nationality Act ( 8 U.S.C. 1151(e) ) is amended by striking 55,000 and inserting 80,000 .\n#### 302. Addressing the impact of the Muslim and African bans\nSection 201 of the Immigration and Nationality Act ( 8 U.S.C. 1151 ) is amended by adding at the end the following:\n(g) Diversity visas Notwithstanding section 204(a)(1)(I)(ii)(II), an immigrant visa for an alien selected in accordance with section 203(e)(2) in fiscal year 2017, 2018, 2019, 2020, 2021, or 2022 shall remain available to such alien (and the spouse and children of such alien) if\u2014 (1) the alien was refused a visa, prevented from seeking admission, or denied admission to the United States solely because of Executive Order 13769, Executive Order 13780, Presidential Proclamation 9645, or Presidential Proclamation 9983; or (2) because of restrictions or limitations on visa processing, visa issuance, travel, or other effects associated with the COVID\u201319 public health emergency\u2014 (A) the alien was unable to receive a visa interview despite submitting an Online Immigrant Visa and Alien Registration Application (Form DS\u2013260) to the Secretary of State; or (B) the alien was unable to seek admission or was denied admission to the United States despite being approved for a visa under section 203(c). .\nIV\nAddressing the Needs of Refugee Families\n#### 401. Prioritization of family reunification in refugee resettlement process\n##### (a) In general\nThe Secretary of State shall prioritize refugees seeking reunification with relatives living in the United States, regardless of the nationality of such refugees.\n##### (b) Regulations\n**(1) In general**\nThe Secretary of State, in consultation with the Secretary of Homeland Security, shall promulgate regulations to ensure that an individual seeking admission to the United States as a refugee shall not be excluded from being interviewed for refugee status based on\u2014\n**(A)**\na close family relationship to a citizen or lawful permanent resident of the United States;\n**(B)**\na potential qualification of the individual for an immigrant visa; or\n**(C)**\na pending application by the individual for admission to the United States.\n**(2) Simultaneous consideration**\nThe regulations promulgated under paragraph (1) shall ensure that an applicant for admission as a refugee is permitted to pursue simultaneously admission to the United States\u2014\n**(A)**\nas a refugee; and\n**(B)**\nunder any visa category for which the applicant may be eligible.\n##### (c) Notice of separate travel\nIn the case of an applicant for admission under section 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ) the application of whom is placed on hold for more than three months and one or more members of the family of the applicant have separate pending applications for admission under such section, the Secretary of Homeland Security shall\u2014\n**(1)**\nnotify any individual on that case who is eligible to travel separately of the option to separate the case of the individual from the family unit; and\n**(2)**\npermit the individual to travel based on the satisfaction by the individual of all security and other requirements for a refugee application.\n##### (d) Use of embassy referrals\n**(1) In general**\nThe Secretary of State shall set forth a plan to ensure that each United States embassy and consulate is equipped and enabled to refer individuals in need of resettlement to the United States refugee admissions program.\n**(2) Training**\nThe Secretary of State shall undertake training for embassy personnel to ensure that each embassy and consulate has sufficient knowledge and expertise to carry out this paragraph.\n#### 402. Priority 3 family reunification cases\n##### (a) In general\nBecause of the importance of reuniting immediate refugee families who have been separated while fleeing from persecution, Priority 3 processing shall be made available to individuals of all nationalities, including stateless individuals.\n##### (b) Universal eligibility for all nationalities\n**(1) In general**\nEligible Priority 3 Affidavit of Relationship filers will include those admitted in asylum, refugee, or Afghan and Iraqi special immigrants admitted under section 1059 of the National Defense Authorization Act for Fiscal Year 2006 ( Public Law 109\u2013163 ; 8 U.S.C. 1101 note), section 1244 of the Refugee Crisis in Iraq Act of 2007 ( Public Law 110\u2013181 ; 8 U.S.C. 1157 note), and section 602 of the Afghan Allies Protection Act of 2009 ( Public Law 111\u20138 ; 8 U.S.C. 1101 note).\n**(2) Eligible affidavit of relationship files**\nEligible Affidavit of Relationship (referred to in this section as AOR ) filers include individuals who are lawful permanent residents of the United States or United States citizens who initially were admitted to the United States in a status described in paragraph (1).\n##### (c) Requirements\nThe United States-based filer shall be at least 18 years of age at the time that the AOR is filed. The filer shall file the AOR not later than 5 years after the date they were admitted as a refugee or special immigrant or were granted asylum. The Secretary of State may reject any AOR for a relationship that does not comport with public policy, such as underage or plural marriages.\n##### (d) Family members included\n**(1) In general**\nThe following family members of the United States-based family members are qualified for Priority 3 access:\n**(A)**\nSpouse or permanent partner.\n**(B)**\nUnmarried children who are younger than 21 years of age.\n**(C)**\nParents.\n**(2) Partners**\nThe Secretary of State may allow a qualifying individual to file for Priority 3 access for a partner of any gender if the filer can provide evidence of a relationship with the partner for at least one year overseas prior to the submission of the AOR and considered that person to be his or her spouse or life partner, and that the relationship is ongoing, together with evidence that legal marriage was not an obtainable option due to social or legal prohibitions.\n##### (e) Derivative refugee status\nIn addition to the qualifying family members of a United States-based individual identified above, the qualifying family member\u2019s spouse or permanent partner, as well as unmarried children younger than 21 years of age, may derive refugee status from the principal applicant for refugee status.\n##### (f) Additional qualifying family members\nOn a case-by-case basis, an individual may be added to a qualifying family member\u2019s Priority 3 case if that individual\u2014\n**(1)**\nlived in the same household as the qualifying family member in the country of nationality or, if stateless, last habitual residence;\n**(2)**\nwas part of the same economic unit as the qualifying family member in the country of nationality or, if stateless, last habitual residence; and\n**(3)**\ndemonstrates exceptional and compelling humanitarian circumstances that justify inclusion on the qualifying family member\u2019s case.\n#### 403. Admission of refugee families and timely adjudication\nSection 207(c)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1157(c)(2) ) is amended to read as follows:\n(2) (A) (i) Irrespective of the date on which such refugee was admitted to the United States, the spouse or permanent partner, or a child (as defined in section 101(b)(1)) of any refugee, or the parent or de facto guardian (as determined by the Secretary of Homeland Security) of such a child who qualifies for admission under paragraph (1), if not otherwise entitled to admission under such paragraph and not described in section 101(a)(42)(B), shall be entitled to the same admission status as such refugee if\u2014 (I) accompanying, or following to join, such refugee; and (II) admissible (except as otherwise provided under paragraph (3)) as an immigrant under this chapter. (ii) The admission to the United States of a spouse or permanent partner, child, parent, or guardian described in clause (i) shall not be charged against the numerical limitation established in accordance with the appropriate subsection under which the refugee\u2019s admission is charged. (B) A mother or father who seeks to accompany, or follow to join, an alien child granted admission as a refugee under this subsection shall continue to be classified as a parent for purposes of this paragraph if the alien child attains 21 years of age while the application filed under this paragraph is pending. (C) The parent or de facto guardian (as determined by the Secretary of Homeland Security) of a refugee child admitted under this section and was admitted under the Unaccompanied Refugee Minors Program (as described in subparagraph (D), (E), or (H) of section 101(b)(1)) shall be treated in accordance with subparagraph (A) if such parent or guardian seeks to follow to join such refugee child and the minor consents to being joined by such individual. (D) (i) Not later than 1 year after the date on which an application for refugee status is filed under this paragraph\u2014 (I) required screenings and background checks shall be completed; and (II) the application shall be adjudicated. (ii) The adjudication of an application may exceed the timeframe under clause (i) only in exceptional circumstances in which additional time to process an application is necessary to satisfy national security concerns, if the Secretary of Homeland Security has\u2014 (I) made a determination that the applicant meets the requirements for refugee status under this section; and (II) notified the applicant of such determination. .",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-12-10",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3419",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Reuniting Families Act",
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
        "name": "Immigration",
        "updateDate": "2026-01-08T17:13:10Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6565ih.xml"
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
      "title": "Reuniting Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:54:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reuniting Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:54:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Filipino Veterans Family Reunification Act",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2026-01-06T06:54:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to promote family unity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:48:39Z"
    }
  ]
}
```
