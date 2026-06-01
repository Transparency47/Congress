# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6145
- Title: EXPERTS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6145
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-04-21T19:17:51Z
- Update date including text: 2026-04-21T19:17:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-19 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-19 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6145",
    "number": "6145",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "J000298",
        "district": "7",
        "firstName": "Pramila",
        "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
        "lastName": "Jayapal",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "EXPERTS Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-21T19:17:51Z",
    "updateDateIncludingText": "2026-04-21T19:17:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-19T15:02:30Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NC"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "RI"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "VT"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OH"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OR"
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
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IN"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
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
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "TN"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
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
      "sponsorshipDate": "2025-11-19",
      "state": "CT"
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
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OR"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MI"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
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
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
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
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
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
      "sponsorshipDate": "2025-11-19",
      "state": "TX"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CT"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NV"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
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
      "sponsorshipDate": "2025-11-19",
      "state": "GA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
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
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "MA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "RI"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "GA"
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
      "sponsorshipDate": "2025-11-19",
      "state": "VA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
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
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "NJ"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
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
      "sponsorshipDate": "2025-11-19",
      "state": "DC"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "ME"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "WI"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OR"
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
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "PA"
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
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "NM"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NV"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "HI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-11-19",
      "state": "GA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-14",
      "state": "WA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NM"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6145ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6145\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Ms. Jayapal (for herself, Ms. Adams , Mr. Amo , Ms. Ansari , Ms. Balint , Mrs. Beatty , Ms. Bonamici , Mr. Boyle of Pennsylvania , Ms. Brownley , Mr. Carson , Mr. Casar , Ms. Chu , Ms. Clarke of New York , Mr. Cohen , Mr. Correa , Ms. Dean of Pennsylvania , Ms. DeLauro , Mr. Deluzio , Mr. DeSaulnier , Ms. Dexter , Mrs. Dingell , Mr. Espaillat , Mr. Evans of Pennsylvania , Mrs. Foushee , Mr. Frost , Mr. Garcia of California , Mr. Garc\u00eda of Illinois , Ms. Garcia of Texas , Mrs. Hayes , Mr. Horsford , Mr. Huffman , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Mr. Khanna , Mr. Krishnamoorthi , Ms. Lee of Pennsylvania , Mr. Levin , Mr. Lieu , Mr. Lynch , Mr. Magaziner , Mrs. McBath , Ms. McClellan , Ms. McCollum , Mr. McGovern , Mrs. McIver , Mr. Nadler , Ms. Norton , Ms. Omar , Ms. Pingree , Mr. Pocan , Mr. Quigley , Mrs. Ramirez , Ms. Salinas , Ms. S\u00e1nchez , Ms. Scanlon , Ms. Schakowsky , Mr. Sherman , Ms. Simon , Mr. Smith of Washington , Ms. Stansbury , Mr. Thanedar , Ms. Titus , Ms. Tlaib , Ms. Tokuda , Mr. Tonko , Ms. Underwood , Mr. Vargas , Ms. Vel\u00e1zquez , Mrs. Watson Coleman , and Ms. Williams of Georgia ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 5, United States Code, to require disclosure of conflicts of interest with respect to rulemaking, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Experts Protect Effective Rules, Transparency, and Stability Act of 2025 or the EXPERTS Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress is dependent on providing discretion to executive officials and agencies (including independent agencies) to implement its statutes. Congress provides appropriate oversight of the use of this discretion.\n**(2)**\nRegulatory legislation is often phrased in broad terms, with an intelligible principle, to empower agencies to address issues, such as those presented by technological, scientific, or social developments that were not precisely foreseen when the legislation was enacted, and to draw upon the agency's specialized knowledge, experience, and responsibility for implementing the statute.\n**(3)**\nSuch broad authorizing language is often necessary to empower the administering agency to take effective action when new or unforeseen issues arise, provided that the rule does not exceed clear limits in statute nor implement it in an impermissible manner.\n**(4)**\nA rule that an agency has adopted to implement a broadly worded regulatory statute should generally not be held to be invalid on the basis that Congress has not addressed the agency\u2019s proposed course of action in specific terms.\n**(5)**\nA rule that an agency has adopted to implement a regulatory statute should generally not be held to be invalid on the basis that the agency has not previously adopted a similar rule or scheme of regulation.\n**(6)**\nThe expectation that a rule will have broad economic, political, or social significance, should not, standing alone, negate application of the principle stated in paragraph (1), (2), or (3).\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nagency economic analyses of regulatory actions commonly underestimate the benefits of regulatory actions that protect public health and safety and overestimate the costs of regulatory action to industry;\n**(2)**\nagency regulatory actions often fail to adequately consider the distributional effects and social equity impact of regulatory action; and\n**(3)**\nan agency shall prioritize the statutory direction of Congress when taking regulatory action.\n#### 4. Disclosure of conflicts of interest\nSection 553 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby striking After notice required and inserting the following:\n(1) After notice required ;\n**(B)**\nin the first sentence of paragraph (1), as so designated, by inserting , subject to subsections (f) and (h), after the agency shall ; and\n**(C)**\nby adding at the end the following:\n(2) In the case of any submission under paragraph (1) by an interested person that includes a scientific, economic, or technical study or research (or a citation thereto) that the interested person funded directly or indirectly, or the nonpublic results of any scientific, economic, or technical study or research that the interested person funded directly or indirectly, the interested person shall disclose to the agency the following: (A) The amount of any funds that were received by the person who conducted the study or research. (B) The entity that provided the funds referred to in subparagraph (A). (C) Any entity that was allowed to review or revise the study or research, and the extent of that review or revision. (D) Any financial relationship between the person who conducted the study or research, and any person that would be affected by the proposed rule. ; and\n**(2)**\nby adding at the end the following:\n(f) With respect to any submission by an interested person under subsection (c) or any other submission by an interested person relating to a proposed rule or final rule that includes a scientific, economic, or technical study or research by the interested person not published in a publicly available peer-reviewed publication, or any result of a scientific, economic, or technical study or research by the interested person not published in a publicly available peer-reviewed publication, the interested person, in making that submission, shall disclose to the agency\u2014 (1) the source of any funding for the study or research, as applicable; (2) any entity that sponsored the study or research; (3) the extent to which the findings of the study or research were reviewed by a person that may be affected by the rulemaking to which the submission relates; (4) the identity of any person identified under paragraph (3); and (5) the nature of any financial relationship, including a consulting agreement, the support of any expert witness, and the funding of research, between any person that conducted the study or research and any interested person with respect to the rulemaking to which the submission relates. .\n#### 5. Increasing disclosures relating to studies and research\nSection 553 of title 5, United States Code, as amended by section 4 of this Act, is amended by adding at the end the following:\n(g) With respect to a study or research that is submitted by an interested person to an agency under subsection (c), the agency shall ensure that the study or research is available to the public (including on the Internet website of the agency and on the public docket of the agency for the rulemaking) unless disclosure is exempted or excluded under section 552. (h) (1) If a study or research submitted by an interested person to an agency under subsection (c) presents a conflict described in paragraph (2), the agency shall disclose the conflict to the public on the internet website of the agency and on the public docket of the agency, and by publication in the Federal Register, unless disclosure is exempted or excluded under section 552. (2) A conflict described in this subsection means a study or research for which\u2014 (A) not less than 10 percent of the funding for the study or research is from an entity subject to the jurisdiction of the agency with respect to that rulemaking; or (B) an entity subject to the jurisdiction of the agency with respect to that rulemaking that is regulated by the agency conducts, reviews, or revises the study or research. (i) In the case of a violation of the requirement to make a disclosure\u2014 (1) under subsection (c)(2) or subsection (f) with respect to a submission; or (2) under subsection (h) with respect to a conflict related to a submission referred to under subsection (g), the agency may exclude from consideration or otherwise disregard the submission, and the agency has no obligation to respond to the submission, except that the submission may be remade with required disclosures during the opportunity for participation referred to in subsection (c)(1). Nothing in this subsection may be construed to affect the level of deference (in accordance with applicable law) accorded to agency action by a court reviewing such action. .\n#### 6. Disclosure of inter-governmental rule change\nWith respect to any material provided to the Office with regard to a regulatory action for purposes of centralized review of regulatory actions, the agency shall\u2014\n**(1)**\nnot later than the date on which the agency publishes a general notice of proposed rulemaking required under section 553(b) of title 5, United States Code, with respect to the action, place in the rulemaking docket\u2014\n**(A)**\nthe substance of any change between the text of any draft regulatory action that the agency provided to the Office and the text published in the general notice with respect to the action; and\n**(B)**\na statement regarding whether any change described in subparagraph (A) was made as a result of communication with\u2014\n**(i)**\nthe Office;\n**(ii)**\nanother agency; or\n**(iii)**\nany other Federal official; and\n**(2)**\nnot later than the date on which the agency publishes the regulatory action in the Federal Register, place in the rulemaking docket\u2014\n**(A)**\nthe substance of any changes between the text of the regulatory action that the agency provided to the Office and the text of the regulatory action that the agency published in the Federal Register; and\n**(B)**\na statement regarding whether any change described in subparagraph (A) was made as a result of communication with\u2014\n**(i)**\nthe Office;\n**(ii)**\nanother agency; or\n**(iii)**\nany other Federal official.\n#### 7. Justification of withdrawn rules\n##### (a) In general\nIf an agency withdraws a regulatory action after providing the action to the Office under section 6(a)(3) of the Executive Order 12866 (or, if the agency does not provide the regulatory action to the Office under that section, after publishing the general notice of proposed rulemaking with respect to the action under section 553(b) of title 5, United States Code), the agency shall publish in the Federal Register, on the public docket of the agency, and on the internet website of the agency a statement regarding the decision by the agency to withdraw the action.\n##### (b) Contents\nA statement required under subsection (a) with respect to a decision by an agency to withdraw a regulatory action shall include, at a minimum\u2014\n**(1)**\na detailed explanation of the reasons that the agency withdrew the action; and\n**(2)**\nan explanation regarding whether the decision by the agency to withdraw the action was based, in whole or in part, on a request by, or input from\u2014\n**(A)**\nthe Office;\n**(B)**\nanother agency; or\n**(C)**\nany other Federal official.\n#### 8. Negotiated rulemaking\n##### (a) In general\nSubchapter III of chapter 5 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 561, in the first sentence, by inserting between agencies and Federal, State, local, or tribal governments. This subchapter shall apply only to informal negotiations between Federal, State, local, or tribal governments after informal rule making process ;\n**(2)**\nin section 563\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (2), by inserting Federal, State, local, or tribal government after identifiable ; and\n**(ii)**\nin paragraph (3), by striking persons who and inserting representatives of Federal, State, local, and tribal governments that ; and\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nin subparagraph (A)\u2014\n**(aa)**\nby striking persons who and inserting Federal, State, local, or tribal governments that ; and\n**(bb)**\nby striking , including residents of rural areas ; and\n**(II)**\nin subparagraph (B)\u2014\n**(aa)**\nby striking with such persons and inserting with representatives of those governments ; and\n**(bb)**\nby striking to such persons and inserting to those governments ; and\n**(ii)**\nin paragraph (2), in the second sentence\u2014\n**(I)**\nby striking persons who and inserting representatives of Federal, State, local, or tribal governments that ; and\n**(II)**\nby striking , including residents of rural areas ;\n**(3)**\nin section 564\u2014\n**(A)**\nin the section heading, by striking ; applications for membership on committees ;\n**(B)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (4), by striking the person or persons and inserting the representatives of Federal, State, local, and tribal governments ;\n**(ii)**\nin paragraph (6), by adding and at the end;\n**(iii)**\nin paragraph (7), by striking ; and and inserting a period; and\n**(iv)**\nby striking paragraph (8);\n**(C)**\nby striking subsection (b);\n**(D)**\nby redesignating subsection (c) as subsection (b); and\n**(E)**\nin subsection (b), as so redesignated\u2014\n**(i)**\nin the subsection heading, by striking and applications ; and\n**(ii)**\nby striking and applications ;\n**(4)**\nin section 565(a)\u2014\n**(A)**\nin paragraph (1), in the first sentence, by striking and applications ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking and applications ; and\n**(ii)**\nby striking publications, and all that follows through the period at the end and inserting publications. ; and\n**(5)**\nin section 569(a), in the first sentence\u2014\n**(A)**\nby striking and encourage agency use of ; and\n**(B)**\nby inserting between Federal, State, local, and tribal governments after negotiated rule making .\n##### (b) Technical and conforming amendments\n**(1) Balanced Budget Act of 1997**\nSection 1856(b)(1) of the Balanced Budget Act of 1997 ( 42 U.S.C. 1395w\u201326 ) is amended by striking , using a negotiated rule making process under subchapter III of chapter 5 of title 5, United States Code .\n**(2) Elementary and secondary education act of 1965**\nThe Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6301 et seq. ) is amended\u2014\n**(A)**\nin section 1601 ( 20 U.S.C. 6571 )\u2014\n**(i)**\nin subsection (a), by striking subsections (b) through (d) and inserting subsection (b) ;\n**(ii)**\nby striking subsections (b) and (c); and\n**(iii)**\nby redesignating subsections (d) and (e) as subsections (b) and (c), respectively;\n**(B)**\nby repealing section 1602 ( 20 U.S.C. 6572 ); and\n**(C)**\nin section 8204(c)(1) ( 20 U.S.C. 7824(c)(1) ), by striking using a negotiated rulemaking process to develop regulations for implementation no later than the 2017\u20132018 academic year, shall define and inserting shall, for implementation no later than the 2017\u20132018 academic year, define .\n**(3) Health insurance portability and accountability act of 1996**\nSection 216(b) of the Health Insurance Portability and Accountability Act of 1996 (42 U.S.C. 1320a\u20137b note) is amended to read as follows:\n(b) Rulemaking for risk-Sharing exception (1) Establishment The Secretary of Health and Human Services (in this subsection referred to as the Secretary ) shall establish standards relating to the exception for risk-sharing arrangements to the anti-kickback penalties described in section 1128B(b)(3)(F) of the Social Security Act, as added by subsection (a). (2) Factors to consider In establishing standards relating to the exception for risk-sharing arrangements to the anti-kickback penalties under paragraph (1), the Secretary\u2014 (A) shall consult with the Attorney General and representatives of the hospital, physician, other health practitioner, and health plan communities, and other interested parties; and (B) shall take into account\u2014 (i) the level of risk appropriate to the size and type of arrangement; (ii) the frequency of assessment and distribution of incentives; (iii) the level of capital contribution; and (iv) the extent to which the risk-sharing arrangement provides incentives to control the cost and quality of health care services. .\n**(3) Higher education act of 1965**\nThe Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) is amended\u2014\n**(A)**\nin section 207\u2014\n**(i)**\nby striking subsection (c); and\n**(ii)**\nby redesignating subsection (d) as subsection (c);\n**(B)**\nin section 422(g)(1)\u2014\n**(i)**\nin subparagraph (B), by adding and at the end;\n**(ii)**\nin subparagraph (C), by striking ; and and inserting a period; and\n**(iii)**\nby striking subparagraph (D);\n**(C)**\nin section 487A(b)(3)(B), by striking as determined in the negotiated rulemaking process under section 492 ;\n**(D)**\nin section 491(l)(4)(A), by striking , not later than two years after the completion of the negotiated rulemaking process required under section 492 resulting from the amendments to this Act made by the Higher Education Opportunity Act, ; and\n**(E)**\nin section 492\u2014\n**(i)**\nin the section heading, by striking Negotiated ; and\n**(ii)**\nby amending subsection (b) to read as follows:\n(b) Issuance of regulations After obtaining the advice and recommendations described in subsection (a)(1), the Secretary shall issue final regulations within the 360-day period described in section 437(e) of the General Education Provisions Act ( 20 U.S.C. 1232(e) ). .\n**(4) Housing Act of 1949**\nSection 515(r)(3) of the Housing Act of 1949 ( 42 U.S.C. 1485(r)(3) ) is amended by striking in accordance with and all that follows through the period at the end and inserting under the rulemaking authority contained in section 553 of title 5, United States Code. .\n**(5) Magnuson-stevens fishery conservation and management act**\nSection 305(g) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1855(g) ) is amended\u2014\n**(A)**\nby striking paragraphs (2) and (3);\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking (A) ; and\n**(ii)**\nby redesignating subparagraph (B) as paragraph (2) and adjusting the margins accordingly; and\n**(C)**\nin paragraph (2), as so redesignated, by striking the second sentence.\n**(6) Mandatory price reporting act of 2010**\nSection 2(b) of the Mandatory Price Reporting Act of 2010 ( Public Law 111\u2013239 ; 124 Stat. 2501) is amended\u2014\n**(A)**\nby striking Wholesale pork cuts and all that follows through chapter 3 and inserting Wholesale pork cuts .\u2014Chapter 3 ; and\n**(B)**\nby striking paragraphs (2), (3), and (4).\n**(7) Patient protection and affordable care act**\nSection 5602 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 254b note) is amended\u2014\n**(A)**\nin the section heading, by striking Negotiated ;\n**(B)**\nby striking subsections (b) through (h);\n**(C)**\nin subsection (a)\u2014\n**(i)**\nby redesignating paragraph (2) as subsection (b) and adjusting the margins accordingly; and\n**(ii)**\nby striking Establishment .\u2014 and all that follows through The Secretary of Health and Human Services and inserting Establishment .\u2014The Secretary of Health and Human Services ;\n**(iii)**\nby striking , through a negotiated rulemaking process under subchapter 3 of chapter 5 of title 5, United States Code, ; and\n**(iv)**\nin paragraph (1), by redesignating subparagraphs (A) and (B) as paragraphs (1) and (2), respectively, and adjusting the margins accordingly; and\n**(D)**\nin subsection (b), as so redesignated, by striking paragraph (1) and inserting subsection (a) .\n**(8) Price-anderson amendments act of 1988**\nSection 19 of the Price-Anderson Amendments Act of 1988 ( 42 U.S.C. 2210 note) is amended\u2014\n**(A)**\nby striking subsection (b); and\n**(B)**\nin subsection (a)\u2014\n**(i)**\nby striking Purpose .\u2014The Nuclear and inserting Rulemaking Proceeding.\u2014 The Nuclear ; and\n**(ii)**\nby redesignating paragraph (2) as subsection (b) and adjusting the margins accordingly.\n**(9) Social security act**\nTitle XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) is amended\u2014\n**(A)**\nin section 1834(l)(1) ( 42 U.S.C. 1395m(l)(1) ), by striking through a negotiated rulemaking process described in title 5, United States Code, ; and\n**(B)**\nin section 1856(a) ( 42 U.S.C. 1395w\u201326(a) );\n**(i)**\nby striking paragraphs (2) through (9);\n**(ii)**\nin paragraph (1)\u2014\n**(I)**\nby striking Establishment.\u2014 and all that follows through The Secretary shall establish and inserting Establishment.\u2014 The Secretary shall establish ;\n**(II)**\nby striking and using a negotiated rulemaking process under subchapter III of chapter 5 of title 5, United States Code ; and\n**(III)**\nby redesignating subparagraphs (B) and (C) as paragraphs (2) and (3), respectively, and adjusting the margins accordingly; and\n**(iii)**\nin paragraph (2), as so redesignated\u2014\n**(I)**\nby striking subparagraph (A) and inserting paragraph (1) ; and\n**(II)**\nby redesignating clauses (i), (ii), and (iii) as subparagraphs (A), (B), and (C), respectively, and adjusting the margins accordingly.\n**(10) Title 5**\nThe table of sections for subchapter III of chapter 5 of title 5, United States Code, is amended by striking the item relating to section 564 and inserting the following:\n564. Publication of notice. .\n**(11) Title 49**\nSection 31136(g)(1) of title 49, United States Code, is amended\u2014\n**(A)**\nby striking shall\u2014 and all that follows through issue and inserting shall issue ;\n**(B)**\nby striking ; or and inserting a period; and\n**(C)**\nby striking subparagraph (B).\n**(12) Toxic substances control act**\nSection 8(a) of the Toxic Substances Control Act ( 15 U.S.C. 2607(a) ) is amended\u2014\n**(A)**\nby striking paragraph (6); and\n**(B)**\nby redesignating paragraph (7) as paragraph (6).\n**(13) United states housing act of 1937**\nSection 9 of the United States Housing Act of 1937 ( 42 U.S.C. 1437g ) is amended by repealing subsection (f).\n#### 9. Streamlining OIRA review\n##### (a) In general\nExcept as provided in subsection (b), if the Office commences a review of a significant regulatory action, the Office shall complete such review not more than 60 days after the date on which the Office receives the significant regulatory action.\n##### (b) Extension\nThe Office may extend the 60-day period described in subsection (a) by a single 30-day period if the Office provides the agency with, and makes publicly available, a written justification for the extension.\n##### (c) Publication of regulatory action\nIf the Office waives review of a significant regulatory action of an agency without a request for further consideration or does not notify the agency in writing of the results of the review within the time frame described in subsection (a) or (b), the agency may publish the significant regulatory action in the Federal Register.\n#### 10. Penalizing public companies that submit false information to agencies\nSection 553 of title 5, United States Code, as amended by sections 4 and 5 of this Act, is amended by adding at the end the following:\n(j) (1) Any entity required to file an annual report under section 13 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m ) that makes a submission under subsection (c) knowing the same\u2014 (A) to include any materially false, fictitious, or fraudulent statement or representation; or (B) to omit any material fact resulting in any statement or representation being false or misleading, shall be subject a civil penalty of not less than $250,000 for a first violation. (2) Any entity that has a subsequent violation of paragraph (1) shall be subject to a civil penalty of not less than $1,000,000 for each subsequent violation. (3) Any submission in violation of this subsection may be excluded from the record and from consideration by the agency or otherwise disregarded, and such submission (or any amendment to such submission) may not be resubmitted thereafter. An exclusion or other disregard of a submission pursuant to this subsection shall not affect the level of deference (in accordance with applicable law) accorded to agency action by a court reviewing such action. (k) Any entity required to file an annual report pursuant to section 13 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m ), shall include in a submission under subsection (c)(2) of this section the annual report filed in the year previous to such submission and the quarterly report filed most recently prior to such submission. .\n#### 11. Establishment of the office of the public advocate\nSubchapter I of chapter 5 of title 5, United States Code, is amended\u2014\n**(1)**\nby adding at the end the following:\n505. Office of the Public Advocate (a) Establishment There is established in the Office of Management and Budget an office to be known as the Office of the Public Advocate . (b) National Public Advocate The Office of the Public Advocate shall be under the supervision of an official to be known as the National Public Advocate , who shall\u2014 (1) be appointed by the President, by and with the advice and consent of the Senate; (2) report to the President; (3) be entitled to compensation at the same rate as the highest rate of basic pay established for the Senior Executive Service under section 5382; (4) have a background in customer service, consumer protection, or administrative law; and (5) have experience working with the public in cases involving rules (as defined in section 551). (c) Duties The duties of the Office of the Public Advocate shall include\u2014 (1) assisting agencies in soliciting public participation in the rulemaking process; (2) assisting individuals in participating in the rulemaking process; (3) working with agencies, Congress, and the public to identify problems and improve public participation in the rulemaking process; (4) conducting and publishing research on social equity impacts of the rulemaking process; (5) developing and coordinating social equity definitions across the executive branch; (6) when requested by the agency or by the public through comments submitted through the process described in section 553 of title 5, United States Code, performing, not later than 30 days after the receipt of such a request, a social equity assessment (as such term is defined in the Stop Corporate Capture Act) for a proposed rule; and (7) facilitating means by which individuals and populations that have not historically participated in the rulemaking process may be better included in the rulemaking process, including by\u2014 (A) recommending and implementing new outreach plans; (B) partnering with State, local, and Tribal governments, and with community-based organizations to propagate information about rules changes; and (C) ensuring information about agency rulemaking and changes to rules are written in clear, accessible language that is accessible in multiple languages. (d) Rulemaking Not later than 180 days after the date on which the National Public Advocate is appointed under this subsection or 180 days after the date of enactment of this section, whichever is later, the National Public Advocate shall make rules to carry out this section. ; and\n**(2)**\nin the table of sections for such chapter, by inserting after the item relating to section 504 the following:\n505. Office of the Public Advocate. .\n#### 12. Scope of review\nSection 706 of title 5, United States Code, is amended\u2014\n**(1)**\nin the first sentence of the matter preceding paragraph (1)\u2014\n**(A)**\nby striking agency action. and inserting agency action. If a statute that an agency administers is silent or ambiguous as to the proper construction of a particular term or provision or set of terms or provisions, and an agency has followed the applicable procedures in subchapter II of chapter 5, has otherwise lawfully adjudicated a matter, or has followed the corresponding procedural provisions of the relevant statute, as applicable, a reviewing court shall defer to the agency\u2019s reasonable or permissible interpretation of that statute, regardless of the significance of the related agency action or a possible future agency action. ; and\n**(B)**\nby striking To the extent necessary and inserting:\n(a) In general To the extent necessary ; and\n**(2)**\nby adding at the end the following:\n(b) Unreasonable delay For purposes of subsection (a)(1), unreasonable delay shall include\u2014 (1) when an agency has not issued a notice of proposed rulemaking before the date that is 1 year after the date of enactment of the legislation mandating the rulemaking, where no deadline for the rulemaking was specified in the enacted law; (2) when an agency has not issued a final version of a proposed rule before the date that is 1 year after the date on which the proposed rule was published in the Federal Register; (3) when an agency has not implemented a final rule before the date that is 1 year after the implementation date published in the Federal Register or, if no implementation date was provided, before the date that is 1 year after the date on which the final rule was published in the Federal Register; and (4) when an agency has not issued or implemented a final rule, upon a showing of good cause therefor. .\n#### 13. Right of review\n##### (a) In General\nChapter 7 of title 5, United States Code, is amended by adding at the end the following:\n707. Statute of limitation Except as otherwise expressly provided by law, an action under this chapter for review of an agency action shall be commenced not later than 6 years after the date of the final agency action. .\n##### (b) Conforming amendment\nSection 2401(a) of title 28, United States Code, is amended by inserting or section 707 of title 5 after title 41 .\n##### (c) Clerical amendment\nThe table of contents for chapter 7 of title 5, United States Code, is amended by adding at the end the following:\n707. Statute of limitation. .\n#### 14. Expanding public awareness of rulemakings\n##### (a) In general\nSection 553 of title 5, United States Code, as amended by section 4, 5, and 10 of this Act, is amended by adding at the end the following:\n(l) (1) The head of each agency shall take such actions as may be necessary to\u2014 (A) expand public awareness of the initiation of each rulemaking proceeding; (B) expand public awareness of the publication of each proposed rule; (C) expand public awareness when a rule is published; and (D) establish a participation log, including all rulemaking participants, with respect to each rulemaking. (2) Not later than two business days after the date on which an agency publishes a notice of proposed rulemaking or a final rule under this section, the agency shall notify interested persons of the publication, including by using contact information that interested persons have provided to the agency and by publishing such notice on the agency's website and any social media accounts. .\n##### (b) Effective date\nThe amendment made by this section shall take effect beginning on the date that is 30 days after the date of enactment of this Act.\n#### 15. Public petitions\nSection 553(e) of title 5, United States Code, is amended\u2014\n**(1)**\nby inserting (1) before Each agency ; and\n**(2)**\nby adding at the end the following:\n(2) Not later than 60 days after the date on which an agency receives more than 100,000 signatures on a single petition under paragraph (1), the agency shall provide a written response that includes\u2014 (A) an explanation of whether the agency has engaged or is engaging in the requested issuance, amendment, or repeal of a rule; and (B) if the agency has not engaged in the requested issuance, amendment, or repeal of a rule, a written explanation for not engaging in the requested issuance, amendment, or repeal. (3) Not later than 30 days after the date of enactment of this paragraph, the head of each agency shall establish and publish procedures for the processing of a petition under paragraph (1), including\u2014 (A) using the agency website, the Federal Register, and other Federal websites to educate the public about how to file a petition under paragraph (1); and (B) creating an accessible docket on the internet website of the agency, or on any existing Government-wide internet website, of any petition filed under paragraph (1). (4) No agency action under paragraph (3) shall be subject to review under chapter 7. .\n#### 16. Amendment to congressional review act\nSection 801(b) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking (1) ; and\n**(2)**\nby striking paragraph (2).\n#### 17. Reinstatement of disapproved rules\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term covered rule means a rule for which a joint resolution of disapproval was enacted under chapter 8 of title 5, United States Code, before the date of enactment of this Act; and\n**(2)**\nthe term Federal agency has the meaning given the term agency in section 551(1) of title 5, United States Code.\n##### (b) Fast-Track reinstatement\nA Federal agency may reinstate a covered rule by publishing the covered rule in the Federal Register during the 1-year period beginning on the date of enactment of this Act.\n##### (c) Reinstatement after 1-Year period\nAfter the end of the 1-year period beginning on the date of enactment of this Act, a Federal agency may reinstate a covered rule using the rulemaking procedures described in section 553 of title 5, United States Code.\n#### 18. Cost-benefit analysis\n##### (a) Requirement of regulatory impact\nIf an agency is performing a cost-benefit or regulatory impact analysis in the course of issuing a rule, the agency shall\u2014\n**(1)**\ntake into account the benefits of the rule to the public, including the nonquantifiable benefits of the rule; and\n**(2)**\nexcept for good cause shown, prioritize adoption of a rule that provides benefits to the public, including nonquantifiable benefits.\n##### (b) Requirement of distributional effects\nAn agency shall agency shall take into account distributional effects and the social equity impact of a rule when issuing such rule.\n##### (c) Scope of review\nSection 706 of title 5, United States Code, as amended by section 12, is amended in subsection (a), as so designated, by inserting after prejudicial error. the following: When acting under paragraph (2)(A), the court shall not require an agency to demonstrate that the challenged action meets a cost-benefit analysis standard except where explicitly required by law. .\n#### 19. Definitions\nIn this Act:\n**(1) Agency; rule**\nThe terms agency and rule have the meanings given such terms in section 551 of title 5, United States Code.\n**(2) Interested person**\nThe term interested person includes individuals, partnerships, corporations, associations, or public or private organizations of any character other than an agency.\n**(3) Office**\nThe term Office means the Office of Information and Regulatory Affairs of the Office of Management and Budget.\n**(4) Regulatory action**\nThe term regulatory action means any substantive action by an agency that promulgates or is expected to lead to the promulgation of a final rule or regulation, including notices of inquiry, advance notices of proposed rulemaking, and notices of proposed rulemaking.\n**(5) Significant regulatory action**\nThe term significant regulatory action means any regulatory action that is likely to result in a rule that may\u2014\n**(A)**\nhave an annual effect on the economy of $100,000,000 or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities;\n**(B)**\ncreate a serious inconsistency or otherwise interfere with an action taken or planned by another agency;\n**(C)**\nmaterially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or\n**(D)**\nraise novel legal or policy issues arising out of legal mandates, the President\u2019s priorities, or the general principles of regulation customarily practiced by the executive branch.\n**(6) Social equity impact**\nThe term social equity impact means any impact of a proposed rule, whether intended or unintended, that might reasonably be expected to disproportionately affect a population of interested persons that is part of a protected class or set of protected classes, based on the rules\u2019s plain language, stated intention, and based on credible statistical projections and data on the impacts of similar rules, laws, and policies.\n**(7) Social equity assessment**\nThe term social equity assessment means a written and publicly available report that shall specifically consider any social equity impact, positive or negative, that the proposed policy might have on a population of interested persons who share a common characteristic that renders them part of a protected class, where that population was previously subjected to discriminatory or exclusionary practices by the agency promulgating the rule or where credible demographic evidence demonstrates significant disparities experienced by different populations within a protected class.",
      "versionDate": "2025-11-19",
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
        "actionDate": "2025-11-19",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3210",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "EXPERTS Act of 2025",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-11-25T19:30:48Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6145ih.xml"
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
      "title": "EXPERTS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EXPERTS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Experts Protect Effective Rules, Transparency, and Stability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to require disclosure of conflicts of interest with respect to rulemaking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-20T10:48:19Z"
    }
  ]
}
```
