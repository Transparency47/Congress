# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/609?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/609
- Title: Assuring Medicare’s Promise Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 609
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-05-19T13:47:56Z
- Update date including text: 2026-05-19T13:47:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/609",
    "number": "609",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000399",
        "district": "37",
        "firstName": "Lloyd",
        "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
        "lastName": "Doggett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Assuring Medicare\u2019s Promise Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-19T13:47:56Z",
    "updateDateIncludingText": "2026-05-19T13:47:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sponsorshipDate": "2025-01-22",
      "state": "NC"
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
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
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CO"
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "PA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MI"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "LA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
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
      "sponsorshipDate": "2025-01-22",
      "state": "AZ"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "WI"
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
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
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
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
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
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
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NV"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "AL"
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
      "sponsorshipDate": "2025-03-06",
      "state": "MA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "AZ"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
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
      "sponsorshipDate": "2025-08-08",
      "state": "CT"
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
      "sponsorshipDate": "2025-09-02",
      "state": "NM"
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
      "sponsorshipDate": "2026-02-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr609ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 609\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Doggett (for himself, Ms. Adams , Ms. Barrag\u00e1n , Mr. Boyle of Pennsylvania , Ms. Brownley , Mr. Carson , Mr. Casar , Mr. Castro of Texas , Ms. Chu , Mr. Cohen , Mr. Davis of Illinois , Ms. DeGette , Ms. DeLauro , Mr. Deluzio , Mrs. Dingell , Ms. Escobar , Mr. Espaillat , Mr. Fields , Mr. Frost , Mr. Garamendi , Mr. Goldman of New York , Mr. Grijalva , Mr. Huffman , Ms. Jayapal , Mr. Johnson of Georgia , Mr. Khanna , Ms. Lee of Pennsylvania , Mr. Levin , Ms. Moore of Wisconsin , Ms. Norton , Ms. Ocasio-Cortez , Ms. Pingree , Mr. Pocan , Mrs. Ramirez , Ms. Salinas , Ms. S\u00e1nchez , Ms. Schakowsky , Ms. Tlaib , Mr. Tonko , Mr. Turner of Texas , Mr. Veasey , Ms. Vel\u00e1zquez , Ms. Williams of Georgia , and Ms. Wilson of Florida ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Social Security Act and the Internal Revenue Code of 1986 to include net investment income tax imposed in the Federal Hospital Insurance Trust Fund and to modify the net investment income tax.\n#### 1. Short title\nThis Act may be cited as the Assuring Medicare\u2019s Promise Act of 2025 .\n#### 2. Inclusion of net investment income tax in Hospital Insurance Trust Fund\n##### (a) In general\nSection 1817(a) of the Social Security Act ( 42 U.S.C. 1395i(a) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (1);\n**(2)**\nby striking the period at the end of paragraph (2) and inserting ; and ; and\n**(3)**\nby inserting after paragraph (2) the following new paragraph:\n(3) the taxes imposed by section 1411 of the Internal Revenue Code of 1986 reported to the Secretary of the Treasury or the Secretary\u2019s delegate on tax returns under subtitle F of such Code. .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to taxes imposed for taxable years beginning after December 31, 2025.\n#### 3. Application of net investment income tax to trade or business income of certain high income individuals\n##### (a) In general\nSection 1411 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(f) Application to certain high income individuals (1) In general In the case of any individual whose modified adjusted gross income for the taxable year exceeds the high income threshold amount, subsection (a)(1) shall be applied by substituting the greater of specified net income or net investment income for net investment income in subparagraph (A) thereof. (2) Phase-in of increase The increase in the tax imposed under subsection (a)(1) by reason of the application of paragraph (1) of this subsection shall not exceed the amount which bears the same ratio to the amount of such increase (determined without regard to this paragraph) as\u2014 (A) the excess described in paragraph (1), bears to (B) $100,000 ( \u00bd such amount in the case of a married taxpayer (as defined in section 7703) filing a separate return). (3) High income threshold amount For purposes of this subsection, the term high income threshold amount means\u2014 (A) except as provided in subparagraph (B) or (C), $400,000, (B) in the case of a taxpayer making a joint return under section 6013 or a surviving spouse (as defined in section 2(a)), $500,000, and (C) in the case of a married taxpayer (as defined in section 7703) filing a separate return, \u00bd of the dollar amount determined under subparagraph (B). (4) Specified net income For purposes of this section, the term specified net income means net investment income determined\u2014 (A) without regard to the phrase other than such income which is derived in the ordinary course of a trade or business not described in paragraph (2), in subsection (c)(1)(A)(i), (B) without regard to the phrase described in paragraph (2) in subsection (c)(1)(A)(ii), (C) without regard to the phrase other than property held in a trade or business not described in paragraph (2) in subsection (c)(1)(A)(iii), (D) without regard to paragraphs (2), (3), and (4) of subsection (c), and (E) by treating paragraphs (5) and (6) of section 469(c) (determined without regard to the phrase To the extent provided in regulations, in such paragraph (6)) as applying for purposes of subsection (c) of this section. .\n##### (b) Application to trusts and estates\nSection 1411(a)(2)(A) of such Code is amended by striking undistributed net investment income and inserting the greater of undistributed specified net income or undistributed net investment income .\n##### (c) Clarifications with respect to determination of net investment income\n**(1) Certain exceptions**\nSection 1411(c)(6) of such Code is amended to read as follows:\n(6) Special rules Net investment income shall not include\u2014 (A) any item taken into account in determining self-employment income for such taxable year on which a tax is imposed by section 1401(b), (B) wages received with respect to employment on which a tax is imposed under section 3101(b) or 3201(a) (including amounts taken into account under section 3121(v)(2)), and (C) wages received from the performance of services earned outside the United States for a foreign employer. .\n**(2) Net operating losses not taken into account**\nSection 1411(c)(1)(B) of such Code is amended by inserting (other than section 172) after this subtitle .\n**(3) Inclusion of certain foreign income**\n**(A) In general**\nSection 1411(c)(1)(A) of such Code is amended by striking and at the end of clause (ii), by striking over at the end of clause (iii) and inserting and , and by adding at the end the following new clause:\n(iv) any amount includible in gross income under section 951, 951A, 1293, or 1296, over .\n**(B) Proper treatment of certain previously taxed income**\nSection 1411(c) of such Code is amended by adding at the end the following new paragraph:\n(7) Certain previously taxed income The Secretary shall issue regulations or other guidance providing for the treatment of\u2014 (A) distributions of amounts previously included in gross income for purposes of chapter 1 but not previously subject to tax under this section, and (B) distributions described in section 962(d). .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n##### (e) Transition rule\nThe regulations or other guidance issued by the Secretary under section 1411(c)(7) of the Internal Revenue Code of 1986 (as added by this section) shall include provisions which provide for the proper coordination and application of clauses (i) and (iv) of section 1411(c)(1)(A) with respect to\u2014\n**(1)**\ntaxable years beginning on or before December 31, 2025, and\n**(2)**\ntaxable years beginning after such date.",
      "versionDate": "2025-01-22",
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
            "name": "Financial services and investments",
            "updateDate": "2025-08-05T19:43:21Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-08-05T19:42:50Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-08-05T19:42:56Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-08-05T19:43:37Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-08-05T19:43:54Z"
          },
          {
            "name": "Income tax rates",
            "updateDate": "2025-08-05T19:43:05Z"
          },
          {
            "name": "Interest, dividends, interest rates",
            "updateDate": "2025-08-05T19:43:46Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-08-05T19:43:28Z"
          },
          {
            "name": "Taxation of foreign income",
            "updateDate": "2025-08-05T19:43:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-25T20:41:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr609",
          "measure-number": "609",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2026-05-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr609v00",
            "update-date": "2026-05-19"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Assuring Medicare\u2019s Promise Act</strong> <strong><strong>of 2025</strong></strong></p><p>This bill increases the net investment tax for certain taxpayers and appropriates revenue from the net investment tax to the Federal Hospital Insurance Trust Fund (which finances Medicare Part A). The bill also requires the Internal Revenue Service (IRS) to issue additional guidance on the net investment tax.</p><p>The bill requires individuals with a modified adjusted gross income (MAGI) exceeding $400,000 ($500,000 for joint filers and $250,000 for married individuals filing separately), estates, and trusts to pay a tax of 3.8% on the greater of their specified net income or net investment income, subject to limitations. (Under current law, individuals with a MAGI exceeding $200,000 [or $250,000 for joint filers], estates, and trusts pay a 3.8% tax on net investment income.)</p><p>The bill defines <em>specified net income</em> by expanding the definition of <em>net investment income</em> to</p><ul><li>include gross income from any trade or business (unless\u00a0subject to employment taxes), including\u00a0interest, dividends, annuities, royalties, and\u00a0rents;</li><li>include net gain from the disposition of business property;</li><li>eliminate the exclusion of income from the investment of working capital; and</li><li>eliminate the exception related to certain active partnership or S corporation interests.</li></ul><p>The bill also</p><ul><li>expands the net investment tax definition of a <em>trade or business</em>,</li><li>disallows net operating losses in calculating net investment income,\u00a0</li><li>includes certain foreign-sourced income in net investment income, and</li><li>requires the IRS to issue guidance on the treatment of certain corporate distributions for purposes of the net investment tax.</li></ul>"
        },
        "title": "Assuring Medicare\u2019s Promise Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr609.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Assuring Medicare\u2019s Promise Act</strong> <strong><strong>of 2025</strong></strong></p><p>This bill increases the net investment tax for certain taxpayers and appropriates revenue from the net investment tax to the Federal Hospital Insurance Trust Fund (which finances Medicare Part A). The bill also requires the Internal Revenue Service (IRS) to issue additional guidance on the net investment tax.</p><p>The bill requires individuals with a modified adjusted gross income (MAGI) exceeding $400,000 ($500,000 for joint filers and $250,000 for married individuals filing separately), estates, and trusts to pay a tax of 3.8% on the greater of their specified net income or net investment income, subject to limitations. (Under current law, individuals with a MAGI exceeding $200,000 [or $250,000 for joint filers], estates, and trusts pay a 3.8% tax on net investment income.)</p><p>The bill defines <em>specified net income</em> by expanding the definition of <em>net investment income</em> to</p><ul><li>include gross income from any trade or business (unless\u00a0subject to employment taxes), including\u00a0interest, dividends, annuities, royalties, and\u00a0rents;</li><li>include net gain from the disposition of business property;</li><li>eliminate the exclusion of income from the investment of working capital; and</li><li>eliminate the exception related to certain active partnership or S corporation interests.</li></ul><p>The bill also</p><ul><li>expands the net investment tax definition of a <em>trade or business</em>,</li><li>disallows net operating losses in calculating net investment income,\u00a0</li><li>includes certain foreign-sourced income in net investment income, and</li><li>requires the IRS to issue guidance on the treatment of certain corporate distributions for purposes of the net investment tax.</li></ul>",
      "updateDate": "2026-05-19",
      "versionCode": "id119hr609"
    },
    "title": "Assuring Medicare\u2019s Promise Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Assuring Medicare\u2019s Promise Act</strong> <strong><strong>of 2025</strong></strong></p><p>This bill increases the net investment tax for certain taxpayers and appropriates revenue from the net investment tax to the Federal Hospital Insurance Trust Fund (which finances Medicare Part A). The bill also requires the Internal Revenue Service (IRS) to issue additional guidance on the net investment tax.</p><p>The bill requires individuals with a modified adjusted gross income (MAGI) exceeding $400,000 ($500,000 for joint filers and $250,000 for married individuals filing separately), estates, and trusts to pay a tax of 3.8% on the greater of their specified net income or net investment income, subject to limitations. (Under current law, individuals with a MAGI exceeding $200,000 [or $250,000 for joint filers], estates, and trusts pay a 3.8% tax on net investment income.)</p><p>The bill defines <em>specified net income</em> by expanding the definition of <em>net investment income</em> to</p><ul><li>include gross income from any trade or business (unless\u00a0subject to employment taxes), including\u00a0interest, dividends, annuities, royalties, and\u00a0rents;</li><li>include net gain from the disposition of business property;</li><li>eliminate the exclusion of income from the investment of working capital; and</li><li>eliminate the exception related to certain active partnership or S corporation interests.</li></ul><p>The bill also</p><ul><li>expands the net investment tax definition of a <em>trade or business</em>,</li><li>disallows net operating losses in calculating net investment income,\u00a0</li><li>includes certain foreign-sourced income in net investment income, and</li><li>requires the IRS to issue guidance on the treatment of certain corporate distributions for purposes of the net investment tax.</li></ul>",
      "updateDate": "2026-05-19",
      "versionCode": "id119hr609"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr609ih.xml"
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
      "title": "Assuring Medicare\u2019s Promise Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Assuring Medicare\u2019s Promise Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Social Security Act and the Internal Revenue Code of 1986 to include net investment income tax imposed in the Federal Hospital Insurance Trust Fund and to modify the net investment income tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T04:48:33Z"
    }
  ]
}
```
