# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/220?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/220
- Title: Veterans Infertility Treatment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 220
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2026-05-14T08:08:46Z
- Update date including text: 2026-05-14T08:08:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-11 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-11 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/220",
    "number": "220",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Veterans Infertility Treatment Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:46Z",
    "updateDateIncludingText": "2026-05-14T08:08:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-11T22:36:36Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "NJ"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "WI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "MI"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "FL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "OH"
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
      "sponsorshipDate": "2025-01-07",
      "state": "MS"
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
      "sponsorshipDate": "2025-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "DC"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "RI"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "MA"
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
      "sponsorshipDate": "2025-01-07",
      "state": "NC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "ME"
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
      "sponsorshipDate": "2025-01-07",
      "state": "IL"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "NM"
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
      "sponsorshipDate": "2025-01-07",
      "state": "HI"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "WA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "NY"
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
      "sponsorshipDate": "2025-01-07",
      "state": "PA"
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
      "sponsorshipDate": "2025-01-07",
      "state": "CT"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
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
      "sponsorshipDate": "2025-01-07",
      "state": "NC"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NJ"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CT"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "ME"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "WI"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "GA"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "IL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "NV"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "NJ"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "TN"
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
      "sponsorshipDate": "2025-01-22",
      "state": "OR"
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
      "sponsorshipDate": "2025-01-22",
      "state": "MA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MD"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "GA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "VA"
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
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "HI"
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
      "sponsorshipDate": "2025-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "FL"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "AZ"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "KS"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MI"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "RI"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "AZ"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "NV"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
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
      "sponsorshipDate": "2025-06-05",
      "state": "AZ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MN"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CO"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CO"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MO"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "IN"
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MN"
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
      "sponsorshipDate": "2025-10-24",
      "state": "WA"
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
      "sponsorshipDate": "2025-10-31",
      "state": "MA"
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
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NH"
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
      "sponsorshipDate": "2026-05-13",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr220ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 220\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Ms. Brownley (for herself, Mrs. Watson Coleman , Ms. Moore of Wisconsin , Ms. Tlaib , Mrs. Cherfilus-McCormick , Mr. Landsman , Mr. Thompson of Mississippi , Ms. Garcia of Texas , Mrs. Dingell , Ms. Norton , Mr. Magaziner , Mrs. Trahan , Mrs. Foushee , Ms. Pingree , Mrs. Ramirez , Ms. Leger Fernandez , Ms. Tokuda , Ms. Strickland , Mr. Tonko , Ms. Scanlon , Mr. Larson of Connecticut , Mr. Levin , Ms. Ross , and Mr. Casar ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide coverage for infertility treatment and standard fertility preservation services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Infertility Treatment Act of 2025 .\n#### 2. Infertility treatments for veterans\n##### (a) Authority\nChapter 17 of title 38, United States Code, is amended by inserting after section 1720J the following new section (and conforming the table of sections at the beginning of such chapter accordingly):\n1720K. Infertility treatment and standard fertility preservation services (a) Treatment and services (1) In furnishing medical services under this chapter, at the election of a covered individual and subject to paragraph (4), the Secretary shall furnish to the covered individual infertility treatments (including through the use of assisted reproductive technology), standard fertility preservation services, or both. (2) In the case of in vitro fertilization treatment furnished under paragraph (1), the Secretary may furnish to a covered individual under such paragraph not more than three completed in vitro fertilization cycles that result in live birth or 10 attempted in vitro fertilization cycles, whichever occurs first. (3) The Secretary may furnish in vitro fertilization treatment under paragraph (1) using donated gametes or embryos. (4) The Secretary may not furnish to a covered individual an in vitro fertilization cycle or other treatment or service under paragraph (1) unless the Secretary receives consent for such cycle, treatment, or service from each of the following: (A) The covered individual. (B) If the covered individual is a partner of a covered veteran, the covered veteran. (C) If applicable, the third-party donor. (b) Rule of construction Nothing in this section shall be construed to require the Secretary to furnish maternity care to a covered individual, in addition to what is otherwise required by section 1786 of this title or other provisions of law. (c) Relationship to State law The legal status, custody, future use, donation, disposition, or destruction, of gametes or embryos relating to treatment or services furnished under this section shall be determined in accordance with the law of the State in which the gametes or embryos are located. (d) Payments for beneficiary travel for partners For purposes of paying travel expenses under section 111 of this title for treatment or services furnished under this section to a partner of a covered veteran, the Secretary shall deem the partner to be a veteran receiving treatment or care under this chapter. (e) Definitions In this section: (1) The term assisted reproductive technology includes in vitro fertilization and other infertility treatments. (2) The term covered individual means a covered veteran or a partner of a covered veteran. (3) The term covered veteran means a veteran who is enrolled in the system of annual patient enrollment established under section 1705(a) of this title and\u2014 (A) has infertility; or (B) is at risk of having infertility, as determined by a licensed physician based on\u2014 (i) the medical, sexual, and reproductive history, age, physical findings, or diagnostic testing, or a combination thereof, of the veteran; or (ii) any planned medication therapy, surgery, radiation, chemotherapy, or other medical treatment. (4) The term infertility means a disease, condition, or status characterized by\u2014 (A) the inability of a person to reproduce either as an individual or with the partner of the individual; or (B) the failure to conceive a pregnancy or to carry a pregnancy to live birth after one year of regular, unprotected sexual intercourse. (5) The term partner , with respect to a veteran, means an individual selected by the veteran who agrees to share with the veteran the parental responsibilities with respect to any child born as a result of the use of any infertility treatment under this section. (6) The term standard fertility preservation service includes the procurement, cryopreservation, and storage of gametes and embryos. .\n##### (b) Applicability; regulations\n**(1) Applicability**\nExcept as provided by paragraph (3)(A), section 1720K of title 38, United States Code, as added by subsection (a), shall apply with respect to infertility treatment and standard fertility preservation services furnished by the Secretary of Veterans Affairs beginning on the date on which the Secretary prescribes regulations under paragraph (2).\n**(2) Regulations**\nNot later than one year after the date of the enactment of this Act, the Secretary shall prescribe regulations to carry out section 1720K of title 38, United States Code, as added by subsection (a).\n**(3) Interim policies**\n**(A) Continuity of services**\nExcept as provided by subparagraph (B), an individual who on the day before the date on which the Secretary prescribes regulations under paragraph (2) is receiving counseling and treatment furnished by the Secretary pursuant to existing infertility authority may elect to\u2014\n**(i)**\ncontinue receiving such counseling and services pursuant to the existing infertility authority, subject to the limitations of that authority; or\n**(ii)**\nbegin receiving such counseling and services pursuant to section 1720K of title 38, United States Code, as added by subsection (a), subject to the limitations of that section that shall be applied in a manner that recognizes such counseling and services previously furnished under the existing infertility authority.\n**(B) Expansion of services**\nDuring the period beginning 180 days after the date of the enactment of this Act and ending on the date on which the Secretary prescribes regulations under paragraph (2), the Secretary shall ensure that counseling and treatment furnished pursuant to existing infertility authority include the following elements:\n**(i)**\nThe Secretary may furnish such counseling and treatment to the partner of a veteran covered by such provision without regard to whether the partner and veteran are married.\n**(ii)**\nThe Secretary may furnish such counseling and treatment using donated gametes or embryos.\n**(4) Definitions**\nIn this subsection:\n**(A)**\nThe term existing infertility authority means section 234(a)(1) of the Military Construction, Veterans Affairs, and Related Agencies Appropriations Act, 2022 (division J of Public Law 117\u2013103 ; 136 Stat. 556), or other provisions of law administered by the Secretary of Veterans Affairs enacted before the date of the enactment of this Act that provide authority to the Secretary to furnish fertility counseling and treatment.\n**(B)**\nThe term partner has the meaning given that term in section 1720K of title 38, United States Code, as added by subsection (a).",
      "versionDate": "2025-01-07",
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
            "name": "Health care coverage and access",
            "updateDate": "2025-03-05T16:03:09Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-03-05T16:02:45Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-03-05T16:03:15Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-05T16:02:53Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-03-05T16:03:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-12T15:41:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr220",
          "measure-number": "220",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr220v00",
            "update-date": "2025-02-13"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Infertility Treatment Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish infertility treatments, standard fertility preservation services, or both to a covered veteran or partner of a covered veteran. A covered veteran is a veteran who is enrolled in the VA health care system and has infertility or is at risk of having infertility, as determined by a licensed physician.</p><p>The VA may furnish up to three completed in vitro fertilization cycles that result in live birth, or 10 attempted cycles, whichever occurs first. Additionally, the VA may furnish in vitro fertilization treatment using donated gametes or embryos.</p><p>The VA must receive consent to furnish an in vitro fertilization cycle from the covered veteran, the partner of a covered veteran, and the third-party donor (if applicable).</p><p>For purposes of paying travel expenses for treatment or services to the partner of a covered veteran, the VA must deem the partner to be a veteran receiving treatment or care.</p><p>The VA must prescribe regulations related to the provision of infertility treatments and standard fertility preservation services as required by this bill.</p><p>Prior to the enactment of such regulations, the VA must ensure that (1) counseling and treatment furnished under existing authority is available to a veteran and the veteran's partner, regardless of whether they are married; and (2) treatment under existing authority may be furnished using donated gametes or embryos.</p>"
        },
        "title": "Veterans Infertility Treatment Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr220.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Infertility Treatment Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish infertility treatments, standard fertility preservation services, or both to a covered veteran or partner of a covered veteran. A covered veteran is a veteran who is enrolled in the VA health care system and has infertility or is at risk of having infertility, as determined by a licensed physician.</p><p>The VA may furnish up to three completed in vitro fertilization cycles that result in live birth, or 10 attempted cycles, whichever occurs first. Additionally, the VA may furnish in vitro fertilization treatment using donated gametes or embryos.</p><p>The VA must receive consent to furnish an in vitro fertilization cycle from the covered veteran, the partner of a covered veteran, and the third-party donor (if applicable).</p><p>For purposes of paying travel expenses for treatment or services to the partner of a covered veteran, the VA must deem the partner to be a veteran receiving treatment or care.</p><p>The VA must prescribe regulations related to the provision of infertility treatments and standard fertility preservation services as required by this bill.</p><p>Prior to the enactment of such regulations, the VA must ensure that (1) counseling and treatment furnished under existing authority is available to a veteran and the veteran's partner, regardless of whether they are married; and (2) treatment under existing authority may be furnished using donated gametes or embryos.</p>",
      "updateDate": "2025-02-13",
      "versionCode": "id119hr220"
    },
    "title": "Veterans Infertility Treatment Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Infertility Treatment Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish infertility treatments, standard fertility preservation services, or both to a covered veteran or partner of a covered veteran. A covered veteran is a veteran who is enrolled in the VA health care system and has infertility or is at risk of having infertility, as determined by a licensed physician.</p><p>The VA may furnish up to three completed in vitro fertilization cycles that result in live birth, or 10 attempted cycles, whichever occurs first. Additionally, the VA may furnish in vitro fertilization treatment using donated gametes or embryos.</p><p>The VA must receive consent to furnish an in vitro fertilization cycle from the covered veteran, the partner of a covered veteran, and the third-party donor (if applicable).</p><p>For purposes of paying travel expenses for treatment or services to the partner of a covered veteran, the VA must deem the partner to be a veteran receiving treatment or care.</p><p>The VA must prescribe regulations related to the provision of infertility treatments and standard fertility preservation services as required by this bill.</p><p>Prior to the enactment of such regulations, the VA must ensure that (1) counseling and treatment furnished under existing authority is available to a veteran and the veteran's partner, regardless of whether they are married; and (2) treatment under existing authority may be furnished using donated gametes or embryos.</p>",
      "updateDate": "2025-02-13",
      "versionCode": "id119hr220"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr220ih.xml"
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
      "title": "Veterans Infertility Treatment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Infertility Treatment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-07T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide coverage for infertility treatment and standard fertility preservation services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T04:33:42Z"
    }
  ]
}
```
