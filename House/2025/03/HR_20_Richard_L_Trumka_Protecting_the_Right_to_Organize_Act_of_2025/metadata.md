# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/20?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/20
- Title: Richard L. Trumka Protecting the Right to Organize Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 20
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-04-29T08:07:09Z
- Update date including text: 2026-04-29T08:07:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/20",
    "number": "20",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S000185",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
        "lastName": "Scott",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Richard L. Trumka Protecting the Right to Organize Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-29T08:07:09Z",
    "updateDateIncludingText": "2026-04-29T08:07:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:00:10Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "OH"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WI"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
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
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NV"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
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
      "sponsorshipDate": "2025-03-05",
      "state": "MA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "MA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MS"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IN"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OH"
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
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "KY"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "IN"
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
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "DE"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
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
      "sponsorshipDate": "2025-03-05",
      "state": "ME"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WI"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
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
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
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
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "NM"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MN"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
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
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "MN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "HI"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OH"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
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
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NV"
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
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "MA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
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
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OH"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "J000294",
      "district": "8",
      "firstName": "Hakeem",
      "fullName": "Rep. Jeffries, Hakeem S. [D-NY-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Jeffries",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "MN"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "ME"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "RI"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MO"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MN"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "HI"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "KS"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
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
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "RI"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "C001101",
      "district": "5",
      "firstName": "Katherine",
      "fullName": "Rep. Clark, Katherine M. [D-MA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Clark",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MO"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "VT"
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
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
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
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NV"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OH"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "MA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NH"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "A000371",
      "district": "33",
      "firstName": "Pete",
      "fullName": "Rep. Aguilar, Pete [D-CA-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Aguilar",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NM"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NM"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NH"
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
      "sponsorshipDate": "2025-03-05",
      "state": "VI"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "TN"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CA"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
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
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    },
    {
      "bioguideId": "M001246",
      "district": "11",
      "firstName": "Analilia",
      "fullName": "Rep. Mejia, Analilia [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Mejia",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr20ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 20\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Scott of Virginia (for himself, Mr. Fitzpatrick , Ms. Brown , Ms. Moore of Wisconsin , Ms. Williams of Georgia , Ms. Norton , Ms. Tlaib , Mr. Bishop , Mrs. McIver , Ms. Titus , Ms. Bonamici , Mr. Keating , Mr. McGovern , Mr. Thompson of Mississippi , Ms. Lofgren , Ms. DeLauro , Ms. Ansari , Mr. Mrvan , Mr. Garamendi , Ms. Budzinski , Ms. Kaptur , Mrs. Ramirez , Ms. Johnson of Texas , Mr. McGarvey , Mr. Schneider , Mr. Takano , Mrs. Dingell , Mr. Sorensen , Mr. Carson , Ms. S\u00e1nchez , Mr. Mullin , Ms. McBride , Mr. Carter of Louisiana , Mr. Gottheimer , Ms. Sherrill , Mr. Golden of Maine , Ms. Scholten , Mr. Tonko , Mr. Deluzio , Mr. Norcross , Ms. Scanlon , Mr. Pocan , Mr. Casar , Ms. Stevens , Ms. Clarke of New York , Ms. Salinas , Mr. Menendez , Ms. Adams , Mr. Grijalva , Mrs. McBath , Ms. Wilson of Florida , Ms. Stansbury , Ms. Craig , Mrs. Hayes , Mr. Soto , Ms. Schakowsky , Mr. Davis of North Carolina , Mr. Thanedar , Mr. Mannion , Ms. Omar , Mr. Vindman , Mr. DeSaulnier , Mrs. Cherfilus-McCormick , Ms. Tokuda , Mrs. Sykes , Mr. Latimer , Ms. Hoyle of Oregon , Mr. Johnson of Georgia , Ms. Gillen , Ms. Lee of Pennsylvania , Ms. Jayapal , Ms. Perez , Mr. Kennedy of New York , Ms. Dexter , Mr. Riley of New York , Mr. Horsford , Mr. Goldman of New York , Mr. Sherman , Mr. Lynch , Ms. Barrag\u00e1n , Mr. Green of Texas , Ms. Meng , Ms. Elfreth , Ms. Randall , Mr. Larson of Connecticut , Mr. Beyer , Mr. Cisneros , Mr. Thompson of California , Mr. Lieu , Mr. Conaway , Ms. Bynum , Mr. Landsman , Ms. Chu , Ms. Houlahan , Mr. Ryan , Mr. Swalwell , Mr. Jeffries , Mrs. Trahan , Ms. McCollum , Mr. Torres of New York , Ms. Vel\u00e1zquez , Mr. Nadler , Ms. Ocasio-Cortez , Mr. Castro of Texas , Mr. Evans of Pennsylvania , Mr. David Scott of Georgia , Ms. Pingree , Mr. Quigley , Mr. Ruiz , Mrs. Foushee , Mr. Ivey , Mr. Magaziner , Ms. Wasserman Schultz , Mr. Cleaver , Mr. Doggett , Ms. Morrison , Mr. Gomez , Mr. Boyle of Pennsylvania , Mr. Krishnamoorthi , Mr. Case , Mr. Frost , Ms. Davids of Kansas , Mr. Veasey , Ms. Ross , Mr. Garc\u00eda of Illinois , Mr. Amo , Ms. DeGette , Mr. Raskin , Ms. Clark of Massachusetts , Mr. Crow , Mr. Bell , Ms. Balint , Ms. DelBene , Mr. Carbajal , Mr. Vargas , Ms. Jacobs , Mr. Panetta , Mr. Foster , Ms. Matsui , Ms. McClellan , Mr. Pallone , Ms. Strickland , Ms. Pettersen , Mr. Smith of Washington , Ms. Lee of Nevada , Mr. Moulton , Mrs. Beatty , Ms. Brownley , Mr. Harder of California , Mr. Subramanyam , Mr. Hoyer , Mr. Olszewski , Mrs. Torres of California , Ms. Lois Frankel of Florida , Ms. Dean of Pennsylvania , Ms. McDonald Rivet , Mrs. McClain Delaney , Mr. Mfume , Ms. Pou , Ms. Friedman , Mr. Min , Mr. Neal , Ms. Waters , Ms. Kelly of Illinois , Ms. Goodlander , Mr. Garcia of California , Ms. Escobar , Mr. Meeks , Mr. Casten , Mrs. Watson Coleman , Mr. Moskowitz , Ms. Garcia of Texas , Mr. Morelle , Ms. Sewell , Mr. Khanna , Mr. Jackson of Illinois , Mr. Larsen of Washington , Mr. Aguilar , Ms. Crockett , Ms. Schrier , Mr. Espaillat , Mr. Stanton , Ms. Simon , Mr. Vasquez , Ms. Leger Fernandez , Mr. Huffman , Ms. Rivas , Mrs. Fletcher , Mr. Suozzi , Mr. Himes , Mr. Figures , Mr. Tran , Mr. Peters , Ms. Kamlager-Dove , Mr. Davis of Illinois , Ms. Castor of Florida , Ms. Pressley , Mr. Courtney , Ms. Pelosi , Mr. Neguse , Mr. Levin , Mr. Gray , Mr. Connolly , Mr. Whitesides , Mr. Bera , Mr. Pappas , Ms. Plaskett , Ms. Underwood , Mr. Cohen , and Mr. Smith of New Jersey ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the National Labor Relations Act, the Labor Management Relations Act, 1947, and the Labor-Management Reporting and Disclosure Act of 1959, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Richard L. Trumka Protecting the Right to Organize Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTitle I\u2014Amendments to the National Labor Relations Act\nSec. 101. Definitions.\nSec. 102. Reports.\nSec. 103. Appointment.\nSec. 104. Unfair labor practices.\nSec. 105. Representatives and elections.\nSec. 106. Damages for unfair labor practices.\nSec. 107. Enforcing compliance with orders of the board.\nSec. 108. Injunctions against unfair labor practices involving discharge or other serious economic harm.\nSec. 109. Penalties.\nSec. 110. Limitations on the right to strike.\nSec. 111. Fair share agreements permitted.\nTitle II\u2014Amendments to the Labor Management Relations Act, 1947, and the Labor-Management Reporting and Disclosure Act of 1959\nSec. 201. Conforming amendments to the Labor Management Relations Act, 1947.\nSec. 202. Amendments to the Labor-Management Reporting and Disclosure Act of 1959.\nTitle III\u2014Other matters\nSec. 301. Electronic voting in Union elections.\nSec. 302. GAO report on sectoral bargaining.\nSec. 303. Severability.\nSec. 304. Authorization of appropriations.\nSec. 305. Rule of Construction.\nSec. 306. Rule of Construction.\nSec. 307. Rule of Construction.\nSec. 308. Rule of Construction.\nSec. 309. GAO Report.\nI\nAmendments to the National Labor Relations Act\n#### 101. Definitions\n##### (a) Joint employer\nSection 2(2) of the National Labor Relations Act ( 29 U.S.C. 152(2) ) is amended by adding at the end the following: Two or more persons shall be employers with respect to an employee if each such person codetermines or shares control over the employee\u2019s essential terms and conditions of employment. In determining whether such control exists, the Board or a court of competent jurisdiction shall consider as relevant direct control and indirect control over such terms and conditions, reserved authority to control such terms and conditions, and control over such terms and conditions exercised by a person in fact: Provided, That nothing herein precludes a finding that indirect or reserved control standing alone can be sufficient given specific facts and circumstances. .\n##### (b) Employee\nSection 2(3) of the National Labor Relations Act ( 29 U.S.C. 152(3) ) is amended by adding at the end the following:\nAn individual performing any service shall be considered an employee (except as provided in the previous sentence) and not an independent contractor, unless\u2014 (A) the individual is free from control and direction in connection with the performance of the service, both under the contract for the performance of service and in fact; (B) the service is performed outside the usual course of the business of the employer; and (C) the individual is customarily engaged in an independently established trade, occupation, profession, or business of the same nature as that involved in the service performed. .\n##### (c) Supervisor\nSection 2(11) of the National Labor Relations Act ( 29 U.S.C. 152(11) ) is amended\u2014\n**(1)**\nby inserting and for a majority of the individual\u2019s worktime after interest of the employer ;\n**(2)**\nby striking assign, ; and\n**(3)**\nby striking or responsibly to direct them, .\n#### 102. Reports\nSection 3(c) of the National Labor Relations Act ( 29 U.S.C. 153(c) ) is amended\u2014\n**(1)**\nby striking The Board and inserting (1) The Board ; and\n**(2)**\nby adding at the end the following:\n(2) Effective January 1, 2027, section 3003 of the Federal Reports Elimination and Sunset Act of 1995 ( Public Law 104\u201366 ; 31 U.S.C. 1113 note) shall not apply with respect to reports required under this subsection. (3) Each report issued under this subsection shall\u2014 (A) include no less detail than reports issued by the Board prior to the termination of such reports under section 3003 of the Federal Reports Elimination and Sunset Act of 1995 ( Public Law 104\u201366 ; 31 U.S.C. 1113 note); (B) list each case in which the Designated Agency Ethics Official provided advice regarding whether a Member should be recused from participating in a case or rulemaking; and (C) list each case in which the Designated Agency Ethics Official determined that a Member should be recused from participating in a case or rulemaking. .\n#### 103. Appointment\nSection 4(a) of the National Labor Relations Act ( 29 U.S.C. 154(a) ) is amended by striking , or for economic analysis .\n#### 104. Unfair labor practices\nSection 8 of the National Labor Relations Act ( 29 U.S.C. 158 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (5), by striking the period and inserting ; ; and\n**(B)**\nby adding at the end the following:\n(6) to promise, threaten, or take any action\u2014 (A) to permanently replace an employee who participates in a strike as defined by section 501(2) of the Labor Management Relations Act, 1947 ( 29 U.S.C. 142(2) ); (B) to discriminate against an employee who is working or has unconditionally offered to return to work for the employer because the employee supported or participated in such a strike; or (C) to lockout, suspend, or otherwise withhold employment from employees in order to influence the position of such employees or the representative of such employees in collective bargaining prior to a strike; and (7) to communicate or misrepresent to an employee under section 2(3) that such employee is excluded from the definition of employee under section 2(3). ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking paragraphs (4) and (7);\n**(B)**\nby redesignating paragraphs (5) and (6) as paragraphs (4) and (5), respectively;\n**(C)**\nin paragraph (4), as so redesignated, by striking affected; and inserting affected; and ; and\n**(D)**\nin paragraph (5), as so redesignated, by striking ; and and inserting a period;\n**(3)**\nin subsection (c), by striking the period at the end and inserting the following: : Provided, That it shall be an unfair labor practice under subsection (a)(1) for any employer to require or coerce an employee to attend or participate in such employer\u2019s campaign activities unrelated to the employee\u2019s job duties, including activities that are subject to the requirements under section 203(b) of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 433(b) ). ;\n**(4)**\nin subsection (d)\u2014\n**(A)**\nby redesignating paragraphs (1) through (4) as subparagraphs (A) through (D), respectively;\n**(B)**\nby striking For the purposes of this section and inserting (1) For purposes of this section ;\n**(C)**\nby inserting and to maintain current wages, hours, and terms and conditions of employment pending an agreement after arising thereunder ;\n**(D)**\nby inserting Provided, That an employer\u2019s duty to collectively bargain shall continue absent decertification of the labor organization following an election conducted pursuant to section 9: after making of a concession: ;\n**(E)**\nby inserting further before , That where there is in effect ;\n**(F)**\nby striking The duties imposed and inserting (2) The duties imposed ;\n**(G)**\nby striking by paragraphs (2), (3), and (4) and inserting by subparagraphs (B), (C), and (D) of paragraph (1) ;\n**(H)**\nby striking section 8(d)(1) and inserting paragraph (1)(A) ;\n**(I)**\nby striking section 8(d)(3) and inserting paragraph (1)(C) in each place it appears;\n**(J)**\nby striking section 8(d)(4) and inserting paragraph (1)(D) ; and\n**(K)**\nby adding at the end the following:\n(3) Whenever collective bargaining is for the purpose of establishing an initial collective bargaining agreement following certification or recognition of a labor organization, the following shall apply: (A) Not later than 10 days after receiving a written request for collective bargaining from an individual or labor organization that has been newly recognized or certified as a representative as defined in section 9(a), or within such further period as the parties agree upon, the parties shall meet and commence to bargain collectively and shall make every reasonable effort to conclude and sign a collective bargaining agreement. (B) If after the expiration of the 90-day period beginning on the date on which bargaining is commenced, or such additional period as the parties may agree upon, the parties have failed to reach an agreement, either party may notify the Federal Mediation and Conciliation Service of the existence of a dispute and request mediation. Whenever such a request is received, it shall be the duty of the Service promptly to put itself in communication with the parties and to use its best efforts, by mediation and conciliation, to bring them to agreement. (C) If after the expiration of the 30-day period beginning on the date on which the request for mediation is made under subparagraph (B), or such additional period as the parties may agree upon, the Service is not able to bring the parties to agreement by conciliation, the Service shall refer the dispute to a tripartite arbitration panel established in accordance with such regulations as may be prescribed by the Service, with one member selected by the labor organization, one member selected by the employer, and one neutral member mutually agreed to by the parties. The labor organization and employer must each select the members of the tripartite arbitration panel within 14 days of the Service\u2019s referral; if the labor organization or employer fail to do so, the Service shall designate any members not selected by the labor organization or the employer. A majority of the tripartite arbitration panel shall render a decision settling the dispute as soon as practicable and not later than within 120 days, absent extraordinary circumstances or by agreement or permission of the parties, and such decision shall be binding upon the parties for a period of 2 years, unless amended during such period by written consent of the parties. Such decision shall be based on\u2014 (i) the employer\u2019s financial status and prospects; (ii) the size and type of the employer\u2019s operations and business; (iii) the employees\u2019 cost of living; (iv) the employees\u2019 ability to sustain themselves, their families, and their dependents on the wages and benefits they earn from the employer; and (v) the wages and benefits other employers in the same business provide their employees. ;\n**(5)**\nby amending subsection (e) to read as follows:\n(e) Notwithstanding chapter 1 of title 9, United States Code (commonly known as the Federal Arbitration Act ), or any other provision of law, it shall be an unfair labor practice under subsection (a)(1) for any employer\u2014 (1) to enter into or attempt to enforce any agreement, express or implied, whereby prior to a dispute to which the agreement applies, an employee undertakes or promises not to pursue, bring, join, litigate, or support any kind of joint, class, or collective claim arising from or relating to the employment of such employee in any forum that, but for such agreement, is of competent jurisdiction; (2) to coerce an employee into undertaking or promising not to pursue, bring, join, litigate, or support any kind of joint, class, or collective claim arising from or relating to the employment of such employee; or (3) to retaliate or threaten to retaliate against an employee for refusing to undertake or promise not to pursue, bring, join, litigate, or support any kind of joint, class, or collective claim arising from or relating to the employment of such employee: Provided , That any agreement that violates this subsection or results from a violation of this subsection shall be to such extent unenforceable and void: Provided further , That this subsection shall not apply to any agreement embodied in or expressly permitted by a contract between an employer and a labor organization. ;\n**(6)**\nin subsection (g), by striking clause (B) of the last sentence of section 8(d) of this Act and inserting subsection (d)(2)(B) ; and\n**(7)**\nby adding at the end the following:\n(h) (1) The Board shall promulgate regulations requiring each employer to post and maintain, in conspicuous places where notices to employees and applicants for employment are customarily posted both physically and electronically, a notice setting forth the rights and protections afforded employees under this Act. The Board shall make available to the public the form and text of such notice. The Board shall promulgate regulations requiring employers to notify each new employee of the information contained in the notice described in the preceding two sentences and to ensure that such notice is provided to employees in a language spoken by such employees. (2) Whenever the Board directs an election under section 9(c) or approves an election agreement, the employer of employees in the bargaining unit shall, not later than 2 business days after the Board directs such election or approves such election agreement, provide a voter list to a labor organization that has petitioned to represent such employees. Such voter list shall include the names of all employees in the bargaining unit and such employees\u2019 home addresses, work locations, shifts, job classifications, and, if available to the employer, personal landline and mobile telephone numbers, work email addresses, and personal email addresses; the voter list must be provided in a searchable electronic format generally approved by the Board unless the employer certifies that the employer does not possess the capacity to produce the list in the required form. Not later than 9 months after the date of enactment of the Richard L. Trumka Protecting the Right to Organize Act of 2025 , the Board shall promulgate regulations implementing the requirements of this paragraph. (i) The rights of an employee under section 7 include the right to use electronic communication devices and systems (including computers, laptops, tablets, internet access, email, cellular telephones, or other company equipment) of the employer of such employee to engage in activities protected under section 7 if such employer has given such employee access to such devices and systems in the course of the work of such employee, absent a compelling business rationale for denying or limiting such use. .\n#### 105. Representatives and elections\nSection 9 of the National Labor Relations Act ( 29 U.S.C. 159 ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) Whenever a petition shall have been filed, in accordance with such regulations as may be prescribed by the Board, by an employee or group of employees or any individual or labor organization acting in their behalf alleging that a substantial number of employees (i) wish to be represented for collective bargaining and that their employer declines to recognize their representative as the representative defined in section 9(a), or (ii) assert that the individual or labor organization, which has been certified or is being recognized by their employer as the bargaining representative, is no longer a representative as defined in section 9(a), the Board shall investigate such petition and if it has reasonable cause to believe that a question of representation affecting commerce exists shall provide for an appropriate hearing upon due notice. Such hearing may be conducted by an officer or employee of the regional office, who shall not make any recommendations with respect thereto. If the Board finds upon the record of such hearing that such a question of representation exists, it shall direct an election by secret ballot and shall certify the results thereof. The Board shall find the labor organization\u2019s proposed unit to be appropriate if the employees in the proposed unit share a community of interest, and if the employees outside the unit do not share an overwhelming community of interest with employees inside. At the request of the labor organization, the Board shall direct that the election be conducted through mail, electronically, at the work location, or at a location other than one owned or controlled by the employer. No employer shall have standing as a party or to intervene in any representation proceeding under this section. ;\n**(B)**\nin paragraph (3), by striking an economic strike who are not entitled to reinstatement and inserting a strike ;\n**(C)**\nby redesignating paragraphs (4) and (5) as paragraphs (6) and (7), respectively;\n**(D)**\nby inserting after paragraph (3) the following:\n(4) If the Board finds that, in an election under paragraph (1), a majority of the valid votes cast in a unit appropriate for purposes of collective bargaining have been cast in favor of representation by the labor organization, the Board shall certify the labor organization as the representative of the employees in such unit and shall issue an order requiring the employer of such employees to collectively bargain with the labor organization in accordance with section 8(d). This order shall be deemed an order under section 10(c) of this Act, without need for a determination of an unfair labor practice. (5) (A) If the Board finds that, in an election under paragraph (1), a majority of the valid votes cast in a unit appropriate for purposes of collective bargaining have not been cast in favor of representation by the labor organization, the Board shall certify the results of the election, subject to subparagraphs (B) and (C). (B) In any case in which a majority of the valid votes cast in a unit appropriate for purposes of collective bargaining have not been cast in favor of representation by the labor organization and the Board determines, following a post-election hearing, that the employer has committed a violation of this Act or otherwise interfered with a fair election, and the employer has not demonstrated that the violation or other interference is unlikely to have affected the outcome of the election, the Board shall, without ordering a new election, set aside the election and certify the labor organization as the representative of the employees in such unit and issue an order requiring the employer to bargain with the labor organization in accordance with section 8(d) if, at any time during the period beginning 1 year preceding the date of the commencement of the election and ending on the date upon which the Board makes the determination of a violation or other interference, a majority of the employees in the bargaining unit have signed authorizations designating the labor organization as their collective bargaining representative. (C) In any case where the Board determines that an election under this paragraph should be set aside, the Board shall direct a new election with appropriate additional safeguards necessary to ensure a fair election process, except in cases where the Board issues a bargaining order under subparagraph (B). ; and\n**(E)**\nby inserting after paragraph (7), as so redesignated, the following:\n(8) Except under extraordinary circumstances\u2014 (A) a pre-election hearing under this subsection shall begin not later than 8 days after a notice of such hearing is served on the labor organization and shall continue from day to day until completed; (B) a regional director shall transmit the notice of election at the same time as the direction of election, and shall transmit such notice and such direction electronically (including transmission by email or facsimile) or by overnight mail if electronic transmission is unavailable; (C) not later than 2 days after the service of the notice of hearing, the employer shall\u2014 (i) post the Notice of Petition for Election in conspicuous places, including all places where notices to employees are customarily posted; (ii) if the employer customarily communicates with employees electronically, distribute such Notice electronically; and (iii) maintain such posting until the petition is dismissed or withdrawn or the Notice of Petition for Election is replaced by the Notice of Election; (D) regional directors shall schedule elections for the earliest date practicable, but not later than the 20th business day after the direction of election; and (E) a post-election hearing under this subsection shall begin not later than 14 days after the filing of objections, if any. ;\n**(2)**\nin subsection (d), by striking (e) or and inserting (d) or ; and\n**(3)**\nby adding at the end the following:\n(f) The Board shall dismiss any petition for an election with respect to a bargaining unit or any subdivision if, during the 12-month period ending on the date on which the petition is filed\u2014 (1) the employer has recognized a labor organization without an election and in accordance with this Act; (2) the labor organization and employer engaged in their first bargaining session following the issuance of a bargaining order by the Board; or (3) the labor organization and successor employer engaged in their first bargaining session following a succession. (g) The Board shall dismiss any petition for an election with respect to a bargaining unit or any subdivision if there is in effect a lawful written collective bargaining agreement between the employer and an exclusive representative covering any employees in the unit specified in the petition, unless the petition is filed\u2014 (1) on or after the date that is 3 years after the date on which the collective bargaining agreement took effect; or (2) during the 30-day period beginning on the date that is 90 days before the date that is 3 years after the date on which the collective bargaining agreement took effect. (h) The Board shall suspend the processing of any petition for an election with respect to a bargaining unit or any subdivision if a labor organization files an unfair labor practice charge alleging a violation of section 8(a) and requesting the suspension of a pending petition until the unlawful conduct, if any, is remedied or the charge is dismissed unless the Board determines that employees can, under the circumstances, exercise free choice in an election despite the unlawful conduct alleged in the charge. .\n#### 106. Damages for unfair labor practices\nSection 10(c) of the National Labor Relations Act ( 29 U.S.C. 160(c) ) is amended by striking suffered by him and inserting suffered by such employee: Provided further, That if the Board finds that an employer has discriminated against an employee in violation of paragraph (3) or (4) of section 8(a) or has committed a violation of section 8(a) that results in the discharge of an employee or other serious economic harm to an employee, the Board shall award the employee back pay without any reduction (including any reduction based on the employee\u2019s interim earnings or failure to earn interim earnings), front pay (when appropriate), full compensation for all direct or foreseeable pecuniary harms suffered as a result of the respondent\u2019s unfair labor practice, and an additional amount as liquidated damages equal to two times the amount of damages awarded: Provided further, no relief under this subsection shall be denied on the basis that the employee is, or was during the time of relevant employment or during the back pay period, an unauthorized alien as defined in section 274A(h)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1324a(h)(3) ) or any other provision of Federal law relating to the unlawful employment of aliens .\n#### 107. Enforcing compliance with orders of the board\n##### (a) In general\nSection 10 of the National Labor Relations Act ( 29 U.S.C. 160 ) is further amended\u2014\n**(1)**\nby striking subsection (e);\n**(2)**\nby redesignating subsection (d) as subsection (e);\n**(3)**\nby inserting after subsection (c) the following:\n(d) (1) Each order of the Board shall be self-enforcing upon issuance of such order, unless otherwise directed by the Board, and shall remain self-enforcing unless modified by the Board or unless a court of competent jurisdiction issues a superseding order. (2) Any person who fails or neglects to obey an order of the Board shall forfeit and pay to the Board a civil penalty of not more than $10,000 for each violation, which shall accrue to the United States and may be recovered in a civil action brought by the Board to the district court of the United States in which the unfair labor practice or other subject of the order occurred, or in which such person or entity resides or transacts business. No action by the Board under this paragraph may be made until 30 days following the issuance of an order. Each separate violation of such an order shall be a separate offense, except that, in the case of a violation in which a person fails to obey or neglects to obey a final order of the Board, each day such failure or neglect continues shall be deemed a separate offense. (3) If, after having provided a person or entity with notice and an opportunity to be heard regarding a civil action under paragraph (2) for the enforcement of an order, the court determines that the order was regularly made and duly served, and that the person or entity is in disobedience of the same, the court shall enforce obedience to such order by an injunction or other proper process, mandatory or otherwise, to\u2014 (A) restrain such person or entity or the officers, agents, or representatives of such person or entity, from further disobedience to such order; or (B) enjoin such person or entity, officers, agents, or representatives to obedience to the same. ;\n**(4)**\nin subsection (f)\u2014\n**(A)**\nby striking proceed in the same manner as in the case of an application by the Board under subsection (e) of this section, and inserting proceed as provided under paragraph (2) of this subsection ;\n**(B)**\nby striking Any and inserting the following:\n(1) Within 30 days of the issuance of an order, any ; and\n**(C)**\nby adding at the end the following:\n(2) No objection that has not been urged before the Board, its member, agent, or agency shall be considered by a court, unless the failure or neglect to urge such objection shall be excused because of extraordinary circumstances. The findings of the Board with respect to questions of fact if supported by substantial evidence on the record considered as a whole shall be conclusive. If either party shall apply to the court for leave to adduce additional evidence and shall show to the satisfaction of the court that such additional evidence is material and that there were reasonable grounds for the failure to adduce such evidence in the hearing before the Board, its member, agent, or agency, the court may order such additional evidence to be taken before the Board, its member, agent, or agency, and to be made a part of the record. The Board may modify its findings as to the facts, or make new findings, by reason of additional evidence so taken and filed, and it shall file such modified or new findings, which findings with respect to questions of fact if supported by substantial evidence on the record considered as a whole shall be conclusive, and shall file its recommendations, if any, for the modification or setting aside of its original order. Upon the filing of the record with it the jurisdiction of the court shall be exclusive and its judgment and decree shall be final, except that the same shall be subject to review by the appropriate United States court of appeals if application was made to the district court, and by the Supreme Court of the United States upon writ of certiorari or certification as provided in section 1254 of title 28, United States Code. ; and\n**(5)**\nin subsection (g), by striking subsection (e) or (f) of this section and inserting subsection (d) or (f) .\n##### (b) Conforming amendment\nSection 18 of the National Labor Relations Act ( 29 U.S.C. 168 ) is amended by striking section 10(e) or (f) and inserting subsection (d) or (f) of section 10 .\n#### 108. Injunctions against unfair labor practices involving discharge or other serious economic harm\nSection 10 of the National Labor Relations Act ( 29 U.S.C. 160 ) is amended\u2014\n**(1)**\nin subsection (j)\u2014\n**(A)**\nby striking The Board and inserting (1) The Board ; and\n**(B)**\nby adding at the end the following:\n(2) Notwithstanding subsection (m), whenever it is charged that an employer has engaged in an unfair labor practice within the meaning of paragraph (1), (3), or (4) of section 8(a) that significantly interferes with, restrains, or coerces employees in the exercise of the rights guaranteed under section 7, or involves discharge or other serious economic harm to an employee, the preliminary investigation of such charge shall be made forthwith and given priority over all other cases except cases of like character in the office where it is filed or to which it is referred. If, after such investigation, the officer or regional attorney to whom the matter may be referred has reasonable cause to believe such charge is true and that a complaint should issue, such officer or attorney shall bring a petition for appropriate temporary relief or restraining order as set forth in paragraph (1). The district court shall grant the relief requested unless the court concludes that there is no reasonable likelihood that the Board will succeed on the merits of the Board\u2019s claim. ; and\n**(2)**\nby repealing subsections (k) and (l).\n#### 109. Penalties\n##### (a) In general\nSection 12 of the National Labor Relations Act ( 29 U.S.C. 162 ) is amended\u2014\n**(1)**\nby striking Sec. 12. Any person and inserting the following:\n12. Penalties (a) Violations for interference with board Any person ; and\n**(2)**\nby adding at the end the following:\n(b) Violations for posting requirements and voter list If the Board, or any agent or agency designated by the Board for such purposes, determines that an employer has violated section 8(h) or regulations issued thereunder, the Board shall\u2014 (1) state the findings of fact supporting such determination; (2) issue and cause to be served on such employer an order requiring that such employer comply with section 8(h) or regulations issued thereunder; and (3) impose a civil penalty in an amount determined appropriate by the Board, except that in no case shall the amount of such penalty exceed $500 for each such violation. (c) Civil penalties for violations (1) In general Any employer who commits an unfair labor practice within the meaning of section 8(a) shall, in addition to any remedy ordered by the Board, be subject to a civil penalty in an amount not to exceed $50,000 for each violation, except that, with respect to an unfair labor practice within the meaning of paragraph (3) or (4) of section 8(a) or a violation of section 8(a) that results in the discharge of an employee or other serious economic harm to an employee, the Board shall double the amount of such penalty, to an amount not to exceed $100,000, in any case where the employer has within the preceding 5 years committed another such violation. (2) Considerations In determining the amount of any civil penalty under this subsection, the Board shall consider\u2014 (A) the gravity of the unfair labor practice; (B) the impact of the unfair labor practice on the charging party, on other persons seeking to exercise rights guaranteed by this Act, and on the public interest; and (C) the gross income of the employer. (3) Director and officer liability If the Board determines, based on the particular facts and circumstances presented, that a director or officer\u2019s personal liability is warranted, a civil penalty for a violation described in this subsection may also be assessed against any director or officer of the employer who directed or committed the violation, had established a policy that led to such a violation, or had actual or constructive knowledge of and the authority to prevent the violation and failed to prevent the violation. (d) Right to civil action (1) In general Any person who is injured by reason of a violation of paragraph (1), (3), or (4) of section 8(a) may, after 60 days following the filing of a charge with the Board alleging an unfair labor practice, bring a civil action in the appropriate district court of the United States against the employer within 90 days after the expiration of the 60-day period or the date the Board notifies the person that no complaint shall issue, whichever occurs earlier, provided that the Board has not filed a petition under section 10(j) of this Act prior to the expiration of the 60-day period. No relief under this subsection shall be denied on the basis that the employee is, or was during the time of relevant employment or during the back pay period, an unauthorized alien as defined in section 274A(h)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1324a(h)(3) ) or any other provision of Federal law relating to the unlawful employment of aliens. (2) Available relief Relief granted in an action under paragraph (1) may include\u2014 (A) back pay without any reduction, including any reduction based on the employee\u2019s interim earnings or failure to earn interim earnings; (B) front pay (when appropriate); (C) all direct or foreseeable pecuniary harms suffered as a result of the unfair labor practice; (D) an additional amount as liquidated damages equal to two times the cumulative amount of damages awarded under subparagraphs (A) through (C); (E) in appropriate cases, punitive damages in accordance with paragraph (4); and (F) any other relief authorized by section 706(g) of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e\u20135(g) ) or by section 1977A(b) of the Revised Statutes ( 42 U.S.C. 1981a(b) ). (3) Attorney\u2019s fees In any civil action under this subsection, the court may allow the prevailing party a reasonable attorney\u2019s fee (including expert fees) and other reasonable costs associated with maintaining the action. (4) Punitive damages In awarding punitive damages under paragraph (2)(E), the court shall consider\u2014 (A) the gravity of the unfair labor practice; (B) the impact of the unfair labor practice on the charging party, on other persons seeking to exercise rights guaranteed by this Act, and on the public interest; and (C) the gross income of the employer. .\n##### (b) Conforming amendments\nSection 10(b) of the National Labor Relations Act ( 29 U.S.C. 160(b) ) is amended\u2014\n**(1)**\nby striking six months and inserting 180 days ; and\n**(2)**\nby striking the six-month period and inserting the 180-day period .\n#### 110. Limitations on the right to strike\nSection 13 of the National Labor Relations Act ( 29 U.S.C. 163 ) is amended by striking the period at the end and inserting the following: : Provided, That the duration, scope, frequency, or intermittence of any strike or strikes shall not render such strike or strikes unprotected or prohibited. .\n#### 111. Fair share agreements permitted\nSection 14(b) of the National Labor Relations Act ( 29 U.S.C. 164(b) ) is amended by striking the period at the end and inserting the following: : Provided, That collective bargaining agreements providing that all employees in a bargaining unit shall contribute fees to a labor organization for the cost of representation, collective bargaining, contract enforcement, and related expenditures as a condition of employment shall be valid and enforceable notwithstanding any State or Territorial law. .\nII\nAmendments to the Labor Management Relations Act, 1947, and the Labor-Management Reporting and Disclosure Act of 1959\n#### 201. Conforming amendments to the Labor Management Relations Act, 1947\nThe Labor Management Relations Act, 1947, is amended\u2014\n**(1)**\nin section 213(a) ( 29 U.S.C. 183(a) ), by striking clause (A) of the last sentence of section 8(d) (which is required by clause (3) of such section 8(d)), or within 10 days after the notice under clause (B) and inserting section 8(d)(2)(A) of the National Labor Relations Act (which is required by section 8(d)(1)(C) of such Act), or within 10 days after the notice under section 8(d)(2)(B) of such Act ; and\n**(2)**\nby repealing section 303 ( 29 U.S.C. 187 ).\n#### 202. Amendments to the Labor-Management Reporting and Disclosure Act of 1959\n##### (a) In General\nSection 203(c) of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 433(c) ) is amended by striking the period at the end and inserting the following : Provided, That this subsection shall not exempt from the requirements of this section any arrangement or part of an arrangement in which a party agrees, for an object described in subsection (b)(1), to plan or conduct employee meetings; train supervisors or employer representatives to conduct meetings; coordinate or direct activities of supervisors or employer representatives; establish or facilitate employee committees; identify employees for disciplinary action, reward, or other targeting; or draft or revise employer personnel policies, speeches, presentations, or other written, recorded, or electronic communications to be delivered or disseminated to employees. .\n##### (b) Whistleblower protections\nThe Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 401 et seq. ) is further amended\u2014\n**(1)**\nby redesignating section 611 ( 29 U.S.C. 531 ) as section 612; and\n**(2)**\nby inserting after section 610 ( 29 U.S.C. 530 ), the following new section:\n611. Whistleblower Protections (a) In general No employer or labor organization shall terminate or in any other way discriminate against, or cause to be terminated or discriminated against, any applicant, covered employee, or former covered employee, of the employer or the labor organization by reason of the fact that such applicant, covered employee, or former covered employee does, or the employer or labor organization perceives the employee to do, any of the following: (1) Provide, cause to be provided, or is about to provide or cause to be provided, information to the labor organization, the employer, the Department of Labor, or any other State, local, or Federal Government authority or law enforcement agency relating to any violation of, or any act or omission that such employee reasonably believes to be a violation of, any provision of this Act. (2) Testify or plan to testify or otherwise participate in any proceeding resulting from the administration or enforcement of any provision of this Act. (3) File, institute, or cause to be filed or instituted, any proceeding under this Act. (4) Assist in any activity described in paragraphs (1) through (3). (5) Object to, or refuse to participate in, any activity, policy, practice, or assigned task that such covered employee reasonably believes to be in violation of any provision of this Act. (b) Definition of covered employee For the purposes of this section, the term covered employee means any employee or agent of an employer or labor organization, including any person with management responsibilities on behalf of the employer or labor organization. (c) Procedures and timetables (1) Complaint (A) In general An applicant, covered employee, or former covered employee who believes that he or she has been terminated or in any other way discriminated against by any person in violation of subsection (a) may file (or have any person file on his or her behalf) a complaint with the Secretary of Labor alleging such violation. Such a complaint must be filed not later than either\u2014 (i) 180 days after the date on which such alleged violation occurs; or (ii) 180 days after the date upon which the employee knows or should reasonably have known that such alleged violation in subsection (a) occurred. (B) Actions of Secretary of Labor Upon receipt of such a complaint, the Secretary of Labor shall notify, in writing, the person named in the complaint who is alleged to have committed the violation, of\u2014 (i) the filing of the complaint; (ii) the allegations contained in the complaint; (iii) the substance of evidence supporting the complaint; and (iv) opportunities that will be afforded to such person under paragraph (2). (2) Investigation by Secretary of Labor (A) In general Not later than 60 days after the date of receipt of a complaint filed under paragraph (1), and after affording the complainant and the person named in the complaint who is alleged to have committed the violation that is the basis for the complaint an opportunity to submit to the Secretary of Labor a written response to the complaint and an opportunity to meet with a representative of the Secretary of Labor to present statements from witnesses, the Secretary of Labor shall\u2014 (i) initiate an investigation and determine whether there is reasonable cause to believe that the complaint has merit; and (ii) notify the complainant and the person alleged to have committed the violation of subsection (a), in writing, of such determination. (B) Grounds for determination of complaints The Secretary of Labor shall dismiss a complaint filed under this subsection, and shall not conduct an investigation otherwise required under subparagraph (A), unless the complainant makes a prima facie showing that any behavior described in paragraphs (1) through (5) of subsection (a) was a contributing factor in the unfavorable personnel action alleged in the complaint. (3) Burdens of proof (A) Criteria for determination In making a determination or adjudicating a complaint pursuant to this subsection, the Secretary, an administrative law judge, or a court may determine that a violation of subsection (a) has occurred only if the complainant demonstrates that any conduct described in subsection (a) with respect to the complainant was a contributing factor in the adverse action alleged in the complaint. (B) Prohibition Notwithstanding subparagraph (A), a decision or order that is favorable to the complainant shall not be issued in any administrative or judicial action pursuant to this subsection if the respondent demonstrates by clear and convincing evidence that the respondent would have taken the same adverse action in the absence of such conduct. (C) Notice of relief available If the Secretary of Labor concludes that there is reasonable cause to believe that a violation of subsection (a) has occurred, the Secretary of Labor shall, together with the notice under paragraph (2)(A)(ii), issue a preliminary order providing the relief prescribed by paragraph (4)(B). (D) Request for hearing Not later than 30 days after the date of receipt of notification of a determination of the Secretary of Labor under this paragraph, either the person alleged to have committed the violation or the complainant may file objections to the findings or preliminary order, or both, and request a hearing on the record. The filing of such objections shall not operate to stay any reinstatement remedy contained in the preliminary order. Any such hearing shall be conducted expeditiously, and if a hearing is not requested in such 30-day period, the preliminary order shall be deemed a final order that is not subject to judicial review. (E) Procedures (i) In general A hearing requested under this paragraph shall be conducted expeditiously and in accordance with rules established by the Secretary for hearings conducted by administrative law judges. (ii) Subpoenas; production of evidence In conducting any such hearing, the administrative law judge may issue subpoenas. The respondent or complainant may request the issuance of subpoenas that require the deposition of, or the attendance and testimony of, witnesses and the production of any evidence (including any books, papers, documents, or recordings) relating to the matter under consideration. (4) Issuance of final orders; review procedures (A) Timing Not later than 120 days after the date of conclusion of any hearing under paragraph (2), the Secretary of Labor shall issue a final order providing the relief prescribed by this paragraph or denying the complaint. At any time before issuance of a final order, a proceeding under this subsection may be terminated on the basis of a settlement agreement entered into by the Secretary of Labor, the complainant, and the person alleged to have committed the violation. (B) Available relief (i) Order of Secretary of Labor If, in response to a complaint filed under paragraph (1), the Secretary of Labor determines that a violation of subsection (a) has occurred, the Secretary of Labor shall order the person who committed such violation\u2014 (I) to take affirmative action to abate the violation; (II) to reinstate the complainant to his or her former position, together with compensation (including back pay with interest) and restore the terms, conditions, and privileges associated with his or her employment; (III) to provide compensatory damages to the complainant; and (IV) expungement of all warnings, reprimands, or derogatory references that have been placed in paper or electronic records or databases of any type relating to the actions by the complainant that gave rise to the unfavorable personnel action, and, at the complainant's direction, transmission of a copy of the decision on the complaint to any person whom the complainant reasonably believes may have received such unfavorable information. (ii) Costs and expenses If an order is issued under clause (i), the Secretary of Labor, at the request of the complainant, shall assess against the person against whom the order is issued, a sum equal to the aggregate amount of all costs and expenses (including attorney fees and expert witness fees) reasonably incurred, as determined by the Secretary of Labor, by the complainant for, or in connection with, the bringing of the complaint upon which the order was issued. (C) Frivolous claims If the Secretary of Labor finds that a complaint under paragraph (1) is frivolous or has been brought in bad faith, the Secretary of Labor may award to the prevailing employer or labor organization a reasonable attorney fee, not exceeding $1,000, to be paid by the complainant. (D) De novo review (i) Failure of the secretary to act If the Secretary of Labor has not issued a final order within 270 days after the date of filing of a complaint under this subsection, or within 90 days after the date of receipt of a written determination, the complainant may bring an action at law or equity for de novo review in the appropriate district court of the United States having jurisdiction, which shall have jurisdiction over such an action without regard to the amount in controversy, and which action shall, at the request of either party to such action, be tried by the court with a jury. (ii) Procedures A proceeding under clause (i) shall be governed by the same legal burdens of proof specified in paragraph (3). The court shall have jurisdiction to grant all relief necessary to make the employee whole, including injunctive relief and compensatory damages, including\u2014 (I) reinstatement with the same seniority status that the employee would have had, but for the discharge or discrimination; (II) the amount of back pay, with interest; (III) compensation for any special damages sustained as a result of the discharge or discrimination, including litigation costs, expert witness fees, and reasonable attorney fees; and (IV) expungement of all warnings, reprimands, or derogatory references that have been placed in paper or electronic records or databases of any type relating to the actions by the complainant that gave rise to the unfavorable personnel action, and, at the complainant's direction, transmission of a copy of the decision on the complaint to any person whom the complainant reasonably believes may have received such unfavorable information. (E) Other appeals Unless the complainant brings an action under subparagraph (D), any person adversely affected or aggrieved by a final order issued under subparagraph (A) may file a petition for review of the order in the United States Court of Appeals for the circuit in which the violation with respect to which the order was issued, allegedly occurred or the circuit in which the complainant resided on the date of such violation, not later than 60 days after the date of the issuance of the final order of the Secretary of Labor under subparagraph (A). Review shall conform to chapter 7 of title 5, United States Code. The commencement of proceedings under this subparagraph shall not, unless ordered by the court, operate as a stay of the order. An order of the Secretary of Labor with respect to which review could have been obtained under this subparagraph shall not be subject to judicial review in any criminal or other civil proceeding. (5) Failure to comply with order (A) Actions by the Secretary If any person has failed to comply with a final order issued under paragraph (4), the Secretary of Labor may file a civil action in the United States district court for the district in which the violation was found to have occurred, or in the United States district court for the District of Columbia, to enforce such order. In actions brought under this paragraph, the district courts shall have jurisdiction to grant all appropriate relief including injunctive relief, compensatory and punitive damages. (B) Civil actions to compel compliance A person on whose behalf an order was issued under paragraph (4) may commence a civil action against the person to whom such order was issued to require compliance with such order. The appropriate United States district court shall have jurisdiction, without regard to the amount in controversy or the citizenship of the parties, to enforce such order. (C) Award of costs authorized The court, in issuing any final order under this paragraph, may award costs of litigation (including reasonable attorney and expert witness fees) to any party, whenever the court determines such award is appropriate. (D) Mandamus proceedings Any nondiscretionary duty imposed by this section shall be enforceable in a mandamus proceeding brought under section 1361 of title 28, United States Code. (d) Unenforceability of certain agreements Notwithstanding any other provision of law, the rights and remedies provided for in this section may not be waived by any agreement, policy, form, or condition of employment, including by any predispute arbitration agreement. (e) Savings Nothing in this section shall be construed to diminish the rights, privileges, or remedies of any employee who exercises rights under any Federal or State law or common law, or under any collective bargaining agreement. .\n##### (c) Public availability of information\nSection 203(b) of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 433(b) ) is amended in the matter following paragraph (2) by striking the period at the end and inserting and shall make such information available to the public in a readily accessible and searchable electronic format, and through a secure software application for use on an electronic device. .\nIII\nOther matters\n#### 301. Electronic voting in Union elections\n##### (a) In general\n**(1) Electronic voting system**\nNotwithstanding any other provision of law, subject to the provisions of this section, not later than 1 year after the date of the enactment of this Act, the National Labor Relations Board shall implement a system and procedures to conduct representation elections remotely using an electronic voting system.\n**(2) Procedures**\nThe procedures under paragraph (1) shall ensure that each employee voting in a representation election may choose to cast a vote using either an internet voting system or a telephone voting system.\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, and in each subsequent report under section 3(c) of the National Labor Relations Act ( 29 U.S.C. 153(c) ), the Board shall submit to Congress a report containing a description of the following:\n**(1)**\nFor each representation petition under section 9 of the National Labor Relations Act filed\u2014\n**(A)**\nthe case name and case number;\n**(B)**\nthe number of days between the petition and the election;\n**(C)**\nthe number of days between the stipulation or direction of election and the election;\n**(D)**\nthe method of the election;\n**(E)**\nthe results of the election; and\n**(F)**\nthe number of eligible voters, the number of voters participating in the election, and the method by which each of the voters submitted their vote.\n**(2)**\nThe total cost of conducting all elections the Board conducted through the system and procedures required by subsection (a).\n##### (c) Definitions\nIn this section:\n**(1) Electronic voting system**\nThe term electronic voting system \u2014\n**(A)**\nincludes an internet voting system and a telephone voting system; and\n**(B)**\ndoes not include machines used for casting votes at a polling site or an electronic tabulation system where votes are cast non-electronically but counted electronically (such as a punch card or optical scanning system).\n**(2) Internet voting system**\nThe term internet voting system means an internet-based voting system that allows a participant to cast a ballot remotely using a personal computer or other mobile electronic device that is connected to the internet.\n**(3) Telephone voting system**\nThe term telephone voting system means a voting system in which participants may cast a vote remotely using a telephone.\n**(4) Remotely**\nThe term remotely , used with respect to voting in a representation election, means a vote may be cast at any site chosen by a participant in such election.\n**(5) Representation election**\nThe term representation election means a representation election under section 9 of the National Labor Relations Act ( 29 U.S.C. 159 ).\n#### 302. GAO report on sectoral bargaining\n##### (a) In general\nNot later than 3 years after the date of enactment of this Act, the Comptroller General shall conduct a review of collective bargaining at the sectoral level in a geographically diverse set of countries where sectoral bargaining is facilitated and prepare and submit to Congress a report with respect to such countries that\u2014\n**(1)**\nidentifies, analyzes, and compares\u2014\n**(A)**\nthe laws and policies governing or related to collective bargaining at the sectoral level;\n**(B)**\nthe administrative systems facilitating such bargaining; and\n**(C)**\nthe procedures involved in sectoral bargaining;\n**(2)**\nto the extent practicable, consider reported effects of the policies and procedures described in paragraph (1) on\u2014\n**(A)**\nthe wages and compensation of employees;\n**(B)**\nthe number of full-time and part-time employees;\n**(C)**\nprices, sales, and revenues;\n**(D)**\nemployee turnover and retention;\n**(E)**\nhiring and training costs;\n**(F)**\nproductivity and absenteeism; and\n**(G)**\nthe development of emerging industries, including those that engage their workforces through technology; and\n**(3)**\ndescribes the methodology used to generate the information in the report.\n#### 303. Severability\nIf any provision of this Act or the application thereof to any person or circumstance is held invalid, the remainder of this Act, or the application of that provision to persons or circumstances other than those as to which it is held invalid, is not affected thereby.\n#### 304. Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out the provisions of this Act and the amendments made by this Act.\n#### 305. Rule of Construction\nThe amendments made under this Act shall not be construed to amend section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ).\n#### 306. Rule of Construction\nThe amendments made by this Act shall not be construed to affect the jurisdictional standards of the National Labor Relations Board, including any standards that measure the size of a business with respect to revenues, that are used to determine whether an industry is affecting commerce for purposes of determining coverage under the National Labor Relations Act ( 29 U.S.C. 151 et seq. ).\n#### 307. Rule of Construction\nNothing in this Act or the amendments made by this Act shall be construed to affect the privacy of employees with respect to voter lists provided to labor organizations by employers pursuant to elections directed by the Board.\n#### 308. Rule of Construction\nThe amendments made under this Act shall not be construed to affect the definitions of employer or employee under the laws of any State that govern the wages, work hours, workers\u2019 compensation, or unemployment insurance of employees.\n#### 309. GAO Report\n##### (a) In General\nThe Comptroller General of the United States shall one year after the date of enactment of this Act commence a study on the impact of section 101(a) and section 101(b) of this Act regarding\u2014\n**(1)**\nthe effect on coverage of employees under of the National Labor Relations Act, and the impact from such change in coverage, on their capacity in various sectors to form unions and collectively bargain as a means to improve wages, benefits, workplace safety, and other working conditions; and\n**(2)**\nthe effect on employers and other enterprises regarding the right of employees to organize and collectively bargain over wages, benefits, workplace safety, and other working conditions in such sectors.\n##### (b) Factors\nSuch study shall identify, compare, and analyze impacts from changes implicated by section 101(a) and section 101(b) on\u2014\n**(1)**\nflexibility for employees with respect to hours, shifts, assignments and working arrangements;\n**(2)**\nrates of compensation, health care, and employee benefits;\n**(3)**\nresolution of grievances and disputes, including employers\u2019 ability to terminate and employees\u2019 right to due process;\n**(4)**\nuse of technology or algorithms, including the adoption of new technology and algorithms; and\n**(5)**\nworkplace safety and health.\n##### (c) Stakeholder input\nIn preparing the report, the Comptroller General of the United States shall gather information from impacted stakeholders, including various business enterprises and labor organizations. In developing a list of stakeholders, the Comptroller General of the United States shall consult with the House Committee on Education and Workforce and the Senate Committee on Health, Education, Labor, and Pensions.\n##### (d) Congressional report\nSix months after the commencement of the study, the Comptroller General of the United States shall transmit the findings and report to the Committee on Education and Workforce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate, and consistent with the policies of the Comptroller General of the United States, make the findings and report available to the public.\n##### (e) Presidential consideration\nThe President, in consultation with the Department of Labor and other agencies as the President deems appropriate, shall, subsequent to the issuance of such report, consider such findings, and within 60 days may recommend that the House of Representatives and the Senate modify section 101(a) or section 101(b), or both or make no recommendations.\n##### (f) Sense of Congress\nIt is the sense of Congress that Congress shall consider whether to accept, reject, or modify any recommendations received under (e), as it deems appropriate.",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-03-05",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "852",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Richard L. Trumka Protecting the Right to Organize Act of 2025",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "National Labor Relations Board (NLRB)",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-02-11T15:43:02Z"
          },
          {
            "name": "Worker safety and health",
            "updateDate": "2026-02-11T15:43:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-05-06T18:42:12Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr20ih.xml"
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
      "title": "Richard L. Trumka Protecting the Right to Organize Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Richard L. Trumka Protecting the Right to Organize Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Labor Relations Act, the Labor Management Relations Act, 1947, and the Labor-Management Reporting and Disclosure Act of 1959, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T05:18:30Z"
    }
  ]
}
```
