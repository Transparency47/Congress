# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1505?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1505
- Title: Public Safety Employer-Employee Cooperation Act
- Congress: 119
- Bill type: HR
- Bill number: 1505
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-05-22T08:08:51Z
- Update date including text: 2026-05-22T08:08:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1505",
    "number": "1505",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Public Safety Employer-Employee Cooperation Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:51Z",
    "updateDateIncludingText": "2026-05-22T08:08:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:32:30Z",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "IL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "IL"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "ME"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NV"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "CO"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "MN"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NV"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "OR"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "CT"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IN"
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
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
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
      "sponsorshipDate": "2025-03-18",
      "state": "VA"
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
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "VA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "WA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MD"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "MD"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "WA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NM"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NJ"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CO"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "PA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "FL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "OR"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "NJ"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "RI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "KY"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "OH"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NJ"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CT"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "MI"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NJ"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "OR"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "DE"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1505ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1505\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Stauber (for himself, Ms. Budzinski , Mr. Van Drew , Mr. Bost , Mr. Golden of Maine , Ms. Titus , Mr. Kean , Ms. Pettersen , Ms. Craig , and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo provide collective bargaining rights for public safety officers employed by States or their political subdivisions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Safety Employer-Employee Cooperation Act .\n#### 2. Purpose and policy\nCongress declares that the following is the policy of the United States:\n**(1)**\nLabor-management relationships and partnerships are based on trust, mutual respect, open communication, bilateral consensual problem solving, and shared accountability. Labor-management cooperation fully utilizes the strengths of both parties to best serve the interests of the public, operating as a team, to carry out the public safety mission in a quality work environment. In many public safety agencies, it is the union that provides the institutional stability as elected leaders and appointees come and go.\n**(2)**\nState and local public safety officers play an essential role in the efforts of the United States to detect, prevent, and respond to terrorist attacks, and to respond to natural disasters, hazardous materials, and other mass casualty incidents. State and local public safety officers, as first responders, are a component of the National Incident Management System, developed by the Department of Homeland Security to coordinate response to and recovery from terrorism, major natural disasters, and other major emergencies. Public safety employer-employee cooperation is essential in meeting these needs and is, therefore, in the national interest.\n**(3)**\nThe Federal Government needs to encourage conciliation, mediation, and arbitration to aid and encourage employers and the representatives of their employees to reach and maintain agreements concerning rates of pay, hours, and working conditions, and to make all reasonable efforts through negotiations to settle their differences by mutual agreement reached through collective bargaining or by such methods as may be provided for in any applicable agreement for the settlement of disputes.\n**(4)**\nThe absence of adequate cooperation between public safety employers and employees has implications for the security of employees and can affect interstate and intrastate commerce. The lack of such labor-management cooperation can detrimentally impact the upgrading of law enforcement, fire, and emergency medical services of local communities, the health and well-being of public safety officers, and the morale of law enforcement, fire, and EMS departments. Additionally, these factors could have significant commercial repercussions. Moreover, providing minimal standards for collective bargaining negotiations in the public safety sector can prevent industrial strife between labor and management that interferes with the normal flow of commerce.\n**(5)**\nMany States and localities already provide public safety officers with collective bargaining rights comparable to or greater than the rights and responsibilities set forth in this Act, and such State and local laws should be respected.\n#### 3. Definitions\nIn this Act:\n**(1) Authority**\nThe term Authority means the Federal Labor Relations Authority.\n**(2) Confidential employee**\nThe term confidential employee has the meaning given such term under applicable State law on the date of enactment of this Act. If no such State law is in effect, the term means an individual, employed by a public safety employer, who\u2014\n**(A)**\nis designated as confidential; and\n**(B)**\nis an individual who routinely assists, in a confidential capacity, supervisory employees and management employees.\n**(3) Emergency medical services personnel**\nThe term emergency medical services personnel means an individual who provides out-of-hospital emergency medical care, including an emergency medical technician, paramedic, or first responder.\n**(4) Employer; public safety agency; public safety employer**\nThe terms employer , public safety agency , and public safety employer mean any State, or political subdivision of a State, that employs public safety officers.\n**(5) Firefighter**\nThe term firefighter has the meaning given the term employee engaged in fire protection activities in section 3(y) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(y) ).\n**(6) Labor organization**\nThe term labor organization means an organization of any kind, in which employees participate and which exists for the purpose, in whole or in part, of dealing with employers concerning grievances, conditions of employment, and related matters.\n**(7) Law enforcement officer**\nThe term law enforcement officer has the meaning given such term in section 1204 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284(6) ).\n**(8) Management employee**\nThe term management employee has the meaning given such term under applicable State law in effect on the date of enactment of this Act. If no such State law is in effect, the term means an individual employed by a public safety employer in a position that requires or authorizes the individual to formulate, determine, or influence the policies of the employer.\n**(9) Person**\nThe term person means an individual or a labor organization.\n**(10) Public safety officer**\nThe term public safety officer \u2014\n**(A)**\nmeans an employee of a public safety agency who is a law enforcement officer, a firefighter, or an emergency medical services personnel;\n**(B)**\nincludes an individual who is temporarily transferred to a supervisory or management position; and\n**(C)**\ndoes not include a permanent supervisory, management, or confidential employee.\n**(11) State**\nThe term State means each of the several States of the United States, the District of Columbia, and any territory or possession of the United States.\n**(12) Substantially provides**\nThe term substantially provides , when used with respect to the rights and responsibilities described in section 4(b), means comparable to or greater than each right and responsibility described in such section.\n**(13) Supervisory employee**\nThe term supervisory employee has the meaning given such term under applicable State law in effect on the date of enactment of this Act. If no such State law is in effect, the term means an individual, employed by a public safety employer, who\u2014\n**(A)**\nhas the authority in the interest of the employer to hire, direct, assign, promote, reward, transfer, furlough, lay off, recall, suspend, discipline, or remove public safety officers, to adjust their grievances, or to effectively recommend such action, if the exercise of the authority is not merely routine or clerical in nature but requires the consistent exercise of independent judgment; and\n**(B)**\ndevotes a majority of time at work to exercising such authority.\n#### 4. Determination of rights and responsibilities\n##### (a) Determination\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Authority shall make a determination as to whether a State substantially provides for the rights and responsibilities described in subsection (b).\n**(2) Consideration of additional opinions**\nIn making the determination described in paragraph (1), the Authority shall consider the opinions of affected employers and labor organizations. In the case where the Authority is notified by an affected employer and labor organization that both parties agree that the law applicable to such employer and labor organization substantially provides for the rights and responsibilities described in subsection (b), the Authority shall give such agreement weight to the maximum extent practicable in making the Authority\u2019s determination under this subsection.\n**(3) Limited criteria**\nIn making the determination described in paragraph (1), the Authority shall be limited to the application of the criteria described in subsection (b) and shall not require any additional criteria.\n**(4) Subsequent determinations**\n**(A) In general**\nA determination made pursuant to paragraph (1) shall remain in effect unless and until the Authority issues a subsequent determination, in accordance with the procedures set forth in subparagraph (B) of this section.\n**(B) Procedures for subsequent determinations**\nUpon establishing that a material change in State law or its interpretation has occurred, an employer or a labor organization may submit a written request for a subsequent determination. If satisfied that a material change in State law or its interpretation has occurred, the Authority shall issue a subsequent determination not later than 30 days after receipt of such request.\n**(5) Judicial review**\nAny person or employer aggrieved by a determination of the Authority under this section may, during the 60-day period beginning on the date on which the determination was made, petition any United States Court of Appeals in the circuit in which the person or employer resides or transacts business or in the District of Columbia Circuit, for judicial review.\n##### (b) Rights and responsibilities\nIn making a determination described in subsection (a), the Authority shall consider a State\u2019s law to substantially provide the required rights and responsibilities unless such law fails to provide rights and responsibilities comparable to or greater than the following:\n**(1)**\nGranting public safety officers the right to form and join a labor organization, which may exclude management employees, supervisory employees, and confidential employees, that is, or seeks to be, recognized as the exclusive bargaining representative of such employees.\n**(2)**\nRequiring public safety employers to recognize the employees\u2019 labor organization (freely chosen by a majority of the employees), to agree to bargain with the labor organization, and to commit any agreements to writing in a contract or memorandum of understanding.\n**(3)**\nProviding for the right to bargain over hours, wages, and terms and conditions of employment.\n**(4)**\nProviding for binding interest arbitration as a mechanism to resolve an impasse in collective bargaining negotiations.\n**(5)**\nRequiring enforcement of all rights, responsibilities, and protections enumerated in this section, and of any written contract or memorandum of understanding between a labor organization and a public safety employer, through\u2014\n**(A)**\na State administrative agency, if the State so chooses; and/or\n**(B)**\nany court of competent jurisdiction.\n##### (c) Compliance with requirements\nIf the Authority determines, acting pursuant to its authority under subsection (a), that a State substantially provides rights and responsibilities described in subsection (b), then this Act shall not preempt State law.\n##### (d) Failure To meet requirements\n**(1) In general**\nIf the Authority determines, acting pursuant to its authority under subsection (a), that a State does not substantially provide for the rights and responsibilities described in subsection (b), then such State shall be subject to the regulations and procedures described in section 5 beginning on the later of\u2014\n**(A)**\nthe date that is 2 years after the date of enactment of this Act;\n**(B)**\nthe date that is the last day of the first regular session of the legislature of the State that begins after the date the Authority makes a determination under subsection (a)(1); or\n**(C)**\nin the case of a State receiving a subsequent determination under subsection (a)(4), the date that is the last day of the first regular session of the legislature of the State that begins after the date the Authority made the determination.\n**(2) Partial failure**\nIf the Authority makes a determination that a State does not substantially provide for the rights and responsibilities described in subsection (b) solely because the State law substantially provides for such rights and responsibilities for certain categories of public safety officers covered by the Act but not others, the Authority shall identify those categories of public safety officers that shall be subject to the regulations and procedures described in section 5, pursuant to section 8(b)(3) and beginning on the appropriate date described in paragraph (1), and those categories of public safety officers that shall remain solely subject to State law with respect to the rights and responsibilities described in subsection (b).\n#### 5. Role of Federal Labor Relations Authority\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Authority shall issue regulations, in accordance with the rights and responsibilities described in section 4(b), establishing collective bargaining procedures for employers and public safety officers in States where the Authority has determined, acting pursuant to section 4(a), do not substantially provide for such rights and responsibilities.\n##### (b) Role of the Federal Labor Relations Authority\nThe Authority, to the extent provided in this Act and in accordance with regulations prescribed by the Authority, shall\u2014\n**(1)**\ndetermine the appropriateness of units for labor organization representation;\n**(2)**\nsupervise or conduct elections to determine whether a labor organization has been selected as an exclusive representative by a voting majority of the employees in an appropriate unit;\n**(3)**\nresolve issues relating to the duty to bargain in good faith;\n**(4)**\nconduct hearings and resolve complaints of unfair labor practices;\n**(5)**\nresolve exceptions to the awards of arbitrators;\n**(6)**\nprotect the right of each employee to form, join, or assist any labor organization, or to refrain from any such activity, freely and without fear of penalty or reprisal, and protect each employee in the exercise of such right; and\n**(7)**\ntake such other actions as are necessary and appropriate to effectively administer this Act, including issuing subpoenas requiring the attendance and testimony of witnesses and the production of documentary or other evidence from any place in the United States, and administering oaths, taking or ordering the taking of depositions, ordering responses to written interrogatories, and receiving and examining witnesses.\n##### (c) Enforcement\n**(1) Authority to petition court**\nThe Authority may petition any United States Court of Appeals with jurisdiction over the parties, or the United States Court of Appeals for the District of Columbia Circuit, to enforce any final orders under this section, and for appropriate temporary relief or a restraining order.\n**(2) Private right of action**\nUnless the Authority has filed a petition for enforcement as provided in paragraph (1), any party has the right to file suit in any appropriate district court of the United States to enforce compliance with the regulations issued by the Authority pursuant to this section, or to enforce compliance with any order issued by the Authority pursuant to this section. The right provided by this subsection to bring a suit to enforce compliance with any order issued by the Authority pursuant to this section shall terminate upon the filing of a petition seeking the same relief by the Authority. Enforcement against a State shall be pursuant to section 8(b)(4).\n#### 6. Strikes and lockouts prohibited\n##### (a) In general\nSubject to subsection (b), an employer, public safety officer, or labor organization may not engage in a lockout, sickout, work slowdown, strike, or any other organized job action that will measurably disrupt the delivery of emergency services and is designed to compel an employer, public safety officer, or labor organization to agree to the terms of a proposed contract.\n##### (b) No preemption\nNothing in this section shall be construed to preempt any law of any State or political subdivision of any State with respect to strikes by public safety officers.\n#### 7. Existing collective bargaining units and agreements\nA certification, recognition, election-held, collective bargaining agreement, or memorandum of understanding that has been issued, approved, or ratified by any public employee relations board or commission or by any State or political subdivision or its agents and is in effect on the day before the date of enactment of this Act shall not be invalidated by the enactment of this Act.\n#### 8. Construction and compliance\n##### (a) Construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto preempt or limit the remedies, rights, and procedures of any law of any State or political subdivision of any State that provides comparable or greater rights and responsibilities than the rights and responsibilities described in section 4(b);\n**(2)**\nto prevent a State from enforcing a right-to-work law that prohibits employers and labor organizations from negotiating provisions in a labor agreement that require union membership or payment of union fees as a condition of employment;\n**(3)**\nto preempt or limit any State law in effect on the date of enactment of this Act that provides for the rights and responsibilities described in section 4(b) solely because such State law permits an employee to appear on the employee\u2019s own behalf with respect to the employee\u2019s employment relations with the public safety agency involved;\n**(4)**\nto prohibit a State from exempting from coverage under this Act a political subdivision of the State that has a population of less than 5,000 or that employs less than 25 full-time employees, including each individual employed by the political subdivision, except any individual elected by popular vote or appointed to serve on a board or commission; or\n**(5)**\nto preempt or limit the laws or ordinances of any State or political subdivision of a State that provide for the rights and responsibilities described in section 4(b) solely because such law or ordinance does not require bargaining with respect to pension, retirement, or health benefits.\n##### (b) Compliance\n**(1) Actions of states**\nNothing in this Act or the regulations promulgated under this Act shall be construed to require a State to rescind or preempt the laws or ordinances of any of the State\u2019s political subdivisions if such laws provide rights and responsibilities for public safety officers that are comparable to or greater than the rights and responsibilities described in section 4(b).\n**(2) Actions of the authority**\nNothing in this Act or the regulations promulgated under this Act shall be construed to preempt\u2014\n**(A)**\nthe laws or ordinances of any State or political subdivision of a State, if such laws provide collective bargaining rights for public safety officers that are comparable to or greater than the rights enumerated in section 4(b);\n**(B)**\nthe laws or ordinances of any State or political subdivision of a State that provide for the rights and responsibilities described in section 4(b) with respect to certain categories of public safety officers covered by this Act solely because such rights and responsibilities have not been extended to other categories of public safety officers covered by this Act; or\n**(C)**\nthe laws or ordinances of any State or political subdivision of a State that provide for the rights and responsibilities described in section 4(b), solely because such laws or ordinances provide that a contract or memorandum of understanding between a public safety employer and a labor organization must be presented to a legislative body as part of the process for approving such contract or memorandum of understanding.\n**(3) Limited enforcement power**\nIn the case of a law described in paragraph (2)(B), the Authority shall only exercise the powers provided in section 5 with respect to those categories of public safety officers who have not been afforded the rights and responsibilities described in section 4(b).\n**(4) Exclusive enforcement provision**\nNotwithstanding any other provision of the Act, and in the absence of a waiver of a State\u2019s sovereign immunity, the Authority shall have the exclusive power to enforce the provisions of this Act with respect to employees of a State.\n#### 9. Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out the provisions of this Act.",
      "versionDate": "2025-02-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Alternative dispute resolution, mediation, arbitration",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Federal Labor Relations Authority",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Fires",
            "updateDate": "2026-01-30T18:35:02Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-01-30T18:35:01Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2026-01-30T18:35:02Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2026-01-30T18:35:02Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2026-01-30T18:35:02Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-01-30T18:35:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-18T14:08:30Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1505ih.xml"
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
      "title": "Public Safety Employer-Employee Cooperation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Safety Employer-Employee Cooperation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide collective bargaining rights for public safety officers employed by States or their political subdivisions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:27Z"
    }
  ]
}
```
