# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5862?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5862
- Title: American Energy Independence and Affordability Act
- Congress: 119
- Bill type: HR
- Bill number: 5862
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2026-04-09T16:01:19Z
- Update date including text: 2026-04-09T16:01:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5862",
    "number": "5862",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "American Energy Independence and Affordability Act",
    "type": "HR",
    "updateDate": "2026-04-09T16:01:19Z",
    "updateDateIncludingText": "2026-04-09T16:01:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
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
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:03:05Z",
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
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
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
      "sponsorshipDate": "2025-10-28",
      "state": "CT"
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
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-28",
      "state": "AL"
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
      "sponsorshipDate": "2025-10-28",
      "state": "WA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "WI"
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
      "sponsorshipDate": "2025-10-28",
      "state": "PA"
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
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "PA"
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
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NV"
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
      "sponsorshipDate": "2025-10-28",
      "state": "VI"
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
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "LA"
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
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "AZ"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MO"
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
      "sponsorshipDate": "2025-10-28",
      "state": "LA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "OR"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MN"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NJ"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "CO"
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
      "sponsorshipDate": "2025-10-28",
      "state": "MA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
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
      "sponsorshipDate": "2025-10-28",
      "state": "DC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NJ"
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
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "OH"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
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
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-28",
      "state": "HI"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "NC"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "RI"
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
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MD"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MN"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "GA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CO"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-28",
      "state": "NC"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CT"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NV"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "AZ"
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
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "KY"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MO"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "DE"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "PA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "WA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "IN"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "OR"
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
      "sponsorshipDate": "2025-10-28",
      "state": "MD"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "ME"
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
      "sponsorshipDate": "2025-10-28",
      "state": "IN"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "TN"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "OR"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "WA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NJ"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MI"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "KS"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MI"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "RI"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
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
      "sponsorshipDate": "2025-10-28",
      "state": "MS"
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
      "sponsorshipDate": "2025-10-28",
      "state": "NM"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NJ"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-10-28",
      "state": "MA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "WI"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "OR"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MD"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CT"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "VA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NH"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "MD"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "IL"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5862ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5862\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Thompson of California (for himself, Mr. Neal , Mr. Doggett , Mr. Larson of Connecticut , Mr. Davis of Illinois , Ms. S\u00e1nchez , Ms. Sewell , Ms. DelBene , Ms. Chu , Ms. Moore of Wisconsin , Mr. Boyle of Pennsylvania , Mr. Beyer , Mr. Evans of Pennsylvania , Mr. Schneider , Mr. Panetta , Mr. Gomez , Mr. Horsford , Ms. Plaskett , Mr. Suozzi , Mr. Fields , Ms. Barrag\u00e1n , Ms. Ansari , Mr. Tonko , Mr. Cleaver , Mr. Carter of Louisiana , Mr. Vargas , Mr. Tran , Ms. Matsui , Ms. Salinas , Ms. McCollum , Mr. Garcia of California , Mr. Norcross , Ms. Castor of Florida , Mr. Garamendi , Mr. Scott of Virginia , Mr. Lieu , Ms. DeGette , Mr. Lynch , Mrs. Cherfilus-McCormick , Ms. Norton , Mrs. McIver , Ms. Kelly of Illinois , Mr. Landsman , Ms. Simon , Mr. Casten , Mr. Goldman of New York , Ms. Tokuda , Mr. Vicente Gonzalez of Texas , Mr. Kennedy of New York , Mr. DeSaulnier , Mr. Min , Mrs. Foushee , Ms. Elfreth , Mr. Magaziner , Mr. Deluzio , Ms. Brownley , Mr. Costa , Mr. Mfume , Ms. Morrison , Mr. Mullin , Ms. Williams of Georgia , Ms. Pettersen , Ms. Lofgren , Ms. Ross , Mr. Courtney , Mr. Takano , Ms. Scholten , Mr. Espaillat , Mr. Correa , Mr. Jackson of Illinois , Ms. Schakowsky , Ms. Titus , Mr. Stanton , Ms. McClellan , Mr. McGarvey , Ms. Budzinski , Mr. Huffman , Ms. Friedman , Mr. Carbajal , Mr. Bell , Ms. McBride , Mr. Quigley , Ms. Scanlon , Ms. Randall , Mr. Carson , Ms. Bynum , Mr. Hoyer , Mr. Nadler , Mr. Torres of New York , Ms. Kamlager-Dove , Mr. Ruiz , Ms. Pingree , Mr. Mrvan , Ms. Lois Frankel of Florida , Mr. Cohen , Ms. Bonamici , Mr. Larsen of Washington , Ms. Jacobs , Mr. Gottheimer , Mr. Khanna , Ms. Garcia of Texas , Mr. Latimer , Mr. Thanedar , Ms. Johnson of Texas , Mr. Foster , Ms. Davids of Kansas , Ms. McDonald Rivet , Mr. Amo , Mr. Sorensen , Mr. Thompson of Mississippi , Ms. Stansbury , Mr. Menendez , Ms. Waters , Mr. McGovern , and Mr. Moulton ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to restore certain energy-related provisions as in effect prior to the enactment of Public Law 119\u201321 .\n#### 1. Short title, etc\n##### (a) Short title\nThis Act may be cited as the American Energy Independence and Affordability Act .\n##### (b) References to the Internal Revenue Code of 1986\nExcept as otherwise expressly provided, whenever in this Act an amendment or repeal is expressed in terms of an amendment to, or repeal of, a section or other provision, the reference shall be considered to be made to a section or other provision of the Internal Revenue Code of 1986.\n#### 2. Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title, etc.\nSec. 2. Table of contents.\nTitle I\u2014Lowering Energy Costs through All-of-the-Above Energy Production\nSec. 101. Clean energy production credit.\nSec. 102. Clean electricity investment credit.\nSec. 103. Advanced manufacturing production credit.\nSec. 104. Repeal of restriction on the extension of advance energy project credit program.\nSec. 105. Reversion of construction date for clean hydrogen production credit.\nSec. 106. Reversion of termination for residential clean energy credit.\nSec. 107. Reinstatement of special rate for sustainable aviation fuel.\nTitle II\u2014Lowering Energy Costs Through Energy Efficiency\nSec. 201. Energy efficient home improvement credit.\nSec. 202. New energy efficient home credit.\nSec. 203. Repeal of termination of new energy efficient commercial buildings deduction.\nSec. 204. Restoration of cost recovery for energy property.\nTitle III\u2014Ensuring America Leads the Way in Our Automotive Future\nSec. 301. Reversion of termination date for previously-owned vehicle credit.\nSec. 302. Reversion of termination date for clean vehicle credit.\nSec. 303. Reversion of termination date for qualified commercial clean vehicles credit.\nSec. 304. Reversion of termination date for alternative fuel vehicle refueling property credit.\nI\nLowering Energy Costs through All-of-the-Above Energy Production\n#### 101. Clean energy production credit\n##### (a) Restoration of phase-Out\nSection 45Y(d)(3) is amended by striking calendar year 2032. and inserting\nmeans the later of\u2014 (A) the calendar year in which the Secretary determines that the annual greenhouse gas emissions from the production of electricity in the United States are equal to or less than 25 percent of the annual greenhouse gas emissions from the production of electricity in the United States for calendar year 2022, or (B) 2032. .\n##### (b) Restoration of credit for wind and solar facilities\nSection 45Y(d) is amended\u2014\n**(1)**\nin paragraph (1), by striking Subject to paragraph (4), the amount and inserting The amount , and\n**(2)**\nby striking paragraph (4).\n##### (c) Restoration of credit for wind and solar leasing arrangements\nSection 45Y is amended by striking subsection (h).\n##### (d) Repeal of provision for existing studies\nSection 45Y(b)(2)(C) is amended by striking clause (iii).\n##### (e) Effective dates\nThe amendments made by this section shall take effect as if included in section 70512 of Public Law 119\u201321 .\n#### 102. Clean electricity investment credit\n##### (a) Repeal of termination for wind and solar facilities\nSection 48E(e) is amended\u2014\n**(1)**\nin paragraph (1), by striking Subject to paragraph (4), the amount and inserting The amount , and\n**(2)**\nby striking paragraph (4).\n##### (b) Restoration of credit for expenditures for wind and solar leasing arrangements\n**(1) In general**\nSection 48E is amended by striking subsection (i) and by redesignating subsections (j) and (k) as subsections (i) and (j), respectively.\n**(2) Conforming rule repeal**\nSection 50 is amended by striking subsection (e).\n##### (c) Restoration of credit for certain energy property\nSection 48(a)(2)(A)(ii) is amended by striking 0 percent and inserting 2 percent .\n##### (d) Effective dates\nThe amendments made by this section shall take effect as if included in section 70513 of Public Law 119\u201321 .\n#### 103. Advanced manufacturing production credit\n##### (a) Repeal of inclusion of metallurgical coal as an applicable critical mineral\nSection 45X(c)(6) is amended by striking subparagraph (R) and by redesignating subparagraphs (S) through (AA) as subparagraphs (R) through (ZZ), respectively.\n##### (b) Repeal of termination for wind energy components\nSection 45X(b)(3) is amended by striking subparagraph (D).\n##### (c) Conforming amendments\n**(1)**\nSection 45X(b)(1)(M) is amended by striking (2.5 percent in the case of metallurgical coal) .\n**(2)**\nThe heading of section 45X(b)(3) is amended by striking and termination .\n**(3)**\nSection 45X(b)(3)(A) is amended by striking subparagraphs (C) and (D) and inserting subparagraph (C) .\n**(4)**\nThe heading of section 45X(b)(3)(C) is amended by striking other than metallurgical coal .\n**(5)**\nThe heading of section 45X(b)(3)(C)(ii) is amended by striking other than metallurgical coal .\n**(6)**\nSection 45X(b)(3) is amended by striking subparagraph (E).\n##### (d) Effective date\nThe amendments made by this section shall take effect as if included in section 70514 of Public Law 119\u201321 .\n#### 104. Repeal of restriction on the extension of advance energy project credit program\n##### (a) In general\nSection 48C(e)(3)(C) is amended by striking shall not be increased and inserting shall be increased .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 70515 of Public Law 119\u201321 .\n#### 105. Reversion of construction date for clean hydrogen production credit\n##### (a) In general\nSection 45V(c)(3)(C) is amended by striking January 1, 2028 and inserting January 1, 2033 .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 70511 of Public Law 119\u201321 .\n#### 106. Reversion of termination for residential clean energy credit\n##### (a) In general\nSection 25D(h) is amended by striking with respect to any expenditures made after December 31, 2025 and inserting to property placed in service after December 31, 2034 .\n##### (b) Conforming amendment\nSection 25D(g) is amended by striking and at the end of paragraph (2), by striking 30 percent. at the end of paragraph (3) and inserting and before January 1, 2033, 30 percent, and by adding at the end the following new paragraphs:\n(4) in the case of property placed in service after December 31, 2032, and before January 1, 2034, 26 percent, and (5) in the case of property placed in service after December 31, 2033, and before January 1, 2035, 22 percent. .\n##### (c) Effective date\nThe amendments made by this section shall take effect as if included in section 70506 of Public Law 119\u201321 .\n#### 107. Reinstatement of special rate for sustainable aviation fuel\n##### (a) In general\nSection 45Z(a)(3) is amended to read as follows:\n(3) Special rate for sustainable aviation fuel (A) In general In the case of a transportation fuel which is sustainable aviation fuel, paragraph (2) shall be applied\u2014 (i) in the case of fuel produced at a qualified facility described in paragraph (2)(A), by substituting 35 cents for 20 cents , and (ii) in the case of fuel produced at a qualified facility described in paragraph (2)(B), by substituting $1.75 for $1.00 . (B) Sustainable aviation fuel For purposes of subparagraph (A), the term sustainable aviation fuel means liquid fuel, the portion of which is not kerosene, which is sold for use in an aircraft and which\u2014 (i) meets the requirements of\u2014 (I) ASTM International Standard D7566, or (II) the Fischer Tropsch provisions of ASTM International Standard D1655, Annex A1, and (ii) is not derived from palm fatty acid distillates or petroleum. .\n##### (b) Conforming amendment\nSection 45Z(c)(1) is amended by striking and the $1.00 amount in subsection (a)(2)(B) and inserting the $1.00 amount in subsection (a)(2)(B), the 35 cent amount in subsection (a)(3)(A)(i), and the $1.75 amount in subsection (a)(3)(A)(ii) .\n##### (c) Effective date\nThe amendments made by this section shall take effect as if included in section 70521 of Public Law 119\u201321 .\nII\nLowering Energy Costs Through Energy Efficiency\n#### 201. Energy efficient home improvement credit\n##### (a) Restoring product identification number requirement\nSection 25C(h) is amended to read as follows:\n(h) Product identification number requirement (1) In general No credit shall be allowed under subsection (a) with respect to any item of specified property placed in service after December 31, 2024, unless\u2014 (A) such item is produced by a qualified manufacturer, and (B) the taxpayer includes the qualified product identification number of such item on the return of tax for the taxable year. (2) Qualified product identification number For purposes of this section, the term qualified product identification number means, with respect to any item of specified property, the product identification number assigned to such item by the qualified manufacturer pursuant to the methodology referred to in paragraph (3). (3) Qualified manufacturer For purposes of this section, the term qualified manufacturer means any manufacturer of specified property which enters into an agreement with the Secretary which provides that such manufacturer will\u2014 (A) assign a product identification number to each item of specified property produced by such manufacturer utilizing a methodology that will ensure that such number (including any alphanumeric) is unique to each such item (by utilizing numbers or letters which are unique to such manufacturer or by such other method as the Secretary may provide), (B) label such item with such number in such manner as the Secretary may provide, and (C) make periodic written reports to the Secretary (at such times and in such manner as the Secretary may provide) of the product identification numbers so assigned and including such information as the Secretary may require with respect to the item of specified property to which such number was so assigned. (4) Specified property For purposes of this subsection, the term specified property means any qualified energy property and any property described in subparagraph (B) or (C) of subsection (c)(3). .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in the enactment of section 70505 of Public Law 119\u201321 .\n#### 202. New energy efficient home credit\n##### (a) In general\nSection 45L(h) is amended by striking acquired after June 30, 2026 and inserting acquired after December 31, 2032 .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 70508 of Public Law 119\u201321 .\n#### 203. Repeal of termination of new energy efficient commercial buildings deduction\n##### (a) In general\nSection 179D is amended by striking subsection (i).\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 70507 of Public Law 119\u201321 .\n#### 204. Restoration of cost recovery for energy property\n##### (a) In general\nSection 168(e)(3)(B)(vi) is amended\u2014\n**(1)**\nby redesignating subclauses (I) and (II) as subclauses (II) and (III), respectively, and\n**(2)**\nby inserting before subclause (II) (as so redesignated) the following subclause:\n(I) is described in subparagraph (A) of section 48(a)(3) (or would be so described if \u201csolar or wind energy\u201d were substituted for \u201csolar energy\u201d in clause (i) thereof and the last sentence of such section did not apply to such subparagraph), .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 70509 of Public Law 119\u201321 .\nIII\nEnsuring America Leads the Way in Our Automotive Future\n#### 301. Reversion of termination date for previously-owned vehicle credit\n##### (a) In general\nSection 25E(g) is amended by striking acquired after September 30, 2025 and inserting acquired after December 31, 2032 .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 70501 of Public Law 119\u201321 .\n#### 302. Reversion of termination date for clean vehicle credit\n##### (a) In general\nSection 30D(h) is amended by striking acquired after September 30, 2025 and inserting placed in service after December 31, 2032 .\n##### (b) Conforming amendments\n**(1)**\nSection 30D(e)(1)(B) is amended by striking and at the end of clause (iii), by striking the period at the end of clause (iv) and inserting , and , and by adding at the end the following clause:\n(v) in the case of a vehicle placed in service after December 31, 2026, 80 percent. .\n**(2)**\nSection 30D(e)(2)(B) is amended by striking and at the end of clause (ii), by striking the period at the end of clause (iii), and by adding at the end the following clauses:\n(iv) in the case of a vehicle placed in service during calendar year 2027, 80 percent, (v) in the case of a vehicle placed in service during calendar year 2028, 90 percent, and (vi) in the case of a vehicle placed in service after December 31, 2028, 100 percent. .\n##### (c) Effective date\nThe amendments made by this section shall take effect as if included in section 70502 of Public Law 119\u201321 .\n#### 303. Reversion of termination date for qualified commercial clean vehicles credit\n##### (a) In general\nSection 45W(g) is amended by striking September 30, 2025 and inserting December 31, 2032 .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 70503 of Public Law 119\u201321 .\n#### 304. Reversion of termination date for alternative fuel vehicle refueling property credit\n##### (a) In general\nSection 30C(i) is amended by striking June 30, 2026 and inserting December 31, 2032 .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 70504 of Public Law 119\u201321 .",
      "versionDate": "2025-10-28",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2026-04-09T16:01:19Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5862ih.xml"
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
      "title": "American Energy Independence and Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T09:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Energy Independence and Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to restore certain energy-related provisions as in effect prior to the enactment of Public Law 119-21.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:33:16Z"
    }
  ]
}
```
