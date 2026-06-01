# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5168?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5168
- Title: Puerto Rico Nutrition Assistance Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 5168
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2026-05-30T08:05:59Z
- Update date including text: 2026-05-30T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5168",
    "number": "5168",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001103",
        "district": "",
        "firstName": "Pablo",
        "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
        "lastName": "Hern\u00e1ndez",
        "party": "D",
        "state": "PR"
      }
    ],
    "title": "Puerto Rico Nutrition Assistance Fairness Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:59Z",
    "updateDateIncludingText": "2026-05-30T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
          "date": "2025-09-08T16:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:54:37Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "NE"
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
      "sponsorshipDate": "2025-09-08",
      "state": "MA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "NY"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
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
      "sponsorshipDate": "2025-09-08",
      "state": "PA"
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
      "sponsorshipDate": "2025-09-08",
      "state": "NY"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "PA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MN"
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
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "GU"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CT"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "WA"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "MD"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "DE"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MI"
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
      "sponsorshipDate": "2026-01-20",
      "state": "HI"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NM"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "OR"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "ME"
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
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "MD"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CT"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NC"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "GA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "OR"
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
      "sponsorshipDate": "2026-03-24",
      "state": "NC"
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
      "sponsorshipDate": "2026-04-16",
      "state": "CT"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "DC"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CT"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "MP"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
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
      "sponsorshipDate": "2026-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "M001245",
      "district": "18",
      "firstName": "Christian",
      "fullName": "Rep. Menefee, Christian D. [D-TX-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Menefee",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "TX"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
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
      "sponsorshipDate": "2026-05-20",
      "state": "KS"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NJ"
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
      "sponsorshipDate": "2026-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "WI"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5168ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5168\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Mr. Hern\u00e1ndez (for himself, Mr. Bacon , Mr. McGovern , Mr. Lawler , Mr. Soto , Mr. Fitzpatrick , Ms. Vel\u00e1zquez , Ms. Salazar , and Ms. Houlahan ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to transition the Commonwealth of Puerto Rico to the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Puerto Rico Nutrition Assistance Fairness Act .\n#### 2. Amendments to the Food and Nutrition Act of 2008\n##### (a) Definitions\nSection 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ) is amended\u2014\n**(1)**\nin subsection (r) by inserting Puerto Rico, after Guam, , and\n**(2)**\nin subsection (u)(2) by inserting , Puerto Rico, after Hawaii .\n##### (b) Eligible households\nSection 5 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014 ) is amended\u2014\n**(1)**\nin subsection (b) by inserting Puerto Rico, after Guam, ,\n**(2)**\nin subsection (c)(1) by striking and Guam and inserting Guam, and Puerto Rico , and\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)(A) by inserting Puerto Rico, after Hawaii, each place it appears, and\n**(B)**\nin paragraph (6)(B) by inserting Puerto Rico, after Guam, .\n#### 3. Submission of plan of operation; technical assistance; determination and certification by Secretary of Agriculture\n##### (a) Submission of plan of operation\nOn designating an agency of the kind described in section 3(s)(1) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(s)(1) ), the Commonwealth of Puerto Rico shall have 180 days to submit to the Secretary of Agriculture (in this Act referred to as the Secretary ) its plan of operation, including a plan to transition to the supplemental nutrition assistance program under section 4(a) of such Act ( 7 U.S.C. 2013(a) ) as a request to participate in the supplemental nutrition assistance program under such Act.\n##### (b) Technical assistance\nWithin the 180-day period specified in subsection (a) and upon request from the Commonwealth of Puerto Rico, the Secretary shall provide appropriate training and technical assistance to enable the Commonwealth of Puerto Rico to formulate a plan of operation described in subsection (a).\n##### (c) Determination by the Secretary of Agriculture\nNot later than 180 days after receiving a plan of operation described in subsection (a), the Secretary shall approve if such plan satisfies the requirements for a supplemental nutrition assistance program State plan in accordance with subsections (d) and (e) of section 11 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2020 ). If the Secretary does not approve such plan, the Secretary shall provide, not later than 30 days after disapproval, a statement that specifies each of the requirements that were not satisfied by such plan.\n##### (d) Certification by the Secretary of Agriculture\nIf the Secretary approves the plan submitted by the Commonwealth of Puerto Rico under subsection (a), the Secretary shall submit to the Congress, not later than 90 days thereafter, a certification that the Commonwealth of Puerto Rico qualifies to participate in the supplemental nutrition assistance program as a State as defined in section 3(r) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(r) ).\n#### 4. Transition from the consolidated block grant for Puerto Rico\n##### (a) Covered period\nThe Secretary may continue to implement the then most recent approved consolidated block grant specified in section 19(b)(1)(A) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2028(b)(1)(A) ) for an implementation period ending 5 years after the effective date of the amendments made by this Act, or on the date the Secretary determines that the Commonwealth of Puerto Rico no longer needs to operate the consolidated block grant to complete the transition described in section 3(a), whichever occurs first.\n##### (b) Report\nFor each year a plan is continued under subsection (a), the Secretary shall submit to the Congress an annual report on the operation of such plan. The Secretary shall include in such report information related to increases in funding that are required to accommodate the transition of the Commonwealth of Puerto Rico from the receipt of block grant payments to the implementation of supplemental nutrition assistance program.\n#### 5. Consolidated block grant for Puerto Rico and American Samoa\nSection 19 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2028 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)(A) by inserting until the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , after (A) ,\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i) by striking and at the end, and\n**(II)**\nin clause (ii)\u2014\n**(aa)**\nby inserting , and ending at the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act after thereafter ,\n**(bb)**\nby striking the period at the end and inserting ; and , and\n**(cc)**\nby adding at the end the following:\n(iii) subject to the availability of appropriations under section 18(a), for each fiscal year beginning after the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , 0.4 percent of the aggregate amount specified in clause (i) and adjusted under clause (ii), as further adjusted by the percentage by which the thrifty food plan has been adjusted under section 3(u)(4) between June 30 of the penultimate fiscal year preceding such effective date and June 30 of the fiscal year for which the adjustment is made under this clause. ,\n**(ii)**\nin subparagraph (B)(i) by inserting ending at the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act after thereafter , and\n**(iii)**\nin subparagraph (C)\u2014\n**(I)**\nby striking For and inserting the following:\n(i) For ,\n**(II)**\nby inserting ending at the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act after thereafter , and\n**(III)**\nby adding at the end, the following:\n(ii) For each fiscal year beginning after the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , the Secretary shall use 100 percent of the funds made available under subparagraph (A) for payment to American Samoa to pay 100 percent of the expenditures by American Samoa for a nutrition assistance program extended under section 601(c) of Public Law 96\u2013597 ( 48 U.S.C. 1469d(c) ). , and\n**(C)**\nin paragraph (3) by striking year, and inserting year ending at the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act , and after year , and\n**(2)**\nin subsection (b)(1)(A) by inserting and ending at the end of the period described in section 4(a) of the Puerto Rico Nutrition Assistance Fairness Act after year the first place it appears.\n#### 6. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act such sums as may be necessary until the end of the period described in section 4(a).\n#### 7. Effective dates\n##### (a) In general\nExcept as provided in subsection (b), this Act shall take effect on the date of the enactment of this Act.\n##### (b) Effective date of amendments\nThe amendments made by this Act shall take effect on the date that is 10 years after the date of the enactment of this Act.",
      "versionDate": "2025-09-08",
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
        "actionDate": "2026-03-02",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3958",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Puerto Rico Nutrition Assistance Fairness Act",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-11T15:41:10Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5168ih.xml"
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
      "title": "Puerto Rico Nutrition Assistance Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Puerto Rico Nutrition Assistance Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to transition the Commonwealth of Puerto Rico to the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:32Z"
    }
  ]
}
```
