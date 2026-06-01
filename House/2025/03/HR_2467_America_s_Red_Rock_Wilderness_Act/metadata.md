# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2467?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2467
- Title: America's Red Rock Wilderness Act
- Congress: 119
- Bill type: HR
- Bill number: 2467
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-05-30T08:05:49Z
- Update date including text: 2026-05-30T08:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2467",
    "number": "2467",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001218",
        "district": "1",
        "firstName": "Melanie",
        "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
        "lastName": "Stansbury",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "America's Red Rock Wilderness Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:49Z",
    "updateDateIncludingText": "2026-05-30T08:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:10:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
    },
    {
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "TN"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "ME"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MO"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CO"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OR"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-27",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-27",
      "state": "DC"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WI"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WI"
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
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CO"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NH"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CT"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "OR"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "OR"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MN"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "OR"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "WA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "HI"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "IL"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "IL"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MN"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "WA"
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
      "sponsorshipDate": "2026-02-23",
      "state": "PA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
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
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2467ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2467\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Ms. Stansbury (for herself, Ms. Tlaib , Mr. Neal , Mr. Connolly , Mr. Cohen , Ms. Brownley , Mr. Casten , Ms. Schakowsky , Ms. Pingree , Ms. DeLauro , Ms. Craig , Mr. Cleaver , Ms. DeGette , Ms. Hoyle of Oregon , Mrs. Hayes , Mr. Krishnamoorthi , Mr. Lieu , Ms. Chu , Ms. DelBene , Mr. Lynch , Mr. Smith of Washington , Mr. Garc\u00eda of Illinois , Mr. Mullin , Ms. Matsui , Ms. Norton , Ms. Moore of Wisconsin , Mr. Pocan , Ms. S\u00e1nchez , Ms. Waters , Mr. Foster , Ms. Stevens , Ms. Omar , Mr. Neguse , Mr. Huffman , Mr. Tonko , Mr. Carbajal , Ms. Meng , Mr. Beyer , Mr. Menendez , Mr. Meeks , Ms. Jayapal , and Mrs. Ramirez ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo designate as wilderness certain Federal portions of the red rock canyons of the Colorado Plateau and the Great Basin Deserts in the State of Utah for the benefit of present and future generations of people in the United States.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the America's Red Rock Wilderness Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nSec. 3. Findings.\nSec. 4. Purposes.\nTITLE I\u2014Designation of wilderness areas\nSec. 101. Great Basin Wilderness Areas.\nSec. 102. Grand Staircase-Escalante Wilderness Areas.\nSec. 103. Moab-La Sal Canyons Wilderness Areas.\nSec. 104. Henry Mountains Wilderness Areas.\nSec. 105. Glen Canyon Wilderness Areas.\nSec. 106. San Juan Wilderness Areas.\nSec. 107. Canyonlands Basin Wilderness Areas.\nSec. 108. San Rafael Swell Wilderness Areas.\nSec. 109. Book Cliffs\u2013Greater Dinosaur Wilderness Areas.\nTITLE II\u2014Administrative provisions\nSec. 201. General provisions.\nSec. 202. Administration.\nSec. 203. State school trust land within wilderness areas.\nSec. 204. Water.\nSec. 205. Roads.\nSec. 206. Livestock.\nSec. 207. Fish and wildlife.\nSec. 208. Protection of Tribal rights.\nSec. 209. Management of newly acquired land.\nSec. 210. Withdrawal.\n#### 2. Definitions\nIn this Act:\n**(1) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Bureau of Land Management.\n**(2) State**\nThe term State means the State of Utah.\n#### 3. Findings\nCongress finds that\u2014\n**(1)**\nthe land designated as wilderness by this Act is one of the largest remaining expanses of unprotected, wild public land in the continental United States;\n**(2)**\nthe designation of wilderness by this Act would\u2014\n**(A)**\nincrease landscape connectivity in the Colorado Plateau; and\n**(B)**\nhelp to mitigate the impacts of climate change by\u2014\n**(i)**\nproviding critical refugia;\n**(ii)**\nreducing surface disturbances that exacerbate the impacts of climate change;\n**(iii)**\nreducing greenhouse gas emissions related to the extraction and use of fossil fuels; and\n**(iv)**\ncontributing to the goal of protecting 30 percent of global land and waters by 2030;\n**(3)**\nthe land designated as wilderness by this Act is\u2014\n**(A)**\na living cultural landscape;\n**(B)**\na place of refuge for wild nature; and\n**(C)**\nan important part of Indigenous and non-Indigenous community values;\n**(4)**\nIndian Tribes have been present on the land designated as wilderness by this Act since time immemorial, using the plant, animal, landform, and spiritual values for sustenance and cultural, medicinal, and ceremonial activities, purposes for which Indigenous people continue to use the land; and\n**(5)**\nthe designation of wilderness by this Act\u2014\n**(A)**\nis vital to the continuation and revitalization of Indigenous cultures; and\n**(B)**\nserves to protect places of Indigenous use and sanctuary.\n#### 4. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto designate as wilderness certain Federal portions of the red rock canyons of the Colorado Plateau and the Great Basin Deserts in the State of Utah for the benefit of present and future generations of people in the United States;\n**(2)**\nto protect the cultural, ecological, and scenic values of land designated as wilderness by this Act for the benefit, use, and enjoyment of present and future generations of people in the United States; and\n**(3)**\nto protect the ability of Indigenous and non-Indigenous people to use the land designated as wilderness by this Act for traditional activities, including hunting, fishing, hiking, horsepacking, camping, and spirituality as people have used the land for generations.\nI\nDesignation of wilderness areas\n#### 101. Great Basin Wilderness Areas\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe Great Basin region of western Utah is comprised of starkly beautiful mountain ranges that rise as islands from the desert floor;\n**(2)**\nthe Wah Wah Mountains in the Great Basin region are arid and austere, with massive cliff faces and leathery slopes speckled with pi\u00f1on and juniper;\n**(3)**\nthe Pilot Range and Stansbury Mountains in the Great Basin region are high enough to draw moisture from passing clouds and support ecosystems found nowhere else on earth;\n**(4)**\nfrom bristlecone pine, the world\u2019s oldest living organism, to newly flowered mountain meadows, mountains of the Great Basin region are islands of nature that\u2014\n**(A)**\nsupport remarkable biological diversity; and\n**(B)**\nprovide opportunities to experience the colossal silence of the Great Basin; and\n**(5)**\nthe Great Basin region of western Utah should be protected and managed to ensure the preservation of the natural conditions of the region.\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(1)**\nBald Eagle Mountain (approximately 9,000 acres).\n**(2)**\nBarn Hills (approximately 21,000 acres).\n**(3)**\nBig Hollow (approximately 4,000 acres).\n**(4)**\nBlack Hills (approximately 8,750 acres).\n**(5)**\nBroken Ridge (approximately 9,250 acres).\n**(6)**\nBullgrass Knoll (approximately 15,750 acres).\n**(7)**\nBurbank Hills (approximately 17,000 acres).\n**(8)**\nBurbank Pass (approximately 30,000 acres).\n**(9)**\nChalk Knolls (approximately 16,500 acres).\n**(10)**\nCobb Peak (approximately 8,500 acres).\n**(11)**\nConger Mountain (approximately 21,750 acres).\n**(12)**\nCrater Bench (approximately 35,000 acres).\n**(13)**\nCrater Island East (approximately 53,000 acres).\n**(14)**\nCrater Island West (approximately 30,000 acres).\n**(15)**\nCricket Mountain (approximately 16,500 acres).\n**(16)**\nCrook Creek (approximately 20,000 acres).\n**(17)**\nDeep Creek Mountains (approximately 127,000 acres).\n**(18)**\nDisappointment Hills (approximately 24,000 acres).\n**(19)**\nDrum Mountains (approximately 14,500 acres).\n**(20)**\nDugway Mountains (approximately 24,500 acres).\n**(21)**\nFish Springs Range (approximately 65,000 acres).\n**(22)**\nGranite Mountain (approximately 19,250 acres).\n**(23)**\nGranite Peak (approximately 19,500 acres).\n**(24)**\nGrassy Mountains North (approximately 8,500 acres).\n**(25)**\nGrassy Mountains South (approximately 16,500 acres).\n**(26)**\nHamlin (approximately 13,750 acres).\n**(27)**\nHeadlight Mountain (approximately 6,000 acres).\n**(28)**\nHowell Peak (approximately 28,750 acres).\n**(29)**\nIndian Peaks (approximately 15,750 acres).\n**(30)**\nJackson Wash (approximately 18,500 acres).\n**(31)**\nJuniper (approximately 17,500 acres).\n**(32)**\nKeg Mountains East (approximately 19,500 acres).\n**(33)**\nKeg Mountains West (approximately 19,250 acres).\n**(34)**\nKern Mountains (approximately 15,000 acres).\n**(35)**\nKing Top (approximately 111,500 acres).\n**(36)**\nLedger Canyon (approximately 9,000 acres).\n**(37)**\nLion Peak (approximately 27,500 acres).\n**(38)**\nLittle Drum Mountains North (approximately 14,000 acres).\n**(39)**\nLittle Drum Mountains South (approximately 10,000 acres).\n**(40)**\nMahogany Peak (approximately 750 acres).\n**(41)**\nMiddle Burbank Hills (approximately 6,750 acres).\n**(42)**\nMiddle Mountains (approximately 39,750 acres).\n**(43)**\nMount Escalante (approximately 17,500 acres).\n**(44)**\nMountain Home Range North (approximately 21,500 acres).\n**(45)**\nMountain Home Range South (approximately 32,750 acres).\n**(46)**\nNeedle Mountains (approximately 12,000 acres).\n**(47)**\nNewfoundland Mountains (approximately 24,500 acres).\n**(48)**\nNorth Peaks (approximately 9,500 acres).\n**(49)**\nNorth Stansbury Mountains (approximately 20,500 acres).\n**(50)**\nNotch Peak (approximately 72,000 acres).\n**(51)**\nNotch View (approximately 8,000 acres).\n**(52)**\nOchre Mountain (approximately 13,500 acres).\n**(53)**\nOquirrh Mountains (approximately 9,000 acres).\n**(54)**\nOrr Ridge (approximately 11,000 acres).\n**(55)**\nPainted Rock (approximately 26,500 acres).\n**(56)**\nParadise Mountain (approximately 40,000 acres).\n**(57)**\nPilot Mountains Central (approximately 8,000 acres).\n**(58)**\nPilot Peak (approximately 30,250 acres).\n**(59)**\nRed Canyon (approximately 15,500 acres).\n**(60)**\nRed Tops (approximately 28,000 acres).\n**(61)**\nSan Francisco Mountains (approximately 39,750 acres).\n**(62)**\nSilver Island Mountains (approximately 37,500 acres).\n**(63)**\nSnake Valley (approximately 66,250 acres).\n**(64)**\nSpring Creek Canyon (approximately 5,250 acres).\n**(65)**\nStansbury Island (approximately 10,000 acres).\n**(66)**\nSteamboat Mountain (approximately 40,250 acres).\n**(67)**\nSwasey Peak (approximately 91,000 acres).\n**(68)**\nThe Toad (approximately 11,250 acres).\n**(69)**\nThomas Range (approximately 40,500 acres).\n**(70)**\nTule Valley (approximately 102,000 acres).\n**(71)**\nTule Valley South (approximately 19,000 acres).\n**(72)**\nTunnel Springs (approximately 23,000 acres).\n**(73)**\nWah Wah Mountains Central (approximately 6,750 acres).\n**(74)**\nWah Wah Mountains North (approximately 93,500 acres).\n**(75)**\nWah Wah Mountains South (approximately 17,750 acres).\n**(76)**\nWhite Rock Range (approximately 5,000 acres).\n**(77)**\nWild Horse Pass (approximately 35,750 acres).\n#### 102. Grand Staircase-Escalante Wilderness Areas\n##### (a) Grand Staircase area\n**(1) Findings**\nCongress finds that\u2014\n**(A)**\nthe area known as the Grand Staircase rises more than 6,000 feet in a series of great cliffs and plateaus from the depths of the Grand Canyon to the forested rim of Bryce Canyon;\n**(B)**\nthe Grand Staircase\u2014\n**(i)**\nspans 6 major life zones, from the lower Sonoran Desert to the alpine forest; and\n**(ii)**\nencompasses geologic formations that display 3,000,000,000 years of Earth\u2019s history;\n**(C)**\nland managed by the Secretary forms a vital natural corridor connecting the deserts and forests of the surrounding landscape, which includes Grand Canyon National Park and Bryce Canyon National Park;\n**(D)**\neach of the areas described in paragraph (2) (other than East of Bryce, Moquith Mountain, Bunting Point, Canaan Mountain, Orderville Canyon, Parunuweap Canyon, Vermillion Cliffs, and the majority of Upper Kanab Creek) is located within the Grand Staircase-Escalante National Monument, as established in 1996; and\n**(E)**\nthe Grand Staircase in Utah should be protected and managed as a wilderness area.\n**(2) Designation**\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(A)**\nBryce Boot (approximately 2,750 acres).\n**(B)**\nBryce View (approximately 4,500 acres).\n**(C)**\nBunting Point (approximately 11,500 acres).\n**(D)**\nCanaan Mountain (approximately 15,250 acres).\n**(E)**\nEast of Bryce (approximately 750 acres).\n**(F)**\nGlass Eye Canyon (approximately 25,500 acres).\n**(G)**\nLadder Canyon (approximately 14,500 acres).\n**(H)**\nMoquith Mountain (approximately 15,750 acres).\n**(I)**\nNephi Point (approximately 14,750 acres).\n**(J)**\nOrderville Canyon (approximately 8,000 acres).\n**(K)**\nParia-Hackberry (approximately 196,000 acres).\n**(L)**\nParia Wilderness Expansion (approximately 4,000 acres).\n**(M)**\nParunuweap Canyon (approximately 44,500 acres).\n**(N)**\nPine Hollow (approximately 11,000 acres).\n**(O)**\nTimber Mountain (approximately 52,750 acres).\n**(P)**\nUpper Kanab Creek (approximately 51,000 acres).\n**(Q)**\nVermillion Cliffs (approximately 25,000 acres).\n**(R)**\nWillis Creek (approximately 22,000 acres).\n##### (b) Kaiparowits Plateau\n**(1) Findings**\nCongress finds that\u2014\n**(A)**\nthe Kaiparowits Plateau east of the Paria River is one of the most rugged and isolated wilderness regions in the United States;\n**(B)**\nthe Kaiparowits Plateau, a windswept land of harsh beauty, contains distant vistas and a remarkable variety of plant and animal species;\n**(C)**\nancient forests, an abundance of big game animals, and 22 species of raptors thrive undisturbed on the grassland mesa tops of the Kaiparowits Plateau;\n**(D)**\neach of the areas described in paragraph (2) (other than Heaps Canyon, Little Valley, and Wide Hollow) is located within the Grand Staircase-Escalante National Monument, as established in 1996; and\n**(E)**\nthe Kaiparowits Plateau should be protected and managed as a wilderness area.\n**(2) Designation**\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(A)**\nAndalex Not (approximately 18,000 acres).\n**(B)**\nBox Canyon (approximately 3,000 acres).\n**(C)**\nBurning Hills (approximately 81,500 acres).\n**(D)**\nCanaan Peak Slopes (approximately 2,500 acres).\n**(E)**\nCarcass Canyon (approximately 84,750 acres).\n**(F)**\nFiftymile Bench (approximately 12,750 acres).\n**(G)**\nFiftymile Mountain (approximately 207,000 acres).\n**(H)**\nHeaps Canyon (approximately 4,000 acres).\n**(I)**\nHorse Spring Canyon (approximately 32,000 acres).\n**(J)**\nKodachrome Headlands (approximately 9,750 acres).\n**(K)**\nLittle Valley Canyon (approximately 4,000 acres).\n**(L)**\nMud Spring Canyon (approximately 65,750 acres).\n**(M)**\nNipple Bench (approximately 31,750 acres).\n**(N)**\nParadise Canyon-Wahweap (approximately 266,500 acres).\n**(O)**\nRock Cove (approximately 17,000 acres).\n**(P)**\nThe Blues (approximately 22,000 acres).\n**(Q)**\nThe Cockscomb (approximately 11,750 acres).\n**(R)**\nWarm Creek (approximately 24,000 acres).\n**(S)**\nWide Hollow (approximately 7,750 acres).\n##### (c) Escalante Canyons\n**(1) Findings**\nCongress finds that\u2014\n**(A)**\nglens and coves carved in massive sandstone cliffs, spring-watered hanging gardens, and the silence of ancient ruins are examples of the unique features that entice hikers, campers, and sightseers from around the world to the Escalante Canyons;\n**(B)**\nthe Escalante Canyons link the spruce fir forests of the 11,000-foot Aquarius Plateau with the winding slickrock canyons that flow into Glen Canyon;\n**(C)**\nthe Escalante Canyons, one of Utah\u2019s most popular natural areas, contains critical habitat for deer, elk, and wild bighorn sheep that also enhances the scenic integrity of the area;\n**(D)**\neach of the areas described in paragraph (2) is located within the Grand Staircase-Escalante National Monument, as established in 1996; and\n**(E)**\nthe Escalante Canyons should be protected and managed as a wilderness area.\n**(2) Designation**\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(A)**\nColt Mesa (approximately 28,250 acres).\n**(B)**\nDeath Hollow (approximately 49,750 acres).\n**(C)**\nForty Mile Gulch (approximately 7,500 acres).\n**(D)**\nLampstand (approximately 11,500 acres).\n**(E)**\nMuley Twist Flank (approximately 3,750 acres).\n**(F)**\nNorth Escalante Canyons (approximately 182,000 acres).\n**(G)**\nPioneer Mesa (approximately 11,000 acres).\n**(H)**\nScorpion (approximately 61,250 acres).\n**(I)**\nSooner Bench (approximately 500 acres).\n**(J)**\nSteep Creek (approximately 35,750 acres).\n**(K)**\nStudhorse Peaks (approximately 24,000 acres).\n#### 103. Moab-La Sal Canyons Wilderness Areas\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe canyons surrounding the La Sal Mountains and the town of Moab offer a variety of extraordinary landscapes;\n**(2)**\noutstanding examples of natural formations and landscapes in the Moab-La Sal Canyons area include the huge sandstone fins of Behind the Rocks, the mysterious Fisher Towers, and the whitewater rapids of Westwater Canyon; and\n**(3)**\nthe Moab-La Sal Canyons should be protected and managed as a wilderness area.\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(1)**\nArches National Park Adjacents (approximately 8,600 acres).\n**(2)**\nBeaver Creek (approximately 45,000 acres).\n**(3)**\nBehind the Rocks (approximately 19,500 acres).\n**(4)**\nBig Triangle (approximately 21,500 acres).\n**(5)**\nCoyote Wash (approximately 27,000 acres).\n**(6)**\nDome Plateau (approximately 36,750 acres).\n**(7)**\nFisher Towers (approximately 19,000 acres).\n**(8)**\nGoldbar Canyon (approximately 9,500 acres).\n**(9)**\nGranite Creek (approximately 5,000 acres).\n**(10)**\nHunter Canyon (approximately 5,500 acres).\n**(11)**\nMary Jane Canyon (approximately 28,500 acres).\n**(12)**\nMill Creek (approximately 17,250 acres).\n**(13)**\nMorning Glory (approximately 11,000 acres).\n**(14)**\nPorcupine Rim (approximately 10,500 acres).\n**(15)**\nRenegade Point (approximately 6,250 acres).\n**(16)**\nWestwater Canyon (approximately 39,000 acres).\n**(17)**\nYellow Bird (approximately 4,500 acres).\n#### 104. Henry Mountains Wilderness Areas\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe Henry Mountain Range, the last mountain range to be discovered and named by early explorers in the contiguous United States, still retains a wild and undiscovered quality;\n**(2)**\nfluted badlands that surround the flanks of 11,000-foot Mounts Ellen and Pennell contain areas of critical habitat for mule deer and for the largest herd of free-roaming buffalo in the United States;\n**(3)**\ndespite their relative accessibility, the Henry Mountain Range remains one of the wildest, least-known ranges in the United States; and\n**(4)**\nthe Henry Mountain Range should be protected and managed to ensure the preservation of the range as a wilderness area.\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(1)**\nBull Mountain (approximately 16,000 acres).\n**(2)**\nBullfrog Creek (approximately 42,000 acres).\n**(3)**\nDogwater Creek (approximately 5,000 acres).\n**(4)**\nFremont Gorge (approximately 22,000 acres).\n**(5)**\nLong Canyon (approximately 16,500 acres).\n**(6)**\nMount Ellen-Blue Hills (approximately 14,750 acres).\n**(7)**\nMount Hillers (approximately 20,250 acres).\n**(8)**\nMount Pennell (approximately 155,500 acres).\n**(9)**\nNotom Bench (approximately 6,250 acres).\n**(10)**\nRagged Mountain (approximately 29,250 acres).\n#### 105. Glen Canyon Wilderness Areas\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe side canyons of Glen Canyon, including the Dirty Devil River and the Red, White and Blue Canyons, contain some of the most remote and outstanding landscapes in southern Utah;\n**(2)**\nthe Dirty Devil River, once the fortress hideout of outlaw Butch Cassidy\u2019s Wild Bunch, has sculpted a maze of slickrock canyons through an imposing landscape of monoliths and inaccessible mesas;\n**(3)**\nthe Red and Blue Canyons contain colorful Chinle/Moenkopi badlands found nowhere else in the region;\n**(4)**\nDark Canyon, Fort Knocker, Tuwa Canyon, Upper Red Canyon, White Canyon, and a portion of Red Rock Plateau are located within the Bears Ears National Monument, as established in 2016; and\n**(5)**\nthe canyons of Glen Canyon in the State should be protected and managed as wilderness areas.\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(1)**\nCane Spring Desert (approximately 18,250 acres).\n**(2)**\nCopper Point (approximately 4,500 acres).\n**(3)**\nDark Canyon (approximately 139,000 acres).\n**(4)**\nDirty Devil (approximately 245,000 acres).\n**(5)**\nFiddler Butte (approximately 93,000 acres).\n**(6)**\nFlat Tops (approximately 29,750 acres).\n**(7)**\nFort Knocker (approximately 12,500 acres).\n**(8)**\nLittle Rockies (approximately 64,000 acres).\n**(9)**\nPleasant Creek Bench (approximately 1,000 acres).\n**(10)**\nRed Rock Plateau (approximately 185,500 acres).\n**(11)**\nThe Needle (approximately 10,750 acres).\n**(12)**\nTuwa Canyon (approximately 9,750 acres).\n**(13)**\nUpper Red Canyon (approximately 25,000 acres).\n**(14)**\nWhite Canyon (approximately 78,000 acres).\n#### 106. San Juan Wilderness Areas\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nmore than 1,000 years ago, Indigenous culture flourished in the slickrock canyons and on the pi\u00f1on-covered mesas of southeastern Utah;\n**(2)**\nevidence of the presence of Indigenous people pervades the Cedar Mesa area of the San Juan area where cliff dwellings, rock art, and ceremonial kivas are found in sandstone overhangs and isolated benchlands;\n**(3)**\nthe Cedar Mesa area is in need of protection from the vandalism and theft of its unique cultural resources;\n**(4)**\nthe Cedar Mesa wilderness areas should be created to protect both the archaeological heritage and the extraordinary wilderness, scenic, and ecological values of the United States;\n**(5)**\neach of the areas described in subsection (b) (other than Cross Canyon, Monument Canyon, Tin Cup Mesa, and most of Nokai Dome and San Juan River) are located within the Bears Ears National Monument, as established in 2016; and\n**(6)**\nthe San Juan area should be protected and managed as a wilderness area to ensure the preservation of the unique and valuable resources of that area.\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(1)**\nAllen Canyon (approximately 6,500 acres).\n**(2)**\nArch Canyon (approximately 30,500 acres).\n**(3)**\nComb Ridge (approximately 16,000 acres).\n**(4)**\nCross Canyon (approximately 2,500 acres).\n**(5)**\nFish and Owl Creek Canyons (approximately 74,000 acres).\n**(6)**\nGrand Gulch (approximately 161,250 acres).\n**(7)**\nHammond Canyon (approximately 4,750 acres).\n**(8)**\nLime Creek (approximately 5,500 acres).\n**(9)**\nMonument Canyon (approximately 18,000 acres).\n**(10)**\nNokai Dome (approximately 94,250 acres).\n**(11)**\nRoad Canyon (approximately 64,000 acres).\n**(12)**\nSan Juan River (approximately 14,750 acres).\n**(13)**\nThe Tabernacle (approximately 7,250 acres).\n**(14)**\nTin Cup Mesa (approximately 26,000 acres).\n**(15)**\nValley of the Gods (approximately 14,500 acres).\n#### 107. Canyonlands Basin Wilderness Areas\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nCanyonlands National Park safeguards only a small portion of the extraordinary red-hued, cliff-walled canyonland region of the Colorado Plateau;\n**(2)**\nareas near Canyonlands National Park contain canyons with rushing perennial streams, natural arches, bridges, and towers;\n**(3)**\nthe gorges of the Green and Colorado Rivers lie on adjacent land managed by the Secretary;\n**(4)**\npopular overlooks in Canyonlands National Park and Dead Horse Point State Park have views directly into adjacent areas, including Lockhart Basin and Indian Creek;\n**(5)**\neach of the areas described in subsection (b) (other than Dead Horse Cliffs, Horsethief Point, Labyrinth Canyon Wilderness Expansion, San Rafael River, Sweetwater Reef, and a portion of Gooseneck) are located within the Bears Ears National Monument, as established in 2016; and\n**(6)**\ndesignation of those areas as wilderness would ensure the protection of this erosional masterpiece of nature and of the rich pockets of wildlife found within its expanded boundaries.\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(1)**\nBridger Jack Mesa (approximately 33,500 acres).\n**(2)**\nButler Wash (approximately 27,000 acres).\n**(3)**\nDead Horse Cliffs (approximately 5,250 acres).\n**(4)**\nDemon\u2019s Playground (approximately 3,6500 acres).\n**(5)**\nGooseneck (approximately 9,500 acres).\n**(6)**\nHatch Point/Lockhart Basin/Harts Point (approximately 150,500 acres).\n**(7)**\nHorsethief Point (approximately 15,500 acres).\n**(8)**\nIndian Creek (approximately 28,500 acres).\n**(9)**\nLabyrinth Canyon Wilderness Expansion (approximately158,750 acres).\n**(10)**\nSan Rafael River (approximately 97,250 acres).\n**(11)**\nShay Mountain (approximately 15,500 acres).\n**(12)**\nSweetwater Reef (approximately 69,250 acres).\n#### 108. San Rafael Swell Wilderness Areas\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe San Rafael Swell towers above the desert like a castle, ringed by 1,000-foot ramparts of Navajo Sandstone;\n**(2)**\nthe highlands of the San Rafael Swell have been fractured by uplift and rendered hollow by erosion over countless millennia, leaving a tremendous basin punctuated by mesas, buttes, and canyons and traversed by sediment-laden desert streams;\n**(3)**\nthe mountains within these areas are among Utah\u2019s most valuable habitat for desert bighorn sheep; and\n**(4)**\nthe San Rafael Swell area should be protected and managed to ensure its preservation as a wilderness area.\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(1)**\nCapitol Reef National Park Adjacents (approximately 9,000 acres).\n**(2)**\nCedar Mountain (approximately 15,250 acres).\n**(3)**\nDevils Canyon Wilderness Expansion (approximately 14,500 acres).\n**(4)**\nEagle Canyon (approximately 39,000 acres).\n**(5)**\nFactory Butte (approximately 22,250 acres).\n**(6)**\nHondu Country Wilderness Expansion (approximately 3,000 acres).\n**(7)**\nJones Bench (approximately 3,500 acres).\n**(8)**\nLimestone Cliffs (approximately 25,500 acres).\n**(9)**\nLost Spring Wash (approximately 36,500 acres).\n**(10)**\nMexican Mountain Wilderness Expansion (approximately 29,750 acres).\n**(11)**\nMolen Reef (approximately 32,500 acres).\n**(12)**\nMuddy Creek Wilderness Expansion (approximately 85,000 acres).\n**(13)**\nMussentuchit Badlands (approximately 25,000 acres).\n**(14)**\nPrice River-Humbug (approximately 122,250 acres).\n**(15)**\nRed Desert (approximately 30,750 acres).\n**(16)**\nRock Canyon (approximately 17,750 acres).\n**(17)**\nSan Rafael Knob (approximately 16,750 acres).\n**(18)**\nSan Rafael Reef Wilderness Expansion (approximately 60,750 acres).\n**(19)**\nSids Mountain Wilderness Expansion (approximately 39,250 acres).\n**(20)**\nUpper Muddy Creek (approximately 18,500 acres).\n**(21)**\nWild Horse Mesa Wilderness Expansion (approximately 56,000 acres).\n#### 109. Book Cliffs\u2013Greater Dinosaur Wilderness Areas\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe Book Cliffs\u2013Greater Dinosaur Wilderness Areas offer\u2014\n**(A)**\nunique big game hunting opportunities in verdant high-plateau forests; and\n**(B)**\nthe opportunity for float trips of several days duration down the Green River in Desolation Canyon;\n**(2)**\nthe long rampart of the Book Cliffs bounds the area on the south, while the uplands, plateaus, rivers, and canyons of the Greater Dinosaur area provide connectivity with Dinosaur National Monument and the northernmost extent of the Colorado Plateau;\n**(3)**\nbears, bighorn sheep, cougars, elk, and mule deer flourish in the backcountry of the Book Cliffs; and\n**(4)**\nthe Book Cliffs\u2013Greater Dinosaur Wilderness Areas should be protected and managed to ensure the protection of the areas as wilderness.\n##### (b) Designation\nIn accordance with the Wilderness Act ( 16 U.S.C. 1131 et seq. ), the following areas in the State are designated as wilderness areas and as components of the National Wilderness Preservation System:\n**(1)**\nBad Land Cliffs (approximately 11,500 acres).\n**(2)**\nBeach Draw (approximately 1,000 acres).\n**(3)**\nBourdette Draw (approximately 15,750 acres).\n**(4)**\nBull Canyon (approximately 3,000 acres).\n**(5)**\nDead Horse Pass (approximately 8,500 acres).\n**(6)**\nDesbrough Canyon (approximately 14,000 acres).\n**(7)**\nDesolation Canyon Wilderness Expansion (approximately 293,500 acres).\n**(8)**\nDiamond Breaks (approximately 8,600 acres).\n**(9)**\nDiamond Canyon (approximately 168,000 acres).\n**(10)**\nDiamond Mountain (approximately 30,500 acres).\n**(11)**\nGoslin Mountain (approximately 3,750 acres).\n**(12)**\nHideout Canyon (approximately 12,750 acres).\n**(13)**\nLower Flaming Gorge (approximately 21,000 acres).\n**(14)**\nMexico Point (approximately 14,750 acres).\n**(15)**\nMoonshine Draw (approximately 10,750 acres).\n**(16)**\nMountain Home (approximately 8,000 acres).\n**(17)**\nO-Wi-Yu-Kuts (approximately 14,500 acres).\n**(18)**\nRed Creek Badlands (approximately 4500 acres).\n**(19)**\nSplit Mountain Benches (approximately 2,750 acres).\n**(20)**\nStone Bridge Draw (approximately 3,500 acres).\n**(21)**\nStuntz Draw (approximately 2,000 acres).\n**(22)**\nSurvey Point (approximately 8,750 acres).\n**(23)**\nTurtle Canyon Wilderness Expansion (approximately 7,500 acres).\n**(24)**\nVivas Cake Hill (approximately 250 acres).\n**(25)**\nWild Mountain (approximately 750 acres).\nII\nAdministrative provisions\n#### 201. General provisions\n##### (a) Names of wilderness areas\nEach wilderness area named in title I shall\u2014\n**(1)**\nconsist of the quantity of land referenced with respect to that named area, as generally depicted on the map entitled America\u2019s Red Rock Wilderness Act, 118th Congress ; and\n**(2)**\nbe known by the name given to it in title I.\n##### (b) Map and description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall file a map and a legal description of each wilderness area designated by this Act with\u2014\n**(A)**\nthe Committee on Natural Resources of the House of Representatives; and\n**(B)**\nthe Committee on Energy and Natural Resources of the Senate.\n**(2) Force of law**\nA map and legal description filed under paragraph (1) shall have the same force and effect as if included in this Act, except that the Secretary may correct clerical and typographical errors in the map and legal description.\n**(3) Public availability**\nEach map and legal description filed under paragraph (1) shall be filed and made available for public inspection in the Office of the Director of the Bureau of Land Management.\n#### 202. Administration\nSubject to valid rights in existence on the date of enactment of this Act, each wilderness area designated under this Act shall be administered by the Secretary in accordance with\u2014\n**(1)**\nthe Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); and\n**(2)**\nthe Wilderness Act ( 16 U.S.C. 1131 et seq. ).\n#### 203. State school trust land within wilderness areas\n##### (a) In general\nSubject to subsection (b), if State-owned land is included in an area designated by this Act as a wilderness area, the Secretary shall offer to exchange land owned by the United States in the State of approximately equal value in accordance with section 603(c) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1782(c) ) and section 5(a) of the Wilderness Act ( 16 U.S.C. 1134(a) ).\n##### (b) Mineral interests\nThe Secretary shall not transfer any mineral interests under subsection (a) unless the State transfers to the Secretary any mineral interests in land designated by this Act as a wilderness area.\n#### 204. Water\n##### (a) Reservation\n**(1) Water for wilderness areas**\n**(A) In general**\nWith respect to each wilderness area designated by this Act, Congress reserves a quantity of water determined by the Secretary to be sufficient for the wilderness area.\n**(B) Priority date**\nThe priority date of a right reserved under subparagraph (A) shall be the date of enactment of this Act.\n**(2) Protection of rights**\nThe Secretary and other officers and employees of the United States shall take any steps necessary to protect the rights reserved by paragraph (1)(A), including the filing of a claim for the quantification of the rights in any present or future appropriate stream adjudication in the courts of the State\u2014\n**(A)**\nin which the United States is or may be joined; and\n**(B)**\nthat is conducted in accordance with section 208 of the Department of Justice Appropriation Act, 1953 (66 Stat. 560, chapter 651).\n##### (b) Prior rights not affected\nNothing in this Act relinquishes or reduces any water rights reserved or appropriated by the United States in the State on or before the date of enactment of this Act.\n##### (c) Administration\n**(1) Specification of rights**\nThe Federal water rights reserved by this Act are specific to the wilderness areas designated by this Act.\n**(2) No precedent established**\nNothing in this Act related to reserved Federal water rights\u2014\n**(A)**\nshall establish a precedent with regard to any future designation of water rights; or\n**(B)**\nshall affect the interpretation of any other Act or any designation made under any other Act.\n#### 205. Roads\n##### (a) Setbacks\n**(1) Measurement in general**\nA setback under this section shall be measured from the center line of the road.\n**(2) Wilderness on 1 side of roads**\nExcept as provided in subsection (b), a setback for a road with wilderness on only 1 side shall be set at\u2014\n**(A)**\n300 feet from a paved Federal or State highway;\n**(B)**\n100 feet from any other paved road or high standard dirt or gravel road; and\n**(C)**\n30 feet from any other road.\n**(3) Wilderness on both sides of roads**\nExcept as provided in subsection (b), a setback for a road with wilderness on both sides (including cherry-stems or roads separating 2 wilderness units) shall be set at\u2014\n**(A)**\n200 feet from a paved Federal or State highway;\n**(B)**\n40 feet from any other paved road or high standard dirt or gravel road; and\n**(C)**\n10 feet from any other roads.\n##### (b) Setback exceptions\n**(1) Well-defined topographical barriers**\nIf, between the road and the boundary of a setback area described in paragraph (2) or (3) of subsection (a), there is a well-defined cliff edge, stream bank, or other topographical barrier, the Secretary shall use the barrier as the wilderness boundary.\n**(2) Fences**\nIf, between the road and the boundary of a setback area specified in paragraph (2) or (3) of subsection (a), there is a fence running parallel to a road, the Secretary shall use the fence as the wilderness boundary if, in the opinion of the Secretary, doing so would result in a more manageable boundary.\n**(3) Deviations from setback areas**\n**(A) Exclusion of disturbances from wilderness boundaries**\nIn cases where there is an existing livestock development, dispersed camping area, borrow pit, or similar disturbance within 100 feet of a road that forms part of a wilderness boundary, the Secretary may delineate the boundary so as to exclude the disturbance from the wilderness area.\n**(B) Limitation on exclusion of disturbances**\nThe Secretary shall make a boundary adjustment under subparagraph (A) only if the Secretary determines that doing so is consistent with wilderness management goals.\n**(C) Deviations restricted to minimum necessary**\nAny deviation under this paragraph from the setbacks required under in paragraph (2) or (3) of subsection (a) shall be the minimum necessary to exclude the disturbance.\n##### (c) Delineation within setback area\nThe Secretary may delineate a wilderness boundary at a location within a setback under paragraph (2) or (3) of subsection (a) if, as determined by the Secretary, the delineation would enhance wilderness management goals.\n#### 206. Livestock\nWithin the wilderness areas designated under title I, the grazing of livestock authorized on the date of enactment of this Act shall be permitted to continue subject to such reasonable regulations and procedures as the Secretary considers necessary, as long as the regulations and procedures are consistent with\u2014\n**(1)**\nthe Wilderness Act ( 16 U.S.C. 1131 et seq. ); and\n**(2)**\nsection 101(f) of the Arizona Desert Wilderness Act of 1990 ( Public Law 101\u2013628 ; 104 Stat. 4469).\n#### 207. Fish and wildlife\nNothing in this Act affects the jurisdiction of the State with respect to wildlife and fish on the public land located in the State.\n#### 208. Protection of Tribal rights\nNothing in this Act affects or modifies\u2014\n**(1)**\nany right of any federally recognized Indian Tribe; or\n**(2)**\nany obligation of the United States to any federally recognized Indian Tribe.\n#### 209. Management of newly acquired land\nAny land within the boundaries of a wilderness area designated under this Act that is acquired by the Federal Government shall\u2014\n**(1)**\nbecome part of the wilderness area in which the land is located; and\n**(2)**\nbe managed in accordance with this Act and other laws applicable to wilderness areas.\n#### 210. Withdrawal\nSubject to valid rights existing on the date of enactment of this Act, the Federal land referred to in title I is withdrawn from all forms of\u2014\n**(1)**\nentry, appropriation, or disposal under public law;\n**(2)**\nlocation, entry, and patent under mining law; and\n**(3)**\ndisposition under all laws pertaining to mineral and geothermal leasing or mineral materials.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-27",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S1908-1912)"
      },
      "number": "1193",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "America\u2019s Red Rock Wilderness Act",
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
            "name": "Land transfers",
            "updateDate": "2026-03-03T20:24:16Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-03-03T20:24:16Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-03-03T20:24:16Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2026-03-03T20:24:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T18:56:38Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2467ih.xml"
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
      "title": "America's Red Rock Wilderness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "America's Red Rock Wilderness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate as wilderness certain Federal portions of the red rock canyons of the Colorado Plateau and the Great Basin Deserts in the State of Utah for the benefit of present and future generations of people in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T02:48:17Z"
    }
  ]
}
```
