# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/844?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/844
- Title: Black History is American History Act
- Congress: 119
- Bill type: HR
- Bill number: 844
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/844",
    "number": "844",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001281",
        "district": "3",
        "firstName": "Joyce",
        "fullName": "Rep. Beatty, Joyce [D-OH-3]",
        "lastName": "Beatty",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Black History is American History Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:04:45Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-31",
      "state": "GA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "OR"
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "IN"
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
      "sponsorshipDate": "2025-01-31",
      "state": "LA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "MO"
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
      "sponsorshipDate": "2025-01-31",
      "state": "SC"
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "NC"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CO"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "NC"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
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
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
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
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "NV"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MD"
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NJ"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
      "state": "DC"
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
      "sponsorshipDate": "2025-01-31",
      "state": "VI"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MA"
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
      "sponsorshipDate": "2025-01-31",
      "state": "AL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "WA"
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
      "sponsorshipDate": "2025-01-31",
      "state": "OH"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
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
      "sponsorshipDate": "2025-01-31",
      "state": "MS"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
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
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-02-07",
      "state": "OR"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
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
      "sponsorshipDate": "2025-06-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr844ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 844\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mrs. Beatty (for herself, Ms. Adams , Ms. Barrag\u00e1n , Mr. Bishop , Ms. Bonamici , Ms. Brown , Mr. Carson , Mr. Carter of Louisiana , Ms. Castor of Florida , Mrs. Cherfilus-McCormick , Ms. Clarke of New York , Mr. Cleaver , Mr. Clyburn , Mr. Davis of Illinois , Mr. Davis of North Carolina , Ms. DeGette , Mr. DeSaulnier , Mrs. Dingell , Mr. Doggett , Mr. Evans of Pennsylvania , Mrs. Foushee , Ms. Lois Frankel of Florida , Mr. Frost , Mr. Goldman of New York , Mr. Green of Texas , Mr. Grijalva , Mrs. Hayes , Mr. Horsford , Mr. Ivey , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Ms. Kamlager-Dove , Mr. Kennedy of New York , Ms. Kelly of Illinois , Mr. Larsen of Washington , Mr. Lynch , Mr. Magaziner , Mrs. McBath , Mrs. McIver , Mr. Meeks , Mr. Menendez , Ms. Meng , Ms. Norton , Ms. Plaskett , Ms. Pressley , Ms. Sewell , Ms. Strickland , Mrs. Sykes , Mr. Thanedar , Mr. Thompson of Mississippi , Ms. Tlaib , Ms. Wasserman Schultz , Ms. Underwood , Ms. Vel\u00e1zquez , Ms. Waters , Mrs. Watson Coleman , Ms. Williams of Georgia , and Ms. Wilson of Florida ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo authorize the Secretary of Education to award grants to eligible entities to carry out educational programs that include the history of peoples of African descent in the settling and founding of America, the economic and political environments that led to the development, institutionalization, and abolition of slavery and its impact on all Americans, the exploration and expansion of America, impact on and contributions to the development and enhancement of American life, United States history, literature, the economy, politics, body of laws, and culture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Black History is American History Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSince before its founding, the United States of America has benefited from and been enhanced by the integral role African Americans have played in our country\u2019s history and contributions to the world.\n**(2)**\nAfrican-American history does not begin in the Americas. It can be traced back to the great empires of West Africa beginning in A.D. 790, which aided the establishment and survival of colonies in America and the New World, generally, and fought against European oppression.\n**(3)**\nAfrican Americans have represented a significant portion of the American population from nearly 20 percent at the signing of the Declaration of Independence, almost all of whom, if not all, were victims of the largest forced deportations in recorded history, the transatlantic slave trade and resulting African diaspora. It is estimated over 10,000,000 free Africans were enslaved between the mid-fifteenth and nineteenth centuries during the diaspora.\n**(4)**\nSlavery was not abolished and African Americans not acknowledged as American citizens until the mid-nineteenth century, servitude did not abate their contributions to the settlement, growth, and development of the United States, which continued through Post-Reconstruction, Jim Crow, industrialization, World Wars and conflicts, innovation and inventiveness, constitutional progress, and every aspect of American society.\n**(5)**\nDuring the civil rights movement of the 1950s and 1960s, civil rights leaders and activists championed the fight for equal rights, including voting rights, for all African Americans.\n**(6)**\nThe seminal case of Brown v. Board of Education, decided May 17, 1954, found that the decades-old policy of separate but equal access to education was inherently unequal, and the segregation of Black public-school students was no longer the law of the land.\n**(7)**\nAfrican Americans continue to fight discrimination, structural racism, economic inequities, and benign and overt omission of the integral role they played in our country\u2019s rise to greatness.\n**(8)**\nA number of States have passed educational laws requiring Black history be incorporated into the curricula of all public schools.\n**(9)**\nCongress established the National Museum of African American History and Culture in 2003 after decades of efforts to promote and highlight the contributions of African Americans, which serves as an indication of the national importance of examining Black history. Since opening in 2016, the museum has worked to educate the public on the American story through the lens of African-American history and culture and provide educators, parents, caregivers, and students with tools and resources on the African-American experience, its national impact, race, racism, and the importance of tolerance and inclusivity.\n**(10)**\nAccording to a 2015 research study conducted by the National Museum of African American History and Culture and reported in Research into the State of African American History and Culture in K\u201312 Public Schools, key findings indicated that teachers considered Black history as influential in understanding the complexity of United States history.\n**(11)**\nThe importance of Black history is reflected in the National Assessment of Educational Progress United States History framework, from pre-colonization through contemporary America.\n**(12)**\nThe Federal Government, through support for educational activities of national museums established under Federal law, can assist teachers in efforts to incorporate historically accurate instruction on the comprehensive history of African Americans and students in their exploration of Black history as an integral part of American history.\n#### 3. American history and civics education\n##### (a) Program authorized\nSection 2231(a) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6661(a) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by inserting , which shall include Black history, after American history ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby inserting which shall include Black history, after American history, ; and\n**(B)**\nby inserting , which shall include Black history after traditional American history .\n##### (b) Presidential and Congressional academies for American History and Civics\nSection 2232 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6662 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by inserting , which shall include Black history, after American History ; and\n**(B)**\nin paragraph (2), by inserting , which shall include Black history, after American History ;\n**(2)**\nin subsection (c)(1), by inserting , which shall include Black history, after American history ;\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby inserting , which shall include Black history, after American history ;\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nby inserting , which shall include Black history, after teachers of American history ; and\n**(II)**\nby inserting , which shall include Black history, after subjects of American history ; and\n**(iii)**\nin subparagraph (B), by inserting , which shall include Black history, after American history ;\n**(B)**\nin paragraph (2), by inserting , which shall include Black history, after American history ; and\n**(C)**\nin paragraph (4), by inserting , and with the Smithsonian Institution\u2019s National Museum of African American History and Culture initiative providing programs and resources for educators and students after National Parks ; and\n**(4)**\nin subsection (f)\u2014\n**(A)**\nby inserting , which shall include Black history, after American history ;\n**(B)**\nin subparagraph (A), by inserting , which shall include Black history, after American history ; and\n**(C)**\nin subparagraph (B), by inserting , which shall include Black history, after American history .\n##### (c) National activities\nSection 2233 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6663 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting which shall include Black history, after American history, ; and\n**(2)**\nin subsection (b), by inserting which shall include Black history, after American history, .\n##### (d) National assessment of educational progress\nSection 303(b)(2)(D) of the National Assessment of Educational Progress Authorization Act ( 20 U.S.C. 9622(b)(2)(D) ) is amended by inserting (which shall include Black history) after history, .",
      "versionDate": "2025-01-31",
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
            "name": "Academic performance and assessments",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "Civics education",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "Smithsonian Institution",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-03-24T16:09:13Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-03-24T16:09:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-03T20:09:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr844",
          "measure-number": "844",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr844v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Black History is American History Act</b></p> <p>This bill requires entities (e.g., institutions of higher education, libraries, and museums), in order to be eligible for certain grants administered by the Department of Education (ED), to include Black history in their teaching of American history. It also requires Black history to be included in tests administered by the National Assessment of Educational Progress (NAEP).</p> <p>Specifically, the bill mandates the inclusion of Black history as a required component of American history for such entities to be eligible for American History and Civics Academies' competitive grants. These grants support the establishment of (1) Presidential Academies for Teachers of American History and Civics, which offer workshops to teachers of American history and civics to strengthen their knowledge and prepare them to teach in these subjects; and (2) Congressional Academies for Students of American History and Civics, which support high school students in developing an understanding of these subjects. (Currently, Black history is not a required component of American history for either academy.)</p> <p>In addition, ED must give priority to grant applicants that align their activities with programs and resources of the Smithsonian Institution's National Museum of African American History and Culture.</p> <p>The bill also requires the inclusion of Black history in tests administered by the NAEP, which measures student academic achievement in various subjects.</p>"
        },
        "title": "Black History is American History Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr844.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Black History is American History Act</b></p> <p>This bill requires entities (e.g., institutions of higher education, libraries, and museums), in order to be eligible for certain grants administered by the Department of Education (ED), to include Black history in their teaching of American history. It also requires Black history to be included in tests administered by the National Assessment of Educational Progress (NAEP).</p> <p>Specifically, the bill mandates the inclusion of Black history as a required component of American history for such entities to be eligible for American History and Civics Academies' competitive grants. These grants support the establishment of (1) Presidential Academies for Teachers of American History and Civics, which offer workshops to teachers of American history and civics to strengthen their knowledge and prepare them to teach in these subjects; and (2) Congressional Academies for Students of American History and Civics, which support high school students in developing an understanding of these subjects. (Currently, Black history is not a required component of American history for either academy.)</p> <p>In addition, ED must give priority to grant applicants that align their activities with programs and resources of the Smithsonian Institution's National Museum of African American History and Culture.</p> <p>The bill also requires the inclusion of Black history in tests administered by the NAEP, which measures student academic achievement in various subjects.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr844"
    },
    "title": "Black History is American History Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Black History is American History Act</b></p> <p>This bill requires entities (e.g., institutions of higher education, libraries, and museums), in order to be eligible for certain grants administered by the Department of Education (ED), to include Black history in their teaching of American history. It also requires Black history to be included in tests administered by the National Assessment of Educational Progress (NAEP).</p> <p>Specifically, the bill mandates the inclusion of Black history as a required component of American history for such entities to be eligible for American History and Civics Academies' competitive grants. These grants support the establishment of (1) Presidential Academies for Teachers of American History and Civics, which offer workshops to teachers of American history and civics to strengthen their knowledge and prepare them to teach in these subjects; and (2) Congressional Academies for Students of American History and Civics, which support high school students in developing an understanding of these subjects. (Currently, Black history is not a required component of American history for either academy.)</p> <p>In addition, ED must give priority to grant applicants that align their activities with programs and resources of the Smithsonian Institution's National Museum of African American History and Culture.</p> <p>The bill also requires the inclusion of Black history in tests administered by the NAEP, which measures student academic achievement in various subjects.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr844"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr844ih.xml"
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
      "title": "Black History is American History Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Black History is American History Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Education to award grants to eligible entities to carry out educational programs that include the history of peoples of African descent in the settling and founding of America, the economic and political environments that led to the development, institutionalization, and abolition of slavery and its impact on all Americans, the exploration and expansion of America, impact on and contributions to the development and enhancement of American life, United States history, literature, the economy, politics, body of laws, and culture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T05:18:36Z"
    }
  ]
}
```
