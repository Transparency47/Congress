# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2021
- Title: American Teacher Act
- Congress: 119
- Bill type: HR
- Bill number: 2021
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-04-23T08:06:53Z
- Update date including text: 2026-04-23T08:06:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2021",
    "number": "2021",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "W000808",
        "district": "24",
        "firstName": "Frederica",
        "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
        "lastName": "Wilson",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "American Teacher Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:06:53Z",
    "updateDateIncludingText": "2026-04-23T08:06:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:04:45Z",
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
      "sponsorshipDate": "2025-03-10",
      "state": "NC"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "OH"
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "IN"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "SC"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NJ"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CT"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NJ"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "CT"
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
      "sponsorshipDate": "2025-03-10",
      "state": "DC"
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
      "sponsorshipDate": "2025-03-10",
      "state": "OR"
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-10",
      "state": "MA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "OH"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "GA"
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "NJ"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
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
      "sponsorshipDate": "2025-03-10",
      "state": "IN"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "CO"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NJ"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "MN"
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
      "sponsorshipDate": "2025-03-10",
      "state": "WA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "MD"
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
      "sponsorshipDate": "2025-03-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
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
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
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
      "sponsorshipDate": "2025-03-10",
      "state": "AL"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NJ"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
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
      "sponsorshipDate": "2025-03-10",
      "state": "OH"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "HI"
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
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "GA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "PA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MO"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "OH"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
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
      "sponsorshipDate": "2025-07-10",
      "state": "IL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "DE"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "GA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MD"
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
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "AZ"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
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
      "sponsorshipDate": "2025-10-31",
      "state": "OR"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NH"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "MN"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-03-24",
      "state": "WA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2021ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2021\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Ms. Wilson of Florida (for herself, Ms. Adams , Ms. Bonamici , Ms. Brown , Mr. Carbajal , Mr. Carson , Ms. Castor of Florida , Mr. Casten , Mrs. Cherfilus-McCormick , Ms. Chu , Ms. Clarke of New York , Mr. Cleaver , Mr. Clyburn , Mrs. Watson Coleman , Mr. Courtney , Mr. Cuellar , Mr. Davis of Illinois , Ms. Dean of Pennsylvania , Ms. DeLauro , Mr. Deluzio , Mrs. Dingell , Mr. Espaillat , Mr. Evans of Pennsylvania , Mrs. Foushee , Mr. Frost , Mr. Gottheimer , Mr. Green of Texas , Mr. Grijalva , Mrs. Hayes , Ms. Norton , Ms. Hoyle of Oregon , Mr. Jackson of Illinois , Ms. Jayapal , Mr. Johnson of Georgia , Ms. Kamlager-Dove , Mr. Keating , Mr. Krishnamoorthi , Mr. Landsman , Mr. Lieu , Mr. Lynch , Mr. Magaziner , Mrs. McBath , Mr. McGovern , Mrs. McIver , Mr. Menendez , Ms. Meng , Ms. Moore of Wisconsin , Mr. Moskowitz , Mr. Mrvan , Mr. Mullin , Mr. Neguse , Mr. Norcross , Ms. Ocasio-Cortez , Ms. Omar , Ms. Perez , Ms. Pingree , Mr. Pocan , Ms. Pressley , Mr. Quigley , Mr. Raskin , Ms. Ross , Ms. Salinas , Ms. S\u00e1nchez , Ms. Schakowsky , Ms. Scholten , Ms. Sewell , Ms. Sherrill , Mr. Sorensen , Ms. Stevens , Mrs. Sykes , Mr. Takano , Mr. Thanedar , Mr. Thompson of Mississippi , Ms. Tlaib , Ms. Tokuda , Ms. Vel\u00e1zquez , Ms. Williams of Georgia , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo provide grants to State educational agencies to support State efforts to increase teacher salaries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Teacher Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nTeachers are the backbone of our nation, from the first bell to the last bell, they act as caregivers, counselors, role models, advocates, and cheerleaders, helping children achieve their greatest potential.\n**(2)**\nWhat is more, teacher shortages are among the most pressing threats to education access today, with districts across the country forced to radically adjust school offerings to respond to turnover and prolonged vacancies. Every day, stories surface of schools shortening their weeks, canceling courses, increasing student-teacher ratios, and placing underprepared or temporary substitute staff in core instructional roles. Such adjustments disrupt learning, take a sustained toll on teacher morale, and harm student achievement.\n**(3)**\nThe teacher wage penalty, characterizing lower weekly wages and overall compensation for teachers compared to college-educated peers in other professions, hit an all-time high of 23.5 percent in 2021 and continues to demonstrate significant, adverse impacts on teacher recruitment and retention. According to a recent report by the Teacher Salary Project, over 90 percent of teachers believe low salary contributes to shortages in their communities and over 45 percent believe their salary is insufficient for medium and long-term career sustainability.\n**(4)**\nSignificant numbers of teachers report maintaining multiple jobs to make ends meet or being able to work in their profession only through the support of a partner\u2019s higher-paying job. This instability is worse for teachers of color who are more likely to work in under-resourced schools. As a result, high-poverty communities face a compounded burden.\n**(5)**\nIn August of 2022, the White House issued a fact sheet renewing attention to the weak teacher pipeline and calling upon legislators to use federal, state, and local resources to strengthen teaching career pathways and ensure competitive, livable wages. This statement accompanies efforts by twenty-five states to propose and enact legislation addressing teacher compensation since January 2021.\n**(6)**\nTo restore stability in our schools and secure equitable access to high-quality education, we must raise awareness surrounding the value of teaching as a profession and provide compensation that reflects this value.\n#### 3. Grants to support State efforts to increase teacher salaries\n##### (a) Teacher salary incentive grants\n**(1) Purpose**\nThe purpose of this section is to ensure that each teacher who is employed full-time at a qualifying school in a State earns an annual salary for any year of employment of not less than $60,000 (adjusted for inflation).\n**(2) Grants for minimum salary threshold**\n**(A) In general**\nFrom amounts made available to carry out this section, the Secretary of Education shall award 4-year grants to State educational agencies.\n**(B) Application**\nTo be eligible to receive such a grant, the State educational agency shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including\u2014\n**(i)**\nthe plan required under subparagraph (C); and\n**(ii)**\nthe assurances required under subparagraph (D).\n**(C) Sustainability plan**\nThe Secretary shall require a State educational agency submitting an application under subparagraph (B) to provide a plan that demonstrates how, following the conclusion of the 4-year grant period, such agency will continue to maintain and adjust the annual base minimum salary in accordance with subsection (b).\n**(D) Required assurances**\nThe Secretary shall require a State educational agency submitting an application under subparagraph (B) to provide an assurance in such application that\u2014\n**(i)**\nif necessary to achieve the purpose of this section, the State will enact and enforce legislation to establish a statewide teacher salary schedule or otherwise to establish minimum teacher salary requirements;\n**(ii)**\neach teacher described in paragraph (1) will be compensated on a salary basis at an annual rate per school year that is not less than the salary threshold described in subsection (b);\n**(iii)**\neach teacher who is employed part-time at a qualifying school in a State will be compensated on a salary basis at an annual rate per school year that is not less than the salary threshold described in subsection (b), proportionately reduced in accordance with the number of hours worked by such teacher;\n**(iv)**\npriority will be given to local educational agencies in accordance with subparagraph (E)(ii); and\n**(v)**\nthe State educational agency will, upon request by the Secretary, carry out the compliance demonstration in accordance with subsection (c)(3).\n**(E) Subgrants**\n**(i) In general**\nA State educational agency awarded a grant under this section shall use not less than 85 percent of the grant funds to award subgrants to local educational agencies to carry out the purpose of this section.\n**(ii) Priority**\nThe State educational agency, in allocating funds to local educational agencies under this section, shall give priority to local educational agencies\u2014\n**(I)**\nserving greater numbers or percentages of elementary or secondary schools receiving funds under title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6301 et seq. ); or\n**(II)**\nwith respect to which all of the schools served by the local educational agency are designated with a locale code of 41, 42, or 43, as determined by the Secretary.\n##### (b) Salary threshold\n**(1) In general**\nFor school year 2026\u20132027, the base minimum salary dollar amount shall be $60,000.\n**(2) Inflation adjustment**\nFor school year 2026\u20132027 and each succeeding school year, the dollar amount referred to in paragraph (1) shall be deemed to refer to the dollar amount calculated under this subsection for the preceding school year, increased by a percentage equal to the annual percentage increase in the Consumer Price Index for All Urban Consumers published by the Department of Labor for the most recent calendar year.\n**(3) No salary limit**\nThe base minimum salary dollar amount may be greater than the dollar amount described in paragraphs (1) or (2).\n##### (c) Supplement, not supplant\n**(1) In general**\nGrant funds received under this section shall be used to supplement and not supplant other Federal, State, and local public funds that would, in the absence of such Federal funds, be made available for teacher base salaries.\n**(2) Maintenance of effort**\nA State educational agency or local educational agency shall not reduce or adjust any teacher pay or State teacher loan forgiveness program due to the eligibility of teachers within the jurisdiction of such agency for pay supplementation under this section.\n**(3) Compliance demonstration to Secretary**\nEach State educational agency and local educational agency, upon request by the Secretary, shall demonstrate that the methodology used to allocate teacher pay and State teacher loan forgiveness (if applicable) to teachers and qualifying schools ensures that each such teacher and school receives the same State and local funds for teacher compensation it would receive if this Act had not been enacted.\n#### 4. Grants for adjustment of teacher salaries\n##### (a) In general\nFrom amounts made available to carry out this section, the Secretary of Education shall award grants to eligible State educational agencies to provide, in accordance with subsection (c), cost-of-living adjustments to the annual base salary of such State and the annual salary of each teacher who is employed full-time at a qualifying school in such State.\n##### (b) Application\nTo be eligible to receive such a grant, the State educational agency shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including the demonstration required under subsection (d)(2).\n##### (c) Adjustment\nThe annual base salary of the State and the annual salary of each teacher described in subsection (a) shall be increased by a percentage equal to the annual percentage increase in the Consumer Price Index for All Urban Consumers published by the Department of Labor for the most recent calendar year.\n##### (d) Eligible State defined\nIn this section, the term eligible State means a State\u2014\n**(1)**\nwith an annual base salary of not less than $60,000 for teachers who are employed full-time at a qualifying school; and\n**(2)**\nthat demonstrates in the application submitted under subsection (b) that, due to inflation, such State is unable to adjust such base salary or the annual salaries of such teachers for cost-of-living.\n#### 5. Enhanced awareness of the value of teaching profession\nThe Secretary may reserve not more than 4 percent of the funds appropriated under section 8 to carry out a national campaign\u2014\n**(1)**\nto increase awareness about the importance of teachers and the value of the teaching profession;\n**(2)**\nto encourage secondary school and college students to consider teaching as a professional career; and\n**(3)**\nto diversify the pool of individuals who enter the teaching profession.\n#### 6. Rule of construction\nNothing in this Act shall be construed to alter or otherwise affect the rights, remedies, and procedures afforded to school or local educational agency employees under Federal, State, or local laws (including applicable regulations, court orders, or requirements that local educational agencies negotiate or meet and confer in good faith) or under the terms of collective bargaining agreements, memoranda of understanding, or other agreements between such employers and their employees.\n#### 7. Definitions\nIn this Act:\n**(1) ESEA definitions**\nThe terms elementary school , local educational agency , secondary school , Secretary , State , and State educational agency have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Qualifying school**\nThe term qualifying school means, with respect to any school year, a public elementary school or a public secondary school.\n**(3) Teacher**\nThe term teacher means an individual who\u2014\n**(A)**\nis a teacher of record who provides direct classroom teaching (or classroom-type teaching in a nonclassroom setting) in a qualifying school for not less than the normal or statutory number of hours of work for a full-time or part-time teacher over a complete school year (as determined by the State in which the school is located);\n**(B)**\nmeets the applicable requirements for State certification or licensure, as applicable, in the State in which such school is located and in the subject area in which the individual is the teacher of record; and\n**(C)**\npossesses skills and knowledge needed for effective classroom practice, including with respect to demonstrating the ability to improve student learning.\n**(4) Teacher of record**\nThe term teacher of record means a teacher who has\u2014\n**(A)**\nbeen assigned the responsibility for specified pupils\u2019 learning in a grade, subject, or course as reflected on the school\u2019s official record of attendance;\n**(B)**\nlearned and developed extensive teaching and basic classroom management skills; and\n**(C)**\ndemonstrated the ability to plan and deliver instruction to students from different cultural backgrounds and with different learning styles and to assess and support student learning.\n#### 8. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act such sums as may be necessary for fiscal years 2026 through 2030.",
      "versionDate": "2025-03-10",
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
            "name": "Education programs funding",
            "updateDate": "2026-02-27T18:04:52Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-02-27T18:04:36Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-02-27T18:04:42Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-02-27T18:04:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-26T14:47:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hr2021",
          "measure-number": "2021",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2021v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Teacher Act</strong></p><p>This bill establishes grants to increase the minimum salary of public elementary and secondary school teachers. It also authorizes a national campaign regarding the value of the teaching profession.</p><p>First, the bill directs the Department of Education (ED) to award four-year grants to state educational agencies (SEAs)\u00a0and, through them, subgrants to local educational agencies to establish a minimum annual salary of $60,000 (to be adjusted annually for inflation) for these teachers.</p><p>Second, the bill directs ED to award grants to eligible SEAs\u00a0to provide cost-of-living adjustments to the annual base salary of teachers.</p><p>Finally, the bill authorizes ED to carry out a national campaign to (1) increase awareness about the importance of teachers and the value of the teaching profession, (2) encourage secondary school and college students to consider teaching as a professional career, and (3) diversify the pool of individuals who enter the teaching profession.</p>"
        },
        "title": "American Teacher Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2021.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Teacher Act</strong></p><p>This bill establishes grants to increase the minimum salary of public elementary and secondary school teachers. It also authorizes a national campaign regarding the value of the teaching profession.</p><p>First, the bill directs the Department of Education (ED) to award four-year grants to state educational agencies (SEAs)\u00a0and, through them, subgrants to local educational agencies to establish a minimum annual salary of $60,000 (to be adjusted annually for inflation) for these teachers.</p><p>Second, the bill directs ED to award grants to eligible SEAs\u00a0to provide cost-of-living adjustments to the annual base salary of teachers.</p><p>Finally, the bill authorizes ED to carry out a national campaign to (1) increase awareness about the importance of teachers and the value of the teaching profession, (2) encourage secondary school and college students to consider teaching as a professional career, and (3) diversify the pool of individuals who enter the teaching profession.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr2021"
    },
    "title": "American Teacher Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Teacher Act</strong></p><p>This bill establishes grants to increase the minimum salary of public elementary and secondary school teachers. It also authorizes a national campaign regarding the value of the teaching profession.</p><p>First, the bill directs the Department of Education (ED) to award four-year grants to state educational agencies (SEAs)\u00a0and, through them, subgrants to local educational agencies to establish a minimum annual salary of $60,000 (to be adjusted annually for inflation) for these teachers.</p><p>Second, the bill directs ED to award grants to eligible SEAs\u00a0to provide cost-of-living adjustments to the annual base salary of teachers.</p><p>Finally, the bill authorizes ED to carry out a national campaign to (1) increase awareness about the importance of teachers and the value of the teaching profession, (2) encourage secondary school and college students to consider teaching as a professional career, and (3) diversify the pool of individuals who enter the teaching profession.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr2021"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2021ih.xml"
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
      "title": "American Teacher Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Teacher Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide grants to State educational agencies to support State efforts to increase teacher salaries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:27Z"
    }
  ]
}
```
