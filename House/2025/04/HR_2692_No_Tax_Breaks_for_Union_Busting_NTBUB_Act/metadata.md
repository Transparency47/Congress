# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2692?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2692
- Title: No Tax Breaks for Union Busting (NTBUB) Act
- Congress: 119
- Bill type: HR
- Bill number: 2692
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-05-14T08:08:14Z
- Update date including text: 2026-05-14T08:08:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2692",
    "number": "2692",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "N000188",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Norcross, Donald [D-NJ-1]",
        "lastName": "Norcross",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "No Tax Breaks for Union Busting (NTBUB) Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:14Z",
    "updateDateIncludingText": "2026-05-14T08:08:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
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
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:01:45Z",
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
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "WA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-07",
      "state": "NC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MD"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "VT"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "ME"
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
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-07",
      "state": "IL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "CO"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NV"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "DC"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MO"
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
      "sponsorshipDate": "2025-04-07",
      "state": "OH"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "IL"
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
      "sponsorshipDate": "2025-04-07",
      "state": "IN"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
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
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
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
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
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
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "CT"
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "ME"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "HI"
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
      "sponsorshipDate": "2025-04-07",
      "state": "MA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "CO"
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
      "sponsorshipDate": "2025-04-07",
      "state": "CT"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MD"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "WA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MD"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "OH"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "WI"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "OR"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "NM"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "IL"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "KY"
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "WA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "WA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
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
      "sponsorshipDate": "2025-04-07",
      "state": "CT"
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
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MD"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "DE"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "IL"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "RI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "KS"
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
      "sponsorshipDate": "2025-04-07",
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
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
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
      "sponsorshipDate": "2025-04-07",
      "state": "MA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NV"
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
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "WA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "OR"
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
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-07",
      "state": "LA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "OR"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "AZ"
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CO"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MO"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "OH"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NC"
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
      "sponsorshipDate": "2026-05-04",
      "state": "VA"
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
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2692ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2692\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Norcross (for himself, Mr. Boyle of Pennsylvania , Ms. Chu , Mr. Smith of Washington , Mr. Green of Texas , Ms. Ocasio-Cortez , Ms. Adams , Ms. Craig , Mrs. McClain Delaney , Ms. Balint , Ms. McCollum , Mr. Foster , Mr. Sherman , Mr. Schneider , Ms. Pingree , Mr. Deluzio , Ms. Houlahan , Mr. Garc\u00eda of Illinois , Mr. Goldman of New York , Mr. Davis of Illinois , Mr. Soto , Mrs. Dingell , Ms. Wasserman Schultz , Mrs. Ramirez , Ms. DeGette , Ms. Titus , Mr. Evans of Pennsylvania , Ms. Norton , Mr. Cleaver , Mrs. Sykes , Mr. Sorensen , Mr. Mrvan , Mr. Pallone , Ms. Wilson of Florida , Mr. Latimer , Mr. Connolly , Mr. Cisneros , Ms. Meng , Mr. Casar , Ms. Stevens , Mr. Johnson of Georgia , Mr. Cuellar , Mr. Conaway , Ms. Omar , Mrs. Hayes , Ms. Schakowsky , Mr. Golden of Maine , Mr. Nadler , Ms. Tokuda , Mr. McGovern , Mr. Gomez , Mr. Panetta , Mr. Neguse , Mr. Larson of Connecticut , Mr. Garamendi , Mr. Mannion , Mr. Olszewski , Mr. Gottheimer , Mrs. Beatty , Ms. Brownley , Ms. Morrison , Mr. Mullin , Ms. Schrier , Ms. McDonald Rivet , Mr. Mfume , Mrs. McIver , Ms. Friedman , Ms. Underwood , Ms. S\u00e1nchez , Mrs. Fletcher , Mr. Doggett , Ms. Lois Frankel of Florida , Mrs. Trahan , Mrs. McBath , Ms. Dean of Pennsylvania , Mr. Veasey , Ms. Kaptur , Mr. DeSaulnier , Mr. Pocan , Mr. Takano , Ms. Scanlon , Ms. Dexter , Ms. Waters , Mr. Frost , Ms. Stansbury , Mr. Quigley , Ms. Sherrill , Mr. McGarvey , Ms. Barrag\u00e1n , Ms. Williams of Georgia , Ms. Budzinski , Ms. Vel\u00e1zquez , Mr. Ryan , Mr. Tonko , Ms. Jayapal , Mr. Krishnamoorthi , Ms. Tlaib , Mr. Larsen of Washington , Mr. Torres of New York , Mr. Khanna , Mr. Garcia of California , Mr. Menendez , Ms. DeLauro , Mr. Bishop , Ms. Elfreth , Ms. McBride , Mr. Casten , Mr. Magaziner , Mr. Moulton , Ms. Davids of Kansas , Ms. Brown , Mr. Thanedar , Mr. Lynch , Mr. Horsford , Ms. Lee of Pennsylvania , Ms. DelBene , Ms. Bonamici , Ms. Garcia of Texas , Mr. Lieu , Mr. Suozzi , Mr. Carter of Louisiana , Ms. Hoyle of Oregon , Ms. Ansari , Ms. Clarke of New York , Mr. Kennedy of New York , and Mr. Crow ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to end the tax subsidy for employer efforts to influence their workers\u2019 exercise of their rights around labor organizations and engaging in collective action.\n#### 1. Short title\nThis Act may be cited as the No Tax Breaks for Union Busting (NTBUB) Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe National Labor Relations Act ( 29 U.S.C. 151 et seq. ) declares that it is the right of employees to form, join, or assist labor organizations.\n**(2)**\nThe National Labor Relations Act further declares that it is the policy of the United States to eliminate the causes of certain substantial obstructions to the free flow of commerce and to mitigate and eliminate these obstructions when they have occurred by encouraging the practice and procedure of collective bargaining and by protecting the exercise by workers of full freedom of association, self-organization, and designation of representatives of their own choosing . . . .\n**(3)**\nDespite Congress\u2019 intention to give workers full agency in these matters, many employers regularly choose to involve themselves, lawfully or unlawfully, in the decisions of their employees about whether to avail themselves of their rights under the National Labor Relations Act and the Railway Labor Act ( 45 U.S.C. 151 et seq. ).\n**(4)**\nEmployers frequently violate labor laws around organizing and collective action. The Economic Policy Institute finds that in approximately 4 of 10 labor organization elections in 2016\u20132017 employers were charged with committing an unfair labor practice. Among larger bargaining units of 61 employees or more, over 54 percent of elections have an unfair labor practice charge.\n**(5)**\nIn practice, these unfair labor practices often include charges such as employees being illegally fired for labor organization activity, refusal to bargain in good faith with labor organizations, or coercion and intimidation. Employers also frequently use captive audience meetings, workplace surveillance, and other lawful or unlawful tactics to sway labor organization elections.\n**(6)**\nWhether or not there are charges of unlawful behavior, employers spend millions of dollars to sway the opinions of their employees with respect to whether or how to exercise their rights under the National Labor Relations Act and the Railway Labor Act. According to the Economic Policy Institute, companies spent $340,000,000 yearly on outside consultants to sway their workers' opinions about labor organization activities. This and other spending interferes with the United States goal of encouraging the practice and procedure of collective bargaining .\n**(7)**\nThe Internal Revenue Code of 1986 has long recognized that spending by businesses with the purpose of influencing the general public with respect to elections, while it may be lawful, is not tax deductible. Congress should extend that principle to spending done by employers to influence workers\u2019 elections and collective bargaining decisions. These free choices to exercise the rights to engage in collective bargaining, labor organization representation, and other lawful collective activities should be made without taxpayer subsidies of undue outside influence from employers.\n#### 3. Denial of deduction for attempting to influence employees with respect to labor organizations or labor organization activities\n##### (a) In general\nSection 162(e)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (C), by striking the period at the end of subparagraph (D) and inserting , or , and by adding at the end the following new subparagraph:\n(E) any attempt to influence the taxpayer's employees with respect to labor organizations or labor organization activities, including with respect to the opinion of such employees regarding such organizations or activities. .\n##### (b) Labor organizations; labor organization activities defined\nSection 162(e) of the Internal Revenue Code of 1986 is amended by redesignating paragraph (6) as paragraph (7) and by inserting after paragraph (5) the following new paragraph:\n(6) Labor organizations and labor organization activity defined For purposes of this subsection\u2014 (A) Labor organization The term labor organization has the meaning given such term in section 3 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 402 ). (B) Labor organization activity (i) In general The term labor organization activity means labor organization elections, labor disputes, collective actions, and such other related activities identified by the Secretary. (ii) Other terms For purposes of clause (i)\u2014 (I) Collective action The term collective action means any action, including collective bargaining, described in section 7 of the National Labor Relations Act ( 29 U.S.C. 157 ) or any action that is a right of employees or labor organizations under the Railway Labor Act ( 45 U.S.C. 151 et seq. ). (II) Labor dispute The term labor dispute has the meaning given such term under section 3 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 402 ). (III) Labor organization election The term labor organization election means any election described in section 9 of the National Labor Relations Act ( 29 U.S.C. 159 ) or section 2 of the Railway Labor Act ( 45 U.S.C. 152 ). .\n##### (c) Special rules\n**(1) In general**\nSection 162(e)(4) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(D) Expenses relating to labor organizations or labor organization activities (i) In general For purposes of paragraph (1)(E), amounts paid or incurred in connection with attempting to influence the taxpayer's employees with respect to labor organizations or labor organization activities include\u2014 (I) any amount paid or incurred directly or indirectly by the taxpayer, including wages and other general and administrative costs, in connection with an action that results in\u2014 (aa) a complaint issued under section 10 of the National Labor Relations Act ( 29 U.S.C. 160 ) against the taxpayer for an unfair labor practice under section 8(a) of such Act ( 29 U.S.C. 158(a) ), (bb) a settlement offer related to an investigation by the National Labor Relations Board of a charge of an unfair labor practice under section 8(a) of such Act ( 29 U.S.C. 158(a) ) that results in a settlement of such charge without issuance of a complaint under section 10 of such Act ( 29 U.S.C. 160 ), or (cc) a finding of interference, influence, or coercion by a Federal court under section 2 of the Railway Labor Act ( 45 U.S.C. 152 ), (II) any amount paid or incurred directly or indirectly by the taxpayer, including wages and other general and administrative costs, in producing, conducting, or attending any meeting or training\u2014 (aa) which includes employees of the taxpayer who are or who could become members of a unit appropriate for the purposes of collective bargaining, and (bb) at which labor organizations or a labor organization activity is discussed, and (III) any amount which is required to be reported under the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 401 et seq. ). (ii) Exceptions The following amounts shall not be treated as amounts paid or incurred in connection with attempting to influence the taxpayer's employees with respect to labor organizations or labor organization activities under paragraph (1)(E): (I) Amounts paid or incurred for communications or negotiations directly with the designated or selected representative of the employees of the taxpayer described in section 9(a) of the National Labor Relations Act ( 29 U.S.C. 159(a) ) or under the Railway Labor Act ( 45 U.S.C. 151 et seq. ). (II) Amounts paid or incurred for communications directly with shareholders, as may be required under section 13 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m ). (III) Amounts paid or incurred for communications or consultations by the taxpayer in the process of voluntarily recognizing a labor organization as a representative in accordance with section 9 of the National Labor Relations Act ( 29 U.S.C. 159 ). (IV) Amounts paid or incurred with respect to the operation of a labor-management partnership described in a collective bargaining agreement in effect between a representative of employees of the taxpayer and the taxpayer, including a labor management committee established pursuant to section 205A(a) of the Labor Management Relations Act, 1947 ( 29 U.S.C. 175a(a) ). (V) Amounts paid or incurred for communications or consultations related to the operation of a grievance procedure described in a collective bargaining agreement in effect between a representative of employees of the taxpayer and the taxpayer. (VI) Amounts paid or incurred by a labor organization. (VII) Amounts paid or incurred for communication materials, including visual or audio media, required to be posted for, or provided to, employees of the taxpayer by law, including under the National Labor Relations Act ( 29 U.S.C. 151 et seq. ) or the Railway Labor Act ( 45 U.S.C. 151 et seq. ). (VIII) Amounts paid or incurred relating to a complaint which is issued by the National Labor Relations Board and which is set aside in full in accordance with subsection (e) or (f) of section 10 of such Act. .\n**(2) Regulatory authority**\n**(A) In general**\nSection 162(e) of such Code, as amended by subsection (b), is amended by redesignating paragraph (7) as paragraph (8) and by inserting after paragraph (6) the following new paragraph:\n(7) Regulations The Secretary shall prescribe such guidance, rules, or regulations as are necessary to carry out the purposes of this subsection, including rules relating to the timing of any deductions in connection with amounts described in paragraph (4)(D)(ii)(VIII). .\n**(B) Timing**\nNot later than the date that is 240 days after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall prescribe guidance, rules, or regulations with respect to the application of the amendments made by this Act.\n##### (d) Information reporting\n**(1) Certain information included in tax returns**\n**(A) In general**\nPart I of subchapter B of chapter 68 is amended by adding at the end the following new section:\n6720D. Failure to include certain information with respect to employer activities relating to labor organizations (a) In general If any taxpayer who makes expenditures described in section 162(e)(1)(E) fails to provide with the return of tax for the taxable year to which such expenditures relate the information provided in subsection (c) with respect to such expenditures, or who fails to provide all of the information required under subsection (b) or fails to provide correct information, shall pay a penalty in the amount determined under subsection (b). (b) Determination of penalty amount (1) In general The amount of the penalty under this section for any failure described in subsection (a) shall be the greater of\u2014 (A) $10,000, or (B) the product of $1,000 and the number of full time equivalent employees of the employer (as determined under section 45R(d)(2)). (2) Increased penalty where failure continues (A) In general If any failure described in subsection (a)(1) continues for more than 90 days after the day on which the Secretary mails notice of such failure to the taxpayer, the taxpayer shall pay a penalty (in addition to the amount of any penalty under paragraph (1)) equal to the amount determined under paragraph (1) for each 30-day period (or fraction thereof) during which such failure continues after the expiration of such 90-day period. (B) Limitation The penalty imposed under this paragraph with respect to any failure shall not exceed $100,000. (c) Information To be provided The information required under this subsection shall include\u2014 (1) the dates that such activities described in section 162(e)(1)(E) took place, (2) a statement indicating whether the activity was an activity described in item (aa), (bb), or (cc) of section 162(e)(4)(D)(i)(I), (3) the amounts paid or incurred for such activities, (4) a copy of any disclosures which are required to be reported under the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 401 et seq. ), and (5) such other information as the Secretary may prescribe. (d) Reasonable cause exception No penalty shall be imposed by this section on any failure which is shown to be due to reasonable cause and not due to willful neglect. .\n**(B) Clerical amendment**\nThe table of sections for part I of subchapter B of chapter 68 is amended by adding at the end the following new item:\nSec. 6720D. Failure to include certain information with respect to employer activities relating to labor organizations. .\n**(2) Third-party information reporting**\n**(A) In general**\nSubpart A of part III of subchapter A of chapter 61 of the Internal Revenue Code of 1986 is amended by inserting after section 6039J the following new section:\n6039K. Information with respect to certain employer activities relating to labor organizations (a) In general Any person conducting activities described in section 162(e)(1)(E) on behalf of another person shall file a return (at such time and in such manner as the Secretary may by regulations prescribe, which includes the information described in subsection (b)). (b) Information To be provided Information required under subsection (a) shall include\u2014 (1) the person on behalf of whom the activities described in section 162(e)(1)(E) were performed, (2) the dates that such activities described in such section took place, (3) a statement indicating whether the activity was an activity described in item (aa), (bb), or (cc) of section 162(e)(4)(D)(i)(I), (4) the amounts paid or incurred for such activities, and (5) such other information as the Secretary may prescribe. .\n**(B) Penalty**\nSubparagraph (B) of section 6724(d)(1) of such Code is amended\u2014\n**(i)**\nby striking the comma at the end of clause (xxvii), as added by the Infrastructure Investment and Jobs Act, and inserting , or , and\n**(ii)**\nby adding at the end the following new clause:\n(xxviii) section 6039K (relating to information with respect to certain employer activities relating to labor organizations), and .\n**(C) Clerical amendment**\nThe table of sections for subpart A of part III of subchapter A of chapter 61 of such Code is amended by inserting after the item relating to section 6039J the following new item:\nSec. 6039K. Information with respect to certain employer activities relating to labor organizations. .\n##### (e) Conforming amendments\n**(1)**\nThe heading for subsection (e) of section 162 of the Internal Revenue Code of 1986 is amended by striking and political expenditures and inserting , political expenditures, and labor organization expenditures .\n**(2)**\nThe heading of subparagraph (C) of section 162(e)(4) of such Code is amended by striking and political activities and inserting , political, and labor organization activities .\n##### (f) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred in taxable years beginning after the date that is 240 days after the date of the enactment of this Act.",
      "versionDate": "2025-04-07",
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
        "actionDate": "2025-04-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1310",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Tax Breaks for Union Busting (NTBUB) Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-05T16:05:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-07",
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
          "measure-id": "id119hr2692",
          "measure-number": "2692",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2026-02-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2692v00",
            "update-date": "2026-02-04"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Tax Breaks for Union Busting (NTBUB) Act</strong></p><p>This bill excludes from the tax deduction for ordinary and necessary business expenses amounts paid or incurred to influence employees with respect to labor organizations or labor organization activities. The bill also imposes information reporting requirements related to such expenses and imposes penalties for failure to comply.\u00a0</p><p>Under the bill, amounts paid to influence employees with respect to labor organizations include amounts paid (including wages and other costs) </p><ul><li>in connection with an action that results in a complaint or settlement related to an unfair labor practice or a finding of interference, influence, or coercion related to railway employees\u2019 rights to organize and bargain collectively;</li><li>for\u00a0any meeting or training attended by employees and at which labor organizations are discussed; and</li><li>that require\u00a0certain employer disclosures and financial reporting.</li></ul><p>(Some exceptions apply.)\u00a0</p><p>The bill requires employers to file a return reporting certain information related to expenses paid to influence employees with respect to labor organizations and imposes a penalty for noncompliance. The amount of the penalty is the greater of (1) $10,000, or (2) $1,000 multiplied by the number full-time equivalent employees. Additional penalties apply for\u00a0violations that continue for more than 90 days.\u00a0</p><p>The bill also imposes information reporting requirements on persons conducting activities on behalf of another person to influence employees with respect to labor organizations.</p><p>The bill allows certain penalties for noncompliance with the reporting requirements to be waived if noncompliance is due to reasonable cause and not willful neglect.</p>"
        },
        "title": "No Tax Breaks for Union Busting (NTBUB) Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2692.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Tax Breaks for Union Busting (NTBUB) Act</strong></p><p>This bill excludes from the tax deduction for ordinary and necessary business expenses amounts paid or incurred to influence employees with respect to labor organizations or labor organization activities. The bill also imposes information reporting requirements related to such expenses and imposes penalties for failure to comply.\u00a0</p><p>Under the bill, amounts paid to influence employees with respect to labor organizations include amounts paid (including wages and other costs) </p><ul><li>in connection with an action that results in a complaint or settlement related to an unfair labor practice or a finding of interference, influence, or coercion related to railway employees\u2019 rights to organize and bargain collectively;</li><li>for\u00a0any meeting or training attended by employees and at which labor organizations are discussed; and</li><li>that require\u00a0certain employer disclosures and financial reporting.</li></ul><p>(Some exceptions apply.)\u00a0</p><p>The bill requires employers to file a return reporting certain information related to expenses paid to influence employees with respect to labor organizations and imposes a penalty for noncompliance. The amount of the penalty is the greater of (1) $10,000, or (2) $1,000 multiplied by the number full-time equivalent employees. Additional penalties apply for\u00a0violations that continue for more than 90 days.\u00a0</p><p>The bill also imposes information reporting requirements on persons conducting activities on behalf of another person to influence employees with respect to labor organizations.</p><p>The bill allows certain penalties for noncompliance with the reporting requirements to be waived if noncompliance is due to reasonable cause and not willful neglect.</p>",
      "updateDate": "2026-02-04",
      "versionCode": "id119hr2692"
    },
    "title": "No Tax Breaks for Union Busting (NTBUB) Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Tax Breaks for Union Busting (NTBUB) Act</strong></p><p>This bill excludes from the tax deduction for ordinary and necessary business expenses amounts paid or incurred to influence employees with respect to labor organizations or labor organization activities. The bill also imposes information reporting requirements related to such expenses and imposes penalties for failure to comply.\u00a0</p><p>Under the bill, amounts paid to influence employees with respect to labor organizations include amounts paid (including wages and other costs) </p><ul><li>in connection with an action that results in a complaint or settlement related to an unfair labor practice or a finding of interference, influence, or coercion related to railway employees\u2019 rights to organize and bargain collectively;</li><li>for\u00a0any meeting or training attended by employees and at which labor organizations are discussed; and</li><li>that require\u00a0certain employer disclosures and financial reporting.</li></ul><p>(Some exceptions apply.)\u00a0</p><p>The bill requires employers to file a return reporting certain information related to expenses paid to influence employees with respect to labor organizations and imposes a penalty for noncompliance. The amount of the penalty is the greater of (1) $10,000, or (2) $1,000 multiplied by the number full-time equivalent employees. Additional penalties apply for\u00a0violations that continue for more than 90 days.\u00a0</p><p>The bill also imposes information reporting requirements on persons conducting activities on behalf of another person to influence employees with respect to labor organizations.</p><p>The bill allows certain penalties for noncompliance with the reporting requirements to be waived if noncompliance is due to reasonable cause and not willful neglect.</p>",
      "updateDate": "2026-02-04",
      "versionCode": "id119hr2692"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2692ih.xml"
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
      "title": "No Tax Breaks for Union Busting (NTBUB) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Tax Breaks for Union Busting (NTBUB) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to end the tax subsidy for employer efforts to influence their workers' exercise of their rights around labor organizations and engaging in collective action.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T04:48:24Z"
    }
  ]
}
```
