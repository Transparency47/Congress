# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4524?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4524
- Title: Equity in Government Act
- Congress: 119
- Bill type: HR
- Bill number: 4524
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-11-01T08:05:25Z
- Update date including text: 2025-11-01T08:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4524",
    "number": "4524",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000617",
        "district": "7",
        "firstName": "Ayanna",
        "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
        "lastName": "Pressley",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Equity in Government Act",
    "type": "HR",
    "updateDate": "2025-11-01T08:05:25Z",
    "updateDateIncludingText": "2025-11-01T08:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NC"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "OH"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "OH"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IN"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "SC"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "LA"
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
      "sponsorshipDate": "2025-07-17",
      "state": "NC"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
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
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NV"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
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
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
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
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
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
      "sponsorshipDate": "2025-07-17",
      "state": "MA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NJ"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MD"
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
      "sponsorshipDate": "2025-07-17",
      "state": "DC"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
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
      "sponsorshipDate": "2025-07-17",
      "state": "MN"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "VI"
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
      "sponsorshipDate": "2025-07-17",
      "state": "IL"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MD"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
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
      "sponsorshipDate": "2025-07-17",
      "state": "NM"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MI"
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
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NJ"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "FL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4524ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4524\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Pressley (for herself, Mr. Garcia of California , Ms. Adams , Mrs. Beatty , Mr. Bishop , Ms. Brown , Mr. Carson , Mr. Clyburn , Ms. Crockett , Mr. Davis of Illinois , Mr. Fields , Mrs. Foushee , Mr. Frost , Ms. Garcia of Texas , Mr. Horsford , Mr. Jackson of Illinois , Ms. Jayapal , Mr. Johnson of Georgia , Ms. Kamlager-Dove , Ms. Kelly of Illinois , Mr. Kennedy of New York , Ms. Lee of Pennsylvania , Mr. Lynch , Mrs. McIver , Mr. Meeks , Mr. Mfume , Ms. Norton , Ms. Ocasio-Cortez , Ms. Omar , Ms. Plaskett , Mrs. Ramirez , Mr. Raskin , Ms. Simon , Mr. Soto , Ms. Stansbury , Ms. Tlaib , Ms. Vel\u00e1zquez , Mrs. Watson Coleman , and Ms. Williams of Georgia ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend titles 5, 31, and 44, United States Code, to improve the equitable provision of services to underserved communities and individuals, to establish an Agency Equity Advisory Team, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Equity in Government Act .\n#### 2. Amendments\n##### (a) Agency strategic plans\nSection 306 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(2), by inserting after of the agency the following: , with at least one goal, or 20 percent of the total number of goals, whichever is greater, relating to improving the equitable provision of services to underserved communities and individuals ;\n**(2)**\nin subsection (d), by inserting after in such a plan the following: , including nongovernmental organizations and other stakeholders, including academic and research partners, State and local governments, and community and advocacy groups, that can address how to improve the equitable provision of services to underserved communities and individuals ; and\n**(3)**\nby adding at the end the following new subsection:\n(d) Additional definitions In this section and sections 1115 and 1120 of title 31: (1) State The term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe. (2) Underserved communities The term underserved communities means populations sharing a particular characteristic, as well as geographic communities, that have been systematically denied a full opportunity to participate in aspects of economic, social, and civic life. (3) Underserved individual The term underserved individual means a member of any underserved communities. .\n##### (b) Agency performance plans\nSection 1115(b) of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by inserting after and the next fiscal year the following: , with at least one performance goal, or 20 percent of the total number of performance goals, whichever is greater, relating to improving the equitable provision of services to underserved communities and individuals ; and\n**(2)**\nin paragraph (5)(E), by inserting after other agencies the following: , nongovernmental organizations, and other stakeholders, including academic and research partners, State and local governments, and community and advocacy groups, .\n##### (c) Agency priority goals\nSection 1120(b)(1) of title 31, United States Code, is amended by inserting after the first sentence the following: At least one of the priority goals of each agency, or 20 percent of the priority goals of the agency, whichever is greater, shall be related to improving the equitable provision of services to underserved communities and individuals. .\n#### 3. Performance improvement officers\nSection 1124 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nin subparagraph (E), by striking ; and and inserting a semicolon;\n**(B)**\nin subparagraph (F), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting at the end the following:\n(G) establish and serve as the head of an Agency Equity Advisory Team, with at least 10 members, that includes representation from at least 10 of the following: (i) The head of the agency. (ii) Regulatory affairs senior designee. (iii) Counsel. (iv) Civil rights enforcement senior designee. (v) Policy development senior designee. (vi) Chief Financial Officer, Controller, or senior designee. (vii) Chief Data Officer or senior designee. (viii) Chief Science Officer or senior designee. (ix) Chief Human Capital Officer or senior designee. (x) Evaluation Officer or senior designee. (xi) Statistical official. (xii) Procurement senior designee. (xiii) Customer or user experience leadership. (xiv) Communications or public affairs senior designee. (xv) Public engagement senior designee. ; and\n**(2)**\nin subsection (b), by adding at the end the following new paragraph:\n(4) Equity Subcommittee (A) Establishment There is established an Equity Subcommittee of the Performance Improvement Council, consisting of members of that Council, to be selected by the Council. (B) Functions The Equity Subcommittee of the Performance Improvement Council shall\u2014 (i) assist the Director of the Office of Management and Budget in identifying guidance agencies need on how to provide services more equitably and developing such guidance; (ii) facilitate the sharing of information across agencies regarding practices that have led to the more equitable provision of services; (iii) coordinate with the Equitable Data Working Group of the Chief Data Officer Council (established pursuant to section 3520A of title 44) to ensure that agencies share best practices related to the equitable collection and use of data; and (iv) solicit input from nongovernmental organizations, State and local governments, and recipients of government services to determine best practices for providing government services equitably. .\n#### 4. Chief data officers\nTitle 44, United States Code, is amended\u2014\n**(1)**\nin section 3520(c)\u2014\n**(A)**\nin paragraph (13), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (14) by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting at the end the following new paragraph:\n(15) ensure the agency applies the recommendations of the Chief Data Officer Council developed pursuant to paragraphs (1) through (5) of section 3520A(b). ; and\n**(2)**\nin section 3520A\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), by striking the use and inserting the equitable use ;\n**(ii)**\nin paragraph (2), by striking between agencies and inserting between agencies, academic and research partners, State and local governments, community and advocacy groups, and other stakeholders ;\n**(iii)**\nin paragraph (3), by striking policymaking and inserting equitable policymaking ;\n**(iv)**\nin paragraph (4), by striking access and inserting equitable access ; and\n**(v)**\nin paragraph (5), by striking collection and inserting equitable collection ;\n**(B)**\nin subsection (d), by striking the Council. and inserting the Council, including the work of the Equitable Data Working Group. ;\n**(C)**\nby amending subsection (e) to read as follows:\n(e) Evaluation and termination (1) GAO Evaluation of Council Not later than 4 years after the date of the enactment of this paragraph, the Comptroller General shall submit to Congress a report on whether the additional duties of the Council, including the Equitable Data Working Group, improved the equitable collection and use of evidence, including for program evaluation, in the Federal Government. (2) Termination of Council The Council, including the Equitable Data Working Group, shall not terminate until at least two years after the date on which the Comptroller General submits the report under paragraph (1) to Congress. ; and\n**(D)**\nby adding at the end the following new subsections:\n(f) Equitable Data Working Group (1) Establishment There is established within the Council an Equitable Data Working Group. (2) Purpose and functions The Equitable Data Working Group shall ensure that the Council prioritizes equity when carrying out the functions of the Council described in paragraphs (1) through (5) of subsection (b). (3) Meetings; reports Not less frequently than once per quarter, the Equitable Data Working Group shall meet submit to the Chief Data Officer Council a written report with recommendations on how to execute the functions described in paragraphs (1) through (5) of subsection (b) to better achieve equitable methods and outcomes. (4) Membership (A) In general The Council shall select a subset of the members of the Council to serve as members of the Equitable Data Working Group. (B) Chair The Chair of the Council shall select the Chair of the Equitable Data Working Group from among the members of the Equitable Data Working Group. (g) State defined In this section and section 1124 of title 31, the term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe. .",
      "versionDate": "2025-07-17",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-17T20:51:02Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4524ih.xml"
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
      "title": "Equity in Government Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Equity in Government Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 5, 31, and 44, United States Code, to improve the equitable provision of services to underserved communities and individuals, to establish an Agency Equity Advisory Team, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:24Z"
    }
  ]
}
```
